"""Unit tests for the report generator (R3.3): each section of report.md
rendered from a small summary, and how generate_report puts them together.

Expected text is written as the list of lines the section joins with
newlines, so a test reads like the markdown it pins.
"""

import json
import math
import re
from decimal import Decimal

import pytest

from ap1_run.reporting import report
from ap1_run.reporting.report import (
    ALL_DIMENSIONS, clopper_pearson_upper_k0, generate_report,
)


def md(*lines):
    return '\n'.join(lines)


CONFIG = {'ap1_version': '1.3', 'ap1_version_doi': '10.5281/zenodo.1',
          'model': 'test-model', 'dimensions_claimed': ['D1', 'D2', 'D7']}


# -- Constants ------------------------------------------------------------

def test_all_dimensions_are_d1_to_d7_in_order():
    assert ALL_DIMENSIONS == ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']


# -- clopper_pearson_upper_k0 ---------------------------------------------

def test_clopper_pearson_k0_is_one_minus_alpha_to_one_over_n():
    assert clopper_pearson_upper_k0(10, 0.05) == 1.0 - 0.05 ** (1.0 / 10)
    assert clopper_pearson_upper_k0(10, 0.05) == pytest.approx(0.25887,
                                                              abs=1e-5)


def test_clopper_pearson_k0_default_alpha_is_five_percent():
    assert clopper_pearson_upper_k0(20) == clopper_pearson_upper_k0(20, 0.05)


def test_clopper_pearson_k0_n1_is_one_minus_alpha():
    assert clopper_pearson_upper_k0(1, 0.1) == pytest.approx(0.9)


@pytest.mark.parametrize('n', [0, -1])
def test_clopper_pearson_k0_n_not_positive_is_nan(n):
    assert math.isnan(clopper_pearson_upper_k0(n))


# -- generate_report: header and section order ----------------------------

def test_report_header_names_version_doi_and_model():
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    assert re.match(
        r'# AP-1 Evaluation Report\n\n'
        r'Generated: \d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+\+00:00\n\n'
        r'AP-1 Version: 1\.3\n\n'
        r'Version DOI: 10\.5281/zenodo\.1\n\n'
        r'Model: test-model\n\n'
        r'---\n\n'
        r'## 1\. Pre-Registration Record\n', text)


def test_report_header_missing_fields_read_unknown():
    text = generate_report(summary={}, config={}, seal_record={})
    assert 'AP-1 Version: unknown\n' in text
    assert 'Version DOI: unknown\n' in text
    assert 'Model: unknown\n' in text


@pytest.mark.finding('T3-45')
def test_report_header_carries_no_disclaimer():
    # report.md opens with "AP-1 Evaluation Report" and no warning that a
    # smoke run is not an AP-1 evaluation. Correct: the run's disclaimer
    # at the top of report.md.
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    head = text[:text.index('## 1.')]
    assert 'disclaimer' not in head.lower()
    assert 'not an ap-1 evaluation' not in text.lower()
    assert 'smoke' not in text.lower()


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
        report._section_preregistration(seal, CONFIG),
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
        {'seal_hash': 'abc', 'ap1_version': '1.3', 'keys': []}, {}) == md(
        '## 1. Pre-Registration Record\n',
        '| Field | Value |',
        '|---|---|',
        '| `ap1_version` | `1.3` |',
        '| `keys` | `[]` |',
        '| `seal_hash` | `abc` |',
        '')


def test_preregistration_without_seal_says_so():
    assert report._section_preregistration({}, CONFIG) == md(
        '## 1. Pre-Registration Record\n',
        '*No seal record available.*',
        '')
    assert report._section_preregistration(None, CONFIG) == \
        report._section_preregistration({}, CONFIG)


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
        '| D1 | **NOT MEASURED** | \u2014 | \u2014 |',
        '| D2 | **NOT MEASURED** | \u2014 | \u2014 |',
        '| D3 | **NOT MEASURED** | \u2014 | \u2014 |',
        '| D4 | **NOT MEASURED** | \u2014 | \u2014 |',
        '| D5 | **NOT MEASURED** | \u2014 | \u2014 |',
        '| D6 | **NOT MEASURED** | \u2014 | \u2014 |',
        '| D7 | **NOT MEASURED** | \u2014 | \u2014 |',
        '')


def test_dimension_results_without_claim_list_none_measured():
    assert report._section_dimension_results({}, {}) == \
        report._section_dimension_results({}, {'dimensions_claimed': []})


def test_dimension_results_claimed_without_data_says_so():
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': {}}, {'dimensions_claimed': ['D1']}))
    assert rows[0] == '| D1 | Claimed but no results | \u2014 | \u2014 |'


@pytest.mark.finding('T3-3', 'T3-32')
def test_dimension_results_d1_prints_pooled_rate_without_interval():
    # T3-3: the rate is correct/(correct+incorrect) over auto-scored items,
    # which is 1 whenever defined, and it is printed as "Accuracy: 1".
    # T3-32: one pooled rate, no category breakdown, no 95 % CI, even when
    # the summary has the counts. Correct: no headline rate without
    # adjudication; per category with a 95 % interval and n.
    d1 = {'n': 10, 'auto_scored_n': 7, 'adjudicated_n': 3,
          'accuracy_rate': Decimal('1'), 'correct': 7, 'incorrect': 0,
          'by_category': {'interest': {'n': 5}}}
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': d1}, {'dimensions_claimed': ['D1']}))
    assert rows[0] == ('| D1 | Measured | 10 | Accuracy: 1 '
                       '(auto-scored 7; 3 adjudicated not in rate) |')


def test_dimension_results_d1_n_falls_back_to_auto_scored_n():
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': {'auto_scored_n': 7, 'accuracy_rate': '0.9'}},
        {'dimensions_claimed': ['D1']}))
    assert rows[0] == ('| D1 | Measured | 7 | Accuracy: 0.9 '
                       '(auto-scored 7; 0 adjudicated not in rate) |')


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
                       '(auto-scored 0; 0 adjudicated not in rate) |')


@pytest.mark.finding('T3-4')
def test_dimension_results_d2_live_shape_is_measured_with_n_na():
    # The live d2_results is keyed '<item>/<condition>' and has no 'n',
    # so D2 is "Measured" with n N/A and a pointer to §9, which is empty
    # (see the §9 test). Correct: D2 distinct answers and spread per
    # question, with n, or D2 declared not measured.
    d2 = {'Q01/base': {'figures': {'mechanism': 'OBSERVED-ONLY'}}}
    rows = dim_rows(report._section_dimension_results(
        {'d2_results': d2}, {'dimensions_claimed': ['D2']}))
    assert rows[1] == ('| D2 | Measured | N/A | '
                       'See \u00a79 D2 Mechanism Classes |')


@pytest.mark.finding('T3-29')
def test_dimension_results_d7_is_one_measured_row():
    # One D7 row says "Measured", although D7.4 is never measured and
    # part of D7.3 is unobservable. Correct: D7.1-D7.4 reported
    # separately, D7.4 declared not measured.
    rows = dim_rows(report._section_dimension_results(
        {'d7_results': {'n': 40, 'auto_scored_n': 22, 'adjudicated_n': 18}},
        {'dimensions_claimed': ['D7']}))
    assert rows[6] == '| D7 | Measured | 40 | See \u00a74-7 D7 Figures |'
    assert len(rows) == 7


def test_dimension_results_other_claimed_dimension_prints_its_data():
    rows = dim_rows(report._section_dimension_results(
        {'d3_results': {'n': 2}}, {'dimensions_claimed': ['D3']}))
    assert rows[2] == "| D3 | Measured | 2 | {'n': 2} |"


# -- 4. D7 figures by evidence class --------------------------------------

@pytest.mark.finding('T3-33')
def test_d7_figures_counts_sorted_by_class():
    # The note cites "§6.4" for non-comparability; T3-33: the clause meant
    # is D7.7. Correct: cite D7.7.
    text = report._section_d7_figures({'evidence_class_counts': {
        'EV-2 PLATFORM-STRUCTURAL': 30, 'EV-0 UNOBSERVABLE': 1}})
    assert text == md(
        '## 4. D7 Figures by Evidence Class\n',
        '> Figures resting on different evidence classes are not '
        'comparable (AP-1 v1.3 \u00a76.4).\n',
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
        'quantisation policy (licensed rounding, EXACT under AP-1 v1.3; '
        'subtract them for a strict v1.2 "match" count).',
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
        'quantisation policy (licensed rounding, EXACT under AP-1 v1.3; '
        'subtract them for a strict v1.2 "match" count).',
        '\n#### Altered Transcriptions\n',
        '| Item | Condition | Rep | Difference | Reason |',
        '|---|---|---|---|---|',
        '| Q03 | base | 3 | 0.01 | rounded |',
        '| ? | ? | ? | ? | ? |',
        '',
        '### B.') in text


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


def test_d73_release_coverage_percentage_one_decimal():
    text = report._section_d73({'release_coverage_results': [
        tr('GOVERNED-RELEASE'), tr('X'), tr('X')]})
    assert '| `GOVERNED-RELEASE` | 1 | 33.3% |' in text


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


def test_d73_partially_governed_capped_at_twenty():
    text = report._section_d73({'release_coverage_results': [
        tr('PARTIALLY-GOVERNED', i) for i in range(1, 24)]})
    assert '| Q20 | base | 20 |' in text
    assert '| Q21 |' not in text
    assert text.endswith('| ... | ... | ... | (3 more) |\n')


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
    'repeats is NOT-INVOKED. UNOBSERVABLE executions (EV-0) are neither '
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
    # The bound is computed in float and shown rounded to 6 places (and
    # 4 as a percentage) by float formatting. T3-61: it duplicates
    # invocation.py and does not round the upper bound up. Correct: one
    # computation, rounded up.
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


def test_clopper_pearson_section_zero_failures_ignores_given_rate():
    text = report._section_clopper_pearson({'invocation_figures': {
        'm': {'n': 500, 'rate': 'whatever'}}})
    assert '| m | 0 | 500 | 500/500 (100.0%) | 0.005974 (0.5974%) | \u2014 |' \
        in text
    assert 'under m.' in text


@pytest.mark.finding('T3-81')
def test_clopper_pearson_section_failures_show_rate_without_bound():
    # k > 0: the given rate and no bound (a declared limitation).
    text = report._section_clopper_pearson({'invocation_figures': {
        'b': {'failures': 2, 'n': 20, 'rate': '18/20'},
        'a': {'failures': 1, 'n': 5}}})
    # V12-5: the rate is always computed from k and n and shown as a
    # percentage, rounded down (4/5 is 80.0 %).
    assert md(
        '|---|---|---|---|---|---|',
        '| a | 1 | 5 | 4/5 (80.0%) | *not computed (see \u00a7Declared '
        'Limitations)* | \u2014 |',
        '| b | 2 | 20 | 18/20 (90.0%) | *not computed (see \u00a7Declared '
        'Limitations)* | \u2014 |',
        '') in text
    assert ('- Deterministic computation was invoked on 80.0% of computable '
            'questions (4/5; 1 not invoked; upper bound on the failure rate '
            'not computed, see \u00a7Declared Limitations), under a.') in text
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


def test_d72a_audit_renders_operation_and_operand_fields():
    text = report._section_d72a_audit({'originated_operand_audit': [
        {'item_id': 'Q03', 'condition': 'base', 'operation': 'mul',
         'originated_operand': '81.0', 'expression': '2400 * 81.0',
         'resolution': 'originated'}]})
    assert text == md(
        '## 6. D7.2(a) Originated-Operand Audit\n',
        '| Item | Condition | Operation | Originated Operand | '
        'Expression | Resolution |',
        '|---|---|---|---|---|---|',
        '| Q03 | base | mul | `81.0` | `2400 * 81.0` | originated |',
        '')


@pytest.mark.finding('T3-64')
def test_d72a_audit_live_entries_render_question_marks():
    # The live audit entries (runner/summary.build_summary) carry 'value'
    # and 'literal', not 'operation' and 'originated_operand', so two
    # columns read '?'. Correct: the operand shown, as §7b does.
    text = report._section_d72a_audit({'originated_operand_audit': [
        {'item_id': 'Q03', 'condition': 'base', 'value': '81.0',
         'literal': '81.0', 'expression': '2400 * (81.0 / 100) / 12',
         'resolution': 'originated', 'sign_inversion_finding': None}]})
    assert ('| Q03 | base | ? | `?` | `2400 * (81.0 / 100) / 12` '
            '| originated |') in text


def test_d72a_audit_missing_fields_read_question_marks():
    text = report._section_d72a_audit({'originated_operand_audit': [{}]})
    assert '| ? | ? | ? | `?` | `?` | ? |\n' in text


# -- 7. D7.2(b) operation correctness -------------------------------------

def test_d72b_without_counts_says_so():
    assert report._section_d72b_counts({}) == md(
        '## 7. D7.2(b) Operation Correctness\n',
        '*No operation correctness data available.*\n')


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


def test_d72b_wrong_operation_split_shown_when_non_zero():
    text = report._section_d72b_counts({
        'operation_correctness_counts': {'WRONG-OPERATION': 3},
        'wrong_operation_split': {'route_divergence': 1, 'item_wrong': 0,
                                  'undetermined': 2}})
    assert text.endswith(md(
        '| OPERATION-UNOBSERVABLE | 0 |',
        '',
        '### WRONG-OPERATION by Item Outcome\n',
        '| Population | Count |',
        '|---|---|',
        '| Route divergence (item answer correct) | 1 |',
        '| Item answer incorrect | 0 |',
        '| Item answer undetermined (adjudicated) | 2 |',
        ''))


def test_d72b_wrong_operation_split_missing_keys_read_zero():
    text = report._section_d72b_counts({
        'operation_correctness_counts': {'WRONG-OPERATION': 1},
        'wrong_operation_split': {'item_wrong': 1}})
    assert '| Route divergence (item answer correct) | 0 |' in text
    assert '| Item answer incorrect | 1 |' in text
    assert '| Item answer undetermined (adjudicated) | 0 |' in text


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


def test_provenance_split_keys_missing_read_zero():
    text = report._section_operand_provenance({'operand_step_counts': {2: 0}})
    assert '| 1 | Source match | 0 |' in text
    assert '| 5 | Originated, sign-inverted from source | 0 |' in text
    assert '| 5 | Originated, computed from ungrounded invocation | 0 |' \
        in text
    assert '| 5 | Originated, no traceable basis | 0 |' in text


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
        '| Outcome | Count |',
        '|---|---|',
        '| OPERANDS-GROUNDED | 2 |',
        '| OPERAND-ORIGINATED | 0 |',
        '')


@pytest.mark.finding('T3-42')
def test_provenance_outcomes_other_than_grounded_or_originated_not_shown():
    # Only OPERANDS-GROUNDED and OPERAND-ORIGINATED get rows; an
    # UNMEASURABLE count (which R2.4 asks for when intermediates are
    # absent, and which is never produced, T3-42) would count towards
    # the total and not be shown. Correct: every outcome listed.
    text = report._section_operand_provenance({
        'provenance_outcomes': {'UNMEASURABLE': 3}})
    assert '### Per-Invocation Outcomes' in text
    assert 'UNMEASURABLE' not in text
    assert '| OPERANDS-GROUNDED | 0 |\n| OPERAND-ORIGINATED | 0 |' in text


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


@pytest.mark.finding('T3-3')
def test_scoring_proportions_d1_split_and_rate():
    # The rate is printed with the note that adjudicated items are not in
    # it; nothing says it cannot be below 1 (T3-3). Correct: no rate
    # until the adjudicated items are scored.
    text = report._section_scoring_proportions({'d1_results': {
        'auto_scored_n': 22, 'adjudicated_n': 18,
        'accuracy_rate': Decimal('1')}})
    assert text == md(
        '## 8. Scoring Proportions\n',
        '### D1 Accuracy\n',
        '- Auto-scored: 22',
        '- Adjudicated: 18',
        '- Total: 40',
        '- Auto-scored proportion: 22/40 = 55.00%',
        '- Accuracy rate: 1 (computed from 22 auto-scored items only; '
        '18 adjudicated items are not represented in this rate)',
        '')


def test_scoring_proportions_d1_proportion_two_decimals():
    text = report._section_scoring_proportions({'d1_results': {
        'auto_scored_n': 1, 'adjudicated_n': 2}})
    assert '- Auto-scored proportion: 1/3 = 33.33%' in text


def test_scoring_proportions_d1_without_counts_or_rate():
    text = report._section_scoring_proportions({'d1_results': {'n': 5}})
    assert text == md(
        '## 8. Scoring Proportions\n',
        '### D1 Accuracy\n',
        '- Auto-scored: 0',
        '- Adjudicated: 0',
        '- Total: 0',
        '')


@pytest.mark.finding('T3-66')
def test_scoring_proportions_d1_total_ignores_n_and_unmeasurable():
    # §8's total is auto + adjudicated; §3 prints d1 'n'. With an
    # UNMEASURABLE item the two disagree (§3 10, §8 9) and the
    # UNMEASURABLE item appears in neither split. Correct: one n, with
    # UNMEASURABLE counted and shown.
    summary = {'d1_results': {'n': 10, 'auto_scored_n': 8,
                              'adjudicated_n': 1, 'unmeasurable_n': 1,
                              'accuracy_rate': Decimal('1')}}
    text = report._section_scoring_proportions(summary)
    assert '- Total: 9' in text
    assert 'nmeasurable' not in text
    assert '| D1 | Measured | 10 |' in report._section_dimension_results(
        summary, {'dimensions_claimed': ['D1']})


@pytest.mark.finding('T3-33')
def test_scoring_proportions_d7_split_labelled_provenance():
    # T3-33: D7 is "Computation invocation" in AP-1 v1.3, not
    # "Provenance" (D3). Correct: the AP-1 name.
    text = report._section_scoring_proportions({'d7_results': {
        'n': 41, 'auto_scored_n': 30, 'adjudicated_n': 10}})
    assert text == md(
        '## 8. Scoring Proportions\n',
        '### D7 Provenance\n',
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


def test_scoring_proportions_d1_then_d7():
    text = report._section_scoring_proportions({
        'd1_results': {'auto_scored_n': 1},
        'd7_results': {'auto_scored_n': 1}})
    assert text.index('### D1 Accuracy') < text.index('### D7 Provenance')
    assert 'No scoring proportion data' not in text


# -- 9. D2 mechanism classes ----------------------------------------------

D2_NOTE = ('> D2 is auto-measured. STRUCTURAL and CONFIGURED are '
           'operator-declared; OBSERVED-ONLY and UNMEASURED are '
           'determined from evidence.\n')


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


def test_d2_surfaces_table_sorted_with_basis():
    text = report._section_d2_mechanisms({'d2_results': {'surfaces': {
        'prose': {'mechanism': 'STRUCTURAL', 'operator_declared': True,
                  'distinct_values': 1, 'successful_runs': 3,
                  'parameter_echo_status': 'VERIFIED'},
        'figures': {}}}})
    assert text == md(
        '## 9. D2 Reproducibility Mechanism Classes\n',
        D2_NOTE,
        '| Surface | Mechanism Class | Basis | Distinct Values | Runs | '
        'Parameter Echo |',
        '|---|---|---|---|---|---|',
        '| figures | `unknown` | evidence | \u2014 | \u2014 | `UNVERIFIED` |',
        '| prose | `STRUCTURAL` | operator-declared | 1 | 3 | `VERIFIED` |',
        '')


@pytest.mark.finding('T3-4', 'T3-75')
def test_d2_live_shape_has_no_per_surface_data():
    # build_summary passes d2_results keyed '<item>/<condition>'; this
    # section reads d2['surfaces'], which the live shape never has, so
    # §9 says there is no data while §3 says D2 was measured (T3-4).
    # The note above uses UNMEASURED, a term SPEC also uses for other
    # things (T3-75). Correct: D2 rendered from the live shape.
    text = report._section_d2_mechanisms({'d2_results': {
        'Q01/base': {'figures': {'mechanism': 'OBSERVED-ONLY'},
                     'prose': {'mechanism': 'OBSERVED-ONLY'}}}})
    assert text == md(
        '## 9. D2 Reproducibility Mechanism Classes\n',
        D2_NOTE,
        '*No per-surface D2 data available.*\n',
        '')


# -- 10. Non-outcome cells ------------------------------------------------

CELLS_HEAD = (
    '## 10. Non-Outcome Cells\n',
    '> Every cell that is not a scoreable outcome is listed with its '
    'reason.\n',
)


def test_cells_without_any_says_so():
    assert report._section_unmeasured_cells({}, None) == md(
        *CELLS_HEAD, '*No non-outcome cells.*\n', '')


def test_cells_from_summary_listed():
    text = report._section_unmeasured_cells({'non_outcome_cells': [
        {'item_id': 'Q01', 'condition': 'base', 'status': 'UNMEASURED',
         'reason': 'rate limited'},
        {}]}, None)
    assert text == md(
        *CELLS_HEAD,
        '| Item | Condition | Status | Reason |',
        '|---|---|---|---|',
        '| Q01 | base | UNMEASURED | rate limited |',
        '| ? | ? | ? | ? |',
        '')


def test_cells_from_transcript_error_state_and_ev0():
    text = report._section_unmeasured_cells({}, [
        {'item_id': 'Q02', 'condition': 'base',
         'error_state': 'TRANSPORT_FAILURE: HTTP 500: boom'},
        {'item_id': 'Q03', 'condition': 'base', 'error_state': 'VOID',
         'evidence_class': 'EV-0 UNOBSERVABLE'},
        {'evidence_class': 'EV-2 PLATFORM-STRUCTURAL'},
        {'error_state': None, 'evidence_class': None},
        {'error_state': 'X:y'},
    ])
    assert text == md(
        *CELLS_HEAD,
        '| Item | Condition | Status | Reason |',
        '|---|---|---|---|',
        '| Q02 | base | TRANSPORT_FAILURE | TRANSPORT_FAILURE: HTTP 500: '
        'boom |',
        '| Q03 | base | VOID | VOID |',
        '| Q03 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |',
        '| ? | ? | X | X:y |',
        '')


def test_cells_summary_cells_come_before_transcript_cells():
    text = report._section_unmeasured_cells(
        {'non_outcome_cells': [{'item_id': 'S', 'condition': 'c',
                                'status': 'VOID', 'reason': 'r'}]},
        [{'item_id': 'T', 'condition': 'c', 'error_state': 'VOID'}])
    assert text.index('| S |') < text.index('| T |')


@pytest.mark.finding('T3-35')
def test_cells_deduplicated_on_item_condition_status():
    # Cells are de-duplicated on (item, condition, status), so 49
    # rate-limited repeats become one row and the later reasons are lost.
    # Correct: one row per cell, repeat identified.
    text = report._section_unmeasured_cells({'non_outcome_cells': [
        {'item_id': 'Q01', 'condition': 'base', 'status': 'UNMEASURED',
         'reason': f'rate limited r{i}'} for i in range(1, 50)]}, None)
    assert text.count('| Q01 | base | UNMEASURED |') == 1
    assert 'rate limited r1 |' in text
    assert 'r2 |' not in text


@pytest.mark.finding('T3-35')
def test_cells_same_failure_listed_once_per_status():
    # One transport failure appears as one row per distinct status: its
    # error_state, its EV-0 class and the summary's UNMEASURED cell.
    # Correct: one row per cell, with its reason.
    text = report._section_unmeasured_cells(
        {'non_outcome_cells': [{'item_id': 'Q01', 'condition': 'base',
                                'status': 'UNMEASURED',
                                'reason': 'transport'}]},
        [{'item_id': 'Q01', 'condition': 'base',
          'error_state': 'TRANSPORT_FAILURE: timeout',
          'evidence_class': 'EV-0 UNOBSERVABLE'}])
    assert len(re.findall(r'^\| Q01 \| base \|', text, flags=re.M)) == 3


@pytest.mark.finding('T3-35')
def test_cells_other_non_outcomes_in_summary_are_not_listed():
    # Figure-level UNMEASURABLE, transcription UNOBSERVABLE,
    # COVERAGE-UNOBSERVABLE and OPERATION-UNOBSERVABLE are in the summary
    # but not in this section. Correct: every non-outcome cell listed.
    summary = {
        'transcription_results': [{'item_id': 'Q01', 'condition': 'base',
                                   'outcome': 'UNOBSERVABLE'}],
        'release_coverage_results': [{'item_id': 'Q01',
                                      'condition': 'base',
                                      'outcome': 'COVERAGE-UNOBSERVABLE'}],
        'operation_correctness_counts': {'OPERATION-UNOBSERVABLE': 2},
        'd1_results': {'unmeasurable_n': 1},
    }
    text = report._section_unmeasured_cells(summary, [
        {'item_id': 'Q07', 'condition': 'base',
         'figure_outcome': 'UNMEASURABLE'}])
    assert '*No non-outcome cells.*' in text


@pytest.mark.finding('T3-35')
def test_cells_from_transcript_are_appended_to_the_summary_list():
    # The section appends transcript cells to summary['non_outcome_cells']
    # in place, so the caller's summary changes. Correct: no side effect.
    summary = {'non_outcome_cells': []}
    report._section_unmeasured_cells(
        summary, [{'item_id': 'Q01', 'condition': 'base',
                   'error_state': 'VOID'}])
    assert summary['non_outcome_cells'] == [
        {'item_id': 'Q01', 'condition': 'base', 'status': 'VOID',
         'reason': 'VOID'}]


def test_cells_error_state_text_without_colon_is_status():
    text = report._section_unmeasured_cells({}, [
        {'item_id': 'Q', 'condition': 'c', 'error_state': 'TIMEOUT'}])
    assert '| Q | c | TIMEOUT | TIMEOUT |' in text


def test_cells_non_string_error_state_without_colon_is_stringified():
    text = report._section_unmeasured_cells({}, [
        {'item_id': 'Q', 'condition': 'c', 'error_state': 504}])
    assert '| Q | c | 504 | 504 |' in text


@pytest.mark.finding('S3-G6-1')
def test_cells_non_string_error_state_with_colon_raises():
    # The colon test goes through str() but the split does not, so a
    # non-string error_state whose text contains ':' raises and no
    # report is written. Engine error states are strings today, so this
    # is latent. Correct: split str(error).
    class Err:
        def __str__(self):
            return 'TRANSPORT_FAILURE: x'
    with pytest.raises(AttributeError):
        report._section_unmeasured_cells({}, [
            {'item_id': 'Q', 'condition': 'c', 'error_state': Err()}])


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


def test_quantisation_findings_listed():
    text = report._section_quantisation({'quantisation_findings': [
        {'item_id': 'Q04', 'operand': '0.0125', 'finding': 'rounded'}, {}]})
    assert text == md(
        '## 11. Quantisation and Near-Miss Findings\n',
        '| Item | Operand | Finding |',
        '|---|---|---|',
        '| Q04 | `0.0125` | rounded |',
        '| ? | `?` | ? |',
        '')


def test_quantisation_near_miss_findings_listed():
    text = report._section_quantisation({'near_miss_findings': [
        'Q07 near miss', 'Q08 near miss']})
    assert text == md(
        '## 11. Quantisation and Near-Miss Findings\n',
        '*No quantisation findings.*',
        '\n### Near-Miss Findings\n',
        '- Q07 near miss',
        '- Q08 near miss',
        '')


# -- 12. Unmeasured dimensions --------------------------------------------

DIMS_HEAD = (
    '## 12. Unmeasured Dimensions Declaration\n',
    '> A dimension not measured is declared, never omitted.\n',
)


@pytest.mark.finding('T3-33')
def test_unmeasured_dimensions_names_d3_to_d6_wrongly():
    # D3-D6 are given dimensions AP-1 does not define. AP-1 v1.3 §4:
    # D3 Provenance, D4 Refusal integrity, D5 Adversarial resistance,
    # D6 Conflicting input. Correct: the AP-1 names.
    text = report._section_unmeasured_dimensions(CONFIG)
    assert text == md(
        *DIMS_HEAD,
        'The following dimensions were **not measured** in this '
        'evaluation and require human adjudication:\n',
        '- **D3**: Completeness of explanation \u2014 requires human '
        'adjudication',
        '- **D4**: Appropriate caveats \u2014 requires human adjudication',
        '- **D5**: Source attribution \u2014 requires human adjudication',
        '- **D6**: Confidence calibration \u2014 requires human '
        'adjudication',
        '')


@pytest.mark.finding('T3-29')
def test_unmeasured_dimensions_does_not_declare_d7_parts():
    # With D7 claimed, nothing declares D7.4 (never measured) or the
    # unobservable part of D7.3. Correct: declare both.
    text = report._section_unmeasured_dimensions(CONFIG)
    assert 'D7' not in text


@pytest.mark.finding('T3-33', 'S3-G6-2')
def test_unmeasured_dimensions_all_unclaimed():
    # Every unclaimed dimension is said to "require human adjudication",
    # D1, D2 and D7 included, which the runner measures automatically
    # (S3-G6-2). D7 is called "Provenance" (T3-33). Correct: the AP-1
    # names, and the reason each one was not measured.
    text = report._section_unmeasured_dimensions({})
    assert text.endswith(md(
        '- **D1**: Accuracy \u2014 requires item-level scoring',
        '- **D2**: Reproducibility \u2014 requires repeated runs',
        '- **D3**: Completeness of explanation \u2014 requires human '
        'adjudication',
        '- **D4**: Appropriate caveats \u2014 requires human adjudication',
        '- **D5**: Source attribution \u2014 requires human adjudication',
        '- **D6**: Confidence calibration \u2014 requires human '
        'adjudication',
        '- **D7**: Provenance \u2014 requires tool-call observation',
        ''))
    assert 'evaluation and require human adjudication:' in text


def test_unmeasured_dimensions_all_claimed():
    assert report._section_unmeasured_dimensions(
        {'dimensions_claimed': ALL_DIMENSIONS}) == md(
        *DIMS_HEAD, 'All seven dimensions were claimed for measurement.', '')


def test_unmeasured_reason_unknown_dimension():
    assert report._unmeasured_reason('D8') == 'Reason not specified'


# -- 13. Declared limitations ---------------------------------------------

@pytest.mark.finding('T3-81')
def test_declared_limitations_text():
    assert report._section_declared_limitations() == md(
        '## 13. Declared Limitations\n',
        '### Clopper-Pearson Bound (k > 0)\n',
        'An exact confidence bound for non-zero failure counts is not '
        'computed; AP-1 v1.3 D7.5 specifies the zero-failure form only. '
        'This is an author-identified defect in the standard, noted for '
        'resolution in the adopted version.\n',
        'For non-zero failure counts, the point estimate is reported with '
        'n. The full Beta quantile would require an external dependency '
        'or a specification extension.\n')


# -- _format_dim_result ---------------------------------------------------

def test_format_dim_result_d2_and_d7_point_to_sections():
    assert report._format_dim_result('D2', {'x': 1}) == \
        'See \u00a79 D2 Mechanism Classes'
    assert report._format_dim_result('D7', {'x': 1}) == \
        'See \u00a74-7 D7 Figures'


def test_format_dim_result_d1_defaults_counts_to_zero():
    assert report._format_dim_result('D1', {'accuracy_rate': '0.5'}) == \
        'Accuracy: 0.5 (auto-scored 0; 0 adjudicated not in rate)'


# -- Boundaries: one observation, twenty-one rows -------------------------

def test_d73_single_result_is_one_hundred_percent():
    text = report._section_d73({
        'transcription_results': [tr('TRANSCRIBED-EXACT')],
        'release_coverage_results': [tr('GOVERNED-RELEASE')]})
    assert '| `TRANSCRIBED-EXACT` | 1 | 100.0% |' in text
    assert '| `GOVERNED-RELEASE` | 1 | 100.0% |' in text


def test_d73_twenty_one_rows_show_one_more():
    text = report._section_d73({
        'transcription_results': [tr('TRANSCRIBED-ALTERED', i)
                                  for i in range(1, 22)],
        'release_coverage_results': [tr('PARTIALLY-GOVERNED', i)
                                     for i in range(1, 22)]})
    assert '| ... | ... | ... | ... | (1 more) |\n' in text
    assert text.endswith('\n| ... | ... | ... | (1 more) |\n')


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


def test_cells_ev0_record_without_ids_reads_question_marks():
    text = report._section_unmeasured_cells({}, [
        {'evidence_class': 'EV-0 UNOBSERVABLE'}])
    assert '| ? | ? | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |' \
        in text


# --- Step 4: correct behaviour (failing until fixed) ---

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
    as fractions (a number followed by '%' divided by 100)."""
    row = next(line for line in text.splitlines()
               if line.startswith(f'| {metric} |'))
    cell = row.split('|')[5]
    return cell, [Decimal(num) / (100 if pct else 1) for num, pct in
                  re.findall(r'(\d+(?:\.\d+)?)\s*(%?)', cell)]


@pytest.mark.finding('T3-61')
@pytest.mark.req('AP-1 D7.5', 'R0.4.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-61: report.py computes the D7.5 bound in '
                          'float, apart from invocation.py')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-61: report §5 rounds the upper bound to '
                          'nearest, not up')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-81: no D7.5 bound for k > 0 ("not computed")')
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

# Group g7-report (fix branch 7, report honesty). Each test asserts what
# SPEC/AP-1 require and is xfail(strict=True) until the fix lands.

# D1 with adjudication pending: 22 auto-scored (all CORRECT), 18 routed to
# adjudication and not yet scored, as on every live run.
D1_PENDING = {'n': 40, 'auto_scored_n': 22, 'adjudicated_n': 18,
              'unmeasurable_n': 0, 'correct': 22, 'incorrect': 0,
              'no_figure': 0, 'accuracy_rate': Decimal('1')}

ACCURACY_ONE = re.compile(r'Accuracy(?: rate)?: 1(?:\.0+)?(?![\d./])')


@pytest.mark.finding('T3-3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-3: "Accuracy: 1" headline from auto-scored '
                          'items while 18 of 40 await adjudication')
def test_dimension_results_d1_pending_adjudication_prints_no_rate_of_one():
    # Every wrong figure routes to adjudication (SPEC R2.0 step 4), so the
    # auto-scored rate is 1 whenever it is defined. Correct (T3-3, fix
    # plan branch 7; SPEC R2.3 "100 % never printed alone", by analogy):
    # no "Accuracy: 1" headline while items await adjudication; the row
    # states the adjudicated share instead.
    rows = dim_rows(report._section_dimension_results(
        {'d1_results': D1_PENDING}, {'dimensions_claimed': ['D1']}))
    assert not ACCURACY_ONE.search(rows[0]), rows[0]
    assert 'adjudicat' in rows[0]


@pytest.mark.finding('T3-3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-3: §8 prints "Accuracy rate: 1" while 18 '
                          'items await adjudication')
def test_scoring_proportions_d1_pending_adjudication_prints_no_rate_of_one():
    # Correct: as for §3, no rate of 1 from the auto-scored items alone
    # while adjudication is pending (T3-3).
    text = report._section_scoring_proportions({'d1_results': D1_PENDING})
    assert not ACCURACY_ONE.search(text), text


@pytest.mark.finding('T3-4')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-4: §9 reads d2["surfaces"]; the live '
                          '"<item>/<condition>" shape renders as no data')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-4: §3 prints D2 "Measured" with n N/A for the '
                          'live shape')
def test_dimension_results_d2_live_shape_states_n():
    # Correct (AP-1 §6.1 "for each dimension, the result and the n"): the
    # D2 row gives its n (questions or runs), never N/A, when results exist.
    d2 = {'Q01/base': {'figures': {'mechanism': 'OBSERVED-ONLY',
                                   'successful_runs': 3}}}
    rows = dim_rows(report._section_dimension_results(
        {'d2_results': d2}, {'dimensions_claimed': ['D2']}))
    assert '| N/A |' not in rows[1], rows[1]


@pytest.mark.finding('T3-29')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-29: one "D7 Measured" row; D7.4 never declared '
                          'not measured')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-29: §12 does not declare the unobservable part '
                          'of D7.3')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-29: D7.2(b) and D7.3 tables carry no evidence '
                          'class')
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


AP1_NAMES = {'D3': 'Provenance', 'D4': 'Refusal integrity', 'D5': 'Adversarial resistance',
             'D6': 'Conflicting input', 'D7': 'Computation invocation'}


@pytest.mark.finding('T3-33')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-33: §12 names D3-D6 and D7 with dimensions '
                          'AP-1 does not define')
def test_unmeasured_dimensions_use_ap1_names():
    # AP-1 v1.3 §4: D3 Provenance, D4 Refusal integrity, D5 Adversarial
    # resistance, D6 Conflicting input, D7 Computation invocation. Correct:
    # §12 uses these names. (D2 is "Determinism" in AP-1 v1.3 but
    # "Reproducibility" in SPEC and the code alike; not asserted here.)
    text = report._section_unmeasured_dimensions({})
    for dim, name in AP1_NAMES.items():
        assert re.search(rf'\*\*{dim}\*\*: {name}\b', text), (dim, text)


@pytest.mark.finding('T3-33')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-33: §8 labels D7 "Provenance"')
def test_scoring_proportions_d7_labelled_computation_invocation():
    # D7 is "Computation invocation" (AP-1 v1.3 §4); "Provenance" is D3.
    text = report._section_scoring_proportions({'d7_results': {
        'auto_scored_n': 30, 'adjudicated_n': 10}})
    assert 'D7 Provenance' not in text
    assert 'Computation invocation' in text


@pytest.mark.finding('T3-33')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-33: §4 cites §6.4 for non-comparability; the '
                          'clause is D7.7')
def test_d7_figures_cite_d77_for_non_comparability():
    # AP-1 v1.3 D7.7: "Figures resting on different classes are not
    # comparable". §6.4 is about discretionary correctness.
    text = report._section_d7_figures({'evidence_class_counts': {
        'EV-2 PLATFORM-STRUCTURAL': 3, 'EV-0 UNOBSERVABLE': 1}})
    assert 'D7.7' in text
    assert '§6.4' not in text


@pytest.mark.finding('S3-G6-2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G6-2: §12 says unclaimed D1, D2 and D7 require '
                          'human adjudication')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-35: §10 de-duplicates cells on (item, '
                          'condition, status)')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-35: figure UNMEASURABLE, transcription '
                          'UNOBSERVABLE and COVERAGE-UNOBSERVABLE cells are '
                          'not listed')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-35: one transport failure is listed three '
                          'times')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-35: §10 appends transcript cells to the '
                          "caller's summary in place")
def test_cells_leave_the_summary_unchanged():
    # Correct: rendering a section has no side effect on its input.
    summary = {'non_outcome_cells': []}
    report._section_unmeasured_cells(
        summary, [{'item_id': 'Q01', 'condition': 'base',
                   'error_state': 'VOID'}])
    assert summary == {'non_outcome_cells': []}


@pytest.mark.finding('S3-G6-1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G6-1: a non-string error_state containing ":" '
                          'raises AttributeError')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-45: report.md has no demonstration-run / '
                          'non-conformance statement')
def test_report_header_says_demonstration_run_not_conformance_result():
    # Marcus (2026-10-13): runs are described as demonstration runs, not
    # conformance results; the README says so (lines 21-22). Correct: the
    # report says so before its first section, since report.md is the
    # artifact most likely to be forwarded. (If the fix passes the
    # statement in from the runner, pass it here.)
    text = generate_report(summary={}, config=CONFIG, seal_record={})
    head = text[:text.index('## 1.')].lower()
    assert 'demonstration run' in head, head
    assert 'not' in head and 'conformance result' in head, head


@pytest.mark.finding('T3-64')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="T3-64: §6 renders '?' for Operation and Operand "
                          'with live audit entries')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-66: §8 total (auto + adjudicated) differs from '
                          '§3 n; UNMEASURABLE not shown')
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

@pytest.mark.finding('V12-6')
@pytest.mark.req('R2.5', 'R3.3')
def test_d73_reports_count_of_exact_rounded_under_declared_policy():
    # Fix plan §2a, V12-6 (in scope, Steven 2026-10-19): keep v1.3's
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

# Group g1-invocation (fix plan branch 1).

@pytest.mark.finding('V12-5')
def test_clopper_pearson_section_rate_as_percentage_with_k_n_and_bound():
    # Correct (AP-1 §6.2 "invoked on [X]% of computable questions"; fix
    # plan row 1): the figure is printed as a percentage, with k/n and
    # the bound beside it (never "100%" alone, SPEC R2.3).
    text = report._section_clopper_pearson({'invocation_figures': {
        'd7_invocation_base': {'failures': 0, 'n': 10, 'rate': '10/10'}}})
    rows = [line for line in text.splitlines() if '10/10' in line]
    assert rows, text
    assert re.search(r'\b100(\.0+)?\s?%', rows[0]), rows[0]
    assert re.search(r'25\.8[89]|25\.9', rows[0]), rows[0]
