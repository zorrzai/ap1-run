"""Mock OpenAI-compatible chat-completions endpoint for regression runs.

Serves canned model responses, so a live run of the runner is
deterministic: the model is the only source of randomness in a run, and
scripting it is the equivalent of fixing an RNG seed.

A real local HTTP server is used (not a stub of `requests`), so the
runner's actual adapter and transport code runs.

Each request is identified from its own content:
  item       -- the "Question: <text>" line of the user message
  condition  -- the system prompt (base or instruction_removed)
  repeat     -- a per-(item, condition) counter, advanced on round 0
  round      -- the number of assistant messages already in the request

Two kinds of script:

  Scripted turns ("responses" in a scenario file). Keys are
  "item/condition/rN" with "*" wildcards; the most specific key wins:
      Q01/base/r2, Q01/base/*, Q01/*/r2, Q01/*/*,
      */base/r2,  */base/*,  */*/r2,  */*/*
  Each value is a list of turns, one per round. A turn is a dict:
      {"call": "1 + 2"}                  one calculator call
      {"calls": ["1 + 2", {"name": "x", "arguments": "{...}"}]}
      {"say": "The answer is ${result}."}
                                         final text; {result} is the last
                                         tool result rounded to 2 places
      {"call": ..., "say": ...}          both, in one message
      {"raw": {...}}                     this exact JSON body
      {"http": 429, "body": "..."}       an HTTP error status
      {"close": true}                    drop the connection (transport failure)
  A round beyond the end of the list gets HTTP 500 "mock script exhausted".

  Replay ("replay" in a scenario file): a published transcript
  (smoke_run.jsonl). Execution n of (item, condition) replays the n-th
  engine record: its assistant messages for the intermediate rounds,
  then its recorded final response. The intermediate rounds were kept
  only as messages, not as full responses (V12-3), so they are wrapped
  in a standard envelope. That envelope names the model the recorded
  final response names, so every round of a replay is served by the
  model the run recorded, not by the mock.
  A replay re-scores the published session, so each tool call is
  answered with the return the published run recorded for it
  (recorded_tool_return), never by running today's tool: the
  system's later messages copy the returns it actually received.

Every request is logged (self.log) for the golden output.

Transport contract: a request must POST to /v1/chat/completions with
"Authorization: Bearer <api_key>". Any other request is refused (405 for
any method but POST, 404 for the path, 401 for the credential) before it
is identified, so it advances no scripted state, and is recorded in
self.violations (the kind, the path and, for a method refusal, the
method; never header names or values). The regression harness fails a
run with any violation, also under --update.
"""

import json
import re
import threading
from decimal import Decimal, ROUND_HALF_UP
from http.server import BaseHTTPRequestHandler, HTTPServer


PATH = '/v1/chat/completions'
MOCK_MODEL = 'mock-model'   # the model a scripted (not replayed) turn names


class ReplayToolReturnError(Exception):
    """A replayed tool call whose recorded return can't be found."""


class MockEndpoint:
    """A scripted chat-completions server on 127.0.0.1, in a thread."""

    def __init__(self, *, questions, system_prompts, api_key, responses=None,
                 replay_records=None):
        self._authorization = f'Bearer {api_key}'
        self.violations = []
        self._question_ids = {
            item['text']: item['id'] for item in questions['items']}
        self._conditions = system_prompts  # {prompt text: condition}
        self._responses = responses or {}
        self._replay = None
        if replay_records is not None:
            self._replay = {}
            for rec in replay_records:
                if rec.get('record_type') == 'figure_identification':
                    continue
                key = (rec.get('item_id'), rec.get('condition'))
                self._replay.setdefault(key, []).append(rec)
        self._repeat = {}
        self._seq = 0
        # Replay: the recorded tool calls, with their returns, of the
        # response last served, in the order it asks for them.
        self._pending_returns = []
        self._served_from = None
        self.log = []
        self._server = None
        self._thread = None

    # -- lifecycle --------------------------------------------------

    def start(self):
        endpoint = self

        class Handler(BaseHTTPRequestHandler):
            def __getattr__(self, name):
                # BaseHTTPRequestHandler looks up do_<METHOD> and answers
                # a missing one with 501 itself, unrecorded. Every method
                # but POST comes here instead, so it is refused and
                # recorded like any other contract violation.
                if name.startswith('do_') and name != 'do_POST':
                    return self._refuse_method
                raise AttributeError(name)

            def _refuse_method(self):
                length = int(self.headers.get('Content-Length', 0) or 0)
                if length:
                    self.rfile.read(length)
                status, payload = endpoint.method_refusal(
                    self.command, self.path)
                self._send(status, payload, allow='POST',
                           body=self.command != 'HEAD')

            def do_POST(self):
                length = int(self.headers.get('Content-Length', 0))
                data = self.rfile.read(length)
                refused = endpoint.refusal(
                    self.path, self.headers.get('Authorization'))
                if refused:
                    self._send(*refused)
                    return
                body = json.loads(data.decode('utf-8'))
                action = endpoint.handle(body)
                if action[0] == 'close':
                    self.close_connection = True
                    try:
                        self.connection.shutdown(2)
                    except OSError:
                        pass
                    return
                self._send(action[1], action[2])

            def _send(self, status, payload, allow=None, body=True):
                data = (payload if isinstance(payload, str)
                        else json.dumps(payload)).encode('utf-8')
                self.send_response(status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(data)))
                if allow:
                    self.send_header('Allow', allow)
                self.end_headers()
                if body:
                    self.wfile.write(data)

            def log_message(self, *args):
                pass

        self._server = HTTPServer(('127.0.0.1', 0), Handler)
        self._thread = threading.Thread(
            target=self._server.serve_forever, daemon=True)
        self._thread.start()
        return self

    @property
    def url(self):
        host, port = self._server.server_address
        return f'http://{host}:{port}{PATH}'

    def point_config(self, config_path, model='mock-model'):
        """Rewrite the run config at config_path so that the run sends
        to this mock, as model: the runner takes the endpoint and model
        from the config alone (T3-80). Call after start()."""
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
        config['endpoint_url'] = self.url
        config['model'] = model
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
            f.write('\n')

    def stop(self):
        if self._server:
            self._server.shutdown()
            self._server.server_close()

    # -- request handling -------------------------------------------

    def method_refusal(self, method, path):
        """(status, body) refusing a request whose method is not POST,
        recorded in self.violations."""
        self.violations.append({'kind': 'method', 'method': method,
                                'path': path})
        return 405, {'error': {'message': f'mock: method {method} not '
                                          f'allowed, only POST',
                               'type': 'invalid_request_error'}}

    def refusal(self, path, authorization):
        """(status, body) refusing a request outside the transport
        contract, recorded in self.violations; None for a valid one."""
        if path != PATH:
            self.violations.append({'kind': 'path', 'path': path})
            return 404, {'error': {'message': f'mock: no route {path}',
                                   'type': 'invalid_request_error'}}
        if authorization != self._authorization:
            self.violations.append({'kind': 'credential', 'path': path})
            return 401, {'error': {'message': 'mock: missing or wrong '
                                              'bearer credential',
                                   'type': 'invalid_request_error'}}
        return None

    def _identify(self, body):
        messages = body.get('messages', [])
        condition = '?'
        item_id = '?'
        for m in messages:
            if m.get('role') == 'system':
                condition = self._conditions.get(m.get('content'), '?')
            elif m.get('role') == 'user':
                match = re.search(r'Question: (.*)\Z', m.get('content') or '',
                                  re.S)
                if match:
                    item_id = self._question_ids.get(match.group(1), '?')
        rnd = sum(1 for m in messages if m.get('role') == 'assistant')
        return item_id, condition, rnd

    def handle(self, body):
        item_id, condition, rnd = self._identify(body)
        key = (item_id, condition)
        if rnd == 0 and not self._is_retry(key, body):
            self._repeat[key] = self._repeat.get(key, 0) + 1
        repeat = self._repeat.get(key, 0)
        self._seq += 1

        if self._replay is not None:
            action, source = self._replay_turn(key, repeat, rnd)
            self._expect_tool_calls(key, repeat, action, source)
        else:
            action, source = self._scripted_turn(
                item_id, condition, repeat, rnd, body)

        self.log.append({
            'seq': self._seq, 'item_id': item_id, 'condition': condition,
            'repeat': repeat, 'round': rnd, 'script_key': source,
            'reply': action[0] if action[0] == 'close' else action[1],
            'request': body,
        })
        self._last_body = (key, rnd, json.dumps(body, sort_keys=True))
        return action

    def _is_retry(self, key, body):
        """True if this round-0 request repeats the previous request
        exactly (the adapter retrying after a transport failure)."""
        last = getattr(self, '_last_body', None)
        return (last is not None and last[0] == key and last[1] == 0
                and last[2] == json.dumps(body, sort_keys=True)
                and self.log and self.log[-1]['reply'] == 'close')

    def _scripted_turn(self, item_id, condition, repeat, rnd, body):
        keys = [f'{i}/{c}/{r}'
                for i in (item_id, '*') for c in (condition, '*')
                for r in (f'r{repeat}', '*')]
        for k in keys:
            if k in self._responses:
                turns = self._responses[k]
                if rnd < len(turns):
                    return self._render(turns[rnd], body, rnd), k
                return ('reply', 500, 'mock script exhausted'), k
        return ('reply', 500, 'no script for this request'), None

    def _replay_turn(self, key, repeat, rnd):
        records = self._replay.get(key, [])
        if repeat < 1 or repeat > len(records):
            return ('reply', 500, 'no recorded execution'), None
        rec = records[repeat - 1]
        source = f'{key[0]}/{key[1]}/r{repeat}'
        rr = (rec.get('request_sent') or {}).get('request_record') or {}
        assistant = [m for m in rr.get('messages', [])
                     if m.get('role') == 'assistant']
        final = rec.get('response_received')
        if final is None:
            return ('reply', 503, str(rec.get('error_state'))), source
        model = self._model_of(final)
        # A recorded final response that still asks for tools means the
        # loop ended because the next request failed (a mid-loop failure,
        # EV-0). That response is also the last assistant message.
        unfinished = bool(self._tool_calls_of(final))
        n_before_final = len(assistant) - 1 if unfinished else len(assistant)
        if rnd < n_before_final:
            return ('reply', 200,
                    self._envelope(assistant[rnd], model)), source
        if rnd == n_before_final:
            return ('reply', 200, final), source
        if unfinished:
            return ('reply', 502,
                    'replayed mid-loop failure: the recorded loop ended '
                    'here without a response'), source
        return ('reply', 500, 'mock script exhausted'), source

    def _expect_tool_calls(self, key, repeat, action, source):
        """After serving a replayed response, line up the recorded return
        of each tool call it asks for, matched by the call's id within
        the same execution's record."""
        self._pending_returns = []
        self._served_from = source
        if action[0] != 'reply' or action[1] != 200:
            return
        calls = self._tool_calls_of(action[2]) or []
        if not calls:
            return
        rec = self._replay[key][repeat - 1]
        recorded = {tc.get('id'): tc for tc in rec.get('tool_calls') or []}
        for call in calls:
            self._pending_returns.append(
                (call.get('id'), call.get('function') or {},
                 recorded.get(call.get('id'))))

    def recorded_tool_return(self, name, arguments_json):
        """The return value the published run recorded for the next tool
        call of the replayed response last served: the tool executor of
        a replay (the driver installs it in place of the engine's).

        The call must be the one the record holds (same name and
        arguments), and the record must hold its return; anything else
        raises ReplayToolReturnError. There is no fallback to running
        the tool, which would score the session against a return the
        system never received.
        """
        where = self._served_from or 'no replayed response'
        if not self._pending_returns:
            raise ReplayToolReturnError(
                f'{where}: tool call {name!r} {arguments_json!r} after a '
                f'response that asked for no (more) tool calls')
        call_id, function, recorded = self._pending_returns.pop(0)
        if recorded is None:
            raise ReplayToolReturnError(
                f'{where}: the record has no tool call with id {call_id!r}')
        if (name != function.get('name')
                or arguments_json != function.get('arguments', '{}')):
            raise ReplayToolReturnError(
                f'{where}: tool call {call_id!r} executed as {name!r} '
                f'{arguments_json!r}, served as {function!r}')
        rec_function = recorded.get('function') or {}
        if (rec_function.get('name') != function.get('name')
                or rec_function.get('arguments')
                != function.get('arguments')):
            raise ReplayToolReturnError(
                f'{where}: tool call {call_id!r} is served as {function!r} '
                f'but recorded as {rec_function!r}')
        if 'return_value' not in recorded:
            raise ReplayToolReturnError(
                f'{where}: tool call {call_id!r} has no recorded '
                f'return_value')
        return recorded['return_value']

    @staticmethod
    def _model_of(response):
        """The model a recorded response names; the mock's own name if
        it names none."""
        model = (response.get('model') if isinstance(response, dict)
                 else None)
        return model if isinstance(model, str) and model else MOCK_MODEL

    @staticmethod
    def _tool_calls_of(response):
        try:
            return response['choices'][0]['message'].get('tool_calls')
        except (KeyError, IndexError, TypeError, AttributeError):
            return None

    # -- rendering --------------------------------------------------

    def _render(self, turn, body, rnd):
        if turn.get('close'):
            return ('close',)
        if 'http' in turn:
            return ('reply', turn['http'], turn.get('body', ''))
        if 'raw' in turn:
            return ('reply', 200, turn['raw'])
        message = {'role': 'assistant', 'content': None}
        calls = list(turn.get('calls', []))
        if 'call' in turn:
            calls.append(turn['call'])
        if calls:
            message['tool_calls'] = []
            for n, c in enumerate(calls, start=1):
                if isinstance(c, str):
                    c = {'name': 'calculator',
                         'arguments': json.dumps({'expression': c})}
                message['tool_calls'].append({
                    'id': c.get('id', f'call_r{rnd}_{n}'),
                    'type': 'function',
                    'function': {'name': c['name'],
                                 'arguments': c['arguments']},
                })
        if 'say' in turn:
            message['content'] = turn['say'].replace(
                '{result}', self._last_result(body))
        return ('reply', 200, self._envelope(message))

    def _envelope(self, message, model=None):
        finish = 'tool_calls' if message.get('tool_calls') else 'stop'
        return {
            'id': f'chatcmpl-mock-{self._seq}',
            'object': 'chat.completion',
            'created': 0,
            'model': model or MOCK_MODEL,
            'choices': [{'index': 0, 'message': message,
                         'finish_reason': finish}],
            'usage': {'prompt_tokens': 0, 'completion_tokens': 0,
                      'total_tokens': 0},
        }

    @staticmethod
    def _last_result(body):
        for m in reversed(body.get('messages', [])):
            if m.get('role') == 'tool':
                try:
                    value = json.loads(m.get('content'))['result']
                    return str(Decimal(str(value)).quantize(
                        Decimal('0.01'), rounding=ROUND_HALF_UP))
                except Exception:
                    return '?'
        return '?'
