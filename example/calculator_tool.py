"""Reference calculator tool implementation.

Extracted from V1 harness.py (L212-230) and adapted.
Placed in example/ per spec -- keeps the runner engine
decoupled from tool execution functions.

This is the reference implementation operators may use
or replace with their own sandboxed calculator.
"""

import ast
import operator
import math


# Allowed operations -- no exec, no eval, no imports
_ALLOWED_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

_ALLOWED_FUNCS = {
    'abs': abs,
    'round': round,
    'min': min,
    'max': max,
    'sqrt': math.sqrt,
}

MAX_EXPRESSION_LENGTH = 500


class CalculatorError(Exception):
    """Expression refused by the calculator sandbox."""


def execute_calculator(expression):
    """Evaluate a mathematical expression in a sandboxed AST walker.

    No exec, no eval, no imports, no attribute access.
    Only arithmetic operators and a small set of safe functions.

    Returns: float result (the tool's output; the RUNNER converts
    this to Decimal for comparison per R0.4).
    """
    if not isinstance(expression, str):
        raise CalculatorError(f'expression must be string, got {type(expression).__name__}')

    expression = expression.strip()
    if not expression:
        raise CalculatorError('empty expression')

    if len(expression) > MAX_EXPRESSION_LENGTH:
        raise CalculatorError(
            f'expression too long: {len(expression)} chars '
            f'(max {MAX_EXPRESSION_LENGTH})')

    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError as e:
        raise CalculatorError(f'syntax error: {e}') from e

    return _eval_node(tree.body)


def _eval_node(node):
    """Recursively evaluate an AST node."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise CalculatorError(f'unsupported constant type: {type(node.value).__name__}')

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPS:
            raise CalculatorError(f'unsupported operator: {op_type.__name__}')
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return _ALLOWED_OPS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPS:
            raise CalculatorError(f'unsupported unary operator: {op_type.__name__}')
        operand = _eval_node(node.operand)
        return _ALLOWED_OPS[op_type](operand)

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise CalculatorError('only named function calls allowed')
        fname = node.func.id
        if fname not in _ALLOWED_FUNCS:
            raise CalculatorError(f'unsupported function: {fname}')
        args = [_eval_node(a) for a in node.args]
        return _ALLOWED_FUNCS[fname](*args)

    raise CalculatorError(f'unsupported AST node: {type(node).__name__}')
