"""Unit tests for the R1.2 single-variable perturbation guard: the
instruction_removed condition may change the system prompt and nothing
else."""

from decimal import Decimal

import pytest

from ap1_run.execution.perturbation_guard import (
    HELD_CONSTANT, PerturbationRefusal, _canonical, _summarise,
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


IDENTICAL = ('instruction_removed condition does not change the system '
             'prompt (must change exactly 1 quantity: system_prompt): the '
             'system prompts are IDENTICAL. Other changed quantities:')

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
def test_guard_held_constant_names_every_compared_quantity():
    # What the guard compares is what the report says was held constant
    # (D7.8), through HELD_CONSTANT.
    assert HELD_CONSTANT == ('tool declarations', 'tool_choice',
                             'sampling parameters', 'fixture content',
                             'message structure template')


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


@pytest.mark.finding('T3-46')
@pytest.mark.req('R1.2', 'AP-1 D7.8')
@pytest.mark.parametrize('base, other, rest', [
    (BASE, dict(BASE), ' none'),
    ({}, {}, ' none'),
    (BASE, {**BASE, 'tool_choice': 'none'},
     '\n  - tool_choice: tool_choice differs between conditions'),
    (BASE, {**BASE, 'tools': [], 'fixture_hash': 'x'},
     '\n  - tools: tool declarations differ between conditions'
     '\n  - fixture_content: fixture content differs between conditions'),
], ids=['identical', 'both-missing', 'plus-tool-choice', 'plus-two'])
def test_guard_identical_prompts_refusal_message(base, other, rest):
    assert refusal(base, other) == IDENTICAL + rest


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


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g3-seal-guards; see inbox/2026-10-20_step4-g3-seal-guards-report.md.

def refusal_or_none(base, other):
    """The PerturbationRefusal message, or None if the guard passed. (Not
    pytest.raises, whose DID NOT RAISE is not an AssertionError.)"""
    try:
        check_single_variable_perturbation(base, other)
    except PerturbationRefusal as exc:
        return str(exc)
    return None


@pytest.mark.finding('T3-46')
@pytest.mark.req('R1.2', 'AP-1 D7.8')
def test_guard_identical_prompts_refused():
    # Correct (AP-1 v1.3 D7.8: the instruction-removal condition "shall
    # vary the instruction"; SPEC R1.2 l.316-321): if the two system
    # prompts are identical nothing was perturbed, both arms are the same
    # condition, and the run is refused rather than reported as a
    # contrast. The refusal names the system prompt.
    msg = refusal_or_none(BASE, dict(BASE))
    assert msg is not None, 'identical prompts passed the guard'
    assert 'system_prompt' in msg


@pytest.mark.finding('T3-46')
@pytest.mark.req('R1.2', 'AP-1 D7.8')
def test_guard_identical_prompts_plus_violation_refusal_says_prompt_unchanged():
    # Correct: the refusal emits the true diff (SPEC R1.2: "refused, not
    # reported, with the diff emitted"). Here the prompt did not change
    # and tool_choice did; the message must not call the prompt "the one
    # allowed change", and must say the prompts are identical.
    msg = refusal_or_none(BASE, {**BASE, 'tool_choice': 'none'})
    assert msg is not None
    assert 'tool_choice' in msg
    assert 'the one allowed change' not in msg
    assert 'identical' in msg.lower()


@pytest.mark.finding('S3-G7-2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G7-2: the guard compares a fixed field list; '
                          'a change of model passes')
@pytest.mark.req('AP-1 D7.8', 'R1.2')
def test_guard_model_changed_with_prompt_refused_naming_model():
    # AP-1 v1.3 D7.8 holds "all other request content" constant; SPEC R1.2:
    # "A run in which more than one quantity differs is refused", with the
    # diff naming every changed quantity.
    base = {**BASE, 'model': 'model-a'}
    other = {**removed(), 'model': 'model-b'}
    try:
        check_single_variable_perturbation(base, other)
    except PerturbationRefusal as e:
        message = str(e)
    else:
        message = None
    assert message is not None and 'model' in message, message
