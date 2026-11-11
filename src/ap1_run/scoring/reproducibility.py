"""R2.2 -- D2 Reproducibility.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.2.

Classify the mechanism per surface, not merely count distinct answers.

Four mechanism classes: STRUCTURAL, CONFIGURED, OBSERVED-ONLY, UNMEASURED.
Classified PER SURFACE (figures vs prose), not per system.

STRUCTURAL and CONFIGURED are operator-declared and marked as such.
The runner can distinguish OBSERVED-ONLY from UNMEASURED from evidence;
it CANNOT establish STRUCTURAL or CONFIGURED from outside the system.

Parameter-echo verification: where the endpoint echoes applied parameters,
diff requested vs applied. A silently ignored parameter is a platform finding.
"""

from decimal import Decimal
from fractions import Fraction

from ap1_run.foundation.numeric import (
    AmbiguousLocaleError, extract_numeric_tokens,
)


# -- Mechanism class constants ---------------------------------------------

STRUCTURAL = 'STRUCTURAL'
CONFIGURED = 'CONFIGURED'
OBSERVED_ONLY = 'OBSERVED-ONLY'
UNMEASURED = 'UNMEASURED'

VALID_CLASSES = frozenset({STRUCTURAL, CONFIGURED, OBSERVED_ONLY, UNMEASURED})

# The surfaces a mechanism is classified on.
SURFACES = ('figures', 'prose')

# What is left out of the D2 comparison, by kind: replies that carry no
# answer to compare (errors, EV-0) and replies that cannot be read.
LEFT_OUT_KINDS = ('errored', 'EV-0', 'unreadable')


class ReproducibilityError(Exception):
    """Reproducibility classification failure."""


def classify_mechanism(responses, *, surface, minimum_runs,
                       operator_declared=None, figures=None,
                       evidence=None, errored=0):
    """Classify the reproducibility mechanism for a surface.

    Args:
        responses: list of dicts -- successful (non-error, non-rate-limited)
            responses for this item+condition on this surface.
        surface: str -- 'figures' or 'prose'
        minimum_runs: int -- minimum successful runs required
        operator_declared: str or None -- if the operator declares
            STRUCTURAL or CONFIGURED, this is that declaration.
        figures: list or None -- each response's answer figure (Decimal,
            or None where the answer is unresolved; see
            runner/executions.py d2_answer_figure). When given, the
            figures surface is that figure (AP-1 D2 "distinct numeric
            answers"; T3-4), compared exactly. An unresolved answer is
            not a value: it is counted ('unresolved'), and a cell with
            any is never classified on agreement it did not show. Two or
            more identified values are variation, reported as at least
            that many; otherwise the cell is UNMEASURED, stability not
            established. When not given, the figures the text states.
        evidence: list or None -- each response's evidence class
            (execution/evidence.py), beside responses.
        errored: int -- executions of this item+condition that errored
            and are not among responses (a failed request: rate limited,
            a transport error, an empty response, or interrupted).

    Only replies that carry an answer are compared. A response that is
    an error or rate limited, one at evidence class EV-0 (no record of
    what happened, for example a tool loop whose rounds cannot be read),
    or one of a shape that cannot be read (SPEC R2.0 step 0) is not a
    run on either surface. How many were left out, by kind, is in
    'left_out' and in the reason.

    Returns:
        dict with keys:
            mechanism: one of the four mechanism class constants
            operator_declared: bool -- True if class came from operator
            distinct_values: int or None
            successful_runs: int
            left_out: dict -- {kind: count} of the responses left out
                ('errored', 'EV-0', 'unreadable'), only kinds with any;
                absent if none was
            reason: str

    Raises:
        ReproducibilityError: surface is not one of SURFACES.
    """
    if surface not in SURFACES:
        raise ReproducibilityError(
            f'unknown surface {surface!r}; expected one of {SURFACES}')

    runs, left_out = _runs(responses, surface, figures, evidence, errored)
    successful = [responses[i] for i in runs]
    n_successful = len(successful)
    note = f' ({_left_out_text(left_out)} left out)' if left_out else ''
    result = _classify(successful, runs, n_successful, note, surface=surface,
                       minimum_runs=minimum_runs,
                       operator_declared=operator_declared, figures=figures)
    if left_out:
        result['left_out'] = left_out
    return result


def _left_out_text(left_out):
    """'1 errored, 2 EV-0': the left-out counts, in LEFT_OUT_KINDS order."""
    return ', '.join(f'{left_out[k]} {k}' for k in LEFT_OUT_KINDS
                     if left_out.get(k))


def _classify(successful, runs, n_successful, note, *, surface,
              minimum_runs, operator_declared, figures):
    """classify_mechanism's class of the runs left after _runs."""
    # Below minimum: UNMEASURED, never "stable" or "1 distinct answer"
    if n_successful < minimum_runs:
        return {
            'mechanism': UNMEASURED,
            'operator_declared': False,
            'distinct_values': None,
            'successful_runs': n_successful,
            'reason': (f'{n_successful} successful runs below minimum '
                       f'{minimum_runs}{note} — UNMEASURED'),
        }

    # No observations (reachable with minimum_runs 0): nothing is known
    # about the mechanism
    if n_successful == 0:
        return {
            'mechanism': UNMEASURED,
            'operator_declared': False,
            'distinct_values': None,
            'successful_runs': 0,
            'reason': f'0 successful runs{note} — UNMEASURED',
        }

    # Extract the surface values
    unresolved = 0
    if surface == 'figures' and figures is not None:
        values = [_answer_key(figures[i]) for i in runs
                  if figures[i] is not None]
        unresolved = n_successful - len(values)
    else:
        values = _extract_surface_values(successful, surface)
    distinct = len(set(values))

    # Unresolved answers (pending adjudication) are not values: they
    # never count as agreement, and identified values that already
    # differ are variation, at least that much (AP-1 D2; T3-4)
    if unresolved and operator_declared not in (STRUCTURAL, CONFIGURED):
        pending = (f'{unresolved} of {n_successful} runs have no '
                   f'identified answer (pending adjudication)')
        if distinct >= 2:
            return {
                'mechanism': OBSERVED_ONLY,
                'operator_declared': False,
                'distinct_values': distinct,
                'unresolved': unresolved,
                'successful_runs': n_successful,
                'reason': (f'{n_successful} runs, at least {distinct} '
                           f'distinct values; {pending}{note} '
                           f'— OBSERVED-ONLY'),
            }
        return {
            'mechanism': UNMEASURED,
            'operator_declared': False,
            'distinct_values': None,
            'unresolved': unresolved,
            'successful_runs': n_successful,
            'reason': (f'{pending}{note}; stability not established '
                       f'— UNMEASURED'),
        }

    # If operator declares STRUCTURAL or CONFIGURED, mark it
    if operator_declared in (STRUCTURAL, CONFIGURED):
        return {
            'mechanism': operator_declared,
            'operator_declared': True,
            'distinct_values': distinct,
            'successful_runs': n_successful,
            'reason': f'operator-declared {operator_declared} for {surface}',
        }

    # Runner can only determine OBSERVED-ONLY from evidence
    if distinct == 1:
        return {
            'mechanism': OBSERVED_ONLY,
            'operator_declared': False,
            'distinct_values': 1,
            'successful_runs': n_successful,
            'reason': f'{n_successful} runs, 1 distinct value — OBSERVED-ONLY',
        }
    else:
        return {
            'mechanism': OBSERVED_ONLY,
            'operator_declared': False,
            'distinct_values': distinct,
            'successful_runs': n_successful,
            'reason': (f'{n_successful} runs, {distinct} distinct values '
                       f'— OBSERVED-ONLY'),
        }


def check_parameter_echo(requested_params, echoed_params):
    """Diff requested vs echoed parameters (AP-1 v1.3 D2.2).

    Where the endpoint echoes applied parameters, a parameter requested
    and silently ignored is a PLATFORM FINDING. A parameter the endpoint
    does not echo was not shown ignored: it is unverified, not a finding.
    Numbers compare as numbers, exactly (0 requested, 0.0 echoed is the
    same temperature; S3-G5-4); anything else compares as text.

    Args:
        requested_params: dict of requested parameter values
        echoed_params: dict of echoed parameter values, or None if
            the endpoint does not echo.

    Returns:
        dict with keys:
            verified: bool -- True if every parameter was echoed and matches
            findings: list of str -- platform findings
            status: 'VERIFIED' (all echoed and matching) / 'MISMATCH'
                (any echoed value differs) / 'UNVERIFIED' otherwise
            not_echoed: list of str -- requested parameters not echoed
    """
    echoed_params = echoed_params or {}
    findings, not_echoed = [], []
    for param, requested_val in requested_params.items():
        echoed_val = echoed_params.get(param)
        if echoed_val is None:
            not_echoed.append(param)
        elif not _same_value(requested_val, echoed_val):
            findings.append(
                f'parameter {param!r}: requested={requested_val!r}, '
                f'applied={echoed_val!r} — silently ignored')
    if findings:
        status = 'MISMATCH'
    elif not_echoed:
        status = 'UNVERIFIED'
    else:
        status = 'VERIFIED'
    return {'verified': status == 'VERIFIED', 'findings': findings,
            'status': status, 'not_echoed': not_echoed}


def _same_value(requested, echoed):
    """True if an echoed parameter is the value that was sent: the same
    text, or a number equal to the request's wire value (adapter.
    wire_value: an integer, or the float sent), compared exactly as
    Decimals of their text. So '1' sent as 1 and echoed 1.0 is applied,
    and so is '0.10' sent and echoed as 0.1."""
    if str(requested) == str(echoed):
        return True
    if isinstance(requested, bool) or isinstance(echoed, bool):
        return False
    from ap1_run.foundation.adapter import AdapterError, wire_value
    try:
        sent = wire_value('', requested)
        return Decimal(repr(sent)) == Decimal(str(echoed))
    except (AdapterError, ArithmeticError, ValueError, TypeError):
        return False


def _is_error_or_limited(response):
    """True if response is an error or rate-limited response."""
    if not isinstance(response, dict):
        return True
    # HTTP error
    if response.get('error'):
        return True
    # Rate limited (HTTP 429)
    if response.get('status_code') == 429:
        return True
    # Explicit flag
    if response.get('rate_limited'):
        return True
    return False


def _extract_surface_values(responses, surface):
    """Extract the surface-specific values from responses.

    For 'prose': the full text content.
    For 'figures': the numeric figures the text states (AP-1 D2 Method:
    "distinct numeric answers per question"; SPEC R2.2 "separately for
    computed figures and for surrounding prose"; T3-4): the set of its
    numeric tokens (value and percent flag, R0.4.2), so the same figure
    worded twice is one value. A text whose numbers cannot be read is
    its own value.
    """
    # A response whose shape cannot be read (S3-G2-1) has no surface
    # value, as one without choices.
    from ap1_run.execution.evidence import _read_message
    values = []
    for r in responses:
        msg = _read_message(r)[0] or {}
        text = msg.get('content', '') or ''
        if surface == 'figures':
            values.append(_figures(text))
        elif surface == 'prose':
            values.append(text)
    return values


def _answer_key(figure):
    """An answer figure's identity: its exact value, whatever the Decimal
    context."""
    return Fraction(figure)


def _runs(responses, surface, figures, evidence=None, errored=0):
    """The indices of the responses that are runs on this surface, and
    {kind: count} of those left out (only kinds with any): an error or
    rate-limited response and the errored executions not among the
    responses ('errored'), a response at evidence class EV-0 ('EV-0'),
    and one whose shape cannot be read (SPEC R2.0 step 0; 'unreadable').
    """
    from ap1_run.execution.evidence import EV_0, _read_message
    runs = []
    left_out = {'errored': errored, 'EV-0': 0, 'unreadable': 0}
    for i, r in enumerate(responses):
        if _is_error_or_limited(r):
            left_out['errored'] += 1
            continue
        if evidence is not None and evidence[i] == EV_0:
            left_out['EV-0'] += 1
            continue
        if _read_message(r)[0] is None:
            left_out['unreadable'] += 1
            continue
        runs.append(i)
    return runs, {k: v for k, v in left_out.items() if v}


def distinct_figures_shown(responses, figures=None, evidence=None):
    """Each distinct figures value of the successful responses (told
    apart as classify_mechanism tells them), as the first response to
    give it states it: the figures in text order, each value as written
    in Decimal ('2600.00', with '%' for a percent), joined by ', ';
    'no figures' for a text without one, 'unreadable' for one extraction
    refuses. First seen first (AP-1 D2 "distinct numeric answers per
    question"; T3-4). With figures (classify_mechanism), each distinct
    identified answer of the runs, as written; unresolved answers are
    not values (classify_mechanism counts them). With evidence, a
    response at EV-0 is left out, as classify_mechanism leaves it out."""
    from ap1_run.execution.evidence import EV_0, _read_message
    if figures is not None:
        runs, _ = _runs(responses, 'figures', figures, evidence)
        shown = {}
        for i in runs:
            if figures[i] is not None:
                shown.setdefault(_answer_key(figures[i]), str(figures[i]))
        return list(shown.values())
    shown = {}
    for i, r in enumerate(responses):
        if _is_error_or_limited(r):
            continue
        if evidence is not None and evidence[i] == EV_0:
            continue
        text = (_read_message(r)[0] or {}).get('content', '') or ''
        key = _figures(text)
        if key in shown:
            continue
        if key and key[0] == 'unreadable':
            shown[key] = 'unreadable'
            continue
        figures, seen = [], set()
        for t in extract_numeric_tokens(text):
            k = (Fraction(t.value), t.percent)
            if k not in seen:
                seen.add(k)
                figures.append(f'{t.value}{"%" if t.percent else ""}')
        shown[key] = ', '.join(figures) or 'no figures'
    return list(shown.values())


def _figures(text):
    """The numeric figures a text states, as a sorted tuple of
    (value, percent) pairs, each value exact and independent of the
    Decimal context (15.2 and 15.20 are one figure, 15.20 and 15.21 two);
    ('unreadable', text) if extraction refuses the text."""
    try:
        tokens = extract_numeric_tokens(text)
    except (AmbiguousLocaleError, ArithmeticError, ValueError):
        return ('unreadable', text)
    return tuple(sorted({(Fraction(t.value), t.percent)
                         for t in tokens}))
