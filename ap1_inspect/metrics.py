"""AP-1 Custom Metrics.

Clopper-Pearson exact binomial confidence bound for the zero-failure
case. This is the runner's existing formula, exposed as an Inspect metric.
"""

import math

from inspect_ai.scorer import Metric, Score, metric, CORRECT


@metric
def clopper_pearson_zero_bound(alpha: float = 0.05):
    """Exact Clopper-Pearson upper bound for k=0 failures.

    For n observations with 0 failures:
        upper_bound = 1 - alpha^(1/n)

    This is used in AP-1 D7.1b to bound the failure rate.
    """
    def compute(scores: list[Score]) -> float:
        n = len([s for s in scores if s.value is not None])
        if n == 0:
            return float('nan')
        # k=0 failures: upper bound = 1 - alpha^(1/n)
        return 1.0 - math.pow(alpha, 1.0 / n)

    return compute


@metric
def invocation_rate():
    """Proportion of samples where invocation_outcome == 'INVOKED'."""
    def compute(scores: list[Score]) -> float:
        scored = [s for s in scores if s.value is not None]
        if not scored:
            return float('nan')
        invoked = sum(
            1 for s in scored
            if s.metadata and s.metadata.get('invocation_outcome') == 'INVOKED'
        )
        return invoked / len(scored)

    return compute
