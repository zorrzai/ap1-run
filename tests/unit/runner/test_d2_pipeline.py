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


# -- the operator's declaration, and what D2 compares (T3-4) ---------------

import json  # noqa: E402
from pathlib import Path  # noqa: E402

from ap1_run.execution.evidence import EV_0, EV_2  # noqa: E402
from ap1_run.foundation.config import (  # noqa: E402
    d2_declared_classes, load_config,
)
from ap1_run.reporting import report  # noqa: E402
from ap1_run.runner.executions import (  # noqa: E402
    Findings, record_not_scored, score_execution,
)
from ap1_run.runner.summary import classify_reproducibility  # noqa: E402

REPO = Path(__file__).resolve().parents[3]
DECLARED_REASON = (
    'T3-4: the operator declares STRUCTURAL or CONFIGURED per surface in '
    'the settings field d2_declared, {surface: class}, sealed with the '
    'config; the field name and its shape are the author\'s design, '
    'requested in review')
LEFT_OUT_REASON = (
    'T3-4: D2 compares only replies that carry an answer: errored and EV-0 '
    'replies are left out of the comparison and counted in report section '
    '9; requested in review')


def config_with(tmp_path, **fields):
    """example/config.json with these fields, loaded as a run loads it."""
    raw = json.loads((REPO / 'example' / 'config.json').read_text('utf-8'))
    raw.update(fields)
    path = tmp_path / 'config.json'
    path.write_text(json.dumps(raw), encoding='utf-8')
    return load_config(path)


def section_9(d2, config):
    return report._section_d2_mechanisms({'d2_results': d2}, config)


def row(text, surface):
    """The §9 table row of Q01/base on this surface."""
    rows = [line for line in text.splitlines()
            if line.startswith(f'| Q01 | base | {surface} |')]
    assert len(rows) == 1, text
    return rows[0]


@pytest.mark.proposal(DECLARED_REASON)
@pytest.mark.req('R2.2', 'R0.1')
@pytest.mark.finding('T3-4')
def test_declared_configured_figures_reported_operator_declared(tmp_path):
    # SPEC R2.2: STRUCTURAL and CONFIGURED come from the operator and are
    # marked operator-declared. The declaration is a settings field, so
    # it is fixed before any result exists.
    config = config_with(tmp_path, repeat_count='3',
                         d2_declared={'figures': 'configured'})
    texts = ['The interest is $15.20.'] * 3
    d2 = classify_reproducibility(
        {('Q01', 'base'): [response(t) for t in texts]},
        config['repeat_count'], None, {('Q01', 'base'): [D('15.20')] * 3},
        d2_declared=d2_declared_classes(config))
    text = section_9(d2, config)
    assert '| `CONFIGURED` | operator-declared |' in row(text, 'figures')
    assert '| `OBSERVED-ONLY` | evidence: observed over 3 runs' in row(
        text, 'prose')
    assert '- figures: `CONFIGURED` (operator-declared)' in text.splitlines()


@pytest.mark.proposal(DECLARED_REASON)
@pytest.mark.req('R2.2')
@pytest.mark.finding('T3-4')
def test_two_surfaces_declared_differently_each_shown_on_its_own_line(
        tmp_path):
    # AP-1 asks per surface; SPEC R2.2: "A system declared STRUCTURAL for
    # figures and CONFIGURED for prose reports both, each marked
    # operator-declared". Here figures CONFIGURED and prose STRUCTURAL,
    # from the loaded settings file to report section 9.
    config = config_with(tmp_path, repeat_count='3',
                         d2_declared={'figures': 'configured',
                                      'prose': 'structural'})
    texts = ['The interest is $15.20.'] * 3
    d2 = classify_reproducibility(
        {('Q01', 'base'): [response(t) for t in texts]},
        config['repeat_count'], None, {('Q01', 'base'): [D('15.20')] * 3},
        d2_declared=d2_declared_classes(config))
    text = section_9(d2, config)
    lines = text.splitlines()
    assert '- figures: `CONFIGURED` (operator-declared)' in lines
    assert '- prose: `STRUCTURAL` (operator-declared)' in lines
    assert '| `CONFIGURED` | operator-declared |' in row(text, 'figures')
    assert '| `STRUCTURAL` | operator-declared |' in row(text, 'prose')


@pytest.mark.proposal(DECLARED_REASON)
@pytest.mark.req('R2.2', 'AP-1 D2.2')
@pytest.mark.finding('T3-4')
def test_declared_class_the_d22_cap_lowers_is_not_marked_declared():
    # A platform-rejected sampling parameter caps D2 at OBSERVED-ONLY
    # (AP-1 D2.2); a declared CONFIGURED then shows as the cap's
    # OBSERVED-ONLY, not as operator-declared.
    d2 = classify_reproducibility(
        {('Q01', 'base'): [response('The interest is $15.20.')] * 3}, 3,
        'D2.2 cap: temperature was platform-rejected.',
        {('Q01', 'base'): [D('15.20')] * 3},
        d2_declared={'figures': 'CONFIGURED'})
    cell = d2['Q01/base']['figures']
    assert (cell['mechanism'], cell['operator_declared']) == (
        OBSERVED_ONLY, False)
    assert '| `OBSERVED-ONLY` | evidence: observed over 3 runs' in row(
        section_9(d2, {'d2_declared': {'figures': 'configured'}}), 'figures')


@pytest.mark.proposal(LEFT_OUT_REASON)
@pytest.mark.req('AP-1 D2', 'R2.2')
@pytest.mark.finding('T3-4')
def test_errored_and_ev0_replies_among_50_left_out_and_counted():
    # 50 executions of Q01/base: one errored (recorded, not scored), one
    # executed at EV-0 whose reply states another figure, 48 the same
    # answer at EV-2. Neither the errored nor the EV-0 one is compared:
    # without the EV-0 reply's 700.00 the figures agree. Report section 9
    # prints how many were left out, by kind.
    findings = Findings()
    record_not_scored(findings, 'Q01', 'base', 1, 'UNMEASURED',
                      {'error': 'HTTP 500: boom', 'cause': 'transport_error'})
    for rep in range(2, 51):
        ev0 = rep == 2
        content = 'The interest is $700.00.' if ev0 else \
            'The interest is $638.40.'
        score_execution(
            findings, {'response': response(content), 'tool_calls': [],
                       'evidence_class': EV_0 if ev0 else EV_2,
                       'invocation_outcome': None if ev0 else 'NOT-INVOKED'},
            item_id='Q01', condition='base', rep=rep, expected=D('638.40'),
            ctx={}, collision=False,
            config={'quantisation': {'places': 2,
                                     'rounding': 'ROUND_HALF_UP'}},
            answer_tolerance=D('0.01'), decline_markers=['cannot'],
            currency_symbols=['$'])
    assert findings.d2_errored == {('Q01', 'base'): 1}
    assert len(findings.d2_responses[('Q01', 'base')]) == 49

    # At the configured 50 repeats the class is given on the 48 compared:
    # one value, the EV-0 reply's 700.00 not in it
    cell = classify_reproducibility(
        findings.d2_responses, 50, None, findings.d2_figures,
        d2_evidence=findings.d2_evidence,
        d2_errored=findings.d2_errored)['Q01/base']
    for surface in ('figures', 'prose'):
        assert cell[surface]['successful_runs'] == 48
        assert cell[surface]['left_out'] == {'errored': 1, 'EV-0': 1}
        assert cell[surface]['distinct_values'] == 1
    assert cell['figures']['mechanism'] == OBSERVED_ONLY
    assert cell['figures']['values'] == ['638.40']
    text = section_9({'Q01/base': cell}, {'repeat_count': 50})
    assert ('Left out of the comparison: 2 replies (1 errored, 1 EV-0). '
            'An errored or EV-0 reply has no answer to compare; an '
            'unreadable one has no shape to read.') in text.splitlines()
    assert '| 48 (1 errored, 1 EV-0 left out) |' in row(text, 'figures')
    # A reply whose shape cannot be read is also at EV-0: it is counted by
    # its cause, unreadable
    assert classify_mechanism(
        [{'output': 'x'}] + [response('$638.40')] * 2, surface='prose',
        minimum_runs=2, evidence=[EV_0, EV_2, EV_2])['left_out'] == {
            'unreadable': 1}


@pytest.mark.proposal(LEFT_OUT_REASON)
@pytest.mark.req('AP-1 D2', 'R2.2')
@pytest.mark.finding('T3-4')
def test_question_condition_whose_every_execution_errored_is_unmeasured():
    # No reply to compare at all: the question-condition is still
    # reported, UNMEASURED, with what was left out.
    d2 = classify_reproducibility({}, 3, None, None,
                                  d2_errored={('Q01', 'base'): 3})
    for surface in ('figures', 'prose'):
        assert d2['Q01/base'][surface]['mechanism'] == UNMEASURED
        assert d2['Q01/base'][surface]['left_out'] == {'errored': 3}


FLOOR_REASON = (
    'T3-4: a D2 class is given on the replies compared, at least two (the '
    'fewest that can show repetition); the floor of two is our reading, '
    'not a number AP-1 gives; requested in review')


@pytest.mark.proposal(FLOOR_REASON)
@pytest.mark.req('AP-1 D2', 'R2.2')
@pytest.mark.finding('T3-4')
def test_one_compared_reply_of_three_is_below_the_floor_of_two():
    # A configured 3 repeats: two errored leave one reply, too few to
    # compare; one errored leaves two, and the class is given on those two.
    one = classify_reproducibility(
        {('Q01', 'base'): [response('The interest is $638.40.')]}, 3, None,
        d2_errored={('Q01', 'base'): 2})['Q01/base']
    for surface in ('figures', 'prose'):
        assert one[surface]['mechanism'] == UNMEASURED
        assert one[surface]['reason'] == (
            '1 successful runs below minimum 2 (2 errored left out) '
            '— UNMEASURED')
    two = classify_reproducibility(
        {('Q01', 'base'): [response('The interest is $638.40.')] * 2}, 3,
        None, d2_errored={('Q01', 'base'): 1})['Q01/base']
    for surface in ('figures', 'prose'):
        assert two[surface]['mechanism'] == OBSERVED_ONLY
        assert two[surface]['successful_runs'] == 2
        assert two[surface]['left_out'] == {'errored': 1}
