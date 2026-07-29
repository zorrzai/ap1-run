"""R0.2 -- Endpoint Adapter.

Spec: AP-1 Runner Build Spec v0.3, section 3 R0.2.

Send requests to one interface class -- an OpenAI-compatible
chat-completions endpoint with tool calling -- and return the
raw response unmodified.

Dependencies: requests (the only external dependency).
No SDK. No interpretation, no retry-on-content, no normalisation.
"""

import requests as _requests


class AdapterError(Exception):
    """Transport or HTTP failure."""


class RateLimitError(AdapterError):
    """HTTP 429 -- rate limited. Recorded as UNMEASURED."""


MAX_RETRIES = 2  # on transport failure only, per R0.2


def send(endpoint_url, *, messages, tools=None, sampling=None,
         model=None, timeout=120):
    """Send a chat-completions request. Return raw JSON response.

    No interpretation, no retry-on-content, no normalisation.
    Retries only on transport failure, bounded, every attempt logged.

    Returns: (response_dict, attempts_log)
    Raises: AdapterError on unrecoverable transport failure.
            RateLimitError on HTTP 429.
    """
    body = {'model': model or '', 'messages': messages}

    if tools:
        body['tools'] = tools

    # Apply sampling parameters (value or explicit 'omitted')
    if sampling:
        for k, v in sampling.items():
            if v != 'omitted':
                body[k] = v

    headers = {'Content-Type': 'application/json'}
    attempts = []

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = _requests.post(
                endpoint_url, json=body, headers=headers,
                timeout=timeout)
            attempts.append({
                'attempt': attempt,
                'status': resp.status_code,
                'error': None,
            })
        except _requests.RequestException as e:
            attempts.append({
                'attempt': attempt,
                'status': None,
                'error': str(e),
            })
            if attempt == MAX_RETRIES:
                raise AdapterError(
                    f'transport failure after {MAX_RETRIES} attempts: {e}'
                ) from e
            continue

        if resp.status_code == 429:
            raise RateLimitError(
                f'rate limited (HTTP 429): {resp.text[:200]}')

        if resp.status_code != 200:
            raise AdapterError(
                f'HTTP {resp.status_code}: {resp.text[:500]}')

        return resp.json(), attempts

    # Should not reach here
    raise AdapterError('exhausted retries with no response')


def build_request_record(body, sampling):
    """Record the request as sent, per R0.2 audit requirement.

    Returns the body dict augmented with sampling_as_sent showing
    every parameter and its value or explicit omission.
    """
    record = dict(body)
    record['sampling_as_sent'] = {}
    if sampling:
        for k, v in sampling.items():
            record['sampling_as_sent'][k] = str(v)
    return record
