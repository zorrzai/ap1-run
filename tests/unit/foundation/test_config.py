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

# Required and optional fields, sorted (S3-G1-15: the optional ones are
# listed too).
PERMITTED_LIST = (
    "['answer_tolerance', 'ap1_text_hash', 'ap1_version', "
    "'ap1_version_doi', 'currency_symbols', 'decimal_separator', "
    "'decline_markers', 'dimensions_claimed', 'endpoint_url', "
    "'fixture_hash', 'grouping_separator', 'message_template', 'model', "
    "'permitted_transformations', 'quantisation', 'repeat_count', "
    "'runner_modified', 'runner_version_commit', 'runner_version_tag', "
    "'sampling', 'structured_answer_field', 'system_prompt', "
    "'system_prompt_base', 'system_prompt_instruction_removed', "
    "'tool_choice', 'tools']")

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


# -- load_config: value checks (step 5 numeric-hardening) ------------------

@pytest.mark.finding('S3-G1-10')
@pytest.mark.parametrize('places, message', [
    (True, "quantisation.places: expected quoted string, got bool: True"),
    (None, "quantisation.places: expected quoted string, got NoneType: None"),
    ('abc', "quantisation.places: cannot parse as integer: 'abc'"),
    ('1.5', "quantisation.places: cannot parse as integer: '1.5'"),
    ('-1', "quantisation.places: must be a non-negative integer: '-1'"),
])
def test_load_config_quantisation_places_refusal_messages(load, places,
                                                          message):
    assert refused(load, quantisation={'places': places,
                                       'rounding': 'ROUND_HALF_UP'}) == message


@pytest.mark.finding('S3-G1-10')
def test_load_config_quantisation_places_zero_loads(load):
    assert load(quantisation={'places': '0', 'rounding': 'ROUND_HALF_UP'})[
        'quantisation']['places'] == 0


@pytest.mark.finding('S3-G1-11')
@pytest.mark.parametrize('tolerance', ['NaN', 'sNaN', '-Infinity', '-0.01'])
def test_load_config_tolerance_refusal_message(load, tolerance):
    assert refused(load, answer_tolerance=tolerance) == (
        f'answer_tolerance: must be a finite, non-negative number: '
        f'{tolerance!r}')


@pytest.mark.finding('S3-G1-11')
def test_load_config_tolerance_zero_loads(load):
    assert load(answer_tolerance='0')['answer_tolerance'] == Decimal('0')


@pytest.mark.finding('S3-G1-12')
def test_load_config_repeat_count_refusal_message_and_one_loads(load):
    assert refused(load, repeat_count='0') == \
        "repeat_count: must be at least 1: '0'"
    assert load(repeat_count='1')['repeat_count'] == 1


@pytest.mark.finding('S3-G1-14')
def test_load_config_sampling_refusal_message(load):
    assert refused(load, sampling=['0']) == \
        "sampling must be an object, got list: ['0']"


@pytest.mark.finding('S3-G1-13')
def test_load_config_valid_sampling_omission_still_loads(load):
    o = omission('platform-rejected', 'the endpoint refused 0.5')
    assert load(sampling={'top_p': o})['sampling']['top_p'] == o


@pytest.mark.finding('S3-G1-19')
@pytest.mark.parametrize('value', ['NaN', 'Infinity', '-inf'])
def test_load_config_non_finite_sampling_value_refused(load, value):
    assert refused(load, sampling={'temperature': value}) == \
        f'sampling.temperature: must be a finite number: {value!r}'


@pytest.mark.finding('S3-G1-21')
@pytest.mark.parametrize('key', ['model', 'messages', 'tools'])
def test_load_config_sampling_body_field_refused(load, key):
    assert refused(load, sampling={key: 'x'}) == \
        f'sampling.{key}: a request body field, not a sampling parameter'


def test_load_config_non_numeric_sampling_string_loads(load):
    assert load(sampling={'reasoning_effort': 'low'})['sampling'] == \
        {'reasoning_effort': 'low'}


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



# --- Step 4: correct behaviour (failing until fixed) ---

def load_outcome(load, **overrides):
    """'refused: <message>' on ConfigError; otherwise what happened, as a
    string, so a test can assert on it (a loaded config's relevant field,
    or another exception's type and message)."""
    try:
        cfg = load(**overrides)
    except ConfigError as e:
        return f'refused: {e}'
    except Exception as e:
        return f'raised {type(e).__name__}: {e}'
    return 'loaded: ' + repr({k: cfg[k] for k in overrides})


@pytest.mark.finding('S3-G1-10')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('places', ['abc', True, '-2', '1.5'])
def test_load_config_quantisation_places_invalid_is_refused_by_name(load,
                                                                    places):
    # SPEC R0.1: "a value that cannot be so parsed is refused", with a
    # named error. places is a quoted non-negative integer; anything else
    # is a ConfigError naming quantisation.places.
    outcome = load_outcome(load, quantisation={'places': places,
                                               'rounding': 'ROUND_HALF_UP'})
    assert outcome.startswith('refused: ') and 'places' in outcome, outcome


@pytest.mark.finding('S3-G1-11')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('tolerance', ['NaN', 'Infinity', '-1', '-0.01'])
def test_load_config_tolerance_not_finite_nonnegative_is_refused(load,
                                                                 tolerance):
    # A tolerance is a finite, non-negative bound: NaN makes every
    # comparison False, a negative one makes every answer INCORRECT.
    outcome = load_outcome(load, answer_tolerance=tolerance)
    assert outcome.startswith('refused: answer_tolerance'), outcome


@pytest.mark.finding('S3-G1-12')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('count', ['0', '-3'])
def test_load_config_repeat_count_below_one_is_refused(load, count):
    # A run of zero (or fewer) repeats measures nothing; refuse at load.
    outcome = load_outcome(load, repeat_count=count)
    assert outcome.startswith('refused: repeat_count'), outcome


@pytest.mark.finding('S3-G1-13')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('overrides', [
    {'tools': [{'value': 'omitted', 'reason': 'any', 'n': 5}]},
    {'sampling': {'top_p': {'value': 'omitted',
                            'reason': 'operator-declared', 'detail': 5}}},
], ids=['outside-sampling', 'detail-in-sampling'])
def test_load_config_bare_numeric_inside_omission_object_is_refused(
        load, overrides):
    # SPEC R0.1 / config docstring: every numeric value is a quoted
    # string; a bare numeric literal is refused at load. Only validated
    # sampling omissions get the omission treatment, and they too may not
    # carry bare numerics.
    outcome = load_outcome(load, **overrides)
    assert outcome.startswith('refused: bare numeric literal'), outcome


@pytest.mark.finding('S3-G1-14')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('sampling', ['x', ['0'], None])
def test_load_config_sampling_not_an_object_is_refused(load, sampling):
    # SPEC R0.1: sampling lists each parameter with a value or an explicit
    # omission, so it is an object; refused otherwise, as quantisation is.
    outcome = load_outcome(load, sampling=sampling)
    assert outcome.startswith('refused: sampling'), outcome


@pytest.mark.finding('S3-G1-15')
@pytest.mark.req('R0.1')
def test_load_config_unknown_field_message_lists_optional_fields(load):
    # The message names the permitted fields; the optional ones (tools,
    # system_prompt_base, ...) are permitted too, so it lists them.
    outcome = load_outcome(load, foo='x')
    assert all(f"'{name}'" in outcome for name in OPTIONAL_FIELDS), outcome

import re  # noqa: E402

V13 = 'v1.3-draft-for-comment-20260730'  # example/config.json


def config_error(fn, *args, **kwargs):
    """The ConfigError message fn raises, or None if it returns."""
    try:
        fn(*args, **kwargs)
    except ConfigError as e:
        return str(e)
    return None


def numbers_in(message):
    """The integers a message names, not counting the digit of a
    dimension name such as D6."""
    return set(re.findall(r'(?<![A-Za-z\d.])\d+(?![\d.])', message or ''))


@pytest.mark.finding('T3-12')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-12: a dimension AP-1 does not define loads')
@pytest.mark.req('R0.1')
def test_load_config_undefined_dimension_refused(load):
    # SPEC R0.1 verification contract: "A dimensions_claimed entry the
    # fixture cannot support is refused at load." AP-1 defines D1-D7;
    # 'D99' cannot be supported by any fixture.
    msg = config_error(load, dimensions_claimed=['D1', 'D99'])
    assert msg is not None and 'D99' in msg, msg


@pytest.mark.finding('T3-12')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-12: no D1 total of 40 is checked')
@pytest.mark.req('R0.1')
def test_minimum_n_d1_under_forty_items_refused():
    # AP-1 v1.3 D1 Method (l.204): "a held-out question set (minimum 40
    # items)", and §11.1 "Minimum 40 items for D1" (same in v1.2). Two
    # categories of 10 meet the per-category minimum but not the total.
    # SPEC R0.1: the refusal names the dimension, the count and the minimum.
    msg = config_error(validate_minimum_n, {'dimensions_claimed': ['D1'],
                                            'ap1_version': V13},
                       questions(10, 'A') + questions(10, 'B'))
    assert msg is not None and 'D1' in msg, msg
    assert {'20', '40'} <= numbers_in(msg), msg


@pytest.mark.finding('T3-12')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-12: D5/D6 count every question, not the '
                          'adversarial or conflict items')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('dim, minimum', [('D5', '20'), ('D6', '10')])
def test_minimum_n_d5_d6_ordinary_items_not_counted_refused(dim, minimum):
    # SPEC R0.1: "the loader counts eligible items". D5 counts adversarial
    # inputs (AP-1 v1.3 §11.5), D6 items with degraded or contradictory
    # source data (§11.6). Twenty ordinary computation items, with only a
    # category, are none of these, so the eligible count is 0 whatever
    # schema the fix uses to mark D5/D6 items.
    msg = config_error(validate_minimum_n, {'dimensions_claimed': [dim],
                                            'ap1_version': V13},
                       questions(20, 'interest'))
    assert msg is not None and dim in msg, msg
    assert {'0', minimum} <= numbers_in(msg), msg


@pytest.mark.finding('V12-7', 'T3-12')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='V12-7: minimum-n ignores ap1_version; v1.2 '
                          'minimums are D5 5 and D6 1')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('dim, v12_min, v13_min', [('D5', '5', '20'),
                                                    ('D6', '1', '10')])
def test_minimum_n_minimum_named_is_the_declared_versions(dim, v12_min,
                                                          v13_min):
    # The minimums are per AP-1 version (choices-for-marcus entry 2; fix
    # plan §2a V12-7): v1.3 D5 20 (l.279), D6 10 (l.301); v1.2 D5 5
    # (v1.2 l.149), D6 1 (v1.2 §11.6, l.292). With no eligible items both
    # versions refuse, and the refusal names the declared version's
    # minimum. 'v1.2' is the ap1_version a v1.2 config would declare.
    v13 = config_error(validate_minimum_n,
                       {'dimensions_claimed': [dim], 'ap1_version': V13}, [])
    v12 = config_error(validate_minimum_n,
                       {'dimensions_claimed': [dim], 'ap1_version': 'v1.2'},
                       [])
    assert v13 is not None and v13_min in numbers_in(v13), v13
    assert v12 is not None and v12_min in numbers_in(v12), v12
    assert v13_min not in numbers_in(v12), v12


@pytest.mark.finding('T3-51')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-51: missing quantisation places/rounding '
                          'default to 2 and ROUND_HALF_UP')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('quantisation, missing', [
    ({}, 'places'),
    ({'rounding': 'ROUND_HALF_UP'}, 'places'),
    ({'places': '2'}, 'rounding'),
])
def test_load_config_quantisation_field_missing_refused(load, quantisation,
                                                        missing):
    # SPEC R0.1: "Every field required; no defaults for anything affecting
    # a result. A missing field is an error, not a fallback." AP-1 v1.3
    # §6.9: "Every evaluation shall declare its rounding policy".
    msg = config_error(load, quantisation=quantisation)
    assert msg is not None and missing in msg, msg


@pytest.mark.finding('T3-51')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-51: the rounding string is not validated')
@pytest.mark.req('R0.1')
def test_load_config_quantisation_unknown_rounding_mode_refused(load):
    # SPEC R0.1 (incomplete configuration halts before any request).
    # Today 'BOGUS' loads and fails only when quantise() first runs.
    msg = config_error(load, quantisation={'places': '2',
                                           'rounding': 'BOGUS'})
    assert msg is not None and 'rounding' in msg, msg


@pytest.mark.finding('F1', 'T3-79')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='F1/T3-79: example/config_mini.json is refused '
                          "(reason 'model-unsupported')")
def test_load_config_example_config_mini_is_the_mini_runs_config():
    # Steven's ruling (choices-for-marcus entry 5): config_mini.json is a
    # valid, complete config for the mini run, with the omission label
    # platform-unsupported and an accurate detail. The published mini runs
    # sent temperature "1" and omitted reasoning_effort
    # (output/run_e_mini smoke_run.jsonl sampling_as_sent).
    path = REPO / 'example' / 'config_mini.json'
    cfg, msg = None, None
    try:
        cfg = load_config(path)
    except ConfigError as e:
        msg = str(e)
    assert msg is None, msg
    effort = cfg['sampling']['reasoning_effort']
    assert effort['value'] == 'omitted'
    assert effort['reason'] == 'platform-unsupported'
    assert effort.get('detail')
    assert cfg['sampling']['temperature'] == '1'
