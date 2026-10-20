"""Unit tests for the scoring pass's output files."""

import json
from decimal import Decimal

import pytest

from ap1_run.runner import outputs
from ap1_run.runner.outputs import attach_scores, write_outputs


def engine(item_id, condition, **fields):
    return dict({'item_id': item_id, 'condition': condition}, **fields)


def executed(item_id, condition, repeat, outcome, **fields):
    """A scored row of all_results."""
    return dict({'item_id': item_id, 'condition': condition,
                 'repeat': repeat, 'status': 'EXECUTED',
                 'figure_outcome': outcome,
                 'operation_correctness': [{'outcome': f'OC {outcome}'}],
                 'provenance_results': [{'outcome': f'P {outcome}'}]},
                **fields)


# -- attach_scores ---------------------------------------------------------

@pytest.mark.finding('T3-21')
def test_attach_scores_gives_each_executed_record_its_scores():
    records = [engine('Q01', 'base', repeat=1, n=1),
               engine('Q02', 'base', repeat=1, n=2)]
    results = [executed('Q02', 'base', 1, 'B'),
               executed('Q01', 'base', 1, 'A')]
    assert attach_scores(records, results) == [
        engine('Q01', 'base', repeat=1, n=1, figure_outcome='A',
               operation_correctness=[{'outcome': 'OC A'}],
               provenance_results=[{'outcome': 'P A'}]),
        engine('Q02', 'base', repeat=1, n=2, figure_outcome='B',
               operation_correctness=[{'outcome': 'OC B'}],
               provenance_results=[{'outcome': 'P B'}])]


@pytest.mark.finding('T3-21')
def test_attach_scores_leaves_the_records_unchanged():
    records = [engine('Q01', 'base', repeat=1)]
    attach_scores(records, [executed('Q01', 'base', 1, 'A')])
    assert records == [engine('Q01', 'base', repeat=1)]


@pytest.mark.finding('T3-9')
@pytest.mark.req('R3.2')
def test_attach_scores_joins_on_item_condition_and_repeat():
    # Repeat 1 failed in transport: it has no scores, and repeats 2 and 3
    # keep their own (fix plan §2 branch 6).
    records = [engine('Q01', 'base', repeat=1,
                      error_state='TRANSPORT_FAILURE: HTTP 500'),
               engine('Q01', 'base', repeat=2),
               engine('Q01', 'removed', repeat=2),
               engine('Q01', 'base', repeat=3)]
    results = [{'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
                'status': 'UNMEASURED', 'figure_outcome': 'NOT THIS'},
               executed('Q01', 'base', 2, 'AUTO-MATCH'),
               executed('Q01', 'base', 3, 'ADJUDICATE-DECLINE'),
               executed('Q01', 'removed', 2, 'R2')]
    assert [(r['condition'], r['repeat'], r.get('figure_outcome'))
            for r in attach_scores(records, results)] == [
        ('base', 1, None), ('base', 2, 'AUTO-MATCH'), ('removed', 2, 'R2'),
        ('base', 3, 'ADJUDICATE-DECLINE')]


def test_attach_scores_defaults_for_a_bare_row():
    (record,) = attach_scores([engine('Q01', 'base', repeat=1)], [
        {'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
         'status': 'EXECUTED'}])
    assert (record['figure_outcome'], record['operation_correctness'],
            record['provenance_results']) == ('', [], [])


def test_attach_scores_in_their_recorded_form():
    # As the transcript held them before T3-21: JSON, sorted keys,
    # Decimals as strings.
    (record,) = attach_scores([engine('Q01', 'base', repeat=1)], [
        executed('Q01', 'base', 1, 'A',
                 provenance_results=[{'z': Decimal('1.50'), 'a': 1}],
                 operation_correctness=[{'y': Decimal('2'), 'b': None}])])
    assert record['provenance_results'] == [{'a': 1, 'z': '1.50'}]
    assert list(record['provenance_results'][0]) == ['a', 'z']
    assert record['operation_correctness'] == [{'b': None, 'y': '2'}]


def test_attach_scores_of_nothing():
    assert attach_scores([], [executed('Q01', 'base', 1, 'A')]) == []


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

    monkeypatch.setattr(outputs.report, 'generate_report', generate_report)
    monkeypatch.setattr(outputs.adjudication, 'generate_sheets',
                        generate_sheets)
    return seen


def test_write_outputs_writes_four_files_and_says_where(
        tmp_path, stubs, capsys):
    records = [{'item_id': 'Q01', 'condition': 'base',
                'figure_outcome': 'AUTO-MATCH'}]
    write_outputs(
        str(tmp_path), records=records, summary={'s': 1},
        config={'c': 2}, seal_record={'seal_hash': 'h'},
        questions={'q': 3}, fixture={'f': 4},
        release_coverage_results=['rc'],
        disclaimer='LINE ONE\nLINE § TWO\n',
        smoke_summary={'seal_hash': 'h', 'all_results': [{'v': '1.50'}],
                       'other': object})

    assert stubs['report'] == ({'s': 1}, {'c': 2}, {'seal_hash': 'h'},
                               records)
    assert stubs['sheets'] == (records, {'q': 3}, {'f': 4},
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
        f'\nSummary written to {tmp_path}/smoke_summary.json\n')
