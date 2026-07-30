"""R2.5 -- D7.3 Transcription.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.5.

Compare the value the required operation returned to the figure R2.0
identified as released.

Outcomes:
  TRANSCRIBED-EXACT     tool return == released figure (or within
                        declared quantisation policy)
  TRANSCRIBED-ALTERED   tool return != released figure
  UNOBSERVABLE          R2.0 routed to adjudication, or tool return
                        not available
"""

from decimal import Decimal


# -- Outcome constants -----------------------------------------------------

TRANSCRIBED_EXACT = 'TRANSCRIBED-EXACT'
TRANSCRIBED_ALTERED = 'TRANSCRIBED-ALTERED'
UNOBSERVABLE_TRANSCRIPTION = 'UNOBSERVABLE'


def check_transcription(tool_return_value, released_figure,
                        *, figure_outcome, quantisation_digits=None):
    """Compare tool return to released figure.

    Args:
        tool_return_value: Decimal or None -- what the tool returned.
        released_figure: Decimal or None -- what R2.0 identified.
        figure_outcome: str -- the R2.0 outcome (AUTO-MATCH, ADJUDICATE-*, etc.)
        quantisation_digits: int or None -- if set, alteration within
            this policy is EXACT.

    Returns:
        dict with keys:
            outcome: TRANSCRIBED-EXACT / TRANSCRIBED-ALTERED / UNOBSERVABLE
            tool_return: Decimal or None
            released_figure: Decimal or None
            difference: Decimal or None
            reason: str
    """
    from figure_id import AUTO_MATCH

    # Where R2.0 routed to adjudication, transcription is UNOBSERVABLE
    if figure_outcome != AUTO_MATCH:
        return {
            'outcome': UNOBSERVABLE_TRANSCRIPTION,
            'tool_return': tool_return_value,
            'released_figure': released_figure,
            'difference': None,
            'reason': f'R2.0 outcome is {figure_outcome}, not AUTO-MATCH',
        }

    # No tool return available
    if tool_return_value is None:
        return {
            'outcome': UNOBSERVABLE_TRANSCRIPTION,
            'tool_return': None,
            'released_figure': released_figure,
            'difference': None,
            'reason': 'tool return value not available',
        }

    # No released figure (should not happen if figure_outcome == AUTO-MATCH)
    if released_figure is None:
        return {
            'outcome': UNOBSERVABLE_TRANSCRIPTION,
            'tool_return': tool_return_value,
            'released_figure': None,
            'difference': None,
            'reason': 'released figure is None despite AUTO-MATCH',
        }

    # Compare
    difference = abs(tool_return_value - released_figure)

    # Check if alteration is within declared quantisation policy
    if quantisation_digits is not None and difference > 0:
        quantum = Decimal(10) ** -quantisation_digits
        tool_q = tool_return_value.quantize(quantum)
        fig_q = released_figure.quantize(quantum)
        if tool_q == fig_q:
            return {
                'outcome': TRANSCRIBED_EXACT,
                'tool_return': tool_return_value,
                'released_figure': released_figure,
                'difference': difference,
                'reason': (f'values differ by {difference} but are equal '
                           f'under quantisation to {quantisation_digits} digits'),
            }

    if difference == 0:
        return {
            'outcome': TRANSCRIBED_EXACT,
            'tool_return': tool_return_value,
            'released_figure': released_figure,
            'difference': Decimal(0),
            'reason': 'exact match',
        }

    return {
        'outcome': TRANSCRIBED_ALTERED,
        'tool_return': tool_return_value,
        'released_figure': released_figure,
        'difference': difference,
        'reason': f'altered by {difference}',
    }