"""Unit tests for the runner's aggregation: the invocation consistency
check and the summary that report.generate_report() reads."""

import pytest

from ap1_run.runner import summary as summary_module
from ap1_run.runner.summary import (
    build_summary, classify_reproducibility, find_d2_cap,
    verify_invocation_consistency,
)


def executed(item_id='Q01', condition='base', repeat=1, **fields):
    record = {'item_id': item_id, 'condition': condition, 'repeat': repeat,
              'status': 'EXECUTED'}
    record.update(fields)
    return record


# -- verify_invocation_consistency ----------------------------------------

def test_consistency_accepts_matching_outcomes():
    verify_invocation_consistency([
        executed(invocation_outcome='INVOKED', tool_calls_count=2),
        executed(invocation_outcome='NOT-INVOKED', tool_calls_count=0),
        executed(invocation_outcome='INVOKED', tool_calls_count=1),
    ])


def test_consistency_skips_executions_that_were_not_executed():
    verify_invocation_consistency([
        {'status': 'UNMEASURED', 'invocation_outcome': 'INVOKED',
         'tool_calls_count': 0},
        {'status': 'VOID', 'invocation_outcome': 'NOT-INVOKED',
         'tool_calls_count': 3},
    ])


def test_consistency_invoked_without_calls_is_fatal():
    with pytest.raises(RuntimeError) as exc:
        verify_invocation_consistency([
            executed(invocation_outcome='INVOKED', tool_calls_count=1),
            executed('Q07', 'instruction_removed', 3,
                     invocation_outcome='INVOKED', tool_calls_count=0),
        ])
    assert str(exc.value) == (
        'FATAL: invocation consistency check failed. '
        'Q07/instruction_removed/r3: INVOKED but tool_calls_count=0. '
        'A scoring outcome that contradicts its own evidence '
        'is a defect, not a finding.')


def test_consistency_invoked_with_count_missing_is_fatal():
    with pytest.raises(RuntimeError, match='INVOKED but tool_calls_count=0'):
        verify_invocation_consistency([executed(invocation_outcome='INVOKED')])


def test_consistency_not_invoked_with_calls_is_fatal():
    with pytest.raises(RuntimeError) as exc:
        verify_invocation_consistency([
            executed('Q02', 'base', 1, invocation_outcome='NOT-INVOKED',
                     tool_calls_count=2)])
    assert str(exc.value) == (
        'FATAL: invocation consistency check failed. '
        'Q02/base/r1: NOT-INVOKED but tool_calls_count=2. '
        'A scoring outcome that contradicts its own evidence '
        'is a defect, not a finding.')


def test_consistency_names_unknown_fields_with_question_marks():
    with pytest.raises(RuntimeError, match=r'\?/\?/r\?: NOT-INVOKED'):
        verify_invocation_consistency([
            {'status': 'EXECUTED', 'invocation_outcome': 'NOT-INVOKED',
             'tool_calls_count': 1}])


def test_consistency_other_outcomes_are_not_checked():
    # An outcome other than INVOKED / NOT-INVOKED (e.g. none recorded)
    # passes whatever the count.
    verify_invocation_consistency([executed(tool_calls_count=0),
                                   executed(invocation_outcome='X',
                                            tool_calls_count=5)])


def test_consistency_stops_at_first_mismatch():
    with pytest.raises(RuntimeError, match='Q01/'):
        verify_invocation_consistency([
            executed('Q01', invocation_outcome='INVOKED', tool_calls_count=0),
            executed('Q02', invocation_outcome='INVOKED', tool_calls_count=0),
        ])


# -- build_summary --------------------------------------------------------

EMPTY = {
    'transcription_results': [],
    'release_coverage_results': [],
    'evidence_class_counts': {},
    'item_evidence': [],
    'invocation_figures': {},
    'operation_correctness_counts': {'OPERATION-CORRECT': 0,
                                     'WRONG-OPERATION': 0,
                                     'OPERATION-UNOBSERVABLE': 0},
    'wrong_operation_split': {'route_divergence': 0, 'item_wrong': 0,
                              'undetermined': 0},
    'd7_results': {'n': 0, 'auto_scored_n': 0, 'adjudicated_n': 0},
    'operand_step_counts': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
    'step_1_source': 0,
    'step_1_constant': 0,
    'step_5_sign_inverted': 0,
    'step_5_ungrounded_chain': 0,
    'step_5_untraceable': 0,
    'provenance_outcomes': {'OPERANDS-GROUNDED': 0, 'OPERAND-ORIGINATED': 0},
    'originated_operand_audit': [],
    'non_outcome_cells': [],
}


def test_summary_of_nothing():
    assert build_summary([], []) == EMPTY


def test_summary_passes_through_results_lists():
    s = build_summary([], [], transcription_results=['t'],
                      release_coverage_results=['rc'])
    assert s['transcription_results'] == ['t']
    assert s['release_coverage_results'] == ['rc']


def test_summary_d1_d2_and_cap_only_when_given():
    s = build_summary([], [], d1_summary={'n': 3}, d2_results={'Q01/base': {}},
                      d2_cap_reason='capped')
    assert s['d1_results'] == {'n': 3}
    assert s['d2_results'] == {'Q01/base': {}}
    assert s['d2_cap_reason'] == 'capped'
    s = build_summary([], [], d1_summary={}, d2_results={}, d2_cap_reason='')
    assert 'd1_results' not in s and 'd2_results' not in s
    assert 'd2_cap_reason' not in s


def test_summary_evidence_class_counts_and_detail():
    findings = [{'evidence_class': 'EV-2'}, {'evidence_class': 'EV-2'},
                {'evidence_class': 'EV-0'}, {}]
    s = build_summary([], findings)
    assert s['evidence_class_counts'] == {'EV-2': 2, 'EV-0': 1, '': 1}
    assert s['item_evidence'] is findings


def test_summary_invocation_figures_per_condition():
    results = [
        executed(condition='base', invocation_outcome='INVOKED'),
        executed(condition='base', invocation_outcome='NOT-INVOKED'),
        executed(condition='base', invocation_outcome='INVOKED'),
        executed(condition='instruction_removed',
                 invocation_outcome='NOT-INVOKED'),
        {'status': 'UNMEASURED', 'condition': 'base', 'cause': 'x'},
    ]
    s = build_summary(results, [])
    assert s['invocation_figures'] == {
        'd7_invocation_base': {'failures': 1, 'n': 3, 'rate': '2/3'},
        'd7_invocation_instruction_removed': {'failures': 1, 'n': 1,
                                              'rate': '0/1'},
    }


def test_summary_invocation_figures_without_condition():
    s = build_summary([{'status': 'EXECUTED'}], [])
    assert s['invocation_figures'] == {
        'd7_invocation_': {'failures': 0, 'n': 1, 'rate': '1/1'}}


def test_summary_operation_correctness_and_wrong_operation_split():
    def oc(*outcomes):
        return [{'outcome': o} for o in outcomes]
    results = [
        executed(figure_outcome='AUTO-MATCH',
                 operation_correctness=oc('WRONG-OPERATION',
                                          'OPERATION-CORRECT')),
        executed(figure_outcome='ADJUDICATE-DECLINE',
                 operation_correctness=oc('WRONG-OPERATION')),
        executed(figure_outcome='AUTO-NO-FIGURE',
                 operation_correctness=oc('WRONG-OPERATION',
                                          'OPERATION-UNOBSERVABLE')),
        executed(operation_correctness=[{}, {'outcome': 'OTHER'}]),
        {'status': 'VOID', 'operation_correctness': oc('WRONG-OPERATION')},
    ]
    s = build_summary(results, [])
    assert s['operation_correctness_counts'] == {
        'OPERATION-CORRECT': 1, 'WRONG-OPERATION': 3,
        'OPERATION-UNOBSERVABLE': 2}
    assert s['wrong_operation_split'] == {
        'route_divergence': 1, 'item_wrong': 1, 'undetermined': 1}


def test_summary_d7_scoring_proportions():
    results = [
        executed(figure_outcome='AUTO-MATCH'),
        executed(figure_outcome='AUTO-NO-FIGURE'),
        executed(figure_outcome='ADJUDICATE-TWO-CANDIDATES'),
        executed(figure_outcome='UNMEASURABLE'),
        executed(),
        {'status': 'UNMEASURED', 'figure_outcome': 'AUTO-MATCH'},
    ]
    assert build_summary(results, [])['d7_results'] == {
        'n': 5, 'auto_scored_n': 2, 'adjudicated_n': 2}


def prov(outcome, *resolutions, originated=()):
    return {'outcome': outcome, 'operand_resolutions': list(resolutions),
            'originated_operands': list(originated)}


def test_summary_operand_provenance_counts():
    results = [
        executed('Q01', 'base', provenance_results=[
            prov('OPERANDS-GROUNDED',
                 {'step': 1, 'resolution': 'source_match'},
                 {'step': 1, 'resolution': 'constant'},
                 {'step': 1, 'resolution': 'constant_magnitude'},
                 {'step': 2}, {'step': 3}, {'step': 4}),
        ]),
        executed('Q02', 'instruction_removed', provenance_results=[
            prov('OPERAND-ORIGINATED',
                 {'step': 5, 'resolution': 'originated',
                  'sign_inversion_finding': {'type': 'SIGN-INVERSION'}},
                 {'step': 5, 'resolution': 'computed_in_session_ungrounded'},
                 {'step': 5, 'resolution': 'originated'},
                 {'step': 9}, {},
                 originated=[{'value': '7', 'expression': '7*2'}]),
            {'outcome': 'OPERANDS-UNOBSERVABLE'},
        ]),
        {'status': 'VOID', 'provenance_results': [
            prov('OPERAND-ORIGINATED', {'step': 5})]},
    ]
    s = build_summary(results, [])
    assert s['operand_step_counts'] == {1: 3, 2: 1, 3: 1, 4: 1, 5: 3}
    # constant_magnitude counts as a source match here (T3-5).
    assert (s['step_1_source'], s['step_1_constant']) == (2, 1)
    assert (s['step_5_sign_inverted'], s['step_5_ungrounded_chain'],
            s['step_5_untraceable']) == (1, 1, 1)
    assert s['provenance_outcomes'] == {'OPERANDS-GROUNDED': 1,
                                        'OPERAND-ORIGINATED': 1}
    assert s['originated_operand_audit'] == [
        {'item_id': 'Q02', 'condition': 'instruction_removed',
         'value': '7', 'expression': '7*2'}]


def test_summary_non_outcome_cells():
    results = [
        executed(),
        {'item_id': 'Q03', 'condition': 'base', 'status': 'UNMEASURED',
         'cause': 'rate_limited'},
        {'item_id': 'Q04', 'condition': 'base', 'status': 'VOID',
         'reason': 'underivable'},
        {'item_id': 'Q05', 'condition': 'base', 'status': 'VOID'},
    ]
    assert build_summary(results, [])['non_outcome_cells'] == [
        {'item_id': 'Q03', 'condition': 'base', 'status': 'UNMEASURED',
         'reason': 'rate_limited'},
        {'item_id': 'Q04', 'condition': 'base', 'status': 'VOID',
         'reason': 'underivable'},
        {'item_id': 'Q05', 'condition': 'base', 'status': 'VOID',
         'reason': ''},
    ]


# -- counting: rows that were not executed come first, and every counter
#    reaches at least 2, so a skipped row or a counter that is set rather
#    than incremented shows.

def test_consistency_checks_rows_after_a_non_executed_row():
    with pytest.raises(RuntimeError, match='Q09/'):
        verify_invocation_consistency([
            {'status': 'VOID'},
            executed('Q09', invocation_outcome='INVOKED', tool_calls_count=0),
        ])


def test_summary_counts_accumulate_after_non_executed_rows():
    def oc(outcome):
        return [{'outcome': outcome}]
    void = {'status': 'VOID', 'item_id': 'Q00', 'condition': 'base'}
    results = [
        void,
        executed(invocation_outcome='NOT-INVOKED'),
        executed(invocation_outcome='NOT-INVOKED'),
        executed(figure_outcome='AUTO-MATCH',
                 operation_correctness=oc('WRONG-OPERATION')),
        executed(figure_outcome='AUTO-MATCH',
                 operation_correctness=oc('WRONG-OPERATION')),
        executed(figure_outcome='ADJUDICATE-DECLINE',
                 operation_correctness=oc('WRONG-OPERATION')),
        executed(figure_outcome='ADJUDICATE-DECLINE',
                 operation_correctness=oc('WRONG-OPERATION')),
        # no figure outcome at all: the answer counts as wrong
        executed(operation_correctness=oc('WRONG-OPERATION')),
        executed(figure_outcome='AUTO-NO-FIGURE',
                 operation_correctness=oc('WRONG-OPERATION')),
        executed(provenance_results=[
            prov('OPERAND-ORIGINATED',
                 {'step': 1, 'resolution': 'constant'},
                 {'step': 1, 'resolution': 'constant'},
                 {'step': 5, 'sign_inversion_finding': {'type': 'S'}},
                 {'step': 5, 'sign_inversion_finding': {'type': 'S'}},
                 {'step': 5, 'resolution': 'computed_in_session_ungrounded'},
                 {'step': 5, 'resolution': 'computed_in_session_ungrounded'},
                 {'step': 5, 'resolution': 'computed_in_session_ungrounded'},
                 {'step': 5, 'resolution': 'originated'},
                 {'step': 5, 'resolution': 'originated'}),
            prov('OPERAND-ORIGINATED'),
        ]),
    ]
    s = build_summary(results, [])
    assert s['invocation_figures']['d7_invocation_base'] == {
        'failures': 2, 'n': 9, 'rate': '7/9'}
    assert s['wrong_operation_split'] == {
        'route_divergence': 2, 'item_wrong': 2, 'undetermined': 2}
    assert s['provenance_outcomes'] == {'OPERANDS-GROUNDED': 0,
                                        'OPERAND-ORIGINATED': 2}
    assert s['step_1_constant'] == 2
    assert (s['step_5_sign_inverted'], s['step_5_ungrounded_chain'],
            s['step_5_untraceable']) == (2, 3, 2)
    assert s['d7_results'] == {'n': 9, 'auto_scored_n': 3,
                               'adjudicated_n': 2}


# -- find_d2_cap ----------------------------------------------------------

def omitted(reason, **extra):
    return dict({'value': 'omitted', 'reason': reason}, **extra)


@pytest.mark.req('D2.2')
def test_d2_cap_platform_rejected_parameter():
    sampling = {'temperature': omitted('platform-rejected',
                                       detail='only the default (1)')}
    assert find_d2_cap(sampling) == (
        'D2.2 cap: temperature was platform-rejected. '
        'Detail: only the default (1)')


def test_d2_cap_platform_unsupported_any_case_without_detail():
    sampling = {'seed': omitted('Platform-Unsupported')}
    assert find_d2_cap(sampling) == (
        'D2.2 cap: seed was Platform-Unsupported. '
        'Detail: Platform-Unsupported')


def test_d2_cap_none_for_values_and_other_omission_reasons():
    sampling = {'temperature': 0, 'top_p': '1',
                'reasoning_effort': omitted('not-supported', detail='x'),
                'seed': {'value': 'omitted'}}
    assert find_d2_cap(sampling) is None
    assert find_d2_cap({}) is None


def test_d2_cap_first_capping_parameter_wins():
    sampling = {'top_p': 1,
                'temperature': omitted('platform-rejected', detail='a'),
                'seed': omitted('platform-rejected', detail='b')}
    assert find_d2_cap(sampling).startswith('D2.2 cap: temperature ')


# -- classify_reproducibility ---------------------------------------------

@pytest.fixture
def fake_mechanism(monkeypatch):
    calls = []

    def classify(responses, *, surface, minimum_runs, operator_declared=None):
        calls.append((list(responses), surface, minimum_runs,
                      operator_declared))
        mechanism = responses[0] if responses else 'UNMEASURED'
        return {'mechanism': mechanism, 'surface': surface}
    monkeypatch.setattr(summary_module, 'classify_mechanism', classify)
    return calls


@pytest.mark.req('D2')
def test_reproducibility_per_item_condition_and_surface(fake_mechanism):
    d2 = {('Q01', 'base'): ['STRUCTURAL', 'r2'],
          ('Q01', 'instruction_removed'): []}
    assert classify_reproducibility(d2, 3, None) == {
        'Q01/base': {
            'figures': {'mechanism': 'STRUCTURAL', 'surface': 'figures'},
            'prose': {'mechanism': 'STRUCTURAL', 'surface': 'prose'}},
        'Q01/instruction_removed': {
            'figures': {'mechanism': 'UNMEASURED', 'surface': 'figures'},
            'prose': {'mechanism': 'UNMEASURED', 'surface': 'prose'}},
    }
    assert fake_mechanism == [
        (['STRUCTURAL', 'r2'], 'figures', 3, None),
        (['STRUCTURAL', 'r2'], 'prose', 3, None),
        ([], 'figures', 3, None),
        ([], 'prose', 3, None),
    ]


@pytest.mark.req('D2.2')
def test_reproducibility_cap_lowers_measured_classes_only(fake_mechanism):
    d2 = {('Q01', 'base'): ['CONFIGURED'], ('Q02', 'base'): []}
    result = classify_reproducibility(d2, 1, 'D2.2 cap: why')
    assert result['Q01/base']['figures'] == {
        'mechanism': 'OBSERVED-ONLY', 'surface': 'figures',
        'd2_cap': 'D2.2 cap: why'}
    assert result['Q02/base']['prose'] == {'mechanism': 'UNMEASURED',
                                           'surface': 'prose'}


def test_reproducibility_with_the_real_classifier_below_minimum():
    result = classify_reproducibility({('Q01', 'base'): []}, 3, 'cap')
    assert result['Q01/base']['figures']['mechanism'] == 'UNMEASURED'
    assert 'd2_cap' not in result['Q01/base']['figures']


def test_reproducibility_of_nothing():
    assert classify_reproducibility({}, 3, None) == {}


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-63')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-63: a WRONG-OPERATION call in an UNMEASURABLE '
                          'execution is counted as "item answer incorrect"')
def test_summary_wrong_operation_in_unmeasurable_execution_not_item_wrong():
    # SPEC R2.0 step 0: an unreadable response is UNMEASURABLE, "never
    # scored as incorrect. The runner does not conclude anything about a
    # response it could not read." So its WRONG-OPERATION calls are not
    # counted under "Item answer incorrect" (report.md §7, console 3i).
    results = [executed(figure_outcome='UNMEASURABLE',
                        operation_correctness=[{'outcome': 'WRONG-OPERATION'}])]
    s = build_summary(results, [])
    assert s['wrong_operation_split']['item_wrong'] == 0


@pytest.mark.finding('T3-63')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-63: a WRONG-OPERATION call in an AUTO-NO-FIGURE '
                          'execution is counted as "item answer incorrect"')
def test_summary_wrong_operation_in_no_figure_execution_not_item_wrong():
    # An AUTO-NO-FIGURE execution released no figure: D1 scores it
    # NO-FIGURE, not INCORRECT (scoring/accuracy.py; SPEC R2.0 step 4 keeps
    # AUTO-NO-FIGURE a separate automatic outcome), so it has no "item
    # answer" to be incorrect. Only executions D1 scores INCORRECT belong in
    # "Item answer incorrect".
    results = [executed(figure_outcome='AUTO-NO-FIGURE',
                        operation_correctness=[{'outcome': 'WRONG-OPERATION'}])]
    s = build_summary(results, [])
    assert s['wrong_operation_split']['item_wrong'] == 0
