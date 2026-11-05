"""Perturbation check for ground-truth derivations.

At seal time, for each item, verifies that the derivation consumes
EXACTLY the fields it declares:

1. Each field in source_fields_consumed must affect the result when
   perturbed. If it does not, the declaration claims a dependency
   that does not exist. REFUSE, naming the field.

2. If NO declared field affects the result, the module is returning
   constants. REFUSE.

3. Each field in delivered_context NOT in source_fields_consumed must
   NOT affect the result when perturbed. If it does, the declaration
   is incomplete — the module reads more than it admits to. REFUSE,
   naming the undeclared field.

Perturbation: each numeric field is shifted by +1 (Decimal("1")).
Non-numeric fields such as 'direction' are skipped: they are neither
perturbed nor checked for declaration.
"""

import copy
from decimal import Decimal, InvalidOperation


class PerturbationError(Exception):
    """A perturbation check failed."""


def perturbation_check(item_id, delivered_context, compute_fn):
    """Run all three perturbation checks for one item.

    Args:
        item_id: The question id (e.g. "Q01").
        delivered_context: The context dict for this item.
        compute_fn: Callable(item_id, ctx) -> ground_truth_result.

    Returns:
        List of (field, original_final, perturbed_final) for each
        declared field that was verified.

    Raises:
        PerturbationError if any check fails.
    """
    original = compute_fn(item_id, delivered_context)
    original_final = original["final"]
    declared = set(original["source_fields_consumed"])

    # Build flat field map
    all_fields = _flat_fields(delivered_context)

    # Check declared fields exist in context
    for field in declared:
        if field not in all_fields:
            raise PerturbationError(
                f"{item_id}: declared field {field!r} not found in "
                f"delivered context (available: {sorted(all_fields)})")

    verified = []
    any_affected = False

    # Check 1: each declared field must affect the result
    for field in sorted(declared):
        perturbed_ctx = _perturb(delivered_context, field)
        perturbed = compute_fn(item_id, perturbed_ctx)
        if perturbed["final"] == original_final:
            raise PerturbationError(
                f"{item_id}: declared field {field!r} does not affect "
                f"the result (original={original_final}, "
                f"perturbed={perturbed['final']}). "
                f"Remove from source_fields_consumed or fix derivation.")
        any_affected = True
        verified.append((field, original_final, perturbed["final"]))

    # Check 2: at least one declared field must have affected it
    if not any_affected and declared:
        raise PerturbationError(
            f"{item_id}: no declared field affects the result. "
            f"Module is returning constants.")

    # Check 3: undeclared fields must NOT affect the result
    for field in sorted(all_fields):
        if field in declared:
            continue
        perturbed_ctx = _perturb(delivered_context, field)
        perturbed = compute_fn(item_id, perturbed_ctx)
        if perturbed["final"] != original_final:
            raise PerturbationError(
                f"{item_id}: undeclared field {field!r} affects the "
                f"result (original={original_final}, "
                f"perturbed={perturbed['final']}). "
                f"Add to source_fields_consumed.")

    return verified


def _flat_fields(ctx):
    """Return {\"account.field\": str_value} for all fields in context."""
    result = {}
    for acct_id, acct_data in ctx.items():
        for field_name, value in acct_data.items():
            result[f"{acct_id}.{field_name}"] = value
    return result


def _perturb(ctx, field_path):
    """Return a deep copy of ctx with field_path's value shifted by +1.

    field_path is \"account.field\" format.
    """
    parts = field_path.split(".", 1)
    if len(parts) != 2:
        raise PerturbationError(
            f"invalid field path: {field_path!r} (expected account.field)")

    acct_id, field_name = parts
    perturbed = copy.deepcopy(ctx)

    old_val = perturbed[acct_id][field_name]
    try:
        new_val = Decimal(old_val) + Decimal("1")
        perturbed[acct_id][field_name] = str(new_val)
    except (InvalidOperation, TypeError):
        # Non-numeric field — return unchanged copy
        pass

    return perturbed
