"""R1.2 -- Execution Engine.

Spec: AP-1 Runner Build Spec v0.3, section 4 R1.2.

Iterate items and conditions; call R0.2; drive the tool loop;
write to R0.3. PERFORM NO SCORING.

Conditions in v1.0: 'base' and 'instruction_removed' (D7.1b).

Perturbation discipline (normative, AP-1 §4.7.1):
  The 'instruction_removed' condition alters the system prompt
  AND NOTHING ELSE. Tool declarations, tool availability, fixture
  content, sampling parameters and message structure are held
  constant. A run in which more than one quantity differs is
  REFUSED (not reported), with the diff emitted.

Item selection (normative):
  An item is eligible for invocation measurement only where
  invocation is correct behaviour. An item declared underivable
  is VOID for that arm and excluded from every invocation denominator.
"""

import json
from decimal import Decimal

from evidence import (
    classify_invocation, classify_attestation,
    check_ev3_guard, EV_0,
)


class EngineError(Exception):
    """Execution engine failure."""


class PerturbationRefusal(EngineError):
    """More than one quantity differs between conditions."""


# -- Condition definitions -------------------------------------------

CONDITION_BASE = 'base'
CONDITION_INSTRUCTION_REMOVED = 'instruction_removed'
VALID_CONDITIONS = {CONDITION_BASE, CONDITION_INSTRUCTION_REMOVED}


# -- Single-variable perturbation check ------------------------------

def check_single_variable_perturbation(base_config, removed_config):
    """Verify that instruction_removed differs from base in exactly
    one quantity: the system prompt.

    Compares: system_prompt, tools, tool_choice, sampling parameters,
    fixture content, message structure template.

    Returns: list of differences found.
    Raises: PerturbationRefusal if more than one quantity differs,
            with the diff naming every changed quantity.
    """
    diffs = []

    # Compare system prompts — this SHOULD differ
    if base_config.get('system_prompt') == removed_config.get('system_prompt'):
        diffs.append({
            'field': 'system_prompt',
            'issue': 'system prompts are IDENTICAL — instruction_removed '
                     'must alter the system prompt',
        })

    # Compare tool declarations — these MUST NOT differ
    base_tools = base_config.get('tools')
    removed_tools = removed_config.get('tools')
    if _canonical(base_tools) != _canonical(removed_tools):
        diffs.append({
            'field': 'tools',
            'issue': 'tool declarations differ between conditions',
            'base': _summarise(base_tools),
            'removed': _summarise(removed_tools),
        })

    # Compare tool_choice — MUST NOT differ
    if base_config.get('tool_choice') != removed_config.get('tool_choice'):
        diffs.append({
            'field': 'tool_choice',
            'issue': 'tool_choice differs between conditions',
            'base': base_config.get('tool_choice'),
            'removed': removed_config.get('tool_choice'),
        })

    # Compare sampling parameters — MUST NOT differ
    base_sampling = base_config.get('sampling', {})
    removed_sampling = removed_config.get('sampling', {})
    if _canonical(base_sampling) != _canonical(removed_sampling):
        diffs.append({
            'field': 'sampling',
            'issue': 'sampling parameters differ between conditions',
            'base': base_sampling,
            'removed': removed_sampling,
        })

    # Compare fixture content — MUST NOT differ
    if base_config.get('fixture_hash') != removed_config.get('fixture_hash'):
        diffs.append({
            'field': 'fixture_content',
            'issue': 'fixture content differs between conditions',
        })

    # Compare message template structure — MUST NOT differ
    base_template = base_config.get('message_template')
    removed_template = removed_config.get('message_template')
    if _canonical(base_template) != _canonical(removed_template):
        diffs.append({
            'field': 'message_template',
            'issue': 'message structure template differs between conditions',
        })

    # Count non-system-prompt diffs
    non_prompt_diffs = [d for d in diffs if d['field'] != 'system_prompt']

    if non_prompt_diffs:
        raise PerturbationRefusal(
            f'instruction_removed condition changes '
            f'{len(non_prompt_diffs) + 1} quantities (must be exactly 1: '
            f'system_prompt). Changed quantities:\n'
            + '\n'.join(
                f'  - {d["field"]}: {d["issue"]}'
                for d in [{'field': 'system_prompt',
                           'issue': 'expected (this is the one allowed)'}]
                + non_prompt_diffs
            )
        )

    return diffs


# -- Context builder -------------------------------------------------

def build_delivered_context(fixture, source_accounts):
    """Build the context delivered to the ground-truth module.

    Only accounts listed in source_accounts are included.
    The ground-truth module never sees the full fixture.

    Returns: dict keyed by account id, each value a dict of
    field_name -> string_value (excluding 'id' and 'name').
    """
    accounts_by_id = {a['id']: a for a in fixture['accounts']}
    ctx = {}
    for acct_id in source_accounts:
        if acct_id not in accounts_by_id:
            raise EngineError(
                f'source_account {acct_id!r} not found in fixture '
                f'(available: {sorted(accounts_by_id)})')
        acct = accounts_by_id[acct_id]
        ctx[acct_id] = {
            k: v for k, v in acct.items() if k not in ('id', 'name')
        }
    return ctx


# -- Lookup collision check ------------------------------------------

def check_lookup_collision(final_value, delivered_context):
    """Check if the expected final value appears verbatim in the
    delivered context.

    R3.1: lookup_collision is computed by the runner at seal time,
    not declared by the operator.

    Returns: (collision_found, colliding_field_or_None)
    """
    for acct_id, acct_data in delivered_context.items():
        for field_name, field_value in acct_data.items():
            try:
                if Decimal(str(field_value)) == final_value:
                    return True, f'{acct_id}.{field_name}'
            except Exception:
                continue
    return False, None


# -- Item execution --------------------------------------------------

def execute_item(item, *, condition, config, fixture,
                 ground_truth_compute, adapter_send,
                 system_prompt, tools, transcript_path,
                 seal_hash):
    """Execute one item under one condition.

    This is the core loop per R1.2: send to model, drive tool loop,
    capture evidence, write transcript. NO SCORING.

    Args:
        item: Question dict from questions.json.
        condition: 'base' or 'instruction_removed'.
        config: Resolved configuration dict.
        fixture: Full fixture dict.
        ground_truth_compute: Callable(item_id, ctx) -> ground_truth.
        adapter_send: Callable matching adapter.send signature.
        system_prompt: The system prompt for this condition.
        tools: Tool definitions for the endpoint.
        transcript_path: Path to the transcript JSONL.
        seal_hash: The seal hash for this run.

    Returns:
        dict with execution results (not scores).
    """
    import transcript

    item_id = item['id']
    source_accounts = item['source_accounts']

    # Build delivered context
    ctx = build_delivered_context(fixture, source_accounts)

    # Compute ground truth
    gt = ground_truth_compute(item_id, ctx)

    # Check if item is derivable
    if not gt.get('derivable', True):
        # VOID: item is underivable, excluded from denominators
        transcript.append(
            transcript_path,
            item_id=item_id,
            arm_id=condition,
            condition=condition,
            request_sent=None,
            response_received=None,
            tool_calls=[],
            evidence_class=None,
            error_state='VOID',
            seal_hash=seal_hash,
            void_reason='underivable',
        )
        return {
            'item_id': item_id,
            'condition': condition,
            'status': 'VOID',
            'reason': 'underivable',
            'ground_truth': gt,
        }

    # Build the request messages
    messages = _build_messages(
        system_prompt=system_prompt,
        item=item,
        fixture=fixture,
        config=config,
    )

    # Determine sampling parameters
    sampling = config.get('sampling', {})

    # Send to endpoint via adapter
    try:
        response, attempts = adapter_send(
            config['endpoint_url'],
            messages=messages,
            tools=tools,
            sampling=sampling,
            model=config.get('model'),
        )
    except Exception as e:
        # Transport failure — record as UNMEASURED
        transcript.append(
            transcript_path,
            item_id=item_id,
            arm_id=condition,
            condition=condition,
            request_sent={'messages': messages},
            response_received=None,
            tool_calls=[],
            evidence_class=EV_0,
            error_state=f'TRANSPORT_FAILURE: {e}',
            seal_hash=seal_hash,
        )
        return {
            'item_id': item_id,
            'condition': condition,
            'status': 'UNMEASURED',
            'error': str(e),
            'ground_truth': gt,
        }

    # Drive tool loop
    tool_calls_record, final_response = _drive_tool_loop(
        response=response,
        messages=messages,
        config=config,
        tools=tools,
        adapter_send=adapter_send,
        sampling=sampling,
    )

    # Classify evidence
    evidence_class, evidence_reason = classify_invocation(
        final_response, tool_calls_record)

    # EV-3 guard — MUST NOT emit EV-3 in v1.0
    check_ev3_guard(evidence_class)

    # Check for attestations in the response and classify
    attestation = _extract_attestation(final_response)
    if attestation:
        att_class, att_reason = classify_attestation(
            attestation, {'ev3_implemented': False})
        # Attestation evidence replaces only if it would be higher,
        # but in v1.0 attestations are always EV-1
        evidence_reason += f'; attestation present: {att_reason}'

    # Write transcript
    transcript.append(
        transcript_path,
        item_id=item_id,
        arm_id=condition,
        condition=condition,
        request_sent={'messages': messages},
        response_received=final_response,
        tool_calls=tool_calls_record,
        evidence_class=evidence_class,
        error_state=None,
        seal_hash=seal_hash,
        evidence_reason=evidence_reason,
        ground_truth_final=str(gt['final']),
        required_operation=gt['required_operation'],
    )

    return {
        'item_id': item_id,
        'condition': condition,
        'status': 'EXECUTED',
        'evidence_class': evidence_class,
        'evidence_reason': evidence_reason,
        'tool_calls': tool_calls_record,
        'response': final_response,
        'ground_truth': gt,
    }


# -- Tool loop -------------------------------------------------------

def _drive_tool_loop(*, response, messages, config, tools,
                     adapter_send, sampling, max_turns=10):
    """Drive the tool-call cycle until the model stops requesting tools.

    All tool calls are recorded. Returns (tool_calls_record, final_response).
    """
    all_tool_calls = []
    current_response = response
    turn = 0

    while turn < max_turns:
        # Extract tool calls from response
        model_tool_calls = _extract_tool_calls(current_response)
        if not model_tool_calls:
            break  # No more tool calls, done

        turn += 1

        # Record each tool call
        for tc in model_tool_calls:
            call_record = {
                'turn': turn,
                'id': tc.get('id', f'call_{turn}'),
                'type': tc.get('type', 'function'),
                'function': tc.get('function', {}),
            }
            all_tool_calls.append(call_record)

        # Append the assistant's response to messages
        messages.append(current_response.get('choices', [{}])[0]
                        .get('message', {}))

        # Execute tool calls and append results
        for tc in model_tool_calls:
            func = tc.get('function', {})
            tool_result = _execute_tool(
                func.get('name', ''), func.get('arguments', '{}'))
            messages.append({
                'role': 'tool',
                'tool_call_id': tc.get('id', ''),
                'content': str(tool_result),
            })

        # Send the continuation
        try:
            current_response, _ = adapter_send(
                config['endpoint_url'],
                messages=messages,
                tools=tools,
                sampling=sampling,
                model=config.get('model'),
            )
        except Exception:
            break

    return all_tool_calls, current_response


def _execute_tool(name, arguments_json):
    """Execute a tool call. Placeholder — operators supply their own.

    In the reference implementation, this dispatches to the calculator
    tool from example/calculator_tool.py.
    """
    try:
        import calculator_tool
        if name == 'calculator':
            args = json.loads(arguments_json)
            expr = args.get('expression', arguments_json)
            result = calculator_tool.execute_calculator(expr)
            return json.dumps({'result': result})
    except Exception as e:
        return json.dumps({'error': str(e)})

    return json.dumps({'error': f'unknown tool: {name}'})


# -- Helpers ---------------------------------------------------------

def _build_messages(*, system_prompt, item, fixture, config):
    """Build the message array for one request."""
    messages = []

    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})

    # User message with the question and context
    context_text = _format_fixture_context(fixture, item)
    user_content = f'{context_text}\n\nQuestion: {item["text"]}'
    messages.append({'role': 'user', 'content': user_content})

    return messages


def _format_fixture_context(fixture, item):
    """Format the fixture context for the user message."""
    source_accounts = item.get('source_accounts', [])
    accounts = {a['id']: a for a in fixture['accounts']}

    lines = ['Here is the financial information:']
    for acct_id in source_accounts:
        if acct_id in accounts:
            acct = accounts[acct_id]
            lines.append(f'\n{acct.get("name", acct_id)}:')
            for k, v in acct.items():
                if k not in ('id', 'name'):
                    label = k.replace('_', ' ').title()
                    lines.append(f'  {label}: {v}')

    return '\n'.join(lines)


def _extract_tool_calls(response):
    """Extract tool_calls from an OpenAI-compatible response."""
    if not isinstance(response, dict):
        return []
    choices = response.get('choices', [])
    if not choices:
        return []
    message = choices[0].get('message', {})
    return message.get('tool_calls', [])


def _extract_attestation(response):
    """Extract an attestation from the response, if present."""
    if not isinstance(response, dict):
        return None
    choices = response.get('choices', [])
    if not choices:
        return None
    message = choices[0].get('message', {})

    # Check for attestation in metadata or content
    metadata = message.get('metadata', {})
    if metadata and 'attestation' in metadata:
        return metadata['attestation']

    # Check for attestation in tool results
    content = message.get('content', '')
    if content and 'attestation' in str(content).lower():
        return {'raw_claim': content, 'type': 'self_reported'}

    return None


def _canonical(obj):
    """Canonical JSON for comparison."""
    if obj is None:
        return 'null'
    return json.dumps(obj, sort_keys=True, default=str)


def _summarise(obj):
    """Short summary of an object for diff messages."""
    s = json.dumps(obj, sort_keys=True, default=str)
    return s[:200] + '...' if len(s) > 200 else s
