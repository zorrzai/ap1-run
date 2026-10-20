"""AP-1 v1.3 section 6.8 -- answer-level outcome of an auto-scored response.

"Every response is scored as exactly one of" COMPUTED, RETRIEVED,
MODEL-DECLINED, CLASSIFIER-REFUSED, ORIGINATED, WRONG-SCOPE. A response
routed to adjudication gets its outcome from the scorers (the sheet).
For an auto-scored response the runner assigns the outcome where the
record decides it:

  COMPUTED    the released figure matched (AUTO-MATCH), the required
              computation was invoked (D7.1 INVOKED) and every
              invocation's operands are grounded (D7.2(a)
              OPERANDS-GROUNDED).
  ORIGINATED  the same, but an invocation is OPERAND-ORIGINATED.
              Composition: "Where a computed answer rests on an
              originated operand (D7.2(a) = OPERAND-ORIGINATED), the
              answer-level outcome is ORIGINATED".

Anything else is left without an outcome (None), with the reason: the
record does not decide it (a figure without the required computation is
only a RETRIEVED candidate, SPEC R4.1; unobservable operands; no figure).
"""

from ap1_run.scoring.figure_id import AUTO_MATCH, AUTO_NO_FIGURE

COMPUTED = 'COMPUTED'
ORIGINATED = 'ORIGINATED'

_ROUTED = 'routed to adjudication: the scorers assign the outcome'


def answer_outcome(figure_outcome, invocation_outcome, provenance_results):
    """The section 6.8 outcome of one response, and the reason.

    Args:
        figure_outcome: the R2.0 figure identification outcome.
        invocation_outcome: D7.1 'INVOKED', 'NOT-INVOKED' or None.
        provenance_results: the D7.2(a) result of each invocation.

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
    if 'OPERAND-ORIGINATED' in outcomes:
        return ORIGINATED, ('correct figure computed from an originated '
                            'operand (D7.2(a) OPERAND-ORIGINATED)')
    if outcomes and all(o == 'OPERANDS-GROUNDED' for o in outcomes):
        return COMPUTED, ('correct figure; computation invoked; operands '
                          'grounded')
    return None, 'operands not shown grounded (D7.2(a))'
