"""Unit tests for the runner's output files."""

import json

import pytest

from ap1_run.runner import outputs
from ap1_run.runner.outputs import attach_figure_outcomes, write_outputs


def engine(item_id, condition, **fields):
    return dict({'item_id': item_id, 'condition': condition}, **fields)


def figure(item_id, condition, outcome=None):
    record = {'item_id': item_id, 'condition': condition,
              'record_type': 'figure_identification'}
    if outcome is not None:
        record['figure_outcome'] = outcome
    return record


# -- attach_figure_outcomes -----------------------------------------------

def test_attach_returns_engine_records_only_in_order():
    records = [engine('Q01', 'base', n=1), figure('Q01', 'base', 'A'),
               engine('Q02', 'base', n=2), figure('Q02', 'base', 'B'),
               engine('Q03', 'base', n=3, record_type='execution')]
    result = attach_figure_outcomes(records)
    assert [r['n'] for r in result] == [1, 2, 3]
    assert [r.get('figure_outcome') for r in result] == ['A', 'B', None]


def test_attach_matches_repeats_in_order_per_item_and_condition():
    records = [engine('Q01', 'base', n=1), engine('Q01', 'removed', n=2),
               engine('Q01', 'base', n=3),
               figure('Q01', 'removed', 'R1'), figure('Q01', 'base', 'B1'),
               figure('Q01', 'base', 'B2')]
    result = attach_figure_outcomes(records)
    assert [(r['n'], r['figure_outcome']) for r in result] == [
        (1, 'B1'), (2, 'R1'), (3, 'B2')]


def test_attach_leaves_engine_records_without_a_figure_alone():
    records = [engine('Q01', 'base'), engine('Q01', 'base'),
               figure('Q01', 'base', 'B1')]
    result = attach_figure_outcomes(records)
    assert result[0]['figure_outcome'] == 'B1'
    assert 'figure_outcome' not in result[1]


def test_attach_figure_record_without_outcome_gives_empty_string():
    result = attach_figure_outcomes([engine('Q01', 'base'),
                                     figure('Q01', 'base')])
    assert result[0]['figure_outcome'] == ''


def test_attach_records_without_ids_match_each_other():
    result = attach_figure_outcomes([
        {'n': 1}, {'record_type': 'figure_identification',
                   'figure_outcome': 'X'}])
    assert result == [{'n': 1, 'figure_outcome': 'X'}]


def test_attach_of_nothing():
    assert attach_figure_outcomes([]) == []


# -- write_outputs --------------------------------------------------------

@pytest.fixture
def stubs(monkeypatch):
    seen = {}

    def generate_report(*, summary, config, seal_record, transcript_records):
        seen['report'] = (summary, config, seal_record, transcript_records)
        return 'REPORT § TEXT\n'

    def generate_sheets(records, questions, fixture, config, *,
                        release_coverage_results):
        seen['sheets'] = (records, questions, fixture, config,
                          release_coverage_results)
        return 'SHEETS TEXT\n'

    def read_all(path):
        seen['transcript'] = path
        return [engine('Q01', 'base'), figure('Q01', 'base', 'AUTO-MATCH')]

    monkeypatch.setattr(outputs.report, 'generate_report', generate_report)
    monkeypatch.setattr(outputs.adjudication, 'generate_sheets',
                        generate_sheets)
    monkeypatch.setattr(outputs.transcript, 'read_all', read_all)
    return seen


def test_write_outputs_writes_four_files_and_says_where(
        tmp_path, stubs, capsys):
    transcript_path = str(tmp_path / 'smoke_run.jsonl')
    write_outputs(
        str(tmp_path), transcript_path, summary={'s': 1},
        config={'c': 2}, seal_record={'seal_hash': 'h'},
        questions={'q': 3}, fixture={'f': 4},
        release_coverage_results=['rc'],
        disclaimer='LINE ONE\nLINE § TWO\n',
        smoke_summary={'seal_hash': 'h', 'all_results': [{'v': '1.50'}],
                       'other': object})

    engine_records = [{'item_id': 'Q01', 'condition': 'base',
                       'figure_outcome': 'AUTO-MATCH'}]
    assert stubs['transcript'] == transcript_path
    assert stubs['report'] == ({'s': 1}, {'c': 2}, {'seal_hash': 'h'},
                               engine_records)
    assert stubs['sheets'] == (engine_records, {'q': 3}, {'f': 4},
                               {'c': 2}, ['rc'])

    # Exact names (the file system may ignore case).
    assert sorted(p.name for p in tmp_path.iterdir()) == [
        'DISCLAIMER.txt', 'adjudication_sheets.md', 'report.md',
        'smoke_summary.json']

    def read(name):
        return (tmp_path / name).read_text(encoding='utf-8')
    assert read('report.md') == 'REPORT § TEXT\n'
    assert read('adjudication_sheets.md') == 'SHEETS TEXT\n'
    assert read('DISCLAIMER.txt') == 'LINE ONE\nLINE § TWO\n'
    summary_text = read('smoke_summary.json')
    assert summary_text == json.dumps({
        '_disclaimer': 'LINE ONE LINE § TWO',
        'seal_hash': 'h', 'all_results': [{'v': '1.50'}],
        'other': str(object),
    }, indent=2, ensure_ascii=False)
    assert list(json.loads(summary_text)) == [
        '_disclaimer', 'seal_hash', 'all_results', 'other']

    rule = '=' * 60
    assert capsys.readouterr().out == (
        f'\n{rule}\nGENERATING FORMAL REPORT (report.py)\n{rule}\n'
        f'Formal report written to {tmp_path}/report.md\n'
        '\nGENERATING ADJUDICATION SHEETS (adjudication.py)\n'
        f'Adjudication sheets written to {tmp_path}/adjudication_sheets.md\n'
        f'\nSummary written to {tmp_path}/smoke_summary.json\n'
        f'Transcript written to {transcript_path}\n')
