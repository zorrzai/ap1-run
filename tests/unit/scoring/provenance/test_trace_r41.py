"""SPEC R4.1 planted behaviour for scoring/provenance/trace.py (legacy
verify_r41.py B27)."""

from decimal import Decimal

import pytest

from ap1_run.scoring.provenance.trace import resolve_operand


@pytest.mark.req('R4.1', 'R2.4')
def test_r41_b27_quantised_prior_return_is_originated_with_near_miss():
    res = resolve_operand(
        Decimal('182.44'), {'savings': {'balance': '15200.00',
                                        'annual_rate': '1.2'}},
        [], set(), [], {'places': '2', 'rounding': 'ROUND_HALF_UP'},
        prior_returns=[{'value': Decimal('182.4375'), 'grounded': True}])
    assert (res['step'], res['resolution']) == (5, 'originated')
    assert res['near_miss_finding'] == {
        'prior_return': '182.4375', 'quantised_to': '182.44',
        'operand': '182.44', 'grounded': True}
