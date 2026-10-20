"""Unit tests for tools/generate_findings.py, which fills FINDINGS.template.md
with figures computed from the published runs' smoke_summary.json.

They pin what the tool does today, defects included, on small summaries
built in the test. The published data and the committed FINDINGS.md are
pinned end to end by the regression scenario tool_generate_findings, and
checked by the legacy suites verify_findings and test_findings_mutation
(mapped by G7).

The tool reads and writes fixed paths (OUTPUT, TEMPLATE, TARGET under its
repository root). Each test points them at tmp_path.
"""

import importlib.util
import json
import os
from decimal import Decimal

import pytest

from ap1_run.reporting.report import clopper_pearson_upper_k0

TOOL = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))), 'tools',
    'generate_findings.py')


def load_tool():
    # Named as its path, tools.generate_findings, so a mutation tool can
    # map the functions to the file.
    spec = importlib.util.spec_from_file_location('tools.generate_findings',
                                                  TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def gf():
    return load_tool()


# -- building summaries ---------------------------------------------------

def result(item, condition='base', invocation='INVOKED', figure='AUTO-MATCH',
           ops=(), prov=()):
    """One all_results entry."""
    return {'item_id': item, 'condition': condition,
            'invocation_outcome': invocation, 'figure_outcome': figure,
            'operation_correctness': [{'outcome': o} for o in ops],
            'provenance_results': list(prov)}


IR = 'instruction_removed'


def grounded(*resolutions):
    return {'outcome': 'OPERANDS-GROUNDED',
            'operand_resolutions': [{'resolution': r} for r in resolutions],
            'originated_operands': []}


def originated(resolutions=(), operands=(), sign=None):
    res = [{'resolution': r} for r in resolutions]
    if sign is not None:
        res.append({'resolution': 'originated',
                    'sign_inversion_finding': sign})
    return {'outcome': 'OPERAND-ORIGINATED', 'operand_resolutions': res,
            'originated_operands': list(operands)}


ONE = [result('Q01')]


@pytest.fixture
def figures(gf, tmp_path, monkeypatch):
    """compute_figures() over the given runs A, B and superseded."""
    def compute(a=ONE, b=ONE, superseded=()):
        out = tmp_path / 'output'
        for rel, results in (('run_a_mini', a), ('run_b_sol', b),
                             ('superseded/run_b_sol_pre_restructure',
                              superseded)):
            (out / rel).mkdir(parents=True, exist_ok=True)
            (out / rel / 'smoke_summary.json').write_text(
                json.dumps({'all_results': list(results)}))
        monkeypatch.setattr(gf, 'OUTPUT', str(out))
        return gf.compute_figures()
    return compute


# -- pct, fmt ---------------------------------------------------------------

def test_pct_one_decimal_place_by_default(gf):
    assert str(gf.pct(1, 3)) == '33.3'
    assert str(gf.pct(3, 40)) == '7.5'


def test_pct_other_places(gf):
    assert str(gf.pct(1, 3, places=2)) == '33.33'
    assert str(gf.pct(1, 3, places=0)) == '33'


def test_pct_zero_denominator_is_unquantised_zero(gf):
    # '0', not '0.0' as a quantised zero would print.
    assert str(gf.pct(5, 0)) == '0'


@pytest.mark.finding('S3-G8-6')
def test_pct_rounds_half_to_even(gf):
    # quantize() uses the context's rounding, ROUND_HALF_EVEN; the module
    # imports ROUND_HALF_UP and never uses it. Correct: half up, 6.3.
    assert str(gf.pct(1, 16)) == '6.2'
    assert str(gf.pct(3, 16)) == '18.8'


def test_import_sets_decimal_precision_50(gf):
    from decimal import getcontext
    assert getcontext().prec == 50


def test_fmt_int_with_thousands_separator(gf):
    assert gf.fmt(1234567) == '1,234,567'


def test_fmt_decimal_as_is(gf):
    assert gf.fmt(Decimal('1234.50')) == '1234.50'


# -- classify_originated_mechanism ------------------------------------------

def test_classify_ungrounded_chain(gf):
    assert gf.classify_originated_mechanism(
        originated(['computed_in_session_ungrounded'])) == 'ungrounded'


def test_classify_ungrounded_chain_wins_over_sign_inversion(gf):
    assert gf.classify_originated_mechanism(
        originated(['computed_in_session_ungrounded'], sign={'x': 1})
    ) == 'ungrounded'


def test_classify_sign_inversion(gf):
    assert gf.classify_originated_mechanism(
        originated(['originated'], sign={'field': 'f'})) == 'sign_inv'


@pytest.mark.parametrize('sign', [None, False])
def test_classify_no_sign_finding_is_untraceable(gf, sign):
    p = originated(['originated'])
    p['operand_resolutions'][0]['sign_inversion_finding'] = sign
    assert gf.classify_originated_mechanism(p) == 'untraceable'


def test_classify_without_resolutions_is_untraceable(gf):
    assert gf.classify_originated_mechanism(
        {'outcome': 'OPERAND-ORIGINATED'}) == 'untraceable'


# -- compute_figures: counts per run ----------------------------------------

def test_compute_entry_and_condition_counts(figures):
    v = figures(a=[result('Q01'), result('Q01', IR), result('Q02', IR)])
    assert (v['a_total_entries'], v['a_base_count'], v['a_ir_count']) == (
        3, 1, 2)


def test_compute_counts_run_b_with_prefix_b(figures):
    v = figures(b=[result('Q01'), result('Q02')])
    assert v['b_total_entries'] == 2
    assert v['a_total_entries'] == 1


def test_compute_invocation_counts(figures):
    v = figures(a=[result('Q01'), result('Q02'), result('Q03'),
                   result('Q01', invocation='NOT-INVOKED'),
                   result('Q01', IR), result('Q02', IR, 'NOT-INVOKED'),
                   result('Q02', IR, 'NOT-INVOKED'),
                   result('Q03', IR, 'NOT-INVOKED'),
                   result('Q04', IR, 'EV-0')])
    assert v['a_invoked_base'] == 3
    assert v['a_not_invoked_base'] == 1
    assert v['a_invoked_ir'] == 1
    assert v['a_not_invoked_ir'] == 3
    assert (v['a_ni_Q02'], v['a_ni_Q03']) == (2, 1)
    assert 'a_ni_Q01' not in v
    assert v['a_ni_pct'] == Decimal('60.0')


def test_compute_operation_counts(figures):
    v = figures(a=[result('Q01', ops=['WRONG-OPERATION', 'OPERATION-CORRECT']),
                   result('Q01', IR, ops=['WRONG-OPERATION'] * 2),
                   result('Q02', IR, ops=['OPERATION-CORRECT'] * 2)])
    assert (v['a_total_ops'], v['a_wrong_ops'], v['a_correct_ops']) == (
        6, 3, 3)
    assert v['a_wo_pct'] == Decimal('50.0')
    assert (v['a_wo_base'], v['a_total_base_ops']) == (1, 2)
    assert v['a_wo_base_pct'] == Decimal('50.0')
    assert (v['a_wo_ir'], v['a_total_ir_ops']) == (2, 4)
    assert v['a_wo_ir_pct'] == Decimal('50.0')


def test_compute_any_outcome_but_wrong_operation_counts_as_correct(figures):
    # An unobservable or unknown operation outcome is counted "correct".
    v = figures(a=[result('Q01', ops=['OPERATION-UNOBSERVABLE', 'other'])])
    assert v['a_correct_ops'] == 2


def test_compute_no_operations_gives_zero_percentages(figures):
    v = figures(a=[result('Q01')])
    assert v['a_wo_pct'] == Decimal('0')
    assert v['a_wo_base_pct'] == Decimal('0')


def test_compute_wrong_operations_split_by_figure_outcome(figures):
    wo = ['WRONG-OPERATION']
    v = figures(a=[result('Q01', figure='AUTO-MATCH', ops=wo * 2),
                   result('Q01', figure='AUTO-MISMATCH', ops=wo),
                   result('Q01', figure='MISMATCH', ops=wo),
                   result('Q01', figure='ADJUDICATE-TWO', ops=wo * 2),
                   result('Q01', figure='ADJUDICATE-NONE', ops=wo),
                   result('Q01', figure='AUTO-MATCH',
                          ops=['OPERATION-CORRECT'])])
    assert v['a_wo_route_divergence'] == 2
    assert v['a_wo_item_wrong'] == 2
    assert v['a_wo_adjudicated'] == 3


def test_compute_provenance_counts(figures):
    other = {'outcome': 'OPERANDS-UNOBSERVABLE'}
    v = figures(a=[result('Q01', prov=[grounded('source_match'),
                                       grounded('constant'),
                                       originated(['originated']), other])])
    assert (v['a_prov_grounded'], v['a_prov_originated'],
            v['a_total_prov']) == (2, 1, 4)
    assert v['a_grounded_pct'] == Decimal('50.0')
    assert v['a_originated_pct'] == Decimal('25.0')


def test_compute_operand_resolution_counts(figures):
    p = grounded('source_match', 'source_match', 'constant',
                 'transformed_source', 'intermediate', 'computed_in_session',
                 'computed_in_session_ungrounded', 'originated')
    p['operand_resolutions'].append({})
    v = figures(a=[result('Q01', prov=[p])])
    assert v['a_total_resolutions'] == 9
    assert v['a_res_source_match'] == 2
    for name in ('constant', 'transformed_source', 'intermediate',
                 'computed_in_session', 'computed_in_session_ungrounded',
                 'originated'):
        assert v[f'a_res_{name}'] == 1
    assert v['a_res_cis_ungrounded'] == 1
    assert 'a_res_UNKNOWN' not in v


def test_compute_absent_resolution_kinds_are_zero(figures):
    v = figures(a=[result('Q01')])
    assert v['a_res_source_match'] == 0
    assert v['a_res_cis_ungrounded'] == 0
    assert v['a_total_resolutions'] == 0


def test_compute_results_without_lists_count_nothing(figures):
    # Entries without operation_correctness or provenance_results (and a
    # provenance result without operand lists) are read as empty.
    bare = {'item_id': 'Q07', 'condition': 'base',
            'invocation_outcome': 'NOT-INVOKED', 'figure_outcome': 'MISMATCH'}
    bare_prov = dict(bare, provenance_results=[
        {'outcome': 'OPERAND-ORIGINATED'}])
    v = figures(a=[bare, bare_prov], b=[bare], superseded=[bare, bare_prov])
    assert (v['a_total_ops'], v['a_total_prov'], v['a_total_resolutions'],
            v['a_total_originated_operands'], v['a_step4_total']) == (
        0, 1, 0, 0, 0)
    assert (v['a_Q07_wo'], v['a_Q07_total_ops']) == (0, 0)
    assert v['a_Q10_calls_per_exec'] == 0.0
    assert v['b_ops_per_exec'] == 0.0
    assert v['a_wo_item_wrong_cp'] == '0/0'
    assert v['sup_total_originated'] == 0


def test_compute_reads_the_three_summaries(gf, figures, monkeypatch):
    # The exact files read (case included: a case-insensitive file
    # system would not notice a wrong case), as UTF-8.
    figures()  # writes the summaries
    read = []
    real_open = open

    def recording_open(path, *args, **kwargs):
        read.append((path, kwargs.get('encoding')))
        return real_open(path, *args, **kwargs)
    monkeypatch.setattr(gf, 'open', recording_open, raising=False)
    gf.compute_figures()
    out = gf.OUTPUT
    assert [p for p, _ in read] == [
        os.path.join(out, 'run_a_mini', 'smoke_summary.json'),
        os.path.join(out, 'run_b_sol', 'smoke_summary.json'),
        os.path.join(out, 'superseded', 'run_b_sol_pre_restructure',
                     'smoke_summary.json')]
    assert all(e is not None and e.lower() == 'utf-8' for _, e in read)


def test_compute_sign_inversions_counts_any_finding_not_none_or_false(
        figures):
    p = grounded('source_match', 'constant', 'intermediate', 'originated')
    for res, sign in zip(p['operand_resolutions'],
                         [{'field': 'f'}, None, False, 0]):
        res['sign_inversion_finding'] = sign
    v = figures(a=[result('Q01', prov=[p])])
    # {'field': 'f'} and 0 count; None and False do not.
    assert v['a_sign_inversions'] == 2


def test_compute_originated_operand_values(figures):
    p1 = originated(['originated'], operands=[{'value': -12.0}, '45', 2])
    p2 = originated(['originated'], operands=[{'value': '-12'}, {'x': 1}])
    v = figures(a=[result('Q01', prov=[p1, p2])])
    assert v['a_total_originated_operands'] == 5
    assert v['a_orig_vals'] == {'-12.0': 1, '45': 1, '2': 1, '-12': 1,
                                "{'x': 1}": 1}
    assert v['a_sign_inv_operand_vals'] == 2
    assert (v['a_orig_-12.0'], v['a_orig_45'], v['a_orig_2']) == (1, 1, 1)
    assert v['a_orig_1.0065'] == 0


def test_compute_named_originated_values_for_both_runs(figures):
    named = ['1.0065', '45', '2', '1.18', '1.015', '35.63', '2436', '-12.0',
             '-12', '233.54166666666666']
    ops = [n for i, n in enumerate(named) for _ in range(i + 1)]
    p = originated(['originated'], operands=ops + ['99'])
    v = figures(a=[result('Q01', prov=[p])], b=[result('Q01', prov=[p])])
    for pfx in ('a', 'b'):
        assert [v[f'{pfx}_orig_{n}'] for n in named] == list(range(1, 11))


def test_compute_originated_outcomes_by_mechanism_and_item(figures):
    v = figures(a=[
        result('Q01', prov=[originated(['originated'], sign={'f': 1}),
                            originated(['originated']),
                            originated(['originated'])]),
        result('Q02', prov=[grounded('source_match'),
                            originated(['computed_in_session_ungrounded'])]),
    ])
    assert (v['a_outcomes_sign_inv'], v['a_outcomes_ungrounded'],
            v['a_outcomes_untraceable']) == (1, 1, 2)
    assert v['a_orig_item_Q01'] == 3
    assert v['a_orig_item_Q01_sign_inv'] == 1
    assert v['a_orig_item_Q01_untraceable'] == 2
    assert 'a_orig_item_Q01_ungrounded' not in v
    assert v['a_orig_item_Q02'] == 1
    assert v['a_excl_sign_originated'] == 3
    assert v['a_untraceable'] == 2
    assert v['a_ungrounded_chain'] == 1


def test_compute_d1_auto_match(figures):
    v = figures(a=[result('Q01'), result('Q01', figure='AUTO-MISMATCH')])
    assert v['a_d1_auto_match'] == 1


def test_compute_d1_auto_match_none_is_zero(figures):
    v = figures(a=[result('Q07', figure='AUTO-MISMATCH')])
    assert v['a_d1_auto_match'] == 0
    assert v['a_Q07_auto_match'] == 0


def test_compute_detail_for_q07_q08_q10(figures):
    v = figures(a=[
        result('Q07', ops=['WRONG-OPERATION', 'OPERATION-CORRECT']),
        result('Q07', IR, figure='AUTO-MISMATCH'),
        result('Q08', ops=['OPERATION-CORRECT']),
        result('Q01', ops=['WRONG-OPERATION']),
    ])
    assert (v['a_Q07_auto_match'], v['a_Q07_total'], v['a_Q07_wo'],
            v['a_Q07_total_ops']) == (1, 2, 1, 2)
    assert v['a_Q07_wo_pct'] == Decimal('50.0')
    assert v['a_Q07_am_pct'] == Decimal('50.0')
    assert v['a_Q08_wo_pct'] == Decimal('0.0')
    # No Q10 results: counts are zero, no percentages.
    assert (v['a_Q10_total'], v['a_Q10_total_ops']) == (0, 0)
    assert 'a_Q10_wo_pct' not in v
    assert 'a_Q10_am_pct' not in v
    assert 'a_Q01_total' not in v


def test_compute_auto_match_percentages_for_both_runs(figures):
    runs = [result('Q07'), result('Q08'), result('Q10'),
            result('Q10', figure='AUTO-MISMATCH')]
    v = figures(a=runs, b=runs)
    for pfx in ('a', 'b'):
        assert (v[f'{pfx}_Q07_am_pct'], v[f'{pfx}_Q08_am_pct'],
                v[f'{pfx}_Q10_am_pct']) == (
            Decimal('100.0'), Decimal('100.0'), Decimal('50.0'))


def test_compute_q08_base_only(figures):
    v = figures(a=[result('Q08'), result('Q08'),
                   result('Q08', figure='AUTO-MISMATCH'), result('Q08', IR)])
    assert (v['a_Q08_base_am'], v['a_Q08_base_total']) == (2, 3)


def test_compute_step4_by_item(figures):
    v = figures(a=[
        result('Q03', prov=[grounded('computed_in_session',
                                     'computed_in_session')]),
        result('Q05', prov=[grounded('computed_in_session',
                                     'computed_in_session_ungrounded')]),
    ])
    assert v['a_step4_total'] == 3
    assert (v['a_step4_Q03'], v['a_step4_Q05']) == (2, 1)


# -- compute_figures: derived and cross-run figures ---------------------------

def test_compute_b_untraceable_is_all_originated_but_constant_2(figures):
    # Every originated operand value of run B except 2 counts as
    # untraceable, whatever its mechanism (sign inversions included).
    p = originated(['originated'], operands=['2', '2', '45', '-12.0'],
                   sign={'f': 1})
    v = figures(b=[result('Q01', prov=[p])])
    assert v['b_untraceable'] == 2
    assert (v['b_orig_2_count'], v['b_orig_45_count'],
            v['b_orig_1_0065_count']) == (2, 1, 0)


def test_compute_combined_untraceable(figures):
    a = [result('Q01', prov=[originated(['originated'])])]
    b = [result('Q01', prov=[originated(['originated'],
                                        operands=['45', '7'])])]
    v = figures(a=a, b=b)
    assert v['combined_untraceable'] == 1 + 2


def test_compute_q07_recomputation_constants(figures):
    v = figures()
    assert v['q07_simple'] == Decimal('777.41')
    assert v['q07_compound'] == Decimal('782.77')
    assert v['q07_difference'] == Decimal('5.36')


def test_compute_b_ops_per_exec_is_a_rounded_float(figures):
    v = figures(b=[result('Q01', ops=['OPERATION-CORRECT'] * 2),
                   result('Q02'), result('Q03')])
    assert v['b_ops_per_exec'] == 0.67
    assert isinstance(v['b_ops_per_exec'], float)


@pytest.mark.finding('S3-G8-8')
def test_compute_empty_run_b_raises_zero_division(figures):
    # Run A guards its Q10 average against zero; run B's ops-per-execution
    # does not. Correct: a clear error naming the empty run (or 0).
    with pytest.raises(ZeroDivisionError):
        figures(b=[])


def test_compute_q10_calls_per_execution_of_run_a(figures):
    v = figures(a=[result('Q10', ops=['OPERATION-CORRECT'] * 3),
                   result('Q10', ops=['OPERATION-CORRECT'] * 2),
                   result('Q01', ops=['OPERATION-CORRECT'] * 9)])
    assert v['a_Q10_calls_per_exec'] == 2.5


def test_compute_q10_calls_per_execution_one_decimal(figures):
    v = figures(a=[result('Q10', ops=['OPERATION-CORRECT']), result('Q10'),
                   result('Q10')])
    assert v['a_Q10_calls_per_exec'] == 0.3


def test_compute_q10_calls_per_execution_without_q10_is_zero(figures):
    v = figures(a=[result('Q01')])
    assert v['a_Q10_calls_per_exec'] == 0.0


def test_compute_wrong_operation_bound_when_none_auto_scored_wrong(figures):
    wo = ['WRONG-OPERATION']
    v = figures(a=[result('Q01', figure='AUTO-MATCH', ops=wo * 2),
                   result('Q01', figure='ADJUDICATE-TWO', ops=wo)])
    assert (v['a_wo_auto_scored'], v['a_wo_auto_wrong']) == (2, 0)
    assert v['a_wo_item_wrong_cp'] == (
        '0/2 auto-scored (p_upper < %.4f, 95%% Clopper–Pearson)'
        % clopper_pearson_upper_k0(2))


def test_compute_wrong_operation_bound_for_a_single_auto_scored(figures):
    v = figures(b=[result('Q01', figure='AUTO-MATCH',
                          ops=['WRONG-OPERATION'])])
    assert v['b_wo_item_wrong_cp'] == (
        '0/1 auto-scored (p_upper < %.4f, 95%% Clopper–Pearson)'
        % clopper_pearson_upper_k0(1))


def test_compute_wrong_operation_ratio_when_some_auto_scored_wrong(figures):
    wo = ['WRONG-OPERATION']
    v = figures(a=[result('Q01', figure='AUTO-MISMATCH', ops=wo),
                   result('Q01', figure='AUTO-MATCH', ops=wo),
                   result('Q01', figure='MISMATCH', ops=wo)])
    assert (v['a_wo_auto_scored'], v['a_wo_auto_wrong']) == (2, 1)
    assert v['a_wo_item_wrong_cp'] == '1/2'


def test_compute_wrong_operation_ratio_when_none_auto_scored(figures):
    v = figures(a=[result('Q01', figure='MISMATCH',
                          ops=['WRONG-OPERATION'])])
    assert v['a_wo_item_wrong_cp'] == '0/0'


def test_compute_wrong_operation_ratio_uses_thousands_separator(figures):
    wo = ['WRONG-OPERATION']
    v = figures(a=[result('Q01', figure='AUTO-MISMATCH', ops=wo * 1000)])
    assert v['a_wo_item_wrong_cp'] == '1000/1,000'


@pytest.mark.finding('S3-G8-7')
def test_compute_base_noninvocation_bound_assumes_500_base_executions(
        figures):
    # The denominator is fixed at 500 (10 items x 50 repeats), whatever
    # the run holds: here a single base execution. Correct: the run's own
    # count of base executions.
    v = figures(a=[result('Q01')])
    assert v['a_base_noninvoke_cp'] == (
        '0/500 (p_upper < %.4f, 95%% Clopper–Pearson)'
        % clopper_pearson_upper_k0(500))


def test_compute_base_noninvocation_ratio_when_some(figures):
    v = figures(b=[result('Q01', invocation='NOT-INVOKED'),
                   result('Q02', invocation='NOT-INVOKED')])
    assert v['b_base_noninvoke_cp'] == '2/500'


def test_compute_superseded_run_counts(figures):
    p = originated(['originated'], operands=[
        '1', 1, {'value': '2400'}, '2400.0', '2400.00', '287500', 287500.0,
        '287500.00', '7'])
    v = figures(superseded=[result('Q01', prov=[p]), result('Q02')])
    assert v['sup_total_originated'] == 9
    assert v['sup_const_1'] == 2
    assert v['sup_remaining'] == 7
    assert v['sup_sign_conv'] == 6
    assert v['sup_entries'] == 2


def test_compute_superseded_without_constant_1_or_sign_conventions(figures):
    p = originated(['originated'], operands=['7'])
    v = figures(superseded=[result('Q01', prov=[p])])
    assert (v['sup_const_1'], v['sup_remaining'], v['sup_sign_conv']) == (
        0, 1, 0)


def test_compute_f6_summary_without_originated_outcomes(figures):
    v = figures()
    assert v['f6_per_item_summary'] == 'No originated outcomes were observed.'


def test_compute_f6_summary_single_item_singular_labels(figures):
    v = figures(a=[result('Q04', prov=[
        originated(['originated'], operands=['9'], sign={'f': 1}),
        originated(['computed_in_session_ungrounded']),
        originated(['originated'])])])
    assert v['f6_per_item_summary'] == (
        'Total: 1 originated operand values, concentrated on 1 item.\n'
        'Q04: 3 (1 sign inversion + 1 ungrounded chain + 1 untraceable).')


def test_compute_f6_summary_sorted_by_total_then_item_plural_labels(
        figures):
    sign = originated(['originated'], sign={'f': 1})
    untr = originated(['originated'])
    chain = originated(['computed_in_session_ungrounded'])
    v = figures(a=[result('Q09', prov=[sign]),
                   result('Q08', prov=[sign, sign, untr, untr, chain, chain]),
                   result('Q02', prov=[untr])])
    assert v['f6_per_item_summary'] == (
        'Total: 0 originated operand values, concentrated on 3 items.\n'
        'Q08: 6 (2 sign inversions + 2 ungrounded chain + 2 untraceable).\n'
        'Q02: 1 (1 untraceable).\n'
        'Q09: 1 (1 sign inversion).')


def test_compute_f6_summary_covers_run_a_only(figures):
    v = figures(b=[result('Q01', prov=[originated(['originated'])])])
    assert v['f6_per_item_summary'] == 'No originated outcomes were observed.'


# -- generate -----------------------------------------------------------------

def template(tmp_path, text):
    path = tmp_path / 'FINDINGS.template.md'
    path.write_text(text, encoding='utf-8')
    return str(path)


def test_generate_substitutes_values_by_type(gf, tmp_path):
    values = {'n': 1234, 'd': Decimal('12.50'), 's': 'text', 'f': 0.5}
    out = gf.generate(values, template(tmp_path, '{{n}} {{d}} {{s}} {{f}}\n'))
    assert out == '1,234 12.50 text 0.5\n'


def test_generate_leaves_other_braces_alone(gf, tmp_path):
    out = gf.generate({'a': 'x'}, template(tmp_path, '{{a}} {{ a }} {a}\n'))
    assert out == 'x {{ a }} {a}\n'


def test_generate_missing_value_is_fatal(gf, tmp_path, capsys):
    with pytest.raises(SystemExit) as exc:
        gf.generate({'a': 1}, template(tmp_path, '{{zz}} {{a}} {{b}}\n'))
    assert exc.value.code == 1
    assert capsys.readouterr().err == (
        'FATAL: 2 placeholders have no computed value:\n  {{b}}\n  {{zz}}\n')


def test_generate_reports_unused_values_on_stderr(gf, tmp_path, capsys):
    values = {'used': 1, 'z_spare': 2, 'b_spare': Decimal('3.0')}
    gf.generate(values, template(tmp_path, '{{used}}\n'))
    assert capsys.readouterr().err == (
        'WARNING: 2 computed values unused in template:\n'
        '  b_spare = 3.0\n  z_spare = 2\n')


@pytest.mark.parametrize('key', [
    'a_orig_vals', 'sup_x', 'a_orig_x', 'b_orig_x', 'a_orig_item_Q01',
    'a_d1_x', 'b_d1_x', 'a_step4_Q01', 'b_step4_x', 'a_base_count',
    'b_base_count', 'a_ir_count', 'b_ir_count', 'a_invoked_base',
    'b_invoked_base', 'a_invoked_ir', 'b_invoked_ir', 'a_correct_ops',
    'b_correct_ops', 'a_total_prov', 'b_total_prov', 'a_total_entries',
    'b_total_entries', 'a_Q08_base_total', 'b_Q08_base_total',
    'a_wo_item_wrong', 'b_wo_item_wrong', 'zz_vals'])
def test_generate_does_not_report_internal_values_unused(gf, tmp_path,
                                                         capsys, key):
    gf.generate({'used': 1, key: 2}, template(tmp_path, '{{used}}\n'))
    assert capsys.readouterr().err == ''


def test_generate_a_step4_total_unused_is_reported(gf, tmp_path, capsys):
    # The noise prefix for run A is 'a_step4_Q', for run B 'b_step4_':
    # an unused a_step4_total is reported, b_step4_total is not.
    gf.generate({'a_step4_total': 1, 'b_step4_total': 1},
                template(tmp_path, 'none\n'))
    assert capsys.readouterr().err == (
        'WARNING: 1 computed values unused in template:\n'
        '  a_step4_total = 1\n')


def test_generate_writes_target_with_lf(gf, tmp_path):
    target = tmp_path / 'FINDINGS.md'
    out = gf.generate({'a': 'é'}, template(tmp_path, 'x {{a}}\ny\n'),
                      str(target))
    assert target.read_bytes() == 'x é\ny\n'.encode('utf-8')
    assert out == 'x é\ny\n'


def test_generate_opens_template_and_target_as_utf8_lf(gf, tmp_path,
                                                      monkeypatch):
    opened = []
    real_open = open

    def recording_open(path, mode='r', **kwargs):
        opened.append((mode, kwargs))
        return real_open(path, mode, **kwargs)
    monkeypatch.setattr(gf, 'open', recording_open, raising=False)
    gf.generate({'a': 1}, template(tmp_path, '{{a}}\n'),
                str(tmp_path / 'out.md'))
    assert opened == [('r', {'encoding': 'utf-8'}),
                      ('w', {'encoding': 'utf-8', 'newline': '\n'})]


def test_generate_without_target_writes_nothing(gf, tmp_path):
    before = sorted(os.listdir(tmp_path))
    gf.generate({'a': 1}, template(tmp_path, '{{a}}\n'))
    assert sorted(os.listdir(tmp_path)) == before + ['FINDINGS.template.md']


def test_generate_defaults_compute_figures_and_template(gf, figures,
                                                        tmp_path,
                                                        monkeypatch):
    figures()  # writes the summaries and points OUTPUT at them
    monkeypatch.setattr(gf, 'TEMPLATE',
                        template(tmp_path, 'n={{a_total_entries}}\n'))
    assert gf.generate() == 'n=1\n'


# -- main ---------------------------------------------------------------------

def test_main_writes_target_and_prints_size(gf, figures, tmp_path,
                                            monkeypatch, capsys):
    figures()
    monkeypatch.setattr(gf, 'TEMPLATE',
                        template(tmp_path, 'é {{a_total_entries}}\nz\n'))
    target = tmp_path / 'out.md'
    monkeypatch.setattr(gf, 'TARGET', str(target))
    gf.main()
    assert target.read_text(encoding='utf-8') == 'é 1\nz\n'
    out = capsys.readouterr().out
    n_values = len(gf.compute_figures())
    assert out == ('Generated FINDINGS.md: 2 lines, 7 bytes\n'
                   f'  Computed {n_values} values\n')


# -- module -------------------------------------------------------------------

def test_paths_are_fixed_under_the_repository_root(gf):
    root = os.path.dirname(os.path.dirname(TOOL))
    assert gf.ROOT == root
    assert gf.OUTPUT == os.path.join(root, 'output')
    assert gf.TEMPLATE == os.path.join(root, 'findings',
                                       'FINDINGS.template.md')
    assert gf.TARGET == os.path.join(root, 'findings', 'FINDINGS.md')


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('S3-G8-6')
@pytest.mark.parametrize('num, denom, shown', [(1, 16, '6.3'), (5, 16, '31.3'),
                                               (9, 16, '56.3')])
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G8-6: pct rounds half to even; ROUND_HALF_UP is '
                          'imported and never used')
def test_pct_rounds_half_up(gf, num, denom, shown):
    # Correct: the module imports ROUND_HALF_UP for pct, and the example
    # config's quantisation declares "rounding": "ROUND_HALF_UP", so
    # 6.25 % prints as 6.3. Each case is a tie on an even digit, where the
    # two modes differ.
    assert str(gf.pct(num, denom)) == shown


@pytest.mark.finding('S3-G8-7')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G8-7: the base non-invocation bound uses a '
                          'fixed n = 500')
def test_compute_base_noninvocation_bound_uses_the_runs_base_count(figures):
    # Correct: n is the run's own count of base executions: here 2 (the
    # instruction_removed result does not count).
    v = figures(a=[result('Q01'), result('Q02'), result('Q01', condition=IR)])
    assert v['a_base_noninvoke_cp'] == (
        '0/2 (p_upper < %.4f, 95%% Clopper–Pearson)'
        % clopper_pearson_upper_k0(2))


@pytest.mark.finding('S3-G8-8')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G8-8: an empty run B raises ZeroDivisionError')
def test_compute_empty_run_b_no_zero_division(figures):
    # Correct: like run A's guarded average, an empty run B gives 0 ops per
    # execution, or a clear error that names the empty run; never a bare
    # ZeroDivisionError.
    try:
        v = figures(b=[])
    except ZeroDivisionError as e:
        raise AssertionError('ZeroDivisionError: %s' % e)
    except Exception as e:  # a clear error is acceptable if it names the run
        assert 'run_b' in str(e) or 'run b' in str(e).lower(), repr(e)
    else:
        assert v['b_ops_per_exec'] == 0
