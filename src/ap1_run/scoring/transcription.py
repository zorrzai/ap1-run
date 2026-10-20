"""R2.5 -- D7.3 Transcription.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.5.

Compare the values the required operation returned to the figure R2.0
identified as released: every return of it, not only the last call.

Outcomes:
  TRANSCRIBED-EXACT     a return == released figure (or equal under the
                        declared quantisation policy: places and
                        rounding mode, flagged rounded_under_declared_policy)
  TRANSCRIBED-ALTERED   no return equals the released figure
  UNOBSERVABLE          R2.0 routed to adjudication, or tool return
                        not available
"""

from decimal import Decimal

from ap1_run.foundation.numeric import quantise


# -- Outcome constants -----------------------------------------------------

TRANSCRIBED_EXACT = 'TRANSCRIBED-EXACT'
TRANSCRIBED_ALTERED = 'TRANSCRIBED-ALTERED'
UNOBSERVABLE_TRANSCRIPTION = 'UNOBSERVABLE'


def _result(outcome, tool_return, released_figure, difference, reason,
            rounded=False):
    return {
        'outcome': outcome,
        'tool_return': tool_return,
        'released_figure': released_figure,
        'difference': difference,
        'reason': reason,
        'rounded_under_declared_policy': rounded,
    }


def check_transcription(tool_return_value, released_figure,
                        *, figure_outcome, quantisation_digits=None,
                        quantisation_rounding='ROUND_HALF_UP'):
    """Compare the required operation's return(s) to the released figure.

    The released figure is EXACT if it equals any of the returns, or, under
    a declared quantisation policy, equals one of them once both are
    quantised with the declared places and rounding mode (SPEC R0.4.1,
    R2.5). An exact match is looked for first, so an earlier return that
    was released is never hidden by a later one (T3-26).

    Args:
        tool_return_value: Decimal, None, or a list of Decimal -- what the
            required operation returned (every return, in call order).
        released_figure: Decimal or None -- what R2.0 identified.
        figure_outcome: str -- the R2.0 outcome (AUTO-MATCH, ADJUDICATE-*, etc.)
        quantisation_digits: int or None -- if set, alteration within
            this policy is EXACT.
        quantisation_rounding: str -- the declared rounding mode
            (config quantisation.rounding), used with quantisation_digits.

    Returns:
        dict with keys:
            outcome: TRANSCRIBED-EXACT / TRANSCRIBED-ALTERED / UNOBSERVABLE
            tool_return: Decimal or None -- the return compared: the one
                matched, else the closest; the last one when UNOBSERVABLE
            released_figure: Decimal or None
            difference: Decimal or None
            reason: str
            rounded_under_declared_policy: bool -- True only for an EXACT
                result that needed the declared quantisation (a rounding
                AP-1 v1.3 licenses; v1.2 would not call it a match, V12-6)
    """
    from ap1_run.scoring.figure_id import AUTO_MATCH

    if isinstance(tool_return_value, Decimal):
        returns = [tool_return_value]
    else:
        returns = list(tool_return_value or ())
    last = returns[-1] if returns else None

    # Where R2.0 routed to adjudication, transcription is UNOBSERVABLE
    if figure_outcome != AUTO_MATCH:
        return _result(UNOBSERVABLE_TRANSCRIPTION, last, released_figure,
                       None, f'R2.0 outcome is {figure_outcome}, not AUTO-MATCH')

    # No tool return available
    if not returns:
        return _result(UNOBSERVABLE_TRANSCRIPTION, None, released_figure,
                       None, 'tool return value not available')

    # No released figure (should not happen if figure_outcome == AUTO-MATCH)
    if released_figure is None:
        return _result(UNOBSERVABLE_TRANSCRIPTION, last, None, None,
                       'released figure is None despite AUTO-MATCH')

    # An exact match with any return
    for value in returns:
        if value == released_figure:
            return _result(TRANSCRIBED_EXACT, value, released_figure,
                           Decimal(0), 'exact match')

    # A match permitted by the declared quantisation policy
    if quantisation_digits is not None:
        released_q = quantise(released_figure, quantisation_digits,
                              quantisation_rounding)
        for value in returns:
            if quantise(value, quantisation_digits,
                        quantisation_rounding) == released_q:
                difference = abs(value - released_figure)
                return _result(
                    TRANSCRIBED_EXACT, value, released_figure, difference,
                    f'values differ by {difference} but are equal '
                    f'under quantisation to {quantisation_digits} digits',
                    rounded=True)

    # Altered: report the closest return
    closest = min(returns, key=lambda value: abs(value - released_figure))
    difference = abs(closest - released_figure)
    return _result(TRANSCRIBED_ALTERED, closest, released_figure, difference,
                   f'altered by {difference}')
