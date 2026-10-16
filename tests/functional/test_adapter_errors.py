"""Credential masking in adapter errors, through the adapter's HTTP path
against a scripted endpoint (from legacy verify_integration.py
test_credential_masking_in_error_bodies). End to end: regression scenario
transport_errors (Q08, HTTP 401 echoing a key)."""

import pytest

from ap1_run.foundation import adapter

CASES = [
    ('sk-proj-ABCDEFGHIJKLMNOP1234567890abcdef',
     'Incorrect API key provided: sk-proj-ABCDEFGHIJKLMNOP1234567890abcdef. '
     'You can find',
     'Incorrect API key provided: [REDACTED]. You can find'),
    ('sk-ABCDEFGHIJKLMNOP1234567890abcdef',
     'Invalid key: sk-ABCDEFGHIJKLMNOP1234567890abcdef',
     'Invalid key: [REDACTED]'),
    ('ghp_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890',
     'Bad credentials with ghp_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890',
     'Bad credentials with [REDACTED]'),
    ('Bearer sk-proj-XYZ123456789abcdef0123456789',
     'Unauthorized: Bearer sk-proj-XYZ123456789abcdef0123456789',
     'Unauthorized: [REDACTED]'),
]


@pytest.mark.req('R0.2')
@pytest.mark.parametrize('key, body, masked', CASES,
                         ids=['sk-proj', 'sk', 'ghp', 'bearer'])
def test_mask_credentials_redacts_key_and_keeps_the_rest(key, body, masked):
    assert adapter._mask_credentials(body) == masked


@pytest.mark.req('R0.2')
@pytest.mark.parametrize('text', [
    'HTTP 429: rate limited, please retry after 30s', '', None])
def test_mask_credentials_leaves_other_text_unchanged(text):
    assert adapter._mask_credentials(text) == text


@pytest.mark.req('R0.2')
@pytest.mark.parametrize('key, body, masked', CASES,
                         ids=['sk-proj', 'sk', 'ghp', 'bearer'])
def test_http_error_from_endpoint_carries_only_masked_text(endpoint, key,
                                                           body, masked):
    endpoint.queue.append((401, body))
    with pytest.raises(adapter.HTTPError) as exc:
        adapter.send(endpoint.url, messages=[{'role': 'user', 'content': 'x'}],
                     model='m', timeout=5)
    err = exc.value
    assert (str(err), err.status_code, err.body) == \
        (f'HTTP 401: {masked}', 401, masked)
    assert all(key not in str(v) for v in vars(err).values())


@pytest.mark.req('R0.2')
def test_rate_limit_error_from_endpoint_is_masked(endpoint):
    endpoint.queue.append((429, CASES[1][1]))
    with pytest.raises(adapter.RateLimitError) as exc:
        adapter.send(endpoint.url, messages=[], model='m', timeout=5)
    assert str(exc.value) == 'rate limited (HTTP 429): Invalid key: [REDACTED]'
