# Unit tests

Run with `python -m pytest` (after `pip install -e .[dev]`). The
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
defect changes the test. `tests/legacy/RETIREMENT.md` maps every check of
the legacy suites to the tests that now cover it.
