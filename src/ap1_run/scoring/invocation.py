"""R2.3 -- D7.1 Invocation.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.3.

Per item and condition, was the required computation invoked -- and on
what class of evidence.

Every outcome carries its R1.3.1 evidence class.

Every failure rate is reported with its exact one-sided 95%
Clopper-Pearson upper bound (AP-1 v1.3 D7.5), never as a bare "100%":
1 - alpha^(1/n) at zero failures, the 1 - alpha quantile of
Beta(k+1, n-k) for k > 0 (the general form DISPOSITION C-1 adopts). The
bound is computed in Decimal and displayed rounded up (T3-61, T3-81).

DPR = (I_base - I_removed) / I_base. Where I_base is zero the ratio
is UNDEFINED, never 1.0.

Aggregate spanning two evidence classes reports per class with a
statement that the figures are not comparable.
"""

import math
from decimal import ROUND_CEILING, Decimal, localcontext

from ap1_run.execution.evidence import EV_0, EV_1, EV_2, EV_3
from ap1_run.foundation.numeric import DECIMAL_CONTEXT


class InvocationError(Exception):
    """Invocation measurement failure."""


def measure_invocation(items_results):
    """Measure invocation rates across items.

    The unit of D7.1 is the computable question (AP-1 v1.3 D7.1 "on what
    proportion of computable questions", the D7.5 "49 items" example,
    DISPOSITION_RECORD GH-5): the repeats of a question are not
    independent trials, so n counts questions, not executions. A question
    is a failure if any of its observed repeats is NOT-INVOKED.

    Only INVOKED (invoked is True) and NOT-INVOKED (invoked is False) are
    observations. Anything else (None: UNOBSERVABLE, EV-0) is neither a
    success nor a failure and stays out of n (SPEC R2.3, R1.3.1).

    Args:
        items_results: list of dicts, one per execution, each with:
            item_id: str (a record without one is its own question)
            condition: str (not read: call once per condition)
            invoked: bool or None (None = unobservable)
            evidence_class: str (EV_0, EV_1, EV_2, EV_3)

    Returns:
        dict with keys:
            per_class: dict of evidence_class -> class_summary
            total_n: int -- executions
            unobservable_n: int -- executions with no observed outcome
            cross_class_warning: str or None
    """
    # Group by evidence class
    by_class = {}
    for r in items_results:
        ec = r['evidence_class']
        by_class.setdefault(ec, []).append(r)

    per_class = {}
    for ec, items in sorted(by_class.items()):
        per_class[ec] = _summarise_class(items, ec)

    # Cross-class warning: the executions span more than one class
    # (an EV-0 class included: it is reported beside the others, and
    # is not comparable with them).
    warning = None
    if len(per_class) > 1:
        warning = (
            f'aggregate spans {len(per_class)} evidence classes '
            f'({", ".join(per_class)}); '
            f'figures are not comparable across classes')

    return {
        'per_class': per_class,
        'total_n': len(items_results),
        'unobservable_n': sum(1 for r in items_results
                              if not _observed(r)),
        'cross_class_warning': warning,
    }


def _observed(record):
    """True if the execution has an observed outcome (INVOKED or
    NOT-INVOKED)."""
    return record.get('invoked') is True or record.get('invoked') is False


def _summarise_class(items, evidence_class):
    """Summarise invocation for the executions of one evidence class.

    n, invoked and not_invoked count questions with at least one observed
    repeat; a question is not_invoked if any observed repeat is.
    unobservable counts executions with no observed outcome.
    """
    questions = {}
    for i, r in enumerate(items):
        if not _observed(r):
            continue
        key = r['item_id'] if r.get('item_id') is not None else ('#', i)
        questions[key] = questions.get(key, True) and r['invoked']
    n = len(questions)
    not_invoked = sum(1 for ok in questions.values() if not ok)
    unobservable = sum(1 for r in items if not _observed(r))

    return {
        'evidence_class': evidence_class,
        'n': n,
        'invoked': n - not_invoked,
        'not_invoked': not_invoked,
        'unobservable': unobservable,
        'failure_rate': format_rate(not_invoked, n),
    }


def format_rate(failures, n):
    """Format a failure rate with its one-sided 95% upper bound.

    Zero failures: "0/n failures; one-sided 95% upper bound on the
    failure rate X%", with p_upper = 1 - alpha^(1/n), alpha = 0.05. For
    n >= 30 the 3/n approximation is noted in parentheses; below n = 30
    it is omitted (misleading).

    Non-zero failures: "k/n (X.X%); one-sided 95% upper bound on the
    failure rate Y%", the exact Clopper-Pearson bound.

    The bound is rounded up to 0.1%, so the figure shown is never below
    the exact bound (T3-61).
    """
    if n == 0:
        return 'no observations'
    with localcontext(DECIMAL_CONTEXT):
        return _format_rate(failures, n)



def _format_rate(failures, n):
    """format_rate's arithmetic, given n > 0."""
    bound_pct = round_up(clopper_pearson_upper(failures, n) * 100,
                         Decimal('0.1'))
    bound_text = f'one-sided 95% upper bound on the failure rate {bound_pct}%'
    if failures == 0:
        text = f'0/{n} failures; {bound_text}'
        if n >= 30:
            approx = (Decimal(3) / Decimal(n) * 100).quantize(Decimal('0.1'))
            text += f' (\u22483/{n}={approx}%)'
        return text

    rate = Decimal(failures) / Decimal(n)
    pct = (rate * 100).quantize(Decimal('0.1'))
    return f'{failures}/{n} ({pct}%); {bound_text}'


def round_up(value, quantum):
    """value rounded up (toward +infinity) to a multiple of quantum: how
    an upper bound is displayed, so that it stays an upper bound."""
    return value.quantize(quantum, rounding=ROUND_CEILING)


def clopper_pearson_upper(failures, n, alpha=None):
    """Exact one-sided upper confidence bound on a failure rate, as a
    Decimal: the p at which P(X <= failures; n, p) = alpha, i.e. the
    1 - alpha quantile of Beta(failures + 1, n - failures) (AP-1 v1.3
    D7.5; DISPOSITION C-1). alpha defaults to 0.05 (95%).

    failures = 0 is the closed form 1 - alpha^(1/n) (_exact_upper_bound).
    failures >= n gives 1. Otherwise the binomial distribution function
    is bisected in Decimal at precision 60, 135 times (a bracket of width
    2^-135, about 2e-41, far wider than the arithmetic's error); the upper
    end of the final bracket is returned, so the value is never below the
    exact bound.

    Raises InvocationError if n is not positive or failures is negative.
    """
    if alpha is None:
        alpha = Decimal('0.05')
    if n <= 0 or failures < 0:
        raise InvocationError(
            f'no bound for {failures} failures in n = {n}')
    if failures == 0:
        return _exact_upper_bound(n, alpha)
    if failures >= n:
        return Decimal(1)
    with localcontext() as ctx:
        ctx.prec = 60
        lo, hi = Decimal(0), Decimal(1)
        for _ in range(135):
            mid = (lo + hi) / 2
            if _binomial_cdf(failures, n, mid) > alpha:
                lo = mid
            else:
                hi = mid
        return hi


def _binomial_cdf(k, n, p):
    """P(X <= k) for X ~ Binomial(n, p), 0 < p < 1, in Decimal."""
    q = 1 - p
    term = q ** n
    total = term
    ratio = p / q
    for i in range(k):
        term = term * (n - i) / (i + 1) * ratio
        total += term
    return total


def _exact_upper_bound(n, alpha=None):
    """Exact Clopper-Pearson upper bound for zero failures in n trials.

    p_upper = 1 - alpha^(1/n)

    Computed in Decimal in DECIMAL_CONTEXT (precision 50).  The result
    is always in (0, 1) for any positive n.
    """
    if alpha is None:
        alpha = Decimal('0.05')
    with localcontext(DECIMAL_CONTEXT):
        exponent = Decimal(1) / Decimal(n)
        return 1 - alpha ** exponent


def compute_dpr(invoked_base, invoked_removed, n_base, n_removed):
    """Compute Drop-in-Performance Ratio.

    DPR = (I_base - I_removed) / I_base

    Where I_base is zero, DPR is UNDEFINED, never 1.0. Where either
    condition has no observations, DPR is UNDEFINED too (S3-G4-1).

    Args:
        invoked_base: int -- invocations in base condition
        invoked_removed: int -- invocations in removed condition
        n_base: int -- total items in base condition
        n_removed: int -- total items in removed condition

    Returns:
        (dpr_value, dpr_string)
        dpr_value: Decimal or None (None = UNDEFINED)
        dpr_string: str representation
    """
    if n_base == 0:
        return None, 'UNDEFINED (no base observations)'
    with localcontext(DECIMAL_CONTEXT):
        return _dpr(invoked_base, invoked_removed, n_base, n_removed)


def _dpr(invoked_base, invoked_removed, n_base, n_removed):
    """compute_dpr's arithmetic, given n_base > 0."""
    rate_base = Decimal(invoked_base) / Decimal(n_base)

    if rate_base == 0:
        return None, 'UNDEFINED (zero base invocation rate)'

    if n_removed == 0:
        return None, 'UNDEFINED (no instruction_removed observations)'
    rate_removed = Decimal(invoked_removed) / Decimal(n_removed)

    dpr = (rate_base - rate_removed) / rate_base
    pct = (dpr * 100).quantize(Decimal('0.1'))
    return dpr, f'{pct}%'