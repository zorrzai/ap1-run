"""Unit tests for run.py's main(): the orchestration of a live run.

main()'s collaborators (the engine, the seal, the scoring, the reports)
have their own tests. Here they are replaced by recording fakes, so that
the order of the run, what main() passes to each, and what it prints are
checked exactly. The inputs are small files in a temporary directory,
reached through the command-line options. The last test runs main() end
to end, with nothing replaced, against the mock endpoint.
"""

import json
import os
import shutil
import sys
from decimal import Decimal

import pytest

from ap1_run import run
from ap1_run.foundation import adapter

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
QUESTIONS = {'items': [{'id': 'Q1', 'source_accounts': ['a']},
                       {'id': 'Q3', 'source_accounts': []},
                       {'id': 'Q2', 'source_accounts': ['b']}]}
FIXTURE = {'accounts': [{'id': 'a'}, {'id': 'b'}]}


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
        self.results = {}     # (item, condition, rep) -> result or exception
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
                     'create_seal', 'check_condition_guard',
                     'build_delivered_context', 'check_lookup_collision',
                     'execute_item', 'score_execution',
                     'verify_invocation_consistency', 'print_run_report',
                     'summarise_accuracy', 'find_d2_cap',
                     'classify_reproducibility', 'build_summary',
                     'print_scoring_report', 'write_outputs'):
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

    def create_seal(self, **kwargs):
        self.calls.append(('seal', kwargs))
        return {'seal_hash': 'SEAL', 'ap1_text_hash': 'TEXTHASH'}

    def check_condition_guard(self, *args):
        self.calls.append(('guard',) + args)

    def build_delivered_context(self, fixture, accounts):
        self.calls.append(('context', fixture, accounts))
        return {'accounts': list(accounts)}

    def check_lookup_collision(self, expected, ctx):
        self.calls.append(('collision', expected, ctx))
        return 'COLLISION', 'field'

    def execute_item(self, item, **kwargs):
        rep = sum(1 for c in self.calls if c[0] == 'execute'
                  and c[1]['id'] == item['id']
                  and c[2]['condition'] == kwargs['condition']) + 1
        self.calls.append(('execute', item, kwargs))
        outcome = self.results.get((item['id'], kwargs['condition'], rep),
                                   {'status': 'EXECUTED', 'n': rep})
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    def score_execution(self, findings, result, **kwargs):
        self.calls.append(('score', result, kwargs))
        findings.all_results.append({'status': 'EXECUTED'})
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

    def write_outputs(self, output_dir, transcript_path, **kwargs):
        self.calls.append(('outputs', output_dir, transcript_path, kwargs))


@pytest.fixture
def r(tmp_path, monkeypatch):
    return Run(tmp_path, monkeypatch)


RULE = '=' * 60


def script_failures(r):
    # Each failure is on a first repeat, so the second still runs.
    r.results[('Q1', 'base', 1)] = adapter.RateLimitError('slow down')
    r.results[('Q2', 'base', 1)] = adapter.AdapterError('HTTP 500: boom')
    r.results[('Q1', 'instruction_removed', 1)] = {'status': 'VOID',
                                                  'error': 'no figure'}
    r.results[('Q2', 'instruction_removed', 1)] = {'status': 'UNMEASURED',
                                                  'reason': 'cut off'}


def test_main_full_run_console(r, capsys):
    script_failures(r)
    assert r.main() == 0
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
        'Seal hash: SEAL\n'
        'AP-1 text hash: TEXTHASH\n'
        '\n'
        'Running 3 items x 2 conditions x 2 repeats\n'
        'Total requests: 12\n'
        f'{RULE}\n'
        '  Q1/base/r1: RATE-LIMITED\n'
        '  Q1/base/r2:   Q3/base: VOID (underivable)\n'
        '  Q2/base/r1: TRANSPORT_ERROR: HTTP 500: boom\n'
        '  Q2/base/r2:   Q1/instruction_removed/r1: VOID\n'
        '  Q1/instruction_removed/r2:   '
        'Q3/instruction_removed: VOID (underivable)\n'
        '  Q2/instruction_removed/r1: UNMEASURED\n'
        '  Q2/instruction_removed/r2:   '
        'Invocation consistency check: PASSED (0 mismatches)\n')


def test_main_full_run_calls(r, capsys):
    script_failures(r)
    assert r.main() == 0
    fx = str(r.fixture_dir)
    out = str(r.output_dir)
    transcript = os.path.join(out, 'smoke_run.jsonl')

    assert r.config_path == os.path.join(fx, 'config.json')
    assert r.named('version') == [(run.BASE_DIR,)]
    assert r.named('source_hash') == [(run.BASE_DIR,)]
    (seal,), = r.named('seal')
    config = seal.pop('config')
    assert seal == {
        'fixture_path': os.path.join(fx, 'fixture.json'),
        'questions_path': os.path.join(fx, 'questions.json'),
        'ground_truth_path': os.path.join(fx, 'ground_truth_example.py'),
        'ap1_text_path': str(r.tmp / 'ap1.md'),
        'runner_source_hash': 'feedfacecafebeef' + '0' * 48}
    assert config['endpoint_url'] == 'http://mock/v1'
    assert config['model'] == 'mock-model'
    assert (config['runner_version_tag'], config['runner_version_commit'],
            config['runner_modified']) == (
        'v9.9.9', '0123456789abcdef0123', False)

    assert r.named('guard') == [(
        config, os.path.join(fx, 'fixture.json'), 'BASE PROMPT',
        'REMOVED PROMPT', CONFIG['tools'], {'temperature': 0})]

    # contexts and collisions: per item and condition, Q3 has no collision
    assert [c[1] for c in r.named('context')] == [
        ['a'], [], ['b'], ['a'], [], ['b']]
    assert all(c[0] == FIXTURE for c in r.named('context'))
    assert r.named('collision') == [(D('10.00'), {'accounts': ['a']}),
                                    (D('10.00'), {'accounts': ['b']})] * 2

    executes = r.named('execute')
    assert [(i['id'], k['condition'], k['system_prompt'])
            for i, k in executes] == [
        ('Q1', 'base', 'BASE PROMPT'), ('Q1', 'base', 'BASE PROMPT'),
        ('Q2', 'base', 'BASE PROMPT'), ('Q2', 'base', 'BASE PROMPT'),
        ('Q1', 'instruction_removed', 'REMOVED PROMPT'),
        ('Q1', 'instruction_removed', 'REMOVED PROMPT'),
        ('Q2', 'instruction_removed', 'REMOVED PROMPT'),
        ('Q2', 'instruction_removed', 'REMOVED PROMPT')]
    item, kwargs = executes[0]
    assert item == QUESTIONS['items'][0]
    assert set(kwargs) == {'condition', 'config', 'fixture',
                           'ground_truth_compute', 'adapter_send',
                           'system_prompt', 'tools', 'transcript_path',
                           'seal_hash'}
    assert kwargs['config'] is config
    assert kwargs['fixture'] == FIXTURE
    assert kwargs['ground_truth_compute']('Q3', {}) == {'derivable': False}
    assert kwargs['tools'] == CONFIG['tools']
    assert kwargs['transcript_path'] == transcript
    assert kwargs['seal_hash'] == 'SEAL'

    # only executed results are scored, each followed by the pause
    scores = r.named('score')
    assert [res for res, _ in scores] == [{'status': 'EXECUTED', 'n': 2}] * 4
    assert [(k['item_id'], k['condition'], k['rep']) for _, k in scores] == [
        ('Q1', 'base', 2), ('Q2', 'base', 2),
        ('Q1', 'instruction_removed', 2), ('Q2', 'instruction_removed', 2)]
    assert scores[1][1]['ctx'] == {'accounts': ['b']}
    kw = scores[0][1]
    assert kw == {
        'item_id': 'Q1', 'condition': 'base', 'rep': 2,
        'expected': D('10.00'), 'ctx': {'accounts': ['a']},
        'collision': 'COLLISION', 'config': config,
        'answer_tolerance': D('0.05'), 'decline_markers': ['cannot'],
        'currency_symbols': ['$'], 'transcript_path': transcript,
        'seal_hash': 'SEAL'}
    assert r.named('sleep') == [(0.5,)] * 4

    # the collected results, in order
    expected_results = [
        {'item_id': 'Q1', 'condition': 'base', 'repeat': 1,
         'status': 'UNMEASURED', 'cause': 'rate_limited'},
        {'status': 'EXECUTED'},
        {'item_id': 'Q3', 'condition': 'base', 'repeat': 0,
         'status': 'VOID'},
        {'item_id': 'Q2', 'condition': 'base', 'repeat': 1,
         'status': 'UNMEASURED', 'cause': 'HTTP 500: boom'},
        {'status': 'EXECUTED'},
        {'item_id': 'Q1', 'condition': 'instruction_removed', 'repeat': 1,
         'status': 'VOID', 'cause': 'no figure'},
        {'status': 'EXECUTED'},
        {'item_id': 'Q3', 'condition': 'instruction_removed', 'repeat': 0,
         'status': 'VOID'},
        {'item_id': 'Q2', 'condition': 'instruction_removed', 'repeat': 1,
         'status': 'UNMEASURED', 'cause': 'cut off'},
        {'status': 'EXECUTED'},
    ]
    assert r.named('consistency') == [(expected_results,)]

    (results, conditions, kw), = r.named('run_report')
    assert results == expected_results
    assert conditions == ['base', 'instruction_removed']
    assert kw['disclaimer'] == run.DISCLAIMER
    assert kw['unmeasured_cells'] == [
        {'item_id': 'Q1', 'condition': 'base', 'repeat': 1,
         'cause': 'rate_limited'},
        {'item_id': 'Q2', 'condition': 'base', 'repeat': 1,
         'cause': 'HTTP 500: boom'}]
    for name in ('grammar_issues', 'decline_findings', 'tool_call_structures',
                 'evidence_findings', 'transcription_results',
                 'release_coverage_results'):
        assert kw[name] == [], name

    assert r.named('summarise') == [([],)]
    assert r.named('d2_cap') == [({'temperature': 0},)]
    d2_responses = {'d2': [res for res, _ in scores]}
    assert r.named('d2') == [(d2_responses, 2, 'CAP')]
    (results, evidence, kw), = r.named('summary')
    assert results == expected_results and evidence == []
    assert kw == {'d1_summary': {'d1': True, 'n': 0},
                  'd2_results': {'d2': 'results'}, 'd2_cap_reason': 'CAP',
                  'transcription_results': [],
                  'release_coverage_results': []}
    assert r.named('scoring_report') == [(
        {'d1': True, 'n': 0}, {'d2': 'results'}, 'CAP', {'summary': True})]

    (output_dir, transcript_path, kw), = r.named('outputs')
    assert (output_dir, transcript_path) == (out, transcript)
    assert kw == {
        'summary': {'summary': True}, 'config': config,
        'seal_record': {'seal_hash': 'SEAL', 'ap1_text_hash': 'TEXTHASH'},
        'questions': QUESTIONS, 'fixture': FIXTURE,
        'release_coverage_results': [], 'disclaimer': run.DISCLAIMER,
        'smoke_summary': {
            'seal_hash': 'SEAL', 'all_results': expected_results,
            'grammar_issues': [], 'decline_findings': [],
            'tool_call_structures': [], 'evidence_findings': [],
            'unmeasured_cells': kw['smoke_summary']['unmeasured_cells']}}
    assert len(kw['smoke_summary']['unmeasured_cells']) == 2

    # the order of the stages
    stages = [c[0] for c in r.calls if c[0] in (
        'version', 'source_hash', 'seal', 'guard', 'consistency',
        'run_report', 'summarise', 'd2_cap', 'd2', 'summary',
        'scoring_report', 'outputs')]
    assert stages == ['version', 'source_hash', 'seal', 'guard',
                      'consistency', 'run_report', 'summarise', 'd2_cap',
                      'd2', 'summary', 'scoring_report', 'outputs']


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
    other = r.output_dir / 'keep.txt'
    other.write_text('kept')
    assert r.main() == 0
    assert not old.exists()
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
def test_main_minimum_n_counts_the_question_items(r):
    # Under v1.2, D6 needs one item with a conflict_class: Q2 has one.
    r.config.update(dimensions_claimed=['D6'], ap1_version='v1.2')
    questions = json.loads(json.dumps(QUESTIONS))
    questions['items'][2]['conflict_class'] = 'stated twice'
    (r.fixture_dir / 'questions.json').write_text(json.dumps(questions))
    assert r.main() == 0
    assert r.named('seal')


@pytest.mark.finding('T3-51')
@pytest.mark.parametrize('key', ['answer_tolerance', 'decline_markers',
                                 'currency_symbols', 'sampling',
                                 'repeat_count'])
def test_main_result_affecting_field_has_no_default(r, key):
    # R0.1: no defaults for anything affecting a result. load_config
    # refuses a config without these; main() never invents one.
    del r.config[key]
    with pytest.raises(KeyError, match=key):
        r.main()
    assert r.named('execute') == []


def test_main_execution_with_no_status_is_scored(r):
    r.results[('Q1', 'base', 1)] = {'no': 'status'}
    r.main()
    assert r.named('score')[0][0] == {'no': 'status'}


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
    assert r.named('outputs')[0][0] == str(r.output_dir)


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
    assert '  Q01/base/r1: AUTO-MATCH | ' in console
    assert '  Q02/instruction_removed/r1: AUTO-MATCH | ' in console
    assert sorted(os.listdir(out)) == [
        'DISCLAIMER.txt', 'adjudication_sheets.md', 'report.md',
        'smoke_run.jsonl', 'smoke_summary.json']
    assert len(mock.log) == 8   # 2 items x 2 conditions x 2 rounds
