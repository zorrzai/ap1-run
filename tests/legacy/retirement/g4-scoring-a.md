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
| verify_d72b.py | test_t1_correct_expression_q01 | Q01 correct expression: OPERATION-CORRECT against expected_value | test_operation_correctness.py::test_classify_operation_result_equal_to_expected_is_correct | uses a local Q07-like ground truth instead of example/ground_truth_example.compute |
| verify_d72b.py | test_t2_wrong_expression_q01 | doubled rate: WRONG-OPERATION | test_operation_correctness.py::test_classify_operation_wrong_operation_detail | |
| verify_d72b.py | test_t3_intermediate_match_q04 | Q04 monthly interest matches an intermediate | test_operation_correctness.py::test_classify_operation_raw_intermediate_is_correct | |
| verify_d72b.py | test_t4_unparseable | prose: OPERATION-UNOBSERVABLE | test_operation_correctness.py::test_classify_operation_unparseable_is_unobservable | |
| verify_d72b.py | test_t5_empty | '': OPERATION-UNOBSERVABLE | test_operation_correctness.py::test_evaluate_expression_non_string_or_blank_is_none, test_classify_operation_non_string_is_unobservable | blank string covered at evaluate_expression level; classify routes every None the same way |
| verify_d72b.py | test_t6_correct_expression_q02 | Q02 '5000 - 2400' correct | test_operation_correctness.py::test_classify_operation_result_equal_to_expected_is_correct | same behaviour (result equals expected); Q02 data not reused |
| verify_d72b.py | test_t7_quantised_intermediate_q07 | '777.41' correct on Q07 | test_operation_correctness.py::test_classify_operation_quantised_intermediate_is_correct, test_classify_operation_quantised_expected_is_correct, test_classify_operation_echoing_the_answer_is_correct | this check asserts the T3-6 echo; pinned there as a finding |
| verify_d72b.py | test_t8_decimal_precision | evaluation equals the Decimal computation | test_operation_correctness.py::test_evaluate_expression_is_exact_decimal_not_float | |
| verify_d72b.py | test_t9_q08_gpt41mini_wrong_operation | '-287500.00 + 1437.00': WRONG-OPERATION, result -286063.00 | test_operation_correctness.py::test_classify_operation_wrong_operation_detail | same behaviour on other data; the transcript provenance is dropped on purpose |
| verify_d72b.py | test_t10_q07_gpt56sol_equivalent_route | annual/4 route correct | test_operation_correctness.py::test_classify_operation_equivalent_route_is_correct | same expression |
| verify_d72b.py | test_t11_wrong_op_split_route_divergence | WRONG-OPERATION split by figure outcome | none (G4) | computes the split inline in the test; tests no code in these modules (the live split is in runner/console.py, another group's module); dropped on purpose for G4 |
| verify_d72b.py | test_t12_multi_call_equivalent_route | three-call Q07: all OPERATION-CORRECT after reclassify_session | test_operation_correctness.py::test_reclassify_session_operand_of_later_correct_call_becomes_correct | same three expressions |
| verify_d72b.py | test_t13_discarded_retry | garbage call not consumed stays WRONG-OPERATION | test_operation_correctness.py::test_reclassify_session_value_not_consumed_stays_wrong | |
| verify_d72b.py | test_t14_incomplete_computation | two components, no final call: both stay WRONG-OPERATION | test_operation_correctness.py::test_reclassify_session_unresolved_chain_stays_wrong | |
| verify_d72b.py | test_t15_per_call_classifier_returns_wo_on_decomposed_calls | per-call: WO, WO, OC on the three-call Q07 | test_operation_correctness.py::test_classify_operation_per_call_decomposition_is_wrong_until_reclassified | ground truth with the final value only, as the example's Q07 |
| verify_d72b.py | test_t16_declared_constants_check_catches_undeclared | declared_constants_check raises for undeclared D("4") | none (G4) | about execution/seal_constants.py; another group's module |
| verify_e7_coverage.py | test_e6_caret_precedence | '(1+0.078/12)^3-1' is ~0.0196, not the XOR result | test_operation_correctness.py::test_evaluate_expression_caret_is_power_with_power_precedence | same expression plus '2^3 - 1' |
