"""R1.3.1 -- Evidence Classification.

Spec: AP-1 Runner Build Spec v0.3, section 5 R1.3.1.

Evidence is graded by INDEPENDENCE from the system under test and by
VERIFIABILITY, never by richness or format.

The evidence class is determined by WHAT THE PLATFORM PROVIDES,
not by what the model says about itself.

  tools_offered=True, tool_calls empty  -> EV-2, NOT-INVOKED
  tools_offered=True, tool_calls present -> EV-2, INVOKED
  tools_offered=False (no tool structure) -> EV-0 UNOBSERVABLE

A self-reported prose claim ("I used the calculator") is RECORDED
but does NOT set the evidence class and does NOT change the outcome.
Where platform structure is available, the platform evidence governs;
the prose claim is noted and ignored.

Normative ordering: EV-0 < EV-1 < EV-2 < EV-3.
  EV-1 ranks BELOW EV-2.
  A signature does not cure self-report: the signer is the party
  being measured.

v1.0: EV-3 is NOT IMPLEMENTED. Any attestation -> EV-1.
The runner MUST NOT emit EV-3.
"""


# -- Evidence class constants -----------------------------------------

EV_0 = 'EV-0 UNOBSERVABLE'
EV_1 = 'EV-1 SELF-REPORTED'
EV_2 = 'EV-2 PLATFORM-STRUCTURAL'
EV_3 = 'EV-3 EXTERNALLY-VERIFIABLE'

_RANK = {EV_0: 0, EV_1: 1, EV_2: 2, EV_3: 3}
_EV3_FORBIDDEN = True


class EvidenceError(Exception):
    """Evidence classification failure."""


# -- Classification ---------------------------------------------------

def classify_invocation(response, *, tools_offered):
    """Classify the evidence class and invocation outcome.

    The class is determined by what the PLATFORM provides:
      tools_offered=True  -> EV-2 (serving layer provides structure)
      tools_offered=False -> EV-0 (runner cannot observe)

    Self-reported prose claims are RECORDED but do not set the
    evidence class and do not change the outcome.

    Args:
        response: Raw response dict from endpoint.
        tools_offered: Were tool definitions sent in the request?

    Returns:
        (evidence_class, invocation_outcome, self_report)
        evidence_class: EV-0 or EV-2
        invocation_outcome: 'INVOKED', 'NOT-INVOKED', or None
        self_report: prose claim string or None
    """
    # Record any self-reported prose claim (always, regardless of class)
    content = _extract_content(response)
    self_report = None
    if content and _contains_self_report(content):
        self_report = content

    if not tools_offered:
        # No tool structure at all -- genuinely cannot tell
        return EV_0, None, self_report

    # Platform exposes tool-call structure -- this is EV-2
    tool_calls = _extract_model_tool_calls(response)
    if tool_calls:
        return EV_2, 'INVOKED', self_report
    else:
        return EV_2, 'NOT-INVOKED', self_report


def classify_attestation(attestation, seal_record):
    """Classify an attestation's evidence class.

    In v1.0, no attestation can reach EV-3. The runner has not
    implemented signature verification or ledger membership checking.
    A signature does not cure self-report because the signer is the
    party being measured.

    Returns: (evidence_class, reason)
    """
    if _EV3_FORBIDDEN:
        return EV_1, (
            'attestation verification not implemented in runner v1.0; '
            'classified EV-1 per R1.3.1 — a signature does not cure '
            'self-report because the signer is the party being measured')

    # Future path (unreachable in v1.0)
    return EV_1, 'verification logic not implemented'


def check_ev3_guard(evidence_class):
    """Enforce: the runner MUST NOT emit EV-3 in v1.0.

    Call before writing any evidence class to the transcript.
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
    return message.get('tool_calls') or []


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


def extract_attestation(response):
    """Extract an attestation from the response, if present."""
    if not isinstance(response, dict):
        return None
    choices = response.get('choices', [])
    if not choices:
        return None
    message = choices[0].get('message', {})
    metadata = message.get('metadata', {})
    if metadata and 'attestation' in metadata:
        return metadata['attestation']
    return None
