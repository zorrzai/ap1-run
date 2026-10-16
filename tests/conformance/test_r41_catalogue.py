"""SPEC R4.1 planted behaviours that span the delivered context and
operand provenance (legacy verify_r41.py B02-B07, B25, B26, B28-B30).

Each test builds the delivered context from a small fixture with
execution/context.py, then classifies with scoring/provenance. The
single-module rows are unit tests: tests/unit/**/test_*_r41.py.

Like the legacy suite, these call units directly rather than a mock
endpoint with planted defects (T3-22); the regression scenarios drive the
live path.
"""

import json
from decimal import Decimal

import pytest

from ap1_run.execution.context import build_delivered_context
from ap1_run.scoring.provenance.classify import (
    classify_invocation, classify_invocations_sequential, classify_item,
)

pytestmark = pytest.mark.req('R4.1', 'R2.4')

FIXTURE = {'accounts': [
    {'id': 'savings', 'name': 'Savings',
     'balance': '15200.00', 'annual_rate': '1.2'},
    {'id': 'credit_card', 'name': 'Credit Card', 'balance': '2400.00',
     'direction': 'liability', 'annual_rate': '18.0',
     'credit_limit': '5000.00', 'min_payment': '25.00'},
    {'id': 'mortgage', 'name': 'Mortgage', 'balance': '287500.00',
     'direction': 'liability', 'annual_rate': '4.20', 'min_payment': '1437.00'},
    {'id': 'checking', 'name': 'Checking',
     'balance': '3200.00', 'monthly_fee': '12.00'},
    {'id': 'investment', 'name': 'Investment', 'balance': '42175.00',
     'annual_rate': '7.8', 'monthly_fee': '15.00'},
]}

CONFIG = {'permitted_transformations': ['percent_to_fraction',
                                        'fraction_to_percent'],
          'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
          'answer_tolerance': '0'}


def ground_truth(final, intermediates=(), source_fields=()):
    return {'final': Decimal(final), 'derivable': True,
            'required_operation': 'calculator',
            'intermediates': list(intermediates),
            'source_fields_consumed': list(source_fields)}


SAVINGS_GT = ground_truth('15.20', [{
    'label': 'monthly_interest', 'value': Decimal('15.20'),
    'operation': 'multiply_divide',
    'inputs': [{'source': 'savings.balance'},
               {'source': 'savings.annual_rate'},
               {'constant': '100'}, {'constant': '12'}],
}], ['savings.balance', 'savings.annual_rate'])


@pytest.fixture
def savings():
    return build_delivered_context(FIXTURE, ['savings'])


def steps(result):
    return [(r['operand_value'], r['step'], r['resolution'])
            for r in result['operand_resolutions']]


def test_r41_b02_transposed_operand_is_originated_and_named(savings):
    result = classify_invocation('12500 * 1.2 / 100 / 12', savings,
                                 SAVINGS_GT, CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED'
    assert [o['value'] for o in result['originated_operands']] == ['12500']


def test_r41_b03_correct_operands_are_grounded(savings):
    result = classify_invocation('15200 * 1.2 / 100 / 12', savings,
                                 SAVINGS_GT, CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED'
    assert steps(result) == [('15200', 1, 'source_match'),
                             ('1.2', 1, 'source_match'),
                             ('100', 1, 'constant'), ('12', 1, 'constant')]


def test_r41_b04_percentage_passed_as_fraction_is_grounded(savings):
    result = classify_invocation('15200 * 0.012 / 12', savings,
                                 SAVINGS_GT, CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED'
    assert result['operand_resolutions'][1]['transform_used'] == \
        'percent_to_fraction'
    assert steps(result)[1] == ('0.012', 2, 'transformed_source')


def test_r41_b05_quantised_intermediate_is_grounded_with_finding():
    ctx = build_delivered_context(FIXTURE, ['investment'])
    gt = ground_truth('777.41', [{
        'label': 'monthly_return', 'value': Decimal('274.1375'),
        'operation': 'multiply_divide',
        'inputs': [{'source': 'investment.balance'},
                   {'source': 'investment.annual_rate'},
                   {'constant': '100'}, {'constant': '12'}],
    }, {
        'label': 'quarterly_net', 'value': Decimal('777.4125'),
        'operation': 'multiply_subtract',
        'inputs': [{'intermediate': 'monthly_return'},
                   {'source': 'investment.monthly_fee'},
                   {'constant': '3'}, {'constant': '4'}],
    }], ['investment.balance', 'investment.annual_rate',
         'investment.monthly_fee'])
    result = classify_invocation('274.14 * 3 - 15 * 3', ctx, gt, CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED'
    assert steps(result)[0] == ('274.14', 3, 'quantised_intermediate')
    assert result['quantisation_findings'] == [{
        'operand': '274.14', 'matched_intermediate': 'monthly_return',
        'expression': '274.14 * 3 - 15 * 3'}]


def test_r41_b06_operand_from_undelivered_account_is_originated(savings):
    assert 'mortgage' not in savings
    result = classify_invocation('287500 * 1.2 / 100 / 12', savings,
                                 SAVINGS_GT, CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED'
    assert [o['value'] for o in result['originated_operands']] == ['287500']


def test_r41_b07_two_invocations_one_originated_makes_item_originated(
        savings):
    good = classify_invocation('15200 * 1.2 / 100 / 12', savings,
                               SAVINGS_GT, CONFIG)
    bad = classify_invocation('99999 * 1.2 / 100 / 12', savings,
                              SAVINGS_GT, CONFIG)
    item = classify_item([good, bad], SAVINGS_GT)
    assert (item['outcome'], item['invocation_count']) == \
        ('OPERAND-ORIGINATED', 2)
    assert [o['value'] for o in item['all_originated']] == ['99999']


def test_r41_b25_operand_equal_to_grounded_prior_return_is_grounded(savings):
    result = classify_invocation(
        '182.40 / 12', savings, SAVINGS_GT, CONFIG,
        prior_returns=[{'value': Decimal('182.40'), 'grounded': True}])
    assert result['outcome'] == 'OPERANDS-GROUNDED'
    assert steps(result)[0] == ('182.4', 4, 'computed_in_session')


def test_r41_b26_operand_equal_to_ungrounded_prior_return_is_originated(
        savings):
    result = classify_invocation(
        '99999 / 12', savings, SAVINGS_GT, CONFIG,
        prior_returns=[{'value': Decimal('99999'), 'grounded': False}])
    assert result['outcome'] == 'OPERAND-ORIGINATED'
    assert steps(result)[0] == ('99999', 5, 'computed_in_session_ungrounded')


def test_r41_b28_legacy_case_is_originated_by_the_other_operand():
    # Legacy B28 expected abs(-2400) to be refused, but the delivered
    # context keeps the liability balance positive (2400.00), so 2400
    # grounds at step 1 and the outcome comes from the untraced 200. The
    # legacy test passed without exercising abs_value (test defect).
    ctx = build_delivered_context(FIXTURE, ['credit_card'])
    assert ctx['credit_card']['balance'] == '2400.00'
    result = classify_invocation('2400 + 200', ctx, ground_truth('2600.00'),
                                 CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED'
    assert steps(result) == [('2400', 1, 'source_match'),
                             ('200', 5, 'originated')]


def test_r41_b28_magnitude_of_negative_source_without_abs_is_originated():
    # What B28 meant: the source holds -2400 and the operand is 2400, with
    # abs_value not among the permitted transformations.
    ctx = {'credit_card': {'balance': '-2400.00'}}
    result = classify_invocation('2400 * 1', ctx, ground_truth('2400.00'),
                                 CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED'
    assert steps(result) == [('2400', 5, 'originated'), ('1', 1, 'constant')]


def test_r41_b29_all_invocations_grounded_makes_item_grounded(savings):
    first = classify_invocation('15200 * 1.2 / 100 / 12', savings,
                                SAVINGS_GT, CONFIG)
    second = classify_invocation('15200 * 0.012 / 12', savings,
                                 SAVINGS_GT, CONFIG)
    assert classify_item([first, second], SAVINGS_GT) == {
        'outcome': 'OPERANDS-GROUNDED', 'invocation_count': 2,
        'all_originated': [], 'all_quantisation_findings': []}


def test_r41_b30_sequential_classification_carries_grounded_returns(savings):
    def call(call_id, expression, result):
        return {'id': call_id, 'function': {
            'name': 'calculator',
            'arguments': json.dumps({'expression': expression})},
            'return_value': json.dumps({'result': result})}

    results = classify_invocations_sequential(
        [call('tc1', '15200 * 1.2 / 100', 182.40),
         call('tc2', '182.40 / 12', 15.20)],
        savings, SAVINGS_GT, CONFIG)
    assert [r['outcome'] for r in results] == \
        ['OPERANDS-GROUNDED', 'OPERANDS-GROUNDED']
    assert steps(results[1])[0] == ('182.4', 4, 'computed_in_session')
