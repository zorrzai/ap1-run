"""ap1_inspect/shim.py: Inspect ToolCall objects to the runner's tool-call
records (from legacy verify_inspect.py test_shim_unit and the record half
of test_inspect_wrapper_agrees_with_runner)."""

import json

import pytest

from ap1_inspect.shim import ShimError, build_final_response, inspect_tc_to_runner


class FakeToolCall:
    def __init__(self, id, function, arguments, type='function'):
        self.id, self.function, self.arguments, self.type = \
            id, function, arguments, type


class UntypedToolCall:
    id = 'c9'
    function = 'calculator'
    arguments = {'expression': '1'}


def test_shim_maps_fields_to_runner_record():
    record = inspect_tc_to_runner(
        FakeToolCall('call_1', 'calculator', {'expression': '1+1'}), turn=1)
    assert record == {'turn': 1, 'id': 'call_1', 'type': 'function',
                      'function': {'name': 'calculator',
                                   'arguments': '{"expression": "1+1"}'}}


def test_shim_defaults_turn_one_and_type_function():
    assert inspect_tc_to_runner(UntypedToolCall()) == {
        'turn': 1, 'id': 'c9', 'type': 'function',
        'function': {'name': 'calculator', 'arguments': '{"expression": "1"}'}}


def test_shim_attaches_json_return_value_unchanged():
    record = inspect_tc_to_runner(
        FakeToolCall('c1', 'calculator', {'expression': '1+1'}), turn=2,
        return_value='{"result": "2"}')
    assert (record['turn'], record['return_value']) == (2, '{"result": "2"}')


def test_shim_refuses_non_string_return_value():
    with pytest.raises(ShimError) as exc:
        inspect_tc_to_runner(FakeToolCall('c1', 'calculator', {}),
                             return_value={'result': '2'})
    assert str(exc.value) == (
        'return_value must be str, got dict; ChatMessageTool.text should '
        'have been used, not .content')


def test_shim_refuses_return_value_that_is_not_json():
    with pytest.raises(ShimError, match=r"^return_value is not valid JSON: "
                                        r"'two'; provenance\.classify\."
                                        r"_parse_return_value will fail: "):
        inspect_tc_to_runner(FakeToolCall('c1', 'calculator', {}),
                             return_value='two')


@pytest.mark.parametrize('present, message', [
    (False, {'content': 'The answer is 2.', 'role': 'assistant',
             'tool_calls': None}),
    (True, {'content': 'The answer is 2.', 'role': 'assistant'}),
])
def test_final_response_has_runner_shape(present, message):
    assert build_final_response('The answer is 2.',
                                tool_calls_present=present) == \
        {'choices': [{'message': message}]}


def test_final_response_of_no_text_has_empty_content():
    assert build_final_response(None, tool_calls_present=False) == \
        {'choices': [{'message': {'content': '', 'role': 'assistant',
                                  'tool_calls': None}}]}


# Records in engine.py's shape, from legacy verify_inspect's step-4
# scenarios (quantised intermediates reused across calls).
RUNNER_RECORDS = {
    'Q07_step4': [
        {'turn': 1, 'id': 'call_Q07s4_1', 'type': 'function',
         'function': {'name': 'calculator', 'arguments': json.dumps(
             {'expression': '42175.00 * 7.8 / 100 / 12'})},
         'return_value': json.dumps({'result': '274.13'})},
        {'turn': 2, 'id': 'call_Q07s4_2', 'type': 'function',
         'function': {'name': 'calculator', 'arguments': json.dumps(
             {'expression': '274.13 - 15.00'})},
         'return_value': json.dumps({'result': '259.13'})},
        {'turn': 3, 'id': 'call_Q07s4_3', 'type': 'function',
         'function': {'name': 'calculator', 'arguments': json.dumps(
             {'expression': '259.13 * 3'})},
         'return_value': json.dumps({'result': '777.39'})},
    ],
    'Q04_step4': [
        {'turn': 1, 'id': 'call_Q04s4_1', 'type': 'function',
         'function': {'name': 'calculator', 'arguments': json.dumps(
             {'expression': '287500 * 4.20 / 100 / 12'})},
         'return_value': json.dumps({'result': '1006.3'})},
        {'turn': 2, 'id': 'call_Q04s4_2', 'type': 'function',
         'function': {'name': 'calculator', 'arguments': json.dumps(
             {'expression': '1437 - 1006.3'})},
         'return_value': json.dumps({'result': '430.7'})},
    ],
}


@pytest.mark.parametrize('scenario', sorted(RUNNER_RECORDS))
def test_real_inspect_toolcalls_round_trip_to_identical_records(scenario):
    # Identical records mean every runner classifier agrees on both paths,
    # which is what the legacy agreement test established (through its own
    # copy of the scorer, T3-43).
    tool = pytest.importorskip('inspect_ai.tool')
    shimmed = [
        inspect_tc_to_runner(
            tool.ToolCall(id=r['id'], function=r['function']['name'],
                          arguments=json.loads(r['function']['arguments']),
                          type=r['type']),
            turn=r['turn'], return_value=r['return_value'])
        for r in RUNNER_RECORDS[scenario]]
    assert shimmed == RUNNER_RECORDS[scenario]
