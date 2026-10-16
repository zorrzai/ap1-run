# Legacy checks mapped to step-3 unit tests: G5 (scoring-b)

Modules: `scoring/transcription.py`, `scoring/release_coverage.py`,
`scoring/reproducibility.py`. Suites mapped here: `verify_phase_c.py` and
`verify_e7_coverage.py` (the module-level suites that import these modules).
`verify.py` does not import them (its "reproducibility" is the CI hash check).
`verify_conformance`, `verify_integration`, `verify_inspect` and `verify_r41`
also reach these modules and are mapped by G7.

Unit test files: `tests/unit/scoring/test_transcription.py` (T),
`tests/unit/scoring/test_release_coverage.py` (C),
`tests/unit/scoring/test_reproducibility.py` (R).

| suite | function | check (short description or line) | new test(s) | note |
|---|---|---|---|---|
| verify_phase_c.py | test_transcription_exact | 182.40 vs 182.40, AUTO-MATCH -> EXACT | T `test_transcription_equal_values_are_exact` | |
| verify_phase_c.py | test_transcription_altered | outcome ALTERED for 182.50 vs 182.40 | T `test_transcription_different_values_are_altered` | |
| verify_phase_c.py | test_transcription_altered | difference == 0.10 | T `test_transcription_different_values_are_altered` | |
| verify_phase_c.py | test_transcription_quantised_exact | 182.404 vs 182.40 at 2 digits -> EXACT | T `test_transcription_difference_within_quantisation_is_exact` | |
| verify_phase_c.py | test_transcription_unobservable_when_adjudicated | ADJUDICATE-DECLINE -> UNOBSERVABLE | T `test_transcription_adjudicated_figure_is_unobservable` | |
| verify_e7_coverage.py | test_b32_auto_matchable_also_transcribed_altered | tool 1006.25, released 430.75, AUTO-MATCH, 2 digits -> ALTERED | T `test_transcription_difference_beyond_quantisation_is_altered`, `test_transcription_compares_a_single_tool_return` | same branch; the second pins T3-26 on the same Q04 figure (430.75) |
