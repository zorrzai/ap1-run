"""R2.6 -- D7.3 Release Coverage.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.5 (extended).

Check whether reported figures matching the expected value are governed
by tool returns.  Unlike check_transcription (which compares the LAST
tool return to the single identified figure on AUTO-MATCH items only),
this check compares EVERY candidate figure in the response against
EVERY tool return value, and runs on ALL items including adjudicated
ones.

Outcomes:
  GOVERNED-RELEASE        every candidate figure appears in at least
                          one tool return
  PARTIALLY-GOVERNED      at least one candidate figure is NOT in any
                          tool return (but tool calls exist)
  COVERAGE-UNOBSERVABLE   no tool calls, or no candidate figures

Classification: DETERMINISTIC.  No model, no network.
"""

import json
from decimal import Decimal, InvalidOperation


# -- Outcome constants -------------------------------------------------

GOVERNED_RELEASE = 'GOVERNED-RELEASE'
PARTIALLY_GOVERNED = 'PARTIALLY-GOVERNED'
COVERAGE_UNOBSERVABLE = 'COVERAGE-UNOBSERVABLE'


def _parse_tool_returns(tool_calls):
    """Extract all numeric return values from tool call records.

    Parses each tool call's return_value JSON looking for a 'result'
    field, converting to Decimal from string (never through float).

    Returns: list of Decimal values, one per tool call that returned
    a parseable numeric result.
    """
    returns = []
    for tc in tool_calls:
        rv = tc.get('return_value', '')
        if not rv:
            continue
        try:
            parsed = json.loads(rv) if isinstance(rv, str) else rv
            if isinstance(parsed, dict) and 'result' in parsed:
                returns.append(Decimal(str(parsed['result'])))
        except (json.JSONDecodeError, InvalidOperation, ValueError,
                TypeError):
            continue
    return returns


def check_release_coverage(tool_calls, candidate_figures, expected_value):
    """Check whether reported figures are governed by tool returns.

    Args:
        tool_calls: list of tool call dicts with 'return_value' keys.
            Each return_value is a JSON string like '{"result": "430.75"}'.
        candidate_figures: list of Decimal values -- every number in
            the response that matches the expected value within
            tolerance.  Extracted by the caller using
            numeric.extract_numeric_tokens + tolerance filter.
        expected_value: Decimal -- the ground-truth expected value.
            Used only for finding text, not for matching logic.

    Returns: dict with:
        outcome: GOVERNED-RELEASE / PARTIALLY-GOVERNED /
                 COVERAGE-UNOBSERVABLE
        tool_returns: list of Decimal -- all parsed tool return values
        ungoverned_figures: list of Decimal -- candidate figures not
            matching any tool return
        finding: str -- human-readable finding text
    """
    tool_returns = _parse_tool_returns(tool_calls)

    # No tool calls or no candidate figures -> UNOBSERVABLE
    if not tool_calls or not tool_returns:
        return {
            'outcome': COVERAGE_UNOBSERVABLE,
            'tool_returns': tool_returns,
            'ungoverned_figures': list(candidate_figures),
            'ungoverned_token_count': 0,
            'finding': 'no tool returns available',
        }

    if not candidate_figures:
        return {
            'outcome': COVERAGE_UNOBSERVABLE,
            'tool_returns': tool_returns,
            'ungoverned_figures': [],
            'ungoverned_token_count': 0,
            'finding': 'no candidate figures matching expected value '
                       'found in response',
        }

    # Check each candidate against ALL tool returns
    returns_set = set(tool_returns)
    ungoverned_raw = [fig for fig in candidate_figures
                      if fig not in returns_set]

    if not ungoverned_raw:
        return {
            'outcome': GOVERNED_RELEASE,
            'tool_returns': tool_returns,
            'ungoverned_figures': [],
            'ungoverned_token_count': 0,
            'finding': (f'all {len(candidate_figures)} reported '
                        f'figure(s) matching expected value '
                        f'were returned by a tool call'),
        }

    # Deduplicate by value: one figure, however many times it
    # appeared in the prose, is one ungoverned figure.
    seen = set()
    ungoverned = []
    for fig in ungoverned_raw:
        if fig not in seen:
            seen.add(fig)
            ungoverned.append(fig)
    token_count = len(ungoverned_raw)

    # Build finding text listing each distinct ungoverned figure
    returns_str = ', '.join(str(r) for r in tool_returns)
    parts = []
    for fig in ungoverned:
        parts.append(
            f'reported figure {fig} was not returned by any tool call')
    finding = '; '.join(parts) + f'; observed returns: [{returns_str}]'

    return {
        'outcome': PARTIALLY_GOVERNED,
        'tool_returns': tool_returns,
        'ungoverned_figures': ungoverned,
        'ungoverned_token_count': token_count,
        'finding': finding,
    }
