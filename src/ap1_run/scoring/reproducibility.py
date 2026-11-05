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


# -- Mechanism class constants ---------------------------------------------

STRUCTURAL = 'STRUCTURAL'
CONFIGURED = 'CONFIGURED'
OBSERVED_ONLY = 'OBSERVED-ONLY'
UNMEASURED = 'UNMEASURED'

VALID_CLASSES = frozenset({STRUCTURAL, CONFIGURED, OBSERVED_ONLY, UNMEASURED})

# The surfaces a mechanism is classified on.
SURFACES = ('figures', 'prose')


class ReproducibilityError(Exception):
    """Reproducibility classification failure."""


def classify_mechanism(responses, *, surface, minimum_runs,
                       operator_declared=None):
    """Classify the reproducibility mechanism for a surface.

    Args:
        responses: list of dicts -- successful (non-error, non-rate-limited)
            responses for this item+condition on this surface.
        surface: str -- 'figures' or 'prose'
        minimum_runs: int -- minimum successful runs required
        operator_declared: str or None -- if the operator declares
            STRUCTURAL or CONFIGURED, this is that declaration.

    Returns:
        dict with keys:
            mechanism: one of the four mechanism class constants
            operator_declared: bool -- True if class came from operator
            distinct_values: int or None
            successful_runs: int
            reason: str

    Raises:
        ReproducibilityError: surface is not one of SURFACES.
    """
    if surface not in SURFACES:
        raise ReproducibilityError(
            f'unknown surface {surface!r}; expected one of {SURFACES}')

    successful = [r for r in responses if not _is_error_or_limited(r)]
    n_successful = len(successful)

    # Below minimum: UNMEASURED, never "stable" or "1 distinct answer"
    if n_successful < minimum_runs:
        return {
            'mechanism': UNMEASURED,
            'operator_declared': False,
            'distinct_values': None,
            'successful_runs': n_successful,
            'reason': (f'{n_successful} successful runs below minimum '
                       f'{minimum_runs} — UNMEASURED'),
        }

    # No observations (reachable with minimum_runs 0): nothing is known
    # about the mechanism
    if n_successful == 0:
        return {
            'mechanism': UNMEASURED,
            'operator_declared': False,
            'distinct_values': None,
            'successful_runs': 0,
            'reason': '0 successful runs — UNMEASURED',
        }

    # Extract the surface values
    values = _extract_surface_values(successful, surface)
    distinct = len(set(values))

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

    For 'figures': extract the numeric content (the released figure).
    For 'prose': extract the full text content.
    """
    values = []
    for r in responses:
        if surface == 'figures':
            # The figure value, normalised to string for comparison
            choices = r.get('choices', [])
            if choices:
                msg = choices[0].get('message', {})
                tool_calls = msg.get('tool_calls') or []
                if tool_calls:
                    # Use tool call arguments as the figure surface
                    val = str(tool_calls[0].get('function', {}).get('arguments', ''))
                else:
                    val = msg.get('content', '') or ''
            else:
                val = ''
            values.append(val)
        elif surface == 'prose':
            choices = r.get('choices', [])
            if choices:
                val = choices[0].get('message', {}).get('content', '') or ''
            else:
                val = ''
            values.append(val)
    return values