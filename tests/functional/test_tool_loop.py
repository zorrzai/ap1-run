"""The live tool loop end to end through engine.execute_item, against a
scripted endpoint on 127.0.0.1: adapter, tool loop, evidence, provenance,
operation correctness and transcript together (from legacy
verify_integration.py).

Legacy verify_integration drove its own copy of the tool loop for its first
two tests; these drive the runner's engine instead.
"""

import json
from decimal import Decimal

import pytest

from ap1_run.execution.engine import execute_item
from ap1_run.execution.evidence import EV_0, EV_2, classify_invocation
from ap1_run.foundation import adapter
from ap1_run.foundation.transcript import read_all


@pytest.fixture
def run_item(example, endpoint, tmp_path):
    """Execute one example item against the scripted endpoint."""
    def run(item_id='Q01', *, script, condition='base'):
        endpoint.queue[:] = script
        config = dict(example['config'], endpoint_url=endpoint.url,
                      model='mock-v1')
        item = next(i for i in example['items'] if i['id'] == item_id)
        transcript = tmp_path / 'transcript.jsonl'
        result = execute_item(
            item, condition=condition, config=config,
            fixture=example['fixture'],
            ground_truth_compute=example['gt'].compute,
            adapter_send=adapter.send,
            system_prompt=config['system_prompt_base'],
            tools=config['tools'], transcript_path=transcript,
            seal_hash='test-seal')
        return result, read_all(transcript)
    return run


# -- multi-round accumulation (R1.3, D7.9) --------------------------------

@pytest.mark.req('R1.3')
def test_multi_round_loop_classifies_from_accumulated_calls(run_item, turns,
                                                            endpoint):
    result, transcript = run_item(script=[
        turns.calls('15200.00 * 1.2 / 100 / 12'),
        turns.text('The monthly interest is $15.20.')])
    assert (result['status'], result['evidence_class'],
            result['invocation_outcome']) == ('EXECUTED', EV_2, 'INVOKED')
    assert result['tool_calls'] == [{
        'turn': 1, 'id': 'call_1', 'type': 'function',
        'function': {'name': 'calculator', 'arguments': json.dumps(
            {'expression': '15200.00 * 1.2 / 100 / 12'})},
        # The example calculator evaluates in float.
        'return_value': '{"result": "15.200000000000001"}'}]
    # Round 2 carried the tool result back to the model.
    assert endpoint.requests[1]['messages'][-1] == {
        'role': 'tool', 'tool_call_id': 'call_1',
        'content': '{"result": "15.200000000000001"}'}
    assert [e['invocation_outcome'] for e in transcript] == ['INVOKED']


@pytest.mark.req('R1.3')
def test_final_response_alone_would_read_as_not_invoked(run_item, turns):
    # The regression guard of legacy verify_integration: the final
    # response of a completed loop has no tool calls by construction.
    result, _ = run_item(script=[turns.calls('15200.00 * 1.2 / 100 / 12'),
                                 turns.text('The monthly interest is $15.20.')])
    assert classify_invocation(
        result['response'], tools_offered=True, accumulated_tool_calls=[],
        round_shapes=[(True, None), (True, None)],
        required_operation='calculator') == (EV_2, 'NOT-INVOKED', None)


@pytest.mark.finding('T3-1')
@pytest.mark.req('R1.3')
def test_unrecognised_shape_in_round_2_gives_ev0_with_no_outcome(run_item,
                                                                 turns):
    # EV-0 with no outcome is what R1.3 asks for here; how the run then
    # aggregates EV-0 into D7.1 is T3-1 (scenario t3_1_unrecognised_shape).
    result, transcript = run_item(script=[
        turns.calls('1 + 1'),
        {'output': [{'text': 'something'}], 'status': 'completed'}])
    assert (result['status'], result['evidence_class'],
            result['invocation_outcome']) == ('EXECUTED', EV_0, None)
    assert len(result['tool_calls']) == 1
    assert transcript[0]['evidence_class'] == EV_0


# -- required operation (D7.1) --------------------------------------------

@pytest.mark.req('R1.3', 'R2.3')
@pytest.mark.parametrize('name, outcome', [('calculator', 'INVOKED'),
                                           ('other_tool', 'NOT-INVOKED')])
def test_invocation_requires_a_call_to_the_required_operation(name, outcome):
    final = {'choices': [{'message': {'role': 'assistant', 'content': 'done'}}]}
    assert classify_invocation(
        final, tools_offered=True,
        accumulated_tool_calls=[{'function': {'name': name}, 'id': 'c1'}],
        round_shapes=[(True, None), (True, None)],
        required_operation='calculator') == (EV_2, outcome, None)


@pytest.mark.finding('T3-38')
@pytest.mark.req('R1.3', 'R2.3')
def test_call_to_an_unknown_tool_is_recorded_and_not_invoked(run_item, turns):
    # The engine answers an unknown tool with an error and scores the
    # execution NOT-INVOKED with one call recorded; since the T3-38 fix
    # the run's consistency check accepts it (no call to the required
    # operation; scenario t3_38_unknown_tool).
    result, _ = run_item(script=[turns.calls('1 + 1', name='other_tool'),
                                 turns.text('The answer is $15.20.')])
    assert (result['evidence_class'], result['invocation_outcome']) == \
        (EV_2, 'NOT-INVOKED')
    assert result['tool_calls'][0]['return_value'] == \
        '{"error": "unknown tool: other_tool"}'
    from ap1_run.runner.summary import verify_invocation_consistency
    verify_invocation_consistency([{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
        'status': result['status'],
        'invocation_outcome': result['invocation_outcome'],
        'tool_calls_count': len(result['tool_calls']),
        'other_tool_calls_count': 1}])


# -- every scorer reachable from the live path ----------------------------

@pytest.mark.req('R1.2', 'R2.0', 'R2.1', 'R2.2', 'R2.4')
def test_live_path_result_feeds_every_scorer(run_item, turns, example):
    from ap1_run.execution.context import build_delivered_context
    from ap1_run.scoring.accuracy import score_accuracy, summarise_accuracy
    from ap1_run.scoring.figure_id import identify_figure
    from ap1_run.scoring.reproducibility import classify_mechanism
    result, transcript = run_item(script=[turns.calls('15.200 * 1'),
                                          turns.text('The answer is $15.200.')])
    assert result['status'] == 'EXECUTED'
    # D7.2(a): provenance with per-operand steps
    assert [(r['operand_value'], r['step'], r['resolution'])
            for p in result['provenance_results']
            for r in p['operand_resolutions']] == \
        [('15.200', 3, 'intermediate'), ('1', 1, 'constant')]
    # D7.2(b): written to the transcript
    assert [o['outcome'] for o in transcript[0]['operation_correctness']] == \
        ['OPERATION-CORRECT']
    # D1
    config = example['config']
    item = example['items'][0]
    ctx = build_delivered_context(example['fixture'], item['source_accounts'])
    expected = result['ground_truth']['final']
    fig = identify_figure(result['response'], expected_value=expected,
                          delivered_context=ctx, lookup_collision=False,
                          answer_tolerance=config['answer_tolerance'],
                          decline_markers=config['decline_markers'],
                          currency_symbols=config['currency_symbols'])
    assert (fig['outcome'], fig['released_figure']) == \
        ('AUTO-MATCH', Decimal('15.200'))
    acc = score_accuracy(fig, expected_value=expected,
                         answer_tolerance=config['answer_tolerance'])
    d1 = summarise_accuracy([acc])
    assert (acc['outcome'], d1['auto_scored_n'], d1['adjudicated_n']) == \
        ('CORRECT', 1, 0)
    # D2
    mech = classify_mechanism([result['response']], surface='figures',
                              minimum_runs=1)
    assert mech['mechanism'] == 'OBSERVED-ONLY'


# -- D22 laundering through the live path ---------------------------------

@pytest.mark.req('R2.4')
def test_return_of_originated_call_stays_originated_in_next_call(run_item,
                                                                 turns):
    result, _ = run_item(script=[
        turns.calls('99999 * 1', ids=['call_d22_1']),
        turns.calls('99999 + 1', ids=['call_d22_2']),
        turns.text('The answer is 100000.')])
    prov = result['provenance_results']
    assert [p['outcome'] for p in prov] == \
        ['OPERAND-ORIGINATED', 'OPERAND-ORIGINATED']
    assert [(r['operand_value'], r['step'], r['resolution'])
            for r in prov[1]['operand_resolutions']] == \
        [('99999', 5, 'computed_in_session_ungrounded'),
         ('1', 1, 'constant')]
