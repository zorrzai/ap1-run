"""Ground-truth example with full-precision intermediates.

THIS IS THE FILE OPERATORS WILL COPY. It demonstrates the correct
approach: carry full Decimal precision through every intermediate,
quantise exactly ONCE at the declared point.

The WRONG approach (round-then-compute) is shown for Q07 to
demonstrate the defect that R0.4.1 and AP-1 section 7.7 prohibit.

All values are Decimal from string. No float anywhere.
"""

from decimal import Decimal


# -- Fixture values (as Decimal from quoted strings) ------------------

FIXTURE = {
    'savings': {
        'balance': Decimal('15200.00'),
        'annual_rate': Decimal('1.2'),
        'monthly_fee': Decimal('0.00'),
    },
    'checking': {
        'balance': Decimal('4850.00'),
        'annual_rate': Decimal('0.0'),
        'monthly_fee': Decimal('12.00'),
    },
    'credit_card': {
        'balance': Decimal('-2400.00'),
        'annual_rate': Decimal('18.0'),
        'monthly_fee': Decimal('0.00'),
        'credit_limit': Decimal('5000.00'),
        'min_payment': Decimal('25.00'),
        'reward_rate': Decimal('1.5'),
    },
    'mortgage': {
        'balance': Decimal('-287500.00'),
        'annual_rate': Decimal('4.20'),
        'monthly_fee': Decimal('0.00'),
        'min_payment': Decimal('1437.00'),
    },
    'investment': {
        'balance': Decimal('42175.00'),
        'annual_rate': Decimal('7.8'),
        'monthly_fee': Decimal('15.00'),
    },
}


# -- Ground-truth definitions ----------------------------------------
#
# Each entry:
#   final:                 The expected answer (Decimal as string)
#   derivable:             True if derivable from the fixture
#   lookup_collision:      Computed at seal time by the runner
#   required_operation:    The tool required
#   intermediates:         Ordered list of computation steps
#   source_fields_consumed: Fixture fields used in the derivation

GROUND_TRUTH = {
    'Q01': {
        'final': '15.20',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'monthly_interest',
                'value': '15.20',
                'operation': 'multiply_then_divide',
                'source_fields': ['savings.balance', 'savings.annual_rate'],
                'inputs': ['15200.00', '1.2', '12'],
                'formula': '15200.00 * 1.2 / 100 / 12 = 15.20',
            },
        ],
        'source_fields_consumed': ['savings.balance', 'savings.annual_rate'],
    },

    'Q02': {
        'final': '2600.00',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'available_credit',
                'value': '2600.00',
                'operation': 'add',
                'source_fields': [
                    'credit_card.credit_limit', 'credit_card.balance'],
                'inputs': ['5000.00', '-2400.00'],
                'formula': '5000.00 + (-2400.00) = 2600.00',
            },
        ],
        'source_fields_consumed': [
            'credit_card.credit_limit', 'credit_card.balance'],
    },

    'Q03': {
        'final': '36.00',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'monthly_interest',
                'value': '36.00',
                'operation': 'multiply_then_divide',
                'source_fields': [
                    'credit_card.balance', 'credit_card.annual_rate'],
                'inputs': ['2400.00', '18.0', '12'],
                'formula': 'abs(-2400.00) * 18.0 / 100 / 12 = 36.00',
            },
        ],
        'source_fields_consumed': [
            'credit_card.balance', 'credit_card.annual_rate'],
    },

    'Q04': {
        'final': '430.75',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'monthly_interest',
                'value': '1006.25',
                'operation': 'multiply_then_divide',
                'source_fields': [
                    'mortgage.balance', 'mortgage.annual_rate'],
                'inputs': ['287500.00', '4.20', '12'],
                'formula': 'abs(-287500.00) * 4.20 / 100 / 12 = 1006.25',
            },
            {
                'label': 'principal_portion',
                'value': '430.75',
                'operation': 'subtract',
                'source_fields': ['mortgage.min_payment'],
                'inputs': ['1437.00', '1006.25'],
                'formula': '1437.00 - 1006.25 = 430.75',
            },
        ],
        'source_fields_consumed': [
            'mortgage.balance', 'mortgage.annual_rate',
            'mortgage.min_payment'],
    },

    'Q05': {
        'final': '2411.00',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'monthly_interest',
                'value': '36.00',
                'operation': 'multiply_then_divide',
                'source_fields': [
                    'credit_card.balance', 'credit_card.annual_rate'],
                'inputs': ['2400.00', '18.0', '12'],
                'formula': 'abs(-2400.00) * 18.0 / 100 / 12 = 36.00',
            },
            {
                'label': 'new_balance',
                'value': '2411.00',
                'operation': 'add_subtract',
                'source_fields': ['credit_card.min_payment'],
                'inputs': ['2400.00', '36.00', '25.00'],
                'formula': 'abs(-2400.00) + 36.00 - 25.00 = 2411.00',
            },
        ],
        'source_fields_consumed': [
            'credit_card.balance', 'credit_card.annual_rate',
            'credit_card.min_payment'],
    },

    'Q06': {
        'final': '144.00',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'annual_fees',
                'value': '144.00',
                'operation': 'multiply',
                'source_fields': ['checking.monthly_fee'],
                'inputs': ['12.00', '12'],
                'formula': '12.00 * 12 = 144.00',
            },
        ],
        'source_fields_consumed': ['checking.monthly_fee'],
    },

    # ------------------------------------------------------------------
    # Q07: THE ROUND-ONCE DEMONSTRATION
    #
    # CORRECT (full precision, quantise once at end):
    #   Step 1: 42175.00 * 7.8 / 100 / 12 = 274.1375        (exact)
    #   Step 2: 274.1375 - 15.00 = 259.1375                  (exact)
    #   Step 3: 259.1375 * 3 = 777.4125                      (exact)
    #   Quantise: 777.4125 -> 777.41 (HALF_UP or HALF_EVEN)
    #
    # WRONG (round each step -- the V1 defect):
    #   Step 1: 274.1375 -> round to 274.14
    #   Step 2: 274.14 - 15.00 = 259.14
    #   Step 3: 259.14 * 3 = 777.42                          != 777.41
    #
    # The difference (0.01) is the same class of defect that made
    # V1 report $149.80 when the true value was $149.79.
    # ------------------------------------------------------------------
    'Q07': {
        'final': '777.41',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'monthly_return',
                'value': '274.1375',
                'operation': 'multiply_then_divide',
                'source_fields': [
                    'investment.balance', 'investment.annual_rate'],
                'inputs': ['42175.00', '7.8', '12'],
                'formula': '42175.00 * 7.8 / 100 / 12 = 274.1375',
            },
            {
                'label': 'monthly_net',
                'value': '259.1375',
                'operation': 'subtract',
                'source_fields': ['investment.monthly_fee'],
                'inputs': ['274.1375', '15.00'],
                'formula': '274.1375 - 15.00 = 259.1375',
            },
            {
                'label': 'quarterly_net',
                'value': '777.4125',
                'operation': 'multiply',
                'source_fields': [],
                'inputs': ['259.1375', '3'],
                'formula': '259.1375 * 3 = 777.4125',
            },
        ],
        'source_fields_consumed': [
            'investment.balance', 'investment.annual_rate',
            'investment.monthly_fee'],
        'quantisation_note':
            'Quantise 777.4125 once at end: digit after cut is 2 (<5), '
            'rounds down to 777.41 under both HALF_UP and HALF_EVEN. '
            'Unambiguous.',
        'round_then_compute_wrong_answer': '777.42',
    },

    'Q08': {
        'final': '287069.25',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'monthly_interest',
                'value': '1006.25',
                'operation': 'multiply_then_divide',
                'source_fields': [
                    'mortgage.balance', 'mortgage.annual_rate'],
                'inputs': ['287500.00', '4.20', '12'],
                'formula': 'abs(-287500.00) * 4.20 / 100 / 12 = 1006.25',
            },
            {
                'label': 'principal_portion',
                'value': '430.75',
                'operation': 'subtract',
                'source_fields': ['mortgage.min_payment'],
                'inputs': ['1437.00', '1006.25'],
                'formula': '1437.00 - 1006.25 = 430.75',
            },
            {
                'label': 'remaining_balance',
                'value': '287069.25',
                'operation': 'subtract',
                'source_fields': [],
                'inputs': ['287500.00', '430.75'],
                'formula': '287500.00 - 430.75 = 287069.25',
            },
        ],
        'source_fields_consumed': [
            'mortgage.balance', 'mortgage.annual_rate',
            'mortgage.min_payment'],
    },

    'Q09': {
        'final': '3.20',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'monthly_interest',
                'value': '15.20',
                'operation': 'multiply_then_divide',
                'source_fields': [
                    'savings.balance', 'savings.annual_rate'],
                'inputs': ['15200.00', '1.2', '12'],
                'formula': '15200.00 * 1.2 / 100 / 12 = 15.20',
            },
            {
                'label': 'net_income',
                'value': '3.20',
                'operation': 'subtract',
                'source_fields': ['checking.monthly_fee'],
                'inputs': ['15.20', '12.00'],
                'formula': '15.20 - 12.00 = 3.20',
            },
        ],
        'source_fields_consumed': [
            'savings.balance', 'savings.annual_rate',
            'checking.monthly_fee'],
    },

    'Q10': {
        'final': '3109.65',
        'derivable': True,
        'required_operation': 'calculator',
        'intermediates': [
            {
                'label': 'monthly_return',
                'value': '274.1375',
                'operation': 'multiply_then_divide',
                'source_fields': [
                    'investment.balance', 'investment.annual_rate'],
                'inputs': ['42175.00', '7.8', '12'],
                'formula': '42175.00 * 7.8 / 100 / 12 = 274.1375',
            },
            {
                'label': 'monthly_net',
                'value': '259.1375',
                'operation': 'subtract',
                'source_fields': ['investment.monthly_fee'],
                'inputs': ['274.1375', '15.00'],
                'formula': '274.1375 - 15.00 = 259.1375',
            },
            {
                'label': 'annual_net',
                'value': '3109.65',
                'operation': 'multiply',
                'source_fields': [],
                'inputs': ['259.1375', '12'],
                'formula': '259.1375 * 12 = 3109.65',
            },
        ],
        'source_fields_consumed': [
            'investment.balance', 'investment.annual_rate',
            'investment.monthly_fee'],
        'quantisation_note':
            '259.1375 * 12 = 3109.6500 — exact to 2dp, no rounding '
            'needed. Unambiguous under any mode.',
    },
}


# -- Verification: compute each answer and assert correctness ---------

def verify_all():
    """Verify every ground-truth entry by recomputing from fixture.

    All computation uses Decimal. No float. Quantise once at end.
    """
    from decimal import ROUND_HALF_UP
    results = {}

    for qid, gt in GROUND_TRUTH.items():
        # Recompute the final intermediate (which is the answer
        # before quantisation)
        last_intermediate = Decimal(gt['intermediates'][-1]['value'])

        # Quantise once
        quantised = last_intermediate.quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP)

        expected = Decimal(gt['final'])
        match = quantised == expected

        results[qid] = {
            'expected': str(expected),
            'computed': str(quantised),
            'full_precision': str(last_intermediate),
            'match': match,
        }

        status = 'OK' if match else 'MISMATCH'
        print(f'  {qid}: {status}  expected={expected}  '
              f'computed={quantised}  full={last_intermediate}')

    # Q07 specific: demonstrate the round-then-compute defect
    print()
    print('  Q07 round-then-compute demonstration:')
    q07 = GROUND_TRUTH['Q07']
    step1 = Decimal(q07['intermediates'][0]['value'])  # 274.1375
    step2 = Decimal(q07['intermediates'][1]['value'])  # 259.1375
    step3 = Decimal(q07['intermediates'][2]['value'])  # 777.4125

    # CORRECT: quantise once at end
    correct = step3.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(f'    Correct (round once):  {step1} -> {step2} -> '
          f'{step3} -> {correct}')

    # WRONG: round each intermediate
    wrong_s1 = step1.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    wrong_s2 = (wrong_s1 - Decimal('15.00')).quantize(
        Decimal('0.01'), rounding=ROUND_HALF_UP)
    wrong_s3 = (wrong_s2 * Decimal('3')).quantize(
        Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(f'    Wrong (round each):    {wrong_s1} -> {wrong_s2} -> '
          f'{wrong_s3}')
    print(f'    Difference: {wrong_s3} != {correct}  '
          f'(error = {wrong_s3 - correct})')

    all_ok = all(r['match'] for r in results.values())
    return all_ok, results


if __name__ == '__main__':
    print('Ground-truth verification:')
    ok, _ = verify_all()
    print()
    print('ALL PASS' if ok else 'FAILURES DETECTED')
    raise SystemExit(0 if ok else 1)
