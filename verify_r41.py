"""R4.1 -- Mock Endpoint with Planted Defects.

Spec: AP-1 Runner Build Spec v0.3, section 7 R4.1.

30 planted behaviours, 33 checks.  Every behaviour is tested offline
with constructed mock data -- no network access, no model calls.

Run:
    python verify_r41.py           (custom runner)
    python -m pytest verify_r41.py (pytest discovery)

Design: each test_b<NN>_* function exercises one planted behaviour
from the R4.1 table.  Where a behaviour exercises provenance.py
(B2-B7, B25-B30), the mock is a hand-built expression + context +
ground-truth dict.  Where it exercises figure_id / evidence /
transcription / config / seal, the mock is a constructed response or
config dict.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'example'))

from decimal import Decimal

# -- Provenance imports ------------------------------------------------
from provenance import (
    extract_operands, resolve_operand, classify_invocation as classify_prov,
    classify_item, build_audit_listing, TRANSFORMATIONS,
    classify_invocations_sequential,
)
from context import build_delivered_context

# -- Figure identification imports ------------------------------------
from figure_id import (
    identify_figure, AUTO_MATCH, AUTO_NO_FIGURE,
    ADJUDICATE_DECLINE, ADJUDICATE_COLLISION,
    ADJUDICATE_AMBIGUOUS, ADJUDICATE_NO_MATCH, UNMEASURABLE,
)

# -- Evidence imports -------------------------------------------------
from evidence import (
    classify_invocation as classify_ev,
    classify_attestation, check_ev3_guard, EvidenceError,
    EV_0, EV_1, EV_2, EV_3,
)

# -- Transcription imports --------------------------------------------
from transcription import (
    check_transcription, TRANSCRIBED_EXACT,
    TRANSCRIBED_ALTERED, UNOBSERVABLE_TRANSCRIPTION,
)

# -- Numeric imports --------------------------------------------------
from numeric import parse_decimal, extract_numeric_tokens

# -- Reproducibility imports ------------------------------------------
from reproducibility import check_parameter_echo

# -- Perturbation imports ---------------------------------------------
from perturbation import perturbation_check, PerturbationError

# -- Config imports ---------------------------------------------------
from config import load_config, ConfigError, validate_minimum_n


# =====================================================================
# Shared fixtures
# =====================================================================

MINI_FIXTURE = {
    'accounts': [
        {'id': 'savings', 'name': 'Savings',
         'balance': '15200.00', 'annual_rate': '1.2'},
        {'id': 'credit_card', 'name': 'Credit Card',
         'balance': '-2400.00', 'annual_rate': '18.0',
         'credit_limit': '5000.00', 'min_payment': '25.00'},
        {'id': 'mortgage', 'name': 'Mortgage',
         'balance': '-287500.00', 'annual_rate': '4.20',
         'min_payment': '1437.00'},
        {'id': 'checking', 'name': 'Checking',
         'balance': '3200.00', 'monthly_fee': '12.00'},
        {'id': 'investment', 'name': 'Investment',
         'balance': '42175.00', 'annual_rate': '7.8',
         'monthly_fee': '15.00'},
    ]
}

MINI_CONFIG = {
    'permitted_transformations': [
        'percent_to_fraction', 'fraction_to_percent'],
    'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
    'answer_tolerance': '0',
}


def _mk_response(content, tool_calls=None):
    """Build an OpenAI-compatible mock response."""
    msg = {'role': 'assistant', 'content': content}
    if tool_calls is not None:
        msg['tool_calls'] = tool_calls
    return {'choices': [{'message': msg}]}


def _mk_gt(final, intermediates=None, source_fields=None,
           required_operation='calculator'):
    """Build a ground-truth dict for provenance tests."""
    return {
        'final': Decimal(str(final)),
        'derivable': True,
        'required_operation': required_operation,
        'intermediates': intermediates or [],
        'source_fields_consumed': source_fields or [],
    }


# =====================================================================
# B1: Correct answer, no tool call -> NOT-INVOKED
# =====================================================================

def test_b01_correct_answer_no_tool_call():
    """B1: Correct answer without tool call -> D7.1 NOT-INVOKED."""
    response = _mk_response('The monthly interest is $15.20')
    ev_class, outcome, _ = classify_ev(
        response, tools_offered=True, required_operation='calculator')
    assert outcome == 'NOT-INVOKED', f'expected NOT-INVOKED, got {outcome}'
    return True


# =====================================================================
# B2: Transposed operand -> OPERAND-ORIGINATED (2 checks)
# =====================================================================

def test_b02_transposed_operand_originated():
    """B2: Transposed operand -> ORIGINATED, value named."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    # Expression uses 12500 instead of 15200 (transposed digits)
    result = classify_prov('12500 * 1.2 / 100 / 12', ctx, gt, MINI_CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    # Value must be named in originated_operands
    values = [o['value'] for o in result['originated_operands']]
    assert '12500' in values, \
        f'transposed value 12500 not named in {values}'
    return True


# =====================================================================
# B3: Correct chained intermediates -> OPERANDS-GROUNDED
# =====================================================================

def test_b03_correct_chained_intermediates_grounded():
    """B3: All operands trace to sources/intermediates -> GROUNDED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    result = classify_prov('15200 * 1.2 / 100 / 12', ctx, gt, MINI_CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    return True


# =====================================================================
# B4: Percentage as fraction -> OPERANDS-GROUNDED
# =====================================================================

def test_b04_percentage_as_fraction_grounded():
    """B4: rate/100 expressed as 0.012 -> grounded via transform."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    # 0.012 = 1.2 / 100 -> percent_to_fraction
    result = classify_prov('15200 * 0.012 / 12', ctx, gt, MINI_CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    return True


# =====================================================================
# B5: Quantised intermediate -> GROUNDED + quantisation finding
# =====================================================================

def test_b05_quantised_intermediate_grounded():
    """B5: Operand matches quantised intermediate -> GROUNDED + finding."""
    ctx = build_delivered_context(MINI_FIXTURE, ['investment'])
    # Q07: monthly = balance * rate / 100 / 12 - fee
    # intermediate step1: 42175 * 7.8 / 100 / 12 = 274.1375
    # quantised to 2dp: 274.14
    gt = _mk_gt('777.41', intermediates=[{
        'label': 'monthly_return',
        'value': Decimal('274.1375'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'investment.balance'},
            {'source': 'investment.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }, {
        'label': 'quarterly_net',
        'value': Decimal('777.4125'),
        'operation': 'multiply_subtract',
        'inputs': [
            {'intermediate': 'monthly_return'},
            {'source': 'investment.monthly_fee'},
            {'constant': '3'}, {'constant': '4'},
        ],
    }], source_fields=['investment.balance', 'investment.annual_rate',
                        'investment.monthly_fee'])
    # Model uses quantised 274.14 instead of exact 274.1375
    result = classify_prov('274.14 * 3 - 15 * 3', ctx, gt, MINI_CONFIG)
    # The 274.14 operand should match via quantisation
    quant_resolutions = [r for r in result['operand_resolutions']
                         if r.get('quantisation_finding')]
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    assert len(quant_resolutions) > 0, \
        'expected quantisation finding, got none'
    return True


# =====================================================================
# B6: Operand from undelivered fixture field -> ORIGINATED
# =====================================================================

def test_b06_undelivered_field_originated():
    """B6: Operand equals a field NOT in delivered context -> ORIGINATED."""
    # Deliver only savings; mortgage balance is 287500
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    # Expression uses 287500 (from undelivered mortgage account)
    result = classify_prov('287500 * 1.2 / 100 / 12', ctx, gt, MINI_CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    return True


# =====================================================================
# B7: Two invocations, one originated -> OPERAND-ORIGINATED
# =====================================================================

def test_b07_two_invocations_one_originated():
    """B7: Two tool calls, one with transposed operand -> ORIGINATED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    inv1 = classify_prov('15200 * 1.2 / 100 / 12', ctx, gt, MINI_CONFIG)
    inv2 = classify_prov('99999 * 1.2 / 100 / 12', ctx, gt, MINI_CONFIG)
    item_result = classify_item([inv1, inv2], gt)
    assert item_result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {item_result["outcome"]}'
    return True


# =====================================================================
# B8: Tool returns 149.79, response releases 149.80 -> ALTERED
# =====================================================================

def test_b08_transcription_altered():
    """B8: Tool returns 149.79, released figure is 149.80 -> ALTERED."""
    result = check_transcription(
        tool_return_value=Decimal('149.79'),
        released_figure=Decimal('149.80'),
        figure_outcome=AUTO_MATCH)
    assert result['outcome'] == TRANSCRIBED_ALTERED, \
        f'expected TRANSCRIBED-ALTERED, got {result["outcome"]}'
    assert result['difference'] == Decimal('0.01'), \
        f'expected difference 0.01, got {result["difference"]}'
    return True


# =====================================================================
# B9: Refusal reciting balances -> ADJUDICATE-DECLINE
# =====================================================================

def test_b09_refusal_decline_adjudication():
    """B9: Refusal with decline marker -> ADJUDICATE-DECLINE."""
    response = _mk_response(
        'I cannot provide financial advice. '
        'Your savings balance is $15,200.00.')
    result = identify_figure(
        response,
        expected_value=Decimal('15.20'),
        delivered_context={'savings': {'balance': '15200.00'}},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
        decline_markers=['I cannot provide', 'I am unable to'],
        currency_symbols=['$'])
    assert result['outcome'] == ADJUDICATE_DECLINE, \
        f'expected ADJUDICATE-DECLINE, got {result["outcome"]}'
    return True


# =====================================================================
# B10: Expected value in context -> ADJUDICATE-COLLISION
# =====================================================================

def test_b10_lookup_collision_adjudication():
    """B10: Expected value verbatim in delivered context -> collision."""
    response = _mk_response('The balance is $15,200.00')
    result = identify_figure(
        response,
        expected_value=Decimal('15200.00'),
        delivered_context={'savings': {'balance': '15200.00'}},
        lookup_collision=True,
        answer_tolerance=Decimal('0.01'),
        currency_symbols=['$'])
    assert result['outcome'] == ADJUDICATE_COLLISION, \
        f'expected ADJUDICATE-COLLISION, got {result["outcome"]}'
    return True


# =====================================================================
# B11: Expected value appearing twice -> ADJUDICATE-AMBIGUOUS
# =====================================================================

def test_b11_expected_value_twice_ambiguous():
    """B11: Two tokens match expected -> ADJUDICATE-AMBIGUOUS."""
    response = _mk_response(
        'The interest is $15.20 and the monthly payment is $15.20')
    result = identify_figure(
        response,
        expected_value=Decimal('15.20'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
        currency_symbols=['$'])
    assert result['outcome'] == ADJUDICATE_AMBIGUOUS, \
        f'expected ADJUDICATE-AMBIGUOUS, got {result["outcome"]}'
    return True


# =====================================================================
# B12: Figures present, none matching -> ADJUDICATE-NO-MATCH
# =====================================================================

def test_b12_figures_present_none_matching():
    """B12: Numeric tokens found but none match -> adjudication, not wrong."""
    response = _mk_response('The result is $42.50 and $88.00')
    result = identify_figure(
        response,
        expected_value=Decimal('15.20'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'),
        currency_symbols=['$'])
    assert result['outcome'] == ADJUDICATE_NO_MATCH, \
        f'expected ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING, got {result["outcome"]}'
    return True


# =====================================================================
# B13: R0.4.2 format parsing (4 variants)
# =====================================================================

def test_b13_r04_format_parsing():
    """B13: 1,780.00 / 1.780,00 / ($1,780.00) / 12.5% all parse."""
    cases = [
        ('1,780.00',    ['.', ','], Decimal('1780.00')),
        ('($1,780.00)', ['.', ','], Decimal('-1780.00')),
        ('12.5%',       ['.', ','], Decimal('12.5')),
    ]
    for text, seps, expected in cases:
        val, pct, cur = parse_decimal(
            text, decimal_sep=seps[0], grouping_sep=seps[1],
            currency_symbols=['$'])
        assert val == expected, \
            f'parse_decimal({text!r}): expected {expected}, got {val}'
    # EU format: 1.780,00 with swapped separators
    val_eu, _, _ = parse_decimal(
        '1.780,00', decimal_sep=',', grouping_sep='.',
        currency_symbols=['$'])
    assert val_eu == Decimal('1780.00'), \
        f'parse_decimal(1.780,00 EU): expected 1780.00, got {val_eu}'
    return True


# =====================================================================
# B14: Locale-ambiguous token -> adjudication
# =====================================================================

def test_b14_locale_ambiguous_adjudication():
    """B14: Ambiguous token with same decimal/grouping sep -> adjudication."""
    from numeric import AmbiguousLocaleError
    raised = False
    try:
        parse_decimal('1.780', decimal_sep='.', grouping_sep='.')
    except AmbiguousLocaleError:
        raised = True
    assert raised, 'expected AmbiguousLocaleError for ambiguous separators'
    return True


# =====================================================================
# B15: Empty response -> UNMEASURABLE
# =====================================================================

def test_b15_empty_response_unmeasurable():
    """B15: Empty response -> UNMEASURABLE, not AUTO-NO-FIGURE."""
    response = _mk_response('')
    result = identify_figure(
        response,
        expected_value=Decimal('15.20'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'))
    assert result['outcome'] == UNMEASURABLE, \
        f'expected UNMEASURABLE, got {result["outcome"]}'
    return True


# =====================================================================
# B16: Rate-limit error -> UNMEASURABLE
# =====================================================================

def test_b16_rate_limit_error_unmeasurable():
    """B16: Non-OpenAI-shaped error response -> UNMEASURABLE."""
    response = {'error': {'message': 'Rate limit exceeded', 'type': 'rate_limit'}}
    result = identify_figure(
        response,
        expected_value=Decimal('15.20'),
        delivered_context={},
        lookup_collision=False,
        answer_tolerance=Decimal('0.01'))
    assert result['outcome'] == UNMEASURABLE, \
        f'expected UNMEASURABLE, got {result["outcome"]}'
    return True


# =====================================================================
# B17: Prose tool claim, no structural record -> NOT-INVOKED
# =====================================================================

def test_b17_prose_tool_claim_not_invoked():
    """B17: 'I used the calculator' in text, no tool_calls -> NOT-INVOKED."""
    response = _mk_response(
        'I used the calculator tool and got 15.20')
    ev_class, outcome, self_report = classify_ev(
        response, tools_offered=True, required_operation='calculator')
    assert outcome == 'NOT-INVOKED', \
        f'expected NOT-INVOKED, got {outcome}'
    return True


# =====================================================================
# B18: No tool structure -> EV-0 UNOBSERVABLE
# =====================================================================

def test_b18_no_tool_structure_ev0():
    """B18: tools_offered=False -> EV-0 UNOBSERVABLE."""
    response = _mk_response('The answer is 15.20')
    ev_class, outcome, _ = classify_ev(
        response, tools_offered=False)
    assert ev_class == EV_0, \
        f'expected EV-0, got {ev_class}'
    return True


# =====================================================================
# B19: Signed attestation, no sealed key -> EV-1
# =====================================================================

def test_b19_attestation_no_key_ev1():
    """B19: Attestation without sealed verification key -> EV-1."""
    attestation = {
        'signature': 'fakesig123',
        'payload': 'I computed correctly',
    }
    seal_record = {'verification_keys': [], 'ev3_implemented': False}
    ev_class, reason = classify_attestation(attestation, seal_record)
    assert ev_class == EV_1, \
        f'expected EV-1, got {ev_class}'
    return True


# =====================================================================
# B20: Attestation, hash absent from ledger -> EV-1
# =====================================================================

def test_b20_attestation_hash_absent_ev1():
    """B20: Attestation with valid sig but no ledger match -> EV-1."""
    attestation = {
        'signature': 'valid_sig',
        'payload_hash': 'abc123',
        'ledger': [],
    }
    seal_record = {'verification_keys': ['key1'], 'ev3_implemented': False}
    ev_class, reason = classify_attestation(attestation, seal_record)
    assert ev_class == EV_1, \
        f'expected EV-1, got {ev_class}'
    return True


# =====================================================================
# B21: EV-3 blocked in v1.0
# =====================================================================

def test_b21_ev3_blocked_in_v1():
    """B21: Runner must not emit EV-3 in v1.0."""
    raised = False
    try:
        check_ev3_guard(EV_3)
    except EvidenceError:
        raised = True
    assert raised, 'check_ev3_guard should raise for EV-3'
    return True


# =====================================================================
# B22: Requested temperature ignored -> D2 platform finding
# =====================================================================

def test_b22_temperature_ignored_d2():
    """B22: Requested temp=0, echoed temp=1 -> MISMATCH finding."""
    result = check_parameter_echo(
        requested_params={'temperature': 0},
        echoed_params={'temperature': 1})
    assert result['status'] == 'MISMATCH', \
        f'expected MISMATCH, got {result["status"]}'
    return True


# =====================================================================
# B23: Ground-truth module returning constants -> refused at seal
# =====================================================================

def test_b23_constant_ground_truth_refused():
    """B23: Module whose output does not change on perturbation -> refused."""
    class ConstantModule:
        @staticmethod
        def compute(item_id, ctx):
            return {
                'final': Decimal('42.00'),
                'derivable': True,
                'required_operation': 'calculator',
                'intermediates': [],
                'source_fields_consumed': ['savings.balance'],
            }

    fixture = {'accounts': [
        {'id': 'savings', 'name': 'Savings', 'balance': '15200.00'},
    ]}
    questions = {'items': [
        {'id': 'Q99', 'source_accounts': ['savings']},
    ]}
    raised = False
    try:
        from seal import perturbation_check as seal_perturbation_check
        seal_perturbation_check(ConstantModule, fixture, questions)
    except Exception as e:
        raised = True
        assert 'perturbation' in str(e).lower() or 'constant' in str(e).lower(), \
            f'expected perturbation failure, got: {e}'
    assert raised, 'constant-returning module should be refused'
    return True


# =====================================================================
# B24: D6 claimed with nine items -> refused at load
# =====================================================================

def test_b24_d6_nine_items_refused():
    """B24: D6 dimension with only 9 items -> ConfigError."""
    questions = [{'id': str(i)} for i in range(9)]
    config = {'dimensions_claimed': ['D6']}
    raised = False
    try:
        validate_minimum_n(config, questions)
    except ConfigError:
        raised = True
    assert raised, 'D6 with 9 items should raise ConfigError'
    return True


# =====================================================================
# B25: Computed-in-session, grounded prior -> OPERANDS-GROUNDED
# =====================================================================

def test_b25_computed_in_session_grounded():
    """B25: Operand matches a grounded prior return -> GROUNDED (step iv)."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    # Prior tool call returned 182.40 (grounded)
    prior = [{'value': Decimal('182.40'), 'grounded': True}]
    result = classify_prov('182.40 / 12', ctx, gt, MINI_CONFIG,
                           prior_returns=prior)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    return True


# =====================================================================
# B26: Computed-in-session, ungrounded prior -> ORIGINATED (laundering)
# =====================================================================

def test_b26_computed_in_session_ungrounded_originated():
    """B26: Operand matches UNGROUNDED prior return -> ORIGINATED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    # Prior return was 99999 (NOT grounded) -- fabricated value
    prior = [{'value': Decimal('99999'), 'grounded': False}]
    result = classify_prov('99999 / 12', ctx, gt, MINI_CONFIG,
                           prior_returns=prior)
    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    return True


# =====================================================================
# B27: Near-miss quantisation on prior return -> ORIGINATED + finding
# =====================================================================

def test_b27_near_miss_quantisation_originated():
    """B27: Operand matches quantised prior return but not exact -> ORIGINATED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[], source_fields=[])
    # Prior returned 182.4375 (grounded), quantised to 182.44
    prior = [{'value': Decimal('182.4375'), 'grounded': True}]
    res = resolve_operand(
        Decimal('182.44'), ctx, [], set(), [],
        {'places': '2', 'rounding': 'ROUND_HALF_UP'},
        prior_returns=prior)
    assert res['step'] == 5, f'expected step 5 (originated), got step {res["step"]}'
    assert res.get('near_miss_finding') is not None, \
        'expected near_miss_finding for quantised prior match'
    return True


# =====================================================================
# B28: abs_value without declared transform -> ORIGINATED
# =====================================================================

def test_b28_abs_value_undeclared_originated():
    """B28: abs(source) used without abs_value in permitted_transforms -> ORIGINATED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['credit_card'])
    gt = _mk_gt('2600.00', intermediates=[], source_fields=[])
    # credit_card balance is -2400; abs(-2400) = 2400
    # Without abs_value in permitted_transforms, 2400 should not resolve
    config_no_abs = {
        'permitted_transformations': [
            'percent_to_fraction', 'fraction_to_percent'],
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
    }
    result = classify_prov('2400 + 200', ctx, gt, config_no_abs)
    # 2400 is abs(-2400) but abs_value is NOT permitted -> ORIGINATED
    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    return True


# =====================================================================
# B29: Multi-invocation rollup all grounded -> OPERANDS-GROUNDED
# =====================================================================

def test_b29_multi_invocation_all_grounded():
    """B29: All invocations grounded -> item-level OPERANDS-GROUNDED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    inv1 = classify_prov('15200 * 1.2 / 100 / 12', ctx, gt, MINI_CONFIG)
    inv2 = classify_prov('15200 * 0.012 / 12', ctx, gt, MINI_CONFIG)
    item_result = classify_item([inv1, inv2], gt)
    assert item_result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {item_result["outcome"]}'
    return True


# =====================================================================
# B30: Sequential classification accumulates prior returns
# =====================================================================

def test_b30_sequential_classification_accumulates():
    """B30: Sequential calls -- call 2 uses call 1's grounded return."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = _mk_gt('15.20', intermediates=[{
        'label': 'monthly_interest',
        'value': Decimal('15.20'),
        'operation': 'multiply_divide',
        'inputs': [
            {'source': 'savings.balance'},
            {'source': 'savings.annual_rate'},
            {'constant': '100'}, {'constant': '12'},
        ],
    }], source_fields=['savings.balance', 'savings.annual_rate'])
    # Simulate two tool calls: first computes annual (182.40),
    # second divides by 12 using the prior return
    tool_calls = [
        {
            'id': 'tc1',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps({'expression': '15200 * 1.2 / 100'}),
            },
            'return_value': json.dumps({'result': 182.40}),
        },
        {
            'id': 'tc2',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps({'expression': '182.40 / 12'}),
            },
            'return_value': json.dumps({'result': 15.20}),
        },
    ]
    results = classify_invocations_sequential(tool_calls, ctx, gt, MINI_CONFIG)
    assert len(results) == 2, f'expected 2 results, got {len(results)}'
    assert results[1]['outcome'] == 'OPERANDS-GROUNDED', \
        f'call 2 expected OPERANDS-GROUNDED, got {results[1]["outcome"]}'
    return True


# =====================================================================
# Runner
# =====================================================================

ALL_TESTS = [
    test_b01_correct_answer_no_tool_call,
    test_b02_transposed_operand_originated,
    test_b03_correct_chained_intermediates_grounded,
    test_b04_percentage_as_fraction_grounded,
    test_b05_quantised_intermediate_grounded,
    test_b06_undelivered_field_originated,
    test_b07_two_invocations_one_originated,
    test_b08_transcription_altered,
    test_b09_refusal_decline_adjudication,
    test_b10_lookup_collision_adjudication,
    test_b11_expected_value_twice_ambiguous,
    test_b12_figures_present_none_matching,
    test_b13_r04_format_parsing,
    test_b14_locale_ambiguous_adjudication,
    test_b15_empty_response_unmeasurable,
    test_b16_rate_limit_error_unmeasurable,
    test_b17_prose_tool_claim_not_invoked,
    test_b18_no_tool_structure_ev0,
    test_b19_attestation_no_key_ev1,
    test_b20_attestation_hash_absent_ev1,
    test_b21_ev3_blocked_in_v1,
    test_b22_temperature_ignored_d2,
    test_b23_constant_ground_truth_refused,
    test_b24_d6_nine_items_refused,
    test_b25_computed_in_session_grounded,
    test_b26_computed_in_session_ungrounded_originated,
    test_b27_near_miss_quantisation_originated,
    test_b28_abs_value_undeclared_originated,
    test_b29_multi_invocation_all_grounded,
    test_b30_sequential_classification_accumulates,
]


def main():
    print('=' * 60)
    print('R4.1 PLANTED DEFECT SUITE')
    print('=' * 60)
    passed = 0
    failed = 0
    for test_fn in ALL_TESTS:
        name = test_fn.__name__
        try:
            result = test_fn()
            if result:
                passed += 1
                print('  PASS  ' + name)
            else:
                failed += 1
                print('  FAIL  ' + name)
        except Exception as e:
            failed += 1
            import traceback
            print('  FAIL  ' + name)
            print('         ' + str(e))
            traceback.print_exc()
    print()
    total = len(ALL_TESTS)
    print('Results: ' + str(passed) + ' passed, '
          + str(failed) + ' failed, ' + str(total) + ' total')
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
