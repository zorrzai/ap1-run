"""Unit tests for the runner's settings from the environment and the
R1.2 condition guard."""

import hashlib

import pytest

from ap1_run.execution.perturbation_guard import PerturbationRefusal
from ap1_run.runner import settings
from ap1_run.runner.settings import (
    check_condition_guard, parse_args, print_sampling,
)


# -- endpoint and model: from the config only -----------------------------

@pytest.mark.finding('T3-80')
def test_no_endpoint_or_model_from_the_environment():
    # Section B decision (T3-80), following the F1 ruling: model and
    # endpoint come from the config file only; there is no environment
    # lookup and no gpt-4o-mini / api.openai.com default.
    for name in ('endpoint_and_model', 'DEFAULT_ENDPOINT', 'DEFAULT_MODEL'):
        assert not hasattr(settings, name), name


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
    check_condition_guard(config, fixture_file, 'BASE', 'REMOVED',
                          ['tool'], {'temperature': 0})
    fixture_hash = hashlib.sha256(b'{"accounts": []}\n').hexdigest()
    base = {'system_prompt': 'BASE', 'tools': ['tool'], 'tool_choice': 'auto',
            'sampling': {'temperature': 0}, 'fixture_hash': fixture_hash,
            'message_template': 'T'}
    assert seen == [(base, dict(base, system_prompt='REMOVED'))]
    assert capsys.readouterr().out == (
        'Perturbation guard: PASSED (single-variable: system_prompt only)\n\n')


def test_guard_with_the_real_check(fixture_file, capsys):
    check_condition_guard({}, fixture_file, 'A', 'B', [], {})
    assert 'PASSED' in capsys.readouterr().out


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
        'ap1_text': '/repo/reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md',
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
        'endpoint, the model and every other setting come from the config; '
        'only the API key comes from the environment (AP1_SMOKE_API_KEY).\n'
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
        'the one the runner expects '
        '(default: reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md)\n')


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g3-seal-guards; see inbox/2026-10-20_step4-g3-seal-guards-report.md.

@pytest.mark.finding('T3-46')
@pytest.mark.req('R1.2', 'AP-1 D7.8')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-46: the live condition guard passes identical '
                          'prompts and prints PASSED')
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
