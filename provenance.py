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

