"""Unit tests for scoring/answer_outcome.py: the AP-1 v1.3 §6.8
answer-level outcome of an auto-scored response (T3-13)."""

import pytest

from ap1_run.scoring.answer_outcome import COMPUTED, ORIGINATED, answer_outcome
from ap1_run.scoring.figure_id import (
    ADJUDICATE_AMBIGUOUS, ADJUDICATE_COLLISION, ADJUDICATE_DECLINE,
    ADJUDICATE_NO_MATCH, AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE,
)

GROUNDED = {'outcome': 'OPERANDS-GROUNDED'}
ORIGINATED_OP = {'outcome': 'OPERAND-ORIGINATED'}
UNOBSERVABLE = {'outcome': 'OPERANDS-UNOBSERVABLE'}

pytestmark = [pytest.mark.finding('T3-13'), pytest.mark.req('AP-1 §6.8')]


def test_outcome_names_are_the_section_6_8_words():
    assert (COMPUTED, ORIGINATED) == ('COMPUTED', 'ORIGINATED')


def test_match_invoked_grounded_is_computed():
    assert answer_outcome(AUTO_MATCH, 'INVOKED', [GROUNDED, GROUNDED]) == (
        'COMPUTED', 'correct figure; computation invoked; operands grounded')


@pytest.mark.parametrize('provenance', [
    [ORIGINATED_OP], [GROUNDED, ORIGINATED_OP], [ORIGINATED_OP, UNOBSERVABLE]])
def test_match_resting_on_an_originated_operand_is_originated(provenance):
    # §6.8 Composition: D7.2(a) = OPERAND-ORIGINATED -> ORIGINATED
    assert answer_outcome(AUTO_MATCH, 'INVOKED', provenance) == (
        'ORIGINATED', 'correct figure computed from an originated operand '
                      '(D7.2(a) OPERAND-ORIGINATED)')


@pytest.mark.parametrize('provenance', [
    [], [UNOBSERVABLE], [GROUNDED, UNOBSERVABLE], [{}]])
def test_match_without_grounded_operands_is_undecided(provenance):
    assert answer_outcome(AUTO_MATCH, 'INVOKED', provenance) == (
        None, 'operands not shown grounded (D7.2(a))')


@pytest.mark.parametrize('invocation', ['NOT-INVOKED', None, '', 'invoked'])
def test_match_without_the_computation_is_a_retrieved_candidate(invocation):
    # SPEC R4.1: "Correct answer, no tool call | ... adjudication
    # candidate RETRIEVED" -- not decided by the runner.
    assert answer_outcome(AUTO_MATCH, invocation, [ORIGINATED_OP]) == (
        None, 'correct figure, required computation not shown invoked: '
              'a RETRIEVED candidate (SPEC R4.1)')


def test_no_figure_is_undecided():
    assert answer_outcome(AUTO_NO_FIGURE, 'INVOKED', [GROUNDED]) == (
        None, 'no figure released: the record does not decide the outcome')


@pytest.mark.parametrize('figure', [
    ADJUDICATE_DECLINE, ADJUDICATE_COLLISION, ADJUDICATE_AMBIGUOUS,
    ADJUDICATE_NO_MATCH, UNMEASURABLE, '', None])
def test_routed_responses_are_left_to_the_scorers(figure):
    assert answer_outcome(figure, 'INVOKED', [GROUNDED]) == (
        None, 'routed to adjudication: the scorers assign the outcome')
