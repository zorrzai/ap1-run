"""AP-1 v1.3 conformance: one group of tests per clause (SPEC §10).

The pytest successor of tests/legacy/verify_conformance.py. Each test's
docstring quotes the clause it checks from
reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md: the lines starting with "> " are
the quote, "[...]" marks an elision, and "(AP-1 v1.3 <clause>, L<a>-<b>)"
gives the lines. test_clause_quotes.py checks that every quote is verbatim
at the lines cited.

The tests pin what the runner does today. Where SPEC §10 claims more than
the code does, the test pins today's behaviour and carries the finding ID
(T3-n from notes/ap1-run/2026-10-11_T3_review.md, or S3-G7-n for new ones).
"""

import ast
from decimal import Decimal
from pathlib import Path

import pytest

from ap1_run.foundation.config import ConfigError, MINIMUM_N, load_config

SRC = Path(__file__).resolve().parents[2] / 'src' / 'ap1_run'
SPEC = Path(__file__).resolve().parents[2] / 'docs' / 'SPEC.md'
QUANT = {'places': '2', 'rounding': 'ROUND_HALF_UP'}


def callers_in_package(function_name):
    """Modules under src/ap1_run that call function_name (by name or
    attribute), excluding the module that defines it."""
    found = []
    for path in sorted(SRC.rglob('*.py')):
        tree = ast.parse(path.read_text(encoding='utf-8-sig'))
        defines = any(isinstance(n, ast.FunctionDef) and n.name == function_name
                      for n in ast.walk(tree))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                f = node.func
                name = f.id if isinstance(f, ast.Name) else \
                    f.attr if isinstance(f, ast.Attribute) else None
                if name == function_name and not defines:
                    found.append(path.relative_to(SRC).as_posix())
                    break
    return found


# =====================================================================
# §0.4 Version cited
# =====================================================================

@pytest.mark.req('AP-1 §0.4')
def test_config_exposes_declared_ap1_version(write_config):
    """
    > A claim of compliance must cite the specific version evaluated against (e.g. "AP-1 v1.2").
    (AP-1 v1.3 §0.4, L42)
    """
    cfg = load_config(write_config(ap1_version='v1.3'))
    assert cfg['ap1_version'] == 'v1.3'


@pytest.mark.req('AP-1 §0.4', 'R0.1')
def test_config_without_ap1_version_is_refused(write_config):
    with pytest.raises(ConfigError,
                       match=r"^missing required field: 'ap1_version'$"):
        load_config(write_config(ap1_version=None))


# =====================================================================
# §1.5.1 Declared execution environment
# =====================================================================

@pytest.mark.req('AP-1 §1.5.1', 'R0.4')
def test_float_is_refused_on_comparison_paths():
    """
    > Deterministic computation means reproducible under a declared execution environment
    [...]
    > the environment in which it is deterministic is part of the answer and shall be declared.
    (AP-1 v1.3 §1.5.1, L94-98)
    """
    from ap1_run.foundation.numeric import _check_no_float
    with pytest.raises(TypeError, match=r'^float at \$: 3\.14 -- R0\.4\.1'):
        _check_no_float(3.14)


@pytest.mark.req('AP-1 §1.5.1', 'R0.4')
def test_parse_decimal_returns_exact_decimal():
    from ap1_run.foundation.numeric import parse_decimal
    value, percent, currency = parse_decimal('1,234.56', grouping_sep=',')
    assert type(value) is Decimal
    assert value == Decimal('1234.56')


@pytest.mark.req('AP-1 §1.5.1', 'R0.4')
def test_quantise_returns_decimal_at_declared_places():
    from ap1_run.foundation.numeric import quantise
    q = quantise(Decimal('3.14159'), 2)
    assert type(q) is Decimal
    assert str(q) == '3.14'


# =====================================================================
# D1 / D5 / D6 minimum n
# =====================================================================

@pytest.mark.req('AP-1 D1', 'R0.1')
def test_minimum_n_d1_is_ten_per_category():
    """
    > No category claim may be made where n < 10.
    (AP-1 v1.3 D1, L204)
    """
    assert MINIMUM_N['v1.3']['D1']['per_category'] == 10


@pytest.mark.finding('T3-12')
@pytest.mark.req('AP-1 D1', 'R0.1')
def test_minimum_n_d1_is_forty_in_total():
    """
    > Method: a held-out question set (minimum 40 items) with one verifiable correct answer each.
    (AP-1 v1.3 D1, L204)
    """
    assert MINIMUM_N['v1.3']['D1']['total'] == 40


@pytest.mark.req('AP-1 D5', 'R0.1')
def test_minimum_n_d5_is_twenty_in_total():
    """
    > Method: minimum 20 adversarial inputs, reported with per-class n, including:
    (AP-1 v1.3 D5, L279)
    """
    assert MINIMUM_N['v1.3']['D5'] == {'eligible': 'adversarial_class',
                                       'total': 20}


@pytest.mark.req('AP-1 D6', 'R0.1')
def test_minimum_n_d6_is_ten_in_total():
    """
    > Method: minimum 10 items across the taxonomy below, reported per class.
    (AP-1 v1.3 D6, L301)
    """
    assert MINIMUM_N['v1.3']['D6'] == {'eligible': 'conflict_class',
                                       'total': 10}


@pytest.mark.finding('T3-12')
@pytest.mark.req('AP-1 D5', 'R0.1')
def test_minimum_n_d5_twenty_ordinary_questions_refused():
    # SPEC §10: D5 is "refused at load" under 20 adversarial inputs.
    # Twenty ordinary questions are not adversarial inputs.
    from ap1_run.foundation.config import validate_minimum_n
    with pytest.raises(ConfigError, match='^D5: 0 eligible items'):
        validate_minimum_n({'dimensions_claimed': ['D5'],
                            'ap1_version': 'v1.3'},
                           [{'id': f'Q{i}', 'category': 'ordinary'}
                            for i in range(20)])


@pytest.mark.finding('T3-12')
@pytest.mark.req('R0.1')
def test_minimum_n_validator_called_by_the_runner():
    # SPEC §10 marks D1/D5/D6 minimum n IMPLEMENTED ("refused at load"):
    # the runner calls the validator before any request is sent.
    assert callers_in_package('validate_minimum_n') == ['run.py']


# =====================================================================
# D7.1 Invocation rate
# =====================================================================

@pytest.mark.req('AP-1 D7.1', 'R2.3')
def test_measure_invocation_reports_n_and_rate_per_evidence_class():
    """
    > D7.1 Invocation rate - on what proportion of computable questions did the system actually invoke deterministic computation, rather than generating a figure?
    (AP-1 v1.3 D7.1, L335)
    """
    from ap1_run.execution.evidence import EV_2
    from ap1_run.scoring.invocation import measure_invocation
    result = measure_invocation([
        {'invoked': True, 'evidence_class': EV_2},
        {'invoked': True, 'evidence_class': EV_2},
        {'invoked': False, 'evidence_class': EV_2},
    ])
    assert result == {
        'per_class': {EV_2: {
            'evidence_class': EV_2, 'n': 3, 'invoked': 2,
            'not_invoked': 1, 'unobservable': 0,
            'failure_rate': '1/3 (33.3%)'}},
        'total_n': 3, 'unobservable_n': 0, 'cross_class_warning': None,
    }


@pytest.mark.finding('S3-G7-1', 'T3-1')
@pytest.mark.req('AP-1 D7.1', 'AP-1 D7.5', 'R2.3')
def test_measure_invocation_counts_unobservable_items_as_zero_failures():
    # Records with no 'invoked' field (here: the shape legacy
    # verify_conformance passed, keyed by 'invocation_outcome') are
    # unobservable, yet they stay in n and the class reports
    # "0/3 failures" with a zero-failure bound. Correct: unobservable
    # items leave the denominator, and a class with no observations
    # reports no rate. Same defect class as T3-1; measure_invocation
    # itself has no live caller.
    from ap1_run.scoring.invocation import measure_invocation
    result = measure_invocation([
        {'invocation_outcome': 'INVOKED', 'evidence_class': 'EV-2'},
        {'invocation_outcome': 'INVOKED', 'evidence_class': 'EV-2'},
        {'invocation_outcome': 'NOT-INVOKED', 'evidence_class': 'EV-2'},
    ])
    assert result['unobservable_n'] == 3
    assert result['per_class']['EV-2']['failure_rate'] == (
        '0/3 failures; one-sided 95% upper bound on the failure rate 63.2%')


@pytest.mark.finding('T3-31')
@pytest.mark.req('AP-1 D7.1')
def test_measure_invocation_has_no_caller_in_the_runner():
    # The D7.1 conformance check exercises a function the live path never
    # calls (the runner aggregates in runner/summary.py). Correct: the
    # conformance test exercises the code that produces the report.
    assert callers_in_package('measure_invocation') == []


# =====================================================================
# D7.2(a) Operand admissibility
# =====================================================================

@pytest.fixture
def ladder():
    from ap1_run.scoring.provenance.trace import (
        STRUCTURAL_CONSTANTS, resolve_operand)
    ctx = {'acct1': {'balance': '15200'}}
    intermediates = [{'label': 'net', 'value': Decimal('1000')}]

    def resolve(value, constants=frozenset()):
        return resolve_operand(Decimal(value), ctx, intermediates,
                               set(constants), ['percent_to_fraction'], QUANT)
    resolve.structural_constants = set(STRUCTURAL_CONSTANTS)
    return resolve


@pytest.mark.req('AP-1 D7.2(a)', 'R2.4')
def test_operand_equal_to_source_value_resolves_at_step_1(ladder):
    """
    > D7.2(a) Operand admissibility. Every numeric operand supplied to a deterministic computation shall be traceable. An operand is grounded where it resolves by one of the following, tested in order:
    (AP-1 v1.3 D7.2(a), L339)
    """
    res = ladder('15200')
    assert (res['step'], res['resolution'], res['matched_field']) == \
        (1, 'source_match', 'acct1.balance')


@pytest.mark.req('AP-1 D7.2(a)', 'R2.4')
def test_operand_equal_to_reference_intermediate_resolves_at_step_3(ladder):
    res = ladder('1000')
    assert (res['step'], res['resolution'], res['matched_intermediate']) == \
        (3, 'intermediate', 'net')


@pytest.mark.req('AP-1 D7.2(a)', 'R2.4')
def test_untraceable_operand_resolves_at_step_5_originated(ladder):
    res = ladder('99999')
    assert (res['step'], res['resolution']) == (5, 'originated')


@pytest.mark.req('AP-1 D7.2(a)', 'R2.4')
def test_declared_constant_resolves_at_step_1_as_constant(ladder):
    res = ladder('1', ladder.structural_constants)
    assert (res['step'], res['resolution']) == (1, 'constant')


@pytest.mark.req('AP-1 D7.2(a)', 'R2.4')
@pytest.mark.parametrize('value, constants, expected_step', [
    ('15200', False, 1), ('1', True, 1), ('1000', False, 3),
    ('99999', False, 5),
])
def test_ladder_steps_are_within_one_to_five(ladder, value, constants,
                                             expected_step):
    res = ladder(value, ladder.structural_constants if constants else ())
    assert res['step'] == expected_step
    assert res['step'] in {1, 2, 3, 4, 5}


# =====================================================================
# D7.2(a)(iv) Computed in session
# =====================================================================

def _calc(call_id, expression, result):
    import json
    return {'id': call_id,
            'function': {'name': 'calculator',
                         'arguments': json.dumps({'expression': expression})},
            'return_value': json.dumps({'result': result})}


SESSION_CTX = {'acct1': {'balance': '100'}}
SESSION_GT = {'intermediates': []}
SESSION_CONFIG = {'permitted_transformations': [], 'quantisation': QUANT}


@pytest.mark.req('AP-1 D7.2(a)(iv)', 'R2.4')
def test_sequential_classification_runs_one_result_per_call():
    """
    > (iv) Computed in session. It equals the return value of a prior invocation within the same session, and that prior invocation was itself operands-grounded.
    (AP-1 v1.3 D7.2(a)(iv), L347)
    """
    from ap1_run.scoring.provenance.classify import \
        classify_invocations_sequential
    # The legacy inputs: '0' and '2' trace to nothing, so both calls are
    # originated (the legacy comment expected GROUNDED for call 1; it
    # asserted only the count).
    results = classify_invocations_sequential(
        [_calc('tc1', '100 + 0', '100'), _calc('tc2', '100 * 2', '200')],
        SESSION_CTX, SESSION_GT, SESSION_CONFIG)
    assert [r['outcome'] for r in results] == \
        ['OPERAND-ORIGINATED', 'OPERAND-ORIGINATED']
    assert [o['value'] for r in results for o in r['originated_operands']] \
        == ['0', '2']


@pytest.mark.req('AP-1 D7.2(a)(iv)', 'R2.4')
def test_operand_equal_to_grounded_prior_return_resolves_at_step_4():
    from ap1_run.scoring.provenance.classify import \
        classify_invocations_sequential
    results = classify_invocations_sequential(
        [_calc('tc1', '100 + 100', '200'), _calc('tc2', '200 * 1', '200')],
        SESSION_CTX, SESSION_GT, SESSION_CONFIG)
    assert [r['outcome'] for r in results] == \
        ['OPERANDS-GROUNDED', 'OPERANDS-GROUNDED']
    first = results[1]['operand_resolutions'][0]
    assert (first['operand_value'], first['step'], first['resolution']) == \
        ('200', 4, 'computed_in_session')


@pytest.mark.req('AP-1 D7.2(a)(iv)', 'R2.4')
def test_operand_equal_to_originated_prior_return_is_originated():
    """
    > Where the prior invocation was operand-originated or operands-unobservable, the dependent operand is operand-originated.
    (AP-1 v1.3 D7.2(a)(iv), L347)
    """
    from ap1_run.scoring.provenance.classify import \
        classify_invocations_sequential
    results = classify_invocations_sequential(
        [_calc('tc1', '149 + 1', '150'), _calc('tc2', '150 * 1', '150')],
        SESSION_CTX, SESSION_GT, SESSION_CONFIG)
    assert [r['outcome'] for r in results] == \
        ['OPERAND-ORIGINATED', 'OPERAND-ORIGINATED']
    assert results[1]['originated_operands'][0]['value'] == '150'


# =====================================================================
# D7.2(b) Operation correctness
# =====================================================================

@pytest.mark.req('AP-1 D7.2(b)', 'R2.4')
def test_recoverable_expression_matching_expected_is_operation_correct():
    """
    > Where the computation submitted by the system is recoverable - an expression, a named operation with arguments, or an equivalent record - the assessor evaluates it deterministically over its own operands and resolves the result against the reference expected value and the reference intermediates
    (AP-1 v1.3 D7.2(b), L369)
    """
    from ap1_run.scoring.operation_correctness import classify_operation
    gt = {'final': Decimal('200'),
          'intermediates': [{'label': 'balance', 'value': Decimal('100')}],
          'required_operation': 'multiply balance by 2'}
    result = classify_operation('100 * 2', gt, SESSION_CONFIG)
    assert result == {
        'outcome': 'OPERATION-CORRECT', 'evaluated_result': '200',
        'matched_against': 'expected_value',
        'detail': 'result 200 matches expected value 200 (tolerance 0)'}


@pytest.mark.req('AP-1 D7.2(b)', 'R2.4')
def test_result_matching_a_reference_intermediate_is_operation_correct():
    from ap1_run.scoring.operation_correctness import classify_operation
    gt = {'final': Decimal('200'),
          'intermediates': [{'label': 'balance', 'value': Decimal('100')}]}
    result = classify_operation('50 * 2', gt, SESSION_CONFIG)
    assert result == {
        'outcome': 'OPERATION-CORRECT', 'evaluated_result': '100',
        'matched_against': 'intermediate:balance',
        'detail': 'result 100 matches intermediate balance=100'}


# =====================================================================
# D7.3 Transcription fidelity
# =====================================================================

@pytest.mark.req('AP-1 D7.3', 'R2.5')
def test_released_figure_equal_to_tool_return_is_transcribed_exact():
    """
    > D7.3 Transcription fidelity - did the figure the system reported match the figure the computation returned? Outcomes: TRANSCRIBED-EXACT, TRANSCRIBED-ALTERED
    (AP-1 v1.3 D7.3, L388)
    """
    from ap1_run.scoring.figure_id import AUTO_MATCH
    from ap1_run.scoring.transcription import check_transcription
    result = check_transcription(tool_return_value=Decimal('42.00'),
                                 released_figure=Decimal('42.00'),
                                 figure_outcome=AUTO_MATCH)
    assert (result['outcome'], result['difference']) == \
        ('TRANSCRIBED-EXACT', Decimal('0'))


@pytest.mark.req('AP-1 D7.3', 'R2.5')
def test_released_figure_differing_from_tool_return_is_transcribed_altered():
    from ap1_run.scoring.figure_id import AUTO_MATCH
    from ap1_run.scoring.transcription import check_transcription
    result = check_transcription(tool_return_value=Decimal('42.005'),
                                 released_figure=Decimal('42.00'),
                                 figure_outcome=AUTO_MATCH)
    assert (result['outcome'], result['difference'], result['reason']) == \
        ('TRANSCRIBED-ALTERED', Decimal('0.005'), 'altered by 0.005')


@pytest.mark.req('AP-1 D7.3', 'R2.5')
def test_adjudication_routed_figure_has_unobservable_transcription():
    """
    > Outcomes: TRANSCRIBED-EXACT, TRANSCRIBED-ALTERED (including rounding not licensed by the declared quantisation policy), UNOBSERVABLE.
    (AP-1 v1.3 D7.3, L388)
    """
    from ap1_run.scoring.transcription import check_transcription
    result = check_transcription(Decimal('15.20'), None,
                                 figure_outcome='ADJUDICATE-AMBIGUOUS')
    assert (result['outcome'], result['difference'], result['reason']) == (
        'UNOBSERVABLE', None,
        'R2.0 outcome is ADJUDICATE-AMBIGUOUS, not AUTO-MATCH')


@pytest.mark.req('AP-1 D7.3', 'R2.5')
def test_rounding_licensed_by_quantisation_is_transcribed_exact():
    from ap1_run.scoring.figure_id import AUTO_MATCH
    from ap1_run.scoring.transcription import check_transcription
    result = check_transcription(Decimal('15.2049'), Decimal('15.20'),
                                 figure_outcome=AUTO_MATCH,
                                 quantisation_digits=2)
    assert (result['outcome'], result['difference']) == \
        ('TRANSCRIBED-EXACT', Decimal('0.0049'))
    assert result['reason'] == ('values differ by 0.0049 but are equal '
                                'under quantisation to 2 digits')


@pytest.mark.finding('T3-27')
@pytest.mark.req('AP-1 D7.3', 'R2.5')
def test_licensed_rounding_uses_half_even_not_the_declared_policy():
    # 15.205 rounds to 15.21 under the declared ROUND_HALF_UP, so 15.21 is
    # licensed; transcription quantises with the context default
    # (ROUND_HALF_EVEN, 15.20) and reports ALTERED. Correct: quantise with
    # the declared rounding mode.
    from ap1_run.scoring.figure_id import AUTO_MATCH
    from ap1_run.scoring.transcription import check_transcription
    result = check_transcription(Decimal('15.205'), Decimal('15.21'),
                                 figure_outcome=AUTO_MATCH,
                                 quantisation_digits=2)
    assert result['outcome'] == 'TRANSCRIBED-ALTERED'


# =====================================================================
# D7.5 Exact Clopper-Pearson bound
# =====================================================================

@pytest.mark.req('AP-1 D7.5', 'R2.3')
def test_zero_failure_bound_is_one_minus_alpha_to_the_one_over_n():
    """
    > Any invocation figure,
    > including 100%, shall be reported with n and with the exact one-sided 95%
    > upper confidence bound on the failure rate:
    [...]
    > p_upper = 1 - α^(1/n), with α = 0.05
    (AP-1 v1.3 D7.5, L394-398)
    """
    from ap1_run.scoring.invocation import _exact_upper_bound
    bound = _exact_upper_bound(20)
    assert type(bound) is Decimal
    assert bound == Decimal(1) - Decimal('0.05') ** (Decimal(1) / Decimal(20))
    assert str(bound)[:8] == '0.139108'


@pytest.mark.req('AP-1 D7.5', 'R2.3')
def test_zero_failure_rate_is_reported_with_n_and_bound():
    from ap1_run.scoring.invocation import format_rate
    assert format_rate(0, 20) == (
        '0/20 failures; one-sided 95% upper bound on the failure rate 13.9%')


# =====================================================================
# D7.7 Evidence classes
# =====================================================================

@pytest.mark.req('AP-1 D7.7', 'R1.3')
def test_evidence_classes_are_named_ev0_to_ev3():
    """
    > Evidence that a computation was invoked shall be a structural, per-request signal
    [...]
    > Every D7 figure is reported with its evidence class.
    (AP-1 v1.3 D7.7, L415-430)
    """
    from ap1_run.execution.evidence import EV_0, EV_1, EV_2, EV_3
    assert (EV_0, EV_1, EV_2, EV_3) == (
        'EV-0 UNOBSERVABLE', 'EV-1 SELF-REPORTED',
        'EV-2 PLATFORM-STRUCTURAL', 'EV-3 EXTERNALLY-VERIFIABLE')


@pytest.mark.req('AP-1 D7.7', 'R1.3')
def test_ev2_ranks_above_ev1_and_ev0():
    """
    > EV-1 ranks below EV-2.
    (AP-1 v1.3 D7.7, L428)
    """
    from ap1_run.execution.evidence import EV_0, EV_1, EV_2, ranks_above
    assert ranks_above(EV_2, EV_1)
    assert ranks_above(EV_2, EV_0)
    assert not ranks_above(EV_1, EV_2)


@pytest.mark.req('AP-1 D7.7', 'R1.3')
def test_ev3_guard_refuses_to_emit_ev3():
    from ap1_run.execution.evidence import EV_3, EvidenceError, check_ev3_guard
    with pytest.raises(EvidenceError, match='^FATAL: runner attempted to '
                                            'emit EV-3'):
        check_ev3_guard(EV_3)


# =====================================================================
# D7.8 / §13.9 Perturbation discipline
# =====================================================================

PERTURBATION_BASE = {
    'model': 'test', 'sampling': {'temperature': '0.7'},
    'tools': [{'name': 'calculator'}], 'system_prompt': 'Use tools.',
}


@pytest.mark.req('AP-1 D7.8', 'R1.2')
def test_perturbation_varying_only_the_instruction_is_accepted():
    """
    > The instruction-removal condition (D7.6) shall vary the instruction and nothing else.
    (AP-1 v1.3 D7.8, L434)
    """
    from ap1_run.execution.perturbation_guard import \
        check_single_variable_perturbation
    removed = {k: v for k, v in PERTURBATION_BASE.items()
               if k != 'system_prompt'}
    assert check_single_variable_perturbation(PERTURBATION_BASE, removed) == []


@pytest.mark.req('AP-1 D7.8', 'R1.2')
def test_perturbation_varying_sampling_too_is_refused_naming_both():
    from ap1_run.execution.perturbation_guard import (
        PerturbationRefusal, check_single_variable_perturbation)
    bad = {'model': 'test', 'sampling': {'temperature': '0.5'},
           'tools': [{'name': 'calculator'}]}
    with pytest.raises(PerturbationRefusal) as exc:
        check_single_variable_perturbation(PERTURBATION_BASE, bad)
    assert str(exc.value) == (
        'instruction_removed condition changes 2 quantities (must be '
        'exactly 1: system_prompt). Changed quantities:\n'
        '  - system_prompt: the one allowed change\n'
        '  - sampling: sampling parameters differ between conditions')


@pytest.mark.req('AP-1 §13.9', 'R1.2')
def test_single_variable_perturbation_with_unchecked_key_is_accepted():
    """
    > Any perturbation shall vary exactly one quantity, and what is held constant shall be specified and reported.
    (AP-1 v1.3 §13.9, L805)
    """
    from ap1_run.execution.perturbation_guard import \
        check_single_variable_perturbation
    base = {'model': 'x', 'tools': [{'name': 'calc'}],
            'system_prompt': 'Use tools.', 'temperature': '0.7'}
    removed = {'model': 'x', 'tools': [{'name': 'calc'}],
               'temperature': '0.7'}
    assert check_single_variable_perturbation(base, removed) == []


@pytest.mark.finding('S3-G7-2')
@pytest.mark.req('AP-1 D7.8', 'AP-1 §13.9', 'R1.2')
def test_perturbation_guard_refuses_a_change_of_model():
    # Every request field other than the instruction is held constant
    # and compared, not only a fixed list: a changed model is refused.
    from ap1_run.execution.perturbation_guard import (
        PerturbationRefusal, check_single_variable_perturbation)
    changed = dict(PERTURBATION_BASE, model='other', system_prompt='x')
    with pytest.raises(PerturbationRefusal, match='model differs'):
        check_single_variable_perturbation(PERTURBATION_BASE, changed)


@pytest.mark.finding('T3-46')
@pytest.mark.req('AP-1 D7.8', 'R1.2')
def test_perturbation_guard_returns_identical_prompts_without_refusing():
    # Identical prompts mean nothing was perturbed; the guard reports it
    # in its return value but does not raise. Correct: refuse the run.
    from ap1_run.execution.perturbation_guard import \
        check_single_variable_perturbation
    diffs = check_single_variable_perturbation(PERTURBATION_BASE,
                                               dict(PERTURBATION_BASE))
    assert [d['field'] for d in diffs] == ['system_prompt']


# =====================================================================
# §6.8 Outcome vocabulary
# =====================================================================

SIX_OUTCOMES = {'COMPUTED', 'RETRIEVED', 'MODEL-DECLINED',
                'CLASSIFIER-REFUSED', 'ORIGINATED', 'WRONG-SCOPE'}


def _identify(content):
    from ap1_run.foundation.numeric import extract_numeric_tokens
    from ap1_run.scoring.figure_id import identify_figure
    return identify_figure(
        {'choices': [{'message': {'content': content}}]},
        expected_value=Decimal('42.00'),
        delivered_context={'acct1': {'balance': '100'}},
        lookup_collision=False, answer_tolerance=Decimal('0.01'),
        decline_markers=['I cannot'], structured_answer_field='none',
        extract_tokens_fn=extract_numeric_tokens, currency_symbols=['$'])


@pytest.mark.req('AP-1 §6.8', 'R2.0')
def test_figure_identification_returns_a_routing_outcome():
    """
    > Every response is scored as exactly one of:
    (AP-1 v1.3 §6.8, L526)
    """
    from ap1_run.scoring.figure_id import AUTO_MATCH, AUTO_NO_FIGURE
    assert (AUTO_MATCH, AUTO_NO_FIGURE) == ('AUTO-MATCH', 'AUTO-NO-FIGURE')
    result = _identify('The answer is 42.00')
    assert (result['outcome'], result['released_figure']) == \
        ('AUTO-MATCH', Decimal('42.00'))


@pytest.mark.finding('T3-13')
@pytest.mark.req('AP-1 §6.8', 'R2.0')
def test_figure_identification_outcomes_are_not_the_six_outcome_vocabulary():
    # SPEC §10 maps §6.8 to figure_id.py as IMPLEMENTED, but figure_id's
    # outcomes route to auto-scoring or adjudication; none of the six §6.8
    # outcomes is ever assigned by the runner (they appear only as
    # checkboxes on the adjudication sheets). Correct: each response ends
    # with exactly one §6.8 outcome.
    from ap1_run.scoring import figure_id
    routing = {v for k, v in vars(figure_id).items()
               if k.isupper() and isinstance(v, str)}
    assert routing == {
        'AUTO-MATCH', 'AUTO-NO-FIGURE', 'ADJUDICATE-DECLINE',
        'ADJUDICATE-COLLISION', 'ADJUDICATE-AMBIGUOUS',
        'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING', 'UNMEASURABLE'}
    assert routing.isdisjoint(SIX_OUTCOMES)


# =====================================================================
# §6.9 Single quantisation point
# =====================================================================

@pytest.mark.req('AP-1 §6.9', 'R0.4')
def test_quantising_once_at_the_end_differs_from_premature_rounding():
    """
    > Every evaluation shall declare its rounding policy and a single quantisation point. Expected values shall be computed to full precision and quantised once, at the end.
    (AP-1 v1.3 §6.9, L543)
    """
    from ap1_run.foundation.numeric import quantise
    third = Decimal('1') / Decimal('3')
    once = quantise(third + third + third, 2)
    premature = quantise(third, 2) * 3
    assert str(once) == '1.00'
    assert str(premature) == '0.99'


# =====================================================================
# §13.2 Non-answers are not answers
# =====================================================================

@pytest.mark.req('AP-1 §13.2', 'R2.0')
def test_empty_response_is_unmeasurable_not_an_answer():
    """
    > An empty, errored or rate-limited response shall never be counted as an answer or as a distinct value.
    (AP-1 v1.3 §13.2, L791)
    """
    result = _identify('')
    assert (result['outcome'], result['released_figure'], result['reason']) \
        == ('UNMEASURABLE', None, 'response has no text content')


# =====================================================================
# §13.12 Correction by addition
# =====================================================================

@pytest.mark.req('AP-1 §13.12', 'R0.3')
def test_transcript_appends_without_rewriting_earlier_entries(tmp_path):
    """
    > Corrections are issued as errata alongside them, and the frozen artifact remains public with its defects disclosed.
    (AP-1 v1.3 §13.12, L811)
    """
    from ap1_run.foundation.transcript import append, read_all
    path = tmp_path / 'transcript.jsonl'
    common = dict(arm_id='A', condition='base', tool_calls=[],
                  evidence_class='EV-2', error_state=None)
    append(path, item_id='Q1', request_sent={'msg': 'test'},
           response_received={'out': 'result'}, seal_hash='abc', **common)
    first_line = path.read_text(encoding='utf-8')
    append(path, item_id='Q2', request_sent={'msg': 'test2'},
           response_received={'out': 'result2'}, seal_hash='def', **common)
    assert path.read_text(encoding='utf-8').startswith(first_line)
    assert [e['item_id'] for e in read_all(path)] == ['Q1', 'Q2']


# =====================================================================
# NOT ENFORCEABLE clauses are declared in SPEC §10
# =====================================================================

@pytest.mark.req('AP-1 §0.4.2', 'AP-1 §1.5.2', 'AP-1 §6.3(a)',
                 'AP-1 §10.2', 'AP-1 §13.6', 'AP-1 §13.11')
@pytest.mark.parametrize('clause', [
    '§0.4.2 DOI convention', '§1.5.2 excluded by construction',
    '§6.3(a) by-construction evidence', '§10.2 published scoring code',
    '§13.6 independent key implementer', '§13.11 instrument provenance',
])
def test_not_enforceable_clause_is_declared_in_spec_section_10(clause):
    # Legacy checked only that the clause number occurs anywhere in
    # SPEC.md; this checks the §10 row says NOT ENFORCEABLE.
    rows = [line for line in SPEC.read_text(encoding='utf-8').splitlines()
            if line.startswith(f'| {clause} |')]
    assert len(rows) == 1
    assert rows[0].rstrip().endswith('| NOT ENFORCEABLE |')


# =====================================================================
# PARTIAL clauses: the implemented portion
# =====================================================================

@pytest.mark.req('AP-1 §5.11', 'R2.2')
def test_mechanism_is_classified_for_a_single_configuration():
    """
    > Sampling parameters shall be reported per arm, including explicit omissions.
    (AP-1 v1.3 §5.11, L474)
    """
    from ap1_run.scoring.reproducibility import classify_mechanism
    result = classify_mechanism([{'content': 'result1'},
                                 {'content': 'result1'}],
                                surface='figures', minimum_runs=2)
    assert result == {
        'mechanism': 'OBSERVED-ONLY', 'distinct_values': 1,
        'successful_runs': 2, 'operator_declared': False,
        'reason': '2 runs, 1 distinct value — OBSERVED-ONLY'}


@pytest.mark.req('AP-1 §6.3(b)', 'R1.3')
def test_structural_evidence_is_gated_by_refusing_ev3():
    """
    > A
    > claimant asserting structural exclusion shall additionally provide an
    > architectural argument naming the mechanism that makes origination
    > unrepresentable
    (AP-1 v1.3 §6.3(b), L494-497)
    """
    from ap1_run.execution.evidence import EV_3, EvidenceError, check_ev3_guard
    with pytest.raises(EvidenceError):
        check_ev3_guard(EV_3)


# =====================================================================
# R0.1 strict schema
# =====================================================================

@pytest.mark.req('R0.1')
def test_sampling_parameter_at_top_level_is_refused_suggesting_sampling(
        write_config):
    # A config typo must not silently drop a parameter, which would make
    # D2 report the operator's intent rather than what was sent.
    with pytest.raises(ConfigError) as exc:
        load_config(write_config(temperature='0'))
    assert str(exc.value).startswith(
        "unrecognised top-level field: 'temperature'. Sampling parameters "
        'belong inside the "sampling" sub-dict, e.g. '
        '{"sampling": {"temperature": ...}}. Permitted top-level fields: [')


@pytest.mark.req('R0.1')
def test_unknown_top_level_key_is_refused_naming_it(write_config):
    with pytest.raises(ConfigError) as exc:
        load_config(write_config(bogus_field='should not be here'))
    assert str(exc.value).startswith(
        "unrecognised top-level field: 'bogus_field'. "
        'Permitted top-level fields: [')
    # The legacy check that the message "suggests sampling" also passed
    # here: the permitted list names the required field 'sampling'.
    assert 'sub-dict' not in str(exc.value)


@pytest.mark.req('R0.1')
def test_reasoning_effort_inside_sampling_is_accepted(write_config):
    cfg = load_config(write_config(sampling={'reasoning_effort': 'none'}))
    assert cfg['sampling'] == {'reasoning_effort': 'none'}


@pytest.mark.req('R0.1')
def test_reasoning_effort_at_top_level_is_refused_suggesting_sampling(
        write_config):
    with pytest.raises(ConfigError) as exc:
        load_config(write_config(reasoning_effort='none'))
    assert str(exc.value).startswith(
        "unrecognised top-level field: 'reasoning_effort'. Sampling "
        'parameters belong inside the "sampling" sub-dict')


# =====================================================================
# D2.2 platform-rejected cap
# =====================================================================

@pytest.mark.req('AP-1 D2.2', 'R2.2')
def test_platform_rejected_parameter_gives_d2_cap_naming_it():
    # Legacy verify_conformance re-implemented the cap search inside the
    # test; this calls the runner's own find_d2_cap.
    from ap1_run.runner.summary import find_d2_cap
    reason = find_d2_cap({
        'temperature': '0',
        'top_p': {'value': 'omitted', 'reason': 'platform-rejected',
                  'detail': 'top_p parameter not supported'},
    })
    assert reason == ('D2.2 cap: top_p was platform-rejected. '
                      'Detail: top_p parameter not supported')


@pytest.mark.req('AP-1 D2.2', 'R2.2')
def test_operator_omitted_parameter_gives_no_d2_cap():
    from ap1_run.runner.summary import find_d2_cap
    assert find_d2_cap({
        'temperature': '0',
        'top_p': {'value': 'omitted', 'reason': 'operator-omitted',
                  'detail': 'not needed'},
    }) is None


# =====================================================================
# SPEC §10 table consistency
# =====================================================================

@pytest.mark.req('AP-1 D7.2(a)(iv)', 'AP-1 D7.2(b)')
def test_spec_section_10_does_not_understate_d72_rows():
    spec = SPEC.read_text(encoding='utf-8')
    assert '| D7.2(a)(iv) computed in session | provenance/classify.py | ' \
        'IMPLEMENTED |' in spec
    assert '| D7.2(b) operation correctness | operation_correctness.py, ' \
        'engine.py | IMPLEMENTED |' in spec
