"""Unit tests for scoring/invocation.py: D7.1 invocation rates per
evidence class, the zero-failure bound, and DPR (R2.3).

Pins today's behaviour, including known defects (marked with
@pytest.mark.finding). None of measure_invocation and compute_dpr has a
live caller; format_rate is used by runner/console.
"""

import decimal
import importlib
import re
from decimal import Decimal

import pytest

from ap1_run.execution.evidence import EV_0, EV_1, EV_2, EV_3
from ap1_run.scoring import invocation
from ap1_run.scoring.invocation import (
    InvocationError, _exact_upper_bound, _summarise_class, compute_dpr,
    format_rate, measure_invocation,
)

D = Decimal


def item(invoked, evidence_class=EV_2, item_id='Q01', condition='base'):
    return {'item_id': item_id, 'condition': condition,
            'invoked': invoked, 'evidence_class': evidence_class}


# -- module ------------------------------------------------------------------

@pytest.mark.finding('T3-60')
def test_invocation_import_sets_global_decimal_precision_to_50():
    # Correct: no module should change the global Decimal context on import;
    # arithmetic elsewhere then depends on whether this module was imported.
    decimal.getcontext().prec = 28
    try:
        importlib.reload(invocation)
        assert decimal.getcontext().prec == 50
    finally:
        decimal.getcontext().prec = 50


def test_invocation_error_is_an_exception():
    assert issubclass(InvocationError, Exception)


# -- measure_invocation ------------------------------------------------------

def test_measure_invocation_empty_list_has_no_classes_and_no_warning():
    assert measure_invocation([]) == {
        'per_class': {}, 'total_n': 0, 'unobservable_n': 0,
        'cross_class_warning': None}


def test_measure_invocation_one_class_counts_invoked_and_not_invoked():
    r = measure_invocation([item(True), item(True), item(False)])
    assert r['per_class'] == {EV_2: {
        'evidence_class': EV_2, 'n': 3, 'invoked': 2, 'not_invoked': 1,
        'unobservable': 0, 'failure_rate': '1/3 (33.3%)'}}
    assert r['total_n'] == 3
    assert r['unobservable_n'] == 0
    assert r['cross_class_warning'] is None


@pytest.mark.req('R2.3')
def test_measure_invocation_reports_each_evidence_class_separately():
    r = measure_invocation([item(True, EV_2), item(False, EV_1),
                            item(True, EV_1), item(True, EV_3)])
    assert list(r['per_class']) == [EV_1, EV_2, EV_3]
    assert r['per_class'][EV_1]['n'] == 2
    assert r['per_class'][EV_1]['not_invoked'] == 1
    assert r['per_class'][EV_2]['n'] == 1
    assert r['per_class'][EV_3]['invoked'] == 1


@pytest.mark.req('R2.3')
def test_measure_invocation_two_classes_warn_not_comparable_in_sorted_order():
    r = measure_invocation([item(True, EV_2), item(False, EV_0)])
    assert r['cross_class_warning'] == (
        'aggregate spans 2 evidence classes '
        '(EV-0 UNOBSERVABLE, EV-2 PLATFORM-STRUCTURAL); '
        'figures are not comparable across classes')


def test_measure_invocation_three_classes_warning_counts_three():
    r = measure_invocation([item(True, EV_3), item(True, EV_1),
                            item(True, EV_2)])
    assert r['cross_class_warning'].startswith(
        'aggregate spans 3 evidence classes (EV-1 SELF-REPORTED, '
        'EV-2 PLATFORM-STRUCTURAL, EV-3 EXTERNALLY-VERIFIABLE); ')


def test_measure_invocation_counts_none_and_missing_invoked_as_unobservable():
    no_key = {'item_id': 'Q02', 'condition': 'base', 'evidence_class': EV_0}
    r = measure_invocation([item(None, EV_0), no_key, item(True)])
    assert r['unobservable_n'] == 2
    assert r['per_class'][EV_0]['unobservable'] == 2
    assert r['total_n'] == 3


def test_measure_invocation_missing_evidence_class_raises_key_error():
    with pytest.raises(KeyError):
        measure_invocation([{'item_id': 'Q01', 'invoked': True}])


@pytest.mark.finding('T3-1')
def test_measure_invocation_unobservable_items_count_in_n_but_not_as_failures():
    # Correct: an unobservable (EV-0, invoked None) execution is neither a
    # success nor a failure; it should stay out of the rate's n, or the
    # rate should be reported as unmeasured. Today it enters n, so two
    # unobservable items print as "0/2 failures" with a bound.
    r = measure_invocation([item(None, EV_0), item(None, EV_0)])
    summary = r['per_class'][EV_0]
    assert summary['n'] == 2
    assert summary['invoked'] == 0
    assert summary['unobservable'] == 2
    assert summary['failure_rate'].startswith('0/2 failures;')


@pytest.mark.finding('T3-1')
def test_measure_invocation_unobservable_mixed_into_class_dilutes_rate():
    # Correct: one failure in one observed execution is 1/1; the
    # unobservable execution in the same class makes it 1/2.
    r = measure_invocation([item(False, EV_2), item(None, EV_2)])
    assert r['per_class'][EV_2]['failure_rate'] == '1/2 (50.0%)'


# -- _summarise_class --------------------------------------------------------

def test_summarise_class_truthy_non_bool_invoked_is_in_no_bucket():
    # 'invoked' must be exactly True, False or None; 1 or 'yes' counts in n only.
    s = _summarise_class([{'invoked': 1}, {'invoked': 0}], EV_2)
    assert (s['n'], s['invoked'], s['not_invoked'], s['unobservable']) == \
        (2, 0, 0, 0)
    assert s['failure_rate'].startswith('0/2 failures;')


def test_summarise_class_all_not_invoked_reports_full_failure_rate():
    s = _summarise_class([{'invoked': False}] * 4, EV_1)
    assert s == {'evidence_class': EV_1, 'n': 4, 'invoked': 0,
                 'not_invoked': 4, 'unobservable': 0,
                 'failure_rate': '4/4 (100.0%)'}


# -- format_rate -------------------------------------------------------------

def test_format_rate_zero_n_is_no_observations():
    assert format_rate(0, 0) == 'no observations'


def test_format_rate_zero_n_with_failures_is_no_observations():
    assert format_rate(3, 0) == 'no observations'


@pytest.mark.req('R2.3')
def test_format_rate_zero_failures_n1_states_95_percent_bound():
    assert format_rate(0, 1) == (
        '0/1 failures; one-sided 95% upper bound on the failure rate 95.0%')


@pytest.mark.req('R2.3')
def test_format_rate_zero_failures_below_30_omits_rule_of_three():
    assert format_rate(0, 29) == (
        '0/29 failures; one-sided 95% upper bound on the failure rate 9.8%')


@pytest.mark.req('R2.3')
def test_format_rate_zero_failures_at_30_adds_rule_of_three():
    assert format_rate(0, 30) == (
        '0/30 failures; one-sided 95% upper bound on the failure rate 9.5%'
        ' (≈3/30=10.0%)')


@pytest.mark.req('R2.3')
def test_format_rate_zero_failures_never_prints_100_percent():
    for n in range(1, 201):
        text = format_rate(0, n)
        assert '100%' not in text
        assert 'upper bound' in text


@pytest.mark.req('R2.3')
def test_format_rate_zero_failures_n100_states_3_percent_bound():
    assert format_rate(0, 100) == (
        '0/100 failures; one-sided 95% upper bound on the failure rate 3.0%'
        ' (≈3/100=3.0%)')


@pytest.mark.finding('T3-61')
def test_format_rate_bound_rounds_half_even_down_at_n49():
    # The exact bound at n = 49 is 5.93 %. Correct: an upper bound is
    # rounded up (6.0 %); today it is rounded to nearest, 5.9 %.
    assert format_rate(0, 49) == (
        '0/49 failures; one-sided 95% upper bound on the failure rate 5.9%'
        ' (≈3/49=6.1%)')


@pytest.mark.finding('T3-61')
def test_format_rate_bound_for_large_n_prints_zero_percent():
    # The exact bound at n = 6000 is about 0.0499 %. Rounded to nearest
    # it prints as 0.0 %, i.e. a zero failure rate, which the bound is
    # there to prevent. Correct: round up, or show more digits.
    assert format_rate(0, 6000) == (
        '0/6000 failures; one-sided 95% upper bound on the failure rate 0.0%'
        ' (≈3/6000=0.0%)')


@pytest.mark.finding('T3-11')
def test_format_rate_treats_n_as_independent_trials():
    # The live D7.1 figure pools 50 repeats of 10 questions as n = 500 and
    # gets 0.6 %. Correct (AP-1 v1.3 D7.1, GH-5): the bound is per
    # question (or per item over its repeats), e.g. n = 10 gives 25.9 %.
    # format_rate has no notion of items; the pooling is the caller's.
    assert format_rate(0, 500).endswith('failure rate 0.6% (≈3/500=0.6%)')
    assert format_rate(0, 10).endswith('failure rate 25.9%')


def test_format_rate_nonzero_failures_prints_count_and_percent():
    assert format_rate(3, 50) == '3/50 (6.0%)'


def test_format_rate_nonzero_percent_rounds_half_even():
    # 1/16 = 6.25 %; the context rounding (half-even) gives 6.2 %.
    assert format_rate(1, 16) == '1/16 (6.2%)'


def test_format_rate_failures_above_n_are_not_refused():
    assert format_rate(5, 3) == '5/3 (166.7%)'


# -- _exact_upper_bound ------------------------------------------------------

@pytest.mark.req('R2.3')
def test_exact_upper_bound_n1_is_one_minus_alpha():
    assert _exact_upper_bound(1) == D('0.95')


@pytest.mark.req('R2.3')
def test_exact_upper_bound_n2_is_one_minus_root_alpha_at_precision_50():
    assert _exact_upper_bound(2) == \
        D('0.77639320225002103035908263312687237645593816403885')


def test_exact_upper_bound_uses_given_alpha():
    assert _exact_upper_bound(2, D('0.01')) == D('0.9')


def test_exact_upper_bound_is_in_open_unit_interval():
    for n in list(range(1, 201)) + [10_000]:
        assert D(0) < _exact_upper_bound(n) < D(1)


def test_exact_upper_bound_within_1pp_of_rule_of_three_from_n30():
    for n in range(30, 201):
        assert abs(_exact_upper_bound(n) * 100 - D(300) / D(n)) <= D('1.0')


# -- compute_dpr -------------------------------------------------------------

@pytest.mark.req('R2.3')
def test_compute_dpr_no_base_observations_is_undefined():
    assert compute_dpr(10, 0, 0, 50) == \
        (None, 'UNDEFINED (no base observations)')


@pytest.mark.req('R2.3')
def test_compute_dpr_zero_base_rate_is_undefined_never_one():
    assert compute_dpr(0, 0, 50, 50) == \
        (None, 'UNDEFINED (zero base invocation rate)')


def test_compute_dpr_relative_drop_in_rate():
    value, text = compute_dpr(45, 10, 50, 50)
    assert value == (D('0.9') - D('0.2')) / D('0.9')
    assert text == '77.8%'


def test_compute_dpr_uses_rates_not_counts():
    # base 1/3, removed 0/1: (1/3 - 0) / (1/3) = 1.
    assert compute_dpr(1, 0, 3, 1) == (D(1), '100.0%')
    # base 2/4, removed 1/1: (0.5 - 1) / 0.5 = -1.
    assert compute_dpr(2, 1, 4, 1) == (D(-1), '-100.0%')


def test_compute_dpr_equal_rates_is_zero():
    assert compute_dpr(10, 10, 10, 10) == (D(0), '0.0%')


def test_compute_dpr_removed_above_base_is_negative():
    assert compute_dpr(5, 10, 10, 10) == (D(-1), '-100.0%')


@pytest.mark.finding('S3-G4-1')
def test_compute_dpr_no_removed_observations_reports_full_drop():
    # Correct: with no observations in the removed arm, DPR is
    # UNDEFINED like the zero-base case. Today the removed rate is taken
    # as 0 and DPR is reported as 100.0 %, a full drop measured on no data.
    assert compute_dpr(10, 5, 10, 0) == (D(1), '100.0%')


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-61')
@pytest.mark.req('AP-1 D7.5', 'R2.3', 'R0.4.1')
@pytest.mark.parametrize('n', [49, 6000])
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-61: the displayed upper bound is rounded to '
                          'nearest (half-even), not up')
def test_format_rate_displayed_bound_is_never_below_the_exact_bound(n):
    # An upper bound rounded down is no longer an upper bound. Exact at
    # n = 49: 5.9306 %, shown 5.9 %; at n = 6000: 0.0499 %, shown 0.0 %.
    # Correct: rounded up at whatever precision is shown (6.0 %, 0.1 %).
    text = format_rate(0, n)
    shown = D(re.search(r'failure rate (\d+(?:\.\d+)?)%', text).group(1))
    assert shown >= _exact_upper_bound(n) * 100, text

# Group g3-seal-guards; see inbox/2026-10-20_step4-g3-seal-guards-report.md.

@pytest.mark.finding('S3-G4-1')
@pytest.mark.req('R2.3', 'AP-1 D7.8')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G4-1: no removed-arm observations taken as a '
                          'removed rate of 0, DPR 100.0%')
def test_compute_dpr_no_removed_observations_undefined():
    # Correct: DPR = (I_base - I_removed) / I_base needs both rates (SPEC
    # R2.3 l.546-547). With no observations in the removed arm, I_removed
    # is unknown, so DPR is UNDEFINED like the zero-base case, never a
    # full drop. Today the removed rate is taken as 0: (D(1), '100.0%').
    value, text = compute_dpr(10, 5, 10, 0)
    assert value is None
    assert text.startswith('UNDEFINED')
