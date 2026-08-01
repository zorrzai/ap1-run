"""R0.2 -- Endpoint Adapter.

Spec: AP-1 Runner Build Spec v0.3, section 3 R0.2.

Send requests to one interface class -- an OpenAI-compatible
chat-completions endpoint with tool calling -- and return the
raw response unmodified.

Dependencies: requests (the only external dependency).
No SDK. No interpretation, no retry-on-content, no normalisation.
No network call to any host other than the configured endpoint.
"""

import re
import time
from decimal import Decimal

import requests as _requests


# Credential-shape patterns to redact from error bodies (Rule 0c).
# Applied BEFORE any error text enters an exception, transcript, or log.
_CREDENTIAL_PATTERNS = re.compile(
    r'(?:'
    r'sk-proj-[A-Za-z0-9_-]{10,}'
    r'|sk-[A-Za-z0-9_-]{10,}'
    r'|ghp_[A-Za-z0-9]{10,}'
    r'|gho_[A-Za-z0-9]{10,}'
    r'|github_pat_[A-Za-z0-9_]{10,}'
    r'|rpa_[A-Za-z0-9]{10,}'
    r'|Bearer\s+[A-Za-z0-9_.-]{10,}'
    r')'
)


def _mask_credentials(text):
    """Redact credential-shaped substrings from error text.

    Retains endpoint URLs, status codes, error types.
    Replaces only credential-shaped tokens with [REDACTED].
    """
    if not text:
        return text
    return _CREDENTIAL_PATTERNS.sub('[REDACTED]', text)


class AdapterError(Exception):
    """Transport or HTTP failure."""


class RateLimitError(AdapterError):
    """HTTP 429 -- rate limited. Recorded as UNMEASURED."""


class HTTPError(AdapterError):
    """Non-200, non-429 HTTP response. Recorded as UNMEASURED."""

    def __init__(self, message, status_code, body):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


MAX_RETRIES = 3     # on transport failure only, per R0.2
RETRY_DELAY = 1.0   # seconds between transport-failure retries


def send(endpoint_url, *, messages, tools=None, sampling=None,
         model=None, api_key=None, timeout=120):
    """Send a chat-completions request. Return raw JSON response.

    No interpretation, no retry-on-content, no normalisation.
    Returns what arrived, including errors.
    Retries only on transport failure, bounded, every attempt logged.

    Returns:
        (raw_response_dict, request_record)
        raw_response_dict: The response JSON, unmodified.
        request_record: The request AS SENT, including every
            sampling parameter with its value or explicit omission.

    Raises:
        AdapterError: Unrecoverable transport failure after all retries.
        RateLimitError: HTTP 429.
        HTTPError: Non-200, non-429 status.
    """
    body = {"model": model or "", "messages": messages}

    if tools:
        body["tools"] = tools

    sampling_as_sent = {}
    if sampling:
        for k, v in sampling.items():
            # Structured omission: {"value": "omitted", "reason": "...", "detail": "..."}
            if isinstance(v, dict) and v.get('value') == 'omitted':
                sampling_as_sent[k] = {
                    'value': 'omitted',
                    'reason': v.get('reason', ''),
                    'detail': v.get('detail', ''),
                }
            # Legacy plain string omission (should be caught by config
            # validation, but defensive)
            elif v == "omitted":
                sampling_as_sent[k] = "omitted"
            else:
                try:
                    d = Decimal(str(v))
                    if d == d.to_integral_value():
                        body[k] = int(d)
                    else:
                        body[k] = float(d)
                except Exception:
                    body[k] = v
                sampling_as_sent[k] = str(v)

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    request_record = {
        "endpoint_url": endpoint_url,
        "model": model or "",
        "messages": messages,
        "tools": tools,
        "sampling_as_sent": sampling_as_sent,
    }

    attempts = []

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = _requests.post(
                endpoint_url, json=body, headers=headers,
                timeout=timeout)
            attempts.append({
                "attempt": attempt,
                "status_code": resp.status_code,
                "error": None,
                "timestamp": time.time(),
            })
        except _requests.RequestException as e:
            attempts.append({
                "attempt": attempt,
                "status_code": None,
                "error": str(e),
                "timestamp": time.time(),
            })
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                continue
            request_record["attempts"] = attempts
            raise AdapterError(
                f"transport failure after {MAX_RETRIES} attempts: {e}"
            ) from e

        request_record["attempts"] = attempts

        if resp.status_code == 429:
            raise RateLimitError(
                f"rate limited (HTTP 429): {_mask_credentials(resp.text[:200])}")

        if resp.status_code != 200:
            masked_body = _mask_credentials(resp.text[:2000])
            raise HTTPError(
                f"HTTP {resp.status_code}: {_mask_credentials(resp.text[:500])}",
                status_code=resp.status_code,
                body=masked_body)

        try:
            raw = resp.json()
        except ValueError as e:
            raise AdapterError(
                f"response is not valid JSON: {_mask_credentials(resp.text[:200])}"
            ) from e

        return raw, request_record

    request_record["attempts"] = attempts
    raise AdapterError("exhausted retries with no response")
