"""The scoring pass's output files.

write_outputs writes report.md, adjudication_sheets.md, DISCLAIMER.txt and
smoke_summary.json to the output directory. The report and the sheets read
the transcript's records with each execution's scores attached
(attach_scores); the transcript itself is never written.
"""

import json
import os

from ap1_run.reporting import adjudication, report
from ap1_run.runner.executions import as_recorded


def attach_scores(tr_records, all_results):
    """Copies of the transcript's records, each executed one given its
    scores from the run's results: figure_outcome, operation_correctness
    and provenance_results (as they were recorded, see as_recorded).

    Records and results are matched by (item_id, condition, repeat). The
    records themselves are not changed.
    """
    scored = {(r.get('item_id'), r.get('condition'), r.get('repeat')): r
              for r in all_results if r.get('status') == 'EXECUTED'}
    records = []
    for record in tr_records:
        record = dict(record)
        result = scored.get((record.get('item_id'), record.get('condition'),
                             record.get('repeat')))
        if result is not None:
            record['operation_correctness'] = as_recorded(
                result.get('operation_correctness', []))
            record['provenance_results'] = as_recorded(
                result.get('provenance_results', []))
            record['figure_outcome'] = result.get('figure_outcome', '')
        records.append(record)
    return records


def write_outputs(output_dir, *, records, summary, config, seal_record,
                  questions, fixture, release_coverage_results, disclaimer,
                  smoke_summary):
    """Generate and write the output files, printing where each went.

    records are the transcript's records with their scores attached
    (attach_scores). smoke_summary holds the content of smoke_summary.json
    after its '_disclaimer' line (seal_hash and the run's collected
    findings).
    """
    # -- Generate formal report (report.py) --
    print('\n' + '=' * 60)
    print('GENERATING FORMAL REPORT (report.py)')
    print('=' * 60)

    report_text = report.generate_report(
        summary=summary,
        config=config,
        seal_record=seal_record,
        transcript_records=records,
    )

    report_path = os.path.join(output_dir, 'report.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
    print(f'Formal report written to {report_path}')

    # -- Generate adjudication sheets (adjudication.py) --
    print('\nGENERATING ADJUDICATION SHEETS (adjudication.py)')

    sheets_text = adjudication.generate_sheets(
        records, questions, fixture, config,
        release_coverage_results=release_coverage_results)

    sheets_path = os.path.join(output_dir, 'adjudication_sheets.md')
    with open(sheets_path, 'w', encoding='utf-8') as f:
        f.write(sheets_text)
    print(f'Adjudication sheets written to {sheets_path}')

    # Write disclaimer file
    disclaimer_path = os.path.join(output_dir, 'DISCLAIMER.txt')
    with open(disclaimer_path, 'w', encoding='utf-8') as f:
        f.write(disclaimer)

    # Write summary to output
    summary_path = os.path.join(output_dir, 'smoke_summary.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump({
            '_disclaimer': disclaimer.replace('\n', ' ').strip(),
            **smoke_summary,
        }, f, indent=2, default=str, ensure_ascii=False)
    print(f'\nSummary written to {summary_path}')
