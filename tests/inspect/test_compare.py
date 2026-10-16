"""ap1_inspect/compare.py: the cross-condition D7.1 comparison over two
eval logs' score metadata. Needs no inspect-ai."""

import math

import pytest

from ap1_inspect.compare import compare_conditions


def scores(*outcomes):
    return [{'invocation_outcome': o} for o in outcomes]


def test_compare_reports_rates_and_excess_invocation():
    result = compare_conditions(scores('INVOKED', 'NOT-INVOKED'),
                                scores('INVOKED', 'INVOKED'))
    assert result['base'] == {'invoked': 1, 'total': 2, 'rate': 0.5,
                              'cp_bound': 1.0 - 0.05 ** 0.5}
    assert result['instruction_removed']['rate'] == 1.0
    assert result['rate_difference'] == 0.5
    assert result['finding'] == ('D7.1b: instruction-removed invocation rate '
                                 '(100.0%) exceeds base rate (50.0%)')


def test_compare_without_excess_says_so():
    result = compare_conditions(scores('INVOKED'), scores('NOT-INVOKED'))
    assert result['finding'] == \
        'D7.1b: no excess invocation under instruction removal'


def test_compare_of_empty_logs_is_nan():
    result = compare_conditions([], [])
    assert math.isnan(result['base']['rate'])
    assert math.isnan(result['base']['cp_bound'])
    assert result['finding'] == \
        'D7.1b: no excess invocation under instruction removal'


@pytest.mark.finding('T3-43')
def test_compare_prints_zero_failure_bound_whatever_the_failures():
    # cp_bound is 1 - alpha^(1/n), the bound for zero failures, even when
    # every item failed. Correct: the k>0 bound, or none.
    result = compare_conditions(scores('NOT-INVOKED', 'NOT-INVOKED'), [])
    assert result['base']['invoked'] == 0
    assert result['base']['cp_bound'] == 1.0 - 0.05 ** 0.5


@pytest.mark.finding('T3-43', 'T3-1')
def test_compare_counts_unobservable_as_not_invoked():
    # EV-0 scores carry invocation_outcome None; they count in the total
    # and as not invoked, the opposite of the runner's T3-1 (which counts
    # them as invoked). Correct: leave them out of the rate.
    result = compare_conditions(scores('INVOKED', None), [])
    assert (result['base']['invoked'], result['base']['total']) == (1, 2)
