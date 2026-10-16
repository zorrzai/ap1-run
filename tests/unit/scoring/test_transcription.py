"""Unit tests for scoring/transcription.py: the D7.3 transcription
check, which compares one tool return to the released figure (R2.5)."""

from decimal import Decimal, InvalidOperation

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
    }


def test_transcription_no_released_figure_despite_auto_match_is_unobservable():
    assert check_transcription(
        D('182.40'), None, figure_outcome=AUTO_MATCH) == {
        'outcome': 'UNOBSERVABLE',
        'tool_return': D('182.40'),
        'released_figure': None,
        'difference': None,
        'reason': 'released figure is None despite AUTO-MATCH',
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
def test_transcription_quantisation_rounds_half_even_tie_down():
    # Today: .quantize() without rounding= uses the context default,
    # ROUND_HALF_EVEN, so the tool's 430.745 quantises to 430.74 and a
    # release of 430.74 is EXACT. Correct: use the declared
    # quantisation.rounding (ROUND_HALF_UP in the shipped config), under
    # which 430.745 -> 430.75 and a release of 430.74 is ALTERED.
    r = check_transcription(D('430.745'), D('430.74'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_EXACT


@pytest.mark.finding('T3-27')
def test_transcription_quantisation_half_up_release_of_tie_is_altered():
    # Today: the correct HALF_UP release of 430.745 (430.75) is ALTERED.
    # Correct: under the declared HALF_UP policy it is EXACT.
    r = check_transcription(D('430.745'), D('430.75'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_ALTERED
    assert r['difference'] == D('0.005')


@pytest.mark.finding('T3-27')
def test_transcription_quantisation_has_no_rounding_parameter():
    # Today: the declared rounding mode cannot be passed in. Correct: the
    # caller passes quantisation.rounding, as for check_release_coverage.
    with pytest.raises(TypeError):
        check_transcription(D('1'), D('1'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2,
                            quantisation_rounding='ROUND_HALF_UP')


@pytest.mark.finding('T3-26')
def test_transcription_compares_a_single_tool_return():
    # Today: the check takes one tool return, and the runner passes the
    # last return of any tool. A response that releases an earlier return
    # (here 430.75, returned before 1437.00) is ALTERED, while release
    # coverage calls the same response GOVERNED-RELEASE. Correct: compare
    # the released figure against every return of the required operation.
    r = check_transcription(D('1437.00'), D('430.75'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)
    assert r['outcome'] == TRANSCRIBED_ALTERED


@pytest.mark.finding('T3-39')
def test_transcription_quantisation_of_infinite_return_raises():
    # Today: a tool return of 'inf' (the calculator gives it for
    # 1e300*1e300) raises InvalidOperation out of the check, which aborts
    # the run. Correct: an unquantisable return is UNOBSERVABLE (or
    # ALTERED), never an exception.
    with pytest.raises(InvalidOperation):
        check_transcription(D('Infinity'), D('430.75'), figure_outcome=AUTO_MATCH,
                            quantisation_digits=2)


def test_transcription_infinite_return_without_policy_is_altered():
    r = check_transcription(D('Infinity'), D('430.75'), figure_outcome=AUTO_MATCH)
    assert r['outcome'] == TRANSCRIBED_ALTERED
    assert r['difference'] == D('Infinity')
