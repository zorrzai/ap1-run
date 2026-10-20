"""The scoring pass (SPEC §2, "R2 SCORE: reads only; never writes back").

score_run scores a run from its transcript alone: it opens the transcript
read-only (R0.3), writes nothing back, and goes through the executions the
run planned (every condition, item and repeat), in the run's order. An
underivable item is VOID; an execution with no record in the transcript
(the run was interrupted before it) is NOT-RUN, never a failure; a record
that was not executed (UNMEASURED) is listed with its cause; every other
execution is scored (runner/executions.py). Then come the consistency check,
the console report, D1, D2, the summary and the output files.

The live run calls it after its execution pass; the re-scorer
(scoring/rescore.py) calls it on a finished or partial transcript. Both
give the same results for the same transcript.
"""

from decimal import Decimal

from ap1_run.execution.context import (
    build_delivered_context, check_lookup_collision,
)
from ap1_run.execution.perturbation_guard import HELD_CONSTANT
from ap1_run.foundation import transcript
from ap1_run.foundation.transcript import TranscriptError
from ap1_run.runner.console import print_run_report, print_scoring_report
from ap1_run.runner.executions import (
    Findings, record_not_run, record_not_scored, record_underivable,
    result_from_record, score_execution,
)
from ap1_run.runner.outputs import attach_scores, write_outputs
from ap1_run.runner.summary import (
    build_summary, classify_reproducibility, find_d2_cap,
    verify_invocation_consistency,
)
from ap1_run.scoring.accuracy import summarise_accuracy

CONDITIONS = ['base', 'instruction_removed']

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


def index_records(records, seal_hash):
    """The transcript's records by execution: (item_id, condition, repeat).

    Raises TranscriptError for a record of another run (another seal
    hash), a record without a status or repeat (a transcript written
    before the two passes were separated: it holds scoring records and
    cannot be re-scored), or two records of one execution.
    """
    index = {}
    for number, record in enumerate(records, 1):
        if record.get('seal_hash') != seal_hash:
            raise TranscriptError(
                f'record {number} has seal hash '
                f'{record.get("seal_hash")!r}, not this run\'s {seal_hash!r}')
        if record.get('status') is None or record.get('repeat') is None:
            raise TranscriptError(
                f'record {number} has no status or repeat: the transcript '
                f'was written by a runner before the scoring pass was '
                f'separated, and cannot be scored by this one')
        key = (record['item_id'], record['condition'], record['repeat'])
        if key in index:
            raise TranscriptError(
                f'record {number} repeats execution {key[0]}/{key[1]}/'
                f'r{key[2]}')
        index[key] = record
    return index


def score_run(transcript_path, *, config, seal_record, fixture, questions,
              gt_module, output_dir):
    """Score the run in transcript_path; write the output files to
    output_dir; return the content of smoke_summary.json after its
    '_disclaimer' line.

    config is the run's resolved configuration and seal_record its
    pre-registration record (R1.1); fixture, questions and gt_module are
    the sealed inputs. The transcript is only read.
    """
    records = transcript.read_all(transcript_path)
    seal_hash = seal_record['seal_hash']
    by_execution = index_records(records, seal_hash)

    repeat_count = config.get('repeat_count', 3)
    answer_tolerance = config.get('answer_tolerance', Decimal('0.01'))
    if isinstance(answer_tolerance, str):
        answer_tolerance = Decimal(answer_tolerance)
    decline_markers = config.get('decline_markers', [])
    currency_symbols = config.get('currency_symbols', [])

    findings = Findings()
    for condition in CONDITIONS:
        for item in questions['items']:
            item_id = item['id']
            ctx = build_delivered_context(fixture, item['source_accounts'])
            gt = gt_module.compute(item_id, ctx)

            # Check derivability
            if not gt.get('derivable', True):
                print(f'  {item_id}/{condition}: VOID (underivable)')
                record_underivable(findings, item_id, condition)
                continue

            expected = gt['final']
            collision, _ = check_lookup_collision(expected, ctx)

            for rep in range(1, repeat_count + 1):
                print(f'  {item_id}/{condition}/r{rep}: ', end='', flush=True)
                record = by_execution.get((item_id, condition, rep))
                if record is None:
                    print('NOT-RUN')
                    record_not_run(findings, item_id, condition, rep)
                    continue

                result = result_from_record(record, gt=gt, ctx=ctx,
                                            config=config)
                status = result['status']
                if status in ('VOID', 'UNMEASURED'):
                    print(f'{status}')
                    record_not_scored(findings, item_id, condition, rep,
                                      status, result)
                    continue

                score_execution(
                    findings, result, item_id=item_id, condition=condition,
                    rep=rep, expected=expected, ctx=ctx, collision=collision,
                    config=config, answer_tolerance=answer_tolerance,
                    decline_markers=decline_markers,
                    currency_symbols=currency_symbols)

    # -- Consistency check (FATAL on mismatch) --
    verify_invocation_consistency(findings.all_results)
    print('  Invocation consistency check: PASSED (0 mismatches)')

    # -- Console Report --
    print_run_report(
        findings.all_results, CONDITIONS, disclaimer=DISCLAIMER,
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

    smoke_summary = {
        'seal_hash': seal_hash,
        'all_results': findings.all_results,
        'grammar_issues': findings.grammar_issues,
        'decline_findings': findings.decline_findings,
        'tool_call_structures': findings.tool_call_structures,
        'evidence_findings': findings.evidence_findings,
        'unmeasured_cells': findings.unmeasured_cells,
    }

    # -- Output files: report, adjudication sheets, disclaimer, summary --
    write_outputs(
        output_dir, records=attach_scores(records, findings.all_results),
        summary=summary, config=config, seal_record=seal_record,
        questions=questions, fixture=fixture,
        release_coverage_results=findings.release_coverage_results,
        disclaimer=DISCLAIMER, smoke_summary=smoke_summary)

    return smoke_summary
