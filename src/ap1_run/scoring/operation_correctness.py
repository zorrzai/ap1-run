"""D7.2(b) -- Operation Correctness.

AP-1 v1.3, D7.2(b): "Was the formula applied the one the question required?"
Per invocation: evaluate the model's expression (Decimal, AST walker, never
eval), resolve against expected value and reference intermediates.
Outcomes: OPERATION-CORRECT, WRONG-OPERATION, OPERATION-UNOBSERVABLE.
"""

import ast
import decimal
import operator
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

from ap1_run.foundation.numeric import quantise
from ap1_run.scoring.provenance.trace import (
    TRANSFORMATIONS, is_number, literal_decimal, parse_expression,
)

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

# pi to 100 decimal places, as text: never through float (R0.4).
_PI = Decimal('3.14159265358979323846264338327950288419716939937510'
              '58209749445923078164062862089986280348253421170679')


def _pi():
    """pi rounded to the current Decimal precision (exact for any
    precision up to 100 digits; the runner uses 28 or 50)."""
    return +_PI


def _e():
    """e to the current Decimal precision."""
    return Decimal(1).exp()


# Evaluated when the expression is, at the context's precision (R0.4).
_ALLOWED_NAMES = {
    'pi': _pi,
    'e': _e,
}

_ALLOWED_FUNCS = {
    'abs': abs,
    # Half away from zero, as the reference calculator rounds and as the
    # example configs declare (ROUND_HALF_UP); round(2.5) is 3.
    'round': lambda v, n=0: v.quantize(Decimal(10) ** -int(n),
                                       rounding=ROUND_HALF_UP),
}

def _eval_decimal(node, source):
    """Recursively evaluate an AST node using Decimal arithmetic.

    Only arithmetic operators and a minimal set of safe functions are
    permitted. Everything else raises ValueError. Literals are read from
    their text in `source`, never through float (T3-58, F5).
    """
    if isinstance(node, ast.Expression):
        return _eval_decimal(node.body, source)

    if isinstance(node, ast.Constant):
        if is_number(node.value):
            return literal_decimal(node, source)[0]
        raise ValueError(
            f'unsupported constant type: {type(node.value).__name__}')

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_BINOPS:
            raise ValueError(f'unsupported operator: {op_type.__name__}')
        left = _eval_decimal(node.left, source)
        right = _eval_decimal(node.right, source)
        return _ALLOWED_BINOPS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_UNARYOPS:
            raise ValueError(
                f'unsupported unary operator: {op_type.__name__}')
        operand = _eval_decimal(node.operand, source)
        return _ALLOWED_UNARYOPS[op_type](operand)

    if isinstance(node, ast.Name):
        if node.id in _ALLOWED_NAMES:
            return _ALLOWED_NAMES[node.id]()
        raise ValueError(f'unsupported name: {node.id!r}')

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError('only named function calls allowed')
        fname = node.func.id
        if fname not in _ALLOWED_FUNCS:
            raise ValueError(f'unsupported function: {fname}')
        args = [_eval_decimal(a, source) for a in node.args]
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
        # E6: translate ^ to ** for correct mathematical precedence
        expr_clean = expression_str.strip().replace('^', '**')
        tree = ast.parse(expr_clean, mode='eval')
        result = _eval_decimal(tree, expr_clean)
        if not isinstance(result, Decimal):
            result = Decimal(str(result))
        return result
    except (SyntaxError, ValueError, InvalidOperation,
            ZeroDivisionError, OverflowError, TypeError):
        return None

# -- Resolution --------------------------------------------------------

def classify_operation(expression_str, ground_truth, config):
    """Classify operation correctness for one tool call expression."""
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

# -- Session-level reclassification (forward-dependency rule) ----------

def reclassify_session(results, expressions):
    """Reclassify WO calls whose result feeds a later resolved call."""
    if not results or not expressions:
        return list(results)
    n = len(results)
    out = list(results)
    # Operand literals of each expression, read exactly as D7.2(a) reads
    # them (T3-58); an unreadable expression has none.
    op_sets = []
    for expr in expressions:
        lits = set()
        parsed = parse_expression(expr)
        if parsed is not None:
            tree, source = parsed
            for nd in ast.walk(tree):
                if isinstance(nd, ast.Constant):
                    lits.add(literal_decimal(nd, source)[0])
        op_sets.append(lits)
    # Evaluated results per call
    evals = []
    for r in results:
        er = r.get('evaluated_result')
        try:
            evals.append(Decimal(str(er)) if er is not None else None)
        except (InvalidOperation, ValueError):
            evals.append(None)
    resolved = [r.get('outcome') == OPERATION_CORRECT for r in results]
    # Backward walk until stable
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if resolved[i] or out[i].get('outcome') != WRONG_OPERATION:
                continue
            if evals[i] is None:
                continue
            for j in range(i + 1, n):
                if resolved[j] and evals[i] in op_sets[j]:
                    out[i] = dict(out[i])
                    out[i]['outcome'] = OPERATION_CORRECT
                    out[i]['matched_against'] = f'operand_of_call_{j}'
                    out[i]['detail'] = (
                        f'result {evals[i]} is an operand of call {j} '
                        f'which resolved as OPERATION-CORRECT')
                    resolved[i] = True
                    changed = True
                    break

    return out

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
