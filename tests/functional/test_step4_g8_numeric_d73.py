"""Step 4: end-to-end tests of the correct behaviour
for D7.3 transcription and numeric parsing.

Each test runs the real runner (ap1_run.run.main) in-process against the
regression mock endpoint (tests/fixtures/mock_endpoint.py), on the shipped
example with repeat_count 1, and reads the files it writes into tmp_path.
Each test is marked xfail(strict=True) until its fix lands; the D7.3 tests
(T3-26, T3-27, V12-6) pass since their fix.
"""

import json
import os
import re
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
AP1_TEXT = ROOT / 'reference' / 'AP-1_v1.3_DRAFT_FOR_COMMENT.md'

# A worktree's VERSION differs from its HEAD; the runner warns, harmlessly.
pytestmark = pytest.mark.filterwarnings(
    'ignore:VERSION file says:UserWarning')

# Items not scripted by a test get one plain answer without a figure.
NO_FIGURE = [{'say': 'No figure in this answer.'}]


def run_example(tmp_path, monkeypatch, responses, **config_changes):
    """Run the shipped example once per (item, condition) against the mock
    endpoint, with the scripted responses (mock_endpoint.py syntax) and
    the config changes given. Returns the output directory."""
    monkeypatch.syspath_prepend(str(ROOT / 'tests' / 'fixtures'))
    from mock_endpoint import MockEndpoint

    config = json.loads((EXAMPLE / 'config.json').read_text('utf-8'))
    config['repeat_count'] = '1'
    # The shipped config claims D1 on 10 items, which minimum-n (R0.1)
    # refuses once wired (T3-12); claim only dimensions R0.1 sets no
    # minimum for, as tests/functional/test_step4_g9_spec_claims.py does.
    config['dimensions_claimed'] = ['D2', 'D7']
    config.update(config_changes)
    config_path = tmp_path / 'config.json'
    config_path.write_text(json.dumps(config), 'utf-8')
    out = tmp_path / 'out'

    questions = json.loads((EXAMPLE / 'questions.json').read_text('utf-8'))
    mock = MockEndpoint(
        api_key='sk-step4-not-a-real-key-0000',
        questions=questions,
        system_prompts={config['system_prompt_base']: 'base',
                        config['system_prompt_instruction_removed']:
                            'instruction_removed'},
        responses={'*/*/*': NO_FIGURE, **responses}).start()

    for name in [n for n in list(os.environ) if n.startswith('AP1_SMOKE_')]:
        monkeypatch.delenv(name)
    monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-step4-not-a-real-key-0000')
    mock.point_config(config_path)  # T3-80: config only
    monkeypatch.setattr(time, 'sleep', lambda seconds: None)
    # main() puts the fixture directory on sys.path and imports the
    # example modules; keep that from leaking into other tests.
    monkeypatch.setattr(sys, 'path', list(sys.path))
    for name in ('calculator_tool', 'ground_truth_example'):
        monkeypatch.delitem(sys.modules, name, raising=False)
    monkeypatch.syspath_prepend(str(EXAMPLE))

    from ap1_run import run
    try:
        code = run.main(['--config', str(config_path),
                         '--fixture-dir', str(EXAMPLE),
                         '--output-dir', str(out),
                         '--ap1-text', str(AP1_TEXT)])
    finally:
        mock.stop()
    assert code == 0
    return out


def rows(out, item_id):
    """The EXECUTED rows of smoke_summary.json for one item, by condition."""
    summary = json.loads((out / 'smoke_summary.json').read_text('utf-8'))
    return {r['condition']: r for r in summary['all_results']
            if r['item_id'] == item_id and r.get('status') == 'EXECUTED'}


def transcription_outcomes(out, item_id):
    return {c: r['transcription_outcome']
            for c, r in rows(out, item_id).items()}


BOTH = ('base', 'instruction_removed')
Q04_SAY = {'say': 'The principal portion of the first mortgage payment is '
                  '$430.75.'}


# -- T3-26: D7.3 compares the return of the required operation -------------

@pytest.mark.finding('T3-26')
@pytest.mark.req('R2.5')
def test_run_release_of_earlier_calculator_return_is_transcribed_exact(
        tmp_path, monkeypatch, capsys):
    # SPEC R2.5: compare "the value the required operation returned" to
    # the released figure. Q04: the calculator returns 430.75, then the
    # model checks it (430.75 + 1006.25 = 1437.0) and releases 430.75.
    # The published runs show this pattern as AUTO-MATCH /
    # TRANSCRIBED-ALTERED / GOVERNED-RELEASE (T3-26, FINDINGS_ERRATA N1).
    out = run_example(tmp_path, monkeypatch, {
        'Q04/*/*': [{'call': '1437.00 - 1006.25'},
                    {'call': '430.75 + 1006.25'}, Q04_SAY]})
    q04 = rows(out, 'Q04')
    assert {c: q04[c]['figure_outcome'] for c in BOTH} == \
        dict.fromkeys(BOTH, 'AUTO-MATCH')
    assert {c: q04[c]['release_coverage_outcome'] for c in BOTH} == \
        dict.fromkeys(BOTH, 'GOVERNED-RELEASE')
    assert transcription_outcomes(out, 'Q04') == \
        dict.fromkeys(BOTH, 'TRANSCRIBED-EXACT')


@pytest.mark.finding('T3-26')
@pytest.mark.req('R2.5')
def test_run_errored_last_call_keeps_earlier_return_transcribed_exact(
        tmp_path, monkeypatch, capsys):
    # T3-26: "If the last call errored, the execution is UNOBSERVABLE even
    # when an earlier return matches." The required operation did return
    # 430.75, which is released: EXACT (SPEC R2.5).
    out = run_example(tmp_path, monkeypatch, {
        'Q04/*/*': [{'call': '1437.00 - 1006.25'},
                    {'call': '430.75 / 0'}, Q04_SAY]})
    assert transcription_outcomes(out, 'Q04') == \
        dict.fromkeys(BOTH, 'TRANSCRIBED-EXACT')


# -- T3-27: the declared rounding mode ---------------------------------------

@pytest.mark.finding('T3-27')
@pytest.mark.req('R2.5', 'R0.4.1')
def test_run_transcription_uses_declared_half_up_rounding(
        tmp_path, monkeypatch, capsys):
    # The shipped config declares quantisation ROUND_HALF_UP at 2 places
    # (SPEC R0.4.1: "using the declared rounding mode"). The calculator
    # returns 430.745; releasing 430.75 is the licensed rounding, so EXACT
    # (AP-1 v1.3 D7.3, SPEC R2.5). Today: 430.74 vs 430.75, ALTERED.
    out = run_example(tmp_path, monkeypatch, {
        'Q04/*/*': [{'call': '861.49 / 2'}, Q04_SAY]})
    assert {c: r['release_coverage_outcome']
            for c, r in rows(out, 'Q04').items()} == \
        dict.fromkeys(BOTH, 'GOVERNED-RELEASE')
    assert transcription_outcomes(out, 'Q04') == \
        dict.fromkeys(BOTH, 'TRANSCRIBED-EXACT')


@pytest.mark.req('R2.5', 'R0.4.1')
def test_run_transcription_declared_half_even_tie_is_altered(
        tmp_path, monkeypatch, capsys):
    # A guard for T3-27's fix, not failing-first: under a declared
    # ROUND_HALF_EVEN the tool's 430.745 is 430.74, so releasing 430.75 is
    # ALTERED. Today's code always uses HALF_EVEN, so this passes; a fix
    # that hard-codes ROUND_HALF_UP to pass the test above fails it.
    out = run_example(tmp_path, monkeypatch, {
        'Q04/*/*': [{'call': '861.49 / 2'}, Q04_SAY]},
        quantisation={'places': '2', 'rounding': 'ROUND_HALF_EVEN'})
    assert transcription_outcomes(out, 'Q04') == \
        dict.fromkeys(BOTH, 'TRANSCRIBED-ALTERED')


# -- V12-6: the "rounded under declared policy" count ------------------------

@pytest.mark.proposal(
    "V12-n: v1.2 behaviour alongside v1.3 is the author's proposal; field "
    "and key names are the fix's")
@pytest.mark.finding('V12-6')
@pytest.mark.req('R2.5', 'R3.3')
def test_run_report_counts_transcriptions_rounded_under_declared_policy(
        tmp_path, monkeypatch, capsys):
    # V12-6: Q07's calculator returns 777.4125 and the model releases
    # 777.41: TRANSCRIBED-EXACT under v1.3 (licensed rounding), with a
    # sub-flag whose count the report states, so a v1.2 reader can take
    # them out. Three repeats of Q07 in both conditions: 6 rounded under
    # the policy. Q01's call returns exactly 15.2 ('1520 / 100'; the
    # shipped expression returns 15.200000000000001, itself a licensed
    # rounding) and the model releases $15.20: EXACT with no rounding, 6
    # more EXACT results that must not be counted. The count (6) differs
    # from the declared places (2), from all EXACT (12) and from the ALTERED
    # count (3, Q04's control, in the base condition only), and is read as
    # a value (": 6" or a table cell), not anywhere on a line.
    out = run_example(tmp_path, monkeypatch, {
        'Q07/*/*': [{'call': '42175 * (0.078 / 4) - (15 * 3)'},
                    {'say': 'The quarterly net growth after fees is '
                            '${result}.'}],
        'Q01/*/*': [{'call': '1520 / 100'},
                    {'say': 'The monthly interest is $15.20.'}],
        'Q04/base/*': [{'call': '1437.00 - 1006.25'},
                    {'say': 'The principal portion of the first mortgage '
                            'payment is $430.76.'}]},
        repeat_count='3')
    summary = json.loads((out / 'smoke_summary.json').read_text('utf-8'))
    exact = [(r['item_id'], r['condition'], r['repeat'])
             for r in summary['all_results']
             if r.get('transcription_outcome') == 'TRANSCRIBED-EXACT']
    assert len(exact) == 12, exact
    # Control: Q04 releases 430.76 for the calculator's 430.75, within the
    # answer tolerance (so AUTO-MATCH) but an alteration the policy does
    # not license: 3 ALTERED results with a non-zero difference, which
    # the count must leave out too (3: base only, so that printing the
    # ALTERED count as the rounded one fails).
    altered = [(r['item_id'], r['condition'], r['repeat'])
               for r in summary['all_results']
               if r.get('transcription_outcome') == 'TRANSCRIBED-ALTERED']
    assert len(altered) == 3 and {i for i, _, _ in altered} == {'Q04'}, \
        altered
    report = (out / 'report.md').read_text('utf-8')
    d73 = report[report.index('## D7.3'):]
    d73 = d73[:d73.index('\n## ', 1)] if '\n## ' in d73[1:] else d73
    lines = [ln for ln in d73.splitlines()
             if re.search(r'rounded under (the )?declared '
                          r'(quantisation )?policy', ln, re.I)]
    # The count as a value: ': 6', a table cell, or the sentence's
    # subject ('Of the 12 ..., 6 were rounded under ...', the step-5 form).
    assert any(re.search(r'(:\s*|\|\s*\**)6\**\s*(\||$|\b)', ln)
               or re.search(r'(^|[,;]\s*)6 were rounded under', ln)
               for ln in lines), lines


# -- T3-41: the configured separators ----------------------------------------

@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2', 'R2.0')
def test_run_european_separators_parse_the_released_figure(
        tmp_path, monkeypatch, capsys):
    # SPEC R0.4.2: tokens are parsed with the configured decimal_separator
    # and grouping_separator (required and sealed, R0.1). With ',' and '.',
    # '430,75' is 430.75: Q04 auto-matches, and the calculator's 430.75
    # governs it. Today: 430 and 75, no match, coverage UNOBSERVABLE.
    out = run_example(tmp_path, monkeypatch, {
        'Q04/*/*': [{'call': '1437.00 - 1006.25'},
                    # The answer comes last: a dollar figure after it
                    # would compete with it (T3-3, report-honesty).
                    {'say': 'Zinsen 1.006,25 $; der Tilgungsanteil der '
                            'ersten Rate betraegt 430,75 $.'}]},
        decimal_separator=',', grouping_separator='.')
    q04 = rows(out, 'Q04')
    assert {c: (q04[c]['figure_outcome'], q04[c]['released_figure'],
                q04[c]['release_coverage_outcome']) for c in BOTH} == \
        dict.fromkeys(BOTH, ('AUTO-MATCH', '430.75', 'GOVERNED-RELEASE'))


# -- S3-G1-5: the minus of a subtraction is not a sign ----------------------

@pytest.mark.finding('S3-G1-5')
@pytest.mark.req('R0.4.2', 'R2.0')
def test_run_expected_value_as_subtrahend_and_answer_routes_ambiguous(
        tmp_path, monkeypatch, capsys):
    # End-to-end check: does S3-G1-5 reach figure
    # identification? Yes. The response states 430.75 twice, once as the
    # subtrahend of a worked step. Read as an operator (the correct
    # reading, S3-G1-5), both mentions match the expected 430.75, and SPEC
    # R2.0 routes "two or more extracted values match" to ADJUDICATE --
    # ambiguous. Today the subtrahend is -430.75, only one mention matches,
    # and the item is AUTO-MATCH. (Provenance is not affected: D7.2(a)
    # reads calculator expressions through the AST, not this extractor.)
    out = run_example(tmp_path, monkeypatch, {
        'Q04/*/*': [{'call': '1437.00 - 1006.25'},
                    {'say': 'Interest is 1437.00 - 430.75 = 1006.25, so the '
                            'principal portion is $430.75.'}]})
    assert {c: r['figure_outcome'] for c, r in rows(out, 'Q04').items()} \
        == dict.fromkeys(BOTH, 'ADJUDICATE-AMBIGUOUS')
