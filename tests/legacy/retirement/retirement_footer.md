## verify_hashes.py (CI only; 3 checks, not counted by run_all_tests.py)

`.github/workflows/hashes.yml` runs it on three operating systems. On each it asserts that the digest
of a known input equals the pinned `EXPECTED_DIGEST`, so every platform is checked against the same
value; it also writes the digest to `hash_digest.txt` (in the repository root, untracked), which
nothing reads back.

| function | line | check | new test(s) | note |
|---|---|---|---|---|
| main | 49 | digest of the known input equals the pinned `EXPECTED_DIGEST` | `unit/foundation/test_numeric.py::test_canonical_hash_known_digest_of_verify_hashes_input` | the unit test pins the canonical text as well as the same digest `831709b2…`, so a cross-platform difference fails on any OS the unit tests run on (G1) |
| main | 61 | same input gives the same digest | `unit/foundation/test_numeric.py::test_canonical_hash_known_digest_of_verify_hashes_input` | (G1) |
| main | 76 | key order does not change the digest | `unit/foundation/test_numeric.py::test_canonical_hash_key_order_irrelevant` | (G1) |

## Not counted, not mapped

- `verify.py`: `check('<file> exists', False)` (l.328) and `check('ground_truth_example.py exists',
  False)` (l.456) run only when an example file is missing; they are a precondition, not a check of
  the runner, and never run on a complete checkout (G3). The regression scenario `clean` fails if
  the example files are missing.
- `verify_phase_c.py`: the helper `_mock_extract` is defined and never called (G1).
- `verify_phase_e.py`: its docstring promises "kappa with small-n caveat"; no check exists and no
  code computes kappa (T3-23); pinned instead by
  `unit/reporting/test_adjudication.py::test_sheet_rubric_marks_and_blank_reasoning` (G6).
- `verify_inspect.py` has four test methods; `run_all_tests.py` lists it as 3 functions and 4
  checks (G7).

## Coverage (criterion 2)

Measured by G9 with coverage.py 7.16 (`--branch`), each legacy suite run on its own as
`run_all_tests.py` runs it (from the repository root, in `ap1-run-inspect`), against one run of the
whole new pytest suite (`tests/unit`, `conformance`, `functional`, `inspect`; 1597 tests in
`ap1-run-inspect`, so the Inspect tests run too). Two scopes: `src/ap1_run/` alone, and the whole
repository except `tests/` (which adds `ap1_inspect/`, `tools/`, `example/`, `smoke_test.py`).
Numbers are executed line numbers and arcs as coverage.py records them.

| suite | `src/ap1_run` lines / arcs | whole repo lines / arcs | lines or arcs the new tests miss |
|---|---|---|---|
| verify.py | 316 / 442 | 592 / 730 | none |
| verify_phase_b.py | 330 / 440 | 330 / 440 | none |
| verify_phase_c.py | 438 / 560 | 438 / 560 | none |
| verify_phase_d.py | 439 / 579 | 715 / 867 | none |
| verify_phase_e.py | 530 / 657 | 530 / 657 | none |
| verify_d72b.py | 309 / 407 | 469 / 574 | none |
| verify_e7_coverage.py | 526 / 685 | 802 / 973 | none |
| verify_integration.py | 1009 / 1297 | 1104 / 1402 | none |
| verify_r41.py | 685 / 867 | 685 / 867 | none |
| verify_conformance.py | 725 / 924 | 725 / 924 | none |
| verify_spec.py | 0 / 0 | 0 / 0 | none (reads docs only) |
| verify_findings.py | 32 / 36 | 367 / 529 | none |
| test_findings_mutation.py | 32 / 36 | 367 / 529 | none |
| verify_inspect.py | 818 / 1030 | 1168 / 1406 | none |
| verify_hashes.py | 51 / 73 | 51 / 73 | none |
| **new pytest suite** | **3650 / 5022** | **4628 / 6281** | |

So no line or branch needs a regression scenario as its only cover. (G7 reported
`scoring/provenance/audit.py` lines 1 and 10 as reached only by `verify_r41`'s unused import; the
step-2 unit tests `unit/scoring/provenance/test_audit.py` import the module, so they are covered.)
`src/ap1_run` as a whole: the new suite misses 4 of 2620 statements and leaves 8 of 1080 branches
partial (99 %), in `run.py`, `runner/summary.py`, `scoring/figure_id.py` and
`scoring/operation_correctness.py`; no legacy suite reaches them either (G4 and step 2 explain them
as unreachable).

## Mutation (criterion 3)

Score = killed / mutants (mutmut 3, `tests/mutation/run_mutation.py`). "New" is the recorded score
in `tests/mutation/scores.json`; "legacy" is the score of the legacy suites that import the module,
run with `--tests` (or, where marked, G1's wrapper that fails on a non-zero `main()`, because the
`check()` suites never raise under pytest). Each group measured its own modules during step 3
(column "measured by"); G9 measured the provenance modules and `runner/summary`.

| module | new | legacy | legacy suites | measured by |
|---|---|---|---|---|
| foundation/numeric | 0.9257 | 0.7430 | verify\*, verify_conformance\*, verify_hashes\*, verify_r41, verify_e7_coverage, verify_phase_c, verify_inspect | G1 |
| foundation/config | 0.9641 | 0.5202 | verify\*, verify_conformance\*, verify_r41, verify_e7_coverage, verify_phase_e, verify_inspect, verify_integration | G1 |
| foundation/transcript | 0.8933 | 0.4933 | verify_conformance\*, verify_phase_b, verify_integration | G1 |
| foundation/adapter | 0.9639 | 0.1265 | verify_conformance\*, verify_integration, verify_phase_b | G1 |
| execution/context | 1.000 | 0.645 | phase_b, phase_d, d72b, e7_coverage, integration, r41, inspect (0.434 without the last three) | G2 |
| execution/evidence | 0.964 | 0.545 | phase_b, phase_c, e7_coverage, integration, r41, inspect (0.433 without the last three) | G2 |
| execution/engine | 0.955 | 0.372 | phase_b, integration (0.072 phase_b alone) | G2 |
| execution/seal | 0.9307 | 0.4654 | verify, phase_d, phase_e, r41, inspect | G3 |
| execution/seal_constants | 0.9804 | 0.7549 | d72b, e7_coverage | G3 |
| execution/perturbation_guard | 0.8359 | 0.4359 | phase_b, e7_coverage | G3 |
| execution/version | 0.9281 | none | no legacy suite imports it | G3 |
| scoring/invocation | 0.994 | 0.605 | phase_c (+ the suites importing it) | G4 |
| scoring/accuracy | 1.000 | 0.510 | as above | G4 |
| scoring/figure_id | 0.911 | 0.354 | as above | G4 |
| scoring/operation_correctness | 0.942 | 0.544 | d72b, e7_coverage (+ the suites importing it) | G4 |
| scoring/transcription | 1.00 | 0.33 | phase_c, e7_coverage | G5 |
| scoring/release_coverage | 0.97 | 0.56 | e7_coverage | G5 |
| scoring/reproducibility | 0.96 | 0.24 | phase_c | G5 |
| scoring/provenance/trace | 1.0 | 0.4604 | phase_d 0.4005, r41 0.3261; phase_d + r41 + e7_coverage + integration + inspect 0.4604 | G9 |
| scoring/provenance/classify | 0.8933 | 0.7154 | phase_d 0.7036, r41 0.6126; all five 0.7154 | G9 |
| scoring/provenance/audit | 1.0 | 0.5686 | phase_d 0.5686; r41 0.0 (never calls it); all five 0.5686 | G9 |
| reporting/adjudication | 0.9481 | 0.3513 | phase_e | G6 |
| reporting/report | 0.9675 | 0.1581 | phase_e | G6 |
| runner/summary | 0.9783 | 0.0614 | integration (the only legacy suite that reaches `runner/`) | G9 |
| runner/console, credentials, executions, outputs, settings; run | 0.92–1.0 | none | no legacy suite executes them | step 2 |

\* through G1's `main()` wrapper. On every module the new score is higher. Two caveats keep the
legacy numbers from being exact, both test-infrastructure issues, not runner defects:

- Under pytest, a legacy test that fails by returning `False` passes (pytest only warns). One check
  fails that way: `verify_e7_coverage.py::test_guard_perturbation_refusal`, l.379 (`return False`
  when no refusal is raised). Its native run would kill a few more `perturbation_guard` mutants;
  the gap to 0.8359 is too wide for that to matter.
- `run_mutation.py --tests` reports "not checked: the tests did not run cleanly" also when the tests
  run cleanly but execute none of the mutated code (mutmut stops early: "could not find any test
  case for any mutant"). That is the `audit` / `verify_r41` case above; read it as 0.

## Blockers to deleting the suites

- **All suites:** the maintainer's approval, the gate before the fixes.
- **`verify_spec.py`:** the maintainer's decision on its 62 checks, which this map proposes to
  drop: line counts are not behaviour, and the ≤300-line limit would go with them. If they are
  dropped, what they check, SPEC §12.9 (the limit) and the §12.10 line-count table, should go in
  the same change (with README's sentence on the limit), or they go stale unchecked. Nothing else
  blocks it.
- **`verify_hashes.py`:** `.github/workflows/hashes.yml` runs it; switch the workflow to
  `pytest tests/unit/foundation/test_numeric.py -k verify_hashes_input` (or to the whole unit
  suite) in the same change that deletes it.
- **`run_all_tests.py` and the docs:** the registry, `.github/workflows/full_suite.yml` (runs
  `run_all_tests.py`), and the docs that cite "14 offline suites" (README, SPEC, the paper's next
  revision) change with the deletion. The regression baseline also runs in CI (`regression.yml`,
  Ubuntu, Python 3.11 and 3.12); it is not registered in `run_all_tests.py`, so it is unaffected.
- **`verify_inspect.py`:** not a blocker, but note that its replacement tests in `tests/inspect/`
  need inspect-ai and skip without it, as the legacy agreement test did. The full-suite workflow
  installs `.[dev]`, without the `inspect` extra, so in CI both skip; run them in an environment
  with inspect-ai (`ap1-run-inspect`).
- None of the suites is blocked by a missing test, a coverage gap or a lower mutation score.
