"""The test marks are used as pyproject.toml describes them.

- ``proposal(reason)``: one non-empty reason string, on a test that also
  names its finding, so ``pytest -m proposal`` lists every expectation that
  rests on the author's proposal rather than SPEC, AP-1 or a maintainer
  decision.
- ``provisional(reason)``: DEC-5's tests of today's behaviour in a module
  SPEC does not define, and the report, summary, console and sheet tests
  that show those modules' results; never on a strict xfail.
- A strict xfail is a test of the correct behaviour for a finding, so it
  carries a ``finding`` mark.
- Both marks match an explicit inventory below, so a mark added, lost or
  widened to a whole parametrised test shows up here.

The marks are read from a collection of the whole suite in a subprocess
(marks_plugin.py), not from this session's items, so a run of one file, a
-k or a -m selection still checks every test. Floors on the counts make a
collection that finds nothing (a broken plugin, a path error) fail.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]

# The inventory, without inspect-ai (its test files skip whole). Adding or
# removing a proposal or provisional mark means updating it here, in the
# same commit, so the change is visible.
EXPECTED_PROPOSAL_CASES = (
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[fifty-digits]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[float-is-the-value]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[floor]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[floordiv-as-python]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[int-truncates]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[interest]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[log-base]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[mod-as-python]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[mod-negative-divisor]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[mortgage]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[no-negative-zero]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[scientific-past-100-digits]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[tenths]',
    'tests/functional/test_example_calculator.py::test_calculator_computes_in_exact_decimal[zero-power-zero]',
    'tests/functional/test_example_calculator.py::test_faithful_copy_of_a_calculator_result_grounds_at_step_4',
    'tests/functional/test_step4_d1_categories.py::test_run_report_d1_per_category_with_n_result_and_interval',
    'tests/functional/test_step4_g1_invocation.py::test_run_d71_bound_counts_questions_not_repeats',
    'tests/functional/test_step4_g1_invocation.py::test_run_refusal_executed_adjudicated_outside_d71_and_d1[content-filter]',
    'tests/functional/test_step4_g1_invocation.py::test_run_refusal_executed_adjudicated_outside_d71_and_d1[refusal]',
    'tests/functional/test_step4_g2_provenance.py::test_run_question_with_mixed_executions_is_unmeasurable_in_every_one',
    'tests/functional/test_step4_g2_provenance.py::test_run_report_states_operands_unobservable_count',
    'tests/functional/test_step4_g2_provenance.py::test_run_unknown_name_in_expression_is_operands_unobservable',
    'tests/functional/test_step4_g4_transcript.py::test_run_ev0_causes_are_distinct',
    'tests/functional/test_step4_g4_transcript.py::test_run_ev0_record_names_cause_and_round[dropped-connection]',
    'tests/functional/test_step4_g4_transcript.py::test_run_ev0_record_names_cause_and_round[http-503]',
    'tests/functional/test_step4_g4_transcript.py::test_run_ev0_record_names_cause_and_round[unrecognised-shape]',
    'tests/functional/test_step4_g5_seal_verifier.py::test_run_ground_truth_values_changing_between_computations_refused',
    'tests/functional/test_step4_g5_seal_verifier.py::test_run_seal_record_binds_expected_values',
    'tests/functional/test_step4_g5_seal_verifier.py::test_run_seal_record_carries_environment_fields',
    'tests/functional/test_step4_g5_seal_verifier.py::test_run_v12_config_seals_the_v12_text',
    'tests/functional/test_step4_g5_seal_verifier.py::test_run_v12_label_never_sealed_over_v13_text[]',
    'tests/functional/test_step4_g5_seal_verifier.py::test_run_v12_label_never_sealed_over_v13_text[placeholder]',
    'tests/functional/test_step4_g8_numeric_d73.py::test_run_report_counts_transcriptions_rounded_under_declared_policy',
    'tests/functional/test_step4_g9_spec_claims.py::test_run_sampling_environment_variable_changes_nothing[env0]',
    'tests/functional/test_step4_g9_spec_claims.py::test_run_sampling_environment_variable_changes_nothing[env1]',
    'tests/functional/test_step4_g9_spec_claims.py::test_run_sampling_environment_variable_changes_nothing[env2]',
    'tests/functional/test_step4_g9_spec_claims.py::test_run_with_config_mini_seals_exactly_that_files_settings',
    'tests/unit/execution/test_engine.py::test_execute_item_ev0_causes_are_told_apart',
    'tests/unit/execution/test_engine.py::test_execute_item_later_send_fails_error_state_names_cause_and_round',
    'tests/unit/execution/test_engine.py::test_execute_item_model_controlled_arguments_recorded_no_raise[true-plus]',
    'tests/unit/execution/test_engine.py::test_execute_item_model_controlled_arguments_recorded_no_raise[true-times]',
    'tests/unit/execution/test_engine.py::test_execute_item_refusal_is_executed_not_unmeasured[content-filter]',
    'tests/unit/execution/test_engine.py::test_execute_item_refusal_is_executed_not_unmeasured[refusal]',
    'tests/unit/execution/test_engine.py::test_execute_item_unrecognised_later_response_error_state_names_round',
    'tests/unit/execution/test_evidence_r41.py::test_r41_ev3_rows_are_declared_exceptions_while_ev3_is_not_built',
    'tests/unit/execution/test_seal.py::test_seal_text_input_hash_independent_of_line_endings_and_bom[bom-calculator]',
    'tests/unit/execution/test_seal.py::test_seal_text_input_hash_independent_of_line_endings_and_bom[bom-fixture]',
    'tests/unit/execution/test_seal.py::test_seal_text_input_hash_independent_of_line_endings_and_bom[bom-ground_truth]',
    'tests/unit/execution/test_seal.py::test_seal_text_input_hash_independent_of_line_endings_and_bom[bom-questions]',
    'tests/unit/execution/test_seal.py::test_seal_text_input_hash_independent_of_line_endings_and_bom[bom_crlf-calculator]',
    'tests/unit/execution/test_seal.py::test_seal_text_input_hash_independent_of_line_endings_and_bom[bom_crlf-fixture]',
    'tests/unit/execution/test_seal.py::test_seal_text_input_hash_independent_of_line_endings_and_bom[bom_crlf-ground_truth]',
    'tests/unit/execution/test_seal.py::test_seal_text_input_hash_independent_of_line_endings_and_bom[bom_crlf-questions]',
    'tests/unit/execution/test_version.py::test_source_hash_editing_tests_leaves_it_unchanged[add]',
    'tests/unit/execution/test_version.py::test_source_hash_editing_tests_leaves_it_unchanged[edit]',
    'tests/unit/execution/test_version.py::test_source_hash_editing_tests_leaves_it_unchanged[other-dir]',
    'tests/unit/execution/test_version.py::test_source_hash_editing_tools_leaves_it_unchanged[add]',
    'tests/unit/execution/test_version.py::test_source_hash_editing_tools_leaves_it_unchanged[edit]',
    'tests/unit/execution/test_version.py::test_source_hash_editing_version_file_changes_it',
    'tests/unit/execution/test_version.py::test_source_hash_scratch_file_outside_package_leaves_it_unchanged',
    'tests/unit/execution/test_version.py::test_source_hash_venv_inside_clone_leaves_it_unchanged[.venv]',
    'tests/unit/execution/test_version.py::test_source_hash_venv_inside_clone_leaves_it_unchanged[venv]',
    'tests/unit/foundation/test_config.py::test_load_config_example_config_mini_is_the_mini_runs_config',
    'tests/unit/foundation/test_config.py::test_minimum_n_minimum_named_is_the_declared_versions[D5-5-20]',
    'tests/unit/foundation/test_config.py::test_minimum_n_minimum_named_is_the_declared_versions[D6-1-10]',
    'tests/unit/foundation/test_numeric.py::test_arabic_indic_and_full_width_three_neither_parse_nor_extract',
    'tests/unit/foundation/test_numeric.py::test_extract_non_ascii_digits_are_not_tokens',
    'tests/unit/foundation/test_numeric.py::test_parse_decimal_refuses_non_ascii_digits[arabic-indic-12]',
    'tests/unit/foundation/test_numeric.py::test_parse_decimal_refuses_non_ascii_digits[arabic-indic-3]',
    'tests/unit/foundation/test_numeric.py::test_parse_decimal_refuses_non_ascii_digits[ascii-then-arabic-indic]',
    'tests/unit/foundation/test_numeric.py::test_parse_decimal_refuses_non_ascii_digits[currency-percent-around]',
    'tests/unit/foundation/test_numeric.py::test_parse_decimal_refuses_non_ascii_digits[devanagari-point-5]',
    'tests/unit/foundation/test_numeric.py::test_parse_decimal_refuses_non_ascii_digits[full-width-3]',
    'tests/unit/foundation/test_numeric.py::test_parse_decimal_refuses_non_ascii_digits[full-width-grouped]',
    'tests/unit/reporting/test_adjudication.py::test_sheet_key_joins_every_sheet_back_to_its_arm',
    'tests/unit/reporting/test_adjudication.py::test_sheet_refusal_shows_text_and_provisional_outcome[content-filter]',
    'tests/unit/reporting/test_adjudication.py::test_sheet_refusal_shows_text_and_provisional_outcome[refusal]',
    'tests/unit/reporting/test_adjudication.py::test_sheets_order_is_seeded_and_does_not_follow_the_arm',
    'tests/unit/reporting/test_report.py::test_clopper_pearson_section_lists_failing_questions_beside_k',
    'tests/unit/reporting/test_report.py::test_d73_reports_count_of_exact_rounded_under_declared_policy',
    'tests/unit/reporting/test_report.py::test_dimension_results_d1_per_category_with_n_and_interval',
    'tests/unit/runner/test_console.py::test_run_report_3h_lists_failing_questions_with_counts',
    'tests/unit/runner/test_console.py::test_run_report_3h_rate_counts_questions_not_repeats',
    'tests/unit/runner/test_console.py::test_run_report_section_3h2_heading_starts_after_a_blank_line',
    'tests/unit/runner/test_executions.py::test_apply_question_measurability_reassigns_section_6_8_outcome',
    'tests/unit/runner/test_executions.py::test_score_execution_refusal_routed_provisional_out_of_d1[content-filter]',
    'tests/unit/runner/test_executions.py::test_score_execution_refusal_routed_provisional_out_of_d1[refusal]',
    'tests/unit/runner/test_executions.py::test_score_execution_transcription_result_carries_rounded_flag',
    'tests/unit/runner/test_outputs.py::test_write_outputs_sheets_show_measurability_per_question',
    'tests/unit/runner/test_summary.py::test_summary_d71_figure_lists_failing_questions_with_counts',
    'tests/unit/runner/test_summary.py::test_summary_d71_n_counts_questions_not_repeats',
    'tests/unit/runner/test_summary.py::test_summary_refusal_after_calculator_calls_is_out_of_d71[content-filter]',
    'tests/unit/runner/test_summary.py::test_summary_refusal_after_calculator_calls_is_out_of_d71[refusal]',
    'tests/unit/runner/test_summary.py::test_summary_refusal_is_out_of_d71_and_counted_adjudicated[content-filter]',
    'tests/unit/runner/test_summary.py::test_summary_refusal_is_out_of_d71_and_counted_adjudicated[refusal]',
    'tests/unit/scoring/provenance/test_classify.py::test_classify_invocation_unknown_name_after_a_grounded_call_is_unobservable',
    'tests/unit/scoring/provenance/test_classify.py::test_classify_invocation_unknown_name_is_unobservable_with_reason',
    'tests/unit/scoring/provenance/test_classify.py::test_mark_unmeasurable_questions_mixed_executions_all_unmeasurable',
    'tests/unit/scoring/provenance/test_classify.py::test_sequential_unreadable_expression_operands_unobservable[true-plus]',
    'tests/unit/scoring/provenance/test_classify.py::test_sequential_unreadable_expression_operands_unobservable[true-times]',
    'tests/unit/scoring/provenance/test_trace.py::test_extract_operands_boolean_literal_not_an_operand_no_raise',
    'tests/unit/scoring/test_answer_outcome.py::test_match_with_any_originated_call_is_originated[grounded-then-originated]',
    'tests/unit/scoring/test_answer_outcome.py::test_match_with_any_originated_call_is_originated[originated-then-grounded]',
    'tests/unit/scoring/test_answer_outcome.py::test_match_with_any_originated_call_is_originated[originated-then-unobservable]',
    'tests/unit/scoring/test_answer_outcome.py::test_refusal_outcome_is_provisional_and_routed[content-filter]',
    'tests/unit/scoring/test_answer_outcome.py::test_refusal_outcome_is_provisional_and_routed[refusal]',
    'tests/unit/scoring/test_figure_id.py::test_identify_figure_matching_non_final_token_is_not_auto_matched',
    'tests/unit/scoring/test_invocation.py::test_format_failing_questions_two_question_failure_case',
    'tests/unit/scoring/test_invocation.py::test_measure_invocation_lists_each_failing_question_with_its_counts',
    'tests/unit/scoring/test_invocation.py::test_measure_invocation_n_counts_questions_not_repeats',
    'tests/unit/scoring/test_invocation.py::test_measure_invocation_question_with_a_repeat_not_invoked_is_a_failure',
    'tests/unit/scoring/test_operation_correctness.py::test_reclassify_session_unreadable_expression_kept_no_raise[bool-literal]',
    'tests/unit/scoring/test_transcription.py::test_transcription_exact_match_is_flagged_not_rounded',
    'tests/unit/scoring/test_transcription.py::test_transcription_licensed_rounding_is_exact_and_flagged_rounded',
    'tests/unit/tools/test_verify_run_seal.py::test_verify_run_makes_no_check_against_on_disk_configs',
    'tests/unit/tools/test_verify_run_seal.py::test_verify_run_same_text_other_line_endings_verifies[bom-crlf]',
    'tests/unit/tools/test_verify_run_seal.py::test_verify_run_same_text_other_line_endings_verifies[bom]',
)
EXPECTED_PROVISIONAL_CASES = {
    'tests/unit/reporting/test_adjudication.py': 4,
    'tests/unit/reporting/test_report.py': 17,
    'tests/unit/runner/test_console.py': 6,
    'tests/unit/runner/test_summary.py': 4,
    'tests/unit/scoring/provenance/test_classify.py': 2,
    'tests/unit/scoring/provenance/test_trace.py': 4,
    'tests/unit/scoring/test_operation_correctness.py': 112,
    'tests/unit/scoring/test_release_coverage.py': 34,
}
MIN_STRICT_XFAIL_CASES = 139


@pytest.fixture(scope='module')
def collected(tmp_path_factory):
    dump = tmp_path_factory.mktemp('marks') / 'marks.json'
    env = dict(os.environ, AP1_MARKS_DUMP=str(dump),
               PYTHONPATH=os.pathsep.join(
                   [str(ROOT / 'tests' / 'conformance'), str(ROOT / 'src'),
                    os.environ.get('PYTHONPATH', '')]))
    result = subprocess.run(
        [sys.executable, '-B', '-m', 'pytest', '--collect-only', '-q',
         '-p', 'no:cacheprovider', '-p', 'marks_plugin'],
        cwd=ROOT, env=env, capture_output=True, text=True)
    assert dump.exists(), result.stdout[-2000:] + result.stderr[-2000:]
    return json.loads(dump.read_text('utf-8'))


def test_marks_collection_covers_the_suite(collected):
    strict = [t for t in collected if t['strict_xfail']]
    assert len(strict) >= MIN_STRICT_XFAIL_CASES, len(strict)


def test_proposal_marks_are_the_expected_inventory(collected):
    found = sorted(t['nodeid'] for t in collected if t['proposal'])
    expected = sorted(EXPECTED_PROPOSAL_CASES)
    assert (sorted(set(found) - set(expected)),
            sorted(set(expected) - set(found))) == ([], [])


def test_provisional_marks_are_the_expected_inventory(collected):
    found = {}
    for t in collected:
        if t['provisional']:
            path = t['nodeid'].split('::')[0]
            found[path] = found.get(path, 0) + 1
    assert found == EXPECTED_PROVISIONAL_CASES


def test_provisional_marks_have_a_dec5_reason_and_no_strict_xfail(collected):
    bad = []
    for t in collected:
        for mark in t['provisional']:
            args = mark['args']
            # DEC-5: a module without a SPEC section, the code its
            # provisional definition
            if (len(args) != 1 or not isinstance(args[0], str)
                    or not args[0].startswith('DEC-5')):
                bad.append((t['nodeid'], 'reason'))
        if t['provisional'] and t['strict_xfail']:
            bad.append((t['nodeid'], 'provisional strict xfail'))
    assert bad == []


def test_proposal_marks_have_a_reason_and_a_finding(collected):
    bad = []
    for t in collected:
        for mark in t['proposal']:
            args = mark['args']
            if (len(args) != 1 or not isinstance(args[0], str)
                    or not args[0].strip() or mark['kwargs']):
                bad.append((t['nodeid'], 'reason'))
        if t['proposal'] and not t['finding']:
            bad.append((t['nodeid'], 'no finding mark'))
    assert bad == []


def test_strict_xfails_name_their_finding(collected):
    bad = [t['nodeid'] for t in collected
           if t['strict_xfail'] and not t['finding']]
    assert bad == []
