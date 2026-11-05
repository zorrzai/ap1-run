"""SPEC §12.10's file classification matches the repository, both ways.

Count-free: the table's "Lines" column is not checked (line counts are not
behaviour). What is checked is the list itself:

- every file the table names exists (a row with a wildcard, such as
  ``tests/legacy/verify_*.py``, matches at least one file), so a file that
  is moved, renamed or deleted takes its row with it;
- every module under ``src/`` has a row, so a new module is classified
  when it is added. Package markers (``__init__.py``) carry no behaviour of
  their own and need no row.

The legacy verify_spec.py checked the table with its line counts; this is
the part of that tie that stays when the legacy suites are retired.
"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / 'docs' / 'SPEC.md'
ROW = re.compile(r'^\| `([^`]+)` \| [^|]* \| ([^|]+) \|$')


def listed_files():
    """The paths in the first column of SPEC §12.10's table, in order."""
    lines = SPEC.read_text(encoding='utf-8').splitlines()
    start = next((i for i, line in enumerate(lines)
                  if line.startswith('**12.10 File classification.**')), None)
    if start is None:
        return []  # test_spec_file_list_table_found says so
    rows, in_table = [], False
    for line in lines[start + 1:]:
        if line.startswith('|'):
            in_table = True
            match = ROW.match(line)
            if match:
                rows.append(match.group(1))
        elif in_table:
            break
    return rows


LISTED = listed_files()

SRC_MODULES = sorted(
    path.relative_to(ROOT).as_posix()
    for path in (ROOT / 'src').rglob('*.py')
    if '__pycache__' not in path.parts and path.name != '__init__.py')

# Modules SPEC §12.10 does not list yet. Each is a SPEC gap with a register
# ID; the fix adds the row (and the xfail goes).
UNLISTED = {
    # T3-73: runner-source sealing (runner version and runner_source_hash)
    # has no SPEC contract, and its module has no §12.10 row.
    'src/ap1_run/execution/version.py': 'T3-73',
}


@pytest.mark.req('SPEC §12.10')
def test_spec_file_list_table_found():
    # Guards the parser: a table that cannot be read would make the two
    # tests below pass or fail for the wrong reason.
    assert len(LISTED) >= 30, LISTED
    assert 'src/ap1_run/run.py' in LISTED


@pytest.mark.req('SPEC §12.10')
@pytest.mark.parametrize('listed', LISTED)
def test_spec_file_list_every_listed_file_exists(listed):
    assert sorted(ROOT.glob(listed)), \
        f'SPEC §12.10 lists {listed}; no such file'


def _module_cases():
    for module in SRC_MODULES:
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
def test_spec_file_list_every_src_module_is_listed(module):
    assert module in LISTED, f'{module} has no row in SPEC §12.10'


def test_spec_file_list_unlisted_entries_are_src_modules():
    # The exceptions above name real modules, so a fixed or removed one
    # cannot leave a stale entry behind.
    assert set(UNLISTED) <= set(SRC_MODULES), set(UNLISTED) - set(SRC_MODULES)
