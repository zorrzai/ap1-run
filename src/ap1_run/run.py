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

    Options (ap1-run --help) move the inputs and outputs from example/,
    reference/ and output/: --config, --fixture-dir, --output-dir,
    --ap1-text.

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

from ap1_run.execution.context import (
    build_delivered_context, check_lookup_collision,
)
from ap1_run.execution.engine import execute_item
from ap1_run.execution.perturbation_guard import HELD_CONSTANT
from ap1_run.execution.seal import (
    perturbation_check, seal as create_seal, source_fields_check,
)
from ap1_run.execution.seal_constants import declared_constants_check
from ap1_run.execution.version import (
    compute_runner_source_hash, resolve_runner_version,
)
from ap1_run.foundation import adapter
from ap1_run.foundation.config import load_config
from ap1_run.runner.console import print_run_report, print_scoring_report
from ap1_run.runner.credentials import get_api_key
from ap1_run.runner.executions import (
    Findings, record_not_scored, record_transport_failure, record_underivable,
    score_execution,
)
from ap1_run.runner.outputs import write_outputs
from ap1_run.runner.settings import (
    apply_sampling_overrides, check_condition_guard, endpoint_and_model,
    parse_args,
)
from ap1_run.runner.summary import (
    build_summary, classify_reproducibility, find_d2_cap,
    verify_invocation_consistency,
)
from ap1_run.scoring.accuracy import summarise_accuracy

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

# The repository root: this file is src/ap1_run/run.py.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))


def main(argv=None):
    # -- Command line: where the inputs and outputs are --
    # The defaults are the shipped example, reference/ and output/.
    args = parse_args(sys.argv[1:] if argv is None else argv, BASE_DIR)
    base_dir = BASE_DIR
    fixture_dir = args.fixture_dir

    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    # -- Read API key (Rule 0c) --
    # The key is NEVER printed, echoed, logged, or written to any file.
    api_key = get_api_key()
    key_length = len(api_key)

    # Endpoint and model are not secrets -- read from env or defaults
    endpoint, model = endpoint_and_model()

    print(f'Endpoint: {endpoint}')
    print(f'Model: {model}')
    print(f'API key: present ({key_length} chars)')
    print()

    # -- Load configuration --
    config = load_config(args.config)

    config['endpoint_url'] = endpoint
    config['model'] = model

    # -- Sampling overrides: AP1_SMOKE_TEMPERATURE, AP1_SMOKE_REASONING_EFFORT --
    apply_sampling_overrides(config)

    with open(os.path.join(fixture_dir, 'fixture.json'), 'r', encoding='utf-8') as f:
        fixture = json.load(f)

    with open(os.path.join(fixture_dir, 'questions.json'), 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # -- Load ground-truth module --
    sys.path.insert(0, fixture_dir)
    import ground_truth_example as gt_module

    # -- Output directory --
    output_dir = args.output_dir
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

    # -- R3.1 seal-time ground-truth guards --
    # The module must compute its expected values from its declared
    # source fields: refused (SealError) before sealing and before any
    # request if its output ignores a declared field, if it reads a field
    # it does not declare, or if it uses an undeclared numeric constant.
    perturbation_check(gt_module, fixture, questions)
    source_fields_check(gt_module, fixture, questions)
    declared_constants_check(gt_module, fixture, questions)
    print('Ground-truth guards (R3.1): PASSED (perturbation, source fields, '
          'declared constants)')
    print()

    # -- SEAL: R1.1 pre-registration record --
    # The real seal, not a sentinel. A live run without a valid seal
    # is refused, exactly as R1.1 requires.
    ap1_text_path = args.ap1_text
    seal_record = create_seal(
        config=config,
        fixture_path=os.path.join(fixture_dir, 'fixture.json'),
        questions_path=os.path.join(fixture_dir, 'questions.json'),
        ground_truth_path=os.path.join(fixture_dir, 'ground_truth_example.py'),
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

    # -- Perturbation guard (R1.2): refuse the run unless the system prompt,
    # and only it, differs. Each condition then runs with what was checked.
    arms = check_condition_guard(
        config, os.path.join(fixture_dir, 'fixture.json'),
        system_prompt_base, system_prompt_removed, tools, sampling)

    # -- Collector for all findings --
    findings = Findings()

    print(f'Running {len(items)} items x {len(conditions)} conditions x {repeat_count} repeats')
    print(f'Total requests: {len(items) * len(conditions) * repeat_count}')
    print('=' * 60)

    for condition in conditions:
        arm = arms[condition]

        for item in items:
            item_id = item['id']
            ctx = build_delivered_context(fixture, item['source_accounts'])
            gt = gt_module.compute(item_id, ctx)

            # Check derivability
            if not gt.get('derivable', True):
                print(f'  {item_id}/{condition}: VOID (underivable)')
                record_underivable(findings, item_id, condition)
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
                        system_prompt=arm['system_prompt'],
                        tools=arm['tools'],
                        transcript_path=transcript_path,
                        seal_hash=seal_hash,
                        repeat=rep,
                    )
                except adapter.RateLimitError:
                    print('RATE-LIMITED')
                    record_transport_failure(findings, item_id, condition,
                                             rep, 'rate_limited')
                    continue
                except adapter.AdapterError as e:
                    print(f'TRANSPORT_ERROR: {e}')
                    record_transport_failure(findings, item_id, condition,
                                             rep, str(e))
                    continue

                status = result.get('status', 'UNKNOWN')
                if status in ('VOID', 'UNMEASURED'):
                    print(f'{status}')
                    record_not_scored(findings, item_id, condition, rep,
                                      status, result)
                    continue

                # -- Score the execution (runner/executions.py) --
                score_execution(
                    findings, result, item_id=item_id, condition=condition,
                    rep=rep, expected=expected, ctx=ctx, collision=collision,
                    config=config, answer_tolerance=answer_tolerance,
                    decline_markers=decline_markers,
                    currency_symbols=currency_symbols,
                    transcript_path=transcript_path, seal_hash=seal_hash)

                # Brief delay to avoid rate limiting
                time.sleep(0.5)

    # -- Consistency check (FATAL on mismatch) --
    verify_invocation_consistency(findings.all_results)
    print('  Invocation consistency check: PASSED (0 mismatches)')

    # -- Console Report --
    print_run_report(
        findings.all_results, conditions, disclaimer=DISCLAIMER,
        grammar_issues=findings.grammar_issues,
        decline_findings=findings.decline_findings,
        tool_call_structures=findings.tool_call_structures,
        evidence_findings=findings.evidence_findings,
        unmeasured_cells=findings.unmeasured_cells,
        transcription_results=findings.transcription_results,
        release_coverage_results=findings.release_coverage_results)

    # -- D1 aggregation --
    d1_summary = summarise_accuracy(findings.all_accuracy_results)
    d1_summary['n'] = len(findings.all_accuracy_results)

    # -- D2 classification per (item, condition) per surface --
    d2_cap_reason = find_d2_cap(config.get('sampling', {}))
    d2_results = classify_reproducibility(findings.d2_responses, repeat_count,
                                          d2_cap_reason)

    summary = build_summary(
        findings.all_results, findings.evidence_findings,
        d1_summary=d1_summary, d2_results=d2_results,
        d2_cap_reason=d2_cap_reason,
        transcription_results=findings.transcription_results,
        release_coverage_results=findings.release_coverage_results,
        held_constant=HELD_CONSTANT)

    # 3j-3l. D1, D2, operand provenance
    print_scoring_report(d1_summary, d2_results, d2_cap_reason, summary)

    # -- Output files: report, adjudication sheets, disclaimer, summary --
    write_outputs(
        output_dir, transcript_path, summary=summary, config=config,
        seal_record=seal_record, questions=questions, fixture=fixture,
        release_coverage_results=findings.release_coverage_results,
        disclaimer=DISCLAIMER,
        smoke_summary={
            'seal_hash': seal_hash,
            'all_results': findings.all_results,
            'grammar_issues': findings.grammar_issues,
            'decline_findings': findings.decline_findings,
            'tool_call_structures': findings.tool_call_structures,
            'evidence_findings': findings.evidence_findings,
            'unmeasured_cells': findings.unmeasured_cells,
        })

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
