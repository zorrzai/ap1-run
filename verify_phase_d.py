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
  11. abs_value transformation -> OPERANDS-GROUNDED for negative balances
  12. Multi-invocation rollup: all grounded -> OPERANDS-GROUNDED
  13. Operand extraction: negative literals
  14. Operand extraction: empty/invalid expressions
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'example'))

from decimal import Decimal
from provenance import (
    extract_operands, resolve_operand, classify_invocation,
    classify_item, build_audit_listing, TRANSFORMATIONS,
)
from context import build_delivered_context, TrackingContext
from seal import perturbation_check, source_fields_check, SealError


# -- Test fixtures -----------------------------------------------------

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
        'percent_to_fraction', 'fraction_to_percent', 'abs_value'],
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
    """Legitimate chained intermediates score OPERANDS-GROUNDED."""
    ctx = build_delivered_context(MINI_FIXTURE, ['mortgage'])
    # Q04: 1437 - 287500*(4.20/100)/12
    # monthly_interest = abs(287500) * 4.20 / 100 / 12 = 1006.25
    ground_truth = {
        'intermediates': [
            {
                'label': 'monthly_interest',
                'value': Decimal('1006.25'),
                'inputs': [
                    {'source': 'mortgage.balance'},
                    {'source': 'mortgage.annual_rate'},
                    {'constant': '100'},
                    {'constant': '12'},
                ],
            },
            {
                'label': 'principal',
                'value': Decimal('430.75'),
                'inputs': [
                    {'source': 'mortgage.min_payment'},
                    {'intermediate': 'monthly_interest'},
                ],
            },
        ],
    }
    result = classify_invocation(
        '1437 - 287500*(4.20/100)/12', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    return True


def test_d3_percentage_as_fraction_grounded():
    """A percentage intermediate expressed as a decimal fraction is grounded."""
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
    # Expression uses 0.18 (percent_to_fraction of 18.0)
    result = classify_invocation(
        '2400 * 0.18 / 12', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    # Check that 0.18 resolved via percent_to_fraction
    res_018 = [r for r in result['operand_resolutions']
               if r['operand_value'] == '0.18']
    assert len(res_018) == 1
    assert res_018[0]['transform_used'] == 'percent_to_fraction'
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


def test_d10_abs_value_transform_grounded():
    """abs_value transformation resolves negative balances correctly."""
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
    # Expression uses 2400 (abs of -2400)
    result = classify_invocation(
        '2400 * 18 / 100 / 12', ctx, ground_truth, MINI_CONFIG)
    assert result['outcome'] == 'OPERANDS-GROUNDED', \
        f'expected OPERANDS-GROUNDED, got {result["outcome"]}'
    # Check that 2400 resolved via abs_value
    res_2400 = [r for r in result['operand_resolutions']
                if r['operand_value'] == '2400']
    assert len(res_2400) == 1
    assert res_2400[0]['transform_used'] == 'abs_value', \
        f'expected abs_value, got {res_2400[0]["transform_used"]}'
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


# -- Runner ----------------------------------------------------------------

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
    test_d10_abs_value_transform_grounded,
    test_d11_all_grounded_rollup,
    test_d12_negative_literal_extraction,
    test_d13_empty_invalid_expression,
    test_d14_audit_listing_format,
    test_d15_tracking_context_records_access,
    test_d16_perturbation_passes_real_module,
    test_d17_source_fields_passes_real_module,
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
