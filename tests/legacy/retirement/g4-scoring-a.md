# Legacy checks mapped to unit tests: group G4 (scoring-a)

Modules: `scoring/invocation.py`, `scoring/accuracy.py`, `scoring/figure_id.py`,
`scoring/operation_correctness.py`. Suites mapped here (step-3 protocol, rule 5): the
module-level suites `verify_phase_c.py`, `verify_d72b.py` and `verify_e7_coverage.py`, for the
checks about these modules. No other module-level suite (`verify.py`, `verify_phase_b.py`,
`verify_phase_d.py`, `verify_phase_e.py`, `verify_hashes.py`) calls them. Checks in those suites
about other modules (reproducibility, transcription, seal, release coverage, ...) are left to
their groups. Unit test files: `tests/unit/scoring/test_<module>.py`.

| suite | function | check (short description or line) | new test(s) | note |
|---|---|---|---|---|
| verify_phase_c.py | test_exact_bound_in_range | bound in (0, 1] for n = 1..200 | test_invocation.py::test_exact_upper_bound_is_in_open_unit_interval | same range, plus n = 10 000; asserts the stricter < 1 |
| verify_phase_c.py | test_exact_bound_n1 | format_rate(0, 1) contains 95.0% | test_invocation.py::test_format_rate_zero_failures_n1_states_95_percent_bound, test_exact_upper_bound_n1_is_one_minus_alpha | whole string pinned |
| verify_phase_c.py | test_exact_bound_n49 | format_rate(0, 49) contains 5.9% | test_invocation.py::test_format_rate_bound_rounds_half_even_down_at_n49 | pinned as T3-61 (an upper bound rounded down) |
| verify_phase_c.py | test_exact_bound_n100 | format_rate(0, 100) contains 3.0% | test_invocation.py::test_format_rate_zero_failures_n100_states_3_percent_bound | |
| verify_phase_c.py | test_100pct_never_printed_alone | no '100%' for n = 1..200 | test_invocation.py::test_format_rate_zero_failures_never_prints_100_percent | |
| verify_phase_c.py | test_exact_and_rule_of_three_agree_above_30 | exact bound within 1 pp of 3/n, n = 30..200 | test_invocation.py::test_exact_upper_bound_within_1pp_of_rule_of_three_from_n30 | |
| verify_phase_c.py | test_nonzero_failures_prints_percentage | format_rate(3, 50) has 3/50 and 6.0% | test_invocation.py::test_format_rate_nonzero_failures_prints_count_and_percent | |
| verify_phase_c.py | test_dpr_zero_base_undefined | zero base: None, UNDEFINED, no '1.0' | test_invocation.py::test_compute_dpr_zero_base_rate_is_undefined_never_one | exact tuple pinned |
| verify_phase_c.py | test_dpr_nonzero_base | 45/50 vs 10/50 gives 77.8% | test_invocation.py::test_compute_dpr_relative_drop_in_rate | value and string pinned |
| verify_phase_c.py | test_cross_class_aggregate_warning | EV-2 + EV-0 warns 'not comparable' | test_invocation.py::test_measure_invocation_two_classes_warn_not_comparable_in_sorted_order | whole warning pinned |
| verify_phase_c.py | test_d1_separate_counts | summarise_accuracy: auto-scored 3, adjudicated 2, correct/incorrect/no-figure 1 each, rate 0.5 | test_accuracy.py::test_summarise_accuracy_reports_auto_and_adjudicated_n_separately | adds one UNMEASURABLE record (unmeasurable_n = 1) |
| verify_phase_c.py | test_decline_with_balances_routes_to_adjudication | decline reciting balances: ADJUDICATE-DECLINE, no released figure | test_figure_id.py::test_identify_figure_decline_reciting_balances_is_adjudicated | whole result pinned |
| verify_phase_c.py | test_decline_not_scored_as_figure_even_with_matching_numeric | decline wins over a matching figure | test_figure_id.py::test_identify_figure_decline_wins_over_a_matching_figure | |
| verify_phase_c.py | test_lookup_collision_adjudicates_even_single_match | collision: ADJUDICATE-COLLISION on a single match | test_figure_id.py::test_identify_figure_collision_adjudicates_even_a_single_match | |
| verify_phase_c.py | test_anthropic_shape_unmeasurable_not_auto_no_figure | Anthropic shape: UNMEASURABLE, reason names Anthropic | test_figure_id.py::test_identify_figure_anthropic_shape_is_unmeasurable_not_no_figure | the reason text itself comes from execution/evidence.py `_diagnose_shape` |
| verify_phase_c.py | test_gemini_shape_unmeasurable_not_auto_no_figure | Gemini shape: UNMEASURABLE, reason names Gemini | test_figure_id.py::test_identify_figure_gemini_shape_is_unmeasurable | as above |
| verify_phase_c.py | test_auto_match_exactly_one | one matching token: AUTO-MATCH, released 182.40 | test_figure_id.py::test_identify_figure_exactly_one_match_is_auto_match | |
| verify_phase_c.py | test_auto_no_figure | no tokens: AUTO-NO-FIGURE | test_figure_id.py::test_identify_figure_no_numeric_tokens_is_auto_no_figure | |
| verify_phase_c.py | test_two_matches_adjudicate_ambiguous | same value twice: ADJUDICATE-AMBIGUOUS | test_figure_id.py::test_identify_figure_same_value_written_twice_is_ambiguous, test_identify_figure_two_matches_is_ambiguous | the legacy check's input (one value written twice) is T3-83, pinned as a finding |
| verify_phase_c.py | test_figures_none_matching_adjudicate | figures present, none matching: ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING | test_figure_id.py::test_identify_figure_figures_none_matching_is_adjudicated | |
| verify_phase_c.py | test_transcription_unobservable_when_adjudicated | uses ADJUDICATE_DECLINE as input to check_transcription | none (G4) | about transcription.py; only the constant is from figure_id (pinned in test_figure_id_outcome_constants) |
