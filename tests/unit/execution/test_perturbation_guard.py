"""Unit tests for the R1.2 single-variable perturbation guard: the
instruction_removed condition may change the system prompt and nothing
else."""

from decimal import Decimal

import pytest

from ap1_run.execution.perturbation_guard import (
    PerturbationRefusal, _canonical, _summarise,
    check_single_variable_perturbation,
)

BASE = {
    'system_prompt': 'Use the calculator.',
    'tools': [{'type': 'function', 'function': {'name': 'calculator'}}],
    'tool_choice': 'auto',
    'sampling': {'temperature': 0, 'max_tokens': 100},
    'fixture_hash': 'abc',
    'message_template': {'role': 'user'},
}


def removed(**changes):
    return {**BASE, 'system_prompt': 'Answer.', **changes}


IDENTICAL = {'field': 'system_prompt',
             'issue': 'system prompts are IDENTICAL — '
                      'instruction_removed must alter the system prompt'}

HEADER = ('instruction_removed condition changes {n} quantities (must be '
          'exactly 1: system_prompt). Changed quantities:\n'
          '  - system_prompt: the one allowed change\n')


def refusal(base, other):
    with pytest.raises(PerturbationRefusal) as exc:
        check_single_variable_perturbation(base, other)
    return str(exc.value)


# -- accepted ---------------------------------------------------------------

@pytest.mark.req('R1.2')
def test_guard_only_system_prompt_differs_returns_empty_list():
    assert check_single_variable_perturbation(BASE, removed()) == []


def test_guard_empty_configs_with_different_prompts_pass():
    assert check_single_variable_perturbation(
        {'system_prompt': 'a'}, {'system_prompt': 'b'}) == []


def test_guard_dict_key_order_does_not_matter():
    other = removed(sampling={'max_tokens': 100, 'temperature': 0},
                    tools=[{'function': {'name': 'calculator'},
                            'type': 'function'}])
    assert check_single_variable_perturbation(BASE, other) == []


def test_guard_missing_tools_and_template_equal_none():
    base = {k: v for k, v in BASE.items()
            if k not in ('tools', 'message_template')}
    other = {**base, 'system_prompt': 'x', 'tools': None,
             'message_template': None}
    assert check_single_variable_perturbation(base, other) == []


def test_guard_missing_sampling_equals_empty_sampling():
    base = {k: v for k, v in BASE.items() if k != 'sampling'}
    assert check_single_variable_perturbation(
        base, {**base, 'system_prompt': 'x', 'sampling': {}}) == []


@pytest.mark.finding('T3-46')
def test_guard_identical_prompts_returned_not_refused():
    # Current behaviour: identical prompts give a diff entry but no
    # refusal, so both arms run the same prompt and are reported as a
    # contrast. Correct: identical prompts are refused (D7.8).
    assert check_single_variable_perturbation(BASE, dict(BASE)) == [IDENTICAL]


@pytest.mark.finding('T3-46')
def test_guard_identical_missing_prompts_returned_not_refused():
    assert check_single_variable_perturbation({}, {}) == [IDENTICAL]


@pytest.mark.finding('T3-46')
def test_guard_valid_result_does_not_report_what_is_held_constant():
    # Current behaviour: a valid pair returns [], with no record of what
    # was held constant. Correct (D7.8): what is held constant is reported.
    assert check_single_variable_perturbation(BASE, removed()) == []


# -- refused ----------------------------------------------------------------

@pytest.mark.req('R1.2')
@pytest.mark.parametrize('key, value, line', [
    ('tools', [], 'tools: tool declarations differ between conditions'),
    ('tool_choice', 'none', 'tool_choice: tool_choice differs between conditions'),
    ('sampling', {'temperature': 1, 'max_tokens': 100},
     'sampling: sampling parameters differ between conditions'),
    ('fixture_hash', 'def', 'fixture_content: fixture content differs between conditions'),
    ('message_template', {'role': 'system'},
     'message_template: message structure template differs'),
])
def test_guard_one_other_change_refused_naming_it(key, value, line):
    assert refusal(BASE, removed(**{key: value})) == \
        HEADER.format(n=2) + f'  - {line}'


def test_guard_every_change_named_in_order():
    other = removed(tools=None, tool_choice=None, sampling=None,
                    fixture_hash=None, message_template=None)
    msg = refusal(BASE, other)
    assert msg.startswith(HEADER.format(n=6))
    assert [line.split(':')[0] for line in msg.split('\n')[1:]] == [
        '  - system_prompt', '  - tools', '  - tool_choice', '  - sampling',
        '  - fixture_content', '  - message_template']


@pytest.mark.finding('T3-46')
def test_guard_identical_prompts_plus_violation_says_prompt_changed():
    # Current behaviour: with identical prompts and one forbidden change,
    # the refusal still lists system_prompt as "the one allowed change"
    # and counts 2 changed quantities. Correct: 1 changed (the forbidden
    # one), and the prompt reported as unchanged.
    assert refusal(BASE, {**BASE, 'tool_choice': 'none'}) == \
        HEADER.format(n=2) + \
        '  - tool_choice: tool_choice differs between conditions'


def test_guard_none_sampling_differs_from_missing_sampling():
    base = {k: v for k, v in BASE.items() if k != 'sampling'}
    assert 'sampling' in refusal(base, {**base, 'system_prompt': 'x',
                                        'sampling': None})


def test_guard_list_order_in_tools_matters():
    tools = [{'name': 'a'}, {'name': 'b'}]
    assert 'tools:' in refusal({**BASE, 'tools': tools},
                               removed(tools=tools[::-1]))


@pytest.mark.finding('T3-71')
def test_guard_compares_non_json_values_through_str():
    # Current behaviour: values JSON cannot encode are compared by str(),
    # so Decimal('0.0') and the string '0.0' count as the same sampling.
    # (Same type-loss as canonical JSON, T3-71.)
    assert check_single_variable_perturbation(
        {**BASE, 'sampling': {'temperature': Decimal('0.0')}},
        removed(sampling={'temperature': '0.0'})) == []


def test_guard_int_and_string_sampling_differ():
    assert 'sampling:' in refusal(
        {**BASE, 'sampling': {'temperature': 0}},
        removed(sampling={'temperature': '0'}))


# -- helpers ----------------------------------------------------------------

def test_canonical_none_is_null():
    assert _canonical(None) == 'null'


def test_canonical_sorted_keys_default_separators():
    assert _canonical({'b': 1, 'a': [Decimal('2')]}) == '{"a": ["2"], "b": 1}'


def test_summarise_short_value_unchanged():
    assert _summarise({'b': 1, 'a': None}) == '{"a": null, "b": 1}'


def test_summarise_200_characters_not_truncated():
    s = 'x' * 198                      # json.dumps adds two quotes
    assert _summarise(s) == '"' + s + '"'


def test_summarise_long_value_truncated_to_200_plus_ellipsis():
    s = 'y' * 199
    assert _summarise(s) == '"' + 'y' * 199 + '...'


def test_summarise_uses_str_for_non_json_values():
    assert _summarise([Decimal('1.5')]) == '["1.5"]'
