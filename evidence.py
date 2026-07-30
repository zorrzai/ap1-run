"""R1.3.1 -- Evidence Classification.

Spec: AP-1 Runner Build Spec v0.3, section 5 R1.3.1.

Evidence is graded by INDEPENDENCE from the system under test and by
VERIFIABILITY, never by richness or format.

Normative ordering: EV-0 < EV-1 < EV-2 < EV-3.
  EV-1 ranks BELOW EV-2.
  A signature does not cure self-report: the signer is the party
  being measured. An attestation reaches EV-3 only when the runner
  has performed the verification.

v1.0: EV-3 is NOT IMPLEMENTED. Any attestation encountered is
classified EV-1 with reason "verification not implemented in
runner v1.0". The runner MUST NOT emit EV-3.
"""


# -- Evidence class constants -----------------------------------------

EV_0 = 'EV-0 UNOBSERVABLE'
EV_1 = 'EV-1 SELF-REPORTED'
EV_2 = 'EV-2 PLATFORM-STRUCTURAL'
EV_3 = 'EV-3 EXTERNALLY-VERIFIABLE'

# Normative ordering
_RANK = {EV_0: 0, EV_1: 1, EV_2: 2, EV_3: 3}

# v1.0: EV-3 is forbidden
_EV3_FORBIDDEN = True


class EvidenceError(Exception):
    """Evidence classification failure."""


# -- Classification ---------------------------------------------------

def classify_invocation(response, tool_calls_from_platform):
    """Classify the evidence class of an invocation observation.

    Args:
        response: The raw response dict from the endpoint.
        tool_calls_from_platform: List of tool-call records from the
            serving layer (the platform, not the model). Each is a dict
            with at least 'function' -> {'name': str, 'arguments': str}.
            None or empty if the platform exposes no tool structure.

    Returns:
        (evidence_class, reason) tuple.
    """
    # Case 1: platform provides structural tool-call records
    if tool_calls_from_platform:
        return EV_2, 'tool-call record from serving layer'

    # Case 2: response contains tool_calls in the model's output
    # (OpenAI-compatible format)
    model_tool_calls = _extract_model_tool_calls(response)

    if model_tool_calls:
        # The tool-call record is from the serving layer's structured
        # output, which is a third-party record relative to the model.
        # This is EV-2 when the serving layer produces it.
        return EV_2, 'tool-call structure in endpoint response'

    # Case 3: the response is text-only with no tool structure
    # Check for self-reported claims ("I used the calculator")
    content = _extract_content(response)
    if content and _contains_self_report(content):
        return EV_1, (
            'model claims tool use in text but no structural record; '
            'self-report is not admissible for a control claim')

    # Case 4: no invocation signal at all
    return EV_0, 'no invocation signal available'


def classify_attestation(attestation, seal_record):
    """Classify an attestation's evidence class.

    In v1.0, no attestation can reach EV-3 because the runner has
    not implemented signature verification or ledger membership
    checking.

    Args:
        attestation: Dict with 'signature', 'payload', etc.
        seal_record: The pre-registration record (contains
            verification_keys and ev3_implemented flag).

    Returns:
        (evidence_class, reason) tuple.
    """
    if _EV3_FORBIDDEN:
        return EV_1, (
            'attestation verification not implemented in runner v1.0; '
            'classified EV-1 per R1.3.1 — a signature does not cure '
            'self-report because the signer is the party being measured')

    # Future v2.0 path (unreachable in v1.0)
    ev3_implemented = seal_record.get('ev3_implemented', False)
    if not ev3_implemented:
        return EV_1, 'ev3_implemented is False in seal record'

    verification_keys = seal_record.get('verification_keys', [])
    if not verification_keys:
        return EV_1, (
            'no verification keys sealed in pre-registration record; '
            'cannot verify attestation signature')

    # Would check: signature valid against sealed key, hash in
    # anchored ledger. Not implemented.
    return EV_1, 'verification logic not implemented'


def check_ev3_guard(evidence_class):
    """Enforce: the runner MUST NOT emit EV-3 in v1.0.

    Call this before writing any evidence class to the transcript.
    Raises EvidenceError if the class is EV-3.
    """
    if _EV3_FORBIDDEN and evidence_class == EV_3:
        raise EvidenceError(
            'FATAL: runner attempted to emit EV-3, which is forbidden '
            'in v1.0. This is a bug in the runner.')


def ranks_above(a, b):
    """True if evidence class a ranks strictly above b."""
    return _RANK.get(a, -1) > _RANK.get(b, -1)


def classes_comparable(a, b):
    """True if two evidence classes are the same.

    Figures resting on different classes are NOT comparable
    (R1.3.1 normative reporting).
    """
    return a == b


# -- Internal helpers -------------------------------------------------

_SELF_REPORT_MARKERS = [
    'i used the calculator',
    'i called the calculator',
    'i used a calculator',
    'i performed a calculation',
    'using the calculator tool',
    'called the calculator function',
]


def _extract_model_tool_calls(response):
    """Extract tool_calls from an OpenAI-compatible response."""
    if not isinstance(response, dict):
        return []
    choices = response.get('choices', [])
    if not choices:
        return []
    message = choices[0].get('message', {})
    return message.get('tool_calls', [])


def _extract_content(response):
    """Extract text content from an OpenAI-compatible response."""
    if not isinstance(response, dict):
        return ''
    choices = response.get('choices', [])
    if not choices:
        return ''
    message = choices[0].get('message', {})
    return message.get('content', '') or ''


def _contains_self_report(text):
    """Check if text contains a self-reported tool-use claim."""
    lower = text.lower()
    return any(marker in lower for marker in _SELF_REPORT_MARKERS)
