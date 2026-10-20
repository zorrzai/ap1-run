"""Step 4, group g1-invocation: the correct behaviour of a whole run, for
the D7.1 aggregation and run-robustness findings (fix plan branches 1 and
10). Every test here fails on today's code and is marked xfail(strict).

Each test runs the real runner (ap1_run.run.main, nothing replaced)
against the regression mock endpoint (tests/fixtures/mock_endpoint.py) on
a copy of the shipped example in tmp_path, with the "clean" scenario's
scripted answers plus the test's own. It then reads what the run left:
its exit, its console, report.md, smoke_summary.json and the transcript.
"""

import json
import os
import re
import shutil
import sys
import time

import pytest

from ap1_run import run

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
EXAMPLE = os.path.join(ROOT, 'example')
CLEAN = os.path.join(ROOT, 'tests', 'regression', 'scenarios', 'clean.json')

# A run from a git checkout warns that VERSION is not HEAD (as in
# tests/unit/test_run.py's end-to-end test).
pytestmark = pytest.mark.filterwarnings('ignore:VERSION file says')


class Run:
    """What one run of the runner left behind."""

    def __init__(self, out, exit_code, exception, console, mock_log):
        self.out = out
        self.exit_code = exit_code
        self.exception = exception
        self.console = console
        self.requests = mock_log

    def file(self, name):
        path = os.path.join(self.out, name)
        if not os.path.exists(path):
            return None
        with open(path, encoding='utf-8') as f:
            return f.read()

    @property
    def report(self):
        return self.file('report.md')

    @property
    def summary(self):
        text = self.file('smoke_summary.json')
        return None if text is None else json.loads(text)

    @property
    def transcript(self):
        text = self.file('smoke_run.jsonl') or ''
        return [json.loads(line) for line in text.splitlines() if line]

    def results(self, item_id, condition):
        return [r for r in self.summary['all_results']
                if (r['item_id'], r['condition']) == (item_id, condition)]

    def report_section(self, number):
        """The text of report.md section <number> (up to the next ##)."""
        match = re.search(rf'^## {number}\..*?(?=^## |\Z)', self.report,
                          re.M | re.S)
        return match.group(0) if match else ''

    def console_section(self, label):
        """The console text from '<label>.' to the next numbered section."""
        match = re.search(rf'^{re.escape(label)}\..*?(?=^\d+[a-z]\d?\. |\Z)',
                          self.console.replace('\\n', '\n'), re.M | re.S)
        return match.group(0) if match else ''


@pytest.fixture
def full_run(tmp_path, monkeypatch, capsys):
    """full_run(responses, repeat_count=): run the runner end to end."""
    sys.path.insert(0, os.path.join(ROOT, 'tests', 'fixtures'))
    from mock_endpoint import MockEndpoint
    monkeypatch.setattr(sys, 'path', list(sys.path))
    for name in ('ground_truth_example', 'calculator_tool'):
        monkeypatch.delitem(sys.modules, name, raising=False)
    monkeypatch.setattr(time, 'sleep', lambda s: None)
    for name in list(os.environ):
        if name.startswith('AP1_SMOKE_'):
            monkeypatch.delenv(name)

    def go(responses, *, repeat_count='1'):
        fx = tmp_path / 'example'
        shutil.copytree(EXAMPLE, fx, ignore=shutil.ignore_patterns(
            '__pycache__'))
        config = json.loads((fx / 'config.json').read_text('utf-8'))
        config['repeat_count'] = repeat_count
        (fx / 'config.json').write_text(json.dumps(config), 'utf-8')
        questions = json.loads((fx / 'questions.json').read_text('utf-8'))
        with open(CLEAN, encoding='utf-8') as f:
            script = dict(json.load(f)['responses'])
        script.update(responses)
        mock = MockEndpoint(
            questions=questions,
            system_prompts={config['system_prompt_base']: 'base',
                            config['system_prompt_instruction_removed']:
                            'instruction_removed'},
            responses=script).start()
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-step4-not-a-real-key')
        mock.point_config(fx / 'config.json')  # T3-80: config only
        out = tmp_path / 'out'
        exit_code, exception = None, None
        try:
            exit_code = run.main(['--config', str(fx / 'config.json'),
                                  '--fixture-dir', str(fx),
                                  '--output-dir', str(out)])
        except Exception as e:  # recorded: the tests assert there is none
            exception = e
        finally:
            mock.stop()
        return Run(str(out), exit_code, exception, capsys.readouterr().out,
                   mock.log)
    return go


def assert_completed(r):
    """The run finished and wrote its report (no exception escaped)."""
    assert r.exception is None, (
        f'the run aborted: {type(r.exception).__name__}: {r.exception}')
    assert r.exit_code == 0
    assert r.report is not None and r.summary is not None


def anthropic_text(text):
    return {'raw': {'id': 'msg_mock', 'type': 'message', 'role': 'assistant',
                    'content': [{'type': 'text', 'text': text}],
                    'stop_reason': 'end_turn'}}


def chat_body(message):
    return {'raw': {'id': 'chatcmpl-mock', 'object': 'chat.completion',
                    'model': 'mock-model', 'choices': [
                        {'index': 0, 'message': message,
                         'finish_reason': 'stop'}]}}


def lines_with(text, *needles):
    return [line for line in text.splitlines()
            if all(n in line for n in needles)]


ALL_ITEMS = [f'Q{n:02d}' for n in range(1, 11)]


# -- T3-1: EV-0 is UNOBSERVABLE, not a success, in D7.1 -------------------

@pytest.mark.finding('T3-1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-1: EV-0 executions counted as INVOKED in the '
                          'D7.1 rate and bound')
def test_run_unrecognised_endpoint_prints_no_rate_or_bound(full_run):
    """An endpoint whose every response has a shape the runner cannot read
    gives EV-0 UNOBSERVABLE for every execution. Correct (SPEC R1.3.1 and
    R2.3, AP-1 v1.3 D7.7): EV-0 is not admissible and not an invocation,
    so D7.1 has no observations, and neither the report nor the console
    prints a zero-failure rate "n/n" with a bound. Today both print
    10/10 with a bound of 25.9 %."""
    r = full_run({f'{q}/*/*': [anthropic_text('The answer is $15.20.')]
                  for q in ALL_ITEMS})
    assert_completed(r)
    assert {e['evidence_class'] for e in r.summary['evidence_findings']} \
        == {'EV-0 UNOBSERVABLE'}
    section5 = r.report_section(5)
    assert not re.search(r'\b(\d+)/\1\b', section5), section5
    section3h = r.console_section('3h')
    assert 'upper bound' not in section3h, section3h


@pytest.mark.finding('T3-1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-1: EV-0 executions counted as INVOKED in the '
                          'D7.1 rate and bound; no evidence class in §5')
def test_run_mixed_classes_d71_counts_only_observed_and_names_classes(
        full_run):
    """Three base questions end EV-0 (an Anthropic-shaped answer after a
    call, a mid-loop HTTP 500, an Anthropic-shaped first answer); seven
    are EV-2 INVOKED. Correct (SPEC R2.3, R1.3.1 "Normative reporting",
    AP-1 v1.3 D7.7): the base D7.1 figure rests on the 7 observed
    questions (7/7), and the EV-0 executions are reported as such, per
    evidence class, not as successes. Today §5 prints 10/10 for base and
    names no class."""
    r = full_run({
        'Q01/base/*': [{'call': '15200.00 * 1.2 / 100 / 12'},
                       anthropic_text('The monthly interest is $15.20.')],
        'Q02/base/*': [{'call': '5000 - 2400'},
                       {'http': 500, 'body': '{"error": "internal"}'}],
        'Q03/base/*': [anthropic_text('The monthly interest is $36.00.')],
    })
    assert_completed(r)
    classes = [(e['item_id'], e['evidence_class'])
               for e in r.summary['evidence_findings']
               if e['condition'] == 'base']
    assert sorted(q for q, c in classes if c.startswith('EV-0')) == \
        ['Q01', 'Q02', 'Q03']
    section5 = r.report_section(5)
    base = lines_with(section5, 'base')
    assert base and not any('10/10' in line for line in base), section5
    assert any('7/7' in line for line in base), section5
    assert 'EV-0' in section5 and 'EV-2' in section5, section5


# -- T3-10: an empty response is UNMEASURED -------------------------------

@pytest.mark.finding('T3-10')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-10: empty response scored EXECUTED/NOT-INVOKED')
def test_run_empty_response_unmeasured_outside_d71(full_run):
    """Q01 answers with empty content and no tool call, under both
    conditions. Correct (SPEC R4.1 "Empty response -> UNMEASURED", R0.2,
    AP-1 v1.3 §13.2): the execution is UNMEASURED, listed among the
    non-outcome cells, and in no denominator, so the base D7.1 figure is
    9/9. Today it is EXECUTED/NOT-INVOKED, a failure in 1/10."""
    r = full_run({'Q01/*/*': [{'say': ''}]})
    assert_completed(r)
    assert [x['status'] for x in r.results('Q01', 'base')] == ['UNMEASURED']
    section10 = r.report_section(10)
    assert lines_with(section10, 'Q01', 'UNMEASURED'), section10
    base = lines_with(r.report_section(5), 'base')
    assert any('9/9' in line for line in base), base


# -- T3-11: the unit of D7.1 is the question ------------------------------

@pytest.mark.finding('T3-11')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-11: D7.1 bound pools repeats as n')
def test_run_d71_bound_counts_questions_not_repeats(full_run):
    """10 questions, 3 repeats each, every one invoked. Correct (AP-1
    v1.3 D7.1 "proportion of computable questions", the D7.5 example
    "49 items", DISPOSITION_RECORD GH-5 ACCEPTED; T3 review T3-11): n is
    the 10 questions, so the bound is 1 - 0.05^(1/10) = 25.89 %. Today
    n = 30 executions and the bound is 9.50 %, about 2.7 times too
    narrow (at 50 repeats, 43 times)."""
    r = full_run({}, repeat_count='3')
    assert_completed(r)
    base = lines_with(r.report_section(5), 'base')
    assert base and not any('30/30' in line for line in base), base
    assert any('10/10' in line and re.search(r'25\.8[89]', line)
               for line in base), base


# -- V12-5: the §6.2 headline ---------------------------------------------

@pytest.mark.finding('V12-5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='V12-5: no "invoked on X% of computable '
                          'questions" headline')
def test_run_report_states_invocation_headline_with_k_n_and_bound(full_run):
    """Correct (AP-1 v1.2/v1.3 §6.2 template "Deterministic computation
    was invoked on [X]% of computable questions, under [conditions]";
    fix plan row 1): the report states the rate as a percentage, with
    k/n and the bound, for each condition. Today §5 prints only "10/10"
    and the bound, and no percentage of questions."""
    r = full_run({})
    assert_completed(r)
    headlines = lines_with(r.report, 'of computable questions')
    assert len(headlines) >= 2, headlines
    for line in headlines[:2]:
        assert re.search(r'100(\.0+)?\s*%', line), line
        assert '10/10' in line and re.search(r'25\.8[89]|25\.9', line), line


# -- T3-65 / F4: round-0 transport errors fill the unmeasured cells -------

@pytest.mark.finding('T3-65', 'F4')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-65/F4: unmeasured-cells list empty after '
                          'round-0 transport errors')
def test_run_round0_transport_errors_listed_as_unmeasured_cells_with_cause(
        full_run):
    """Round 0 of Q03/base/r1 is rate limited (429), of Q04/base/r1 an
    HTTP 500, and Q05/base/r1's connection drops (three attempts).
    Correct (Steven's ruling, step-4 decisions F4 option 1;
    choices-for-marcus #7; SPEC R0.2): the engine keeps the transcript
    record and returns UNMEASURED, the run continues, and the runner's
    unmeasured-cells list (smoke_summary.json and console 3g) names each
    cell with its cause, a rate limit distinct from a transport error;
    the cells are in no denominator. Today the list is empty and 3g
    prints 0 next to "3 unmeasured"."""
    r = full_run({
        'Q03/base/r1': [{'http': 429,
                         'body': '{"error": {"message": "Rate limit"}}'}],
        'Q04/base/r1': [{'http': 500,
                         'body': '{"error": {"message": "server error"}}'}],
        'Q05/base/r1': [{'close': True}],
    })
    assert_completed(r)
    # The engine's side, unchanged by the fix: recorded, UNMEASURED.
    for q in ('Q03', 'Q04', 'Q05'):
        assert [x['status'] for x in r.results(q, 'base')] == ['UNMEASURED']
    assert 'TRANSPORT_FAILURE' in str(
        [t['error_state'] for t in r.transcript if t['item_id'] == 'Q03'])
    cells = {(c['item_id'], c['condition'], c['repeat']): c['cause']
             for c in r.summary['unmeasured_cells']}
    assert set(cells) == {('Q03', 'base', 1), ('Q04', 'base', 1),
                          ('Q05', 'base', 1)}, cells
    assert 'rate' in cells[('Q03', 'base', 1)].lower()
    assert 'rate' not in cells[('Q05', 'base', 1)].lower()
    assert 'transport' in cells[('Q05', 'base', 1)].lower()
    section3g = r.console_section('3g')
    assert '3' in section3g.splitlines()[0], section3g
    for q in ('Q03', 'Q04', 'Q05'):
        assert q in section3g, section3g


# -- T3-38: a call to a tool not offered is a legitimate NOT-INVOKED ------

@pytest.mark.finding('T3-38')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-38: call to an unoffered tool trips the FATAL '
                          'consistency check after all requests')
def test_run_call_to_unoffered_tool_recorded_not_invoked_run_completes(
        full_run):
    """Q06/base calls a tool named "python", which was not offered.
    Correct (SPEC R0.3 "calls not matching the declared required
    operation are recorded and reported but do not affect D7.1"; R2.3
    NOT-INVOKED is a legitimate outcome): the call is in the transcript,
    the execution is NOT-INVOKED, and the run completes with its report.
    Today the consistency check raises RuntimeError (FATAL) after every
    request is spent, and nothing is written."""
    r = full_run({'Q06/base/*': [
        {'calls': [{'name': 'python',
                    'arguments': '{"code": "print(12 * 12)"}'}]},
        {'say': 'The total annual cost is $144.00.'}]})
    assert_completed(r)
    [q06] = r.results('Q06', 'base')
    assert (q06['status'], q06['invocation_outcome']) == \
        ('EXECUTED', 'NOT-INVOKED')
    [record] = [t for t in r.transcript if t['item_id'] == 'Q06'
                and t['condition'] == 'base'
                and t.get('record_type') != 'figure_identification']
    assert [c['function']['name'] for c in record['tool_calls']] == \
        ['python']


# -- T3-39, F6, S3-G2-4: model-controlled input never aborts the run ------

@pytest.mark.finding('T3-39', 'F6', 'S3-G2-4', 'S3-G4-5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-39/F6/S3-G2-4/S3-G4-5: model-controlled '
                          'calculator input aborts the run')
@pytest.mark.parametrize('arguments', [
    '{"expression": 15.2}',             # T3-39: not a string
    '{"expression": "True * 15.2"}',    # T3-39: boolean literal
    '{"expression": "True + 1"}',       # F6
    '{"expression": "1e308*10"}',       # T3-39: the calculator returns inf
    '"15200 * 1.2 / 100 / 12"',         # S3-G2-4: JSON, not an object
    '["15200 * 1.2 / 100 / 12"]',       # S3-G2-4
], ids=['number', 'true-times', 'true-plus', 'overflow', 'json-string',
        'json-list'])
def test_run_model_controlled_calculator_input_run_completes(full_run,
                                                             arguments):
    """Q01/base calls the calculator with arguments the model controls.
    Correct (T3 review T3-39; Steven's ruling on F6, choices-for-marcus
    #9; S3-G2-4): no exception escapes, the run completes with its
    report, the call is recorded, and every other execution is scored.
    (The call's operands being unreadable/unobservable is asserted at
    unit level.) Today the run aborts after its paid requests. The
    boolean cases also cover S3-G4-5: with provenance fixed, the same
    run aborts next in operation_correctness.reclassify_session (called
    without a try at engine.py:138), checked on a scratch copy."""
    r = full_run({'Q01/base/*': [
        {'calls': [{'name': 'calculator', 'arguments': arguments}]},
        {'say': 'The monthly interest is $15.20.'}]})
    assert_completed(r)
    assert len(r.summary['all_results']) == 20
    [q01] = r.results('Q01', 'base')
    assert q01['status'] == 'EXECUTED'
    assert q01['tool_calls_count'] == 1


# -- S3-G2-1, S3-G2-2: platform-shaped surprises never abort the run ------

@pytest.mark.finding('S3-G2-1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G2-1: malformed response shape aborts the run')
@pytest.mark.parametrize('body', [
    {'choices': [{'index': 0, 'message': None, 'finish_reason': 'stop'}]},
    {'choices': ['The monthly interest is $15.20.']},
], ids=['null-message', 'str-choice'])
def test_run_malformed_response_shape_ev0_run_completes(full_run, body):
    """Q01/base's response is valid JSON in a shape the evidence code
    reports as unrecognised. Correct (S3-G2-1; SPEC R1.3 "if any round
    has an unrecognised shape ... EV-0 UNOBSERVABLE"): the execution is
    recorded as EV-0 (or UNMEASURED) and the run completes. Today
    engine._extract_tool_calls raises AttributeError and the run stops
    with no record and no report."""
    r = full_run({'Q01/base/*': [{'raw': body}]})
    assert_completed(r)
    [q01] = r.results('Q01', 'base')
    assert q01['status'] == 'UNMEASURED' or \
        q01['evidence_class'].startswith('EV-0'), q01


@pytest.mark.finding('S3-G2-2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G2-2: a tool call without an id aborts the '
                          'run')
def test_run_tool_call_without_id_executed_and_scored(full_run):
    """Q01/base's calculator call has no "id" (some OpenAI-compatible
    servers omit it). Correct (S3-G2-2): the call is executed, its
    return value is attached to its record, the execution is INVOKED,
    and the run completes. Today EngineError aborts the run."""
    call = {'type': 'function', 'function': {
        'name': 'calculator',
        'arguments': json.dumps({'expression': '15200.00 * 1.2 / 100 / 12'})}}
    r = full_run({'Q01/base/*': [
        chat_body({'role': 'assistant', 'content': None,
                   'tool_calls': [call]}),
        {'say': 'The monthly interest is $15.20.'}]})
    assert_completed(r)
    [q01] = r.results('Q01', 'base')
    assert q01['invocation_outcome'] == 'INVOKED'
    [record] = [t for t in r.transcript if t['item_id'] == 'Q01'
                and t['condition'] == 'base'
                and t.get('record_type') != 'figure_identification']
    assert 'result' in json.loads(record['tool_calls'][0]['return_value'])
