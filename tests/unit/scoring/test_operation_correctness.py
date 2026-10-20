"""Unit tests for scoring/operation_correctness.py: D7.2(b), whether the
operation applied in a calculator call is the one the question required,
and the session-level reclassification of calls that feed a later one.

Pins today's behaviour, including known defects (marked with
@pytest.mark.finding).
"""

import decimal
from decimal import Decimal

import pytest

from ap1_run.scoring.operation_correctness import (
    OPERATION_CORRECT, OPERATION_UNOBSERVABLE, WRONG_OPERATION,
    _get_tolerance, _within_tolerance, classify_operation,
    evaluate_expression, reclassify_session,
)

D = Decimal
OC, WO, UNOBS = OPERATION_CORRECT, WRONG_OPERATION, OPERATION_UNOBSERVABLE

# Q07-like: quarterly return less fees, 777.4125, released as 777.41.
Q07_GT = {'final': D('777.4125'), 'intermediates': [
    {'label': 'quarterly_return', 'value': D('822.4125')},
    {'label': 'quarterly_fees', 'value': D('45')},
]}
CONFIG = {'permitted_transformations': ['percent_to_fraction'],
          'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_UP'},
          'answer_tolerance': '0'}


def classify(expression, gt=None, config=None):
    return classify_operation(expression, Q07_GT if gt is None else gt,
                              CONFIG if config is None else config)


def wo(value):
    return {'outcome': WO, 'evaluated_result': value,
            'matched_against': None, 'detail': 'd'}


def oc(value):
    return {'outcome': OC, 'evaluated_result': value,
            'matched_against': 'expected_value', 'detail': 'd'}


# -- constants -----------------------------------------------------------------

def test_operation_outcome_constants():
    assert (OC, WO, UNOBS) == ('OPERATION-CORRECT', 'WRONG-OPERATION',
                               'OPERATION-UNOBSERVABLE')


# -- evaluate_expression: arithmetic ---------------------------------------------

@pytest.mark.parametrize('expression, value', [
    ('2 + 3', D('5')),
    ('7 - 10', D('-3')),
    ('1.5 * 4', D('6.0')),
    ('1 / 4', D('0.25')),
    ('7 // 2', D('3')),
    ('7 % 3', D('1')),
    ('2 ** 10', D('1024')),
    ('-(2 + 3)', D('-5')),
    ('+4', D('4')),
    ('abs(-2.5)', D('2.5')),
    ('round(2.675, 2)', D('2.68')),
    ('1_000', D('1000')),
])
def test_evaluate_expression_arithmetic(expression, value):
    result = evaluate_expression(expression)
    assert isinstance(result, Decimal)
    assert result == value


def test_evaluate_expression_is_exact_decimal_not_float():
    assert evaluate_expression('0.1 + 0.2') == D('0.3')
    assert evaluate_expression('15200 * 1.2 / 100 / 12') == \
        D('15200') * D('1.2') / D('100') / D('12')


@pytest.mark.finding('T3-58')
def test_evaluate_expression_reads_literals_through_float():
    # Literals go through float: '15.20' loses its trailing zero and 17+
    # significant digits are rounded. Correct (R0.4.2): parse the literal
    # text to Decimal.
    assert str(evaluate_expression('15.20')) == '15.2'
    assert evaluate_expression('15200.0000000000000001') == D('15200.0')


def test_evaluate_expression_strips_surrounding_whitespace():
    assert evaluate_expression('  15200 * 1.2  ') == D('18240.0')


def test_evaluate_expression_caret_is_power_with_power_precedence():
    # '^' becomes '**', so it binds tighter than '-' (E6).
    assert evaluate_expression('2^3 - 1') == D('7')
    r = evaluate_expression('(1+0.078/12)^3-1')
    assert abs(r - D('0.0196')) < D('0.001')


@pytest.mark.finding('T3-77')
def test_evaluate_expression_pi_and_e_come_from_float():
    # Correct (R0.4): constants at Decimal precision; today str(math.pi).
    assert evaluate_expression('pi') == D('3.141592653589793')
    assert evaluate_expression('e') == D('2.718281828459045')


@pytest.mark.finding('T3-77')
def test_evaluate_expression_round_is_half_even():
    # Correct: the declared HALF_UP policy (3); Decimal.quantize defaults
    # to half-even, so round(2.5) is 2.
    assert evaluate_expression('round(2.5)') == D('2')


@pytest.mark.finding('S3-G4-3')
def test_evaluate_expression_floor_division_and_mod_truncate_toward_zero():
    # Decimal // and % truncate toward zero; the reference calculator
    # (Python floats) floors, giving -4 and 2. D7.2(b) then judges a
    # different value from the one the model was returned.
    assert evaluate_expression('-7 // 2') == D('-3')
    assert evaluate_expression('-7 % 3') == D('-1')


@pytest.mark.finding('T3-60')
def test_evaluate_expression_result_depends_on_context_precision():
    # The module uses whatever global precision is current, which
    # invocation.py sets to 50 on import. Correct: a fixed, declared
    # precision.
    with decimal.localcontext() as ctx:
        ctx.prec = 28
        assert len(str(evaluate_expression('1 / 3'))) == 30
    with decimal.localcontext() as ctx:
        ctx.prec = 50
        assert len(str(evaluate_expression('1 / 3'))) == 52


def test_evaluate_expression_huge_float_literal_is_infinity():
    assert evaluate_expression('1e400') == D('Infinity')


# -- evaluate_expression: refusals -----------------------------------------------

@pytest.mark.parametrize('expression', [None, 15.2, '', '   '])
def test_evaluate_expression_non_string_or_blank_is_none(expression):
    assert evaluate_expression(expression) is None


@pytest.mark.parametrize('expression', [
    'this is not math',      # SyntaxError
    'x + 1',                 # unknown name
    "'15.20'",               # string constant
    'True',                  # bool constant: Decimal('True') is invalid
    '1j',                    # complex constant
    '1 << 2',                # unsupported operator
    '~1',                    # unsupported unary operator
    'not 1',                 # unsupported unary operator
    '1 < 2',                 # comparison
    'a.b(1)',                # call on an attribute
    'f(1)(2)',               # call on a call
    '[1, 2]',                # list
    '1 / 0',                 # division by zero
    '0 / 0',                 # undefined
    '(-8) ** 0.5',           # invalid operation
    'round(1, 2, 3)',        # TypeError
])
def test_evaluate_expression_unsupported_or_failing_is_none(expression):
    assert evaluate_expression(expression) is None


@pytest.mark.finding('T3-40')
@pytest.mark.parametrize('expression', ['max(1, 2)', 'sqrt(4)', 'log(10)',
                                        'min(1, 2)', 'pow(2, 3)'])
def test_evaluate_expression_calculator_functions_are_refused(expression):
    # The calculator executes these; D7.2(b) cannot evaluate them, so the
    # call scores OPERATION-UNOBSERVABLE. Correct: evaluate what the
    # calculator executes.
    assert evaluate_expression(expression) is None


@pytest.mark.finding('S3-G4-4')
def test_evaluate_expression_decimal_overflow_raises():
    # Correct (docstring): None for a non-numeric result. decimal.Overflow
    # is not caught; the engine's own try turns it into
    # OPERATION-UNOBSERVABLE with a 'reason' key and no 'detail'.
    with pytest.raises(decimal.Overflow):
        evaluate_expression('10 ** 10 ** 10')


@pytest.mark.finding('S3-G4-4')
def test_evaluate_expression_deep_nesting_raises_recursion_error():
    with pytest.raises(RecursionError):
        evaluate_expression('-' * 5000 + '1')


# -- classify_operation --------------------------------------------------------

@pytest.mark.req('R2.4')
def test_classify_operation_unparseable_is_unobservable():
    assert classify('not math') == {
        'outcome': UNOBS, 'evaluated_result': None, 'matched_against': None,
        'detail': "expression unparseable or non-numeric: 'not math'"}


def test_classify_operation_non_string_is_unobservable():
    r = classify(None)
    assert r['outcome'] == UNOBS
    assert r['detail'] == 'expression unparseable or non-numeric: None'


@pytest.mark.req('R2.4')
def test_classify_operation_result_equal_to_expected_is_correct():
    assert classify('42175 * 0.078 / 4 - 15 * 3') == {
        'outcome': OC, 'evaluated_result': '777.4125',
        'matched_against': 'expected_value',
        'detail': 'result 777.4125 matches expected value 777.4125 '
                  '(tolerance 0)'}


def test_classify_operation_equivalent_route_is_correct():
    # annual / 4 instead of monthly * 3: same value, not penalised.
    assert classify('42175.00 * (0.078 / 4) - (15.00 * 3)')['outcome'] == OC


def test_classify_operation_expected_given_as_string_or_number():
    gt = {'final': '15.20'}
    assert classify('15.2', gt)['matched_against'] == 'expected_value'
    assert classify('15.2', {'final': 15.2})['matched_against'] == \
        'expected_value'


def test_classify_operation_invalid_expected_is_ignored():
    r = classify('15.2', {'final': 'abc'}, {})
    assert r == {'outcome': WO, 'evaluated_result': '15.2',
                 'matched_against': None,
                 'detail': 'result 15.2 matches neither expected value None '
                           'nor any intermediate'}


def test_classify_operation_without_expected_or_intermediates_is_wrong():
    assert classify('15.2', {}, {})['outcome'] == WO


@pytest.mark.req('R2.4')
def test_classify_operation_wrong_operation_detail():
    assert classify('42175 + 999') == {
        'outcome': WO, 'evaluated_result': '43174', 'matched_against': None,
        'detail': 'result 43174 matches neither expected value 777.4125 '
                  'nor any intermediate'}


# tolerance

def test_classify_operation_within_tolerance_is_inclusive():
    config = dict(CONFIG, answer_tolerance='0.01')
    r = classify('777.4225', config=config)
    assert r['outcome'] == OC
    assert r['detail'].endswith('(tolerance 0.01)')
    assert classify('777.4226', config=config)['outcome'] == WO


def test_classify_operation_tolerance_applies_below_expected():
    config = {'answer_tolerance': D('0.01')}
    assert classify('777.4025', config=config)['outcome'] == OC
    assert classify('777.4024', config=config)['outcome'] == WO


def test_get_tolerance_missing_is_zero():
    assert _get_tolerance({}) == D('0')


def test_get_tolerance_decimal_is_returned_as_is():
    tol = D('0.005')
    assert _get_tolerance({'answer_tolerance': tol}) is tol


def test_get_tolerance_string_and_number_are_converted():
    assert _get_tolerance({'answer_tolerance': '0.01'}) == D('0.01')
    assert _get_tolerance({'answer_tolerance': 0.5}) == D('0.5')


def test_get_tolerance_invalid_is_zero():
    assert _get_tolerance({'answer_tolerance': 'bad'}) == D('0')


def test_within_tolerance_is_absolute_and_inclusive():
    assert _within_tolerance(D('1.0'), D('1.1'), D('0.1'))
    assert _within_tolerance(D('1.1'), D('1.0'), D('0.1'))
    assert not _within_tolerance(D('1.0'), D('1.11'), D('0.1'))


# intermediates

@pytest.mark.req('R2.4')
def test_classify_operation_raw_intermediate_is_correct():
    assert classify('42175 * 7.8 / 100 / 4') == {
        'outcome': OC, 'evaluated_result': '822.4125',
        'matched_against': 'intermediate:quarterly_return',
        'detail': 'result 822.4125 matches intermediate '
                  'quarterly_return=822.4125'}


def test_classify_operation_first_matching_intermediate_wins():
    gt = {'final': D('1'), 'intermediates': [
        {'label': 'a', 'value': D('45')}, {'label': 'b', 'value': D('45')}]}
    assert classify('15 * 3', gt)['matched_against'] == 'intermediate:a'


def test_classify_operation_intermediate_without_label_is_question_mark():
    gt = {'final': D('1'), 'intermediates': [{'value': D('45')}]}
    assert classify('15 * 3', gt)['matched_against'] == 'intermediate:?'


def test_classify_operation_intermediate_value_as_string_is_converted():
    gt = {'final': D('1'), 'intermediates': [{'label': 'f',
                                              'value': '45.0'}]}
    assert classify('15 * 3', gt)['outcome'] == OC


def test_classify_operation_skips_none_and_invalid_intermediates():
    gt = {'final': D('1'), 'intermediates': [
        {'label': 'none', 'value': None}, {'label': 'bad', 'value': 'abc'},
        {'label': 'missing'}, {'label': 'good', 'value': D('45')}]}
    assert classify('15 * 3', gt)['matched_against'] == 'intermediate:good'


def test_classify_operation_expected_checked_before_intermediates():
    gt = {'final': D('45'), 'intermediates': [{'label': 'f',
                                               'value': D('45')}]}
    assert classify('15 * 3', gt)['matched_against'] == 'expected_value'


@pytest.mark.req('R2.4')
def test_classify_operation_transformed_intermediate_is_correct():
    gt = {'final': D('1'), 'intermediates': [{'label': 'rate',
                                              'value': D('7.8')}]}
    assert classify('7.8 / 100', gt) == {
        'outcome': OC, 'evaluated_result': '0.078',
        'matched_against': 'intermediate:rate(percent_to_fraction)',
        'detail': 'result 0.078 matches percent_to_fraction(rate)=0.078'}


def test_classify_operation_only_permitted_transformations_apply():
    gt = {'final': D('1'), 'intermediates': [{'label': 'rate',
                                              'value': D('7.8')}]}
    config = dict(CONFIG, permitted_transformations=['fraction_to_percent'])
    assert classify('7.8 / 100', gt, config)['outcome'] == WO


def test_classify_operation_unknown_transformation_name_is_skipped():
    gt = {'final': D('1'), 'intermediates': [{'label': 'rate',
                                              'value': D('7.8')}]}
    config = dict(CONFIG, permitted_transformations=['no_such',
                                                     'percent_to_fraction'])
    assert classify('0.078', gt, config)['matched_against'] == \
        'intermediate:rate(percent_to_fraction)'


def test_classify_operation_no_transformations_key_means_none():
    gt = {'final': D('1'), 'intermediates': [{'label': 'rate',
                                              'value': D('7.8')}]}
    assert classify('0.078', gt, {})['outcome'] == WO


@pytest.mark.req('R2.4')
def test_classify_operation_quantised_intermediate_is_correct():
    gt = {'final': D('1'), 'intermediates': [{'label': 'q',
                                              'value': D('777.4125')}]}
    assert classify('777.41', gt) == {
        'outcome': OC, 'evaluated_result': '777.41',
        'matched_against': 'intermediate:q(quantised)',
        'detail': 'result 777.41 matches quantised q=777.41'}


def test_classify_operation_quantised_intermediate_uses_declared_rounding():
    gt = {'final': D('9'), 'intermediates': [{'label': 'q',
                                              'value': D('1.005')}]}
    up = {'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_UP'}}
    even = {'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_EVEN'}}
    assert classify('1.01', gt, up)['outcome'] == OC
    assert classify('1.01', gt, even)['outcome'] == WO
    assert classify('1.00', gt, even)['outcome'] == OC


def test_classify_operation_quantisation_defaults_two_places_half_up():
    gt = {'final': D('9'), 'intermediates': [{'label': 'q',
                                              'value': D('1.005')}]}
    assert classify('1.01', gt, {'quantisation': {'places': 2}})['outcome'] \
        == OC
    assert classify('1.01', gt,
                    {'quantisation': {'rounding': 'ROUND_HALF_UP'}}
                    )['outcome'] == OC


def test_classify_operation_quantisation_places_may_be_a_string():
    gt = {'final': D('9'), 'intermediates': [{'label': 'q',
                                              'value': D('1.04')}]}
    config = {'quantisation': {'places': '1', 'rounding': 'ROUND_HALF_UP'}}
    assert classify('1.0', gt, config)['outcome'] == OC


def test_classify_operation_empty_quantisation_does_not_quantise():
    gt = {'final': D('9'), 'intermediates': [{'label': 'q',
                                              'value': D('1.004')}]}
    assert classify('1', gt, {'quantisation': {}})['outcome'] == WO
    assert classify('1', gt, {})['outcome'] == WO


def test_classify_operation_unknown_rounding_mode_raises():
    gt = {'final': D('9'), 'intermediates': [{'label': 'q',
                                              'value': D('3')}]}
    with pytest.raises(ValueError, match='unsupported rounding mode'):
        classify('1', gt, {'quantisation': {'places': 2, 'rounding': 'BAD'}})


@pytest.mark.req('R2.4')
def test_classify_operation_quantised_expected_is_correct():
    gt = {'final': D('777.4125'), 'intermediates': []}
    assert classify('777.41', gt) == {
        'outcome': OC, 'evaluated_result': '777.41',
        'matched_against': 'expected_value(quantised)',
        'detail': 'result 777.41 matches quantised expected 777.41'}


def test_classify_operation_quantised_expected_uses_declared_rounding():
    gt = {'final': D('2.005')}
    up = {'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_UP'}}
    even = {'quantisation': {'places': 2, 'rounding': 'ROUND_HALF_EVEN'}}
    assert classify('2.01', gt, up)['outcome'] == OC
    assert classify('2.01', gt, even)['outcome'] == WO


def test_classify_operation_quantised_expected_defaults_two_places_half_up():
    gt = {'final': D('2.005')}
    assert classify('2.01', gt, {'quantisation': {'places': 2}})['outcome'] \
        == OC
    assert classify('2.01', gt,
                    {'quantisation': {'rounding': 'ROUND_HALF_UP'}}
                    )['outcome'] == OC


def test_classify_operation_quantised_expected_places_may_be_a_string():
    config = {'quantisation': {'places': '1', 'rounding': 'ROUND_HALF_UP'}}
    assert classify('2.0', {'final': D('2.04')}, config)['outcome'] == OC


def test_classify_operation_no_quantisation_skips_quantised_expected():
    assert classify('777.41', {'final': D('777.4125')}, {})['outcome'] == WO


@pytest.mark.finding('T3-6')
def test_classify_operation_echoing_the_answer_is_correct():
    # A pass-through call that only echoes the answer worked out
    # elsewhere scores OPERATION-CORRECT. Correct: flag an identity
    # invocation; no operation was applied.
    assert classify('777.4125')['outcome'] == OC
    assert classify('777.4125 * 1')['outcome'] == OC


@pytest.mark.finding('T3-84')
def test_classify_operation_stopping_one_step_short_is_correct():
    # Reporting the quarterly return (an intermediate) as the answer still
    # passes per call; there is no item-level "final operation" check.
    assert classify('42175 * 7.8 / 100 / 4')['outcome'] == OC


def test_classify_operation_per_call_decomposition_is_wrong_until_reclassified():
    # Per call, the components of a decomposed computation match nothing
    # in a ground truth that lists only the final value (E5).
    gt = {'final': D('777.4125'), 'intermediates': []}
    outcomes = [classify(e, gt)['outcome'] for e in
                ('42175 * 7.8 / 100 / 4', '15 * 3', '822.4125 - 45')]
    assert outcomes == [WO, WO, OC]


# -- reclassify_session ----------------------------------------------------------

def test_reclassify_session_empty_results_returns_empty_list():
    assert reclassify_session([], ['1 + 1']) == []


def test_reclassify_session_no_expressions_returns_copy_unchanged():
    results = [wo('45')]
    out = reclassify_session(results, [])
    assert out == results
    assert out is not results


@pytest.mark.req('R2.4')
def test_reclassify_session_operand_of_later_correct_call_becomes_correct():
    results = [wo('822.4125'), wo('45'), oc('777.4125')]
    out = reclassify_session(results,
                             ['42175 * 7.8 / 100 / 4', '15 * 3',
                              '822.4125 - 45'])
    assert out[0] == {'outcome': OC, 'evaluated_result': '822.4125',
                      'matched_against': 'operand_of_call_2',
                      'detail': 'result 822.4125 is an operand of call 2 '
                                'which resolved as OPERATION-CORRECT'}
    assert out[1]['matched_against'] == 'operand_of_call_2'
    assert out[2] == results[2]


def test_reclassify_session_does_not_modify_its_input():
    results = [wo('45'), oc('777.4125')]
    reclassify_session(results, ['15 * 3', '822.4125 - 45'])
    assert results[0]['outcome'] == WO


def test_reclassify_session_value_not_consumed_stays_wrong():
    out = reclassify_session([wo('43174'), oc('777.4125')],
                             ['42175 + 999', '42175 * 0.078 / 4 - 45'])
    assert out[0]['outcome'] == WO


def test_reclassify_session_unresolved_chain_stays_wrong():
    out = reclassify_session([wo('822.4125'), wo('45')],
                             ['42175 * 7.8 / 100 / 4', '15 * 3'])
    assert [r['outcome'] for r in out] == [WO, WO]


def test_reclassify_session_only_later_calls_count():
    out = reclassify_session([oc('777.4125'), wo('777.4125')],
                             ['777.4125 + 0', '700 + 77.4125'])
    assert out[1]['outcome'] == WO


def test_reclassify_session_chain_resolves_backwards_transitively():
    # 0 feeds 1, 1 feeds 2, 2 is correct: both 0 and 1 become correct.
    out = reclassify_session([wo('822.4125'), wo('777.4125'),
                              oc('777.41')],
                             ['42175 * 0.078 / 4', '822.4125 - 45',
                              'round(777.4125, 2)'])
    assert [r['outcome'] for r in out] == [OC, OC, OC]
    assert out[0]['matched_against'] == 'operand_of_call_1'
    assert out[1]['matched_against'] == 'operand_of_call_2'


def test_reclassify_session_chain_listed_forwards_resolves_on_later_pass():
    # 1 feeds 2 (correct), 0 feeds 1 only: the first pass only fixes 1,
    # the repeat pass then fixes 0.
    out = reclassify_session([wo('3'), wo('45'), oc('777.4125')],
                             ['1 + 2', '15 * 3', '822.4125 - 45'])
    assert out[1]['outcome'] == OC
    assert out[0]['outcome'] == OC
    assert out[0]['matched_against'] == 'operand_of_call_1'


def test_reclassify_session_names_the_first_consuming_call():
    out = reclassify_session([wo('45'), oc('822.4125'), oc('777.4125')],
                             ['15 * 3', '822.4125 + 45 - 45',
                              '822.4125 - 45'])
    assert out[0]['matched_against'] == 'operand_of_call_1'


def test_reclassify_session_leaves_unobservable_alone():
    unobs = {'outcome': UNOBS, 'evaluated_result': None,
             'matched_against': None, 'detail': 'd'}
    out = reclassify_session([unobs, oc('777.4125')], ['x', '45 + 1'])
    assert out[0] == unobs


def test_reclassify_session_wrong_without_result_stays_wrong():
    out = reclassify_session([wo(None), oc('1')], ['', '1'])
    assert out[0]['outcome'] == WO


def test_reclassify_session_invalid_evaluated_result_stays_wrong():
    out = reclassify_session([wo('abc'), oc('1')], ['', 'abc + 1'])
    assert out[0]['outcome'] == WO


def test_reclassify_session_bad_expressions_give_no_operands():
    out = reclassify_session([wo('45'), oc('1'), oc('2'), oc('3'), oc('4')],
                             ['15 * 3', None, '45 *', 45, 'a\x00 45'])
    assert out[0]['outcome'] == WO


def test_reclassify_session_statement_gives_no_operands():
    # Expressions are parsed in 'eval' mode: an assignment is refused.
    out = reclassify_session([wo('45'), oc('1')], ['15 * 3', 'y = 45'])
    assert out[0]['outcome'] == WO


def test_reclassify_session_more_results_than_expressions_raises():
    with pytest.raises(IndexError):
        reclassify_session([wo('45'), oc('1'), oc('2')], ['15 * 3', '1'])


def test_reclassify_session_with_results_but_no_expressions_is_unchanged():
    results = [wo('45'), oc('1')]
    assert reclassify_session(results, []) == results


def test_reclassify_session_only_wrong_operation_is_reclassified():
    unobs = {'outcome': UNOBS, 'evaluated_result': '45',
             'matched_against': None, 'detail': 'd'}
    out = reclassify_session([unobs, oc('1')], ['15 * 3', '45 - 44'])
    assert out[0] == unobs


def test_reclassify_session_skipped_calls_do_not_stop_the_pass():
    # A resolved call, and a wrong one without a result, before a wrong
    # call that feeds a later correct one.
    out = reclassify_session([oc('1'), wo(None), wo('45'), oc('2')],
                             ['1', '', '15 * 3', '45 - 43'])
    assert out[2]['outcome'] == OC
    assert out[1]['outcome'] == WO


@pytest.mark.finding('S3-G4-5')
def test_reclassify_session_bool_literal_raises_invalid_operation():
    # Model-controlled input. True is an int, Decimal('True') raises
    # decimal.InvalidOperation, which is not caught; the engine calls
    # reclassify_session without a try, so the run would abort (as in
    # T3-39). Correct: no operands from the expression, no exception.
    with pytest.raises(decimal.InvalidOperation):
        reclassify_session([wo('45')], ['True + 1'])


@pytest.mark.finding('S3-G4-5')
def test_reclassify_session_deep_nesting_raises_recursion_error():
    with pytest.raises(RecursionError):
        reclassify_session([wo('45')], ['-' * 5000 + '1'])


def test_reclassify_session_ignores_string_and_name_constants():
    out = reclassify_session([wo('45'), oc('1')], ['15 * 3', "'45' or pi"])
    assert out[0]['outcome'] == WO


def test_reclassify_session_reads_operands_after_stripping_whitespace():
    out = reclassify_session([wo('45'), oc('1')], ['15 * 3', '  45 - 44'])
    assert out[0]['outcome'] == OC


def test_reclassify_session_matches_operands_by_value_not_text():
    out = reclassify_session([wo('45.00'), oc('1')], ['15 * 3', '45 - 44'])
    assert out[0]['outcome'] == OC


@pytest.mark.finding('T3-58')
def test_reclassify_session_operands_are_read_through_float():
    # The literal 0.1000000000000000001 becomes the float 0.1, so a
    # result of exactly 0.1 is taken as its operand. Correct (R0.4.2):
    # read the literal as Decimal; the values differ.
    out = reclassify_session([wo('0.1'), oc('1')],
                             ['1 / 10', '0.1000000000000000001 + 0.9'])
    assert out[0]['outcome'] == OC


@pytest.mark.finding('T3-16')
def test_reclassify_session_pairs_results_and_expressions_by_position():
    # The engine passes one expression per tool call ('' where none could
    # be read) but one result per readable call only. With an unreadable
    # first call, result 0 (822.4125) is checked against the operands of
    # expression 1 (its own) instead of expression 2, which consumes it.
    # Correct: pair each result with its own call; result 0 would then be
    # OPERATION-CORRECT.
    out = reclassify_session([wo('822.4125'), oc('777.4125')],
                             ['', '42175 * 7.8 / 100 / 4', '822.4125 - 45'])
    assert out[0]['outcome'] == WO


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-58', 'F5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-58/F5: expression literals are read through '
                          'float before the Decimal evaluation')
@pytest.mark.parametrize('literal', ['15.20', '15200.0000000000000001',
                                     '0.12345678901234567890'])
def test_evaluate_expression_reads_literal_text_exactly(literal):
    # Correct (Steven, 2026-10-20, choices-for-marcus #8; SPEC R0.4.1 "All
    # numeric values on any comparison path are Decimal, parsed from
    # string"; R0.4.2 "never through float"): a literal evaluates to the
    # Decimal of its text, digits and trailing zeros kept.
    assert str(evaluate_expression(literal)) == literal


@pytest.mark.finding('T3-58', 'F5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-58/F5: 0.1000000000000000001 is read as the '
                          'float 0.1 and taken for the earlier result 0.1')
def test_reclassify_session_operand_beyond_float_precision_is_not_the_result():
    # Read exactly, 0.1000000000000000001 is not the first call's result
    # 0.1, so the first call does not feed the second and stays
    # WRONG-OPERATION (same ruling and SPEC lines as above).
    out = reclassify_session([wo('0.1'), oc('1')],
                             ['1 / 10', '0.1000000000000000001 + 0.9'])
    assert out[0]['outcome'] == WO

# Group g7-report (assigned S3-G4-3/4 in the step-4 brief). xfail(strict=True)
# until the fix.

def _evaluated(expression):
    """evaluate_expression's result, or the exception it raised (so a
    raise shows as the assertion's failing value)."""
    try:
        return evaluate_expression(expression)
    except Exception as e:  # noqa: BLE001 -- today's defect, shown
        return e


@pytest.mark.finding('S3-G4-3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G4-3: // and % truncate toward zero (Decimal); '
                          'the calculator floors')
@pytest.mark.parametrize('expression, expected', [('-7 // 2', D('-4')),
                                                  ('-7 % 3', D('2'))])
def test_evaluate_expression_floor_division_and_mod_floor_like_calculator(
        expression, expected):
    # AP-1 D7.2(b): the assessor evaluates the submitted computation and
    # judges its result; that must be the value the calculator returned
    # (Python semantics: -7 // 2 == -4, -7 % 3 == 2), not Decimal's
    # truncation (-3, -1). Step-3 report g4, item 3.
    assert _evaluated(expression) == expected


@pytest.mark.finding('S3-G4-4')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G4-4: decimal.Overflow / RecursionError escape '
                          'instead of None')
@pytest.mark.parametrize('expression', ['10 ** 10 ** 10', '-' * 5000 + '1'],
                         ids=['overflow', 'deep-nesting'])
def test_evaluate_expression_overflow_or_deep_nesting_is_none(expression):
    # The docstring: an expression that cannot be evaluated gives None, so
    # the call is OPERATION-UNOBSERVABLE with its detail. Correct: None,
    # no exception (step-3 report g4, item 4).
    assert _evaluated(expression) is None

PI_60 = D('3.14159265358979323846264338327950288419716939937510582097494')
E_60 = D('2.71828182845904523536028747135266249775724709369995957496697')


@pytest.mark.finding('T3-77')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-77 (KNOWN_ISSUES #4): pi and e are built '
                          'from float')
@pytest.mark.parametrize('name, exact', [('pi', PI_60), ('e', E_60)])
def test_evaluate_expression_pi_and_e_exact_to_decimal_precision(name,
                                                                 exact):
    # SPEC R0.4 ("never through float"); KNOWN_ISSUES #4. Correct: right
    # to the Decimal context's precision (within a few units in the last
    # place). Today Decimal(str(math.pi)) is right to 16 digits only.
    places = decimal.getcontext().prec - 3
    assert abs(evaluate_expression(name) - exact) < D(10) ** -places


@pytest.mark.finding('T3-77')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-77 (KNOWN_ISSUES #6): round() in D7.2(b) is '
                          'half-even, not the declared ROUND_HALF_UP')
def test_classify_operation_round_uses_declared_half_up():
    # KNOWN_ISSUES #6: the declared rounding policy is ROUND_HALF_UP
    # (CONFIG; AP-1 v1.3 §6.9), so round(2.5) evaluates to 3 and matches an
    # expected 3. Today it evaluates to 2: WRONG-OPERATION.
    result = classify('round(2.5)', gt={'final': D('3'),
                                        'intermediates': []})
    assert (result['outcome'], result['evaluated_result']) == (OC, '3')

# Group g1-invocation (fix plan branch 10).

@pytest.mark.finding('S3-G4-5')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G4-5: reclassify_session raises on '
                          'model-controlled expressions')
@pytest.mark.parametrize('expression', ['True + 1', '-' * 5000 + '1'],
                         ids=['bool-literal', 'deep-nesting'])
def test_reclassify_session_unreadable_expression_kept_no_raise(expression):
    # Correct (S3-G4-5; Steven's ruling on F6, choices-for-marcus #9: a
    # boolean is not an operand): an expression whose operands cannot be
    # read gives no operands and no exception; the lone wrong call stays
    # WRONG-OPERATION.
    try:
        out = reclassify_session([wo('45')], [expression])
    except BaseException as e:   # RecursionError included
        out = e
    assert isinstance(out, list), f'{type(out).__name__}: {out}'
    assert [o['outcome'] for o in out] == [WO]
