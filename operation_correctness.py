"""D7.2(b) -- Operation Correctness.

AP-1 v1.3, D7.2(b): "Was the formula applied the one the question required?"

Design: Mirrors D7.2(a) at the other end of the computation.
  D7.2(a) resolves the INPUTS  against source values and reference intermediates.
  D7.2(b) resolves the OUTPUT  against the expected value and reference intermediates.

Algorithm, per invocation of the required operation:
  1. Evaluate the model's expression deterministically (Decimal, AST walker).
     Never eval().
  2. Resolve the result:
       equals the reference expected value (within declared tolerance)
         -> OPERATION-CORRECT
       equals a reference intermediate (raw, transformed, or quantised)
         -> OPERATION-CORRECT (intermediate step)
       equals neither
         -> WRONG-OPERATION
       expression unparseable or non-numeric
         -> OPERATION-UNOBSERVABLE (declared, never assumed correct)

Classification: DETERMINISTIC.
Dependencies: numeric.py (quantise), provenance.py (TRANSFORMATIONS).
"""

import ast
import operator
import math
from decimal import Decimal, InvalidOperation

from numeric import quantise
from provenance import TRANSFORMATIONS


# -- Outcome constants ------------------------------------------------

OPERATION_CORRECT = 'OPERATION-CORRECT'
WRONG_OPERATION = 'WRONG-OPERATION'
OPERATION_UNOBSERVABLE = 'OPERATION-UNOBSERVABLE'


# -- Safe AST evaluator (Decimal-only) --------------------------------

_ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.BitXor: operator.pow,  # ^ = exponentiation in math notation
}

_ALLOWED_UNARYOPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

_ALLOWED_NAMES = {
    'pi': Decimal(str(math.pi)),
    'e': Decimal(str(math.e)),
}

_ALLOWED_FUNCS = {
    'abs': abs,
    'round': lambda v, n=0: v.quantize(Decimal(10) ** -int(n)),
}


def _eval_decimal(node):
    """Recursively evaluate an AST node using Decimal arithmetic.

    Only arithmetic operators and a minimal set of safe functions are
    permitted. Everything else raises ValueError.
    """
    if isinstance(node, ast.Expression):
        return _eval_decimal(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return Decimal(str(node.value))
        raise ValueError(
            f'unsupported constant type: {type(node.value).__name__}')

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_BINOPS:
            raise ValueError(f'unsupported operator: {op_type.__name__}')
        left = _eval_decimal(node.left)
        right = _eval_decimal(node.right)
        return _ALLOWED_BINOPS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_UNARYOPS:
            raise ValueError(
                f'unsupported unary operator: {op_type.__name__}')
        operand = _eval_decimal(node.operand)
        return _ALLOWED_UNARYOPS[op_type](operand)

    if isinstance(node, ast.Name):
        if node.id in _ALLOWED_NAMES:
            return _ALLOWED_NAMES[node.id]
        raise ValueError(f'unsupported name: {node.id!r}')

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError('only named function calls allowed')
        fname = node.func.id
        if fname not in _ALLOWED_FUNCS:
            raise ValueError(f'unsupported function: {fname}')
        args = [_eval_decimal(a) for a in node.args]
        return _ALLOWED_FUNCS[fname](*args)

    raise ValueError(f'unsupported AST node: {type(node).__name__}')


def evaluate_expression(expression_str):
    """Evaluate a mathematical expression string to a Decimal.

    Uses the safe AST walker -- no eval(), no exec().

    Returns:
        Decimal result, or None if the expression is unparseable
        or produces a non-numeric result.
    """
    if not isinstance(expression_str, str) or not expression_str.strip():
        return None
    try:
        tree = ast.parse(expression_str.strip(), mode='eval')
        result = _eval_decimal(tree)
        if not isinstance(result, Decimal):
            result = Decimal(str(result))
        return result
    except (SyntaxError, ValueError, InvalidOperation,
            ZeroDivisionError, OverflowError, TypeError):
        return None


# -- Resolution --------------------------------------------------------

def classify_operation(expression_str, ground_truth, config):
    """Classify operation correctness for one tool call expression.

    Args:
        expression_str: the calculator expression string
        ground_truth: dict from ground-truth module (must have
            'final', 'intermediates')
        config: runner config dict (needs 'answer_tolerance',
            'permitted_transformations', 'quantisation')

    Returns: dict with:
        outcome: OPERATION-CORRECT | WRONG-OPERATION | OPERATION-UNOBSERVABLE
        evaluated_result: str or None (the Decimal result as string)
        matched_against: str or None (what it matched: 'expected_value',
            'intermediate:<label>', or None)
        detail: str (human-readable explanation)
    """
    result = evaluate_expression(expression_str)

    if result is None:
        return {
            'outcome': OPERATION_UNOBSERVABLE,
            'evaluated_result': None,
            'matched_against': None,
            'detail': f'expression unparseable or non-numeric: '
                      f'{expression_str!r}',
        }

    expected = ground_truth.get('final')
    if expected is not None and not isinstance(expected, Decimal):
        try:
            expected = Decimal(str(expected))
        except (InvalidOperation, ValueError):
            expected = None

    tolerance = _get_tolerance(config)
    intermediates = ground_truth.get('intermediates', [])
    permitted_transforms = config.get('permitted_transformations', [])
    quant_config = config.get('quantisation', {})

    # Check 1: does result equal the expected value (within tolerance)?
    if expected is not None and _within_tolerance(result, expected, tolerance):
        return {
            'outcome': OPERATION_CORRECT,
            'evaluated_result': str(result),
            'matched_against': 'expected_value',
            'detail': f'result {result} matches expected value '
                      f'{expected} (tolerance {tolerance})',
        }

    # Check 2: does result equal a reference intermediate?
    for inter in intermediates:
        inter_val = inter.get('value')
        if inter_val is None:
            continue
        if not isinstance(inter_val, Decimal):
            try:
                inter_val = Decimal(str(inter_val))
            except (InvalidOperation, ValueError):
                continue

        label = inter.get('label', '?')

        # 2a: raw intermediate
        if _within_tolerance(result, inter_val, tolerance):
            return {
                'outcome': OPERATION_CORRECT,
                'evaluated_result': str(result),
                'matched_against': f'intermediate:{label}',
                'detail': f'result {result} matches intermediate '
                          f'{label}={inter_val}',
            }

        # 2b: intermediate under permitted transformation
        for tname in permitted_transforms:
            tfunc = TRANSFORMATIONS.get(tname)
            if tfunc is None:
                continue
            transformed = tfunc(inter_val)
            if _within_tolerance(result, transformed, tolerance):
                return {
                    'outcome': OPERATION_CORRECT,
                    'evaluated_result': str(result),
                    'matched_against': f'intermediate:{label}({tname})',
                    'detail': f'result {result} matches {tname}('
                              f'{label})={transformed}',
                }

        # 2c: quantised intermediate
        if quant_config:
            places = int(quant_config.get('places', 2))
            rounding = quant_config.get('rounding', 'ROUND_HALF_UP')
            quantised_val = quantise(inter_val, places, rounding)
            if _within_tolerance(result, quantised_val, tolerance):
                return {
                    'outcome': OPERATION_CORRECT,
                    'evaluated_result': str(result),
                    'matched_against': f'intermediate:{label}(quantised)',
                    'detail': f'result {result} matches quantised '
                              f'{label}={quantised_val}',
                }

    # Check 3: also check expected value under quantisation
    if expected is not None and quant_config:
        places = int(quant_config.get('places', 2))
        rounding = quant_config.get('rounding', 'ROUND_HALF_UP')
        quantised_expected = quantise(expected, places, rounding)
        if _within_tolerance(result, quantised_expected, tolerance):
            return {
                'outcome': OPERATION_CORRECT,
                'evaluated_result': str(result),
                'matched_against': 'expected_value(quantised)',
                'detail': f'result {result} matches quantised expected '
                          f'{quantised_expected}',
            }

    # No match -- wrong operation
    return {
        'outcome': WRONG_OPERATION,
        'evaluated_result': str(result),
        'matched_against': None,
        'detail': f'result {result} matches neither expected value '
                  f'{expected} nor any intermediate',
    }


def _get_tolerance(config):
    """Extract answer tolerance from config as Decimal."""
    tol = config.get('answer_tolerance')
    if tol is None:
        return Decimal('0')
    if isinstance(tol, Decimal):
        return tol
    try:
        return Decimal(str(tol))
    except (InvalidOperation, ValueError):
        return Decimal('0')


def _within_tolerance(a, b, tolerance):
    """Check if two Decimals are within tolerance of each other."""
    return abs(a - b) <= tolerance
