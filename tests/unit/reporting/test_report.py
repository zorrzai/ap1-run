"""Unit tests for the report generator (R3.3): each section of report.md
rendered from a small summary, and how generate_report puts them together.

Expected text is written as the list of lines the section joins with
newlines, so a test reads like the markdown it pins.
"""

import decimal
import json
import math
import re
from decimal import Decimal

import pytest

from ap1_run.reporting import report
from ap1_run.reporting.report import (
    ALL_DIMENSIONS, clopper_pearson_upper_k0, generate_report,
)


# DEC-5: D7.2(b) operation correctness, release coverage and sign inversion
# have no SPEC section, so the tests below that show their results are
# provisional (the code is the definition for now). Strict xfails are not.
PROVISIONAL = pytest.mark.provisional(
    'DEC-5: shows D7.2(b) operation-correctness, release-coverage or '
    'sign-inversion results; the code is the provisional definition')


def md(*lines):
    return '\n'.join(lines)


CONFIG = {'ap1_version': '1.3', 'ap1_version_doi': '10.5281/zenodo.1',
          'model': 'test-model', 'dimensions_claimed': ['D1', 'D2', 'D7']}


# -- Constants ------------------------------------------------------------

def test_all_dimensions_are_d1_to_d7_in_order():
    assert ALL_DIMENSIONS == ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']


# -- clopper_pearson_upper_k0 ---------------------------------------------

@pytest.mark.finding('T3-61')
def test_clopper_pearson_k0_is_one_minus_alpha_to_one_over_n():
    # T3-61: in Decimal (SPEC R0.4.1), the one implementation in
    # invocation.py.
    from ap1_run.foundation.numeric import DECIMAL_CONTEXT
    with decimal.localcontext(DECIMAL_CONTEXT):
        assert clopper_pearson_upper_k0(10, 0.05) == \
            1 - Decimal('0.05') ** (Decimal(1) / 10)
    assert abs(clopper_pearson_upper_k0(10, 0.05) - Decimal('0.25887')) < \
        Decimal('1e-5')


def test_clopper_pearson_k0_default_alpha_is_five_percent():
    assert clopper_pearson_upper_k0(20) == clopper_pearson_upper_k0(20, 0.05)


@pytest.mark.finding('T3-61')
def test_clopper_pearson_k0_n1_is_one_minus_alpha():
    # A float alpha is read from its text, never used as a binary float.
    assert clopper_pearson_upper_k0(1, 0.1) == Decimal('0.9')
    assert clopper_pearson_upper_k0(1, Decimal('0.1')) == Decimal('0.9')


@pytest.mark.parametrize('n', [0, -1])
def test_clopper_pearson_k0_n_not_positive_is_nan(n):
    assert math.isnan(clopper_pearson_upper_k0(n))


# -- generate_report: header and section order ----------------------------

@pytest.mark.finding('T3-45')
def test_report_header_names_version_doi_and_model():
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    assert re.match(
        r'# AP-1 Evaluation Report\n\n'
        r'Generated: \d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+\+00:00\n\n'
        r'AP-1 Version: 1\.3\n\n'
        r'Version DOI: 10\.5281/zenodo\.1\n\n'
        r'Model: test-model\n\n'
        r'> \*\*Demonstration run, not a conformance result\.\*\* .*\n\n'
        r'---\n\n'
        r'## 1\. Pre-Registration Record\n', text)


def test_report_header_missing_fields_read_unknown():
    text = generate_report(summary={}, config={}, seal_record={})
    assert 'AP-1 Version: unknown\n' in text
    assert 'Version DOI: unknown\n' in text
    assert 'Model: unknown\n' in text


@pytest.mark.finding('T3-45')
def test_report_header_carries_the_readme_statement():
    # Fixed (T3-45): the README's statement, before the first section.
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    head = text[:text.index('## 1.')]
    assert report.DEMONSTRATION_STATEMENT == (
        '> **Demonstration run, not a conformance result.** ap1-run '
        'implements the AP-1 v1.3 Draft for Comment; v1.2 remains the '
        'version in force. A run of this instrument is a demonstration '
        'run, not a conformance result under either version (README, '
        '"Which version of AP-1").\n')
    assert '\n' + report.DEMONSTRATION_STATEMENT + '\n---\n' in head


def test_report_sections_in_order():
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    headings = re.findall(r'^## (.*)$', text, flags=re.M)
    assert headings == [
        '1. Pre-Registration Record',
        '2. Resolved Configuration',
        '3. Per-Dimension Results',
        '4. D7 Figures by Evidence Class',
        'D7.3 Transcription Fidelity',
        '5. Invocation Figures with Confidence Bounds',
        '6. D7.2(a) Originated-Operand Audit',
        '7. D7.2(b) Operation Correctness',
        '7b. D7.2(a) Operand Provenance Step Counts',
        '8. Scoring Proportions',
        '9. D2 Reproducibility Mechanism Classes',
        '9b. D2.2 Execution Conditions',
        '10. Non-Outcome Cells',
        '11. Quantisation and Near-Miss Findings',
        '12. Unmeasured Dimensions Declaration',
        '13. Declared Limitations',
    ]


def test_report_is_header_and_sections_joined_by_newlines():
    summary = {'evidence_class_counts': {'EV-2': 1}}
    seal = {'seal_hash': 'abc'}
    text = generate_report(summary=summary, config=CONFIG, seal_record=seal,
                           transcript_records=[
                               {'item_id': 'Q09', 'condition': 'base',
                                'error_state': 'VOID: x'}])
    body = text[text.index('---\n') + len('---\n') + 1:]
    assert body == md(
        report._section_preregistration(seal),
        report._section_configuration(CONFIG),
        report._section_dimension_results(summary, CONFIG),
        report._section_d7_figures(summary),
        report._section_d73(summary),
        report._section_clopper_pearson(summary),
        report._section_condition_contrast(summary),
        report._section_d72a_audit(summary),
        report._section_d72b_counts(summary),
        report._section_operand_provenance(summary),
        report._section_scoring_proportions(summary),
        report._section_d2_mechanisms(summary),
        report._section_d2_conditions(summary, CONFIG),
        report._section_unmeasured_cells({}, [
            {'item_id': 'Q09', 'condition': 'base',
             'error_state': 'VOID: x'}]),
        report._section_quantisation(summary),
        report._section_unmeasured_dimensions(CONFIG),
        report._section_declared_limitations(),
    )


@pytest.mark.finding('T3-46')
@pytest.mark.req('AP-1 D7.8', 'R2.3')
def test_condition_contrast_states_held_constant_and_dpr():
    summary = {'held_constant': ['tool declarations', 'sampling parameters'],
               'dpr': '100.0%'}
    assert report._section_condition_contrast(summary) == (
        '### 5a. Instruction-Removal Contrast (D7.8)\n\n'
        'Held constant between base and instruction_removed (compared '
        'before execution, R1.2): tool declarations, sampling parameters. '
        'Varied: the system prompt only.\n\n'
        'DPR (drop-in-performance ratio, (I_base - I_removed) / I_base): '
        '100.0%\n')


@pytest.mark.finding('T3-46')
@pytest.mark.parametrize('summary', [{}, {'held_constant': []}])
def test_condition_contrast_without_a_record(summary):
    assert report._section_condition_contrast(summary) == (
        '### 5a. Instruction-Removal Contrast (D7.8)\n\n'
        'Held constant between base and instruction_removed: not '
        'recorded.\n\n'
        'DPR (drop-in-performance ratio, (I_base - I_removed) / I_base): '
        'not computed\n')


def test_report_passes_transcript_records_to_non_outcome_cells():
    text = generate_report(summary={}, config=CONFIG, seal_record={},
                           transcript_records=[
                               {'item_id': 'Q09', 'condition': 'base',
                                'error_state': 'VOID: perturbed'}])
    assert '| Q09 | base | VOID | VOID: perturbed |' in text


def test_report_without_transcript_records_lists_summary_cells_only():
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    assert '*No non-outcome cells.*' in text


# -- 1. Pre-registration --------------------------------------------------

def test_preregistration_lists_seal_fields_sorted():
    assert report._section_preregistration(
        {'seal_hash': 'abc', 'ap1_version': '1.3', 'keys': []}) == md(
        '## 1. Pre-Registration Record\n',
        '| Field | Value |',
        '|---|---|',
        '| `ap1_version` | `1.3` |',
        '| `keys` | `[]` |',
        '| `seal_hash` | `abc` |',
        '')


@pytest.mark.finding('T3-21')
def test_preregistration_names_the_transcript_scored():
    text = report._section_preregistration(
        {'seal_hash': 'h'}, {'sha256': 'ab' * 32, 'records': 7})
    assert text.endswith(
        f'Transcript scored: SHA-256 `{"ab" * 32}`, 7 records.\n')
    assert 'Transcript scored' not in report._section_preregistration(
        {'seal_hash': 'h'})


@pytest.mark.finding('T3-21')
def test_preregistration_of_a_re_score_says_so_and_names_both_runners():
    rescore = {
        'rescored_at': '2026-11-05T12:00:00+00:00',
        'run': {'seal_hash': 'h', 'runner_source_hash': 'a' * 64,
                'runner_version_tag': 'v1', 'runner_version_commit': 'c1',
                'runner_modified': False},
        'scorer': {'runner_source_hash': 'b' * 64,
                   'runner_version_tag': 'v2', 'runner_version_commit': 'c2',
                   'runner_modified': True}}
    text = report._section_preregistration({'seal_hash': 'h'}, None,
                                           rescore)
    assert ('**Re-scored** on 2026-11-05T12:00:00+00:00: the figures in '
            'this report were computed by a re-score of the run\'s '
            'transcript, not by the run.') in text
    assert ('| the run (sealed) | `v1` | `c1` | `False` | `' + 'a' * 64
            + '` |') in text
    assert ('| the scorer | `v2` | `c2` | `True` | `' + 'b' * 64
            + '` |') in text
    assert 'Re-scored' not in report._section_preregistration(
        {'seal_hash': 'h'})


def test_preregistration_without_seal_says_so():
    assert report._section_preregistration({}) == md(
        '## 1. Pre-Registration Record\n',
        '*No seal record available.*',
        '')
    assert report._section_preregistration(None) == \
        report._section_preregistration({})


# -- 2. Configuration -----------------------------------------------------

def test_configuration_is_sorted_indented_json_with_decimals_as_strings():
    config = {'b': Decimal('0.01'), 'a': {'z': 'caf\u00e9', 'y': [1, 2]}}
    assert report._section_configuration(config) == md(
        '## 2. Resolved Configuration\n',
        '```json',
        '{',
        '  "a": {',
        '    "y": [',
        '      1,',
        '      2',
        '    ],',
        '    "z": "caf\u00e9"',
        '  },',
        '  "b": "0.01"',
        '}',
        '```\n')


def test_make_json_safe_converts_decimals_recursively():
    out = report._make_json_safe(
        {'a': Decimal('1.50'), 'b': [Decimal('2'), ('x', Decimal('3'))],
         'c': None, 'd': 4.5})
    assert out == {'a': '1.50', 'b': ['2', ['x', '3']], 'c': None, 'd': 4.5}
    assert isinstance(out['b'][1], list)
    json.dumps(out)


def test_make_json_safe_leaves_other_values():
    obj = object()
    assert report._make_json_safe(obj) is obj
    assert report._make_json_safe('s') == 's'


# -- 3. Per-dimension results ---------------------------------------------

def dim_rows(text):
    return [line for line in text.split('\n')
            if re.match(r'\| D\d \|', line)]


def test_dimension_results_table_layout():
    text = report._section_dimension_results({}, {'dimensions_claimed': []})
    assert text == md(
        '## 3. Per-Dimension Results\n',
        '| Dimension | Status | n | Result |',
        '|---|---|---|---|',
        '| D1 | not claimed | \u2014 | not claimed in this configuration '
        '(the runner auto-scores it) (\u00a712) |',
        '| D2 | not claimed | \u2014 | not claimed in this configuration '
        '(the runner measures it from repeated runs) (\u00a712) |',
        '| D3 | not claimed | \u2014 | requires human adjudication; the '
        'runner does not measure it (\u00a712) |',
        '| D4 | not claimed | \u2014 | requires human adjudication; the '
        'runner does not measure it (\u00a712) |',
        '| D5 | not claimed | \u2014 | requires human adjudication; the '
        'runner does not measure it (\u00a712) |',
        '| D6 | not claimed | \u2014 | requires human adjudication; the '
        'runner does not measure it (\u00a712) |',
        '| D7 | not claimed | \u2014 | not claimed in this configuration '
        '(the runner measures D7.1-D7.3 from tool-call evidence) '
        '(\u00a712) |',
        '')


@pytest.mark.req('R3.3')
def test_dimension_results_unclaimed_d1_reads_not_claimed():
    # A dimension the configuration doesn't claim is a choice, not a
    # gap: section 3 says "not claimed", in section 12's words, and
    # keeps "NOT MEASURED" for a claimed dimension that wasn't measured
    config = {'dimensions_claimed': ['D2', 'D7']}
    text = report._section_dimension_results({}, config)
    d1 = [row for row in dim_rows(text) if row.startswith('| D1 |')]
    assert d1 == ['| D1 | not claimed | \u2014 | not claimed in this '
                  'configuration (the runner auto-scores it) (\u00a712) |']
    assert '**NOT MEASURED**' not in d1[0]
    twelve = report._section_unmeasured_dimensions(config)
    assert ('- **D1**: Accuracy \u2014 not claimed in this configuration '
            '(the runner auto-scores it)') in twelve
    # Claimed, with no results: not "not claimed"
    claimed = report._section_dimension_results(
        {}, {'dimensions_claimed': ['D1']})
    assert '| D1 | Claimed but no results |' in claimed


def test_dimension_results_without_claim_list_none_measured():
    assert report._section_dimension_results({}, {}) == \
        report._section_dimension_results({}, {'dimensions_claimed': []})


def test_dimension_results_claimed_without_data_says_so():
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': {}}, {'dimensions_claimed': ['D1']}))
    assert rows[0] == '| D1 | Claimed but no results | \u2014 | \u2014 |'


@pytest.mark.finding('T3-3')
def test_dimension_results_d1_pending_adjudication_states_counts_not_rate():
    # T3-3 (fixed): with 3 items awaiting adjudication the row gives the
    # counts, not the auto-scored rate (which would leave out every wrong
    # figure, SPEC R2.0).
    d1 = {'n': 10, 'auto_scored_n': 7, 'adjudicated_n': 2,
          'unmeasurable_n': 1, 'accuracy_rate': Decimal('5') / 6,
          'correct': 5, 'incorrect': 1, 'no_figure': 1}
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': d1}, {'dimensions_claimed': ['D1']}))
    assert rows[0] == ('| D1 | Measured | 10 | No rate: 3 items await '
                       'adjudication (base condition only; auto-scored 7: '
                       '5 correct, 1 incorrect, 1 no figure) |')


def test_dimension_results_d1_pending_counts_default_to_zero():
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': {'n': 1, 'adjudicated_n': 1, 'accuracy_rate': 1}},
        {'dimensions_claimed': ['D1']}))
    assert rows[0] == ('| D1 | Measured | 1 | No rate: 1 items await '
                       'adjudication (base condition only; auto-scored 0: '
                       '0 correct, 0 incorrect, 0 no figure) |')


def test_dimension_results_d1_n_falls_back_to_auto_scored_n():
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': {'auto_scored_n': 7, 'accuracy_rate': '0.9'}},
        {'dimensions_claimed': ['D1']}))
    assert rows[0] == ('| D1 | Measured | 7 | Accuracy: 0.9 '
                       '(base condition only; auto-scored 7; '
                       '0 adjudicated not in rate) |')


def test_dimension_results_d1_without_rate_says_so():
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': {'n': 4, 'accuracy_rate': None}},
        {'dimensions_claimed': ['D1']}))
    assert rows[0] == '| D1 | Measured | 4 | No rate computed |'


def test_dimension_results_d1_rate_zero_is_printed():
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': {'n': 4, 'accuracy_rate': 0}},
        {'dimensions_claimed': ['D1']}))
    assert rows[0] == ('| D1 | Measured | 4 | Accuracy: 0 '
                       '(base condition only; auto-scored 0; '
                       '0 adjudicated not in rate) |')


EV0 = 'EV-0 UNOBSERVABLE'
EV1 = 'EV-1 SELF-REPORTED'
EV2 = 'EV-2 PLATFORM-STRUCTURAL'


def d7_summary(arms, prov=None, ops=None, transcription=(), by_class=None,
               n=40, cells=(), seen=None, ev_counts=None):
    """A summary with what D7.1-D7.3 computed. arms: {condition: [(class,
    executions, questions in n, unobservable executions)]}; prov and ops:
    the D7.2(a) and (b) outcome counts; transcription: D7.3 outcomes."""
    figures, evidence = {}, {}
    for cond, classes in arms.items():
        evidence[cond] = {'classes': {
            ec: {'executions': e, 'questions': max(q, 1),
                 'observed_questions': q, 'unobservable_executions': u}
            for ec, e, q, u in classes}, 'cross_class_warning': None}
        observed = [(ec, q) for ec, _, q, _ in classes if q]
        for ec, q in observed or [(None, 0)]:
            key = f'd7_invocation_{cond}' + (
                f' ({ec})' if len(observed) > 1 else '')
            figures[key] = {'failures': 0, 'n': q, 'condition': cond,
                            'evidence_class': ec}
    return {'d7_results': {'n': n},
            'invocation_figures': figures, 'invocation_evidence': evidence,
            'provenance_outcomes': prov or {},
            'operation_correctness_counts': ops or {},
            'transcription_results': [
                {'item_id': f'Q{i:02d}', 'condition': 'base', 'repeat': i,
                 'outcome': o} for i, o in enumerate(transcription, 1)],
            'd7_outcomes_by_class': by_class or {},
            'non_outcome_cells': [
                {'item_id': i, 'condition': c, 'repeat': r, 'status': st}
                for i, c, r, st in cells],
            'item_evidence': [
                {'item_id': i, 'condition': c, 'evidence_class': ec,
                 'invocation_outcome': o} for i, c, ec, o in seen or ()],
            'evidence_class_counts': ev_counts or {}}


def d7_rows(summary):
    text = report._section_dimension_results(summary,
                                             {'dimensions_claimed': ['D7']})
    return [line for line in text.split('\n') if line.startswith('| D7')]


# Every part of D7.1-D7.3 measured, on one evidence class
MEASURED_D7 = d7_summary(
    {'base': [(EV2, 20, 10, 0)], 'instruction_removed': [(EV2, 20, 10, 0)]},
    prov={'OPERANDS-GROUNDED': 40}, ops={'OPERATION-CORRECT': 40},
    transcription=['TRANSCRIBED-EXACT'] * 40,
    by_class={'D7.2(a)': {EV2: {'OPERANDS-GROUNDED': 40}},
              'D7.2(b)': {EV2: {'OPERATION-CORRECT': 40}},
              'D7.3': {EV2: {'TRANSCRIBED-EXACT': 40}}})


@pytest.mark.finding('T3-29')
def test_dimension_results_d7_reported_per_sub_dimension():
    # Fixed (T3-29; AP-1 v1.3 D7 "Report all four"): D7.1-D7.4 each have
    # a row; D7.4 is not measured; each other part's status follows from
    # what was computed for it.
    text = report._section_dimension_results(
        MEASURED_D7, {'dimensions_claimed': ['D7']})
    assert text.split('\n')[-6:] == [
        '| D7 | Partly measured | 40 | D7.1 measured, D7.2 measured, D7.3 '
        'measured; D7.4 not measured (\u00a712) |',
        '| D7.1 | Measured | see \u00a75 | Invocation rate per condition '
        '(\u00a75): base measured (n = 10, EV-2 PLATFORM-STRUCTURAL); '
        'instruction_removed measured (n = 10, EV-2 PLATFORM-STRUCTURAL) |',
        '| D7.2 | Measured | see \u00a76-7b | (a) operand provenance '
        'measured: 40 calls (\u00a76, \u00a77b); (b) operation correctness '
        'measured: 40 operations (\u00a77) |',
        '| D7.3 | Measured | 40 | Transcription fidelity (D7.3 section): '
        'measured: 40 executions |',
        '| D7.4 | **NOT MEASURED** | \u2014 | Invocation under pressure '
        '(\u00a712) |',
        '']
    assert len(dim_rows(text)) == 7


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7', 'R3.3')
def test_dimension_results_d7_parts_follow_each_arm_and_class():
    # The unrecognised-shape run: base has 6 EV-0 executions beside 14
    # EV-2, and instruction_removed has no observed outcome at all; the
    # report said "D7.1 | Measured" beside "D7.1 is not measured" in §5.
    rows = d7_rows(d7_summary(
        {'base': [(EV0, 6, 0, 6), (EV2, 14, 7, 0)],
         'instruction_removed': [(EV0, 20, 0, 20)]},
        prov={'OPERANDS-GROUNDED': 20}, ops={'OPERATION-CORRECT': 20},
        transcription=['TRANSCRIBED-EXACT'] * 14 + ['UNOBSERVABLE'] * 26,
        by_class={'D7.2(a)': {EV0: {'OPERANDS-GROUNDED': 6},
                              EV2: {'OPERANDS-GROUNDED': 14}},
                  'D7.2(b)': {EV0: {'OPERATION-CORRECT': 6},
                              EV2: {'OPERATION-CORRECT': 14}},
                  'D7.3': {EV0: {'UNOBSERVABLE': 26},
                           EV2: {'TRANSCRIBED-EXACT': 14}}}))
    assert rows[:4] == [
        '| D7 | Partly measured | 40 | D7.1 partly measured, D7.2 '
        'measured, D7.3 partly measured; D7.4 not measured (\u00a712) |',
        '| D7.1 | Partly measured | see \u00a75 | Invocation rate per '
        'condition (\u00a75): base partly measured (n = 7, EV-2 '
        'PLATFORM-STRUCTURAL; 6 of 20 executions UNOBSERVABLE); '
        'instruction_removed not measured (no observed outcome; 20 of 20 '
        'executions UNOBSERVABLE) |',
        '| D7.2 | Measured | see \u00a76-7b | (a) operand provenance '
        'measured: 20 calls (\u00a76, \u00a77b); (b) operation correctness '
        'measured: 20 operations (\u00a77); on 2 evidence classes, not '
        'comparable (per class: \u00a77, \u00a77b) |',
        '| D7.3 | Partly measured | 40 | Transcription fidelity (D7.3 '
        'section): partly measured: 26 of 40 executions UNOBSERVABLE; on 2 '
        'evidence classes, not comparable (per class: D7.3 section) |']


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7', 'R3.3')
def test_dimension_results_d72_partly_or_not_measured_by_its_counts():
    # The malformed-calls run: 12 of 44 calls OPERANDS-UNOBSERVABLE and 16
    # of 44 operations OPERATION-UNOBSERVABLE, labelled "Measured".
    arms = {'base': [(EV2, 20, 10, 0)],
            'instruction_removed': [(EV2, 20, 10, 0)]}
    partly = d7_rows(d7_summary(
        arms, prov={'OPERANDS-GROUNDED': 32, 'OPERANDS-UNOBSERVABLE': 12},
        ops={'OPERATION-CORRECT': 28, 'OPERATION-UNOBSERVABLE': 16},
        transcription=['TRANSCRIBED-EXACT'] * 40))[2]
    assert partly == (
        '| D7.2 | Partly measured | see \u00a76-7b | (a) operand provenance '
        'partly measured: 12 of 44 calls OPERANDS-UNOBSERVABLE or '
        'UNMEASURABLE (\u00a76, \u00a77b); (b) operation correctness '
        'partly measured: 16 of 44 operations OPERATION-UNOBSERVABLE '
        '(\u00a77) |')
    # Every call unreadable: not measured, (a) and (b)
    none_read = d7_rows(d7_summary(
        arms, prov={'OPERANDS-UNOBSERVABLE': 3, 'UNMEASURABLE': 1},
        ops={'OPERATION-UNOBSERVABLE': 4}))[2]
    assert none_read == (
        '| D7.2 | **NOT MEASURED** | see \u00a76-7b | (a) operand provenance '
        'not measured: all 4 calls OPERANDS-UNOBSERVABLE or UNMEASURABLE '
        '(\u00a76, \u00a77b); (b) operation correctness not measured: all 4 '
        'operations OPERATION-UNOBSERVABLE (\u00a77) |')
    # (a) read, (b) not: partly
    assert d7_rows(d7_summary(
        arms, prov={'OPERANDS-GROUNDED': 2},
        ops={'OPERATION-UNOBSERVABLE': 2}))[2].startswith(
            '| D7.2 | Partly measured |')


def transport_errors_summary():
    """The transport-errors run: base Q03, Q04, Q06 r1 and Q05, Q08 r1, r2
    UNMEASURED, Q07 r1 EV-0; instruction_removed Q08 r1, r2 UNMEASURED
    (HTTP 401)."""
    cells = [('Q03', 'base', 1, 'UNMEASURED'), ('Q04', 'base', 1,
                                                 'UNMEASURED'),
             ('Q05', 'base', 1, 'UNMEASURED'), ('Q05', 'base', 2,
                                                 'UNMEASURED'),
             ('Q06', 'base', 1, 'UNMEASURED'),
             ('Q08', 'base', 1, 'UNMEASURED'), ('Q08', 'base', 2,
                                                 'UNMEASURED'),
             ('Q08', 'instruction_removed', 1, 'UNMEASURED'),
             ('Q08', 'instruction_removed', 2, 'UNMEASURED'),
             ('Q00', 'base', 0, 'VOID')]
    evidence = [(f'Q{i:02d}', 'instruction_removed', EV2, 'INVOKED')
                for i in range(1, 11) if i != 8 for _ in (1, 2)]
    evidence += [(f'Q{i:02d}', 'base', EV2, 'INVOKED')
                 for i in (1, 2, 9, 10) for _ in (1, 2)]
    evidence += [(f'Q{i:02d}', 'base', EV2, 'INVOKED') for i in (3, 4, 6, 7)]
    evidence += [('Q07', 'base', EV0, None)]
    return d7_summary(
        {'base': [(EV0, 1, 0, 1), (EV2, 12, 8, 0)],
         'instruction_removed': [(EV2, 18, 9, 0)]},
        prov={'OPERANDS-GROUNDED': 31}, ops={'OPERATION-CORRECT': 31},
        transcription=['TRANSCRIBED-EXACT'] * 30 + ['UNOBSERVABLE'],
        cells=cells, seen=evidence,
        ev_counts={EV0: 1, EV2: 30})


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7', 'R3.3')
def test_dimension_results_d7_counts_executions_never_observed():
    # A question lost to transport failures left "instruction_removed
    # measured (n = 9)" beside §10's two UNMEASURED Q08 cells. An arm is
    # measured only if every computable execution of it was observed.
    rows = d7_rows(transport_errors_summary())
    assert rows[1] == (
        '| D7.1 | Partly measured | see \u00a75 | Invocation rate per '
        'condition (\u00a75): base partly measured (n = 8, EV-2 '
        'PLATFORM-STRUCTURAL; 1 of 13 executions UNOBSERVABLE; 7 '
        'executions UNMEASURED or not run; 2 of 10 computable questions '
        'not in n); instruction_removed partly measured (n = 9, EV-2 '
        'PLATFORM-STRUCTURAL; 2 executions UNMEASURED or not run; 1 of 10 '
        'computable questions not in n) |')
    assert rows[2].startswith(
        '| D7.2 | Partly measured | see \u00a76-7b | (a) operand provenance '
        'measured: 31 calls (\u00a76, \u00a77b); (b) operation correctness '
        'measured: 31 operations (\u00a77); call inventory incomplete for '
        '10 executions (1 EV-0 UNOBSERVABLE, 9 UNMEASURED or not run)')
    assert rows[3].startswith(
        '| D7.3 | Partly measured | 31 | Transcription fidelity (D7.3 '
        'section): partly measured: 1 of 31 executions UNOBSERVABLE; 9 '
        'executions UNMEASURED or not run')
    s12 = report._section_unmeasured_dimensions(CONFIG,
                                                transport_errors_summary())
    assert ('instruction_removed partly measured (n = 9, EV-2 '
            'PLATFORM-STRUCTURAL; 2 executions UNMEASURED or not run; 1 of '
            '10 computable questions not in n)') in s12
    assert ('- **D7.2**: Computation correctness \u2014 partly measured: '
            'call inventory incomplete for 10 executions (1 EV-0 '
            'UNOBSERVABLE, 9 UNMEASURED or not run)') in s12


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7', 'AP-1 D7.7', 'R3.3')
def test_dimension_results_d72_partly_measured_with_unreadable_inventory():
    # One execution with a readable, grounded, correct call; another of
    # an unrecognised shape (EV-0) whose calls were never seen. The
    # counts hold only the first call; D7.2 is not fully measured.
    summary = d7_summary(
        {'base': [(EV2, 1, 1, 0), (EV0, 1, 0, 1)]},
        prov={'OPERANDS-GROUNDED': 1}, ops={'OPERATION-CORRECT': 1},
        ev_counts={EV2: 1, EV0: 1})
    assert d7_rows(summary)[2].startswith(
        '| D7.2 | Partly measured | see \u00a76-7b | (a) operand provenance '
        'measured: 1 calls (\u00a76, \u00a77b); (b) operation correctness '
        'measured: 1 operations (\u00a77); call inventory incomplete for 1 '
        'execution (1 EV-0 UNOBSERVABLE)')


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7', 'R3.3')
def test_dimension_results_d7_with_nothing_observed_is_not_measured():
    # A run of transport failures only: no invocation outcome, no call,
    # no executed response. It read "D7.1-D7.3 measured" and
    # "D7.3 | Measured | 0".
    rows = d7_rows({'d7_results': {'n': 0}})
    assert rows == [
        '| D7 | **NOT MEASURED** | 0 | D7.1 not measured, D7.2 not '
        'measured, D7.3 not measured; D7.4 not measured (\u00a712) |',
        '| D7.1 | **NOT MEASURED** | see \u00a75 | Invocation rate per '
        'condition (\u00a75): base not measured (no executions); '
        'instruction_removed not measured (no executions) |',
        '| D7.2 | **NOT MEASURED** | see \u00a76-7b | (a) operand '
        'provenance not measured: no call evaluated (\u00a76, \u00a77b); '
        '(b) operation correctness not measured: no operation evaluated '
        '(\u00a77) |',
        '| D7.3 | **NOT MEASURED** | 0 | Transcription fidelity (D7.3 '
        'section): not measured: no executions |',
        '| D7.4 | **NOT MEASURED** | \u2014 | Invocation under pressure '
        '(\u00a712) |']
    assert d7_rows({'d7_results': {'auto_scored_n': 1}})[0].startswith(
        '| D7 | **NOT MEASURED** | N/A |')
    # Every execution UNOBSERVABLE for D7.3: not measured
    assert d7_rows(d7_summary(
        {}, transcription=['UNOBSERVABLE'] * 3))[3] == (
            '| D7.3 | **NOT MEASURED** | 3 | Transcription fidelity (D7.3 '
            'section): not measured: all 3 executions UNOBSERVABLE |')


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7.7')
def test_dimension_results_d71_per_class_within_an_arm():
    # An arm whose observations span classes has a figure per class; the
    # row names each, and says they are not comparable.
    row = d7_rows(d7_summary(
        {'base': [(EV1, 10, 4, 0), (EV2, 10, 6, 0)],
         'instruction_removed': [(EV2, 20, 10, 0)]}))[1]
    assert row == (
        '| D7.1 | Measured | see \u00a75 | Invocation rate per condition '
        '(\u00a75): base measured (n = 4, EV-1 SELF-REPORTED; n = 6, EV-2 '
        'PLATFORM-STRUCTURAL; not comparable); instruction_removed measured '
        '(n = 10, EV-2 PLATFORM-STRUCTURAL) |')


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7.7')
def test_evidence_line_prefers_the_figures_own_executions():
    summary = {'evidence_class_counts': {'EV-0 UNOBSERVABLE': 1,
                                         'EV-2 PLATFORM-STRUCTURAL': 5},
               'd7_evidence': {'D7.2(b)': {'EV-2 PLATFORM-STRUCTURAL': 4},
                               'D7.3': {}}}
    assert report._evidence_line(summary, 'D7.2(b)') == (
        'Evidence class (AP-1 D7.7), executions: '
        '`EV-2 PLATFORM-STRUCTURAL` (4).\n')
    # No executions recorded for the figure: the run's classes, and a
    # statement that figures across classes are not comparable.
    assert report._evidence_line(summary, 'D7.3') == (
        'Evidence class (AP-1 D7.7), executions: `EV-0 UNOBSERVABLE` (1), '
        '`EV-2 PLATFORM-STRUCTURAL` (5). Figures resting on different '
        'classes are not comparable.\n')
    assert report._evidence_line({}, 'D7.3') is None
    assert report._evidence_line({'d7_evidence': {}}, 'D7.3') is None


@pytest.mark.finding('T3-29')
def test_d72b_and_d73_evidence_line_placement():
    summary = {'d7_evidence': {'D7.2(b)': {'EV-2': 2}, 'D7.3': {'EV-1': 3}},
               'operation_correctness_counts': {'OPERATION-CORRECT': 2}}
    assert report._section_d72b_counts(summary).startswith(md(
        '## 7. D7.2(b) Operation Correctness\n',
        'Evidence class (AP-1 D7.7), executions: `EV-2` (2).\n',
        'Total operations evaluated: 2\n'))
    assert report._section_d73(summary).startswith(md(
        '## D7.3 Transcription Fidelity\n',
        'Evidence class (AP-1 D7.7), executions: `EV-1` (3).\n',
        '### A. Transcription Check\n'))


def test_dimension_results_other_claimed_dimension_prints_its_data():
    rows = dim_rows(report._section_dimension_results(
        {'d3_results': {'n': 2}}, {'dimensions_claimed': ['D3']}))
    assert rows[2] == "| D3 | Measured | 2 | {'n': 2} |"


# -- 4. D7 figures by evidence class --------------------------------------

@pytest.mark.finding('T3-33')
def test_d7_figures_counts_sorted_by_class():
    # T3-33 (fixed): the non-comparability clause is D7.7, not §6.4.
    text = report._section_d7_figures({'evidence_class_counts': {
        'EV-2 PLATFORM-STRUCTURAL': 30, 'EV-0 UNOBSERVABLE': 1}})
    assert text == md(
        '## 4. D7 Figures by Evidence Class\n',
        '> Figures resting on different evidence classes are not '
        'comparable (AP-1 v1.3 D7.7).\n',
        '| Evidence Class | Count |',
        '|---|---|',
        '| `EV-0 UNOBSERVABLE` | 1 |',
        '| `EV-2 PLATFORM-STRUCTURAL` | 30 |',
        '')


def test_d7_figures_without_counts_says_so():
    text = report._section_d7_figures({})
    assert text.endswith(md('*No evidence class data available.*', ''))


def test_d7_figures_per_item_detail_in_given_order():
    text = report._section_d7_figures({'item_evidence': [
        {'item_id': 'Q07', 'condition': 'base',
         'evidence_class': 'EV-0 UNOBSERVABLE', 'invocation_outcome': None},
        {'item_id': 'Q01', 'condition': 'base',
         'evidence_class': 'EV-2', 'invocation_outcome': 'INVOKED'},
        {}]})
    assert text.endswith(md(
        '*No evidence class data available.*',
        '\n### Per-Item Evidence Detail\n',
        '| Item | Condition | Evidence Class | Outcome |',
        '|---|---|---|---|',
        '| Q07 | base | `EV-0 UNOBSERVABLE` | None |',
        '| Q01 | base | `EV-2` | INVOKED |',
        '| ? | ? | `?` | ? |',
        ''))


# -- D7.3 transcription fidelity and release coverage ---------------------

def tr(outcome, i=1, **fields):
    r = {'item_id': f'Q{i:02d}', 'condition': 'base', 'repeat': i,
         'outcome': outcome}
    r.update(fields)
    return r


D73_HEAD = (
    '## D7.3 Transcription Fidelity\n',
    '### A. Transcription Check\n',
    '> Compares EVERY return of the required operation to the single ',
    '> figure R2.0 identified as released (AUTO-MATCH items only), ',
    '> under the declared quantisation policy (places and rounding mode).\n',
)
RC_HEAD = (
    '### B. Release Coverage\n',
    '> Compares EVERY candidate figure in the response against ',
    '> EVERY tool return value (ALL items including adjudicated).\n',
)


@PROVISIONAL
@pytest.mark.finding('T3-62')
def test_d73_without_data_says_so_for_both_parts():
    # T3-62: part B describes coverage as a comparison against every tool
    # return; GOVERNED-RELEASE then says nothing about which call governs
    # (an echo or an ORIGINATED call counts). Correct: say what governs.
    assert report._section_d73({}) == md(
        *D73_HEAD,
        '*No transcription data available.*\n',
        *RC_HEAD,
        '*No release coverage data available.*\n')


@pytest.mark.finding('T3-26')
def test_d73_transcription_counts_and_percentages():
    text = report._section_d73({'transcription_results': [
        tr('TRANSCRIBED-EXACT'), tr('TRANSCRIBED-EXACT'),
        tr('UNOBSERVABLE'), tr('OTHER')]})
    assert text.startswith(md(
        *D73_HEAD,
        '| Outcome | Count | % |',
        '|---|---|---|',
        '| `TRANSCRIBED-EXACT` | 2 | 50.0% |',
        '| `TRANSCRIBED-ALTERED` | 0 | 0.0% |',
        '| `UNOBSERVABLE` | 1 | 25.0% |',
        '| **Total** | **4** | |',
        '\nOf the 2 `TRANSCRIBED-EXACT`, 0 were rounded under the declared '
        'quantisation policy (licensed rounding, EXACT under AP-1 v1.3). '
        'Of these: roundings of the tool\'s return to the declared places, '
        '0; float artefacts of the tool (the return differs from the release '
        'only past a binary float\'s 15 significant digits, such as '
        '15.200000000000001 for 15.20), 0. A strict v1.2 "match" count '
        'subtracts the roundings, or all 0 for the strictest reading.',
        '',
        '### B.'))


@pytest.mark.finding('V12-6')
def test_d73_rounded_count_counts_only_flagged_exact_results():
    rounded = dict(tr('TRANSCRIBED-EXACT'), rounded_under_declared_policy=True)
    text = report._section_d73({'transcription_results': [
        rounded, rounded, tr('TRANSCRIBED-EXACT'),
        dict(tr('TRANSCRIBED-EXACT'), rounded_under_declared_policy=False),
        dict(tr('TRANSCRIBED-ALTERED'), rounded_under_declared_policy=True),
        tr('UNOBSERVABLE')]})
    assert ('\nOf the 4 `TRANSCRIBED-EXACT`, 2 were rounded under the '
            'declared quantisation policy (') in text


@pytest.mark.finding('V12-6')
def test_d73_rounded_count_splits_model_roundings_from_float_artefacts():
    # Run E's 291 rounded were 99 roundings of 777.4125 and 192 returns
    # like 15.200000000000001: the report says which.
    rounded = dict(tr('TRANSCRIBED-EXACT'), rounded_under_declared_policy=True,
                   float_artefact=False)
    artefact = dict(rounded, float_artefact=True)
    text = report._section_d73({'transcription_results': [
        rounded, artefact, artefact, artefact, tr('TRANSCRIBED-EXACT')]})
    assert ('\nOf the 5 `TRANSCRIBED-EXACT`, 4 were rounded under the '
            'declared quantisation policy (licensed rounding, EXACT under '
            'AP-1 v1.3). Of these: roundings of the tool\'s return to the '
            'declared places, 1; float artefacts of the tool (the return '
            'differs from the release only past a binary float\'s 15 '
            'significant digits, such as 15.200000000000001 for 15.20), 3. A '
            'strict v1.2 "match" count subtracts the roundings, or all 4 for '
            'the strictest reading.') in text


def test_d73_rounded_count_without_exact_results_is_zero_of_zero():
    text = report._section_d73({'transcription_results': [
        dict(tr('TRANSCRIBED-ALTERED'), rounded_under_declared_policy=True)]})
    assert 'Of the 0 `TRANSCRIBED-EXACT`, 0 were rounded' in text


def test_d73_transcription_percentage_one_decimal():
    text = report._section_d73({'transcription_results': [
        tr('TRANSCRIBED-EXACT'), tr('UNOBSERVABLE'), tr('UNOBSERVABLE')]})
    assert '| `TRANSCRIBED-EXACT` | 1 | 33.3% |' in text
    assert '| `UNOBSERVABLE` | 2 | 66.7% |' in text


def test_d73_altered_transcriptions_listed():
    text = report._section_d73({'transcription_results': [
        tr('TRANSCRIBED-ALTERED', 3, difference='0.01', reason='rounded'),
        tr('TRANSCRIBED-EXACT'), {'outcome': 'TRANSCRIBED-ALTERED'}]})
    assert md(
        '| **Total** | **3** | |',
        '\nOf the 1 `TRANSCRIBED-EXACT`, 0 were rounded under the declared '
        'quantisation policy (licensed rounding, EXACT under AP-1 v1.3). '
        'Of these: roundings of the tool\'s return to the declared places, '
        '0; float artefacts of the tool (the return differs from the release '
        'only past a binary float\'s 15 significant digits, such as '
        '15.200000000000001 for 15.20), 0. A strict v1.2 "match" count '
        'subtracts the roundings, or all 0 for the strictest reading.',
        '\n#### Altered Transcriptions\n',
        'Difference: the gap between the released figure and the closest '
        'return, without the tool\'s binary float tail (digits past 15 '
        'significant digits of the return); the comparison is exact.\n',
        '| Item | Condition | Rep | Difference | Reason |',
        '|---|---|---|---|---|',
        '| Q03 | base | 3 | 0.01 | rounded |',
        '| ? | ? | ? | ? | ? |',
        '',
        '### B.') in text


@pytest.mark.req('R2.5')
def test_d73_altered_difference_printed_without_float_tail():
    # The Difference column prints the gap the run recorded without the
    # tool's float tail (12.000000000000001 as 12; 0.005 stays 0.005)
    text = report._section_d73({'transcription_results': [
        tr('TRANSCRIBED-ALTERED', 22, difference='12.000000000000001',
           difference_shown='12', reason='altered by 12'),
        tr('TRANSCRIBED-ALTERED', 23, difference='0.005',
           difference_shown='0.005', reason='altered by 0.005')]})
    assert '| Q22 | base | 22 | 12 | altered by 12 |' in text
    assert '| Q23 | base | 23 | 0.005 | altered by 0.005 |' in text
    assert '000000000000001' not in text


def test_d73_altered_transcriptions_capped_at_twenty():
    text = report._section_d73({'transcription_results': [
        tr('TRANSCRIBED-ALTERED', i) for i in range(1, 23)]})
    assert '| Q20 | base | 20 |' in text
    assert '| Q21 |' not in text
    assert '| ... | ... | ... | ... | (2 more) |\n' in text


def test_d73_altered_transcriptions_twenty_has_no_more_row():
    text = report._section_d73({'transcription_results': [
        tr('TRANSCRIBED-ALTERED', i) for i in range(1, 21)]})
    assert '| Q20 | base | 20 |' in text
    assert 'more) |' not in text


@PROVISIONAL
def test_d73_release_coverage_counts_and_percentages():
    text = report._section_d73({'release_coverage_results': [
        tr('GOVERNED-RELEASE'), tr('COVERAGE-UNOBSERVABLE'),
        tr('COVERAGE-UNOBSERVABLE'), tr('X')]})
    assert text.endswith(md(
        *RC_HEAD,
        '| Outcome | Count | % |',
        '|---|---|---|',
        '| `GOVERNED-RELEASE` | 1 | 25.0% |',
        '| `PARTIALLY-GOVERNED` | 0 | 0.0% |',
        '| `COVERAGE-UNOBSERVABLE` | 2 | 50.0% |',
        '| **Total** | **4** | |',
        ''))


@PROVISIONAL
def test_d73_release_coverage_percentage_one_decimal():
    text = report._section_d73({'release_coverage_results': [
        tr('GOVERNED-RELEASE'), tr('X'), tr('X')]})
    assert '| `GOVERNED-RELEASE` | 1 | 33.3% |' in text


@PROVISIONAL
def test_d73_partially_governed_listed():
    text = report._section_d73({'release_coverage_results': [
        tr('PARTIALLY-GOVERNED', 4, finding='430.75 not returned'),
        {'outcome': 'PARTIALLY-GOVERNED'}]})
    assert text.endswith(md(
        '| **Total** | **2** | |',
        '\n#### Partially-Governed Findings\n',
        '| Item | Condition | Rep | Finding |',
        '|---|---|---|---|',
        '| Q04 | base | 4 | 430.75 not returned |',
        '| ? | ? | ? | ? |',
        ''))


@PROVISIONAL
def test_d73_partially_governed_capped_at_twenty():
    text = report._section_d73({'release_coverage_results': [
        tr('PARTIALLY-GOVERNED', i) for i in range(1, 24)]})
    assert '| Q20 | base | 20 |' in text
    assert '| Q21 |' not in text
    assert text.endswith('| ... | ... | ... | (3 more) |\n')


@PROVISIONAL
def test_d73_partially_governed_twenty_has_no_more_row():
    text = report._section_d73({'release_coverage_results': [
        tr('PARTIALLY-GOVERNED', i) for i in range(1, 21)]})
    assert 'more) |' not in text


# -- 5. Invocation figures with Clopper-Pearson bounds --------------------

CP_HEAD = (
    '## 5. Invocation Figures with Confidence Bounds\n',
    '> AP-1 v1.3 D7.5: any invocation figure, including 100%, shall be '
    'reported with the exact one-sided 95% upper confidence bound.\n',
)


CP_UNIT = (
    '> D7.1 n counts the computable questions that have an observed '
    'outcome, not the executions: the repeats of a question are not '
    'independent trials. A question counts as a failure if any of its '
    'repeats is NOT-INVOKED; beside k, each failing question with its '
    'NOT-INVOKED repeats out of its observed repeats (EV-0 repeats are '
    'in neither). UNOBSERVABLE executions (EV-0) are neither '
    'successes nor failures and are in no n (SPEC R2.3, R1.3.1).\n')
CP_TABLE = ('| Metric | k (failures) | n | Rate | 95% Upper Bound '
            '| Evidence Class |',
            '|---|---|---|---|---|---|')
EV2 = 'EV-2 PLATFORM-STRUCTURAL'


def test_clopper_pearson_section_without_figures_says_so():
    assert report._section_clopper_pearson({}) == md(
        *CP_HEAD, '*No invocation figures available.*\n')


@pytest.mark.finding('T3-61')
def test_clopper_pearson_section_zero_failures_shows_bound():
    # T3-61 (fixed): the bound is invocation.py's Decimal one, shown
    # rounded up to 6 places (and 4 as a percentage).
    # T3-1, T3-11, V12-5 (fixed): n is questions, the rate is a
    # percentage beside k/n and the bound, with its evidence class, the
    # AP-1 §6.2 headline and the executions per class.
    text = report._section_clopper_pearson({
        'invocation_figures': {'d7_invocation_base': {
            'failures': 0, 'n': 10, 'rate': '10/10', 'condition': 'base',
            'evidence_class': EV2, 'unobservable': 1}},
        'invocation_evidence': {'base': {
            'classes': {
                'EV-0 UNOBSERVABLE': {
                    'executions': 1, 'questions': 1,
                    'observed_questions': 0, 'unobservable_executions': 1},
                EV2: {'executions': 30, 'questions': 10,
                      'observed_questions': 10,
                      'unobservable_executions': 0}},
            'cross_class_warning': 'aggregate spans 2 evidence classes'}}})
    assert text == md(
        *CP_HEAD, CP_UNIT, *CP_TABLE,
        f'| d7_invocation_base | 0 | 10 | 10/10 (100.0%) | '
        f'0.258866 (25.8866%) | `{EV2}` |',
        '',
        '**Headline (AP-1 \u00a76.2):**\n',
        '- Deterministic computation was invoked on 100.0% of computable '
        'questions (10/10; 0 not invoked; one-sided 95% upper bound on the '
        f'failure rate 25.8866%), under base, on evidence class {EV2}.',
        '',
        '**Executions by evidence class:**\n',
        '| Condition | Evidence Class | Executions | Questions '
        '| Questions in n | Unobservable Executions |',
        '|---|---|---|---|---|---|',
        '| base | `EV-0 UNOBSERVABLE` | 1 | 1 | 0 | 1 |',
        f'| base | `{EV2}` | 30 | 10 | 10 | 0 |',
        '',
        '> base: aggregate spans 2 evidence classes; only observed '
        'outcomes are in n.',
        '')


@pytest.mark.finding('T3-11')
def test_clopper_pearson_section_zero_failures_ignores_given_rate():
    text = report._section_clopper_pearson({'invocation_figures': {
        'm': {'n': 500, 'rate': 'whatever'}}})
    assert '| m | 0 | 500 | 500/500 (100.0%) | 0.005974 (0.5974%) | \u2014 |' \
        in text
    assert 'under m.' in text


@pytest.mark.finding('T3-81')
def test_clopper_pearson_section_failures_show_rate_and_bound():
    # k > 0 (fixed, T3-81): the rate and the exact Clopper-Pearson bound,
    # rounded up (1/5: 0.6574084...; 2/20: 0.2826185...), and beside it
    # the exact two-sided 95% interval, its ends rounded outward to 0.01%
    # (1/5: 0.50%-71.65%; 2/20: 1.23%-31.70%).
    text = report._section_clopper_pearson({'invocation_figures': {
        'b': {'failures': 2, 'n': 20, 'rate': '18/20'},
        'a': {'failures': 1, 'n': 5}}})
    # V12-5: the rate is always computed from k and n and shown as a
    # percentage, rounded down (4/5 is 80.0 %).
    assert md(
        '|---|---|---|---|---|---|',
        '| a | 1 | 5 | 4/5 (80.0%) | 0.657409 (65.7409%); two-sided 95% '
        'interval [0.50%, 71.65%] | \u2014 |',
        '| b | 2 | 20 | 18/20 (90.0%) | 0.282619 (28.2619%); two-sided 95% '
        'interval [1.23%, 31.70%] | \u2014 |',
        '') in text
    assert ('- Deterministic computation was invoked on 80.0% of computable '
            'questions (4/5; 1 not invoked; one-sided 95% upper bound on the '
            'failure rate 65.7409%; two-sided 95% interval [0.50%, 71.65%]), '
            'under a.') in text
    assert '**Executions by evidence class:**' not in text


def test_clopper_pearson_section_n_zero_shows_dashes():
    text = report._section_clopper_pearson({'invocation_figures': {
        'z': {'failures': 3, 'n': 0, 'rate': '0/0'}, 'y': {}}})
    assert md('| y | 0 | 0 | \u2014 | \u2014 | \u2014 |',
              '| z | 3 | 0 | \u2014 | \u2014 | \u2014 |', '') in text
    assert ('- Under z: no computable question has an observed invocation '
            'outcome; D7.1 is not measured.') in text
    assert not re.search(r'\b(\d+)/\1\b', text)


@pytest.mark.finding('V12-5')
def test_clopper_pearson_section_rate_below_100_never_rounds_up_to_100():
    # 1999/2000 is 99.95 %: rounded down to 99.9 %, never 100.0 %.
    text = report._section_clopper_pearson({'invocation_figures': {
        'm': {'failures': 1, 'n': 2000, 'condition': 'base'}}})
    assert '1999/2000 (99.9%)' in text and '100.0%' not in text


# -- 6. D7.2(a) originated-operand audit ----------------------------------

def test_d72a_audit_without_entries_says_so():
    assert report._section_d72a_audit({}) == md(
        '## 6. D7.2(a) Originated-Operand Audit\n',
        '*No originated operands detected.*\n')


@pytest.mark.finding('T3-64')
def test_d72a_audit_renders_the_live_entries():
    # Fixed (T3-64): the columns are the fields build_summary writes; the
    # operand is its literal, else its value.
    text = report._section_d72a_audit({'originated_operand_audit': [
        {'item_id': 'Q03', 'condition': 'base', 'repeat': 2,
         'value': '81.0', 'literal': '81.00', 'expression': '2400 * 81.00',
         'resolution': 'originated'},
        {'item_id': 'Q05', 'condition': 'instruction_removed', 'repeat': 1,
         'value': '-25', 'expression': '2400 + -25',
         'resolution': 'originated'}]})
    assert text == md(
        '## 6. D7.2(a) Originated-Operand Audit\n',
        '| Item | Condition | Repeat | Originated Operand | '
        'Expression | Resolution |',
        '|---|---|---|---|---|---|',
        '| Q03 | base | 2 | `81.00` | `2400 * 81.00` | originated |',
        '| Q05 | instruction_removed | 1 | `-25` | `2400 + -25` '
        '| originated |',
        '')


@pytest.mark.finding('T3-64')
def test_d72a_audit_missing_fields_read_dashes():
    text = report._section_d72a_audit({'originated_operand_audit': [{}]})
    assert '| \u2014 | \u2014 | \u2014 | `\u2014` | `\u2014` | \u2014 |\n' \
        in text


# -- 7. D7.2(b) operation correctness -------------------------------------

def test_d72b_without_counts_says_so():
    assert report._section_d72b_counts({}) == md(
        '## 7. D7.2(b) Operation Correctness\n',
        '*No operation correctness data available.*\n')


@PROVISIONAL
def test_d72b_counts_in_fixed_order_with_total():
    text = report._section_d72b_counts({'operation_correctness_counts': {
        'WRONG-OPERATION': 8, 'OPERATION-CORRECT': 26, 'OTHER': 1}})
    assert text == md(
        '## 7. D7.2(b) Operation Correctness\n',
        'Total operations evaluated: 35\n',
        '| Outcome | Count |',
        '|---|---|',
        '| OPERATION-CORRECT | 26 |',
        '| WRONG-OPERATION | 8 |',
        '| OPERATION-UNOBSERVABLE | 0 |',
        '')


@PROVISIONAL
@pytest.mark.finding('T3-63')
def test_d72b_wrong_operation_split_shown_when_non_zero():
    text = report._section_d72b_counts({
        'operation_correctness_counts': {'WRONG-OPERATION': 3},
        'wrong_operation_split': {'route_divergence': 1, 'item_wrong': 0,
                                  'undetermined': 2, 'no_figure': 4}})
    assert text.endswith(md(
        '| OPERATION-UNOBSERVABLE | 0 |',
        '',
        '### WRONG-OPERATION by Item Outcome\n',
        '| Population | Count |',
        '|---|---|',
        '| Route divergence (item answer correct) | 1 |',
        '| Item answer incorrect | 0 |',
        '| Item answer undetermined (adjudicated) | 2 |',
        '| No figure released (no item answer) | 4 |',
        ''))


@PROVISIONAL
def test_d72b_wrong_operation_split_missing_keys_read_zero():
    text = report._section_d72b_counts({
        'operation_correctness_counts': {'WRONG-OPERATION': 1},
        'wrong_operation_split': {'item_wrong': 1}})
    assert '| Route divergence (item answer correct) | 0 |' in text
    assert '| Item answer incorrect | 1 |' in text
    assert '| No figure released (no item answer) | 0 |' in text
    assert '| Item answer undetermined (adjudicated) | 0 |' in text


@PROVISIONAL
def test_d72b_wrong_operation_split_all_zero_is_omitted():
    text = report._section_d72b_counts({
        'operation_correctness_counts': {'OPERATION-CORRECT': 1},
        'wrong_operation_split': {'route_divergence': 0, 'item_wrong': 0,
                                  'undetermined': 0}})
    assert text.endswith('| OPERATION-UNOBSERVABLE | 0 |\n')


# -- 7b. Operand provenance step counts -----------------------------------

PROV_HEAD = (
    '## 7b. D7.2(a) Operand Provenance Step Counts\n',
    '> Each operand in each tool-call expression is resolved through the '
    'five-step hierarchy (AP-1 v1.3 D7.2(a)).\n',
)


def test_provenance_without_data_says_so():
    assert report._section_operand_provenance({}) == md(
        *PROV_HEAD, '*No operand provenance data available.*\n')


@PROVISIONAL
def test_provenance_step_table_with_split_steps():
    text = report._section_operand_provenance({
        'operand_step_counts': {1: 6, 2: 1, 3: 0, 4: 1, 5: 2},
        'step_1_source': 4, 'step_1_constant': 2,
        'step_5_sign_inverted': 1, 'step_5_ungrounded_chain': 0,
        'step_5_untraceable': 1})
    assert text == md(
        *PROV_HEAD,
        'Total operands resolved: 10\n',
        '| Step | Resolution | Count | % |',
        '|---|---|---|---|',
        '| 1 | Source match | 4 | 40.0% |',
        '| 1 | Declared constant | 2 | 20.0% |',
        '| 2 | Transformed source | 1 | 10.0% |',
        '| 3 | Reference intermediate | 0 | 0.0% |',
        '| 4 | Computed in session | 1 | 10.0% |',
        '| 5 | Originated, sign-inverted from source | 1 | 10.0% |',
        '| 5 | Originated, computed from ungrounded invocation | 0 | 0.0% |',
        '| 5 | Originated, no traceable basis | 1 | 10.0% |',
        '')


@PROVISIONAL
def test_provenance_step_percentages_one_decimal():
    text = report._section_operand_provenance({
        'operand_step_counts': {1: 1, 2: 1, 3: 1},
        'step_1_constant': 1, 'step_5_untraceable': 2,
        'step_5_sign_inverted': 1, 'step_5_ungrounded_chain': 1})
    assert '| 2 | Transformed source | 1 | 33.3% |' in text
    assert '| 1 | Declared constant | 1 | 33.3% |' in text
    assert '| 5 | Originated, no traceable basis | 2 | 66.7% |' in text
    assert '| 5 | Originated, sign-inverted from source | 1 | 33.3% |' in text
    assert ('| 5 | Originated, computed from ungrounded invocation | 1 '
            '| 33.3% |') in text


def test_provenance_source_count_falls_back_to_step_1_count():
    text = report._section_operand_provenance({
        'operand_step_counts': {1: 3}})
    assert '| 1 | Source match | 3 | 100.0% |' in text
    assert '| 1 | Declared constant | 0 | 0.0% |' in text


@PROVISIONAL
def test_provenance_split_keys_missing_read_zero():
    text = report._section_operand_provenance({'operand_step_counts': {2: 0}})
    assert '| 1 | Source match | 0 |' in text
    assert '| 5 | Originated, sign-inverted from source | 0 |' in text
    assert '| 5 | Originated, computed from ungrounded invocation | 0 |' \
        in text
    assert '| 5 | Originated, no traceable basis | 0 |' in text


@PROVISIONAL
@pytest.mark.finding('T3-16')
def test_provenance_outcomes_only_shows_dashes_for_percentages():
    text = report._section_operand_provenance({
        'provenance_outcomes': {'OPERANDS-GROUNDED': 2}})
    assert text == md(
        *PROV_HEAD,
        'Total operands resolved: 0\n',
        '| Step | Resolution | Count | % |',
        '|---|---|---|---|',
        '| 1 | Source match | 0 | \u2014% |',
        '| 1 | Declared constant | 0 | \u2014% |',
        '| 2 | Transformed source | 0 | \u2014% |',
        '| 3 | Reference intermediate | 0 | \u2014% |',
        '| 4 | Computed in session | 0 | \u2014% |',
        '| 5 | Originated, sign-inverted from source | 0 | \u2014% |',
        '| 5 | Originated, computed from ungrounded invocation | 0 '
        '| \u2014% |',
        '| 5 | Originated, no traceable basis | 0 | \u2014% |',
        '',
        '### Per-Invocation Outcomes\n',
        '> OPERANDS-UNOBSERVABLE: a calculator call whose operands could not '
        'be read (malformed arguments or an unreadable expression); '
        'declared, never grounded. UNMEASURABLE: a call in a chained item '
        'whose ground truth declares no intermediates (SPEC R2.4); its '
        'operands are not counted in the step table.\n',
        '| Outcome | Count | Proportion |',
        '|---|---|---|',
        '| OPERANDS-GROUNDED | 2 | 2/2 (100.0%) |',
        '| OPERAND-ORIGINATED | 0 | 0/2 (0.0%) |',
        '| OPERANDS-UNOBSERVABLE | 0 | 0/2 (0.0%) |',
        '| UNMEASURABLE | 0 | 0/2 (0.0%) |',
        '')


@pytest.mark.finding('T3-42')
def test_provenance_unmeasurable_count_and_executions_shown():
    # SPEC R2.4/R3.3: UNMEASURABLE invocations get their row, and each
    # execution for which D7.2 is UNMEASURABLE is listed with its reason.
    text = report._section_operand_provenance({
        'provenance_outcomes': {'OPERANDS-GROUNDED': 1, 'UNMEASURABLE': 3},
        'provenance_unmeasurable': [
            {'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
             'reason': 'chained'}, {}]})
    assert ('| OPERANDS-GROUNDED | 1 | 1/4 (25.0%) |\n'
            '| OPERAND-ORIGINATED | 0 | 0/4 (0.0%) |\n'
            '| OPERANDS-UNOBSERVABLE | 0 | 0/4 (0.0%) |\n'
            '| UNMEASURABLE | 3 | 3/4 (75.0%) |\n') in text
    assert text.endswith(md(
        '### D7.2 UNMEASURABLE Executions\n',
        '| Item | Condition | Repeat | Reason |',
        '|---|---|---|---|',
        '| Q01 | base | 2 | chained |',
        '| ? | ? | ? | ? |',
        ''))


def test_provenance_outcomes_all_zero_are_omitted():
    text = report._section_operand_provenance({
        'operand_step_counts': {1: 1},
        'provenance_outcomes': {'OPERANDS-GROUNDED': 0,
                                'OPERAND-ORIGINATED': 0}})
    assert 'Per-Invocation' not in text
    assert text.endswith('| 5 | Originated, no traceable basis | 0 | 0.0% |\n')


def test_provenance_audit_lists_value_and_expression():
    text = report._section_operand_provenance({
        'operand_step_counts': {5: 1},
        'originated_operand_audit': [
            {'item_id': 'Q03', 'condition': 'base', 'value': '81.0',
             'expression': '2400 * 81.0', 'resolution': 'originated'},
            {}]})
    assert text.endswith(md(
        '| 5 | Originated, no traceable basis | 0 | 0.0% |',
        '',
        '### Originated Operand Audit\n',
        '| Item | Condition | Value | Expression | Resolution |',
        '|---|---|---|---|---|',
        '| Q03 | base | `81.0` | `2400 * 81.0` | originated |',
        '| ? | ? | `?` | `?` | ? |',
        ''))


# -- 8. Scoring proportions -----------------------------------------------

def test_scoring_proportions_without_data_says_so():
    assert report._section_scoring_proportions({}) == md(
        '## 8. Scoring Proportions\n',
        '*No scoring proportion data available.*\n')


@pytest.mark.finding('T3-3', 'T3-66')
def test_scoring_proportions_d1_split_and_no_rate_while_pending():
    # T3-3 (fixed): no rate until the adjudicated items are scored;
    # T3-66 (fixed): UNMEASURABLE shown and in the total.
    text = report._section_scoring_proportions({'d1_results': {
        'auto_scored_n': 22, 'adjudicated_n': 17, 'unmeasurable_n': 1,
        'accuracy_rate': Decimal('1')}})
    assert text == md(
        '## 8. Scoring Proportions\n',
        '### D1 Accuracy (base condition only)\n',
        '- Auto-scored: 22',
        '- Adjudicated: 17',
        '- Unmeasurable: 1 (response unreadable, routed to adjudication)',
        '- Total: 40',
        '- Auto-scored proportion: 22/40 = 55.00%',
        '- Accuracy rate: not computed: 18 items await adjudication, and '
        'R2.0 routes every wrong figure there, so a rate over the 22 '
        'auto-scored items alone would leave the wrong answers out (T3-3)',
        '')


def test_scoring_proportions_d1_rate_when_nothing_pending():
    text = report._section_scoring_proportions({'d1_results': {
        'auto_scored_n': 5, 'accuracy_rate': Decimal('0.8')}})
    assert text.endswith(md(
        '- Auto-scored proportion: 5/5 = 100.00%',
        '- Accuracy rate: 0.8 (computed from 5 auto-scored items only; '
        '0 adjudicated items are not represented in this rate)', ''))


def test_scoring_proportions_d1_proportion_two_decimals():
    text = report._section_scoring_proportions({'d1_results': {
        'auto_scored_n': 1, 'adjudicated_n': 2}})
    assert '- Auto-scored proportion: 1/3 = 33.33%' in text


@pytest.mark.finding('T3-66')
def test_scoring_proportions_d1_without_counts_or_rate():
    text = report._section_scoring_proportions({'d1_results': {'n': 5}})
    assert text == md(
        '## 8. Scoring Proportions\n',
        '### D1 Accuracy (base condition only)\n',
        '- Auto-scored: 0',
        '- Adjudicated: 0',
        '- Unmeasurable: 0 (response unreadable, routed to adjudication)',
        '- Total: 0',
        '')


@pytest.mark.finding('T3-33')
def test_scoring_proportions_d7_split_labelled_computation_invocation():
    # T3-33 (fixed): D7 is "Computation invocation" in AP-1 v1.3, not
    # "Provenance" (D3).
    text = report._section_scoring_proportions({'d7_results': {
        'n': 41, 'auto_scored_n': 30, 'adjudicated_n': 10}})
    assert text == md(
        '## 8. Scoring Proportions\n',
        '### D7 Computation invocation\n',
        '- Auto-scored: 30',
        '- Adjudicated: 10',
        '- Total: 40',
        '- Auto-scored proportion: 30/40 = 75.00%',
        '')


def test_scoring_proportions_d7_proportion_two_decimals():
    text = report._section_scoring_proportions({'d7_results': {
        'auto_scored_n': 2, 'adjudicated_n': 1}})
    assert '- Auto-scored proportion: 2/3 = 66.67%' in text


def test_scoring_proportions_d7_without_counts():
    text = report._section_scoring_proportions({'d7_results': {'n': 3}})
    assert text.endswith(md('- Auto-scored: 0', '- Adjudicated: 0',
                            '- Total: 0', ''))


@pytest.mark.finding('T3-33')
def test_scoring_proportions_d1_then_d7():
    text = report._section_scoring_proportions({
        'd1_results': {'auto_scored_n': 1},
        'd7_results': {'auto_scored_n': 1}})
    assert text.index('### D1 Accuracy') < \
        text.index('### D7 Computation invocation')
    assert 'No scoring proportion data' not in text


# -- 9. D2 mechanism classes ----------------------------------------------

D2_NOTE = ('> D2 is auto-measured. STRUCTURAL and CONFIGURED are '
           'operator-declared; OBSERVED-ONLY and UNMEASURED are '
           'determined from evidence.\n\n'
           '> Figures surface: each run\'s identified answer, its released '
           'figure or else the one value it states. An answer not '
           'identified (a decline, no figure, several figures) is '
           'unresolved: counted, never a value, and never evidence that the '
           'answers were stable. A question-condition with one is '
           'UNMEASURED unless its identified answers already differ, '
           'counted then as at least that many.\n')


@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2')
@pytest.mark.parametrize('data, cell', [
    ({'distinct_values': 1, 'values': ['144.00']}, '1: 144.00'),
    ({'distinct_values': None, 'values': ['144.00'], 'unresolved': 14},
     '\u2014: 144.00; 14 unresolved'),
    ({'distinct_values': None, 'values': [], 'unresolved': 3},
     '\u2014: 3 unresolved'),
    ({'distinct_values': 2, 'values': ['777.41', '782.77'],
      'unresolved': 41}, 'at least 2: 777.41; 782.77; 41 unresolved'),
    ({'distinct_values': None}, '\u2014'),
])
def test_d2_distinct_counts_unresolved_answers_apart(data, cell):
    assert report._d2_distinct(data) == cell


def test_d2_without_results_says_so():
    assert report._section_d2_mechanisms({}) == md(
        '## 9. D2 Reproducibility Mechanism Classes\n',
        D2_NOTE,
        '*No D2 results available.*\n')


def test_d2_cap_reason_shown_before_note():
    text = report._section_d2_mechanisms({
        'd2_cap_reason': 'D2.2 cap: temperature was platform-rejected.'})
    assert text == md(
        '## 9. D2 Reproducibility Mechanism Classes\n',
        '> **D2.2 cap: temperature was platform-rejected.**\n',
        '> *The platform-rejection detail above is the verbatim error '
        'recorded during config setup. The rejection is model-independent: '
        'it applies to any model run under this config.*\n',
        D2_NOTE,
        '*No D2 results available.*\n')


@pytest.mark.finding('T3-4')
def test_d2_live_shape_table_per_question_condition_and_surface():
    # Fixed (T3-4): §9 reads the live shape, keyed '<item>/<condition>',
    # with each row's evidence basis and, on figures, the distinct
    # values.
    text = report._section_d2_mechanisms({'d2_results': {
        'Q02/instruction_removed': {'figures': {
            'mechanism': 'UNMEASURED', 'operator_declared': False,
            'distinct_values': None, 'successful_runs': 1}},
        'Q01/base': {
            'prose': {'mechanism': 'STRUCTURAL', 'operator_declared': True,
                      'distinct_values': 1, 'successful_runs': 3,
                      'parameter_echo_status': 'VERIFIED'},
            'figures': {'mechanism': 'OBSERVED-ONLY',
                        'distinct_values': 2, 'values': ['15.20', '15.21'],
                        'successful_runs': 3}},
        'Q03': {'figures': {}}}}, {'repeat_count': 3})
    assert text == md(
        '## 9. D2 Reproducibility Mechanism Classes\n',
        D2_NOTE,
        'n = 3 questions \u00d7 3 runs, per condition.\n',
        '> **Below AP-1 D2\'s 10 \u00d7 50: n = 3 \u00d7 3** (AP-1 D2: '
        'minimum 10 questions \u00d7 minimum 50 runs). The runner accepts '
        'any run count and classifies on what was run.\n',
        'Operator\'s declaration (settings field `d2_declared`): none, so '
        'no surface is STRUCTURAL or CONFIGURED.\n',
        'Left out of the comparison: none.\n',
        'Classes per surface, over question-conditions: figures: '
        'OBSERVED-ONLY 1, UNMEASURED 1, unknown 1; prose: STRUCTURAL 1.\n',
        '| Question | Condition | Surface | Mechanism Class | Basis '
        '| Distinct Values | Runs | Parameter Echo |',
        '|---|---|---|---|---|---|---|---|',
        '| Q01 | base | figures | `OBSERVED-ONLY` | evidence: observed over '
        '3 runs; not operator-declared | 2: 15.20; 15.21 | 3 '
        '| `UNVERIFIED` |',
        '| Q01 | base | prose | `STRUCTURAL` | operator-declared | 1 | 3 '
        '| `VERIFIED` |',
        '| Q02 | instruction_removed | figures | `UNMEASURED` | evidence: '
        'observed over 1 run; not operator-declared | \u2014 | 1 '
        '| `UNVERIFIED` |',
        '| Q03 | \u2014 | figures | `unknown` | evidence: no runs recorded; '
        'not operator-declared | \u2014 | \u2014 | `UNVERIFIED` |',
        '')


@pytest.mark.finding('T3-4')
def test_dimension_results_d2_row_counts_questions_and_classes():
    d2 = {'Q01/base': {'figures': {'mechanism': 'OBSERVED-ONLY'},
                       'prose': {'mechanism': 'OBSERVED-ONLY'}},
          'Q01/instruction_removed': {'figures': {'mechanism': 'UNMEASURED'},
                                      'prose': {'mechanism': 'UNMEASURED'}},
          'Q02/base': {'figures': {'mechanism': 'OBSERVED-ONLY'},
                       'prose': {'mechanism': 'OBSERVED-ONLY'}},
          'Q03/base': {'figures': {'mechanism': 'OBSERVED-ONLY'}}}
    rows = dim_rows(report._section_dimension_results(
        {'d2_results': d2}, {'dimensions_claimed': ['D2']}))
    # n is the number of questions (3), not of question-conditions (4)
    # (with no repeat count in the config, n is questions only; 3 is
    # below AP-1 D2's 10 questions, which the row says)
    assert rows[1] == ('| D2 | Measured | 3 | figures: OBSERVED-ONLY 3, '
                       'UNMEASURED 1; prose: OBSERVED-ONLY 2, UNMEASURED 1; '
                       'below AP-1 D2\'s 10 \u00d7 50 (\u00a79) |')


RUN_COUNT_REASON = (
    'T3-4: any run count is accepted; report sections 3 and 9 give D2\'s n '
    '(questions x runs) and say in one line when a run is below AP-1 D2\'s '
    '10 questions x 50 runs; the minimum is reported, not enforced, as '
    'requested in review; the line\'s words are the author\'s')


def d2_run(questions, runs):
    """The D2 results of a run of these many questions, each repeated
    runs times with the same answer, classified as the scoring pass
    classifies them (minimum runs: the repeat count)."""
    from ap1_run.runner.summary import classify_reproducibility
    reply = {'choices': [{'message': {'role': 'assistant',
                                      'content': 'The interest is $15.20.'}}]}
    keys = [(f'Q{i:02d}', 'base') for i in range(1, questions + 1)]
    return classify_reproducibility(
        {k: [reply] * runs for k in keys}, runs, None,
        {k: [Decimal('15.20')] * runs for k in keys})


def d2_report(questions, runs):
    """Sections 3 and 9 of that run, with its repeat count configured."""
    d2 = d2_run(questions, runs)
    config = {'dimensions_claimed': ['D2'], 'repeat_count': runs}
    return (dim_rows(report._section_dimension_results(
                {'d2_results': d2}, config))[1],
            report._section_d2_mechanisms({'d2_results': d2}, config), d2)


@pytest.mark.proposal(RUN_COUNT_REASON)
@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2')
def test_d2_run_of_3_repeats_is_classified_and_says_below_10_by_50():
    # AP-1 D2 Method: minimum 10 questions x minimum 50 runs. A run of 10
    # questions x 3 repeats is accepted and classified; its n is given,
    # and one line says it is below that minimum.
    row, text, d2 = d2_report(10, 3)
    assert {cell['mechanism'] for surfaces in d2.values()
            for cell in surfaces.values()} == {'OBSERVED-ONLY'}
    assert row == ('| D2 | Measured | 10 \u00d7 3 | figures: OBSERVED-ONLY '
                   '10; prose: OBSERVED-ONLY 10; below AP-1 D2\'s 10 \u00d7 '
                   '50 (\u00a79) |')
    lines = text.splitlines()
    assert 'n = 10 questions \u00d7 3 runs, per condition.' in lines
    below = [line for line in lines if '10 \u00d7 50' in line]
    assert below == [
        '> **Below AP-1 D2\'s 10 \u00d7 50: n = 10 \u00d7 3** (AP-1 D2: '
        'minimum 10 questions \u00d7 minimum 50 runs). The runner accepts '
        'any run count and classifies on what was run.']


@pytest.mark.proposal(RUN_COUNT_REASON)
@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2')
def test_d2_run_of_10_by_50_prints_no_below_minimum_line():
    row, text, _ = d2_report(10, 50)
    assert row == ('| D2 | Measured | 10 \u00d7 50 | figures: OBSERVED-ONLY '
                   '10; prose: OBSERVED-ONLY 10 (\u00a79) |')
    assert 'n = 10 questions \u00d7 50 runs, per condition.' in \
        text.splitlines()
    assert 'Below' not in text and 'below' not in row


@pytest.mark.proposal(RUN_COUNT_REASON)
@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2')
def test_d2_run_of_5_questions_by_50_says_below_on_questions():
    # Under on questions only: 50 repeats of 5 questions is still below.
    row, text, _ = d2_report(5, 50)
    assert row.endswith('; below AP-1 D2\'s 10 \u00d7 50 (\u00a79) |')
    assert '| 5 \u00d7 50 |' in row
    assert ('> **Below AP-1 D2\'s 10 \u00d7 50: n = 5 \u00d7 50** (AP-1 '
            'D2: minimum 10 questions \u00d7 minimum 50 runs). The runner '
            'accepts any run count and classifies on what was run.'
            ) in text.splitlines()


D1_CATEGORY_HEAD = (
    '\n### D1 per Category\n',
    '> AP-1 v1.3 D1: results per category, with 95% confidence intervals '
    'and n stated; no category claim where n < 10. Base condition only; '
    'the instruction-removed repeats measure D7. n counts questions; a '
    'question is correct only if every base execution of it is. Interval: '
    'exact two-sided 95% Clopper-Pearson.\n',
    '| Category | n (questions) | Executions | Correct | Incorrect '
    '| No Figure | Awaiting Adjudication | Accuracy (95% CI) |',
    '|---|---|---|---|---|---|---|---|')


@pytest.mark.finding('T3-32')
@pytest.mark.req('AP-1 D1')
def test_dimension_results_d1_per_category_with_interval():
    def cat(n, correct_questions, pending=0, interval=None):
        return {'n': n, 'executions': 2 * n, 'correct': 2 * n - 1,
                'incorrect': 1, 'no_figure': 0, 'pending': pending,
                'correct_questions': correct_questions,
                'rate': None, 'interval': interval}
    d1 = {'n': 4, 'auto_scored_n': 4, 'accuracy_rate': Decimal('1'),
          'by_category': {
              'interest': cat(2, 1),
              'growth': cat(10, 8, interval=(Decimal('0.44390'),
                                             Decimal('0.97479'))),
              'fees': cat(12, 12, pending=3),
              'balance': cat(10, 10, pending=1)}}
    text = report._section_dimension_results(
        {'d1_results': d1}, {'dimensions_claimed': ['D1']})
    assert text.endswith(md(
        *D1_CATEGORY_HEAD,
        '| interest | 2 | 4 | 3 | 1 | 0 | 0 | no category claim: n < 10 |',
        '| growth | 10 | 20 | 19 | 1 | 0 | 0 | 8/10 (80.0%; 95% CI '
        '44.3%-97.5%) |',
        '| fees | 12 | 24 | 23 | 1 | 0 | 3 | no rate: 3 executions await '
        'adjudication |',
        '| balance | 10 | 20 | 19 | 1 | 0 | 1 | no rate: 1 executions await '
        'adjudication |',
        ''))


@pytest.mark.proposal(
    'T3-32: a question with no category is listed under the D1 table as '
    'not in any category, with the count, and the run goes ahead; AP-1 D1 '
    'asks for results per category and says nothing of a question with '
    'none')
@pytest.mark.finding('T3-32')
@pytest.mark.req('AP-1 D1')
def test_dimension_results_d1_lists_the_question_not_in_any_category():
    c = {'n': 10, 'executions': 10, 'correct': 10, 'incorrect': 0,
         'no_figure': 0, 'pending': 0, 'correct_questions': 10,
         'rate': Decimal(1), 'interval': (Decimal('0.69150'), Decimal(1))}
    d1 = {'n': 11, 'by_category': {'interest': c}, 'uncategorised': ['Q11']}
    text = report._section_dimension_results(
        {'d1_results': d1}, {'dimensions_claimed': ['D1']})
    assert text.endswith(md(
        *D1_CATEGORY_HEAD,
        '| interest | 10 | 10 | 10 | 0 | 0 | 0 | 10/10 (100.0%; 95% CI '
        '69.1%-100.0%) |',
        '\nNot in any category: 1 question (`Q11`). It is in no row above '
        "and in no category's n.",
        ''))


@pytest.mark.proposal(
    'T3-32: a question with no category is listed under the D1 table as '
    'not in any category, with the count, and the run goes ahead; AP-1 D1 '
    'asks for results per category and says nothing of a question with '
    'none')
@pytest.mark.finding('T3-32')
@pytest.mark.req('AP-1 D1')
def test_dimension_results_d1_lists_questions_not_in_any_category_alone():
    # No question has a category: no row, but the questions are listed,
    # not dropped with the table.
    d1 = {'n': 2, 'by_category': {}, 'uncategorised': ['Q1', 'Q2']}
    text = report._section_dimension_results(
        {'d1_results': d1}, {'dimensions_claimed': ['D1']})
    assert text.endswith(md(
        *D1_CATEGORY_HEAD,
        '\nNot in any category: 2 questions (`Q1`, `Q2`). They are in no '
        "row above and in no category's n.",
        ''))
    assert 'Not in any category' not in report._section_dimension_results(
        {'d1_results': d1}, {'dimensions_claimed': ['D7']})


def test_dimension_results_d1_categories_only_when_d1_claimed():
    summary = {'d1_results': {'n': 1, 'by_category': {'x': {}}}}
    assert 'D1 per Category' not in report._section_dimension_results(
        summary, {'dimensions_claimed': ['D7']})
    assert 'D1 per Category' not in report._section_dimension_results(
        {'d1_results': {'n': 1, 'by_category': {}}},
        {'dimensions_claimed': ['D1']})


def test_dimension_results_other_dimension_without_n_reads_na():
    rows = dim_rows(report._section_dimension_results(
        {'d3_results': {'x': 1}}, {'dimensions_claimed': ['D3']}))
    assert rows[2] == "| D3 | Measured | N/A | {'x': 1} |"


# -- 10. Non-outcome cells ------------------------------------------------

CELLS_HEAD = (
    '## 10. Non-Outcome Cells\n',
    '> Every cell that is not a scoreable outcome is listed with its '
    'reason.\n',
)


def test_cells_without_any_says_so():
    assert report._section_unmeasured_cells({}, None) == md(
        *CELLS_HEAD, '*No non-outcome cells.*\n', '')


CELLS_TABLE = ('| Item | Condition | Status | Reason | Repeat | Measurement |',
               '|---|---|---|---|---|---|')


def test_cells_from_summary_listed():
    text = report._section_unmeasured_cells({'non_outcome_cells': [
        {'item_id': 'Q01', 'condition': 'base', 'repeat': 3,
         'status': 'UNMEASURED', 'reason': 'rate limited'},
        {}]}, None)
    assert text == md(
        *CELLS_HEAD,
        '2 cells: execution 2.\n',
        *CELLS_TABLE,
        '| Q01 | base | UNMEASURED | rate limited | 3 | execution |',
        '| \u2014 | \u2014 | \u2014 | \u2014 | \u2014 | execution |',
        '')


@pytest.mark.finding('T3-35')
def test_cells_from_transcript_error_state_or_ev0_one_row_per_record():
    # An execution-level cell per transcript record: its error state, else
    # its EV-0 class (never both). Figure-identification records are not
    # executions.
    text = report._section_unmeasured_cells({}, [
        {'item_id': 'Q02', 'condition': 'base', 'repeat': 1,
         'error_state': 'TRANSPORT_FAILURE: HTTP 500: boom'},
        {'item_id': 'Q03', 'condition': 'base', 'error_state': 'VOID',
         'evidence_class': 'EV-0 UNOBSERVABLE'},
        {'item_id': 'Q04', 'condition': 'base', 'repeat': 2,
         'evidence_class': 'EV-0 UNOBSERVABLE'},
        {'evidence_class': 'EV-2 PLATFORM-STRUCTURAL'},
        {'error_state': None, 'evidence_class': None},
        {'error_state': 'X:y'},
        {'record_type': 'figure_identification', 'item_id': 'Q09',
         'error_state': 'E', 'figure_outcome': 'UNMEASURABLE'},
    ])
    assert text == md(
        *CELLS_HEAD,
        '4 cells: execution 3; D7.1 invocation 1.\n',
        *CELLS_TABLE,
        '| Q02 | base | TRANSPORT_FAILURE | TRANSPORT_FAILURE: HTTP 500: '
        'boom | 1 | execution |',
        '| Q03 | base | VOID | VOID | \u2014 | execution |',
        '| Q04 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE | 2 '
        '| D7.1 invocation |',
        '| \u2014 | \u2014 | X | X:y | \u2014 | execution |',
        '')


EXHAUSTED = ('TOOL_LOOP_EXHAUSTED: the response after 10 tool turns still '
             'asked for 1 tool call(s), which were not executed')


@pytest.mark.finding('T3-67')
@pytest.mark.req('R3.3')
def test_cells_tool_loop_exhaustion_is_a_reason_not_a_status():
    # An exhausted loop is an EXECUTED, scored execution with a flag
    # (T3-67), not one of section 10's statuses (SPEC R3.3: UNMEASURED,
    # UNOBSERVABLE, UNMEASURABLE, VOID). With no figure to read, its R2.0
    # figure is the UNMEASURABLE cell, and the flag is its reason; with a
    # scored figure it has no non-outcome cell.
    record = {'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
              'status': 'EXECUTED', 'evidence_class': 'EV-2 '
              'PLATFORM-STRUCTURAL', 'error_state': EXHAUSTED}
    text = report._section_unmeasured_cells({}, [
        dict(record, figure_outcome='UNMEASURABLE')])
    assert text == md(
        *CELLS_HEAD,
        '1 cells: R2.0 figure 1.\n',
        *CELLS_TABLE,
        '| Q01 | base | UNMEASURABLE | response could not be read; routed '
        f'to adjudication; {EXHAUSTED} | 1 | R2.0 figure |',
        '')
    assert report._section_unmeasured_cells({}, [
        dict(record, figure_outcome='AUTO-MATCH')]) == md(
        *CELLS_HEAD, '*No non-outcome cells.*\n', '')


@pytest.mark.finding('T3-67', 'T3-35')
@pytest.mark.req('R3.3', 'AP-1 D7.7')
def test_cells_tool_loop_exhaustion_keeps_the_ev0_invocation_cell():
    # The loop flag is handled apart from invocation observability: an
    # exhausted loop whose invocation is EV-0 still has its D7.1 cell, the
    # flag beside its reason; with an unreadable figure, both cells.
    record = {'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
              'status': 'EXECUTED', 'evidence_class': 'EV-0 UNOBSERVABLE',
              'error_state': EXHAUSTED}
    invocation = ('| Q01 | base | UNOBSERVABLE | Evidence class: EV-0 '
                  f'UNOBSERVABLE; {EXHAUSTED} | 1 | D7.1 invocation |')
    assert report._section_unmeasured_cells({}, [
        dict(record, figure_outcome='AUTO-MATCH')]) == md(
        *CELLS_HEAD, '1 cells: D7.1 invocation 1.\n', *CELLS_TABLE,
        invocation, '')
    assert report._section_unmeasured_cells({}, [
        dict(record, figure_outcome='UNMEASURABLE')]) == md(
        *CELLS_HEAD, '2 cells: D7.1 invocation 1; R2.0 figure 1.\n',
        *CELLS_TABLE, invocation,
        '| Q01 | base | UNMEASURABLE | response could not be read; routed '
        f'to adjudication; {EXHAUSTED} | 1 | R2.0 figure |', '')


def test_cells_summary_cells_come_before_transcript_cells():
    text = report._section_unmeasured_cells(
        {'non_outcome_cells': [{'item_id': 'S', 'condition': 'c',
                                'status': 'VOID', 'reason': 'r'}]},
        [{'item_id': 'T', 'condition': 'c', 'error_state': 'VOID'}])
    assert text.index('| S |') < text.index('| T |')


@pytest.mark.finding('T3-35')
def test_cells_execution_level_deduplicated_on_the_repeat_only():
    # The same execution (item, condition, repeat) from the summary and
    # the transcript is one row, the summary's; other repeats, and
    # records without a repeat, are rows of their own.
    text = report._section_unmeasured_cells(
        {'non_outcome_cells': [
            {'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
             'status': 'UNMEASURED', 'reason': 'transport'}]},
        [{'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
          'error_state': 'TRANSPORT_FAILURE: timeout'},
         {'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
          'error_state': 'TRANSPORT_FAILURE: timeout'},
         {'item_id': 'Q01', 'condition': 'instruction_removed', 'repeat': 1,
          'evidence_class': 'EV-0 UNOBSERVABLE'},
         {'item_id': 'Q01', 'condition': 'base', 'error_state': 'E'},
         {'item_id': 'Q01', 'condition': 'base', 'error_state': 'E'}])
    rows = [line for line in text.split('\n') if line.startswith('| Q01 ')]
    assert rows == [
        '| Q01 | base | UNMEASURED | transport | 1 | execution |',
        '| Q01 | base | TRANSPORT_FAILURE | TRANSPORT_FAILURE: timeout | 2 '
        '| execution |',
        '| Q01 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 '
        'UNOBSERVABLE | 1 | D7.1 invocation |',
        '| Q01 | base | E | E | \u2014 | execution |',
        '| Q01 | base | E | E | \u2014 | execution |']


@pytest.mark.finding('T3-35')
def test_cells_every_measurement_kind_listed_with_its_reason():
    summary = {
        'provenance_unmeasurable': [{'item_id': 'Q10', 'condition': 'base',
                                     'repeat': 1, 'reason': 'chained'}],
        'operands_unobservable': [{'item_id': 'Q11', 'condition': 'base',
                                   'repeat': 2, 'reason': 'no operand'}],
        'operation_unobservable': [{'item_id': 'Q12', 'condition': 'base',
                                    'repeat': 3, 'reason': "max(1, 2)"}],
        'transcription_results': [
            {'item_id': 'Q13', 'condition': 'base', 'repeat': 4,
             'outcome': 'UNOBSERVABLE',
             'reason': 'R2.0 outcome is ADJUDICATE-DECLINE, not AUTO-MATCH'},
            {'item_id': 'Q14', 'condition': 'base', 'repeat': 5,
             'outcome': 'UNOBSERVABLE',
             'reason': 'tool return value not available'},
            {'item_id': 'Q15', 'outcome': 'TRANSCRIBED-EXACT'}],
        'release_coverage_results': [
            {'item_id': 'Q16', 'condition': 'base', 'repeat': 6,
             'outcome': 'COVERAGE-UNOBSERVABLE', 'finding': 'no tool call'},
            {'item_id': 'Q17', 'outcome': 'GOVERNED-RELEASE'}]}
    text = report._section_unmeasured_cells(summary, [
        {'item_id': 'Q09', 'condition': 'base', 'repeat': 7,
         'figure_outcome': 'UNMEASURABLE'},
        {'item_id': 'Q08', 'figure_outcome': 'AUTO-MATCH'}])
    assert text == md(
        *CELLS_HEAD,
        '7 cells: R2.0 figure 1; D7.2(a) provenance 2; D7.2(b) operation '
        '1; D7.3 transcription 2; D7.3 release coverage 1.\n',
        *CELLS_TABLE,
        '| Q09 | base | UNMEASURABLE | response could not be read; routed '
        'to adjudication | 7 | R2.0 figure |',
        '| Q10 | base | UNMEASURABLE | chained | 1 | D7.2(a) provenance |',
        '| Q11 | base | OPERANDS-UNOBSERVABLE | no operand | 2 '
        '| D7.2(a) provenance |',
        '| Q12 | base | OPERATION-UNOBSERVABLE | max(1, 2) | 3 '
        '| D7.2(b) operation |',
        '| Q13 | base | UNOBSERVABLE | no released figure to compare (not '
        'auto-matched) | 4 | D7.3 transcription |',
        '| Q14 | base | UNOBSERVABLE | tool return value not available | 5 '
        '| D7.3 transcription |',
        '| Q16 | base | COVERAGE-UNOBSERVABLE | no tool call | 6 '
        '| D7.3 release coverage |',
        '')


@pytest.mark.finding('T3-35')
def test_cells_one_execution_one_row_per_measurement():
    # An EV-0 execution that is also the summary's UNMEASURED cell is one
    # execution row; its other measurements are rows of their own, even
    # for the same execution. Cells of other items are never merged.
    text = report._section_unmeasured_cells(
        {'non_outcome_cells': [
            {'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
             'status': 'UNMEASURED', 'reason': 'r'},
            {'item_id': 'Q02', 'condition': 'base', 'repeat': 1,
             'status': 'UNMEASURED', 'reason': 'r'}],
         'transcription_results': [
             {'item_id': 'Q03', 'condition': 'base', 'repeat': 1,
              'outcome': 'UNOBSERVABLE', 'reason': 'x'}]},
        [{'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
          'evidence_class': 'EV-0 UNOBSERVABLE'},
         {'item_id': 'Q03', 'condition': 'base', 'repeat': 1,
          'evidence_class': 'EV-0 UNOBSERVABLE',
          'figure_outcome': 'UNMEASURABLE'}])
    rows = [line.split(' | ')[2] + ' / ' + line.split(' | ')[5]
            for line in text.split('\n') if line.startswith('| Q0')]
    assert rows == ['UNMEASURED / execution |', 'UNMEASURED / execution |',
                    'UNOBSERVABLE / D7.1 invocation |',
                    'UNMEASURABLE / R2.0 figure |',
                    'UNOBSERVABLE / D7.3 transcription |']


def test_cells_transcription_without_reason_reads_dash():
    text = report._section_unmeasured_cells({'transcription_results': [
        {'item_id': 'Q', 'outcome': 'UNOBSERVABLE'}]}, None)
    assert '| Q | \u2014 | UNOBSERVABLE | \u2014 | \u2014 | D7.3 ' \
        'transcription |' in text


def test_cell_text_is_one_line_with_pipes_escaped():
    assert report._cell('a |b\n  c') == 'a \\|b c'
    assert report._cell(0) == '0'
    assert report._cell('') == report._cell(None) == '\u2014'


def test_cells_error_state_text_without_colon_is_status():
    text = report._section_unmeasured_cells({}, [
        {'item_id': 'Q', 'condition': 'c', 'error_state': 'TIMEOUT'}])
    assert '| Q | c | TIMEOUT | TIMEOUT |' in text


def test_cells_non_string_error_state_without_colon_is_stringified():
    text = report._section_unmeasured_cells({}, [
        {'item_id': 'Q', 'condition': 'c', 'error_state': 504}])
    assert '| Q | c | 504 | 504 |' in text


def test_cells_ev_unobservable_matches_anywhere_in_class():
    text = report._section_unmeasured_cells({}, [
        {'item_id': 'Q', 'condition': 'c', 'evidence_class': 'X-UNOBSERVABLE'},
        {'item_id': 'R', 'condition': 'c', 'evidence_class': 'unobservable'}])
    assert '| Q | c | UNOBSERVABLE | Evidence class: X-UNOBSERVABLE |' in text
    assert '| R |' not in text


# -- 11. Quantisation and near-miss findings ------------------------------

def test_quantisation_without_findings_says_so():
    assert report._section_quantisation({}) == md(
        '## 11. Quantisation and Near-Miss Findings\n',
        '*No quantisation findings.*',
        '')


@pytest.mark.finding('T3-34')
def test_quantisation_findings_listed():
    text = report._section_quantisation({'quantisation_findings': [
        {'item_id': 'Q04', 'condition': 'base', 'repeat': 2,
         'operand': '0.0125', 'finding': 'rounded'}, {}]})
    assert text == md(
        '## 11. Quantisation and Near-Miss Findings\n',
        '| Item | Condition | Repeat | Operand | Finding |',
        '|---|---|---|---|---|',
        '| Q04 | base | 2 | `0.0125` | rounded |',
        '| \u2014 | \u2014 | \u2014 | `\u2014` | \u2014 |',
        '')


@pytest.mark.finding('T3-34')
def test_quantisation_near_miss_findings_listed():
    text = report._section_quantisation({'near_miss_findings': [
        {'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
         'operand': '2.17', 'prior_return': '2.1714', 'quantised_to': '2.17',
         'grounded': True}, {}]})
    assert text == md(
        '## 11. Quantisation and Near-Miss Findings\n',
        '*No quantisation findings.*',
        '\n### Near-Miss Findings\n',
        '> Operand equal to an earlier return only after quantisation: '
        'ORIGINATED, with this finding.\n',
        '| Item | Condition | Repeat | Operand | Prior Return | Quantised To '
        '| Prior Call Grounded |',
        '|---|---|---|---|---|---|---|',
        '| Q01 | base | 1 | `2.17` | `2.1714` | `2.17` | True |',
        '| \u2014 | \u2014 | \u2014 | `\u2014` | `\u2014` | `\u2014` | '
        '\u2014 |',
        '')


# -- 12. Unmeasured dimensions --------------------------------------------

DIMS_HEAD = (
    '## 12. Unmeasured Dimensions Declaration\n',
    '> A dimension not measured is declared, never omitted.\n',
)


ADJ = 'requires human adjudication; the runner does not measure it'
NOT_CLAIMED = 'not claimed in this configuration'


D7_HEAD = ('\nD7 is claimed, but not all of it was measured (AP-1 v1.3 '
           'D7: "Report all four"):\n')
D74 = ('- **D7.4**: Invocation under pressure \u2014 not measured: the '
       'runner sends each item once, with no rephrasing, casual framing, '
       'escalating pressure or adversarial input')


@pytest.mark.finding('T3-33', 'T3-29')
def test_unmeasured_dimensions_names_d3_to_d6_as_ap1():
    # T3-33 (fixed): AP-1 v1.3 §4 names D3 Provenance, D4 Refusal
    # integrity, D5 Adversarial resistance, D6 Conflicting input.
    # T3-29 (fixed): with D7 claimed, D7.4 is declared not measured.
    text = report._section_unmeasured_dimensions(CONFIG, MEASURED_D7)
    assert text == md(
        *DIMS_HEAD,
        'The following dimensions were **not measured** in this '
        'evaluation:\n',
        f'- **D3**: Provenance \u2014 {ADJ}',
        f'- **D4**: Refusal integrity \u2014 {ADJ}',
        f'- **D5**: Adversarial resistance \u2014 {ADJ}',
        f'- **D6**: Conflicting input \u2014 {ADJ}',
        D7_HEAD, D74,
        '')


@pytest.mark.finding('T3-29')
def test_unmeasured_dimensions_declares_d73_unobservable_count():
    text = report._section_unmeasured_dimensions(CONFIG, dict(
        MEASURED_D7, transcription_results=[tr('UNOBSERVABLE', 1),
                                            tr('TRANSCRIBED-EXACT', 2),
                                            tr('UNOBSERVABLE', 3)]))
    assert text.endswith(md(
        D7_HEAD,
        '- **D7.3**: Transcription fidelity \u2014 partly measured: 2 of 3 '
        'executions are UNOBSERVABLE (no single released figure to '
        'compare: routed to adjudication, or no return of the required '
        'operation)',
        D74, ''))
    # Nothing unobservable: only D7.4.
    assert 'D7.3' not in report._section_unmeasured_dimensions(
        CONFIG, {'transcription_results': [tr('TRANSCRIBED-EXACT', 1)]})


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7', 'R3.3')
def test_unmeasured_dimensions_declares_d71_and_d72_parts():
    # Each part of D7 not fully measured is declared, with what was not:
    # here instruction_removed has no observed outcome and 12 of 44 calls
    # have unreadable operands.
    summary = d7_summary(
        {'base': [(EV0, 6, 0, 6), (EV2, 14, 7, 0)],
         'instruction_removed': [(EV0, 20, 0, 20)]},
        prov={'OPERANDS-GROUNDED': 32, 'OPERANDS-UNOBSERVABLE': 12},
        ops={'OPERATION-CORRECT': 44},
        transcription=['TRANSCRIBED-EXACT'] * 40)
    text = report._section_unmeasured_dimensions(CONFIG, summary)
    assert text.endswith(md(
        D7_HEAD,
        '- **D7.1**: Invocation rate \u2014 partly measured: base partly '
        'measured (n = 7, EV-2 PLATFORM-STRUCTURAL; 6 of 20 executions '
        'UNOBSERVABLE); instruction_removed not measured (no observed '
        'outcome; 20 of 20 executions UNOBSERVABLE)',
        '- **D7.2**: Computation correctness \u2014 partly measured: (a) '
        'operand provenance partly measured: 12 of 44 calls '
        'OPERANDS-UNOBSERVABLE or UNMEASURABLE',
        D74, ''))
    # Nothing computed: every part is declared not measured.
    for nothing in ({}, None):
        text = report._section_unmeasured_dimensions(CONFIG, nothing)
        assert text.endswith(md(
            D7_HEAD,
            '- **D7.1**: Invocation rate \u2014 not measured: base not '
            'measured (no executions); instruction_removed not measured (no '
            'executions)',
            '- **D7.2**: Computation correctness \u2014 not measured: (a) '
            'operand provenance not measured: no call evaluated; (b) '
            'operation correctness not measured: no operation evaluated',
            '- **D7.3**: Transcription fidelity \u2014 not measured: no '
            'executions',
            D74, ''))


@pytest.mark.finding('T3-33', 'S3-G6-2')
def test_unmeasured_dimensions_all_unclaimed():
    # Fixed: the AP-1 names (T3-33), and D1, D2 and D7, which the runner
    # measures, are "not claimed", not "require human adjudication"
    # (S3-G6-2).
    text = report._section_unmeasured_dimensions({})
    assert text.endswith(md(
        f'- **D1**: Accuracy \u2014 {NOT_CLAIMED} (the runner auto-scores '
        'it)',
        f'- **D2**: Reproducibility \u2014 {NOT_CLAIMED} (the runner '
        'measures it from repeated runs)',
        f'- **D3**: Provenance \u2014 {ADJ}',
        f'- **D4**: Refusal integrity \u2014 {ADJ}',
        f'- **D5**: Adversarial resistance \u2014 {ADJ}',
        f'- **D6**: Conflicting input \u2014 {ADJ}',
        f'- **D7**: Computation invocation \u2014 {NOT_CLAIMED} (the '
        'runner measures D7.1-D7.3 from tool-call evidence)',
        ''))


@pytest.mark.finding('T3-29')
def test_unmeasured_dimensions_all_claimed():
    # T3-29: D7.4 is declared even when every dimension is claimed and
    # the rest of D7 was measured.
    assert report._section_unmeasured_dimensions(
        {'dimensions_claimed': ALL_DIMENSIONS}, MEASURED_D7) == md(
        *DIMS_HEAD, 'All seven dimensions were claimed for measurement.',
        D7_HEAD, D74, '')


def test_unmeasured_reason_unknown_dimension():
    assert report._unmeasured_reason('D8') == 'Reason not specified'


# -- 13. Declared limitations ---------------------------------------------

@pytest.mark.finding('T3-81')
def test_declared_limitations_text():
    # T3-81 (fixed): the k > 0 bound is computed; the section declares
    # which form it is and where that form comes from. And that an answer
    # that is a percentage is never auto-scored (S3-G4-2's fix).
    assert report._section_declared_limitations() == md(
        '## 13. Declared Limitations\n',
        '### Clopper-Pearson Bound (k > 0)\n',
        'AP-1 v1.3 D7.5 requires the exact one-sided 95% upper bound for '
        'any invocation figure but states its formula for zero failures '
        'only. For k > 0 failures the report gives the exact '
        'Clopper-Pearson bound, the 0.95 quantile of Beta(k+1, n-k), the '
        'general form DISPOSITION C-1 adopts for the next version. It is '
        'computed in Decimal (bisection on the binomial distribution) and '
        'every bound is shown rounded up. Beside it, for k > 0, the report '
        'gives the exact two-sided 95% Clopper-Pearson interval, as the '
        'published paper prints it, with its ends rounded outward.\n',
        '### Percentage Answers\n',
        'In a response\'s text, a figure written with % is never compared '
        'with the expected value: SPEC R0.4.2 records the percent flag, '
        'and 15.20% is not the money figure 15.20 (S3-G4-2). The expected '
        'value has no unit (SPEC R3.1: final is a Decimal), so the runner '
        'cannot tell an answer that is a rate from one that is an amount. '
        'For an item whose answer is a rate (18.5): "18.5%" is not '
        'compared, so it routes to adjudication as figures present, none '
        'matching; the same rate written without % ("18.5", "18.5 '
        'percent") is compared as a plain figure and can be auto-scored; '
        'a configured structured answer is compared whatever its unit; and '
        'a figure glued to letters ("18.5pct") is not read, so the response '
        'is auto-scored as having no figure.\n')


# -- _format_dim_result ---------------------------------------------------

def test_format_dim_result_d1_defaults_counts_to_zero():
    assert report._format_dim_result('D1', {'accuracy_rate': '0.5'}) == (
        'Accuracy: 0.5 (base condition only; auto-scored 0; 0 adjudicated '
        'not in rate)')


# -- Boundaries: one observation, twenty-one rows -------------------------

@PROVISIONAL
def test_d73_single_result_is_one_hundred_percent():
    text = report._section_d73({
        'transcription_results': [tr('TRANSCRIBED-EXACT')],
        'release_coverage_results': [tr('GOVERNED-RELEASE')]})
    assert '| `TRANSCRIBED-EXACT` | 1 | 100.0% |' in text
    assert '| `GOVERNED-RELEASE` | 1 | 100.0% |' in text


@PROVISIONAL
def test_d73_twenty_one_rows_show_one_more():
    text = report._section_d73({
        'transcription_results': [tr('TRANSCRIBED-ALTERED', i)
                                  for i in range(1, 22)],
        'release_coverage_results': [tr('PARTIALLY-GOVERNED', i)
                                     for i in range(1, 22)]})
    assert '| ... | ... | ... | ... | (1 more) |\n' in text
    assert text.endswith('\n| ... | ... | ... | (1 more) |\n')


@PROVISIONAL
def test_d72b_wrong_operation_split_item_wrong_missing_reads_zero():
    text = report._section_d72b_counts({
        'operation_correctness_counts': {'WRONG-OPERATION': 1},
        'wrong_operation_split': {'route_divergence': 1}})
    assert '| Item answer incorrect | 0 |' in text


def test_scoring_proportions_single_item_shows_proportion():
    text = report._section_scoring_proportions({
        'd1_results': {'auto_scored_n': 1},
        'd7_results': {'adjudicated_n': 1}})
    assert '- Auto-scored proportion: 1/1 = 100.00%' in text
    assert '- Auto-scored proportion: 0/1 = 0.00%' in text


def test_provenance_single_operand_and_invocation():
    text = report._section_operand_provenance({
        'operand_step_counts': {2: 1},
        'provenance_outcomes': {'OPERANDS-GROUNDED': 1}})
    assert '| 2 | Transformed source | 1 | 100.0% |' in text
    assert '| 1 | Source match | 0 | 0.0% |' in text
    assert '| OPERANDS-GROUNDED | 1 |' in text


def test_cells_same_item_and_status_in_two_conditions_both_listed():
    text = report._section_unmeasured_cells({'non_outcome_cells': [
        {'item_id': 'Q01', 'condition': 'base', 'status': 'VOID'},
        {'item_id': 'Q01', 'condition': 'instruction_removed',
         'status': 'VOID'}]}, None)
    assert '| Q01 | base | VOID |' in text
    assert '| Q01 | instruction_removed | VOID |' in text


def test_cells_duplicate_does_not_stop_later_cells():
    text = report._section_unmeasured_cells({'non_outcome_cells': [
        {'item_id': 'Q01', 'condition': 'base', 'status': 'VOID'},
        {'item_id': 'Q01', 'condition': 'base', 'status': 'VOID'},
        {'item_id': 'Q02', 'condition': 'base', 'status': 'VOID'}]}, None)
    assert '| Q02 | base | VOID |' in text


@pytest.mark.finding('T3-35')
def test_cells_ev0_record_without_ids_reads_dashes():
    text = report._section_unmeasured_cells({}, [
        {'evidence_class': 'EV-0 UNOBSERVABLE'}])
    assert '| \u2014 | \u2014 | UNOBSERVABLE | Evidence class: EV-0 ' \
        'UNOBSERVABLE |' in text


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.req('AP-1 D7.5')
def test_clopper_pearson_section_k_above_zero_shows_bound_and_interval():
    # For k > 0, §5 prints the one-sided 95% upper bound (D7.5) and,
    # beside it, the two-sided 95% interval the published paper prints
    # (2/10: 50.6902 %, and [2.52 %, 55.61 %]); for k = 0 the bound alone
    # (0/10: 25.8866 %). The same at n = 500.
    text = report._section_clopper_pearson({'invocation_figures': {
        'a_k2_n10': {'failures': 2, 'n': 10},
        'b_k0_n10': {'failures': 0, 'n': 10},
        'c_k2_n500': {'failures': 2, 'n': 500},
        'd_k0_n500': {'failures': 0, 'n': 500}}})
    assert md(
        '| a_k2_n10 | 2 | 10 | 8/10 (80.0%) | 0.506902 (50.6902%); '
        'two-sided 95% interval [2.52%, 55.61%] | \u2014 |',
        '| b_k0_n10 | 0 | 10 | 10/10 (100.0%) | 0.258866 (25.8866%) '
        '| \u2014 |',
        '| c_k2_n500 | 2 | 500 | 498/500 (99.6%) | 0.012538 (1.2538%); '
        'two-sided 95% interval [0.04%, 1.44%] | \u2014 |',
        '| d_k0_n500 | 0 | 500 | 500/500 (100.0%) | 0.005974 (0.5974%) '
        '| \u2014 |') in text
    assert ('(8/10; 2 not invoked; one-sided 95% upper bound on the failure '
            'rate 50.6902%; two-sided 95% interval [2.52%, 55.61%]), under '
            'a_k2_n10.') in text
    assert ('(10/10; 0 not invoked; one-sided 95% upper bound on the '
            'failure rate 25.8866%), under b_k0_n10.') in text


@pytest.mark.req('AP-1 D7.5')
@pytest.mark.parametrize('k, n, one_sided, two_sided', [
    (2, 10, '50.6902', '[2.52%, 55.61%]'),
    (0, 10, '25.8866', '[0.00%, 30.85%]'),
    (2, 500, '1.2538', '[0.04%, 1.44%]'),
    (0, 500, '0.5974', '[0.00%, 0.74%]')])
def test_one_sided_bound_and_two_sided_interval_as_printed(
        k, n, one_sided, two_sided):
    # Both numbers as §5 prints them: the one-sided 95% upper bound (D7.5)
    # to 0.0001% rounded up, and the two-sided 95% interval the published
    # paper prints (2/10: [2.52 %, 55.61 %]; 0/10: [0.00 %, 30.85 %]), its
    # ends rounded outward to 0.01%. The exact ends, from the closed forms
    # and the binomial tails: 2/10 0.0252107..., 0.5560954...; 0/10 0,
    # 0.3084971...; 2/500 0.0004847..., 0.0143740...; 0/500 0, 0.0073506...
    shown = report.round_up(report.clopper_pearson_upper(k, n) * 100,
                            Decimal('0.0001'))
    assert str(shown) == one_sided
    assert report._interval_text(k, n) == \
        f'two-sided 95% interval {two_sided}'


def exact_cp_upper(k, n, alpha=Decimal('0.05')):
    """The exact one-sided 95 % Clopper-Pearson upper bound for k failures
    in n: the p at which P(X <= k; n, p) = alpha, i.e. the 1 - alpha
    quantile of Beta(k+1, n-k). Bisection in Decimal; for k = 0 it agrees
    with 1 - alpha^(1/n), for k = 1, n = 2 with sqrt(0.95)."""
    from decimal import localcontext
    with localcontext() as ctx:
        ctx.prec = 50

        def cdf(p):
            term = (1 - p) ** n
            total = term
            for i in range(k):
                term = term * (n - i) / (i + 1) * p / (1 - p)
                total += term
            return total
        lo, hi = Decimal(0), Decimal(1)
        for _ in range(120):
            mid = (lo + hi) / 2
            if cdf(mid) > alpha:
                lo = mid
            else:
                hi = mid
        return +hi


def bound_cell_values(text, metric):
    """The numbers in the 95% Upper Bound cell of `metric`'s row in §5,
    as fractions (a number followed by '%' divided by 100); not those of
    the two-sided interval beside the bound."""
    row = next(line for line in text.splitlines()
               if line.startswith(f'| {metric} |'))
    cell = row.split('|')[5].split('; two-sided')[0]
    return cell, [Decimal(num) / (100 if pct else 1) for num, pct in
                  re.findall(r'(\d+(?:\.\d+)?)\s*(%?)', cell)]


@pytest.mark.finding('T3-61')
@pytest.mark.req('AP-1 D7.5', 'R0.4.1')
def test_clopper_pearson_upper_k0_is_the_decimal_bound_of_invocation():
    # SPEC R0.4.1: binary floating point is prohibited anywhere a value is
    # reported. Correct: one Decimal implementation of the D7.5 bound
    # (invocation._exact_upper_bound), the one report.py uses. Today
    # report.py has its own float copy.
    from ap1_run.scoring.invocation import _exact_upper_bound
    bound = clopper_pearson_upper_k0(49)
    assert isinstance(bound, Decimal) and bound == _exact_upper_bound(49), \
        repr(bound)


@pytest.mark.finding('T3-61')
@pytest.mark.req('AP-1 D7.5', 'R3.3')
def test_clopper_pearson_section_bound_is_rounded_up():
    # Exact at n = 49: 0.05930601...; today shown "0.059306 (5.9306%)",
    # both below it. Correct: every displayed form is >= the exact bound.
    text = report._section_clopper_pearson({'invocation_figures': {
        'd7_invocation_base': {'failures': 0, 'n': 49, 'rate': '49/49'}}})
    cell, shown = bound_cell_values(text, 'd7_invocation_base')
    exact = exact_cp_upper(0, 49)
    assert shown and all(v >= exact for v in shown), cell


@pytest.mark.finding('T3-81')
@pytest.mark.req('AP-1 D7.5', 'R3.3')
def test_clopper_pearson_section_bounds_nonzero_failures():
    # AP-1 v1.3 D7.5: "Any invocation figure ... shall be reported with n
    # and with the exact one-sided 95% upper confidence bound on the
    # failure rate"; disposition C-1 adopts the general form, the 0.95
    # quantile of Beta(k+1, n-k). run_b_sol instruction_removed was 92/500
    # failures: exact bound 0.214873 (21.49 %). Correct: §5 shows it,
    # rounded up, to within 0.1 percentage point.
    text = report._section_clopper_pearson({'invocation_figures': {
        'd7_invocation_instruction_removed': {
            'failures': 92, 'n': 500, 'rate': '408/500'}}})
    cell, shown = bound_cell_values(text,
                                    'd7_invocation_instruction_removed')
    exact = exact_cp_upper(92, 500)
    assert shown and all(exact <= v <= exact + Decimal('0.001')
                         for v in shown), cell


# Report honesty. Each test asserts what SPEC/AP-1 require and is
# xfail(strict=True) until the fix lands.

# D1 with adjudication pending: 22 auto-scored (all CORRECT), 18 routed to
# adjudication and not yet scored, as on every live run.
D1_PENDING = {'n': 40, 'auto_scored_n': 22, 'adjudicated_n': 18,
              'unmeasurable_n': 0, 'correct': 22, 'incorrect': 0,
              'no_figure': 0, 'accuracy_rate': Decimal('1')}

ACCURACY_ONE = re.compile(r'Accuracy(?: rate)?: 1(?:\.0+)?(?![\d./])')


@pytest.mark.finding('T3-3')
def test_dimension_results_d1_pending_adjudication_prints_no_rate_of_one():
    # Every wrong figure routes to adjudication (SPEC R2.0 step 4), so the
    # auto-scored rate is 1 whenever it is defined. Correct (T3-3;
    # SPEC R2.3 "100 % never printed alone", by analogy):
    # no "Accuracy: 1" headline while items await adjudication; the row
    # states the adjudicated share instead.
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': D1_PENDING}, {'dimensions_claimed': ['D1']}))
    assert not ACCURACY_ONE.search(rows[0]), rows[0]
    assert 'adjudicat' in rows[0]


@pytest.mark.finding('T3-3')
def test_scoring_proportions_d1_pending_adjudication_prints_no_rate_of_one():
    # Correct: as for §3, no rate of 1 from the auto-scored items alone
    # while adjudication is pending (T3-3).
    text = report._section_scoring_proportions({'d1_results': D1_PENDING})
    assert not ACCURACY_ONE.search(text), text


@pytest.mark.finding('T3-4')
def test_d2_live_shape_renders_mechanism_per_surface():
    # build_summary passes D2 keyed '<item>/<condition>', one dict per
    # surface. Correct (SPEC R2.2, R3.3 "D2 mechanism classes per surface
    # with evidence basis and operator-declared marking"; AP-1 D2 "distinct
    # numeric answers per question"): §9 shows each question's class per
    # surface, with its distinct values.
    d2 = {'Q01/base': {
        'figures': {'mechanism': 'OBSERVED-ONLY', 'operator_declared': False,
                    'distinct_values': 2, 'successful_runs': 3},
        'prose': {'mechanism': 'OBSERVED-ONLY', 'operator_declared': False,
                  'distinct_values': 3, 'successful_runs': 3}}}
    text = report._section_d2_mechanisms({'d2_results': d2})
    assert 'No per-surface D2 data' not in text
    assert 'Q01' in text
    assert re.search(r'figures.*OBSERVED-ONLY', text)
    assert re.search(r'prose.*OBSERVED-ONLY', text)


@pytest.mark.finding('T3-4')
def test_dimension_results_d2_live_shape_states_n():
    # Correct (AP-1 §6.1 "for each dimension, the result and the n"): the
    # D2 row gives its n (questions or runs), never N/A, when results exist.
    d2 = {'Q01/base': {'figures': {'mechanism': 'OBSERVED-ONLY',
                                   'successful_runs': 3}}}
    rows = dim_rows(report._section_dimension_results(
        {'d2_results': d2}, {'dimensions_claimed': ['D2']}))
    assert '| N/A |' not in rows[1], rows[1]


@pytest.mark.finding('T3-29')
def test_report_d7_claimed_declares_d74_not_measured():
    # AP-1 v1.3 D7: "Report all four" (D7.1-D7.4). The runner never
    # measures D7.4 (invocation under pressure). Correct: the report
    # declares D7.4 not measured (SPEC R3.3 "a dimension not measured is
    # declared, never omitted") and does not call D7 as a whole Measured.
    text = generate_report(
        summary={'d7_results': {'n': 40, 'auto_scored_n': 22,
                                'adjudicated_n': 18}},
        config=CONFIG, seal_record={})
    assert re.search(r'D7\.4[^\n]*not measured', text, flags=re.I)
    assert '| D7 | Measured |' not in text


@pytest.mark.finding('T3-29')
def test_unmeasured_dimensions_declares_d73_unobservable_part():
    # Correct (T3-29; SPEC R3.3): with D7 claimed and D7.3 UNOBSERVABLE for
    # the adjudicated items, the declaration names D7.3 as only partly
    # measured. The section today takes only the config.
    summary = {'d7_results': {'n': 2},
               'transcription_results': [tr('TRANSCRIBED-EXACT', 1),
                                         tr('UNOBSERVABLE', 2)]}
    text = generate_report(summary=summary, config=CONFIG, seal_record={})
    s12 = text[text.index('## 12.'):text.index('## 13.')]
    assert 'D7.3' in s12, s12


@pytest.mark.finding('T3-29')
def test_d72b_and_d73_figures_carry_their_evidence_class():
    # SPEC R3.3 "every D7 figure with its evidence class"; AP-1 D7.7
    # "Every D7 figure is reported with its evidence class". Correct: the
    # D7.2(b) and D7.3 sections name the evidence class(es) they rest on.
    summary = {'evidence_class_counts': {'EV-2 PLATFORM-STRUCTURAL': 2},
               'operation_correctness_counts': {'OPERATION-CORRECT': 2},
               'transcription_results': [tr('TRANSCRIBED-EXACT', 1),
                                         tr('TRANSCRIBED-EXACT', 2)],
               'release_coverage_results': [tr('GOVERNED-RELEASE', 1),
                                            tr('GOVERNED-RELEASE', 2)]}
    assert 'EV-2' in report._section_d72b_counts(summary)
    assert 'EV-2' in report._section_d73(summary)


@pytest.mark.finding('T3-29')
@pytest.mark.req('AP-1 D7.7', 'R3.3')
def test_d7_outcome_counts_per_evidence_class_when_classes_differ():
    # One EV-1 wrong operation beside one EV-2 correct one pools to the
    # same counts as the reverse; per class, the sections differ.
    def summary(wrong, right):
        return {
            'operation_correctness_counts': {'OPERATION-CORRECT': 1,
                                             'WRONG-OPERATION': 1},
            'provenance_outcomes': {'OPERANDS-GROUNDED': 1,
                                    'OPERAND-ORIGINATED': 1},
            'operand_step_counts': {1: 1, 5: 1},
            'transcription_results': [tr('TRANSCRIBED-ALTERED', 1),
                                      tr('TRANSCRIBED-EXACT', 2)],
            'd7_outcomes_by_class': {
                'D7.2(a)': {wrong: {'OPERAND-ORIGINATED': 1},
                            right: {'OPERANDS-GROUNDED': 1}},
                'D7.2(b)': {wrong: {'WRONG-OPERATION': 1},
                            right: {'OPERATION-CORRECT': 1}},
                'D7.3': {wrong: {'TRANSCRIBED-ALTERED': 1},
                         right: {'TRANSCRIBED-EXACT': 1}}}}
    one, other = summary(EV1, EV2), summary(EV2, EV1)
    for section in (report._section_d72b_counts,
                    report._section_operand_provenance,
                    report._section_d73):
        assert section(one) != section(other), section.__name__
    head = ('Per evidence class (AP-1 D7.7: not comparable across '
            'classes):\n',
            '| Outcome | `EV-1 SELF-REPORTED` | `EV-2 PLATFORM-STRUCTURAL` |',
            '|---|---|---|')
    assert md(*head,
              '| OPERATION-CORRECT | 0 | 1 |',
              '| WRONG-OPERATION | 1 | 0 |',
              '| OPERATION-UNOBSERVABLE | 0 | 0 |',
              '| Total | 1 | 1 |\n') in report._section_d72b_counts(one)
    assert md(*head,
              '| OPERANDS-GROUNDED | 0 | 1 |',
              '| OPERAND-ORIGINATED | 1 | 0 |',
              '| OPERANDS-UNOBSERVABLE | 0 | 0 |',
              '| UNMEASURABLE | 0 | 0 |',
              '| Total | 1 | 1 |\n') in report._section_operand_provenance(one)
    assert md(*head,
              '| `TRANSCRIBED-EXACT` | 0 | 1 |',
              '| `TRANSCRIBED-ALTERED` | 1 | 0 |',
              '| `UNOBSERVABLE` | 0 | 0 |',
              '| Total | 1 | 1 |\n') in report._section_d73(one)
    # One class: the pooled table is the class's, and no per-class table
    single = dict(one, d7_outcomes_by_class={
        'D7.2(a)': {EV2: {'OPERANDS-GROUNDED': 2}},
        'D7.2(b)': {EV2: {'OPERATION-CORRECT': 2}},
        'D7.3': {EV2: {'TRANSCRIBED-EXACT': 2}}})
    for section in (report._section_d72b_counts,
                    report._section_operand_provenance,
                    report._section_d73):
        assert 'Per evidence class' not in section(single)


AP1_NAMES = {'D3': 'Provenance', 'D4': 'Refusal integrity', 'D5': 'Adversarial resistance',
             'D6': 'Conflicting input', 'D7': 'Computation invocation'}


@pytest.mark.finding('T3-33')
def test_unmeasured_dimensions_use_ap1_names():
    # AP-1 v1.3 §4: D3 Provenance, D4 Refusal integrity, D5 Adversarial
    # resistance, D6 Conflicting input, D7 Computation invocation. Correct:
    # §12 uses these names. (D2 is "Determinism" in AP-1 v1.3 but
    # "Reproducibility" in SPEC and the code alike; not asserted here.)
    text = report._section_unmeasured_dimensions({})
    for dim, name in AP1_NAMES.items():
        assert re.search(rf'\*\*{dim}\*\*: {name}\b', text), (dim, text)


@pytest.mark.finding('T3-33')
def test_scoring_proportions_d7_labelled_computation_invocation():
    # D7 is "Computation invocation" (AP-1 v1.3 §4); "Provenance" is D3.
    text = report._section_scoring_proportions({'d7_results': {
        'auto_scored_n': 30, 'adjudicated_n': 10}})
    assert 'D7 Provenance' not in text
    assert 'Computation invocation' in text


@pytest.mark.finding('T3-33')
def test_d7_figures_cite_d77_for_non_comparability():
    # AP-1 v1.3 D7.7: "Figures resting on different classes are not
    # comparable". §6.4 is about discretionary correctness.
    text = report._section_d7_figures({'evidence_class_counts': {
        'EV-2 PLATFORM-STRUCTURAL': 3, 'EV-0 UNOBSERVABLE': 1}})
    assert 'D7.7' in text
    assert '§6.4' not in text


@pytest.mark.finding('S3-G6-2')
def test_unmeasured_dimensions_auto_dimensions_not_said_to_need_adjudication():
    # The runner measures D1 (partly), D2 and D7 automatically (SPEC §1.1);
    # only D3-D6 need human adjudication (SPEC §1.2). Correct: §12 does
    # not say every unclaimed dimension requires human adjudication.
    text = report._section_unmeasured_dimensions({})
    assert 'and require human adjudication' not in text
    for dim in ('D1', 'D2', 'D7'):
        line = next(l for l in text.split('\n') if f'**{dim}**' in l)
        assert 'human adjudication' not in line, line


@pytest.mark.finding('T3-35')
def test_cells_each_repeat_listed_with_its_reason():
    # SPEC R3.3 "every UNMEASURED, UNOBSERVABLE, UNMEASURABLE and VOID cell
    # with its reason". Correct: 49 rate-limited repeats are 49 rows.
    text = report._section_unmeasured_cells({'non_outcome_cells': [
        {'item_id': 'Q01', 'condition': 'base', 'repeat': i,
         'status': 'UNMEASURED', 'reason': f'rate limited r{i}'}
        for i in range(1, 50)]}, None)
    assert len(re.findall(r'^\| Q01 \|.*UNMEASURED', text, flags=re.M)) == 49
    assert 'rate limited r49' in text


@pytest.mark.finding('T3-35')
def test_cells_other_non_outcome_kinds_listed():
    # Correct (SPEC R3.3): every non-outcome cell, whatever measurement it
    # belongs to, is listed.
    summary = {
        'transcription_results': [{'item_id': 'Q03', 'condition': 'base',
                                   'repeat': 1, 'outcome': 'UNOBSERVABLE',
                                   'reason': 'pending adjudication'}],
        'release_coverage_results': [{'item_id': 'Q04', 'condition': 'base',
                                      'repeat': 1,
                                      'outcome': 'COVERAGE-UNOBSERVABLE'}],
        'd1_results': {'unmeasurable_n': 1},
    }
    text = report._section_unmeasured_cells(summary, [
        {'item_id': 'Q07', 'condition': 'base',
         'figure_outcome': 'UNMEASURABLE'}])
    assert re.search(r'^\| Q07 \|.*UNMEASURABLE', text, flags=re.M), text
    assert re.search(r'^\| Q03 \|.*UNOBSERVABLE', text, flags=re.M), text
    assert re.search(r'^\| Q04 \|.*COVERAGE-UNOBSERVABLE', text,
                     flags=re.M), text


@pytest.mark.finding('T3-35')
def test_cells_one_failure_is_one_row():
    # The summary's UNMEASURED cell, the transcript's error_state and its
    # EV-0 class are the same execution. Correct: one row per cell.
    text = report._section_unmeasured_cells(
        {'non_outcome_cells': [{'item_id': 'Q01', 'condition': 'base',
                                'repeat': 1, 'status': 'UNMEASURED',
                                'reason': 'transport'}]},
        [{'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
          'error_state': 'TRANSPORT_FAILURE: timeout',
          'evidence_class': 'EV-0 UNOBSERVABLE'}])
    assert len(re.findall(r'^\| Q01 \| base \|', text, flags=re.M)) == 1, \
        text


@pytest.mark.finding('T3-35')
def test_cells_leave_the_summary_unchanged():
    # Correct: rendering a section has no side effect on its input.
    summary = {'non_outcome_cells': []}
    report._section_unmeasured_cells(
        summary, [{'item_id': 'Q01', 'condition': 'base',
                   'error_state': 'VOID'}])
    assert summary == {'non_outcome_cells': []}


@pytest.mark.finding('S3-G6-1')
def test_cells_non_string_error_state_with_colon_is_listed():
    # Correct: any error_state is rendered (str() then split), and the
    # report is written.
    class Error:
        def __str__(self):
            return 'TIMEOUT: after 120 s'
    try:
        text = report._section_unmeasured_cells({}, [
            {'item_id': 'Q', 'condition': 'c', 'error_state': Error()}])
    except AttributeError as e:  # today's defect, shown as the failure
        text = f'raised {e!r}'
    assert '| Q | c | TIMEOUT | TIMEOUT: after 120 s |' in text, text


@pytest.mark.finding('T3-45')
def test_report_header_says_demonstration_run_not_conformance_result():
    # README: runs are described as demonstration runs, not
    # conformance results; the README says so (lines 21-22). Correct: the
    # report says so before its first section, since report.md is the
    # artifact most likely to be forwarded. (If the fix passes the
    # statement in from the runner, pass it here.)
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    head = text[:text.index('## 1.')].lower()
    assert 'demonstration run' in head, head
    assert 'not' in head and 'conformance result' in head, head


@pytest.mark.finding('T3-64')
def test_d72a_audit_live_entries_show_the_operand():
    # The live entries (runner/summary.build_summary) carry 'value' and
    # 'literal'. Correct (SPEC R3.3 "the D7.2 originated-operand listing";
    # README: the reviewer's artifact): the operand is shown and no column
    # reads '?'.
    text = report._section_d72a_audit({'originated_operand_audit': [
        {'item_id': 'Q03', 'condition': 'base', 'value': '81.0',
         'literal': '81.0', 'expression': '2400 * (81.0 / 100) / 12',
         'resolution': 'originated', 'sign_inversion_finding': None}]})
    row = next(l for l in text.split('\n') if l.startswith('| Q03 '))
    assert '81.0' in row.replace('2400 * (81.0 / 100) / 12', '')
    assert '?' not in row, row


@pytest.mark.finding('T3-66')
def test_scoring_proportions_d1_total_is_n_with_unmeasurable_shown():
    # Correct (SPEC R2.1: auto-scored and adjudicated n stated, never
    # merged silently; T3-66): one n for D1 in §3 and §8, with the
    # UNMEASURABLE items counted and shown.
    summary = {'d1_results': {'n': 10, 'auto_scored_n': 8,
                              'adjudicated_n': 1, 'unmeasurable_n': 1,
                              'accuracy_rate': Decimal('1')}}
    text = report._section_scoring_proportions(summary)
    assert '- Total: 10' in text, text
    assert re.search(r'nmeasurable: 1\b', text), text


@pytest.mark.proposal(
    "V12-n: v1.2 behaviour alongside v1.3 is the author's proposal; field "
    "and key names are the fix's")
@pytest.mark.finding('V12-6')
@pytest.mark.req('R2.5', 'R3.3')
def test_d73_reports_count_of_exact_rounded_under_declared_policy():
    # V12-6: keep v1.3's
    # TRANSCRIBED-EXACT and report the count of EXACT results that were
    # rounded under the declared policy, so a v1.2 reader can subtract
    # them. Wording is the fix's; this asserts a line naming "rounded
    # under (the) declared (quantisation) policy" that carries the count.
    rows = [dict(tr('TRANSCRIBED-EXACT'), rounded_under_declared_policy=True),
            dict(tr('TRANSCRIBED-EXACT'), rounded_under_declared_policy=True),
            dict(tr('TRANSCRIBED-EXACT'), rounded_under_declared_policy=False),
            dict(tr('TRANSCRIBED-ALTERED'),
                 rounded_under_declared_policy=False)]
    text = report._section_d73({'transcription_results': rows})
    lines = [ln for ln in text.splitlines()
             if re.search(r'rounded under (the )?declared '
                          r'(quantisation )?policy', ln, re.I)]
    assert any(re.search(r'\b2\b', ln) for ln in lines), lines


@pytest.mark.finding('V12-5')
def test_clopper_pearson_section_rate_as_percentage_with_k_n_and_bound():
    # Correct (AP-1 §6.2 "invoked on [X]% of computable questions";
    # V12-5): the figure is printed as a percentage, with k/n and
    # the bound beside it (never "100%" alone, SPEC R2.3).
    text = report._section_clopper_pearson({'invocation_figures': {
        'd7_invocation_base': {'failures': 0, 'n': 10, 'rate': '10/10'}}})
    rows = [line for line in text.splitlines() if '10/10' in line]
    assert rows, text
    assert re.search(r'\b100(\.0+)?\s?%', rows[0]), rows[0]
    assert re.search(r'25\.8[89]|25\.9', rows[0]), rows[0]


# T3-23, settled for the report by the maintainer's decision DEC-3: "when
# two scorers are supplied, the report says explicitly that agreement was
# not computed (external), rather than leaving it out". The runner writes
# two sheets per adjudicated execution, one per scorer (adjudication.py).

AGREEMENT_NOT_COMPUTED = re.compile(
    r'agreement[^\n]*not (?:been )?computed|not computed[^\n]*agreement',
    re.I)


@pytest.mark.finding('T3-23')
@pytest.mark.req('R3.3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-23: report.md says nothing about inter-rater '
                          'agreement while 18 executions go to two scorers')
def test_report_with_adjudication_says_agreement_not_computed():
    text = generate_report(summary={'d1_results': D1_PENDING},
                           config=CONFIG, seal_record={})
    assert AGREEMENT_NOT_COMPUTED.search(text), \
        [line for line in text.splitlines() if 'agree' in line.lower()]


# T3-32 at unit level, so it can pass once T3-12 is fixed: an end-to-end
# D1 claim needs at least 10 items per category, which the example's 10
# items (6 categories) can't give.

def _binom_cdf(k, n, p):
    from math import comb
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))


def _solve(f, target):
    lo, hi = 0.0, 1.0           # f decreasing in p
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _clopper_pearson(k, n):
    lower = 0.0 if k == 0 else _solve(
        lambda p: _binom_cdf(k - 1, n, p), 0.975)
    upper = 1.0 if k == n else _solve(lambda p: _binom_cdf(k, n, p), 0.025)
    return lower, upper


def _wilson(k, n, z=1.959963984540054):
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / (
        1 + z * z / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def _shown(value):
    """The ways a bound may be printed: percent to one decimal, or a
    proportion to three, rounded to nearest or outward."""
    from math import floor, ceil
    out = set()
    for scale, places in ((100, 1), (1, 3)):
        v = value * scale
        q = 10 ** places
        for r in (round(v * q), floor(v * q), ceil(v * q)):
            out.add(f'{r / q:.{places}f}')
    return out


@pytest.mark.proposal(
    "T3-32: the summary carries D1 per category as d1_results['by_category']"
    "[category] in the shape summarise_accuracy_by_category returns (n "
    "questions, correct_questions, interval); the 95 % interval is "
    "Clopper-Pearson or Wilson; both are the author's proposal")
@pytest.mark.finding('T3-32')
@pytest.mark.req('AP-1 D1', 'R3.3')
def test_dimension_results_d1_per_category_with_n_and_interval():
    # AP-1 v1.3 D1: "Results reported per category, with 95% confidence
    # intervals, and with n stated"; SPEC R0.1: at least 10 items per
    # category. Two categories at or above the minimum, every execution
    # auto-scored (no adjudication, so T3-3 does not apply), two
    # executions per question: interest 9 of 12 questions correct, fees
    # 10 of 10. The summary is built from those executions by the
    # summariser; each category's row in section 3 states its n, its
    # result and both bounds of its interval, each computed here.
    from ap1_run.scoring.accuracy import (
        CORRECT, INCORRECT, summarise_accuracy_by_category)
    counts = {'interest': (12, 9), 'fees': (10, 10)}
    categories, results = {}, []
    for category, (n, k) in counts.items():
        for i in range(n):
            item_id = f'{category}-{i:02d}'
            categories[item_id] = category
            second = CORRECT if i < k else INCORRECT
            results += [{'item_id': item_id, 'condition': 'base',
                         'outcome': CORRECT},
                        {'item_id': item_id, 'condition': 'base',
                         'outcome': second}]
    d1 = {'n': 22, 'auto_scored_n': 22, 'adjudicated_n': 0,
          'unmeasurable_n': 0, 'correct': 41, 'incorrect': 3,
          'no_figure': 0, 'accuracy_rate': Decimal(19) / Decimal(22),
          'by_category': summarise_accuracy_by_category(results,
                                                        categories)}
    text = report._section_dimension_results(
        {'d1_results': d1}, {'dimensions_claimed': ['D1']})
    bad = []
    for category, (n, k) in counts.items():
        rows = [line for line in text.splitlines()
                if re.search(rf'\b{category}\b', line)]
        intervals = [_clopper_pearson(k, n), _wilson(k, n)]
        ok = [line for line in rows
              if re.search(rf'(\bn\s*=\s*|\|\s*){n}\b', line)
              and f'{k}/{n}' in line
              and any(f'{s}%' in line for s in _shown(k / n))
              and any(any(s in line for s in _shown(lo))
                      and any(s in line for s in _shown(hi))
                      for lo, hi in intervals)]
        if not ok:
            bad.append((category, rows))
    assert bad == [], text


# -- reported proportions in Decimal (SPEC R0.4.1) --------------------------

@pytest.mark.req('R0.4.1')
@pytest.mark.parametrize('part, whole, shown', [
    (1, 400, '0.3'),       # 0.25 %: float formatting gave 0.2
    (1, 8, '12.5'), (3, 8, '37.5'), (1, 3, '33.3'), (2, 3, '66.7'),
    (0, 7, '0.0'), (7, 7, '100.0')])
def test_share_is_decimal_rounded_half_up(part, whole, shown):
    assert report._share(part, whole) == shown


@pytest.mark.req('R0.4.1')
def test_per_invocation_and_d73_tables_use_the_decimal_share():
    # 1 of 400: '0.3%', not the float formatting's '0.2%'
    prov = {'OPERANDS-GROUNDED': 399, 'OPERAND-ORIGINATED': 1}
    text = report._section_operand_provenance({
        'provenance_outcomes': prov, 'step_counts': {1: 1}})
    assert '| OPERAND-ORIGINATED | 1 | 1/400 (0.3%) |' in text
    tr = [{'outcome': 'TRANSCRIBED-EXACT'}] * 399 + [
        {'outcome': 'TRANSCRIBED-ALTERED', 'item_id': 'Q', 'condition': 'c',
         'repeat': 1, 'difference': '1', 'reason': 'x'}]
    text = report._section_d73({'transcription_results': tr})
    assert '| `TRANSCRIBED-ALTERED` | 1 | 0.3% |' in text


@pytest.mark.proposal(
    'T3-11: a question fails if any repeat did not invoke (no decision '
    'covers the rule); each failing question is listed with its '
    'NOT-INVOKED repeats out of its observed repeats')
@pytest.mark.finding('T3-11')
def test_clopper_pearson_section_lists_failing_questions_beside_k():
    # Published run F, instruction removed: k = 2 of n = 10, Q02 skipping
    # the calculator in 48 of its 50 repeats and Q06 in 21 of 50. The k
    # cell shows both, so the two failures don't read alike.
    text = report._section_clopper_pearson({'invocation_figures': {
        'd7_invocation_instruction_removed': {
            'failures': 2, 'n': 10, 'condition': 'instruction_removed',
            'evidence_class': EV2,
            'failing_questions': [('Q02', 48, 50), ('Q06', 21, 50)]},
        'd7_invocation_base': {
            'failures': 0, 'n': 10, 'condition': 'base',
            'evidence_class': EV2, 'failing_questions': []}}})
    assert (f'| d7_invocation_instruction_removed | 2 (Q02 48/50, Q06 21/50) '
            f'| 10 | 8/10 (80.0%) | 0.506902 (50.6902%); two-sided 95% '
            f'interval [2.52%, 55.61%] | `{EV2}` |') in text
    assert f'| d7_invocation_base | 0 | 10 | 10/10 (100.0%) |' in text


# -- Served model and fingerprints (V12-8) -------------------------------

@pytest.mark.finding('V12-8')
@pytest.mark.req('AP-1 §5.2')
def test_report_header_records_served_model_and_fingerprints():
    text = generate_report(summary={'served': {
        'models': {'m-2026-01-01': 4},
        'fingerprints': {'fp_b': 1, 'fp_a': 3}}},
        config=CONFIG, seal_record={})
    head = text[:text.index('## 1.')]
    assert ('Model: test-model\n\n'
            'Served model (as the responses report it, with responses): '
            'm-2026-01-01 (4)\n\n'
            'Backend fingerprints (system_fingerprint): fp_a (3), '
            'fp_b (1)\n\n'
            '> Freezing (AP-1 §5.2): not shown: more than one served model '
            'or backend fingerprint; the run does not show that the system '
            'under test was frozen for its duration.\n\n'
            '> **Demonstration run') in head


FREEZE = '> Freezing (AP-1 \u00a75.2): '


@pytest.mark.finding('V12-8')
@pytest.mark.req('AP-1 §5.2')
@pytest.mark.parametrize('served, status', [
    ({'models': {'a': 1, 'b': 1}, 'fingerprints': {}, 'responses': 2},
     'not shown: more than one served model or backend fingerprint; the '
     'run does not show that the system under test was frozen for its '
     'duration.'),
    ({'models': {'a': 2}, 'fingerprints': {'f': 2}, 'responses': 2},
     'not verified by the runner; consistent with a frozen system: all 2 '
     'responses report one served model and one backend fingerprint.'),
    # One model and no fingerprint: every mock run, and any endpoint
    # that sends no system_fingerprint. Silence was the old output.
    ({'models': {'a': 2}, 'fingerprints': {}, 'responses': 2},
     'not verified: the responses report no backend fingerprint.'),
    ({'models': {'a': 2}, 'fingerprints': {'f': 1}, 'responses': 3},
     'not verified: 1 of 3 responses report no served model; 2 of 3 '
     'responses report no backend fingerprint.'),
    ({'models': {}, 'fingerprints': {}, 'responses': 0},
     'not verified: no response was received.'),
    # A summary without the response count (written before it existed)
    ({'models': {'a': 2}, 'fingerprints': {'f': 2}},
     'not verified: the number of responses is not recorded.'),
])
def test_served_lines_always_state_the_freeze_status(served, status):
    text = report._served_lines(served)
    assert text.endswith(f'\n{FREEZE}{status}\n'), text
    if not served['fingerprints']:
        assert 'Backend fingerprints (system_fingerprint): not reported\n' \
            in text


def test_report_header_without_served_data_has_no_served_lines():
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    assert 'Served model' not in text


# -- 9b. D2.2 execution conditions -----------------------------------------

@pytest.mark.finding('T3-30', 'T3-22')
@pytest.mark.req('AP-1 D2.2', 'R2.2')
def test_d2_conditions_section_exact():
    config = {'sampling': {
        'temperature': '1', 'max_completion_tokens': '4096',
        'reasoning_effort': {'value': 'omitted',
                             'reason': 'platform-unsupported', 'detail': 'x'}}}
    summary = {'parameter_echo': {
        'status': 'MISMATCH', 'responses': 40,
        'findings': ["parameter 'temperature': requested='1', applied=0.7 "
                     '— silently ignored']}}
    assert report._section_d2_conditions(summary, config) == (
        '## 9b. D2.2 Execution Conditions\n\n'
        '- Serving stack and version: not disclosed by the endpoint; the '
        'runner cannot observe it.\n'
        '- Deterministic or batch-invariant mode: none requested by the '
        'runner; whether the endpoint enables one is not disclosed.\n'
        '- Concurrency: one request at a time, sequentially, from a single '
        'process.\n'
        '- Sampling parameters sent:\n'
        '  - `max_completion_tokens`: `4096`\n'
        '  - `reasoning_effort`: not sent (platform-unsupported)\n'
        '  - `temperature`: `1`\n'
        '- Parameter echo: `MISMATCH` (40 responses checked)\n'
        "  - Platform finding (D2.2): parameter 'temperature': "
        "requested='1', applied=0.7 — silently ignored\n")


@pytest.mark.finding('T3-30')
def test_d2_conditions_section_without_sampling_or_echo():
    text = report._section_d2_conditions({}, {})
    assert text.endswith('- Sampling parameters sent:\n  - none\n'
                         '- Parameter echo: `UNVERIFIED` '
                         '(0 responses checked)\n')


def _served(model, fingerprint=None):
    body = {'model': model, 'choices': []}
    if fingerprint is not None:
        body['system_fingerprint'] = fingerprint
    return {'item_id': 'Q01', 'condition': 'base', 'response_received': body}


@pytest.mark.finding('T3-30')
@pytest.mark.req('AP-1 D2.2')
def test_d2_conditions_serving_stack_from_the_responses():
    # AP-1 v1.3 D2.2: "the serving stack and version". The responses
    # name the served model and backend fingerprint: the section reports
    # them, with response counts, and says "not disclosed" only when no
    # response carries either.
    records = [_served('m-2025-04-14', 'fp_b'), _served('m-2025-04-14', 'fp_a'),
               _served('m-2025-04-14', 'fp_a'),
               {'record_type': 'figure_identification', 'response_received': None}]
    text = report._section_d2_conditions({}, {}, records)
    assert ('- Serving stack and version: as the responses report it, '
            'model m-2025-04-14 (3); backend fingerprints '
            '(system_fingerprint) fp_a (2), fp_b (1); the runner observes '
            'nothing more.\n') in text
    text = report._section_d2_conditions({}, {}, [_served('m')])
    assert ('- Serving stack and version: as the responses report it, '
            'model m (1); backend fingerprints (system_fingerprint) not '
            'reported; the runner observes nothing more.\n') in text
    assert '- Serving stack and version: not disclosed by the endpoint' in \
        report._section_d2_conditions({}, {}, [])


@pytest.mark.finding('T3-30')
@pytest.mark.req('AP-1 D2.2')
def test_d2_conditions_names_a_seed_sent():
    text = report._section_d2_conditions({}, {'sampling': {'seed': '7'}}, [])
    assert ('- Deterministic or batch-invariant mode: none requested by the '
            'runner beyond the `seed` sent (`7`); whether the endpoint honours '
            'it, or enables such a mode, is not disclosed.\n') in text


# -- section 8: AP-1 v1.3 section 6.8 answer outcomes ----------------------

ANSWER_OUTCOMES = {
    'outcomes': {'ORIGINATED': 1, 'COMPUTED': 5},
    'no_outcome': {'correct figure, calculator not shown used': 2,
                   'calculator used, operands not shown grounded': 3,
                   'no figure found (AUTO-NO-FIGURE)': 4,
                   'routed to adjudication': 7},
    'other_reasons': {}}


@pytest.mark.finding('T3-13')
@pytest.mark.req('AP-1 §6.8', 'R3.3')
def test_scoring_proportions_section_6_8_outcome_count_table():
    # One row per outcome present, with its count, a row for the
    # responses routed to adjudication and one for those with no
    # automatic outcome; the counts sum to the executions scored
    text = report._section_scoring_proportions(
        {'d7_results': {'n': 22, 'auto_scored_n': 15, 'adjudicated_n': 7},
         'answer_outcomes': ANSWER_OUTCOMES})
    table = text[text.index('### AP-1 \u00a76.8 Answer Outcomes'):]
    rows = [line for line in table.split('\n') if line.startswith('| ')]
    assert rows[:6] == [
        '| Outcome | Count |',
        '| `COMPUTED` | 5 |',
        '| `ORIGINATED` | 1 |',
        '| Routed to adjudication (the scorers assign the outcome) | 7 |',
        '| No automatic outcome (by kind below) | 9 |',
        '| **Total (executions scored)** | **22** |']
    # only the outcomes present; the sum is the D7 n of executions scored
    assert '`RETRIEVED`' not in table and '`WRONG-SCOPE`' not in table
    assert 5 + 1 + 7 + 9 == 22


@pytest.mark.proposal(
    "the listing of responses with no automatic \u00a76.8 outcome, by kind "
    "with a count, is the fix's format; AP-1 v1.3 gives every response one "
    "outcome and names no such kinds")
@pytest.mark.finding('T3-13')
@pytest.mark.req('AP-1 §6.8', 'R3.3')
def test_scoring_proportions_lists_responses_without_outcome_by_kind():
    # The three kinds AP-1's labels don't fit automatically stay
    # unlabelled and are listed by kind, with a count: correct but the
    # calculator not shown used (worked out "in its head"), operands
    # unobservable, no figure found. One response of each, scored by
    # answer_outcome and counted by build_summary, as a run does.
    from ap1_run.runner.summary import build_summary
    from ap1_run.scoring.answer_outcome import answer_outcome
    grounded = [{'outcome': 'OPERANDS-GROUNDED'}]
    responses = [('AUTO-MATCH', 'INVOKED', grounded, 'CORRECT'),
                 ('AUTO-MATCH', 'NOT-INVOKED', [], 'CORRECT'),
                 ('AUTO-MATCH', 'INVOKED',
                  [{'outcome': 'OPERANDS-UNOBSERVABLE'}], 'CORRECT'),
                 ('AUTO-NO-FIGURE', 'INVOKED', grounded, 'NO-FIGURE')]
    results = []
    for i, (figure, invocation, provenance, accuracy) in enumerate(responses):
        outcome, reason = answer_outcome(figure, invocation, provenance,
                                         accuracy_outcome=accuracy)
        results.append({'item_id': f'Q{i}', 'condition': 'base',
                        'repeat': 1, 'status': 'EXECUTED',
                        'figure_outcome': figure,
                        'invocation_outcome': invocation,
                        'answer_outcome': outcome,
                        'answer_outcome_reason': reason})
    text = report._section_scoring_proportions(build_summary(results, []))
    assert '| `COMPUTED` | 1 |' in text
    assert '| No automatic outcome (by kind below) | 3 |' in text
    assert '| **Total (executions scored)** | **4** |' in text
    listing = text[text.index('#### No Automatic Outcome, by Kind'):]
    assert listing == md(
        '#### No Automatic Outcome, by Kind\n',
        '| Kind | Count |',
        '|---|---|',
        '| correct figure, calculator not shown used | 1 |',
        '| calculator used, operands not shown grounded | 1 |',
        '| no figure found (AUTO-NO-FIGURE) | 1 |',
        '')
    # counts per kind, in the listing's order
    counted = report._section_scoring_proportions(
        {'answer_outcomes': ANSWER_OUTCOMES})
    assert counted.endswith(md(
        '| correct figure, calculator not shown used | 2 |',
        '| calculator used, operands not shown grounded | 3 |',
        '| no figure found (AUTO-NO-FIGURE) | 4 |', ''))
    # a reason of no known kind is listed by its text
    other = dict(ANSWER_OUTCOMES, no_outcome={'other': 2},
                 other_reasons={'some reason': 2})
    assert '| other: some reason | 2 |' in \
        report._section_scoring_proportions({'answer_outcomes': other})


@pytest.mark.finding('T3-13')
def test_scoring_proportions_every_response_with_an_outcome():
    text = report._section_scoring_proportions({'answer_outcomes': {
        'outcomes': {'COMPUTED': 3}, 'no_outcome': {}, 'other_reasons': {}}})
    assert '| **Total (executions scored)** | **3** |' in text
    assert text.endswith(
        '#### No Automatic Outcome, by Kind\n\nNone: every response not '
        'routed to adjudication has an outcome.\n')


def test_scoring_proportions_without_answer_outcomes_has_no_table():
    assert '6.8' not in report._section_scoring_proportions({})
