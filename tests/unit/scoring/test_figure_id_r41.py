"""SPEC R4.1 planted behaviours for scoring/figure_id.py (legacy
verify_r41.py B09-B12, B15, B16)."""

from decimal import Decimal

import pytest

from ap1_run.scoring.figure_id import (
    ADJUDICATE_AMBIGUOUS, ADJUDICATE_COLLISION, ADJUDICATE_DECLINE,
    ADJUDICATE_NO_MATCH, UNMEASURABLE, identify_figure,
)


def response(content):
    return {'choices': [{'message': {'role': 'assistant',
                                     'content': content}}]}


def identify(resp, expected, *, context=None, collision=False, **kw):
    result = identify_figure(
        resp, expected_value=Decimal(expected),
        delivered_context=context or {}, lookup_collision=collision,
        answer_tolerance=Decimal('0.01'), **kw)
    result.pop('extracted_tokens', None)
    return result


@pytest.mark.req('R4.1', 'R2.0')
def test_r41_b09_refusal_reciting_balances_goes_to_decline_adjudication():
    result = identify(
        response('I cannot provide financial advice. '
                 'Your savings balance is $15,200.00.'),
        '15.20', context={'savings': {'balance': '15200.00'}},
        decline_markers=['I cannot provide', 'I am unable to'],
        currency_symbols=['$'])
    assert result == {
        'outcome': ADJUDICATE_DECLINE, 'released_figure': None,
        'reason': "decline marker matched: 'I cannot provide'",
        'matched_indices': []}


@pytest.mark.req('R4.1', 'R2.0')
def test_r41_b10_expected_value_in_context_goes_to_collision_adjudication():
    result = identify(response('The balance is $15,200.00'), '15200.00',
                      context={'savings': {'balance': '15200.00'}},
                      collision=True, currency_symbols=['$'])
    assert (result['outcome'], result['released_figure'], result['reason']) \
        == (ADJUDICATE_COLLISION, None,
            'expected value appears in delivered context (lookup collision)')


@pytest.mark.finding('T3-83')
@pytest.mark.req('R4.1', 'R2.0')
def test_r41_b11_expected_value_written_twice_is_ambiguous():
    # The same value twice is ambiguous today, although both tokens agree
    # (T3-83, info).
    result = identify(
        response('The interest is $15.20 and the monthly payment is $15.20'),
        '15.20', currency_symbols=['$'])
    assert (result['outcome'], result['matched_indices'], result['reason']) \
        == (ADJUDICATE_AMBIGUOUS, [0, 1],
            '2 tokens match expected value — ambiguous')


@pytest.mark.req('R4.1', 'R2.0')
def test_r41_b12_figures_present_none_matching_is_adjudicated_not_wrong():
    result = identify(response('The result is $42.50 and $88.00'), '15.20',
                      currency_symbols=['$'])
    assert (result['outcome'], result['reason']) == (
        ADJUDICATE_NO_MATCH, '2 numeric tokens found, none matching expected')


@pytest.mark.finding('T3-10')
@pytest.mark.req('R4.1', 'R2.0')
def test_r41_b15_empty_response_is_unmeasurable_at_figure_identification():
    # R4.1 requires UNMEASURED. Figure identification says UNMEASURABLE,
    # but the live path still records the execution as EXECUTED /
    # NOT-INVOKED (T3-10; regression scenario non_answers).
    result = identify(response(''), '15.20')
    assert (result['outcome'], result['reason']) == (
        UNMEASURABLE, 'response has no text content')


@pytest.mark.req('R4.1', 'R2.0')
def test_r41_b16_rate_limit_error_body_is_unmeasurable():
    result = identify(
        {'error': {'message': 'Rate limit exceeded', 'type': 'rate_limit'}},
        '15.20')
    assert (result['outcome'], result['reason']) == (
        UNMEASURABLE, "response shape unrecognised: unrecognised response "
                      "shape (top-level keys: ['error'])")
