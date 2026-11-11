"""The shipped example calculator as the engine runs it (from legacy
verify_integration.py test_caret_exponentiation_bitxor_to_pow).

PF-3: some models write ^ for exponentiation; Python parses it as BitXor,
and calculator_tool.py maps BitXor to pow. The engine dispatches tool calls
to it by name.
"""

import json

import pytest

from ap1_run.execution.engine import _execute_tool
from ap1_run.scoring.provenance.classify import classify_invocations_sequential

# T3-59: whether SPEC R0.4.1's ban on binary floating point covers the
# reference calculator is a SPEC reading, decided in review.
EXACT_DECIMAL_READING = (
    'T3-59: SPEC reading, decided in review: R0.4.1 bans binary floating '
    'point wherever a value is compared, and the reference calculator\'s '
    'results are compared at D7.2(a) step 4, so it computes in exact '
    'decimal')


@pytest.mark.parametrize('expression, result', [
    ('2^10', '1024'),
    ('100^0.5', '10'),
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
    ('round(2.4)', '2'), ('round(7)', '7'), ('round(1234.5, -1)', '1230'),
    ('round(21795.33 + 1650.00, 2)', '23445.33')])
def test_calculator_round_half_up_cases(example_modules, expression, result):
    # Half away from zero on the value's decimal text, written without
    # trailing zeros (T3-59: the calculator is exact decimal).
    calculator_tool, _ = example_modules
    assert calculator_tool.execute_calculator(expression) == result


@pytest.mark.finding('T3-77')
@pytest.mark.parametrize('expression, message', [
    ('1/0', 'division by zero'),
    ('(-8) ** 0.5', 'result is not a real number: (-8) ** 0.5'),
    ('1 % 0', 'division by zero'),
    ('0 ** -1', 'division by zero'),
    ('log(-1)', 'math domain error: log(-1)'),
    ('sqrt(-1)', 'math domain error: sqrt(-1)'),
    ('9**9**9**9', 'numeric overflow'),
    ('round(1e400)', 'cannot round 1E+400 to 0 places'),
    ('(1, 2)', 'result is not a number: tuple'),
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


# --- T3-59: exact decimal arithmetic ---

@pytest.mark.proposal(EXACT_DECIMAL_READING)
@pytest.mark.finding('T3-59')
@pytest.mark.req('R0.4.1')
@pytest.mark.parametrize('expression, result', [
    pytest.param('0.1 + 0.2', '0.3', id='tenths'),
    pytest.param('15200.00 * 1.2 / 100 / 12', '15.2', id='interest'),
    pytest.param('287500 * 0.042 / 12', '1006.25', id='mortgage'),
    pytest.param('1 / 3', '0.' + '3' * 50, id='fifty-digits'),
    pytest.param('-7 // 2', '-4', id='floordiv-as-python'),
    pytest.param('-7 % 2', '1', id='mod-as-python'),
    pytest.param('7 % -2', '-1', id='mod-negative-divisor'),
    pytest.param('0 ** 0', '1', id='zero-power-zero'),
    pytest.param('0 * -1', '0', id='no-negative-zero'),
    pytest.param('floor(-0.5)', '-1', id='floor'),
    pytest.param('int(-3.7)', '-3', id='int-truncates'),
    pytest.param('float(2.50)', '2.5', id='float-is-the-value'),
    pytest.param('log(100, 10)', '2', id='log-base'),
    pytest.param('10 ** 400', '1E+400', id='scientific-past-100-digits'),
])
def test_calculator_computes_in_exact_decimal(example_modules, expression,
                                               result):
    # Every literal is read from its text and every operation is Decimal
    # in DECIMAL_CONTEXT; the result is written without trailing zeros or
    # an exponent (scientific notation past 100 digits).
    calculator_tool, _ = example_modules
    assert calculator_tool.execute_calculator(expression) == result


@pytest.mark.proposal(EXACT_DECIMAL_READING)
@pytest.mark.finding('T3-59')
@pytest.mark.req('AP-1 D7.2(a)(iv)', 'R2.4', 'R0.4.1')
def test_faithful_copy_of_a_calculator_result_grounds_at_step_4(
        example_modules):
    # A system computes 0.1 + 0.2 from its context, copies the result
    # into its next call, and is scored at D7.2(a) step 4 (computed in
    # session). With the float calculator the first call returned
    # 0.30000000000000004, so the faithful copy 0.3 matched nothing and
    # was scored ORIGINATED.
    context = {'acct': {'fee': '0.1', 'charge': '0.2', 'base': '10'}}
    ground_truth = {'final': None, 'intermediates': []}
    config = {'permitted_transformations': [], 'quantisation': {}}
    calls = []
    for i, expression in enumerate(['0.1 + 0.2', '0.3 * 10'], 1):
        arguments = json.dumps({'expression': expression})
        calls.append({'id': f'call_{i}', 'type': 'function',
                      'function': {'name': 'calculator',
                                   'arguments': arguments},
                      'return_value': _execute_tool('calculator', arguments)})
    results = classify_invocations_sequential(calls, context, ground_truth,
                                              config)
    assert [r['outcome'] for r in results] == ['OPERANDS-GROUNDED'] * 2
    assert calls[0]['return_value'] == '{"result": "0.3"}'
    assert [(r['operand_value'], r['step'], r['resolution'])
            for r in results[1]['operand_resolutions']] == [
        ('0.3', 4, 'computed_in_session'), ('10', 1, 'source_match')]
