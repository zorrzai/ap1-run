"""Unit tests for scoring/provenance/provenance_classify.py: provenance
of one invocation, of an item, and of a sequence of calls (D7.2(a))."""

import json
from decimal import Decimal

import pytest

from ap1_run.scoring.provenance.provenance_classify import (
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
