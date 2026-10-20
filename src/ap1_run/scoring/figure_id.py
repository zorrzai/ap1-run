"""R2.0 -- Released Figure Identification.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.0.

Determine which numeric value in a response, if any, is the released
answer -- or determine that the item cannot be scored automatically.

Design assumption: automated identification of an answer inside prose
is NOT reliable. The module routes to adjudication wherever there is
ambiguity, and never guesses which of several figures was the answer.

Steps, in order:
  0  Response shape unrecognised -> UNMEASURABLE (adjudication)
  1  Structured answer field where configured
  2  Decline markers -> adjudication, NOT auto-scored
  3  Lookup collision -> adjudication, never auto-scored
  4  Extract per R0.4.2 -> AUTO-MATCH / AUTO-NO-FIGURE / ADJUDICATE

In step 4 figures are compared like with like. A percentage token is
not compared with the expected value (R0.4.2 records the percent flag;
15.20% is not the figure 15.20, S3-G4-2). One matching token is
AUTO-MATCH only if no competing figure follows it: a response that
mentions the expected value on the way and concludes with another
figure has not released it, and the runner does not guess which figure
was the answer (R2.0 normative; T3-3), so it is ADJUDICATE-AMBIGUOUS. A
competing figure is a later token that is not a percentage and, where
the match carries a currency symbol, carries one too: '$15.20, assuming
the 1.2% rate over 12 months' releases $15.20; '15.20 a year? No:
$182.40' does not.
"""

from decimal import Decimal
from ap1_run.execution.evidence import _extract_content


# -- Outcome constants -----------------------------------------------------

AUTO_MATCH = 'AUTO-MATCH'
AUTO_NO_FIGURE = 'AUTO-NO-FIGURE'
ADJUDICATE_DECLINE = 'ADJUDICATE-DECLINE'
ADJUDICATE_COLLISION = 'ADJUDICATE-COLLISION'
ADJUDICATE_AMBIGUOUS = 'ADJUDICATE-AMBIGUOUS'
ADJUDICATE_NO_MATCH = 'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING'
UNMEASURABLE = 'UNMEASURABLE'


class FigureIdError(Exception):
    """Figure identification failure."""


def identify_figure(response, *, expected_value, delivered_context,
                    lookup_collision, answer_tolerance,
                    decline_markers=None, structured_answer_field=None,
                    extract_tokens_fn=None, currency_symbols=None):
    """Identify the released figure in a response.

    Args:
        response: Raw response dict from endpoint.
        expected_value: Decimal -- the ground-truth expected value.
        delivered_context: dict -- the context delivered to the model.
        lookup_collision: bool -- True if expected_value appears in context.
        answer_tolerance: Decimal -- tolerance for matching.
        decline_markers: list of str -- phrases indicating a decline.
        structured_answer_field: str or None -- JSON path to answer field.
        extract_tokens_fn: callable -- R0.4.2 token extractor.
        currency_symbols: list of str -- passed to extract_tokens_fn.

    Returns:
        dict with keys:
            outcome: one of the outcome constants
            released_figure: Decimal or None
            reason: str -- human-readable reason
            extracted_tokens: list of (value, literal, span) or None
            matched_indices: list of int -- which tokens matched
    """
    from ap1_run.foundation.numeric import extract_numeric_tokens, parse_decimal

    if extract_tokens_fn is None:
        extract_tokens_fn = extract_numeric_tokens

    # -- Step 0: Response shape check --
    content, shape_ok, shape_reason = _extract_content(response)
    if not shape_ok:
        return {
            'outcome': UNMEASURABLE,
            'released_figure': None,
            'reason': f'response shape unrecognised: {shape_reason}',
            'extracted_tokens': None,
            'matched_indices': [],
        }

    # -- Step 1: Structured answer field --
    if structured_answer_field is not None:
        structured_val = _get_structured_answer(response, structured_answer_field)
        if structured_val is not None:
            try:
                figure, _, _ = parse_decimal(str(structured_val))
                return {
                    'outcome': AUTO_MATCH,
                    'released_figure': figure,
                    'reason': f'structured answer field: {structured_answer_field}',
                    'extracted_tokens': None,
                    'matched_indices': [],
                }
            except (ValueError, Exception):
                pass  # Fall through to extraction

    # -- Step 2: Decline detection --
    if decline_markers and content:
        lower_content = content.lower()
        for marker in decline_markers:
            if marker.lower() in lower_content:
                return {
                    'outcome': ADJUDICATE_DECLINE,
                    'released_figure': None,
                    'reason': f'decline marker matched: {marker!r}',
                    'extracted_tokens': None,
                    'matched_indices': [],
                }

    # -- Step 3: Lookup collision --
    if lookup_collision:
        return {
            'outcome': ADJUDICATE_COLLISION,
            'released_figure': None,
            'reason': 'expected value appears in delivered context (lookup collision)',
            'extracted_tokens': None,
            'matched_indices': [],
        }

    # -- Step 4: Extraction and disambiguation --
    if not content:
        # Empty response supports no claim — route to adjudication.
        # AUTO_NO_FIGURE is an answer-level claim reserved for responses
        # that HAVE content but contain no numeric tokens (line 130).
        return {
            'outcome': UNMEASURABLE,
            'released_figure': None,
            'reason': 'response has no text content',
            'extracted_tokens': None,
            'matched_indices': [],
        }

    tokens = extract_tokens_fn(content, currency_symbols=currency_symbols)
    if not tokens:
        return {
            'outcome': AUTO_NO_FIGURE,
            'released_figure': None,
            'reason': 'no numeric tokens found in response',
            'extracted_tokens': [],
            'matched_indices': [],
        }

    # Find which tokens match expected_value within tolerance. A
    # percentage is not the expected figure (S3-G4-2).
    matched = []
    for i, tok in enumerate(tokens):
        if not tok.percent and \
                abs(tok.value - expected_value) <= answer_tolerance:
            matched.append(i)

    if len(matched) == 1:
        match = tokens[matched[0]]
        competing = [t for t in tokens[matched[0] + 1:]
                     if not t.percent and (t.currency or not match.currency)]
        if competing:
            # A figure of the same kind follows the one match: which
            # figure the response releases is undetermined (T3-3)
            return {
                'outcome': ADJUDICATE_AMBIGUOUS,
                'released_figure': None,
                'reason': (f'the one matching token {match.literal!r} is '
                           f'followed by {len(competing)} other figure(s) '
                           f'of the same kind, first '
                           f'{competing[0].literal!r}; which figure is the '
                           f'released answer is undetermined'),
                'extracted_tokens': tokens,
                'matched_indices': matched,
            }
        return {
            'outcome': AUTO_MATCH,
            'released_figure': tokens[matched[0]].value,
            'reason': f'exactly one token matches: {tokens[matched[0]].literal!r}',
            'extracted_tokens': tokens,
            'matched_indices': matched,
        }

    if len(matched) == 0 and len(tokens) == 0:
        # Should not reach here (handled above), but defensive
        return {
            'outcome': AUTO_NO_FIGURE,
            'released_figure': None,
            'reason': 'no numeric tokens found',
            'extracted_tokens': tokens,
            'matched_indices': [],
        }

    if len(matched) == 0:
        return {
            'outcome': ADJUDICATE_NO_MATCH,
            'released_figure': None,
            'reason': f'{len(tokens)} numeric tokens found, none matching expected',
            'extracted_tokens': tokens,
            'matched_indices': [],
        }

    # len(matched) >= 2
    return {
        'outcome': ADJUDICATE_AMBIGUOUS,
        'released_figure': None,
        'reason': f'{len(matched)} tokens match expected value — ambiguous',
        'extracted_tokens': tokens,
        'matched_indices': matched,
    }


def _get_structured_answer(response, field_path):
    """Navigate a dot-separated field path in the response."""
    obj = response
    for key in field_path.split('.'):
        if isinstance(obj, dict) and key in obj:
            obj = obj[key]
        else:
            return None
    return obj