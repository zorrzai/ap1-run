"""Step 4, group g7-report (fix branch 7, report honesty): failing-first
tests of the correct behaviour, end to end.

Each test reads the files a real run writes. The run is the real runner
(ap1_run.run.main) against the regression suite's mock endpoint
(tests/fixtures/mock_endpoint.py) on 127.0.0.1, with a copy of the shipped
example as --fixture-dir and everything written under tmp_path. One run
serves the whole module; every test is xfail(strict=True) until the fix.

The scripted run (repeat_count 2, both conditions):
  Q01  the calculator returns 15.20; the response mentions 15.20 on the way
       and concludes $182.40 (a wrong final answer, T3-3)
  Q02  r1 releases 2600.00, r2 releases 2500.00 (D2 variation, T3-4)
  Q03  operand 81.0 originated, wrong answer (T3-64)
  Q04  structured answer field 'answer' = 430.75 in the final response,
       prose with two figures within tolerance (T3-75, R2.0 step 1)
  Q05  final content null: figure UNMEASURABLE (T3-35, T3-66)
  Q06  'max(144, 0)', which the calculator executes and D7.2(b) cannot
       evaluate: OPERATION-UNOBSERVABLE (T3-35)
  Q07, Q10  correct
  Q08  HTTP 401 on every request: four UNMEASURED cells (T3-35)
  Q09  correct, but the copied fixture gives the checking account a field
       equal to Q09's expected 3.20: a lookup collision (T3-75, R3.1)
Every mock response carries a served model snapshot and one of two
system fingerprints (V12-8).
"""

import json
import re
import shutil
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
FIXTURES = ROOT / 'tests' / 'fixtures'

SERVED_MODEL = 'mock-model-2026-01-01'
FINGERPRINTS = ('fp_mock_a', 'fp_mock_b')

Q01_CALL = '15200.00 * 1.2 / 100 / 12'
Q04_CALL = '1437.00 - (287500.00 * (4.20 / 100) / 12)'

RESPONSES = {
    'Q01/*/*': [{'call': Q01_CALL},
                {'say': 'Rate 1.2% on 15200 gives 15.20 a year? '
                        'No: answer is $182.40.'}],
    'Q02/*/r1': [{'call': '5000 - 2400'},
                 {'say': 'You have ${result} of credit left.'}],
    'Q02/*/r2': [{'call': '5000 - 2500'},
                 {'say': 'You have ${result} of credit left.'}],
    'Q03/*/*': [{'call': '2400 * (81.0 / 100) / 12'},
                {'say': 'The monthly interest charge is ${result}.'}],
    'Q04/*/*': [{'call': Q04_CALL}, 'Q04_STRUCTURED'],
    'Q05/*/*': [{'call': '2400*(1+0.18/12)+0-25'}, 'Q05_NULL'],
    'Q06/*/*': [{'call': 'max(144, 0)'},
                {'say': 'The total annual cost is ${result}.'}],
    'Q07/*/*': [{'call': '42175 * (0.078 / 4) - (15 * 3)'},
                {'say': 'The quarterly net growth after fees is ${result}.'}],
    'Q08/*/*': [{'http': 401,
                 'body': '{"error": {"message": "invalid key"}}'}],
    'Q09/*/*': [{'call': '15200 * (1.2 / 100) / 12 - 12'},
                {'say': 'The net monthly income is ${result}.'}],
    'Q10/*/*': [{'call': '42175.00 * (7.8 / 100) - (15.00 * 12)'},
                {'say': 'The annual net growth after all fees is '
                        '${result}.'}],
}


def _final(content, **extra):
    return {'raw': {'id': 'chatcmpl-raw', 'object': 'chat.completion',
                    'created': 0, 'model': SERVED_MODEL,
                    'system_fingerprint': FINGERPRINTS[0],
                    'choices': [{'index': 0, 'message': {
                        'role': 'assistant', 'content': content},
                        'finish_reason': 'stop'}], **extra}}


def _script():
    script = {}
    for key, turns in RESPONSES.items():
        out = []
        for t in turns:
            if t == 'Q04_STRUCTURED':
                t = _final('The principal portion is $430.75, or about '
                           '$430.76.', answer='430.75')
            elif t == 'Q05_NULL':
                t = _final(None)
            out.append(t)
        script[key] = out
    return script


@pytest.fixture(scope='module')
def run(tmp_path_factory):
    """One run of the real runner; returns its output files."""
    tmp = tmp_path_factory.mktemp('g7run')
    fixture_dir = tmp / 'inputs'
    fixture_dir.mkdir()
    for name in ('questions.json', 'ground_truth_example.py',
                 'calculator_tool.py'):
        shutil.copyfile(EXAMPLE / name, fixture_dir / name)
    fixture = json.loads((EXAMPLE / 'fixture.json').read_text('utf-8'))
    checking = next(a for a in fixture['accounts'] if a['id'] == 'checking')
    checking['atm_fee'] = '3.20'  # Q09's expected value: a collision
    (fixture_dir / 'fixture.json').write_text(json.dumps(fixture, indent=2),
                                              'utf-8')
    config = json.loads((EXAMPLE / 'config.json').read_text('utf-8'))
    config['repeat_count'] = '2'
    config['structured_answer_field'] = 'answer'
    config_path = tmp / 'config.json'
    config_path.write_text(json.dumps(config, indent=2), 'utf-8')
    output_dir = tmp / 'output'

    questions = json.loads((EXAMPLE / 'questions.json').read_text('utf-8'))
    with pytest.MonkeyPatch.context() as mp:
        mp.syspath_prepend(str(FIXTURES))
        mp.setattr(sys, 'path', list(sys.path))  # main() inserts into it
        for name in ('ground_truth_example', 'calculator_tool',
                     'mock_endpoint'):
            mp.delitem(sys.modules, name, raising=False)
        from mock_endpoint import MockEndpoint
        mock = MockEndpoint(
            questions=questions,
            system_prompts={
                config['system_prompt_base']: 'base',
                config['system_prompt_instruction_removed']:
                    'instruction_removed'},
            responses=_script())
        envelope = mock._envelope

        def served(message):
            body = envelope(message)
            body['model'] = SERVED_MODEL
            body['system_fingerprint'] = FINGERPRINTS[mock._seq % 2]
            return body
        mock._envelope = served
        mock.start()
        try:
            import os
            for name in list(os.environ):
                if name.startswith('AP1_SMOKE_'):
                    mp.delenv(name)
            mp.setenv('AP1_SMOKE_API_KEY', 'sk-step4-not-a-real-key-0000')
            mp.setenv('AP1_SMOKE_ENDPOINT', mock.url)
            mp.setenv('AP1_SMOKE_MODEL', 'mock-model')
            mp.setattr(time, 'sleep', lambda seconds: None)
            from ap1_run import run as runner
            exit_code = runner.main([
                '--config', str(config_path),
                '--fixture-dir', str(fixture_dir),
                '--output-dir', str(output_dir)])
        finally:
            mock.stop()
        for name in ('ground_truth_example', 'calculator_tool'):
            sys.modules.pop(name, None)
    assert exit_code == 0
    report = (output_dir / 'report.md').read_text('utf-8')
    return {
        'report': report,
        'summary': json.loads(
            (output_dir / 'smoke_summary.json').read_text('utf-8')),
        'transcript': [json.loads(line) for line in
                       (output_dir / 'smoke_run.jsonl').read_text(
                           'utf-8').splitlines() if line.strip()],
    }


def section(report, number):
    """The text of section '## <number>.' up to the next '## ' heading."""
    match = re.search(rf'^## {re.escape(number)}\. .*?(?=^## |\Z)', report,
                      flags=re.M | re.S)
    assert match, f'no section {number}'
    return match.group(0)


# --- Step 4: correct behaviour (failing until fixed) ---

ACCURACY_ONE = re.compile(r'Accuracy(?: rate)?: 1(?:\.0+)?(?![\d./])')


def d1_row(report):
    return next(line for line in section(report, '3').split('\n')
                if line.startswith('| D1 |'))


@pytest.mark.finding('T3-3')
def test_run_report_prints_no_accuracy_of_one_with_adjudication_pending(run):
    # The run has wrong final answers (Q01 concludes $182.40, Q02 r2 and
    # Q03 release wrong figures) and 14 items routed to adjudication that
    # nobody scores. Correct (T3-3; fix plan branch 7): report.md carries
    # no "Accuracy: 1" headline (§3 or §8) while adjudication is pending.
    report = run['report']
    assert not ACCURACY_ONE.search(report), d1_row(report)


@pytest.mark.finding('T3-4')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-4: D2 "Measured" in §3 but §9 says no '
                          'per-surface data')
def test_run_report_shows_d2_classes_per_question_and_surface(run):
    # Correct (SPEC R2.2, R3.3; AP-1 D2 Method and D2.1): §9 gives each
    # question's mechanism class per surface (figures, prose) with the
    # distinct values; Q02's two releases (2600.00, 2500.00) are visible;
    # §3 states D2's n.
    s9 = section(run['report'], '9')
    assert 'No per-surface D2 data' not in s9, s9
    assert re.search(r'figures', s9) and re.search(r'prose', s9), s9
    assert 'Q02' in s9, s9
    d2 = next(line for line in section(run['report'], '3').split('\n')
              if line.startswith('| D2 |'))
    assert '| N/A |' not in d2, d2


@pytest.mark.finding('T3-29')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-29: report.md says "D7 Measured"; D7.4 is not '
                          'declared not measured')
def test_run_report_declares_d74_not_measured(run):
    # AP-1 v1.3 D7: "Report all four"; the runner never measures D7.4.
    # Correct: report.md declares D7.4 not measured, and no single D7 row
    # reads "Measured".
    report = run['report']
    assert re.search(r'D7\.4[^\n]*not measured', report, flags=re.I), \
        section(report, '12')
    assert '| D7 | Measured |' not in section(report, '3')


@pytest.mark.finding('T3-32')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-32: D1 is one pooled rate, not per category '
                          'with a 95 % CI')
def test_run_report_d1_per_category_with_confidence_interval(run):
    # AP-1 v1.3 D1: "Results reported per category, with 95% confidence
    # intervals, and with n stated." The example has six categories.
    # Correct: §3 (per-dimension results, SPEC R3.3) gives D1 for each
    # category with n and a 95 % interval (or, below n = 10, says no
    # category claim can be made).
    s3 = section(run['report'], '3')
    for category in ('interest', 'balance', 'amortisation', 'fees',
                     'growth', 'net_income'):
        assert category in s3, (category, s3)
    assert re.search(r'95\s*%', s3), s3


@pytest.mark.finding('T3-35')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-35: §10 lists the four failed Q08 executions '
                          'as one row per condition')
def test_run_report_lists_every_unmeasured_execution(run):
    # Q08 fails (HTTP 401) on both repeats in both conditions: four
    # UNMEASURED cells. Correct (SPEC R3.3 "every UNMEASURED ... cell with
    # its reason"): four rows, one per execution.
    s10 = section(run['report'], '10')
    rows = [line for line in s10.split('\n')
            if line.startswith('| Q08 |') and '| UNMEASURED |' in line]
    assert len(rows) == 4, s10


@pytest.mark.finding('T3-35')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-35: figure UNMEASURABLE, OPERATION-'
                          'UNOBSERVABLE, transcription and coverage '
                          'UNOBSERVABLE cells are missing from §10')
def test_run_report_lists_every_non_outcome_kind(run):
    # Correct (SPEC R3.3): §10 lists Q05's four UNMEASURABLE figures (null
    # content), Q06's four OPERATION-UNOBSERVABLE calls ('max(144, 0)'),
    # the transcription UNOBSERVABLE cells of adjudicated items (Q03) and
    # the COVERAGE-UNOBSERVABLE cells.
    s10 = section(run['report'], '10')
    lines = s10.split('\n')
    assert len([l for l in lines if l.startswith('| Q05 |')
                and 'UNMEASURABLE' in l]) == 4, s10
    assert len([l for l in lines if l.startswith('| Q06 |')
                and 'OPERATION-UNOBSERVABLE' in l]) == 4, s10
    assert any(l.startswith('| Q03 |') and 'UNOBSERVABLE' in l
               for l in lines), s10
    assert 'COVERAGE-UNOBSERVABLE' in s10, s10


@pytest.mark.finding('T3-45')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-45: report.md carries no demonstration-run / '
                          'non-conformance statement')
def test_run_report_says_demonstration_run_not_conformance_result(run):
    # Marcus (2026-10-13): runs are demonstration runs, not conformance
    # results (README lines 21-22). The run writes that only to
    # DISCLAIMER.txt and smoke_summary.json. Correct: report.md says so
    # before its first section.
    head = run['report'][:run['report'].index('## 1.')].lower()
    assert 'demonstration run' in head, head
    assert 'conformance result' in head, head


@pytest.mark.finding('T3-64')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="T3-64: §6 shows '?' for Operation and Originated "
                          'Operand')
def test_run_report_originated_operand_audit_names_the_operand(run):
    # Q03's operand 81.0 is originated. Correct (SPEC R3.3, the D7.2
    # originated-operand listing): §6 names it, with no '?' column.
    rows = [line for line in section(run['report'], '6').split('\n')
            if line.startswith('| Q03 |')]
    assert rows
    for row in rows:
        assert '?' not in row, row


@pytest.mark.finding('T3-66')
def test_run_report_d1_n_agrees_between_sections(run):
    # Correct (SPEC R2.1; T3-66): §3's D1 n equals §8's D1 total, and §8
    # shows the UNMEASURABLE count.
    report = run['report']
    n = int(d1_row(report).split('|')[3])
    s8 = section(report, '8')
    d1_part = s8[s8.index('### D1'):]
    total = int(re.search(r'- Total: (\d+)', d1_part).group(1))
    assert (n, total) == (n, n), f'§3 n={n}, §8 total={total}'
    assert re.search(r'nmeasurable: 4\b', d1_part), d1_part


@pytest.mark.finding('T3-75')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-75: structured_answer_field not used live; Q04 '
                          'is ADJUDICATE-AMBIGUOUS')
def test_run_structured_answer_field_releases_the_figure(run):
    # The config sets structured_answer_field 'answer'; Q04's final
    # response carries answer '430.75' and prose with two figures within
    # tolerance. Correct (SPEC R2.0 step 1): the structured value is the
    # released figure, AUTO-MATCH, for every Q04 execution.
    q04 = [r for r in run['summary']['all_results']
           if r['item_id'] == 'Q04']
    assert len(q04) == 4
    assert [(r['figure_outcome'], r['released_figure']) for r in q04] == \
        [('AUTO-MATCH', '430.75')] * 4, [r['figure_reason'] for r in q04]


@pytest.mark.finding('T3-75')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-75: the lookup collision is computed at run '
                          'time; the seal does not record it')
def test_run_seal_records_the_lookup_collision(run):
    # Q09's expected 3.20 appears in its delivered context (checking
    # account atm_fee). SPEC R3.1: "lookup_collision is computed by the
    # runner at seal time ... reported at seal"; verification: "flagged
    # at seal". Correct: the pre-registration record (§1 lists every seal
    # field) names the collision and the item.
    s1 = section(run['report'], '1')
    assert 'collision' in s1.lower(), s1
    assert 'Q09' in s1, s1


@pytest.mark.finding('V12-8')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='V12-8: report.md records neither the served model '
                          'snapshot nor the backend fingerprints')
def test_run_report_records_served_model_and_fingerprints(run):
    # AP-1 §5.2: "Confirmation that the system under test was frozen for
    # the duration, with a version or commit identifier." The mock serves
    # 'mock-model-2026-01-01' (configured: 'mock-model') under two
    # system_fingerprint values. Correct (fix plan branch 7): report.md
    # records the served snapshot(s) and the fingerprints seen, so a
    # reader can tell whether the system was frozen.
    report = run['report']
    assert SERVED_MODEL in report, report[:report.index('## 1.')]
    for fp in FINGERPRINTS:
        assert fp in report, fp
