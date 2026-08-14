"""R2.3 -- D7.1 Invocation.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.3.

Per item and condition, was the required computation invoked -- and on
what class of evidence.

Every outcome carries its R1.3.1 evidence class.

Zero failures in n: "0/n; upper bound ~= 3/n". In this module, a zero-failure rate is reported with its
Clopper-Pearson bound rather than as a bare "100%".

DPR = (I_base - I_removed) / I_base. Where I_base is zero the ratio
is UNDEFINED, never 1.0.

Aggregate spanning two evidence classes reports per class with a
statement that the figures are not comparable.
"""

import math
from decimal import Decimal, getcontext

from evidence import EV_0, EV_1, EV_2, EV_3

# Ensure sufficient precision for Decimal exponentiation
getcontext().prec = 50


class InvocationError(Exception):
    """Invocation measurement failure."""


def measure_invocation(items_results):
    """Measure invocation rates across items.

    Args:
        items_results: list of dicts, each with:
            item_id: str
            condition: str ('base' or 'removed')
            invoked: bool or None (None = unobservable)
            evidence_class: str (EV_0, EV_1, EV_2, EV_3)

    Returns:
        dict with keys:
            per_class: dict of evidence_class -> class_summary
            total_n: int
            unobservable_n: int
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

    # Cross-class warning
    classes_with_findings = [ec for ec in per_class
                            if per_class[ec]['n'] > 0]
    warning = None
    if len(classes_with_findings) > 1:
        warning = (
            f'aggregate spans {len(classes_with_findings)} evidence classes '
            f'({", ".join(classes_with_findings)}); '
            f'figures are not comparable across classes')

    return {
        'per_class': per_class,
        'total_n': len(items_results),
        'unobservable_n': sum(1 for r in items_results
                              if r.get('invoked') is None),
        'cross_class_warning': warning,
    }


def _summarise_class(items, evidence_class):
    """Summarise invocation for items of a single evidence class."""
    n = len(items)
    invoked = sum(1 for r in items if r.get('invoked') is True)
    not_invoked = sum(1 for r in items if r.get('invoked') is False)
    unobservable = sum(1 for r in items if r.get('invoked') is None)

    failures = not_invoked
    summary = format_rate(failures, n)

    return {
        'evidence_class': evidence_class,
        'n': n,
        'invoked': invoked,
        'not_invoked': not_invoked,
        'unobservable': unobservable,
        'failure_rate': summary,
    }


def format_rate(failures, n):
    """Format a failure rate. Reports zero-failure rates with their Clopper-Pearson bound.

    Zero failures: exact one-sided 95% Clopper-Pearson upper bound.
      p_upper = 1 - alpha^(1/n)  with alpha = 0.05
    This is exact at every n.  For n >= 30 the 3/n approximation
    is noted in parentheses; below n=30 it is omitted (misleading).

    Non-zero failures: "k/n (X.X%)"
    """
    if n == 0:
        return 'no observations'

    if failures == 0:
        bound = _exact_upper_bound(n)
        bound_pct = (bound * 100).quantize(Decimal('0.1'))
        text = f'0/{n} failures; one-sided 95% upper bound on the failure rate {bound_pct}%'
        if n >= 30:
            approx = (Decimal(3) / Decimal(n) * 100).quantize(Decimal('0.1'))
            text += f' (\u22483/{n}={approx}%)'
        return text

    rate = Decimal(failures) / Decimal(n)
    pct = (rate * 100).quantize(Decimal('0.1'))
    return f'{failures}/{n} ({pct}%)'


def _exact_upper_bound(n, alpha=None):
    """Exact Clopper-Pearson upper bound for zero failures in n trials.

    p_upper = 1 - alpha^(1/n)

    Computed in Decimal at the context's precision.  The result is
    always in (0, 1) for any positive n.
    """
    if alpha is None:
        alpha = Decimal('0.05')
    exponent = Decimal(1) / Decimal(n)
    return 1 - alpha ** exponent


def compute_dpr(invoked_base, invoked_removed, n_base, n_removed):
    """Compute Drop-in-Performance Ratio.

    DPR = (I_base - I_removed) / I_base

    Where I_base is zero, DPR is UNDEFINED, never 1.0.

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

    rate_base = Decimal(invoked_base) / Decimal(n_base)

    if rate_base == 0:
        return None, 'UNDEFINED (zero base invocation rate)'

    rate_removed = Decimal(invoked_removed) / Decimal(n_removed) \
        if n_removed > 0 else Decimal(0)

    dpr = (rate_base - rate_removed) / rate_base
    pct = (dpr * 100).quantize(Decimal('0.1'))
    return dpr, f'{pct}%'