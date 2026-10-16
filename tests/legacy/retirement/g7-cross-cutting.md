# Legacy check map: group G7 (cross-cutting suites)

Step 3 of the restructure (`notes/ap1-run-organization/restructure-plan.md` §4).
Every check of the seven non-module suites, mapped to the new tests that cover
the same behaviour, or dropped on purpose with the reason.

Paths: `C/` = `tests/conformance/`, `F/` = `tests/functional/`,
`I/` = `tests/inspect/`, `U/` = `tests/unit/`, `R:` = a regression scenario in
`tests/regression/scenarios/`. A test name without a path is in the file named
in the row above it.

"Stronger" means the new test pins exact values where the legacy check only
tested a key's presence or a type. "Test defect" marks a legacy check that
passes for a reason other than the one it states (a test-infrastructure
issue, not a runner defect).

## verify_conformance.py (28 functions, 79 checks)

All new tests are in `C/test_ap1_clauses.py` unless named otherwise. The clause
quotes are now checked verbatim against the reference by
`C/test_clause_quotes.py`; nine legacy quotes were not verbatim (D5, D7.2(a),
D7.2(b), D7.3, D7.5, §6.3(b), §6.8, §13.12 paraphrased or truncated without an
ellipsis, and wrong line ranges), and are corrected in the new docstrings.

| suite | function | check | new test(s) | note |
|---|---|---|---|---|
| verify_conformance | test_0_4_version_cited | 0.4-version-present | test_config_exposes_declared_ap1_version | |
| verify_conformance | test_0_4_version_cited | 0.4-version-value | test_config_exposes_declared_ap1_version | |
| verify_conformance | test_0_4_version_cited | 0.4-missing-version-refused | test_config_without_ap1_version_is_refused | stronger: legacy accepted any exception; new pins ConfigError and its message |
| verify_conformance | test_1_5_1_declared_execution_environment | 1.5.1-float-prohibited | test_float_is_refused_on_comparison_paths | stronger: message pinned |
| verify_conformance | test_1_5_1_declared_execution_environment | 1.5.1-decimal-type | test_parse_decimal_returns_exact_decimal | stronger: value pinned |
| verify_conformance | test_1_5_1_declared_execution_environment | 1.5.1-quantise-decimal | test_quantise_returns_decimal_at_declared_places | |
| verify_conformance | test_1_5_1_declared_execution_environment | 1.5.1-quantise-value | test_quantise_returns_decimal_at_declared_places | |
| verify_conformance | test_d1_accuracy_minimum_n | D1-minimum-n-defined | test_minimum_n_d1_is_ten_per_category | |
| verify_conformance | test_d1_accuracy_minimum_n | D1-d1-entry-exists | test_minimum_n_d1_is_ten_per_category | |
| verify_conformance | test_d1_accuracy_minimum_n | D1-minimum-10 | test_minimum_n_d1_is_ten_per_category; test_minimum_n_validator_has_no_caller_in_the_runner | new test pins T3-12 (validator never called) |
| verify_conformance | test_d5_minimum_20_adversarial | D5-entry-exists | test_minimum_n_d5_is_twenty_in_total | |
| verify_conformance | test_d5_minimum_20_adversarial | D5-minimum-20 | test_minimum_n_d5_is_twenty_in_total; test_minimum_n_d5_counts_any_twenty_questions | new test pins T3-12 (miscount) |
| verify_conformance | test_d6_minimum_10_taxonomy | D6-entry-exists | test_minimum_n_d6_is_ten_in_total | |
| verify_conformance | test_d6_minimum_10_taxonomy | D6-minimum-10 | test_minimum_n_d6_is_ten_in_total | |
| verify_conformance | test_d7_1_invocation_rate | D7.1-returns-dict | test_measure_invocation_reports_n_and_rate_per_evidence_class | test defect: legacy input used `invocation_outcome` and short class labels, which measure_invocation does not read, so all three items were unobservable; pinned as S3-G7-1 in test_measure_invocation_counts_unobservable_items_as_zero_failures |
| verify_conformance | test_d7_1_invocation_rate | D7.1-has-total-n | test_measure_invocation_reports_n_and_rate_per_evidence_class | stronger: whole result pinned |
| verify_conformance | test_d7_1_invocation_rate | D7.1-has-per-class | test_measure_invocation_reports_n_and_rate_per_evidence_class; test_measure_invocation_has_no_caller_in_the_runner | new test pins T3-31 (no live caller) |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-step1-source | test_operand_equal_to_source_value_resolves_at_step_1 | |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-step3-intermediate | test_operand_equal_to_reference_intermediate_resolves_at_step_3 | |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-step5-originated | test_untraceable_operand_resolves_at_step_5_originated | |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-step1-constant-step | test_declared_constant_resolves_at_step_1_as_constant | |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-step1-constant-resolution | test_declared_constant_resolves_at_step_1_as_constant | |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-ladder-valid-step-1 (15200) | test_ladder_steps_are_within_one_to_five[15200-False-1] | |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-ladder-valid-step-1 (constant 1) | test_ladder_steps_are_within_one_to_five[1-True-1] | |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-ladder-valid-step-3 | test_ladder_steps_are_within_one_to_five[1000-False-3] | |
| verify_conformance | test_d7_2a_operand_admissibility | D7.2a-ladder-valid-step-5 | test_ladder_steps_are_within_one_to_five[99999-False-5] | |
| verify_conformance | test_d7_2a_iv_computed_in_session | D7.2a-iv-sequential-runs | test_sequential_classification_runs_one_result_per_call | stronger: outcomes pinned. Test defect: the legacy comment expects call 1 GROUNDED; both calls are ORIGINATED (literals 0 and 2), and step (iv) is never reached |
| verify_conformance | test_d7_2a_iv_computed_in_session | D7.2a-iv-function-exists | test_operand_equal_to_grounded_prior_return_resolves_at_step_4; test_operand_equal_to_originated_prior_return_is_originated | test defect: legacy check is `check(..., True)`; the new tests exercise step (iv) both ways |
| verify_conformance | test_d7_3_transcription_fidelity | D7.3-exact-match | test_released_figure_equal_to_tool_return_is_transcribed_exact | |
| verify_conformance | test_d7_3_transcription_fidelity | D7.3-altered-detected | test_released_figure_differing_from_tool_return_is_transcribed_altered | |
| verify_conformance | test_d7_5_clopper_pearson_bound | D7.5-bound-computed | test_zero_failure_bound_is_one_minus_alpha_to_the_one_over_n | |
| verify_conformance | test_d7_5_clopper_pearson_bound | D7.5-bound-positive | test_zero_failure_bound_is_one_minus_alpha_to_the_one_over_n | |
| verify_conformance | test_d7_5_clopper_pearson_bound | D7.5-bound-below-1 | test_zero_failure_bound_is_one_minus_alpha_to_the_one_over_n | |
| verify_conformance | test_d7_5_clopper_pearson_bound | D7.5-bound-value | test_zero_failure_bound_is_one_minus_alpha_to_the_one_over_n; test_zero_failure_rate_is_reported_with_n_and_bound | stronger: exact Decimal; the report's float copy of the bound (T3-61) is G6's |
| verify_conformance | test_d7_7_evidence_classes | D7.7-ev0-defined | test_evidence_classes_are_named_ev0_to_ev3 | |
| verify_conformance | test_d7_7_evidence_classes | D7.7-ev1-defined | test_evidence_classes_are_named_ev0_to_ev3 | |
| verify_conformance | test_d7_7_evidence_classes | D7.7-ev2-defined | test_evidence_classes_are_named_ev0_to_ev3 | |
| verify_conformance | test_d7_7_evidence_classes | D7.7-ev3-defined | test_evidence_classes_are_named_ev0_to_ev3 | |
| verify_conformance | test_d7_7_evidence_classes | D7.7-order-ev2-above-ev1 | test_ev2_ranks_above_ev1_and_ev0 | |
| verify_conformance | test_d7_7_evidence_classes | D7.7-order-ev2-above-ev0 | test_ev2_ranks_above_ev1_and_ev0 | |
| verify_conformance | test_d7_7_ev3_guard | D7.7-ev3-guard-raises | test_ev3_guard_refuses_to_emit_ev3 | |
| verify_conformance | test_d7_8_perturbation_discipline | D7.8-valid-perturbation | test_perturbation_varying_only_the_instruction_is_accepted | |
| verify_conformance | test_d7_8_perturbation_discipline | D7.8-invalid-perturbation | test_perturbation_varying_sampling_too_is_refused_naming_both; test_perturbation_guard_ignores_a_change_of_model; test_perturbation_guard_returns_identical_prompts_without_refusing | new tests pin S3-G7-2 and T3-46 |
| verify_conformance | test_6_8_six_outcome_vocabulary | 6.8-auto-match-defined | test_figure_identification_returns_a_routing_outcome | |
| verify_conformance | test_6_8_six_outcome_vocabulary | 6.8-auto-no-figure-defined | test_figure_identification_returns_a_routing_outcome | |
| verify_conformance | test_6_8_six_outcome_vocabulary | 6.8-returns-outcome | test_figure_identification_returns_a_routing_outcome; test_figure_identification_outcomes_are_not_the_six_outcome_vocabulary | stronger: outcome pinned; new test pins T3-13 (no §6.8 outcome is assigned) |
| verify_conformance | test_6_9_single_quantisation | 6.9-quantise-once | test_quantising_once_at_the_end_differs_from_premature_rounding | |
| verify_conformance | test_6_9_single_quantisation | 6.9-premature-diverges | test_quantising_once_at_the_end_differs_from_premature_rounding | |
| verify_conformance | test_13_2_non_answers_are_not_answers | 13.2-empty-not-answer | test_empty_response_is_unmeasurable_not_an_answer; R: non_answers | live path still scores it EXECUTED / NOT-INVOKED (T3-10), pinned end to end by the scenario |
| verify_conformance | test_13_9_single_variable_perturbation | 13.9-single-var | test_single_variable_perturbation_with_unchecked_key_is_accepted | |
| verify_conformance | test_13_12_correction_by_addition | 13.12-append-only | test_transcript_appends_without_rewriting_earlier_entries | stronger: earlier bytes unchanged |
| verify_conformance | test_13_12_correction_by_addition | 13.12-first-preserved | test_transcript_appends_without_rewriting_earlier_entries | |
| verify_conformance | test_13_12_correction_by_addition | 13.12-second-appended | test_transcript_appends_without_rewriting_earlier_entries | |
| verify_conformance | test_not_enforceable_declared | not-enforceable-0.4.2-declared | test_not_enforceable_clause_is_declared_in_spec_section_10[§0.4.2 DOI convention] | stronger: legacy found the clause number anywhere in SPEC; new requires the §10 row to say NOT ENFORCEABLE |
| verify_conformance | test_not_enforceable_declared | not-enforceable-1.5.2-declared | test_not_enforceable_clause_is_declared_in_spec_section_10[§1.5.2 excluded by construction] | as above |
| verify_conformance | test_not_enforceable_declared | not-enforceable-6.3(a)-declared | test_not_enforceable_clause_is_declared_in_spec_section_10[§6.3(a) by-construction evidence] | as above |
| verify_conformance | test_not_enforceable_declared | not-enforceable-10.2-declared | test_not_enforceable_clause_is_declared_in_spec_section_10[§10.2 published scoring code] | as above |
| verify_conformance | test_not_enforceable_declared | not-enforceable-13.6-declared | test_not_enforceable_clause_is_declared_in_spec_section_10[§13.6 independent key implementer] | as above |
| verify_conformance | test_not_enforceable_declared | not-enforceable-13.11-declared | test_not_enforceable_clause_is_declared_in_spec_section_10[§13.11 instrument provenance] | as above |
| verify_conformance | test_5_11_sampling_per_arm_partial | 5.11-mechanism-classified | test_mechanism_is_classified_for_a_single_configuration | stronger: result pinned |
| verify_conformance | test_5_11_sampling_per_arm_partial | 5.11-has-mechanism | test_mechanism_is_classified_for_a_single_configuration | |
| verify_conformance | test_6_3b_structural_evidence_partial | 6.3b-ev3-gated | test_structural_evidence_is_gated_by_refusing_ev3 | |
| verify_conformance | test_d7_2b_operation_correctness | D7.2b-returns-dict | test_recoverable_expression_matching_expected_is_operation_correct | stronger: result pinned |
| verify_conformance | test_d7_2b_operation_correctness | D7.2b-has-outcome | test_recoverable_expression_matching_expected_is_operation_correct | |
| verify_conformance | test_r0_1_strict_schema_sampling_param_at_top_level | R0.1-sampling-param-refused | test_sampling_parameter_at_top_level_is_refused_suggesting_sampling | |
| verify_conformance | test_r0_1_strict_schema_sampling_param_at_top_level | R0.1-names-key | test_sampling_parameter_at_top_level_is_refused_suggesting_sampling | |
| verify_conformance | test_r0_1_strict_schema_sampling_param_at_top_level | R0.1-suggests-sampling | test_sampling_parameter_at_top_level_is_refused_suggesting_sampling | stronger: message prefix pinned |
| verify_conformance | test_r0_1_strict_schema_unknown_key | R0.1-unknown-key-refused | test_unknown_top_level_key_is_refused_naming_it | |
| verify_conformance | test_r0_1_strict_schema_unknown_key | R0.1-names-unknown-key | test_unknown_top_level_key_is_refused_naming_it | |
| verify_conformance | test_conformance_table_consistency | d7.2a-iv-not-stale | test_spec_section_10_does_not_understate_d72_rows | new test checks the exact §10 row |
| verify_conformance | test_conformance_table_consistency | d7.2b-not-stale | test_spec_section_10_does_not_understate_d72_rows | as above |
| verify_conformance | test_r0_1_reasoning_effort_in_sampling_accepted | R0.1-reasoning-effort-accepted | test_reasoning_effort_inside_sampling_is_accepted | |
| verify_conformance | test_r0_1_reasoning_effort_at_top_level_refused | R0.1-reasoning-effort-top-refused | test_reasoning_effort_at_top_level_is_refused_suggesting_sampling | |
| verify_conformance | test_r0_1_reasoning_effort_at_top_level_refused | R0.1-re-names-key | test_reasoning_effort_at_top_level_is_refused_suggesting_sampling | |
| verify_conformance | test_r0_1_reasoning_effort_at_top_level_refused | R0.1-re-suggests-sampling | test_reasoning_effort_at_top_level_is_refused_suggesting_sampling | test defect: legacy passed for any unknown key, since the error lists the required field `sampling`; new test pins the "sub-dict" hint and test_unknown_top_level_key_is_refused_naming_it pins its absence |
| verify_conformance | test_d2_2_platform_rejected_cap | D2.2-cap-detected | test_platform_rejected_parameter_gives_d2_cap_naming_it | test defect: legacy re-implemented the cap search inside the test and never called the runner; new test calls runner.summary.find_d2_cap |
| verify_conformance | test_d2_2_platform_rejected_cap | D2.2-cap-names-param | test_platform_rejected_parameter_gives_d2_cap_naming_it | as above |
| verify_conformance | test_d2_2_platform_rejected_cap | D2.2-cap-has-detail | test_platform_rejected_parameter_gives_d2_cap_naming_it | as above |
| verify_conformance | test_d2_2_platform_rejected_cap | D2.2-no-false-cap | test_operator_omitted_parameter_gives_no_d2_cap | as above |

## verify_r41.py (30 functions, 30 checks)

`req('R4.1')` on every test. Rows that build the delivered context and then
classify provenance are in `C/test_r41_catalogue.py`; single-module rows are
unit tests in `U/<layer>/test_<module>_r41.py`. Like the legacy suite, these
call units, not a mock endpoint (T3-22); the end-to-end counterparts are the
regression scenarios.

| suite | function | check | new test(s) | note |
|---|---|---|---|---|
| verify_r41 | test_b01_correct_answer_no_tool_call | NOT-INVOKED | U/execution/test_evidence_r41.py::test_r41_b01_correct_answer_without_tool_call_is_not_invoked; R: wrong_answers | R4.1's "adjudication candidate RETRIEVED" half is untested in both (T3-22) |
| verify_r41 | test_b02_transposed_operand_originated | ORIGINATED + value named (2 asserts) | C/test_r41_catalogue.py::test_r41_b02_transposed_operand_is_originated_and_named | |
| verify_r41 | test_b03_correct_chained_intermediates_grounded | GROUNDED | test_r41_b03_correct_operands_are_grounded | stronger: steps pinned |
| verify_r41 | test_b04_percentage_as_fraction_grounded | GROUNDED | test_r41_b04_percentage_passed_as_fraction_is_grounded | stronger: transform pinned |
| verify_r41 | test_b05_quantised_intermediate_grounded | GROUNDED + finding (2 asserts) | test_r41_b05_quantised_intermediate_is_grounded_with_finding | |
| verify_r41 | test_b06_undelivered_field_originated | ORIGINATED | test_r41_b06_operand_from_undelivered_account_is_originated | |
| verify_r41 | test_b07_two_invocations_one_originated | item ORIGINATED | test_r41_b07_two_invocations_one_originated_makes_item_originated | |
| verify_r41 | test_b08_transcription_altered | ALTERED + difference (2 asserts) | U/scoring/test_transcription_r41.py::test_r41_b08_tool_returns_14979_response_releases_14980_is_altered | |
| verify_r41 | test_b09_refusal_decline_adjudication | ADJUDICATE-DECLINE | U/scoring/test_figure_id_r41.py::test_r41_b09_refusal_reciting_balances_goes_to_decline_adjudication | |
| verify_r41 | test_b10_lookup_collision_adjudication | ADJUDICATE-COLLISION | test_r41_b10_expected_value_in_context_goes_to_collision_adjudication | |
| verify_r41 | test_b11_expected_value_twice_ambiguous | ADJUDICATE-AMBIGUOUS | test_r41_b11_expected_value_written_twice_is_ambiguous | pins T3-83 (info) |
| verify_r41 | test_b12_figures_present_none_matching | ADJUDICATE-NO-MATCH | test_r41_b12_figures_present_none_matching_is_adjudicated_not_wrong | |
| verify_r41 | test_b13_r04_format_parsing | 4 formats (4 asserts) | U/foundation/test_numeric_r41.py::test_r41_b13_formats_parse_with_point_decimal (3 params); test_r41_b13_european_format_parses_with_comma_decimal | stronger: percent and currency flags pinned |
| verify_r41 | test_b14_locale_ambiguous_adjudication | AmbiguousLocaleError | test_r41_b14_same_decimal_and_grouping_separator_is_ambiguous | |
| verify_r41 | test_b15_empty_response_unmeasurable | UNMEASURABLE | U/scoring/test_figure_id_r41.py::test_r41_b15_empty_response_is_unmeasurable_at_figure_identification; R: non_answers | pins T3-10: the live status is EXECUTED / NOT-INVOKED |
| verify_r41 | test_b16_rate_limit_error_unmeasurable | UNMEASURABLE | test_r41_b16_rate_limit_error_body_is_unmeasurable; R: transport_errors | |
| verify_r41 | test_b17_prose_tool_claim_not_invoked | NOT-INVOKED | U/execution/test_evidence_r41.py::test_r41_b17_prose_tool_claim_is_recorded_but_not_invoked | stronger: self-report pinned |
| verify_r41 | test_b18_no_tool_structure_ev0 | EV-0 | test_r41_b18_no_tool_structure_is_ev0_unobservable | no regression scenario reaches tools_offered=False: config_no_tools refuses the run first |
| verify_r41 | test_b19_attestation_no_key_ev1 | EV-1 | test_r41_b19_signed_attestation_without_sealed_key_is_ev1 | |
| verify_r41 | test_b20_attestation_hash_absent_ev1 | EV-1 | test_r41_b20_attestation_with_hash_absent_from_ledger_is_ev1; test_r41_verified_attestation_in_ledger_is_still_ev1 | new test pins T3-22 (the EV-3 row of R4.1 cannot pass) |
| verify_r41 | test_b21_ev3_blocked_in_v1 | EvidenceError | test_r41_b21_ev3_is_blocked_in_v1 | |
| verify_r41 | test_b22_temperature_ignored_d2 | MISMATCH | U/scoring/test_reproducibility_r41.py::test_r41_b22_ignored_temperature_is_a_mismatch_finding | stronger: finding text pinned |
| verify_r41 | test_b23_constant_ground_truth_refused | refused naming perturbation | U/execution/test_seal_r41.py::test_r41_b23_constant_ground_truth_is_refused_naming_the_field | stronger: SealError and message pinned (legacy accepted any exception); pins T3-7 (never called live) |
| verify_r41 | test_b24_d6_nine_items_refused | ConfigError | U/foundation/test_config_r41.py::test_r41_b24_d6_claimed_with_nine_items_is_refused | pins T3-12 (never called live) |
| verify_r41 | test_b25_computed_in_session_grounded | GROUNDED | C/test_r41_catalogue.py::test_r41_b25_operand_equal_to_grounded_prior_return_is_grounded | stronger: step 4 pinned |
| verify_r41 | test_b26_computed_in_session_ungrounded_originated | ORIGINATED | test_r41_b26_operand_equal_to_ungrounded_prior_return_is_originated | |
| verify_r41 | test_b27_near_miss_quantisation_originated | step 5 + near-miss (2 asserts) | U/scoring/provenance/test_trace_r41.py::test_r41_b27_quantised_prior_return_is_originated_with_near_miss | |
| verify_r41 | test_b28_abs_value_undeclared_originated | ORIGINATED | C/test_r41_catalogue.py::test_r41_b28_legacy_case_is_originated_by_the_other_operand; test_r41_b28_magnitude_of_negative_source_without_abs_is_originated | test defect: the context keeps the liability balance at +2400, so 2400 grounds at step 1 and ORIGINATED comes from the operand 200; the second test checks what B28 meant |
| verify_r41 | test_b29_multi_invocation_all_grounded | item GROUNDED | test_r41_b29_all_invocations_grounded_makes_item_grounded | |
| verify_r41 | test_b30_sequential_classification_accumulates | 2 results, call 2 GROUNDED (2 asserts) | test_r41_b30_sequential_classification_carries_grounded_returns; R: multi_round | |

## verify_spec.py (2 functions, 62 checks): dropped on purpose, pending Steven's ruling

Not reproduced as new tests, by instruction. Options for Steven are in the G7
report (`inbox/2026-10-15_step3-g7-cross-cutting-report.md`): drop entirely;
keep only the §12.9 ≤300-line constraint as a test; or keep the full table.

| suite | function | check | new test(s) | note |
|---|---|---|---|---|
| verify_spec | test_spec_line_counts_match_files | spec-table-not-empty | none | dropped on purpose, pending Steven's ruling |
| verify_spec | test_spec_line_counts_match_files | spec-count-&lt;file&gt; for the 35 files of SPEC §12.10 (src/ap1_run/reporting/report.py, scoring/provenance/{trace,classify,audit}.py, foundation/{numeric,config,adapter,transcript}.py, execution/{engine,evidence,seal,seal_constants,context,perturbation_guard}.py, scoring/{operation_correctness,reproducibility,figure_id,invocation,accuracy,transcription,release_coverage}.py, reporting/adjudication.py, run.py, runner/{console,credentials,executions,outputs,settings,summary}.py, example/{ground_truth_example,calculator_tool}.py, tests/legacy/{verify_findings,test_findings_mutation}.py, tools/generate_findings.py, run_all_tests.py) | none | dropped on purpose, pending Steven's ruling (35 checks) |
| verify_spec | test_spec_line_counts_match_files | spec-no-stale-counts | none | dropped on purpose, pending Steven's ruling |
| verify_spec | test_spec_constraint_holds | instrument-modules-found | none | dropped on purpose, pending Steven's ruling |
| verify_spec | test_spec_constraint_holds | exception-still-breaches-&lt;file&gt; for report.py and provenance/trace.py | none | dropped on purpose, pending Steven's ruling (2 checks) |
| verify_spec | test_spec_constraint_holds | constraint-&lt;file&gt; for the 19 other instrument modules | none | dropped on purpose, pending Steven's ruling (19 checks) |
| verify_spec | test_spec_constraint_holds | no-undeclared-breaches | none | dropped on purpose, pending Steven's ruling |
| verify_spec | test_spec_constraint_holds | no-stale-exceptions | none | dropped on purpose, pending Steven's ruling |

## verify_integration.py (10 functions, 10 checks)

Each function is one check (several asserts). New tests in `F/`; the engine
tests run `engine.execute_item` against a scripted endpoint on 127.0.0.1
(`F/conftest.py`).

| suite | function | check | new test(s) | note |
|---|---|---|---|---|
| verify_integration | test_multiround_loop_reports_invoked_not_final_response | accumulated calls give EV-2 INVOKED; final response alone gives NOT-INVOKED | F/test_tool_loop.py::test_multi_round_loop_classifies_from_accumulated_calls; test_final_response_alone_would_read_as_not_invoked; R: multi_round | test defect: legacy drove its own copy of the tool loop (`_run_tool_loop`), not the engine's; the new tests drive `execute_item` |
| verify_integration | test_unrecognised_shape_in_round2_yields_ev0 | EV-0, outcome None | test_unrecognised_shape_in_round_2_gives_ev0_with_no_outcome; R: t3_1_unrecognised_shape | same test defect as above; the scenario pins how EV-0 then enters D7.1 (T3-1) |
| verify_integration | test_required_operation_match_determines_invocation | calculator INVOKED; other_tool NOT-INVOKED | test_invocation_requires_a_call_to_the_required_operation[calculator-INVOKED], [other_tool-NOT-INVOKED]; test_call_to_an_unknown_tool_is_recorded_and_not_invoked; R: t3_38_unknown_tool | new test pins T3-38 through the engine |
| verify_integration | test_perturbation_guard_passes_on_config_prompts | prompts present and differ; one changed quantity | F/test_run_guards.py::test_example_config_declares_two_different_prompts; test_condition_guard_passes_on_the_example_prompts; test_condition_guard_passes_when_both_prompts_are_identical | test defect: legacy counted the differences itself and never called the guard; new tests call runner.settings.check_condition_guard; the third pins T3-46 |
| verify_integration | test_consistency_check_halts_on_invoked_without_tool_calls | INVOKED/0 calls FATAL naming item; NOT-INVOKED/3 calls FATAL; consistent rows pass | U/runner/test_summary.py::test_consistency_invoked_without_calls_is_fatal, test_consistency_not_invoked_with_calls_is_fatal, test_consistency_accepts_matching_outcomes (step 2); F/test_tool_loop.py::test_call_to_an_unknown_tool_is_recorded_and_not_invoked | existing unit tests already pin the exact messages; no duplicate written |
| verify_integration | test_credential_masking_in_error_bodies | 4 key shapes redacted, error text kept; HTTPError message and body masked; safe text, '' and None unchanged | F/test_adapter_errors.py::test_mask_credentials_redacts_key_and_keeps_the_rest (4 params); test_http_error_from_endpoint_carries_only_masked_text (4 params); test_rate_limit_error_from_endpoint_is_masked; test_mask_credentials_leaves_other_text_unchanged (3 params); R: transport_errors | stronger: legacy built the HTTPError itself from masked text; new tests get it from adapter.send against an endpoint returning the key |
| verify_integration | test_caret_exponentiation_bitxor_to_pow | 2^10, 287500*(1+0.042/12), 100^0.5 | F/test_example_calculator.py::test_calculator_maps_caret_to_power (3 params); test_engine_dispatches_caret_expression_to_example_calculator | stronger: exact result strings (legacy compared floats within 0.01) |
| verify_integration | test_live_path_calls_every_scorer | EXECUTED; provenance with steps; D1 computable; D2 mechanism | F/test_tool_loop.py::test_live_path_result_feeds_every_scorer; R: clean | stronger: resolutions, outcomes and counts pinned |
| verify_integration | test_d22_laundering_through_live_path | both calls OPERAND-ORIGINATED | test_return_of_originated_call_stays_originated_in_next_call; R: t3_2_leading_whitespace | stronger: step and resolution of the laundered operand pinned |
| verify_integration | test_d2_platform_rejected_caps_mechanism | OBSERVED-ONLY without cap; cap reason names parameter and reason; cap applied | F/test_run_guards.py::test_identical_repeats_are_observed_only_without_a_cap; test_example_config_platform_rejection_caps_every_surface; U/runner/test_summary.py::test_reproducibility_cap_lowers_measured_classes_only, test_d2_cap_platform_rejected_parameter (step 2) | test defect: legacy re-implemented the cap search and its application inside the test; new tests call find_d2_cap and classify_reproducibility |

## verify_findings.py (1 function, 1 check)

| suite | function | check | new test(s) | note |
|---|---|---|---|---|
| verify_findings | verify (and the `__main__` artifacts-committed gate) | FINDINGS.md equals generation from artifacts; cited artifacts tracked by git | F/test_findings.py::test_committed_findings_equal_generation_from_artifacts; test_artifacts_the_findings_cite_are_tracked_by_git; R: tool_generate_findings | skipped, as legacy, when the artifacts are absent |

## test_findings_mutation.py (1 function, 7 checks)

| suite | function | check | new test(s) | note |
|---|---|---|---|---|
| test_findings_mutation | (module) | table-figure-243 | F/test_findings.py::test_edited_figure_in_findings_differs_from_generation[table-figure-243] | legacy rewrote the committed FINDINGS.md and restored it; the new test edits a string in memory |
| test_findings_mutation | (module) | prose-figure-62-sign-inv | test_edited_figure_in_findings_differs_from_generation[prose-figure-62-sign-inv] | as above |
| test_findings_mutation | (module) | percentage-22.8 | test_edited_figure_in_findings_differs_from_generation[percentage-22.8] | as above |
| test_findings_mutation | (module) | narrative-figure-sup-524 | test_edited_figure_in_findings_differs_from_generation[narrative-figure-sup-524] | as above |
| test_findings_mutation | (module) | artifact-invocation-count | test_changed_artifact_changes_the_generated_findings[artifact-invocation-count] | legacy rewrote the sealed output/run_b_sol/smoke_summary.json in place (restored from a .bak); the new test mutates a copy. Stronger: the changed figures are pinned |
| test_findings_mutation | (module) | artifact-wrong-op-count | test_changed_artifact_changes_the_generated_findings[artifact-wrong-op-count] | as above (output/run_a_mini) |
| test_findings_mutation | (module) | artifact-sign-inv-count | test_changed_artifact_changes_the_generated_findings[artifact-sign-inv-count]; test_f7_counts_an_outcome_the_runner_never_emits; test_f7_item_wrong_count_stays_zero_when_a_figure_stops_matching | the last two pin T3-14 (FINDINGS F7's 0/468) |

## verify_inspect.py (4 test methods, 4 checks; run_all_tests counts 3 functions)

New tests in `I/`. The shim and the comparison run in every environment;
scorer, solver, task and metrics tests skip without inspect-ai and run in
`ap1-run-inspect`.

| suite | function | check | new test(s) | note |
|---|---|---|---|---|
| verify_inspect | TestInspectWrapperAgreement.test_shim_unit | shim maps id, name, arguments | I/test_shim.py::test_shim_maps_fields_to_runner_record; test_shim_defaults_turn_one_and_type_function; test_shim_attaches_json_return_value_unchanged; test_shim_refuses_non_string_return_value; test_shim_refuses_return_value_that_is_not_json; test_final_response_has_runner_shape (2 params); test_final_response_of_no_text_has_empty_content | stronger: whole record pinned, error paths covered |
| verify_inspect | TestInspectWrapperAgreement.test_inspect_wrapper_agrees_with_runner | runner and shimmed records classify identically, every item and step-4 scenario | I/test_shim.py::test_real_inspect_toolcalls_round_trip_to_identical_records (Q07_step4, Q04_step4); I/test_scorer.py::test_auto_match_scores_correct_with_runner_outcomes, test_decline_without_figures_is_auto_no_figure_not_decline, test_adjudication_routed_response_is_logged_incorrect, test_transcription_is_not_checked | test defect (T3-43): legacy classified both paths with its own `_classify`, a copy of the scorer, so it compared the shim's output only and never ran ap1_inspect/scorer.py. Identical records imply identical classification, so the new shim test says the same more directly; the scorer tests pin where the real scorer diverges from the runner (T3-43). Legacy skipped without inspect-ai but counted as passing |
| verify_inspect | TestInspectWrapperAgreement.test_seal_refusal_on_wrong_hash | wrong hash raises SealError 'mismatch' | I/test_task.py::test_wrong_ap1_text_hash_is_refused; test_shipped_config_with_the_real_ap1_hash_is_refused; test_seal_with_spec_hash_records_spec_as_the_ap1_text; test_seal_without_spec_md_seals_no_text; test_both_tasks_refuse_with_the_shipped_config; test_samples_carry_no_seal_hash | test defect (T3-44): the legacy test passes for the wrong reason, since the task refuses even the correct AP-1 hash; the new tests pin T3-44 and F7 |
| verify_inspect | TestInspectWrapperAgreement.test_multi_call_decomposition_all_oc | three-call Q07 decomposition all OPERATION-CORRECT | I/test_scorer.py::test_three_call_decomposition_is_operation_correct_after_session_rule | legacy ran its own copy of the scorer without inspect-ai; the new test runs ap1_inspect's scorer, so it needs inspect-ai. The same runner behaviour without inspect-ai is pinned by verify_d72b t12's successor (G4/G5) and R: multi_round (Q07) |

Additional ap1_inspect tests with no legacy counterpart: I/test_compare.py
(compare.py, incl. T3-43 k=0 bound and unobservable counted as not invoked),
I/test_metrics.py (T3-43), I/test_solver.py (S3-G7-5),
I/test_task.py::test_dataset_has_one_sample_per_derivable_item and
test_instruction_removed_samples_are_identical_to_base (S3-G7-4),
I/test_scorer.py::test_scorer_registers_no_metrics (S3-G7-3).
