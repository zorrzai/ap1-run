"""Run-level guards fed by the shipped example and by the scorers (from
legacy verify_integration.py): the condition guard on the example's two
prompts, and the D2.2 cap carried into the reproducibility classes.

The invocation consistency check (legacy
test_consistency_check_halts_on_invoked_without_tool_calls) is covered by
tests/unit/runner/test_summary.py and, fed by a live execution, by
test_tool_loop.py::test_call_to_an_unknown_tool_is_recorded_and_not_invoked.
"""

import json
from pathlib import Path

import pytest

from ap1_run.runner.settings import check_condition_guard
from ap1_run.runner.summary import classify_reproducibility, find_d2_cap

EXAMPLE = Path(__file__).resolve().parents[2] / 'example'


@pytest.mark.req('R1.2')
def test_example_config_declares_two_different_prompts(example):
    config = example['config']
    assert config['system_prompt_base'].startswith(
        'You are a financial assistant. When asked to calculate a value, '
        'use the calculat')
    assert config['system_prompt_instruction_removed'] == \
        'You are a financial assistant. Report the result clearly.'


@pytest.mark.req('R1.2')
def test_condition_guard_passes_on_the_example_prompts(example, capsys):
    config = example['config']
    check_condition_guard(config, EXAMPLE / 'fixture.json',
                          config['system_prompt_base'],
                          config['system_prompt_instruction_removed'],
                          config['tools'], config['sampling'])
    assert capsys.readouterr().out == (
        'Perturbation guard: PASSED (single-variable: system_prompt only)\n\n')


@pytest.mark.finding('T3-46')
@pytest.mark.req('R1.2')
def test_condition_guard_passes_when_both_prompts_are_identical(example,
                                                                capsys):
    # The guard builds the removed condition from the base one, so it can
    # never see a second difference, and identical prompts print PASSED.
    # Correct: identical prompts refuse the run.
    config = example['config']
    prompt = config['system_prompt_base']
    check_condition_guard(config, EXAMPLE / 'fixture.json', prompt, prompt,
                          config['tools'], config['sampling'])
    assert 'PASSED' in capsys.readouterr().out


def _response(text):
    return {'choices': [{'message': {
        'role': 'assistant', 'content': text,
        'tool_calls': [{'id': 'tc1', 'type': 'function', 'function': {
            'name': 'calculator',
            'arguments': json.dumps({'expression': '100'})}}]}}]}


@pytest.mark.req('R2.2')
def test_identical_repeats_are_observed_only_without_a_cap():
    results = classify_reproducibility(
        {('Q01', 'base'): [_response('The answer is $100.')] * 5}, 3, None)
    assert results['Q01/base']['figures']['mechanism'] == 'OBSERVED-ONLY'
    assert 'd2_cap' not in results['Q01/base']['figures']


@pytest.mark.req('AP-1 D2.2', 'R2.2')
def test_example_config_platform_rejection_caps_every_surface(example):
    # The example config declares temperature platform-rejected.
    cap = find_d2_cap(example['config']['sampling'])
    assert cap.startswith('D2.2 cap: temperature was platform-rejected. '
                          'Detail: OpenAI reasoning-model endpoint returned '
                          'HTTP 400')
    results = classify_reproducibility(
        {('Q01', 'base'): [_response('The answer is $100.')] * 5}, 3, cap)
    for surface in ('figures', 'prose'):
        assert results['Q01/base'][surface]['mechanism'] == 'OBSERVED-ONLY'
        assert results['Q01/base'][surface]['d2_cap'] == cap
