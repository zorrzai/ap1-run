"""Unit tests for the scoring pass (runner/scoring_pass.py, T3-21).

score_run reads a transcript and scores every execution the run planned.
Its collaborators (reading a record back, scoring an execution, the
consistency check, the reports, D1, D2, the summary, the output files)
have their own tests. Here they are replaced by recording fakes, so that
the order, what score_run passes to each and what it prints are checked
exactly. The transcript is real, in a temporary directory. The run's
end-to-end use is in tests/unit/test_run.py and
tests/functional/test_step4_g4_transcript.py.
"""

import os
import stat
from decimal import Decimal

import pytest

from ap1_run.execution.perturbation_guard import HELD_CONSTANT
from ap1_run.foundation import transcript
from ap1_run.foundation.transcript import TranscriptError
from ap1_run.runner import scoring_pass
from ap1_run.runner.scoring_pass import (
    CONDITIONS, DISCLAIMER, index_records, score_run,
)

D = Decimal
RULE = '=' * 60

QUESTIONS = {'items': [{'id': 'Q1', 'source_accounts': ['a']},
                       {'id': 'Q3', 'source_accounts': []},
                       {'id': 'Q2', 'source_accounts': ['b']}]}
FIXTURE = {'accounts': [{'id': 'a'}, {'id': 'b'}]}
CONFIG = {'repeat_count': 2, 'sampling': {'temperature': '0'},
          'answer_tolerance': '0.05', 'decline_markers': ['cannot'],
          'currency_symbols': ['$']}
SEAL = {'seal_hash': 'SEAL', 'ap1_text_hash': 'TEXTHASH'}


class GroundTruth:
    """Q3 is underivable; the others are 10.00."""

    def __init__(self, calls):
        self.calls = calls

    def compute(self, item_id, ctx):
        self.calls.append(('gt', item_id, ctx))
        if item_id == 'Q3':
            return {'derivable': False}
        return {'final': D('10.00'), 'item': item_id}


def write(path, item_id, condition, repeat, status, seal_hash='SEAL',
          **extra):
    transcript.append(path, item_id=item_id, arm_id=condition,
                      condition=condition, request_sent=None,
                      response_received=None, tool_calls=[],
                      evidence_class=None, error_state=None,
                      seal_hash=seal_hash, repeat=repeat, status=status,
                      **extra)


class Pass:
    """Recording fakes for score_run's collaborators, and its inputs."""

    def __init__(self, tmp_path, monkeypatch):
        self.calls = []
        self.tmp = tmp_path
        self.transcript = str(tmp_path / 'run' / 'smoke_run.jsonl')
        os.makedirs(os.path.dirname(self.transcript))
        self.config = dict(CONFIG)
        self.gt = GroundTruth(self.calls)
        for name in ('build_delivered_context', 'check_lookup_collision',
                     'result_from_record', 'score_execution',
                     'verify_invocation_consistency', 'print_run_report',
                     'summarise_accuracy', 'find_d2_cap',
                     'classify_reproducibility', 'build_summary',
                     'print_scoring_report', 'attach_scores',
                     'write_outputs'):
            monkeypatch.setattr(scoring_pass, name, getattr(self, name))

    def run(self):
        return score_run(self.transcript, config=self.config,
                         seal_record=dict(SEAL), fixture=FIXTURE,
                         questions=QUESTIONS, gt_module=self.gt,
                         output_dir='OUT')

    def named(self, name):
        return [c[1:] for c in self.calls if c[0] == name]

    # -- fakes ---------------------------------------------------------
    def build_delivered_context(self, fixture, accounts):
        self.calls.append(('context', fixture, accounts))
        return {'accounts': list(accounts)}

    def check_lookup_collision(self, expected, ctx):
        self.calls.append(('collision', expected, ctx))
        return 'COLLISION', 'field'

    def result_from_record(self, record, **kwargs):
        self.calls.append(('read', record, kwargs))
        result = {'status': record['status'], 'n': record['repeat']}
        if record['status'] != 'EXECUTED':
            result['error'] = 'cause of ' + record['status']
        return result

    def score_execution(self, findings, result, **kwargs):
        self.calls.append(('score', result, kwargs))
        findings.all_results.append({'status': 'EXECUTED'})
        findings.all_accuracy_results.append({'acc': result['n']})
        findings.d2_responses.setdefault('d2', []).append(result)

    def verify_invocation_consistency(self, results):
        self.calls.append(('consistency', list(results)))

    def print_run_report(self, results, conditions, **kwargs):
        self.calls.append(('run_report', list(results), conditions, kwargs))

    def summarise_accuracy(self, results):
        self.calls.append(('summarise', list(results)))
        return {'d1': True}

    def find_d2_cap(self, sampling):
        self.calls.append(('d2_cap', sampling))
        return 'CAP'

    def classify_reproducibility(self, responses, repeat_count, cap):
        self.calls.append(('d2', responses, repeat_count, cap))
        return {'d2': 'results'}

    def build_summary(self, results, evidence, **kwargs):
        self.calls.append(('summary', list(results), evidence, kwargs))
        return {'summary': True}

    def print_scoring_report(self, *args):
        self.calls.append(('scoring_report',) + args)

    def attach_scores(self, records, results):
        self.calls.append(('attach', list(records), list(results)))
        return ['SCORED RECORDS']

    def write_outputs(self, output_dir, **kwargs):
        self.calls.append(('outputs', output_dir, kwargs))


@pytest.fixture
def p(tmp_path, monkeypatch):
    return Pass(tmp_path, monkeypatch)


def script(p):
    """Q1/base: UNMEASURED then EXECUTED; Q2/base: EXECUTED, then no
    record (NOT-RUN); Q1/removed: VOID then EXECUTED; Q2/removed: none
    (NOT-RUN twice). Written out of order: the run's order is the plan's."""
    write(p.transcript, 'Q1', 'instruction_removed', 2, 'EXECUTED')
    write(p.transcript, 'Q1', 'base', 1, 'UNMEASURED')
    write(p.transcript, 'Q1', 'base', 2, 'EXECUTED')
    write(p.transcript, 'Q2', 'base', 1, 'EXECUTED')
    write(p.transcript, 'Q1', 'instruction_removed', 1, 'VOID')


def test_conditions_and_disclaimer():
    assert CONDITIONS == ['base', 'instruction_removed']
    assert DISCLAIMER.startswith(
        'THIS IS AN INSTRUMENT SMOKE TEST, NOT AN AP-1 EVALUATION.\n')


@pytest.mark.finding('T3-21', 'T3-52')
def test_score_run_console(p, capsys):
    script(p)
    p.run()
    assert capsys.readouterr().out == (
        '  Q1/base/r1: UNMEASURED\n'
        '  Q1/base/r2:   Q3/base: VOID (underivable)\n'
        '  Q2/base/r1:   Q2/base/r2: NOT-RUN\n'
        '  Q1/instruction_removed/r1: VOID\n'
        '  Q1/instruction_removed/r2:   '
        'Q3/instruction_removed: VOID (underivable)\n'
        '  Q2/instruction_removed/r1: NOT-RUN\n'
        '  Q2/instruction_removed/r2: NOT-RUN\n'
        '  Invocation consistency check: PASSED (0 mismatches)\n')


@pytest.mark.finding('T3-21', 'T3-52')
@pytest.mark.req('R0.3')
def test_score_run_calls(p, capsys):
    script(p)
    records = transcript.read_all(p.transcript)
    by_key = {(r['item_id'], r['condition'], r['repeat']): r
              for r in records}
    smoke = p.run()

    # ground truth and context per item and condition; no collision check
    # for the underivable Q3
    assert [c[1] for c in p.named('context')] == [
        ['a'], [], ['b'], ['a'], [], ['b']]
    assert all(c[0] is FIXTURE for c in p.named('context'))
    assert p.named('gt') == [('Q1', {'accounts': ['a']}),
                             ('Q3', {'accounts': []}),
                             ('Q2', {'accounts': ['b']})] * 2
    assert p.named('collision') == [(D('10.00'), {'accounts': ['a']}),
                                    (D('10.00'), {'accounts': ['b']})] * 2

    # each record found is read back with its item's ground truth
    reads = p.named('read')
    assert [r for r, _ in reads] == [
        by_key[('Q1', 'base', 1)], by_key[('Q1', 'base', 2)],
        by_key[('Q2', 'base', 1)], by_key[('Q1', 'instruction_removed', 1)],
        by_key[('Q1', 'instruction_removed', 2)]]
    assert reads[0][1] == {'gt': {'final': D('10.00'), 'item': 'Q1'},
                           'ctx': {'accounts': ['a']}, 'config': p.config}

    # only executed results are scored
    scores = p.named('score')
    assert [(k['item_id'], k['condition'], k['rep']) for _, k in scores] == [
        ('Q1', 'base', 2), ('Q2', 'base', 1),
        ('Q1', 'instruction_removed', 2)]
    assert scores[0][1] == {
        'item_id': 'Q1', 'condition': 'base', 'rep': 2,
        'expected': D('10.00'), 'ctx': {'accounts': ['a']},
        'collision': 'COLLISION', 'config': p.config,
        'answer_tolerance': D('0.05'), 'decline_markers': ['cannot'],
        'currency_symbols': ['$']}

    expected_results = [
        {'item_id': 'Q1', 'condition': 'base', 'repeat': 1,
         'status': 'UNMEASURED', 'cause': 'cause of UNMEASURED'},
        {'status': 'EXECUTED'},
        {'item_id': 'Q3', 'condition': 'base', 'repeat': 0,
         'status': 'VOID'},
        {'status': 'EXECUTED'},
        {'item_id': 'Q2', 'condition': 'base', 'repeat': 2,
         'status': 'NOT-RUN',
         'cause': 'not reached: the transcript has no record of it'},
        {'item_id': 'Q1', 'condition': 'instruction_removed', 'repeat': 1,
         'status': 'VOID', 'cause': 'cause of VOID'},
        {'status': 'EXECUTED'},
        {'item_id': 'Q3', 'condition': 'instruction_removed', 'repeat': 0,
         'status': 'VOID'},
        {'item_id': 'Q2', 'condition': 'instruction_removed', 'repeat': 1,
         'status': 'NOT-RUN',
         'cause': 'not reached: the transcript has no record of it'},
        {'item_id': 'Q2', 'condition': 'instruction_removed', 'repeat': 2,
         'status': 'NOT-RUN',
         'cause': 'not reached: the transcript has no record of it'},
    ]
    assert p.named('consistency') == [(expected_results,)]

    (results, conditions, kw), = p.named('run_report')
    assert results == expected_results
    assert conditions == ['base', 'instruction_removed']
    assert kw == {'disclaimer': DISCLAIMER, 'grammar_issues': [],
                  'decline_findings': [], 'tool_call_structures': [],
                  'evidence_findings': [], 'unmeasured_cells': [],
                  'transcription_results': [],
                  'release_coverage_results': []}

    assert p.named('summarise') == [([{'acc': 2}, {'acc': 1}, {'acc': 2}],)]
    assert p.named('d2_cap') == [({'temperature': '0'},)]
    d2_responses = {'d2': [res for res, _ in scores]}
    assert p.named('d2') == [(d2_responses, 2, 'CAP')]
    (results, evidence, kw), = p.named('summary')
    assert results == expected_results and evidence == []
    assert kw == {'d1_summary': {'d1': True, 'n': 3},
                  'd2_results': {'d2': 'results'}, 'd2_cap_reason': 'CAP',
                  'transcription_results': [],
                  'release_coverage_results': [],
                  'held_constant': HELD_CONSTANT}
    assert p.named('scoring_report') == [(
        {'d1': True, 'n': 3}, {'d2': 'results'}, 'CAP', {'summary': True})]

    assert p.named('attach') == [(records, expected_results)]
    smoke_summary = {
        'seal_hash': 'SEAL', 'all_results': expected_results,
        'grammar_issues': [], 'decline_findings': [],
        'tool_call_structures': [], 'evidence_findings': [],
        'unmeasured_cells': []}
    assert p.named('outputs') == [('OUT', {
        'records': ['SCORED RECORDS'], 'summary': {'summary': True},
        'config': p.config, 'seal_record': SEAL, 'questions': QUESTIONS,
        'fixture': FIXTURE, 'release_coverage_results': [],
        'disclaimer': DISCLAIMER, 'smoke_summary': smoke_summary})]
    assert smoke == smoke_summary

    stages = [c[0] for c in p.calls if c[0] in (
        'consistency', 'run_report', 'summarise', 'd2_cap', 'd2', 'summary',
        'scoring_report', 'attach', 'outputs')]
    assert stages == ['consistency', 'run_report', 'summarise', 'd2_cap',
                      'd2', 'summary', 'scoring_report', 'attach', 'outputs']


def test_score_run_defaults_without_tolerance_markers_or_symbols(p):
    p.config = {}
    write(p.transcript, 'Q1', 'base', 1, 'EXECUTED')
    p.run()
    kw = p.named('score')[0][1]
    assert (kw['answer_tolerance'], kw['decline_markers'],
            kw['currency_symbols']) == (D('0.01'), [], [])
    # repeat_count 3: 2 items x 2 conditions x 3, one record
    assert sum(1 for r in p.named('consistency')[0][0]
               if r['status'] == 'NOT-RUN') == 11
    assert p.named('d2_cap') == [({},)]
    assert p.named('d2')[0][1] == 3


def test_score_run_numeric_tolerance_is_kept_as_given(p):
    p.config['answer_tolerance'] = 0.5   # not a string: not converted
    write(p.transcript, 'Q1', 'base', 1, 'EXECUTED')
    p.run()
    tolerance = p.named('score')[0][1]['answer_tolerance']
    assert tolerance == 0.5 and isinstance(tolerance, float)


@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.3')
def test_score_run_empty_transcript_everything_not_run(p):
    open(p.transcript, 'w').close()
    smoke = p.run()
    assert [r['status'] for r in smoke['all_results']] == [
        'NOT-RUN', 'NOT-RUN', 'VOID', 'NOT-RUN', 'NOT-RUN'] * 2
    assert smoke['unmeasured_cells'] == []
    assert p.named('score') == []


@pytest.mark.finding('T3-21', 'T3-52')
@pytest.mark.req('R0.3')
def test_score_run_reads_a_read_only_transcript_and_leaves_it(p):
    # SPEC R0.3 "The scorer opens the transcript read-only"; §2 "reads
    # only; never writes back".
    script(p)
    before = open(p.transcript, 'rb').read()
    os.chmod(p.transcript, stat.S_IRUSR)
    try:
        p.run()
    finally:
        os.chmod(p.transcript, stat.S_IRUSR | stat.S_IWUSR)
    assert open(p.transcript, 'rb').read() == before


def test_score_run_flushes_each_progress_prefix(p, monkeypatch):
    # "  Q1/base/r1: " is flushed before the execution is scored.
    seen = []

    class Stdout:
        def write(self, text):
            seen.append(('write', text))

        def flush(self):
            seen.append(('flush',))
    script(p)
    monkeypatch.setattr('sys.stdout', Stdout())
    p.run()
    prefixes = [i for i, e in enumerate(seen)
                if e[0] == 'write' and e[1].endswith(('/r1: ', '/r2: '))]
    after = [[e for e in seen[i + 1:] if e != ('write', '')][0]
             for i in prefixes]
    assert after == [('flush',)] * 8


# -- index_records ---------------------------------------------------------

def record(item_id='Q1', condition='base', repeat=1, status='EXECUTED',
           seal_hash='SEAL'):
    return {'item_id': item_id, 'condition': condition, 'repeat': repeat,
            'status': status, 'seal_hash': seal_hash}


def test_index_records_by_item_condition_repeat():
    records = [record(), record(repeat=2), record(condition='other'),
               record(item_id='Q2')]
    assert index_records(records, 'SEAL') == {
        ('Q1', 'base', 1): records[0], ('Q1', 'base', 2): records[1],
        ('Q1', 'other', 1): records[2], ('Q2', 'base', 1): records[3]}
    assert index_records([], 'SEAL') == {}


def test_index_records_refuses_another_runs_record():
    with pytest.raises(TranscriptError, match=(
            "^record 2 has seal hash 'OTHER', not this run's 'SEAL'$")):
        index_records([record(), record(repeat=2, seal_hash='OTHER')],
                      'SEAL')


@pytest.mark.parametrize('field', ['status', 'repeat'])
def test_index_records_refuses_a_transcript_from_before_the_split(field):
    # A transcript of the published runs has figure_identification
    # records and engine records without a status: not scoreable here.
    old = record()
    del old[field]
    with pytest.raises(TranscriptError, match=(
            '^record 1 has no status or repeat: the transcript was written '
            'by a runner before the scoring pass was separated, and cannot '
            'be scored by this one$')):
        index_records([old], 'SEAL')


def test_index_records_refuses_two_records_of_one_execution():
    with pytest.raises(TranscriptError,
                       match='^record 3 repeats execution Q1/base/r2$'):
        index_records([record(repeat=2), record(), record(repeat=2)],
                      'SEAL')


def test_score_run_refuses_a_bad_transcript_before_scoring(p):
    write(p.transcript, 'Q1', 'base', 1, 'EXECUTED', seal_hash='OTHER')
    with pytest.raises(TranscriptError, match='not this run'):
        p.run()
    assert p.calls == []
