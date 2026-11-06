"""SPEC §12.10's file list matches the repository, both ways.

File-list conformance only: the table's "Classification" column is not
checked, and the table has no line counts (SPEC §12.9: line counts are not
behaviour). What is checked is the list itself:

- every row of the table can be read (a row that can't is an error, not
  silently skipped);
- every file the table names exists as a file (a row with a wildcard
  must match at least one), so a file that is moved, renamed or deleted
  takes its row with it;
- every Python file shipped outside ``tests/`` has a row: the modules
  under ``src/``, the scripts in ``tools/``, the example's modules and the
  root scripts, so a new one is classified when it is added. Package
  markers (``__init__.py``) carry no behaviour of their own, and
  ``ap1_inspect/`` is unsupported for now (README), so neither needs one.

The legacy verify_spec.py checked the table with its line counts; this is
the part of that tie that stayed when the legacy suites were retired.
"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / 'docs' / 'SPEC.md'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+) \|$')
HEADER = re.compile(r'^\| File \| Classification \|$')
RULE = re.compile(r'^\|(-+\|)+$')


# The end of §12.10: the next numbered paragraph, heading or rule.
BOUNDARY = re.compile(r'^(\*\*\d+\.\d+|#|---)')


def table_rows():
    """(parsed paths, lines that look like table rows but could not be
    read). Every line from the §12.10 heading to the next section boundary
    whose text, indentation stripped, starts with '|' is a table line; it
    must be the header, the rule or a readable row, wherever it is (also
    after a blank line)."""
    lines = SPEC.read_text(encoding='utf-8').splitlines()
    start = next((i for i, line in enumerate(lines)
                  if line.startswith('**12.10 File classification.**')), None)
    if start is None:
        return [], []  # test_spec_file_list_table_found says so
    rows, unread = [], []
    for line in lines[start + 1:]:
        if BOUNDARY.match(line):
            break
        text = line.strip()
        if not text.startswith('|'):
            continue
        match = ROW.match(text)
        if match:
            rows.append(match.group(1))
        elif not (HEADER.match(text) or RULE.match(text)):
            unread.append(line)
    return rows, unread


LISTED, UNREAD = table_rows()


def _pattern(listed):
    """A listed path as a regex with Path.glob's rules: '*' and '?' never
    match '/'. The same rule decides both directions."""
    return re.compile(re.escape(listed).replace(r'\*', '[^/]*')
                      .replace(r'\?', '[^/]') + r'\Z')


def _tracked_python_files():
    """The repository's tracked .py files (git ls-files), or, outside a
    checkout, every .py file under the root."""
    import subprocess
    try:
        out = subprocess.run(['git', 'ls-files', '-z', '*.py'], cwd=ROOT,
                             capture_output=True, check=True).stdout
        files = [f for f in out.decode('utf-8').split('\0') if f]
        if files:
            return files
    except (OSError, subprocess.CalledProcessError):
        pass
    return [p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.py')]


def _shipped():
    """Every tracked .py file outside tests/ that needs a row."""
    found = []
    for rel in _tracked_python_files():
        parts = rel.split('/')
        top = parts[0]
        if (parts[-1] == '__init__.py' or '__pycache__' in parts
                or top in ('tests', 'ap1_inspect', 'build', 'output',
                           'reference', 'docs', 'findings')
                or top.startswith('.')):
            continue
        if len(parts) == 1 or top in ('src', 'tools', 'example'):
            found.append(rel)
    return sorted(found)


SHIPPED = _shipped()

# Modules SPEC §12.10 does not list yet. Each is a SPEC gap with a register
# ID; the fix adds the row (and the xfail goes).
UNLISTED = {
    # T3-73: runner-source sealing (runner version and runner_source_hash)
    # has no SPEC contract, and its module has no §12.10 row.
    'src/ap1_run/execution/version.py': 'T3-73',
    # T3-74 (plain corrections to SPEC's inventory): the published-run
    # verifier and the root smoke_test.py shim (named in §12.9's prose)
    # have no row.
    'tools/verify_run_seal.py': 'T3-74',
    'smoke_test.py': 'T3-74',
}


@pytest.mark.req('SPEC §12.10')
def test_spec_file_list_table_found():
    # Guards the parser: a table that cannot be read would make the two
    # tests below pass or fail for the wrong reason.
    assert len(LISTED) >= 30, LISTED
    assert 'src/ap1_run/run.py' in LISTED
    assert UNREAD == [], UNREAD


@pytest.mark.req('SPEC §12.10')
@pytest.mark.parametrize('listed', LISTED)
def test_spec_file_list_every_listed_file_exists(listed):
    matches = sorted(ROOT.glob(listed))
    assert matches and all(path.is_file() for path in matches), \
        f'SPEC §12.10 lists {listed}; no such file'


def _module_cases():
    for module in SHIPPED:
        finding = UNLISTED.get(module)
        if finding is None:
            yield module
        else:
            yield pytest.param(module, marks=[
                pytest.mark.finding(finding),
                pytest.mark.xfail(strict=True, raises=AssertionError,
                                  reason=f'{finding}: {module} has no '
                                         f'SPEC §12.10 row')])


@pytest.mark.req('SPEC §12.10')
@pytest.mark.parametrize('module', list(_module_cases()))
def test_spec_file_list_every_shipped_python_file_is_listed(module):
    assert any(_pattern(listed).match(module) for listed in LISTED), \
        f'{module} has no row in SPEC §12.10'


def test_spec_file_list_unlisted_entries_are_src_modules():
    # The exceptions above name real modules, so a fixed or removed one
    # cannot leave a stale entry behind.
    assert set(UNLISTED) <= set(SHIPPED), set(UNLISTED) - set(SHIPPED)
