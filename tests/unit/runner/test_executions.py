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
        'record_type': 'figure_identification', 'repeat': 2,
        'figure_outcome': 'AUTO-MATCH', 'figure_reason': 'one figure', 'released_figure': '638.40',
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
        'release_coverage_outcome': 'PARTIALLY-GOVERNED',
        'answer_outcome': 'COMPUTED',
        'answer_outcome_reason': 'correct figure; computation invoked; '
                                 'operands grounded'}]


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
        'TRANSCRIBED-EXACT', 'release_coverage_outcome': 'PARTIALLY-GOVERNED',
        'answer_outcome': None, 'answer_outcome_reason':
        'no figure released: the record does not decide the outcome'}]
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
# Group g7-report (fix branch 7). xfail(strict=True) until the fix.

@pytest.mark.finding('T3-75')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-75: structured_answer_field is not passed to '
                          'identify_figure, so R2.0 step 1 never runs live')
def test_score_execution_passes_structured_answer_field(fakes, tpath):
    # SPEC R2.0 step 1: "If structured_answer_field is configured and
    # present, that value is the released figure. Preferred path." The
    # config loader parses the field (R0.1). Correct: score_execution
    # passes the configured field to identify_figure.
    config = dict(CONFIG, structured_answer_field='answer')
    score(Findings(), {'response': response('It is $638.40.')}, tpath,
          config=config)
    (_, kwargs), = fakes.calls['identify_figure']
    assert kwargs.get('structured_answer_field') == 'answer', kwargs


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


HALF_UP_2 = {'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_UP'}}
GT_CALCULATOR = {'required_operation': 'calculator'}


def tool(name, return_value):
    """A call to a tool other than the calculator."""
    return {'id': 'o1', 'type': 'function',
            'function': {'name': name, 'arguments': '{}'},
            'return_value': return_value}


def real_score(tool_calls, content, expected, config=HALF_UP_2):
    """Score one execution with the real scorers; the findings."""
    import tempfile
    import os
    findings = Findings()
    with tempfile.TemporaryDirectory() as d:
        score(findings, {'response': response(content),
                         'tool_calls': tool_calls,
                         'ground_truth': GT_CALCULATOR,
                         'evidence_class': 'EV-2',
                         'invocation_outcome': 'INVOKED'},
              os.path.join(d, 'run.jsonl'), expected=D(expected),
              config=config)
    return findings


@pytest.mark.finding('T3-26')
@pytest.mark.req('R2.5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-26: D7.3 compares only the last tool return; '
                          'a release of an earlier return is ALTERED')
def test_score_execution_release_of_earlier_calculator_return_is_exact(
        capsys):
    # SPEC R2.5: compare "the value the required operation returned" to
    # the released figure; fix plan branch 8: compare against every return
    # of the required operation. The Q04 pattern: the answer 430.75 is
    # returned first, then the model checks it (430.75 + 1006.25 = 1437).
    calls = [calc('1437.00 - 1006.25', '{"result": 430.75}'),
             calc('430.75 + 1006.25', '{"result": 1437.0}')]
    f = real_score(calls, 'The principal portion is $430.75.', '430.75')
    assert f.all_results[0]['figure_outcome'] == 'AUTO-MATCH'
    assert f.transcription_results[0]['outcome'] == 'TRANSCRIBED-EXACT'


@pytest.mark.finding('T3-26')
@pytest.mark.req('R2.5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-26: an errored last call hides an earlier '
                          'matching return; D7.3 is UNOBSERVABLE')
def test_score_execution_errored_last_call_keeps_earlier_return(capsys):
    # T3-26: "if the last call errored, the execution is UNOBSERVABLE even
    # when an earlier return matches". The calculator did return the
    # released figure, so D7.3 is observable and EXACT (SPEC R2.5).
    calls = [calc('1437.00 - 1006.25', '{"result": 430.75}'),
             calc('430.75 / 0', '{"error": "division by zero"}')]
    f = real_score(calls, 'The principal portion is $430.75.', '430.75')
    assert f.transcription_results[0]['outcome'] == 'TRANSCRIBED-EXACT'


@pytest.mark.finding('T3-26')
@pytest.mark.req('R2.5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-26: the return of a tool other than the '
                          'required operation decides D7.3')
def test_score_execution_other_tools_return_does_not_govern_transcription(
        capsys):
    # SPEC R2.5 names the REQUIRED operation (ground truth
    # required_operation: calculator). Here the calculator returned
    # 1437.00 and another tool returned 430.75; the released 430.75 is not
    # what the required operation returned, so ALTERED (today: EXACT,
    # because the last return of any tool is taken).
    calls = [calc('1437.00', '{"result": 1437.0}'),
             tool('lookup', '{"result": "430.75"}')]
    f = real_score(calls, 'The principal portion is $430.75.', '430.75')
    assert f.all_results[0]['figure_outcome'] == 'AUTO-MATCH'
    assert f.transcription_results[0]['outcome'] == 'TRANSCRIBED-ALTERED'


@pytest.mark.finding('T3-27')
@pytest.mark.req('R2.5', 'R0.4.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-27: the declared ROUND_HALF_UP is not passed '
                          'to the transcription check')
def test_score_execution_transcription_uses_declared_rounding(capsys):
    # SPEC R0.4.1: the declared rounding mode. Under the declared
    # ROUND_HALF_UP the tool's 430.745 is 430.75, so releasing 430.75 is
    # EXACT (today ALTERED: HALF_EVEN gives 430.74). Release coverage,
    # which does use the declared mode, already says GOVERNED-RELEASE.
    f = real_score([calc('861.49 / 2', '{"result": 430.745}')],
                   'The principal portion is $430.75.', '430.745')
    assert f.release_coverage_results[0]['outcome'] == 'GOVERNED-RELEASE'
    assert f.transcription_results[0]['outcome'] == 'TRANSCRIBED-EXACT'


@pytest.mark.finding('T3-27')
@pytest.mark.req('R2.1', 'R0.4.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-27: the declared ROUND_HALF_UP is not passed '
                          'to D1 accuracy')
def test_score_execution_accuracy_uses_declared_rounding(capsys):
    # The T3 SCORE checker's boundary case: 2.005 vs 2.015, tolerance
    # 0.01. Under the declared ROUND_HALF_UP they quantise to 2.01 and
    # 2.02, within tolerance: CORRECT (today INCORRECT, 2.00 vs 2.02).
    f = real_score([], 'The answer is 2.005.', '2.015')
    assert f.all_results[0]['figure_outcome'] == 'AUTO-MATCH'
    assert f.all_accuracy_results[0]['outcome'] == 'CORRECT'


@pytest.mark.finding('V12-6')
@pytest.mark.req('R2.5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='V12-6: the collected D7.3 result has no "rounded '
                          'under declared policy" sub-flag')
def test_score_execution_transcription_result_carries_rounded_flag(capsys):
    # Fix plan §2a, V12-6: each D7.3 result carries the sub-flag, so the
    # report can count it. Q07: tool 777.4125, released 777.41.
    f = real_score([calc('42175 * (0.078 / 4) - (15 * 3)',
                         '{"result": 777.4125}')],
                   'The quarterly net growth is $777.41.', '777.4125')
    tr = f.transcription_results[0]
    assert tr['outcome'] == 'TRANSCRIBED-EXACT'
    assert tr.get('rounded_under_declared_policy') is True


EUROPEAN = {'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_UP'},
            'decimal_separator': ',', 'grouping_separator': '.'}


@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-41: the configured separators are not passed '
                          'to figure identification')
def test_score_execution_figure_parsed_with_configured_separators(capsys):
    # SPEC R0.4.2: a token is grouped by the configured grouping_separator
    # and has the configured decimal_separator. Under ',' decimal and '.'
    # grouping, '1.006,25' is one figure, 1006.25 (Q04's monthly interest).
    # Today the US defaults split it into 1.006 and 25: no match.
    f = real_score([], 'Die Zinsen betragen 1.006,25 $.', '1006.25',
                   config=EUROPEAN)
    assert f.all_results[0]['figure_outcome'] == 'AUTO-MATCH'
    assert f.all_results[0]['released_figure'] == '1006.25'


@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2', 'R2.5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-41: the configured separators are not passed '
                          'to release-coverage extraction')
def test_score_execution_coverage_candidates_parsed_with_configured_separators(
        capsys):
    # T3-41: under European separators coverage "silently becomes
    # UNOBSERVABLE". Correct: '1.006,25' is the candidate 1006.25, which
    # the calculator returned, so GOVERNED-RELEASE.
    f = real_score([calc('287500 * 4.2 / 100 / 12', '{"result": 1006.25}')],
                   'Die Zinsen betragen 1.006,25 $.', '1006.25',
                   config=EUROPEAN)
    assert f.release_coverage_results[0]['outcome'] == 'GOVERNED-RELEASE'


@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-41: a token ambiguous under the configured '
                          'separators is read with the US defaults and '
                          'auto-scored')
def test_score_execution_locale_ambiguous_figure_routes_to_adjudication(
        capsys):
    # SPEC R0.4.2: where the configuration does not disambiguate (here '.'
    # is both decimal and grouping separator), '1.780' admits two readings
    # and "the item routes to adjudication". Today it is read as 1.780
    # under the defaults and auto-matched.
    config = {'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_UP'},
              'decimal_separator': '.', 'grouping_separator': '.'}
    try:
        f = real_score([], 'The answer is 1.780.', '1.78', config=config)
        outcome = f.all_results[0]['figure_outcome']
    except Exception as e:  # the fix must route, not raise
        outcome = f'raised {type(e).__name__}: {e}'
    assert outcome.startswith('ADJUDICATE')


NO_FIGURE = {'outcome': 'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING',
             'reason': '1 numeric tokens found, none matching expected',
             'released_figure': None}


@pytest.mark.finding('S4-G9-1')
def test_score_execution_no_released_figure_written_as_string_none(fakes,
                                                                    tpath):
    # Current behaviour: identify_figure gives released_figure None for
    # every outcome that releases no figure, and score_execution writes
    # str(None), so the transcript and smoke_summary.json say "None" (the
    # no-key case writes ''). Correct: no figure is recorded as null.
    fakes.figure = dict(NO_FIGURE)
    findings = Findings()
    score(findings, {'response': response('It is $15.25.'),
                     'tool_calls': []}, tpath)
    assert transcript.read_all(tpath)[-1]['released_figure'] == 'None'
    assert findings.all_results[0]['released_figure'] == 'None'


@pytest.mark.finding('S4-G9-1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="S4-G9-1: no released figure is written as the "
                          "string 'None'")
def test_score_execution_no_released_figure_recorded_as_null(fakes, tpath):
    # R0.3: the transcript records what happened; a figure that was not
    # released is null, not the text "None".
    fakes.figure = dict(NO_FIGURE)
    findings = Findings()
    score(findings, {'response': response('It is $15.25.'),
                     'tool_calls': []}, tpath)
    assert transcript.read_all(tpath)[-1]['released_figure'] is None
    assert findings.all_results[0]['released_figure'] is None

# Group g1-invocation (fix plan branch 10).

@pytest.mark.finding('T3-65', 'F4')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-65/F4: engine UNMEASURED results never reach '
                          'unmeasured_cells')
@pytest.mark.parametrize('error, word', [
    ('rate limited (HTTP 429): {"error": "Rate limit"}', 'rate'),
    ('transport failure after 3 attempts: reset', 'transport'),
], ids=['rate-limited', 'transport'])
def test_record_not_scored_unmeasured_listed_with_cause(error, word):
    # Correct (Steven's ruling on F4, choices-for-marcus #7): the engine
    # returns UNMEASURED for a failed round-0 request; the runner lists
    # that cell among the unmeasured cells, with its cause, as well as in
    # all_results.
    findings = Findings()
    record_not_scored(findings, 'Q03', 'base', 1, 'UNMEASURED',
                      {'status': 'UNMEASURED', 'error': error})
    assert [(c['item_id'], c['condition'], c['repeat'])
            for c in findings.unmeasured_cells] == [('Q03', 'base', 1)]
    assert word in findings.unmeasured_cells[0]['cause'].lower()
    assert [r['status'] for r in findings.all_results] == ['UNMEASURED']
