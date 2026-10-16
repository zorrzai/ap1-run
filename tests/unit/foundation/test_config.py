"""Unit tests for R0.1 configuration loading and the minimum-n check
(foundation/config.py).

These pin today's behaviour. Where today's behaviour is a known or newly
found defect, the test carries @pytest.mark.finding and a comment saying
what the correct behaviour would be.
"""

import json
from decimal import Decimal
from pathlib import Path

import pytest

from ap1_run.foundation.config import (
    DECIMAL_FIELDS, KNOWN_SAMPLING_PARAMS, MINIMUM_N, OPTIONAL_FIELDS,
    PERMITTED_OMISSION_REASONS, REQUIRED_FIELDS, ConfigError,
    _refuse_bare_numerics, load_config, validate_minimum_n,
)

REPO = Path(__file__).resolve().parents[3]

PERMITTED_LIST = (
    "['answer_tolerance', 'ap1_text_hash', 'ap1_version', "
    "'ap1_version_doi', 'currency_symbols', 'decimal_separator', "
    "'decline_markers', 'dimensions_claimed', 'endpoint_url', "
    "'grouping_separator', 'model', 'permitted_transformations', "
    "'quantisation', 'repeat_count', 'sampling', 'structured_answer_field']")

REASONS = 'operator-declared, platform-rejected, platform-unsupported'


def valid_config(**overrides):
    """A minimal config that loads. A value of ... removes the field."""
    cfg = {
        'endpoint_url': 'http://test/v1/chat/completions',
        'model': 'test-model',
        'sampling': {'temperature': '0', 'max_completion_tokens': '4096'},
        'answer_tolerance': '0.01',
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
        'permitted_transformations': ['percent_to_fraction'],
        'decline_markers': ['I cannot'],
        'decimal_separator': '.',
        'grouping_separator': ',',
        'currency_symbols': ['$'],
        'dimensions_claimed': ['D1'],
        'repeat_count': '3',
        'structured_answer_field': 'none',
        'ap1_version': 'v1.3',
        'ap1_text_hash': 'abc',
        'ap1_version_doi': '10.5281/zenodo.1',
    }
    for k, v in overrides.items():
        if v is ...:
            cfg.pop(k, None)
        else:
            cfg[k] = v
    return cfg


@pytest.fixture
def load(tmp_path):
    """Write a config dict (or raw text) to a file and load it."""
    def _load(cfg=None, *, text=None, **overrides):
        p = tmp_path / 'config.json'
        if text is None:
            text = json.dumps(valid_config(**overrides) if cfg is None
                              else cfg)
        p.write_text(text, encoding='utf-8')
        return load_config(p)
    return _load


def refused(load, **overrides):
    with pytest.raises(ConfigError) as e:
        load(**overrides)
    return str(e.value)


def omission(reason, detail=None):
    o = {'value': 'omitted', 'reason': reason}
    if detail is not None:
        o['detail'] = detail
    return o


# -- module constants -----------------------------------------------------

@pytest.mark.req('R0.1')
def test_required_fields_are_the_sixteen_declared():
    assert REQUIRED_FIELDS == [
        'endpoint_url', 'model', 'sampling', 'answer_tolerance',
        'quantisation', 'permitted_transformations', 'decline_markers',
        'decimal_separator', 'grouping_separator', 'currency_symbols',
        'dimensions_claimed', 'repeat_count', 'structured_answer_field',
        'ap1_version', 'ap1_text_hash', 'ap1_version_doi']


def test_optional_fields():
    assert OPTIONAL_FIELDS == [
        'tools', 'tool_choice', 'system_prompt', 'system_prompt_base',
        'system_prompt_instruction_removed', 'fixture_hash',
        'message_template', 'runner_version_tag', 'runner_version_commit',
        'runner_modified']


def test_minimum_n_table():
    assert MINIMUM_N == {'D1': {'type': 'per_category', 'min': 10},
                         'D5': {'type': 'total', 'min': 20},
                         'D6': {'type': 'total', 'min': 10}}


def test_decimal_fields_and_known_sampling_params():
    assert DECIMAL_FIELDS == ['answer_tolerance']
    assert KNOWN_SAMPLING_PARAMS == {
        'temperature', 'top_p', 'seed', 'max_tokens',
        'max_completion_tokens', 'top_k', 'presence_penalty',
        'frequency_penalty', 'stop', 'reasoning_effort'}


def test_permitted_omission_reasons():
    assert PERMITTED_OMISSION_REASONS == {
        'operator-declared', 'platform-rejected', 'platform-unsupported'}


# -- load_config: a valid config ------------------------------------------

@pytest.mark.req('R0.1')
def test_load_config_valid_parses_typed_fields(load):
    cfg = load()
    assert cfg['answer_tolerance'] == Decimal('0.01')
    assert type(cfg['answer_tolerance']) is Decimal
    assert cfg['quantisation'] == {'places': 2, 'rounding': 'ROUND_HALF_UP'}
    assert cfg['repeat_count'] == 3
    assert cfg['structured_answer_field'] is None


def test_load_config_other_fields_passed_through(load):
    cfg = load()
    expected = valid_config()
    for k in ('endpoint_url', 'model', 'sampling', 'permitted_transformations',
              'decline_markers', 'decimal_separator', 'grouping_separator',
              'currency_symbols', 'dimensions_claimed', 'ap1_version',
              'ap1_text_hash', 'ap1_version_doi'):
        assert cfg[k] == expected[k]
    assert set(cfg) == set(expected)


def test_load_config_accepts_str_path(load, tmp_path):
    load()
    assert load_config(str(tmp_path / 'config.json'))['repeat_count'] == 3


def test_load_config_reads_utf8(load):
    cfg = load(decline_markers=['Je ne peux pas − désolé'])
    assert cfg['decline_markers'] == ['Je ne peux pas − désolé']


def test_load_config_named_structured_answer_field_kept(load):
    assert load(structured_answer_field='answer')[
        'structured_answer_field'] == 'answer'


def test_load_config_null_structured_answer_field_is_none(load):
    assert load(structured_answer_field=None)[
        'structured_answer_field'] is None


def test_load_config_optional_fields_accepted(load):
    cfg = load(tools=[{'type': 'function'}], tool_choice='auto',
               system_prompt='s', system_prompt_base='b',
               system_prompt_instruction_removed='r', fixture_hash='h',
               message_template='m', runner_version_tag='t',
               runner_version_commit='c', runner_modified=True)
    assert cfg['runner_modified'] is True
    assert cfg['tool_choice'] == 'auto'


def test_load_config_booleans_are_not_bare_numerics(load):
    assert load(runner_modified=False)['runner_modified'] is False


def test_load_config_example_config_loads():
    cfg = load_config(REPO / 'example' / 'config.json')
    assert cfg['repeat_count'] == 50
    assert cfg['answer_tolerance'] == Decimal('0.01')


# -- load_config: file-level errors ---------------------------------------

def test_load_config_missing_file_refused(tmp_path):
    p = tmp_path / 'absent.json'
    with pytest.raises(ConfigError) as e:
        load_config(p)
    assert str(e.value) == f'config file not found: {p}'


def test_load_config_invalid_json_refused(load, tmp_path):
    with pytest.raises(ConfigError) as e:
        load(text='{bad')
    msg = str(e.value)
    assert msg.startswith(f'invalid JSON in {tmp_path / "config.json"}: ')
    assert 'Expecting property name' in msg
    assert isinstance(e.value.__cause__, json.JSONDecodeError)


def test_load_config_non_object_refused(load):
    with pytest.raises(ConfigError) as e:
        load(text='[1, 2]')
    assert str(e.value) == 'config must be a JSON object, got list'


def test_load_config_json_nan_is_a_bare_numeric(load):
    # json.load reads NaN as a float, which the bare-numeric check refuses.
    with pytest.raises(ConfigError,
                       match='^bare numeric literal at fixture_hash: nan '):
        load(text=json.dumps(valid_config()).replace(
            '{', '{"fixture_hash": NaN, ', 1))


# -- load_config: required and unknown fields -----------------------------

@pytest.mark.req('R0.1')
@pytest.mark.parametrize('field', REQUIRED_FIELDS)
def test_load_config_each_missing_required_field_refused(load, field):
    assert refused(load, **{field: ...}) == \
        f'missing required field: {field!r}'


def test_load_config_missing_field_reported_before_unknown_field(load):
    assert refused(load, model=..., foo='x') == \
        "missing required field: 'model'"


def test_load_config_unknown_field_refused(load):
    assert refused(load, foo='x') == (
        "unrecognised top-level field: 'foo'. "
        f"Permitted top-level fields: {PERMITTED_LIST}")


def test_load_config_top_level_sampling_param_suggests_sampling(load):
    assert refused(load, temperature='0') == (
        "unrecognised top-level field: 'temperature'. Sampling parameters "
        'belong inside the "sampling" sub-dict, e.g. '
        '{"sampling": {"temperature": ...}}. '
        f"Permitted top-level fields: {PERMITTED_LIST}")


@pytest.mark.finding('S3-g1-15')
def test_load_config_unknown_field_message_omits_optional_fields(load):
    # Current behaviour: the list of permitted fields names only the
    # required ones, though the optional ones (tools, ...) are accepted.
    # Correct: list both.
    assert 'tools' not in refused(load, foo='x')


def test_load_config_unknown_field_reported_before_sampling_errors(load):
    msg = refused(load, foo='x', sampling={'temperature': 'omitted'})
    assert msg.startswith("unrecognised top-level field: 'foo'")


# -- load_config: sampling omissions --------------------------------------

@pytest.mark.req('R0.1')
def test_load_config_plain_omitted_refused(load):
    assert refused(load, sampling={'temperature': 'omitted'}) == (
        'sampling.temperature: omitted without a reason. '
        'Use {"value": "omitted", "reason": "...", "detail": "..."}. '
        f'Permitted reasons: {REASONS}')


def test_load_config_omission_operator_declared_needs_no_detail(load):
    cfg = load(sampling={'top_p': omission('operator-declared')})
    assert cfg['sampling'] == {'top_p': omission('operator-declared')}


@pytest.mark.parametrize('reason', ['platform-rejected',
                                    'platform-unsupported'])
def test_load_config_platform_omission_with_detail_accepted(load, reason):
    o = omission(reason, 'HTTP 400')
    assert load(sampling={'temperature': o})['sampling']['temperature'] == o


@pytest.mark.parametrize('reason', ['platform-rejected',
                                    'platform-unsupported'])
@pytest.mark.parametrize('detail', [None, ''])
def test_load_config_platform_omission_without_detail_refused(
        load, reason, detail):
    assert refused(load, sampling={'temperature': omission(reason, detail)}) \
        == f'sampling.temperature: detail is required when reason is {reason!r}'


def test_load_config_omission_without_reason_refused(load):
    assert refused(load, sampling={'seed': {'value': 'omitted'}}) == (
        f'sampling.seed: invalid or missing reason None. '
        f'Permitted reasons: {REASONS}')


def test_load_config_omission_unknown_reason_refused(load):
    assert refused(load, sampling={'seed': omission('because', 'x')}) == (
        "sampling.seed: invalid or missing reason 'because'. "
        f'Permitted reasons: {REASONS}')


@pytest.mark.finding('F1', 'T3-79')
def test_load_config_model_unsupported_reason_refused(load):
    # Current behaviour: 'model-unsupported', the reason used in
    # example/config_mini.json, is not a permitted reason. Correct: either
    # the reason is permitted or the shipped config uses a permitted one;
    # the two must agree.
    o = omission('model-unsupported', 'not a reasoning model')
    assert refused(load, sampling={'reasoning_effort': o}).startswith(
        "sampling.reasoning_effort: invalid or missing reason "
        "'model-unsupported'.")


@pytest.mark.finding('F1', 'T3-79')
def test_load_config_example_config_mini_refused():
    # Current behaviour: the shipped example/config_mini.json does not
    # load (regression scenario mini_config). Correct: it loads.
    with pytest.raises(ConfigError, match="sampling.reasoning_effort: "
                       "invalid or missing reason 'model-unsupported'"):
        load_config(REPO / 'example' / 'config_mini.json')


@pytest.mark.finding('T3-67')
def test_load_config_not_supported_reason_refused(load):
    # The reason smoke_test.py writes for AP1_SMOKE_REASONING_EFFORT=omit
    # into the sealed config; load_config refuses it (T3-67).
    o = omission('not-supported', 'x')
    assert 'invalid or missing reason' in refused(
        load, sampling={'reasoning_effort': o})


def test_load_config_omission_checked_before_bare_numerics(load):
    # The omission error wins over a bare numeric elsewhere.
    msg = refused(load, sampling={'temperature': 'omitted'}, repeat_count=3)
    assert msg.startswith('sampling.temperature: omitted without a reason')


@pytest.mark.finding('S3-g1-14')
def test_load_config_sampling_not_an_object_loads(load):
    # Current behaviour: a non-object 'sampling' skips validation and
    # loads. Correct: refuse, as for 'quantisation'.
    assert load(sampling='x')['sampling'] == 'x'


# -- load_config: bare numerics -------------------------------------------

@pytest.mark.req('R0.1')
def test_load_config_bare_float_refused(load):
    assert refused(load, answer_tolerance=0.01) == (
        'bare numeric literal at answer_tolerance: 0.01 -- numeric values '
        'must be quoted strings, e.g. "0.01" not 0.01')


@pytest.mark.req('R0.1')
def test_load_config_bare_int_refused(load):
    assert refused(load, repeat_count=50).startswith(
        'bare numeric literal at repeat_count: 50 --')


def test_load_config_bare_numeric_path_nested_dict(load):
    assert refused(load, sampling={'temperature': 0}).startswith(
        'bare numeric literal at sampling.temperature: 0 --')


def test_load_config_bare_numeric_path_list_index(load):
    assert refused(load, tools=[{'a': 'x'}, {'a': [1.5]}]).startswith(
        'bare numeric literal at tools[1].a[0]: 1.5 --')


def test_load_config_bare_numeric_in_top_level_list(load):
    assert refused(load, decline_markers=['x', 7]).startswith(
        'bare numeric literal at decline_markers[1]: 7 --')


def test_load_config_bare_numeric_inside_omission_value_refused(load):
    # {'value': 0.5} is not an omission (value is not 'omitted').
    assert refused(load, sampling={'t': {'value': 0.5}}).startswith(
        'bare numeric literal at sampling.t.value: 0.5 --')


def test_load_config_omission_shape_needs_reason_to_skip_check(load):
    # An omission-shaped object without 'reason' outside sampling is walked.
    assert refused(load, tools=[{'value': 'omitted', 'n': 5}]).startswith(
        'bare numeric literal at tools[0].n: 5 --')


@pytest.mark.finding('S3-g1-13')
def test_load_config_omission_shaped_object_skips_bare_numeric_check(load):
    # Current behaviour: any object with value 'omitted' and a 'reason'
    # key, anywhere in the tree and with any reason, is not walked, so the
    # bare 5 is accepted. Correct: skip only validated sampling omissions,
    # and still refuse bare numerics inside them.
    cfg = load(tools=[{'value': 'omitted', 'reason': 'any', 'n': 5}])
    assert cfg['tools'] == [{'value': 'omitted', 'reason': 'any', 'n': 5}]


@pytest.mark.finding('S3-g1-13')
def test_load_config_bare_numeric_detail_in_omission_accepted(load):
    o = {'value': 'omitted', 'reason': 'operator-declared', 'detail': 5}
    assert load(sampling={'top_p': o})['sampling']['top_p']['detail'] == 5


def test_refuse_bare_numerics_root_value_named_root():
    # Unreachable through load_config, which refuses a non-object first.
    with pytest.raises(ConfigError) as e:
        _refuse_bare_numerics(5)
    assert str(e.value) == ('bare numeric literal at root: 5 -- numeric '
                            'values must be quoted strings, e.g. "5" not 5')


# -- load_config: answer_tolerance ----------------------------------------

@pytest.mark.parametrize('value, type_name', [(True, 'bool'),
                                              (None, 'NoneType'),
                                              (['0.01'], 'list')])
def test_load_config_tolerance_not_a_string_refused(load, value, type_name):
    assert refused(load, answer_tolerance=value) == (
        f'answer_tolerance: expected quoted string, got {type_name}: '
        f'{value!r}')


def test_load_config_tolerance_not_a_number_refused(load):
    assert refused(load, answer_tolerance='x') == \
        "answer_tolerance: cannot parse as Decimal: 'x'"


def test_load_config_tolerance_keeps_exact_text(load):
    assert str(load(answer_tolerance='0.0050')['answer_tolerance']) == \
        '0.0050'


@pytest.mark.finding('S3-g1-11')
def test_load_config_tolerance_nan_and_negative_accepted(load):
    # Current behaviour: any Decimal() text loads, including NaN and
    # negative values. Correct: refuse; a tolerance is finite and >= 0.
    assert load(answer_tolerance='NaN')['answer_tolerance'].is_nan()
    assert load(answer_tolerance='-1')['answer_tolerance'] == Decimal('-1')


# -- load_config: quantisation --------------------------------------------

def test_load_config_quantisation_not_an_object_refused(load):
    assert refused(load, quantisation='2') == \
        'quantisation must be an object'


def test_load_config_quantisation_half_even_kept(load):
    assert load(quantisation={'places': '4', 'rounding': 'ROUND_HALF_EVEN'})[
        'quantisation'] == {'places': 4, 'rounding': 'ROUND_HALF_EVEN'}


def test_load_config_quantisation_extra_keys_dropped(load):
    q = {'places': '2', 'rounding': 'ROUND_HALF_UP', 'note': 'x'}
    assert load(quantisation=q)['quantisation'] == {
        'places': 2, 'rounding': 'ROUND_HALF_UP'}


@pytest.mark.finding('T3-51')
def test_load_config_empty_quantisation_gets_defaults(load):
    # Current behaviour: {} loads as places 2, ROUND_HALF_UP. Correct
    # (R0.1, no defaults for anything affecting a result): refuse.
    assert load(quantisation={})['quantisation'] == {
        'places': 2, 'rounding': 'ROUND_HALF_UP'}


@pytest.mark.finding('T3-51')
def test_load_config_quantisation_rounding_not_validated(load):
    # Current behaviour: any rounding string loads; quantise() fails later.
    # Correct: refuse a mode quantise() does not support.
    assert load(quantisation={'places': '2', 'rounding': 'BOGUS'})[
        'quantisation']['rounding'] == 'BOGUS'


@pytest.mark.finding('S3-g1-10')
def test_load_config_quantisation_places_not_integer_raises_valueerror(load):
    # Current behaviour: int('abc') escapes as ValueError, not ConfigError.
    # Correct: ConfigError naming quantisation.places.
    with pytest.raises(ValueError, match="invalid literal for int"):
        load(quantisation={'places': 'abc', 'rounding': 'ROUND_HALF_UP'})


@pytest.mark.finding('S3-g1-10')
def test_load_config_quantisation_places_bool_and_negative_accepted(load):
    # Current behaviour: places true loads as 1 (booleans pass the
    # bare-numeric check) and '-2' as -2. Correct: a quoted non-negative
    # integer only.
    assert load(quantisation={'places': True})['quantisation']['places'] == 1
    assert load(quantisation={'places': '-2'})['quantisation']['places'] == -2


# -- load_config: repeat_count --------------------------------------------

@pytest.mark.parametrize('value, type_name', [(True, 'bool'),
                                              (None, 'NoneType'),
                                              (['3'], 'list')])
def test_load_config_repeat_count_not_a_string_refused(load, value,
                                                       type_name):
    assert refused(load, repeat_count=value) == \
        f'repeat_count: expected quoted string, got {type_name}'


def test_load_config_repeat_count_not_an_integer_refused(load):
    assert refused(load, repeat_count='5.0') == \
        "repeat_count: cannot parse as integer: '5.0'"


def test_load_config_repeat_count_surrounding_spaces_accepted(load):
    assert load(repeat_count=' 5 ')['repeat_count'] == 5


@pytest.mark.finding('S3-g1-12')
def test_load_config_repeat_count_zero_and_negative_accepted(load):
    # Current behaviour: '0' and '-3' load. Correct: refuse a repeat count
    # below 1.
    assert load(repeat_count='0')['repeat_count'] == 0
    assert load(repeat_count='-3')['repeat_count'] == -3


# -- load_config: dimensions ----------------------------------------------

@pytest.mark.finding('T3-12')
def test_load_config_unknown_dimension_loads(load):
    # Current behaviour: 'D99' is accepted at load. Correct: refuse a
    # dimension AP-1 does not define.
    assert load(dimensions_claimed=['D99'])['dimensions_claimed'] == ['D99']


# -- validate_minimum_n ---------------------------------------------------

def questions(n, category=None):
    qs = [{'id': f'Q{i}'} for i in range(n)]
    if category is not None:
        for q in qs:
            q['category'] = category
    return qs


@pytest.mark.req('R0.1')
def test_minimum_n_d6_below_minimum_refused():
    with pytest.raises(ConfigError) as e:
        validate_minimum_n({'dimensions_claimed': ['D6']}, questions(9))
    assert str(e.value) == 'D6: 9 items, minimum 10 required'


def test_minimum_n_d6_at_minimum_accepted():
    assert validate_minimum_n({'dimensions_claimed': ['D6']},
                              questions(10)) is None


def test_minimum_n_d5_below_minimum_refused():
    with pytest.raises(ConfigError, match='^D5: 19 items, minimum 20 '
                                          'required$'):
        validate_minimum_n({'dimensions_claimed': ['D5']}, questions(19))


def test_minimum_n_d5_at_minimum_accepted():
    validate_minimum_n({'dimensions_claimed': ['D5']}, questions(20))


@pytest.mark.req('R0.1')
def test_minimum_n_d1_small_category_refused():
    qs = questions(10, 'A') + questions(9, 'B')
    with pytest.raises(ConfigError) as e:
        validate_minimum_n({'dimensions_claimed': ['D1']}, qs)
    assert str(e.value) == "D1 category 'B': 9 items, minimum 10 required"


def test_minimum_n_d1_every_category_at_minimum_accepted():
    validate_minimum_n({'dimensions_claimed': ['D1']},
                       questions(10, 'A') + questions(10, 'B'))


def test_minimum_n_d1_uncategorised_items_share_default_category():
    with pytest.raises(ConfigError, match="category 'default': 9 items"):
        validate_minimum_n({'dimensions_claimed': ['D1']}, questions(9))
    validate_minimum_n({'dimensions_claimed': ['D1']}, questions(10))


def test_minimum_n_d1_first_failing_category_reported():
    qs = questions(3, 'A') + questions(4, 'B')
    with pytest.raises(ConfigError, match="category 'A': 3 items"):
        validate_minimum_n({'dimensions_claimed': ['D1']}, qs)


def test_minimum_n_checks_every_claimed_dimension():
    with pytest.raises(ConfigError, match='^D5:'):
        validate_minimum_n({'dimensions_claimed': ['D6', 'D5']},
                           questions(10))


def test_minimum_n_unlisted_dimension_does_not_stop_the_check():
    with pytest.raises(ConfigError, match='^D6:'):
        validate_minimum_n({'dimensions_claimed': ['D2', 'D6']},
                           questions(9))


def test_minimum_n_no_claims_accepted():
    validate_minimum_n({}, [])
    validate_minimum_n({'dimensions_claimed': []}, [])


@pytest.mark.finding('T3-12')
def test_minimum_n_unknown_or_unlisted_dimensions_skipped():
    # Current behaviour: dimensions without a MINIMUM_N entry (D2, D7,
    # D99) are skipped. Correct: refuse an undefined dimension.
    validate_minimum_n({'dimensions_claimed': ['D2', 'D7', 'D99']}, [])


@pytest.mark.finding('T3-12')
def test_minimum_n_d1_total_not_checked():
    # Current behaviour: 2 categories of 10 (20 items) satisfy D1. Correct
    # (AP-1 v1.3 D1): at least 40 items in total as well.
    validate_minimum_n({'dimensions_claimed': ['D1']},
                       questions(10, 'A') + questions(10, 'B'))


@pytest.mark.finding('T3-12')
def test_minimum_n_d5_counts_every_question():
    # Current behaviour: D5 and D6 count all questions, not the
    # adversarial or conflicting-input items. Correct: count eligible
    # items only.
    validate_minimum_n({'dimensions_claimed': ['D5', 'D6']},
                       questions(20, 'ordinary'))

