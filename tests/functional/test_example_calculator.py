"""The shipped example calculator as the engine runs it (from legacy
verify_integration.py test_caret_exponentiation_bitxor_to_pow).

PF-3: some models write ^ for exponentiation; Python parses it as BitXor,
and calculator_tool.py maps BitXor to pow. The engine dispatches tool calls
to it by name.
"""

import json

import pytest

from ap1_run.execution.engine import _execute_tool


@pytest.mark.parametrize('expression, result', [
    ('2^10', '1024'),
    ('100^0.5', '10.0'),
    ('287500*(1+0.042/12)', '288506.25'),
])
def test_calculator_maps_caret_to_power(example_modules, expression, result):
    calculator_tool, _ = example_modules
    assert calculator_tool.execute_calculator(expression) == result


def test_engine_dispatches_caret_expression_to_example_calculator(
        example_modules):
    assert _execute_tool('calculator',
                         json.dumps({'expression': '2^10'})) == \
        '{"result": "1024"}'


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-77')
@pytest.mark.parametrize('expression', ['1/0', '1 % 0', 'log(-1)',
                                        'sqrt(-1)', '(-8) ** 0.5'])
def test_calculator_arithmetic_error_refused_with_calculator_error(
        example_modules, expression):
    # The calculator's contract (its docstring and CalculatorError): an
    # expression it cannot evaluate to a real number is refused with
    # CalculatorError. Today 1/0 and 1 % 0 raise ZeroDivisionError,
    # log(-1) and sqrt(-1) ValueError, and (-8) ** 0.5 returns a complex
    # number as a string (KNOWN_ISSUES #1; SPEC R0.4).
    calculator_tool, _ = example_modules
    try:
        got = calculator_tool.execute_calculator(expression)
    except calculator_tool.CalculatorError:
        return
    except Exception as e:
        got = f'{type(e).__name__}: {e}'
    assert False, f'{expression!r} gave {got!r}, not CalculatorError'


@pytest.mark.finding('T3-77')
def test_calculator_round_half_is_half_up(example_modules):
    # KNOWN_ISSUES #6: every example config declares ROUND_HALF_UP (AP-1
    # v1.3 §6.9, declared rounding policy); the example calculator rounds
    # 2.5 to 2.
    calculator_tool, _ = example_modules
    assert calculator_tool.execute_calculator('round(2.5)') == '3'


@pytest.mark.finding('T3-77')
@pytest.mark.parametrize('expression, result', [
    ('round(-2.5)', '-3'), ('round(3.5)', '4'), ('round(2.675, 2)', '2.68'),
    ('round(2.4)', '2'), ('round(7)', '7'), ('round(1234.5, -1)', '1230.0'),
    ('round(21795.33 + 1650.00, 2)', '23445.33')])
def test_calculator_round_half_up_cases(example_modules, expression, result):
    # Half away from zero on the value's decimal text; an int without
    # ndigits and a float with it, as round() gives.
    calculator_tool, _ = example_modules
    assert calculator_tool.execute_calculator(expression) == result


@pytest.mark.finding('T3-77')
@pytest.mark.parametrize('expression, message', [
    ('1/0', 'division by zero'),
    ('(-8) ** 0.5', 'result is not a real number: '
                    '(1.7319121124709868e-16+2.8284271247461903j)'),
    ('round(1e400)', 'cannot round inf'),
    ('float(10**400)', 'int too large to convert to float'),
    ('min()', 'min expected at least 1 argument, got 0'),
])
def test_calculator_error_message(example_modules, expression, message):
    calculator_tool, _ = example_modules
    with pytest.raises(calculator_tool.CalculatorError) as e:
        calculator_tool.execute_calculator(expression)
    assert str(e.value) == message


def test_engine_records_a_calculator_refusal_as_its_error(example_modules):
    assert _execute_tool('calculator', json.dumps({'expression': '1/0'})) \
        == '{"error": "division by zero"}'
