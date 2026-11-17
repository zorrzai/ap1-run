# Unit tests

Run with `python -m pytest` (after `pip install -e '.[dev]'`). The
configuration is in `pyproject.toml`.

## Layout

`tests/unit/` mirrors `src/ap1_run/`: the tests for
`src/ap1_run/<layer>/<module>.py` are in `tests/unit/<layer>/test_<module>.py`.
Closely related modules may share one test module. Tests run against the
package, imported from `src/`, never against copies.

## Conventions

- Name a test by behaviour: `test_<unit>_<condition>_<expected>`.
- Mark a test with the requirements it checks:
  `@pytest.mark.req('R2.4')`. Unknown markers are an error.
- A test checks one behaviour, with inputs built in the test or in a
  small fixture beside it, and needs no network or model.

## The gate before a module's internals change

1. Its unit tests are green.
2. Its mutation score has been measured with mutmut and recorded in
   `tests/mutation/scores.json`, and does not drop (see
   `tests/mutation/README.md`).
3. The regression baseline (`tests/regression/`) is unchanged.

Every module in `src/ap1_run/` has unit tests and a recorded mutation
score. Tests that pin today's behaviour where it is known to be
wrong carry `@pytest.mark.finding(...)` with the finding's ID; fixing the
defect changes the test. `tests/RETIREMENT.md` maps every check of the
retired legacy suites (`tests/legacy/`) to the tests that now cover it.

## When a test may change

A marked test changes only together with the fix of its finding. An
unmarked test that pins the exact text of a report or console section may
be rewritten when that code is refactored, but the change is still
reviewed like any other: it has to keep checking the same behaviour. A fix
that breaks an unmarked test has found a pin that should have been marked;
mark it (or register the defect) rather than just updating it.
