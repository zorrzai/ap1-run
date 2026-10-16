"""Fixtures for the functional tests: a scripted chat-completions endpoint
on 127.0.0.1 and the shipped example (config, fixture, questions, ground
truth, calculator)."""

import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'


class ScriptedEndpoint:
    """Serves the queued bodies in order, one per POST; HTTP 500 when the
    queue is empty. A queued (status, text) tuple is sent as is."""

    def __init__(self):
        self.queue = []
        self.requests = []
        endpoint = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                length = int(self.headers.get('Content-Length', 0))
                endpoint.requests.append(json.loads(self.rfile.read(length)))
                if endpoint.queue:
                    item = endpoint.queue.pop(0)
                else:
                    item = (500, '{"error": "no scenarios left"}')
                status, text = item if isinstance(item, tuple) else \
                    (200, json.dumps(item))
                data = text.encode()
                self.send_response(status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def log_message(self, format, *args):
                pass

        self._server = HTTPServer(('127.0.0.1', 0), Handler)
        self.url = (f'http://127.0.0.1:{self._server.server_address[1]}'
                    '/v1/chat/completions')
        self._thread = threading.Thread(target=self._server.serve_forever,
                                        kwargs={"poll_interval": 0.02},
                                        daemon=True)
        self._thread.start()

    def close(self):
        self._server.shutdown()
        self._server.server_close()


@pytest.fixture
def endpoint():
    server = ScriptedEndpoint()
    yield server
    server.close()


def tool_call_turn(*expressions, name='calculator', ids=None):
    calls = [{'id': (ids or [f'call_{i + 1}' for i in range(len(expressions))])[i],
              'type': 'function',
              'function': {'name': name,
                           'arguments': json.dumps({'expression': e})}}
             for i, e in enumerate(expressions)]
    return {'choices': [{'index': 0, 'message': {
        'role': 'assistant', 'content': None, 'tool_calls': calls},
        'finish_reason': 'tool_calls'}], 'model': 'mock-v1'}


def text_turn(text):
    return {'choices': [{'index': 0, 'message': {
        'role': 'assistant', 'content': text}, 'finish_reason': 'stop'}],
        'model': 'mock-v1'}


@pytest.fixture
def example_modules(monkeypatch):
    """example/ first on sys.path, with calculator_tool and
    ground_truth_example imported fresh from it."""
    monkeypatch.syspath_prepend(str(EXAMPLE))
    for name in ('calculator_tool', 'ground_truth_example'):
        monkeypatch.delitem(sys.modules, name, raising=False)
    import calculator_tool
    import ground_truth_example
    return calculator_tool, ground_truth_example


@pytest.fixture
def example(example_modules):
    """The shipped example: config (loaded), fixture, questions, the
    ground-truth module."""
    from ap1_run.foundation.config import load_config
    config = load_config(EXAMPLE / 'config.json')
    fixture = json.loads((EXAMPLE / 'fixture.json').read_text('utf-8'))
    questions = json.loads((EXAMPLE / 'questions.json').read_text('utf-8'))
    return {'config': config, 'fixture': fixture,
            'items': questions['items'], 'gt': example_modules[1]}


@pytest.fixture
def turns():
    """Builders for scripted model turns: turns.calls(*expressions, name=,
    ids=) and turns.text(text)."""
    from types import SimpleNamespace
    return SimpleNamespace(calls=tool_call_turn, text=text_turn)
