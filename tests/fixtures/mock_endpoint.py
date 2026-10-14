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
  in a standard envelope.

Every request is logged (self.log) for the golden output.
"""

import json
import re
import threading
from decimal import Decimal, ROUND_HALF_UP
from http.server import BaseHTTPRequestHandler, HTTPServer


class MockEndpoint:
    """A scripted chat-completions server on 127.0.0.1, in a thread."""

    def __init__(self, *, questions, system_prompts, responses=None,
                 replay_records=None):
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
        self.log = []
        self._server = None
        self._thread = None

    # -- lifecycle --------------------------------------------------

    def start(self):
        endpoint = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                length = int(self.headers.get('Content-Length', 0))
                body = json.loads(self.rfile.read(length).decode('utf-8'))
                action = endpoint.handle(body)
                if action[0] == 'close':
                    self.close_connection = True
                    try:
                        self.connection.shutdown(2)
                    except OSError:
                        pass
                    return
                status, payload = action[1], action[2]
                data = (payload if isinstance(payload, str)
                        else json.dumps(payload)).encode('utf-8')
                self.send_response(status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
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
        return f'http://{host}:{port}/v1/chat/completions'

    def stop(self):
        if self._server:
            self._server.shutdown()
            self._server.server_close()

    # -- request handling -------------------------------------------

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
        if rnd < len(assistant):
            return ('reply', 200, self._envelope(assistant[rnd])), source
        if rec.get('response_received') is None:
            return ('reply', 503, str(rec.get('error_state'))), source
        return ('reply', 200, rec['response_received']), source

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

    def _envelope(self, message):
        finish = 'tool_calls' if message.get('tool_calls') else 'stop'
        return {
            'id': f'chatcmpl-mock-{self._seq}',
            'object': 'chat.completion',
            'created': 0,
            'model': 'mock-model',
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
