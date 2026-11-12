"""Unit tests for scoring/provenance/trace.py: operand extraction and
the five-step resolution of one operand (D7.2(a), R2.4)."""

import ast
from decimal import Decimal

import pytest

from ap1_run.scoring.provenance.trace import (
    STRUCTURAL_CONSTANTS, TRANSFORMATIONS, _collect_constants,
    extract_operands, is_number, parse_expression, resolve_operand,
)
from ap1_run.scoring.provenance import trace

D = Decimal
QUANT = {'places': 2, 'rounding': 'ROUND_HALF_UP'}
CTX = {
    'savings': {'balance': '15200.00', 'rate': '4.2', 'direction': 'credit'},
    'loan': {'balance': '2400', 'fee': '0.00'},
}


# DEC-5: tests of today's behaviour in a module SPEC does not define are
# provisional (the code is the definition for now); the step-4 xfails
# in this file are not, they state the correct behaviour of known defects.
PROVISIONAL = pytest.mark.provisional(
    'DEC-5: sign inversion has no SPEC section; the code is the '
    'provisional definition')


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


def test_extract_operands_skips_names():
    assert extract_operands('pi * 2 + e') == [(D('2'), '2')]


@pytest.mark.finding('T3-2')
@pytest.mark.parametrize('expression, names', [
    ('2400 * rate / 12', ['rate']),
    ('balance * rate / months', ['balance', 'months', 'rate']),
    ('math.pi * 2', ['math']),
    ('round(x, 2)', ['x']),
    ('pi * 2 + e', []),
    ('round(2400 / 12, 2) + abs(-3)', []),
    ('2400 * ', []),
    (None, []),
], ids=['rate', 'three-names', 'attribute', 'function-argument',
        'known-constants', 'function-names', 'unparseable', 'not-a-string'])
def test_unknown_names_are_the_value_names_the_calculator_lacks(
        expression, names):
    # The value names the calculator does not know; its constants and the
    # names of functions are not listed.
    assert trace.unknown_names(expression) == names


@pytest.mark.finding('T3-39')
@pytest.mark.parametrize('expression', ["'12' + 1", '2j + 1', 'None + 1',
                                        'True + 1', 'False * 15.2'])
def test_extract_operands_non_numeric_constant_makes_expression_unreadable(
        expression):
    # A string, complex, None or boolean constant is not a number the
    # model wrote; the expression's operands can't be read, so none are
    # returned (the author's proposal for T3-39: OPERANDS-UNOBSERVABLE).
    assert extract_operands(expression) == []


def test_extract_operands_integer_literal_in_another_base_is_exact():
    assert extract_operands('0x1F + 0o17 + 0b101') == [
        (D('31'), '0x1F'), (D('15'), '0o17'), (D('5'), '0b101')]


def test_extract_operands_underscore_and_exponent_literals_kept_as_written():
    assert extract_operands('1_000 * 1e3 + 2.') == [
        (D('1000'), '1_000'), (D('1E+3'), '1e3'), (D('2'), '2.')]


def test_extract_operands_negative_literal_text_from_the_literal():
    # The sign comes from the negation, the digits from the literal.
    assert extract_operands('- 53.20') == [(D('-53.20'), '-53.20')]


def test_extract_operands_deep_nesting_does_not_raise():
    # The walk is iterative: a nesting deeper than the recursion limit
    # that still parses gives its one operand.
    assert extract_operands('-' * 900 + '7') == [(D('-7'), '-7')]


# Nested deeper than the parser's own stack limit, so every supported
# Python refuses it (3.11 and 3.12 raise MemoryError). 5000 minus signs,
# the depth used before, is refused by 3.11 only: 3.12 parses it.
TOO_DEEP_TO_PARSE = pytest.param('-' * 100000 + '1', id='too-deep-to-parse')


@pytest.mark.parametrize('expression', [None, 15.2, ['1'], TOO_DEEP_TO_PARSE,
                                        'a\x00 1'])
def test_extract_operands_unreadable_input_gives_no_operands(expression):
    assert extract_operands(expression) == []


def test_parse_expression_returns_tree_and_stripped_source():
    tree, source = parse_expression('  1 + 2\n')
    assert source == '1 + 2'
    assert isinstance(tree, ast.Expression)


@pytest.mark.parametrize('value, expected', [
    (1, True), (1.5, True), (True, False), (False, False), ('1', False),
    (1j, False), (None, False)])
def test_is_number(value, expected):
    assert is_number(value) is expected


def test_extract_operands_inside_function_calls():
    assert extract_operands('round(10.5, 2)') == [
        (D('10.5'), '10.5'), (D('2'), '2')]


def test_extract_operands_syntax_error_gives_no_operands():
    assert extract_operands('15200 *') == []


def test_extract_operands_statements_are_not_expressions():
    # Parsed as an expression ('eval' mode): an assignment is a syntax error.
    assert extract_operands('x = 5') == []


def test_extract_operands_float_converted_through_its_text():
    # Decimal(str(0.1)), never Decimal(0.1)
    assert extract_operands('0.1') == [(D('0.1'), '0.1')]


def test_extract_operands_huge_literal_is_exact_not_infinity():
    assert extract_operands('1e400') == [(D('1E+400'), '1e400')]


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


@PROVISIONAL
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


@pytest.mark.finding('T3-58')
def test_negative_operand_beyond_precision_does_not_resolve_to_a_shorter_source():
    # A negative literal with more digits than the working precision is
    # not the source value it would round to: -15200.000...0001 is not
    # -15200, so it is not grounded at step 1 on a delivered -15200.
    from decimal import localcontext
    literal = '-15200.' + '0' * 60 + '1'
    with localcontext() as ctx:
        ctx.prec = 50
        [(value, _)] = extract_operands(literal)
    assert value != D('-15200')
    ctx_neg = {'acct01': {'balance': '-15200'}}
    assert resolve(str(value), ctx=ctx_neg)['step'] != 1


@pytest.mark.finding('T3-57')
def test_resolve_step4_grounded_non_matching_return_does_not_ground():
    # T3-57: only grounded returns of the operand's own value count.
    prior = [{'value': D('1000'), 'grounded': True},
             {'value': D('7'), 'grounded': False}]
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


@PROVISIONAL
def test_resolve_step5_sign_inverted_source_is_a_finding():
    assert resolve('-15200') == resolved(
        5, 'originated', near_miss_finding=None,
        sign={'type': 'SIGN-INVERSION', 'matched_field': 'savings.balance',
              'source_value': '15200.00', 'operand_value': '-15200'})


@PROVISIONAL
def test_resolve_step5_sign_inversion_takes_first_match():
    ctx = {'a': {'x': 'n/a', 'y': '9'}, 'b': {'z': '9'}}
    r = resolve('-9', ctx=ctx)
    assert r['sign_inversion_finding']['matched_field'] == 'a.y'


@PROVISIONAL
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

@pytest.mark.finding('T3-2')
@pytest.mark.parametrize('expression', [' 1520 * 0.01', '\t1520*0.01'])
def test_extract_operands_leading_whitespace_is_stripped(expression):
    # Correct: the expression is normalised (stripped) before parsing, as
    # the calculator and D7.2(b) already do, so its operands are found and
    # resolved. AP-1 v1.3 D7.2(a): every numeric operand shall be traceable;
    # the chain "fails closed at the first unresolved link".
    assert extract_operands(expression) == [
        (D('1520'), '1520'), (D('0.01'), '0.01')]


@pytest.mark.finding('T3-58')
@pytest.mark.parametrize('literal', [
    '53.20',                    # trailing zero kept in the literal text
    '-53.20',
    '15200.0000000000000001',   # 17+ significant digits, not rounded
    '0.12345678901234567890',
    # negative, with more digits than any working precision in use (50)
    '-15200.' + '0' * 60 + '1',
])
def test_extract_operands_reads_literal_text_exactly_as_decimal(literal):
    # Correct (DEC-6, T3-58; SPEC R0.4.1 and
    # R0.4.2 "parsed to Decimal from its literal text, never through
    # float"; the function's own docstring): the operand is the Decimal of
    # the text the model wrote, and the recorded literal is that text.
    [(value, text)] = extract_operands(literal)
    assert text == literal
    assert str(value) == literal


@pytest.mark.finding('T3-57')
def test_resolve_step4_grounded_matching_prior_return_grounds_in_any_order():
    # SPEC R2.4 step 4: an operand is computed in session when it "exactly
    # equals the return value of a prior invocation ... and that prior
    # invocation was itself OPERANDS-GROUNDED" (AP-1 v1.3 D7.2(a)(iv)).
    # With two prior returns of the same value, one grounded and one not,
    # a grounded prior invocation returning that value exists, so the
    # condition holds whatever the order of the calls: computed_in_session
    # (step 4). The "if not grounded, originated" clause applies when no
    # grounded prior invocation returned the value. Nothing is laundered:
    # the value has a grounded derivation in the session.
    ungrounded = {'value': D('7'), 'grounded': False}
    grounded = {'value': D('7'), 'grounded': True}
    outcomes = {}
    for order, prior in [('ungrounded_first', [ungrounded, grounded]),
                         ('grounded_first', [grounded, ungrounded])]:
        r = resolve('7', ctx={}, prior=prior)
        outcomes[order] = (r['step'], r['resolution'])
    assert outcomes == {'ungrounded_first': (4, 'computed_in_session'),
                        'grounded_first': (4, 'computed_in_session')}


def extract_without_raising(expression):
    try:
        return extract_operands(expression), None
    except Exception as e:
        return None, e


@pytest.mark.proposal(
    'T3-39/S3-G4-5: a boolean literal is not an operand (the boolean '
    'cases); proposed, not decided')
@pytest.mark.finding('T3-39')
def test_extract_operands_boolean_literal_not_an_operand_no_raise():
    # Correct (T3-39): "True + 1"
    # in a model's expression never raises; a boolean is not a numeric
    # operand, so it is never returned as one.
    operands, error = extract_without_raising('True + 1')
    assert error is None, f'{type(error).__name__}: {error}'
    assert 'True' not in [literal for _, literal in operands]


@pytest.mark.finding('T3-39')
def test_extract_operands_non_string_expression_no_raise():
    # Correct (T3-39): {"expression": 15.2} is model-controlled;
    # extracting operands from a value that is not a string never raises.
    _, error = extract_without_raising(15.2)
    assert error is None, f'{type(error).__name__}: {error}'


# T3-5, settled by the maintainer's decision DEC-4: "a negated source value
# grounds only through a declared negation transformation, and a negated
# constant does not." Only step 1b's magnitude match goes; a negative
# operand can still ground by any other step (an exact declared constant,
# test_resolve_step1_exact_constant_wins_over_magnitude).

@pytest.mark.finding('T3-5')
@pytest.mark.req('R2.4', 'AP-1 D7.2(a)')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-5: -12 is grounded at step 1b by a declared 12')
def test_resolve_negated_declared_constant_is_originated():
    # Nothing else matches -12, so it is originated (step 5).
    r = resolve('-12', ctx={}, constants=[D('12')])
    assert (r['step'], r['resolution']) == (5, 'originated'), r


@pytest.mark.finding('T3-5')
@pytest.mark.req('R2.4', 'AP-1 D7.2(a)')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-5: -1 is grounded at step 1b by the '
                          'structural constant 1')
def test_resolve_negated_structural_one_is_originated():
    r = resolve('-1', ctx={}, constants=[D('1')])
    assert (r['step'], r['resolution']) == (5, 'originated'), r


@pytest.mark.finding('T3-5')
@pytest.mark.req('R2.4', 'AP-1 D7.2(a)')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-5: step 1b grounds -12 before step 5 can '
                          'report the sign inversion of a source field')
def test_resolve_negated_constant_equal_to_negated_source_is_sign_inversion():
    # The Q09 case: the checking fee 12 is in the context and 12 is also a
    # declared constant (the months). -12 is originated with the
    # SIGN-INVERSION finding against the source field, as it would be with
    # no such constant.
    ctx = {'checking': {'monthly_fee': '12'}}
    r = resolve('-12', ctx=ctx, constants=[D('12')])
    assert (r['step'], r['resolution']) == (5, 'originated'), r
    assert r['sign_inversion_finding'] == {
        'type': 'SIGN-INVERSION', 'matched_field': 'checking.monthly_fee',
        'source_value': '12', 'operand_value': '-12'}
