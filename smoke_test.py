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

NOTE ON REASONING MODELS:
  Reasoning models (e.g. gpt-5.6-sol) on /v1/chat/completions require
  reasoning_effort to be set when tools are supplied. Set
  "reasoning_effort": "none" inside the "sampling" sub-dict in
  config.json. The /v1/responses endpoint is the alternative the API
  suggests, but this runner targets /v1/chat/completions only.
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
from engine import execute_item
from evidence import EV_0, EV_2
from figure_id import identify_figure, AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE
from invocation import format_rate
from accuracy import score_accuracy, summarise_accuracy
from reproducibility import classify_mechanism
from numeric import extract_numeric_tokens
from seal import seal as create_seal
import transcript
import report
import adjudication


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
        print("  PowerShell:  $env:AP1_SMOKE_API_KEY = '<key>'")
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


def _build_summary(all_results, evidence_findings, *,
                   d1_summary=None, d2_results=None,
                   d2_cap_reason=None):
    """Build the summary dict that report.generate_report() expects.

    Aggregates per-item results into the structure report.py reads.
    """
    summary = {}

    # Evidence class counts
    ev_counts = {}
    for ef in evidence_findings:
        ec = ef.get('evidence_class', '')
        ev_counts[ec] = ev_counts.get(ec, 0) + 1
    summary['evidence_class_counts'] = ev_counts

    # Item evidence detail
    summary['item_evidence'] = evidence_findings

    # Invocation figures per condition
    inv_figures = {}
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        cond = r.get('condition', '')
        key = f'd7_invocation_{cond}'
        if key not in inv_figures:
            inv_figures[key] = {'failures': 0, 'n': 0, 'rate': None}
        inv_figures[key]['n'] += 1
        if r.get('invocation_outcome') == 'NOT-INVOKED':
            inv_figures[key]['failures'] += 1
    for key, data in inv_figures.items():
        if data['n'] > 0:
            data['rate'] = f"{data['n'] - data['failures']}/{data['n']}"
    summary['invocation_figures'] = inv_figures

    # Operation correctness counts
    op_counts = {'OPERATION-CORRECT': 0, 'WRONG-OPERATION': 0,
                 'OPERATION-UNOBSERVABLE': 0}
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        for oc in r.get('operation_correctness', []):
            outcome = oc.get('outcome', 'OPERATION-UNOBSERVABLE')
            if outcome in op_counts:
                op_counts[outcome] += 1
    summary['operation_correctness_counts'] = op_counts

    # Scoring proportions (D1 and D7)
    auto_n = sum(1 for r in all_results
                 if r.get('status') == 'EXECUTED' and
                 r.get('figure_outcome', '').startswith('AUTO'))
    adj_n = sum(1 for r in all_results
                if r.get('status') == 'EXECUTED' and
                (r.get('figure_outcome', '').startswith('ADJUDICATE') or
                 r.get('figure_outcome') == 'UNMEASURABLE'))
    total_executed = sum(1 for r in all_results
                        if r.get('status') == 'EXECUTED')
    summary['d7_results'] = {
        'n': total_executed,  # every execution with observable evidence
        'auto_scored_n': auto_n,
        'adjudicated_n': adj_n,
    }

    # D1 results
    if d1_summary:
        summary['d1_results'] = d1_summary

    # D2 results
    if d2_results:
        summary['d2_results'] = d2_results
    if d2_cap_reason:
        summary['d2_cap_reason'] = d2_cap_reason

    # Operand provenance step counts (D7.2(a))
    step_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    prov_outcomes = {'OPERANDS-GROUNDED': 0, 'OPERAND-ORIGINATED': 0}
    originated_audit = []
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        for prov in r.get('provenance_results', []):
            outcome = prov.get('outcome', '')
            if outcome in prov_outcomes:
                prov_outcomes[outcome] += 1
            for res in prov.get('operand_resolutions', []):
                step = res.get('step')
                if step in step_counts:
                    step_counts[step] += 1
            for orig in prov.get('originated_operands', []):
                originated_audit.append({
                    'item_id': r.get('item_id'),
                    'condition': r.get('condition'),
                    **orig,
                })
    summary['operand_step_counts'] = step_counts
    summary['provenance_outcomes'] = prov_outcomes
    summary['originated_operand_audit'] = originated_audit

    # Non-outcome cells
    non_outcome = []
    for r in all_results:
        if r['status'] in ('UNMEASURED', 'VOID'):
            non_outcome.append({
                'item_id': r.get('item_id'),
                'condition': r.get('condition'),
                'status': r['status'],
                'reason': r.get('cause', r.get('reason', '')),
            })
    summary['non_outcome_cells'] = non_outcome

    return summary


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

    config = load_config(os.path.join(example_dir, 'config.json'))

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

    # -- SEAL: R1.1 pre-registration record --
    # The real seal, not a sentinel. A live run without a valid seal
    # is refused, exactly as R1.1 requires.
    ap1_text_path = os.path.join(
        base_dir, 'reference', 'AP-1_v1.3_DRAFT_FOR_COMMENT.md')
    seal_record = create_seal(
        config=config,
        fixture_path=os.path.join(example_dir, 'fixture.json'),
        questions_path=os.path.join(example_dir, 'questions.json'),
        ground_truth_path=os.path.join(example_dir, 'ground_truth_example.py'),
        ap1_text_path=ap1_text_path,
    )
    seal_hash = seal_record['seal_hash']
    print(f'Seal hash: {seal_hash}')
    print(f'AP-1 text hash: {seal_record["ap1_text_hash"]}')
    print()

    # -- Run configuration --
    repeat_count = config.get('repeat_count', 3)
    conditions = ['base', 'instruction_removed']
    items = questions['items']

    sampling = config.get('sampling', {})
    answer_tolerance = config.get('answer_tolerance', Decimal('0.01'))
    if isinstance(answer_tolerance, str):
        answer_tolerance = Decimal(answer_tolerance)
    decline_markers = config.get('decline_markers', [])
    currency_symbols = config.get('currency_symbols', [])

    # -- Adapter wrapper (binds api_key) --
    def adapter_send(endpoint_url, *, messages, tools=None,
                     sampling=None, model=None, timeout=120):
        return adapter.send(
            endpoint_url, messages=messages, tools=tools,
            sampling=sampling, model=model, api_key=api_key,
            timeout=timeout)

    # -- Collector for all findings --
    all_results = []
    all_accuracy_results = []  # D1: per-item accuracy scores
    d2_responses = {}  # D2: (item_id, condition) -> [response, ...]
    grammar_issues = []
    decline_findings = []
    tool_call_structures = []
    evidence_findings = []
    unmeasured_cells = []

    print(f'Running {len(items)} items x {len(conditions)} conditions x {repeat_count} repeats')
    print(f'Total requests: {len(items) * len(conditions) * repeat_count}')
    print('=' * 60)

    for condition in conditions:
        system_prompt = system_prompt_base if condition == 'base' else system_prompt_removed

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

                # === CALL engine.execute_item — THE TESTED PATH ===
                try:
                    result = execute_item(
                        item,
                        condition=condition,
                        config=config,
                        fixture=fixture,
                        ground_truth_compute=gt_module.compute,
                        adapter_send=adapter_send,
                        system_prompt=system_prompt,
                        tools=tools,
                        transcript_path=transcript_path,
                        seal_hash=seal_hash,
                    )
                except adapter.RateLimitError as e:
                    print('RATE-LIMITED')
                    unmeasured_cells.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep, 'cause': 'rate_limited',
                    })
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

                status = result.get('status', 'UNKNOWN')
                if status in ('VOID', 'UNMEASURED'):
                    print(f'{status}')
                    all_results.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep, 'status': status,
                        'cause': result.get('error', result.get('reason', '')),
                    })
                    continue

                # -- Figure identification (after execute_item) --
                final_response = result.get('response')
                fig_result = identify_figure(
                    final_response,
                    expected_value=expected,
                    delivered_context=ctx,
                    lookup_collision=collision,
                    answer_tolerance=answer_tolerance,
                    decline_markers=decline_markers,
                    currency_symbols=currency_symbols,
                )

                # Append figure_outcome to the transcript record
                transcript.append(
                    transcript_path, item_id=item_id,
                    arm_id=condition, condition=condition,
                    request_sent=None,  # already in engine's record
                    response_received=None,
                    tool_calls=[],
                    evidence_class=result.get('evidence_class'),
                    error_state=None,
                    seal_hash=seal_hash,
                    record_type='figure_identification',
                    figure_outcome=fig_result['outcome'],
                    figure_reason=fig_result.get('reason', ''),
                    released_figure=str(fig_result.get('released_figure', '')),
                    expected=str(expected),
                )

                # -- D1: Accuracy scoring --
                acc_result = score_accuracy(
                    fig_result,
                    expected_value=expected,
                    answer_tolerance=answer_tolerance,
                    quantisation_digits=int(
                        config.get('quantisation', {}).get('places', 2)),
                )
                all_accuracy_results.append(acc_result)

                # -- D2: Collect response for reproducibility --
                d2_key = (item_id, condition)
                d2_responses.setdefault(d2_key, []).append(
                    result.get('response'))

                ev_class = result.get('evidence_class', '')
                inv_outcome = result.get('invocation_outcome', '')
                tool_calls = result.get('tool_calls', [])

                evidence_findings.append({
                    'item_id': item_id, 'condition': condition,
                    'repeat': rep, 'evidence_class': ev_class,
                    'invocation_outcome': inv_outcome,
                })

                # -- Record tool call structures --
                for tc in tool_calls:
                    raw_args = tc.get('function', {}).get('arguments', '')
                    tool_call_structures.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep, 'raw_arguments': raw_args,
                    })

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

                # -- Check for unrecognised decline patterns --
                if content and fig_result['outcome'] not in (
                        'ADJUDICATE-DECLINE',) and any(
                        phrase in content.lower() for phrase in [
                            "i can't", "i cannot", "i'm unable",
                            "i don't have", "i am unable",
                            "i'm not able", "not possible",
                            "unable to", "i apologize",
                        ]):
                    decline_findings.append({
                        'item_id': item_id, 'condition': condition,
                        'repeat': rep,
                        'content_excerpt': content[:300],
                        'configured_markers': decline_markers,
                    })

                outcome = fig_result['outcome']
                print(f'{outcome} | {ev_class} | {inv_outcome}')

                # Collect operation_correctness from engine result
                op_correctness = []
                # Read from the transcript (engine wrote it)
                tr_records = transcript.read_all(transcript_path)
                for tr in reversed(tr_records):
                    if (tr.get('item_id') == item_id and
                            tr.get('condition') == condition and
                            tr.get('record_type') != 'figure_identification'):
                        op_correctness = tr.get('operation_correctness', [])
                        break

                all_results.append({
                    'item_id': item_id, 'condition': condition,
                    'repeat': rep, 'status': 'EXECUTED',
                    'evidence_class': ev_class,
                    'invocation_outcome': inv_outcome,
                    'figure_outcome': outcome,
                    'figure_reason': fig_result.get('reason', ''),
                    'tool_calls_count': len(tool_calls),
                    'released_figure': str(fig_result.get('released_figure', '')),
                    'expected': str(expected),
                    'shape_ok': shape_ok,
                    'operation_correctness': op_correctness,
                    'provenance_results': result.get('provenance_results', []),
                })

                # Brief delay to avoid rate limiting
                time.sleep(0.5)

    # -- Consistency check (FATAL on mismatch) --
    _verify_invocation_consistency(all_results)
    print('  Invocation consistency check: PASSED (0 mismatches)')

    # -- Console Report --
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

    # 3d. Decline findings
    print(f'\n3d. DECLINE MARKERS: {len(decline_findings)} unrecognised declines')

    # 3e. Tool-call structures
    print(f'\n3e. TOOL-CALL ARGUMENT STRUCTURES: {len(tool_call_structures)} calls')

    # 3f. Evidence classes
    print(f'\n3f. EVIDENCE CLASSES:')
    ev_counts = {}
    for ef in evidence_findings:
        ec = ef['evidence_class']
        ev_counts[ec] = ev_counts.get(ec, 0) + 1
    for ec, c in sorted(ev_counts.items()):
        print(f'  {ec}: {c}')

    # 3g. Unmeasured cells
    print(f'\n3g. UNMEASURED CELLS: {len(unmeasured_cells)}')

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

    # 3i. D7.2(b) operation correctness
    print(f'\n3i. D7.2(b) OPERATION CORRECTNESS:')
    op_counts = {'OPERATION-CORRECT': 0, 'WRONG-OPERATION': 0,
                 'OPERATION-UNOBSERVABLE': 0}
    for r in executed:
        for oc in r.get('operation_correctness', []):
            outcome = oc.get('outcome', 'OPERATION-UNOBSERVABLE')
            if outcome in op_counts:
                op_counts[outcome] += 1
    for outcome in ['OPERATION-CORRECT', 'WRONG-OPERATION', 'OPERATION-UNOBSERVABLE']:
        print(f'  {outcome}: {op_counts[outcome]}')

    # 3j. D1 Accuracy
    print(f'\n3j. D1 ACCURACY:')
    if d1_summary:
        print(f'  Auto-scored: {d1_summary.get("auto_scored_n", 0)}')
        print(f'  Adjudicated: {d1_summary.get("adjudicated_n", 0)}')
        print(f'  Correct: {d1_summary.get("correct", 0)}')
        print(f'  Incorrect: {d1_summary.get("incorrect", 0)}')
        print(f'  No figure: {d1_summary.get("no_figure", 0)}')
        rate = d1_summary.get('accuracy_rate')
        if rate is not None:
            print(f'  Accuracy rate: {rate}')

    # 3k. D2 Reproducibility
    print(f'\n3k. D2 REPRODUCIBILITY:')
    if d2_cap_reason:
        print(f'  CAP: {d2_cap_reason}')
    d2_mechs = {}
    for key, surfaces in d2_results.items():
        for surface, mech in surfaces.items():
            m = mech['mechanism']
            d2_mechs[m] = d2_mechs.get(m, 0) + 1
    for m, c in sorted(d2_mechs.items()):
        print(f'  {m}: {c}')

    # 3l. Operand provenance step counts
    print(f'\n3l. D7.2(a) OPERAND PROVENANCE:')
    step_counts = summary.get('operand_step_counts', {})
    step_names = {1: 'source match', 2: 'transformed source',
                  3: 'reference intermediate', 4: 'computed in session',
                  5: 'originated'}
    for step in range(1, 6):
        print(f'  step {step} ({step_names[step]}): {step_counts.get(step, 0)}')
    prov_out = summary.get('provenance_outcomes', {})
    print(f'  OPERANDS-GROUNDED: {prov_out.get("OPERANDS-GROUNDED", 0)}')
    print(f'  OPERAND-ORIGINATED: {prov_out.get("OPERAND-ORIGINATED", 0)}')

    # -- Generate formal report (report.py) --
    print('\n' + '=' * 60)
    print('GENERATING FORMAL REPORT (report.py)')
    print('=' * 60)

    # -- D1 aggregation --
    d1_summary = summarise_accuracy(all_accuracy_results)
    d1_summary['n'] = len(all_accuracy_results)

    # -- D2 classification per (item, condition) per surface --
    d2_results = {}
    sampling_cfg = config.get('sampling', {})
    # D2.2 cap: if any sampling parameter was platform-rejected,
    # mechanism class is capped at OBSERVED-ONLY.
    d2_cap_reason = None
    omission_reasons = config.get('sampling_omission_reasons', {})
    for param_name, reason_info in omission_reasons.items():
        reason = reason_info if isinstance(reason_info, str) else \
            reason_info.get('reason', '') if isinstance(reason_info, dict) else ''
        if 'platform-rejected' in reason.lower() or \
                'platform-unsupported' in reason.lower():
            detail = reason_info.get('detail', reason) \
                if isinstance(reason_info, dict) else reason
            d2_cap_reason = (
                f'D2.2 cap: {param_name} was {reason}. '
                f'Detail: {detail}')
            break

    for (item_id, cond), responses in d2_responses.items():
        key = f'{item_id}/{cond}'
        d2_results[key] = {}
        for surface in ('figures', 'prose'):
            mech = classify_mechanism(
                responses,
                surface=surface,
                minimum_runs=repeat_count,
                operator_declared=None,
            )
            # D2.2 cap: platform-rejected -> cap at OBSERVED-ONLY
            if d2_cap_reason and mech['mechanism'] not in ('UNMEASURED',):
                mech['mechanism'] = 'OBSERVED-ONLY'
                mech['d2_cap'] = d2_cap_reason
            d2_results[key][surface] = mech

    summary = _build_summary(
        all_results, evidence_findings,
        d1_summary=d1_summary, d2_results=d2_results,
        d2_cap_reason=d2_cap_reason)

    # Read full transcript for report
    tr_records = transcript.read_all(transcript_path)

    # Merge figure_outcome into engine transcript records
    # Engine records don't have figure_outcome; figure_identification records do
    engine_records = [r for r in tr_records
                      if r.get('record_type') != 'figure_identification']
    figure_records = [r for r in tr_records
                      if r.get('record_type') == 'figure_identification']

    # Build lookup: (item_id, condition) -> list of figure_outcomes
    fig_lookup = {}
    for fr in figure_records:
        key = (fr.get('item_id'), fr.get('condition'))
        fig_lookup.setdefault(key, []).append(fr.get('figure_outcome', ''))

    # Attach figure_outcome to engine records for adjudication routing
    for er in engine_records:
        key = (er.get('item_id'), er.get('condition'))
        figs = fig_lookup.get(key, [])
        if figs:
            er['figure_outcome'] = figs.pop(0)

    report_text = report.generate_report(
        summary=summary,
        config=config,
        seal_record=seal_record,
        transcript_records=engine_records,
    )

    report_path = os.path.join(output_dir, 'report.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
    print(f'Formal report written to {report_path}')

    # -- Generate adjudication sheets (adjudication.py) --
    print('\nGENERATING ADJUDICATION SHEETS (adjudication.py)')

    sheets_text = adjudication.generate_sheets(
        engine_records, questions, fixture, config)

    sheets_path = os.path.join(output_dir, 'adjudication_sheets.md')
    with open(sheets_path, 'w', encoding='utf-8') as f:
        f.write(sheets_text)
    print(f'Adjudication sheets written to {sheets_path}')

    # Write disclaimer file
    disclaimer_path = os.path.join(output_dir, 'DISCLAIMER.txt')
    with open(disclaimer_path, 'w', encoding='utf-8') as f:
        f.write(DISCLAIMER)

    # Write summary to output
    summary_path = os.path.join(output_dir, 'smoke_summary.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump({
            '_disclaimer': DISCLAIMER.replace('\n', ' ').strip(),
            'seal_hash': seal_hash,
            'all_results': all_results,
            'grammar_issues': grammar_issues,
            'decline_findings': decline_findings,
            'tool_call_structures': tool_call_structures,
            'evidence_findings': evidence_findings,
            'unmeasured_cells': unmeasured_cells,
        }, f, indent=2, default=str, ensure_ascii=False)
    print(f'\nSummary written to {summary_path}')
    print(f'Transcript written to {transcript_path}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
