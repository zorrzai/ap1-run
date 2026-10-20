"""Unit tests for the runner's per-execution scoring.

score_execution wires the scoring modules together; those have their own
tests. Here they are replaced by recording fakes, so that what is passed
to each and what is collected from each is checked exactly. The
transcript is real, in a temporary directory. One test at the end runs
the real scoring modules on a realistic response.
"""

import json
from decimal import Decimal
from types import SimpleNamespace

import pytest

from ap1_run.foundation import transcript
from ap1_run.runner import executions
from ap1_run.runner.executions import (
    Findings, record_not_scored, record_transport_failure, record_underivable,
    score_execution,
)

D = Decimal
DECLINE_PHRASES = ["i can't", "i cannot", "i'm unable", "i don't have",
                   "i am unable", "i'm not able", "not possible",
                   "unable to", "i apologize"]


def response(content):
    return {'choices': [{'message': {'role': 'assistant',
                                     'content': content}}]}


def calc(expression, return_value):
    return {'id': 'c1', 'type': 'function',
            'function': {'name': 'calculator',
                         'arguments': json.dumps({'expression': expression})},
            'return_value': return_value}


class Fakes:
    """Recording stand-ins for the scoring modules score_execution calls."""

    def __init__(self, monkeypatch):
        self.calls = {}
        self.figure = {'outcome': 'AUTO-MATCH', 'reason': 'one figure',
                       'released_figure': D('638.40')}
        self.tokens = {}       # content -> list of values, or an exception
        for name in ('identify_figure', 'check_transcription',
                     'check_release_coverage', 'score_accuracy',
                     'extract_numeric_tokens'):
            monkeypatch.setattr(executions, name, getattr(self, name))

    def record(self, name, *args, **kwargs):
        self.calls.setdefault(name, []).append((args, kwargs))

    def identify_figure(self, *args, **kwargs):
        self.record('identify_figure', *args, **kwargs)
        return dict(self.figure)

    def check_transcription(self, *args, **kwargs):
        self.record('check_transcription', *args, **kwargs)
        return {'outcome': 'TRANSCRIBED-EXACT', 'difference': D('0.00'),
                'reason': 'equal'}

    def check_release_coverage(self, *args, **kwargs):
        self.record('check_release_coverage', *args, **kwargs)
        return {'outcome': 'PARTIALLY-GOVERNED', 'finding': 'one ungoverned',
                'ungoverned_figures': [D('12.5'), D('7')]}

    def score_accuracy(self, *args, **kwargs):
        self.record('score_accuracy', *args, **kwargs)
        return {'scored': 'accuracy'}

    def extract_numeric_tokens(self, content, *, currency_symbols):
        self.record('extract_numeric_tokens', content,
                    currency_symbols=currency_symbols)
        found = self.tokens.get(content, [])
        if isinstance(found, Exception):
            raise found
        return [SimpleNamespace(value=D(v)) for v in found]


@pytest.fixture
def fakes(monkeypatch):
    return Fakes(monkeypatch)


@pytest.fixture
def tpath(tmp_path):
    return str(tmp_path / 'run.jsonl')


CONFIG = {'quantisation': {'places': 3, 'rounding': 'ROUND_HALF_EVEN'}}


def score(findings, result, tpath, **overrides):
    kwargs = dict(item_id='Q01', condition='base', rep=2,
                  expected=D('638.40'), ctx={'savings': {'balance': '1'}},
                  collision=False, config=CONFIG,
                  answer_tolerance=D('0.01'), decline_markers=['cannot'],
                  currency_symbols=['$'], transcript_path=tpath,
                  seal_hash='seal-1')
    kwargs.update(overrides)
    score_execution(findings, result, **kwargs)


# -- the collected records ------------------------------------------------

def test_score_execution_collects_every_record(fakes, tpath, capsys):
    transcript.append(tpath, item_id='Q01', arm_id='base', condition='base',
                      request_sent={}, response_received={}, tool_calls=[],
                      evidence_class='EV-2', error_state=None,
                      seal_hash='seal-1',
                      operation_correctness=[{'outcome': 'OPERATION-CORRECT'}])
    content = 'The total is $638.40, about 640.'
    fakes.tokens[content] = ['638.40', '640', '638.41', '638.39', '638.3899']
    result = {
        'response': response(content),
        'tool_calls': [calc('15200 * 0.042', '{"result": 638.4}')],
        'evidence_class': 'EV-2', 'invocation_outcome': 'INVOKED',
        'provenance_results': [{'outcome': 'OPERANDS-GROUNDED'}],
    }
    findings = Findings()
    score(findings, result, tpath)

    assert capsys.readouterr().out == 'AUTO-MATCH | EV-2 | INVOKED\n'

    # figure identification, recorded in the transcript
    assert fakes.calls['identify_figure'] == [((response(content),), {
        'expected_value': D('638.40'),
        'delivered_context': {'savings': {'balance': '1'}},
        'lookup_collision': False, 'answer_tolerance': D('0.01'),
        'decline_markers': ['cannot'], 'currency_symbols': ['$']})]
    records = transcript.read_all(tpath)
    figure_record = records[-1]
    del figure_record['timestamp']
    assert figure_record == {
        'item_id': 'Q01', 'arm_id': 'base', 'condition': 'base',
        'request_sent': None, 'response_received': None, 'tool_calls': [],
        'evidence_class': 'EV-2', 'error_state': None, 'seal_hash': 'seal-1',
        'record_type': 'figure_identification', 'figure_outcome': 'AUTO-MATCH',
        'figure_reason': 'one figure', 'released_figure': '638.40',
        'expected': '638.40'}

    # D7.3 transcription
    assert fakes.calls['check_transcription'] == [((D('638.4'), D('638.40')), {
        'figure_outcome': 'AUTO-MATCH', 'quantisation_digits': 3})]
    assert findings.transcription_results == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'outcome': 'TRANSCRIBED-EXACT', 'difference': '0.00',
        'reason': 'equal'}]

    # D7.3 release coverage: candidates within the tolerance, inclusive
    assert fakes.calls['check_release_coverage'] == [((
        result['tool_calls'], [D('638.40'), D('638.41'), D('638.39')],
        D('638.40')), {'quantisation_places': 3,
                       'quantisation_rounding': 'ROUND_HALF_EVEN'})]
    assert findings.release_coverage_results == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'outcome': 'PARTIALLY-GOVERNED', 'finding': 'one ungoverned',
        'ungoverned_figures': ['12.5', '7']}]

    # D1 and D2
    assert fakes.calls['score_accuracy'] == [((fakes.figure,), {
        'expected_value': D('638.40'), 'answer_tolerance': D('0.01'),
        'quantisation_digits': 3})]
    assert findings.all_accuracy_results == [{'scored': 'accuracy'}]
    assert findings.d2_responses == {('Q01', 'base'): [response(content)]}

    # evidence, tool-call structures, grammar (both token extractions)
    assert findings.evidence_findings == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'evidence_class': 'EV-2', 'invocation_outcome': 'INVOKED'}]
    assert findings.tool_call_structures == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'raw_arguments': '{"expression": "15200 * 0.042"}'}]
    assert fakes.calls['extract_numeric_tokens'] == [
        ((content,), {'currency_symbols': ['$']})] * 2
    assert findings.grammar_issues == []
    assert findings.decline_findings == []
    assert findings.unmeasured_cells == []

    assert findings.all_results == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'status': 'EXECUTED', 'evidence_class': 'EV-2',
        'invocation_outcome': 'INVOKED', 'figure_outcome': 'AUTO-MATCH',
        'figure_reason': 'one figure', 'tool_calls_count': 1,
        'released_figure': '638.40', 'expected': '638.40', 'shape_ok': True,
        'operation_correctness': [{'outcome': 'OPERATION-CORRECT'}],
        'provenance_results': [{'outcome': 'OPERANDS-GROUNDED'}],
        'transcription_outcome': 'TRANSCRIBED-EXACT',
        'release_coverage_outcome': 'PARTIALLY-GOVERNED'}]


def test_score_execution_defaults_for_a_bare_result(fakes, tpath, capsys):
    fakes.figure = {'outcome': 'AUTO-NO-FIGURE'}
    findings = Findings()
    score(findings, {}, tpath, config={})
    assert capsys.readouterr().out == 'AUTO-NO-FIGURE |  | \n'
    assert fakes.calls['check_transcription'] == [((None, None), {
        'figure_outcome': 'AUTO-NO-FIGURE', 'quantisation_digits': 2})]
    assert fakes.calls['check_release_coverage'] == [(([], [], D('638.40')), {
        'quantisation_places': 2, 'quantisation_rounding': 'ROUND_HALF_UP'})]
    assert fakes.calls['score_accuracy'][0][1]['quantisation_digits'] == 2
    assert 'extract_numeric_tokens' not in fakes.calls  # no content
    assert findings.d2_responses == {('Q01', 'base'): [None]}
    assert findings.evidence_findings == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'evidence_class': '', 'invocation_outcome': ''}]
    assert findings.tool_call_structures == []
    assert findings.all_results == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'status': 'EXECUTED', 'evidence_class': '', 'invocation_outcome': '',
        'figure_outcome': 'AUTO-NO-FIGURE', 'figure_reason': '',
        'tool_calls_count': 0, 'released_figure': '', 'expected': '638.40',
        'shape_ok': False, 'operation_correctness': [],
        'provenance_results': [], 'transcription_outcome':
        'TRANSCRIBED-EXACT', 'release_coverage_outcome': 'PARTIALLY-GOVERNED'}]
    figure_record = transcript.read_all(tpath)[-1]
    assert (figure_record['evidence_class'], figure_record['figure_reason'],
            figure_record['released_figure']) == (None, '', '')


def test_score_execution_empty_results_from_scorers(fakes, tpath, monkeypatch):
    monkeypatch.setattr(executions, 'check_transcription',
                        lambda *a, **k: {'outcome': 'UNOBSERVABLE'})
    monkeypatch.setattr(executions, 'check_release_coverage',
                        lambda *a, **k: {'outcome': 'COVERAGE-UNOBSERVABLE'})
    findings = Findings()
    score(findings, {}, tpath)
    assert findings.transcription_results == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'outcome': 'UNOBSERVABLE', 'difference': '', 'reason': ''}]
    assert findings.release_coverage_results == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'outcome': 'COVERAGE-UNOBSERVABLE', 'finding': '',
        'ungoverned_figures': []}]


# -- the tool's return value for D7.3 -------------------------------------

@pytest.mark.parametrize('tool_calls, expected', [
    # the last call with a return value decides
    ([calc('1', '{"result": 1}'), calc('2', '{"result": "2.50"}')], D('2.50')),
    ([calc('1', '{"result": 1}'), calc('2', '')], D('1')),
    ([calc('1', '{"result": 1}'), {'function': {}}], D('1')),
    # a dict return value is used as it is
    ([calc('1', {'result': 3})], D('3')),
    # the last non-empty return value decides, even when it has no result
    ([calc('1', '{"result": 1}'), calc('2', '{"error": "x"}')], None),
    ([calc('1', '{"result": 1}'), calc('2', 'not json')], None),
    ([calc('1', '{"result": 1}'), calc('2', '[1]')], None),
    ([calc('1', '{"result": 1}'), calc('2', '{"result": "abc"}')], None),
    ([], None),
])
def test_score_execution_tool_return_value(fakes, tpath, tool_calls,
                                           expected):
    score(Findings(), {'tool_calls': tool_calls}, tpath)
    assert fakes.calls['check_transcription'][0][0][0] == expected


# -- release coverage candidates ------------------------------------------

def test_score_execution_coverage_without_tokens_when_extraction_fails(
        fakes, tpath):
    content = 'bad 1,2,3.4.5'
    fakes.tokens[content] = ValueError('ambiguous grouping')
    findings = Findings()
    score(findings, {'response': response(content)}, tpath)
    assert fakes.calls['check_release_coverage'][0][0][1] == []
    # the same failure is a numeric-grammar finding
    assert findings.grammar_issues == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'error': 'ambiguous grouping', 'content': content}]


def test_score_execution_grammar_issue_keeps_500_characters(fakes, tpath):
    content = 'x' * 600
    fakes.tokens[content] = ValueError('e')
    findings = Findings()
    score(findings, {'response': response(content)}, tpath)
    assert findings.grammar_issues[0]['content'] == 'x' * 500


# -- unrecognised declines ------------------------------------------------

@pytest.mark.parametrize('phrase', DECLINE_PHRASES)
def test_score_execution_decline_phrase_is_a_finding(fakes, tpath, phrase):
    content = f'Sorry, {phrase.upper()} help.'
    findings = Findings()
    score(findings, {'response': response(content)}, tpath)
    assert findings.decline_findings == [{
        'item_id': 'Q01', 'condition': 'base', 'repeat': 2,
        'content_excerpt': content, 'configured_markers': ['cannot']}]


def test_score_execution_decline_excerpt_keeps_300_characters(fakes, tpath):
    content = 'I apologize. ' + 'y' * 400
    findings = Findings()
    score(findings, {'response': response(content)}, tpath)
    assert findings.decline_findings[0]['content_excerpt'] == content[:300]


def test_score_execution_recognised_decline_is_not_a_finding(fakes, tpath):
    fakes.figure = {'outcome': 'ADJUDICATE-DECLINE'}
    findings = Findings()
    score(findings, {'response': response("I can't do that.")}, tpath)
    assert findings.decline_findings == []


def test_score_execution_other_text_is_not_a_decline(fakes, tpath):
    findings = Findings()
    score(findings, {'response': response('The answer is 5.')}, tpath)
    assert findings.decline_findings == []


# -- tool-call structures -------------------------------------------------

def test_score_execution_records_each_calls_raw_arguments(fakes, tpath):
    calls = [calc('1 + 1', ''), {'id': 'x'},
             {'function': {'name': 'calculator'}}]
    findings = Findings()
    score(findings, {'tool_calls': calls}, tpath)
    assert [s['raw_arguments'] for s in findings.tool_call_structures] == [
        '{"expression": "1 + 1"}', '', '']
    assert findings.all_results[0]['tool_calls_count'] == 3


# -- operation correctness, read back from the transcript ----------------

def test_score_execution_takes_the_latest_engine_record_of_the_item(
        fakes, tpath):
    def engine_record(item_id, condition, outcome, **extra):
        transcript.append(tpath, item_id=item_id, arm_id=condition,
                          condition=condition, request_sent=None,
                          response_received=None, tool_calls=[],
                          evidence_class=None, error_state=None,
                          seal_hash='s',
                          operation_correctness=[{'outcome': outcome}],
                          **extra)
    engine_record('Q01', 'base', 'OLD')
    engine_record('Q01', 'base', 'LATEST')
    engine_record('Q02', 'base', 'OTHER ITEM')
    engine_record('Q01', 'removed', 'OTHER CONDITION')
    findings = Findings()
    score(findings, {}, tpath)
    assert findings.all_results[0]['operation_correctness'] == [
        {'outcome': 'LATEST'}]


def test_score_execution_engine_record_without_operation_correctness(
        fakes, tpath):
    transcript.append(tpath, item_id='Q01', arm_id='base', condition='base',
                      request_sent=None, response_received=None,
                      tool_calls=[], evidence_class=None, error_state=None,
                      seal_hash='s')
    findings = Findings()
    score(findings, {}, tpath)
    assert findings.all_results[0]['operation_correctness'] == []


def test_score_execution_d2_responses_accumulate_per_item_and_condition(
        fakes, tpath):
    findings = Findings()
    score(findings, {'response': 'r1'}, tpath)
    score(findings, {'response': 'r2'}, tpath)
    score(findings, {'response': 'r3'}, tpath, condition='removed')
    assert findings.d2_responses == {('Q01', 'base'): ['r1', 'r2'],
                                     ('Q01', 'removed'): ['r3']}


# -- executions that are not scored ---------------------------------------

def test_record_underivable():
    findings = Findings()
    record_underivable(findings, 'Q04', 'base')
    assert findings.all_results == [{'item_id': 'Q04', 'condition': 'base',
                                     'repeat': 0, 'status': 'VOID'}]
    assert findings.unmeasured_cells == []


def test_record_transport_failure():
    findings = Findings()
    record_transport_failure(findings, 'Q05', 'base', 3, 'rate_limited')
    assert findings.unmeasured_cells == [{'item_id': 'Q05',
                                          'condition': 'base', 'repeat': 3,
                                          'cause': 'rate_limited'}]
    assert findings.all_results == [{'item_id': 'Q05', 'condition': 'base',
                                     'repeat': 3, 'status': 'UNMEASURED',
                                     'cause': 'rate_limited'}]


@pytest.mark.parametrize('result, cause', [
    ({'error': 'E', 'reason': 'R'}, 'E'),
    ({'reason': 'R'}, 'R'),
    ({}, ''),
])
def test_record_not_scored(result, cause):
    findings = Findings()
    record_not_scored(findings, 'Q06', 'removed', 1, 'VOID', result)
    assert findings.all_results == [{'item_id': 'Q06', 'condition': 'removed',
                                     'repeat': 1, 'status': 'VOID',
                                     'cause': cause}]


def test_findings_start_empty_and_separate():
    a, b = Findings(), Findings()
    a.all_results.append(1)
    a.d2_responses['k'] = 1
    assert b == Findings()
    assert vars(b) == {
        'all_results': [], 'all_accuracy_results': [], 'd2_responses': {},
        'grammar_issues': [], 'decline_findings': [],
        'tool_call_structures': [], 'evidence_findings': [],
        'transcription_results': [], 'release_coverage_results': [],
        'unmeasured_cells': []}


# -- the real scoring modules, on a realistic response --------------------

def test_score_execution_with_real_scorers(tpath, capsys):
    content = 'The interest is $638.40.'
    result = {'response': response(content),
              'tool_calls': [calc('15200 * 0.042', '{"result": 638.4}')],
              'evidence_class': 'EV-2', 'invocation_outcome': 'INVOKED'}
    findings = Findings()
    score(findings, result, tpath,
          config={'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_UP'}})
    assert capsys.readouterr().out == 'AUTO-MATCH | EV-2 | INVOKED\n'
    row = findings.all_results[0]
    assert (row['figure_outcome'], row['released_figure'],
            row['transcription_outcome'],
            row['release_coverage_outcome']) == (
        'AUTO-MATCH', '638.40', 'TRANSCRIBED-EXACT', 'GOVERNED-RELEASE')


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-21', 'T3-52')
@pytest.mark.req('R0.3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-21: score_execution appends a '
                          'figure_identification record to the transcript')
def test_score_execution_transcript_left_byte_identical(fakes, tpath, capsys):
    # Correct (SPEC §2 "R2 SCORE: reads only; never writes back"; R0.3
    # "The scorer opens the transcript read-only"; Steven's ruling,
    # choices-for-marcus.md entry 1): scoring an execution leaves the
    # transcript as the engine wrote it.
    transcript.append(tpath, item_id='Q01', arm_id='base', condition='base',
                      request_sent={}, response_received={}, tool_calls=[],
                      evidence_class='EV-2', error_state=None,
                      seal_hash='seal-1')
    with open(tpath, 'rb') as f:
        before = f.read()
    score(Findings(), {'response': response('The total is $638.40.'),
                       'evidence_class': 'EV-2',
                       'invocation_outcome': 'NOT-INVOKED'}, tpath)
    with open(tpath, 'rb') as f:
        after = f.read()
    assert (len(after.splitlines()), after) == (1, before)
