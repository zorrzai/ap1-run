"""R1.2 -- Execution Engine.

Spec: AP-1 Runner Build Spec v0.3, section 4 R1.2.

Iterate items and conditions; call R0.2; drive the tool loop;
write to R0.3. PERFORM NO SCORING.

Conditions in v1.0: 'base' and 'instruction_removed' (D7.1b).

Item selection (normative):
  An item declared underivable is VOID for that arm and excluded
  from every invocation denominator.
"""

import json

import transcript
from context import build_delivered_context, format_fixture_context
from evidence import (
    classify_invocation, classify_attestation,
    extract_attestation, check_ev3_guard, EV_0,
)
from operation_correctness import classify_operation
from provenance_classify import classify_invocations_sequential


class EngineError(Exception):
    """Execution engine failure."""


CONDITION_BASE = 'base'
CONDITION_INSTRUCTION_REMOVED = 'instruction_removed'
VALID_CONDITIONS = {CONDITION_BASE, CONDITION_INSTRUCTION_REMOVED}


# -- Item execution --------------------------------------------------

def execute_item(item, *, condition, config, fixture,
                 ground_truth_compute, adapter_send,
                 system_prompt, tools, transcript_path,
                 seal_hash):
    """Execute one item under one condition.

    Core loop per R1.2: send to model, drive tool loop, capture
    evidence, write transcript. NO SCORING.
    """
    item_id = item['id']
    ctx = build_delivered_context(fixture, item['source_accounts'])
    gt = ground_truth_compute(item_id, ctx)

    # Underivable -> VOID, excluded from denominators
    if not gt.get('derivable', True):
        transcript.append(
            transcript_path,
            item_id=item_id, arm_id=condition,
            condition=condition, request_sent=None,
            response_received=None, tool_calls=[],
            evidence_class=None, error_state='VOID',
            seal_hash=seal_hash, void_reason='underivable',
        )
        return {
            'item_id': item_id, 'condition': condition,
            'status': 'VOID', 'reason': 'underivable',
            'ground_truth': gt,
        }

    messages = _build_messages(
        system_prompt=system_prompt, item=item,
        fixture=fixture, config=config,
    )
    sampling = config.get('sampling', {})
    tools_offered = tools is not None and len(tools) > 0

    # Send to endpoint via adapter
    try:
        response, attempts = adapter_send(
            config['endpoint_url'], messages=messages,
            tools=tools, sampling=sampling,
            model=config.get('model'),
        )
    except Exception as e:
        transcript.append(
            transcript_path,
            item_id=item_id, arm_id=condition,
            condition=condition,
            request_sent={'messages': messages},
            response_received=None, tool_calls=[],
            evidence_class=EV_0,
            error_state=f'TRANSPORT_FAILURE: {e}',
            seal_hash=seal_hash,
        )
        return {
            'item_id': item_id, 'condition': condition,
            'status': 'UNMEASURED', 'error': str(e),
            'ground_truth': gt,
        }

    # Drive tool loop
    tool_calls_record, final_response, round_shapes = _drive_tool_loop(
        response=response, messages=messages, config=config,
        tools=tools, adapter_send=adapter_send,
        sampling=sampling,
    )

    # Classify evidence from ACCUMULATED records (R1.3 normative)
    ev_class, outcome, self_report = classify_invocation(
        final_response, tools_offered=tools_offered,
        accumulated_tool_calls=tool_calls_record,
        round_shapes=round_shapes,
        required_operation=gt.get('required_operation'))
    check_ev3_guard(ev_class)

    # Check for attestation
    attestation = extract_attestation(final_response)
    att_reason = None
    if attestation:
        _, att_reason = classify_attestation(
            attestation, {'ev3_implemented': False})

    # D7.2(a): sequential operand provenance (D22 transitivity guard)
    provenance_results = classify_invocations_sequential(
        tool_calls_record, ctx, gt, config)

    # D7.2(b): evaluate operation correctness for each tool call
    op_correctness_results = []
    for tc in tool_calls_record:
        expr = _extract_calc_expression(tc)
        if expr is not None:
            try:
                oc = classify_operation(expr, gt, config)
                op_correctness_results.append(oc)
            except Exception as e:
                op_correctness_results.append({
                    'outcome': 'OPERATION-UNOBSERVABLE',
                    'reason': f'evaluation failed: '
                              f'{type(e).__name__}: {e}',
                })

    # Write transcript
    transcript.append(
        transcript_path,
        item_id=item_id, arm_id=condition,
        condition=condition,
        request_sent={'messages': messages},
        response_received=final_response,
        tool_calls=tool_calls_record,
        evidence_class=ev_class,
        error_state=None, seal_hash=seal_hash,
        invocation_outcome=outcome,
        self_report=self_report,
        attestation_reason=att_reason,
        ground_truth_final=str(gt['final']),
        required_operation=gt['required_operation'],
        operation_correctness=op_correctness_results,
        provenance_results=provenance_results,
    )

    return {
        'item_id': item_id, 'condition': condition,
        'status': 'EXECUTED', 'evidence_class': ev_class,
        'invocation_outcome': outcome,
        'self_report': self_report,
        'tool_calls': tool_calls_record,
        'response': final_response, 'ground_truth': gt,
        'provenance_results': provenance_results,
    }


# -- Tool loop -------------------------------------------------------

def _drive_tool_loop(*, response, messages, config, tools,
                     adapter_send, sampling, max_turns=10):
    """Drive the tool-call cycle.

    Returns (tool_calls, final_response, round_shapes).
    round_shapes: list of (shape_recognised, reason) per round.
    """
    all_tool_calls = []
    round_shapes = []
    current = response

    # Check shape of the initial response (round 0)
    _record_shape(current, round_shapes)

    for turn in range(1, max_turns + 1):
        model_calls = _extract_tool_calls(current)
        if not model_calls:
            break

        for tc in model_calls:
            all_tool_calls.append({
                'turn': turn,
                'id': tc.get('id', f'call_{turn}'),
                'type': tc.get('type', 'function'),
                'function': tc.get('function', {}),
            })

        messages.append(
            current.get('choices', [{}])[0].get('message', {}))

        for tc in model_calls:
            func = tc.get('function', {})
            result = _execute_tool(
                func.get('name', ''), func.get('arguments', '{}'))
            messages.append({
                'role': 'tool',
                'tool_call_id': tc.get('id', ''),
                'content': str(result),
            })
            # D7.2(a)(iv): attach return value by tool_call_id
            tc_id = tc.get('id', '')
            matched = [r for r in all_tool_calls if r['id'] == tc_id]
            if not matched:
                raise EngineError(
                    f'tool_call_id {tc_id!r} not found in all_tool_calls; '
                    f'cannot attach return_value')
            matched[0]['return_value'] = result

        try:
            current, _ = adapter_send(
                config['endpoint_url'], messages=messages,
                tools=tools, sampling=sampling,
                model=config.get('model'),
            )
            # Check shape of this round's response
            _record_shape(current, round_shapes)
        except Exception as exc:
            # D7.9 normative: any round that fails to complete is
            # recorded as unrecognised. The evidence class is EV-0,
            # never a definitive invocation finding.
            round_shapes.append(
                (False, f'adapter_send failed on turn {turn}: {exc}'))
            break

    return all_tool_calls, current, round_shapes

def _execute_tool(name, arguments_json):
    """Execute a tool call. Operators supply their own dispatch."""
    try:
        import calculator_tool
        if name == 'calculator':
            args = json.loads(arguments_json)
            return json.dumps({
                'result': calculator_tool.execute_calculator(
                    args.get('expression', arguments_json))
            })
    except Exception as e:
        return json.dumps({'error': str(e)})
    return json.dumps({'error': f'unknown tool: {name}'})



def _record_shape(response, round_shapes):
    """Record the response shape for evidence classification."""
    from evidence import _extract_model_tool_calls
    _, recognised, reason = _extract_model_tool_calls(response)
    round_shapes.append((recognised, reason))


# -- Expression extraction -------------------------------------------

def _extract_calc_expression(tool_call_record):
    """Extract calculator expression from a tool-call record.

    Returns the expression string, or None if not a calculator call.
    """
    func = tool_call_record.get('function', {})
    if func.get('name') != 'calculator':
        return None
    try:
        args = json.loads(func.get('arguments', '{}'))
        return args.get('expression')
    except (json.JSONDecodeError, TypeError):
        return None


# -- Helpers ---------------------------------------------------------

def _build_messages(*, system_prompt, item, fixture, config):
    """Build the message array for one request."""
    messages = []
    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})
    context_text = format_fixture_context(fixture, item)
    messages.append({
        'role': 'user',
        'content': f'{context_text}\n\nQuestion: {item["text"]}',
    })
    return messages


def _extract_tool_calls(response):
    """Extract tool_calls from an OpenAI-compatible response."""
    if not isinstance(response, dict):
        return []
    choices = response.get('choices', [])
    if not choices:
        return []
    return choices[0].get('message', {}).get('tool_calls') or []
