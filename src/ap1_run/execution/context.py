"""Delivered-context construction from fixture + source_accounts.

Spec: AP-1 Runner Build Spec v0.3, R1.2 and R3.1.

The ground-truth module never sees the full fixture. The runner builds
a delivered_context containing ONLY the accounts listed in the item's
source_accounts.

lookup_collision is computed by the runner at seal time, not declared
by the operator.
"""

from decimal import Decimal


class ContextError(Exception):
    """Context construction failure."""


def build_delivered_context(fixture, source_accounts):
    """Build the context delivered to the ground-truth module.

    Only accounts listed in source_accounts are included.
    Fields 'id' and 'name' are excluded (structural, not data).

    Returns: dict keyed by account id, each value a dict of
    field_name -> string_value.
    """
    accounts_by_id = {a['id']: a for a in fixture['accounts']}
    ctx = {}
    for acct_id in source_accounts:
        if acct_id not in accounts_by_id:
            raise ContextError(
                f'source_account {acct_id!r} not found in fixture '
                f'(available: {sorted(accounts_by_id)})')
        acct = accounts_by_id[acct_id]
        ctx[acct_id] = {
            k: v for k, v in acct.items() if k not in ('id', 'name')
        }
    return ctx


def check_lookup_collision(final_value, delivered_context):
    """Check if the expected final value appears verbatim in the
    delivered context.

    R3.1: lookup_collision is computed by the runner at seal time,
    not declared by the operator.

    Returns: (collision_found, colliding_field_or_None)
    """
    for acct_id, acct_data in delivered_context.items():
        for field_name, field_value in acct_data.items():
            try:
                if Decimal(str(field_value)) == final_value:
                    return True, f'{acct_id}.{field_name}'
            except Exception:
                continue
    return False, None


def lookup_collisions(compute, fixture, questions):
    """Every item whose expected value appears in its delivered context,
    computed at seal time (R3.1: "computed by the runner at seal time ...
    reported at seal"; T3-75). Underivable items have no expected value
    and are skipped.

    Args:
        compute: the ground-truth module's compute(item_id, ctx)
        fixture, questions: as loaded (questions['items'])

    Returns: list of (item_id, colliding 'account.field'), in item order.
    """
    found = []
    for item in questions['items']:
        ctx = build_delivered_context(fixture, item['source_accounts'])
        gt = compute(item['id'], ctx)
        if not gt.get('derivable', True):
            continue
        collision, field = check_lookup_collision(gt['final'], ctx)
        if collision:
            found.append((item['id'], field))
    return found


def format_fixture_context(fixture, item):
    """Format the fixture context for the user message.

    Only source_accounts are included in the formatted output.
    """
    source_accounts = item.get('source_accounts', [])
    accounts = {a['id']: a for a in fixture['accounts']}

    lines = ['Here is the financial information:']
    for acct_id in source_accounts:
        if acct_id in accounts:
            acct = accounts[acct_id]
            lines.append(f'\n{acct.get("name", acct_id)}:')
            for k, v in acct.items():
                if k not in ('id', 'name'):
                    label = k.replace('_', ' ').title()
                    lines.append(f'  {label}: {v}')

    return '\n'.join(lines)


class TrackingContext(dict):
    """Dict wrapper that records field accesses.

    Used at seal time to verify that a ground-truth module reads
    ONLY the fields declared in source_fields_consumed.

    Usage:
        tc = TrackingContext(delivered_context)
        ground_truth_module.compute(item_id, tc)
        accessed = tc.accessed_fields()
        # compare with source_fields_consumed

    The __getitem__ on the outer dict returns TrackingAccount
    wrappers. Each TrackingAccount records which fields are read.
    """

    def __init__(self, base_dict):
        super().__init__()
        self._accesses = set()
        for acct_id, acct_data in base_dict.items():
            self[acct_id] = TrackingAccount(acct_id, acct_data,
                                            self._accesses)

    def accessed_fields(self):
        """Return set of 'account.field' strings that were read."""
        return set(self._accesses)


class TrackingAccount(dict):
    """Account dict that records field accesses.

    Every method that hands out a field's value records the field (T3-8):
    a subscript, get(), pop() and setdefault() record the field named;
    items(), values(), copy(), popitem() and repr() hand out every value,
    so they record every field. Iteration and keys() give names only and
    record nothing, but overriding __iter__ also takes dict(acct) and
    {**acct} off CPython's dict-merge fast path, so that they read each
    value through __getitem__ and are recorded.
    """

    def __init__(self, acct_id, base_dict, access_set):
        super().__init__(base_dict)
        self._acct_id = acct_id
        self._access_set = access_set

    def _record(self, key):
        self._access_set.add(f'{self._acct_id}.{key}')

    def _record_all(self):
        for key in super().keys():
            self._record(key)

    def __getitem__(self, key):
        self._record(key)
        return super().__getitem__(key)

    def get(self, key, default=None):
        self._record(key)
        return super().get(key, default)

    def pop(self, key, *default):
        self._record(key)
        return super().pop(key, *default)

    def setdefault(self, key, default=None):
        self._record(key)
        return super().setdefault(key, default)

    def popitem(self):
        self._record_all()
        return super().popitem()

    def items(self):
        self._record_all()
        return super().items()

    def values(self):
        self._record_all()
        return super().values()

    def copy(self):
        self._record_all()
        return dict(super().items())

    def __repr__(self):
        self._record_all()
        return super().__repr__()

    def __iter__(self):
        return super().__iter__()

    def keys(self):
        return super().keys()
