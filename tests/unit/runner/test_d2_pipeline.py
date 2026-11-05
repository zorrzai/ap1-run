"""D2's figures surface through the real pipeline: each response through
identify_figure (SPEC R2.0), its D2 answer (runner/executions.py
d2_answer_figure), and the classification of the question-condition
(scoring/reproducibility.py, SPEC R2.2; AP-1 D2 "distinct numeric
answers per question").

An answer R2.0 could not identify is unresolved: it is counted and
shown, never a value, and never evidence that the answers were stable.
"""

from decimal import Decimal as D

import pytest

from ap1_run.runner.executions import d2_answer_figure
from ap1_run.scoring.figure_id import identify_figure
from ap1_run.scoring.reproducibility import (
    OBSERVED_ONLY, UNMEASURED, classify_mechanism, distinct_figures_shown,
)

GRAMMAR = {'currency_symbols': ['$'], 'decimal_separator': '.',
           'grouping_separator': ','}


def response(content):
    return {'choices': [{'message': {'role': 'assistant',
                                     'content': content}}]}


def d2(texts, expected, *, collision=False, minimum_runs=None):
    """The figures cell of these responses, and the values shown."""
    responses = [response(t) for t in texts]
    figures = []
    for r, text in zip(responses, texts):
        fig = identify_figure(
            r, expected_value=D(expected), delivered_context={},
            lookup_collision=collision, answer_tolerance=D('0.01'),
            decline_markers=['cannot'], **GRAMMAR)
        figures.append(d2_answer_figure(fig, text, **GRAMMAR))
    cell = classify_mechanism(
        responses, surface='figures',
        minimum_runs=len(texts) if minimum_runs is None else minimum_runs,
        figures=figures)
    return cell, distinct_figures_shown(responses, figures)


def summary(cell):
    return (cell['mechanism'], cell['distinct_values'],
            cell.get('unresolved', 0))


@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2', 'R2.0')
def test_different_unresolved_answers_are_not_one_value():
    # Three different answers, each stated with its working: none is
    # identified, so none is a value. They read "1 distinct value" before.
    cell, shown = d2(['Interest 1006.25, so principal 500.00',
                      'Interest 1006.25, so principal 600.00',
                      'Interest 1006.25, so principal 700.00'], '430.75')
    assert summary(cell) == (UNMEASURED, None, 3)
    assert 'stability not established' in cell['reason']
    assert shown == []
    # Two wrong answers with working, the expected value in neither
    cell, _ = d2(['5000 - 2500 = 2500', '4800 - 2400 = 2400'], '2600')
    assert summary(cell) == (UNMEASURED, None, 2)


@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2', 'R2.0')
def test_the_same_answer_with_working_is_not_a_second_value():
    # Run F Q06: 144.00 released, and the same 144.00 with its working
    # routed to adjudication. It read "2: 144.00; no single figure".
    texts = (['The total annual cost is $144.00.'] * 3 +
             ['The total annual cost is $144.00 ($12 monthly fee x 12 '
              'months).'] * 2)
    cell, shown = d2(texts, '144.00')
    assert summary(cell) == (UNMEASURED, None, 2)
    assert shown == ['144.00']
    # The same answer stated twice is one identified value (R2.0 routes
    # the second to adjudication: two tokens match)
    cell, shown = d2(['2600', '2600, so the answer is 2600'], '2600')
    assert summary(cell) == (OBSERVED_ONLY, 1, 0)
    assert shown == ['2600']
    cell, shown = d2(['2600.00', 'It is 2600.00; yes, 2600.00.'], '9.99')
    assert summary(cell) == (OBSERVED_ONLY, 1, 0)


@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2', 'R2.0')
def test_variation_among_identified_answers_is_shown_as_a_lower_bound():
    cell, shown = d2(['2500.00', '2700.00', '5000 - 2400 = 2600. So 2600.'],
                     '2600')
    assert summary(cell) == (OBSERVED_ONLY, 2, 1)
    assert 'at least 2 distinct values' in cell['reason']
    assert shown == ['2500.00', '2700.00']


@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2', 'R2.0')
def test_collision_answers_are_read_for_d2():
    # A collision item is never auto-scored, and R2.0 returns before
    # extraction; its answers still differ, and D2 sees them.
    cell, shown = d2(['The answer is 14.00', 'The answer is 13.00'], '3.20',
                     collision=True)
    assert summary(cell) == (OBSERVED_ONLY, 2, 0)
    assert shown == ['14.00', '13.00']
    cell, _ = d2(['The answer is 14.00'] * 2, '3.20', collision=True)
    assert summary(cell) == (OBSERVED_ONLY, 1, 0)


@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2', 'R2.0')
def test_a_decline_is_unresolved_whatever_numbers_it_recites():
    # A decline reciting a balance (SPEC R4.1) is not an answer: its
    # number is not a D2 value, and two declines are not stability.
    cell, shown = d2(['I cannot compute it; your balance is 15200.00.'] * 2,
                     '15.20')
    assert summary(cell) == (UNMEASURED, None, 2)
    assert shown == []


@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2')
def test_too_few_runs_stays_unmeasured_before_anything_else():
    cell, _ = d2(['2600.00'], '2600', minimum_runs=2)
    assert summary(cell)[:2] == (UNMEASURED, None)
    assert 'below minimum' in cell['reason']
