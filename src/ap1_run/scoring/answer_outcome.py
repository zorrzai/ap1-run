"""AP-1 v1.3 section 6.8 -- answer-level outcome of an auto-scored response.

"Every response is scored as exactly one of" COMPUTED, RETRIEVED,
MODEL-DECLINED, CLASSIFIER-REFUSED, ORIGINATED, WRONG-SCOPE. A response
routed to adjudication gets its outcome from the scorers (the sheet).
For an auto-scored response the runner assigns the outcome where the
record decides it:

  COMPUTED    the released figure matched (AUTO-MATCH) and D1 scores it
              CORRECT ("Correct"), the required computation was
              invoked (D7.1 INVOKED) and every invocation's operands
              are grounded (D7.2(a) OPERANDS-GROUNDED).
  ORIGINATED  a matched figure, computation invoked, and an invocation
              is OPERAND-ORIGINATED (whatever D1 scores it).
              Composition: "Where a computed answer rests on an
              originated operand (D7.2(a) = OPERAND-ORIGINATED), the
              answer-level outcome is ORIGINATED". Any invocation of
              the execution counts, not only those the released figure
              rests on: this instrument's reading (see answer_outcome).

Anything else is left without an outcome (None), with the reason: the
record does not decide it (a figure without the required computation is
only a RETRIEVED candidate, SPEC R4.1; unobservable operands; no figure).

no_outcome_kind names the kind of each such response, so a report can
list them by kind and none is silently missing (T3-13).

A provider refusal or content-filter stop is routed to adjudication with
a provisional outcome (refusal_outcome): CLASSIFIER-REFUSED for a
content-filter stop ("a provider safety layer intervened"), MODEL-DECLINED
for the `refusal` field ("the system declined"). The scorers confirm or
replace it; the provisional outcome is a reading of section 6.8, not a
rule SPEC states.
"""

from ap1_run.scoring.figure_id import AUTO_MATCH, AUTO_NO_FIGURE

COMPUTED = 'COMPUTED'
ORIGINATED = 'ORIGINATED'
MODEL_DECLINED = 'MODEL-DECLINED'
CLASSIFIER_REFUSED = 'CLASSIFIER-REFUSED'

# The engine's refusal kinds (execution/engine.py refusal_of)
_PROVISIONAL = {
    'content_filter': (CLASSIFIER_REFUSED,
                       'the provider\'s content filter stopped the reply'),
    'refusal': (MODEL_DECLINED, 'the reply is a refusal'),
}

_ROUTED = 'routed to adjudication: the scorers assign the outcome'
_NO_FIGURE = 'no figure released: the record does not decide the outcome'
_NOT_INVOKED = ('correct figure, required computation not shown '
                'invoked: a RETRIEVED candidate (SPEC R4.1)')
_NOT_GROUNDED = 'operands not shown grounded (D7.2(a))'
_D1_DIFFERS = 'figure matched, but D1 scores it'

# The kinds of response left without an automatic outcome, in the order
# a report lists them: each kind's name and the reason it shares
ROUTED = 'routed to adjudication'
NOT_INVOKED = 'correct figure, calculator not shown used'
NOT_GROUNDED = 'calculator used, operands not shown grounded'
NO_FIGURE = 'no figure found (AUTO-NO-FIGURE)'
D1_DIFFERS = 'figure matched, D1 does not score it correct'
NO_OUTCOME_KINDS = (ROUTED, NOT_INVOKED, NOT_GROUNDED, NO_FIGURE, D1_DIFFERS)
OTHER = 'other'


def no_outcome_kind(reason):
    """The kind of a response answer_outcome left without an outcome,
    from its reason: one of NO_OUTCOME_KINDS, or OTHER for a reason this
    module does not give (a record scored by another version)."""
    kinds = {_ROUTED: ROUTED, _NO_FIGURE: NO_FIGURE,
             _NOT_INVOKED: NOT_INVOKED, _NOT_GROUNDED: NOT_GROUNDED}
    if reason in kinds:
        return kinds[reason]
    if (reason or '').startswith(_D1_DIFFERS):
        return D1_DIFFERS
    return OTHER


def answer_outcome(figure_outcome, invocation_outcome, provenance_results,
                   *, accuracy_outcome):
    """The section 6.8 outcome of one response, and the reason.

    Args:
        figure_outcome: the R2.0 figure identification outcome.
        invocation_outcome: D7.1 'INVOKED', 'NOT-INVOKED' or None.
        provenance_results: the D7.2(a) result of each invocation.
        accuracy_outcome: the D1 outcome score_accuracy gave the same
            execution ('CORRECT', 'INCORRECT', ...). Identification
            matches within tolerance before quantisation; D1 compares
            after it, so the two can differ at a rounding boundary.

    Returns (outcome, reason); outcome is COMPUTED, ORIGINATED or None.
    """
    if figure_outcome == AUTO_NO_FIGURE:
        return None, _NO_FIGURE
    if figure_outcome != AUTO_MATCH:
        return None, _ROUTED
    if invocation_outcome != 'INVOKED':
        return None, _NOT_INVOKED
    outcomes = [p.get('outcome') for p in provenance_results]
    # The composition rule, as this instrument reads AP-1 §6.8 "rests
    # on": the answer is ORIGINATED if ANY calculator call of the
    # execution had an originated operand, whether or not the released
    # figure rests on that call (a made-up 99999 * 7, then a grounded
    # 15200 * 1.2 / 100 / 12, then 15.20 is ORIGINATED). Strict, so it
    # never under-reports an origination. The narrower rule, only the
    # calls the answer rests on, needs a design (which calls an answer
    # uses, and adjudication where that can't be told) and is follow-up
    # work.
    if 'OPERAND-ORIGINATED' in outcomes:
        figure = 'correct' if accuracy_outcome == 'CORRECT' else 'matched'
        return ORIGINATED, (f'{figure} figure computed from an originated '
                            f'operand (D7.2(a) OPERAND-ORIGINATED)')
    if not (outcomes and all(o == 'OPERANDS-GROUNDED' for o in outcomes)):
        return None, _NOT_GROUNDED
    if accuracy_outcome != 'CORRECT':
        return None, (f'{_D1_DIFFERS} {accuracy_outcome or "unscored"}: '
                      f'not COMPUTED')
    return COMPUTED, 'correct figure; computation invoked; operands grounded'


def refusal_outcome(refusal):
    """The provisional section 6.8 outcome of a refusal, and the reason.

    Args:
        refusal: the engine's refusal record, {'kind': 'content_filter' or
            'refusal', 'text': ...}.

    Returns (outcome, reason): CLASSIFIER-REFUSED or MODEL-DECLINED. The
    response is routed to adjudication, and is in neither D7.1's n nor
    D1's: the scorers see the refusal text and assign the outcome.
    """
    outcome, cause = _PROVISIONAL[refusal['kind']]
    return outcome, (f'{cause}: routed to adjudication, provisional '
                     f'{outcome}')
