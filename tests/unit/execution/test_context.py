"""Unit tests for the delivered context (execution/context.py).

build_delivered_context gives the ground-truth module only the accounts an
item names; check_lookup_collision looks for the expected answer among the
delivered values; format_fixture_context is the text the model is shown;
TrackingContext records which fields a ground-truth module reads at seal
time.
"""

from decimal import Decimal

import pytest

from ap1_run.execution.context import (
    ContextError, TrackingAccount, TrackingContext, build_delivered_context,
    check_lookup_collision, format_fixture_context,
)

D = Decimal


def fixture():
    return {'accounts': [
        {'id': 'savings', 'name': 'Savings', 'balance': '15200.00',
         'annual_rate': '1.2'},
        {'id': 'checking', 'name': 'Checking', 'balance': '3200.00',
         'monthly_fee': '12.00'},
        {'id': 'credit_card', 'name': 'Credit Card', 'balance': '2400.00',
         'min_payment': '25.00'},
    ]}


# -- build_delivered_context ------------------------------------------

@pytest.mark.req('R1.2')
def test_build_delivered_context_named_accounts_only():
    ctx = build_delivered_context(fixture(), ['savings'])
    assert ctx == {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}


def test_build_delivered_context_id_and_name_dropped_other_fields_kept():
    fx = {'accounts': [{'id': 'a', 'name': 'A', 'x_id': '1', 'nickname': 'n',
                        'direction': 'liability'}]}
    ctx = build_delivered_context(fx, ['a'])
    assert ctx == {'a': {'x_id': '1', 'nickname': 'n',
                         'direction': 'liability'}}


def test_build_delivered_context_order_follows_source_accounts():
    ctx = build_delivered_context(fixture(), ['credit_card', 'savings'])
    assert list(ctx) == ['credit_card', 'savings']


def test_build_delivered_context_no_source_accounts_empty():
    assert build_delivered_context(fixture(), []) == {}


def test_build_delivered_context_fixture_not_modified():
    fx = fixture()
    ctx = build_delivered_context(fx, ['savings'])
    ctx['savings']['balance'] = '0'
    assert fx == fixture()


def test_build_delivered_context_unknown_account_raises_naming_it():
    with pytest.raises(ContextError) as exc:
        build_delivered_context(fixture(), ['savings', 'pension'])
    assert str(exc.value) == (
        "source_account 'pension' not found in fixture "
        "(available: ['checking', 'credit_card', 'savings'])")


# -- check_lookup_collision -------------------------------------------

@pytest.mark.req('R3.1')
def test_check_lookup_collision_value_present_names_field():
    ctx = {'savings': {'balance': '15.20', 'annual_rate': '1.0'}}
    assert check_lookup_collision(D('15.20'), ctx) == (True, 'savings.balance')


def test_check_lookup_collision_compares_numerically():
    ctx = {'savings': {'balance': '15.2'}}
    assert check_lookup_collision(D('15.200'), ctx) == (True, 'savings.balance')


def test_check_lookup_collision_value_absent_none():
    ctx = {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}
    assert check_lookup_collision(D('15.20'), ctx) == (False, None)


def test_check_lookup_collision_empty_context_none():
    assert check_lookup_collision(D('1'), {}) == (False, None)


def test_check_lookup_collision_non_numeric_field_skipped():
    ctx = {'card': {'direction': 'liability', 'balance': '25'},
           'other': {'note': None, 'min_payment': '25.00'}}
    assert check_lookup_collision(D('25'), ctx) == (True, 'card.balance')


def test_check_lookup_collision_non_numeric_before_match_in_later_account():
    ctx = {'card': {'direction': 'liability'},
           'loan': {'kind': 'fixed', 'balance': '7'}}
    assert check_lookup_collision(D('7'), ctx) == (True, 'loan.balance')


def test_check_lookup_collision_first_match_in_context_order():
    ctx = {'a': {'x': '1', 'y': '5'}, 'b': {'z': '5'}}
    assert check_lookup_collision(D('5'), ctx) == (True, 'a.y')


def test_check_lookup_collision_numeric_value_not_string():
    ctx = {'a': {'count': 12}}
    assert check_lookup_collision(D('12'), ctx) == (True, 'a.count')


# -- format_fixture_context -------------------------------------------

@pytest.mark.finding('T3-56')
def test_format_fixture_context_exact_text():
    # T3-56 is a test gap (nothing checked what the model is shown); this
    # pins the text exactly.
    item = {'source_accounts': ['savings', 'credit_card']}
    assert format_fixture_context(fixture(), item) == (
        'Here is the financial information:\n'
        '\n'
        'Savings:\n'
        '  Balance: 15200.00\n'
        '  Annual Rate: 1.2\n'
        '\n'
        'Credit Card:\n'
        '  Balance: 2400.00\n'
        '  Min Payment: 25.00')


def test_format_fixture_context_only_source_accounts():
    text = format_fixture_context(fixture(), {'source_accounts': ['checking']})
    assert 'Savings' not in text and '15200.00' not in text
    assert 'Monthly Fee: 12.00' in text


def test_format_fixture_context_no_name_uses_id():
    fx = {'accounts': [{'id': 'acct_1', 'balance': '5'}]}
    assert format_fixture_context(fx, {'source_accounts': ['acct_1']}) == (
        'Here is the financial information:\n\nacct_1:\n  Balance: 5')


def test_format_fixture_context_no_source_accounts_key_header_only():
    assert format_fixture_context(fixture(), {}) == (
        'Here is the financial information:')


def test_format_fixture_context_unknown_account_skipped():
    # Unlike build_delivered_context, which raises ContextError. In
    # execute_item build_delivered_context runs first, so an unknown
    # account never gets here on the live path.
    text = format_fixture_context(
        fixture(), {'source_accounts': ['pension', 'checking']})
    assert text == ('Here is the financial information:\n\nChecking:\n'
                    '  Balance: 3200.00\n  Monthly Fee: 12.00')


# -- TrackingContext ---------------------------------------------------

def test_tracking_context_subscript_reads_recorded():
    tc = TrackingContext({'savings': {'balance': '1', 'annual_rate': '2',
                                      'fee': '3'}})
    assert tc['savings']['balance'] == '1'
    assert tc['savings']['annual_rate'] == '2'
    assert tc.accessed_fields() == {'savings.balance', 'savings.annual_rate'}


def test_tracking_context_nothing_read_empty():
    tc = TrackingContext({'savings': {'balance': '1'}})
    assert tc.accessed_fields() == set()


def test_tracking_context_accounts_shared_one_record():
    tc = TrackingContext({'a': {'x': '1'}, 'b': {'y': '2'}})
    _ = tc['a']['x']
    _ = tc['b']['y']
    assert tc.accessed_fields() == {'a.x', 'b.y'}


def test_tracking_context_values_and_keys_preserved():
    base = {'a': {'x': '1', 'y': '2'}, 'b': {}}
    tc = TrackingContext(base)
    assert tc == base
    assert isinstance(tc['a'], TrackingAccount)


def test_tracking_context_accessed_fields_returns_copy():
    tc = TrackingContext({'a': {'x': '1'}})
    _ = tc['a']['x']
    tc.accessed_fields().add('a.forged')
    assert tc.accessed_fields() == {'a.x'}


def test_tracking_context_missing_field_read_recorded_then_raises():
    tc = TrackingContext({'a': {'x': '1'}})
    with pytest.raises(KeyError):
        tc['a']['nope']
    assert tc.accessed_fields() == {'a.nope'}


def test_tracking_context_base_dict_not_modified():
    base = {'a': {'x': '1'}}
    tc = TrackingContext(base)
    tc['a']['x'] = '9'
    assert base == {'a': {'x': '1'}}


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g3-seal-guards; see inbox/2026-10-20_step4-g3-seal-guards-report.md.

@pytest.mark.finding('T3-8')
@pytest.mark.req('R3.1')
@pytest.mark.parametrize('read', [
    lambda acct: acct.get('annual_rate'),
    lambda acct: list(acct.items()),
    lambda acct: list(acct.values()),
    lambda acct: acct.copy()['annual_rate'],
    lambda acct: dict(acct)['annual_rate'],
    lambda acct: {**acct}['annual_rate'],
], ids=['get', 'items', 'values', 'copy', 'dict', 'unpack'])
def test_tracking_context_non_subscript_read_recorded(read):
    # Correct (T3-8; R3.1 via source_fields_check: an undeclared read is
    # refused with the field named): every path that hands out a field's
    # value records the field. Each read here exposes annual_rate, so it
    # must be among the accessed fields (a path that exposes every value,
    # like .items(), may record every field). Today nothing is recorded.
    tc = TrackingContext({'savings': {'balance': '1', 'annual_rate': '2'}})
    read(tc['savings'])
    assert 'savings.annual_rate' in tc.accessed_fields()


# --- Step 5 (seal-gt-guards): the exact record of each access path ---

ACCT = {'balance': '1', 'annual_rate': '2'}
BOTH = {'s.balance', 's.annual_rate'}


def tracked():
    tc = TrackingContext({'s': dict(ACCT)})
    return tc, tc['s']


@pytest.mark.finding('T3-8')
@pytest.mark.parametrize('read, value, recorded', [
    (lambda a: a.get('balance'), '1', {'s.balance'}),
    (lambda a: a.get('nope'), None, {'s.nope'}),
    (lambda a: a.get('nope', 'd'), 'd', {'s.nope'}),
    (lambda a: a.pop('balance'), '1', {'s.balance'}),
    (lambda a: a.pop('nope', 'd'), 'd', {'s.nope'}),
    (lambda a: a.setdefault('balance'), '1', {'s.balance'}),
    (lambda a: a.setdefault('nope', 'd'), 'd', {'s.nope'}),
    (lambda a: a.popitem(), ('annual_rate', '2'), BOTH),
    (lambda a: sorted(a.items()), [('annual_rate', '2'), ('balance', '1')],
     BOTH),
    (lambda a: sorted(a.values()), ['1', '2'], BOTH),
    (lambda a: a.copy(), ACCT, BOTH),
    (lambda a: type(a.copy()), dict, BOTH),
    (lambda a: dict(a), ACCT, BOTH),
    (lambda a: {**a}, ACCT, BOTH),
    (lambda a: repr(a), repr(ACCT), BOTH),
    (lambda a: sorted(a), ['annual_rate', 'balance'], set()),
    (lambda a: sorted(a.keys()), ['annual_rate', 'balance'], set()),
    (lambda a: 'balance' in a, True, set()),
    (lambda a: len(a), 2, set()),
])
def test_tracking_account_access_path_value_and_record(read, value, recorded):
    tc, acct = tracked()
    assert read(acct) == value
    assert tc.accessed_fields() == recorded


def test_tracking_account_pop_missing_without_default_recorded_then_raises():
    tc, acct = tracked()
    with pytest.raises(KeyError):
        acct.pop('nope')
    assert tc.accessed_fields() == {'s.nope'}


def test_tracking_account_setdefault_without_default_inserts_none():
    tc, acct = tracked()
    assert acct.setdefault('nope') is None
    assert dict.__getitem__(acct, 'nope') is None
