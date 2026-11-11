"""R0.2 -- Endpoint Adapter.

Spec: AP-1 Runner Build Spec v0.3, section 3 R0.2.

Send requests to one interface class -- an OpenAI-compatible
chat-completions endpoint with tool calling -- and return the
raw response unmodified.

Dependencies: requests (the external dependency used by this module).
No SDK. No interpretation, no retry-on-content, no normalisation.
Network calls target only the configured endpoint: HTTP redirects are not
followed (a 3xx is an HTTP error), and the environment is ignored (no proxy
from HTTP_PROXY, HTTPS_PROXY, ALL_PROXY or the system settings, no .netrc
credentials), so no request reaches another host.
"""

import copy
import json
import math
import re
import time
from decimal import Decimal, InvalidOperation

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
    """Transport or HTTP failure, or a request that may not be sent.

    After a transport failure on every attempt, request_record is the
    request record with its attempt log (S3-G1-18); otherwise None.
    """
    request_record = None


class RateLimitError(AdapterError):
    """HTTP 429 -- rate limited. Recorded as UNMEASURED."""


class HTTPError(AdapterError):
    """Non-200, non-429 HTTP response. Recorded as UNMEASURED."""

    def __init__(self, message, status_code, body):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


def wire_value(name, value):
    """A sampling value as the request body carries it: a number as a JSON
    number (an integer if integral, else a float), anything else as given.
    Refused (AdapterError): a value that is not finite, or whose float is
    not (a finite number too large for a float, sent as Infinity) or
    loses it entirely (one that underflows to 0) (S3-G1-19)."""
    try:
        d = Decimal(str(value))
    except InvalidOperation:
        return value
    if not d.is_finite():
        # NaN would go out as the non-JSON token NaN, and Infinity as a
        # string
        raise AdapterError(
            f'sampling.{name}: not a finite number: {value!r}; not sent')
    if d == d.to_integral_value():
        return int(d)
    f = float(d)
    if not math.isfinite(f) or f == 0:
        raise AdapterError(
            f'sampling.{name}: {value!r} has no finite non-zero float '
            f'(it would be sent as {f!r}); not sent')
    return f


class RawResponse(dict):
    """A response as received: the parsed JSON (the dict itself, which
    every reader uses) and its body text, exactly as it arrived
    (raw_text: the body's bytes decoded as UTF-8, so that
    raw_text.encode('utf-8') is those bytes). SPEC R0.2: "unmodified"
    means byte for byte, so key order and number spelling (15.200, not
    15.2) are kept in the text the transcript stores."""

    raw_text = None


class RawList(list):
    """A response whose JSON is a list (not a chat completion, so read as
    an unrecognised shape), with its body text as RawResponse has it."""

    raw_text = None


def raw_text(response):
    """The body text a response arrived as (RawResponse.raw_text), or None
    for a response that did not come from send."""
    return getattr(response, 'raw_text', None)


MAX_RETRIES = 3     # on transport failure only, per R0.2
RETRY_DELAY = 1.0   # seconds between transport-failure retries

# Request body fields a sampling parameter may not set (S3-G1-21).
BODY_FIELDS = ('model', 'messages', 'tools')


def _post(url, **kwargs):
    """requests.post, without the environment: trust_env is off, so no
    proxy, .netrc credential or CA bundle is taken from environment
    variables or system settings (SPEC R0.2: no network call to a host
    other than the configured endpoint)."""
    with _requests.Session() as session:
        session.trust_env = False
        return session.post(url, **kwargs)


def send(endpoint_url, *, messages, tools=None, sampling=None,
         model=None, api_key=None, timeout=120):
    """Send a chat-completions request. Return raw JSON response.

    No interpretation, no retry-on-content, no normalisation.
    Returns what arrived, including errors.
    Retries only on transport failure, bounded, every attempt logged.

    Returns:
        (raw_response_dict, request_record)
        raw_response_dict: The response JSON, unmodified: a RawResponse,
            the parsed body, whose raw_text is the body byte for byte.
        request_record: The request AS SENT, including every
            sampling parameter with its value or explicit omission.

    Raises:
        AdapterError: Unrecoverable transport failure after all retries
            (carrying request_record); a 200 response whose body is not
            UTF-8 or not JSON; or, before anything is sent, a sampling
            parameter that names a body field or whose value is a
            non-finite number.
        RateLimitError: HTTP 429.
        HTTPError: Non-200, non-429 status.
    """
    body = {"model": model or "", "messages": messages}

    if tools:
        body["tools"] = tools

    sampling_as_sent = {}
    if sampling:
        for k, v in sampling.items():
            if k in BODY_FIELDS:
                raise AdapterError(
                    f'sampling.{k}: names a request body field; not sent')
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
                body[k] = wire_value(k, v)
                sampling_as_sent[k] = str(v)

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    # A copy, so the record stays the request as sent when the caller
    # goes on to extend its message list (SPEC R0.2).
    request_record = {
        "endpoint_url": endpoint_url,
        "model": model or "",
        "messages": copy.deepcopy(messages),
        "tools": copy.deepcopy(tools),
        "sampling_as_sent": sampling_as_sent,
    }

    attempts = []

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            # Never follow a redirect, nor a proxy from the environment:
            # either could send the request (with the key and the fixture
            # data in it) to another host (SPEC R0.2).
            resp = _post(
                endpoint_url, json=body, headers=headers,
                timeout=timeout, allow_redirects=False)
            attempts.append({
                "attempt": attempt,
                "status_code": resp.status_code,
                "error": None,
                "timestamp": time.time(),
            })
        except _requests.RequestException as e:
            error_text = _mask_credentials(str(e))
            attempts.append({
                "attempt": attempt,
                "status_code": None,
                "error": error_text,
                "timestamp": time.time(),
            })
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                continue
            request_record["attempts"] = attempts
            failure = AdapterError(
                f"transport failure after {MAX_RETRIES} attempts: "
                f"{error_text}")
            failure.request_record = request_record
            # Not chained: the original's text is unmasked, and a printed
            # traceback shows chained exceptions (rule 0c).
            raise failure from None

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

        # The body as received, kept as text beside its parse (SPEC R0.2:
        # byte for byte). JSON between systems is UTF-8 (RFC 8259 8.1);
        # a body that is not cannot be kept as text, and is refused as a
        # body that is not JSON is.
        try:
            text = resp.content.decode('utf-8')
        except UnicodeDecodeError:
            raise AdapterError(
                f"response is not UTF-8: {_mask_credentials(resp.text[:200])}"
            ) from None
        try:
            parsed = json.loads(text)
        except ValueError:
            raise AdapterError(
                f"response is not valid JSON: {_mask_credentials(resp.text[:200])}"
            ) from None
        # A body that is neither an object nor a list (a bare string,
        # number or null) is returned as parsed, without its text.
        raw = parsed
        if isinstance(parsed, dict):
            raw = RawResponse(parsed)
        elif isinstance(parsed, list):
            raw = RawList(parsed)
        if raw is not parsed:
            raw.raw_text = text

        return raw, request_record

    request_record["attempts"] = attempts
    raise AdapterError("exhausted retries with no response")
