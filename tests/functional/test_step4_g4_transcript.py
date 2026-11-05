"""Step 4: the transcript and the two-pass design,
end to end (raw-response preservation).

Correct behaviour, written failing in step 4 (each test was a strict xfail
with its finding):

- T3-21: SPEC §2 ("Two passes ... The separation is a conformance
  requirement"), R1.2 ("Perform no scoring"), R0.3 ("The scorer opens the
  transcript read-only"). The run writes the transcript with no scoring
  in it; scoring is a separate pass that reads the transcript and writes
  nothing back; re-scoring a finished run's transcript reproduces its
  scores. The maintainer's decision DEC-6 lists T3-21 (two passes).
- V12-3 / T3-52: SPEC R0.2 ("Every request and response is written to the
  transcript before any other processing"), AP-1 §5.6: every round of a
  tool loop, request and raw response, is in the transcript.
- T3-52: the other R0.2/R0.3 verification contracts (single-host egress,
  read-only scorer, interrupted run reported not-run).
- T3-35 (engine part): SPEC R1.3 ("EV-0 UNOBSERVABLE with the round
  identified"): an EV-0 execution's record carries its cause and round.

Each run is the real runner (ap1_run.run.main) against the regression
mock endpoint (tests/fixtures/mock_endpoint.py) on 127.0.0.1, with a copy
of the shipped example in tmp_path; nothing is written into the
repository.

The tests that need the re-scorer import it in one place, _rescore()
below:

    ap1_run.scoring.rescore.rescore_transcript(
        transcript_path, *, config_path, fixture_dir, output_dir) -> dict

It scores a finished (or partial) transcript, opening it read-only, and
returns the run summary: the same content as the run's smoke_summary.json
(without its '_disclaimer' line).

All of these were strict xfails written in step 4; the two-pass fix
(T3-21, V12-3) turned them green.
"""

import importlib.util
import json
import re
from decimal import Decimal
import os
import shutil
import stat
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from types import SimpleNamespace

import pytest

from ap1_run import run
from ap1_run.execution.evidence import EV_0
from ap1_run.foundation import adapter

# The runner warns that VERSION and git HEAD differ (any branch commit).
pytestmark = pytest.mark.filterwarnings('ignore:VERSION file says')

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
AP1_TEXT = ROOT / 'reference' / 'AP-1_v1.3_DRAFT_FOR_COMMENT.md'
SCORING_FIELDS = ('operation_correctness', 'provenance_results',
                  'figure_outcome', 'figure_reason', 'released_figure')



def _mock_endpoint_class():
    """tests/fixtures/mock_endpoint.py, loaded without writing bytecode
    into the repository."""
    path = ROOT / 'tests' / 'fixtures' / 'mock_endpoint.py'
    spec = importlib.util.spec_from_file_location('_g4_mock_endpoint', path)
    module = importlib.util.module_from_spec(spec)
    saved = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = saved
    return module.MockEndpoint


class MockEndpoint(_mock_endpoint_class()):
    """The regression mock, also keeping each reply's body: log entries
    get 'body', the JSON sent back (the log's own 'reply' is the status).
    close_once: (item_id, condition, round) whose first request is
    answered by closing the connection, so the adapter retries it."""

    close_once = frozenset()

    def handle(self, body):
        item_id, condition, rnd = self._identify(body)
        key = (item_id, condition, rnd)
        if key in self.close_once and key not in getattr(self, '_closed',
                                                         set()):
            self._closed = getattr(self, '_closed', set()) | {key}
            self.log.append({'seq': None, 'item_id': item_id,
                             'condition': condition, 'repeat': None,
                             'round': rnd, 'reply': 'close',
                             'request': body, 'retried': True})
            return ('close',)
        action = super().handle(body)
        if action[0] == 'reply':
            payload = action[2]
            self.log[-1]['body'] = (json.loads(payload)
                                    if isinstance(payload, str) else payload)
        return action


def _contains(tree, target):
    """True if target is tree or any value nested in it (dicts, lists)."""
    if tree == target:
        return True
    if isinstance(tree, dict):
        return any(_contains(v, target) for v in tree.values())
    if isinstance(tree, list):
        return any(_contains(v, target) for v in tree)
    return False


def _dicts(tree):
    """Every dict nested in tree (dicts and lists), tree included."""
    if isinstance(tree, dict):
        yield tree
        for v in tree.values():
            yield from _dicts(v)
    elif isinstance(tree, list):
        for v in tree:
            yield from _dicts(v)


def _read_jsonl(path):
    with open(path, encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]


def _rescore(transcript_path, *, config_path, fixture_dir, output_dir):
    """The scoring pass over a transcript (T3-21). See the module
    docstring."""
    from ap1_run.scoring.rescore import rescore_transcript
    return rescore_transcript(transcript_path, config_path=config_path,
                              fixture_dir=fixture_dir, output_dir=output_dir)


@pytest.fixture
def cli(tmp_path, monkeypatch):
    """Run the real runner over a copy of the example, against the mock
    endpoint: cli(responses, items=, repeat=, around_execute=).

    around_execute(real, *args, **kwargs), if given, replaces the runner's
    call to engine.execute_item (to observe or interrupt the run).
    Returns a namespace: code, error (an exception main() raised, or None),
    out, transcript, mock, fixture_dir, config_path.
    """
    monkeypatch.setattr(sys, 'path', list(sys.path))
    for name in ('ground_truth_example', 'calculator_tool'):
        monkeypatch.delitem(sys.modules, name, raising=False)
    for name in list(os.environ):
        if name.startswith('AP1_SMOKE_'):
            monkeypatch.delenv(name)
    monkeypatch.setattr(run.time, 'sleep', lambda s: None)
    monkeypatch.setattr(adapter.time, 'sleep', lambda s: None)
    counter = {'n': 0}

    def go(responses, *, items=('Q01', 'Q02'), repeat=1,
           around_execute=None):
        counter['n'] += 1
        fx = tmp_path / f'example{counter["n"]}'
        shutil.copytree(EXAMPLE, fx,
                        ignore=shutil.ignore_patterns('__pycache__'))
        questions = json.loads((fx / 'questions.json').read_text('utf-8'))
        questions['items'] = [i for i in questions['items']
                              if i['id'] in items]
        (fx / 'questions.json').write_text(json.dumps(questions), 'utf-8')
        config = json.loads((fx / 'config.json').read_text('utf-8'))
        config['repeat_count'] = str(repeat)
        # The shipped config claims D1 on 10 items, which minimum-n (R0.1)
        # refuses once wired (T3-12); claim only dimensions R0.1 sets no
        # minimum for, as tests/functional/test_step4_g9_spec_claims.py does.
        config['dimensions_claimed'] = ['D2', 'D7']
        (fx / 'config.json').write_text(json.dumps(config), 'utf-8')
        mock = MockEndpoint(
            api_key='sk-test',
            questions=questions,
            system_prompts={config['system_prompt_base']: 'base',
                            config['system_prompt_instruction_removed']:
                            'instruction_removed'},
            responses=responses).start()
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-test')
        mock.point_config(fx / 'config.json')  # T3-80: config only
        if around_execute is not None:
            real = run.execute_item
            monkeypatch.setattr(
                run, 'execute_item',
                lambda *a, **k: around_execute(real, *a, **k))
        out = tmp_path / f'out{counter["n"]}'
        code = error = None
        try:
            code = run.main(['--config', str(fx / 'config.json'),
                             '--fixture-dir', str(fx),
                             '--output-dir', str(out),
                             '--ap1-text', str(AP1_TEXT)])
        except BaseException as e:   # observed, not re-raised
            error = e
        finally:
            mock.stop()
            if around_execute is not None:
                monkeypatch.setattr(run, 'execute_item', real)
        return SimpleNamespace(code=code, error=error, out=out,
                               transcript=out / 'smoke_run.jsonl', mock=mock,
                               fixture_dir=fx,
                               config_path=fx / 'config.json')
    return go


ONE_ROUND = {'Q01/*/*': [{'call': '15200.00 * 1.2 / 100 / 12'},
                         {'say': 'The monthly interest is ${result}.'}],
             'Q02/*/*': [{'call': '5000 - 2400'},
                         {'say': 'The available credit is ${result}.'}]}

# Q05: three responses (two tool rounds, then the answer), with text in
# the intermediate rounds; Q02: two responses.
MULTI_ROUND = {
    'Q05/*/*': [
        {'calls': ['2400.00 * (18.0 / 100) / 12', '2400.00 - 25.00'],
         'say': 'First the monthly interest and the balance after the '
                'payment.'},
        {'call': '2375.0 + 36.0', 'say': 'Now adding the interest.'},
        {'say': 'The credit card balance after one month is ${result}.'}],
    'Q02/*/*': [{'call': '5000 - 2400'},
                {'say': 'The available credit is ${result}.'}]}


# -- T3-21: the two passes -------------------------------------------------

@pytest.mark.finding('T3-21')
@pytest.mark.req('R1.2', 'R0.3')
def test_run_transcript_contains_no_scoring(cli):
    # Correct (SPEC §2 diagram "R1 EXECUTE: no scoring occurs here", R1.2
    # "Perform no scoring", R0.3's record fields): the transcript holds
    # what happened, never a score.
    r = cli(ONE_ROUND)
    assert (r.code, r.error) == (0, None)
    records = _read_jsonl(r.transcript)
    scoring = sorted({key for rec in records for key in rec
                      if key in SCORING_FIELDS}
                     | {f"record_type={rec['record_type']}" for rec in records
                        if rec.get('record_type') == 'figure_identification'})
    assert scoring == []


@pytest.mark.finding('T3-21')
@pytest.mark.req('R0.3')
def test_run_transcript_is_only_what_the_execution_wrote(cli):
    # Correct (SPEC §2 "R2 SCORE: reads only; never writes back"): every
    # byte of the transcript is written by the execution pass
    # (engine.execute_item); scoring adds nothing, so the transcript after
    # the run is byte-identical to the concatenation of what each
    # execution wrote.
    written = []

    def around(real, *args, **kwargs):
        path = Path(kwargs['transcript_path'])
        before = path.read_bytes() if path.exists() else b''
        result = real(*args, **kwargs)
        after = path.read_bytes()
        assert after.startswith(before)
        written.append(after[len(before):])
        return result

    r = cli(ONE_ROUND, around_execute=around)
    assert (r.code, r.error) == (0, None)
    final = r.transcript.read_bytes()
    extra = len(final.splitlines()) - len(b''.join(written).splitlines())
    assert (extra, final) == (0, b''.join(written))


@pytest.mark.finding('T3-21')
@pytest.mark.req('R0.3', 'R2.0')
def test_rescore_of_finished_run_reproduces_its_summary(cli, tmp_path):
    # Correct (the maintainer's decision DEC-6, T3-21; SPEC §2 "A
    # single-pass design makes re-scoring impossible"): re-scoring a
    # finished run's transcript reproduces the run's scores, and leaves
    # the transcript byte-identical.
    r = cli(MULTI_ROUND, items=('Q02', 'Q05'), repeat=2)
    assert (r.code, r.error) == (0, None)
    before = r.transcript.read_bytes()
    summary = _rescore(r.transcript, config_path=r.config_path,
                       fixture_dir=r.fixture_dir,
                       output_dir=tmp_path / 'rescored')
    published = json.loads((r.out / 'smoke_summary.json').read_text('utf-8'))
    published.pop('_disclaimer')
    assert json.loads(json.dumps(summary, default=str)) == published
    assert r.transcript.read_bytes() == before


# -- V12-3 / T3-52: every round in the transcript ---------------------------

@pytest.mark.finding('V12-3', 'T3-52')
@pytest.mark.req('R0.2', 'R0.3', 'AP-1 §5.6')
def test_run_multi_round_every_raw_response_in_transcript(cli):
    # Correct (SPEC R0.2 "Every request and response is written to the
    # transcript before any other processing"; AP-1 §5.6): every response
    # the endpoint returned, as received (the whole body: id, usage,
    # finish_reason, not only the message), is in the transcript.
    r = cli(MULTI_ROUND, items=('Q02', 'Q05'), repeat=2)
    assert (r.code, r.error) == (0, None)
    records = _read_jsonl(r.transcript)
    assert len(r.mock.log) == 2 * 2 * 2 + 2 * 2 * 3   # 20 responses
    assert all(e['reply'] == 200 for e in r.mock.log)
    missing = [(e['item_id'], e['condition'], e['repeat'], e['round'])
               for e in r.mock.log if not _contains(records, e['body'])]
    assert missing == []


@pytest.mark.finding('V12-3', 'T3-52')
@pytest.mark.req('R0.2', 'R0.3', 'AP-1 §5.6')
def test_run_multi_round_every_request_in_transcript(cli, monkeypatch):
    # Correct (SPEC R0.2 "Every request and response is written to the
    # transcript ... The request as sent", with its sampling parameters
    # and its attempts): every request sent, round by round, is in the
    # record of its own execution, complete: a request record with the
    # model, messages and tools the endpoint received, the value of every
    # sampling parameter sent (in sampling_as_sent), and the attempts made
    # for it, each numbered and with a status or an error, the last one
    # HTTP 200. Round 1 of the base condition is answered first by a
    # dropped connection, so its record has two attempts, the first an
    # error. Today only the first request is kept, and its messages are
    # the list as it stood after the loop (S4-G4-1).
    monkeypatch.setattr(MockEndpoint, 'close_once',
                        frozenset({('Q05', 'base', 1)}))
    r = cli(MULTI_ROUND, items=('Q05',), repeat=1)
    assert (r.code, r.error) == (0, None)
    records = [rec for rec in _read_jsonl(r.transcript)
               if rec.get('record_type') != 'figure_identification']
    served = [e for e in r.mock.log if not e.get('retried')]
    assert [e['round'] for e in served] == [0, 1, 2] * 2

    def same(a, b):
        try:
            return Decimal(str(a)) == Decimal(str(b))
        except Exception:
            return a == b

    def attempts_ok(attempts, retried):
        if not attempts or not all(
                isinstance(a, dict) and isinstance(a.get('attempt'), int)
                and (isinstance(a.get('status_code'), int)
                     or isinstance(a.get('error'), str))
                for a in attempts):
            return False
        if attempts[-1].get('status_code') != 200:
            return False
        return (len(attempts) == 2 and attempts[0].get('error')) \
            if retried else len(attempts) == 1

    def complete(e):
        own = [rec for rec in records if rec['condition'] == e['condition']]
        sent = e['request']
        sampling = set(sent) - {'model', 'messages', 'tools'}
        retried = (e['condition'], e['round']) == ('base', 1)
        return any(
            d.get('messages') == sent['messages']
            and d.get('model') == sent['model']
            and d.get('tools') == sent.get('tools')
            and all(k in (d.get('sampling_as_sent') or {})
                    and same(d['sampling_as_sent'][k], sent[k])
                    for k in sampling)
            and attempts_ok(d.get('attempts'), retried)
            for d in _dicts(own))

    missing = [(e['condition'], e['round']) for e in served
               if not complete(e)]
    assert missing == []


# -- T3-52: the other R0.2 / R0.3 contracts --------------------------------

class _Server:
    """A one-route HTTP server on 127.0.0.1 that replies with handler()."""

    def __init__(self, handler):
        self.requests = []
        server = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                length = int(self.headers.get('Content-Length', 0))
                server.requests.append(self.rfile.read(length))
                status, headers, body = handler(self)
                self.send_response(status)
                for k, v in headers.items():
                    self.send_header(k, v)
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                pass

        self._server = HTTPServer(('127.0.0.1', 0), Handler)
        self.port = self._server.server_address[1]
        threading.Thread(target=self._server.serve_forever,
                         kwargs={'poll_interval': 0.02}, daemon=True).start()

    def close(self):
        self._server.shutdown()
        self._server.server_close()


@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.2')
def test_adapter_redirect_to_other_host_not_followed():
    # Correct (SPEC R0.2 verification contract: "The adapter makes no
    # network call to any host other than the configured endpoint"; §9
    # exfiltration mitigation): a 307 from the endpoint to another host
    # is not followed. The request (the messages, with the fixture data
    # in them) never reaches the other host; the send fails and
    # the item is UNMEASURED. Here the other host is "localhost" while the
    # endpoint is "127.0.0.1" (both loopback, so nothing leaves the
    # machine). Needs real HTTP, so it is here and not in the adapter's
    # unit file (which replaces the adapter's post).
    ok = json.dumps({'choices': [{'message': {
        'role': 'assistant', 'content': 'exfiltrated'}}]}).encode()
    other = _Server(lambda h: (200, {'Content-Type': 'application/json'},
                               ok))
    target = f'http://localhost:{other.port}/collect'
    endpoint = _Server(lambda h: (307, {'Location': target}, b''))
    try:
        try:
            adapter.send(
                f'http://127.0.0.1:{endpoint.port}/v1/chat/completions',
                messages=[{'role': 'user', 'content': 'secret context'}],
                model='m', api_key='sk-test', timeout=5)
        except adapter.AdapterError:
            pass
    finally:
        endpoint.close()
        other.close()
    assert len(endpoint.requests) == 1
    assert other.requests == []


@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.3')
def test_run_scoring_with_read_only_transcript_completes(cli):
    # Correct (SPEC R0.3 verification contract: "The scorer opens the
    # transcript read-only"): once an execution's record is written, the
    # scoring of it only reads the transcript, so it completes with the
    # file read-only. The file is made writable for each execution and
    # read-only again as soon as the execution returns.
    def around(real, *args, **kwargs):
        path = Path(kwargs['transcript_path'])
        if path.exists():
            path.chmod(stat.S_IRUSR | stat.S_IWUSR)
        try:
            return real(*args, **kwargs)
        finally:
            path.chmod(stat.S_IRUSR)

    r = cli(ONE_ROUND, around_execute=around)
    if r.transcript.exists():
        r.transcript.chmod(stat.S_IRUSR | stat.S_IWUSR)
    assert (r.code, repr(r.error)) == (0, 'None')


@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.3')
def test_interrupted_run_partial_transcript_scored_unreached_not_run(
        cli, tmp_path):
    # Correct (SPEC R0.3 verification contract: "An interrupted run leaves
    # a valid partial transcript; unreached items are reported not-run,
    # never as failures"). The run is interrupted (KeyboardInterrupt)
    # after its second execution. The partial transcript is valid JSONL
    # (this part holds today); scoring it reports the two unreached
    # executions as NOT-RUN and nothing as UNMEASURED or a failure.
    done = []

    def around(real, *args, **kwargs):
        if len(done) == 2:
            raise KeyboardInterrupt
        result = real(*args, **kwargs)
        done.append((args[0]['id'], kwargs['condition']))
        return result

    r = cli(ONE_ROUND, items=('Q01', 'Q02'), repeat=1,
            around_execute=around)
    assert isinstance(r.error, KeyboardInterrupt)
    _read_jsonl(r.transcript)   # valid JSONL, else JSONDecodeError
    summary = _rescore(r.transcript, config_path=r.config_path,
                       fixture_dir=r.fixture_dir,
                       output_dir=tmp_path / 'rescored')
    rows = {(row['item_id'], row['condition'], row['repeat']): row['status']
            for row in summary['all_results']}
    assert rows == {('Q01', 'base', 1): 'EXECUTED',
                    ('Q02', 'base', 1): 'EXECUTED',
                    ('Q01', 'instruction_removed', 1): 'NOT-RUN',
                    ('Q02', 'instruction_removed', 1): 'NOT-RUN'}
    assert summary['unmeasured_cells'] == []


@pytest.mark.finding('V12-3', 'T3-52')
@pytest.mark.req('R0.2', 'R0.3')
def test_run_interrupted_inside_a_tool_loop_keeps_its_rounds(
        cli, tmp_path, monkeypatch):
    # SPEC R0.2 ("Every request and response is written to the transcript
    # before any other processing"), R0.3. The run is interrupted while
    # running Q05/base's second tool turn (round 1's call): rounds 0 and 1
    # were received, and both are in the transcript as received. Scored
    # again, that execution is UNMEASURED (interrupted, round 1), not
    # NOT-RUN; the one after it was never reached.
    from ap1_run.execution import engine
    real_tool = engine._execute_tool
    seen = []

    def tool(name, arguments):
        seen.append(arguments)
        if len(seen) == 3:   # round 0 asks for two calls, round 1 for one
            raise KeyboardInterrupt
        return real_tool(name, arguments)
    monkeypatch.setattr(engine, '_execute_tool', tool)
    r = cli(MULTI_ROUND, items=('Q05',), repeat=1)
    assert isinstance(r.error, KeyboardInterrupt)
    records = _read_jsonl(r.transcript)
    assert [(rec.get('kind'), rec.get('round')) for rec in records] == [
        ('round', 0), ('round', 1)]
    received = [e['body'] for e in r.mock.log]
    assert len(received) == 2
    assert [rec['response_received'] for rec in records] == received
    summary = _rescore(r.transcript, config_path=r.config_path,
                       fixture_dir=r.fixture_dir,
                       output_dir=tmp_path / 'rescored')
    cause = ('interrupted: round 1: the run stopped during this execution, '
             'after the rounds the transcript holds')
    rows = {(row['item_id'], row['condition'], row['repeat']):
            (row['status'], row.get('cause')) for row in summary['all_results']}
    assert rows == {
        ('Q05', 'base', 1): ('UNMEASURED', cause),
        ('Q05', 'instruction_removed', 1): (
            'NOT-RUN', 'not reached: the transcript has no record of it')}
    assert summary['unmeasured_cells'] == [{
        'item_id': 'Q05', 'condition': 'base', 'repeat': 1, 'cause': cause}]
    report = (tmp_path / 'rescored' / 'report.md').read_text('utf-8')
    assert 'interrupted' in report


# -- T3-35 (engine part): the cause and round of an EV-0 --------------------

ANTHROPIC = {'id': 'msg_mock', 'type': 'message', 'role': 'assistant',
             'content': [{'type': 'text',
                          'text': 'The monthly interest is $15.20.'}],
             'stop_reason': 'end_turn'}


EV0_STATE = ("T3-35: error_state as {'cause': <non-empty text>, 'round': "
             "<int, the first request is round 0>}; the field names and the "
             "counting are this test's proposal, SPEC R1.3 says only 'the "
             "round identified'")


# What each cause's text must mention (part of the EV0_STATE proposal):
# broad word families, so wording is free but the causes can't be swapped.
CAUSE_WORDS = {
    'http': r'503|http|status',
    'transport': r'connect|transport|network|reset|closed|dropped|socket',
    'rate': r'rate|429|limit',
    'shape': r'shape|format|unrecogni[sz]ed|schema|pars|anthropic',
}


def _ev0_error_state(cli, second_round):
    """The error state of Q01/base, whose second request (round 1)
    fails or comes back in an unrecognised shape."""
    r = cli({'Q01/base/*': [{'call': '15200.00 * 1.2 / 100 / 12'},
                            second_round],
             'Q01/instruction_removed/*': ONE_ROUND['Q01/*/*']},
            items=('Q01',), repeat=1)
    records = [rec for rec in _read_jsonl(r.transcript)
               if rec['condition'] == 'base'
               and rec.get('record_type') != 'figure_identification'
               and rec.get('kind') != 'round']
    assert [rec['evidence_class'] for rec in records] == [EV_0]
    return records[0]['error_state']


@pytest.mark.proposal(EV0_STATE)
@pytest.mark.finding('T3-35')
@pytest.mark.req('R1.3', 'AP-1 D7.9')
@pytest.mark.parametrize('second_round, cause', [
    ({'http': 503, 'body': '{"error": "upstream down"}'}, 'http'),
    ({'close': True}, 'transport'),
    ({'raw': ANTHROPIC}, 'shape'),
], ids=['http-503', 'dropped-connection', 'unrecognised-shape'])
def test_run_ev0_record_names_cause_and_round(cli, second_round, cause):
    # Correct (SPEC R1.3 "the evidence class is EV-0 UNOBSERVABLE with the
    # round identified"; R0.3 record field "error state"): the transcript
    # record of an execution whose second round (round 1, counting the
    # first request as round 0) fails, or comes back in an unrecognised
    # shape, has evidence class EV-0 and an error state naming the cause
    # and the round, structured so the round can't be misread (EV0_STATE:
    # round 1, the first request being round 0). The HTTP case's cause
    # names the status; the other two causes are any non-empty text, and
    # test_run_ev0_causes_are_distinct checks they differ.
    error_state = _ev0_error_state(cli, second_round)
    assert isinstance(error_state, dict), error_state
    assert error_state.get('round') == 1, error_state
    assert isinstance(error_state.get('cause'), str) \
        and error_state['cause'].strip(), error_state
    others = [w for c, w in CAUSE_WORDS.items()
              if c not in (cause, 'rate')]
    assert re.search(CAUSE_WORDS[cause], error_state['cause'], re.I), \
        error_state
    assert not any(re.search(w, error_state['cause'], re.I)
                   for w in others), error_state


@pytest.mark.proposal(EV0_STATE)
@pytest.mark.finding('T3-35')
@pytest.mark.req('R1.3', 'AP-1 D7.9')
def test_run_ev0_causes_are_distinct(cli):
    # An HTTP error, a dropped connection and an unrecognised shape are
    # three causes; the record tells them apart.
    states = [_ev0_error_state(cli, second_round) for second_round in (
        {'http': 503, 'body': '{"error": "upstream down"}'},
        {'close': True}, {'raw': ANTHROPIC})]
    causes = [s.get('cause') if isinstance(s, dict) else s for s in states]
    assert None not in causes and len(set(causes)) == 3, causes


# -- S4-G4-1 (new): the round-0 request record is not the request as sent ----

def _round0_request_messages(cli):
    r = cli(MULTI_ROUND, items=('Q05',), repeat=1)
    assert (r.code, r.error) == (0, None)
    base = [rec for rec in _read_jsonl(r.transcript)
            if rec['condition'] == 'base'
            and rec.get('record_type') != 'figure_identification'
            and rec.get('kind') != 'round']
    sent = [e['request']['messages'] for e in r.mock.log
            if e['condition'] == 'base']
    return base[0]['request_sent']['request_record']['messages'], sent


@pytest.mark.finding('S4-G4-1')
@pytest.mark.req('R0.2')
def test_run_round0_request_record_is_the_request_as_sent(cli):
    # Correct (SPEC R0.2 "The request as sent -- not as constructed -- is
    # recorded"): the recorded round-0 request has exactly the messages
    # sent in round 0.
    recorded, sent = _round0_request_messages(cli)
    assert recorded == sent[0]
