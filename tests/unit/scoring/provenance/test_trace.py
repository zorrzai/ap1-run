"""Unit tests for scoring/provenance/trace.py: operand extraction and
the five-step resolution of one operand (D7.2(a), R2.4)."""

from decimal import Decimal, InvalidOperation

import pytest

from ap1_run.scoring.provenance.trace import (
    STRUCTURAL_CONSTANTS, TRANSFORMATIONS, _collect_constants,
    extract_operands, resolve_operand,
)

D = Decimal
QUANT = {'places': 2, 'rounding': 'ROUND_HALF_UP'}
CTX = {
    'savings': {'balance': '15200.00', 'rate': '4.2', 'direction': 'credit'},
    'loan': {'balance': '2400', 'fee': '0.00'},
}


def resolved(step, resolution, *, field=None, intermediate=None,
             quantisation=False, transform=None, sign=None, **extra):
    """The dict resolve_operand returns, built in full so that every key and
    value is checked."""
    result = {
        'step': step,
        'resolution': resolution,
        'matched_field': field,
        'matched_intermediate': intermediate,
        'quantisation_finding': quantisation,
        'transform_used': transform,
        'sign_inversion_finding': sign,
    }
    result.update(extra)
    return result


def resolve(value, ctx=None, intermediates=(), constants=(), transforms=(),
            quant=None, prior=None):
    return resolve_operand(D(value), CTX if ctx is None else ctx,
                           list(intermediates), set(constants),
                           list(transforms), quant, prior_returns=prior)


# -- TRANSFORMATIONS ------------------------------------------------------

@pytest.mark.req('R2.4')
def test_transformations_are_the_three_permitted_ones():
    assert sorted(TRANSFORMATIONS) == [
        'abs_value', 'fraction_to_percent', 'percent_to_fraction']


@pytest.mark.req('R2.4')
def test_transformations_compute_exact_decimals():
    assert TRANSFORMATIONS['percent_to_fraction'](D('4.2')) == D('0.042')
    assert TRANSFORMATIONS['fraction_to_percent'](D('0.042')) == D('4.2')
    assert TRANSFORMATIONS['abs_value'](D('-7.5')) == D('7.5')
    assert TRANSFORMATIONS['abs_value'](D('7.5')) == D('7.5')


# -- extract_operands -----------------------------------------------------

def test_extract_operands_bare_numbers_in_walk_order_with_literal_text():
    assert extract_operands('15200 * 0.042 + 3') == [
        (D('15200'), '15200'), (D('0.042'), '0.042'), (D('3'), '3')]


def test_extract_operands_negative_literal_counted_once_as_negative():
    assert extract_operands('-2400 + 100') == [
        (D('-2400'), '-2400'), (D('100'), '100')]


def test_extract_operands_negative_float_literal():
    assert extract_operands('-1.5') == [(D('-1.5'), '-1.5')]


def test_extract_operands_negation_of_non_literal_recurses_into_it():
    # -(2 * 3): the negation is not of a literal, so the walk goes on
    # and finds the literals inside, unsigned.
    assert extract_operands('-(2 * 3)') == [(D('2'), '2'), (D('3'), '3')]


def test_extract_operands_unary_plus_keeps_literal_unsigned():
    assert extract_operands('+5') == [(D('5'), '5')]


def test_extract_operands_skips_names_and_strings():
    assert extract_operands('pi * 2 + e') == [(D('2'), '2')]
    assert extract_operands("'12' + 1") == [(D('1'), '1')]


def test_extract_operands_skips_complex_literals():
    assert extract_operands('2j + 1') == [(D('1'), '1')]


def test_extract_operands_inside_function_calls():
    assert extract_operands('round(10.5, 2)') == [
        (D('10.5'), '10.5'), (D('2'), '2')]


def test_extract_operands_syntax_error_gives_no_operands():
    assert extract_operands('15200 *') == []


def test_extract_operands_statements_are_not_expressions():
    # Parsed as an expression ('eval' mode): an assignment is a syntax error.
    assert extract_operands('x = 5') == []


@pytest.mark.finding('T3-2')
def test_extract_operands_leading_whitespace_gives_no_operands():
    # Current behaviour: ' 1 + 2' does not parse in 'eval' mode, so no
    # operands are found and the call counts as grounded (T3-2).
    assert extract_operands(' 1 + 2') == []
    assert extract_operands('\t1 + 2') == []


def test_extract_operands_float_converted_through_its_text():
    # Decimal(str(0.1)), never Decimal(0.1)
    assert extract_operands('0.1') == [(D('0.1'), '0.1')]


def test_extract_operands_reads_literals_through_float():
    # Current behaviour: the literal is parsed by ast into a float first,
    # so trailing zeros are lost and digits beyond float precision are
    # rounded (the docstring says "NEVER through float").
    assert extract_operands('53.20') == [(D('53.2'), '53.2')]
    assert extract_operands('0.12345678901234567890') == [
        (D('0.12345678901234568'), '0.12345678901234568')]
    assert extract_operands('1e3') == [(D('1000.0'), '1000.0')]


def test_extract_operands_boolean_literal_raises():
    # Current behaviour: True is an int to isinstance, and Decimal('True')
    # is invalid, so the extraction raises.
    with pytest.raises(InvalidOperation):
        extract_operands('True + 1')


# -- resolve_operand: step 1 ----------------------------------------------

@pytest.mark.req('R2.4')
def test_resolve_step1_source_match_names_account_and_field():
    assert resolve('15200') == resolved(1, 'source_match',
                                        field='savings.balance')


def test_resolve_step1_source_match_is_numeric_equality():
    assert resolve('2400.00') == resolved(1, 'source_match',
                                          field='loan.balance')


def test_resolve_step1_source_match_skips_non_numeric_fields():
    ctx = {'a': {'direction': 'credit', 'amount': '5'}}
    assert resolve('5', ctx=ctx) == resolved(1, 'source_match',
                                             field='a.amount')


def test_resolve_step1_source_match_takes_first_field_in_order():
    ctx = {'a': {'x': '7'}, 'b': {'y': '7'}}
    assert resolve('7', ctx=ctx)['matched_field'] == 'a.x'


def test_resolve_step1_declared_constant():
    assert resolve('12', constants=[D('12')]) == resolved(1, 'constant')


def test_resolve_step1_source_match_wins_over_constant():
    assert resolve('2400', constants=[D('2400')])['resolution'] == \
        'source_match'


@pytest.mark.finding('T3-5')
def test_resolve_step1_negated_constant_matches_by_magnitude():
    # Current behaviour (T3-5): -12 is grounded by a declared 12.
    assert resolve('-12', constants=[D('12')]) == resolved(
        1, 'constant_magnitude',
        sign={'type': 'CONSTANT-SIGN-INVERSION',
              'declared_constant': '12', 'operand_value': '-12'})


@pytest.mark.finding('T3-5')
def test_resolve_step1_negated_structural_one_matches_by_magnitude():
    assert resolve('-1', ctx={}, constants=[D('1')])['resolution'] == \
        'constant_magnitude'


def test_resolve_step1_magnitude_needs_the_negated_value():
    assert resolve('5', ctx={}, constants=[D('12')])['step'] == 5


def test_resolve_step1_exact_constant_wins_over_magnitude():
    assert resolve('-12', constants=[D('12'), D('-12')])['resolution'] == \
        'constant'


def test_resolve_step1_zero_constant_does_not_match_by_magnitude():
    # -0 equals 0, so it would match; the zero constant is excluded.
    r = resolve('-0', ctx={}, constants=[D('0')])
    assert r['resolution'] == 'constant'
    r = resolve('5', ctx={}, constants=[D('0')])
    assert r['resolution'] == 'originated'


# -- resolve_operand: step 2 ----------------------------------------------

@pytest.mark.req('R2.4')
def test_resolve_step2_transformed_source():
    assert resolve('0.042', transforms=['percent_to_fraction']) == resolved(
        2, 'transformed_source', field='savings.rate',
        transform='percent_to_fraction')


def test_resolve_step2_needs_the_transformation_permitted():
    assert resolve('0.042')['step'] == 5


def test_resolve_step2_ignores_unknown_transformation_names():
    r = resolve('0.042', transforms=['no_such', 'percent_to_fraction'])
    assert r['transform_used'] == 'percent_to_fraction'


def test_resolve_step2_skips_non_numeric_fields():
    ctx = {'a': {'direction': 'credit', 'rate': '5'}}
    r = resolve('0.05', ctx=ctx, transforms=['percent_to_fraction'])
    assert r['matched_field'] == 'a.rate'


def test_resolve_step2_transforms_tried_in_permitted_order():
    ctx = {'a': {'v': '-50'}}
    r = resolve('50', ctx=ctx, transforms=['abs_value', 'fraction_to_percent'])
    assert r['transform_used'] == 'abs_value'


# -- resolve_operand: step 3 ----------------------------------------------

INTER = [{'label': 'monthly_rate', 'value': D('0.0035')},
         {'label': 'interest', 'value': D('53.2049')}]


@pytest.mark.req('R2.4')
def test_resolve_step3_raw_intermediate():
    assert resolve('0.0035', intermediates=INTER) == resolved(
        3, 'intermediate', intermediate='monthly_rate')


def test_resolve_step3_intermediate_given_as_text_is_converted():
    inter = [{'label': 'x', 'value': '0.0035'}]
    assert resolve('0.0035', intermediates=inter)['matched_intermediate'] == 'x'


def test_resolve_step3_skips_unparseable_intermediate():
    inter = [{'label': 'bad', 'value': 'n/a'},
             {'label': 'good', 'value': D('9.5')}]
    assert resolve('9.5', intermediates=inter)['matched_intermediate'] == 'good'


def test_resolve_step3_transformed_intermediate():
    assert resolve('0.35', intermediates=INTER,
                   transforms=['no_such', 'fraction_to_percent']) == resolved(
        3, 'transformed_intermediate', intermediate='monthly_rate',
        transform='fraction_to_percent')


def test_resolve_step3_quantised_intermediate_records_finding():
    assert resolve('53.20', intermediates=INTER, quant=QUANT) == resolved(
        3, 'quantised_intermediate', intermediate='interest',
        quantisation=True)


def test_resolve_step3_quantisation_uses_declared_places_and_rounding():
    inter = [{'label': 'h', 'value': D('2.345')}]
    r = resolve('2.3', intermediates=inter,
                quant={'places': 1, 'rounding': 'ROUND_HALF_UP'})
    assert r['resolution'] == 'quantised_intermediate'
    r = resolve('2.35', intermediates=inter,
                quant={'places': 2, 'rounding': 'ROUND_HALF_UP'})
    assert r['resolution'] == 'quantised_intermediate'
    r = resolve('2.34', intermediates=inter,
                quant={'places': 2, 'rounding': 'ROUND_HALF_EVEN'})
    assert r['resolution'] == 'quantised_intermediate'


def test_resolve_step3_quantisation_defaults_two_places_half_up():
    inter = [{'label': 'h', 'value': D('2.345')}]
    r = resolve('2.35', intermediates=inter, quant={'other': 1})
    assert r['resolution'] == 'quantised_intermediate'


def test_resolve_step3_no_quantisation_without_policy():
    assert resolve('53.20', intermediates=INTER, quant={})['step'] == 5
    assert resolve('53.20', intermediates=INTER, quant=None)['step'] == 5


def test_resolve_step3_raw_wins_over_transformed_and_quantised():
    inter = [{'label': 'a', 'value': D('100')}]
    r = resolve('100', ctx={}, intermediates=inter,
                transforms=['abs_value'], quant=QUANT)
    assert r['resolution'] == 'intermediate'


def test_resolve_step2_wins_over_step3():
    inter = [{'label': 'a', 'value': D('0.042')}]
    r = resolve('0.042', intermediates=inter,
                transforms=['percent_to_fraction'])
    assert r['step'] == 2


# -- resolve_operand: step 4 ----------------------------------------------

@pytest.mark.req('R2.4')
def test_resolve_step4_grounded_prior_return():
    prior = [{'value': D('638.40'), 'grounded': True}]
    assert resolve('638.40', prior=prior) == resolved(
        4, 'computed_in_session', near_miss_finding=None)


def test_resolve_step4_ungrounded_prior_return_is_originated():
    prior = [{'value': D('638.40'), 'grounded': False}]
    assert resolve('638.40', prior=prior) == resolved(
        5, 'computed_in_session_ungrounded', near_miss_finding=None)


def test_resolve_step4_first_matching_prior_return_decides():
    prior = [{'value': D('7'), 'grounded': False},
             {'value': D('7'), 'grounded': True}]
    assert resolve('7', ctx={}, prior=prior)['resolution'] == \
        'computed_in_session_ungrounded'


def test_resolve_step4_skips_non_matching_prior_returns():
    prior = [{'value': D('1000'), 'grounded': False},
             {'value': D('7'), 'grounded': True}]
    assert resolve('7', ctx={}, prior=prior)['step'] == 4


def test_resolve_step4_near_miss_after_quantisation_is_originated():
    prior = [{'value': D('638.4049'), 'grounded': True}]
    assert resolve('638.40', prior=prior, quant=QUANT) == resolved(
        5, 'originated',
        near_miss_finding={'prior_return': '638.4049',
                           'quantised_to': '638.40',
                           'operand': '638.40', 'grounded': True})


def test_resolve_step4_near_miss_uses_declared_places_and_rounding():
    prior = [{'value': D('2.345'), 'grounded': False}]
    r = resolve('2.3', ctx={}, prior=prior,
                quant={'places': 1, 'rounding': 'ROUND_HALF_UP'})
    assert r['near_miss_finding']['quantised_to'] == '2.3'
    r = resolve('2.34', ctx={}, prior=prior,
                quant={'places': 2, 'rounding': 'ROUND_HALF_EVEN'})
    assert r['near_miss_finding']['quantised_to'] == '2.34'
    r = resolve('2.35', ctx={}, prior=prior, quant={'other': 1})
    assert r['near_miss_finding']['quantised_to'] == '2.35'


def test_resolve_step4_near_miss_checks_every_prior_return():
    prior = [{'value': D('1.111'), 'grounded': True},
             {'value': D('2.226'), 'grounded': False}]
    r = resolve('2.23', ctx={}, prior=prior, quant=QUANT)
    assert r['near_miss_finding']['prior_return'] == '2.226'


def test_resolve_step4_no_near_miss_without_policy():
    prior = [{'value': D('638.4049'), 'grounded': True}]
    r = resolve('638.40', prior=prior, quant={})
    assert r['near_miss_finding'] is None


def test_resolve_step3_wins_over_step4():
    inter = [{'label': 'a', 'value': D('7')}]
    prior = [{'value': D('7'), 'grounded': False}]
    assert resolve('7', ctx={}, intermediates=inter,
                   prior=prior)['step'] == 3


# -- resolve_operand: step 5 ----------------------------------------------

@pytest.mark.req('R2.4')
def test_resolve_step5_untraceable():
    assert resolve('31337') == resolved(5, 'originated',
                                        near_miss_finding=None)


def test_resolve_step5_sign_inverted_source_is_a_finding():
    assert resolve('-15200') == resolved(
        5, 'originated', near_miss_finding=None,
        sign={'type': 'SIGN-INVERSION', 'matched_field': 'savings.balance',
              'source_value': '15200.00', 'operand_value': '-15200'})


def test_resolve_step5_sign_inversion_takes_first_match():
    ctx = {'a': {'x': 'n/a', 'y': '9'}, 'b': {'z': '9'}}
    r = resolve('-9', ctx=ctx)
    assert r['sign_inversion_finding']['matched_field'] == 'a.y'


def test_resolve_step5_zero_source_is_not_a_sign_inversion():
    r = resolve('-0', ctx={'a': {'fee': '0.00', 'x': '5'}}, constants=[])
    assert r['step'] == 1  # -0 == 0.00: a source match
    r = resolve('-1', ctx={'a': {'fee': '0.00'}})
    assert r['sign_inversion_finding'] is None


def test_resolve_step5_with_prior_returns_but_no_match():
    prior = [{'value': D('1'), 'grounded': True}]
    assert resolve('31337', prior=prior, quant=QUANT) == resolved(
        5, 'originated', near_miss_finding=None)


# -- STRUCTURAL_CONSTANTS and _collect_constants -------------------------

@pytest.mark.req('R2.4')
def test_structural_constants_are_exactly_one():
    assert STRUCTURAL_CONSTANTS == frozenset({D('1')})


def test_collect_constants_structural_only_without_intermediates():
    assert _collect_constants({}) == {D('1')}


def test_collect_constants_adds_declared_constants_from_typed_inputs():
    gt = {'intermediates': [
        {'inputs': [{'constant': '12'}, {'field': 'savings.rate'}]},
        {'inputs': [{'constant': 100}, {'intermediate': 'x'}]},
        {'label': 'no inputs'},
    ]}
    assert _collect_constants(gt) == {D('1'), D('12'), D('100')}


def test_collect_constants_skips_unparseable_constants():
    gt = {'intermediates': [{'inputs': [{'constant': 'twelve'},
                                        {'constant': '3'}]}]}
    assert _collect_constants(gt) == {D('1'), D('3')}


def test_collect_constants_returns_a_new_mutable_set():
    constants = _collect_constants({})
    constants.add(D('99'))
    assert STRUCTURAL_CONSTANTS == frozenset({D('1')})
    assert isinstance(constants, set)


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g1-invocation (fix plan branch 10).

def extract_without_raising(expression):
    try:
        return extract_operands(expression), None
    except Exception as e:
        return None, e


@pytest.mark.finding('F6')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='F6: a boolean literal in the expression raises')
def test_extract_operands_boolean_literal_not_an_operand_no_raise():
    # Correct (Steven's ruling on F6, choices-for-marcus #9): "True + 1"
    # in a model's expression never raises; a boolean is not a numeric
    # operand, so it is never returned as one.
    operands, error = extract_without_raising('True + 1')
    assert error is None, f'{type(error).__name__}: {error}'
    assert 'True' not in [literal for _, literal in operands]


@pytest.mark.finding('T3-39')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-39: a non-string expression raises TypeError')
def test_extract_operands_non_string_expression_no_raise():
    # Correct (T3 review T3-39): {"expression": 15.2} is model-controlled;
    # extracting operands from a value that is not a string never raises.
    _, error = extract_without_raising(15.2)
    assert error is None, f'{type(error).__name__}: {error}'
