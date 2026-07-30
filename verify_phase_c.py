"""Phase C verification tests.

Exit gates:
  1. Refusal reciting fixture balances -> adjudication, not scored as figure
  2. lookup_collision -> adjudication even on a single match
  3. Unrecognised response shape -> UNMEASURABLE, not AUTO-NO-FIGURE
  4. Zero-failure result prints confidence bound, never "100%" alone
  5. Zero base rate -> UNDEFINED
  6. D1 reports auto-scored and adjudicated n separately
  7. 49 rate-limited + 1 success -> UNMEASURED, not "1 distinct answer"
  8. Unexpected response shape -> EV-0, not EV-2 NOT-INVOKED (Phase B gate)
"""

import os
import sys
from decimal import Decimal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from figure_id import (
    identify_figure, AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE,
    ADJUDICATE_DECLINE, ADJUDICATE_COLLISION, ADJUDICATE_AMBIGUOUS,
    ADJUDICATE_NO_MATCH,
)
from accuracy import (
    score_accuracy, summarise_accuracy,
    CORRECT, INCORRECT, NO_FIGURE, ADJUDICATED, ITEM_UNMEASURABLE,
)
from reproducibility import (
    classify_mechanism, check_parameter_echo,
    STRUCTURAL, CONFIGURED, OBSERVED_ONLY, UNMEASURED,
)
from invocation import (
    measure_invocation, format_rate, compute_dpr, _exact_upper_bound,
)
from transcription import (
    check_transcription,
    TRANSCRIBED_EXACT, TRANSCRIBED_ALTERED,
    UNOBSERVABLE_TRANSCRIPTION,
)
from evidence import EV_0, EV_2


# =====================================================================
#  Helper: mock OpenAI response
# =====================================================================

def _openai_response(content, tool_calls=None):
    """Build a minimal OpenAI-shaped response."""
    msg = {'role': 'assistant', 'content': content}
    if tool_calls is not None:
        msg['tool_calls'] = tool_calls
    return {'choices': [{'message': msg}]}


def _mock_extract(text):
    """Mock extractor that returns (value, literal) tuples."""
    from numeric import extract_numeric_tokens
    return extract_numeric_tokens(text)


# =====================================================================
#  EXIT GATE 1: Refusal reciting fixture balances -> adjudication
# =====================================================================

def test_decline_with_balances_routes_to_adjudication():
    """A response that declines and recites three fixture balances
    routes to adjudication, NOT scored as a figure of any kind.
    This is the direct regression test for the V1 defect."""
    response = _openai_response(
        "I'm unable to provide financial advice. Your current balances are: "
        "Savings $15,200.00, Checking $4,500.00, Investment $22,750.00."
    )
    result = identify_figure(
        response,
        expected_value=Decimal('15200.00'),
        delivered_context={'savings': {'balance': '15200.00'}},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
        decline_markers=["unable to provide", "cannot provide"],
    )
    assert result['outcome'] == ADJUDICATE_DECLINE, \
        f'expected ADJUDICATE-DECLINE, got {result["outcome"]}'
    assert result['released_figure'] is None, \
        'declined response must not produce a released figure'
    return True


def test_decline_not_scored_as_figure_even_with_matching_numeric():
    """Even if the decline response contains the exact expected value,
    the decline marker takes priority and it is NOT auto-scored."""
    response = _openai_response(
        "I cannot provide this. The monthly payment would be $182.40."
    )
    result = identify_figure(
        response,
        expected_value=Decimal('182.40'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
        decline_markers=["cannot provide"],
    )
    assert result['outcome'] == ADJUDICATE_DECLINE, \
        f'expected ADJUDICATE-DECLINE even with matching figure, got {result["outcome"]}'
    return True


# =====================================================================
#  EXIT GATE 2: lookup_collision -> adjudication even on single match
# =====================================================================

def test_lookup_collision_adjudicates_even_single_match():
    """An item flagged lookup_collision routes to adjudication even
    where exactly one extracted value matches the expected."""
    response = _openai_response(
        "The balance in your savings account is $15,200.00."
    )
    result = identify_figure(
        response,
        expected_value=Decimal('15200.00'),
        delivered_context={'savings': {'balance': '15200.00'}},
        lookup_collision=True,
        answer_tolerance=Decimal('0.01'),
    )
    assert result['outcome'] == ADJUDICATE_COLLISION, \
        f'expected ADJUDICATE-COLLISION, got {result["outcome"]}'
    return True


# =====================================================================
#  EXIT GATE 3: Unrecognised response shape -> UNMEASURABLE
# =====================================================================

def test_anthropic_shape_unmeasurable_not_auto_no_figure():
    """An Anthropic-shaped response yields UNMEASURABLE, not AUTO-NO-FIGURE."""
    response = {
        'id': 'msg_01XFDUDYJgAACzvnptvVoYEL',
        'type': 'message',
        'role': 'assistant',
        'content': [{'type': 'text', 'text': 'The answer is $15.20.'}],
        'model': 'claude-sonnet-4-20250514',
    }
    result = identify_figure(
        response,
        expected_value=Decimal('15.20'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
    )
    assert result['outcome'] == UNMEASURABLE, \
        f'expected UNMEASURABLE for Anthropic shape, got {result["outcome"]}'
    assert 'Anthropic' in result['reason'], \
        f'reason should mention Anthropic: {result["reason"]}'
    return True


def test_gemini_shape_unmeasurable_not_auto_no_figure():
    """A Gemini-shaped response yields UNMEASURABLE, not AUTO-NO-FIGURE."""
    response = {
        'candidates': [{
            'content': {'parts': [{'text': 'The answer is $15.20.'}]},
            'finishReason': 'STOP',
        }],
    }
    result = identify_figure(
        response,
        expected_value=Decimal('15.20'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
    )
    assert result['outcome'] == UNMEASURABLE, \
        f'expected UNMEASURABLE for Gemini shape, got {result["outcome"]}'
    assert 'Gemini' in result['reason'], \
        f'reason should mention Gemini: {result["reason"]}'
    return True


# =====================================================================
#  EXIT GATE 4: Zero failures prints confidence bound, never "100%"
# =====================================================================

def test_exact_bound_in_range():
    """(a) For n=1..200, the bound is strictly > 0 and <= 1."""
    for n in range(1, 201):
        bound = _exact_upper_bound(n)
        assert bound > 0, f'bound <= 0 for n={n}: {bound}'
        assert bound <= 1, f'bound > 1 for n={n}: {bound}'
    return True


def test_exact_bound_n1():
    """(b) n=1 yields 95.0%."""
    result = format_rate(0, 1)
    assert '95.0%' in result, f'n=1 should yield 95.0%: {result}'
    return True


def test_exact_bound_n49():
    """(c) n=49 yields 5.9%."""
    result = format_rate(0, 49)
    assert '5.9%' in result, f'n=49 should yield 5.9%: {result}'
    return True


def test_exact_bound_n100():
    """(d) n=100 yields 3.0%."""
    result = format_rate(0, 100)
    assert '3.0%' in result, f'n=100 should yield 3.0%: {result}'
    return True


def test_100pct_never_printed_alone():
    """(e) The string '100%' never appears alone in any output."""
    for n in range(1, 201):
        result = format_rate(0, n)
        assert '100%' not in result, \
            f'100% appeared for n={n}: {result}'
    return True


def test_exact_and_rule_of_three_agree_above_30():
    """(f) For n >= 30, exact bound and 3/n agree within 1pp."""
    for n in range(30, 201):
        exact = _exact_upper_bound(n) * 100
        approx = Decimal(3) / Decimal(n) * 100
        diff = abs(exact - approx)
        assert diff <= Decimal('1.0'), \
            f'n={n}: exact={exact}, 3/n={approx}, diff={diff}pp > 1pp'
    return True


def test_nonzero_failures_prints_percentage():
    """Non-zero failures print k/n (X.X%)."""
    result = format_rate(3, 50)
    assert '3/50' in result, f'should contain 3/50: {result}'
    assert '6.0%' in result, f'should contain 6.0%: {result}'
    return True


# =====================================================================
#  EXIT GATE 5: Zero base rate -> UNDEFINED
# =====================================================================

def test_dpr_zero_base_undefined():
    """DPR is UNDEFINED where base invocation is zero, never 1.0."""
    dpr_val, dpr_str = compute_dpr(
        invoked_base=0, invoked_removed=0,
        n_base=50, n_removed=50)
    assert dpr_val is None, f'expected None for zero base, got {dpr_val}'
    assert 'UNDEFINED' in dpr_str, f'expected UNDEFINED: {dpr_str}'
    assert '1.0' not in dpr_str, f'must not contain 1.0: {dpr_str}'
    return True


def test_dpr_nonzero_base():
    """Normal DPR computation."""
    dpr_val, dpr_str = compute_dpr(
        invoked_base=45, invoked_removed=10,
        n_base=50, n_removed=50)
    assert dpr_val is not None
    # (0.9 - 0.2) / 0.9 = 0.7/0.9 ~= 77.8%
    assert '77.8%' in dpr_str, f'expected ~77.8%: {dpr_str}'
    return True


# =====================================================================
#  EXIT GATE 6: D1 reports auto-scored n and adjudicated n separately
# =====================================================================

def test_d1_separate_counts():
    """D1 reports auto-scored and adjudicated n separately."""
    results = [
        {'outcome': CORRECT, 'auto_scored': True,
         'released_figure': Decimal('15.20'), 'expected_value': Decimal('15.20'),
         'difference': Decimal('0')},
        {'outcome': INCORRECT, 'auto_scored': True,
         'released_figure': Decimal('15.30'), 'expected_value': Decimal('15.20'),
         'difference': Decimal('0.10')},
        {'outcome': ADJUDICATED, 'auto_scored': False,
         'released_figure': None, 'expected_value': Decimal('15.20'),
         'difference': None},
        {'outcome': ADJUDICATED, 'auto_scored': False,
         'released_figure': None, 'expected_value': Decimal('100.00'),
         'difference': None},
        {'outcome': NO_FIGURE, 'auto_scored': True,
         'released_figure': None, 'expected_value': Decimal('200.00'),
         'difference': None},
    ]
    summary = summarise_accuracy(results)
    assert summary['auto_scored_n'] == 3, \
        f'expected 3 auto-scored, got {summary["auto_scored_n"]}'
    assert summary['adjudicated_n'] == 2, \
        f'expected 2 adjudicated, got {summary["adjudicated_n"]}'
    assert summary['correct'] == 1
    assert summary['incorrect'] == 1
    assert summary['no_figure'] == 1
    # accuracy_rate = 1/(1+1) = 0.5
    assert summary['accuracy_rate'] == Decimal('0.5'), \
        f'expected 0.5, got {summary["accuracy_rate"]}'
    return True


# =====================================================================
#  EXIT GATE 7: 49 rate-limited + 1 success -> UNMEASURED
# =====================================================================

def test_49_limited_1_success_unmeasured():
    """49 rate-limited runs plus one success -> UNMEASURED,
    not '1 distinct answer'."""
    responses = []
    # 49 rate-limited
    for _ in range(49):
        responses.append({'error': True, 'status_code': 429, 'rate_limited': True})
    # 1 success
    responses.append(_openai_response("The answer is $15.20."))

    result = classify_mechanism(
        responses, surface='prose', minimum_runs=3)
    assert result['mechanism'] == UNMEASURED, \
        f'expected UNMEASURED, got {result["mechanism"]}'
    assert result['successful_runs'] == 1, \
        f'expected 1 successful, got {result["successful_runs"]}'
    assert '1 distinct' not in result['reason'].lower(), \
        f'must not say "1 distinct answer": {result["reason"]}'
    return True


# =====================================================================
#  Additional exit gates
# =====================================================================

def test_cross_class_aggregate_warning():
    """Aggregate spanning two evidence classes warns they are not comparable."""
    items = [
        {'item_id': 'Q1', 'condition': 'base', 'invoked': True,
         'evidence_class': EV_2},
        {'item_id': 'Q2', 'condition': 'base', 'invoked': False,
         'evidence_class': EV_0},
    ]
    result = measure_invocation(items)
    assert result['cross_class_warning'] is not None, \
        'should warn about cross-class aggregate'
    assert 'not comparable' in result['cross_class_warning'], \
        f'warning should mention not comparable: {result["cross_class_warning"]}'
    return True


def test_auto_match_exactly_one():
    """Exactly one matching token -> AUTO-MATCH."""
    response = _openai_response(
        "The monthly payment is $182.40."
    )
    result = identify_figure(
        response,
        expected_value=Decimal('182.40'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
    )
    assert result['outcome'] == AUTO_MATCH, \
        f'expected AUTO-MATCH, got {result["outcome"]}'
    assert result['released_figure'] == Decimal('182.40'), \
        f'expected 182.40, got {result["released_figure"]}'
    return True


def test_auto_no_figure():
    """No numeric tokens -> AUTO-NO-FIGURE."""
    response = _openai_response(
        "I would be happy to help you with your question."
    )
    result = identify_figure(
        response,
        expected_value=Decimal('182.40'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
    )
    assert result['outcome'] == AUTO_NO_FIGURE, \
        f'expected AUTO-NO-FIGURE, got {result["outcome"]}'
    return True


def test_two_matches_adjudicate_ambiguous():
    """Two matching values -> ADJUDICATE-AMBIGUOUS."""
    response = _openai_response(
        "The payment is $182.40 which I confirm is $182.40."
    )
    result = identify_figure(
        response,
        expected_value=Decimal('182.40'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
    )
    assert result['outcome'] == ADJUDICATE_AMBIGUOUS, \
        f'expected ADJUDICATE-AMBIGUOUS, got {result["outcome"]}'
    return True


def test_figures_none_matching_adjudicate():
    """Figures present but none matching -> ADJUDICATE, not scored incorrect."""
    response = _openai_response(
        "The savings balance is $15,200.00 and interest rate is 1.2%."
    )
    result = identify_figure(
        response,
        expected_value=Decimal('182.40'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
    )
    assert result['outcome'] == ADJUDICATE_NO_MATCH, \
        f'expected ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING, got {result["outcome"]}'
    return True


def test_transcription_exact():
    """Tool return equals released figure -> TRANSCRIBED-EXACT."""
    result = check_transcription(
        Decimal('182.40'), Decimal('182.40'),
        figure_outcome=AUTO_MATCH)
    assert result['outcome'] == TRANSCRIBED_EXACT
    return True


def test_transcription_altered():
    """Tool return differs from released figure -> TRANSCRIBED-ALTERED."""
    result = check_transcription(
        Decimal('182.50'), Decimal('182.40'),
        figure_outcome=AUTO_MATCH)
    assert result['outcome'] == TRANSCRIBED_ALTERED
    assert result['difference'] == Decimal('0.10')
    return True


def test_transcription_quantised_exact():
    """Alteration within quantisation policy -> TRANSCRIBED-EXACT."""
    result = check_transcription(
        Decimal('182.404'), Decimal('182.40'),
        figure_outcome=AUTO_MATCH,
        quantisation_digits=2)
    assert result['outcome'] == TRANSCRIBED_EXACT, \
        f'expected EXACT under quantisation, got {result["outcome"]}'
    return True


def test_transcription_unobservable_when_adjudicated():
    """Where R2.0 routed to adjudication, D7.3 is UNOBSERVABLE."""
    result = check_transcription(
        Decimal('182.40'), Decimal('182.40'),
        figure_outcome=ADJUDICATE_DECLINE)
    assert result['outcome'] == UNOBSERVABLE_TRANSCRIPTION, \
        f'expected UNOBSERVABLE, got {result["outcome"]}'
    return True


def test_parameter_echo_mismatch():
    """A parameter requested and silently ignored is a platform finding."""
    result = check_parameter_echo(
        {'temperature': '0.0', 'top_p': '1.0'},
        {'temperature': '0.7'})
    assert result['status'] == 'MISMATCH'
    assert len(result['findings']) >= 1
    assert any('silently ignored' in f for f in result['findings'])
    return True


def test_parameter_echo_unverified():
    """No echo -> UNVERIFIED."""
    result = check_parameter_echo(
        {'temperature': '0.0'}, None)
    assert result['status'] == 'UNVERIFIED'
    return True


def test_operator_declared_marked():
    """STRUCTURAL/CONFIGURED operator declarations are marked."""
    responses = [_openai_response("$15.20") for _ in range(5)]
    result = classify_mechanism(
        responses, surface='figures', minimum_runs=3,
        operator_declared=STRUCTURAL)
    assert result['mechanism'] == STRUCTURAL
    assert result['operator_declared'] is True
    assert 'operator-declared' in result['reason']
    return True


# =====================================================================
#  Run all
# =====================================================================

ALL_TESTS = [
    # Gate 1: refusal -> adjudication
    test_decline_with_balances_routes_to_adjudication,
    test_decline_not_scored_as_figure_even_with_matching_numeric,

    # Gate 2: lookup_collision -> adjudication
    test_lookup_collision_adjudicates_even_single_match,

    # Gate 3: unrecognised shape -> UNMEASURABLE
    test_anthropic_shape_unmeasurable_not_auto_no_figure,
    test_gemini_shape_unmeasurable_not_auto_no_figure,

    # Gate 4: exact Clopper-Pearson bound
    test_exact_bound_in_range,
    test_exact_bound_n1,
    test_exact_bound_n49,
    test_exact_bound_n100,
    test_100pct_never_printed_alone,
    test_exact_and_rule_of_three_agree_above_30,
    test_nonzero_failures_prints_percentage,

    # Gate 5: zero base -> UNDEFINED
    test_dpr_zero_base_undefined,
    test_dpr_nonzero_base,

    # Gate 6: D1 auto/adjudicated separate
    test_d1_separate_counts,

    # Gate 7: 49 limited + 1 success -> UNMEASURED
    test_49_limited_1_success_unmeasured,

    # Additional
    test_cross_class_aggregate_warning,
    test_auto_match_exactly_one,
    test_auto_no_figure,
    test_two_matches_adjudicate_ambiguous,
    test_figures_none_matching_adjudicate,
    test_transcription_exact,
    test_transcription_altered,
    test_transcription_quantised_exact,
    test_transcription_unobservable_when_adjudicated,
    test_parameter_echo_mismatch,
    test_parameter_echo_unverified,
    test_operator_declared_marked,
]


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    passed = failed = 0
    errors = []
    for fn in ALL_TESTS:
        name = fn.__name__
        try:
            if fn():
                passed += 1
                print(f'  PASS  {name}')
            else:
                failed += 1
                errors.append((name, 'returned False'))
                print(f'  FAIL  {name}')
        except Exception as e:
            failed += 1
            errors.append((name, str(e)))
            print(f'  FAIL  {name}: {e}')

    print(f'\nResults: {passed} passed, {failed} failed, '
          f'{passed + failed} total')
    if errors:
        print('\nFailures:')
        for n, e in errors:
            print(f'  {n}: {e}')
    raise SystemExit(0 if failed == 0 else 1)