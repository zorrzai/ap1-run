"""SPEC R4.1 planted behaviour for execution/seal.py (legacy
verify_r41.py B23)."""

from decimal import Decimal

import pytest

from ap1_run.execution.seal import SealError, perturbation_check


class ConstantModule:
    @staticmethod
    def compute(item_id, ctx):
        return {'final': Decimal('42.00'), 'derivable': True,
                'required_operation': 'calculator', 'intermediates': [],
                'source_fields_consumed': ['savings.balance']}


@pytest.mark.finding('T3-7')
@pytest.mark.req('R4.1', 'R1.1')
def test_r41_b23_constant_ground_truth_is_refused_naming_the_field():
    # perturbation_check refuses the module, but the live run never calls
    # it (T3-7), so R4.1's "refused at seal" holds for the unit only.
    fixture = {'accounts': [{'id': 'savings', 'name': 'Savings',
                             'balance': '15200.00'}]}
    questions = {'items': [{'id': 'Q99', 'source_accounts': ['savings']}]}
    with pytest.raises(SealError) as exc:
        perturbation_check(ConstantModule, fixture, questions)
    assert str(exc.value) == (
        'perturbation check failed: constant-returning module detected. '
        'Fields that had no effect: savings.balance')
