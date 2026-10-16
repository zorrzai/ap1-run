"""The shipped example ground truth (example/ground_truth_example.py) as the
runner uses it: computed from the delivered context of each item, and its
declared constants read by operand provenance (scoring/provenance/trace.py).

From legacy verify.py test_ground_truth and verify_e7_coverage.py
test_e3_q07_constant_4_resolves, test_q09_q05_unaffected and
test_q09_q08_unaffected (step 3, G9).
"""

from decimal import Decimal

import pytest

from ap1_run.execution.context import build_delivered_context
from ap1_run.scoring.provenance.trace import _collect_constants, resolve_operand

D = Decimal
QUANT = {'places': 2, 'rounding': 'ROUND_HALF_UP'}

# Unquantised finals as computed today from example/fixture.json.
FINALS = {
    'Q01': '15.200', 'Q02': '2600.00', 'Q03': '36.000', 'Q04': '430.7500',
    'Q05': '2411.000', 'Q06': '144.00', 'Q07': '777.4125',
    'Q08': '287069.2500', 'Q09': '3.200', 'Q10': '3109.6500',
}


def ground_truth(example, item_id):
    item = next(i for i in example['items'] if i['id'] == item_id)
    ctx = build_delivered_context(example['fixture'], item['source_accounts'])
    return ctx, example['gt'].compute(item_id, ctx)


def test_example_ground_truth_every_item_derivable_with_its_final(example):
    finals = {}
    for item in example['items']:
        _, gt = ground_truth(example, item['id'])
        assert gt['derivable'] is True
        finals[item['id']] = str(gt['final'])
    assert finals == FINALS


def test_example_ground_truth_declared_constants_per_item(example):
    constants = {item['id']: sorted(_collect_constants(
        ground_truth(example, item['id'])[1]))
        for item in example['items']}
    assert constants == {
        'Q01': [D(1), D(12), D(100)], 'Q02': [D(1)],
        'Q03': [D(1), D(12), D(100)], 'Q04': [D(1), D(12), D(100)],
        'Q05': [D(1), D(12), D(100)], 'Q06': [D(1), D(12)],
        'Q07': [D(1), D(3), D(4), D(12), D(100)],
        'Q08': [D(1), D(12), D(100)], 'Q09': [D(1), D(12), D(100)],
        'Q10': [D(1), D(12), D(100)],
    }


@pytest.mark.req('R2.4')
def test_example_q07_operand_4_resolves_as_declared_constant(example):
    # Q07 declares 4 (quarters per year) although derive_q07 does not use
    # it; an operand 4 is then grounded at step 1.
    ctx, gt = ground_truth(example, 'Q07')
    intermediates = [{'label': i['label'], 'value': D(str(i['value']))}
                     for i in gt['intermediates']]
    result = resolve_operand(D('4'), ctx, intermediates, _collect_constants(gt),
                             permitted_transforms=[], quant_config=QUANT)
    assert (result['step'], result['resolution']) == (1, 'constant')


@pytest.mark.parametrize('item_id', ['Q05', 'Q08'])
@pytest.mark.parametrize('operand', ['100', '12'])
def test_example_declared_constants_resolve_at_step1(example, item_id,
                                                     operand):
    ctx, gt = ground_truth(example, item_id)
    result = resolve_operand(D(operand), ctx, [], _collect_constants(gt),
                             [], QUANT)
    assert (result['step'], result['resolution']) == (1, 'constant')
