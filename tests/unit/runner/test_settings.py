"""Unit tests for the runner's settings from the environment and the
R1.2 condition guard."""

import hashlib

import pytest

from ap1_run.execution.perturbation_guard import PerturbationRefusal
from ap1_run.runner import settings
from ap1_run.runner.settings import (
    DEFAULT_ENDPOINT, DEFAULT_MODEL, apply_sampling_overrides,
    check_condition_guard, endpoint_and_model,
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
