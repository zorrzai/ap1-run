"""SPEC R4.1 planted behaviours for foundation/numeric.py (legacy
verify_r41.py B13, B14)."""

from decimal import Decimal

import pytest

from ap1_run.foundation.numeric import AmbiguousLocaleError, parse_decimal


@pytest.mark.req('R4.1', 'R0.4')
@pytest.mark.parametrize('text, expected', [
    ('1,780.00', (Decimal('1780.00'), False, '')),
    ('($1,780.00)', (Decimal('-1780.00'), False, '$')),
    ('12.5%', (Decimal('12.5'), True, '')),
])
def test_r41_b13_formats_parse_with_point_decimal(text, expected):
    assert parse_decimal(text, decimal_sep='.', grouping_sep=',',
                         currency_symbols=['$']) == expected


@pytest.mark.req('R4.1', 'R0.4')
def test_r41_b13_european_format_parses_with_comma_decimal():
    assert parse_decimal('1.780,00', decimal_sep=',', grouping_sep='.',
                         currency_symbols=['$']) == (Decimal('1780.00'),
                                                     False, '')


@pytest.mark.req('R4.1', 'R0.4')
def test_r41_b14_same_decimal_and_grouping_separator_is_ambiguous():
    with pytest.raises(AmbiguousLocaleError) as exc:
        parse_decimal('1.780', decimal_sep='.', grouping_sep='.')
    assert str(exc.value) == (
        "'1.780': separator '.' is configured as both decimal and "
        "grouping -- cannot disambiguate")
