"""Step 4, group g9: correct behaviour for the SPEC conformance claims and
the config rulings, end to end (failing until fixed).

Each test drives the real runner (``ap1_run.run.main``) against the mock
chat-completions endpoint the regression scenarios use
(``tests/fixtures/mock_endpoint.py``, which routes by question, condition
and repeat), on a copy of the shipped example in ``tmp_path``, with
``--fixture-dir`` and ``--output-dir`` there. Nothing is written into the
repository.

Tests marked ``xfail(strict=True)`` assert what SPEC (or Steven's ruling)
says is correct and fail on today's code; the fix removes the marker.
Unmarked tests assert R4.1 rows that today's live path already gets right.
"""

import json
import shutil
import sys
import time
from pathlib import Path
from types import SimpleNamespace

import pytest

from ap1_run import run as run_module
from ap1_run.foundation.config import load_config

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
FIXTURES = ROOT / 'tests' / 'fixtures'

EXAMPLE_FILES = ('fixture.json', 'questions.json', 'ground_truth_example.py',
                 'calculator_tool.py', 'config.json', 'config_mini.json')

# Every question answered correctly with a grounded call (regression
# scenario "clean").
CLEAN = json.loads((ROOT / 'tests' / 'regression' / 'scenarios' /
                    'clean.json').read_text('utf-8'))['responses']


@pytest.fixture
def ap1_run(tmp_path, monkeypatch, capsys):
    """run(responses=, config=, config_file=, questions=, env=, args=):
    one live run of the runner on a copy of example/ in tmp_path.

    config        dict of top-level fields to change in the config copy
                  (a value of ... removes the field); the copy has
                  repeat_count "1" and dimensions_claimed D2, D7 unless
                  changed here
    fixture_edit  function changing the fixture dict before the run
    config_file   which shipped config to copy (default config.json)
    questions     replacement list of question items
    env           extra environment variables

    Returns a namespace: exit (code or None), exception (or None), seals
    (the records create_seal returned), sealed_configs (the config each
    seal was made from), requests (the mock endpoint's log), out (console
    output), output_dir, transcript (records, [] if none).
    """
    monkeypatch.syspath_prepend(str(FIXTURES))
    from mock_endpoint import MockEndpoint

    # The runner prepends --fixture-dir to sys.path and imports
    # ground_truth_example and calculator_tool from it; undo both.
    monkeypatch.setattr(sys, 'path', list(sys.path))
    monkeypatch.setattr(sys, 'dont_write_bytecode', True)
    for name in ('ground_truth_example', 'calculator_tool'):
        monkeypatch.delitem(sys.modules, name, raising=False)
    monkeypatch.setattr(time, 'sleep', lambda seconds: None)

    def run(responses=CLEAN, config=None, config_file='config.json',
            questions=None, fixture_edit=None, env=None, args=()):
        fixture_dir = tmp_path / 'example'
        fixture_dir.mkdir(exist_ok=True)
        for name in EXAMPLE_FILES:
            shutil.copy(EXAMPLE / name, fixture_dir / name)
        config_path = fixture_dir / config_file
        cfg = json.loads(config_path.read_text('utf-8'))
        cfg['repeat_count'] = '1'
        # The shipped configs claim D1 on 10 items, which minimum-n (R0.1)
        # refuses once wired (T3-12). Tests not about minimum-n claim only
        # dimensions R0.1 sets no minimum for.
        cfg['dimensions_claimed'] = ['D2', 'D7']
        for key, value in (config or {}).items():
            if value is ...:
                cfg.pop(key, None)
            else:
                cfg[key] = value
        config_path.write_text(json.dumps(cfg, indent=2), 'utf-8')
        if fixture_edit is not None:
            fx = json.loads((fixture_dir / 'fixture.json').read_text('utf-8'))
            fixture_edit(fx)
            (fixture_dir / 'fixture.json').write_text(
                json.dumps(fx, indent=2), 'utf-8')
        q = json.loads((fixture_dir / 'questions.json').read_text('utf-8'))
        if questions is not None:
            q['items'] = questions
            (fixture_dir / 'questions.json').write_text(
                json.dumps(q, indent=2), 'utf-8')

        mock = MockEndpoint(
            questions=q, responses=responses,
            system_prompts={
                cfg['system_prompt_base']: 'base',
                cfg['system_prompt_instruction_removed']:
                    'instruction_removed'}).start()
        for name in ('AP1_SMOKE_TEMPERATURE', 'AP1_SMOKE_REASONING_EFFORT'):
            monkeypatch.delenv(name, raising=False)
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-test-not-a-real-key-0000')
        monkeypatch.setenv('AP1_SMOKE_ENDPOINT', mock.url)
        monkeypatch.setenv('AP1_SMOKE_MODEL', 'mock-model')
        for key, value in (env or {}).items():
            monkeypatch.setenv(key, value)

        seals, sealed_configs = [], []
        real_seal = run_module.create_seal

        def observed_seal(**kwargs):
            sealed_configs.append(json.loads(json.dumps(
                kwargs['config'], default=str)))
            record = real_seal(**kwargs)
            seals.append(record)
            return record
        monkeypatch.setattr(run_module, 'create_seal', observed_seal)

        output_dir = tmp_path / 'out'
        result = SimpleNamespace(exit=None, exception=None)
        try:
            result.exit = run_module.main(
                ['--config', str(config_path),
                 '--fixture-dir', str(fixture_dir),
                 '--output-dir', str(output_dir), *args])
        except SystemExit as e:
            result.exit = e.code
        except Exception as e:  # recorded; the tests assert on it
            result.exception = e
        finally:
            mock.stop()
        result.seals = seals
        result.sealed_configs = sealed_configs
        result.requests = mock.log
        result.out = capsys.readouterr().out
        result.output_dir = output_dir
        path = output_dir / 'smoke_run.jsonl'
        result.transcript = ([json.loads(line) for line in
                              path.read_text('utf-8').splitlines() if line]
                             if path.exists() else [])
        return result

    return run


def engine_records(result, item_id=None):
    return [r for r in result.transcript
            if r.get('record_type') != 'figure_identification'
            and (item_id is None or r['item_id'] == item_id)]


def figure_records(result, item_id=None):
    return [r for r in result.transcript
            if r.get('record_type') == 'figure_identification'
            and (item_id is None or r['item_id'] == item_id)]


def refused_before_any_request(result):
    """(refused, why): the run stopped with an error and sent nothing."""
    why = (f'exit={result.exit!r}, exception={result.exception!r}, '
           f'{len(result.requests)} requests sent, '
           f'{len(result.transcript)} transcript records')
    stopped = result.exception is not None or result.exit not in (0, None)
    return stopped and not result.requests and not result.transcript, why



def script(**items):
    """The clean script with the given items' turns replaced (both
    conditions, every repeat)."""
    responses = dict(CLEAN)
    for item_id, turns in items.items():
        responses[f'{item_id}/*/*'] = turns
    return responses


def raw_turn(message, **top_level):
    """One scripted turn sending this exact assistant message, with extra
    top-level response fields."""
    body = {'id': 'chatcmpl-raw', 'object': 'chat.completion', 'created': 0,
            'model': 'mock-model',
            'choices': [{'index': 0, 'message': message,
                         'finish_reason': 'stop'}]}
    body.update(top_level)
    return {'raw': body}


def base_record(result, item_id):
    records = [r for r in engine_records(result, item_id)
               if r['condition'] == 'base']
    assert records, f'no engine record for {item_id}/base: {result.out[-800:]}'
    return records[0]


def base_figure(result, item_id):
    records = [r for r in figure_records(result, item_id)
               if r['condition'] == 'base']
    assert records, f'no figure record for {item_id}/base'
    return records[0]


def report_text(result):
    return (result.output_dir / 'report.md').read_text('utf-8')


def sheet_sections(result):
    """{(item_id, condition): [sheet text, ...]} from
    adjudication_sheets.md."""
    import re
    text = (result.output_dir / 'adjudication_sheets.md').read_text('utf-8')
    sheets = {}
    for chunk in re.split(r'(?m)^## Item ', text)[1:]:
        m = re.match(r'\d+: (\S+) \(Condition: (\S+)\)', chunk)
        if m:
            sheets.setdefault((m.group(1), m.group(2)), []).append(chunk)
    return sheets


# --- T3-12 / R0.1 minimum-n, end to end ------------------------------------

@pytest.mark.finding('T3-12')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-12: minimum-n is never enforced live; the '
                          'shipped D1 claim on 10 items runs')
@pytest.mark.req('R0.1')
def test_run_shipped_config_d1_claim_on_ten_items_refused_before_any_request(
        ap1_run):
    # SPEC R0.1 (l.148-152): for each claimed dimension "the loader counts
    # eligible items and refuses the run" below the minimum (D1: >= 10 per
    # category; AP-1 v1.3 D1: minimum 40 items), naming the dimension, the
    # count and the minimum; "Incomplete configuration halts before any
    # request is sent." The shipped example claims D1, D2, D7 over 10
    # items in 6 categories (2, 2, 2, 2, 1, 1).
    shipped = json.loads((EXAMPLE / 'config.json').read_text('utf-8'))
    result = ap1_run(config={'dimensions_claimed':
                             shipped['dimensions_claimed']})
    refused, why = refused_before_any_request(result)
    assert refused, why
    assert 'D1' in f'{result.exception} {result.out[-500:]}'


@pytest.mark.finding('T3-12', 'T3-22')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-12: a D6 claim on nine items runs')
@pytest.mark.req('R4.1', 'R0.1')
def test_r41_d6_claimed_with_nine_items_refused_at_load(ap1_run):
    # SPEC R4.1 row "D6 claimed with nine items | Refused at load"; R0.1
    # verification contract "A D6 claim with nine items is refused, naming
    # the count and the minimum".
    items = json.loads((EXAMPLE / 'questions.json').read_text('utf-8'))[
        'items'][:9]
    result = ap1_run(config={'dimensions_claimed': ['D6']}, questions=items)
    refused, why = refused_before_any_request(result)
    assert refused, why
    assert 'D6' in f'{result.exception} {result.out[-500:]}'


# --- F1 / T3-79 / T3-67: one config file per run ------------------------------

def sampling_sent(body, sampling):
    """The sampling fields of one request body that disagree with the
    declared sampling block: {name: (declared, sent)}."""
    from decimal import Decimal
    wrong = {}
    for name, declared in sampling.items():
        omitted = isinstance(declared, dict) and \
            declared.get('value') == 'omitted'
        if omitted:
            if name in body:
                wrong[name] = (declared, body[name])
        elif name not in body or \
                Decimal(str(body[name])) != Decimal(declared):
            wrong[name] = (declared, body.get(name, '<absent>'))
    return wrong


def assert_run_used_the_file(result, config_path):
    """The run sealed, and sent, exactly the sampling block of the file
    it was given."""
    declared = json.loads(Path(config_path).read_text('utf-8'))['sampling']
    assert result.exception is None, repr(result.exception)
    assert result.seals, 'no seal was made'
    assert result.sealed_configs[0]['sampling'] == declared, (
        result.sealed_configs[0]['sampling'], declared)
    for entry in result.requests:
        assert sampling_sent(entry['request'], declared) == {}


@pytest.mark.finding('F1', 'T3-79')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="F1/T3-79: config_mini.json is refused at load "
                          "(reason 'model-unsupported')")
def test_run_with_config_mini_seals_exactly_that_files_settings(ap1_run,
                                                                tmp_path):
    # Steven's ruling (choices-for-marcus entry 5; decisions file, F1,
    # "Steven's Response 2"): "a run with --config seals exactly that
    # file's settings", with example/config_mini.json the mini run's
    # valid, complete config.
    result = ap1_run(config_file='config_mini.json')
    assert_run_used_the_file(result, tmp_path / 'example' / 'config_mini.json')


@pytest.mark.finding('T3-67', 'F1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-67/F1: AP1_SMOKE_TEMPERATURE and '
                          'AP1_SMOKE_REASONING_EFFORT rewrite the sampling '
                          'block after validation')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('env', [
    {'AP1_SMOKE_TEMPERATURE': '1'},
    {'AP1_SMOKE_REASONING_EFFORT': 'omit'},
    {'AP1_SMOKE_REASONING_EFFORT': 'high'},
])
def test_run_sampling_environment_variable_changes_nothing(ap1_run, tmp_path,
                                                           env):
    # Steven's ruling (choices-for-marcus entry 5): the two overrides are
    # removed, so "no environment variable can change a sampling setting
    # after validation". Today AP1_SMOKE_REASONING_EFFORT=omit writes the
    # reason 'not-supported', which load_config refuses, into the sealed
    # config (T3-67). A run that refuses to start while such a variable
    # is set would also be correct.
    result = ap1_run(env=env)
    refused, _ = refused_before_any_request(result)
    if not refused:
        assert_run_used_the_file(result, tmp_path / 'example' / 'config.json')
