"""R2.1 -- D1 Accuracy.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.1.

Score correctness for items R2.0 resolved automatically; supply
the remainder to adjudication.

Quantisation applied ONCE, at comparison. Component values never
rounded before combination.

Reports auto-scored n and adjudicated n SEPARATELY; the two are
never merged without both being stated.
"""

from decimal import Decimal

from figure_id import AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE


# -- Outcome constants -----------------------------------------------------

CORRECT = 'CORRECT'
INCORRECT = 'INCORRECT'
NO_FIGURE = 'NO-FIGURE'
ADJUDICATED = 'ADJUDICATED'
ITEM_UNMEASURABLE = 'UNMEASURABLE'


def score_accuracy(figure_result, *, expected_value, answer_tolerance,
                   quantisation_digits=None):
    """Score a single item for D1 accuracy.

    Args:
        figure_result: dict from identify_figure()
        expected_value: Decimal
        answer_tolerance: Decimal
        quantisation_digits: int or None -- if set, quantise once here

    Returns:
        dict with keys:
            outcome: CORRECT / INCORRECT / NO_FIGURE / ADJUDICATED / UNMEASURABLE
            auto_scored: bool -- True if scored without human review
            released_figure: Decimal or None
            expected_value: Decimal
            difference: Decimal or None
    """
    outcome_map = figure_result['outcome']

    # Items that R2.0 could not resolve automatically
    if outcome_map == UNMEASURABLE:
        return {
            'outcome': ITEM_UNMEASURABLE,
            'auto_scored': False,
            'released_figure': None,
            'expected_value': expected_value,
            'difference': None,
        }

    if outcome_map not in (AUTO_MATCH, AUTO_NO_FIGURE):
        # Routes to adjudication (DECLINE, COLLISION, AMBIGUOUS, NO_MATCH)
        return {
            'outcome': ADJUDICATED,
            'auto_scored': False,
            'released_figure': figure_result.get('released_figure'),
            'expected_value': expected_value,
            'difference': None,
        }

    if outcome_map == AUTO_NO_FIGURE:
        return {
            'outcome': NO_FIGURE,
            'auto_scored': True,
            'released_figure': None,
            'expected_value': expected_value,
            'difference': None,
        }

    # AUTO-MATCH: quantise once at comparison
    released = figure_result['released_figure']
    expected = expected_value

    if quantisation_digits is not None:
        released = released.quantize(Decimal(10) ** -quantisation_digits)
        expected = expected.quantize(Decimal(10) ** -quantisation_digits)

    difference = abs(released - expected)
    if difference <= answer_tolerance:
        return {
            'outcome': CORRECT,
            'auto_scored': True,
            'released_figure': figure_result['released_figure'],
            'expected_value': expected_value,
            'difference': difference,
        }
    else:
        return {
            'outcome': INCORRECT,
            'auto_scored': True,
            'released_figure': figure_result['released_figure'],
            'expected_value': expected_value,
            'difference': difference,
        }


def summarise_accuracy(results):
    """Summarise D1 accuracy across items.

    Reports auto-scored n and adjudicated n SEPARATELY, never merged.

    Returns:
        dict with keys:
            auto_scored_n: int
            adjudicated_n: int
            unmeasurable_n: int
            correct: int (auto-scored only)
            incorrect: int (auto-scored only)
            no_figure: int (auto-scored only)
            accuracy_rate: Decimal or None (correct / auto-scored with figures)
    """
    auto_scored = [r for r in results if r['auto_scored']]
    adjudicated = [r for r in results if not r['auto_scored']
                   and r['outcome'] == ADJUDICATED]
    unmeasurable = [r for r in results if r['outcome'] == ITEM_UNMEASURABLE]

    correct = sum(1 for r in auto_scored if r['outcome'] == CORRECT)
    incorrect = sum(1 for r in auto_scored if r['outcome'] == INCORRECT)
    no_figure = sum(1 for r in auto_scored if r['outcome'] == NO_FIGURE)

    scored_with_figures = correct + incorrect
    accuracy_rate = None
    if scored_with_figures > 0:
        accuracy_rate = Decimal(correct) / Decimal(scored_with_figures)

    return {
        'auto_scored_n': len(auto_scored),
        'adjudicated_n': len(adjudicated),
        'unmeasurable_n': len(unmeasurable),
        'correct': correct,
        'incorrect': incorrect,
        'no_figure': no_figure,
        'accuracy_rate': accuracy_rate,
    }