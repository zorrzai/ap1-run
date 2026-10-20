"""The live runner's output files.

write_outputs writes report.md, adjudication_sheets.md, DISCLAIMER.txt and
smoke_summary.json to the output directory, from the transcript the run
wrote. attach_figure_outcomes joins each engine record with the figure
outcome recorded for it.
"""

import json
import os

from ap1_run.foundation import transcript
from ap1_run.reporting import adjudication, report


def attach_figure_outcomes(tr_records):
    """The engine records of a transcript, each given the figure_outcome
    of the matching figure_identification record.

    Records are matched by (item_id, condition, repeat): an execution
    takes the figure outcome recorded for its own repeat, so a repeat
    with no figure record (a transport failure) gets none and never
    shifts the others. Within one key (a transcript written before
    records carried a repeat index has repeat None throughout), the n-th
    engine record takes the n-th figure outcome.
    """
    # Engine records don't have figure_outcome; figure_identification records do
    engine_records = [r for r in tr_records
                      if r.get('record_type') != 'figure_identification']
    figure_records = [r for r in tr_records
                      if r.get('record_type') == 'figure_identification']

    def key(record):
        return (record.get('item_id'), record.get('condition'),
                record.get('repeat'))

    fig_lookup = {}
    for fr in figure_records:
        fig_lookup.setdefault(key(fr), []).append(
            fr.get('figure_outcome', ''))

    # Attach figure_outcome to engine records for adjudication routing
    for er in engine_records:
        figs = fig_lookup.get(key(er))
        if figs:
            er['figure_outcome'] = figs.pop(0)
    return engine_records


def write_outputs(output_dir, transcript_path, *, summary, config,
                  seal_record, questions, fixture, release_coverage_results,
                  disclaimer, smoke_summary):
    """Generate and write the output files, printing where each went.

    smoke_summary holds the content of smoke_summary.json after its
    '_disclaimer' line (seal_hash and the run's collected findings).
    """
    # -- Generate formal report (report.py) --
    print('\n' + '=' * 60)
    print('GENERATING FORMAL REPORT (report.py)')
    print('=' * 60)

    # Read full transcript for report
    tr_records = transcript.read_all(transcript_path)

    engine_records = attach_figure_outcomes(tr_records)

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
        engine_records, questions, fixture, config,
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
    print(f'Transcript written to {transcript_path}')
