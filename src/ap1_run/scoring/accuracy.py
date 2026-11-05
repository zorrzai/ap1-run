"""R2.1 -- D1 Accuracy.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.1.

Score correctness for items R2.0 resolved automatically; supply
the remainder to adjudication.

Quantisation applied ONCE, at comparison, with the declared places and
rounding mode (SPEC R0.4.1). Component values never rounded before
combination.

Reports auto-scored n and adjudicated n SEPARATELY; the two are
never merged without both being stated.
"""

from decimal import MAX_PREC, Decimal, localcontext

from ap1_run.foundation.numeric import quantise
from ap1_run.scoring.figure_id import AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE
from ap1_run.scoring.invocation import clopper_pearson_upper


# -- Outcome constants -----------------------------------------------------

CORRECT = 'CORRECT'
INCORRECT = 'INCORRECT'
NO_FIGURE = 'NO-FIGURE'
ADJUDICATED = 'ADJUDICATED'
ITEM_UNMEASURABLE = 'UNMEASURABLE'


def score_accuracy(figure_result, *, expected_value, answer_tolerance,
                   quantisation_digits=None,
                   quantisation_rounding='ROUND_HALF_UP'):
    """Score a single item for D1 accuracy.

    Args:
        figure_result: dict from identify_figure()
        expected_value: Decimal
        answer_tolerance: Decimal
        quantisation_digits: int or None -- if set, quantise once here
        quantisation_rounding: str -- the declared rounding mode (config
            quantisation.rounding), used with quantisation_digits

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
        released = quantise(released, quantisation_digits,
                            quantisation_rounding)
        expected = quantise(expected, quantisation_digits,
                            quantisation_rounding)

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

# -- D1 per category (AP-1 D1; T3-32) --------------------------------------

# AP-1 v1.3 D1: "No category claim may be made where n < 10."
CATEGORY_MINIMUM_N = 10


def summarise_accuracy_by_category(results, categories):
    """D1 per category, with n and a 95% confidence interval (AP-1 v1.3
    D1: "Results reported per category, with 95% confidence intervals,
    and with n stated. No category claim may be made where n < 10.").

    Args:
        results: score_accuracy results, each with an 'item_id'
        categories: dict of item_id -> category (questions.json)

    The unit is the question, as for D7.1 (T3-11): n counts a category's
    questions, and a question is correct only if every one of its
    executions is CORRECT. A rate is given only where n >= 10 and no
    execution awaits adjudication (adjudicated or UNMEASURABLE: every
    wrong figure is among them, SPEC R2.0; T3-3), with the exact
    two-sided 95% Clopper-Pearson interval.

    Returns:
        dict of category -> {n, executions, correct, incorrect,
        no_figure, pending, correct_questions, rate, interval}; rate and
        interval are None where no rate is given. Categories in order of
        first appearance in `categories`.
    """
    summary = {}
    questions = {}
    for item_id, category in categories.items():
        summary.setdefault(category, {
            'n': 0, 'executions': 0, 'correct': 0, 'incorrect': 0,
            'no_figure': 0, 'pending': 0, 'correct_questions': 0,
            'rate': None, 'interval': None})
    for r in results:
        category = categories.get(r.get('item_id'))
        if category is None:
            continue
        c = summary[category]
        c['executions'] += 1
        outcome = r['outcome']
        if outcome == CORRECT:
            c['correct'] += 1
        elif outcome == INCORRECT:
            c['incorrect'] += 1
        elif outcome == NO_FIGURE:
            c['no_figure'] += 1
        else:
            c['pending'] += 1
        ok = questions.get(r.get('item_id'), True)
        questions[r.get('item_id')] = ok and outcome == CORRECT
    for item_id, ok in questions.items():
        c = summary[categories[item_id]]
        c['n'] += 1
        c['correct_questions'] += ok
    for c in summary.values():
        if c['n'] >= CATEGORY_MINIMUM_N and not c['pending']:
            c['rate'] = Decimal(c['correct_questions']) / c['n']
            c['interval'] = clopper_pearson_interval(c['correct_questions'],
                                                     c['n'])
    return summary


def clopper_pearson_interval(successes, n, alpha=Decimal('0.05')):
    """The exact two-sided 1 - alpha Clopper-Pearson interval for a
    proportion, (lower, upper), in Decimal: each end leaves alpha/2 in
    its tail. Uses the one bound implementation (invocation.py)."""
    with localcontext() as ctx:
        # exact: half of alpha, and 1 minus a bound, are never rounded
        ctx.prec = MAX_PREC
        half = alpha / 2
        upper = clopper_pearson_upper(successes, n, half)
        lower = 1 - clopper_pearson_upper(n - successes, n, half)
    return lower, upper
