import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'example'))

from decimal import Decimal
from ground_truth_example import compute
from operation_correctness import (
    evaluate_expression, classify_operation,
    OPERATION_CORRECT, WRONG_OPERATION, OPERATION_UNOBSERVABLE,
)


MINI_CONFIG = {
    'permitted_transformations': [
        'percent_to_fraction', 'fraction_to_percent'],
    'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
    'answer_tolerance': '0',
}


def test_t1_correct_expression_q01():
    ctx = {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}
    gt = compute('Q01', ctx)
    r = classify_operation('15200 * 1.2 / 100 / 12', gt, MINI_CONFIG)
    assert r['outcome'] == OPERATION_CORRECT
    assert r['matched_against'] == 'expected_value'
    return True

def test_t2_wrong_expression_q01():
    ctx = {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}
    gt = compute('Q01', ctx)
    r = classify_operation('15200 * 2.4 / 100 / 12', gt, MINI_CONFIG)
    assert r['outcome'] == WRONG_OPERATION
    return True

def test_t3_intermediate_match_q04():
    ctx = {'mortgage': {'balance': '287500.00', 'direction': 'liability',
                        'annual_rate': '4.20', 'min_payment': '1437.00'}}
    gt = compute('Q04', ctx)
    r = classify_operation('287500 * 4.2 / 100 / 12', gt, MINI_CONFIG)
    assert r['outcome'] == OPERATION_CORRECT
    return True

def test_t4_unparseable():
    ctx = {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}
    gt = compute('Q01', ctx)
    r = classify_operation('this is not math', gt, MINI_CONFIG)
    assert r['outcome'] == OPERATION_UNOBSERVABLE
    return True

def test_t5_empty():
    ctx = {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}
    gt = compute('Q01', ctx)
    r = classify_operation('', gt, MINI_CONFIG)
    assert r['outcome'] == OPERATION_UNOBSERVABLE
    return True

def test_t6_correct_expression_q02():
    ctx = {'credit_card': {'credit_limit': '5000.00', 'balance': '2400.00',
                           'direction': 'liability', 'annual_rate': '18.0',
                           'min_payment': '25.00'}}
    gt = compute('Q02', ctx)
    r = classify_operation('5000 - 2400', gt, MINI_CONFIG)
    assert r['outcome'] == OPERATION_CORRECT
    return True

def test_t7_quantised_intermediate_q07():
    ctx = {'investment': {'balance': '42175.00', 'annual_rate': '7.8',
                          'monthly_fee': '15.00'}}
    gt = compute('Q07', ctx)
    r = classify_operation('777.41', gt, MINI_CONFIG)
    assert r['outcome'] == OPERATION_CORRECT
    return True

def test_t8_decimal_precision():
    val = evaluate_expression('15200 * 1.2 / 100 / 12')
    expected = Decimal('15200') * Decimal('1.2') / Decimal('100') / Decimal('12')
    assert val == expected
    return True

def test_t9_q08_gpt41mini_wrong_operation():
    # Source: output/run1b_gpt41mini_transcript.jsonl
    # Expression: '-287500.00 + 1437.00'
    # Model computed balance + payment, omitting the interest step.
    # Evaluates to -286063.00; expected is 287069.25.
    ctx = {'mortgage': {'balance': '287500.00', 'direction': 'liability',
                        'annual_rate': '4.20', 'min_payment': '1437.00'}}
    gt = compute('Q08', ctx)
    expr = '-287500.00 + 1437.00'
    r = classify_operation(expr, gt, MINI_CONFIG)
    assert r['outcome'] == WRONG_OPERATION
    assert Decimal(r['evaluated_result']) == Decimal('-286063.00')
    return True

def test_t10_q07_gpt56sol_equivalent_route():
    # Source: output/smoke_run_gpt56sol.jsonl
    # Expression: '42175.00 * (0.078 / 4) - (15.00 * 3)'
    # Model used annual/4 instead of monthly*3. Both = 777.4125.
    # Must not penalise a valid alternative derivation.
    ctx = {'investment': {'balance': '42175.00', 'annual_rate': '7.8',
                          'monthly_fee': '15.00'}}
    gt = compute('Q07', ctx)
    expr = '42175.00 * (0.078 / 4) - (15.00 * 3)'
    r = classify_operation(expr, gt, MINI_CONFIG)
    assert r['outcome'] == OPERATION_CORRECT
    return True



def test_t11_wrong_op_split_route_divergence():
    """WRONG-OPERATION on an item with correct answer is route divergence."""
    # Construct a mock result: WRONG-OPERATION + AUTO-MATCH
    mock_results = [
        {
            'status': 'EXECUTED',
            'figure_outcome': 'AUTO-MATCH',
            'operation_correctness': [
                {'outcome': 'WRONG-OPERATION',
                 'detail': 'result 123 matches neither expected nor intermediate',
                 'evaluated_result': '123', 'matched_against': None},
            ],
        },
        {
            'status': 'EXECUTED',
            'figure_outcome': 'ADJUDICATE-AMBIGUOUS',
            'operation_correctness': [
                {'outcome': 'WRONG-OPERATION',
                 'detail': 'result 456 matches neither expected nor intermediate',
                 'evaluated_result': '456', 'matched_against': None},
            ],
        },
        {
            'status': 'EXECUTED',
            'figure_outcome': 'AUTO-MATCH',
            'operation_correctness': [
                {'outcome': 'OPERATION-CORRECT',
                 'detail': 'result matches expected',
                 'evaluated_result': '789', 'matched_against': 'expected_value'},
            ],
        },
    ]
    # Compute the split
    wo_split = {'route_divergence': 0, 'item_wrong': 0, 'undetermined': 0}
    for r in mock_results:
        fig = r.get('figure_outcome', '')
        for oc in r.get('operation_correctness', []):
            if oc.get('outcome') == 'WRONG-OPERATION':
                if fig == 'AUTO-MATCH':
                    wo_split['route_divergence'] += 1
                elif fig.startswith('ADJUDICATE'):
                    wo_split['undetermined'] += 1
                else:
                    wo_split['item_wrong'] += 1
    assert wo_split['route_divergence'] == 1, f'expected 1 route_divergence, got {wo_split}'
    assert wo_split['undetermined'] == 1, f'expected 1 undetermined, got {wo_split}'
    assert wo_split['item_wrong'] == 0, f'expected 0 item_wrong, got {wo_split}'
    return True

ALL_TESTS = [
    test_t1_correct_expression_q01,
    test_t2_wrong_expression_q01,
    test_t3_intermediate_match_q04,
    test_t4_unparseable,
    test_t5_empty,
    test_t6_correct_expression_q02,
    test_t7_quantised_intermediate_q07,
    test_t8_decimal_precision,
    test_t9_q08_gpt41mini_wrong_operation,
    test_t10_q07_gpt56sol_equivalent_route,
    test_t11_wrong_op_split_route_divergence,
]


def main():
    print('============================================================')
    print('D7.2(b) OPERATION CORRECTNESS TESTS')
    print('============================================================')
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
    print('Results: ' + str(passed) + ' passed, ' + str(failed) + ' failed, ' + str(total) + ' total')
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
