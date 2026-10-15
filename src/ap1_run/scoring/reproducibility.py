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
    """
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
    """Diff requested vs echoed parameters.

    Where the endpoint echoes applied parameters, a parameter requested
    and silently ignored is a PLATFORM FINDING.

    Args:
        requested_params: dict of requested parameter values
        echoed_params: dict of echoed parameter values, or None if
            the endpoint does not echo.

    Returns:
        dict with keys:
            verified: bool -- True if all parameters match or no echo
            findings: list of str -- platform findings
            status: 'VERIFIED' / 'UNVERIFIED' / 'MISMATCH'
    """
    if echoed_params is None:
        return {
            'verified': False,
            'findings': [],
            'status': 'UNVERIFIED',
        }

    findings = []
    for param, requested_val in requested_params.items():
        echoed_val = echoed_params.get(param)
        if echoed_val is None:
            findings.append(
                f'parameter {param!r} requested but not echoed')
        elif str(echoed_val) != str(requested_val):
            findings.append(
                f'parameter {param!r}: requested={requested_val!r}, '
                f'applied={echoed_val!r} — silently ignored')

    if findings:
        return {
            'verified': False,
            'findings': findings,
            'status': 'MISMATCH',
        }

    return {
        'verified': True,
        'findings': [],
        'status': 'VERIFIED',
    }


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