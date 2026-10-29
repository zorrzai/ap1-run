"""ap1_inspect/metrics.py: the custom Inspect metrics. (Not attached to the
scorer today: S3-G7-3.)"""

import math

import pytest

pytest.importorskip('inspect_ai')

from inspect_ai.scorer import Score  # noqa: E402

from ap1_inspect.metrics import clopper_pearson_zero_bound, invocation_rate  # noqa: E402


def test_zero_failure_bound_over_scored_samples():
    compute = clopper_pearson_zero_bound()
    assert compute([Score(value='C')] * 20) == 1.0 - math.pow(0.05, 1 / 20)


def test_zero_failure_bound_of_no_samples_is_nan():
    assert math.isnan(clopper_pearson_zero_bound()([]))


@pytest.mark.finding('T3-43')
def test_zero_failure_bound_ignores_failures():
    # Every sample INCORRECT still gives the k=0 bound for n=2. Correct:
    # the bound for the observed failures, or none.
    assert clopper_pearson_zero_bound()([Score(value='I'), Score(value='I')]) \
        == 1.0 - math.pow(0.05, 1 / 2)


@pytest.mark.finding('T3-43', 'T3-1')
def test_invocation_rate_counts_unobservable_as_not_invoked():
    # An EV-0 sample (invocation_outcome None) is in the denominator as a
    # non-invocation. Correct: leave unobservable samples out.
    scores = [Score(value='C', metadata={'invocation_outcome': 'INVOKED'}),
              Score(value='C', metadata={'invocation_outcome': None})]
    assert invocation_rate()(scores) == 0.5


def test_invocation_rate_of_no_samples_is_nan():
    assert math.isnan(invocation_rate()([]))
