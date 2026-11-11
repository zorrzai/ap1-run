"""Unit tests for the R0.2 endpoint adapter (foundation/adapter.py).

No network: the adapter's post (adapter._post) and time.sleep are replaced
by fakes, except in the proxy tests at the end, which use local servers.
The real HTTP path is covered end to end by the regression scenarios, which
run against tests/fixtures/mock_endpoint.py (clean, transport_errors, ...).
"""

import json
from types import SimpleNamespace

import pytest
import requests

from ap1_run.foundation import adapter
from ap1_run.foundation.adapter import (
    BODY_FIELDS, MAX_RETRIES, RETRY_DELAY, AdapterError, HTTPError,
    RateLimitError, _mask_credentials, send,
)

URL = 'http://endpoint.test/v1/chat/completions'
MESSAGES = [{'role': 'user', 'content': 'hi'}]
OK = {'choices': [{'message': {'role': 'assistant', 'content': '42'}}]}


class FakeResponse:
    def __init__(self, status_code=200, payload=None, text=None,
                 content=None):
        self.status_code = status_code
        self._payload = payload
        if text is None:
            text = (content.decode('latin-1') if content is not None
                    else json.dumps(payload) if payload is not None else '')
        self.text = text
        # The body's bytes, as requests.Response.content has them
        self.content = text.encode('utf-8') if content is None else content

    def json(self):
        if self._payload is None:
            return json.loads(self.text)   # raises ValueError if not JSON
        return self._payload


class FakeTransport:
    """Records each post() and plays back a list of outcomes: a
    FakeResponse is returned, an exception is raised."""

    def __init__(self, *outcomes):
        self.outcomes = list(outcomes)
        self.calls = []
        self.sleeps = []

    def post(self, url, **kw):
        self.calls.append(dict(kw, url=url))
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome

    def sleep(self, seconds):
        self.sleeps.append(seconds)


@pytest.fixture
def transport(monkeypatch):
    def _install(*outcomes):
        t = FakeTransport(*outcomes)
        monkeypatch.setattr(adapter, '_post', t.post)
        monkeypatch.setattr(adapter.time, 'sleep', t.sleep)
        monkeypatch.setattr(adapter.time, 'time', lambda: 1000.5)
        return t
    return _install


def ok_send(transport, **kw):
    t = transport(FakeResponse(200, OK))
    raw, record = send(URL, messages=MESSAGES, **kw)
    return t, raw, record


# -- constants ------------------------------------------------------------

def test_retry_constants():
    assert (MAX_RETRIES, RETRY_DELAY) == (3, 1.0)


def test_error_hierarchy():
    assert issubclass(RateLimitError, AdapterError)
    assert issubclass(HTTPError, AdapterError)
    e = HTTPError('m', status_code=500, body='b')
    assert (str(e), e.status_code, e.body) == ('m', 500, 'b')


# -- request body and headers ---------------------------------------------

@pytest.mark.req('R0.2')
def test_send_returns_raw_response_unmodified(transport):
    _, raw, _ = ok_send(transport)
    assert raw == OK and isinstance(raw, dict)


# A body whose spelling a parse and re-serialisation would change: keys
# not in sorted order, a number with trailing zeros, a non-ASCII
# character, and spacing of its own.
RAW_BODY = ('{"model":"m","x": 15.200, "choices":[{"message":{"role":'
            '"assistant","content":"15.20 \\u2212 0.00 = 15.20 −"}}],'
            '"id": "r1"}')

RAW_BYTES = ("R0.2 'unmodified' read as byte for byte: each answered round "
             "keeps the response body as received, as text (response_raw), "
             "beside the parsed response every reader uses; the reading and "
             "the field are this test's proposal, for review")


@pytest.mark.proposal(RAW_BYTES)
@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.2')
def test_send_keeps_the_body_text_byte_for_byte(transport):
    # The parsed response is the body's JSON; its raw_text is the body as
    # received, so 15.200, the key order and the spacing survive.
    transport(FakeResponse(200, content=RAW_BODY.encode('utf-8')))
    raw, _ = send(URL, messages=MESSAGES)
    assert raw == json.loads(RAW_BODY)
    assert raw['x'] == 15.2
    assert adapter.raw_text(raw).encode('utf-8') == RAW_BODY.encode('utf-8')


@pytest.mark.proposal(RAW_BYTES)
@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.2')
def test_send_keeps_the_text_of_a_list_body(transport):
    # A body that is not a chat completion (here a list) keeps its text
    # too; the engine reads it as an unrecognised shape.
    transport(FakeResponse(200, content=b'[1.50, {"b": 1, "a": 2}]'))
    raw, _ = send(URL, messages=MESSAGES)
    assert raw == [1.5, {'b': 1, 'a': 2}]
    assert adapter.raw_text(raw) == '[1.50, {"b": 1, "a": 2}]'


def test_raw_text_of_a_response_not_from_send_is_none():
    assert adapter.raw_text({'choices': []}) is None
    assert adapter.raw_text(None) is None


@pytest.mark.proposal(RAW_BYTES)
@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.2')
def test_send_200_body_not_utf8_raises_adapter_error(transport):
    # JSON between systems is UTF-8 (RFC 8259 8.1); a body that is not
    # cannot be kept as text, and is refused as a body that is not JSON
    # is: an AdapterError, so the round is recorded as failed.
    transport(FakeResponse(200, content=b'{"x": "caf\xe9"}'))
    with pytest.raises(AdapterError, match='response is not UTF-8'):
        send(URL, messages=MESSAGES)


@pytest.mark.finding('T3-52')
def test_send_minimal_body_and_headers(transport):
    t, _, _ = ok_send(transport)
    assert t.calls == [{
        'url': URL,
        'json': {'model': '', 'messages': MESSAGES},
        'headers': {'Content-Type': 'application/json'},
        'timeout': 120, 'allow_redirects': False}]


def test_send_model_tools_key_and_timeout(transport):
    tools = [{'type': 'function', 'function': {'name': 'calculator'}}]
    t, _, _ = ok_send(transport, model='m1', tools=tools, api_key='k',
                      timeout=5)
    call = t.calls[0]
    assert call['json'] == {'model': 'm1', 'messages': MESSAGES,
                            'tools': tools}
    assert call['headers'] == {'Content-Type': 'application/json',
                               'Authorization': 'Bearer k'}
    assert call['timeout'] == 5


def test_send_empty_tools_and_key_left_out(transport):
    t, _, _ = ok_send(transport, tools=[], api_key='')
    assert 'tools' not in t.calls[0]['json']
    assert 'Authorization' not in t.calls[0]['headers']


@pytest.mark.req('R0.2')
def test_send_integral_sampling_values_sent_as_int(transport):
    t, _, record = ok_send(transport, sampling={
        'temperature': '0', 'max_completion_tokens': '4096', 'seed': '1.0',
        'n': 2, 'big': '1e2'})
    body = t.calls[0]['json']
    assert [(body[k], type(body[k])) for k in
            ('temperature', 'max_completion_tokens', 'seed', 'n', 'big')] == [
        (0, int), (4096, int), (1, int), (2, int), (100, int)]
    assert record['sampling_as_sent'] == {
        'temperature': '0', 'max_completion_tokens': '4096', 'seed': '1.0',
        'n': '2', 'big': '1e2'}


def test_send_fractional_sampling_value_sent_as_float(transport):
    t, _, record = ok_send(transport, sampling={'top_p': '0.7'})
    assert t.calls[0]['json']['top_p'] == 0.7
    assert type(t.calls[0]['json']['top_p']) is float
    assert record['sampling_as_sent'] == {'top_p': '0.7'}


def test_send_non_numeric_sampling_value_sent_as_is(transport):
    t, _, record = ok_send(transport, sampling={'reasoning_effort': 'high',
                                                'stop': ['\n']})
    assert t.calls[0]['json']['reasoning_effort'] == 'high'
    assert t.calls[0]['json']['stop'] == ['\n']
    assert record['sampling_as_sent'] == {'reasoning_effort': 'high',
                                          'stop': "['\\n']"}


@pytest.mark.req('R0.2')
def test_send_structured_omission_recorded_not_sent(transport):
    o = {'value': 'omitted', 'reason': 'platform-rejected', 'detail': 'd',
         'extra': 'dropped'}
    t, _, record = ok_send(transport, sampling={'temperature': o})
    assert 'temperature' not in t.calls[0]['json']
    assert record['sampling_as_sent'] == {'temperature': {
        'value': 'omitted', 'reason': 'platform-rejected', 'detail': 'd'}}


def test_send_omission_without_reason_or_detail_recorded_empty(transport):
    _, _, record = ok_send(transport, sampling={'top_p': {'value': 'omitted'}})
    assert record['sampling_as_sent'] == {'top_p': {
        'value': 'omitted', 'reason': '', 'detail': ''}}


def test_send_plain_omitted_string_recorded_not_sent(transport):
    t, _, record = ok_send(transport, sampling={'top_p': 'omitted'})
    assert 'top_p' not in t.calls[0]['json']
    assert record['sampling_as_sent'] == {'top_p': 'omitted'}


def test_send_dict_not_omitted_sent_as_is(transport):
    t, _, record = ok_send(transport, sampling={'x': {'value': '1'}})
    assert t.calls[0]['json']['x'] == {'value': '1'}
    assert record['sampling_as_sent'] == {'x': "{'value': '1'}"}


# -- request record -------------------------------------------------------

@pytest.mark.req('R0.2')
def test_send_request_record_as_sent(transport):
    tools = [{'type': 'function'}]
    _, _, record = ok_send(transport, model='m', tools=tools,
                           sampling={'temperature': '0'})
    assert record == {
        'endpoint_url': URL, 'model': 'm', 'messages': MESSAGES,
        'tools': tools, 'sampling_as_sent': {'temperature': '0'},
        'attempts': [{'attempt': 1, 'status_code': 200, 'error': None,
                      'timestamp': 1000.5}]}


@pytest.mark.finding('S4-G4-1')
@pytest.mark.req('R0.2')
def test_send_request_record_unchanged_when_caller_extends_messages(
        transport):
    # SPEC R0.2 "The request as sent": the record holds copies, so a
    # caller that goes on extending its message list (the engine's tool
    # loop) or its tools does not change what the record says was sent.
    messages = [{'role': 'user', 'content': 'hi'}]
    tools = [{'type': 'function', 'function': {'name': 'calculator'}}]
    transport(FakeResponse(200, OK))
    _, record = send(URL, messages=messages, tools=tools)
    messages.append({'role': 'assistant', 'content': 'later'})
    messages[0]['content'] = 'changed'
    tools[0]['function']['name'] = 'changed'
    assert record['messages'] == [{'role': 'user', 'content': 'hi'}]
    assert record['tools'] == [{'type': 'function',
                                'function': {'name': 'calculator'}}]


@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.2')
@pytest.mark.parametrize('status', [301, 302, 307, 308])
def test_send_redirect_not_followed_http_error(transport, status):
    # SPEC R0.2: no network call to any host but the configured endpoint.
    # requests is told not to follow redirects, and a 3xx is an HTTP
    # error like any other non-200 status, never retried.
    t = transport(FakeResponse(status, text=''))
    with pytest.raises(HTTPError) as e:
        send(URL, messages=MESSAGES)
    assert e.value.status_code == status
    assert [c['allow_redirects'] for c in t.calls] == [False]


def test_send_request_record_defaults(transport):
    _, _, record = ok_send(transport)
    assert (record['model'], record['tools'], record['sampling_as_sent']) \
        == ('', None, {})


def test_send_api_key_not_in_request_record(transport):
    _, _, record = ok_send(transport, api_key='sk-secretsecretsecret')
    assert 'sk-secret' not in json.dumps(record)


# -- transport failures and retries ---------------------------------------

@pytest.mark.req('R0.2')
def test_send_retries_transport_failure_then_succeeds(transport):
    t = transport(requests.ConnectionError('refused'),
                  requests.Timeout('slow'), FakeResponse(200, OK))
    raw, record = send(URL, messages=MESSAGES)
    assert raw == OK
    assert len(t.calls) == 3
    assert t.sleeps == [1.0, 1.0]
    assert record['attempts'] == [
        {'attempt': 1, 'status_code': None, 'error': 'refused',
         'timestamp': 1000.5},
        {'attempt': 2, 'status_code': None, 'error': 'slow',
         'timestamp': 1000.5},
        {'attempt': 3, 'status_code': 200, 'error': None,
         'timestamp': 1000.5}]


def test_send_transport_failure_every_attempt_raises(transport):
    t = transport(*[requests.ConnectionError(f'e{i}') for i in range(3)])
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES)
    assert type(e.value) is AdapterError
    assert str(e.value) == 'transport failure after 3 attempts: e2'
    # the unmasked transport exception is not chained (see below)
    assert e.value.__cause__ is None and e.value.__suppress_context__
    assert len(t.calls) == 3
    assert t.sleeps == [1.0, 1.0]   # no sleep after the last attempt


def test_send_non_requests_exception_not_retried(transport):
    t = transport(RuntimeError('bug'))
    with pytest.raises(RuntimeError, match='bug'):
        send(URL, messages=MESSAGES)
    assert len(t.calls) == 1


def test_send_no_attempts_allowed_raises_exhausted(transport, monkeypatch):
    # Unreachable with MAX_RETRIES >= 1.
    monkeypatch.setattr(adapter, 'MAX_RETRIES', 0)
    t = transport()
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES)
    assert str(e.value) == 'exhausted retries with no response'
    assert t.calls == []


# -- HTTP errors ----------------------------------------------------------

@pytest.mark.req('R0.2')
def test_send_429_raises_rate_limit_without_retry(transport):
    t = transport(FakeResponse(429, text='slow down ' + 'x' * 300))
    with pytest.raises(RateLimitError) as e:
        send(URL, messages=MESSAGES)
    assert str(e.value) == 'rate limited (HTTP 429): ' + \
        ('slow down ' + 'x' * 300)[:200]
    assert len(t.calls) == 1
    assert t.sleeps == []


def test_send_429_body_masked(transport):
    transport(FakeResponse(429, text='key sk-abcdefghijklmnop bad'))
    with pytest.raises(RateLimitError) as e:
        send(URL, messages=MESSAGES)
    assert str(e.value) == 'rate limited (HTTP 429): key [REDACTED] bad'


@pytest.mark.req('R0.2')
def test_send_non_200_raises_http_error_without_retry(transport):
    text = 'E' * 3000
    t = transport(FakeResponse(500, text=text))
    with pytest.raises(HTTPError) as e:
        send(URL, messages=MESSAGES)
    assert str(e.value) == 'HTTP 500: ' + 'E' * 500
    assert e.value.status_code == 500
    assert e.value.body == 'E' * 2000
    assert len(t.calls) == 1


def test_send_http_error_body_and_message_masked(transport):
    text = '{"error": "Incorrect API key provided: sk-proj-ABCDEFGHIJKL"}'
    transport(FakeResponse(401, text=text))
    with pytest.raises(HTTPError) as e:
        send(URL, messages=MESSAGES)
    masked = '{"error": "Incorrect API key provided: [REDACTED]"}'
    assert str(e.value) == 'HTTP 401: ' + masked
    assert e.value.body == masked


def test_send_other_success_codes_are_http_errors(transport):
    transport(FakeResponse(201, OK))
    with pytest.raises(HTTPError) as e:
        send(URL, messages=MESSAGES)
    assert e.value.status_code == 201


def test_send_200_not_json_raises_adapter_error(transport):
    text = '<html> sk-abcdefghijklmnop ' + 'x' * 300
    transport(FakeResponse(200, text=text))
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES)
    assert type(e.value) is AdapterError
    assert str(e.value) == 'response is not valid JSON: ' + \
        text[:200].replace('sk-abcdefghijklmnop', '[REDACTED]')
    # not chained: the JSON error's .doc holds the whole unmasked body
    assert e.value.__cause__ is None and e.value.__suppress_context__


def test_send_200_not_json_truncated_before_masking(transport):
    # The text is cut to 200 characters first, then masked.
    transport(FakeResponse(200, text='y' * 195 + 'sk-abcdefghijklmnop'))
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES)
    assert str(e.value).endswith('y' * 195 + 'sk-ab')


# -- _mask_credentials ----------------------------------------------------

@pytest.mark.parametrize('secret', [
    'sk-proj-abcdefghij', 'sk-abcdefghij', 'sk-abc_def-ghij',
    'ghp_ABCDEFGHIJ', 'gho_ABCDEFGHIJ', 'github_pat_ABCDEFGH_IJ',
    'rpa_ABCDEFGHIJ', 'Bearer abc.def-ghi_j', 'Bearer   abcdefghij',
])
def test_mask_credentials_redacts_each_shape(secret):
    assert _mask_credentials(f'x {secret} y') == 'x [REDACTED] y'


@pytest.mark.parametrize('text', [
    'sk-abcdefghi', 'ghp_ABCDEFGHI', 'gho_abc-defghij', 'rpa_abcdefghi',
    'Bearer short', 'github_pat_ABCDEFGHI',
])
def test_mask_credentials_short_or_other_shapes_kept(text):
    assert _mask_credentials(text) == text


def test_mask_credentials_keeps_urls_and_status():
    text = 'HTTP 401 at https://api.example.com/v1 for sk-abcdefghijklmnop.'
    assert _mask_credentials(text) == \
        'HTTP 401 at https://api.example.com/v1 for [REDACTED].'


def test_mask_credentials_several_secrets():
    assert _mask_credentials('sk-aaaaaaaaaa and ghp_bbbbbbbbbb') == \
        '[REDACTED] and [REDACTED]'


@pytest.mark.parametrize('empty', ['', None])
def test_mask_credentials_empty_returned_as_is(empty):
    assert _mask_credentials(empty) is empty


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('S3-G1-18')
@pytest.mark.req('R0.2')
def test_send_transport_failure_exception_carries_attempt_log(transport):
    # send()'s docstring and SPEC R0.2: retries "bounded, every attempt
    # logged". When all attempts fail, the AdapterError carries the request
    # record with its attempts (attribute name proposed here:
    # request_record, as send() returns on success).
    transport(*[requests.ConnectionError('x')] * 3)
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES)
    record = getattr(e.value, 'request_record', None) or {}
    assert [a['attempt'] for a in record.get('attempts', [])] == [1, 2, 3]


@pytest.mark.finding('S3-G1-19')
@pytest.mark.req('R0.2')
def test_send_non_finite_sampling_value_never_reaches_the_wire(transport):
    # A request body must be valid JSON; json.dumps writes float('nan') as
    # the non-JSON token NaN. Correct: refuse a non-finite sampling value
    # (here or, better, at config load), never send it.
    t = transport(FakeResponse(200, OK))
    try:
        send(URL, messages=MESSAGES, sampling={'temperature': 'NaN'})
        json.dumps(t.calls[0]['json'], allow_nan=False)
        outcome = 'sent as valid JSON'
    except (AdapterError, ValueError) as e:
        outcome = ('refused' if not t.calls
                   else f'sent invalid JSON: {e}')
    assert outcome in ('refused', 'sent as valid JSON'), outcome


@pytest.mark.finding('S3-G1-20')
@pytest.mark.req('R0.2')
def test_send_transport_error_text_is_masked(transport):
    # Rule 0c (adapter.py): credential-shaped text is redacted "BEFORE any
    # error text enters an exception, transcript, or log"; the transport
    # exception's text is error text too.
    transport(*[requests.ConnectionError('GET ?key=sk-abcdefghijklmnop')] * 3)
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES)
    assert 'sk-abcdefghijklmnop' not in str(e.value)
    assert '[REDACTED]' in str(e.value)


@pytest.mark.finding('S3-G1-21')
@pytest.mark.req('R0.2')
@pytest.mark.parametrize('key', ['model', 'messages', 'tools'])
def test_send_sampling_key_cannot_overwrite_body_field(transport, key):
    # SPEC R0.2: the request record is "the request AS SENT". A sampling
    # key that names a body field is refused before anything is sent, or
    # cannot change that field: the caller's own model, messages and tools
    # are what is sent and what is recorded. (Recording the overwritten
    # value faithfully is not enough.)
    tools = [{'type': 'function', 'function': {'name': 'calculator'}}]
    original = {'model': 'm', 'messages': MESSAGES, 'tools': tools}[key]
    t = transport(FakeResponse(200, OK))
    try:
        _, record = send(URL, messages=MESSAGES, model='m', tools=tools,
                         sampling={key: 'other'})
        sent = t.calls[0]['json'][key]
        outcome = ('kept' if sent == record[key] == original
                   else f'sent {sent!r}, recorded {record[key]!r}')
    except (AdapterError, ValueError) as e:
        outcome = 'refused' if not t.calls else f'raised after send: {e}'
    assert outcome in ('refused', 'kept'), outcome


# --- Number grammar and transport hardening (S3-G1) ---

@pytest.mark.finding('S3-G1-19')
@pytest.mark.parametrize('value', ['NaN', 'Infinity', '-inf', 'sNaN'])
def test_send_non_finite_sampling_value_refused_before_sending(transport,
                                                               value):
    t = transport(FakeResponse(200, OK))
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES, sampling={'temperature': value})
    assert str(e.value) == (f'sampling.temperature: not a finite number: '
                            f'{value!r}; not sent')
    assert t.calls == []


@pytest.mark.finding('S3-G1-21')
@pytest.mark.parametrize('key', BODY_FIELDS)
def test_send_sampling_body_field_refused_before_sending(transport, key):
    t = transport(FakeResponse(200, OK))
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES, sampling={key: 'x'})
    assert str(e.value) == (f'sampling.{key}: names a request body field; '
                            f'not sent')
    assert t.calls == []


def test_body_fields_are_model_messages_tools():
    assert BODY_FIELDS == ('model', 'messages', 'tools')


@pytest.mark.finding('S3-G1-18', 'S3-G1-20')
def test_send_transport_failure_record_is_the_request_with_masked_attempts(
        transport):
    transport(*[requests.ConnectionError('GET ?key=sk-abcdefghijklmnop')] * 3)
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES, model='m',
             sampling={'temperature': '0'})
    assert str(e.value) == \
        'transport failure after 3 attempts: GET ?key=[REDACTED]'
    assert e.value.request_record == {
        'endpoint_url': URL, 'model': 'm', 'messages': MESSAGES,
        'tools': None, 'sampling_as_sent': {'temperature': '0'},
        'attempts': [{'attempt': i, 'status_code': None,
                      'error': 'GET ?key=[REDACTED]', 'timestamp': 1000.5}
                     for i in (1, 2, 3)]}


@pytest.mark.finding('S3-G1-18')
def test_adapter_error_without_transport_failure_has_no_record():
    assert AdapterError('x').request_record is None
    assert RateLimitError('x').request_record is None


def test_send_non_numeric_sampling_string_sent_as_is(transport):
    t, _, record = ok_send(transport, sampling={'reasoning_effort': 'low'})
    assert t.calls[0]['json']['reasoning_effort'] == 'low'
    assert record['sampling_as_sent'] == {'reasoning_effort': 'low'}


@pytest.mark.finding('S3-G1-20')
@pytest.mark.parametrize('failure', ['transport', 'not-json'])
def test_send_formatted_traceback_carries_no_credential(transport, failure):
    # Rule 0c: no credential in any exception text. The traceback a
    # caller prints shows the chained exceptions too, so the unmasked
    # original must not be chained to the masked one.
    import traceback
    secret = 'sk-abcdefghijklmnopqrst'
    if failure == 'transport':
        transport(*[requests.ConnectionError(f'GET ?key={secret}')] * 3)
    else:
        transport(FakeResponse(200, text=f'not json {secret}'))
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES)
    text = ''.join(traceback.format_exception(e.value))
    assert secret not in text and 'sk-abcdef' not in text, text


@pytest.mark.finding('S3-G1-19')
@pytest.mark.parametrize('value', ['9' * 400 + '.5', '1e-400'],
                         ids=['overflows-to-infinity', 'underflows-to-zero'])
def test_send_refuses_a_sampling_value_with_no_finite_float(transport, value):
    # A finite, non-integral Decimal whose float is inf (sent as the
    # non-JSON token Infinity) or 0.0 (sent, while the record says
    # 1e-400) is refused before any request.
    t = transport(FakeResponse(200, payload={}))
    with pytest.raises(AdapterError, match='no finite non-zero float'):
        send(URL, messages=MESSAGES, sampling={'temperature': value})
    assert t.calls == []


# -- No proxy from the environment (SPEC R0.2 single-host egress) ----------

PROXY_VARIABLES = ('HTTP_PROXY', 'http_proxy', 'HTTPS_PROXY', 'https_proxy',
                   'ALL_PROXY', 'all_proxy', 'NO_PROXY', 'no_proxy')


@pytest.fixture
def proxy(monkeypatch):
    """A local HTTP server that answers any request as a proxy would, and
    records what reached it; and a closed local port for the endpoint."""
    import socket
    import threading
    from http.server import BaseHTTPRequestHandler, HTTPServer

    seen = []

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get('Content-Length') or 0)
            seen.append((self.path, self.headers.get('Authorization'),
                         self.rfile.read(length)))
            body = json.dumps({'choices': [{'message': {
                'role': 'assistant', 'content': 'from the proxy'}}]})
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body.encode())

        def log_message(self, *args):
            pass

    server = HTTPServer(('127.0.0.1', 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    with socket.socket() as s:
        s.bind(('127.0.0.1', 0))
        closed = s.getsockname()[1]
    for name in PROXY_VARIABLES:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(adapter.time, 'sleep', lambda seconds: None)
    yield SimpleNamespace(
        url=f'http://127.0.0.1:{server.server_port}', seen=seen,
        endpoint=f'http://127.0.0.1:{closed}/v1/chat/completions')
    server.shutdown()
    server.server_close()


@pytest.mark.finding('T3-52')
@pytest.mark.req('R0.2')
@pytest.mark.parametrize('variable', ['HTTP_PROXY', 'http_proxy',
                                      'ALL_PROXY', 'all_proxy'])
def test_send_ignores_a_proxy_named_in_the_environment(proxy, monkeypatch,
                                                       variable):
    # SPEC R0.2: "The adapter makes no network call to any host other than
    # the configured endpoint". A proxy named in the environment is never
    # contacted: the request (the key, the fixture data) goes only to the
    # endpoint, here a closed port, so the send fails.
    monkeypatch.setenv(variable, proxy.url)
    with pytest.raises(AdapterError, match='transport failure'):
        adapter.send(proxy.endpoint, messages=[
            {'role': 'user', 'content': 'FIXTURE DATA 15200'}],
            model='m', api_key='sk-test-not-a-real-key-000')
    assert proxy.seen == []


def test_proxy_fixture_proxy_answers_when_asked(proxy):
    # The fixture's proxy is reachable and answers: the test above would
    # see it if the adapter used it.
    r = requests.post(proxy.url + '/x', json={}, timeout=5)
    assert r.json()['choices'][0]['message']['content'] == 'from the proxy'
    assert len(proxy.seen) == 1
