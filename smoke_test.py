"""Smoke test runner for the AP-1 instrument.

THIS IS AN INSTRUMENT SMOKE TEST, NOT AN AP-1 EVALUATION.
Not conformant: R2.4 not built, no adjudication, no second scorer,
toy fixture. Must never be reported, cited or described as an AP-1
result. Output goes to ap1-runner/output/ which is gitignored.

Usage:
    export AP1_SMOKE_API_KEY=<key>    (Linux/macOS)
    set AP1_SMOKE_API_KEY=<key>       (Windows cmd)
    $env:AP1_SMOKE_API_KEY = '<key>'  (Windows PowerShell)

    Optional:
    export AP1_SMOKE_ENDPOINT=<url>   (default: https://api.openai.com/v1/chat/completions)
    export AP1_SMOKE_MODEL=<model>    (default: gpt-4o-mini)
    python smoke_test.py

On Windows only, if AP1_SMOKE_API_KEY is not set, the runner will attempt
to read from Windows Credential Manager (target: ap1-smoke:openai).
"""

import json
import os
import sys
import time
from decimal import Decimal
from pathlib import Path

DISCLAIMER = (
    'THIS IS AN INSTRUMENT SMOKE TEST, NOT AN AP-1 EVALUATION.\n'
    '\n'
    'It is not conformant: R2.4 is not built, there is no adjudication, no\n'
    'second scorer, no blind set, and the fixture is the shipped toy example.\n'
    'No figure from it may be reported, cited, quoted or described as an AP-1\n'
    'result, by us or by anyone, in any document.\n'
)

# Runner modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import adapter
from config import load_config
from context import build_delivered_context, check_lookup_collision, format_fixture_context
from evidence import classify_invocation, check_ev3_guard, EV_0, EV_2
from figure_id import identify_figure, AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE
from invocation import format_rate
from numeric import extract_numeric_tokens
import transcript




# Credential target for the API key
_CRED_TARGET = 'ap1-smoke:openai'


def _read_credential_windows(target):
    """Read a credential from Windows Credential Manager via ctypes.

    Only called on Windows when AP1_SMOKE_API_KEY is not set.
    Returns the credential blob as a string, or None if not found.
    """
    try:
        import ctypes
        import ctypes.wintypes
    except ImportError:
        return None

    CRED_TYPE_GENERIC = 1

    class CREDENTIAL(ctypes.Structure):
        _fields_ = [
            ("Flags", ctypes.wintypes.DWORD),
            ("Type", ctypes.wintypes.DWORD),
            ("TargetName", ctypes.c_wchar_p),
            ("Comment", ctypes.c_wchar_p),
            ("LastWritten", ctypes.wintypes.FILETIME),
            ("CredentialBlobSize", ctypes.wintypes.DWORD),
            ("CredentialBlob", ctypes.c_void_p),
            ("Persist", ctypes.wintypes.DWORD),
            ("AttributeCount", ctypes.wintypes.DWORD),
            ("Attributes", ctypes.c_void_p),
            ("TargetAlias", ctypes.c_wchar_p),
            ("UserName", ctypes.c_wchar_p),
        ]

    pcred = ctypes.POINTER(CREDENTIAL)()
    ok = ctypes.windll.advapi32.CredReadW(
        target, CRED_TYPE_GENERIC, 0, ctypes.byref(pcred))

    if not ok:
        return None

    blob = ctypes.string_at(
        pcred.contents.CredentialBlob, pcred.contents.CredentialBlobSize)
    # Decode UTF-16LE (Windows credential store encoding)
    value = blob.decode('utf-16-le').rstrip('\x00')
    ctypes.windll.advapi32.CredFree(pcred)
    return value


def _get_api_key():
    """Resolve the API key. Never prints, logs, or writes the value.

    Priority:
      1. AP1_SMOKE_API_KEY environment variable (all platforms)
      2. Windows Credential Manager (Windows only, target: ap1-smoke:openai)

    Raises SystemExit with platform-appropriate setup instructions if
    neither source provides a key.
    """
    key = os.environ.get('AP1_SMOKE_API_KEY')
    if key:
        return key

    # Windows-only fallback: Credential Manager
    if sys.platform == 'win32':
        key = _read_credential_windows(_CRED_TARGET)
        if key:
            return key

    # Neither source provided a key -- error with setup instructions
    print('ERROR: API key not found.')
    print()
    print('Set the AP1_SMOKE_API_KEY environment variable:')
    print()
    if sys.platform == 'win32':
        print('  cmd:         set AP1_SMOKE_API_KEY=<key>')
        print('  PowerShell:  $env:AP1_SMOKE_API_KEY = \'<key>\'')
        print()
        print('Or store in Windows Credential Manager:')
        print(f'  Target: {_CRED_TARGET}')
        print('  User name: ap1-smoke')
        print('  Password: <the API key>')
    else:
        print('  export AP1_SMOKE_API_KEY=<key>')
    print()
    print('The key is never printed, logged, or written to any file.')
    sys.exit(1)


def _verify_invocation_consistency(results):
    """INVARIANT: INVOKED implies tool_calls present; NOT-INVOKED implies none.

    A scoring outcome that contradicts its own evidence is not a finding,
    it is a defect. The instrument must refuse to report it.

    Raises RuntimeError (FATAL) on the first mismatch, naming the item.
    """
    for r in results:
        if r.get('status') != 'EXECUTED':
            continue
        outcome = r.get('invocation_outcome', '')
        tc_count = r.get('tool_calls_count', 0)
        item_id = r.get('item_id', '?')
        condition = r.get('condition', '?')
        repeat = r.get('repeat', '?')

        if outcome == 'INVOKED' and tc_count == 0:
            raise RuntimeError(
                f'FATAL: invocation consistency check failed. '
                f'{item_id}/{condition}/r{repeat}: '
                f'INVOKED but tool_calls_count=0. '
                f'A scoring outcome that contradicts its own evidence '
                f'is a defect, not a finding.')

        if outcome == 'NOT-INVOKED' and tc_count > 0:
            raise RuntimeError(
                f'FATAL: invocation consistency check failed. '
                f'{item_id}/{condition}/r{repeat}: '
                f'NOT-INVOKED but tool_calls_count={tc_count}. '
                f'A scoring outcome that contradicts its own evidence '
                f'is a defect, not a finding.')


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    # -- Read API key (Rule 0c) --
    # The key is NEVER printed, echoed, logged, or written to any file.
    api_key = _get_api_key()
    key_length = len(api_key)

    # Endpoint and model are not secrets -- read from env or defaults
    endpoint = os.environ.get('AP1_SMOKE_ENDPOINT',
                              'https://api.openai.com/v1/chat/completions')
    model = os.environ.get('AP1_SMOKE_MODEL', 'gpt-4o-mini')

    print(f'Endpoint: {endpoint}')
    print(f'Model: {model}')
    print(f'API key: present ({key_length} chars)')
    print()

    # -- Load example configuration --
    base_dir = os.path.dirname(os.path.abspath(__file__))
    example_dir = os.path.join(base_dir, 'example')

    with open(os.path.join(example_dir, 'config.json'), 'r', encoding='utf-8') as f:
        config = json.load(f)

    config['endpoint_url'] = endpoint
    config['model'] = model

    with open(os.path.join(example_dir, 'fixture.json'), 'r', encoding='utf-8') as f:
        fixture = json.load(f)

    with open(os.path.join(example_dir, 'questions.json'), 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # -- Load ground-truth module --
    sys.path.insert(0, example_dir)
    import ground_truth_example as gt_module

    # -- Output directory --
    output_dir = os.path.join(base_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    transcript_path = os.path.join(output_dir, 'smoke_run.jsonl')

    # Remove old transcript if present
    if os.path.exists(transcript_path):
        os.remove(transcript_path)

    # -- Tool definitions (R1.3: operator-declared, not runner-authored) --
    tools = config.get('tools')
    if not tools:
        print('ERROR: config.json must contain a "tools" array')
        return 1

    # -- System prompts (from config) --
    system_prompt_base = config.get('system_prompt_base')
    system_prompt_removed = config.get('system_prompt_instruction_removed')
    if not system_prompt_base or not system_prompt_removed:
        print('ERROR: config.json must contain system_prompt_base '
              'and system_prompt_instruction_removed')
        return 1

    # -- Run configuration --
    repeat_count = 3  # D2: 3 repeats per condition
    conditions = ['base', 'instruction_removed']
    items = questions['items']

    sampling = config.get('sampling', {})
    answer_tolerance = Decimal(config.get('answer_tolerance', '0.01'))
    decline_markers = config.get('decline_markers', [])
    currency_symbols = config.get('currency_symbols', [])

    # -- Adapter wrapper (binds api_key) --
    def adapter_send(endpoint_url, *, messages, tools=None,
                     sampling=None, model=None, timeout=120):
        return adapter.send(
            endpoint_url, messages=messages, tools=tools,
            sampling=sampling, model=model, api_key=api_key,
            timeout=timeout)

    # -- Calculator tool execution --
    import calculator_tool

    def execute_tool(name, arguments_json):
        if name == 'calculator':
            try:
                args = json.loads(arguments_json)
                expr = args.get('expression', arguments_json)
                result = calculator_tool.execute_calculator(expr)
                return json.dumps({'result': result})
            except (calculator_tool.CalculatorError, json.JSONDecodeError,
                    ValueError, ZeroDivisionError) as e:
                return json.dumps({'error': f'calculator error: {e}'})
        return json.dumps({'error': f'unknown tool: {name}'})

    # -- Collector for all findings --
    all_results = []
    grammar_issues = []
    decline_findings = []
    tool_call_structures = []
    evidence_findings = []
    unmeasured_cells = []

    print(f'Running {len(items)} items x {len(conditions)} conditions x {repeat_count} repeats')
    print(f'Total requests: {len(items) * len(conditions) * repeat_count}')
    print('=' * 60)

    for condition in conditions:
        prompt = system_prompt_base if condition == 'base' else system_prompt_removed
        tools_for_condition = tools  # tools always offered per perturbation discipline

        for item in items:
            item_id = item['id']
            ctx = build_delivered_context(fixture, item['source_accounts'])
            gt = gt_module.compute(item_id, ctx)

            # Check derivability
            if not gt.get('derivable', True):
                print(f'  {item_id}/{condition}: VOID (underivable)')
                all_results.append({
                    'item_id': item_id, 'condition': condition,
                    'repeat': 0, 'status': 'VOID',
                })
                continue

            expected = gt['final']
            collision, collision_field = check_lookup_collision(expected, ctx)

            for rep in range(1, repeat_count + 1):
                print(f'  {item_id}/{condition}/r{rep}: ', end='', flush=True)

                # Build messages
                context_text = format_fixture_context(fixture, item)
                messages = [
                    {'role': 'system', 'content': prompt},
                    {'role': 'user', 'content': f'{context_text}\n\nQuestion: {item["text"]}'},
                ]

                try:
                    response, request_record = adapter_send(
                        endpoint, messages=messages,
                        tools=tools_for_condition,
                        sampling=sampling, model=model)
                except adapter.RateLimitError as e:
                    print(f'RATE-LIMITED')
                    unmeasured_cells.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep, 'cause': 'rate_limited',
                    })
                    transcript.append(
                        transcript_path, item_id=item_id,
                        arm_id=condition, condition=condition,
                        request_sent={'messages': messages},
                        response_received=None, tool_calls=[],
                        evidence_class=None,
                        error_state='RATE_LIMITED',
                        seal_hash='smoke-test',
                    )
                    all_results.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep, 'status': 'UNMEASURED',
                        'cause': 'rate_limited',
                    })
                    continue
                except adapter.AdapterError as e:
                    print(f'TRANSPORT_ERROR: {e}')
                    unmeasured_cells.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep, 'cause': str(e),
                    })
                    all_results.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep, 'status': 'UNMEASURED',
                        'cause': str(e),
                    })
                    continue

                # -- Drive tool loop --
                all_tc = []
                round_shapes = []
                current = response
                tool_loop_messages = list(messages)

                # Check shape of initial response (round 0)
                from evidence import _extract_model_tool_calls
                _, r0_recognised, r0_reason = _extract_model_tool_calls(response)
                round_shapes.append((r0_recognised, r0_reason))

                for turn in range(1, 11):
                    choices = current.get('choices', [])
                    if not choices:
                        break
                    msg = choices[0].get('message', {})
                    model_calls = msg.get('tool_calls') or []
                    if not model_calls:
                        break

                    for tc in model_calls:
                        tc_record = {
                            'turn': turn,
                            'id': tc.get('id', ''),
                            'type': tc.get('type', 'function'),
                            'function': tc.get('function', {}),
                        }
                        all_tc.append(tc_record)
                        tool_call_structures.append({
                            'item_id': item_id,
                            'condition': condition,
                            'repeat': rep,
                            'tool_call': tc_record,
                            'raw_arguments': tc.get('function', {}).get('arguments', ''),
                        })

                    tool_loop_messages.append(msg)
                    for tc in model_calls:
                        func = tc.get('function', {})
                        result = execute_tool(
                            func.get('name', ''),
                            func.get('arguments', '{}'))
                        tool_loop_messages.append({
                            'role': 'tool',
                            'tool_call_id': tc.get('id', ''),
                            'content': result,
                        })

                    try:
                        current, _ = adapter_send(
                            endpoint, messages=tool_loop_messages,
                            tools=tools_for_condition,
                            sampling=sampling, model=model)
                        # Check shape of this round's response
                        _, rn_recognised, rn_reason = _extract_model_tool_calls(current)
                        round_shapes.append((rn_recognised, rn_reason))
                    except Exception:
                        break

                final_response = current

                # -- Evidence classification (R1.3 normative: accumulated records) --
                tools_offered = tools_for_condition is not None and len(tools_for_condition) > 0
                required_op = gt.get('required_operation', 'calculator')
                ev_class, inv_outcome, self_report = classify_invocation(
                    final_response, tools_offered=tools_offered,
                    accumulated_tool_calls=all_tc,
                    round_shapes=round_shapes,
                    required_operation=required_op)
                check_ev3_guard(ev_class)

                evidence_findings.append({
                    'item_id': item_id, 'condition': condition,
                    'repeat': rep, 'evidence_class': ev_class,
                    'invocation_outcome': inv_outcome,
                    'self_report': self_report,
                })

                # -- Figure identification --
                fig_result = identify_figure(
                    final_response,
                    expected_value=expected,
                    delivered_context=ctx,
                    lookup_collision=collision,
                    answer_tolerance=answer_tolerance,
                    decline_markers=decline_markers,
                    currency_symbols=currency_symbols,
                )

                # -- Numeric grammar check --
                from evidence import _extract_content
                content, shape_ok, shape_reason = _extract_content(final_response)
                if content:
                    try:
                        tokens = extract_numeric_tokens(
                            content, currency_symbols=currency_symbols)
                    except Exception as e:
                        grammar_issues.append({
                            'item_id': item_id, 'condition': condition,
                            'repeat': rep, 'error': str(e),
                            'content': content[:500],
                        })
                        tokens = []

                # -- Check for unrecognised decline patterns --
                if content and fig_result['outcome'] not in (
                        'ADJUDICATE-DECLINE',) and any(
                        phrase in content.lower() for phrase in [
                            "i can't", "i cannot", "i'm unable",
                            "i don't have", "i am unable",
                            "i'm not able", "not possible",
                            "unable to", "i apologize",
                        ]):
                    # Potential decline not caught by configured markers
                    decline_findings.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep,
                        'content_excerpt': content[:300],
                        'configured_markers': decline_markers,
                    })

                # Write transcript
                transcript.append(
                    transcript_path, item_id=item_id,
                    arm_id=condition, condition=condition,
                    request_sent=request_record,
                    response_received=final_response,
                    tool_calls=all_tc,
                    evidence_class=ev_class,
                    error_state=None,
                    seal_hash='smoke-test',
                    invocation_outcome=inv_outcome,
                    figure_outcome=fig_result['outcome'],
                    figure_reason=fig_result.get('reason', ''),
                )

                outcome = fig_result['outcome']
                print(f'{outcome} | {ev_class} | {inv_outcome}')

                all_results.append({
                    'item_id': item_id, 'condition': condition,
                    'repeat': rep, 'status': 'EXECUTED',
                    'evidence_class': ev_class,
                    'invocation_outcome': inv_outcome,
                    'figure_outcome': outcome,
                    'figure_reason': fig_result.get('reason', ''),
                    'tool_calls_count': len(all_tc),
                    'released_figure': str(fig_result.get('released_figure', '')),
                    'expected': str(expected),
                    'shape_ok': shape_ok,
                })

                # Brief delay to avoid rate limiting
                time.sleep(0.5)

    # -- Consistency check (FATAL on mismatch) --
    _verify_invocation_consistency(all_results)
    print('  Invocation consistency check: PASSED (0 mismatches)')

    # -- Report --
    print()
    print('=' * 60)
    print('SMOKE TEST REPORT')
    print('=' * 60)
    print()
    print(DISCLAIMER)

    # 3a. Completion
    executed = [r for r in all_results if r['status'] == 'EXECUTED']
    unmeasured = [r for r in all_results if r['status'] == 'UNMEASURED']
    void = [r for r in all_results if r['status'] == 'VOID']
    print(f'\n3a. COMPLETION: {len(executed)} executed, {len(unmeasured)} unmeasured, {len(void)} void')

    # 3b. Figure identification
    print('\n3b. FIGURE IDENTIFICATION:')
    outcomes = {}
    for r in executed:
        o = r.get('figure_outcome', 'unknown')
        outcomes[o] = outcomes.get(o, 0) + 1
    for o, c in sorted(outcomes.items()):
        print(f'  {o}: {c}')
    auto_scored = sum(c for o, c in outcomes.items()
                      if o in ('AUTO-MATCH', 'AUTO-NO-FIGURE'))
    adjudicated = sum(c for o, c in outcomes.items()
                      if o.startswith('ADJUDICATE') or o == 'UNMEASURABLE')
    total = auto_scored + adjudicated
    if total > 0:
        print(f'  Auto-scored: {auto_scored}/{total} ({100*auto_scored/total:.0f}%)')
        print(f'  Adjudicated: {adjudicated}/{total} ({100*adjudicated/total:.0f}%)')

    # Per-item detail
    print('\n  Per item (base condition, first repeat):')
    for r in executed:
        if r['condition'] == 'base' and r['repeat'] == 1:
            print(f'    {r["item_id"]}: {r["figure_outcome"]} — {r.get("figure_reason", "")}')

    # 3c. Grammar issues
    print(f'\n3c. NUMERIC GRAMMAR: {len(grammar_issues)} issues')
    for gi in grammar_issues:
        print(f'  {gi["item_id"]}/{gi["condition"]}/r{gi["repeat"]}: {gi["error"]}')
        print(f'    content: {gi["content"][:200]}')

    # 3d. Decline findings
    print(f'\n3d. DECLINE MARKERS: {len(decline_findings)} unrecognised declines')
    for df in decline_findings:
        print(f'  {df["item_id"]}/{df["condition"]}/r{df["repeat"]}:')
        print(f'    "{df["content_excerpt"][:200]}"')

    # 3e. Tool-call structures
    print(f'\n3e. TOOL-CALL ARGUMENT STRUCTURES: {len(tool_call_structures)} calls')
    # Group by unique argument structure
    seen_structures = {}
    for tcs in tool_call_structures:
        tc = tcs['tool_call']
        func = tc.get('function', {})
        raw_args = tcs.get('raw_arguments', '')
        try:
            parsed = json.loads(raw_args)
            key_names = sorted(parsed.keys()) if isinstance(parsed, dict) else ['<non-dict>']
            value_types = {k: type(v).__name__ for k, v in parsed.items()} if isinstance(parsed, dict) else {}
        except Exception:
            key_names = ['<parse-error>']
            value_types = {}
            parsed = raw_args

        structure_key = str(key_names)
        if structure_key not in seen_structures:
            seen_structures[structure_key] = {
                'count': 0, 'example_raw': raw_args,
                'key_names': key_names, 'value_types': value_types,
                'example_parsed': parsed,
            }
        seen_structures[structure_key]['count'] += 1

    for sk, sv in seen_structures.items():
        print(f'  Structure: keys={sv["key_names"]} types={sv["value_types"]}')
        print(f'    count: {sv["count"]}')
        print(f'    example raw: {sv["example_raw"][:200]}')
        print(f'    example parsed: {json.dumps(sv["example_parsed"], default=str)[:200]}')

    # 3f. Evidence classes
    print(f'\n3f. EVIDENCE CLASSES:')
    ev_counts = {}
    for ef in evidence_findings:
        ec = ef['evidence_class']
        ev_counts[ec] = ev_counts.get(ec, 0) + 1
    for ec, c in sorted(ev_counts.items()):
        print(f'  {ec}: {c}')
    unrecognised = [ef for ef in evidence_findings if not ef.get('evidence_class')]
    if unrecognised:
        print(f'  UNRECOGNISED SHAPES: {len(unrecognised)}')

    # 3g. Unmeasured cells
    print(f'\n3g. UNMEASURED CELLS: {len(unmeasured_cells)}')
    for uc in unmeasured_cells:
        print(f'  {uc["item_id"]}/{uc["condition"]}/r{uc["repeat"]}: {uc["cause"]}')

    # 3h. Invocation under both conditions
    print(f'\n3h. D7.1 INVOCATION:')
    for cond in conditions:
        cond_results = [r for r in executed if r['condition'] == cond]
        invoked = sum(1 for r in cond_results
                      if r.get('invocation_outcome') == 'INVOKED')
        not_invoked = sum(1 for r in cond_results
                          if r.get('invocation_outcome') == 'NOT-INVOKED')
        failures = not_invoked
        n = len(cond_results)
        rate_str = format_rate(failures, n) if n > 0 else 'no observations'
        print(f'  {cond}: invoked={invoked} not_invoked={not_invoked} n={n}')
        print(f'    failure rate: {rate_str}')

    # Write disclaimer file
    disclaimer_path = os.path.join(output_dir, 'DISCLAIMER.txt')
    with open(disclaimer_path, 'w', encoding='utf-8') as f:
        f.write(DISCLAIMER)

    # Write summary to output
    summary_path = os.path.join(output_dir, 'smoke_summary.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump({
            '_disclaimer': DISCLAIMER.replace('\n', ' ').strip(),
            'all_results': all_results,
            'grammar_issues': grammar_issues,
            'decline_findings': decline_findings,
            'tool_call_structures': [
                {k: v for k, v in tcs.items() if k != 'tool_call'}
                for tcs in tool_call_structures
            ],
            'evidence_findings': evidence_findings,
            'unmeasured_cells': unmeasured_cells,
        }, f, indent=2, default=str, ensure_ascii=False)
    print(f'\nSummary written to {summary_path}')
    print(f'Transcript written to {transcript_path}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
