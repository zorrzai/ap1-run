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
"""

from ap1_run.scoring.figure_id import AUTO_MATCH, AUTO_NO_FIGURE

COMPUTED = 'COMPUTED'
ORIGINATED = 'ORIGINATED'

_ROUTED = 'routed to adjudication: the scorers assign the outcome'


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
        return None, 'no figure released: the record does not decide the outcome'
    if figure_outcome != AUTO_MATCH:
        return None, _ROUTED
    if invocation_outcome != 'INVOKED':
        return None, ('correct figure, required computation not shown '
                      'invoked: a RETRIEVED candidate (SPEC R4.1)')
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
        return None, 'operands not shown grounded (D7.2(a))'
    if accuracy_outcome != 'CORRECT':
        return None, (f'figure matched, but D1 scores it '
                      f'{accuracy_outcome or "unscored"}: not COMPUTED')
    return COMPUTED, 'correct figure; computation invoked; operands grounded'
