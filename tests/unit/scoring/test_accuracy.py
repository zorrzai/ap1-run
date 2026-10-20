"""Unit tests for scoring/accuracy.py: D1 accuracy of one item and the
summary across items (R2.1).

Pins today's behaviour, including known defects (marked with
@pytest.mark.finding).
"""

from decimal import Decimal

import pytest

from ap1_run.scoring.accuracy import (
    ADJUDICATED, CORRECT, INCORRECT, ITEM_UNMEASURABLE, NO_FIGURE,
    score_accuracy, summarise_accuracy,
)
from ap1_run.scoring.figure_id import (
    ADJUDICATE_AMBIGUOUS, ADJUDICATE_COLLISION, ADJUDICATE_DECLINE,
    ADJUDICATE_NO_MATCH, AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE,
    identify_figure,
)

D = Decimal
TOL = D('0.01')


def figure(outcome, released=None):
    return {'outcome': outcome, 'released_figure': released,
            'reason': 'r', 'extracted_tokens': None, 'matched_indices': []}


def score(fig, expected='15.20', tol=TOL, digits=None):
    return score_accuracy(fig, expected_value=D(expected),
                          answer_tolerance=tol, quantisation_digits=digits)


def response(content):
    return {'choices': [{'message': {'role': 'assistant',
                                     'content': content}}]}


def result(outcome, auto_scored):
    return {'outcome': outcome, 'auto_scored': auto_scored,
            'released_figure': None, 'expected_value': D('1'),
            'difference': None}


# -- constants ---------------------------------------------------------------

def test_accuracy_outcome_constants():
    assert (CORRECT, INCORRECT, NO_FIGURE, ADJUDICATED, ITEM_UNMEASURABLE) \
        == ('CORRECT', 'INCORRECT', 'NO-FIGURE', 'ADJUDICATED',
            'UNMEASURABLE')


# -- score_accuracy: routes --------------------------------------------------

@pytest.mark.req('R2.1')
def test_score_accuracy_unmeasurable_is_not_auto_scored():
    assert score(figure(UNMEASURABLE, D('15.20'))) == {
        'outcome': ITEM_UNMEASURABLE, 'auto_scored': False,
        'released_figure': None, 'expected_value': D('15.20'),
        'difference': None}


@pytest.mark.req('R2.1')
@pytest.mark.parametrize('outcome', [
    ADJUDICATE_DECLINE, ADJUDICATE_COLLISION, ADJUDICATE_AMBIGUOUS,
    ADJUDICATE_NO_MATCH])
def test_score_accuracy_adjudicate_outcomes_go_to_adjudication(outcome):
    assert score(figure(outcome, D('9'))) == {
        'outcome': ADJUDICATED, 'auto_scored': False,
        'released_figure': D('9'), 'expected_value': D('15.20'),
        'difference': None}


def test_score_accuracy_unknown_outcome_goes_to_adjudication():
    assert score(figure('SOMETHING-ELSE'))['outcome'] == ADJUDICATED


def test_score_accuracy_adjudicated_without_released_key_has_none():
    r = score({'outcome': ADJUDICATE_DECLINE})
    assert r['released_figure'] is None


@pytest.mark.req('R2.1')
def test_score_accuracy_auto_no_figure_is_auto_scored_no_figure():
    assert score(figure(AUTO_NO_FIGURE)) == {
        'outcome': NO_FIGURE, 'auto_scored': True, 'released_figure': None,
        'expected_value': D('15.20'), 'difference': None}


# -- score_accuracy: AUTO-MATCH ------------------------------------------------

@pytest.mark.req('R2.1')
def test_score_accuracy_auto_match_within_tolerance_is_correct():
    assert score(figure(AUTO_MATCH, D('15.21'))) == {
        'outcome': CORRECT, 'auto_scored': True,
        'released_figure': D('15.21'), 'expected_value': D('15.20'),
        'difference': D('0.01')}


@pytest.mark.req('R2.1')
def test_score_accuracy_auto_match_outside_tolerance_is_incorrect():
    assert score(figure(AUTO_MATCH, D('15.30'))) == {
        'outcome': INCORRECT, 'auto_scored': True,
        'released_figure': D('15.30'), 'expected_value': D('15.20'),
        'difference': D('0.10')}


def test_score_accuracy_difference_is_absolute():
    assert score(figure(AUTO_MATCH, D('15.10')))['difference'] == D('0.10')


@pytest.mark.finding('T3-78')
def test_score_accuracy_tolerance_bound_is_inclusive():
    # Q07 round-each (777.42) against round-once (777.41) with the shipped
    # tolerance 0.01 scores CORRECT. Correct: the shipped tolerance should
    # be able to tell the two apart (SPEC R0.4.1, round once).
    r = score(figure(AUTO_MATCH, D('777.42')), expected='777.41')
    assert r['outcome'] == CORRECT
    assert r['difference'] == D('0.01')


@pytest.mark.req('R2.1')
def test_score_accuracy_no_quantisation_compares_full_precision():
    r = score(figure(AUTO_MATCH, D('182.404')), expected='182.40',
              tol=D('0'))
    assert r['outcome'] == INCORRECT
    assert r['difference'] == D('0.004')


@pytest.mark.req('R2.1')
def test_score_accuracy_quantises_both_once_at_comparison():
    r = score(figure(AUTO_MATCH, D('182.404')), expected='182.396',
              tol=D('0'), digits=2)
    assert r['outcome'] == CORRECT
    assert r['difference'] == D('0.00')
    # The record keeps the unquantised figures.
    assert r['released_figure'] == D('182.404')
    assert r['expected_value'] == D('182.396')


def test_score_accuracy_quantisation_zero_digits_rounds_to_integer():
    r = score(figure(AUTO_MATCH, D('3.4')), expected='2.6', tol=D('0'),
              digits=0)
    assert r['outcome'] == CORRECT
    assert r['difference'] == D('0')


@pytest.mark.finding('T3-27')
def test_score_accuracy_quantisation_default_rounding_is_half_up():
    # Fixed (T3-27): quantisation used the Decimal default HALF_EVEN
    # (2.005 -> 2.00, INCORRECT against 2.015). The default of
    # quantisation_rounding is ROUND_HALF_UP: 2.01 vs 2.02, within 0.01.
    r = score(figure(AUTO_MATCH, D('2.005')), expected='2.015', digits=2)
    assert r['outcome'] == CORRECT
    assert r['difference'] == D('0.01')


@pytest.mark.finding('T3-27')
def test_score_accuracy_quantisation_zero_digits_rounds_half_up():
    # 2.5 -> 3 under HALF_UP, so 2.5 vs 2.9 (-> 3) differs by 0.
    r = score(figure(AUTO_MATCH, D('2.5')), expected='2.9', tol=D('0'),
              digits=0)
    assert r['outcome'] == CORRECT
    assert r['difference'] == D('0')


@pytest.mark.finding('T3-27')
def test_score_accuracy_declared_half_even_rounding_is_used():
    r = score_accuracy(figure(AUTO_MATCH, D('2.5')), expected_value=D('2.9'),
                       answer_tolerance=D('0'), quantisation_digits=0,
                       quantisation_rounding='ROUND_HALF_EVEN')
    assert (r['outcome'], r['difference']) == (INCORRECT, D('1'))


@pytest.mark.parametrize('mode, outcome', [
    ('ROUND_HALF_EVEN', INCORRECT),   # expected 2.5 -> 2, released 3
    ('ROUND_HALF_UP', CORRECT),       # expected 2.5 -> 3, released 3
])
def test_score_accuracy_declared_rounding_applies_to_the_expected_value(
        mode, outcome):
    r = score_accuracy(figure(AUTO_MATCH, D('2.9')), expected_value=D('2.5'),
                       answer_tolerance=D('0'), quantisation_digits=0,
                       quantisation_rounding=mode)
    assert r['outcome'] == outcome


def test_score_accuracy_unsupported_rounding_mode_raises():
    with pytest.raises(ValueError, match='unsupported rounding mode'):
        score_accuracy(figure(AUTO_MATCH, D('2.5')), expected_value=D('2.9'),
                       answer_tolerance=D('0'), quantisation_digits=0,
                       quantisation_rounding='ROUND_DOWN')


# -- score_accuracy with identify_figure (the live chain) ---------------------

def identify(content, expected):
    return identify_figure(response(content), expected_value=D(expected),
                           delivered_context={}, lookup_collision=False,
                           answer_tolerance=TOL)


@pytest.mark.finding('T3-3')
def test_score_accuracy_wrong_conclusion_with_one_matching_token_is_adjudicated():
    # The response concludes 182.40; the one token that equals the expected
    # 15.20 comes before it. Fixed (T3-3, SPEC R2.0): R2.0 no longer takes
    # 15.20 as the released figure, so D1 does not score it CORRECT; the
    # item goes to adjudication.
    fig = identify('Rate 1.2% on 15200 gives 15.20 a year? '
                   'No: answer is $182.40.', '15.20')
    assert score(fig, digits=2)['outcome'] == ADJUDICATED


@pytest.mark.finding('T3-3')
def test_score_accuracy_wrong_answer_is_adjudicated_never_incorrect():
    # A plainly wrong answer routes to adjudication, so on the live path
    # (no adjudication) D1 can never count it INCORRECT. This is SPEC
    # R2.0 ("does not conclude that a response containing unmatched
    # figures is wrong"; ruling on T3-3), so the report prints no
    # auto-scored rate while items await adjudication (report.py).
    fig = identify('The answer is $15.30.', '15.20')
    r = score(fig, digits=2)
    assert r['outcome'] == ADJUDICATED
    assert summarise_accuracy([r, score(identify('It is 15.20.', '15.20'),
                                        digits=2)])['accuracy_rate'] == D(1)


# -- summarise_accuracy --------------------------------------------------------

def test_summarise_accuracy_empty_has_no_rate():
    assert summarise_accuracy([]) == {
        'auto_scored_n': 0, 'adjudicated_n': 0, 'unmeasurable_n': 0,
        'correct': 0, 'incorrect': 0, 'no_figure': 0,
        'accuracy_rate': None}


@pytest.mark.req('R2.1')
def test_summarise_accuracy_reports_auto_and_adjudicated_n_separately():
    results = [result(CORRECT, True), result(INCORRECT, True),
               result(ADJUDICATED, False), result(ADJUDICATED, False),
               result(NO_FIGURE, True), result(ITEM_UNMEASURABLE, False)]
    assert summarise_accuracy(results) == {
        'auto_scored_n': 3, 'adjudicated_n': 2, 'unmeasurable_n': 1,
        'correct': 1, 'incorrect': 1, 'no_figure': 1,
        'accuracy_rate': D('0.5')}


def test_summarise_accuracy_rate_excludes_no_figure():
    results = [result(CORRECT, True), result(CORRECT, True),
               result(INCORRECT, True), result(NO_FIGURE, True)]
    s = summarise_accuracy(results)
    assert s['accuracy_rate'] == D(2) / D(3)


def test_summarise_accuracy_only_no_figure_has_no_rate():
    s = summarise_accuracy([result(NO_FIGURE, True)])
    assert s['auto_scored_n'] == 1
    assert s['accuracy_rate'] is None


def test_summarise_accuracy_all_incorrect_rate_is_zero():
    s = summarise_accuracy([result(INCORRECT, True)])
    assert s['accuracy_rate'] == D(0)


def test_summarise_accuracy_unmeasurable_is_in_neither_auto_nor_adjudicated():
    # D1 keeps UNMEASURABLE apart; the n of auto-scored plus adjudicated
    # is then one short of the items scored (cf. T3-66, in the report).
    s = summarise_accuracy([result(ITEM_UNMEASURABLE, False),
                            result(CORRECT, True)])
    assert (s['auto_scored_n'], s['adjudicated_n'], s['unmeasurable_n']) \
        == (1, 0, 1)


def test_summarise_accuracy_counts_outcomes_only_among_auto_scored():
    # A not-auto-scored record is never counted correct, whatever it says.
    s = summarise_accuracy([result(CORRECT, False)])
    assert (s['auto_scored_n'], s['adjudicated_n'], s['correct']) == (0, 0, 0)
    assert s['accuracy_rate'] is None


def test_summarise_accuracy_adjudicated_needs_not_auto_scored():
    s = summarise_accuracy([result(ADJUDICATED, True)])
    assert (s['auto_scored_n'], s['adjudicated_n']) == (1, 0)


def test_summarise_accuracy_missing_auto_scored_raises_key_error():
    with pytest.raises(KeyError):
        summarise_accuracy([{'outcome': CORRECT}])


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-27')
@pytest.mark.req('R2.1', 'R0.4.1')
def test_score_accuracy_declared_half_up_boundary_within_tolerance_is_correct():
    # SPEC R0.4.1: quantise once "using the declared rounding mode". Under
    # the shipped ROUND_HALF_UP, 2.005 -> 2.01 and 2.015 -> 2.02: they
    # differ by 0.01, within the 0.01 tolerance, so CORRECT. (Today:
    # 2.00 vs 2.02, INCORRECT; found by the T3 SCORE checker.)
    r = score_accuracy(figure(AUTO_MATCH, D('2.005')),
                       expected_value=D('2.015'), answer_tolerance=TOL,
                       quantisation_digits=2,
                       quantisation_rounding='ROUND_HALF_UP')
    assert r['outcome'] == CORRECT
    assert r['difference'] == D('0.01')
