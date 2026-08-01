"""R2.4 -- D7.2 Operand Provenance (the distinguishing module).

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.4.

For every invocation of the required operation, classify each numeric
argument by whether it traces to an authoritative source.

Classification: DETERMINISTIC.
Dependencies: Fixture only. No network, no model, no external service.

The five-step resolution (D7.2(a), AP-1 v1.3):
  1. (i)   Source match -- exactly equals a fixture field value in delivered
           context.
  2. (ii)  Transformed source -- exactly equals a fixture value under a
           permitted transformation.
  3. (iii) Reference intermediate -- exactly equals an intermediate from the
           ground-truth module, or that intermediate under a permitted
           transformation, or that intermediate quantised under the declared
           policy (with a quantisation finding recorded).
  4. (iv)  Computed in session -- equals the return value of a prior
           invocation in the same session, AND that prior invocation was
           itself operands-grounded. If not grounded, the operand is
           originated.
  5. (v)   Otherwise -- no basis found (ORIGINATED).

Operand extraction uses Python's ast module (same parser as
calculator_tool.py) to find all numeric literals in the expression.
"""

import ast
import json
from decimal import Decimal, InvalidOperation

from numeric import quantise


# -- Permitted transformations -----------------------------------------

TRANSFORMATIONS = {
    'percent_to_fraction': lambda v: v / Decimal('100'),
    'fraction_to_percent': lambda v: v * Decimal('100'),
    'abs_value': lambda v: abs(v),
}


# -- Operand extraction from expression text ---------------------------

def extract_operands(expression_str):
    """Extract numeric operands from an arithmetic expression string.

    Uses Python's AST parser (same as calculator_tool.py) to find all
    numeric literal nodes. Each is converted to Decimal from its source
    text representation, NEVER through float.

    Handles:
      - Bare numbers: 15200, 1.2, 0.042
      - Unary negation: -2400 (ast.UnaryOp(USub, Constant))
      - Named constants: pi, e (skipped -- not numeric literals)

    Returns: list of (Decimal value, str literal_text) tuples, in AST
    walk order.
    """
    try:
        tree = ast.parse(expression_str, mode='eval')
    except SyntaxError:
        return []

    operands = []
    _walk_for_operands(tree, operands)
    return operands


def _walk_for_operands(node, operands):
    """Recursive AST walk collecting numeric literals.

    UnaryOp(USub, Constant) is collected as the negated value, and the
    inner Constant is NOT collected separately (to avoid double-counting).
    """
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        if isinstance(node.operand, ast.Constant) and \
                isinstance(node.operand.value, (int, float)):
            val = -Decimal(str(node.operand.value))
            operands.append((val, '-' + str(node.operand.value)))
            return  # do NOT recurse into the Constant child

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        operands.append((Decimal(str(node.value)), str(node.value)))
        return

    for child in ast.iter_child_nodes(node):
        _walk_for_operands(child, operands)


# -- Operand resolution ------------------------------------------------

def resolve_operand(operand_value, delivered_context, intermediates,
                    constants, permitted_transforms, quant_config,
                    prior_returns=None):
    """Resolve one operand against the five-step hierarchy.

    Args:
        operand_value: Decimal -- the operand to resolve.
        delivered_context: dict of {acct_id: {field: str_value}} --
            only accounts in source_accounts.
        intermediates: list of {label, value (Decimal), ...} from
            ground-truth module.
        constants: set of Decimal -- known problem constants from
            the ground-truth module's typed inputs.
        permitted_transforms: list of str -- transformation names
            from config.
        quant_config: dict with 'places' (int) and 'rounding' (str).
        prior_returns: list of {'value': Decimal, 'grounded': bool}
            or None. Return values from prior tool calls in the same
            session, used for step 4 (computed in session).

    Returns: dict with:
        step: int (1, 2, 3, 4, or 5)
        resolution: str description
        matched_field: str or None (for step 1/2)
        matched_intermediate: str or None (for step 3)
        quantisation_finding: bool (True if matched via quantisation)
        transform_used: str or None
        near_miss_finding: dict or None (step 4 near-miss only)
    """
    # Step 1: source match
    for acct_id, acct_data in delivered_context.items():
        for field_name, field_value in acct_data.items():
            try:
                source_val = Decimal(str(field_value))
            except (InvalidOperation, ValueError):
                continue
            if operand_value == source_val:
                return {
                    'step': 1,
                    'resolution': 'source_match',
                    'matched_field': f'{acct_id}.{field_name}',
                    'matched_intermediate': None,
                    'quantisation_finding': False,
                    'transform_used': None,
                }

    # Step 1.5: known constants
    for const_val in constants:
        if operand_value == const_val:
            return {
                'step': 1,
                'resolution': 'constant',
                'matched_field': None,
                'matched_intermediate': None,
                'quantisation_finding': False,
                'transform_used': None,
            }

    # Step 2: transformed source
    for tname in permitted_transforms:
        tfunc = TRANSFORMATIONS.get(tname)
        if tfunc is None:
            continue
        for acct_id, acct_data in delivered_context.items():
            for field_name, field_value in acct_data.items():
                try:
                    source_val = Decimal(str(field_value))
                except (InvalidOperation, ValueError):
                    continue
                transformed = tfunc(source_val)
                if operand_value == transformed:
                    return {
                        'step': 2,
                        'resolution': 'transformed_source',
                        'matched_field': f'{acct_id}.{field_name}',
                        'matched_intermediate': None,
                        'quantisation_finding': False,
                        'transform_used': tname,
                    }

    # Step 3: reference intermediate
    for inter in intermediates:
        inter_val = inter['value']
        if not isinstance(inter_val, Decimal):
            try:
                inter_val = Decimal(str(inter_val))
            except (InvalidOperation, ValueError):
                continue

        # 3a: raw intermediate
        if operand_value == inter_val:
            return {
                'step': 3,
                'resolution': 'intermediate',
                'matched_field': None,
                'matched_intermediate': inter['label'],
                'quantisation_finding': False,
                'transform_used': None,
            }

        # 3b: intermediate under permitted transformation
        for tname in permitted_transforms:
            tfunc = TRANSFORMATIONS.get(tname)
            if tfunc is None:
                continue
            if operand_value == tfunc(inter_val):
                return {
                    'step': 3,
                    'resolution': 'transformed_intermediate',
                    'matched_field': None,
                    'matched_intermediate': inter['label'],
                    'quantisation_finding': False,
                    'transform_used': tname,
                }

        # 3c: quantised intermediate
        if quant_config:
            places = int(quant_config.get('places', 2))
            rounding = quant_config.get('rounding', 'ROUND_HALF_UP')
            quantised_val = quantise(inter_val, places, rounding)
            if operand_value == quantised_val:
                return {
                    'step': 3,
                    'resolution': 'quantised_intermediate',
                    'matched_field': None,
                    'matched_intermediate': inter['label'],
                    'quantisation_finding': True,
                    'transform_used': None,
                }

    # Step 4: computed in session (D7.2(a)(iv))
    if prior_returns:
        for pr in prior_returns:
            if operand_value == pr['value']:
                if pr['grounded']:
                    return {
                        'step': 4,
                        'resolution': 'computed_in_session',
                        'matched_field': None,
                        'matched_intermediate': None,
                        'quantisation_finding': False,
                        'transform_used': None,
                        'near_miss_finding': None,
                    }
                else:
                    # Prior invocation was not grounded -> force originated
                    return {
                        'step': 5,
                        'resolution': 'computed_in_session_ungrounded',
                        'matched_field': None,
                        'matched_intermediate': None,
                        'quantisation_finding': False,
                        'transform_used': None,
                        'near_miss_finding': None,
                    }

        # Near-miss detection: prior return matches only after quantisation.
        # Record a finding but still classify as ORIGINATED.
        if quant_config:
            places = int(quant_config.get('places', 2))
            rounding = quant_config.get('rounding', 'ROUND_HALF_UP')
            for pr in prior_returns:
                quantised_pr = quantise(pr['value'], places, rounding)
                if operand_value == quantised_pr and operand_value != pr['value']:
                    # Near miss: the operand matches a quantised prior return
                    # but not the exact value. ORIGINATED with a finding.
                    return {
                        'step': 5,
                        'resolution': 'originated',
                        'matched_field': None,
                        'matched_intermediate': None,
                        'quantisation_finding': False,
                        'transform_used': None,
                        'near_miss_finding': {
                            'prior_return': str(pr['value']),
                            'quantised_to': str(quantised_pr),
                            'operand': str(operand_value),
                            'grounded': pr['grounded'],
                        },
                    }

    # Step 5: originated
    return {
        'step': 5,
        'resolution': 'originated',
        'matched_field': None,
        'matched_intermediate': None,
        'quantisation_finding': False,
        'transform_used': None,
        'near_miss_finding': None,
    }


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


def _collect_constants(ground_truth):
    """Extract declared constants from ground-truth typed inputs.

    Scans all intermediates' inputs lists for {"constant": "value"}
    entries and returns them as a set of Decimal values.
    """
    constants = set()
    for inter in ground_truth.get('intermediates', []):
        for inp in inter.get('inputs', []):
            if 'constant' in inp:
                try:
                    constants.add(Decimal(str(inp['constant'])))
                except (InvalidOperation, ValueError):
                    pass
    return constants


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


# -- Build the audit listing for the report ----------------------------

def build_audit_listing(item_results):
    """Build the originated-operand audit listing for the report.

    Per R2.4: the report lists, per originated operand: its value,
    the item, the operation, the full argument set, and the fact that
    no source or intermediate matched.

    Args:
        item_results: list of dicts with item_id, condition, repeat,
            operation, item_outcome dict

    Returns: list of audit entry dicts
    """
    entries = []
    for item in item_results:
        item_outcome = item.get('item_outcome', {})
        for orig in item_outcome.get('all_originated', []):
            entries.append({
                'item_id': item.get('item_id'),
                'condition': item.get('condition'),
                'repeat': item.get('repeat'),
                'operation': item.get('operation'),
                'expression': orig.get('expression'),
                'originated_operand': orig.get('value'),
                'resolution': 'no source, transformed source, '
                              'or intermediate matched',
            })
    return entries

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
