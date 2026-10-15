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

Modules get full unit tests as they are changed. The legacy suites in
`tests/legacy/` still cover the rest, and are retired module by module
as unit tests replace them.
