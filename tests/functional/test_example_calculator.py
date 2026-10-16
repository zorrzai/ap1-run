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
