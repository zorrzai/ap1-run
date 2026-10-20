"""Unit tests for the runner's settings from the environment and the
R1.2 condition guard."""

import hashlib
import os

import pytest

from ap1_run.execution.perturbation_guard import PerturbationRefusal
from ap1_run.runner import settings
from ap1_run.runner.settings import (
    DEFAULT_ENDPOINT, DEFAULT_MODEL, RUN_OUTPUT_FILES,
    check_condition_guard, check_output_dir, condition_request,
    endpoint_and_model, parse_args, print_sampling,
)


# -- endpoint_and_model ---------------------------------------------------

def test_endpoint_and_model_defaults():
    assert DEFAULT_ENDPOINT == 'https://api.openai.com/v1/chat/completions'
    assert DEFAULT_MODEL == 'gpt-4o-mini'
    assert endpoint_and_model({}) == (DEFAULT_ENDPOINT, DEFAULT_MODEL)


def test_endpoint_and_model_from_environment():
    env = {'AP1_SMOKE_ENDPOINT': 'http://127.0.0.1:9/v1',
           'AP1_SMOKE_MODEL': 'mock-model'}
    assert endpoint_and_model(env) == ('http://127.0.0.1:9/v1', 'mock-model')


def test_endpoint_and_model_reads_os_environ_by_default(monkeypatch):
    monkeypatch.setenv('AP1_SMOKE_MODEL', 'from-os-environ')
    monkeypatch.delenv('AP1_SMOKE_ENDPOINT', raising=False)
    assert endpoint_and_model() == (DEFAULT_ENDPOINT, 'from-os-environ')


# -- print_sampling -------------------------------------------------------

def printed(sampling, capsys):
    config = {'sampling': dict(sampling)}
    print_sampling(config)
    assert config == {'sampling': sampling}   # printed, never changed
    return capsys.readouterr().out


def test_print_sampling_reports_config_values(capsys):
    assert printed({'temperature': '0', 'reasoning_effort': 'none'},
                   capsys) == ('  temperature=0\n'
                               '  reasoning_effort=none (from config)\n')


def test_print_sampling_omitted_temperature_with_reason(capsys):
    omitted = {'value': 'omitted', 'reason': 'platform-rejected'}
    assert printed({'temperature': omitted}, capsys) == (
        '  temperature omitted (reason: platform-rejected)\n'
        '  reasoning_effort=None (from config)\n')


def test_print_sampling_omitted_temperature_without_reason(capsys):
    assert printed({'temperature': {'value': 'omitted'}}, capsys).startswith(
        '  temperature omitted (reason: ?)\n')


def test_print_sampling_temperature_dict_not_omitted_printed_as_is(capsys):
    assert printed({'temperature': {'value': 1}}, capsys).startswith(
        "  temperature={'value': 1}\n")


def test_print_sampling_omitted_reasoning_effort_with_reason(capsys):
    effort = {'value': 'omitted', 'reason': 'platform-unsupported',
              'detail': 'x'}
    assert printed({'temperature': '1', 'reasoning_effort': effort},
                   capsys) == ('  temperature=1\n'
                               '  reasoning_effort omitted '
                               '(reason: platform-unsupported)\n')


def test_print_sampling_omitted_reasoning_effort_without_reason(capsys):
    assert printed({'reasoning_effort': {'value': 'omitted'}},
                   capsys).endswith('  reasoning_effort omitted (reason: ?)\n')


def test_print_sampling_without_sampling_block(capsys):
    print_sampling({})
    assert capsys.readouterr().out == ('  temperature=None\n'
                                       '  reasoning_effort=None (from config)\n')


@pytest.mark.finding('F1', 'T3-67')
def test_print_sampling_environment_changes_nothing(monkeypatch, capsys):
    # The AP1_SMOKE_TEMPERATURE and AP1_SMOKE_REASONING_EFFORT overrides
    # are gone (Steven's ruling, choices-for-marcus entry 5).
    monkeypatch.setenv('AP1_SMOKE_TEMPERATURE', '0.5')
    monkeypatch.setenv('AP1_SMOKE_REASONING_EFFORT', 'omit')
    assert printed({'temperature': '1', 'reasoning_effort': 'none'},
                   capsys) == ('  temperature=1\n'
                               '  reasoning_effort=none (from config)\n')
    assert not hasattr(settings, 'apply_sampling_overrides')


# -- check_condition_guard ------------------------------------------------

@pytest.fixture
def fixture_file(tmp_path):
    path = tmp_path / 'fixture.json'
    path.write_bytes(b'{"accounts": []}\n')
    return str(path)


def test_guard_passes_when_only_the_prompt_differs(fixture_file, capsys,
                                                    monkeypatch):
    seen = []

    def check(base, removed):
        seen.append((base, removed))
        return []
    monkeypatch.setattr(settings, 'check_single_variable_perturbation', check)
    config = {'tool_choice': 'auto', 'message_template': 'T'}
    arms = check_condition_guard(config, fixture_file, 'BASE', 'REMOVED',
                                 ['tool'], {'temperature': 0})
    fixture_hash = hashlib.sha256(b'{"accounts": []}\n').hexdigest()
    base = {'system_prompt': 'BASE', 'tools': ['tool'], 'tool_choice': 'auto',
            'sampling': {'temperature': 0}, 'fixture_hash': fixture_hash,
            'message_template': 'T'}
    assert seen == [(base, dict(base, system_prompt='REMOVED'))]
    # The run gives the engine each condition's own checked request.
    assert arms == {'base': base,
                    'instruction_removed': dict(base, system_prompt='REMOVED')}
    assert seen[0][0] is arms['base']
    assert seen[0][1] is arms['instruction_removed']
    assert capsys.readouterr().out == (
        'Perturbation guard: PASSED (single-variable: system_prompt only)\n\n')


def test_guard_with_the_real_check(fixture_file, capsys):
    arms = check_condition_guard({}, fixture_file, 'A', 'B', [], {})
    assert 'PASSED' in capsys.readouterr().out
    assert [arms[c]['system_prompt'] for c in arms] == ['A', 'B']


@pytest.mark.finding('T3-46')
def test_condition_request_is_what_one_condition_sends():
    config = {'tool_choice': 'none', 'message_template': {'role': 'user'},
              'model': 'm', 'sampling': {'ignored': True}}
    assert condition_request(config, 'HASH', 'P', ['t'], {'s': 1}) == {
        'system_prompt': 'P', 'tools': ['t'], 'tool_choice': 'none',
        'sampling': {'s': 1}, 'fixture_hash': 'HASH',
        'message_template': {'role': 'user'}}
    assert condition_request({}, 'H', 'P', None, {}) == {
        'system_prompt': 'P', 'tools': None, 'tool_choice': None,
        'sampling': {}, 'fixture_hash': 'H', 'message_template': None}


def test_guard_refusal_propagates_and_prints_nothing(fixture_file, capsys,
                                                     monkeypatch):
    def refuse(base, removed):
        raise PerturbationRefusal('tools differ')
    monkeypatch.setattr(settings, 'check_single_variable_perturbation',
                        refuse)
    with pytest.raises(PerturbationRefusal, match='tools differ'):
        check_condition_guard({}, fixture_file, 'A', 'B', [], {})
    assert capsys.readouterr().out == ''


# -- parse_args -----------------------------------------------------------

BASE = '/repo'


def native(path):
    """The absolute path os.path makes of a POSIX-style test path: itself
    on POSIX, with a drive and backslashes on Windows."""
    return os.path.abspath(path)


def test_parse_args_defaults_are_the_fixed_paths():
    args = parse_args([], BASE)
    assert vars(args) == {
        'config': native('/repo/example/config.json'),
        'fixture_dir': native('/repo/example'),
        'output_dir': native('/repo/output'),
        'output_dir_explicit': False,
        'ap1_text': native('/repo/reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md'),
    }


def test_parse_args_absolute_paths_kept():
    args = parse_args(['--config', '/a/c.json', '--fixture-dir', '/b',
                       '--output-dir', '/c/out', '--ap1-text', '/d/ap1.md'],
                      BASE)
    assert vars(args) == {'config': native('/a/c.json'),
                          'fixture_dir': native('/b'),
                          'output_dir': native('/c/out'),
                          'output_dir_explicit': True,
                          'ap1_text': native('/d/ap1.md')}


def test_parse_args_relative_paths_resolve_against_the_working_directory(
        tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    args = parse_args(['--config', 'c.json', '--fixture-dir', 'in',
                       '--output-dir', 'out/x', '--ap1-text', '../t.md'],
                      BASE)
    root = str(tmp_path.resolve())
    parent = str(tmp_path.resolve().parent)
    assert vars(args) == {'config': os.path.join(root, 'c.json'),
                          'fixture_dir': os.path.join(root, 'in'),
                          'output_dir': os.path.join(root, 'out', 'x'),
                          'output_dir_explicit': True,
                          'ap1_text': os.path.join(parent, 't.md')}


def test_parse_args_rejects_unknown_options(capsys):
    with pytest.raises(SystemExit) as exc:
        parse_args(['--model', 'x'], BASE)
    assert exc.value.code == 2
    assert 'unrecognized arguments: --model x' in capsys.readouterr().err


def test_parse_args_help_text(capsys, monkeypatch):
    monkeypatch.setenv('COLUMNS', '200')  # one line per help string
    with pytest.raises(SystemExit) as exc:
        parse_args(['--help'], BASE)
    assert exc.value.code == 0
    pad = ' ' * 24
    assert capsys.readouterr().out == (
        'usage: ap1-run [-h] [--config CONFIG] [--fixture-dir FIXTURE_DIR] '
        '[--output-dir OUTPUT_DIR] [--ap1-text AP1_TEXT]\n'
        '\n'
        'Run the AP-1 instrument smoke test against a live endpoint. The '
        'endpoint, model and API key come from the AP1_SMOKE_* environment '
        'variables.\n'
        '\n'
        'options:\n'
        '  -h, --help            show this help message and exit\n'
        '  --config CONFIG       the run configuration '
        '(default: example/config.json)\n'
        '  --fixture-dir FIXTURE_DIR\n'
        f'{pad}the directory holding fixture.json, questions.json and '
        'ground_truth_example.py (default: example/)\n'
        '  --output-dir OUTPUT_DIR\n'
        f'{pad}where the transcript, report and summary are written '
        '(default: output/, where files of the same name are replaced); a '
        'directory given here that already holds a run is refused\n'
        '  --ap1-text AP1_TEXT   the AP-1 text to seal; its hash must match '
        'the one the runner expects '
        # AP1_TEXT is built with os.path.join, so its help shows the native
        # separator (a backslash on Windows); the other defaults are literals
        '(default: '
        + os.path.join('reference', 'AP-1_v1.3_DRAFT_FOR_COMMENT.md')
        + ')\n')


def test_parse_args_output_dir_given_as_the_default_path_is_explicit():
    args = parse_args(['--output-dir', '/repo/output'], BASE)
    assert args.output_dir == native('/repo/output')
    assert args.output_dir_explicit is True


# -- check_output_dir -----------------------------------------------------

def test_run_output_files():
    assert RUN_OUTPUT_FILES == ('smoke_run.jsonl', 'report.md',
                                'smoke_summary.json')


def output_args(path, explicit):
    return parse_args(['--output-dir', str(path)] if explicit else [],
                      str(path.parent))


@pytest.mark.parametrize('name', RUN_OUTPUT_FILES)
def test_check_output_dir_refuses_an_explicit_dir_holding_a_run_file(
        tmp_path, capsys, name):
    out = tmp_path / 'output'
    out.mkdir()
    (out / name).write_text('x')
    assert check_output_dir(output_args(out, explicit=True)) == 2
    captured = capsys.readouterr()
    assert captured.out == ''
    assert captured.err == (
        f'ERROR: --output-dir {out} already holds a run ({name}); choose '
        'another directory or remove those files\n')


def test_check_output_dir_names_every_run_file_found(tmp_path, capsys):
    out = tmp_path / 'output'
    out.mkdir()
    for name in RUN_OUTPUT_FILES:
        (out / name).write_text('x')
    assert check_output_dir(output_args(out, explicit=True)) == 2
    assert ('already holds a run (smoke_run.jsonl, report.md, '
            'smoke_summary.json); ') in capsys.readouterr().err


@pytest.mark.parametrize('contents', [[], ['notes.txt', 'DISCLAIMER.txt']])
def test_check_output_dir_allows_an_explicit_dir_without_run_files(
        tmp_path, capsys, contents):
    out = tmp_path / 'output'
    out.mkdir()
    for name in contents:
        (out / name).write_text('x')
    assert check_output_dir(output_args(out, explicit=True)) is None
    assert capsys.readouterr() == ('', '')


def test_check_output_dir_allows_an_explicit_dir_that_does_not_exist(
        tmp_path):
    out = tmp_path / 'new' / 'run'
    assert check_output_dir(output_args(out, explicit=True)) is None
    assert not out.exists()


def test_check_output_dir_allows_the_default_dir_holding_a_run(tmp_path,
                                                                capsys):
    out = tmp_path / 'output'
    out.mkdir()
    for name in RUN_OUTPUT_FILES:
        (out / name).write_text('x')
    args = output_args(out, explicit=False)
    assert args.output_dir == str(out)
    assert check_output_dir(args) is None
    assert capsys.readouterr() == ('', '')


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-46')
@pytest.mark.req('R1.2', 'AP-1 D7.8')
def test_guard_identical_prompts_refused(fixture_file, capsys):
    # Correct (AP-1 v1.3 D7.8; SPEC R1.2 l.316-321): identical prompts
    # mean there is no contrast; the run is refused before execution and
    # PASSED is not printed. Today the guard builds the removed condition
    # from the base one, so it can never refuse, and prints PASSED.
    refused = None
    try:
        check_condition_guard({}, fixture_file, 'SAME', 'SAME', [], {})
    except PerturbationRefusal as exc:
        refused = str(exc)
    assert refused is not None, 'identical prompts passed the guard'
    assert 'PASSED' not in capsys.readouterr().out
