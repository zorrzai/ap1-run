"""Ground-truth module: derivation logic for 10 example items.

THIS IS THE FILE OPERATORS WILL COPY.

C8.5 compliance:
  - No expected value or intermediate appears as a numeric literal.
  - Every value is the RETURN VALUE of an expression over delivered_context.
  - Numeric literals are permitted ONLY as genuine constants of the
    problem: 12 (months), 3 (quarter), 4 (quarters/year), 100 (percentage conversion).
  - The module never sees the full fixture; it receives only the
    accounts named in the item's source_accounts.
  - The module returns UNQUANTISED values. The runner quantises once.

C8.6 disclosure:
  - The author of this module is the same agent that wrote the runner.
    This is the same-implementer condition C8.6 names.
  - This example module is DEMONSTRATION MATERIAL, not an independent
    derivation.
  - An independent ground-truth module must be authored by a party
    who did not write or review the runner code.

Typed inputs (for D7.2 operand provenance):
  Each intermediate's inputs list uses typed dicts:
    {"source": "account.field"}      - from delivered_context
    {"intermediate": "step_label"}   - from a prior intermediate
    {"constant": "12"}               - genuine problem constant
"""

from decimal import Decimal as D


# -- Public interface -------------------------------------------------

def compute(item_id, delivered_context):
    """Compute ground truth for one item.

    Args:
        item_id: Question identifier (e.g. "Q01").
        delivered_context: Dict built by the runner from fixture data
            for ONLY the accounts listed in the item's source_accounts.
            The module never sees the full fixture.

    Returns:
        GroundTruth dict with keys:
            final              Decimal (unquantised)
            derivable          bool
            required_operation str
            intermediates      list of step dicts
            source_fields_consumed  list of "account.field" strings

    Raises:
        KeyError if a required field is absent from delivered_context.
        ValueError if no derivation is registered for item_id.
    """
    if item_id not in DERIVATIONS:
        raise ValueError(f"no derivation registered for {item_id!r}")
    return DERIVATIONS[item_id](delivered_context)


# -- Q01: Monthly savings interest ------------------------------------

def derive_q01(ctx):
    bal = D(ctx["savings"]["balance"])
    rate = D(ctx["savings"]["annual_rate"])

    monthly_interest = bal * rate / D("100") / D("12")

    return {
        "final": monthly_interest,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "monthly_interest",
                "value": monthly_interest,
                "operation": "multiply_then_divide",
                "inputs": [
                    {"source": "savings.balance"},
                    {"source": "savings.annual_rate"},
                    {"constant": "100"},
                    {"constant": "12"},
                ],
            },
        ],
        "source_fields_consumed": ["savings.balance", "savings.annual_rate"],
    }


# -- Q02: Available credit -------------------------------------------

def derive_q02(ctx):
    limit = D(ctx["credit_card"]["credit_limit"])
    balance = D(ctx["credit_card"]["balance"])

    available = limit - balance  # balance is positive magnitude; subtract for available

    return {
        "final": available,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "available_credit",
                "value": available,
                "operation": "subtract",
                "inputs": [
                    {"source": "credit_card.credit_limit"},
                    {"source": "credit_card.balance"},
                ],
            },
        ],
        "source_fields_consumed": [
            "credit_card.credit_limit", "credit_card.balance"],
    }


# -- Q03: Monthly credit card interest --------------------------------

def derive_q03(ctx):
    balance = D(ctx["credit_card"]["balance"])
    rate = D(ctx["credit_card"]["annual_rate"])

    monthly_interest = balance * rate / D("100") / D("12")

    return {
        "final": monthly_interest,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "monthly_interest",
                "value": monthly_interest,
                "operation": "multiply_then_divide",
                "inputs": [
                    {"source": "credit_card.balance"},
                    {"source": "credit_card.annual_rate"},
                    {"constant": "100"},
                    {"constant": "12"},
                ],
            },
        ],
        "source_fields_consumed": [
            "credit_card.balance", "credit_card.annual_rate"],
    }


# -- Q04: First mortgage payment principal ----------------------------

def derive_q04(ctx):
    balance = D(ctx["mortgage"]["balance"])
    rate = D(ctx["mortgage"]["annual_rate"])
    payment = D(ctx["mortgage"]["min_payment"])

    monthly_interest = balance * rate / D("100") / D("12")
    principal = payment - monthly_interest

    return {
        "final": principal,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "monthly_interest",
                "value": monthly_interest,
                "operation": "multiply_then_divide",
                "inputs": [
                    {"source": "mortgage.balance"},
                    {"source": "mortgage.annual_rate"},
                    {"constant": "100"},
                    {"constant": "12"},
                ],
            },
            {
                "label": "principal_portion",
                "value": principal,
                "operation": "subtract",
                "inputs": [
                    {"source": "mortgage.min_payment"},
                    {"intermediate": "monthly_interest"},
                ],
            },
        ],
        "source_fields_consumed": [
            "mortgage.balance", "mortgage.annual_rate",
            "mortgage.min_payment"],
    }


# -- Q05: Credit card after one month --------------------------------

def derive_q05(ctx):
    balance = D(ctx["credit_card"]["balance"])
    rate = D(ctx["credit_card"]["annual_rate"])
    min_pay = D(ctx["credit_card"]["min_payment"])

    monthly_interest = balance * rate / D("100") / D("12")
    # Balance is positive magnitude of a liability.
    # New magnitude = old + interest - payment. Reported as negative.
    new_balance = -(balance + monthly_interest - min_pay)

    return {
        "final": new_balance,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "monthly_interest",
                "value": monthly_interest,
                "operation": "multiply_then_divide",
                "inputs": [
                    {"source": "credit_card.balance"},
                    {"source": "credit_card.annual_rate"},
                    {"constant": "100"},
                    {"constant": "12"},
                ],
            },
            {
                "label": "new_balance",
                "value": new_balance,
                "operation": "sign_from_direction",
                "inputs": [
                    {"source": "credit_card.balance"},
                    {"intermediate": "monthly_interest"},
                    {"source": "credit_card.min_payment"},
                ],
            },
        ],
        "source_fields_consumed": [
            "credit_card.balance", "credit_card.annual_rate",
            "credit_card.min_payment"],
    }


# -- Q06: Annual checking fees ----------------------------------------
#
# D7.2 NOTE: This item is AMBIGUOUS for operand-origination testing.
# The expression is monthly_fee * 12, but checking.monthly_fee = "12.00",
# so the operand "12" resolves both as a source field and as a permitted
# constant (months in a year). This item cannot detect origination at
# that position. Do not use Q06 as a positive or negative case for D7.2.

def derive_q06(ctx):
    fee = D(ctx["checking"]["monthly_fee"])

    annual_fees = fee * D("12")

    return {
        "final": annual_fees,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "annual_fees",
                "value": annual_fees,
                "operation": "multiply",
                "inputs": [
                    {"source": "checking.monthly_fee"},
                    {"constant": "12"},
                ],
            },
        ],
        "source_fields_consumed": ["checking.monthly_fee"],
    }


# -- Q07: Investment quarterly net growth -----------------------------
#
# THE ROUND-ONCE DEMONSTRATION.
#
# Unquantised result: 777.4125
# Quantised once at end: 777.41  (remainder 0.0025, rounds DOWN
#   under both HALF_UP and HALF_EVEN — mode-independent)
#
# If rounded at each step: 274.14 -> 259.14 -> 777.42 != 777.41
# That is the round-then-compute defect R0.4.1 prohibits.

def derive_q07(ctx):
    balance = D(ctx["investment"]["balance"])
    rate = D(ctx["investment"]["annual_rate"])
    fee = D(ctx["investment"]["monthly_fee"])

    monthly_return = balance * rate / D("100") / D("12")
    monthly_net = monthly_return - fee
    quarterly_net = monthly_net * D("3")

    return {
        "final": quarterly_net,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "monthly_return",
                "value": monthly_return,
                "operation": "multiply_then_divide",
                "inputs": [
                    {"source": "investment.balance"},
                    {"source": "investment.annual_rate"},
                    {"constant": "100"},
                    {"constant": "12"},
                ],
            },
            {
                "label": "monthly_net",
                "value": monthly_net,
                "operation": "subtract",
                "inputs": [
                    {"intermediate": "monthly_return"},
                    {"source": "investment.monthly_fee"},
                ],
            },
            {
                "label": "quarterly_net",
                "value": quarterly_net,
                "operation": "multiply",
                "inputs": [
                    {"intermediate": "monthly_net"},
                    {"constant": "3"},
                ],
            },
        ],
        "source_fields_consumed": [
            "investment.balance", "investment.annual_rate",
            "investment.monthly_fee"],
    }


# -- Q08: Mortgage balance after first payment ------------------------

def derive_q08(ctx):
    balance = D(ctx["mortgage"]["balance"])
    rate = D(ctx["mortgage"]["annual_rate"])
    payment = D(ctx["mortgage"]["min_payment"])

    monthly_interest = balance * rate / D("100") / D("12")
    principal = payment - monthly_interest
    remaining = balance - principal

    return {
        "final": remaining,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "monthly_interest",
                "value": monthly_interest,
                "operation": "multiply_then_divide",
                "inputs": [
                    {"source": "mortgage.balance"},
                    {"source": "mortgage.annual_rate"},
                    {"constant": "100"},
                    {"constant": "12"},
                ],
            },
            {
                "label": "principal_portion",
                "value": principal,
                "operation": "subtract",
                "inputs": [
                    {"source": "mortgage.min_payment"},
                    {"intermediate": "monthly_interest"},
                ],
            },
            {
                "label": "remaining_balance",
                "value": remaining,
                "operation": "subtract",
                "inputs": [
                    {"source": "mortgage.balance"},
                    {"intermediate": "principal_portion"},
                ],
            },
        ],
        "source_fields_consumed": [
            "mortgage.balance", "mortgage.annual_rate",
            "mortgage.min_payment"],
    }


# -- Q09: Net monthly savings after checking fees --------------------

def derive_q09(ctx):
    sav_balance = D(ctx["savings"]["balance"])
    sav_rate = D(ctx["savings"]["annual_rate"])
    chk_fee = D(ctx["checking"]["monthly_fee"])

    monthly_interest = sav_balance * sav_rate / D("100") / D("12")
    net = monthly_interest - chk_fee

    return {
        "final": net,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "monthly_interest",
                "value": monthly_interest,
                "operation": "multiply_then_divide",
                "inputs": [
                    {"source": "savings.balance"},
                    {"source": "savings.annual_rate"},
                    {"constant": "100"},
                    {"constant": "12"},
                ],
            },
            {
                "label": "net_income",
                "value": net,
                "operation": "subtract",
                "inputs": [
                    {"intermediate": "monthly_interest"},
                    {"source": "checking.monthly_fee"},
                ],
            },
        ],
        "source_fields_consumed": [
            "savings.balance", "savings.annual_rate",
            "checking.monthly_fee"],
    }


# -- Q10: Investment annual net growth --------------------------------

def derive_q10(ctx):
    balance = D(ctx["investment"]["balance"])
    rate = D(ctx["investment"]["annual_rate"])
    fee = D(ctx["investment"]["monthly_fee"])

    monthly_return = balance * rate / D("100") / D("12")
    monthly_net = monthly_return - fee
    annual_net = monthly_net * D("12")

    return {
        "final": annual_net,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "monthly_return",
                "value": monthly_return,
                "operation": "multiply_then_divide",
                "inputs": [
                    {"source": "investment.balance"},
                    {"source": "investment.annual_rate"},
                    {"constant": "100"},
                    {"constant": "12"},
                ],
            },
            {
                "label": "monthly_net",
                "value": monthly_net,
                "operation": "subtract",
                "inputs": [
                    {"intermediate": "monthly_return"},
                    {"source": "investment.monthly_fee"},
                ],
            },
            {
                "label": "annual_net",
                "value": annual_net,
                "operation": "multiply",
                "inputs": [
                    {"intermediate": "monthly_net"},
                    {"constant": "12"},
                ],
            },
        ],
        "source_fields_consumed": [
            "investment.balance", "investment.annual_rate",
            "investment.monthly_fee"],
    }


# -- Dispatch table ---------------------------------------------------

DERIVATIONS = {
    "Q01": derive_q01,
    "Q02": derive_q02,
    "Q03": derive_q03,
    "Q04": derive_q04,
    "Q05": derive_q05,
    "Q06": derive_q06,
    "Q07": derive_q07,
    "Q08": derive_q08,
    "Q09": derive_q09,
    "Q10": derive_q10,
}


# -- Standalone verification -----------------------------------------

if __name__ == "__main__":
    import json
    import os
    import sys
    from decimal import ROUND_HALF_UP

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    base = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(base, "fixture.json"), "r", encoding="utf-8") as f:
        fixture = json.load(f)

    with open(os.path.join(base, "questions.json"), "r", encoding="utf-8") as f:
        questions = json.load(f)

    accounts = {a["id"]: a for a in fixture["accounts"]}

    print("Ground-truth verification (C8.5 compliant):")
    print("All values computed from fixture expressions, no authored literals.")
    print()

    all_ok = True
    for item in questions["items"]:
        item_id = item["id"]

        # Build delivered context — runner's responsibility
        ctx = {}
        for acct_id in item["source_accounts"]:
            acct = accounts[acct_id]
            ctx[acct_id] = {
                k: v for k, v in acct.items() if k not in ("id", "name")
            }

        result = compute(item_id, ctx)
        full = result["final"]
        quantised = full.quantize(D("0.01"), rounding=ROUND_HALF_UP)
        n_steps = len(result["intermediates"])

        print(f"  {item_id} ({n_steps}-step): {item['text']}")
        for step in result["intermediates"]:
            typed_inputs = []
            for inp in step["inputs"]:
                if "source" in inp:
                    typed_inputs.append(f"src:{inp['source']}")
                elif "intermediate" in inp:
                    typed_inputs.append(f"int:{inp['intermediate']}")
                elif "constant" in inp:
                    typed_inputs.append(f"const:{inp['constant']}")
            print(f"    {step['label']} = {step['value']}")
            print(f"      [{step['operation']}({', '.join(typed_inputs)})]")
        print(f"    -> full_precision={full}  quantised_2dp={quantised}")
        print()

    # Q07 round-once vs round-each
    ctx_inv = {}
    for acct_id in ["investment"]:
        acct = accounts[acct_id]
        ctx_inv[acct_id] = {
            k: v for k, v in acct.items() if k not in ("id", "name")
        }

    q07 = compute("Q07", ctx_inv)
    s1 = q07["intermediates"][0]["value"]
    s2 = q07["intermediates"][1]["value"]
    s3 = q07["intermediates"][2]["value"]

    correct = s3.quantize(D("0.01"), rounding=ROUND_HALF_UP)

    wrong_s1 = s1.quantize(D("0.01"), rounding=ROUND_HALF_UP)
    wrong_s2 = (wrong_s1 - D(ctx_inv["investment"]["monthly_fee"])).quantize(
        D("0.01"), rounding=ROUND_HALF_UP)
    wrong_s3 = (wrong_s2 * D("3")).quantize(D("0.01"), rounding=ROUND_HALF_UP)

    print("Q07 round-once vs round-each:")
    print(f"  Correct (round once):  {s1} -> {s2} -> {s3} -> {correct}")
    print(f"  Wrong (round each):    {wrong_s1} -> {wrong_s2} -> {wrong_s3}")
    differ = correct != wrong_s3
    print(f"  Differ: {differ}  (must be True)")
    if not differ:
        print("  ERROR: round-once and round-each produce the same result!")
        all_ok = False
    print()

    print("ALL PASS" if all_ok else "FAILURES DETECTED")
    raise SystemExit(0 if all_ok else 1)
