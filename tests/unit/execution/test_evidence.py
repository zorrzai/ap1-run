"""Unit tests for evidence classification (execution/evidence.py).

classify_invocation gives the evidence class and the invocation outcome
from what the platform returned: the response shape of every round and
the tool calls accumulated over the tool loop. Prose claims are recorded
but never set the class. Attestations are capped at EV-1, and EV-3 is
never emitted.
"""

import pytest

from ap1_run.execution import evidence
from ap1_run.execution.evidence import (
    EV_0, EV_1, EV_2, EV_3, EvidenceError, check_ev3_guard,
    classes_comparable, classify_attestation, classify_invocation,
    extract_attestation, ranks_above,
)


def response(content='The answer is 15.20.', tool_calls=None, **message):
    msg = {'role': 'assistant', 'content': content, **message}
    if tool_calls is not None:
        msg['tool_calls'] = tool_calls
    return {'choices': [{'message': msg}]}


def call(name='calculator', expression='15200*1.2/100/12'):
    return {'id': 'call_1', 'type': 'function',
            'function': {'name': name,
                         'arguments': f'{{"expression": "{expression}"}}'}}


ANTHROPIC = {'type': 'message', 'role': 'assistant',
             'content': [{'type': 'text', 'text': 'I used the calculator.'}]}


# -- the evidence class constants --------------------------------------

def test_evidence_class_constants_exact_labels():
    assert (EV_0, EV_1, EV_2, EV_3) == (
        'EV-0 UNOBSERVABLE', 'EV-1 SELF-REPORTED',
        'EV-2 PLATFORM-STRUCTURAL', 'EV-3 EXTERNALLY-VERIFIABLE')


# -- classify_invocation: no tools offered -----------------------------

@pytest.mark.req('R1.3.1')
def test_classify_invocation_tools_not_offered_ev0_no_outcome():
    result = classify_invocation(response(tool_calls=[call()]),
                                 tools_offered=False,
                                 accumulated_tool_calls=[call()],
                                 round_shapes=[(True, None)],
                                 required_operation='calculator')
    assert result == (EV_0, None, None)


def test_classify_invocation_tools_not_offered_self_report_recorded():
    text = 'I used the calculator and got 15.20.'
    assert classify_invocation(response(text), tools_offered=False) == (
        EV_0, None, text)


# -- classify_invocation: round shapes ---------------------------------

@pytest.mark.finding('T3-1')
def test_classify_invocation_any_round_unrecognised_ev0_no_outcome():
    # T3-1 (aggregation side): EV-0 gives outcome None, which the run's
    # summary then counts as a success. The classification itself is
    # what R1.3 asks for; the fix belongs in the aggregation.
    result = classify_invocation(
        response(), tools_offered=True,
        accumulated_tool_calls=[call()],
        round_shapes=[(True, None), (False, 'adapter_send failed')],
        required_operation='calculator')
    assert result == (EV_0, None, None)


def test_classify_invocation_first_round_unrecognised_ev0():
    result = classify_invocation(
        response(), tools_offered=True, accumulated_tool_calls=[call()],
        round_shapes=[(False, 'x'), (True, None)])
    assert result == (EV_0, None, None)


def test_classify_invocation_unrecognised_round_self_report_still_recorded():
    text = 'Using the calculator tool, 15.20.'
    result = classify_invocation(response(text), tools_offered=True,
                                 accumulated_tool_calls=[],
                                 round_shapes=[(False, 'x')])
    assert result == (EV_0, None, text)


def test_classify_invocation_round_shapes_override_final_shape():
    # With round_shapes given, the final response's shape is not checked
    # again: an Anthropic-shaped final response is EV-2 here.
    result = classify_invocation(ANTHROPIC, tools_offered=True,
                                 accumulated_tool_calls=[call()],
                                 round_shapes=[(True, None)])
    assert result == (EV_2, 'INVOKED', None)


def test_classify_invocation_empty_round_shapes_counts_as_recognised():
    result = classify_invocation(ANTHROPIC, tools_offered=True,
                                 accumulated_tool_calls=[], round_shapes=[])
    assert result == (EV_2, 'NOT-INVOKED', None)


def test_classify_invocation_no_round_shapes_final_shape_unrecognised_ev0():
    assert classify_invocation(ANTHROPIC, tools_offered=True,
                               accumulated_tool_calls=[call()]) == (
        EV_0, None, None)


@pytest.mark.parametrize('final', [
    {'candidates': [{'content': {'parts': [{'text': '15.20'}]}}]},
    {'output': [], 'status': 'completed'},
    {'choices': []},
    'not a dict',
], ids=['gemini', 'responses', 'no-choices', 'str'])
def test_classify_invocation_no_round_shapes_other_shapes_ev0(final):
    assert classify_invocation(final, tools_offered=True) == (EV_0, None, None)


# -- classify_invocation: outcome from accumulated calls ---------------

@pytest.mark.req('R1.3')
def test_classify_invocation_required_call_accumulated_invoked():
    result = classify_invocation(
        response(), tools_offered=True,
        accumulated_tool_calls=[call('other'), call('calculator')],
        round_shapes=[(True, None), (True, None)],
        required_operation='calculator')
    assert result == (EV_2, 'INVOKED', None)


@pytest.mark.finding('T3-38')
def test_classify_invocation_only_other_tool_called_not_invoked():
    # T3-38: a call to an unoffered or hallucinated tool gives
    # NOT-INVOKED with tool calls present, which the run's consistency
    # check then treats as FATAL. The classification follows R2.3; the
    # fix is in the consistency check (or a distinct outcome here).
    result = classify_invocation(
        response(), tools_offered=True,
        accumulated_tool_calls=[call('python')],
        round_shapes=[(True, None)], required_operation='calculator')
    assert result == (EV_2, 'NOT-INVOKED', None)


def test_classify_invocation_call_without_function_not_required_op():
    result = classify_invocation(
        response(), tools_offered=True,
        accumulated_tool_calls=[{'id': 'c1'}],
        round_shapes=[(True, None)], required_operation='calculator')
    assert result == (EV_2, 'NOT-INVOKED', None)


def test_classify_invocation_no_required_operation_any_call_invoked():
    result = classify_invocation(
        response(), tools_offered=True,
        accumulated_tool_calls=[call('python')],
        round_shapes=[(True, None)])
    assert result == (EV_2, 'INVOKED', None)


@pytest.mark.finding('T3-16')
def test_classify_invocation_malformed_arguments_still_invoked():
    # T3-16: a call whose arguments are not JSON counts as INVOKED but
    # drops out of D7.2(a)/(b). Correct: declared OPERANDS-UNOBSERVABLE
    # downstream; the INVOKED here follows D7.7.
    bad = {'id': 'c1', 'function': {'name': 'calculator',
                                    'arguments': '15200*1.2/100/12'}}
    result = classify_invocation(
        response(), tools_offered=True, accumulated_tool_calls=[bad],
        round_shapes=[(True, None)], required_operation='calculator')
    assert result == (EV_2, 'INVOKED', None)


def test_classify_invocation_no_calls_not_invoked():
    result = classify_invocation(
        response(), tools_offered=True, accumulated_tool_calls=[],
        round_shapes=[(True, None)], required_operation='calculator')
    assert result == (EV_2, 'NOT-INVOKED', None)


def test_classify_invocation_no_accumulated_reads_final_response():
    assert classify_invocation(
        response(None, tool_calls=[call()]), tools_offered=True,
        required_operation='calculator') == (EV_2, 'INVOKED', None)


def test_classify_invocation_empty_accumulated_falls_back_to_final_calls():
    assert classify_invocation(
        response(None, tool_calls=[call()]), tools_offered=True,
        accumulated_tool_calls=[], round_shapes=[(True, None)],
        required_operation='calculator') == (EV_2, 'INVOKED', None)


def test_classify_invocation_accumulated_preferred_over_final_calls():
    assert classify_invocation(
        response(None, tool_calls=[call('calculator')]), tools_offered=True,
        accumulated_tool_calls=[call('python')], round_shapes=[(True, None)],
        required_operation='calculator') == (EV_2, 'NOT-INVOKED', None)


def test_classify_invocation_tool_calls_field_absent_not_invoked():
    assert classify_invocation(response(), tools_offered=True) == (
        EV_2, 'NOT-INVOKED', None)


@pytest.mark.finding('T3-10')
def test_classify_invocation_empty_response_not_invoked():
    # T3-10: an empty response is a definite NOT-INVOKED. Correct (AP-1
    # §13.2, SPEC R4.1 "Empty response -> UNMEASURED"): unmeasured, out
    # of the D7.1 denominator.
    assert classify_invocation(response(''), tools_offered=True,
                               accumulated_tool_calls=[],
                               round_shapes=[(True, None)],
                               required_operation='calculator') == (
        EV_2, 'NOT-INVOKED', None)


# -- classify_invocation: self-reports --------------------------------

@pytest.mark.parametrize('marker', [
    'i used the calculator', 'i called the calculator', 'i used a calculator',
    'i performed a calculation', 'using the calculator tool',
    'called the calculator function',
])
def test_classify_invocation_each_marker_recorded_not_class(marker):
    text = f'Note: {marker.upper()} here; 15.20.'
    assert classify_invocation(response(text), tools_offered=True) == (
        EV_2, 'NOT-INVOKED', text)


def test_classify_invocation_no_marker_no_self_report():
    assert classify_invocation(response('I computed 15.20 by hand.'),
                               tools_offered=True)[2] is None


def test_classify_invocation_content_none_no_self_report():
    assert classify_invocation(response(None), tools_offered=True)[2] is None


def test_classify_invocation_anthropic_text_claim_not_read():
    # Content outside the OpenAI shape is not read for claims.
    assert classify_invocation(ANTHROPIC, tools_offered=False) == (
        EV_0, None, None)


# -- classify_attestation, check_ev3_guard -----------------------------

@pytest.mark.parametrize('attestation, seal_record', [
    ({'signature': 'sig', 'payload': {}}, {'ev3_implemented': False}),
    ({'signature': 'valid', 'ledger_hash': 'x'},
     {'ev3_implemented': True, 'verification_keys': ['k']}),
    (None, {}),
])
def test_classify_attestation_always_ev1(attestation, seal_record):
    assert classify_attestation(attestation, seal_record) == (
        EV_1,
        'attestation verification not implemented in runner v1.0; '
        'classified EV-1 per R1.3.1 — a signature does not cure '
        'self-report because the signer is the party being measured')


def test_classify_attestation_ev3_allowed_still_ev1(monkeypatch):
    monkeypatch.setattr(evidence, '_EV3_FORBIDDEN', False)
    assert classify_attestation({}, {}) == (
        EV_1, 'verification logic not implemented')


def test_check_ev3_guard_ev3_raises():
    with pytest.raises(EvidenceError) as exc:
        check_ev3_guard(EV_3)
    assert str(exc.value) == (
        'FATAL: runner attempted to emit EV-3, which is forbidden '
        'in v1.0. This is a bug in the runner.')


@pytest.mark.parametrize('cls', [EV_0, EV_1, EV_2, None, 'EV-3'])
def test_check_ev3_guard_other_values_pass(cls):
    assert check_ev3_guard(cls) is None


def test_check_ev3_guard_ev3_allowed_passes(monkeypatch):
    monkeypatch.setattr(evidence, '_EV3_FORBIDDEN', False)
    assert check_ev3_guard(EV_3) is None


# -- ranks_above, classes_comparable -----------------------------------

@pytest.mark.parametrize('a, b, expected', [
    (EV_1, EV_0, True), (EV_2, EV_1, True), (EV_3, EV_2, True),
    (EV_0, EV_1, False), (EV_1, EV_2, False), (EV_2, EV_3, False),
    (EV_2, EV_2, False),
    (EV_0, 'unknown', True), ('unknown', EV_0, False),
    ('unknown', 'other', False),
])
def test_ranks_above_normative_order(a, b, expected):
    assert ranks_above(a, b) is expected


@pytest.mark.parametrize('a, b, expected', [
    (EV_2, EV_2, True), (EV_1, EV_2, False), (EV_0, EV_2, False),
])
def test_classes_comparable_same_class_only(a, b, expected):
    assert classes_comparable(a, b) is expected


# -- _extract_model_tool_calls, _extract_content -----------------------

@pytest.mark.parametrize('resp, reason', [
    ('text', 'response is not a dict'),
    ({'choices': {}}, 'choices is empty or not a list'),
    ({'choices': []}, 'choices is empty or not a list'),
    ({'choices': 'abc'}, 'choices is empty or not a list'),
    ({'choices': ['x']}, 'choices[0] is not a dict'),
    ({'choices': [{}]}, 'choices[0].message is missing or not a dict'),
    ({'choices': [{'message': 'x'}]},
     'choices[0].message is missing or not a dict'),
    ({'type': 'message', 'content': []},
     'response appears Anthropic-shaped (has type=message, content)'),
    ({'candidates': []}, 'response appears Gemini-shaped (has candidates)'),
    ({'output': [], 'status': 'completed'},
     'response appears OpenAI Responses-shaped (has output, status)'),
    ({'type': 'message', 'output': []},
     "unrecognised response shape (top-level keys: ['output', 'type'])"),
    ({'content': [], 'status': 'x'},
     "unrecognised response shape (top-level keys: ['content', 'status'])"),
], ids=['str', 'dict-choices', 'empty-choices', 'str-choices', 'str-choice',
        'no-message', 'str-message', 'anthropic', 'gemini', 'responses',
        'type-without-content', 'status-without-output'])
def test_extract_shape_unrecognised_reason(resp, reason):
    assert evidence._extract_model_tool_calls(resp) == ([], False, reason)
    assert evidence._extract_content(resp) == ('', False, reason)


def test_extract_model_tool_calls_recognised_returns_calls():
    calls = [call()]
    assert evidence._extract_model_tool_calls(
        response(tool_calls=calls)) == (calls, True, None)


def test_extract_model_tool_calls_null_tool_calls_empty_list():
    resp = {'choices': [{'message': {'role': 'assistant',
                                     'tool_calls': None}}]}
    assert evidence._extract_model_tool_calls(resp) == ([], True, None)


def test_extract_content_recognised_returns_text():
    assert evidence._extract_content(response('hello')) == ('hello', True, None)


@pytest.mark.parametrize('msg', [{'role': 'assistant'},
                                 {'role': 'assistant', 'content': None}])
def test_extract_content_missing_or_null_content_empty(msg):
    assert evidence._extract_content({'choices': [{'message': msg}]}) == (
        '', True, None)


# -- extract_attestation ----------------------------------------------

def test_extract_attestation_in_message_metadata_returned():
    att = {'signature': 's'}
    assert extract_attestation(
        response(metadata={'attestation': att})) is att


@pytest.mark.parametrize('resp', [
    'text', {}, {'choices': []}, {'choices': [{}]},
    response(), response(metadata={}), response(metadata={'other': 1}),
    response(metadata=None),
], ids=['str', 'no-choices', 'empty-choices', 'no-message', 'no-metadata',
        'empty-metadata', 'other-metadata', 'null-metadata'])
def test_extract_attestation_absent_none(resp):
    assert extract_attestation(resp) is None


@pytest.mark.finding('S3-g2-1')
@pytest.mark.parametrize('resp, error', [
    ({'choices': ['x']}, AttributeError),
    ({'choices': [{'message': None}]}, AttributeError),
    ({'choices': {'a': 1}}, KeyError),
    ({'choices': [{'message': {'metadata': 'attestation'}}]}, TypeError),
], ids=['str-choice', 'null-message', 'dict-choices', 'str-metadata'])
def test_extract_attestation_malformed_shape_raises(resp, error):
    # S3-g2-1: shapes that _extract_model_tool_calls reports as
    # unrecognised (EV-0) make extract_attestation raise; in execute_item
    # that is uncaught. Correct: None for any shape it cannot read.
    with pytest.raises(error):
        extract_attestation(resp)
