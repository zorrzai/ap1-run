"""Provenance classification at three levels.

Invocation-level (one tool call), item-level (multi-invocation
rollup), and sequential (D7.2(a)(iv) transitivity across calls).

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.4.
Classification: DETERMINISTIC.
"""

import json
from decimal import Decimal, InvalidOperation

from ap1_run.scoring.provenance.trace import (
    extract_operands, resolve_operand, _collect_constants,
)


# -- Classify one invocation (one tool call) ---------------------------

def classify_invocation(expression_str, delivered_context, ground_truth,
                        config, prior_returns=None):
    """Classify operand provenance for one tool call expression.

    Args:
        expression_str: the calculator expression
        delivered_context: dict of {acct_id: {field: str_value}}
        ground_truth: dict from ground-truth module (must have
            'intermediates' list with typed inputs)
        config: runner config dict

    An expression with no operand that can be read (unparseable, not a
    string, a boolean or string constant, or only named constants) is
    OPERANDS-UNOBSERVABLE, never vacuously grounded (T3-2; AP-1 v1.3
    D7.2(a): the unobservable case is declared, never silently skipped).

    Returns: dict with:
        outcome: 'OPERANDS-GROUNDED' | 'OPERAND-ORIGINATED' |
            'OPERANDS-UNOBSERVABLE'
        operand_resolutions: list of per-operand resolution dicts
        originated_operands: list of originated operand audit entries
        quantisation_findings: list of quantisation findings
    """
    operands = extract_operands(expression_str)

    intermediates = ground_truth.get('intermediates', [])
    permitted_transforms = config.get('permitted_transformations', [])
    quant_config = config.get('quantisation', {})

    # Collect known constants from ground-truth typed inputs
    constants = _collect_constants(ground_truth)

    resolutions = []
    originated = []
    quant_findings = []

    for op_val, op_literal in operands:
        res = resolve_operand(
            op_val, delivered_context, intermediates,
            constants, permitted_transforms, quant_config,
            prior_returns=prior_returns)
        res['operand_value'] = str(op_val)
        res['operand_literal'] = op_literal
        res['expression'] = expression_str
        resolutions.append(res)

        if res['step'] == 5:
            originated.append({
                'value': str(op_val),
                'literal': op_literal,
                'expression': expression_str,
                'resolution': res['resolution'],
                'sign_inversion_finding': res.get('sign_inversion_finding'),
            })

        if res.get('quantisation_finding'):
            quant_findings.append({
                'operand': str(op_val),
                'matched_intermediate': res['matched_intermediate'],
                'expression': expression_str,
            })

    if not operands:
        outcome = 'OPERANDS-UNOBSERVABLE'
    elif originated:
        outcome = 'OPERAND-ORIGINATED'
    else:
        outcome = 'OPERANDS-GROUNDED'

    result = {
        'outcome': outcome,
        'operand_resolutions': resolutions,
        'originated_operands': originated,
        'quantisation_findings': quant_findings,
    }
    if not operands:
        result['reason'] = (f'no operand could be read from the expression '
                            f'{expression_str!r}')
    return result


# -- Classify an item (multi-invocation rollup) ------------------------

UNMEASURABLE_REASON = ('chained item whose ground truth declares no '
                       'intermediates (SPEC R2.4)')

# Resolutions that mean an operand matched an earlier call's return.
_SESSION_RESOLUTIONS = ('computed_in_session', 'computed_in_session_ungrounded')


def _session_is_chained(invocation_results):
    """True if a call consumed an earlier call's return: one of its
    operands matched a prior return, exactly or after quantisation (a
    near miss)."""
    return any(res.get('resolution') in _SESSION_RESOLUTIONS
               or res.get('near_miss_finding')
               for inv in invocation_results
               for res in inv.get('operand_resolutions', []))


def classify_item(invocation_results, ground_truth):
    """Roll up per-invocation results to an item-level outcome.

    Per R1.3: where the required operation is invoked more than once,
    every instance is evaluated. The item is OPERANDS-GROUNDED only if
    ALL instances are.

    The outcome, in this order:
      - no invocations: OPERANDS-UNOBSERVABLE;
      - a chained item whose ground truth declares no intermediates:
        UNMEASURABLE, never grounded by default (SPEC R2.4 Failure Modes;
        T3-42). The ground-truth schema has no "chained" flag; an item is
        chained when a call consumed an earlier call's return. (The
        ground truth's own chain, an intermediate whose inputs name
        another, can't show when no intermediates are declared.)
      - any invocation originated: OPERAND-ORIGINATED;
      - any invocation unobservable: OPERANDS-UNOBSERVABLE (fail closed);
      - otherwise OPERANDS-GROUNDED.

    Args:
        invocation_results: list of classify_invocation() return dicts
        ground_truth: dict from ground-truth module

    Returns: dict with:
        outcome: str
        invocation_count: int
        all_originated: combined list of originated operands
        all_quantisation_findings: combined list
        reason: str (UNMEASURABLE only)
    """
    if not invocation_results:
        return {
            'outcome': 'OPERANDS-UNOBSERVABLE',
            'invocation_count': 0,
            'all_originated': [],
            'all_quantisation_findings': [],
        }

    all_originated = []
    all_quant = []
    for inv_res in invocation_results:
        all_originated.extend(inv_res.get('originated_operands', []))
        all_quant.extend(inv_res.get('quantisation_findings', []))
    outcomes = [inv_res.get('outcome') for inv_res in invocation_results]

    result = {
        'invocation_count': len(invocation_results),
        'all_originated': all_originated,
        'all_quantisation_findings': all_quant,
    }
    if not ground_truth.get('intermediates') and \
            _session_is_chained(invocation_results):
        result['outcome'] = 'UNMEASURABLE'
        result['reason'] = UNMEASURABLE_REASON
    elif 'OPERAND-ORIGINATED' in outcomes:
        result['outcome'] = 'OPERAND-ORIGINATED'
    elif 'OPERANDS-UNOBSERVABLE' in outcomes:
        result['outcome'] = 'OPERANDS-UNOBSERVABLE'
    else:
        result['outcome'] = 'OPERANDS-GROUNDED'
    return result


def mark_unmeasurable_item(invocation_results, ground_truth):
    """The invocation results, with the item's D7.2 measurability applied.

    Where classify_item finds the item UNMEASURABLE, each grounded or
    originated invocation is marked UNMEASURABLE with the reason (its
    operand resolutions are kept for the audit); an unobservable one stays
    unobservable. Otherwise the results are returned unchanged.
    """
    item = classify_item(invocation_results, ground_truth)
    if item['outcome'] != 'UNMEASURABLE':
        return invocation_results
    return [r if r.get('outcome') == 'OPERANDS-UNOBSERVABLE'
            else dict(r, outcome='UNMEASURABLE', reason=item['reason'])
            for r in invocation_results]


# -- Sequential classification (D7.2(a)(iv)) --------------------------

def is_calculator_call(tool_call_record):
    """True if the tool-call record is a call to the calculator."""
    return tool_call_record.get('function', {}).get('name') == 'calculator'


def _extract_expression(tool_call_record):
    """Extract calculator expression from a tool-call record.

    Returns the 'expression' argument, or None if this is not a calculator
    call or the arguments are malformed (not JSON, not a JSON object, or
    without an 'expression' key).
    """
    if not is_calculator_call(tool_call_record):
        return None
    try:
        args = json.loads(tool_call_record['function'].get('arguments', '{}'))
    except (json.JSONDecodeError, TypeError):
        return None
    if not isinstance(args, dict):
        return None
    return args.get('expression')


def _parse_return_value(return_value_str):
    """Parse a tool return-value JSON string to extract numeric result.

    Returns Decimal or None.
    """
    if return_value_str is None:
        return None
    try:
        parsed = json.loads(return_value_str)
        if isinstance(parsed, dict) and 'result' in parsed:
            return Decimal(str(parsed['result']))
    except (json.JSONDecodeError, TypeError, InvalidOperation, ValueError):
        pass
    return None


def classify_invocations_sequential(tool_calls, delivered_context,
                                    ground_truth, config):
    """Classify invocations sequentially, accumulating prior return values.

    Implements D7.2(a)(iv): an operand matching a prior invocation's
    return value is grounded only if that prior invocation was itself
    grounded. If the prior invocation was originated or unobservable,
    the dependent operand is ORIGINATED.

    Args:
        tool_calls: list of tool-call records from the engine. Each
            must have 'id', 'function', and 'return_value' keys.
        delivered_context: dict of {acct_id: {field: str_value}}.
        ground_truth: dict from ground-truth module.
        config: runner config dict.

    Every calculator call gets a result, in order. One whose arguments
    carry no readable expression (malformed or wrongly keyed) is
    OPERANDS-UNOBSERVABLE, declared and counted, never skipped, and the
    calls after it are still classified (T3-16; AP-1 v1.3 D7.2(a)).

    Returns: list of classify_invocation() return dicts, one per
        calculator invocation found in tool_calls.
    """
    prior_returns = []
    results = []

    for tc in tool_calls:
        if not is_calculator_call(tc):
            continue
        expr = _extract_expression(tc)
        result = classify_invocation(
            expr, delivered_context, ground_truth, config,
            prior_returns=prior_returns)
        results.append(result)

        # Record this invocation's return value and grounding status
        return_val = _parse_return_value(tc.get('return_value'))
        if return_val is not None:
            is_grounded = (result['outcome'] == 'OPERANDS-GROUNDED')
            prior_returns.append({
                'value': return_val,
                'grounded': is_grounded,
            })

    return results

