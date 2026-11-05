# Legacy checks mapped to unit tests: group G6 (reporting)

Modules: `src/ap1_run/reporting/adjudication.py`, `src/ap1_run/reporting/report.py`.
New tests: `tests/unit/reporting/test_adjudication.py` (A), `tests/unit/reporting/test_report.py` (R).

Among the module-level suites (`verify.py`, `verify_phase_b.py` … `verify_phase_e.py`,
`verify_d72b.py`, `verify_e7_coverage.py`, `verify_hashes.py`), only `verify_phase_e.py` imports
either module. Its `TestDOIRequired` and `TestDOISeal` classes test `foundation/config` and
`execution/seal` and are left to those modules' groups. Suites mapped by G7 (`verify_conformance`,
`verify_integration`, `verify_inspect`, ...) are not listed here.

| suite | function | check (short description or line) | new test(s) | note |
|---|---|---|---|---|
| verify_phase_e | TestSheetCompleteness.test_sheet_has_question | question text on the sheet (l.180) | A `test_sheet_question_quoted_with_category` | |
| verify_phase_e | TestSheetCompleteness.test_sheet_has_response_verbatim | response content verbatim (l.190) | A `test_sheet_response_verbatim_from_chat_completion` | |
| verify_phase_e | TestSheetCompleteness.test_sheet_has_fixture_excerpt | account name, balance, rate (l.200-202) | A `test_sheet_fixture_excerpt_lists_account_fields_but_id_and_name` | |
| verify_phase_e | TestSheetCompleteness.test_sheet_has_tool_call_record | tool name and arguments (l.212-213) | A `test_sheet_tool_calls_listed_with_arguments_and_returns` | |
| verify_phase_e | TestSheetCompleteness.test_sheet_has_evidence_class | evidence class (l.223) | A `test_sheet_tool_calls_listed_with_arguments_and_returns` | |
| verify_phase_e | TestSheetCompleteness.test_sheet_has_reason | decline routing reason (l.233) | A `test_sheet_reason_is_the_routing_text[ADJUDICATE-DECLINE]`, `test_adjudication_reasons_text` | |
| verify_phase_e | TestSheetCompleteness.test_sheet_has_all_six_outcomes | six §6.8 outcomes (l.244-247) | A `test_rubric_table_text`, `test_sheet_rubric_marks_and_blank_reasoning` | |
| verify_phase_e | TestSheetCompleteness.test_sheet_has_two_scorer_copies | "Scorer 1" and "Scorer 2" (l.258-259) | A `test_sheets_two_copies_per_item_with_shared_item_number`, `test_sheets_scorer_copies_are_identical_apart_from_heading` | |
| verify_phase_e | TestSheetCompleteness.test_sheet_has_reference_values | expected value 15.20 (l.269) | A `test_sheet_reference_values_and_closing_rule` | the legacy check also passes on the response text, which contains 15.20 |
| verify_phase_e | TestSheetCompleteness.test_no_sheet_for_auto_scored | AUTO-MATCH gets no sheet (l.282) | A `test_sheets_none_routed_says_so_and_counts_zero`, `test_needs_adjudication_other_outcomes_are_false` | |
| verify_phase_e | TestReportStructure.test_declares_unmeasured_d3_d6 | D3-D6 present, "NOT MEASURED" (l.338-340) | R `test_dimension_results_table_layout`, `test_unmeasured_dimensions_names_d3_to_d6_wrongly` | the new tests pin the rows and §12 text exactly, including the wrong names (T3-33) |
| verify_phase_e | TestReportStructure.test_does_not_declare_d2_as_human_adjudicated | D2 row not "NOT MEASURED" when claimed (l.353-358) | R `test_dimension_results_d2_live_shape_is_measured_with_n_na`, `test_unmeasured_dimensions_names_d3_to_d6_wrongly` | |
| verify_phase_e | TestReportStructure.test_d2_mechanism_section_present | §9 heading and "D2 is auto-measured" (l.368-369) | R `test_d2_without_results_says_so`, `test_d2_surfaces_table_sorted_with_basis` | |
| verify_phase_e | TestReportStructure.test_d2_shows_operator_declared_basis | "operator-declared" basis (l.382) | R `test_d2_surfaces_table_sorted_with_basis` | the legacy check also passes on the §9 note, which always says "operator-declared" |
| verify_phase_e | TestReportStructure.test_d2_shows_evidence_basis | "evidence" basis (l.392) | R `test_d2_surfaces_table_sorted_with_basis` | as above: lowercase "evidence" is always in the §9 note and the §4 comparability note, so the legacy check is vacuous |
| verify_phase_e | TestReportStructure.test_d2_shows_parameter_echo_status | UNVERIFIED echo status (l.402) | R `test_d2_surfaces_table_sorted_with_basis` | legacy uses the `{'surfaces': ...}` shape the live path never produces (T3-4); the live shape is pinned in `test_d2_live_shape_has_no_per_surface_data` |
| verify_phase_e | TestReportStructure.test_has_evidence_classes | evidence classes listed (l.411-412) | R `test_d7_figures_counts_sorted_by_class` | |
| verify_phase_e | TestReportStructure.test_has_auto_adjudicated_split | "Auto-scored", "Adjudicated" (l.421-422) | R `test_scoring_proportions_d1_split_and_rate`, `test_scoring_proportions_d7_split_labelled_provenance` | |
| verify_phase_e | TestReportStructure.test_has_operation_correctness | three D7.2(b) outcomes (l.431-433) | R `test_d72b_counts_in_fixed_order_with_total` | |
| verify_phase_e | TestReportStructure.test_has_version_doi | DOI in report (l.442) | R `test_report_header_names_version_doi_and_model`, `test_preregistration_lists_seal_fields_sorted` | |
| verify_phase_e | TestPartialDimension.test_d1_only_declares_rest | D2-D7 present and "NOT MEASURED" with only D1 claimed (l.461-463) | R `test_dimension_results_table_layout`, `test_unmeasured_dimensions_all_unclaimed` | |
| verify_phase_e | TestClopperPearson.test_k0_n10 | 1 - 0.05^(1/10), about 0.2589 (l.472-479) | R `test_clopper_pearson_k0_is_one_minus_alpha_to_one_over_n` | |
| verify_phase_e | TestClopperPearson.test_k0_n20 | 1 - 0.05^(1/20) (l.484-486) | R `test_clopper_pearson_k0_default_alpha_is_five_percent`, `test_clopper_pearson_k0_is_one_minus_alpha_to_one_over_n` | |
| verify_phase_e | TestClopperPearson.test_k0_n0_returns_nan | n = 0 gives NaN (l.490-491) | R `test_clopper_pearson_k0_n_not_positive_is_nan` | |
| verify_phase_e | TestClopperPearson.test_declared_limitation_in_report | k > 0 limitation text in report (l.504) | R `test_declared_limitations_text`, `test_clopper_pearson_section_failures_show_rate_without_bound` | |
| verify_phase_e | TestClopperPearsonNumeric.test_recompute_k0_n10 | function equals step-by-step recomputation (l.523-525) | R `test_clopper_pearson_k0_is_one_minus_alpha_to_one_over_n` | exact equality, as in legacy |

`verify_phase_e` docstring item 3 claims "kappa with small-n caveat"; no check exists for it and no
code computes it (T3-23), so there is nothing to map. Pinned instead by A
`test_sheet_rubric_marks_and_blank_reasoning`.
