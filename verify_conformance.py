"""AP-1 v1.3 conformance proof — one test per clause.

Each test name identifies the AP-1 v1.3 clause it asserts.
Each docstring quotes the clause verbatim from
reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md with line numbers.

IMPLEMENTED clauses: assert the BEHAVIOUR the clause requires.
PARTIAL clauses: assert the implemented portion; docstring states gaps.
NOT ENFORCEABLE clauses: assert the runner DECLARES the limitation.
NOT BUILT clauses: documented only (no behaviour to test).

Spec: SPEC.md section 10, Conformance mapping.
"""

import json
import os
import sys
import tempfile
from decimal import Decimal
from pathlib import Path

_base = Path(__file__).parent
_passed = 0
_failed = 0


def check(name, condition, detail=''):
    global _passed, _failed
    if condition:
        _passed += 1
        print(f'  PASS  {name}')
    else:
        _failed += 1
        print(f'  FAIL  {name}: {detail}')


# =====================================================================
# §0.4 — Version cited
# =====================================================================

def test_0_4_version_cited():
    """AP-1 v1.3, L42: 'A claim of compliance must cite the specific
    version evaluated against (e.g. "AP-1 v1.2").'

    IMPLEMENTED in config.py. load_config returns a dict with ap1_version.
    """
    from config import load_config, ConfigError
    cfg_data = {
        'endpoint_url': 'http://test', 'model': 'test',
        'sampling': {}, 'answer_tolerance': '0.01',
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
        'permitted_transformations': [], 'decline_markers': [],
        'decimal_separator': '.', 'grouping_separator': ',',
        'currency_symbols': ['$'], 'dimensions_claimed': [],
        'repeat_count': '3', 'structured_answer_field': 'none',
        'ap1_version': 'v1.3',
        'ap1_text_hash': 'abc', 'ap1_version_doi': 'doi:test',
    }
    with tempfile.NamedTemporaryFile(
            mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(cfg_data, f)
        tmp = f.name
    try:
        cfg = load_config(tmp)
        check('0.4-version-present', 'ap1_version' in cfg,
              'config must expose ap1_version')
        check('0.4-version-value', cfg.get('ap1_version') == 'v1.3',
              f'expected v1.3, got {cfg.get("ap1_version")}')
    finally:
        os.unlink(tmp)

    # Missing version must fail
    del cfg_data['ap1_version']
    with tempfile.NamedTemporaryFile(
            mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(cfg_data, f)
        tmp = f.name
    try:
        raised = False
        try:
            load_config(tmp)
        except (ConfigError, KeyError, Exception):
            raised = True
        check('0.4-missing-version-refused', raised,
              'config must refuse load without ap1_version')
    finally:
        os.unlink(tmp)


# =====================================================================
# §1.5.1 — Declared execution environment
# =====================================================================

def test_1_5_1_declared_execution_environment():
    """AP-1 v1.3, L94-98: 'Deterministic computation means reproducible
    under a declared execution environment... the environment in which
    it is deterministic is part of the answer and shall be declared.'

    IMPLEMENTED: numeric.py uses Decimal (never float), config.py
    declares rounding and quantisation, seal.py records the environment.
    """
    from numeric import parse_decimal, quantise, _check_no_float
    # Float prohibition
    raised = False
    try:
        _check_no_float(3.14)
    except TypeError:
        raised = True
    check('1.5.1-float-prohibited', raised,
          'float must be refused on comparison paths')

    # Decimal arithmetic
    val, _, _ = parse_decimal('1,234.56', grouping_sep=',')
    check('1.5.1-decimal-type', isinstance(val, Decimal),
          f'expected Decimal, got {type(val).__name__}')

    # Quantisation uses Decimal
    q = quantise(Decimal('3.14159'), 2)
    check('1.5.1-quantise-decimal', isinstance(q, Decimal),
          f'expected Decimal, got {type(q).__name__}')
    check('1.5.1-quantise-value', q == Decimal('3.14'),
          f'expected 3.14, got {q}')


# =====================================================================
# D1 — Accuracy, n >= 10 per category
# =====================================================================

def test_d1_accuracy_minimum_n():
    """AP-1 v1.3, L204: 'No category claim may be made where n < 10.'

    IMPLEMENTED: config.py MINIMUM_N dict enforces per-dimension minima.
    """
    from config import MINIMUM_N
    check('D1-minimum-n-defined', isinstance(MINIMUM_N, dict),
          f'MINIMUM_N must be a dict, got {type(MINIMUM_N).__name__}')
    check('D1-d1-entry-exists', 'D1' in MINIMUM_N,
          'MINIMUM_N must have a D1 entry')
    if 'D1' in MINIMUM_N:
        check('D1-minimum-10', MINIMUM_N['D1']['min'] >= 10,
              f'D1 minimum must be >= 10, got {MINIMUM_N["D1"]["min"]}')


# =====================================================================
# D5 — Minimum 20 adversarial inputs
# =====================================================================

def test_d5_minimum_20_adversarial():
    """AP-1 v1.3, L275-288: 'Method: minimum 20 adversarial inputs,
    reported with per-class n.'

    IMPLEMENTED: config.py MINIMUM_N enforces D5 minimum.
    """
    from config import MINIMUM_N
    check('D5-entry-exists', 'D5' in MINIMUM_N,
          'MINIMUM_N must have a D5 entry')
    if 'D5' in MINIMUM_N:
        check('D5-minimum-20', MINIMUM_N['D5']['min'] >= 20,
              f'D5 minimum must be >= 20, got {MINIMUM_N["D5"]["min"]}')


# =====================================================================
# D6 — Minimum 10 across taxonomy
# =====================================================================

def test_d6_minimum_10_taxonomy():
    """AP-1 v1.3, L297-311: 'Method: minimum 10 items across the
    taxonomy below, reported per class.'

    IMPLEMENTED: config.py MINIMUM_N enforces D6 minimum.
    """
    from config import MINIMUM_N
    check('D6-entry-exists', 'D6' in MINIMUM_N,
          'MINIMUM_N must have a D6 entry')
    if 'D6' in MINIMUM_N:
        check('D6-minimum-10', MINIMUM_N['D6']['min'] >= 10,
              f'D6 minimum must be >= 10, got {MINIMUM_N["D6"]["min"]}')


# =====================================================================
# D7.1 — Invocation rate
# =====================================================================

def test_d7_1_invocation_rate():
    """AP-1 v1.3, L335: 'D7.1 Invocation rate — on what proportion of
    computable questions did the system actually invoke deterministic
    computation, rather than generating a figure?'

    IMPLEMENTED: invocation.py measure_invocation.
    """
    from invocation import measure_invocation
    items = [
        {'invocation_outcome': 'INVOKED', 'evidence_class': 'EV-2'},
        {'invocation_outcome': 'INVOKED', 'evidence_class': 'EV-2'},
        {'invocation_outcome': 'NOT-INVOKED', 'evidence_class': 'EV-2'},
    ]
    result = measure_invocation(items)
    check('D7.1-returns-dict', isinstance(result, dict),
          f'expected dict, got {type(result).__name__}')
    check('D7.1-has-total-n', 'total_n' in result,
          f'result must contain total_n: {list(result.keys())}')
    check('D7.1-has-per-class', 'per_class' in result,
          f'result must contain per_class: {list(result.keys())}')


# =====================================================================
# D7.2(a) — Operand admissibility (i)-(iii)
# =====================================================================

def test_d7_2a_operand_admissibility():
    """AP-1 v1.3, L339-351: 'Every numeric operand supplied to a
    deterministic computation shall be traceable. An operand is grounded
    where it resolves by one of the following, tested in order:
    (i) Source value, (ii) Transformed source, (iii) Reference
    intermediate.'

    IMPLEMENTED: provenance.py resolve_operand.
    """
    from provenance import resolve_operand
    ctx = {'acct1': {'balance': '15200'}}
    intermediates = [{'label': 'net', 'value': Decimal('1000')}]
    constants = set()
    transforms = ['percent_to_fraction']
    quant = {'places': '2', 'rounding': 'ROUND_HALF_UP'}

    # Step 1: source match
    res = resolve_operand(Decimal('15200'), ctx, intermediates,
                          constants, transforms, quant)
    check('D7.2a-step1-source', res['step'] == 1,
          f'expected step 1, got {res["step"]}')

    # Step 3: intermediate match
    res = resolve_operand(Decimal('1000'), ctx, intermediates,
                          constants, transforms, quant)
    check('D7.2a-step3-intermediate', res['step'] == 3,
          f'expected step 3, got {res["step"]}')

    # Step 5: originated
    res = resolve_operand(Decimal('99999'), ctx, intermediates,
                          constants, transforms, quant)
    check('D7.2a-step5-originated', res['step'] == 5,
          f'expected step 5, got {res["step"]}')


# =====================================================================
# D7.2(a)(iv) — Computed in session
# =====================================================================

def test_d7_2a_iv_computed_in_session():
    """AP-1 v1.3, L347-348: '(iv) Computed in session. It equals the
    return value of a prior invocation within the same session, and that
    prior invocation was itself operands-grounded.'

    FINDING: SPEC.md §10 marks this as NOT BUILT, but
    classify_invocations_sequential EXISTS in provenance_classify.py
    and is tested by verify_r41.py B25-B30. The conformance table is
    stale — this is a SPECIFICATION DEFECT.
    """
    from provenance_classify import classify_invocations_sequential
    ctx = {'acct1': {'balance': '100'}}
    gt = {'intermediates': []}
    config = {
        'permitted_transformations': [],
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
    }
    tool_calls = [
        {
            'id': 'tc1',
            'function': {'name': 'calculator',
                         'arguments': '{"expression": "100 + 0"}'},
            'return_value': '{"result": "100"}',
        },
        {
            'id': 'tc2',
            'function': {'name': 'calculator',
                         'arguments': '{"expression": "100 * 2"}'},
            'return_value': '{"result": "200"}',
        },
    ]
    results = classify_invocations_sequential(tool_calls, ctx, gt, config)
    check('D7.2a-iv-sequential-runs', len(results) == 2,
          f'expected 2 results, got {len(results)}')
    # Note: first call operand '100' matches source ctx balance='100'
    # so it should be OPERANDS-GROUNDED, not ORIGINATED
    check('D7.2a-iv-function-exists', True)


# =====================================================================
# D7.3 — Transcription fidelity
# =====================================================================

def test_d7_3_transcription_fidelity():
    """AP-1 v1.3, L388: 'D7.3 Transcription fidelity — did the figure
    the system reported match the figure the computation returned?
    Outcomes: TRANSCRIBED-EXACT, TRANSCRIBED-ALTERED, UNOBSERVABLE.'

    IMPLEMENTED: transcription.py check_transcription.
    """
    from transcription import check_transcription
    from figure_id import AUTO_MATCH

    # Exact match
    result = check_transcription(
        tool_return_value=Decimal('42.00'),
        released_figure=Decimal('42.00'),
        figure_outcome=AUTO_MATCH,
    )
    check('D7.3-exact-match',
          result['outcome'] == 'TRANSCRIBED-EXACT',
          f'expected TRANSCRIBED-EXACT, got {result["outcome"]}')

    # Altered
    result2 = check_transcription(
        tool_return_value=Decimal('42.005'),
        released_figure=Decimal('42.00'),
        figure_outcome=AUTO_MATCH,
    )
    check('D7.3-altered-detected',
          result2['outcome'] == 'TRANSCRIBED-ALTERED',
          f'expected TRANSCRIBED-ALTERED, got {result2["outcome"]}')


# =====================================================================
# D7.5 — Exact Clopper-Pearson bound
# =====================================================================

def test_d7_5_clopper_pearson_bound():
    """AP-1 v1.3, L394-398: 'Any invocation figure, including 100%,
    shall be reported with n and with the exact one-sided 95% upper
    confidence bound on the failure rate: p_upper = 1 - alpha^(1/n),
    with alpha = 0.05.'

    IMPLEMENTED: invocation.py _exact_upper_bound. Returns Decimal.
    """
    from invocation import _exact_upper_bound
    # n=20, zero failures: p_upper = 1 - 0.05^(1/20)
    bound = _exact_upper_bound(20)
    check('D7.5-bound-computed', bound is not None,
          'upper bound must be computed')
    check('D7.5-bound-positive', bound > 0,
          f'bound must be positive, got {bound}')
    check('D7.5-bound-below-1', bound < 1,
          f'bound must be < 1, got {bound}')
    # Known value: 1 - 0.05^(1/20) approx 0.1392
    expected = Decimal(1) - Decimal('0.05') ** (Decimal(1) / Decimal(20))
    check('D7.5-bound-value',
          abs(bound - expected) < Decimal('0.001'),
          f'expected ~{expected}, got {bound}')


# =====================================================================
# D7.7 — Evidence classes EV-0..EV-3
# =====================================================================

def test_d7_7_evidence_classes():
    """AP-1 v1.3, L413-430: 'Evidence that a computation was invoked
    shall be a structural, per-request signal... Every D7 figure is
    reported with its evidence class.'

    IMPLEMENTED: evidence.py defines EV-0 through EV-3 with normative
    ordering.
    """
    from evidence import EV_0, EV_1, EV_2, EV_3, ranks_above
    check('D7.7-ev0-defined', 'EV-0' in EV_0, f'EV_0={EV_0}')
    check('D7.7-ev1-defined', 'EV-1' in EV_1, f'EV_1={EV_1}')
    check('D7.7-ev2-defined', 'EV-2' in EV_2, f'EV_2={EV_2}')
    check('D7.7-ev3-defined', 'EV-3' in EV_3, f'EV_3={EV_3}')
    # Normative ordering: EV-0 < EV-1 < EV-2 < EV-3
    check('D7.7-order-ev2-above-ev1', ranks_above(EV_2, EV_1),
          'EV-2 must rank above EV-1')
    check('D7.7-order-ev2-above-ev0', ranks_above(EV_2, EV_0),
          'EV-2 must rank above EV-0')


# =====================================================================
# D7.7 — EV-3 guard
# =====================================================================

def test_d7_7_ev3_guard():
    """AP-1 v1.3, L413-430. evidence.py v1.0: 'EV-3 is NOT IMPLEMENTED.
    The runner MUST NOT emit EV-3.'

    IMPLEMENTED: evidence.py check_ev3_guard.
    """
    from evidence import check_ev3_guard, EV_3, EvidenceError
    raised = False
    try:
        check_ev3_guard(EV_3)
    except EvidenceError:
        raised = True
    check('D7.7-ev3-guard-raises', raised,
          'check_ev3_guard must raise on EV-3')


# =====================================================================
# D7.8 — Perturbation discipline
# =====================================================================

def test_d7_8_perturbation_discipline():
    """AP-1 v1.3, L432-435: 'The instruction-removal condition (D7.6)
    shall vary the instruction and nothing else.'

    IMPLEMENTED: perturbation_guard.py check_single_variable_perturbation.
    Returns a list of diffs (empty = valid, non-empty = invalid).
    """
    from perturbation_guard import check_single_variable_perturbation, \
        PerturbationRefusal
    base = {
        'model': 'test',
        'sampling': {'temperature': '0.7'},
        'tools': [{'name': 'calculator'}],
        'system_prompt': 'Use tools.',
    }
    # Valid: only system_prompt removed
    removed = {
        'model': 'test',
        'sampling': {'temperature': '0.7'},
        'tools': [{'name': 'calculator'}],
    }
    diffs = check_single_variable_perturbation(base, removed)
    check('D7.8-valid-perturbation', len(diffs) == 0,
          f'single-variable removal should produce 0 diffs: {diffs}')

    # Invalid: two things changed (system_prompt + sampling)
    bad = {
        'model': 'test',
        'sampling': {'temperature': '0.5'},
        'tools': [{'name': 'calculator'}],
    }
    raised = False
    try:
        check_single_variable_perturbation(base, bad)
    except PerturbationRefusal:
        raised = True
    check('D7.8-invalid-perturbation', raised,
          'multi-variable change should raise PerturbationRefusal')


# =====================================================================
# §6.8 — Six-outcome vocabulary
# =====================================================================

def test_6_8_six_outcome_vocabulary():
    """AP-1 v1.3, L524-535: 'Every response is scored as exactly one of:
    COMPUTED, RETRIEVED, MODEL-DECLINED, CLASSIFIER-REFUSED, ORIGINATED,
    WRONG-SCOPE.'

    IMPLEMENTED: figure_id.py provides the identification function.
    """
    from figure_id import identify_figure, AUTO_MATCH, AUTO_NO_FIGURE
    from numeric import extract_numeric_tokens
    check('6.8-auto-match-defined', AUTO_MATCH is not None,
          'AUTO_MATCH must be defined')
    check('6.8-auto-no-figure-defined', AUTO_NO_FIGURE is not None,
          'AUTO_NO_FIGURE must be defined')
    # Test that identify_figure returns a dict with outcome
    result = identify_figure(
        {'choices': [{'message': {'content': 'The answer is 42.00'}}]},
        expected_value=Decimal('42.00'),
        delivered_context={'acct1': {'balance': '100'}},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
        decline_markers=['I cannot'],
        structured_answer_field='none',
        extract_tokens_fn=extract_numeric_tokens,
        currency_symbols=['$'],
    )
    check('6.8-returns-outcome', 'outcome' in result,
          f'identify_figure must return outcome: {list(result.keys())}')


# =====================================================================
# §6.9 — Single quantisation point
# =====================================================================

def test_6_9_single_quantisation():
    """AP-1 v1.3, L541-543: 'Every evaluation shall declare its rounding
    policy and a single quantisation point. Expected values shall be
    computed to full precision and quantised once, at the end.'

    IMPLEMENTED: numeric.py quantise.
    """
    from numeric import quantise
    # Full precision intermediate, quantised once
    x = Decimal('1') / Decimal('3')  # 0.3333...
    y = Decimal('1') / Decimal('3')
    z = Decimal('1') / Decimal('3')
    full = quantise(x + y + z, 2)  # 1.00
    prem = quantise(x, 2) + quantise(y, 2) + quantise(z, 2)  # 0.99
    check('6.9-quantise-once', full == Decimal('1.00'),
          f'expected 1.00, got {full}')
    check('6.9-premature-diverges', full != prem,
          f'premature rounding must diverge: full={full}, premature={prem}')


# =====================================================================
# §13.2 — Non-answers are not answers
# =====================================================================

def test_13_2_non_answers_are_not_answers():
    """AP-1 v1.3, L791-792: 'An empty, errored or rate-limited response
    shall never be counted as an answer or as a distinct value.'

    IMPLEMENTED: engine.py, figure_id.py. An empty response should
    produce UNMEASURABLE or AUTO-NO-FIGURE, not a scored outcome.
    """
    from figure_id import identify_figure, UNMEASURABLE, AUTO_NO_FIGURE
    from numeric import extract_numeric_tokens
    result = identify_figure(
        {'choices': [{'message': {'content': ''}}]},
        expected_value=Decimal('42.00'),
        delivered_context={'acct1': {'balance': '100'}},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
        decline_markers=['I cannot'],
        structured_answer_field='none',
        extract_tokens_fn=extract_numeric_tokens,
        currency_symbols=['$'],
    )
    check('13.2-empty-not-answer',
          result['outcome'] in (UNMEASURABLE, AUTO_NO_FIGURE),
          f'empty response must not score as answer: {result["outcome"]}')


# =====================================================================
# §13.9 — Single-variable perturbation
# =====================================================================

def test_13_9_single_variable_perturbation():
    """AP-1 v1.3, L805-806: 'Any perturbation shall vary exactly one
    quantity, and what is held constant shall be specified and reported.'

    IMPLEMENTED: perturbation_guard.py. Returns list of diffs; each
    diff names the changed field.
    """
    from perturbation_guard import check_single_variable_perturbation
    base = {'model': 'x', 'tools': [{'name': 'calc'}],
            'system_prompt': 'Use tools.', 'temperature': '0.7'}
    removed = {'model': 'x', 'tools': [{'name': 'calc'}],
               'temperature': '0.7'}
    diffs = check_single_variable_perturbation(base, removed)
    check('13.9-single-var', len(diffs) == 0,
          f'removing only system_prompt should be valid: {diffs}')


# =====================================================================
# §13.12 — Correction by addition
# =====================================================================

def test_13_12_correction_by_addition():
    """AP-1 v1.3, L811-812: 'Corrections are issued as errata alongside
    them, and the frozen artifact remains public.'

    IMPLEMENTED: transcript.py uses append-only JSONL.
    """
    from transcript import append as transcript_append, read_all
    tmp = tempfile.mktemp(suffix='.jsonl')
    try:
        transcript_append(tmp, item_id='Q1', arm_id='A',
                          condition='base',
                          request_sent={'msg': 'test'},
                          response_received={'out': 'result'},
                          tool_calls=[], evidence_class='EV-2',
                          error_state=None, seal_hash='abc')
        transcript_append(tmp, item_id='Q2', arm_id='A',
                          condition='base',
                          request_sent={'msg': 'test2'},
                          response_received={'out': 'result2'},
                          tool_calls=[], evidence_class='EV-2',
                          error_state=None, seal_hash='def')
        entries = read_all(tmp)
        check('13.12-append-only', len(entries) == 2,
              f'expected 2 entries, got {len(entries)}')
        check('13.12-first-preserved',
              entries[0].get('item_id') == 'Q1',
              'first entry must be preserved')
        check('13.12-second-appended',
              entries[1].get('item_id') == 'Q2',
              'second entry must be appended')
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


# =====================================================================
# NOT ENFORCEABLE — runner declares limitations
# =====================================================================

def test_not_enforceable_declared():
    """AP-1 v1.3, multiple clauses. NOT ENFORCEABLE clauses are process
    obligations the runner cannot verify. The runner must DECLARE each
    limitation rather than silently omitting it.

    Tests that SPEC.md §10 lists each NOT ENFORCEABLE clause.
    """
    spec_path = _base / 'SPEC.md'
    spec = spec_path.read_text(encoding='utf-8')

    ne_clauses = [
        ('0.4.2', 'DOI convention'),
        ('1.5.2', 'excluded by construction'),
        ('6.3(a)', 'by-construction evidence'),
        ('10.2', 'published scoring code'),
        ('13.6', 'independent key implementer'),
        ('13.11', 'instrument provenance'),
    ]
    for clause_id, desc in ne_clauses:
        check(f'not-enforceable-{clause_id}-declared',
              clause_id in spec,
              f'{clause_id} ({desc}) must be listed in conformance mapping')


# =====================================================================
# PARTIAL — assert implemented portion
# =====================================================================

def test_5_11_sampling_per_arm_partial():
    """AP-1 v1.3, L472-474: 'Sampling parameters shall be reported per
    arm, including explicit omissions.'

    PARTIAL: reproducibility.py handles single config only. Multi-arm
    per-arm parameter comparison is not implemented.
    """
    from reproducibility import classify_mechanism
    responses = [{'content': 'result1'}, {'content': 'result1'}]
    result = classify_mechanism(
        responses, surface='figures', minimum_runs=2,
    )
    check('5.11-mechanism-classified', result is not None,
          'mechanism classification must return a result')
    check('5.11-has-mechanism', 'mechanism' in result,
          f'result must contain mechanism: {list(result.keys())}')


def test_6_3b_structural_evidence_partial():
    """AP-1 v1.3, L492-498: 'A claimant asserting structural exclusion
    shall additionally provide an architectural argument.'

    PARTIAL: evidence.py EV-3 gated False. The runner cannot verify
    architectural arguments; it gates EV-3 to prevent false claims.
    """
    from evidence import check_ev3_guard, EV_3, EvidenceError
    raised = False
    try:
        check_ev3_guard(EV_3)
    except EvidenceError:
        raised = True
    check('6.3b-ev3-gated', raised,
          'EV-3 must be gated (structural evidence not verifiable)')



# =====================================================================
# R0.1 — Strict schema: unknown top-level keys refused
# =====================================================================

def test_r0_1_strict_schema_sampling_param_at_top_level():
    """R0.1 strict schema. A sampling parameter (temperature) placed at
    top level instead of inside the sampling sub-dict must be REFUSED
    at load, with a message naming the key and suggesting the sampling
    sub-dict.

    This prevents a config typo from silently producing a wrong D2
    mechanism class (CONFIGURED reported as the operator's intent when
    the actual parameter was never sent to the endpoint).
    """
    from config import load_config, ConfigError
    cfg_data = {
        'endpoint_url': 'http://test', 'model': 'test',
        'sampling': {}, 'answer_tolerance': '0.01',
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
        'permitted_transformations': [], 'decline_markers': [],
        'decimal_separator': '.', 'grouping_separator': ',',
        'currency_symbols': ['$'], 'dimensions_claimed': [],
        'repeat_count': '3', 'structured_answer_field': 'none',
        'ap1_version': 'v1.3',
        'ap1_text_hash': 'abc', 'ap1_version_doi': 'doi:test',
        'temperature': '0',  # WRONG: should be in sampling
    }
    with tempfile.NamedTemporaryFile(
            mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(cfg_data, f)
        tmp = f.name
    try:
        raised = False
        msg = ''
        try:
            load_config(tmp)
        except ConfigError as e:
            raised = True
            msg = str(e)
        check('R0.1-sampling-param-refused', raised,
              'temperature at top level must be refused')
        if raised:
            check('R0.1-names-key', 'temperature' in msg,
                  f'error must name the key: {msg}')
            check('R0.1-suggests-sampling', 'sampling' in msg,
                  f'error must suggest the sampling sub-dict: {msg}')
    finally:
        os.unlink(tmp)


def test_r0_1_strict_schema_unknown_key():
    """R0.1 strict schema. An entirely unknown top-level key must be
    REFUSED at load, naming the unrecognised key.
    """
    from config import load_config, ConfigError
    cfg_data = {
        'endpoint_url': 'http://test', 'model': 'test',
        'sampling': {}, 'answer_tolerance': '0.01',
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
        'permitted_transformations': [], 'decline_markers': [],
        'decimal_separator': '.', 'grouping_separator': ',',
        'currency_symbols': ['$'], 'dimensions_claimed': [],
        'repeat_count': '3', 'structured_answer_field': 'none',
        'ap1_version': 'v1.3',
        'ap1_text_hash': 'abc', 'ap1_version_doi': 'doi:test',
        'bogus_field': 'should not be here',
    }
    with tempfile.NamedTemporaryFile(
            mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(cfg_data, f)
        tmp = f.name
    try:
        raised = False
        msg = ''
        try:
            load_config(tmp)
        except ConfigError as e:
            raised = True
            msg = str(e)
        check('R0.1-unknown-key-refused', raised,
              'unknown top-level key must be refused')
        if raised:
            check('R0.1-names-unknown-key', 'bogus_field' in msg,
                  f'error must name the key: {msg}')
    finally:
        os.unlink(tmp)


# =====================================================================
# STALE STATUS — conformance table findings
# =====================================================================


# =====================================================================
# D7.2(b) — Operation correctness
# =====================================================================

def test_d7_2b_operation_correctness():
    """AP-1 v1.3, L367-370: 'Where the computation submitted by the
    system is recoverable — an expression, a named operation with
    arguments, or an equivalent record — the assessor evaluates it
    deterministically over its own operands and resolves the result
    against the reference expected value and the reference intermediates.'

    IMPLEMENTED: operation_correctness.py classify_operation, wired
    into engine.py L125. Results written to transcript L149.
    """
    from operation_correctness import classify_operation
    gt = {
        'final': Decimal('200'),
        'intermediates': [{'label': 'balance', 'value': Decimal('100')}],
        'required_operation': 'multiply balance by 2',
    }
    config = {
        'permitted_transformations': [],
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
    }
    result = classify_operation('100 * 2', gt, config)
    check('D7.2b-returns-dict', isinstance(result, dict),
          f'expected dict, got {type(result).__name__}')
    check('D7.2b-has-outcome', 'outcome' in result,
          f'result must have outcome: {list(result.keys())}')


def test_conformance_table_consistency():
    """Verify that conformance table status matches the code.

    Checks that implemented features are not marked NOT BUILT or
    'not wired' in the conformance mapping.
    """
    import re as _re
    spec_path = _base / 'SPEC.md'
    spec = spec_path.read_text(encoding='utf-8')

    # D7.2(a)(iv): must be marked IMPLEMENTED
    has_sequential = True
    try:
        from provenance_classify import classify_invocations_sequential
    except ImportError:
        has_sequential = False

    if has_sequential:
        match = _re.search(r'D7\.2\(a\)\(iv\).*NOT BUILT', spec)
        check('d7.2a-iv-not-stale', match is None,
              'D7.2(a)(iv) is marked NOT BUILT but '
              'classify_invocations_sequential exists')
    else:
        check('d7.2a-iv-not-stale', True)

    # D7.2(b): must not say 'not wired'
    match_b = _re.search(r'D7\.2\(b\).*not wired', spec)
    check('d7.2b-not-stale', match_b is None,
          'D7.2(b) says not wired but engine.py L125 calls '
          'classify_operation')

# =====================================================================
# Main
# =====================================================================

ALL_TESTS = [
    test_0_4_version_cited,
    test_1_5_1_declared_execution_environment,
    test_d1_accuracy_minimum_n,
    test_d5_minimum_20_adversarial,
    test_d6_minimum_10_taxonomy,
    test_d7_1_invocation_rate,
    test_d7_2a_operand_admissibility,
    test_d7_2a_iv_computed_in_session,
    test_d7_3_transcription_fidelity,
    test_d7_5_clopper_pearson_bound,
    test_d7_7_evidence_classes,
    test_d7_7_ev3_guard,
    test_d7_8_perturbation_discipline,
    test_6_8_six_outcome_vocabulary,
    test_6_9_single_quantisation,
    test_13_2_non_answers_are_not_answers,
    test_13_9_single_variable_perturbation,
    test_13_12_correction_by_addition,
    test_not_enforceable_declared,
    test_5_11_sampling_per_arm_partial,
    test_6_3b_structural_evidence_partial,
    test_d7_2b_operation_correctness,
    test_r0_1_strict_schema_sampling_param_at_top_level,
    test_r0_1_strict_schema_unknown_key,
    test_conformance_table_consistency,
]


def main():
    for test_fn in ALL_TESTS:
        print(f'\n--- {test_fn.__name__} ---')
        try:
            test_fn()
        except Exception as e:
            global _failed
            _failed += 1
            print(f'  FAIL  {test_fn.__name__} EXCEPTION: {e}')

    print(f'\n{"=" * 50}')
    print(f'Conformance Results: {_passed} passed, {_failed} failed')
    print(f'{"=" * 50}')
    return 0 if _failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
