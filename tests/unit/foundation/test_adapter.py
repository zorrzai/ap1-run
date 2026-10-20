"""Unit tests for the R0.2 endpoint adapter (foundation/adapter.py).

No network: requests.post and time.sleep are replaced by fakes. The real
HTTP path is covered end to end by the regression scenarios, which run
against tests/fixtures/mock_endpoint.py (clean, transport_errors, ...).
"""

import json

import pytest
import requests

from ap1_run.foundation import adapter
from ap1_run.foundation.adapter import (
    MAX_RETRIES, RETRY_DELAY, AdapterError, HTTPError, RateLimitError,
    _mask_credentials, send,
)

URL = 'http://endpoint.test/v1/chat/completions'
MESSAGES = [{'role': 'user', 'content': 'hi'}]
OK = {'choices': [{'message': {'role': 'assistant', 'content': '42'}}]}


class FakeResponse:
    def __init__(self, status_code=200, payload=None, text=None):
        self.status_code = status_code
        self._payload = payload
        if text is None:
            text = json.dumps(payload) if payload is not None else ''
        self.text = text

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
        monkeypatch.setattr(adapter._requests, 'post', t.post)
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
    assert raw is OK


def test_send_minimal_body_and_headers(transport):
    t, _, _ = ok_send(transport)
    assert t.calls == [{
        'url': URL,
        'json': {'model': '', 'messages': MESSAGES},
        'headers': {'Content-Type': 'application/json'},
        'timeout': 120}]


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


def test_send_infinite_sampling_value_sent_as_string(transport):
    # int(Decimal('Infinity')) raises, and the except keeps the text.
    t, _, _ = ok_send(transport, sampling={'max_tokens': 'Infinity'})
    assert t.calls[0]['json']['max_tokens'] == 'Infinity'


@pytest.mark.finding('S3-G1-19')
def test_send_nan_sampling_value_sent_as_float_nan(transport):
    # Current behaviour: 'NaN' is not integral, so it is sent as
    # float('nan'), which json.dumps writes as the non-JSON token NaN.
    # Correct: refuse a non-finite sampling value (at config load).
    t, _, _ = ok_send(transport, sampling={'temperature': 'NaN'})
    v = t.calls[0]['json']['temperature']
    assert type(v) is float and v != v


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


@pytest.mark.finding('S3-G1-21')
def test_send_sampling_key_overrides_body_field(transport):
    # Current behaviour: sampling keys are written into the same body as
    # model and messages, so a sampling 'model' replaces the configured
    # model (the request record still shows 'm'). Correct: refuse sampling
    # keys that name body fields.
    t, _, _ = ok_send(transport, model='m', sampling={'model': 'other'})
    assert t.calls[0]['json']['model'] == 'other'


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
    assert raw is OK
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
    assert isinstance(e.value.__cause__, requests.ConnectionError)
    assert len(t.calls) == 3
    assert t.sleeps == [1.0, 1.0]   # no sleep after the last attempt


@pytest.mark.finding('S3-G1-18')
def test_send_transport_failure_attempts_not_reachable(transport):
    # Current behaviour: the attempt log is written into a request_record
    # that is never returned or attached to the exception, so the caller
    # cannot record the attempts ("every attempt logged"). Correct: the
    # exception carries the request record with its attempts.
    transport(*[requests.ConnectionError('x')] * 3)
    with pytest.raises(AdapterError) as e:
        send(URL, messages=MESSAGES)
    assert not hasattr(e.value, 'request_record')
    assert not hasattr(e.value, 'attempts')


@pytest.mark.finding('S3-G1-20')
def test_send_transport_error_text_not_masked(transport):
    # Current behaviour: HTTP error bodies are masked, but the transport
    # exception text goes into the message unmasked. Correct: mask it too
    # (a URL with a key in its query string would leak).
    transport(*[requests.ConnectionError('GET ?key=sk-abcdefghijklmnop')] * 3)
    with pytest.raises(AdapterError, match='sk-abcdefghijklmnop'):
        send(URL, messages=MESSAGES)


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
    assert isinstance(e.value.__cause__, ValueError)


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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-18: the attempt log of a failed send is '
                          'not reachable from the exception')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-19: a NaN sampling value is sent as '
                          'float nan, which is not JSON')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-20: the transport exception text is not '
                          'masked')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-21: a sampling key named like a body field '
                          'overwrites it; the request record disagrees with '
                          'what was sent')
@pytest.mark.parametrize('key', ['model', 'messages'])
def test_send_sampling_key_cannot_overwrite_body_field(transport, key):
    # SPEC R0.2: the request record is "the request AS SENT". A sampling
    # key that names a body field is refused, or cannot change that field.
    t = transport(FakeResponse(200, OK))
    try:
        _, record = send(URL, messages=MESSAGES, model='m',
                         sampling={key: 'other'})
        sent = t.calls[0]['json'][key]
        outcome = ('kept' if sent == record[key]
                   else f'sent {sent!r}, recorded {record[key]!r}')
    except (AdapterError, ValueError) as e:
        outcome = 'refused' if not t.calls else f'raised after send: {e}'
    assert outcome in ('refused', 'kept'), outcome
