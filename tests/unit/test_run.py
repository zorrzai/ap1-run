"""Unit tests for run.py's main(): the orchestration of a live run.

main() runs the execution pass, then hands the transcript to the scoring
pass (runner/scoring_pass.py, tested in tests/unit/runner/
test_scoring_pass.py). Its collaborators (the engine, the seal, the
scoring pass, the re-scorer) have their own tests. Here they are replaced
by recording fakes, so that the order of the run, what main() passes to
each, and what it prints are checked exactly. The inputs are small files
in a temporary directory, reached through the command-line options. The
last tests run main() end to end, with nothing replaced, against the mock
endpoint, and re-score its transcript.
"""

import json
import os
import re
import shutil
import sys
from decimal import Decimal

import pytest

from ap1_run import run
from ap1_run.execution.seal import SealError

D = Decimal
REPO = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

GROUND_TRUTH = '''
from decimal import Decimal

def compute(item_id, ctx):
    if item_id == 'Q3':
        return {'derivable': False}
    if item_id == 'Q2':
        return {'final': Decimal('10.00')}   # derivable by default
    return {'final': Decimal('10.00'), 'derivable': True}
'''

CONFIG = {
    'endpoint_url': 'http://mock/v1',
    'model': 'mock-model',
    'system_prompt_base': 'BASE PROMPT',
    'system_prompt_instruction_removed': 'REMOVED PROMPT',
    'tools': [{'type': 'function', 'function': {'name': 'calculator'}}],
    'repeat_count': 2,
    'sampling': {'temperature': 0},
    'answer_tolerance': '0.05',
    'decline_markers': ['cannot'],
    'currency_symbols': ['$'],
}
# Q3, the underivable item, is in the middle: the items after it still run.
QUESTIONS = {'items': [{'id': 'Q1', 'source_accounts': ['a'],
                        'category': 'interest'},
                       {'id': 'Q3', 'source_accounts': []},
                       {'id': 'Q2', 'source_accounts': ['b'],
                        'category': 'fees'}]}
# b.fee equals Q2's expected 10.00: a lookup collision found at seal
FIXTURE = {'accounts': [{'id': 'a'}, {'id': 'b', 'fee': '10.00'}]}


class Run:
    """Recording fakes for main()'s collaborators, and the inputs."""

    def __init__(self, tmp_path, monkeypatch):
        self.tmp = tmp_path
        self.fixture_dir = tmp_path / 'fx'
        self.fixture_dir.mkdir()
        self.output_dir = tmp_path / 'out' / 'run1'
        self.config = json.loads(json.dumps(CONFIG))
        self.write_inputs()
        self.calls = []
        self.results = {}     # (item, condition, rep) -> result
        self.refuse = set()   # R3.1 guards that raise SealError
        self.verify_refusals = []  # verify_seal calls that raise, by index
        self.version = {'version_tag': 'v9.9.9',
                        'version_commit': '0123456789abcdef0123'}
        monkeypatch.setattr(sys, 'path', list(sys.path))
        monkeypatch.delitem(sys.modules, 'ground_truth_example',
                            raising=False)
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-0123456789')
        for name in ('AP1_SMOKE_TEMPERATURE', 'AP1_SMOKE_REASONING_EFFORT'):
            monkeypatch.delenv(name, raising=False)
        monkeypatch.setattr(run.time, 'sleep',
                            lambda s: self.calls.append(('sleep', s)))
        for name in ('load_config', 'resolve_runner_version',
                     'compute_runner_source_hash',
                     'perturbation_check', 'source_fields_check',
                     'declared_constants_check',
                     'create_seal', 'verify_seal', 'check_condition_guard',
                     'build_delivered_context', 'write_pre_registration',
                     'execute_item', 'score_run', 'rescore_transcript'):
            monkeypatch.setattr(run, name, getattr(self, name))

    def write_inputs(self, config=None):
        fx = self.fixture_dir
        (fx / 'config.json').write_text(json.dumps(config or self.config))
        (fx / 'fixture.json').write_text(json.dumps(FIXTURE))
        (fx / 'questions.json').write_text(json.dumps(QUESTIONS))
        (fx / 'ground_truth_example.py').write_text(GROUND_TRUTH)

    def argv(self):
        return ['--config', str(self.fixture_dir / 'config.json'),
                '--fixture-dir', str(self.fixture_dir),
                '--output-dir', str(self.output_dir),
                '--ap1-text', str(self.tmp / 'ap1.md')]

    def main(self):
        return run.main(self.argv())

    def named(self, name):
        return [c[1:] for c in self.calls if c[0] == name]

    # -- fakes ---------------------------------------------------------
    def load_config(self, path):
        # The real load_config validates every field; main() is tested
        # here with whatever config it is given, with answer_tolerance
        # parsed to Decimal as load_config does.
        self.config_path = path
        config = json.loads(json.dumps(self.config))
        if isinstance(config.get('answer_tolerance'), str):
            config['answer_tolerance'] = D(config['answer_tolerance'])
        return config

    def resolve_runner_version(self, base_dir):
        self.calls.append(('version', base_dir))
        return dict(self.version)

    def compute_runner_source_hash(self, base_dir):
        self.calls.append(('source_hash', base_dir))
        return 'feedfacecafebeef' + '0' * 48

    def _gt_guard(self, name, module, fixture, questions):
        self.calls.append(('gt_guard', name, module, fixture, questions))
        if name in self.refuse:
            raise SealError(f'{name} refused')
        return []

    def perturbation_check(self, *args):
        return self._gt_guard('perturbation', *args)

    def source_fields_check(self, *args):
        return self._gt_guard('source_fields', *args)

    def declared_constants_check(self, *args):
        return self._gt_guard('declared_constants', *args)

    def create_seal(self, **kwargs):
        self.calls.append(('seal', kwargs))
        return {'seal_hash': 'SEAL', 'ap1_text_hash': 'TEXTHASH',
                'lookup_collisions': 'COLLISIONS'}

    def verify_seal(self, record, **kwargs):
        self.calls.append(('verify_seal', record, kwargs))
        if len(self.named('verify_seal')) in self.verify_refusals:
            raise SealError('seal verification failed:\n  fixture: changed')
        return True

    def check_condition_guard(self, *args):
        self.calls.append(('guard',) + args)
        # Each condition's checked request; marked, so that the test sees
        # the engine is given these and not the config's own values.
        base, removed, tools = args[2], args[3], args[4]
        return {'base': {'system_prompt': base + ' (checked)',
                         'tools': ['base'] + tools},
                'instruction_removed': {'system_prompt': removed + ' (checked)',
                                        'tools': ['removed'] + tools}}

    def build_delivered_context(self, fixture, accounts):
        self.calls.append(('context', fixture, accounts))
        return {'accounts': list(accounts)}

    def write_pre_registration(self, output_dir, **kwargs):
        self.calls.append(('pre_registration', output_dir, kwargs))

    def execute_item(self, item, **kwargs):
        self.calls.append(('execute', item, kwargs))
        return self.results.get(
            (item['id'], kwargs['condition'], kwargs['repeat']),
            {'status': 'EXECUTED', 'evidence_class': 'EV-2',
             'invocation_outcome': 'INVOKED'})

    def score_run(self, transcript_path, **kwargs):
        self.calls.append(('score_run', transcript_path, kwargs))
        print('(scoring pass)')
        return {'smoke': 'summary'}

    def rescore_transcript(self, transcript_path, **kwargs):
        self.calls.append(('rescore', transcript_path, kwargs))
        print('(re-scoring)')
        return {'smoke': 'summary'}


@pytest.fixture
def r(tmp_path, monkeypatch):
    return Run(tmp_path, monkeypatch)


RULE = '=' * 60


def script_statuses(r):
    # Each not-executed status is on a first repeat; the second still runs.
    # A failed request comes back from the engine UNMEASURED with its
    # cause (F4, T3-65); nothing is raised.
    r.results[('Q1', 'base', 1)] = {'status': 'UNMEASURED',
                                    'error': 'slow down',
                                    'cause': 'rate_limited'}
    r.results[('Q2', 'base', 1)] = {'status': 'UNMEASURED',
                                    'error': 'HTTP 500: boom',
                                    'cause': 'transport_error'}
    r.results[('Q1', 'instruction_removed', 1)] = {'status': 'VOID',
                                                  'reason': 'underivable'}
    r.results[('Q2', 'instruction_removed', 1)] = {
        'status': 'EXECUTED', 'evidence_class': 'EV-0 UNOBSERVABLE',
        'invocation_outcome': None}


def test_main_full_run_console(r, capsys):
    script_statuses(r)
    assert r.main() == 0
    out = os.path.join(str(r.output_dir), 'smoke_run.jsonl')
    assert capsys.readouterr().out == (
        'Endpoint: http://mock/v1\n'
        'Model: mock-model\n'
        'API key: present (13 chars)\n'
        '\n'
        '  temperature=0\n'
        '  reasoning_effort=None (from config)\n'
        'Runner version: v9.9.9 (0123456789ab)\n'
        'Runner source hash: feedfacecafebeef...\n'
        '\n'
        'Ground-truth guards (R3.1): PASSED (perturbation, source fields, '
        'declared constants)\n'
        '\n'
        'Lookup collisions (R3.1): COLLISIONS\n'
        'Seal hash: SEAL\n'
        'AP-1 text hash: TEXTHASH\n'
        '\n'
        'Running 3 items x 2 conditions x 2 repeats\n'
        'Total requests: 12\n'
        f'{RULE}\n'
        '  Q1/base/r1: UNMEASURED\n'
        '  Q1/base/r2: EXECUTED | EV-2 | INVOKED\n'
        '  Q3/base: VOID (underivable)\n'
        '  Q2/base/r1: UNMEASURED\n'
        '  Q2/base/r2: EXECUTED | EV-2 | INVOKED\n'
        '  Q1/instruction_removed/r1: VOID\n'
        '  Q1/instruction_removed/r2: EXECUTED | EV-2 | INVOKED\n'
        '  Q3/instruction_removed: VOID (underivable)\n'
        '  Q2/instruction_removed/r1: EXECUTED | EV-0 UNOBSERVABLE | None\n'
        '  Q2/instruction_removed/r2: EXECUTED | EV-2 | INVOKED\n'
        '\n'
        'SCORING THE TRANSCRIPT (scoring pass: reads it, writes nothing '
        'back)\n'
        f'{RULE}\n'
        '(scoring pass)\n'
        f'Transcript written to {out}\n')


@pytest.mark.finding('T3-21')
def test_main_full_run_calls(r, capsys):
    script_statuses(r)
    assert r.main() == 0
    fx = str(r.fixture_dir)
    out = str(r.output_dir)
    transcript = os.path.join(out, 'smoke_run.jsonl')

    assert r.config_path == os.path.join(fx, 'config.json')
    assert r.named('version') == [(run.BASE_DIR,)]
    assert r.named('source_hash') == [(run.BASE_DIR,)]
    guards = r.named('gt_guard')
    assert [g[0] for g in guards] == [
        'perturbation', 'source_fields', 'declared_constants']
    assert all(g[1] is sys.modules['ground_truth_example']
               and g[2] == FIXTURE and g[3] == QUESTIONS for g in guards)
    (seal,), = r.named('seal')
    config = seal.pop('config')
    # T3-48: the expected values of every item, computed before the seal;
    # T3-72: the bytes read are the bytes sealed.
    expected_values = {'Q1': {'final': D('10.00'), 'derivable': True},
                       'Q3': {'derivable': False},
                       'Q2': {'final': D('10.00')}}
    assert seal == {
        'fixture_path': os.path.join(fx, 'fixture.json'),
        'questions_path': os.path.join(fx, 'questions.json'),
        'ground_truth_path': os.path.join(fx, 'ground_truth_example.py'),
        'ap1_text_path': str(r.tmp / 'ap1.md'),
        'runner_source_hash': 'feedfacecafebeef' + '0' * 48,
        'lookup_collisions': [('Q2', 'b.fee')],
        'expected_values': expected_values,
        'loaded': {'fixture': json.dumps(FIXTURE).encode(),
                   'questions': json.dumps(QUESTIONS).encode(),
                   'ground_truth': GROUND_TRUTH.encode()}}
    # T3-17: the seal is verified, the whole record and every input,
    # before the first request and again before anything is reported.
    verified = {
        'config': config,
        'fixture_path': os.path.join(fx, 'fixture.json'),
        'questions_path': os.path.join(fx, 'questions.json'),
        'ground_truth_path': os.path.join(fx, 'ground_truth_example.py'),
        'ap1_text_path': str(r.tmp / 'ap1.md'),
        'runner_source_hash': 'feedfacecafebeef' + '0' * 48,
        'expected_values': expected_values}
    assert r.named('verify_seal') == [
        ({'seal_hash': 'SEAL', 'ap1_text_hash': 'TEXTHASH',
          'lookup_collisions': 'COLLISIONS'}, verified)] * 2
    assert config['endpoint_url'] == 'http://mock/v1'
    assert config['model'] == 'mock-model'
    assert (config['runner_version_tag'], config['runner_version_commit'],
            config['runner_modified']) == (
        'v9.9.9', '0123456789abcdef0123', False)

    assert r.named('guard') == [(
        config, os.path.join(fx, 'fixture.json'), 'BASE PROMPT',
        'REMOVED PROMPT', CONFIG['tools'], {'temperature': 0})]

    # the pre-registration record, beside the transcript
    seal_record = {'seal_hash': 'SEAL', 'ap1_text_hash': 'TEXTHASH',
                   'lookup_collisions': 'COLLISIONS'}
    assert r.named('pre_registration') == [(
        out, {'seal_record': seal_record, 'config': config})]

    # contexts: per item and condition
    assert [c[1] for c in r.named('context')] == [
        ['a'], [], ['b'], ['a'], [], ['b']]
    assert all(c[0] == FIXTURE for c in r.named('context'))

    executes = r.named('execute')
    assert [(i['id'], k['condition'], k['system_prompt'])
            for i, k in executes] == [
        ('Q1', 'base', 'BASE PROMPT (checked)'),
        ('Q1', 'base', 'BASE PROMPT (checked)'),
        ('Q2', 'base', 'BASE PROMPT (checked)'),
        ('Q2', 'base', 'BASE PROMPT (checked)'),
        ('Q1', 'instruction_removed', 'REMOVED PROMPT (checked)'),
        ('Q1', 'instruction_removed', 'REMOVED PROMPT (checked)'),
        ('Q2', 'instruction_removed', 'REMOVED PROMPT (checked)'),
        ('Q2', 'instruction_removed', 'REMOVED PROMPT (checked)')]
    assert [k['tools'][0] for _, k in executes] == ['base'] * 4 + [
        'removed'] * 4
    item, kwargs = executes[0]
    assert item == QUESTIONS['items'][0]
    assert set(kwargs) == {'condition', 'config', 'fixture',
                           'ground_truth_compute', 'adapter_send',
                           'system_prompt', 'tools', 'transcript_path',
                           'seal_hash', 'repeat'}
    # T3-9: each execution passes its repeat index to the engine
    assert [kw['repeat'] for _, kw in executes] == [1, 2] * 4
    assert kwargs['config'] is config
    assert kwargs['fixture'] == FIXTURE
    assert kwargs['ground_truth_compute']('Q3', {}) == {'derivable': False}
    assert kwargs['tools'] == ['base'] + CONFIG['tools']
    assert kwargs['transcript_path'] == transcript
    assert kwargs['seal_hash'] == 'SEAL'

    # each executed result is followed by the pause; nothing is scored
    # during the execution pass
    assert r.named('sleep') == [(0.5,)] * 5

    # then the scoring pass, once, on the transcript
    assert r.named('score_run') == [(transcript, {
        'config': config, 'seal_record': seal_record, 'fixture': FIXTURE,
        'questions': QUESTIONS,
        'ground_truth_compute': kwargs['ground_truth_compute'],
        'output_dir': out})]

    # the order of the stages
    stages = [c[0] for c in r.calls if c[0] in (
        'version', 'source_hash', 'gt_guard', 'seal', 'guard',
        'verify_seal', 'pre_registration', 'execute', 'score_run')]
    # the seal is verified before the first request and again before the
    # scoring pass reports anything (T3-17)
    assert stages == ['version', 'source_hash', 'gt_guard', 'gt_guard',
                      'gt_guard', 'seal', 'guard', 'verify_seal',
                      'pre_registration'] + ['execute'] * 8 + [
        'verify_seal', 'score_run']


@pytest.mark.finding('T3-7')
@pytest.mark.req('R3.1', 'R1.1')
@pytest.mark.parametrize('guard, ran', [
    ('perturbation', ['perturbation']),
    ('source_fields', ['perturbation', 'source_fields']),
    ('declared_constants',
     ['perturbation', 'source_fields', 'declared_constants']),
])
def test_main_ground_truth_guard_refusal_stops_before_seal_and_requests(
        r, capsys, guard, ran):
    r.refuse.add(guard)
    with pytest.raises(SealError, match=f'^{guard} refused$'):
        r.main()
    assert [g[0] for g in r.named('gt_guard')] == ran
    assert r.named('seal') == [] and r.named('execute') == []
    assert r.named('pre_registration') == []
    assert 'Ground-truth guards' not in capsys.readouterr().out


@pytest.mark.finding('T3-17')
@pytest.mark.req('R1.1')
def test_main_seal_verification_refused_before_any_request(r, capsys):
    r.verify_refusals = [1]
    with pytest.raises(SealError, match='fixture: changed'):
        r.main()
    assert r.named('execute') == [] and r.named('outputs') == []


@pytest.mark.finding('T3-17')
@pytest.mark.req('R1.1')
def test_main_seal_verification_refused_before_anything_is_reported(r):
    r.verify_refusals = [2]
    with pytest.raises(SealError, match='fixture: changed'):
        r.main()
    assert len(r.named('execute')) == 8
    assert r.named('consistency') == [] and r.named('outputs') == []


@pytest.mark.finding('T3-48', 'T3-72')
def test_main_scores_against_the_sealed_expected_values(r):
    # The module is not called again after the seal: a module whose
    # answer changes between calls cannot change the expected values.
    real_seal = r.create_seal

    def seal_then_change(**kwargs):
        record = real_seal(**kwargs)
        sys.modules['ground_truth_example'].compute = \
            lambda item_id, ctx: {'final': D('99')}
        return record
    r.create_seal = seal_then_change
    run.create_seal = seal_then_change
    assert r.main() == 0
    compute = r.named('execute')[0][1]['ground_truth_compute']
    assert compute('Q1', {}) == {'final': D('10.00'), 'derivable': True}
    # the scoring pass gets the same sealed values
    assert r.named('score_run')[0][1]['ground_truth_compute'] is compute


@pytest.mark.finding('T3-72')
def test_main_runs_the_ground_truth_file_not_a_shadowing_package(r):
    package = r.fixture_dir / 'ground_truth_example'
    package.mkdir()
    (package / '__init__.py').write_text('raise ImportError("shadow")\n')
    assert r.main() == 0
    assert sys.modules['ground_truth_example'].__file__ == str(
        r.fixture_dir / 'ground_truth_example.py')


V12_HASH = '14659fc1c2a3357c22081a9109841475861c34f2b315ee7eb546e80fecbb58a5'


@pytest.mark.finding('V12-4')
def test_main_ap1_text_of_the_declared_version(r, monkeypatch):
    # Without --ap1-text the seal takes the text of the config's version.
    r.config['ap1_version'] = 'v1.2'
    monkeypatch.setattr(r, 'create_seal', lambda **kw: r.calls.append(
        ('seal', kw)) or {'seal_hash': 'SEAL', 'ap1_text_hash': V12_HASH,
                          'lookup_collisions': 'none'})
    monkeypatch.setattr(run, 'create_seal', r.create_seal)
    assert run.main(r.argv()[:-2]) == 0
    assert r.named('seal')[0][0]['ap1_text_path'] == os.path.join(
        run.BASE_DIR, 'reference', 'AP-1_Admissibility_Protocol_v1.2.md')


@pytest.mark.finding('V12-4')
def test_main_version_label_over_another_text_refused_before_requests(r):
    # The fake seal records 'TEXTHASH', which is no v1.2 text.
    r.config['ap1_version'] = 'v1.2'
    with pytest.raises(SealError, match='not the AP-1 v1.2 text'):
        r.main()
    assert r.named('seal') and r.named('execute') == []
    assert r.named('verify_seal') == []


def test_main_unknown_version_without_ap1_text_refused_before_seal(r):
    r.config['ap1_version'] = 'v7'
    with pytest.raises(SealError, match="no text is known for ap1_version"):
        run.main(r.argv()[:-2])
    assert r.named('seal') == []


def test_main_adapter_send_binds_the_key(r, monkeypatch):
    sent = []
    monkeypatch.setattr(run.adapter, 'send',
                        lambda url, **kw: sent.append((url, kw)) or 'RESP')
    r.main()
    adapter_send = r.named('execute')[0][1]['adapter_send']
    assert adapter_send('http://x', messages=['m']) == 'RESP'
    assert adapter_send('http://y', messages=['n'], tools=['t'],
                        sampling={'s': 1}, model='M', timeout=7) == 'RESP'
    assert sent == [
        ('http://x', {'messages': ['m'], 'tools': None, 'sampling': None,
                      'model': None, 'api_key': 'sk-0123456789',
                      'timeout': 120}),
        ('http://y', {'messages': ['n'], 'tools': ['t'],
                      'sampling': {'s': 1}, 'model': 'M',
                      'api_key': 'sk-0123456789', 'timeout': 7})]


def test_main_creates_the_output_dir_and_removes_an_old_transcript(r):
    os.makedirs(r.output_dir)
    old = r.output_dir / 'smoke_run.jsonl'
    old.write_text('{"old": true}\n')
    old_record = r.output_dir / 'pre_registration.json'
    old_record.write_text('{"old": true}\n')
    other = r.output_dir / 'keep.txt'
    other.write_text('kept')
    assert r.main() == 0
    assert not old.exists()
    assert not old_record.exists()   # the fake did not write a new one
    assert other.read_text() == 'kept'


def test_main_creates_a_missing_output_dir(r):
    assert r.main() == 0
    assert r.output_dir.is_dir()


@pytest.mark.finding('T3-80')
def test_main_endpoint_and_model_from_the_config_only(r, monkeypatch, capsys):
    # Section B decision (T3-80): the environment supplies only the key.
    monkeypatch.setenv('AP1_SMOKE_ENDPOINT', 'http://elsewhere/v1')
    monkeypatch.setenv('AP1_SMOKE_MODEL', 'other-model')
    r.config.update(endpoint_url='http://from-config/v1', model='cfg-model')
    assert r.main() == 0
    out = capsys.readouterr().out
    assert out.startswith('Endpoint: http://from-config/v1\n'
                          'Model: cfg-model\n'
                          'API key: present (13 chars)\n\n')
    sealed = r.named('seal')[0][0]['config']
    assert (sealed['endpoint_url'], sealed['model']) == (
        'http://from-config/v1', 'cfg-model')


@pytest.mark.finding('T3-12')
@pytest.mark.req('R0.1')
def test_main_under_powered_claim_refused_before_seal_and_requests(r):
    # R0.1: the minimum-n refusal comes before the seal and any request.
    from ap1_run.foundation.config import ConfigError
    r.config.update(dimensions_claimed=['D6'], ap1_version='v1.3')
    with pytest.raises(ConfigError, match=r'^D6: 0 eligible items'):
        r.main()
    assert (r.named('seal'), r.named('execute')) == ([], [])


@pytest.mark.finding('T3-12', 'V12-7')
def test_main_minimum_n_counts_the_question_items(r, monkeypatch):
    # Under v1.2, D6 needs one item with a conflict_class: Q2 has one.
    r.config.update(dimensions_claimed=['D6'], ap1_version='v1.2')
    # V12-4: a v1.2 run must seal the v1.2 text.
    monkeypatch.setattr(run, 'create_seal', lambda **kw: r.calls.append(
        ('seal', kw)) or {'seal_hash': 'SEAL', 'ap1_text_hash': V12_HASH,
                          'lookup_collisions': 'none'})
    questions = json.loads(json.dumps(QUESTIONS))
    questions['items'][2]['conflict_class'] = 'stated twice'
    (r.fixture_dir / 'questions.json').write_text(json.dumps(questions))
    assert r.main() == 0
    assert r.named('seal')


@pytest.mark.finding('T3-51')
@pytest.mark.parametrize('key', ['sampling', 'repeat_count'])
def test_main_result_affecting_field_has_no_default(r, key):
    # R0.1: no defaults for anything affecting a result. load_config
    # refuses a config without these; main() never invents one. (The
    # scoring settings are the scoring pass's: test_scoring_pass.py.)
    del r.config[key]
    with pytest.raises(KeyError, match=key):
        r.main()
    assert r.named('execute') == []


def test_main_execution_with_no_status_unknown_and_no_pause(r, capsys):
    r.results[('Q1', 'base', 1)] = {'no': 'status'}
    r.main()
    assert '  Q1/base/r1: UNKNOWN\n' in capsys.readouterr().out
    assert len(r.named('sleep')) == 7


def test_main_executed_without_evidence_prints_empty_fields(r, capsys):
    r.results[('Q1', 'base', 1)] = {'status': 'EXECUTED'}
    r.main()
    assert '  Q1/base/r1: EXECUTED |  | \n' in capsys.readouterr().out


def test_main_modified_runner_warning(r, capsys):
    r.version.update(version_modified=True, git_commit='abcdef0123456789')
    r.main()
    out = capsys.readouterr().out
    assert ('Runner version: v9.9.9 (0123456789ab)\n'
            '  WARNING: runner appears modified (git HEAD: abcdef012345)\n'
            'Runner source hash: feedfacecafebeef...\n') in out
    config = r.named('seal')[0][0]['config']
    assert config['runner_modified'] is True


def test_main_modified_runner_without_git_commit(r, capsys):
    r.version.update(version_modified=True)
    r.main()
    assert '  WARNING: runner appears modified (git HEAD: ?)\n' in \
        capsys.readouterr().out


@pytest.mark.parametrize('missing, message', [
    ('tools', 'ERROR: config.json must contain a "tools" array\n'),
    ('system_prompt_base',
     'ERROR: config.json must contain system_prompt_base and '
     'system_prompt_instruction_removed\n'),
    ('system_prompt_instruction_removed',
     'ERROR: config.json must contain system_prompt_base and '
     'system_prompt_instruction_removed\n'),
])
def test_main_incomplete_config_returns_1(r, capsys, missing, message):
    r.config[missing] = [] if missing == 'tools' else ''
    assert r.main() == 1
    out = capsys.readouterr().out
    assert out.endswith('reasoning_effort=None (from config)\n' + message)
    assert r.calls == []
    assert r.output_dir.is_dir()


def test_main_puts_the_fixture_dir_first_on_the_path(r, tmp_path,
                                                     monkeypatch):
    decoy = tmp_path / 'decoy'
    decoy.mkdir()
    (decoy / 'ground_truth_example.py').write_text(
        'raise ImportError("the decoy was imported")\n')
    monkeypatch.setattr(sys, 'path', [str(decoy)] + sys.path)
    assert r.main() == 0
    assert sys.path[0] == str(r.fixture_dir)


def test_main_reads_sys_argv_without_argv(r, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ap1-run'] + r.argv())
    assert run.main() == 0
    assert r.named('score_run')[0][1]['output_dir'] == str(r.output_dir)


# -- ap1-run --rescore: the scoring pass alone ------------------------------

@pytest.mark.finding('T3-21')
def test_main_rescore_scores_the_transcript_without_a_key(r, monkeypatch,
                                                          capsys):
    monkeypatch.delenv('AP1_SMOKE_API_KEY')
    transcript = r.tmp / 'run1' / 'smoke_run.jsonl'
    argv = ['--rescore', str(transcript),
            '--config', str(r.fixture_dir / 'config.json'),
            '--fixture-dir', str(r.fixture_dir),
            '--output-dir', str(r.tmp / 'rescored')]
    assert run.main(argv) == 0
    assert r.calls == [('rescore', str(transcript), {
        'config_path': str(r.fixture_dir / 'config.json'),
        'fixture_dir': str(r.fixture_dir),
        'output_dir': str(r.tmp / 'rescored')})]
    assert capsys.readouterr().out == (
        f'Re-scoring transcript: {transcript}\n'
        f'{RULE}\n'
        '(re-scoring)\n'
        f'Transcript scored (not changed): {transcript}\n')


def test_main_help_exits_before_the_key_is_read(r, monkeypatch, capsys):
    monkeypatch.delenv('AP1_SMOKE_API_KEY')
    with pytest.raises(SystemExit) as exc:
        run.main(['--help'])
    assert exc.value.code == 0
    assert capsys.readouterr().out.startswith('usage: ap1-run')


def test_main_reconfigures_stdout_and_flushes_each_progress_prefix(
        r, monkeypatch):
    seen = []

    class Stdout:
        def write(self, text):
            seen.append(('write', text))

        def flush(self):
            seen.append(('flush',))

        def reconfigure(self, **kwargs):
            seen.append(('reconfigure', kwargs))
    monkeypatch.setattr(sys, 'stdout', Stdout())
    r.main()
    assert seen[0] == ('reconfigure', {'encoding': 'utf-8',
                                       'errors': 'replace'})
    # The "  Q1/base/r1: " prefix is flushed before the request is sent.
    prefixes = [i for i, e in enumerate(seen)
                if e[0] == 'write' and e[1].endswith('/r1: ')]
    after = [[e for e in seen[i + 1:] if e != ('write', '')][0]
             for i in prefixes]
    assert after == [('flush',)] * len(prefixes) and prefixes
    assert seen.count(('flush',)) == len(r.named('execute'))


def test_base_dir_is_the_repository_root():
    assert run.BASE_DIR == REPO
    assert os.path.exists(os.path.join(run.BASE_DIR, 'VERSION'))


def test_disclaimer_text():
    assert run.DISCLAIMER == (
        'THIS IS AN INSTRUMENT SMOKE TEST, NOT AN AP-1 EVALUATION.\n'
        '\n'
        'It is not conformant: no adjudication, no second scorer, no blind '
        'set,\n'
        'the fixture is the shipped example (10 items, burned under AP-1 '
        '§5.8),\n'
        'and the D1 minimum of 40 items is not met.\n'
        'No figure from it may be reported, cited, quoted or described as '
        'an AP-1\n'
        'result, by us or by anyone, in any document.\n')


# -- end to end, nothing replaced -----------------------------------------

@pytest.mark.filterwarnings('ignore:VERSION file says')
def test_main_end_to_end_against_the_mock_endpoint(tmp_path, monkeypatch,
                                                   capsys):
    sys.path.insert(0, os.path.join(REPO, 'tests', 'fixtures'))
    from mock_endpoint import MockEndpoint
    monkeypatch.setattr(sys, 'path', list(sys.path))
    monkeypatch.delitem(sys.modules, 'ground_truth_example', raising=False)
    fx = tmp_path / 'example'
    shutil.copytree(os.path.join(REPO, 'example'), fx)
    questions = json.loads((fx / 'questions.json').read_text())
    questions['items'] = questions['items'][:2]
    (fx / 'questions.json').write_text(json.dumps(questions))
    config = json.loads((fx / 'config.json').read_text())
    config['repeat_count'] = '1'
    (fx / 'config.json').write_text(json.dumps(config))

    mock = MockEndpoint(
        questions=questions,
        system_prompts={config['system_prompt_base']: 'base',
                        config['system_prompt_instruction_removed']:
                        'instruction_removed'},
        responses={
            'Q01/*/*': [{'call': '15200.00 * 1.2 / 100 / 12'},
                        {'say': 'The monthly interest is ${result}.'}],
            'Q02/*/*': [{'call': '5000 - 2400'},
                        {'say': 'The available credit is ${result}.'}],
        }).start()
    try:
        for name in list(os.environ):
            if name.startswith('AP1_SMOKE_'):
                monkeypatch.delenv(name)
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-test')
        mock.point_config(fx / 'config.json')
        monkeypatch.setattr(run.time, 'sleep', lambda s: None)
        out = tmp_path / 'out'
        code = run.main(['--config', str(fx / 'config.json'),
                         '--fixture-dir', str(fx),
                         '--output-dir', str(out)])
    finally:
        mock.stop()
    console = capsys.readouterr().out
    assert code == 0
    # the execution pass, then the scoring pass
    assert '  Q01/base/r1: EXECUTED | EV-2 PLATFORM-STRUCTURAL | ' \
        'INVOKED\n' in console
    assert '  Q01/base/r1: AUTO-MATCH | ' in console
    assert console.index('EXECUTED | ') < console.index('SCORING THE '
                                                       'TRANSCRIPT') \
        < console.index('AUTO-MATCH | ')
    assert '  Q02/instruction_removed/r1: AUTO-MATCH | ' in console
    assert sorted(os.listdir(out)) == [
        'DISCLAIMER.txt', 'adjudication_sheets.md', 'pre_registration.json',
        'report.md', 'smoke_run.jsonl', 'smoke_summary.json']
    assert len(mock.log) == 8   # 2 items x 2 conditions x 2 rounds

    # ap1-run --rescore on its transcript: the same summary and report,
    # elsewhere, with no endpoint or key; the transcript is unchanged
    monkeypatch.delenv('AP1_SMOKE_API_KEY')
    before = (out / 'smoke_run.jsonl').read_bytes()
    again = tmp_path / 'again'
    assert run.main(['--rescore', str(out / 'smoke_run.jsonl'),
                     '--config', str(fx / 'config.json'),
                     '--fixture-dir', str(fx),
                     '--output-dir', str(again)]) == 0
    assert (out / 'smoke_run.jsonl').read_bytes() == before
    assert sorted(os.listdir(again)) == [
        'DISCLAIMER.txt', 'adjudication_sheets.md', 'report.md',
        'smoke_summary.json']
    def text(path):   # the report's own generation time aside
        return re.sub(r'(Generated: \S+?)T[\d:.+]+', r'\1',
                      path.read_text('utf-8'))
    for name in ('smoke_summary.json', 'report.md', 'adjudication_sheets.md',
                 'DISCLAIMER.txt'):
        assert text(again / name) == text(out / name), name

# Step 5 (run-robustness): removing the runner's dead transport handlers
# (F4, T3-65) removed the code whose mutants they killed, so the ratchet
# needs these mutants of main() killed instead.

# (test_main_reads_fixture_and_questions_as_utf8_text was removed on the
# merge with seal-verifier-hardening: main() no longer opens these files;
# execution/sealed_inputs.py reads every input once, as UTF-8, and
# tests/unit/execution/test_sealed_inputs.py covers that.)
