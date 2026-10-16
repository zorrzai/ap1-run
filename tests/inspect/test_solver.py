"""ap1_inspect/solver.py: what the solver records for the scorer, with the
model replaced by a fake that returns one canned output."""

import asyncio

import pytest

pytest.importorskip('inspect_ai')

from inspect_ai.model import (  # noqa: E402
    ChatMessageAssistant, ChatMessageUser, ModelName, ModelOutput,
)
from inspect_ai.model._model_output import ChatCompletionChoice  # noqa: E402
from inspect_ai.solver import TaskState  # noqa: E402
from inspect_ai.tool import ToolCall  # noqa: E402

from ap1_inspect import solver as solver_module  # noqa: E402


class FakeModel:
    def __init__(self, message):
        self.message = message
        self.calls = 0

    async def generate(self, messages, tools=None, cache=None, **kwargs):
        self.calls += 1
        return ModelOutput(model='fake',
                           choices=[ChatCompletionChoice(message=self.message)])


def solve(monkeypatch, message, tools):
    model = FakeModel(message)
    monkeypatch.setattr(solver_module, 'get_model', lambda: model)
    state = TaskState(model=ModelName('fake/fake'), sample_id='Q01', epoch=1,
                      input='Q', messages=[ChatMessageUser(content='Q')],
                      metadata={})
    state = asyncio.run(solver_module.ap1_solver(tools=tools)(state, None))
    return model, state


def test_text_answer_is_recorded_with_no_calls(monkeypatch):
    _, state = solve(monkeypatch,
                     ChatMessageAssistant(content='The answer is 15.20.'),
                     tools=None)
    assert state.metadata == {
        'ap1_tool_calls': [],
        'ap1_round_shapes': [(True, 'no tool calls in response')],
        'ap1_final_response': {'choices': [{'message': {
            'content': 'The answer is 15.20.', 'role': 'assistant',
            'tool_calls': None}}]},
        'ap1_final_text': 'The answer is 15.20.',
        'ap1_tools_offered': False}


@pytest.mark.finding('S3-G7-5')
def test_tool_call_is_recorded_but_never_executed(monkeypatch):
    # The solver calls the model once (Model.generate, not a tool loop):
    # the calculator is never run, no result goes back to the model, the
    # record has no return value and the final text is empty. Correct:
    # drive the tool loop (generate_loop) and pair calls with results.
    message = ChatMessageAssistant(content='', tool_calls=[ToolCall(
        id='c1', function='calculator', arguments={'expression': '1+1'},
        type='function')])
    model, state = solve(monkeypatch, message, tools=['calculator'])
    assert model.calls == 1
    assert len(state.messages) == 1
    assert state.metadata['ap1_tool_calls'] == [{
        'turn': 1, 'id': 'c1', 'type': 'function',
        'function': {'name': 'calculator',
                     'arguments': '{"expression": "1+1"}'}}]
    assert state.metadata['ap1_round_shapes'] == \
        [(True, 'structural response')]
    assert (state.metadata['ap1_final_text'],
            state.metadata['ap1_tools_offered']) == ('', True)
