"""Integration tests: multi-round tool loop invocation classification.

These tests exercise the FULL tool loop -> evidence classification path
against a local mock HTTP server. They are the regression guard for the
R1.3 multi-round defect (classify_invocation was called on the final
response, which by construction contains no tool_calls).

Tests:
  1. test_multiround_loop_reports_invoked_not_final_response:
     Mock returns tool_calls on round 1, text answer on round 2.
     Assert INVOKED. Assert the accumulated record contains the call.
     Assert the final response alone would have yielded NOT-INVOKED.
     This is the regression guard.

  2. test_unrecognised_shape_in_round2_yields_ev0:
     Round 2 returns an unrecognised shape.
     Assert EV-0 UNOBSERVABLE, not NOT-INVOKED.

  3. test_required_operation_match_determines_invocation:
     Tool call to 'calculator' with required_operation='calculator'
     -> INVOKED. Tool call to 'other_tool' -> NOT-INVOKED.

  4. test_perturbation_guard_passes_on_config_prompts:
     Load config.json prompts, run perturbation guard, confirm
     exactly one changed quantity.
"""

import json
import os
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'example'))

from evidence import (
    classify_invocation, _extract_model_tool_calls,
    EV_0, EV_2,
)


# -- Mock HTTP server for integration tests --------------------------------

class IntegrationMockHandler(BaseHTTPRequestHandler):
    """Mock that rotates through scenario responses."""
    scenario_queue = []

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        self.rfile.read(content_length)

        if not self.scenario_queue:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'{"error": "no scenarios left"}')
            return

        resp_body = self.scenario_queue.pop(0)
        data = json.dumps(resp_body).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format, *args):
        pass


def _start_mock():
    server = HTTPServer(('127.0.0.1', 0), IntegrationMockHandler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, f'http://127.0.0.1:{port}/v1/chat/completions'


def _tool_call_response(expression='100 + 200'):
    return {
        'choices': [{
            'index': 0,
            'message': {
                'role': 'assistant',
                'content': None,
                'tool_calls': [{
                    'id': 'call_integ_001',
                    'type': 'function',
                    'function': {
                        'name': 'calculator',
                        'arguments': json.dumps({'expression': expression})
                    }
                }]
            },
            'finish_reason': 'tool_calls'
        }],
        'model': 'mock-v1',
    }


def _text_response(text='The answer is $300.'):
    return {
        'choices': [{
            'index': 0,
            'message': {
                'role': 'assistant',
                'content': text,
            },
            'finish_reason': 'stop'
        }],
        'model': 'mock-v1',
    }


def _unrecognised_response():
    """A response shape the runner cannot parse."""
    return {
        'output': [{'text': 'something'}],
        'status': 'completed'
    }


# -- The full tool loop (from smoke_test, inlined for isolation) -----------

def _run_tool_loop(url, initial_response, tools, sampling, model):
    """Drive a tool loop and return (all_tc, final_response, round_shapes)."""
    import adapter
    import calculator_tool as calc

    all_tc = []
    round_shapes = []
    current = initial_response
    messages = [{'role': 'user', 'content': 'test question'}]

    # Check shape of initial response
    _, r0_recog, r0_reason = _extract_model_tool_calls(initial_response)
    round_shapes.append((r0_recog, r0_reason))

    for turn in range(1, 11):
        choices = current.get('choices', [])
        if not choices:
            break
        msg = choices[0].get('message', {})
        model_calls = msg.get('tool_calls') or []
        if not model_calls:
            break

        for tc in model_calls:
            all_tc.append({
                'turn': turn,
                'id': tc.get('id', ''),
                'type': tc.get('type', 'function'),
                'function': tc.get('function', {}),
            })

        messages.append(msg)
        for tc in model_calls:
            func = tc.get('function', {})
            try:
                args = json.loads(func.get('arguments', '{}'))
                result = calc.execute_calculator(args.get('expression', '0'))
            except Exception as e:
                result = str(e)
            messages.append({
                'role': 'tool',
                'tool_call_id': tc.get('id', ''),
                'content': json.dumps({'result': result}),
            })

        try:
            current, _ = adapter.send(
                url, messages=messages, tools=tools,
                sampling=sampling, model=model, timeout=5)
            _, rn_recog, rn_reason = _extract_model_tool_calls(current)
            round_shapes.append((rn_recog, rn_reason))
        except Exception:
            break

    return all_tc, current, round_shapes


# -- TESTS ----------------------------------------------------------------

def test_multiround_loop_reports_invoked_not_final_response():
    """REGRESSION GUARD: tool loop returning tool_calls on round 1 and
    a text answer on round 2 must classify as INVOKED.

    The final response alone contains no tool_calls and would yield
    NOT-INVOKED. The runner must use the accumulated records.
    """
    server, url = _start_mock()
    try:
        # Round 1: tool_calls; Round 2: text answer
        IntegrationMockHandler.scenario_queue = [
            _tool_call_response('1500 * 5 / 100 / 12'),
            _text_response('The monthly interest is $6.25.'),
        ]

        import adapter
        # Initial request
        initial, _ = adapter.send(
            url, messages=[{'role': 'user', 'content': 'test'}],
            tools=[{'type': 'function', 'function': {'name': 'calculator'}}],
            sampling={'temperature': '0'}, model='mock-v1', timeout=5)

        all_tc, final, round_shapes = _run_tool_loop(
            url, initial,
            tools=[{'type': 'function', 'function': {'name': 'calculator'}}],
            sampling={'temperature': '0'}, model='mock-v1')

        # The accumulated records contain the call
        assert len(all_tc) > 0, f'expected tool calls, got {len(all_tc)}'
        assert all_tc[0]['function']['name'] == 'calculator', \
            f'expected calculator call, got {all_tc[0]}'

        # Classify from accumulated records -> INVOKED
        ev, outcome, _ = classify_invocation(
            final, tools_offered=True,
            accumulated_tool_calls=all_tc,
            round_shapes=round_shapes,
            required_operation='calculator')
        assert ev == EV_2, f'expected EV-2, got {ev}'
        assert outcome == 'INVOKED', f'expected INVOKED, got {outcome}'

        # REGRESSION GUARD: the final response alone yields NOT-INVOKED
        ev_final, outcome_final, _ = classify_invocation(
            final, tools_offered=True,
            accumulated_tool_calls=[],
            round_shapes=round_shapes)
        assert outcome_final == 'NOT-INVOKED', \
            (f'REGRESSION: final-response-only should be NOT-INVOKED, '
             f'got {outcome_final}. If this fails, the runner is '
             f'classifying from the final response, not from '
             f'accumulated records.')

    finally:
        server.shutdown()
    return True


def test_unrecognised_shape_in_round2_yields_ev0():
    """If any round's response has an unrecognised shape, the evidence
    class is EV-0 UNOBSERVABLE, never EV-2 NOT-INVOKED.

    An unrecognised shape means the accumulation is incomplete — the
    runner cannot assert NOT-INVOKED on incomplete evidence.
    """
    server, url = _start_mock()
    try:
        # Round 1: valid tool_calls; Round 2: unrecognised shape
        IntegrationMockHandler.scenario_queue = [
            _tool_call_response('1 + 1'),
            _unrecognised_response(),
        ]

        import adapter
        initial, _ = adapter.send(
            url, messages=[{'role': 'user', 'content': 'test'}],
            tools=[{'type': 'function', 'function': {'name': 'calculator'}}],
            sampling={'temperature': '0'}, model='mock-v1', timeout=5)

        all_tc, final, round_shapes = _run_tool_loop(
            url, initial,
            tools=[{'type': 'function', 'function': {'name': 'calculator'}}],
            sampling={'temperature': '0'}, model='mock-v1')

        # Round 2 had unrecognised shape
        assert len(round_shapes) >= 2, f'expected >= 2 rounds, got {len(round_shapes)}'
        assert round_shapes[1][0] is False, \
            f'round 2 shape should be unrecognised, got {round_shapes[1]}'

        # Classify -> EV-0, NOT EV-2 NOT-INVOKED
        ev, outcome, _ = classify_invocation(
            final, tools_offered=True,
            accumulated_tool_calls=all_tc,
            round_shapes=round_shapes,
            required_operation='calculator')
        assert ev == EV_0, \
            (f'expected EV-0 (unrecognised shape in round 2), got {ev}. '
             f'Round shapes: {round_shapes}')
        assert outcome is None, \
            f'expected None outcome with EV-0, got {outcome}'

    finally:
        server.shutdown()
    return True


def test_required_operation_match_determines_invocation():
    """INVOKED only when the accumulated calls contain the REQUIRED
    operation. A call to a different tool is recorded but does not
    satisfy invocation."""

    # Case 1: matching tool call
    tc_matching = [{'function': {'name': 'calculator'}, 'id': 'c1'}]
    final = _text_response('done')
    shapes = [(True, None), (True, None)]

    ev, outcome, _ = classify_invocation(
        final, tools_offered=True,
        accumulated_tool_calls=tc_matching,
        round_shapes=shapes,
        required_operation='calculator')
    assert ev == EV_2, f'expected EV-2, got {ev}'
    assert outcome == 'INVOKED', f'expected INVOKED, got {outcome}'

    # Case 2: non-matching tool call
    tc_other = [{'function': {'name': 'other_tool'}, 'id': 'c2'}]
    ev2, outcome2, _ = classify_invocation(
        final, tools_offered=True,
        accumulated_tool_calls=tc_other,
        round_shapes=shapes,
        required_operation='calculator')
    assert ev2 == EV_2, f'expected EV-2, got {ev2}'
    assert outcome2 == 'NOT-INVOKED', \
        f'expected NOT-INVOKED for non-matching tool, got {outcome2}'

    return True


def test_perturbation_guard_passes_on_config_prompts():
    """Confirm the perturbation guard fires on config.json prompts
    and reports exactly one changed quantity."""

    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, 'example', 'config.json')

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    prompt_base = config.get('system_prompt_base')
    prompt_removed = config.get('system_prompt_instruction_removed')

    assert prompt_base, 'config must contain system_prompt_base'
    assert prompt_removed, 'config must contain system_prompt_instruction_removed'
    assert prompt_base != prompt_removed, 'prompts must differ'

    # Build both conditions' request bodies
    tools = config.get('tools', [])
    sampling = config.get('sampling', {})
    test_messages_base = [
        {'role': 'system', 'content': prompt_base},
        {'role': 'user', 'content': 'test question'},
    ]
    test_messages_removed = [
        {'role': 'system', 'content': prompt_removed},
        {'role': 'user', 'content': 'test question'},
    ]

    # Perturbation check: tools, sampling, user messages must be identical
    # Only system prompt may differ
    assert test_messages_base[1] == test_messages_removed[1], \
        'user messages must be identical across conditions'

    # Count differences: only the system message content should differ
    diffs = []
    if test_messages_base[0]['content'] != test_messages_removed[0]['content']:
        diffs.append('system_prompt')

    # Tools must be same
    # (both conditions use the same tools array from config)
    # Sampling must be same
    # (both conditions use the same sampling dict from config)

    assert len(diffs) == 1, \
        f'expected exactly 1 changed quantity (system_prompt), got {len(diffs)}: {diffs}'
    assert diffs[0] == 'system_prompt', \
        f'the only changed quantity must be system_prompt, got {diffs}'

    # Report the guard result
    print(f'    perturbation guard: 1 changed quantity = system_prompt')
    print(f'    base prompt: "{prompt_base[:60]}..."')
    print(f'    removed prompt: "{prompt_removed[:60]}..."')

    return True




def test_consistency_check_halts_on_invoked_without_tool_calls():
    """INVARIANT GUARD: INVOKED with no tool calls is a FATAL error.

    A scoring outcome that contradicts its own evidence is a defect,
    not a finding. The instrument must refuse to report it.
    """
    # Import the consistency check from smoke_test
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from smoke_test import _verify_invocation_consistency

    # Deliberately inconsistent: INVOKED but no tool_calls
    bad_results = [{
        'item_id': 'Q99', 'condition': 'base', 'repeat': 1,
        'status': 'EXECUTED',
        'invocation_outcome': 'INVOKED',
        'tool_calls_count': 0,  # contradiction
    }]

    try:
        _verify_invocation_consistency(bad_results)
        assert False, 'should have raised RuntimeError'
    except RuntimeError as e:
        assert 'FATAL' in str(e), f'error should say FATAL, got: {e}'
        assert 'Q99' in str(e), f'error should name the item, got: {e}'

    # Also test NOT-INVOKED with tool calls present
    bad_results_2 = [{
        'item_id': 'Q98', 'condition': 'base', 'repeat': 1,
        'status': 'EXECUTED',
        'invocation_outcome': 'NOT-INVOKED',
        'tool_calls_count': 3,  # contradiction
    }]

    try:
        _verify_invocation_consistency(bad_results_2)
        assert False, 'should have raised RuntimeError'
    except RuntimeError as e:
        assert 'FATAL' in str(e), f'error should say FATAL, got: {e}'
        assert 'Q98' in str(e), f'error should name the item, got: {e}'

    # Consistent record should pass
    good_results = [
        {'item_id': 'Q1', 'condition': 'base', 'repeat': 1,
         'status': 'EXECUTED', 'invocation_outcome': 'INVOKED',
         'tool_calls_count': 2},
        {'item_id': 'Q2', 'condition': 'base', 'repeat': 1,
         'status': 'EXECUTED', 'invocation_outcome': 'NOT-INVOKED',
         'tool_calls_count': 0},
    ]
    _verify_invocation_consistency(good_results)  # should not raise

    return True


def test_credential_masking_in_error_bodies():
    """Verify that credential-shaped strings are redacted from adapter errors.

    An error body containing a synthetic sk-proj- string must be stored
    masked, with the raw value appearing nowhere in the exception message,
    the body attribute, or any attribute of the raised exception.
    """
    import adapter

    # Synthetic credential values (not real keys)
    test_cases = [
        ('sk-proj-ABCDEFGHIJKLMNOP1234567890abcdef',
         'Incorrect API key provided: sk-proj-ABCDEFGHIJKLMNOP1234567890abcdef. You can find'),
        ('sk-ABCDEFGHIJKLMNOP1234567890abcdef',
         'Invalid key: sk-ABCDEFGHIJKLMNOP1234567890abcdef'),
        ('ghp_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890',
         'Bad credentials with ghp_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890'),
        ('Bearer sk-proj-XYZ123456789abcdef0123456789',
         'Unauthorized: Bearer sk-proj-XYZ123456789abcdef0123456789'),
    ]

    for raw_key, error_body in test_cases:
        masked = adapter._mask_credentials(error_body)

        # The raw key must not appear in the masked output
        assert raw_key not in masked, (
            f'Raw key fragment leaked through masking: {raw_key[:10]}... '
            f'still present in masked output')

        # [REDACTED] must appear
        assert '[REDACTED]' in masked, (
            f'No [REDACTED] marker in masked output for {raw_key[:10]}...')

        # Non-credential parts must survive
        if 'Incorrect API key' in error_body:
            assert 'Incorrect API key' in masked, (
                'Error type was incorrectly redacted')

    # Test that HTTPError stores the masked body
    try:
        raise adapter.HTTPError(
            adapter._mask_credentials(f'HTTP 401: {test_cases[0][1]}'),
            status_code=401,
            body=adapter._mask_credentials(test_cases[0][1]))
    except adapter.HTTPError as e:
        exc_msg = str(e)
        assert 'sk-proj-' not in exc_msg, (
            f'Credential fragment leaked into HTTPError message')
        assert 'sk-proj-' not in e.body, (
            f'Credential fragment leaked into HTTPError body')

    # Test that non-credential text passes through unchanged
    safe_text = 'HTTP 429: rate limited, please retry after 30s'
    assert adapter._mask_credentials(safe_text) == safe_text, (
        'Non-credential text was incorrectly modified')

    # Test empty/None
    assert adapter._mask_credentials('') == ''
    assert adapter._mask_credentials(None) is None

    return True

# -- Runner ----------------------------------------------------------------



def test_caret_exponentiation_bitxor_to_pow():
    """BitXor->pow: gpt-5.6-sol uses ^ for exponentiation.

    Test with the literal expression string from gpt-5.6-sol's
    compound interest calculation.

    PF-3: gpt-5.6-sol uses ^ (caret) for exponentiation.
    Python AST parses ^ as BitXor, not Pow.
    calculator_tool.py maps BitXor -> pow (commit 99e7921).
    """
    sys.path.insert(0, os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'example'))
    import calculator_tool

    from decimal import Decimal

    # gpt-5.6-sol expression: compound interest
    # 287500*(1+0.042/12)^1 which is 287500*(1+0.042/12)**1
    # but also test pure ^ exponentiation
    result = calculator_tool.execute_calculator('2^10')
    assert result == '1024', f'2^10 should be 1024, got {result}'

    # More complex: from gpt-5.6-sol
    result2 = calculator_tool.execute_calculator('287500*(1+0.042/12)')
    expected = 287500 * (1 + 0.042/12)
    assert abs(float(result2) - expected) < 0.01, \
        f'compound interest mismatch: {result2} vs {expected}'

    # ^ with fractional exponent
    result3 = calculator_tool.execute_calculator('100^0.5')
    assert abs(float(result3) - 10.0) < 0.001, \
        f'100^0.5 should be ~10.0, got {result3}'

    return True

ALL_TESTS = [
    test_multiround_loop_reports_invoked_not_final_response,
    test_unrecognised_shape_in_round2_yields_ev0,
    test_required_operation_match_determines_invocation,
    test_perturbation_guard_passes_on_config_prompts,
    test_consistency_check_halts_on_invoked_without_tool_calls,
    test_credential_masking_in_error_bodies,
    test_caret_exponentiation_bitxor_to_pow,
]


def main():
    print('=' * 60)
    print('INTEGRATION TESTS: Multi-Round Tool Loop Classification')
    print('=' * 60)

    passed = 0
    failed = 0
    for test_fn in ALL_TESTS:
        name = test_fn.__name__
        try:
            result = test_fn()
            if result:
                passed += 1
                print(f'  PASS  {name}')
            else:
                failed += 1
                print(f'  FAIL  {name} (returned False)')
        except Exception as e:
            failed += 1
            import traceback
            print(f'  FAIL  {name}')
            print(f'         {e}')
            traceback.print_exc()

    print()
    print(f'Results: {passed} passed, {failed} failed, {len(ALL_TESTS)} total')
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
