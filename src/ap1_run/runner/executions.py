"""The live runner's scoring of each execution.

score_execution scores one executed response, as the runner always has:
figure identification (recorded in the transcript), D7.3 transcription
and release coverage, D1 accuracy, the response kept for D2, evidence,
tool-call structures, numeric grammar and decline checks. Each part of
the result is appended to a Findings collector, which also records the
executions that could not be scored.
"""

import json
from dataclasses import dataclass, field
from decimal import Decimal

from ap1_run.foundation import transcript
from ap1_run.foundation.numeric import extract_numeric_tokens
from ap1_run.scoring.accuracy import score_accuracy
from ap1_run.scoring.answer_outcome import answer_outcome
from ap1_run.scoring.figure_id import identify_figure
from ap1_run.scoring.release_coverage import check_release_coverage
from ap1_run.scoring.transcription import check_transcription


@dataclass
class Findings:
    """Everything the run collects, one entry per execution or finding."""
    all_results: list = field(default_factory=list)
    all_accuracy_results: list = field(default_factory=list)  # D1
    d2_responses: dict = field(default_factory=dict)  # (item, cond) -> [response]
    grammar_issues: list = field(default_factory=list)
    decline_findings: list = field(default_factory=list)
    tool_call_structures: list = field(default_factory=list)
    evidence_findings: list = field(default_factory=list)
    transcription_results: list = field(default_factory=list)  # D7.3
    release_coverage_results: list = field(default_factory=list)  # D7.3
    unmeasured_cells: list = field(default_factory=list)


def record_underivable(findings, item_id, condition):
    """The ground truth is not derivable: the item is VOID (repeat 0)."""
    findings.all_results.append({
        'item_id': item_id, 'condition': condition,
        'repeat': 0, 'status': 'VOID',
    })


def record_transport_failure(findings, item_id, condition, rep, cause):
    """The request failed (rate limit or transport error): UNMEASURED."""
    findings.unmeasured_cells.append({
        'item_id': item_id, 'condition': condition,
        'repeat': rep, 'cause': cause,
    })
    findings.all_results.append({
        'item_id': item_id, 'condition': condition,
        'repeat': rep, 'status': 'UNMEASURED',
        'cause': cause,
    })


def record_not_scored(findings, item_id, condition, rep, status, result):
    """The engine returned VOID or UNMEASURED: recorded, not scored."""
    findings.all_results.append({
        'item_id': item_id, 'condition': condition,
        'repeat': rep, 'status': status,
        'cause': result.get('error', result.get('reason', '')),
    })


def _operation_returns(tool_calls, operation):
    """The numeric returns of every call to the operation, in call order.

    A return counts when its return_value is a JSON object (or dict) with a
    'result' that reads as a Decimal; errored or unreadable calls are left
    out. With no operation named (no ground truth), every tool's calls
    count, as for invocation in execution/evidence.py.
    """
    returns = []
    for tc in tool_calls:
        if operation and tc.get('function', {}).get('name') != operation:
            continue
        rv = tc.get('return_value')
        if not rv:
            continue
        try:
            parsed = json.loads(rv) if isinstance(rv, str) else rv
            if isinstance(parsed, dict) and 'result' in parsed:
                returns.append(Decimal(str(parsed['result'])))
        except Exception:
            pass
    return returns


def score_execution(findings, result, *, item_id, condition, rep, expected,
                    ctx, collision, config, answer_tolerance,
                    decline_markers, currency_symbols, transcript_path,
                    seal_hash):
    """Score one executed response and print its outcome line."""
    # -- Figure identification (after execute_item) --
    final_response = result.get('response')
    fig_result = identify_figure(
        final_response,
        expected_value=expected,
        delivered_context=ctx,
        lookup_collision=collision,
        answer_tolerance=answer_tolerance,
        decline_markers=decline_markers,
        structured_answer_field=config.get('structured_answer_field'),
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
        repeat=rep,
        figure_outcome=fig_result['outcome'],
        figure_reason=fig_result.get('reason', ''),
        released_figure=str(fig_result.get('released_figure', '')),
        expected=str(expected),
    )

    # -- D7.3: Transcription check (E7 fix; T3-26, T3-27, V12-6) --
    # Every return of the required operation, under the declared policy
    _quant = config.get('quantisation', {})
    _required_op = (result.get('ground_truth') or {}).get('required_operation')
    transcription_result = check_transcription(
        _operation_returns(result.get('tool_calls', []), _required_op),
        fig_result.get('released_figure'),
        figure_outcome=fig_result['outcome'],
        quantisation_digits=int(_quant.get('places', 2)),
        quantisation_rounding=_quant.get('rounding', 'ROUND_HALF_UP'),
    )
    findings.transcription_results.append({
        'item_id': item_id,
        'condition': condition,
        'repeat': rep,
        'outcome': transcription_result['outcome'],
        'difference': str(transcription_result.get('difference', '')),
        'reason': transcription_result.get('reason', ''),
        'rounded_under_declared_policy': transcription_result.get(
            'rounded_under_declared_policy', False),
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
    coverage_result = check_release_coverage(
        _rc_tool_calls, _rc_candidates, expected,
        quantisation_places=int(_quant.get('places', 2)),
        quantisation_rounding=_quant.get(
            'rounding', 'ROUND_HALF_UP'))
    findings.release_coverage_results.append({
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
        quantisation_digits=int(_quant.get('places', 2)),
        quantisation_rounding=_quant.get('rounding', 'ROUND_HALF_UP'),
    )
    # The question it belongs to, for D1 per category (T3-32)
    findings.all_accuracy_results.append(
        dict(acc_result, item_id=item_id, condition=condition))

    # -- D2: Collect response for reproducibility --
    d2_key = (item_id, condition)
    findings.d2_responses.setdefault(d2_key, []).append(
        result.get('response'))

    ev_class = result.get('evidence_class', '')
    inv_outcome = result.get('invocation_outcome', '')
    tool_calls = result.get('tool_calls', [])

    findings.evidence_findings.append({
        'item_id': item_id, 'condition': condition,
        'repeat': rep, 'evidence_class': ev_class,
        'invocation_outcome': inv_outcome,
    })

    # -- Record tool call structures --
    for tc in tool_calls:
        raw_args = tc.get('function', {}).get('arguments', '')
        findings.tool_call_structures.append({
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
            findings.grammar_issues.append({
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
        findings.decline_findings.append({
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

    # AP-1 v1.3 section 6.8: the answer-level outcome, where it is decided
    section_6_8, section_6_8_reason = answer_outcome(
        outcome, inv_outcome, result.get('provenance_results', []))

    findings.all_results.append({
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
        'answer_outcome': section_6_8,
        'answer_outcome_reason': section_6_8_reason,
    })
