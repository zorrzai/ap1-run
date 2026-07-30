"""Reference calculator tool implementation.

Ported from the AST variant of harness.py (blob 3cb2a57, commit 10741c9
in scratch/admissibility-protocol). The V1 harness used eval() with
restricted builtins; this version walks the AST directly.

No eval(), no exec(), no compile(), no __builtins__.

Placed in example/ per spec -- keeps the runner engine decoupled from
tool execution functions. Operators may replace this with their own
sandboxed calculator; the interface is string in, string out.
"""

import ast
import math
import operator
from decimal import Decimal, InvalidOperation


# -- Allow-lists (explicit, exhaustive) ------------------------------------

_ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_ALLOWED_UNARYOPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

_ALLOWED_FUNCS = {
    'abs': abs, 'round': round, 'min': min, 'max': max, 'sum': sum,
    'pow': pow, 'int': int, 'float': float,
    'sqrt': math.sqrt, 'ceil': math.ceil, 'floor': math.floor,
    'log': math.log, 'log10': math.log10,
}

_ALLOWED_NAMES = {'pi': math.pi, 'e': math.e}

MAX_EXPRESSION_LENGTH = 500


class CalculatorError(Exception):
    """Expression refused by the calculator sandbox."""


# -- AST walker ------------------------------------------------------------

def _eval_node(node):
    """Recursively evaluate an AST node.

    Only the node types listed below are accepted. Everything else
    -- attribute access, imports, subscripts, comprehensions, calls
    to unlisted functions -- raises CalculatorError.
    """
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise CalculatorError(
            f'unsupported constant type: {type(node.value).__name__}')

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_BINOPS:
            raise CalculatorError(f'unsupported operator: {op_type.__name__}')
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return _ALLOWED_BINOPS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_UNARYOPS:
            raise CalculatorError(
                f'unsupported unary operator: {op_type.__name__}')
        operand = _eval_node(node.operand)
        return _ALLOWED_UNARYOPS[op_type](operand)

    if isinstance(node, ast.Name):
        if node.id in _ALLOWED_NAMES:
            return _ALLOWED_NAMES[node.id]
        raise CalculatorError(f'unsupported name: {node.id!r}')

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise CalculatorError('only named function calls allowed')
        fname = node.func.id
        if fname not in _ALLOWED_FUNCS:
            raise CalculatorError(f'unsupported function: {fname}')
        if node.keywords:
            raise CalculatorError('keyword arguments not permitted')
        args = [_eval_node(a) for a in node.args]
        return _ALLOWED_FUNCS[fname](*args)

    # Tuple and List nodes support min([...]), max([...]) etc.
    if isinstance(node, ast.Tuple):
        return tuple(_eval_node(e) for e in node.elts)

    if isinstance(node, ast.List):
        return [_eval_node(e) for e in node.elts]

    raise CalculatorError(f'unsupported AST node: {type(node).__name__}')


# -- Public interface -------------------------------------------------------

def execute_calculator(expression):
    """Evaluate a mathematical expression in a sandboxed AST walker.

    No eval(), no exec(), no imports, no attribute access.
    Only arithmetic operators and the listed safe functions.

    Returns: str -- the result as a string. The RUNNER converts this
    to Decimal for comparison per R0.4.
    """
    if not isinstance(expression, str):
        raise CalculatorError(
            f'expression must be string, got {type(expression).__name__}')

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

    result = _eval_node(tree)
    return str(result)


# -- Self-test (ported from AST variant _selftest_calculator) ---------------

def selftest():
    """Run the calculator self-test.

    Arithmetic cases must produce the expected result.
    Security cases must ALL be refused.
    """
    cases = {
        '4215.33 * 0.125 / 12': '43.9096875',
        'round(21795.33 + 1650.00, 2)': '23445.33',
        'max(7340, 14380)': '14380',
        '-log(1 - (0.125/12)*1650/100) / log(1 + 0.125/12)': None,
        '2 ** 10': '1024',
        'pi * 2': str(math.pi * 2),
        'sqrt(144)': '12.0',
        'ceil(3.2)': '4',
        'floor(3.9)': '3',
        '17 % 5': '2',
        '17 // 3': '5',
    }

    # Security: these MUST all be refused
    dangers = [
        "__import__('os').system('echo hi')",
        '().__class__',
        "open('x')",
        "eval('1')",
        '__builtins__',
        'lambda: 1',
        '[x for x in range(10)]',
        'type(1).__bases__',
    ]

    ok = True
    for expr, expected in cases.items():
        try:
            got = execute_calculator(expr)
        except CalculatorError as e:
            ok = False
            print(f'  FAIL  {expr!r} -> CalculatorError: {e}')
            continue
        if expected is not None and got != expected:
            ok = False
            print(f'  FAIL  {expr!r} -> {got!r} (expected {expected!r})')

    for danger in dangers:
        try:
            got = execute_calculator(danger)
            ok = False
            print(f'  SECURITY FAIL  {danger!r} -> {got!r} (should refuse)')
        except CalculatorError:
            pass  # expected

    return ok


if __name__ == '__main__':
    if selftest():
        print('  calculator self-test: PASS')
    else:
        print('  calculator self-test: FAIL')
        raise SystemExit(1)
