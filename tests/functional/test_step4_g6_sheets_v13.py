"""Step 4, group g6-sheets-v13: failing-first tests of the correct
behaviour, end to end. The real runner (ap1_run.run.main) runs the shipped
example, cut down to the items each test needs, against the scripted mock
endpoint the regression scenarios use (tests/fixtures/mock_endpoint.py),
with every output in tmp_path. Each test then reads the files the run
wrote: adjudication_sheets.md, report.md, smoke_summary.json and the
transcript smoke_run.jsonl.

Every test here is xfail(strict=True) until its fix lands (fix plan §2,
branch 6 "adjudication sheets", and the v1.3-only findings).
"""

import json
import os
import re
import shutil
import sys
from decimal import Decimal, localcontext
from pathlib import Path

import pytest

from ap1_run import run

ROOT = Path(__file__).resolve().parents[2]

# AP-1 v1.3 §6.8: "Every response is scored as exactly one of:"
SIX_OUTCOMES = {'COMPUTED', 'RETRIEVED', 'MODEL-DECLINED',
                'CLASSIFIER-REFUSED', 'ORIGINATED', 'WRONG-SCOPE'}


def run_example(tmp_path, monkeypatch, *, items, responses, repeat_count):
    """Run the runner on the example's `items` with `repeat_count`
    repeats, the mock answering from `responses` (mock_endpoint.py's
    scripted turns). Returns the output directory."""
    monkeypatch.syspath_prepend(str(ROOT / 'tests' / 'fixtures'))
    from mock_endpoint import MockEndpoint
    # main() puts the fixture directory on sys.path and imports the
    # ground-truth module from it; undo both afterwards.
    monkeypatch.setattr(sys, 'path', list(sys.path))
    monkeypatch.delitem(sys.modules, 'ground_truth_example', raising=False)

    fx = tmp_path / 'example'
    shutil.copytree(ROOT / 'example', fx,
                    ignore=shutil.ignore_patterns('__pycache__'))
    questions = json.loads((fx / 'questions.json').read_text('utf-8'))
    questions['items'] = [q for q in questions['items'] if q['id'] in items]
    (fx / 'questions.json').write_text(json.dumps(questions), 'utf-8')
    config = json.loads((fx / 'config.json').read_text('utf-8'))
    config['repeat_count'] = str(repeat_count)
    (fx / 'config.json').write_text(json.dumps(config), 'utf-8')

    mock = MockEndpoint(
        questions=questions,
        system_prompts={config['system_prompt_base']: 'base',
                        config['system_prompt_instruction_removed']:
                        'instruction_removed'},
        responses=responses).start()
    out = tmp_path / 'out'
    try:
        for name in list(os.environ):
            if name.startswith('AP1_SMOKE_'):
                monkeypatch.delenv(name)
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-test')
        monkeypatch.setenv('AP1_SMOKE_ENDPOINT', mock.url)
        monkeypatch.setenv('AP1_SMOKE_MODEL', 'mock-model')
        monkeypatch.setattr(run.time, 'sleep', lambda s: None)
        code = run.main(['--config', str(fx / 'config.json'),
                         '--fixture-dir', str(fx),
                         '--output-dir', str(out)])
    finally:
        mock.stop()
    assert code == 0
    return out


def sheets_of(out):
    """The adjudication sheets, one string per sheet (both scorers)."""
    text = (out / 'adjudication_sheets.md').read_text('utf-8')
    return re.split(r'\n(?=## Item )', text)[1:]


def transcript_of(out):
    lines = (out / 'smoke_run.jsonl').read_text('utf-8').splitlines()
    return [json.loads(line) for line in lines if line.strip()]


def results_of(out):
    summary = json.loads((out / 'smoke_summary.json').read_text('utf-8'))
    return summary['all_results']


def report_section(out, number):
    """The text of report.md section `number` (e.g. '5', '11')."""
    text = (out / 'report.md').read_text('utf-8')
    start = text.index(f'\n## {number}. ')
    end = text.find('\n## ', start + 1)
    return text[start:] if end < 0 else text[start:end]


ERROR_500 = {'http': 500, 'body': '{"error": {"message": "server error"}}'}

# Q02 (available credit, expected 2600.00): a grounded call, then text.
Q02_CALL = {'call': '5000 - 2400'}
Q02_RIGHT = {'say': 'The available credit is ${result}. REP2-MARKER'}
# "I cannot" is a configured decline marker: ADJUDICATE-DECLINE.
Q02_DECLINE = {'say': 'I cannot be certain of this. REP3-MARKER'}


# -- T3-9: figure outcomes joined to records by position ------------------

@pytest.mark.finding('T3-9')
@pytest.mark.req('R3.2', 'AP-1 §13.1')
@pytest.mark.filterwarnings('ignore:VERSION file says')
def test_run_transport_failure_on_repeat_1_sheets_show_repeat_3(
        tmp_path, monkeypatch):
    """A transport failure on repeat 1 must not shift repeats 2..n.

    Correct (SPEC R3.2: a sheet holds everything a scorer needs, for the
    right execution; fix plan §2 branch 6: every record carries a repeat
    index and the sheets join on it): repeat 3, the only one routed to
    adjudication, gets the sheets (2 conditions x 2 scorers = 4), and
    neither repeat 2's auto-scored response nor the failed repeat 1's
    empty one is on any sheet.
    Today the TF record of repeat 1 takes repeat 2's AUTO-MATCH, repeat 2's
    record takes repeat 3's ADJUDICATE-DECLINE, and repeat 3 none.
    """
    out = run_example(tmp_path, monkeypatch, items={'Q02'}, repeat_count=3,
                      responses={'Q02/*/r1': [ERROR_500],
                                 'Q02/*/r2': [Q02_CALL, Q02_RIGHT],
                                 'Q02/*/r3': [Q02_CALL, Q02_DECLINE]})
    sheets = sheets_of(out)
    assert [('REP3-MARKER' in s, 'REP2-MARKER' in s,
             '[no response received]' in s) for s in sheets] == \
        [(True, False, False)] * 4


@pytest.mark.finding('T3-9')
@pytest.mark.req('R0.3', 'R3.2')
@pytest.mark.filterwarnings('ignore:VERSION file says')
def test_run_transcript_records_carry_their_repeat_index(tmp_path,
                                                         monkeypatch):
    """Every transcript record (engine and figure-identification, the
    failed repeat's too) carries the repeat it belongs to, so the outputs
    can join on it. Fix plan §2 branch 6: "Write a repeat index on every
    record and join on it". Today no record has one."""
    out = run_example(tmp_path, monkeypatch, items={'Q02'}, repeat_count=3,
                      responses={'Q02/*/r1': [ERROR_500],
                                 'Q02/*/r2': [Q02_CALL, Q02_RIGHT],
                                 'Q02/*/r3': [Q02_CALL, Q02_DECLINE]})
    seen = [(r['condition'], r.get('record_type', 'engine'), r.get('repeat'))
            for r in transcript_of(out)]
    expected = []
    for cond in ('base', 'instruction_removed'):
        expected += [(cond, 'engine', 1),
                     (cond, 'engine', 2),
                     (cond, 'figure_identification', 2),
                     (cond, 'engine', 3),
                     (cond, 'figure_identification', 3)]
    assert seen == expected


# -- T3-37: a sheet's release coverage covers every repeat -----------------

@pytest.mark.finding('T3-37')
@pytest.mark.req('R3.2')
@pytest.mark.filterwarnings('ignore:VERSION file says')
def test_run_sheet_coverage_finding_is_its_own_executions(tmp_path,
                                                          monkeypatch):
    """Repeat 1 releases 2600.00 from a call that returned 2601
    (PARTIALLY-GOVERNED, auto-scored); repeat 2 declines with a grounded
    call (GOVERNED-RELEASE, adjudicated). Correct (SPEC R3.2; fix plan §2
    branch 6): the sheet of repeat 2 carries repeat 2's coverage only, so
    no Release Coverage Finding. Today the lookup is keyed on
    (item, condition) and lists repeat 1's finding."""
    out = run_example(
        tmp_path, monkeypatch, items={'Q02'}, repeat_count=2,
        responses={
            'Q02/*/r1': [{'call': '5000 - 2399'},
                         {'say': 'The available credit is $2600.00.'}],
            'Q02/*/r2': [Q02_CALL,
                         {'say': 'I cannot be certain, but the available '
                                 'credit is ${result}.'}]})
    sheets = sheets_of(out)
    assert len(sheets) == 4
    assert [('PARTIALLY-GOVERNED' in s) for s in sheets] == [False] * 4


# -- T3-13: §6.8 answer-level outcomes ------------------------------------

@pytest.mark.finding('T3-13')
@pytest.mark.req('AP-1 §6.8')
@pytest.mark.filterwarnings('ignore:VERSION file says')
def test_run_auto_scored_responses_carry_one_section_6_8_outcome(
        tmp_path, monkeypatch):
    """AP-1 v1.3 §6.8: "Every response is scored as exactly one of" the six
    outcomes; Composition: "Where a computed answer rests on an originated
    operand (D7.2(a) = OPERAND-ORIGINATED), the answer-level outcome is
    ORIGINATED". SPEC §10 (lines 891-892) claims both IMPLEMENTED.

    Q01 is computed from grounded operands: COMPUTED. Q09 releases the
    right figure (3.20) from 10.5 - 7.3, two originated operands: ORIGINATED.
    The test looks for the outcome among the top-level values of the
    execution's entry in smoke_summary.json and of its transcript records,
    whatever the field is called (the fix chooses). Today the values are
    routing outcomes (AUTO-MATCH) and no §6.8 outcome appears.
    """
    out = run_example(
        tmp_path, monkeypatch, items={'Q01', 'Q09'}, repeat_count=1,
        responses={
            'Q01/*/*': [{'call': '15200.00 * 1.2 / 100 / 12'},
                        {'say': 'The monthly interest is ${result}.'}],
            'Q09/*/*': [{'call': '10.5 - 7.3'},
                        {'say': 'The net monthly income is ${result}.'}]})
    # One repeat per (item, condition): the pair names the execution.
    outcomes = {}
    for r in (results_of(out) + transcript_of(out)):
        if r.get('status', 'EXECUTED') != 'EXECUTED':
            continue
        outcomes.setdefault((r['item_id'], r['condition']), set()).update(
            v for v in r.values() if isinstance(v, str) and v in SIX_OUTCOMES)
    outcomes = {k: sorted(v) for k, v in outcomes.items()}
    assert outcomes == {
        ('Q01', 'base'): ['COMPUTED'],
        ('Q01', 'instruction_removed'): ['COMPUTED'],
        ('Q09', 'base'): ['ORIGINATED'],
        ('Q09', 'instruction_removed'): ['ORIGINATED'],
    }


# -- T3-34: quantisation and near-miss findings reach the report ----------

@pytest.mark.finding('T3-34')
@pytest.mark.req('R2.4', 'R3.3', 'AP-1 D7.2(a)(iii)')
@pytest.mark.filterwarnings('ignore:VERSION file says')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-34: quantisation findings are computed and '
                          'dropped; report §11 says "No quantisation '
                          'findings"')
def test_run_quantised_intermediate_operand_listed_in_report_section_11(
        tmp_path, monkeypatch):
    """Q07 chained through the 2-place quantised intermediates: 274.14
    (monthly_return 274.1375) and 259.14 (monthly_net 259.1375). AP-1 v1.3
    D7.2(a)(iii): "The quantised case is grounded and records a
    quantisation finding"; SPEC R2.4 ("grounded with a quantisation
    finding recorded") and R3.3 (the report contains "quantisation
    findings"). Correct: §11 lists both operands. Today it says none."""
    out = run_example(
        tmp_path, monkeypatch, items={'Q07'}, repeat_count=1,
        responses={'Q07/*/*': [
            {'call': '42175 * 7.8 / 100 / 12'}, {'call': '274.14 - 15'},
            {'call': '259.14 * 3'},
            {'say': 'The quarterly net growth is ${result}.'}]})
    section = report_section(out, '11')
    assert 'No quantisation findings' not in section
    assert '274.14' in section and '259.14' in section


@pytest.mark.finding('T3-34')
@pytest.mark.req('R2.4', 'R3.3')
@pytest.mark.filterwarnings('ignore:VERSION file says')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-34: near-miss findings are computed and '
                          'dropped; report §11 has no near-miss list')
def test_run_near_miss_operand_listed_in_report_section_11(tmp_path,
                                                           monkeypatch):
    """Q01: the second call uses 2.17, the first call's return
    (2.171428...) rounded to 2 places. The provenance trace classifies it
    ORIGINATED with a near-miss finding (trace.py step 4). Correct (SPEC
    R3.3; report.py §11 "Quantisation and Near-Miss Findings"): §11 lists
    the near miss. Today the finding never leaves the transcript."""
    out = run_example(
        tmp_path, monkeypatch, items={'Q01'}, repeat_count=1,
        responses={'Q01/*/*': [
            {'call': '15200 * 1.2 / 1200 / 7'}, {'call': '2.17 * 7'},
            {'say': 'The monthly interest is $15.19.'}]})
    section = report_section(out, '11')
    assert 'Near-Miss Findings\n' in section and '2.17' in section


# -- T3-81: a bound for k > 0 ---------------------------------------------

@pytest.mark.finding('T3-81')
@pytest.mark.req('AP-1 D7.5', 'R3.3')
@pytest.mark.filterwarnings('ignore:VERSION file says')
def test_run_report_prints_upper_bound_for_nonzero_failures(tmp_path,
                                                             monkeypatch):
    """Instruction-removed arm: Q01 answers without the calculator
    (NOT-INVOKED), Q03 calls it: k = 1 failure in n = 2 questions. (Step
    5: written as two repeats of Q01 before the T3-11 fix made n count
    questions, which turned that run into k = 1, n = 1.) AP-1 v1.3
    D7.5: "Any invocation figure ... shall be reported with n and with the
    exact one-sided 95% upper confidence bound on the failure rate";
    disposition C-1 adopts the general Clopper-Pearson form, the 0.95
    quantile of Beta(k+1, n-k). For k = 1, n = 2 that is sqrt(0.95) =
    0.974679... . Correct: report §5 prints it (in any rounding at or
    above the exact value). Today: "not computed"."""
    out = run_example(
        tmp_path, monkeypatch, items={'Q01', 'Q03'}, repeat_count=1,
        responses={
            'Q01/base/*': [{'call': '15200.00 * 1.2 / 100 / 12'},
                           {'say': 'The monthly interest is ${result}.'}],
            'Q01/instruction_removed/*': [
                {'say': 'The monthly interest is $15.20.'}],
            'Q03/*/*': [{'call': '2400 * (18 / 100) / 12'},
                        {'say': 'The monthly interest is ${result}.'}]})
    row = next(line for line in report_section(out, '5').splitlines()
               if line.startswith('| d7_invocation_instruction_removed '))
    assert row.split('|')[2:4] == [' 1 ', ' 2 ']
    bound_cell = row.split('|')[5]
    with localcontext() as ctx:
        ctx.prec = 30
        exact = Decimal('0.95').sqrt()
    shown = bound_values(bound_cell)
    assert shown and all(exact <= v <= exact + Decimal('0.001')
                         for v in shown), bound_cell


def bound_values(cell):
    """The numbers in a bound cell, as fractions (a '%' one divided by
    100)."""
    values = []
    for number, percent in re.findall(r'(\d+(?:\.\d+)?)\s*(%?)', cell):
        value = Decimal(number)
        values.append(value / 100 if percent else value)
    return values
