"""Step 4, group g2-provenance: the correct D7.2(a) behaviour end to end
(fix plan branch 2, D7.2(a) fail-closed), failing until fixed.

Each test drives the real runner (ap1_run.run.main) against the scripted
mock endpoint the regression scenarios use (tests/fixtures/mock_endpoint.py),
with --config and --output-dir in tmp_path, and reads the run's
smoke_summary.json and report.md. Items a test does not script answer as in
the regression scenario `clean` (every call grounded).
"""

import json
import re
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
CLEAN = ROOT / 'tests' / 'regression' / 'scenarios' / 'clean.json'

# A worktree's git HEAD is not the commit in VERSION; the runner warns.
pytestmark = pytest.mark.filterwarnings(
    'ignore:VERSION file says:UserWarning')


@pytest.fixture
def full_run(tmp_path, monkeypatch):
    """Run the whole instrument once against the mock endpoint.

    run(responses, repeat_count=1, ground_truth=None) returns
    (exit code, smoke_summary.json as a dict, report.md text). `responses`
    overrides the clean scenario's script per "item/condition/rN" key;
    `ground_truth` is the text of a ground_truth_example.py to run with
    (in a copy of example/), or None for the shipped one.
    """
    monkeypatch.syspath_prepend(str(ROOT / 'tests' / 'fixtures'))
    from mock_endpoint import MockEndpoint
    import ap1_run.run as runner

    def run(responses, *, repeat_count=1, ground_truth=None):
        config = json.loads((EXAMPLE / 'config.json').read_text('utf-8'))
        config['repeat_count'] = str(repeat_count)
        config_path = tmp_path / 'config.json'
        config_path.write_text(json.dumps(config), 'utf-8')

        fixture_dir = EXAMPLE
        if ground_truth is not None:
            fixture_dir = tmp_path / 'inputs'
            fixture_dir.mkdir()
            for name in ('fixture.json', 'questions.json'):
                (fixture_dir / name).write_bytes((EXAMPLE / name).read_bytes())
            (fixture_dir / 'ground_truth_example.py').write_text(
                ground_truth, 'utf-8')

        script = json.loads(CLEAN.read_text('utf-8'))['responses']
        script.update(responses)
        questions = json.loads(
            (fixture_dir / 'questions.json').read_text('utf-8'))
        mock = MockEndpoint(
            questions=questions,
            system_prompts={
                config['system_prompt_base']: 'base',
                config['system_prompt_instruction_removed']:
                    'instruction_removed'},
            responses=script).start()

        for name in ('AP1_SMOKE_TEMPERATURE', 'AP1_SMOKE_REASONING_EFFORT'):
            monkeypatch.delenv(name, raising=False)
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-step4-not-a-real-key-0000')
        monkeypatch.setenv('AP1_SMOKE_ENDPOINT', mock.url)
        monkeypatch.setenv('AP1_SMOKE_MODEL', 'mock-model')
        # The runner sleeps between executions and retries; skip it.
        monkeypatch.setattr(time, 'sleep', lambda seconds: None)
        # The runner puts the fixture directory on sys.path and imports
        # ground_truth_example from it: undo both, write no bytecode.
        monkeypatch.setattr(sys, 'path', list(sys.path))
        monkeypatch.setattr(sys, 'dont_write_bytecode', True)
        saved = sys.modules.pop('ground_truth_example', None)
        output_dir = tmp_path / 'output'
        try:
            code = runner.main(['--config', str(config_path),
                                '--fixture-dir', str(fixture_dir),
                                '--output-dir', str(output_dir)])
        finally:
            mock.stop()
            sys.modules.pop('ground_truth_example', None)
            if saved is not None:
                sys.modules['ground_truth_example'] = saved
        summary = json.loads(
            (output_dir / 'smoke_summary.json').read_text('utf-8'))
        report = (output_dir / 'report.md').read_text('utf-8')
        return code, summary, report

    return run


def executions(summary, item_id):
    return [r for r in summary['all_results']
            if r['item_id'] == item_id and r['status'] == 'EXECUTED']


def section(report, heading):
    """The text of the report section whose heading starts with `heading`,
    up to the next section of the same or a higher level."""
    match = re.search(rf'^(#+) {re.escape(heading)}.*$', report, re.M)
    assert match, f'no section {heading!r} in the report'
    level = len(match.group(1))
    rest = report[match.end():]
    end = re.search(rf'^#{{1,{level}}} ', rest, re.M)
    return rest[:end.start()] if end else rest


def table_count(text, label):
    """The count in the `| label | count |` row, or None."""
    match = re.search(rf'^\| {re.escape(label)} \| (\d+) \|', text, re.M)
    return int(match.group(1)) if match else None


# -- T3-2: leading whitespace, vacuous grounding and step-4 laundering ----

@pytest.mark.finding('T3-2')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-2: a leading space makes the fabricated first '
                          'call GROUNDED and step 4 launders its return')
def test_run_leading_whitespace_chain_is_originated(full_run):
    # The T3 review's chain on Q01: ' 7777 * 3' fabricates 23331 and the
    # next call consumes it. Correct: the expression is stripped, 7777 and
    # 3 are originated, and the dependent call is originated too (AP-1 v1.3
    # D7.2(a)(iv) and box "Why (iv) carries a condition": "The chain fails
    # closed at the first unresolved link"; SPEC R2.4 step 4).
    code, summary, report = full_run({'Q01/*/*': [
        {'call': ' 7777 * 3'}, {'call': '23331 * 1.2 / 12'},
        {'say': 'The monthly interest earned on the savings account is '
                '${result}.'}]})
    assert code == 0
    runs = executions(summary, 'Q01')
    assert len(runs) == 2
    assert [[p['outcome'] for p in r['provenance_results']] for r in runs] \
        == [['OPERAND-ORIGINATED', 'OPERAND-ORIGINATED']] * 2
    audit = section(report, '7b. D7.2(a)')
    assert '`7777`' in audit


# -- T3-16: unreadable calculator calls are declared, never skipped -------

UNREADABLE = {
    # not JSON
    'Q01/*/*': [{'calls': [{'name': 'calculator',
                            'arguments': '15200*1.2/100/12'}]},
                {'say': 'The monthly interest earned is $15.20.'}],
    # wrongly keyed
    'Q02/*/*': [{'calls': [{'name': 'calculator',
                            'arguments': '{"expr": "5000 - 2400"}'}]},
                {'say': 'The available credit is $2,600.00.'}],
    # an unreadable call before a valid one in the same round
    'Q04/*/*': [{'calls': [{'name': 'calculator', 'arguments': 'not json'},
                           '1437.00 - (287500.00 * (4.20 / 100) / 12)']},
                {'say': 'The principal portion is ${result}.'}],
}


@pytest.mark.finding('T3-16')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-16: unreadable calculator calls vanish from '
                          'D7.2(a)')
def test_run_unreadable_calls_are_operands_unobservable(full_run):
    # Correct: every calculator invocation gets a D7.2(a) outcome; one whose
    # arguments can't be read is OPERANDS-UNOBSERVABLE, and a valid call
    # after it is still classified (AP-1 v1.3 D7.2(a): "The unobservable
    # case is declared, never silently skipped"; SPEC R2.4).
    code, summary, _ = full_run(UNREADABLE)
    assert code == 0
    got = {item: [[p['outcome'] for p in r['provenance_results']]
                  for r in executions(summary, item)]
           for item in ('Q01', 'Q02', 'Q04')}
    assert got == {
        'Q01': [['OPERANDS-UNOBSERVABLE']] * 2,
        'Q02': [['OPERANDS-UNOBSERVABLE']] * 2,
        'Q04': [['OPERANDS-UNOBSERVABLE', 'OPERANDS-GROUNDED']] * 2,
    }


@pytest.mark.finding('T3-16')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-16: the report has no OPERANDS-UNOBSERVABLE '
                          'count, so the proportion is not reported')
def test_run_report_states_operands_unobservable_count(full_run):
    # AP-1 v1.3 D7.2(a): the unobservable case is declared and "its
    # proportion reported". Three unreadable calls per condition, one
    # repeat: 6 OPERANDS-UNOBSERVABLE invocations beside the grounded ones.
    code, _, report = full_run(UNREADABLE)
    assert code == 0
    provenance = section(report, '7b. D7.2(a)')
    assert table_count(provenance, 'OPERANDS-UNOBSERVABLE') == 6


@pytest.mark.finding('T3-16')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-16: unreadable calculator calls vanish from '
                          'D7.2(b) and its report table')
def test_run_unreadable_calls_are_operation_unobservable(full_run):
    # AP-1 v1.3 D7.2(b): outcomes OPERATION-CORRECT, WRONG-OPERATION,
    # OPERATION-UNOBSERVABLE; a call whose computation can't be recovered
    # is OPERATION-UNOBSERVABLE, counted, not dropped (SPEC R2.4 and the
    # same "never silently skipped" rule). 6 such calls in this run.
    code, summary, report = full_run(UNREADABLE)
    assert code == 0
    got = {item: [[oc['outcome'] for oc in r['operation_correctness']]
                  for r in executions(summary, item)]
           for item in ('Q01', 'Q02')}
    assert got == {'Q01': [['OPERATION-UNOBSERVABLE']] * 2,
                   'Q02': [['OPERATION-UNOBSERVABLE']] * 2}
    assert table_count(report, 'OPERATION-UNOBSERVABLE') == 6


@pytest.mark.finding('T3-16')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-16: with an unreadable call first, the engine '
                          'pairs D7.2(b) results with the wrong expressions')
def test_run_unreadable_call_does_not_shift_d72b_reclassification(full_run):
    # Q07 by an unanticipated route: annual return / 4 (822.4125, not a
    # reference intermediate, so WRONG-OPERATION on its own), then
    # 822.4125 - 45 = 777.4125, the expected value. The forward-dependency
    # rule makes the first call OPERATION-CORRECT because the second
    # consumes its result (AP-1 v1.3 D7.2(b): a correct value by an
    # unanticipated route "shall not be scored otherwise"). An unreadable
    # call before them must not change that. Today the engine passes one
    # expression per tool call but one result per readable call, so the
    # results are checked against the wrong calls' operands (the T3 review's
    # unverified side observation; confirmed here).
    code, summary, _ = full_run({'Q07/*/*': [
        {'calls': [{'name': 'calculator', 'arguments': 'not json'},
                   '42175 * 7.8 / 100 / 4']},
        {'call': '822.4125 - 45'},
        {'say': 'The quarterly net growth after fees is ${result}.'}]})
    assert code == 0
    readable = [[oc['outcome'] for oc in r['operation_correctness']
                 if oc['outcome'] != 'OPERATION-UNOBSERVABLE']
                for r in executions(summary, 'Q07')]
    assert readable == [['OPERATION-CORRECT', 'OPERATION-CORRECT']] * 2


# -- T3-42: a chained item without declared intermediates -----------------

GT_Q01_WITHOUT_INTERMEDIATES = f'''
"""The shipped ground truth, except that Q01 declares no intermediates."""
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "_shipped_ground_truth", {str(EXAMPLE / 'ground_truth_example.py')!r})
_shipped = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_shipped)


def compute(item_id, delivered_context):
    result = _shipped.compute(item_id, delivered_context)
    if item_id == "Q01":
        result = dict(result, intermediates=[])
    return result
'''


@pytest.mark.finding('T3-42')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-42: a chained item whose ground truth declares '
                          'no intermediates is scored GROUNDED by default')
def test_run_chained_item_without_intermediates_is_unmeasurable(
        full_run, monkeypatch):
    # SPEC R2.4 Failure Modes: "Where the ground-truth module declares no
    # intermediates for a chained item, D7.2 is UNMEASURABLE for that
    # item. Never grounded by default." Q01 (15200 x 1.2 / 100 / 12) is a
    # multi-step derivation; here its module declares no intermediates and
    # the model's chained calls resolve by source match, the structural
    # constant 1 and step 4. Correct: Q01's 4 invocations (2 per condition)
    # are not counted OPERANDS-GROUNDED, and the report says D7.2 was
    # UNMEASURABLE for the item. The other 9 items answer as in `clean`,
    # one grounded call each per condition: 18.
    #
    # Constants are declared only through intermediates' inputs, so this
    # module cannot declare Q01's 100 and 12, and the R3.1 declared-
    # constants check, live since step 5 (seal-gt-guards, T3-7), refuses it
    # at seal. That check is switched off here so the test reaches R2.4.
    import ap1_run.run as runner
    monkeypatch.setattr(runner, 'declared_constants_check',
                        lambda *args: [])
    code, _, report = full_run(
        {'Q01/*/*': [{'call': '15200.00 * 1.2'}, {'call': '18240.0 * 1'},
                     {'say': 'The monthly interest earned on the savings '
                             'account is ${result}.'}]},
        ground_truth=GT_Q01_WITHOUT_INTERMEDIATES)
    assert code == 0
    provenance = section(report, '7b. D7.2(a)')
    assert table_count(provenance, 'OPERANDS-GROUNDED') == 18
    assert 'UNMEASURABLE' in provenance
