"""Smoke test runner for the AP-1 instrument.

THIS IS AN INSTRUMENT SMOKE TEST, NOT AN AP-1 EVALUATION.
Not conformant: no adjudication, no second scorer, no blind set,
the fixture is burned under §5.8, and 10 items < D1 minimum of 40.
Must never be reported, cited or described as an AP-1 result.
Output goes to output/ in the repository, which is gitignored
(apart from the published runs).

Usage:
    export AP1_SMOKE_API_KEY=<key>    (Linux/macOS)
    set AP1_SMOKE_API_KEY=<key>       (Windows cmd)
    $env:AP1_SMOKE_API_KEY = '<key>'  (Windows PowerShell)

    Optional:
    export AP1_SMOKE_ENDPOINT=<url>   (default: https://api.openai.com/v1/chat/completions)
    export AP1_SMOKE_MODEL=<model>    (default: gpt-4o-mini)
    ap1-run                           (after pip install -e .)
    python smoke_test.py              (the same, from a clone)

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

# NOTE: This disclaimer is a hand correction (E4). It will be replaced
# by a generated disclaimer once the conformance-declaration mechanism
# (operator_declaration + conformance_checks) is built.
DISCLAIMER = (
    'THIS IS AN INSTRUMENT SMOKE TEST, NOT AN AP-1 EVALUATION.\n'
    '\n'
    'It is not conformant: no adjudication, no second scorer, no blind set,\n'
    'the fixture is the shipped example (10 items, burned under AP-1 \xa75.8),\n'
    'and the D1 minimum of 40 items is not met.\n'
    'No figure from it may be reported, cited, quoted or described as an AP-1\n'
    'result, by us or by anyone, in any document.\n'
)

from ap1_run.foundation import adapter
from ap1_run.foundation.config import load_config
from ap1_run.execution.context import build_delivered_context, check_lookup_collision, format_fixture_context
from ap1_run.execution.engine import execute_item
from ap1_run.execution.evidence import EV_0, EV_2
from ap1_run.scoring.figure_id import identify_figure, AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE
from ap1_run.scoring.accuracy import score_accuracy, summarise_accuracy
from ap1_run.scoring.transcription import check_transcription
from ap1_run.scoring.release_coverage import check_release_coverage
from ap1_run.execution.perturbation_guard import check_single_variable_perturbation
from ap1_run.foundation.numeric import extract_numeric_tokens
from ap1_run.execution.seal import seal as create_seal
from ap1_run.foundation import transcript
from ap1_run.runner.console import print_run_report, print_scoring_report
from ap1_run.runner.credentials import get_api_key
from ap1_run.runner.outputs import write_outputs
from ap1_run.runner.summary import (
    build_summary, classify_reproducibility, find_d2_cap,
    verify_invocation_consistency,
)


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    # -- Read API key (Rule 0c) --
    # The key is NEVER printed, echoed, logged, or written to any file.
    api_key = get_api_key()
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
    # The repository root: this file is src/ap1_run/run.py.
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    example_dir = os.path.join(base_dir, 'example')

    config = load_config(os.path.join(example_dir, 'config.json'))

    config['endpoint_url'] = endpoint
    config['model'] = model

    # -- Sampling override: AP1_SMOKE_TEMPERATURE --
    # gpt-5.6-sol rejects temperature=0 with HTTP 400 (verified 2026-09-07).
    # Its error says: "Only the default (1) value is supported."
    # gpt-4.1-mini accepts temperature=0 and temperature=1 (verified 2026-09-07).
    #
    # To keep both arms at the same temperature (1), the operator sets
    # AP1_SMOKE_TEMPERATURE=1 for mini. For sol, the env var is not set
    # and the structured omission (platform-rejected) is kept.
    #
    # This is a declared env-var override, not a model-name heuristic.
    # The resolved config in report.md §2 records what was actually sent.
    temp_override = os.environ.get('AP1_SMOKE_TEMPERATURE')
    if temp_override is not None:
        config['sampling']['temperature'] = temp_override
        print(f'  temperature={temp_override} '
              f'(AP1_SMOKE_TEMPERATURE override)')
    else:
        temp_val = config.get('sampling', {}).get('temperature')
        if isinstance(temp_val, dict) and temp_val.get('value') == 'omitted':
            print(f'  temperature omitted '
                  f'(reason: {temp_val.get("reason", "?")})')
        else:
            print(f'  temperature={temp_val}')

    # -- Sampling override: AP1_SMOKE_REASONING_EFFORT --
    # gpt-4.1-mini does not support reasoning_effort (HTTP 400:
    #   "Unrecognized request argument supplied: reasoning_effort").
    # gpt-5.6-sol requires it and accepts "none" for tool use.
    #
    # For mini: set AP1_SMOKE_REASONING_EFFORT=omit to remove it.
    # For sol:  leave unset, config value "none" is sent.
    re_override = os.environ.get('AP1_SMOKE_REASONING_EFFORT')
    if re_override == 'omit':
        config['sampling']['reasoning_effort'] = {
            'value': 'omitted',
            'reason': 'not-supported',
            'detail': 'gpt-4.1-mini does not recognize reasoning_effort',
        }
        print('  reasoning_effort omitted (AP1_SMOKE_REASONING_EFFORT=omit)')
    elif re_override is not None:
        config['sampling']['reasoning_effort'] = re_override
        print(f'  reasoning_effort={re_override} '
              f'(AP1_SMOKE_REASONING_EFFORT override)')
    else:
        re_val = config.get('sampling', {}).get('reasoning_effort')
        print(f'  reasoning_effort={re_val} (from config)')

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

    # -- Runner version and source hash --
    from ap1_run.execution.version import resolve_runner_version, compute_runner_source_hash
    runner_info = resolve_runner_version(base_dir)
    config['runner_version_tag'] = runner_info['version_tag']
    config['runner_version_commit'] = runner_info['version_commit']
    config['runner_modified'] = runner_info.get('version_modified', False)
    # runner_source_hash is NOT in config -- it is a separate seal
    # component so a verifier can distinguish code changes from config
    # changes. Computed here, passed to seal() as a separate argument.
    runner_source_hash = compute_runner_source_hash(base_dir)
    print(f'Runner version: {runner_info["version_tag"]} '
          f'({runner_info["version_commit"][:12]})')
    if runner_info.get('version_modified'):
        print(f'  WARNING: runner appears modified '
              f'(git HEAD: {runner_info.get("git_commit", "?")[:12]})')
    print(f'Runner source hash: {runner_source_hash[:16]}...')
    print()

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
        runner_source_hash=runner_source_hash,
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

    # -- Perturbation guard (R1.2): refuse run if more than system prompt differs --
    import hashlib as _hashlib
    _fixture_bytes = open(os.path.join(example_dir, 'fixture.json'), 'rb').read()
    _fixture_hash = _hashlib.sha256(_fixture_bytes).hexdigest()
    _base_guard = {
        'system_prompt': system_prompt_base,
        'tools': tools,
        'tool_choice': config.get('tool_choice'),
        'sampling': sampling,
        'fixture_hash': _fixture_hash,
        'message_template': config.get('message_template'),
    }
    _removed_guard = dict(_base_guard)
    _removed_guard['system_prompt'] = system_prompt_removed
    check_single_variable_perturbation(_base_guard, _removed_guard)
    print('Perturbation guard: PASSED (single-variable: system_prompt only)')
    print()

    # -- Collector for all findings --
    all_results = []
    all_accuracy_results = []  # D1: per-item accuracy scores
    d2_responses = {}  # D2: (item_id, condition) -> [response, ...]
    grammar_issues = []
    decline_findings = []
    tool_call_structures = []
    evidence_findings = []
    transcription_results = []  # E7: D7.3 transcription check
    release_coverage_results = []  # E7: D7.3 release coverage check
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

                # -- D7.3: Transcription check (E7 fix) --
                # Extract last calculator tool return value
                _tool_return_val = None
                _tc_list = result.get('tool_calls', [])
                for _tc in reversed(_tc_list):
                    _rv = _tc.get('return_value', '')
                    if _rv:
                        import json as _json
                        try:
                            _parsed = _json.loads(_rv) if isinstance(_rv, str) else _rv
                            if isinstance(_parsed, dict) and 'result' in _parsed:
                                _tool_return_val = Decimal(str(_parsed['result']))
                        except Exception:
                            pass
                        break

                transcription_result = check_transcription(
                    _tool_return_val,
                    fig_result.get('released_figure'),
                    figure_outcome=fig_result['outcome'],
                    quantisation_digits=int(
                        config.get('quantisation', {}).get('places', 2)),
                )
                transcription_results.append({
                    'item_id': item_id,
                    'condition': condition,
                    'repeat': rep,
                    'outcome': transcription_result['outcome'],
                    'difference': str(transcription_result.get('difference', '')),
                    'reason': transcription_result.get('reason', ''),
                })

                # -- D7.3: Release coverage check (E7 fix, all items) --
                # Extract candidate figures: every number in the response
                # matching expected within tolerance (per Steven's spec)
                _rc_candidates = []
                from ap1_run.execution.evidence import _extract_content as _rc_extract
                _rc_content, _, _ = _rc_extract(final_response)
                if _rc_content:
                    try:
                        _rc_tokens = extract_numeric_tokens(
                            _rc_content,
                            currency_symbols=currency_symbols)
                        _rc_candidates = [t.value for t in _rc_tokens
                                          if abs(t.value - expected)
                                          <= answer_tolerance]
                    except Exception:
                        pass
                _rc_tool_calls = result.get('tool_calls', [])
                _quant = config.get('quantisation', {})
                coverage_result = check_release_coverage(
                    _rc_tool_calls, _rc_candidates, expected,
                    quantisation_places=int(_quant.get('places', 2)),
                    quantisation_rounding=_quant.get(
                        'rounding', 'ROUND_HALF_UP'))
                release_coverage_results.append({
                    'item_id': item_id,
                    'condition': condition,
                    'repeat': rep,
                    'outcome': coverage_result['outcome'],
                    'finding': coverage_result.get('finding', ''),
                    'ungoverned_figures': [
                        str(f) for f in
                        coverage_result.get('ungoverned_figures', [])],
                })

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
                from ap1_run.execution.evidence import _extract_content
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
                    'transcription_outcome': transcription_result['outcome'],
                    'release_coverage_outcome': coverage_result['outcome'],
                })

                # Brief delay to avoid rate limiting
                time.sleep(0.5)

    # -- Consistency check (FATAL on mismatch) --
    verify_invocation_consistency(all_results)
    print('  Invocation consistency check: PASSED (0 mismatches)')

    # -- Console Report --
    print_run_report(
        all_results, conditions, disclaimer=DISCLAIMER,
        grammar_issues=grammar_issues, decline_findings=decline_findings,
        tool_call_structures=tool_call_structures,
        evidence_findings=evidence_findings,
        unmeasured_cells=unmeasured_cells,
        transcription_results=transcription_results,
        release_coverage_results=release_coverage_results)

    # -- D1 aggregation --
    d1_summary = summarise_accuracy(all_accuracy_results)
    d1_summary['n'] = len(all_accuracy_results)

    # -- D2 classification per (item, condition) per surface --
    d2_cap_reason = find_d2_cap(config.get('sampling', {}))
    d2_results = classify_reproducibility(d2_responses, repeat_count,
                                          d2_cap_reason)

    summary = build_summary(
        all_results, evidence_findings,
        d1_summary=d1_summary, d2_results=d2_results,
        d2_cap_reason=d2_cap_reason,
        transcription_results=transcription_results,
        release_coverage_results=release_coverage_results)

    # 3j-3l. D1, D2, operand provenance
    print_scoring_report(d1_summary, d2_results, d2_cap_reason, summary)

    # -- Output files: report, adjudication sheets, disclaimer, summary --
    write_outputs(
        output_dir, transcript_path, summary=summary, config=config,
        seal_record=seal_record, questions=questions, fixture=fixture,
        release_coverage_results=release_coverage_results,
        disclaimer=DISCLAIMER,
        smoke_summary={
            'seal_hash': seal_hash,
            'all_results': all_results,
            'grammar_issues': grammar_issues,
            'decline_findings': decline_findings,
            'tool_call_structures': tool_call_structures,
            'evidence_findings': evidence_findings,
            'unmeasured_cells': unmeasured_cells,
        })

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
