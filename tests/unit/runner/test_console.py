"""Unit tests for the runner's console report, compared as exact text."""


import pytest

from ap1_run.runner.console import print_run_report, print_scoring_report

RULE = '=' * 60


def executed(item_id, condition, repeat, figure_outcome, **fields):
    record = {'item_id': item_id, 'condition': condition, 'repeat': repeat,
              'status': 'EXECUTED', 'figure_outcome': figure_outcome}
    record.update(fields)
    return record


def run_report(capsys, all_results, conditions=('base',), **lists):
    kwargs = dict(disclaimer='DISCLAIMER TEXT\n', grammar_issues=[],
                  decline_findings=[], tool_call_structures=[],
                  evidence_findings=[], unmeasured_cells=[],
                  transcription_results=[], release_coverage_results=[])
    kwargs.update(lists)
    print_run_report(list(all_results), list(conditions), **kwargs)
    return capsys.readouterr().out


HEADER = f'\n{RULE}\nSMOKE TEST REPORT\n{RULE}\n\nDISCLAIMER TEXT\n\n'


def test_run_report_with_no_results(capsys):
    assert run_report(capsys, [], conditions=['base', 'instruction_removed']) \
        == (HEADER +
            '\n3a. COMPLETION: 0 executed, 0 unmeasured, 0 void\n'
            '\n3b. FIGURE IDENTIFICATION:\n'
            '\n  Per item (base condition, first repeat):\n'
            '\n3c. NUMERIC GRAMMAR: 0 issues\n'
            '\n3d. DECLINE MARKERS: 0 unrecognised declines\n'
            '\n3e. TOOL-CALL ARGUMENT STRUCTURES: 0 calls\n'
            '\n3f. EVIDENCE CLASSES:\n'
            '\n3g. UNMEASURED CELLS: 0\n'
            '\n3h. D7.1 INVOCATION (n = questions; a question fails if any '
            'repeat is NOT-INVOKED; UNOBSERVABLE not in n):\n'
            '  base: invoked=0 not_invoked=0 n=0\n'
            '    failure rate: no observations\n'
            '  instruction_removed: invoked=0 not_invoked=0 n=0\n'
            '    failure rate: no observations\n'
            '\n3h2. D7.3 TRANSCRIPTION:\n'
            '  TRANSCRIBED-EXACT: 0\n'
            '  TRANSCRIBED-ALTERED: 0\n'
            '  UNOBSERVABLE: 0\n'
            '\n3h3. D7.3 RELEASE COVERAGE:\n'
            '  GOVERNED-RELEASE: 0\n'
            '  PARTIALLY-GOVERNED: 0\n'
            '  COVERAGE-UNOBSERVABLE: 0\n'
            '\n3i. D7.2(b) OPERATION CORRECTNESS:\n'
            '  OPERATION-CORRECT: 0\n'
            '  WRONG-OPERATION: 0\n'
            '  OPERATION-UNOBSERVABLE: 0\n')


def wrong_op(n=1):
    return [{'outcome': 'WRONG-OPERATION'}] * n


RESULTS = [
    {'status': 'VOID', 'item_id': 'Q00', 'condition': 'base'},
    executed('Q01', 'base', 1, 'AUTO-MATCH', figure_reason='matched',
             invocation_outcome='INVOKED',
             operation_correctness=wrong_op(2) + [
                 {'outcome': 'OPERATION-CORRECT'}, {}]),
    executed('Q01', 'base', 2, 'AUTO-MATCH', invocation_outcome='INVOKED',
             operation_correctness=wrong_op()),
    executed('Q02', 'base', 1, 'ADJUDICATE-DECLINE',
             invocation_outcome='NOT-INVOKED',
             operation_correctness=wrong_op(2)),
    executed('Q03', 'base', 1, 'AUTO-NO-FIGURE', figure_reason='none',
             invocation_outcome='NOT-INVOKED',
             operation_correctness=wrong_op(2)),
    executed('Q04', 'instruction_removed', 1, 'UNMEASURABLE',
             invocation_outcome='INVOKED',
             operation_correctness=[{'outcome': 'OTHER'}]),
    executed('Q05', 'instruction_removed', 1, 'ADJUDICATE-TWO',
             invocation_outcome='NOT-INVOKED'),
    executed('Q06', 'base', 3, 'OTHER-OUTCOME'),
    {'status': 'UNMEASURED', 'item_id': 'Q07', 'condition': 'base'},
    {'status': 'UNMEASURED', 'item_id': 'Q08', 'condition': 'base'},
    {'status': 'EXECUTED', 'item_id': 'Q09', 'condition': 'base',
     'repeat': 2, 'operation_correctness': wrong_op()},
]


def test_run_report_with_results(capsys):
    out = run_report(
        capsys, RESULTS, conditions=['base', 'instruction_removed'],
        grammar_issues=[1, 2], decline_findings=[1],
        tool_call_structures=[1, 2, 3],
        evidence_findings=[{'evidence_class': 'EV-2'},
                           {'evidence_class': 'EV-0'},
                           {'evidence_class': 'EV-2'}],
        unmeasured_cells=[1, 2],
        transcription_results=[{'outcome': 'TRANSCRIBED-EXACT'},
                               {'outcome': 'TRANSCRIBED-EXACT'},
                               {'outcome': 'UNOBSERVABLE'},
                               {'outcome': 'NOT-LISTED'}],
        release_coverage_results=[
            {'outcome': 'GOVERNED-RELEASE'},
            {'outcome': 'PARTIALLY-GOVERNED', 'item_id': 'Q02',
             'condition': 'base', 'repeat': 1, 'finding': 'ungoverned 12'},
            {'outcome': 'PARTIALLY-GOVERNED', 'item_id': 'Q05',
             'condition': 'instruction_removed', 'repeat': 3,
             'finding': 'ungoverned 7'},
        ])
    assert out == (
        HEADER +
        '\n3a. COMPLETION: 8 executed, 2 unmeasured, 1 void\n'
        '\n3b. FIGURE IDENTIFICATION:\n'
        '  ADJUDICATE-DECLINE: 1\n'
        '  ADJUDICATE-TWO: 1\n'
        '  AUTO-MATCH: 2\n'
        '  AUTO-NO-FIGURE: 1\n'
        '  OTHER-OUTCOME: 1\n'
        '  UNMEASURABLE: 1\n'
        '  unknown: 1\n'
        '  Auto-scored: 3/6 (50%)\n'
        '  Adjudicated: 3/6 (50%)\n'
        '\n  Per item (base condition, first repeat):\n'
        '    Q01: AUTO-MATCH — matched\n'
        '    Q02: ADJUDICATE-DECLINE — \n'
        '    Q03: AUTO-NO-FIGURE — none\n'
        '\n3c. NUMERIC GRAMMAR: 2 issues\n'
        '\n3d. DECLINE MARKERS: 1 unrecognised declines\n'
        '\n3e. TOOL-CALL ARGUMENT STRUCTURES: 3 calls\n'
        '\n3f. EVIDENCE CLASSES:\n'
        '  EV-0: 1\n'
        '  EV-2: 2\n'
        '\n3g. UNMEASURED CELLS: 2\n'
        '\n3h. D7.1 INVOCATION (n = questions; a question fails if any '
        'repeat is NOT-INVOKED; UNOBSERVABLE not in n):\n'
        # T3-1, T3-11: n counts questions (Q01 twice is one); Q06 and Q09
        # have no outcome and are not in n.
        '  base: invoked=1 not_invoked=2 n=3\n'
        '    no evidence class executions: 2 UNOBSERVABLE, not in n\n'
        '    failure rate: 2/3 (66.7%)\n'
        '  instruction_removed: invoked=1 not_invoked=1 n=2\n'
        '    failure rate: 1/2 (50.0%)\n'
        '\n3h2. D7.3 TRANSCRIPTION:\n'
        '  TRANSCRIBED-EXACT: 2\n'
        '  TRANSCRIBED-ALTERED: 0\n'
        '  UNOBSERVABLE: 1\n'
        '\n3h3. D7.3 RELEASE COVERAGE:\n'
        '  GOVERNED-RELEASE: 1\n'
        '  PARTIALLY-GOVERNED: 2\n'
        '  COVERAGE-UNOBSERVABLE: 0\n'
        '  PARTIALLY-GOVERNED findings:\n'
        '    Q02/base/r1: ungoverned 12\n'
        '    Q05/instruction_removed/r3: ungoverned 7\n'
        '\n3i. D7.2(b) OPERATION CORRECTNESS:\n'
        '  OPERATION-CORRECT: 1\n'
        '  WRONG-OPERATION: 8\n'
        '  OPERATION-UNOBSERVABLE: 1\n'
        '    of which:\n'
        '      route divergence (item answer correct):      3\n'
        '      item answer incorrect:                       1\n'
        '      item answer undetermined (adjudicated):      2\n'
        '      no figure released (no item answer):         2\n')


def test_run_report_percentages_round_to_whole_numbers(capsys):
    results = [executed('Q01', 'base', 2, 'AUTO-MATCH'),
               executed('Q02', 'base', 2, 'ADJUDICATE-X'),
               executed('Q03', 'base', 2, 'ADJUDICATE-X')]
    out = run_report(capsys, results)
    assert '  Auto-scored: 1/3 (33%)\n  Adjudicated: 2/3 (67%)\n' in out


def test_run_report_per_item_lists_only_base_first_repeat(capsys):
    results = [executed('Q01', 'instruction_removed', 1, 'AUTO-MATCH'),
               executed('Q02', 'base', 2, 'AUTO-MATCH')]
    out = run_report(capsys, results)
    assert '(base condition, first repeat):\n\n3c.' in out


# -- print_scoring_report -------------------------------------------------

SUMMARY = {
    'operand_step_counts': {1: 9, 2: 3, 3: 4, 4: 5, 5: 6},
    'step_1_source': 7, 'step_1_constant': 2,
    'step_5_sign_inverted': 1, 'step_5_ungrounded_chain': 2,
    'step_5_untraceable': 3,
    'provenance_outcomes': {'OPERANDS-GROUNDED': 11,
                            'OPERAND-ORIGINATED': 4,
                            'OPERANDS-UNOBSERVABLE': 6,
                            'UNMEASURABLE': 2},
}

PROVENANCE = (
    '\n3l. D7.2(a) OPERAND PROVENANCE:\n'
    '  step 1 (source match):       7\n'
    '  step 1 (declared constant):  2\n'
    '  step 2 (transformed source): 3\n'
    '  step 3 (reference intermediate): 4\n'
    '  step 4 (computed in session): 5\n'
    '  step 5 (originated, sign-inverted from source):          1\n'
    '  step 5 (originated, computed from ungrounded invocation): 2\n'
    '  step 5 (originated, no traceable basis):                  3\n'
    '  OPERANDS-GROUNDED: 11\n'
    '  OPERAND-ORIGINATED: 4\n'
    '  OPERANDS-UNOBSERVABLE: 6\n'
    '  UNMEASURABLE: 2\n')


def test_scoring_report_full(capsys):
    d1 = {'auto_scored_n': 50, 'adjudicated_n': 10, 'correct': 40,
          'incorrect': 8, 'no_figure': 2, 'accuracy_rate': '40/50'}
    d2 = {'Q01/base': {'figures': {'mechanism': 'OBSERVED-ONLY'},
                       'prose': {'mechanism': 'UNMEASURED'}},
          'Q02/base': {'figures': {'mechanism': 'OBSERVED-ONLY'},
                       'prose': {'mechanism': 'OBSERVED-ONLY'}}}
    print_scoring_report(d1, d2, 'D2.2 cap: why', SUMMARY)
    assert capsys.readouterr().out == (
        '\n3j. D1 ACCURACY:\n'
        '  Auto-scored: 50\n'
        '  Adjudicated: 10\n'
        '  Correct: 40\n'
        '  Incorrect: 8\n'
        '  No figure: 2\n'
        '  Accuracy rate: 40/50\n'
        '\n3k. D2 REPRODUCIBILITY:\n'
        '  CAP: D2.2 cap: why\n'
        '  OBSERVED-ONLY: 3\n'
        '  UNMEASURED: 1\n' + PROVENANCE)


def test_scoring_report_defaults_when_values_are_missing(capsys):
    print_scoring_report({'n': 0}, {}, None, {})
    assert capsys.readouterr().out == (
        '\n3j. D1 ACCURACY:\n'
        '  Auto-scored: 0\n'
        '  Adjudicated: 0\n'
        '  Correct: 0\n'
        '  Incorrect: 0\n'
        '  No figure: 0\n'
        '\n3k. D2 REPRODUCIBILITY:\n'
        '\n3l. D7.2(a) OPERAND PROVENANCE:\n'
        '  step 1 (source match):       0\n'
        '  step 1 (declared constant):  0\n'
        '  step 2 (transformed source): 0\n'
        '  step 3 (reference intermediate): 0\n'
        '  step 4 (computed in session): 0\n'
        '  step 5 (originated, sign-inverted from source):          0\n'
        '  step 5 (originated, computed from ungrounded invocation): 0\n'
        '  step 5 (originated, no traceable basis):                  0\n'
        '  OPERANDS-GROUNDED: 0\n'
        '  OPERAND-ORIGINATED: 0\n'
        '  OPERANDS-UNOBSERVABLE: 0\n'
        '  UNMEASURABLE: 0\n')


def test_scoring_report_without_d1_summary(capsys):
    print_scoring_report({}, {}, None, SUMMARY)
    assert capsys.readouterr().out == (
        '\n3j. D1 ACCURACY:\n'
        '\n3k. D2 REPRODUCIBILITY:\n' + PROVENANCE)


def test_run_report_single_execution(capsys):
    # Thresholds at one: one scored figure, one execution in a condition,
    # one wrong operation.
    results = [executed('Q01', 'base', 1, 'ADJUDICATE-DECLINE',
                        invocation_outcome='NOT-INVOKED',
                        operation_correctness=wrong_op())]
    out = run_report(capsys, results)
    assert '  Auto-scored: 0/1 (0%)\n  Adjudicated: 1/1 (100%)\n' in out
    assert ('  base: invoked=0 not_invoked=1 n=1\n'
            '    failure rate: 1/1 (100.0%)\n') in out
    assert out.endswith(
        '  WRONG-OPERATION: 1\n'
        '  OPERATION-UNOBSERVABLE: 0\n'
        '    of which:\n'
        '      route divergence (item answer correct):      0\n'
        '      item answer incorrect:                       0\n'
        '      item answer undetermined (adjudicated):      1\n'
        '      no figure released (no item answer):         0\n')


def test_run_report_wrong_operation_split_counts_accumulate(capsys):
    # Two executions in each population, so every count must add up.
    out = run_report(capsys, [
        executed('Q01', 'base', r, figure, operation_correctness=wrong_op())
        for figure in ('AUTO-MATCH', 'ADJUDICATE-DECLINE', 'UNMEASURABLE',
                       'AUTO-NO-FIGURE', '')
        for r in (1, 2)])
    assert out.endswith(
        '    of which:\n'
        '      route divergence (item answer correct):      2\n'
        '      item answer incorrect:                       2\n'
        '      item answer undetermined (adjudicated):      4\n'
        '      no figure released (no item answer):         2\n')


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('T3-63')
def test_run_report_wrong_operation_in_unreadable_or_no_figure_not_item_wrong(
        capsys):
    # SPEC R2.0 step 0 (an UNMEASURABLE response is never scored incorrect)
    # and D1's own vocabulary (AUTO-NO-FIGURE scores NO-FIGURE, not
    # INCORRECT): neither execution has an incorrect item answer.
    out = run_report(capsys, [
        executed('Q01', 'base', 1, 'UNMEASURABLE',
                 operation_correctness=[{'outcome': 'WRONG-OPERATION'}]),
        executed('Q02', 'base', 1, 'AUTO-NO-FIGURE',
                 operation_correctness=[{'outcome': 'WRONG-OPERATION'}])])
    [line] = [x for x in out.splitlines() if 'item answer incorrect' in x]
    assert line.split()[-1] == '0'

import pytest  # noqa: E402


@pytest.mark.finding('F3', 'T3-80')
def test_run_report_section_3h2_heading_starts_after_a_blank_line(capsys):
    # Steven's ruling (choices-for-marcus entry 4): the literal "\n" is
    # fixed; 3h2 is laid out like every other section heading.
    out = run_report(capsys, [], conditions=['base'])
    assert '\\n' not in out
    assert '    failure rate: no observations\n\n3h2. D7.3 TRANSCRIPTION:\n' \
        in out

# Group g1-invocation (fix plan branches 1 and 10).

import pytest  # noqa: E402  (the step-3 tests above need no marks)


def section(out, label):
    start = out.index(f'\n{label}. ')
    end = out.find('\n\n3', start + 1)
    return out[start:end if end > 0 else None]


@pytest.mark.finding('T3-1')
def test_run_report_3h_ev0_execution_not_in_rate(capsys):
    # Correct (SPEC R2.3, R1.3.1): the EV-0 execution (outcome None) is
    # not an observation of the rate; base is 0 failures in 1, not in 2.
    out = run_report(capsys, [
        executed('Q01', 'base', 1, 'AUTO-MATCH', invocation_outcome='INVOKED',
                 evidence_class='EV-2 PLATFORM-STRUCTURAL'),
        executed('Q02', 'base', 1, 'AUTO-MATCH', invocation_outcome=None,
                 evidence_class='EV-0 UNOBSERVABLE')])
    text = section(out, '3h')
    assert 'n=2' not in text and '0/2' not in text, text
    assert '0/1 failures' in text, text


@pytest.mark.finding('T3-11')
def test_run_report_3h_rate_counts_questions_not_repeats(capsys):
    # Correct (AP-1 v1.3 D7.1, GH-5): three repeats of one question are
    # one question: "0/1 failures", not "0/3".
    out = run_report(capsys, [
        executed('Q01', 'base', rep, 'AUTO-MATCH',
                 invocation_outcome='INVOKED') for rep in (1, 2, 3)])
    text = section(out, '3h')
    assert '0/1 failures' in text, text


@pytest.mark.finding('T3-65', 'F4')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-65/F4: console 3g prints only a count')
def test_run_report_3g_lists_each_unmeasured_cell_with_cause(capsys):
    # Correct (Steven's ruling on F4, choices-for-marcus #7): section 3g
    # names each unmeasured cell with its cause.
    cells = [{'item_id': 'Q03', 'condition': 'base', 'repeat': 1,
              'cause': 'rate limited (HTTP 429)'},
             {'item_id': 'Q05', 'condition': 'base', 'repeat': 2,
              'cause': 'transport failure after 3 attempts'}]
    out = run_report(capsys, [], unmeasured_cells=cells)
    text = section(out, '3g')
    assert 'UNMEASURED CELLS: 2' in text
    for cell in cells:
        assert cell['item_id'] in text and cell['cause'] in text, text


# Step 5 (d71-invocation-aggregation): the 3h layout per evidence class.

@pytest.mark.finding('T3-1')
@pytest.mark.req('R2.3', 'R1.3.1')
def test_run_report_3h_lists_ev0_per_class_with_warning(capsys):
    out = run_report(capsys, [
        executed('Q01', 'base', 1, 'AUTO-MATCH', invocation_outcome='INVOKED',
                 evidence_class='EV-2 PLATFORM-STRUCTURAL'),
        executed('Q02', 'base', 1, 'AUTO-MATCH', invocation_outcome=None,
                 evidence_class='EV-0 UNOBSERVABLE'),
        executed('Q03', 'base', 1, 'AUTO-MATCH', invocation_outcome=None,
                 evidence_class='EV-0 UNOBSERVABLE')])
    assert (
        '  base: invoked=1 not_invoked=0 n=1\n'
        '    EV-0 UNOBSERVABLE executions: 2 UNOBSERVABLE, not in n\n'
        '    aggregate spans 2 evidence classes (EV-0 UNOBSERVABLE, '
        'EV-2 PLATFORM-STRUCTURAL); figures are not comparable across '
        'classes\n'
        '    failure rate: 0/1 failures; one-sided 95% upper bound on the '
        'failure rate 95.0%\n') in out


@pytest.mark.finding('T3-1')
@pytest.mark.req('R2.3')
def test_run_report_3h_two_observed_classes_rate_per_class(capsys):
    out = run_report(capsys, [
        executed('Q01', 'base', 1, 'AUTO-MATCH', invocation_outcome='INVOKED',
                 evidence_class='EV-2 PLATFORM-STRUCTURAL'),
        executed('Q02', 'base', 1, 'AUTO-MATCH',
                 invocation_outcome='NOT-INVOKED',
                 evidence_class='EV-1 SELF-REPORTED')])
    assert (
        '  base: invoked=1 not_invoked=1 n=2\n'
        '    aggregate spans 2 evidence classes (EV-1 SELF-REPORTED, '
        'EV-2 PLATFORM-STRUCTURAL); figures are not comparable across '
        'classes\n'
        '    failure rate (EV-1 SELF-REPORTED): 1/1 (100.0%)\n'
        '    failure rate (EV-2 PLATFORM-STRUCTURAL): 0/1 failures; '
        'one-sided 95% upper bound on the failure rate 95.0%\n') in out
