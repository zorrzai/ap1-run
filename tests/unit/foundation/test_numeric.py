"""Unit tests for R0.4 numeric parsing, extraction, quantisation and
canonical hashing (foundation/numeric.py).

These pin today's behaviour. Where today's behaviour is a known or newly
found defect, the test carries @pytest.mark.finding and a comment saying
what the correct behaviour would be.
"""

import hashlib
from decimal import Decimal, InvalidOperation, localcontext

import pytest

from ap1_run.foundation.numeric import (
    ROUNDING_MODES, AmbiguousLocaleError, NumericParseError, NumericToken,
    _check_no_float, canonical_hash, canonical_json, extract_numeric_tokens,
    file_hash, parse_decimal, quantise,
)

D = Decimal


def parsed(text, **kw):
    return parse_decimal(text, **kw)


def tokens(text, **kw):
    """(value, percent, currency, literal) of each token, as strings."""
    return [(str(t.value), t.percent, t.currency, t.literal)
            for t in extract_numeric_tokens(text, **kw)]


def values(text, **kw):
    return [str(t.value) for t in extract_numeric_tokens(text, **kw)]


# -- parse_decimal: plain values ------------------------------------------

@pytest.mark.req('R0.4.2')
def test_parse_decimal_plain_value_returns_decimal_triple():
    v, pct, cur = parse_decimal('1780.00')
    assert (v, pct, cur) == (D('1780.00'), False, '')
    assert type(v) is Decimal
    assert str(v) == '1780.00'


def test_parse_decimal_keeps_trailing_zeros_exactly():
    assert str(parsed('15.20')[0]) == '15.20'


def test_parse_decimal_long_literal_keeps_every_digit():
    # Never through float: 22 significant digits survive (contrast T3-58,
    # which is in provenance.py and operation_correctness.py, not here).
    assert str(parsed('15200.0000000000000001')[0]) == \
        '15200.0000000000000001'


def test_parse_decimal_surrounding_whitespace_ignored():
    assert parsed('  7 ') == (D('7'), False, '')


def test_parse_decimal_grouping_removed():
    assert parsed('1,000,000.5') == (D('1000000.5'), False, '')


def test_parse_decimal_leading_and_trailing_point():
    assert parsed('.5')[0] == D('0.5')
    assert parsed('5.')[0] == D('5')


# -- parse_decimal: errors ------------------------------------------------

def test_parse_decimal_empty_raises_with_message():
    with pytest.raises(NumericParseError, match='^empty string$'):
        parse_decimal('')


def test_parse_decimal_whitespace_only_is_empty():
    with pytest.raises(NumericParseError, match='^empty string$'):
        parse_decimal('   ')


def test_parse_decimal_symbol_only_has_no_digits():
    with pytest.raises(NumericParseError) as e:
        parse_decimal('$', currency_symbols=['$'])
    assert str(e.value) == "no digits in: '$'"


def test_parse_decimal_percent_only_has_no_digits():
    with pytest.raises(NumericParseError, match="no digits in: '%'"):
        parse_decimal('%')


def test_parse_decimal_empty_parentheses_have_no_digits():
    with pytest.raises(NumericParseError, match=r"no digits in: '\(\)'"):
        parse_decimal('()')


def test_parse_decimal_garbage_raises_with_both_texts():
    with pytest.raises(NumericParseError) as e:
        parse_decimal('1.2.3')
    assert str(e.value) == "cannot parse as Decimal: '1.2.3' from '1.2.3'"


def test_parse_decimal_error_shows_text_after_stripping():
    with pytest.raises(NumericParseError) as e:
        parse_decimal('$1.2.3', currency_symbols=['$'])
    assert str(e.value) == "cannot parse as Decimal: '1.2.3' from '$1.2.3'"


def test_parse_decimal_unclosed_parenthesis_raises():
    # T3-55: a mutant parsing '(123' as -12 survived the legacy suites.
    with pytest.raises(NumericParseError):
        parse_decimal('(123')
    with pytest.raises(NumericParseError):
        parse_decimal('123)')


def test_parse_decimal_hex_raises():
    with pytest.raises(NumericParseError):
        parse_decimal('0x10')


def test_parse_decimal_error_is_not_chained_from_decimal():
    # The InvalidOperation is replaced, not wrapped with 'from'.
    with pytest.raises(NumericParseError) as e:
        parse_decimal('abc')
    assert isinstance(e.value.__context__, InvalidOperation)


# -- parse_decimal: signs and parentheses ---------------------------------

@pytest.mark.req('R0.4.2')
def test_parse_decimal_parenthesised_is_negative():
    assert parsed('(1,780.00)') == (D('-1780.00'), False, '')


def test_parse_decimal_parenthesised_with_inner_spaces():
    assert parsed('( 5 )')[0] == D('-5')


def test_parse_decimal_hyphen_minus_is_negative():
    assert parsed('-42.50')[0] == D('-42.50')


def test_parse_decimal_unicode_minus_is_negative():
    assert parsed('−42.50')[0] == D('-42.50')


def test_parse_decimal_plus_is_positive():
    assert parsed('+5')[0] == D('5')


def test_parse_decimal_space_after_sign_ignored():
    assert parsed('- 5')[0] == D('-5')
    assert parsed('+ 5')[0] == D('5')


def test_parse_decimal_sign_before_parenthesis_raises():
    with pytest.raises(NumericParseError):
        parse_decimal('-(5)')


# -- parse_decimal: percent -----------------------------------------------

@pytest.mark.req('R0.4.2')
def test_parse_decimal_percent_flag_and_value():
    assert parsed('12.5%') == (D('12.5'), True, '')


def test_parse_decimal_percent_with_space():
    assert parsed('12.5 %') == (D('12.5'), True, '')


def test_parse_decimal_negative_percent():
    assert parsed('-5%') == (D('-5'), True, '')


# -- parse_decimal: currency ----------------------------------------------

@pytest.mark.req('R0.4.2')
def test_parse_decimal_leading_currency():
    assert parsed('$1,780.00', currency_symbols=['$']) == \
        (D('1780.00'), False, '$')


def test_parse_decimal_leading_currency_with_space():
    assert parsed('USD 5', currency_symbols=['$', 'USD']) == \
        (D('5'), False, 'USD')


def test_parse_decimal_trailing_currency():
    assert parsed('5 USD', currency_symbols=['$', 'USD']) == \
        (D('5'), False, 'USD')
    assert parsed('5$', currency_symbols=['$']) == (D('5'), False, '$')


def test_parse_decimal_currency_inside_parentheses():
    assert parsed('($1,780.00)', currency_symbols=['$']) == \
        (D('-1780.00'), False, '$')
    assert parsed('(5$)', currency_symbols=['$']) == (D('-5'), False, '$')


def test_parse_decimal_currency_after_sign():
    assert parsed('-$2411.00', currency_symbols=['$', 'USD']) == \
        (D('-2411.00'), False, '$')


def test_parse_decimal_sign_after_currency():
    assert parsed('$-2411.00', currency_symbols=['$', 'USD']) == \
        (D('-2411.00'), False, '$')


def test_parse_decimal_currency_and_percent():
    assert parsed('$5%', currency_symbols=['$']) == (D('5'), True, '$')


def test_parse_decimal_leading_currency_longest_symbol_first():
    # 'US' would leave 'D5'; the longest symbol must be tried first.
    assert parsed('USD5', currency_symbols=['US', 'USD']) == \
        (D('5'), False, 'USD')


def test_parse_decimal_currency_after_sign_longest_symbol_first():
    assert parsed('-USD5', currency_symbols=['US', 'USD']) == \
        (D('-5'), False, 'USD')


def test_parse_decimal_trailing_currency_longest_symbol_first():
    # 'SD' would leave '5U'.
    assert parsed('5USD', currency_symbols=['SD', 'USD']) == \
        (D('5'), False, 'USD')


def test_parse_decimal_leading_currency_stripped_once():
    with pytest.raises(NumericParseError):
        parse_decimal('$$5', currency_symbols=['$'])


def test_parse_decimal_currency_after_sign_stripped_once():
    with pytest.raises(NumericParseError):
        parse_decimal('-$$5', currency_symbols=['$'])


def test_parse_decimal_trailing_currency_longest_not_alphabetical_first():
    # Reverse alphabetical order would try 'r' before 'Fr', leaving '5F'.
    assert parsed('5Fr', currency_symbols=['r', 'Fr']) == (D('5'), False, 'Fr')


def test_parse_decimal_letter_is_not_a_sign():
    with pytest.raises(NumericParseError):
        parse_decimal('X5')


def test_parse_decimal_trailing_currency_stripped_once():
    with pytest.raises(NumericParseError):
        parse_decimal('5$$', currency_symbols=['$'])


def test_parse_decimal_without_symbols_currency_is_not_stripped():
    with pytest.raises(NumericParseError):
        parse_decimal('$5')


def test_parse_decimal_symbols_none_and_empty_list_agree():
    assert parsed('5', currency_symbols=None) == parsed('5',
                                                       currency_symbols=[])


# -- parse_decimal: separators --------------------------------------------

@pytest.mark.req('R0.4.2')
def test_parse_decimal_european_separators():
    assert parsed('1.780,00', decimal_sep=',', grouping_sep='.') == \
        (D('1780.00'), False, '')


def test_parse_decimal_european_decimal_only():
    assert parsed('1,5', decimal_sep=',', grouping_sep='.')[0] == D('1.5')


def test_parse_decimal_space_grouping():
    assert parsed('1 000,5', decimal_sep=',', grouping_sep=' ')[0] == \
        D('1000.5')


def test_parse_decimal_no_grouping_separator_none():
    assert parsed('1,000', decimal_sep=',', grouping_sep=None)[0] == \
        D('1.000')


def test_parse_decimal_no_grouping_separator_empty():
    assert parsed('1,000', decimal_sep=',', grouping_sep='')[0] == \
        D('1.000')


def test_parse_decimal_second_decimal_separator_not_normalised():
    with pytest.raises(NumericParseError) as e:
        parse_decimal('1,5,6', decimal_sep=',', grouping_sep='.')
    assert "'1.5,6'" in str(e.value)


@pytest.mark.req('R0.4.2')
def test_parse_decimal_same_separators_with_separator_is_ambiguous():
    with pytest.raises(AmbiguousLocaleError) as e:
        parse_decimal('1.780', decimal_sep='.', grouping_sep='.')
    assert str(e.value) == (
        "'1.780': separator '.' is configured as both decimal and "
        "grouping -- cannot disambiguate")


def test_parse_decimal_grouping_point_with_default_decimal_is_ambiguous():
    # The default decimal separator is '.', so a '.' grouping clashes.
    with pytest.raises(AmbiguousLocaleError):
        parse_decimal('1.000', grouping_sep='.')


def test_parse_decimal_same_separators_without_separator_parses():
    assert parsed('100', decimal_sep='.', grouping_sep='.')[0] == D('100')


def test_parse_decimal_ambiguity_checked_after_stripping():
    # The check sees the digit string, not the currency or sign.
    with pytest.raises(AmbiguousLocaleError, match="^'1,5'"):
        parse_decimal('$-1,5', decimal_sep=',', grouping_sep=',',
                      currency_symbols=['$'])


@pytest.mark.finding('S3-G1-3')
def test_parse_decimal_grammar_refusal_names_digits_and_text():
    with pytest.raises(NumericParseError) as e:
        parse_decimal('$1,23', currency_symbols=['$'])
    assert str(e.value) == "not a number under R0.4.2: '1,23' from '$1,23'"


@pytest.mark.req('R0.4.2')
@pytest.mark.parametrize('text, decimal_sep, grouping_sep, value', [
    ('1,234,567.5', '.', ',', '1234567.5'),
    ('1.234.567,5', ',', '.', '1234567.5'),
    ('12,5', ',', '.', '12.5'),
    ('1234567', '.', ',', '1234567'),
    ('1234,5', ',', '.', '1234.5'),
    ('1,5', ',', '', '1.5'),
])
def test_parse_decimal_grammar_accepts_well_formed(text, decimal_sep,
                                                   grouping_sep, value):
    assert str(parsed(text, decimal_sep=decimal_sep,
                      grouping_sep=grouping_sep)[0]) == value


@pytest.mark.req('R0.4.2')
@pytest.mark.parametrize('text, decimal_sep, grouping_sep', [
    ('1234,567', '.', ','),     # a group of four before the separator
    ('1,2345', '.', ','),       # a group of four after it
    (',123', '.', ','),         # no leading group
    ('1,234.5,6', '.', ','),    # grouping in the decimal part
    ('1.234,5', ',', ''),       # no grouping configured
    ('1.5', ',', '.'),          # '.' configured as grouping: misplaced
])
def test_parse_decimal_grammar_refuses_malformed(text, decimal_sep,
                                                 grouping_sep):
    with pytest.raises(NumericParseError):
        parse_decimal(text, decimal_sep=decimal_sep,
                      grouping_sep=grouping_sep)


@pytest.mark.finding('S3-G1-7')
def test_parse_decimal_accepts_non_ascii_digits():
    # Current behaviour: Arabic-Indic digits parse (Decimal accepts any
    # Unicode decimal digit). Correct per R0.4.2: decide and declare.
    assert parsed('١٢')[0] == D('12')


# -- extract_numeric_tokens -----------------------------------------------

def test_extract_returns_named_tokens_with_positions():
    toks = extract_numeric_tokens('x 12.5% y')
    assert toks == [NumericToken(value=D('12.5'), percent=True, currency='',
                                 literal='12.5%', start=2, end=7)]


def test_extract_empty_and_digitless_text_give_nothing():
    assert extract_numeric_tokens('') == []
    assert extract_numeric_tokens('no numbers here') == []


@pytest.mark.req('R0.4.2')
def test_extract_several_values_in_order():
    text = 'Step 1: 274.1375, Step 2: 259.1375, Final: 777.41'
    assert values(text) == ['1', '274.1375', '2', '259.1375', '777.41']


def test_extract_grouped_value_is_one_token():
    assert tokens('a 1,234,567.89 b') == [
        ('1234567.89', False, '', '1,234,567.89')]


def test_extract_badly_grouped_value_splits():
    assert values('12,34') == ['12', '34']
    assert values('1234,567') == ['1234', '567']


def test_extract_currency_led_with_space():
    assert tokens('pay $ 5 now', currency_symbols=['$']) == [
        ('5', False, '$', '$ 5')]


def test_extract_currency_led_then_sign():
    assert tokens('$-2411.00', currency_symbols=['$', 'USD']) == [
        ('-2411.00', False, '$', '$-2411.00')]


def test_extract_currency_led_unicode_minus_and_percent():
    assert tokens('$ − 5 %', currency_symbols=['$']) == [
        ('-5', True, '$', '$ − 5 %')]


def test_extract_sign_led_then_currency():
    assert tokens('is -$2411.00.', currency_symbols=['$', 'USD']) == [
        ('-2411.00', False, '$', '-$2411.00')]


def test_extract_sign_led_with_trailing_currency():
    assert tokens('-5 USD', currency_symbols=['USD']) == [
        ('-5', False, 'USD', '-5 USD')]


def test_extract_trailing_currency_both_spacings():
    assert tokens('5 USD and 6USD', currency_symbols=['USD']) == [
        ('5', False, 'USD', '5 USD'), ('6', False, 'USD', '6USD')]


def test_extract_currency_longest_symbol_first():
    assert tokens('USD5', currency_symbols=['US', 'USD']) == [
        ('5', False, 'USD', 'USD5')]


def test_extract_trailing_currency_longest_symbol_first():
    # Trying 'US' first would match '5US' and report currency 'US'.
    assert tokens('5USD', currency_symbols=['US', 'USD']) == [
        ('5', False, 'USD', '5USD')]


def test_extract_symbol_with_regex_metacharacters_is_literal():
    assert tokens('cost $5 or x5', currency_symbols=['$']) == [
        ('5', False, '$', '$5'), ('5', False, '', '5')]


def test_extract_without_symbols_ignores_currency_characters():
    assert tokens('$5') == [('5', False, '', '5')]


@pytest.mark.req('R0.4.2')
def test_extract_parenthesised_negative():
    assert tokens('The loss was ($2,400.00) this quarter.',
                  currency_symbols=['$']) == [
        ('-2400.00', False, '$', '($2,400.00)')]


def test_extract_parenthesised_negative_without_symbols():
    # T3-55: a mutant reading '(1,780)' as -178 survived the legacy suites.
    assert tokens('(1,780)') == [('-1780', False, '', '(1,780)')]


def test_extract_parenthesised_with_spaces_and_trailing_currency():
    assert tokens('( 5 $)', currency_symbols=['$']) == [
        ('-5', False, '$', '( 5 $)')]


def test_extract_unclosed_parenthesis_gives_positive():
    assert tokens('(123') == [('123', False, '', '123')]


def test_extract_sign_led_negative_without_symbols():
    # T3-55: mutants losing the sign when no symbols are configured survived.
    assert tokens('was -5 and −7 and +3') == [
        ('-5', False, '', '-5'), ('-7', False, '', '−7'),
        ('3', False, '', '+3')]


def test_extract_percent_with_space():
    assert tokens('rate 3 %') == [('3', True, '', '3 %')]


def test_extract_adjacent_tokens_both_kept():
    # T3-55: a mutant dropping '-3' from '5-3' survived the legacy suites.
    assert tokens('5-3') == [('5', False, '', '5'), ('-3', False, '', '-3')]


def test_extract_adjacent_currency_tokens_positions():
    toks = extract_numeric_tokens('$5 $10', currency_symbols=['$'])
    assert [(t.literal, t.start, t.end) for t in toks] == [
        ('$5', 0, 3), ('$10', 3, 6)]


def test_extract_overlap_keeps_longest_match():
    # The sign-led match '-$5' and the currency-led '$5' overlap; the
    # longer, earlier one wins and '$5' is not reported twice.
    assert tokens('-$5', currency_symbols=['$']) == [
        ('-5', False, '$', '-$5')]


@pytest.mark.finding('S3-G1-5')
def test_extract_subtraction_operand_read_as_negative():
    # Current behaviour: the sign-led pattern takes the minus of a
    # subtraction, so '1437.00 - 1006.25 = 430.75' yields -1006.25.
    # Correct: a minus between two operands is an operator; 1006.25.
    text = 'Principal portion = 1437.00 - 1006.25 = 430.75'
    assert tokens(text) == [
        ('1437.00', False, '', '1437.00'),
        ('-1006.25', False, '', '- 1006.25'),
        ('430.75', False, '', '430.75')]


@pytest.mark.finding('S3-G1-6')
def test_extract_digits_inside_words_are_tokens():
    # Current behaviour: no word boundary, so identifiers and version
    # strings yield numbers ('Q04' -> 4, 'v2.0.1' -> 2.0 and 1, '1e5' ->
    # 1 and 5). Correct: digits inside a word are not numeric tokens.
    assert tokens('Q04') == [('4', False, '', '04')]
    assert values('v2.0.1') == ['2.0', '1']
    assert values('1e5') == ['1', '5']


def test_extract_unparseable_match_is_skipped_and_extraction_goes_on():
    # T3-55: a mutant ending extraction at the first unparseable match
    # ('continue' -> 'break') survived the legacy suites. '($5$)' matches
    # the parenthesised pattern but has two currency symbols, so
    # parse_decimal refuses it; the 7 after it is still extracted. (This
    # replaces the S3-G1-4 pin on '10%USD', which now parses.)
    assert tokens('($5$) and 7', currency_symbols=['$']) == [
        ('7', False, '', '7')]


@pytest.mark.finding('S3-G1-8')
def test_extract_parenthesised_percent_loses_negative():
    # Current behaviour: the parenthesised pattern has no '%', so
    # '(12.5%)' is read as +12.5 %. Correct: -12.5 %.
    assert tokens('(12.5%)') == [('12.5', True, '', '12.5%')]


@pytest.mark.req('R0.4.2')
def test_extract_european_separators_when_configured():
    assert tokens('1.006,25 and 2,5', decimal_sep=',', grouping_sep='.') \
        == [('1006.25', False, '', '1.006,25'), ('2.5', False, '', '2,5')]


@pytest.mark.finding('T3-41')
def test_extract_default_separators_split_european_amount():
    # Current behaviour: the defaults are US separators, and no caller
    # passes the configured decimal_separator/grouping_separator (T3-41),
    # so '1.006,25' becomes 1.006 and 25. Correct (in the callers): pass
    # the configured separators, giving one token 1006.25.
    assert values('1.006,25') == ['1.006', '25']


def test_extract_no_grouping_separator_reads_digits_only():
    assert tokens('1,000', decimal_sep=',', grouping_sep='') == [
        ('1.000', False, '', '1,000')]
    assert values('1 234', grouping_sep='') == ['1', '234']


def test_extract_grouping_separator_none_reads_digits_only():
    assert values('1,000', decimal_sep=',', grouping_sep=None) == ['1.000']


def test_extract_space_grouping_separator():
    assert values('1 234,5', decimal_sep=',', grouping_sep=' ') == \
        ['1234.5']


@pytest.mark.req('R0.4.2')
def test_extract_ambiguous_token_raises():
    with pytest.raises(AmbiguousLocaleError):
        extract_numeric_tokens('1.780', decimal_sep='.', grouping_sep='.')


def test_extract_same_separators_unambiguous_token_passes():
    assert values('1780', decimal_sep='.', grouping_sep='.') == ['1780']


@pytest.mark.finding('S3-G1-7')
def test_extract_non_ascii_digits_are_tokens():
    # Current behaviour: '\d' matches any Unicode digit. See S3-G1-7.
    assert values('٣٤ and ５') == ['34', '5']


def test_extract_run1_literal_mortgage_prose():
    text = ('The remaining mortgage balance after the first monthly payment '
            'of $1437.00 will be $286,063.00.')
    assert tokens(text, currency_symbols=['$', 'USD']) == [
        ('1437.00', False, '$', '$1437.00'),
        ('286063.00', False, '$', '$286,063.00')]


# -- quantise -------------------------------------------------------------

def test_rounding_modes_are_the_two_declared():
    assert set(ROUNDING_MODES) == {'ROUND_HALF_UP', 'ROUND_HALF_EVEN'}


@pytest.mark.req('R0.4.1')
def test_quantise_default_is_half_up():
    assert str(quantise(D('2.345'), 2)) == '2.35'
    assert str(quantise(D('-2.345'), 2)) == '-2.35'


def test_quantise_half_even():
    assert str(quantise(D('2.345'), 2, 'ROUND_HALF_EVEN')) == '2.34'
    assert str(quantise(D('2.5'), 0, 'ROUND_HALF_EVEN')) == '2'


def test_quantise_half_up_explicit():
    assert str(quantise(D('2.5'), 0, 'ROUND_HALF_UP')) == '3'


def test_quantise_pads_to_places():
    assert str(quantise(D('2'), 2)) == '2.00'


@pytest.mark.req('R0.4.1')
def test_quantise_once_differs_from_each_step():
    a = D('42175.00') * D('7.8') / D('100') / D('12')
    once = quantise((a - D('15.00')) * 3, 2)
    each = quantise((quantise(a, 2) - D('15.00')) * 3, 2)
    assert (str(once), str(each)) == ('777.41', '777.42')


def test_quantise_unknown_mode_raises():
    with pytest.raises(ValueError) as e:
        quantise(D('1'), 2, 'ROUND_DOWN')
    assert str(e.value) == "unsupported rounding mode: 'ROUND_DOWN'"


@pytest.mark.finding('S3-G1-9')
@pytest.mark.parametrize('places', [-1, 2.0, '2', True, None])
def test_quantise_places_not_a_non_negative_int_refused(places):
    with pytest.raises(ValueError) as e:
        quantise(D('1.5'), places)
    assert str(e.value) == (
        f'quantisation places must be a non-negative int: {places!r}')


def test_quantise_zero_places_rounds_to_units():
    assert str(quantise(D('2.5'), 0)) == '3'


@pytest.mark.finding('T3-60')
def test_quantise_overflow_does_not_depend_on_context_precision():
    # T3-60 fixed: quantise runs in numeric.DECIMAL_CONTEXT (precision
    # 50), so 1E30 to two places gives the same result whatever the
    # caller's precision, and the caller's context is left as it was.
    for prec in (28, 50):
        with localcontext() as ctx:
            ctx.prec = prec
            assert quantise(D('1E30'), 2) == D('1E30')
            assert ctx.prec == prec


# -- _check_no_float ------------------------------------------------------

def test_check_no_float_top_level_float_refused_with_path():
    with pytest.raises(TypeError) as e:
        _check_no_float(1.5)
    assert str(e.value) == ('float at $: 1.5 -- R0.4.1 prohibits float '
                            'on comparison paths')


def test_check_no_float_paths_name_keys_and_indexes():
    with pytest.raises(TypeError, match=r'^float at \$\.a\.b\[1\]: 2\.0 '):
        _check_no_float({'a': {'b': [1, 2.0]}})
    with pytest.raises(TypeError, match=r'^float at \$\[1\]\[0\]: 3\.5 '):
        _check_no_float([1, (3.5,)])


def test_check_no_float_accepts_other_types():
    assert _check_no_float({'a': [1, True, None, 'x', D('1.5')]}) is None


# -- canonical_json and canonical_hash ------------------------------------

@pytest.mark.req('R0.4.3')
def test_canonical_json_sorted_compact_decimal_as_string():
    obj = {'b': D('3.0'), 'a': ['x', 1, True, None], 'c': {'z': 1, 'y': 2}}
    assert canonical_json(obj) == \
        '{"a":["x",1,true,null],"b":"3.0","c":{"y":2,"z":1}}'


def test_canonical_json_keeps_decimal_text_exactly():
    obj = {'a': D('1.0'), 'b': D('1E+2'), 'c': D('-0')}
    assert canonical_json(obj) == '{"a":"1.0","b":"1E+2","c":"-0"}'


def test_canonical_json_non_ascii_written_as_is():
    assert canonical_json({'u': '−é'}) == '{"u":"−é"}'


@pytest.mark.req('R0.4.1')
def test_canonical_json_refuses_float_anywhere():
    with pytest.raises(TypeError, match='float at'):
        canonical_json({'value': 1.5})
    with pytest.raises(TypeError, match=r'float at \$\.outer\.inner\[2\]'):
        canonical_json({'outer': {'inner': [1, 2, 3.0]}})


def test_canonical_json_unserialisable_object_raises():
    with pytest.raises(TypeError,
                       match='^Object of type object is not JSON serializable$'):
        canonical_json({'x': object()})


def test_canonical_json_mixed_key_types_raise():
    # sort_keys cannot order int and str keys.
    with pytest.raises(TypeError):
        canonical_json({1: 'a', 'b': 'c'})


@pytest.mark.req('R0.4.3')
def test_canonical_hash_is_sha256_of_utf8_canonical_json():
    obj = {'k': D('1.50'), 'u': '−'}
    expected = hashlib.sha256(
        '{"k":"1.50","u":"−"}'.encode('utf-8')).hexdigest()
    assert canonical_hash(obj) == expected


def test_canonical_hash_key_order_irrelevant():
    assert canonical_hash({'b': 'two', 'a': 'one'}) == \
        canonical_hash({'a': 'one', 'b': 'two'})


def test_canonical_hash_known_digest_of_verify_hashes_input():
    # The input of the retired verify_hashes.py. CI runs this test on Linux,
    # macOS and Windows (.github/workflows/hashes.yml), so a platform that
    # hashes differently fails against the pinned digest.
    obj = {
        'z_last': 'should sort last',
        'a_first': 'should sort first',
        'decimal_value': D('274.1375'),
        'nested': {'inner_b': D('777.4125'),
                   'inner_a': [D('15.20'), D('3109.65')]},
        'empty_list': [],
        'unicode': '−',
    }
    text = canonical_json(obj)
    assert text == (
        '{"a_first":"should sort first","decimal_value":"274.1375",'
        '"empty_list":[],"nested":{"inner_a":["15.20","3109.65"],'
        '"inner_b":"777.4125"},"unicode":"−","z_last":"should sort last"}')
    assert canonical_hash(obj) == \
        hashlib.sha256(text.encode('utf-8')).hexdigest()
    # The digest verify_hashes.py prints, the same on every platform.
    assert canonical_hash(obj) == \
        '831709b2231846ed20fd63ff0bc0764d73cee50db271f733e6a2f1c377c7cff3'


def test_canonical_hash_trailing_zero_changes_hash():
    assert canonical_hash({'v': D('1.5')}) != canonical_hash({'v': D('1.50')})


@pytest.mark.finding('T3-71')
def test_canonical_hash_decimal_and_string_collide():
    # Current behaviour: a Decimal is written as a JSON string, so
    # Decimal('0.01') and '0.01' hash the same. Correct: the type is
    # preserved (e.g. tagged), so they differ.
    assert canonical_hash({'x': D('0.01')}) == canonical_hash({'x': '0.01'})


@pytest.mark.finding('T3-71')
def test_canonical_hash_tuple_and_list_collide():
    assert canonical_hash({'x': (1, 2)}) == canonical_hash({'x': [1, 2]})


@pytest.mark.finding('T3-71')
def test_canonical_json_float_key_accepted():
    # Current behaviour: _check_no_float looks only at values, so a float
    # dict key passes and is written as a string. Correct: refuse it.
    assert canonical_json({0.1: 'x'}) == '{"0.1":"x"}'


@pytest.mark.finding('T3-71')
def test_canonical_hash_int_and_string_keys_collide():
    assert canonical_hash({1: 'a'}) == canonical_hash({'1': 'a'})


@pytest.mark.finding('T3-71')
def test_canonical_hash_no_unicode_normalisation():
    # Current behaviour: precomposed and decomposed e-acute hash
    # differently. Correct (T3-71): normalise (NFC) before hashing.
    assert canonical_hash({'s': 'é'}) != canonical_hash({'s': 'é'})


# -- file_hash ------------------------------------------------------------

def test_file_hash_is_sha256_of_raw_bytes(tmp_path):
    data = bytes(range(256)) * 100   # 25600 bytes: several 8192-byte chunks
    p = tmp_path / 'f.bin'
    p.write_bytes(data)
    assert file_hash(p) == hashlib.sha256(data).hexdigest()
    assert file_hash(str(p)) == hashlib.sha256(data).hexdigest()


def test_file_hash_empty_file(tmp_path):
    p = tmp_path / 'empty'
    p.write_bytes(b'')
    assert file_hash(p) == hashlib.sha256(b'').hexdigest()


def test_file_hash_no_newline_translation(tmp_path):
    p = tmp_path / 'crlf.txt'
    p.write_bytes(b'a\r\nb\r\n')
    assert file_hash(p) == hashlib.sha256(b'a\r\nb\r\n').hexdigest()


def test_file_hash_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        file_hash(tmp_path / 'nope')


# --- Step 4: correct behaviour (failing until fixed) ---

def parse_outcome(text, **kw):
    """parse_decimal's result as (value, percent, currency) strings, or
    'refused' when it raises NumericParseError."""
    try:
        value, pct, cur = parse_decimal(text, **kw)
    except NumericParseError:
        return 'refused'
    return (str(value), pct, cur)


@pytest.mark.finding('S3-G1-1')
@pytest.mark.req('R0.4.2')
@pytest.mark.parametrize('text', ['NaN', 'Infinity', 'inf', '1e3', '1_000'])
def test_parse_decimal_value_outside_grammar_is_refused(text):
    # SPEC R0.4.2: a token is digits, optionally grouped, with an optional
    # decimal part; nothing else. Decimal() accepts more, and step 6
    # ("digits + separators only") checks only for emptiness. Reachable
    # through figure_id's structured-answer path, where a NaN figure then
    # breaks every comparison.
    assert parse_outcome(text) == 'refused'


@pytest.mark.finding('S3-G1-2')
@pytest.mark.req('R0.4.2')
@pytest.mark.parametrize('text', ['--5', '+-5', '(-5)'])
def test_parse_decimal_doubled_sign_is_refused(text):
    # SPEC R0.4.2 item 2: "an optional sign -- a leading +/-, OR an
    # enclosing pair of parentheses": one sign at most.
    assert parse_outcome(text) == 'refused'


@pytest.mark.finding('S3-G1-3')
@pytest.mark.req('R0.4.2')
@pytest.mark.parametrize('text', ['1,23', '1,2,3'])
def test_parse_decimal_misplaced_grouping_separator_is_refused(text):
    # SPEC R0.4.2 item 3: digits "optionally grouped by the configured
    # grouping_separator", i.e. in groups of three, as extraction's own
    # pattern requires. A separator elsewhere is not grouping. (Lakh
    # grouping, 12,34,567, is left out: SPEC does not say.)
    assert parse_outcome(text) == 'refused'


@pytest.mark.finding('S3-G1-4')
@pytest.mark.req('R0.4.2')
def test_parse_decimal_percent_then_trailing_currency_parses():
    # SPEC R0.4.2: currency "leading or trailing" and an optional trailing
    # '%'; '5%$' is 5, percent, '$', as '$5%' is.
    assert parse_outcome('5%$', currency_symbols=['$']) == ('5', True, '$')


@pytest.mark.finding('S3-G1-4')
@pytest.mark.req('R0.4.2')
def test_extract_percent_then_currency_token_kept():
    assert tokens('10%USD and 5', currency_symbols=['USD']) == [
        ('10', True, 'USD', '10%USD'), ('5', False, '', '5')]


@pytest.mark.finding('S3-G1-5')
@pytest.mark.req('R0.4.2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-5: the minus of a subtraction is read as the '
                          'sign of the next token')
@pytest.mark.parametrize('text, expected', [
    ('Principal portion = 1437.00 - 1006.25 = 430.75',
     ['1437.00', '1006.25', '430.75']),
    ('5-3', ['5', '3']),
], ids=['spaced', 'unspaced'])
def test_extract_minus_between_operands_is_an_operator(text, expected):
    # A '-' that follows a number is a binary operator, not the sign of
    # the next token (G1 report, S3-g1-5). Reading it as a sign negates an
    # operand quoted in the prose, which changes R2.0's match count (see
    # the end-to-end test in tests/functional/test_step4_g8_numeric_d73.py).
    # A leading sign elsewhere ('was -5') stays a sign. Note: the step-3
    # test test_extract_adjacent_tokens_both_kept pins '5-3' -> [5, -3]
    # (written for T3-55, before this finding); the fix updates it.
    assert values(text) == expected


@pytest.mark.finding('S3-G1-6')
@pytest.mark.req('R0.4.2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-6: digits inside identifiers are numeric '
                          'tokens (Q04 -> 4)')
@pytest.mark.parametrize('text', ['Q04', 'v2.0.1', 'item A1'])
def test_extract_digits_inside_a_word_are_not_tokens(text):
    # SPEC R0.4.2 defines a token as currency/sign/digits/decimal/percent;
    # a run of digits glued to letters is part of a word (an item ID or a
    # version), not a figure. Q04 yielding 4 can create or spoil a match.
    assert values(text) == []


@pytest.mark.finding('S3-G1-8')
@pytest.mark.req('R0.4.2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-8: (12.5%) is extracted as +12.5 %')
def test_extract_parenthesised_percent_is_negative():
    # SPEC R0.4.2: parentheses denote negative; a trailing '%' is allowed.
    # '(12.5%)' is -12.5, percent.
    assert tokens('(12.5%)') == [('-12.5', True, '', '(12.5%)')]


@pytest.mark.finding('S3-G1-9')
@pytest.mark.req('R0.4.1')
def test_quantise_negative_places_refused_or_rounds_to_hundreds():
    # Either refuse negative places (ValueError), or honour them:
    # 1234.5 to -2 places is 1.2E+3. Today: 1235.
    try:
        q = quantise(D('1234.5'), -2)
    except ValueError:
        q = 'refused'
    assert q == 'refused' or (q == D('1200') and q.as_tuple().exponent == 2), q


@pytest.mark.finding('T3-71')
@pytest.mark.req('R0.4.1', 'R0.4.3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-71: _check_no_float looks only at values; a '
                          'float dict key is hashed')
def test_canonical_json_float_key_is_refused():
    # SPEC R0.4.1: no float anywhere a value is compared or hashed;
    # canonical_json refuses float values (TypeError), so a float key must
    # be refused the same way.
    try:
        result = canonical_json({0.1: 'x'})
    except TypeError:
        result = 'refused'
    assert result == 'refused'

# The digest committed in hash_digest.txt from 5522598 (2026-08-03) until
# step 1e stopped tracking the file (5f2a9ae); it never changed. Recover
# it with: git show 5f2a9ae^:hash_digest.txt
VERIFY_HASHES_DIGEST = \
    '831709b2231846ed20fd63ff0bc0764d73cee50db271f733e6a2f1c377c7cff3'


@pytest.mark.finding('T3-20', 'F8')
@pytest.mark.req('R0.4.3')
def test_canonical_hash_pinned_digest_same_on_every_platform():
    # Not an xfail: passes today and must pass on every OS CI runs.
    # T3-20/F8 (Steven's ruling and Marcus's request, 2026-10-16): the CI
    # job wrote this digest on three platforms and compared nothing; the
    # expected value is now pinned in the test, so a platform that hashes
    # differently fails here (SPEC R0.4.3 verification item 1). Inputs are
    # those of tests/legacy/verify_hashes.py, key order varied as there.
    # (test_canonical_hash_known_digest_of_verify_hashes_input, step 3,
    # pins the same digest and the canonical text.)
    obj = {
        'z_last': 'should sort last',
        'a_first': 'should sort first',
        'decimal_value': D('274.1375'),
        'nested': {'inner_b': D('777.4125'),
                   'inner_a': [D('15.20'), D('3109.65')]},
        'empty_list': [],
        'unicode': '−',
    }
    reordered = {
        'unicode': '−',
        'nested': {'inner_a': [D('15.20'), D('3109.65')],
                   'inner_b': D('777.4125')},
        'z_last': 'should sort last',
        'empty_list': [],
        'decimal_value': D('274.1375'),
        'a_first': 'should sort first',
    }
    assert canonical_hash(obj) == VERIFY_HASHES_DIGEST
    assert canonical_hash(reordered) == VERIFY_HASHES_DIGEST

@pytest.mark.finding('T3-77', 'S3-G1-3')
@pytest.mark.parametrize('text', ['1,23', '12,5', '1,2,3'])
def test_parse_decimal_misplaced_grouping_separator_refused(text):
    # KNOWN_ISSUES #5; SPEC R0.4.2 step 3: digits "optionally grouped by
    # the configured grouping_separator", i.e. in groups of three, as the
    # extraction regex already requires. A comma anywhere else is not a
    # grouping separator, so the token is refused rather than read as 123
    # (in a European locale '1,23' means 1.23).
    try:
        value = parse_decimal(text)[0]
    except (NumericParseError, AmbiguousLocaleError):
        return
    assert False, f'{text!r} parsed as {value}'
