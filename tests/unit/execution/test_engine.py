"""Unit tests for the execution engine (execution/engine.py).

execute_item builds the request, sends it through the adapter, drives the
tool loop, classifies the evidence, runs D7.2(a)/(b) and writes one
transcript record. The adapter is a recording fake that returns scripted
responses; the calculator is a fake module put in sys.modules. The
transcript is real, in a temporary directory. The scoring modules are
real unless a test replaces them with recorders to check the wiring.
"""

import copy
import json
import sys
import types
from decimal import Decimal

import pytest

from ap1_run.execution import engine
from ap1_run.execution.context import ContextError
from ap1_run.execution.engine import (
    CONDITION_BASE, CONDITION_INSTRUCTION_REMOVED, VALID_CONDITIONS,
    EngineError, execute_item,
)
from ap1_run.execution.evidence import EV_0, EV_2, EV_3, EvidenceError
from ap1_run.foundation import adapter, transcript

D = Decimal

FIXTURE = {'accounts': [
    {'id': 'savings', 'name': 'Savings', 'balance': '15200.00',
     'annual_rate': '1.2'},
    {'id': 'checking', 'name': 'Checking', 'balance': '3200.00'},
]}
ITEM = {'id': 'Q01', 'text': 'What is the monthly interest?',
        'source_accounts': ['savings']}
GT = {'final': D('15.20'), 'derivable': True,
      'required_operation': 'calculator',
      'intermediates': [], 'source_fields_consumed': ['savings.balance',
                                                      'savings.annual_rate']}
CONFIG = {'endpoint_url': 'http://endpoint.test/v1', 'model': 'model-1',
          'sampling': {'temperature': '0'},
          'permitted_transformations': ['percent_to_fraction'],
          'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'}}
TOOLS = [{'type': 'function', 'function': {'name': 'calculator'}}]
USER_TEXT = ('Here is the financial information:\n\nSavings:\n'
             '  Balance: 15200.00\n  Annual Rate: 1.2\n\n'
             'Question: What is the monthly interest?')
INITIAL = [{'role': 'system', 'content': 'Use the calculator.'},
           {'role': 'user', 'content': USER_TEXT}]


def answer(content='The monthly interest is $15.20.', **message):
    return {'choices': [{'message': {'role': 'assistant',
                                     'content': content, **message}}]}


def tool_call(expression='15200*1.2/100/12', id='call_1', name='calculator',
              arguments=None):
    if arguments is None:
        arguments = json.dumps({'expression': expression})
    return {'id': id, 'type': 'function',
            'function': {'name': name, 'arguments': arguments}}


def calls(*tcs):
    return {'choices': [{'message': {'role': 'assistant', 'content': None,
                                     'tool_calls': list(tcs)}}]}


class FakeAdapter:
    """Returns scripted replies (an Exception is raised) and records calls."""

    def __init__(self, *replies):
        self.replies = list(replies)
        self.calls = []

    def __call__(self, url, *, messages, tools, sampling, model):
        self.calls.append({'url': url, 'messages': copy.deepcopy(messages),
                           'tools': tools, 'sampling': sampling,
                           'model': model})
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return reply, {'request_no': len(self.calls)}


@pytest.fixture
def calculator(monkeypatch):
    """A fake calculator_tool module; records expressions."""
    module = types.ModuleType('calculator_tool')
    module.seen = []

    def execute_calculator(expression):
        module.seen.append(expression)
        if expression == 'boom':
            raise ValueError('cannot evaluate boom')
        return '15.2'

    module.execute_calculator = execute_calculator
    monkeypatch.setitem(sys.modules, 'calculator_tool', module)
    return module


def run(tmp_path, adapter_send, *, item=ITEM, gt=GT, config=CONFIG,
        tools=TOOLS, system_prompt='Use the calculator.', condition='base'):
    path = tmp_path / 'run.jsonl'
    result = execute_item(
        item, condition=condition, config=config, fixture=FIXTURE,
        ground_truth_compute=lambda item_id, ctx: dict(gt),
        adapter_send=adapter_send, system_prompt=system_prompt,
        tools=tools, transcript_path=str(path), seal_hash='seal-1')
    return result, transcript.read_all(path)


def without_timestamp(record):
    assert record.pop('timestamp')
    return record


class Recorders:
    """Recording stand-ins for the scoring functions execute_item calls."""

    def __init__(self, monkeypatch):
        self.calls = {}
        self.operation = {}      # expression -> result dict or exception
        monkeypatch.setattr(engine, 'classify_invocations_sequential',
                            self.classify_invocations_sequential)
        monkeypatch.setattr(engine, 'classify_operation',
                            self.classify_operation)
        monkeypatch.setattr(engine, 'reclassify_session',
                            self.reclassify_session)

    def classify_invocations_sequential(self, *args):
        self.calls.setdefault('provenance', []).append(copy.deepcopy(args))
        return [{'provenance': 'P'}]

    def classify_operation(self, *args):
        self.calls.setdefault('operation', []).append(args)
        found = self.operation.get(args[0], {'outcome': f'OC {args[0]}'})
        if isinstance(found, Exception):
            raise found
        return found

    def reclassify_session(self, results, exprs):
        self.calls.setdefault('reclassify', []).append(
            (list(results), list(exprs)))
        return [dict(r, reclassified=True) for r in results]


@pytest.fixture
def recorders(monkeypatch):
    return Recorders(monkeypatch)


# -- constants ---------------------------------------------------------

def test_conditions_base_and_instruction_removed():
    assert (CONDITION_BASE, CONDITION_INSTRUCTION_REMOVED) == (
        'base', 'instruction_removed')
    assert VALID_CONDITIONS == {'base', 'instruction_removed'}


# -- underivable items -------------------------------------------------

@pytest.mark.req('R1.2')
def test_execute_item_underivable_void_without_request(tmp_path):
    gt = dict(GT, derivable=False)
    send = FakeAdapter()
    result, records = run(tmp_path, send, gt=gt,
                          condition='instruction_removed')
    assert send.calls == []
    assert result == {'item_id': 'Q01', 'condition': 'instruction_removed',
                      'status': 'VOID', 'reason': 'underivable',
                      'ground_truth': gt}
    assert [without_timestamp(r) for r in records] == [{
        'item_id': 'Q01', 'arm_id': 'instruction_removed',
        'condition': 'instruction_removed', 'request_sent': None,
        'response_received': None, 'tool_calls': [], 'evidence_class': None,
        'error_state': 'VOID', 'seal_hash': 'seal-1',
        'void_reason': 'underivable', 'repeat': None}]


def test_execute_item_derivable_missing_treated_derivable(tmp_path):
    gt = {k: v for k, v in GT.items() if k != 'derivable'}
    result, _ = run(tmp_path, FakeAdapter(answer()), gt=gt)
    assert result['status'] == 'EXECUTED'


def test_execute_item_ground_truth_given_delivered_context(tmp_path):
    seen = []

    def compute(item_id, ctx):
        seen.append((item_id, ctx))
        return dict(GT, derivable=False)

    execute_item(ITEM, condition='base', config=CONFIG, fixture=FIXTURE,
                 ground_truth_compute=compute, adapter_send=FakeAdapter(),
                 system_prompt='', tools=TOOLS,
                 transcript_path=str(tmp_path / 't.jsonl'), seal_hash='s')
    assert seen == [('Q01', {'savings': {'balance': '15200.00',
                                         'annual_rate': '1.2'}})]


def test_execute_item_unknown_source_account_raises_before_request(tmp_path):
    send = FakeAdapter()
    with pytest.raises(ContextError):
        run(tmp_path, send, item=dict(ITEM, source_accounts=['pension']))
    assert send.calls == []


# -- the request -------------------------------------------------------

def test_execute_item_first_request_exact(tmp_path):
    send = FakeAdapter(answer())
    run(tmp_path, send)
    assert send.calls == [{'url': 'http://endpoint.test/v1',
                           'messages': INITIAL, 'tools': TOOLS,
                           'sampling': {'temperature': '0'},
                           'model': 'model-1'}]


def test_execute_item_no_sampling_no_model_defaults(tmp_path):
    send = FakeAdapter(answer())
    config = {'endpoint_url': 'http://e'}
    run(tmp_path, send, config=config)
    assert (send.calls[0]['sampling'], send.calls[0]['model']) == ({}, None)


@pytest.mark.parametrize('prompt', ['', None])
def test_execute_item_no_system_prompt_user_message_only(tmp_path, prompt):
    send = FakeAdapter(answer())
    run(tmp_path, send, system_prompt=prompt)
    assert send.calls[0]['messages'] == [{'role': 'user',
                                          'content': USER_TEXT}]


# -- round-0 transport failure -----------------------------------------

@pytest.mark.finding('F4', 'T3-65')
@pytest.mark.parametrize('error, cause', [
    (adapter.RateLimitError('Rate limit reached'), 'rate_limited'),
    (adapter.HTTPError('HTTP 500: server error', 500, '{}'),
     'transport_error'),
    (adapter.AdapterError('connection dropped'), 'transport_error'),
    (RuntimeError('anything'), 'transport_error'),
], ids=['rate-limit', 'http', 'adapter', 'other'])
def test_execute_item_first_send_fails_unmeasured(tmp_path, error, cause):
    # F4 / T3-65 (Steven, choices-for-marcus #7): every exception from the
    # first send is caught here, written to the transcript and returned
    # as UNMEASURED with its cause (a rate limit or a transport error);
    # the runner lists the cell (runner/executions.record_not_scored).
    result, records = run(tmp_path, FakeAdapter(error))
    assert result == {'item_id': 'Q01', 'condition': 'base',
                      'status': 'UNMEASURED', 'error': str(error),
                      'cause': cause, 'ground_truth': GT}
    assert [without_timestamp(r) for r in records] == [{
        'item_id': 'Q01', 'arm_id': 'base', 'condition': 'base',
        'request_sent': {'messages': INITIAL}, 'response_received': None,
        'tool_calls': [], 'evidence_class': EV_0,
        'error_state': f'TRANSPORT_FAILURE: {error}', 'seal_hash': 'seal-1',
        'repeat': None}]


# -- the repeat index (T3-9) --------------------------------------------

@pytest.mark.finding('T3-9')
@pytest.mark.req('R0.3', 'R3.2')
@pytest.mark.parametrize('gt, replies', [
    (dict(GT, derivable=False), []),
    (GT, [adapter.AdapterError('HTTP 500')]),
    (GT, [answer()])], ids=['void', 'transport-failure', 'executed'])
def test_execute_item_writes_its_repeat_on_the_record(tmp_path, gt, replies):
    # Every record the engine writes carries the repeat it was given, so
    # the outputs can join a record to its own execution.
    path = tmp_path / 'run.jsonl'
    execute_item(
        ITEM, condition='base', config=CONFIG, fixture=FIXTURE,
        ground_truth_compute=lambda item_id, ctx: dict(gt),
        adapter_send=FakeAdapter(*replies), system_prompt='S',
        tools=TOOLS, transcript_path=str(path), seal_hash='seal-1',
        repeat=7)
    assert [r['repeat'] for r in transcript.read_all(path)] == [7]


# -- a plain answer ----------------------------------------------------

@pytest.mark.finding('T3-21')
def test_execute_item_answer_without_tools_record_exact(tmp_path):
    # T3-21: the record carries the D7.2 scoring (operation_correctness,
    # provenance_results) computed before the write. Correct (SPEC §2):
    # the engine writes what happened; scoring is a separate pass.
    result, records = run(tmp_path, FakeAdapter(answer()))
    assert [without_timestamp(r) for r in records] == [{
        'item_id': 'Q01', 'arm_id': 'base', 'condition': 'base',
        'request_sent': {'messages': INITIAL,
                         'request_record': {'request_no': 1}},
        'response_received': answer(), 'tool_calls': [],
        'evidence_class': EV_2, 'error_state': None, 'seal_hash': 'seal-1',
        'repeat': None,
        'invocation_outcome': 'NOT-INVOKED', 'self_report': None,
        'attestation_reason': None, 'ground_truth_final': '15.20',
        'required_operation': 'calculator', 'operation_correctness': [],
        'provenance_results': []}]
    assert result == {
        'item_id': 'Q01', 'condition': 'base', 'status': 'EXECUTED',
        'evidence_class': EV_2, 'invocation_outcome': 'NOT-INVOKED',
        'self_report': None, 'tool_calls': [], 'response': answer(),
        'ground_truth': GT, 'provenance_results': []}


def test_execute_item_self_report_recorded(tmp_path):
    text = 'I used the calculator: 15.20.'
    result, records = run(tmp_path, FakeAdapter(answer(text)))
    assert (result['self_report'], records[0]['self_report']) == (text, text)
    assert result['invocation_outcome'] == 'NOT-INVOKED'


@pytest.mark.finding('T3-10')
def test_execute_item_empty_response_recorded_as_empty_without_outcome(
        tmp_path):
    # T3-10 (fixed): an empty response is UNMEASURED with its cause; it
    # carries no evidence class and no invocation outcome, and the
    # transcript record names it.
    result, records = run(tmp_path, FakeAdapter(answer('')))
    assert result['error'] == 'empty response'
    assert 'invocation_outcome' not in result
    assert 'evidence_class' not in result
    assert (records[0]['error_state'], records[0]['evidence_class'],
            records[0]['tool_calls']) == ('UNMEASURED: empty response', None, [])
    assert records[0]['request_sent'] == {
        'messages': INITIAL, 'request_record': {'request_no': 1}}
    assert (records[0]['seal_hash'], records[0]['item_id'],
            records[0]['arm_id'], records[0]['condition']) == (
        'seal-1', 'Q01', 'base', 'base')
    assert result['ground_truth'] == GT
    assert (result['item_id'], result['condition']) == ('Q01', 'base')


@pytest.mark.finding('T3-10')
def test_execute_item_empty_answer_after_tool_call_stays_executed(
        tmp_path, calculator):
    # Only a response with no text and no tool call in any round is
    # "empty". An empty final answer after an observed call keeps its
    # observed invocation (the figure is then UNMEASURABLE in R2.0).
    result, _ = run(tmp_path, FakeAdapter(calls(tool_call()), answer('')))
    assert (result['status'], result['invocation_outcome']) == (
        'EXECUTED', 'INVOKED')


@pytest.mark.finding('T3-10')
def test_execute_item_unrecognised_empty_shape_is_ev0_not_unmeasured(
        tmp_path):
    # An unreadable shape is EV-0 UNOBSERVABLE (R1.3), not an empty
    # response.
    result, _ = run(tmp_path, FakeAdapter({'choices': []}))
    assert (result['status'], result['evidence_class']) == ('EXECUTED', EV_0)


@pytest.mark.finding('T3-10')
def test_execute_item_whitespace_response_is_not_empty(tmp_path):
    # As in R2.0 figure identification ("response has no text content"),
    # only no content at all is empty.
    result, _ = run(tmp_path, FakeAdapter(answer(' ')))
    assert (result['status'], result['invocation_outcome']) == (
        'EXECUTED', 'NOT-INVOKED')


@pytest.mark.parametrize('tools', [None, []])
def test_execute_item_no_tools_ev0(tmp_path, tools):
    send = FakeAdapter(answer())
    result, _ = run(tmp_path, send, tools=tools)
    assert (result['evidence_class'], result['invocation_outcome']) == (
        EV_0, None)
    assert send.calls[0]['tools'] == tools


def test_execute_item_attestation_reason_recorded_class_unchanged(tmp_path):
    final = answer(metadata={'attestation': {'signature': 'sig'}})
    result, records = run(tmp_path, FakeAdapter(final))
    assert records[0]['attestation_reason'].startswith(
        'attestation verification not implemented in runner v1.0')
    assert result['evidence_class'] == EV_2
    assert 'attestation_reason' not in result


def test_execute_item_ev3_guard_raises_before_write(tmp_path, monkeypatch):
    monkeypatch.setattr(engine, 'classify_invocation',
                        lambda *a, **k: (EV_3, 'INVOKED', None))
    with pytest.raises(EvidenceError):
        _, _ = run(tmp_path, FakeAdapter(answer()))
    assert transcript.read_all(tmp_path / 'run.jsonl') == []


# -- the tool loop -----------------------------------------------------

@pytest.mark.req('R1.3')
def test_execute_item_one_calculator_round_invoked(tmp_path, calculator):
    send = FakeAdapter(calls(tool_call()), answer())
    result, records = run(tmp_path, send)
    record = {'turn': 1, 'id': 'call_1', 'type': 'function',
              'function': tool_call()['function'],
              'return_value': '{"result": "15.2"}'}
    assert result['tool_calls'] == [record]
    assert records[0]['tool_calls'] == [record]
    assert (result['evidence_class'], result['invocation_outcome']) == (
        EV_2, 'INVOKED')
    assert calculator.seen == ['15200*1.2/100/12']
    assert result['response'] == answer()


def test_execute_item_tool_result_sent_back(tmp_path, calculator):
    send = FakeAdapter(calls(tool_call()), answer())
    run(tmp_path, send)
    assert len(send.calls) == 2
    assert send.calls[1] == {
        'url': 'http://endpoint.test/v1',
        'messages': INITIAL + [
            calls(tool_call())['choices'][0]['message'],
            {'role': 'tool', 'tool_call_id': 'call_1',
             'content': '{"result": "15.2"}'}],
        'tools': TOOLS, 'sampling': {'temperature': '0'},
        'model': 'model-1'}


def test_execute_item_transcript_request_is_initial_messages(
        tmp_path, calculator):
    _, records = run(tmp_path, FakeAdapter(calls(tool_call()), answer()))
    assert records[0]['request_sent'] == {
        'messages': INITIAL, 'request_record': {'request_no': 1}}


def test_execute_item_two_calls_one_turn_each_return_attached(
        tmp_path, calculator):
    send = FakeAdapter(calls(tool_call('1+1', id='a'),
                             tool_call('boom', id='b')), answer())
    result, _ = run(tmp_path, send)
    assert [(r['turn'], r['id'], r['return_value'])
            for r in result['tool_calls']] == [
        (1, 'a', '{"result": "15.2"}'),
        (1, 'b', '{"error": "cannot evaluate boom"}')]
    assert [m['role'] for m in send.calls[1]['messages']] == [
        'system', 'user', 'assistant', 'tool', 'tool']


def test_execute_item_turns_numbered_across_rounds(tmp_path, calculator):
    send = FakeAdapter(calls(tool_call(id='a')), calls(tool_call(id='b')),
                       answer())
    result, _ = run(tmp_path, send)
    assert [(r['turn'], r['id']) for r in result['tool_calls']] == [
        (1, 'a'), (2, 'b')]
    assert len(send.calls) == 3


def test_execute_item_call_type_missing_defaults_function(
        tmp_path, calculator):
    tc = tool_call()
    del tc['type']
    result, _ = run(tmp_path, FakeAdapter(calls(tc), answer()))
    assert result['tool_calls'][0]['type'] == 'function'


def test_execute_item_call_type_kept(tmp_path, calculator):
    tc = dict(tool_call(), type='custom')
    result, _ = run(tmp_path, FakeAdapter(calls(tc), answer()))
    assert result['tool_calls'][0]['type'] == 'custom'


def test_execute_item_calculator_without_arguments_gets_empty_object(
        tmp_path, calculator):
    # No arguments: '{}' is used, which has no expression, so the raw
    # '{}' itself is passed to the calculator.
    tc = {'id': 'c1', 'type': 'function', 'function': {'name': 'calculator'}}
    result, _ = run(tmp_path, FakeAdapter(calls(tc), answer()))
    assert calculator.seen == ['{}']
    assert result['tool_calls'][0]['return_value'] == '{"result": "15.2"}'


def test_execute_item_call_without_function_unknown_tool(tmp_path,
                                                         calculator):
    result, _ = run(tmp_path, FakeAdapter(calls({'id': 'c1'}), answer()))
    assert result['tool_calls'] == [{
        'turn': 1, 'id': 'c1', 'type': 'function', 'function': {},
        'return_value': '{"error": "unknown tool: "}'}]
    assert result['invocation_outcome'] == 'NOT-INVOKED'


@pytest.mark.finding('T3-38')
def test_execute_item_hallucinated_tool_not_invoked_with_calls(
        tmp_path, calculator):
    # T3-38: NOT-INVOKED with a tool call recorded, which run.py's
    # consistency check treats as FATAL after every request is spent.
    result, _ = run(tmp_path, FakeAdapter(
        calls(tool_call(name='python')), answer()))
    assert result['invocation_outcome'] == 'NOT-INVOKED'
    assert result['tool_calls'][0]['return_value'] == (
        '{"error": "unknown tool: python"}')


@pytest.mark.finding('T3-67')
def test_execute_item_tool_loop_stops_after_ten_turns_flagged(
        tmp_path, calculator):
    # After 10 turns the 11th response's calls are not executed; the
    # execution is still EXECUTED/INVOKED (the calls made were observed),
    # and the exhaustion is recorded in the transcript and the result.
    replies = [calls(tool_call(id=f'c{n}')) for n in range(1, 12)]
    send = FakeAdapter(*replies)
    result, records = run(tmp_path, send)
    assert len(send.calls) == 11
    assert [r['id'] for r in result['tool_calls']] == [
        f'c{n}' for n in range(1, 11)]
    assert result['response'] == replies[10]
    assert (result['status'], result['invocation_outcome']) == (
        'EXECUTED', 'INVOKED')
    flag = ('TOOL_LOOP_EXHAUSTED: the response after 10 tool turns still '
            'asked for 1 tool call(s), which were not executed')
    assert records[0]['error_state'] == flag
    assert result['error_state'] == flag


@pytest.mark.finding('T3-67')
def test_execute_item_loop_ending_at_turn_limit_not_flagged(tmp_path,
                                                           calculator):
    # Ten tool turns followed by an answer: the loop completed.
    replies = [calls(tool_call(id=f'c{n}')) for n in range(1, 11)]
    result, records = run(tmp_path, FakeAdapter(*replies, answer()))
    assert len(result['tool_calls']) == 10
    assert records[0]['error_state'] is None
    assert 'error_state' not in result


def test_loop_exhaustion_counts_pending_calls():
    final = calls(tool_call(id='a'), tool_call(id='b'))
    assert engine._loop_exhaustion(final, [(True, None)]) == (
        'TOOL_LOOP_EXHAUSTED: the response after 10 tool turns still '
        'asked for 2 tool call(s), which were not executed')
    assert engine._loop_exhaustion(final, [(True, None), (False, 'x')]) \
        is None
    assert engine._loop_exhaustion(final, []) is None
    assert engine._loop_exhaustion(answer(), [(True, None)]) is None


# -- unrecognised shapes and mid-loop failures -------------------------

ANTHROPIC = {'type': 'message', 'role': 'assistant',
             'content': [{'type': 'text', 'text': '15.20'}]}


@pytest.mark.finding('T3-1')
def test_execute_item_unrecognised_first_response_executed_ev0(tmp_path):
    # T3-1: EXECUTED with outcome None (EV-0). Since the T3-1 fix the
    # run's summary keeps it out of the D7.1 rate and reports it per
    # class.
    send = FakeAdapter(ANTHROPIC)
    result, records = run(tmp_path, send)
    assert len(send.calls) == 1
    assert (result['status'], result['evidence_class'],
            result['invocation_outcome']) == ('EXECUTED', EV_0, None)
    assert records[0]['error_state'] is None


def test_execute_item_unrecognised_later_response_ev0(tmp_path, calculator):
    result, _ = run(tmp_path, FakeAdapter(calls(tool_call()), ANTHROPIC))
    assert (result['evidence_class'], result['invocation_outcome']) == (
        EV_0, None)
    assert result['response'] == ANTHROPIC


@pytest.mark.finding('T3-1', 'T3-35')
def test_execute_item_later_send_fails_executed_ev0_no_error(
        tmp_path, calculator):
    # T3-1: a mid-loop failure is EXECUTED with outcome None (EV-0); since
    # the T3-1 fix it is out of the D7.1 rate. T3-35: the failure itself
    # is not recorded (error_state None; the last good response stands
    # as final). Correct: the cause of the EV-0 is recorded.
    first = calls(tool_call())
    send = FakeAdapter(first, adapter.RateLimitError('Rate limit reached'))
    result, records = run(tmp_path, send)
    assert len(send.calls) == 2
    assert (result['status'], result['evidence_class'],
            result['invocation_outcome']) == ('EXECUTED', EV_0, None)
    assert result['response'] == first
    assert len(result['tool_calls']) == 1
    assert records[0]['error_state'] is None


def test_drive_tool_loop_failed_round_recorded_unrecognised(calculator):
    send = FakeAdapter(RuntimeError('reset by peer'))
    messages = []
    tcs, final, shapes = engine._drive_tool_loop(
        response=calls(tool_call()), messages=messages, config=CONFIG,
        tools=TOOLS, adapter_send=send, sampling={})
    assert shapes == [(True, None),
                      (False, 'adapter_send failed on turn 1: reset by peer')]
    assert final == calls(tool_call())
    assert len(tcs) == 1


def test_drive_tool_loop_max_turns_parameter_bounds_sends(calculator):
    send = FakeAdapter(*[calls(tool_call(id=f'c{n}')) for n in range(5)])
    tcs, _, shapes = engine._drive_tool_loop(
        response=calls(tool_call(id='c')), messages=[], config=CONFIG,
        tools=TOOLS, adapter_send=send, sampling={}, max_turns=2)
    assert (len(send.calls), len(tcs), len(shapes)) == (2, 2, 3)


def test_drive_tool_loop_round_shapes_one_per_response(calculator):
    send = FakeAdapter(calls(tool_call(id='b')), answer())
    _, _, shapes = engine._drive_tool_loop(
        response=calls(tool_call(id='a')), messages=[], config=CONFIG,
        tools=TOOLS, adapter_send=send, sampling={})
    assert shapes == [(True, None)] * 3


# -- D7.2 wiring -------------------------------------------------------

def test_execute_item_scoring_wired(tmp_path, calculator, recorders):
    send = FakeAdapter(calls(tool_call('1+1', id='a'),
                             tool_call(name='python', id='b'),
                             tool_call('2*3', id='c')), answer())
    result, records = run(tmp_path, send)
    tcs = result['tool_calls']
    ctx = {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}
    assert recorders.calls['provenance'] == [(tcs, ctx, GT, CONFIG)]
    assert recorders.calls['operation'] == [('1+1', GT, CONFIG),
                                            ('2*3', GT, CONFIG)]
    # One expression per calculator call, aligned with the results; the
    # python call is not a calculator call (T3-16).
    assert recorders.calls['reclassify'] == [
        ([{'outcome': 'OC 1+1'}, {'outcome': 'OC 2*3'}],
         ['1+1', '2*3'])]
    assert records[0]['operation_correctness'] == [
        {'outcome': 'OC 1+1', 'reclassified': True},
        {'outcome': 'OC 2*3', 'reclassified': True}]
    assert records[0]['provenance_results'] == [{'provenance': 'P'}]
    assert result['provenance_results'] == [{'provenance': 'P'}]


def test_execute_item_operation_error_unobservable(tmp_path, calculator,
                                                   recorders):
    recorders.operation['1+1'] = ZeroDivisionError('division by zero')
    _, records = run(tmp_path, FakeAdapter(calls(tool_call('1+1')),
                                           answer()))
    assert records[0]['operation_correctness'] == [{
        'outcome': 'OPERATION-UNOBSERVABLE',
        'reason': 'evaluation failed: ZeroDivisionError: division by zero',
        'reclassified': True}]


@pytest.mark.finding('T3-16')
def test_execute_item_malformed_arguments_invoked_and_scored(
        tmp_path, calculator, recorders):
    # T3-16: non-JSON arguments count as INVOKED (D7.7) and are scored:
    # classify_operation gets no expression (None, so its outcome is
    # OPERATION-UNOBSERVABLE), and reclassify_session gets one result and
    # one expression for the call, aligned.
    bad = tool_call(arguments='15200*1.2/100/12')
    result, records = run(tmp_path, FakeAdapter(calls(bad), answer()))
    assert result['invocation_outcome'] == 'INVOKED'
    assert recorders.calls['operation'] == [(None, GT, CONFIG)]
    assert recorders.calls['reclassify'] == [([{'outcome': 'OC None'}],
                                              [None])]
    assert records[0]['operation_correctness'] == [
        {'outcome': 'OC None', 'reclassified': True}]


@pytest.mark.finding('T3-16')
def test_execute_item_malformed_call_real_scoring_unobservable(
        tmp_path, calculator):
    # With the real scorers, the malformed call is OPERANDS-UNOBSERVABLE
    # and OPERATION-UNOBSERVABLE, and the valid call after it is scored.
    bad = tool_call(arguments='15200*1.2/100/12', id='a')
    send = FakeAdapter(calls(bad, tool_call('15200*1.2', id='b')), answer())
    result, records = run(tmp_path, send)
    assert [p['outcome'] for p in result['provenance_results']] == [
        'OPERANDS-UNOBSERVABLE', 'OPERANDS-GROUNDED']
    assert [o['outcome'] for o in records[0]['operation_correctness']] == [
        'OPERATION-UNOBSERVABLE', 'WRONG-OPERATION']


@pytest.mark.finding('T3-21')
def test_execute_item_scoring_error_nothing_written(tmp_path, calculator,
                                                    monkeypatch):
    # T3-21: scoring runs before the transcript write, so a scoring
    # failure loses the spent request and its response. Correct: the
    # record is written first.
    def broken(*args):
        raise RuntimeError('scorer bug')

    monkeypatch.setattr(engine, 'classify_invocations_sequential', broken)
    send = FakeAdapter(calls(tool_call()), answer())
    with pytest.raises(RuntimeError, match='scorer bug'):
        run(tmp_path, send)
    assert len(send.calls) == 2
    assert transcript.read_all(tmp_path / 'run.jsonl') == []


def test_execute_item_real_scoring_correct_call(tmp_path, calculator):
    result, records = run(tmp_path, FakeAdapter(calls(tool_call('15200*1.2')),
                                                answer()))
    assert [p['outcome'] for p in result['provenance_results']] == [
        'OPERANDS-GROUNDED']
    assert len(records[0]['operation_correctness']) == 1


# -- _execute_tool -----------------------------------------------------

def test_execute_tool_calculator_result_json(calculator):
    assert engine._execute_tool('calculator', '{"expression": "1+1"}') == (
        '{"result": "15.2"}')
    assert calculator.seen == ['1+1']


def test_execute_tool_no_expression_key_passes_raw_arguments(calculator):
    engine._execute_tool('calculator', '{"expr": "1+1"}')
    assert calculator.seen == ['{"expr": "1+1"}']


def test_execute_tool_calculator_error_returned(calculator):
    assert engine._execute_tool('calculator', '{"expression": "boom"}') == (
        '{"error": "cannot evaluate boom"}')


def test_execute_tool_invalid_json_error_returned(calculator):
    result = json.loads(engine._execute_tool('calculator', 'one plus one'))
    assert result['error'].startswith('Expecting value')
    assert calculator.seen == []


def test_execute_tool_unknown_tool_error(calculator):
    assert engine._execute_tool('python', '{}') == (
        '{"error": "unknown tool: python"}')


def test_execute_tool_calculator_not_importable_error(monkeypatch):
    monkeypatch.setitem(sys.modules, 'calculator_tool', None)
    result = json.loads(engine._execute_tool('python', '{}'))
    assert 'calculator_tool' in result['error']


# -- _extract_calc_expression ------------------------------------------

@pytest.mark.parametrize('record, expected', [
    (tool_call('1+1'), '1+1'),
    (tool_call(name='python'), None),
    ({'id': 'x'}, None),
    (tool_call(arguments='{"expr": "1+1"}'), None),
    (tool_call(arguments='1+1'), None),
    ({'function': {'name': 'calculator', 'arguments': None}}, None),
    ({'function': {'name': 'calculator'}}, None),
    (tool_call(arguments='{"expression": 15.2}'), 15.2),
], ids=['calc', 'other-tool', 'no-function', 'no-expression', 'not-json',
        'null-arguments', 'no-arguments', 'numeric'])
def test_extract_calc_expression(record, expected):
    assert engine._extract_calc_expression(record) == expected


# -- _extract_tool_calls, _record_shape, _build_messages ---------------

@pytest.mark.parametrize('resp', [
    'text', None, {}, {'choices': []}, {'choices': [{}]},
    answer(), answer(tool_calls=None), answer(tool_calls=[]),
], ids=['str', 'none', 'no-choices', 'empty-choices', 'no-message',
        'no-tool-calls', 'null-tool-calls', 'empty-tool-calls'])
def test_extract_tool_calls_none_found_empty(resp):
    assert engine._extract_tool_calls(resp) == []


def test_extract_tool_calls_found():
    assert engine._extract_tool_calls(calls(tool_call())) == [tool_call()]


def test_record_shape_appends_recognition():
    shapes = [(True, None)]
    engine._record_shape(ANTHROPIC, shapes)
    engine._record_shape(answer(), shapes)
    assert shapes == [
        (True, None),
        (False, 'response appears Anthropic-shaped (has type=message, '
                'content)'),
        (True, None)]


def test_build_messages_system_then_user():
    assert engine._build_messages(system_prompt='Use the calculator.',
                                  item=ITEM, fixture=FIXTURE,
                                  config=CONFIG) == INITIAL


# --- Step 4: correct behaviour (failing until fixed) ---

import re  # noqa: E402  (kept in this section to ease merging)


def _contains(tree, target):
    """True if target is tree or any value nested in it."""
    if tree == target:
        return True
    if isinstance(tree, dict):
        return any(_contains(v, target) for v in tree.values())
    if isinstance(tree, list):
        return any(_contains(v, target) for v in tree)
    return False


@pytest.mark.finding('T3-21')
@pytest.mark.req('R1.2', 'R0.3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-21: the engine writes D7.2(a)/(b) scoring '
                          '(provenance_results, operation_correctness) into '
                          'the transcript record')
def test_execute_item_record_has_no_scoring_fields(tmp_path, calculator):
    # Correct (SPEC §2 "R1 EXECUTE: no scoring occurs here"; R1.2 "Perform
    # no scoring"; Steven's ruling, choices-for-marcus.md entry 1): the
    # record holds what happened; D7.2 is scored by the separate pass.
    _, records = run(tmp_path, FakeAdapter(calls(tool_call()), answer()))
    assert sorted(set(records[0]) & {'operation_correctness',
                                     'provenance_results'}) == []


@pytest.mark.finding('V12-3', 'T3-52')
@pytest.mark.req('R0.2', 'R0.3', 'AP-1 §5.6')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='V12-3: only the first request and the final '
                          'response of a tool loop reach the transcript')
def test_execute_item_every_round_request_and_response_recorded(
        tmp_path, calculator):
    # Correct (SPEC R0.2 "Every request and response is written to the
    # transcript before any other processing"; AP-1 §5.6): each of the
    # three rounds' request records (as the adapter returned them) and
    # raw responses is in the transcript. Today: request 1 and response 3.
    replies = [calls(tool_call(id='a')), calls(tool_call(id='b')), answer()]
    send = FakeAdapter(*copy.deepcopy(replies))
    _, records = run(tmp_path, send)
    assert len(send.calls) == 3
    missing = ([f'request {n}' for n in (1, 2, 3)
                if not _contains(records, {'request_no': n})]
               + [f'response {n}' for n, reply in enumerate(replies, 1)
                  if not _contains(records, reply)])
    assert missing == []


@pytest.mark.finding('T3-35')
@pytest.mark.req('R1.3', 'AP-1 D7.9')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-35: a mid-loop send failure gives EV-0 with '
                          'error_state None; cause and round only in the '
                          'unwritten round_shapes')
def test_execute_item_later_send_fails_error_state_names_cause_and_round(
        tmp_path, calculator):
    # Correct (SPEC R1.3 "EV-0 UNOBSERVABLE with the round identified";
    # R0.3 "error state" field): the record says what failed and in which
    # round (the second request, round 1 counting the first as round 0).
    # Today's round_shapes reason "adapter_send failed on turn 1: Rate
    # limit reached" written into error_state would pass.
    send = FakeAdapter(calls(tool_call()),
                       adapter.RateLimitError('Rate limit reached'))
    _, records = run(tmp_path, send)
    assert records[0]['evidence_class'] == EV_0
    error_state = records[0]['error_state']
    assert error_state is not None
    text = json.dumps(error_state).lower()
    assert 'rate limit' in text
    assert re.search(r'\b(round|turn)\D{0,3}[12]\b', text)


@pytest.mark.finding('T3-35')
@pytest.mark.req('R1.3', 'AP-1 D7.9')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-35: an unrecognised later response gives EV-0 '
                          'with error_state None and the round unidentified')
def test_execute_item_unrecognised_later_response_error_state_names_round(
        tmp_path, calculator):
    # Correct (SPEC R1.3, as above): the record names the unrecognised
    # shape and the round it came in (round 1).
    _, records = run(tmp_path, FakeAdapter(calls(tool_call()), ANTHROPIC))
    assert records[0]['evidence_class'] == EV_0
    error_state = records[0]['error_state']
    assert error_state is not None
    text = json.dumps(error_state).lower()
    assert 'shape' in text
    assert re.search(r'\b(round|turn)\D{0,3}[12]\b', text)

# Group g1-invocation (fix plan branches 1 and 10).

def run_without_raising(tmp_path, adapter_send, **kwargs):
    """run(), with any exception returned instead of raised, so a test
    can assert that there was none."""
    try:
        return run(tmp_path, adapter_send, **kwargs) + (None,)
    except Exception as e:
        return None, transcript.read_all(tmp_path / 'run.jsonl'), e


@pytest.mark.finding('T3-10')
@pytest.mark.parametrize('content', ['', None], ids=['empty', 'null'])
def test_execute_item_empty_response_unmeasured(tmp_path, content):
    # Correct (SPEC R4.1 "Empty response -> UNMEASURED", R0.2; AP-1 v1.3
    # §13.2 "an empty response shall never be counted as an answer"): a
    # response with no content and no tool call is UNMEASURED, out of
    # every denominator, and still written to the transcript as received.
    final = answer(content)
    result, records = run(tmp_path, FakeAdapter(final))
    assert result['status'] == 'UNMEASURED'
    assert [r['response_received'] for r in records] == [final]


@pytest.mark.finding('T3-67')
def test_execute_item_tool_loop_exhausted_flagged_in_transcript(
        tmp_path, calculator):
    # Correct (T3 review T3-67; SPEC R0.1, R1.3 "the accumulation is
    # incomplete"): when the 11th response still asks for a tool after
    # ten turns, the exhaustion is recorded in the transcript record
    # (error_state) and in the result, not passed off as a completed
    # loop. Which outcome the item then gets is the fix's choice; here
    # only the flag is asserted.
    replies = [calls(tool_call(id=f'c{n}')) for n in range(1, 12)]
    result, records = run(tmp_path, FakeAdapter(*replies))
    assert records[0]['error_state'] is not None
    assert result['status'] != 'EXECUTED' or \
        result['invocation_outcome'] != 'INVOKED' or \
        result.get('error_state') is not None, result


@pytest.mark.finding('S3-G2-1')
@pytest.mark.parametrize('final', [
    {'choices': [{'message': None}]},
    {'choices': ['x']},
    {'choices': [{'message': {'role': 'assistant', 'content': 'x',
                              'metadata': 'attestation'}}]},
], ids=['null-message', 'str-choice', 'str-metadata'])
def test_execute_item_malformed_response_shape_ev0_recorded(tmp_path, final):
    # Correct (S3-G2-1; SPEC R1.3: an unrecognised shape is EV-0
    # UNOBSERVABLE): no exception; the execution is recorded in the
    # transcript and comes back EV-0 (or UNMEASURED).
    result, records, error = run_without_raising(tmp_path,
                                                 FakeAdapter(final))
    assert error is None, f'{type(error).__name__}: {error}'
    assert len(records) == 1
    assert result['status'] == 'UNMEASURED' or \
        result['evidence_class'] == EV_0, result


@pytest.mark.finding('S3-G2-1')
@pytest.mark.parametrize('message', [
    {'content': None, 'tool_calls': {'id': 'c1'}},
    {'content': None, 'tool_calls': ['calculator']},
    {'content': None, 'tool_calls': [{'id': 'c1', 'function': 'calc'}]},
    {'content': [{'type': 'text', 'text': '15.20'}]},
], ids=['dict-tool-calls', 'str-call', 'str-function', 'list-content'])
def test_execute_item_unreadable_message_part_ev0_no_tool_run(
        tmp_path, calculator, message):
    # Step 5 (run-robustness): a message part the evidence code cannot
    # read is an unrecognised shape: EV-0 with outcome None, nothing is
    # executed, the execution is recorded.
    final = {'choices': [{'message': {'role': 'assistant', **message}}]}
    send = FakeAdapter(final)
    result, records = run(tmp_path, send)
    assert (result['status'], result['evidence_class'],
            result['invocation_outcome']) == ('EXECUTED', EV_0, None)
    assert (result['tool_calls'], calculator.seen, len(send.calls)) == (
        [], [], 1)
    assert [r['response_received'] for r in records] == [final]


@pytest.mark.finding('S3-G2-2', 'S3-G2-3')
def test_execute_item_two_calls_without_id_in_one_turn_each_own_return(
        tmp_path, calculator):
    # Two calls of one turn without ids share the default id 'call_1';
    # each return still goes on its own record, in order.
    a, b = tool_call('1+1'), tool_call('boom')
    del a['id'], b['id']
    send = FakeAdapter(calls(a, b), answer())
    result, _ = run(tmp_path, send)
    assert [(r['id'], r['return_value']) for r in result['tool_calls']] == [
        ('call_1', '{"result": "15.2"}'),
        ('call_1', '{"error": "cannot evaluate boom"}')]
    assert [m.get('tool_call_id') for m in send.calls[1]['messages']
            if m['role'] == 'tool'] == ['call_1', 'call_1']


@pytest.mark.finding('S3-G2-2')
def test_execute_item_call_without_id_return_attached(tmp_path, calculator):
    # Correct (S3-G2-2): a call the platform sent without an id is
    # executed and its return value attached to its own record (by the
    # same default id, or by position); the run is never aborted.
    tc = tool_call()
    del tc['id']
    result, _, error = run_without_raising(
        tmp_path, FakeAdapter(calls(tc), answer()))
    assert error is None, f'{type(error).__name__}: {error}'
    assert [r.get('return_value') for r in result['tool_calls']] == \
        ['{"result": "15.2"}']
    assert result['invocation_outcome'] == 'INVOKED'


@pytest.mark.finding('S3-G2-3')
def test_execute_item_repeated_call_id_return_on_own_record(tmp_path,
                                                            calculator):
    # Correct (S3-G2-3; AP-1 v1.3 D7.2(a)(iv) uses prior returns): each
    # turn's return value is attached to that turn's call, so a reused
    # id never overwrites an earlier return.
    send = FakeAdapter(calls(tool_call('1+1', id='x')),
                       calls(tool_call('boom', id='x')), answer())
    result, _ = run(tmp_path, send)
    assert [r.get('return_value') for r in result['tool_calls']] == [
        '{"result": "15.2"}', '{"error": "cannot evaluate boom"}']


@pytest.mark.finding('S3-G2-4')
@pytest.mark.parametrize('arguments', ['["1+1"]', '"1+1"', '15.2'])
def test_extract_calc_expression_non_object_json_none(arguments):
    # Correct (S3-G2-4): arguments that are valid JSON but not an object
    # carry no expression: None, as for malformed JSON.
    try:
        found = engine._extract_calc_expression(tool_call(arguments=arguments))
    except Exception as e:
        found = e
    assert found is None


@pytest.mark.finding('T3-39', 'F6', 'S3-G2-4')
@pytest.mark.parametrize('arguments', [
    '{"expression": 15.2}', '{"expression": "True * 15.2"}',
    '{"expression": "True + 1"}', '"1+1"', '["1+1"]',
], ids=['number', 'true-times', 'true-plus', 'json-string', 'json-list'])
def test_execute_item_model_controlled_arguments_recorded_no_raise(
        tmp_path, calculator, arguments):
    # Correct (T3 review T3-39; Steven's ruling on F6, choices-for-marcus
    # #9; S3-G2-4): input the model controls never raises out of the
    # engine; the call is recorded and the execution written to the
    # transcript, with that call's operands unobservable.
    send = FakeAdapter(calls(tool_call(arguments=arguments)), answer())
    result, records, error = run_without_raising(tmp_path, send)
    assert error is None, f'{type(error).__name__}: {error}'
    assert len(records) == 1 and len(result['tool_calls']) == 1
    assert all(p['outcome'] != 'OPERANDS-GROUNDED'
               for p in result['provenance_results'])
