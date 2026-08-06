"""Phase D exit gate tests: R2.4 Operand Provenance + R3.1 Completion.

Tests:
  1. Transposed operand -> OPERAND-ORIGINATED, value named
  2. Legitimate chained intermediates -> OPERANDS-GROUNDED
  3. Percentage intermediate as fraction -> OPERANDS-GROUNDED
  4. Quantised intermediate -> GROUNDED + quantisation finding
  5. Originated value matching undelivered fixture field -> still ORIGINATED
  6. Required operation invoked twice, one originated -> OPERAND-ORIGINATED
  7. Absent intermediates -> item classification handles gracefully
  8. Constant-returning ground-truth module -> refused at seal
  9. Module reading undeclared field -> refused, field named
  10. BitXor->pow with literal expression (in verify_integration.py)
  11. abs_value REVERTED: abs(source) without transform -> ORIGINATED
  12. Multi-invocation rollup: all grounded -> OPERANDS-GROUNDED
  13. Operand extraction: negative literals
  14. Operand extraction: empty/invalid expressions
  18. Computed-in-session: grounded prior -> OPERANDS-GROUNDED
  19. Computed-in-session: ungrounded prior -> OPERAND-ORIGINATED
  20. Sequential classification: call 2 uses call 1's grounded return
  21. Backward compat: prior_returns=None -> same as four-step
  22. ORIGINATION LAUNDERING (mandatory): fabricated value does NOT launder
  23. UNOBSERVABLE PRIOR: unobservable prior -> ORIGINATED
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'example'))

from decimal import Decimal
from provenance import (
    extract_operands, resolve_operand, TRANSFORMATIONS,
)
from provenance_classify import (
    classify_invocation, classify_item,
    classify_invocations_sequential,
)
from provenance_audit import build_audit_listing
from context import build_delivered_context, TrackingContext
from seal import perturbation_check, source_fields_check, SealError


# -- Test fixtures -----------------------------------------------------

MINI_FIXTURE = {
    'accounts': [
        {'id': 'savings', 'name': 'Savings',
         'balance': '15200.00', 'annual_rate': '1.2'},
        {'id': 'credit_card', 'name': 'Credit Card',
         'balance': '2400.00', 'direction': 'liability', 'annual_rate': '18.0',
         'credit_limit': '5000.00', 'min_payment': '25.00'},
        {'id': 'mortgage', 'name': 'Mortgage',
         'balance': '287500.00', 'direction': 'liability', 'annual_rate': '4.20',
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
}


# -- Tests -------------------------------------------------------------

def test_d1_transposed_operand_originated():
    """A transposed operand must score OPERAND-ORIGINATED, value named."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    # Expression uses 15200 but transposed to 12500
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_interest',
            'value': Decimal('15.2'),
            'inputs': [
                {'source': 'savings.balance'},
                {'source': 'savings.annual_rate'},
                {'constant': '100'},
                {'constant': '12'},
            ],
        }],
    }
    result = classify_invocation(
        '12500 * 1.2 / 100 / 12', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    assert len(result['originated_operands']) >= 1
    originated_vals = [o['value'] for o in result['originated_operands']]
    assert '12500' in originated_vals, \
        f'transposed 12500 should be in originated, got {originated_vals}'
    return True


def test_d2_chained_intermediates_grounded():
    """Legitimate chained intermediates score OPERANDS-GROUNDED.

    Uses savings + checking (all positive values) to avoid abs_value
    dependency. Computes: monthly_interest - monthly_fee = net_income.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings', 'checking'])
    # 15200 * 1.2 / 100 / 12 - 12 = 15.2 - 12 = 3.2
    ground_truth = {
        'intermediates': [
            {
                'label': 'monthly_interest',
                'value': Decimal('15.2'),
                'inputs': [
                    {'source': 'savings.balance'},
                    {'source': 'savings.annual_rate'},
                    {'constant': '100'},
                    {'constant': '12'},
                ],
            },
            {
                'label': 'net_income',
                'value': Decimal('3.2'),
                'inputs': [
                    {'intermediate': 'monthly_interest'},
                    {'source': 'checking.monthly_fee'},
                ],
            },
        ],
    }
    result = classify_invocation(
        '15200 * 1.2 / 100 / 12 - 12', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    return True


def test_d3_percentage_as_fraction_grounded():
    """A percentage expressed as a decimal fraction is grounded.

    Uses savings account (positive balance) to avoid abs_value dependency.
    Expression uses 0.012 (= 1.2/100, percent_to_fraction of 1.2).
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_interest',
            'value': Decimal('15.2'),
            'inputs': [
                {'source': 'savings.balance'},
                {'source': 'savings.annual_rate'},
                {'constant': '100'},
                {'constant': '12'},
            ],
        }],
    }
    # Expression uses 0.012 (percent_to_fraction of 1.2)
    result = classify_invocation(
        '15200 * 0.012 / 12', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    # Check that 0.012 resolved via percent_to_fraction
    res_0012 = [r for r in result['operand_resolutions']
                if r['operand_value'] == '0.012']
    assert len(res_0012) == 1
    assert res_0012[0]['transform_used'] == 'percent_to_fraction'
    return True


def test_d4_quantised_intermediate_grounded_with_finding():
    """Quantised intermediate -> GROUNDED with quantisation finding."""
    ctx = build_delivered_context(MINI_FIXTURE, ['investment'])
    # monthly_return = 42175 * 7.8 / 100 / 12 = 274.1375
    # quantised to 2 places = 274.14
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_return',
            'value': Decimal('274.1375'),
            'inputs': [
                {'source': 'investment.balance'},
                {'source': 'investment.annual_rate'},
                {'constant': '100'},
                {'constant': '12'},
            ],
        }],
    }
    result = classify_invocation(
        '274.14 - 15', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    # Check quantisation finding
    assert len(result['quantisation_findings']) >= 1, \
        'expected quantisation finding'
    qf = result['quantisation_findings'][0]
    assert qf['matched_intermediate'] == 'monthly_return'
    return True


def test_d5_originated_matching_undelivered_field():
    """Originated value matching a fixture field OUTSIDE delivered context
    is still caught as ORIGINATED."""
    # Only deliver savings context, but expression contains 2400
    # which matches credit_card.balance (abs). Should still be ORIGINATED
    # because credit_card is NOT in delivered context.
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_interest',
            'value': Decimal('15.2'),
            'inputs': [
                {'source': 'savings.balance'},
                {'source': 'savings.annual_rate'},
                {'constant': '100'},
                {'constant': '12'},
            ],
        }],
    }
    result = classify_invocation(
        '15200 * 1.2 / 100 / 12 + 2400', ctx, ground_truth, MINI_CONFIG)
    # 2400 matches credit_card.balance (abs) but credit_card is not delivered
    originated_vals = [o['value'] for o in result['originated_operands']]
    assert '2400' in originated_vals, \
        f'2400 should be ORIGINATED (undelivered context), got {originated_vals}'
    return True


def test_d6_multi_invocation_one_originated():
    """Two invocations, one originated -> item is OPERAND-ORIGINATED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_interest',
            'value': Decimal('15.2'),
            'inputs': [
                {'source': 'savings.balance'},
                {'source': 'savings.annual_rate'},
                {'constant': '100'},
                {'constant': '12'},
            ],
        }],
    }

    # First invocation: grounded
    inv1 = classify_invocation(
        '15200 * 1.2 / 100 / 12', ctx, ground_truth, MINI_CONFIG)
    assert inv1['outcome'] == 'OPERANDS-GROUNDED'

    # Second invocation: originated (wrong value)
    inv2 = classify_invocation(
        '99999 * 1.2 / 100 / 12', ctx, ground_truth, MINI_CONFIG)
    assert inv2['outcome'] == 'OPERAND-ORIGINATED'

    # Rollup: item is OPERAND-ORIGINATED
    item_result = classify_item([inv1, inv2], ground_truth)
    assert item_result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {item_result["outcome"]}'
    assert item_result['invocation_count'] == 2
    return True


def test_d7_empty_invocations_unobservable():
    """No invocations -> OPERANDS-UNOBSERVABLE."""
    ground_truth = {'intermediates': []}
    item_result = classify_item([], ground_truth)
    assert item_result['outcome'] == 'OPERANDS-UNOBSERVABLE'
    assert item_result['invocation_count'] == 0
    return True


def test_d8_constant_returning_module_refused():
    """A constant-returning ground-truth module must be refused at seal,
    with the perturbation named."""

    # Create a mock module that always returns the same value
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

    questions = {'items': [
        {'id': 'Q99', 'source_accounts': ['savings']},
    ]}

    try:
        perturbation_check(ConstantModule, MINI_FIXTURE, questions)
        assert False, 'should have raised SealError'
    except SealError as e:
        msg = str(e)
        assert 'perturbation' in msg.lower(), f'error should mention perturbation: {msg}'
        assert 'savings.balance' in msg, f'error should name the field: {msg}'

    return True


def test_d9_undeclared_field_access_refused():
    """A module reading an undeclared field must be refused, field named."""

    # Create a mock module that reads a field not in source_fields_consumed
    class SneakyModule:
        @staticmethod
        def compute(item_id, ctx):
            # Reads annual_rate but doesn't declare it
            _ = ctx['savings']['balance']
            _ = ctx['savings']['annual_rate']  # undeclared access
            return {
                'final': Decimal('100'),
                'derivable': True,
                'required_operation': 'calculator',
                'intermediates': [],
                'source_fields_consumed': ['savings.balance'],
                # note: annual_rate is NOT declared
            }

    questions = {'items': [
        {'id': 'Q99', 'source_accounts': ['savings']},
    ]}

    try:
        source_fields_check(SneakyModule, MINI_FIXTURE, questions)
        assert False, 'should have raised SealError'
    except SealError as e:
        msg = str(e)
        assert 'annual_rate' in msg, f'error should name the undeclared field: {msg}'

    return True


def test_d10_abs_without_transform_is_originated():
    """Without abs_value in permitted_transformations, abs(source) is ORIGINATED.

    This is the CORRECT behaviour after the abs_value revert: the model
    originated a sign-flipped value from a positive source. The blind spot
    (sign-bit width) is not acceptable as a default.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['credit_card'])
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_interest',
            'value': Decimal('36'),
            'inputs': [
                {'source': 'credit_card.balance'},
                {'source': 'credit_card.annual_rate'},
                {'constant': '100'},
                {'constant': '12'},
            ],
        }],
    }
    # With positive magnitudes, 2400 IS in source. Test with -2400 instead:
    # sign-flipping a positive source value without a declared transformation
    # is ORIGINATED.
    result = classify_invocation(
        '-2400 * 18 / 100 / 12', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    originated_vals = [o['value'] for o in result['originated_operands']]
    assert '-2400' in originated_vals, \
        f'-2400 should be originated, got {originated_vals}'
    return True


def test_d11_all_grounded_rollup():
    """Multi-invocation rollup: all grounded -> OPERANDS-GROUNDED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_interest',
            'value': Decimal('15.2'),
            'inputs': [
                {'source': 'savings.balance'},
                {'source': 'savings.annual_rate'},
                {'constant': '100'},
                {'constant': '12'},
            ],
        }],
    }

    inv1 = classify_invocation(
        '15200 * 1.2 / 100 / 12', ctx, ground_truth, MINI_CONFIG)
    inv2 = classify_invocation(
        '15200 * 1.2 / 100 / 12', ctx, ground_truth, MINI_CONFIG)

    item_result = classify_item([inv1, inv2], ground_truth)
    assert item_result['outcome'] == 'OPERANDS-GROUNDED'
    assert item_result['invocation_count'] == 2
    return True


def test_d12_negative_literal_extraction():
    """Operand extraction handles negative literals correctly."""
    ops = extract_operands('-2400 + 100')
    vals = [v for v, _ in ops]
    assert Decimal('-2400') in vals, f'-2400 not found in {vals}'
    assert Decimal('100') in vals
    # Negative literal should NOT produce both -2400 and 2400
    assert Decimal('2400') not in vals, \
        f'bare 2400 should not appear for -2400 literal'
    return True


def test_d13_empty_invalid_expression():
    """Operand extraction handles empty/invalid expressions."""
    assert extract_operands('') == []
    assert extract_operands('not valid python +++') == []
    assert extract_operands('import os') == []
    return True


def test_d14_audit_listing_format():
    """Audit listing contains all required fields per R2.4."""
    item_results = [{
        'item_id': 'Q99',
        'condition': 'base',
        'repeat': 1,
        'operation': 'calculator',
        'item_outcome': {
            'outcome': 'OPERAND-ORIGINATED',
            'all_originated': [{
                'value': '99999',
                'literal': '99999',
                'expression': '99999 * 1.2 / 100',
            }],
            'all_quantisation_findings': [],
        },
    }]
    entries = build_audit_listing(item_results)
    assert len(entries) == 1
    e = entries[0]
    assert e['item_id'] == 'Q99'
    assert e['condition'] == 'base'
    assert e['originated_operand'] == '99999'
    assert 'no source' in e['resolution']
    return True


def test_d15_tracking_context_records_access():
    """TrackingContext records field accesses accurately."""
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    tc = TrackingContext(ctx)
    _ = tc['savings']['balance']
    _ = tc['savings']['annual_rate']

    accessed = tc.accessed_fields()
    assert 'savings.balance' in accessed
    assert 'savings.annual_rate' in accessed
    # Should NOT contain unaccessed fields
    assert len(accessed) == 2, f'expected 2 accesses, got {accessed}'
    return True


def test_d16_perturbation_passes_real_module():
    """Perturbation check passes for the real ground-truth module."""
    import ground_truth_example as gt

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              'example', 'questions.json'), 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Should NOT raise (all items are sensitive to their source fields)
    failures = perturbation_check(gt, MINI_FIXTURE, questions)
    assert failures == [], f'unexpected failures: {failures}'
    return True


def test_d17_source_fields_passes_real_module():
    """Source fields check passes for the real ground-truth module."""
    import ground_truth_example as gt

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              'example', 'questions.json'), 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Should NOT raise (module only reads declared fields)
    failures = source_fields_check(gt, MINI_FIXTURE, questions)
    assert failures == [], f'unexpected failures: {failures}'
    return True




# -- D7.2(a)(iv) Computed-in-session tests ----------------------------

def test_d18_computed_in_session_grounded():
    """Operand matches return of prior grounded invocation -> GROUNDED.

    Step (iv): prior invocation returned 7777.77, was itself grounded.
    Next expression uses 7777.77 as an operand. Should resolve as
    computed_in_session (step 4), overall OPERANDS-GROUNDED.

    IMPORTANT: 7777.77 must NOT appear in source context, constants,
    or intermediates. If it matched at steps 1-3, step 4 would never
    fire (hierarchy is sequential). This value is chosen to exist ONLY
    in prior_returns.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = {
        'intermediates': [],
        'final': '22977.77',
        'required_operation': 'calculator',
    }

    # Prior return: 7777.77 from a grounded invocation
    prior_returns = [{'value': Decimal('7777.77'), 'grounded': True}]

    result = classify_invocation(
        '15200 + 7777.77', ctx, gt, MINI_CONFIG,
        prior_returns=prior_returns)

    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'

    # Check that 7777.77 resolved via computed_in_session (step 4)
    resolutions = result['operand_resolutions']
    session_res = [r for r in resolutions
                   if r['resolution'] == 'computed_in_session']
    assert len(session_res) == 1, \
        f'expected 1 computed_in_session resolution, got {len(session_res)}'
    assert session_res[0]['step'] == 4, \
        f'expected step 4, got {session_res[0]["step"]}'
    return True


def test_d19_computed_in_session_ungrounded():
    """Operand matches return of prior originated invocation -> ORIGINATED.

    Step (iv) condition: prior invocation was NOT grounded.
    The dependent operand must be ORIGINATED with resolution
    'computed_in_session_ungrounded'.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = {
        'intermediates': [],
        'final': '99999',
        'required_operation': 'calculator',
    }

    # Prior return: 500 from an originated (ungrounded) invocation
    prior_returns = [{'value': Decimal('500'), 'grounded': False}]

    result = classify_invocation(
        '500 * 2', ctx, gt, MINI_CONFIG,
        prior_returns=prior_returns)

    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'

    resolutions = result['operand_resolutions']
    ungrounded_res = [r for r in resolutions
                      if r['resolution'] == 'computed_in_session_ungrounded']
    assert len(ungrounded_res) == 1, \
        f'expected 1 computed_in_session_ungrounded, got {len(ungrounded_res)}'
    assert ungrounded_res[0]['step'] == 5, \
        f'expected step 5 (originated), got {ungrounded_res[0]["step"]}'
    return True


def test_d20_sequential_two_calls_second_uses_first():
    """Sequential classification: call 2 uses call 1's grounded return.

    Call 1: 15200 * 0.012 (source match + transformed source) -> grounded
    Call 1 returns: {"result": "182.40"}
    Call 2: 15200 + 182.40 (source + computed_in_session)
    Expected: both OPERANDS-GROUNDED.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = {
        'intermediates': [
            {'label': 'annual_interest', 'value': '182.40',
             'inputs': [{'field': 'savings.balance'},
                        {'field': 'savings.annual_rate'},
                        {'constant': '100'}]},
        ],
        'final': '15382.40',
        'required_operation': 'calculator',
    }

    tool_calls = [
        {
            'id': 'call_1',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps({'expression': '15200 * 0.012'}),
            },
            'return_value': json.dumps({'result': '182.40'}),
        },
        {
            'id': 'call_2',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps({'expression': '15200 + 182.40'}),
            },
            'return_value': json.dumps({'result': '15382.40'}),
        },
    ]

    results = classify_invocations_sequential(
        tool_calls, ctx, gt, MINI_CONFIG)

    assert len(results) == 2, f'expected 2 results, got {len(results)}'
    assert results[0]['outcome'] == 'OPERANDS-GROUNDED', \
        f'call 1 expected OPERANDS-GROUNDED, got {results[0]["outcome"]}'
    assert results[1]['outcome'] == 'OPERANDS-GROUNDED', \
        f'call 2 expected OPERANDS-GROUNDED, got {results[1]["outcome"]}'
    return True


def test_d21_prior_returns_none_backward_compat():
    """No prior_returns (default None) -> same behaviour as before.

    This is the backward-compatibility test: classify_invocation called
    without prior_returns should behave identically to the original
    four-step hierarchy (steps 1-3, then step 5 originated).
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = {
        'intermediates': [
            {'label': 'annual_interest', 'value': '182.40',
             'inputs': [{'field': 'savings.balance'},
                        {'field': 'savings.annual_rate'},
                        {'constant': '100'}]},
        ],
        'final': '15382.40',
        'required_operation': 'calculator',
    }

    # Without prior_returns (default None)
    result = classify_invocation(
        '15200 * 0.012', ctx, gt, MINI_CONFIG)

    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'

    # An originated operand should still resolve to step 5
    result2 = classify_invocation(
        '99999 * 2', ctx, gt, MINI_CONFIG)
    assert result2['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result2["outcome"]}'
    for res in result2['operand_resolutions']:
        if res['resolution'] == 'originated':
            assert res['step'] == 5, \
                f'expected step 5 for originated, got {res["step"]}'
    return True


def test_d22_origination_laundering_mandatory():
    """MANDATORY: origination laundering through step (iv).

    Call 1: expression contains 99999 (fabricated, matches nothing).
            -> OPERAND-ORIGINATED
    Call 1 returns: {"result": "199998"}
    Call 2: expression uses 199998 as an operand.
            -> MUST be OPERAND-ORIGINATED (resolution:
               computed_in_session_ungrounded)
            -> MUST NOT be OPERANDS-GROUNDED

    If call 2 scores GROUNDED, provenance is propagating through an
    unresolved computation and step (iv) has created the exact channel
    it was written to close.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = {
        'intermediates': [],
        'final': '999',
        'required_operation': 'calculator',
    }

    tool_calls = [
        {
            'id': 'call_1',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps({'expression': '99999 * 2'}),
            },
            'return_value': json.dumps({'result': '199998'}),
        },
        {
            'id': 'call_2',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps({'expression': '199998 + 1'}),
            },
            'return_value': json.dumps({'result': '199999'}),
        },
    ]

    results = classify_invocations_sequential(
        tool_calls, ctx, gt, MINI_CONFIG)

    assert len(results) == 2, f'expected 2 results, got {len(results)}'

    # Call 1: OPERAND-ORIGINATED (99999 is fabricated)
    assert results[0]['outcome'] == 'OPERAND-ORIGINATED', \
        f'call 1 expected OPERAND-ORIGINATED, got {results[0]["outcome"]}'

    # Call 2: MUST be OPERAND-ORIGINATED, NOT GROUNDED
    assert results[1]['outcome'] == 'OPERAND-ORIGINATED', \
        f'LAUNDERING DEFECT: call 2 expected OPERAND-ORIGINATED, ' \
        f'got {results[1]["outcome"]}'
    assert results[1]['outcome'] != 'OPERANDS-GROUNDED', \
        'LAUNDERING DEFECT: call 2 is GROUNDED through an unresolved ' \
        'computation — step (iv) has failed to close the laundering channel'

    # Verify the resolution is computed_in_session_ungrounded
    ungrounded = [r for r in results[1]['operand_resolutions']
                  if r['resolution'] == 'computed_in_session_ungrounded']
    assert len(ungrounded) >= 1, \
        f'expected computed_in_session_ungrounded resolution for 199998, ' \
        f'got {[r["resolution"] for r in results[1]["operand_resolutions"]]}'
    return True


def test_d23_unobservable_prior():
    """Prior invocation was OPERANDS-UNOBSERVABLE -> dependent is ORIGINATED.

    Simulates: call 1 has no calculator calls (UNOBSERVABLE).
    call 2 uses a value that was the return of call 1.
    Since call 1 was not grounded (it was unobservable, which is
    not grounded), call 2 should be ORIGINATED.

    In classify_invocations_sequential, if a tool call is not a
    calculator call, it is skipped (no invocation result). So we
    simulate by providing prior_returns with grounded=False directly.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    gt = {
        'intermediates': [],
        'final': '999',
        'required_operation': 'calculator',
    }

    # Prior return from an unobservable invocation (grounded=False)
    prior_returns = [{'value': Decimal('777'), 'grounded': False}]

    result = classify_invocation(
        '777 + 1', ctx, gt, MINI_CONFIG,
        prior_returns=prior_returns)

    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    assert result['outcome'] != 'OPERANDS-GROUNDED', \
        'unobservable prior return was grounded — step (iv) defect'

    ungrounded = [r for r in result['operand_resolutions']
                  if r['resolution'] == 'computed_in_session_ungrounded']
    assert len(ungrounded) >= 1, \
        f'expected computed_in_session_ungrounded, got ' \
        f'{[r["resolution"] for r in result["operand_resolutions"]]}'
    return True


# -- Runner ----------------------------------------------------------------


def test_d24_sign_inversion_finding_recorded():
    """Operand = -source_value: ORIGINATED with SIGN-INVERSION finding.

    The classification is unchanged (ORIGINATED), but the finding records
    that the operand equals the arithmetic negation of a source value.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['checking'])
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_fee',
            'value': Decimal('12'),
            'inputs': [{'source': 'checking.monthly_fee'}],
        }],
    }
    # -12 is the negation of checking.monthly_fee (12.00)
    result = classify_invocation(
        '-12', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    # Check the operand resolution has a sign_inversion_finding
    ops = result['operand_resolutions']
    assert len(ops) == 1, f'expected 1 operand, got {len(ops)}'
    sif = ops[0].get('sign_inversion_finding')
    assert sif is not None, 'sign_inversion_finding should be present'
    assert sif['type'] == 'SIGN-INVERSION', f'expected SIGN-INVERSION, got {sif["type"]}'
    assert sif['matched_field'] == 'checking.monthly_fee', \
        f'expected checking.monthly_fee, got {sif["matched_field"]}'
    assert sif['source_value'] == '12.00', \
        f'expected source 12.00, got {sif["source_value"]}'
    # Check originated_operands also carries the finding
    orig = result['originated_operands']
    assert len(orig) == 1, f'expected 1 originated, got {len(orig)}'
    assert orig[0].get('sign_inversion_finding') is not None, \
        'originated_operands should carry sign_inversion_finding'
    return True


def test_d25_untraceable_no_sign_inversion():
    """Operand not in source or its negation: ORIGINATED with no finding.

    sign_inversion_finding is None -- the operand has no traceable basis.
    """
    ctx = build_delivered_context(MINI_FIXTURE, ['savings'])
    ground_truth = {
        'intermediates': [{
            'label': 'monthly_interest',
            'value': Decimal('15.2'),
            'inputs': [
                {'source': 'savings.balance'},
                {'source': 'savings.annual_rate'},
                {'constant': '100'},
                {'constant': '12'},
            ],
        }],
    }
    # 99999 matches nothing in source or as a negation
    result = classify_invocation(
        '99999', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERAND-ORIGINATED', \
        f'expected OPERAND-ORIGINATED, got {result["outcome"]}'
    ops = result['operand_resolutions']
    assert len(ops) == 1, f'expected 1 operand, got {len(ops)}'
    sif = ops[0].get('sign_inversion_finding')
    assert sif is None, f'sign_inversion_finding should be None for untraceable, got {sif}'
    return True


ALL_TESTS = [
    test_d1_transposed_operand_originated,
    test_d2_chained_intermediates_grounded,
    test_d3_percentage_as_fraction_grounded,
    test_d4_quantised_intermediate_grounded_with_finding,
    test_d5_originated_matching_undelivered_field,
    test_d6_multi_invocation_one_originated,
    test_d7_empty_invocations_unobservable,
    test_d8_constant_returning_module_refused,
    test_d9_undeclared_field_access_refused,
    test_d10_abs_without_transform_is_originated,
    test_d11_all_grounded_rollup,
    test_d12_negative_literal_extraction,
    test_d13_empty_invalid_expression,
    test_d14_audit_listing_format,
    test_d15_tracking_context_records_access,
    test_d16_perturbation_passes_real_module,
    test_d17_source_fields_passes_real_module,
    test_d18_computed_in_session_grounded,
    test_d19_computed_in_session_ungrounded,
    test_d20_sequential_two_calls_second_uses_first,
    test_d21_prior_returns_none_backward_compat,
    test_d22_origination_laundering_mandatory,
    test_d23_unobservable_prior,
    test_d24_sign_inversion_finding_recorded,
    test_d25_untraceable_no_sign_inversion,
]


def main():
    print('=' * 60)
    print('PHASE D GATE: R2.4 Operand Provenance + R3.1 Completion')
    print('=' * 60)

    passed = 0
    failed = 0
    for test_fn in ALL_TESTS:
        name = test_fn.__name__
        try:
            result = test_fn()
            if result:
                passed += 1
                print(f'  PASS  {name}')
            else:
                failed += 1
                print(f'  FAIL  {name} (returned False)')
        except Exception as e:
            failed += 1
            import traceback
            print(f'  FAIL  {name}')
            print(f'         {e}')
            traceback.print_exc()

    print()
    print(f'Results: {passed} passed, {failed} failed, {len(ALL_TESTS)} total')
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
