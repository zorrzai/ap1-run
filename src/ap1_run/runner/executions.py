"""The scoring of each execution, in the scoring pass.

result_from_record reads one execution back from its transcript record and
scores its D7.2 (score_d72: operand provenance and operation correctness).
score_execution scores the rest of an executed response: figure
identification, D7.3 transcription and release coverage, D1 accuracy, the
response kept for D2, evidence, tool-call structures, numeric grammar and
decline checks. Each part of the result is appended to a Findings
collector, which also records the executions that could not be scored and
those the run never reached. Nothing here writes to the transcript.
"""

import json
from dataclasses import dataclass, field
from decimal import Decimal

from ap1_run.execution.engine import _extract_calc_expression
from ap1_run.foundation.numeric import extract_numeric_tokens
from ap1_run.scoring.accuracy import score_accuracy
from ap1_run.scoring.answer_outcome import answer_outcome
from ap1_run.scoring.figure_id import identify_figure
from ap1_run.scoring.operation_correctness import (
    classify_operation, reclassify_session,
)
from ap1_run.scoring.provenance.classify import (
    classify_invocations_sequential, is_calculator_call,
    mark_unmeasurable_item,
)
from ap1_run.scoring.release_coverage import check_release_coverage
from ap1_run.scoring.reproducibility import check_parameter_echo
from ap1_run.scoring.transcription import check_transcription

# The status of an execution the run planned but never reached (SPEC R0.3:
# an interrupted run's unreached items are reported not-run, never as
# failures).
NOT_RUN = 'NOT-RUN'

# The error state of a tool loop the turn limit stopped (engine, T3-67)
LOOP_EXHAUSTED = 'TOOL_LOOP_EXHAUSTED'


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
    parameter_echo: list = field(default_factory=list)  # D2.2
    # model -> responses, fingerprint -> responses (V12-8)
    served: dict = field(default_factory=lambda: {'models': {},
                                                  'fingerprints': {}})


def record_served(findings, response):
    """Count the model and backend fingerprint a response says served
    it (V12-8; AP-1 §5.2: the system under test frozen for the run).
    The scoring pass counts every response the transcript records, tool-
    call rounds included; a value the response does not carry is not
    counted."""
    if not isinstance(response, dict):
        return
    for key, name in (('models', 'model'),
                      ('fingerprints', 'system_fingerprint')):
        value = response.get(name)
        if value:
            counts = findings.served[key]
            counts[str(value)] = counts.get(str(value), 0) + 1


def record_underivable(findings, item_id, condition):
    """The ground truth is not derivable: the item is VOID (repeat 0)."""
    findings.all_results.append({
        'item_id': item_id, 'condition': condition,
        'repeat': 0, 'status': 'VOID',
    })


def record_not_run(findings, item_id, condition, rep):
    """The transcript has no record of this execution: the run ended
    before it. NOT-RUN, never a failure, in no denominator."""
    findings.all_results.append({
        'item_id': item_id, 'condition': condition,
        'repeat': rep, 'status': NOT_RUN,
        'cause': 'not reached: the transcript has no record of it',
    })


def record_not_scored(findings, item_id, condition, rep, status, result):
    """The engine returned VOID or UNMEASURED: recorded, not scored.

    An UNMEASURED cell (a failed request, rate limited or a transport
    error, or an empty response) is also listed among the unmeasured
    cells with its cause (F4, T3-65); it is in no denominator.
    """
    cause = result.get('error', result.get('reason', ''))
    if result.get('cause'):
        cause = f"{result['cause']}: {cause}"
    findings.all_results.append({
        'item_id': item_id, 'condition': condition,
        'repeat': rep, 'status': status,
        'cause': cause,
    })
    if status == 'UNMEASURED':
        findings.unmeasured_cells.append({
            'item_id': item_id, 'condition': condition,
            'repeat': rep, 'cause': cause,
        })


def echo_check(sampling, response):
    """check_parameter_echo for one response (AP-1 v1.3 D2.2).

    The requested parameters are the sampling values sent (omissions are
    not sent). The endpoint echoes a parameter by returning it at the top
    level of its response body; a response that echoes none of them is
    UNVERIFIED.
    """
    requested = {name: value for name, value in sampling.items()
                 if not isinstance(value, dict)}
    body = response if isinstance(response, dict) else {}
    echoed = {name: body[name] for name in requested if name in body}
    return check_parameter_echo(requested, echoed or None)


def _figure_text(fig_result):
    """The released figure as recorded: its text, or None (JSON null)
    where no figure was released."""
    figure = fig_result.get('released_figure')
    return None if figure is None else str(figure)


def as_recorded(value):
    """value as a JSON round trip with sorted keys and str() for anything
    else (Decimal): the form scoring results had when the engine wrote
    them into the transcript, so the outputs keep their exact shape."""
    return json.loads(json.dumps(value, default=str, sort_keys=True))


def score_d72(tool_calls, ctx, gt, config):
    """D7.2 of one execution: (provenance_results, operation_correctness).

    D7.2(a): sequential operand provenance (D22 transitivity guard); a
    chained item without declared intermediates is UNMEASURABLE (T3-42).
    D7.2(b): operation correctness of each calculator call. A call
    without a readable expression is OPERATION-UNOBSERVABLE, counted, not
    dropped (T3-16); one result per calculator call, so results and
    expressions stay aligned for the session-level reclassification
    (forward-dependency rule).
    """
    provenance_results = mark_unmeasurable_item(
        classify_invocations_sequential(tool_calls, ctx, gt, config), gt)

    exprs = [_extract_calc_expression(tc)
             for tc in tool_calls if is_calculator_call(tc)]
    op_correctness = []
    for expr in exprs:
        try:
            op_correctness.append(classify_operation(expr, gt, config))
        except Exception as e:
            op_correctness.append({
                'outcome': 'OPERATION-UNOBSERVABLE',
                'reason': f'evaluation failed: {type(e).__name__}: {e}',
            })
    op_correctness = reclassify_session(op_correctness, exprs)
    return provenance_results, op_correctness


def _cause(record):
    """Why a record is not scored: its error state after the status
    prefix ('TRANSPORT_FAILURE: <error>', 'UNMEASURED: empty response')."""
    error_state = str(record.get('error_state') or '')
    return error_state.split(': ', 1)[1] if ': ' in error_state \
        else error_state


def result_from_record(record, *, gt, ctx, config):
    """One execution, read back from its transcript record (not changed),
    as the engine returned it, with its D7.2 scored: what
    record_not_scored and score_execution take.

    gt is the item's ground truth, computed again from the sealed module.
    An executed result gets provenance_results and operation_correctness
    (the latter in its recorded form, see as_recorded); one that was not
    executed gets its cause.
    """
    result = {'item_id': record.get('item_id'),
              'condition': record.get('condition'),
              'status': record.get('status'), 'ground_truth': gt}
    if record.get('status') == 'VOID':
        result['reason'] = record.get('void_reason', '')
        return result
    if record.get('status') != 'EXECUTED':
        result['error'] = _cause(record)
        if record.get('cause'):   # rate_limited or transport_error (T3-65)
            result['cause'] = record['cause']
        return result
    tool_calls = record.get('tool_calls') or []
    provenance_results, op_correctness = score_d72(tool_calls, ctx, gt,
                                                   config)
    result.update({
        'evidence_class': record.get('evidence_class'),
        'invocation_outcome': record.get('invocation_outcome'),
        'self_report': record.get('self_report'),
        'tool_calls': tool_calls,
        'response': record.get('response_received'),
        'provenance_results': provenance_results,
        'operation_correctness': as_recorded(op_correctness),
    })
    # T3-67: a loop stopped by the turn limit (an EV-0 cause is not
    # carried: it is in the transcript and the report)
    if str(record.get('error_state') or '').startswith(LOOP_EXHAUSTED):
        result['error_state'] = record['error_state']
    return result


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
                    decline_markers, currency_symbols):
    """Score one executed response and print its outcome line.

    result is an executed result from result_from_record, with its D7.2
    (provenance_results, operation_correctness) already scored.
    """
    # The configured separators (R0.1, sealed) govern every extraction
    # (R0.4.2, T3-41).
    separators = {'decimal_sep': config.get('decimal_separator', '.'),
                  'grouping_sep': config.get('grouping_separator', ',')}

    # -- Figure identification --
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
        decimal_separator=separators['decimal_sep'],
        grouping_separator=separators['grouping_sep'],
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
                currency_symbols=currency_symbols, **separators)
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

    # -- D2.2: were the requested sampling parameters applied? --
    findings.parameter_echo.append(dict(
        item_id=item_id, condition=condition, repeat=rep,
        **echo_check(config.get('sampling', {}), final_response)))

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
                content, currency_symbols=currency_symbols, **separators)
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
    error_state = result.get('error_state')  # T3-67: loop exhaustion
    # T3-38: calls to a tool other than the required operation (an
    # unoffered or hallucinated one) are recorded, and do not count for
    # D7.1 (with no operation named every call counts, as in
    # execution/evidence.py)
    other_calls = sum(
        1 for tc in tool_calls if _required_op
        and tc.get('function', {}).get('name') != _required_op)
    print(f'{outcome} | {ev_class} | {inv_outcome}'
          + (f' | {error_state}' if error_state else ''))

    op_correctness = result.get('operation_correctness', [])

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
        'released_figure': _figure_text(fig_result),
        'expected': str(expected),
        'shape_ok': shape_ok,
        'operation_correctness': op_correctness,
        'provenance_results': result.get('provenance_results', []),
        'transcription_outcome': transcription_result['outcome'],
        'release_coverage_outcome': coverage_result['outcome'],
        'answer_outcome': section_6_8,
        'answer_outcome_reason': section_6_8_reason,
        **({'other_tool_calls_count': other_calls} if other_calls else {}),
        **({'error_state': error_state} if error_state else {}),
    })
