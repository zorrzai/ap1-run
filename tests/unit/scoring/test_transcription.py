"""Unit tests for scoring/transcription.py: the D7.3 transcription
check, which compares the returns of the required operation to the
released figure (R2.5)."""

from decimal import Decimal

import pytest

from ap1_run.scoring.figure_id import (
    ADJUDICATE_AMBIGUOUS, ADJUDICATE_DECLINE, AUTO_MATCH, AUTO_NO_FIGURE,
)
from ap1_run.scoring.transcription import (
    TRANSCRIBED_ALTERED, TRANSCRIBED_EXACT, UNOBSERVABLE_TRANSCRIPTION,
    check_transcription,
)

D = Decimal


def test_transcription_outcome_constants():
    assert TRANSCRIBED_EXACT == 'TRANSCRIBED-EXACT'
    assert TRANSCRIBED_ALTERED == 'TRANSCRIBED-ALTERED'
    assert UNOBSERVABLE_TRANSCRIPTION == 'UNOBSERVABLE'


# -- R2.0 did not auto-match ------------------------------------------------

@pytest.mark.req('R2.5')
def test_transcription_adjudicated_figure_is_unobservable():
    assert check_transcription(
        D('182.40'), D('182.40'), figure_outcome=ADJUDICATE_DECLINE) == {
        'outcome': 'UNOBSERVABLE',
        'tool_return': D('182.40'),
        'released_figure': D('182.40'),
        'difference': None,
        'reason': 'R2.0 outcome is ADJUDICATE-DECLINE, not AUTO-MATCH',
        'rounded_under_declared_policy': False,
    }


def test_transcription_any_non_auto_match_outcome_is_unobservable():
    for outcome in (ADJUDICATE_AMBIGUOUS, AUTO_NO_FIGURE, 'anything', None):
        r = check_transcription(D('1'), D('2'), figure_outcome=outcome,
                                quantisation_digits=2)
        assert r['outcome'] == UNOBSERVABLE_TRANSCRIPTION
        assert r['reason'] == f'R2.0 outcome is {outcome}, not AUTO-MATCH'


def test_transcription_figure_outcome_is_keyword_only():
    with pytest.raises(TypeError):
        check_transcription(D('1'), D('1'), AUTO_MATCH)


# -- missing values ---------------------------------------------------------

def test_transcription_no_tool_return_is_unobservable():
    assert check_transcription(
        None, D('182.40'), figure_outcome=AUTO_MATCH) == {
        'outcome': 'UNOBSERVABLE',
        'tool_return': None,
        'released_figure': D('182.40'),
        'difference': None,
        'reason': 'tool return value not available',
        'rounded_under_declared_policy': False,
    }


def test_transcription_no_released_figure_despite_auto_match_is_unobservable():
    assert check_transcription(
        D('182.40'), None, figure_outcome=AUTO_MATCH) == {
        'outcome': 'UNOBSERVABLE',
        'tool_return': D('182.40'),
        'released_figure': None,
        'difference': None,
        'reason': 'released figure is None despite AUTO-MATCH',
        'rounded_under_declared_policy': False,
    }


def test_transcription_adjudication_checked_before_missing_values():
    r = check_transcription(None, None, figure_outcome=ADJUDICATE_DECLINE)
    assert r['reason'] == 'R2.0 outcome is ADJUDICATE-DECLINE, not AUTO-MATCH'


def test_transcription_missing_tool_return_checked_before_missing_figure():
    r = check_transcription(None, None, figure_outcome=AUTO_MATCH)
    assert r['reason'] == 'tool return value not available'


# -- comparison without a quantisation policy -------------------------------

@pytest.mark.req('R2.5')
def test_transcription_equal_values_are_exact():
    assert check_transcription(
        D('182.40'), D('182.40'), figure_outcome=AUTO_MATCH) == {
        'outcome': 'TRANSCRIBED-EXACT',
        'tool_return': D('182.40'),
        'released_figure': D('182.40'),
        'difference': D(0),
        'reason': 'exact match',
        'rounded_under_declared_policy': False,
    }


def test_transcription_equal_values_with_different_exponent_are_exact():
    r = check_transcription(D('182.4'), D('182.400'), figure_outcome=AUTO_MATCH)
    assert r['outcome'] == TRANSCRIBED_EXACT
    assert r['reason'] == 'exact match'


@pytest.mark.req('R2.5')
def test_transcription_different_values_are_altered():
    assert check_transcription(
        D('182.50'), D('182.40'), figure_outcome=AUTO_MATCH) == {
        'outcome': 'TRANSCRIBED-ALTERED',
        'tool_return': D('182.50'),
        'released_figure': D('182.40'),
        'difference': D('0.10'),
        'reason': 'altered by 0.10',
        'rounded_under_declared_policy': False,
    }


def test_transcription_difference_is_absolute():
    r = check_transcription(D('182.40'), D('182.50'), figure_outcome=AUTO_MATCH)
    assert r['outcome'] == TRANSCRIBED_ALTERED
    assert r['difference'] == D('0.10')


def test_transcription_without_policy_any_difference_is_altered():
    r = check_transcription(D('182.404'), D('182.40'), figure_outcome=AUTO_MATCH)
    assert r['outcome'] == TRANSCRIBED_ALTERED
    assert r['difference'] == D('0.004')
    assert r['reason'] == 'altered by 0.004'


def test_transcription_sign_inversion_is_altered():
    r = check_transcription(D('-182.40'), D('182.40'), figure_outcome=AUTO_MATCH)
    assert r['outcome'] == TRANSCRIBED_ALTERED
    assert r['difference'] == D('364.80')


# -- comparison under a declared quantisation policy ------------------------

@pytest.mark.req('R2.5')
def test_transcription_difference_within_quantisation_is_exact():
    assert check_transcription(
        D('182.404'), D('182.40'), figure_outcome=AUTO_MATCH,
        quantisation_digits=2) == {
        'outcome': 'TRANSCRIBED-EXACT',
        'tool_return': D('182.404'),
        'released_figure': D('182.40'),
        'difference': D('0.004'),
        'reason': ('values differ by 0.004 but are equal under '
                   'quantisation to 2 digits'),
        'rounded_under_declared_policy': True,
    }


def test_transcription_difference_beyond_quantisation_is_altered():
    r = check_transcription(D('182.416'), D('182.40'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)
    assert r == {
        'outcome': 'TRANSCRIBED-ALTERED',
        'tool_return': D('182.416'),
        'released_figure': D('182.40'),
        'difference': D('0.016'),
        'reason': 'altered by 0.016',
        'rounded_under_declared_policy': False,
    }


def test_transcription_equal_values_with_policy_take_exact_match_reason():
    r = check_transcription(D('182.40'), D('182.40'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_EXACT
    assert r['difference'] == D(0)
    assert r['reason'] == 'exact match'


def test_transcription_quantisation_digits_set_the_quantum():
    # 0.04 apart: equal at 1 digit (182.4), not at 2 (182.40 vs 182.44).
    r1 = check_transcription(D('182.44'), D('182.40'), figure_outcome=AUTO_MATCH,
                             quantisation_digits=1)
    r2 = check_transcription(D('182.44'), D('182.40'), figure_outcome=AUTO_MATCH,
                             quantisation_digits=2)
    assert r1['outcome'] == TRANSCRIBED_EXACT
    assert r1['reason'].endswith('quantisation to 1 digits')
    assert r2['outcome'] == TRANSCRIBED_ALTERED


def test_transcription_zero_digits_quantise_to_integers():
    r = check_transcription(D('182.4'), D('182'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=0)
    assert r['outcome'] == TRANSCRIBED_EXACT


def test_transcription_quantisation_rounds_both_sides():
    # Neither value is at the declared precision; both quantise to 182.40.
    r = check_transcription(D('182.404'), D('182.396'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_EXACT
    assert r['difference'] == D('0.008')


@pytest.mark.finding('T3-27')
def test_transcription_quantisation_default_rounding_is_half_up():
    # Fixed (T3-27): quantisation used the Decimal default HALF_EVEN
    # (430.745 -> 430.74). It now uses quantisation_rounding, whose default
    # is ROUND_HALF_UP, as in numeric.quantise and the config loader.
    r1 = check_transcription(D('430.745'), D('430.75'),
                             figure_outcome=AUTO_MATCH, quantisation_digits=2)
    r2 = check_transcription(D('430.745'), D('430.74'),
                             figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert (r1['outcome'], r1['difference']) == (TRANSCRIBED_EXACT, D('0.005'))
    assert (r2['outcome'], r2['difference']) == (TRANSCRIBED_ALTERED,
                                                 D('0.005'))


@pytest.mark.finding('T3-27')
def test_transcription_declared_half_even_rounding_is_used():
    r = check_transcription(D('430.745'), D('430.74'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2,
                            quantisation_rounding='ROUND_HALF_EVEN')
    assert r['outcome'] == TRANSCRIBED_EXACT
    assert r['rounded_under_declared_policy'] is True


def test_transcription_declared_rounding_applies_to_the_released_figure():
    # A released 430.745 is 430.74 under HALF_EVEN (EXACT against the
    # return 430.74) and 430.75 under HALF_UP (ALTERED).
    outcomes = [check_transcription(D('430.74'), D('430.745'),
                                    figure_outcome=AUTO_MATCH,
                                    quantisation_digits=2,
                                    quantisation_rounding=mode)['outcome']
                for mode in ('ROUND_HALF_EVEN', 'ROUND_HALF_UP')]
    assert outcomes == [TRANSCRIBED_EXACT, TRANSCRIBED_ALTERED]


def test_transcription_unsupported_rounding_mode_raises():
    with pytest.raises(ValueError, match='unsupported rounding mode'):
        check_transcription(D('430.745'), D('430.74'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2,
                            quantisation_rounding='ROUND_SIDEWAYS')


def test_transcription_rounding_mode_unused_for_an_exact_match():
    # The quantisation is only reached when no return matches exactly.
    r = check_transcription(D('430.74'), D('430.74'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2,
                            quantisation_rounding='ROUND_SIDEWAYS')
    assert (r['outcome'], r['reason']) == (TRANSCRIBED_EXACT, 'exact match')


@pytest.mark.finding('T3-26')
def test_transcription_single_other_return_is_altered():
    # With one return, a released figure that differs from it is ALTERED.
    # (T3-26 was that the runner passed only the last return of any tool;
    # it now passes every return of the required operation, below.)
    r = check_transcription(D('1437.00'), D('430.75'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_ALTERED


# -- several returns of the required operation (T3-26) ----------------------

@pytest.mark.finding('T3-26')
@pytest.mark.req('R2.5')
def test_transcription_release_of_an_earlier_return_is_exact():
    r = check_transcription([D('430.75'), D('1437.0')], D('430.75'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert r == {'outcome': TRANSCRIBED_EXACT, 'tool_return': D('430.75'),
                 'released_figure': D('430.75'), 'difference': D(0),
                 'reason': 'exact match',
                 'rounded_under_declared_policy': False}


def test_transcription_exact_match_preferred_to_an_earlier_rounded_one():
    r = check_transcription([D('430.749'), D('430.75')], D('430.75'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert (r['tool_return'], r['reason'],
            r['rounded_under_declared_policy']) == (D('430.75'), 'exact match',
                                                    False)


def test_transcription_rounded_match_with_a_later_return():
    r = check_transcription([D('1437.0'), D('430.749')], D('430.75'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert r == {'outcome': TRANSCRIBED_EXACT, 'tool_return': D('430.749'),
                 'released_figure': D('430.75'), 'difference': D('0.001'),
                 'reason': ('values differ by 0.001 but are equal under '
                            'quantisation to 2 digits'),
                 'rounded_under_declared_policy': True}


def test_transcription_first_of_several_rounded_matches_is_reported():
    r = check_transcription([D('430.751'), D('430.749')], D('430.75'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert r['tool_return'] == D('430.751')


def test_transcription_altered_reports_the_closest_return():
    r = check_transcription([D('1437.0'), D('430.70'), D('430.90')],
                            D('430.75'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)
    assert r == {'outcome': TRANSCRIBED_ALTERED, 'tool_return': D('430.70'),
                 'released_figure': D('430.75'), 'difference': D('0.05'),
                 'reason': 'altered by 0.05',
                 'rounded_under_declared_policy': False}


def test_transcription_altered_tie_reports_the_first_closest_return():
    r = check_transcription([D('430.80'), D('430.70')], D('430.75'),
                            figure_outcome=AUTO_MATCH)
    assert r['tool_return'] == D('430.80')


def test_transcription_empty_list_of_returns_is_unobservable():
    r = check_transcription([], D('430.75'), figure_outcome=AUTO_MATCH)
    assert (r['outcome'], r['tool_return'], r['reason']) == (
        UNOBSERVABLE_TRANSCRIPTION, None, 'tool return value not available')


def test_transcription_unobservable_shows_the_last_return():
    r1 = check_transcription([D('1'), D('2')], D('430.75'),
                             figure_outcome=ADJUDICATE_DECLINE)
    r2 = check_transcription((D('1'), D('2')), None, figure_outcome=AUTO_MATCH)
    assert (r1['tool_return'], r2['tool_return']) == (D('2'), D('2'))
    assert r2['reason'] == 'released figure is None despite AUTO-MATCH'


def test_transcription_infinite_return_without_policy_is_altered():
    r = check_transcription(D('Infinity'), D('430.75'), figure_outcome=AUTO_MATCH)
    assert r['outcome'] == TRANSCRIBED_ALTERED
    assert r['difference'] == D('Infinity')


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-27')
@pytest.mark.req('R2.5', 'R0.4.1')
@pytest.mark.parametrize('released, expected_outcome', [
    ('430.75', TRANSCRIBED_EXACT),     # the HALF_UP rounding of 430.745
    ('430.74', TRANSCRIBED_ALTERED),   # not licensed by HALF_UP
], ids=['licensed-rounding-exact', 'unlicensed-rounding-altered'])
def test_transcription_declared_half_up_policy_decides_the_tie(
        released, expected_outcome):
    # SPEC R0.4.1: quantisation uses "the declared rounding mode"; R2.5:
    # "an alteration permitted by the declared quantisation policy is
    # EXACT"; AP-1 v1.3 D7.3 (l.388): rounding not licensed by the
    # declared policy is ALTERED. The shipped config declares
    # ROUND_HALF_UP, under which the tool's 430.745 is 430.75.
    r = check_transcription(D('430.745'), D(released),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2,
                            quantisation_rounding='ROUND_HALF_UP')
    assert r['outcome'] == expected_outcome


@pytest.mark.finding('V12-6')
@pytest.mark.req('R2.5')
def test_transcription_licensed_rounding_is_exact_and_flagged_rounded():
    # Fix plan §2a, V12-6 (Steven, 2026-10-19: in scope): keep v1.3's
    # TRANSCRIBED-EXACT for rounding the declared policy licenses (Q07:
    # the tool returned 777.4125, the model released 777.41), and add a
    # sub-flag so a v1.2 reader can count the strict "match" cases. The
    # key name is this test's proposal: 'rounded_under_declared_policy'.
    r = check_transcription(D('777.4125'), D('777.41'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_EXACT
    assert r.get('rounded_under_declared_policy') is True


@pytest.mark.finding('V12-6')
@pytest.mark.req('R2.5')
def test_transcription_exact_match_is_flagged_not_rounded():
    # The sub-flag is False when the released figure equals the return
    # with no rounding (fix plan §2a, V12-6).
    r = check_transcription(D('430.75'), D('430.75'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_EXACT
    assert r.get('rounded_under_declared_policy') is False

# Group g1-invocation (fix plan branch 10).

@pytest.mark.finding('T3-39')
@pytest.mark.parametrize('value', ['Infinity', '1e+60'])
def test_transcription_unquantisable_return_altered_or_unobservable(value):
    # Correct (T3 review T3-39, the step-3 pin's own comment): a tool
    # return that cannot be quantised is UNOBSERVABLE (or ALTERED), never
    # an exception.
    try:
        r = check_transcription(D(value), D('430.75'),
                                figure_outcome=AUTO_MATCH,
                                quantisation_digits=2)
    except Exception as e:
        r = {'outcome': e}
    assert r['outcome'] in (UNOBSERVABLE_TRANSCRIPTION, TRANSCRIBED_ALTERED), r


# Step 5 (run-robustness): values that cannot be quantised or ordered
# (T3-39).

@pytest.mark.finding('T3-39')
def test_transcription_unquantisable_released_figure_matches_nothing():
    r = check_transcription(D('430.75'), D('1e+60'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_ALTERED


@pytest.mark.finding('T3-39')
def test_transcription_nan_return_never_the_closest_beside_a_number():
    # The calculator gives 'nan' for inf - inf; NaN does not order, so the
    # closest return is the number.
    r = check_transcription([D('NaN'), D('430'), D('NaN')], D('430.75'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert (r['outcome'], r['tool_return'], r['difference']) == (
        TRANSCRIBED_ALTERED, D('430'), D('0.75'))


@pytest.mark.finding('T3-39')
def test_transcription_only_nan_returns_altered_by_nan():
    r = check_transcription([D('NaN')], D('430.75'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_ALTERED
    assert r['tool_return'].is_nan() and r['difference'].is_nan()


@pytest.mark.finding('T3-39')
def test_transcription_infinite_return_orders_before_nan():
    # inf against -inf is an infinite distance, not NaN: it is reported.
    r = check_transcription([D('NaN'), D('Infinity')], D('-Infinity'),
                            figure_outcome=AUTO_MATCH, quantisation_digits=2)
    assert (r['outcome'], r['tool_return']) == (
        TRANSCRIBED_ALTERED, D('Infinity'))
