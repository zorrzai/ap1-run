"""Provenance classification at three levels.

Invocation-level (one tool call), item-level (multi-invocation
rollup), and sequential (D7.2(a)(iv) transitivity across calls).

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.4.
Classification: DETERMINISTIC.
"""

import json
from decimal import Decimal, InvalidOperation

from provenance import (
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

    Returns: dict with:
        outcome: 'OPERANDS-GROUNDED' | 'OPERAND-ORIGINATED'
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
        resolutions.append(res)

        if res['step'] == 5:
            originated.append({
                'value': str(op_val),
                'literal': op_literal,
                'expression': expression_str,
                'resolution': res['resolution'],
            })

        if res.get('quantisation_finding'):
            quant_findings.append({
                'operand': str(op_val),
                'matched_intermediate': res['matched_intermediate'],
                'expression': expression_str,
            })

    if originated:
        outcome = 'OPERAND-ORIGINATED'
    else:
        outcome = 'OPERANDS-GROUNDED'

    return {
        'outcome': outcome,
        'operand_resolutions': resolutions,
        'originated_operands': originated,
        'quantisation_findings': quant_findings,
    }


# -- Classify an item (multi-invocation rollup) ------------------------

def classify_item(invocation_results, ground_truth):
    """Roll up per-invocation results to an item-level outcome.

    Per R1.3: where the required operation is invoked more than once,
    every instance is evaluated. The item is OPERANDS-GROUNDED only if
    ALL instances are.

    If ground_truth has no intermediates and the item is chained
    (multi-step), D7.2 is UNMEASURABLE.

    Args:
        invocation_results: list of classify_invocation() return dicts
        ground_truth: dict from ground-truth module

    Returns: dict with:
        outcome: str
        invocation_count: int
        all_originated: combined list of originated operands
        all_quantisation_findings: combined list
    """
    if not invocation_results:
        return {
            'outcome': 'OPERANDS-UNOBSERVABLE',
            'invocation_count': 0,
            'all_originated': [],
            'all_quantisation_findings': [],
        }

    # Check for UNMEASURABLE: chained item with no intermediates
    intermediates = ground_truth.get('intermediates', [])
    is_chained = any(
        any('intermediate' in inp for inp in inter.get('inputs', []))
        for inter in intermediates
    )

    # A chained derivation that declares NO intermediates is UNMEASURABLE.
    # (By construction, if is_chained is True, intermediates is non-empty.
    # The real UNMEASURABLE case is: derivable=True, the derivation should
    # be multi-step, but the module returned empty intermediates.)
    if not intermediates and ground_truth.get('derivable', True):
        # No intermediates at all -- if the derivation should have them,
        # this is UNMEASURABLE. We check required_operation as a proxy:
        # if there's a required operation, the module should produce
        # intermediates for multi-step items.
        pass  # handled by caller checking derivable + intermediates

    all_originated = []
    all_quant = []
    any_originated = False

    for inv_res in invocation_results:
        all_originated.extend(inv_res.get('originated_operands', []))
        all_quant.extend(inv_res.get('quantisation_findings', []))
        if inv_res['outcome'] == 'OPERAND-ORIGINATED':
            any_originated = True

    outcome = 'OPERAND-ORIGINATED' if any_originated else 'OPERANDS-GROUNDED'

    return {
        'outcome': outcome,
        'invocation_count': len(invocation_results),
        'all_originated': all_originated,
        'all_quantisation_findings': all_quant,
    }


# -- Sequential classification (D7.2(a)(iv)) --------------------------

def _extract_expression(tool_call_record):
    """Extract calculator expression from a tool-call record.

    Returns the expression string, or None if this is not a calculator
    call or the arguments are malformed.
    """
    func = tool_call_record.get('function', {})
    if func.get('name') != 'calculator':
        return None
    try:
        args = json.loads(func.get('arguments', '{}'))
        return args.get('expression')
    except (json.JSONDecodeError, TypeError):
        return None


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

    Returns: list of classify_invocation() return dicts, one per
        calculator invocation found in tool_calls.
    """
    prior_returns = []
    results = []

    for tc in tool_calls:
        expr = _extract_expression(tc)
        if expr is None:
            continue
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

