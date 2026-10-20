"""Unit tests for the runner's settings from the environment and the
R1.2 condition guard."""

import hashlib

import pytest

from ap1_run.execution.perturbation_guard import PerturbationRefusal
from ap1_run.runner import settings
from ap1_run.runner.settings import (
    DEFAULT_ENDPOINT, DEFAULT_MODEL, apply_sampling_overrides,
    check_condition_guard, condition_request, endpoint_and_model, parse_args,
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


# -- apply_sampling_overrides ---------------------------------------------

def overrides(sampling, env, capsys):
    config = {'sampling': dict(sampling)}
    apply_sampling_overrides(config, env)
    return config['sampling'], capsys.readouterr().out


def test_overrides_none_set_reports_config_values(capsys):
    sampling, out = overrides({'temperature': 0, 'reasoning_effort': 'none'},
                              {}, capsys)
    assert sampling == {'temperature': 0, 'reasoning_effort': 'none'}
    assert out == ('  temperature=0\n'
                   '  reasoning_effort=none (from config)\n')


def test_overrides_reports_omitted_temperature_with_reason(capsys):
    omitted = {'value': 'omitted', 'reason': 'platform-rejected'}
    _, out = overrides({'temperature': omitted}, {}, capsys)
    assert out == ('  temperature omitted (reason: platform-rejected)\n'
                   '  reasoning_effort=None (from config)\n')


def test_overrides_omitted_temperature_without_reason(capsys):
    _, out = overrides({'temperature': {'value': 'omitted'}}, {}, capsys)
    assert out.startswith('  temperature omitted (reason: ?)\n')


def test_overrides_temperature_dict_not_omitted_is_printed_as_is(capsys):
    _, out = overrides({'temperature': {'value': 1}}, {}, capsys)
    assert out.startswith("  temperature={'value': 1}\n")


def test_overrides_temperature_from_environment(capsys):
    sampling, out = overrides({'temperature': {'value': 'omitted'}},
                              {'AP1_SMOKE_TEMPERATURE': '1'}, capsys)
    assert sampling['temperature'] == '1'
    assert out.startswith('  temperature=1 (AP1_SMOKE_TEMPERATURE override)\n')


def test_overrides_empty_temperature_still_overrides(capsys):
    sampling, _ = overrides({'temperature': 0},
                            {'AP1_SMOKE_TEMPERATURE': ''}, capsys)
    assert sampling['temperature'] == ''


def test_overrides_reasoning_effort_omit(capsys):
    sampling, out = overrides({'reasoning_effort': 'none'},
                              {'AP1_SMOKE_REASONING_EFFORT': 'omit'}, capsys)
    assert sampling['reasoning_effort'] == {
        'value': 'omitted', 'reason': 'not-supported',
        'detail': 'gpt-4.1-mini does not recognize reasoning_effort'}
    assert out.endswith(
        '  reasoning_effort omitted (AP1_SMOKE_REASONING_EFFORT=omit)\n')


def test_overrides_reasoning_effort_value(capsys):
    sampling, out = overrides({}, {'AP1_SMOKE_REASONING_EFFORT': 'low'},
                              capsys)
    assert sampling == {'reasoning_effort': 'low'}
    assert out == ('  temperature=None\n'
                   '  reasoning_effort=low '
                   '(AP1_SMOKE_REASONING_EFFORT override)\n')


def test_overrides_empty_reasoning_effort_still_overrides(capsys):
    sampling, _ = overrides({'reasoning_effort': 'none'},
                            {'AP1_SMOKE_REASONING_EFFORT': ''}, capsys)
    assert sampling['reasoning_effort'] == ''


def test_overrides_without_sampling_block(capsys):
    apply_sampling_overrides({}, {})
    assert capsys.readouterr().out == ('  temperature=None\n'
                                       '  reasoning_effort=None (from config)\n')


def test_overrides_read_os_environ_by_default(monkeypatch, capsys):
    monkeypatch.setenv('AP1_SMOKE_TEMPERATURE', '0.5')
    monkeypatch.delenv('AP1_SMOKE_REASONING_EFFORT', raising=False)
    config = {'sampling': {}}
    apply_sampling_overrides(config)
    assert config['sampling'] == {'temperature': '0.5'}


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


def test_parse_args_defaults_are_the_fixed_paths():
    args = parse_args([], BASE)
    assert vars(args) == {
        'config': '/repo/example/config.json',
        'fixture_dir': '/repo/example',
        'output_dir': '/repo/output',
        # V12-4: no fixed text; the run takes the text of the config's
        # ap1_version (execution/ap1_texts.py).
        'ap1_text': None,
    }


def test_parse_args_absolute_paths_kept():
    args = parse_args(['--config', '/a/c.json', '--fixture-dir', '/b',
                       '--output-dir', '/c/out', '--ap1-text', '/d/ap1.md'],
                      BASE)
    assert vars(args) == {'config': '/a/c.json', 'fixture_dir': '/b',
                          'output_dir': '/c/out', 'ap1_text': '/d/ap1.md'}


def test_parse_args_relative_paths_resolve_against_the_working_directory(
        tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    args = parse_args(['--config', 'c.json', '--fixture-dir', 'in',
                       '--output-dir', 'out/x', '--ap1-text', '../t.md'],
                      BASE)
    root = str(tmp_path.resolve())
    parent = str(tmp_path.resolve().parent)
    assert vars(args) == {'config': f'{root}/c.json',
                          'fixture_dir': f'{root}/in',
                          'output_dir': f'{root}/out/x',
                          'ap1_text': f'{parent}/t.md'}


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
        f'{pad}where the transcript, report and summary are written; files '
        'of the same name there are replaced (default: output/)\n'
        '  --ap1-text AP1_TEXT   the AP-1 text to seal; its hash must match '
        "the config's ap1_text_hash (default: the text of the config's "
        'ap1_version under reference/)\n')


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g3-seal-guards; see inbox/2026-10-20_step4-g3-seal-guards-report.md.

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
