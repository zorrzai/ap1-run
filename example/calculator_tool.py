"""Reference calculator tool implementation.

Ported from the AST variant of harness.py (blob 3cb2a57, commit 10741c9
in scratch/admissibility-protocol). The V1 harness used eval() with
restricted builtins; this version walks the AST directly.

No eval(), no exec(), no compile(), no __builtins__.

Placed in example/ per spec -- keeps the runner engine decoupled from
tool execution functions. Operators may replace this with their own
sandboxed calculator; the interface is string in, string out.

Arithmetic is exact decimal (T3-59): every number is a Decimal read from
the expression's text, never through float, and every operation runs in
the runner's Decimal context (DECIMAL_CONTEXT, precision 50, SPEC
R0.4.1). So 0.1 + 0.2 returns '0.3', not '0.30000000000000004', and a
system that copies a result into its next call copies a value the
scorer's D7.2(a) step 4 matches exactly. Only an operation whose exact
result has more than 50 significant digits (1/3, sqrt(2), log, a power
with a fractional exponent) is rounded, half-even, to 50 digits.
"""

import ast
import decimal
import operator
from decimal import (ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_UP,
                     Decimal, localcontext)

from ap1_run.foundation.numeric import DECIMAL_CONTEXT

# pi to 100 decimal places, as text, rounded to the context's precision
# when used (as D7.2(b)'s evaluator does).
_PI = Decimal('3.14159265358979323846264338327950288419716939937510'
              '58209749445923078164062862089986280348253421170679')


class CalculatorError(Exception):
    """Expression refused by the calculator sandbox."""


# -- Operations (Decimal in, Decimal out) ------------------------------------

def _check_divisor(right):
    if right.is_zero():
        raise CalculatorError('division by zero')


def _div(left, right):
    _check_divisor(right)
    return left / right


def _floordiv(left, right):
    """Python's // (rounds toward minus infinity); Decimal's // truncates."""
    _check_divisor(right)
    quotient, remainder = divmod(left, right)
    if not remainder.is_zero() and (remainder < 0) != (right < 0):
        quotient -= 1
    return quotient


def _mod(left, right):
    """Python's % (the sign of the divisor); Decimal's % takes the
    dividend's."""
    _check_divisor(right)
    remainder = left % right
    if not remainder.is_zero() and (remainder < 0) != (right < 0):
        remainder += right
    return remainder


def _pow(base, exponent, modulus=None):
    if modulus is not None:
        return pow(base, exponent, modulus)
    if base.is_zero():
        if exponent.is_zero():
            return Decimal(1)          # 0 ** 0 is 1, as in Python
        if exponent < 0:
            raise CalculatorError('division by zero')
    if base < 0 and exponent != exponent.to_integral_value():
        raise CalculatorError(
            f'result is not a real number: ({base}) ** {exponent}')
    return base ** exponent


_ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: _div,
    ast.FloorDiv: _floordiv,
    ast.Mod: _mod,
    ast.Pow: _pow,
    ast.BitXor: _pow,  # ^ is math notation for exponentiation
}

_ALLOWED_UNARYOPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _round_half_up(value, ndigits=None):
    """round(), but half away from zero (ROUND_HALF_UP), the rounding
    the example configs declare, not Python's half-to-even: round(2.5)
    is 3, round(2.675, 2) is 2.68. ndigits may be negative:
    round(1234.5, -1) is 1230."""
    places = 0 if ndigits is None else int(ndigits)
    try:
        return value.quantize(Decimal(1).scaleb(-places),
                              rounding=ROUND_HALF_UP)
    except decimal.InvalidOperation as e:
        # The rounded value would need more digits than the context has.
        raise CalculatorError(
            f'cannot round {value} to {places} places') from e


def _positive(name, value):
    if value <= 0:
        raise CalculatorError(f'math domain error: {name}({value})')
    return value


def _log(value, base=None):
    """log(x) is the natural logarithm; log(x, b) the logarithm to base b."""
    ln = _positive('log', value).ln()
    if base is None:
        return ln
    ln_base = _positive('log', base).ln()
    _check_divisor(ln_base)
    return ln / ln_base


def _sqrt(value):
    if value < 0:
        raise CalculatorError(f'math domain error: sqrt({value})')
    return value.sqrt()


_ALLOWED_FUNCS = {
    'abs': abs, 'round': _round_half_up, 'min': min, 'max': max, 'sum': sum,
    'pow': _pow,
    # int() truncates toward zero, as Python's does; float() is the value
    # itself (there is no binary floating point here).
    'int': lambda value: value.to_integral_value(rounding=ROUND_DOWN),
    'float': lambda value: value,
    'sqrt': _sqrt,
    'ceil': lambda value: value.to_integral_value(rounding=ROUND_CEILING),
    'floor': lambda value: value.to_integral_value(rounding=ROUND_FLOOR),
    'log': _log,
    'log10': lambda value: _positive('log10', value).log10(),
}

# Evaluated when used, at the context's precision.
_ALLOWED_NAMES = {'pi': lambda: +_PI, 'e': lambda: Decimal(1).exp()}

MAX_EXPRESSION_LENGTH = 500

# A result is written in plain digits, without an exponent, when it has
# at most this many digits before or after the point; otherwise in
# scientific notation (1E+60), so that 10 ** 999999 does not return a
# million characters.
_PLAIN_DIGITS = 100


# -- AST walker ------------------------------------------------------------

def _literal(node, source):
    """A numeric literal as an exact Decimal: an int by its value, a
    float literal from its text in the expression (0.1 is 0.1, never
    0.1000000000000000055511151231257827)."""
    value = node.value
    if isinstance(value, int):
        return Decimal(int(value))
    text = ast.get_source_segment(source, node)
    try:
        return Decimal(text)
    except (TypeError, decimal.InvalidOperation) as e:
        raise CalculatorError(f'unreadable number: {text!r}') from e


def _eval_node(node, source):
    """Recursively evaluate an AST node to a Decimal (or, for the
    arguments of min, max and sum, a tuple or list of them).

    Only the node types listed below are accepted. Everything else
    -- attribute access, imports, subscripts, comprehensions, calls
    to unlisted functions -- raises CalculatorError.
    """
    if isinstance(node, ast.Expression):
        return _eval_node(node.body, source)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return _literal(node, source)
        raise CalculatorError(
            f'unsupported constant type: {type(node.value).__name__}')

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_BINOPS:
            raise CalculatorError(f'unsupported operator: {op_type.__name__}')
        left = _eval_node(node.left, source)
        right = _eval_node(node.right, source)
        return _ALLOWED_BINOPS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_UNARYOPS:
            raise CalculatorError(
                f'unsupported unary operator: {op_type.__name__}')
        operand = _eval_node(node.operand, source)
        return _ALLOWED_UNARYOPS[op_type](operand)

    if isinstance(node, ast.Name):
        if node.id in _ALLOWED_NAMES:
            return _ALLOWED_NAMES[node.id]()
        raise CalculatorError(f'unsupported name: {node.id!r}')

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise CalculatorError('only named function calls allowed')
        fname = node.func.id
        if fname not in _ALLOWED_FUNCS:
            raise CalculatorError(f'unsupported function: {fname}')
        if node.keywords:
            raise CalculatorError('keyword arguments not permitted')
        args = [_eval_node(a, source) for a in node.args]
        return _ALLOWED_FUNCS[fname](*args)

    # Tuple and List nodes support min([...]), max([...]) etc.
    if isinstance(node, ast.Tuple):
        return tuple(_eval_node(e, source) for e in node.elts)

    if isinstance(node, ast.List):
        return [_eval_node(e, source) for e in node.elts]

    raise CalculatorError(f'unsupported AST node: {type(node).__name__}')


def _format(value):
    """The result as text: plain digits, no trailing zeros after the
    point, no exponent ('0.3', '1024', '288506.25', '1230'); scientific
    notation beyond _PLAIN_DIGITS digits. Zero is '0', never '-0'."""
    if value.is_zero():
        return '0'
    value = value.normalize()
    if -_PLAIN_DIGITS < value.adjusted() < _PLAIN_DIGITS:
        return format(value, 'f')
    return str(value)


# -- Public interface -------------------------------------------------------

def execute_calculator(expression):
    """Evaluate a mathematical expression in a sandboxed AST walker.

    No eval(), no exec(), no imports, no attribute access.
    Only arithmetic operators and the listed safe functions, in exact
    decimal arithmetic (see the module docstring).

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

    # E6: translate ^ to ** for correct mathematical precedence.
    # Python's ^ is XOR (BitXor) with lower precedence than - and +.
    # In math notation, ^ means exponentiation and binds tighter.
    # Translating before ast.parse gives ** (Pow) the correct precedence.
    expression = expression.replace('^', '**')

    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError as e:
        raise CalculatorError(f'syntax error: {e}') from e

    # An arithmetic error (1/0, log(-1), an overflow) is a refusal, like
    # any other expression the calculator cannot evaluate. The context
    # traps overflow and invalid operations; DivisionByZero is checked
    # before dividing, with Python's message.
    with localcontext(DECIMAL_CONTEXT):
        try:
            result = _eval_node(tree, expression)
            if not isinstance(result, Decimal):
                raise CalculatorError(
                    f'result is not a number: {type(result).__name__}')
            return _format(result)
        except decimal.Overflow as e:
            raise CalculatorError('numeric overflow') from e
        except decimal.InvalidOperation as e:
            raise CalculatorError('invalid operation') from e
        except (ArithmeticError, ValueError, TypeError) as e:
            raise CalculatorError(str(e)) from e


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
        'pi * 2': '6.2831853071795864769252867665590057683943387987502',
        'sqrt(144)': '12',
        'ceil(3.2)': '4',
        'floor(3.9)': '3',
        '17 % 5': '2',
        '17 // 3': '5',
        '0.1 + 0.2': '0.3',  # T3-59: exact decimal, not 0.30000000000000004
        '(1+0.078/12)^3-1': None,  # E6: caret precedence
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

    # E6 specific: verify caret precedence is correct
    e6_result = Decimal(execute_calculator('(1+0.078/12)^3-1'))
    e6_expected_approx = Decimal('0.01959')  # approx (1.0065)^3 - 1
    if abs(e6_result - e6_expected_approx) > Decimal('0.001'):
        ok = False
        print(f'  FAIL  E6 caret precedence: got {e6_result}, '
              f'expected ~{e6_expected_approx}')

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
