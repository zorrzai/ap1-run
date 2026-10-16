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
