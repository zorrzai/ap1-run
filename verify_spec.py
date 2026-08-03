"""Verify SPEC.md line counts and constraints are self-consistent.

Parses the §12.10 classification table and §12.9 declared exceptions
from SPEC.md, then checks every claim against the actual files.

No hardcoded file lists — all data comes from the specification itself.
"""

import re
import sys
from pathlib import Path

_base = Path(__file__).parent
_passed = 0
_failed = 0


def check(name, condition, detail=''):
    global _passed, _failed
    if condition:
        _passed += 1
        print(f'  PASS  {name}')
    else:
        _failed += 1
        print(f'  FAIL  {name}: {detail}')


# -- Parsing helpers ---------------------------------------------------

def _parse_classification_table(spec_text):
    """Parse §12.10 classification table from SPEC.md.

    Returns list of dicts: {file, lines, classification}.
    Rows with 'varies' in the Lines column are skipped (e.g. verify_*.py).
    """
    rows = []
    # Match table rows: | `filename` | NNN | classification |
    # or | `path/filename` | NNN | ... |
    pat = re.compile(
        r'^\|\s*`([^`]+)`\s*\|\s*(\d+|varies)\s*\|\s*(.+?)\s*\|',
        re.MULTILINE,
    )
    for m in pat.finditer(spec_text):
        filename = m.group(1)
        lines_str = m.group(2)
        classification = m.group(3).strip()
        if lines_str == 'varies':
            continue
        rows.append({
            'file': filename,
            'lines': int(lines_str),
            'classification': classification,
        })
    return rows


def _parse_declared_exceptions(spec_text):
    """Parse declared exceptions from §12.9.

    Looks for: **Declared exception — `filename` (NNN lines).**
    Returns dict: {filename: recorded_lines}.
    """
    exceptions = {}
    pat = re.compile(
        r'\*\*Declared exception[^`]*`([^`]+)`\s*\((\d+)\s*lines?\)',
    )
    for m in pat.finditer(spec_text):
        exceptions[m.group(1)] = int(m.group(2))
    return exceptions


def _count_lines(filepath):
    """Count total lines in a file, including blank lines.

    Equivalent to PowerShell (Get-Content file).Count.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


# -- Tests -------------------------------------------------------------

def test_spec_line_counts_match_files():
    """Every line count in §12.10 matches the actual file."""
    spec_path = _base / 'SPEC.md'
    spec_text = spec_path.read_text(encoding='utf-8')
    rows = _parse_classification_table(spec_text)

    check('spec-table-not-empty', len(rows) > 0,
          'No rows parsed from §12.10 table')
    if not rows:
        return

    stale = []
    for row in rows:
        filepath = _base / row['file']
        if not filepath.exists():
            check(f'spec-file-exists-{row["file"]}', False,
                  f'{row["file"]} listed in §12.10 but file not found')
            continue
        actual = _count_lines(filepath)
        if actual != row['lines']:
            stale.append((row['file'], row['lines'], actual))
            check(f'spec-count-{row["file"]}', False,
                  f'recorded {row["lines"]}, actual {actual}')
        else:
            check(f'spec-count-{row["file"]}', True)

    check('spec-no-stale-counts', len(stale) == 0,
          f'{len(stale)} stale: {stale}')


def test_spec_constraint_holds():
    """Every instrument module <=300 unless declared exception.
    Declared exceptions must still exceed 300 (stale exception = failure).
    """
    spec_path = _base / 'SPEC.md'
    spec_text = spec_path.read_text(encoding='utf-8')
    rows = _parse_classification_table(spec_text)
    exceptions = _parse_declared_exceptions(spec_text)

    instrument_modules = [
        r for r in rows
        if 'instrument module' in r['classification'].lower()
    ]

    check('instrument-modules-found', len(instrument_modules) > 0,
          'No instrument modules found in §12.10')
    if not instrument_modules:
        return

    breaching = []
    stale_exceptions = []

    for mod in instrument_modules:
        filepath = _base / mod['file']
        if not filepath.exists():
            continue  # already reported in test_spec_line_counts_match_files
        actual = _count_lines(filepath)
        is_excepted = mod['file'] in exceptions

        if is_excepted:
            # Exception must still breach — a stale exception is wrong
            if actual <= 300:
                stale_exceptions.append((mod['file'], actual))
                check(f'exception-still-breaches-{mod["file"]}', False,
                      f'declared exception at {actual} lines no longer '
                      f'exceeds 300 — remove the exception')
            else:
                check(f'exception-still-breaches-{mod["file"]}', True)
        else:
            # Must be at or under 300
            if actual > 300:
                breaching.append((mod['file'], actual))
                check(f'constraint-{mod["file"]}', False,
                      f'{actual} lines exceeds 300 with no declared exception')
            else:
                check(f'constraint-{mod["file"]}', True)

    check('no-undeclared-breaches', len(breaching) == 0,
          f'{len(breaching)} breaching: {breaching}')
    check('no-stale-exceptions', len(stale_exceptions) == 0,
          f'{len(stale_exceptions)} stale exceptions: {stale_exceptions}')


# -- Main --------------------------------------------------------------

ALL_TESTS = [
    test_spec_line_counts_match_files,
    test_spec_constraint_holds,
]


def main():
    for test_fn in ALL_TESTS:
        print(f'\n--- {test_fn.__name__} ---')
        test_fn()

    print(f'\n{"=" * 50}')
    print(f'Spec Enforcement Results: {_passed} passed, {_failed} failed')
    print(f'{"=" * 50}')
    return 0 if _failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
