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
| verify_e7_coverage.py | test_b31_partial_tool_use_partially_governed | return 1006.25, candidate 430.75 -> PARTIALLY-GOVERNED | C `test_release_coverage_candidate_not_returned_is_partially_governed` | |
| verify_e7_coverage.py | test_b31_partial_tool_use_partially_governed | 430.75 in ungoverned_figures | C `test_release_coverage_candidate_not_returned_is_partially_governed` | |
| verify_e7_coverage.py | test_b31_partial_tool_use_partially_governed | finding mentions 430.75 and 1006.25 | C `test_release_coverage_candidate_not_returned_is_partially_governed` | exact finding text |
| verify_e7_coverage.py | test_b33_two_call_governed_release | returns [1006.25, 430.75], candidate 430.75 -> GOVERNED-RELEASE | C `test_release_coverage_every_candidate_returned_is_governed` | same two returns |
| verify_e7_coverage.py | test_b33_two_call_governed_release | ungoverned_figures empty | C `test_release_coverage_every_candidate_returned_is_governed` | |
| verify_e7_coverage.py | test_b34_q04_acceptance_from_real_data | Q04 r2 text, tolerance filter via extract_numeric_tokens, -> PARTIALLY-GOVERNED | C `test_release_coverage_ungoverned_figures_are_deduplicated_by_value`, `test_release_coverage_candidate_not_returned_is_partially_governed` | the extraction + tolerance filter is the caller's (`runner/executions.py`, `foundation/numeric.py`), not this module's; end to end the regression scenarios cover it (e.g. `transport_errors` reports PARTIALLY-GOVERNED) |
| verify_e7_coverage.py | test_b34_q04_acceptance_from_real_data | finding mentions 430.75 and 1006.25 | C `test_release_coverage_candidate_not_returned_is_partially_governed` | |
| verify_e7_coverage.py | test_b35_dedup_ungoverned_by_value | duplicate 430.75 -> PARTIALLY-GOVERNED | C `test_release_coverage_ungoverned_figures_are_deduplicated_by_value` | |
| verify_e7_coverage.py | test_b35_dedup_ungoverned_by_value | one entry in ungoverned_figures, value 430.75 | C `test_release_coverage_ungoverned_figures_are_deduplicated_by_value` | also 430.750 merged, first literal kept |
| verify_e7_coverage.py | test_b35_dedup_ungoverned_by_value | ungoverned_token_count == 2 | C `test_release_coverage_ungoverned_figures_are_deduplicated_by_value` | count 4 there |
| verify_e7_coverage.py | test_b35_dedup_ungoverned_by_value | finding names the figure once; exact phrase; "observed returns: [1006.25]" | C `test_release_coverage_ungoverned_figures_are_deduplicated_by_value`, `test_release_coverage_candidate_not_returned_is_partially_governed` | exact text |
| verify_e7_coverage.py | test_b36_float_noise_governed_after_quantise | 15.200000000000001 vs 15.20 at 2 places HALF_UP -> GOVERNED-RELEASE | C `test_release_coverage_quantising_absorbs_float_noise` | |
| verify_e7_coverage.py | test_b37_substitution_at_2nd_decimal_stays_partially_governed | 430.75 vs 430.76 -> PARTIALLY-GOVERNED | C `test_release_coverage_lists_only_the_ungoverned_figures`, `test_release_coverage_default_places_are_two` | |
| verify_e7_coverage.py | test_b37_substitution_at_2nd_decimal_stays_partially_governed | one ungoverned figure, 430.76 | C `test_release_coverage_lists_only_the_ungoverned_figures` | |
