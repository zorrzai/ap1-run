"""Step 4, group g8-numeric-d73: end-to-end tests of the correct behaviour
for D7.3 transcription (fix branch 8) and numeric parsing (fix branch 9).

Each test runs the real runner (ap1_run.run.main) in-process against the
regression mock endpoint (tests/fixtures/mock_endpoint.py), on the shipped
example with repeat_count 1, and reads the files it writes into tmp_path.
Every test is marked xfail(strict=True): it fails on today's code and the
fix turns it green.
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
    config.update(config_changes)
    config_path = tmp_path / 'config.json'
    config_path.write_text(json.dumps(config), 'utf-8')
    out = tmp_path / 'out'

    questions = json.loads((EXAMPLE / 'questions.json').read_text('utf-8'))
    mock = MockEndpoint(
        questions=questions,
        system_prompts={config['system_prompt_base']: 'base',
                        config['system_prompt_instruction_removed']:
                            'instruction_removed'},
        responses={'*/*/*': NO_FIGURE, **responses}).start()

    for name in [n for n in list(os.environ) if n.startswith('AP1_SMOKE_')]:
        monkeypatch.delenv(name)
    monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-step4-not-a-real-key-0000')
    monkeypatch.setenv('AP1_SMOKE_ENDPOINT', mock.url)
    monkeypatch.setenv('AP1_SMOKE_MODEL', 'mock-model')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-26: D7.3 compares only the last tool return; '
                          'a released earlier return is TRANSCRIBED-ALTERED')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-26: an errored last calculator call makes D7.3 '
                          'UNOBSERVABLE despite an earlier matching return')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-27: transcription quantises with HALF_EVEN, not '
                          'the declared ROUND_HALF_UP')
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


# -- V12-6: the "rounded under declared policy" count ------------------------

@pytest.mark.finding('V12-6')
@pytest.mark.req('R2.5', 'R3.3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='V12-6: report.md does not count the EXACT '
                          'transcriptions rounded under the declared policy')
def test_run_report_counts_transcriptions_rounded_under_declared_policy(
        tmp_path, monkeypatch, capsys):
    # Fix plan §2a, V12-6: Q07's calculator returns 777.4125 and the model
    # releases 777.41: TRANSCRIBED-EXACT under v1.3 (licensed rounding),
    # with a sub-flag whose count the report states, so a v1.2 reader can
    # take them out. One execution per condition: the count is 2.
    out = run_example(tmp_path, monkeypatch, {
        'Q07/*/*': [{'call': '42175 * (0.078 / 4) - (15 * 3)'},
                    {'say': 'The quarterly net growth after fees is '
                            '${result}.'}]})
    assert transcription_outcomes(out, 'Q07') == \
        dict.fromkeys(BOTH, 'TRANSCRIBED-EXACT')
    report = (out / 'report.md').read_text('utf-8')
    d73 = report[report.index('## D7.3'):]
    d73 = d73[:d73.index('\n## ', 1)] if '\n## ' in d73[1:] else d73
    lines = [ln for ln in d73.splitlines()
             if re.search(r'rounded under (the )?declared '
                          r'(quantisation )?policy', ln, re.I)]
    assert any(re.search(r'\b2\b', ln) for ln in lines), lines


# -- T3-41: the configured separators ----------------------------------------

@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-41: a run sealed with European separators '
                          'parses the responses with US separators')
def test_run_european_separators_parse_the_released_figure(
        tmp_path, monkeypatch, capsys):
    # SPEC R0.4.2: tokens are parsed with the configured decimal_separator
    # and grouping_separator (required and sealed, R0.1). With ',' and '.',
    # '430,75' is 430.75: Q04 auto-matches, and the calculator's 430.75
    # governs it. Today: 430 and 75, no match, coverage UNOBSERVABLE.
    out = run_example(tmp_path, monkeypatch, {
        'Q04/*/*': [{'call': '1437.00 - 1006.25'},
                    {'say': 'Der Tilgungsanteil der ersten Rate betraegt '
                            '430,75 $ (Zinsen 1.006,25 $).'}]},
        decimal_separator=',', grouping_separator='.')
    q04 = rows(out, 'Q04')
    assert {c: (q04[c]['figure_outcome'], q04[c]['released_figure'],
                q04[c]['release_coverage_outcome']) for c in BOTH} == \
        dict.fromkeys(BOTH, ('AUTO-MATCH', '430.75', 'GOVERNED-RELEASE'))


# -- S3-G1-5: the minus of a subtraction is not a sign ----------------------

@pytest.mark.finding('S3-G1-5')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-5: the subtrahend in "1437.00 - 430.75" is '
                          'extracted as -430.75, hiding a second mention of '
                          'the expected value from figure identification')
def test_run_expected_value_as_subtrahend_and_answer_routes_ambiguous(
        tmp_path, monkeypatch, capsys):
    # End-to-end check asked for in the brief: does S3-G1-5 reach figure
    # identification? Yes. The response states 430.75 twice, once as the
    # subtrahend of a worked step. Read as an operator (the G1 report's
    # correct reading), both mentions match the expected 430.75, and SPEC
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
