# Mutation scores

How strong the unit tests are, module by module. mutmut makes small
changes (mutants) to a module's code, and runs the module's unit tests
against each one. A mutant the tests notice is killed; one they don't
notice survives. The score is the share killed.

## The ratchet

`scores.json` records the score of every module that has been through the
step-2 gate (`tests/unit/README.md`). A score may rise, never fall:

```
python tests/mutation/run_mutation.py                  # check every recorded module
python tests/mutation/run_mutation.py scoring/accuracy # check one
python tests/mutation/run_mutation.py --record scoring/accuracy
python tests/mutation/run_mutation.py --survivors scoring/accuracy
```

A module is named by its path under `src/ap1_run/`, without `.py`. Its
tests are the mirrored `tests/unit/<layer>/test_<name>.py`, unless its
entry lists others under `"tests"`. The run happens in a scratch copy, so
the repository is never modified. It needs the `[dev]` extra.

**Target:** at least 80 % for a module that is being changed. Every
surviving mutant of such a module is reviewed: either a test is added, or
the entry's `"notes"` says why the mutant is acceptable (for example, it
changes only a message, or it is equivalent to the original).

A commit that changes a module's code changes its set of mutants, so the
score can move without the tests getting weaker (an extracted function
brings its own equivalent mutants, say). Such a commit re-records the
score with `--record`, and the entry's notes account for every survivor.

A mutant that no test runs counts as a survivor. A score is only
comparable with itself: it measures the unit tests of one module, not
the legacy suites or the regression baseline.

## Running mutmut directly

`run_mutation.py` writes the configuration mutmut needs. To run mutmut by
hand, note that mutmut 3 copies only the mutated files into `mutants/`, so
the configuration needs `also_copy = ["src/"]`, and it must run with
`PYTHONPATH=src`. Otherwise the editable install of the repository is
imported instead of the mutants, and every mutant survives.
