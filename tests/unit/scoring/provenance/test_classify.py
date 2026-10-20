"""Unit tests for scoring/provenance/classify.py: provenance
of one invocation, of an item, and of a sequence of calls (D7.2(a))."""

import json
from decimal import Decimal

import pytest

from ap1_run.scoring.provenance.classify import (
    _extract_expression, _parse_return_value, classify_invocation,
    classify_invocations_sequential, classify_item,
)

D = Decimal
CTX = {'savings': {'balance': '15200.00', 'rate': '4.2'}}
GT = {'intermediates': [
    {'label': 'interest', 'value': D('53.2049'),
     'inputs': [{'field': 'savings.balance'}, {'constant': '12'}]},
]}
CONFIG = {'permitted_transformations': ['percent_to_fraction'],
          'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_UP'}}


def call(expression, return_value=None, name='calculator', call_id='c1'):
    return {'id': call_id,
            'function': {'name': name,
                         'arguments': json.dumps({'expression': expression})},
            'return_value': return_value}


def result_json(value):
    return json.dumps({'result': value})


# -- classify_invocation --------------------------------------------------

@pytest.mark.req('R2.4')
def test_classify_invocation_all_operands_traced_is_grounded():
    r = classify_invocation('15200 * 0.042 / 12', CTX, GT, CONFIG)
    assert r['outcome'] == 'OPERANDS-GROUNDED'
    assert r['originated_operands'] == []
    assert r['quantisation_findings'] == []
    assert [(x['step'], x['resolution']) for x in r['operand_resolutions']] \
        == [(1, 'source_match'), (2, 'transformed_source'), (1, 'constant')]


def test_classify_invocation_resolution_carries_operand_and_expression():
    r = classify_invocation('-15200', CTX, GT, CONFIG)
    res = r['operand_resolutions'][0]
    assert res['operand_value'] == '-15200'
    assert res['operand_literal'] == '-15200'
    assert res['expression'] == '-15200'


@pytest.mark.req('R2.4')
def test_classify_invocation_one_untraced_operand_is_originated():
    r = classify_invocation('15200 * 0.05', CTX, GT, CONFIG)
    assert r['outcome'] == 'OPERAND-ORIGINATED'
    assert r['originated_operands'] == [{
        'value': '0.05', 'literal': '0.05', 'expression': '15200 * 0.05',
        'resolution': 'originated', 'sign_inversion_finding': None}]


def test_classify_invocation_originated_entry_keeps_sign_inversion():
    r = classify_invocation('-15200', CTX, GT, CONFIG)
    assert r['originated_operands'][0]['sign_inversion_finding'] == {
        'type': 'SIGN-INVERSION', 'matched_field': 'savings.balance',
        'source_value': '15200.00', 'operand_value': '-15200'}


def test_classify_invocation_quantised_intermediate_is_a_finding():
    r = classify_invocation('53.20 + 1', CTX, GT, CONFIG)
    assert r['outcome'] == 'OPERANDS-GROUNDED'
    # The operand is read through a float, so '53.20' becomes '53.2'.
    assert r['quantisation_findings'] == [{
        'operand': '53.2', 'matched_intermediate': 'interest',
        'expression': '53.20 + 1'}]


def test_classify_invocation_uses_config_transformations_and_quantisation():
    r = classify_invocation('0.042', CTX, GT, {})
    assert r['outcome'] == 'OPERAND-ORIGINATED'
    r = classify_invocation('53.20', CTX, GT, {})
    assert r['outcome'] == 'OPERAND-ORIGINATED'
    assert r['quantisation_findings'] == []


def test_classify_invocation_declared_constants_from_ground_truth():
    assert classify_invocation('12', CTX, GT, CONFIG)['outcome'] == \
        'OPERANDS-GROUNDED'
    assert classify_invocation('12', CTX, {}, CONFIG)['outcome'] == \
        'OPERAND-ORIGINATED'


def test_classify_invocation_ground_truth_without_intermediates():
    r = classify_invocation('15200', CTX, {}, CONFIG)
    assert r['outcome'] == 'OPERANDS-GROUNDED'


def test_classify_invocation_passes_prior_returns_to_step4():
    prior = [{'value': D('638.40'), 'grounded': True}]
    r = classify_invocation('638.40 * 2', CTX, GT, CONFIG, prior_returns=prior)
    assert r['operand_resolutions'][0]['resolution'] == 'computed_in_session'
    r = classify_invocation('638.40 * 2', CTX, GT, CONFIG)
    assert r['operand_resolutions'][0]['resolution'] == 'originated'


@pytest.mark.finding('T3-2', 'T3-16')
def test_classify_invocation_no_operands_is_grounded():
    # Current behaviour: an expression with no operands found (unparseable,
    # or a leading space) is OPERANDS-GROUNDED, vacuously.
    r = classify_invocation(' 99999 * 7', CTX, GT, CONFIG)
    assert r == {'outcome': 'OPERANDS-GROUNDED', 'operand_resolutions': [],
                 'originated_operands': [], 'quantisation_findings': []}


# -- classify_item --------------------------------------------------------

def inv(outcome, originated=(), quant=()):
    return {'outcome': outcome, 'originated_operands': list(originated),
            'quantisation_findings': list(quant)}


def test_classify_item_without_invocations_is_unobservable():
    assert classify_item([], GT) == {
        'outcome': 'OPERANDS-UNOBSERVABLE', 'invocation_count': 0,
        'all_originated': [], 'all_quantisation_findings': []}


@pytest.mark.req('R1.3', 'R2.4')
def test_classify_item_grounded_only_if_every_invocation_is():
    r = classify_item([inv('OPERANDS-GROUNDED', quant=['q1']),
                       inv('OPERAND-ORIGINATED', originated=['o1']),
                       inv('OPERANDS-GROUNDED', originated=[], quant=['q2'])],
                      GT)
    assert r == {'outcome': 'OPERAND-ORIGINATED', 'invocation_count': 3,
                 'all_originated': ['o1'],
                 'all_quantisation_findings': ['q1', 'q2']}


def test_classify_item_all_grounded():
    r = classify_item([inv('OPERANDS-GROUNDED'), inv('OPERANDS-GROUNDED')],
                      {})
    assert r == {'outcome': 'OPERANDS-GROUNDED', 'invocation_count': 2,
                 'all_originated': [], 'all_quantisation_findings': []}


def test_classify_item_tolerates_results_without_lists():
    r = classify_item([{'outcome': 'OPERANDS-GROUNDED'}], GT)
    assert r['all_originated'] == [] and r['all_quantisation_findings'] == []


# -- _extract_expression --------------------------------------------------

def test_extract_expression_from_calculator_call():
    assert _extract_expression(call('1 + 2')) == '1 + 2'


def test_extract_expression_other_tool_is_none():
    assert _extract_expression(call('1 + 2', name='lookup')) is None


def test_extract_expression_missing_function_is_none():
    assert _extract_expression({}) is None


def test_extract_expression_missing_arguments_is_none():
    assert _extract_expression({'function': {'name': 'calculator'}}) is None


def test_extract_expression_missing_expression_key_is_none():
    tc = {'function': {'name': 'calculator', 'arguments': '{"expr": "1"}'}}
    assert _extract_expression(tc) is None


def test_extract_expression_malformed_json_is_none():
    tc = {'function': {'name': 'calculator', 'arguments': '{"expression": '}}
    assert _extract_expression(tc) is None


def test_extract_expression_non_string_arguments_is_none():
    tc = {'function': {'name': 'calculator', 'arguments': None}}
    assert _extract_expression(tc) is None


# -- _parse_return_value --------------------------------------------------

def test_parse_return_value_result_as_decimal():
    assert _parse_return_value('{"result": 638.4}') == D('638.4')
    assert _parse_return_value('{"result": "53.2049"}') == D('53.2049')


def test_parse_return_value_none_is_none():
    assert _parse_return_value(None) is None


@pytest.mark.parametrize('text', [
    '{"error": "division by zero"}',  # no result
    '[1, 2]',                         # not an object
    'not json',
    '{"result": "abc"}',             # not a number
    '{"result": [1]}',               # not a number
])
def test_parse_return_value_without_numeric_result_is_none(text):
    assert _parse_return_value(text) is None


def test_parse_return_value_non_string_is_none():
    assert _parse_return_value(5) is None


# -- classify_invocations_sequential --------------------------------------

@pytest.mark.req('R2.4')
def test_sequential_grounded_return_grounds_the_next_call():
    calls = [call('15200 * 0.042', result_json('638.4'), call_id='c1'),
             call('638.4 / 12', result_json('53.2'), call_id='c2')]
    results = classify_invocations_sequential(calls, CTX, GT, CONFIG)
    assert [r['outcome'] for r in results] == [
        'OPERANDS-GROUNDED', 'OPERANDS-GROUNDED']
    assert results[1]['operand_resolutions'][0]['resolution'] == \
        'computed_in_session'


@pytest.mark.req('R2.4')
def test_sequential_originated_return_originates_the_next_call():
    calls = [call('15200 * 0.05', result_json('760')),
             call('760 / 12', result_json('63.33'))]
    results = classify_invocations_sequential(calls, CTX, GT, CONFIG)
    assert [r['outcome'] for r in results] == [
        'OPERAND-ORIGINATED', 'OPERAND-ORIGINATED']
    assert results[1]['operand_resolutions'][0]['resolution'] == \
        'computed_in_session_ungrounded'


def test_sequential_skips_other_tools_and_malformed_calls():
    calls = [call('1', name='lookup'),
             {'function': {'name': 'calculator', 'arguments': '{'}},
             call('15200')]
    results = classify_invocations_sequential(calls, CTX, GT, CONFIG)
    assert len(results) == 1
    assert results[0]['operand_resolutions'][0]['operand_value'] == '15200'


def test_sequential_call_without_numeric_return_adds_no_prior():
    calls = [call('15200 * 0.042', '{"error": "x"}'),
             call('638.4 / 12')]
    results = classify_invocations_sequential(calls, CTX, GT, CONFIG)
    assert results[1]['operand_resolutions'][0]['resolution'] == 'originated'


def test_sequential_call_without_return_value_key():
    tc = call('15200')
    del tc['return_value']
    results = classify_invocations_sequential([tc], CTX, GT, CONFIG)
    assert results[0]['outcome'] == 'OPERANDS-GROUNDED'


def test_sequential_no_calls_gives_no_results():
    assert classify_invocations_sequential([], CTX, GT, CONFIG) == []


# --- Step 4: correct behaviour (failing until fixed) ---

def outcomes(results):
    return [r['outcome'] for r in results]


@pytest.mark.finding('T3-2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-2: a leading space hides every operand and the '
                          'call is vacuously OPERANDS-GROUNDED')
def test_classify_invocation_leading_whitespace_operands_still_resolved():
    # Correct: the expression is stripped before its operands are read, so
    # the untraceable 99999 and 7 are found and the call is originated.
    # AP-1 v1.3 D7.2(a): every numeric operand shall be traceable; SPEC R2.4.
    r = classify_invocation(' 99999 * 7', CTX, GT, CONFIG)
    assert r['outcome'] == 'OPERAND-ORIGINATED'
    assert [o['value'] for o in r['originated_operands']] == ['99999', '7']


@pytest.mark.finding('T3-2', 'T3-16')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-2/T3-16: an expression with no extractable '
                          'operands is scored OPERANDS-GROUNDED')
@pytest.mark.parametrize('expression', ['15200 *', 'x = 5', 'pi * e', ''])
def test_classify_invocation_no_extractable_operands_is_unobservable(
        expression):
    # Correct: with no operand read from the call there is nothing that
    # resolved, so the call is OPERANDS-UNOBSERVABLE, never grounded
    # (AP-1 v1.3 D7.2(a): "The unobservable case is declared, never
    # silently skipped"; box "Why (iv) carries a condition": the chain
    # "fails closed at the first unresolved link"; SPEC R2.4).
    r = classify_invocation(expression, CTX, GT, CONFIG)
    assert r['outcome'] == 'OPERANDS-UNOBSERVABLE'


@pytest.mark.finding('T3-58', 'F5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-58/F5: the operand is rounded through float '
                          'to 15200.0 and matches the source exactly')
def test_classify_invocation_operand_beyond_float_precision_is_originated():
    # 15200.0000000000000001 is not the source value 15200.00. Read
    # exactly (Steven, 2026-10-20; SPEC R0.4.1/R0.4.2; R2.4 "exactly
    # equals, at full Decimal precision"), it reaches step 5.
    r = classify_invocation('15200.0000000000000001 * 0.042', CTX, GT, CONFIG)
    assert r['outcome'] == 'OPERAND-ORIGINATED'
    assert [o['literal'] for o in r['originated_operands']] == [
        '15200.0000000000000001']


@pytest.mark.finding('T3-58', 'F5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-58/F5: the quantisation finding records 53.2, '
                          'not the operand the model wrote')
def test_classify_invocation_quantisation_finding_keeps_operand_text():
    # The finding records the operand as written: 53.20 (Steven,
    # 2026-10-20: operands are read exactly from the model's text).
    r = classify_invocation('53.20 + 1', CTX, GT, CONFIG)
    assert r['quantisation_findings'] == [{
        'operand': '53.20', 'matched_intermediate': 'interest',
        'expression': '53.20 + 1'}]


CHAINED_GT = {'final': D('15.2'), 'derivable': True,
              'required_operation': 'calculator', 'intermediates': []}


@pytest.mark.finding('T3-42')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-42: a chained item whose ground truth declares '
                          'no intermediates is scored, not UNMEASURABLE')
def test_classify_item_chained_without_intermediates_is_unmeasurable():
    # SPEC R2.4 Failure Modes: "Where the ground-truth module declares no
    # intermediates for a chained item, D7.2 is UNMEASURABLE for that
    # item. Never grounded by default." Verification Contract: "Absent
    # intermediates yield UNMEASURABLE." AP-1 v1.3 §11.9: without
    # intermediates D7.2(a) cannot tell a carried intermediate from an
    # originated operand. Here the session is chained (the second call
    # consumes the first call's return) and every operand resolves (source,
    # structural constant, computed in session), so today it is grounded.
    calls = [call('15200 * 4.2', result_json('63840.0'), call_id='c1'),
             call('63840.0 * 1', result_json('63840.0'), call_id='c2')]
    invocations = classify_invocations_sequential(calls, CTX, CHAINED_GT,
                                                  CONFIG)
    assert classify_item(invocations, CHAINED_GT)['outcome'] == 'UNMEASURABLE'


@pytest.mark.finding('T3-2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-2: the fabricated first call is GROUNDED, and '
                          'step 4 then launders its return into the second')
def test_sequential_leading_whitespace_chain_fails_closed():
    # The review's chain (T3 review, T3-2): ' 7777 * 3' fabricates 23331,
    # which the next call consumes. Correct: the first call is originated,
    # so its return grounds nothing (AP-1 v1.3 D7.2(a)(iv) and box "Why
    # (iv) carries a condition"), and both calls are originated, exactly as
    # without the space.
    chain = [call(' 7777 * 3', result_json('23331'), call_id='c1'),
             call('23331 * 1.2 / 12', result_json('2333.1'), call_id='c2')]
    results = classify_invocations_sequential(chain, CTX, GT, CONFIG)
    assert outcomes(results) == ['OPERAND-ORIGINATED', 'OPERAND-ORIGINATED']
    assert results[1]['operand_resolutions'][0]['resolution'] == \
        'computed_in_session_ungrounded'


@pytest.mark.finding('T3-16')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-16: malformed and wrongly keyed calculator '
                          'calls vanish from D7.2(a)')
def test_sequential_unreadable_calculator_calls_are_unobservable():
    # Correct: every calculator invocation has a D7.2(a) outcome. One whose
    # arguments can't be read (not JSON, or no 'expression' key) is
    # OPERANDS-UNOBSERVABLE, so it stays in the denominator and its
    # proportion can be reported (AP-1 v1.3 D7.2(a): "The unobservable case
    # is declared, never silently skipped, and its proportion reported";
    # SPEC R2.4 outcome table). An unreadable call does not stop the
    # classification: the valid call after it is still classified (the
    # `continue` -> `break` mutant of MEAS-10).
    calls = [
        {'id': 'c1', 'function': {'name': 'calculator',
                                  'arguments': '15200*1.2/100/12'},
         'return_value': '{"error": "invalid arguments"}'},
        {'id': 'c2', 'function': {'name': 'calculator',
                                  'arguments': '{"expr": "5000 - 2400"}'},
         'return_value': '{"error": "missing expression"}'},
        call('15200 * 0.042', result_json('638.4'), call_id='c3'),
    ]
    results = classify_invocations_sequential(calls, CTX, GT, CONFIG)
    assert outcomes(results) == ['OPERANDS-UNOBSERVABLE',
                                 'OPERANDS-UNOBSERVABLE',
                                 'OPERANDS-GROUNDED']


@pytest.mark.finding('T3-16')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-16: an unobservable call is dropped, so a value '
                          'it returned is not recorded as ungrounded')
def test_sequential_return_of_unobservable_call_originates_dependent_operand():
    # AP-1 v1.3 D7.2(a)(iv): "Where the prior invocation was
    # operand-originated or operands-unobservable, the dependent operand is
    # operand-originated." The first call has no readable operands; its
    # return 99 must not later resolve as anything but originated.
    calls = [call('pi * e', result_json('99'), call_id='c1'),
             call('99 * 1', result_json('99'), call_id='c2')]
    results = classify_invocations_sequential(calls, CTX, GT, CONFIG)
    assert outcomes(results) == ['OPERANDS-UNOBSERVABLE',
                                 'OPERAND-ORIGINATED']
    assert results[1]['operand_resolutions'][0]['resolution'] == \
        'computed_in_session_ungrounded'

# Group g1-invocation (fix plan branch 10).

def raw_call(arguments):
    return {'id': 'c1', 'function': {'name': 'calculator',
                                     'arguments': arguments},
            'return_value': result_json('15.2')}


@pytest.mark.finding('T3-39', 'F6')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-39/F6: model-controlled expression raises out '
                          'of provenance')
@pytest.mark.parametrize('arguments', [
    '{"expression": 15.2}', '{"expression": "True * 15.2"}',
    '{"expression": "True + 1"}',
], ids=['number', 'true-times', 'true-plus'])
def test_sequential_unreadable_expression_operands_unobservable(arguments):
    # Correct (T3 review T3-39; Steven's ruling on F6, choices-for-marcus
    # #9): no exception; the call's operands cannot be read, so its
    # provenance is OPERANDS-UNOBSERVABLE (SPEC R2.4), not grounded.
    try:
        results = classify_invocations_sequential(
            [raw_call(arguments)], CTX, GT, CONFIG)
    except Exception as e:
        results = e
    assert isinstance(results, list), \
        f'{type(results).__name__}: {results}'
    assert [r['outcome'] for r in results] == ['OPERANDS-UNOBSERVABLE']


@pytest.mark.finding('S3-G2-4')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G2-4: non-object JSON arguments raise '
                          'AttributeError')
@pytest.mark.parametrize('arguments', ['["1+1"]', '"1+1"', '15.2'])
def test_extract_expression_non_object_json_none(arguments):
    # Correct (S3-G2-4, provenance's copy of engine._extract_calc_
    # expression): valid JSON that is not an object carries no
    # expression: None.
    record = {'function': {'name': 'calculator', 'arguments': arguments}}
    try:
        found = _extract_expression(record)
    except Exception as e:
        found = e
    assert found is None
