"""Mock ground-truth module with an undeclared constant (E3 pattern)."""
from decimal import Decimal as D


def derive_q99(ctx):
    balance = D(ctx['acct']['balance'])
    quarterly = balance * D("7.8") / D("100") / D("4")
    return {
        "final": quarterly,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [
            {
                "label": "quarterly",
                "value": quarterly,
                "operation": "divide",
                "inputs": [
                    {"source": "acct.balance"},
                    {"source": "acct.annual_rate"},
                    {"constant": "100"},
                    # "4" deliberately NOT declared -- this is the E3 defect
                ],
            },
        ],
        "source_fields_consumed": ["acct.balance", "acct.annual_rate"],
    }


def compute(item_id, ctx):
    if item_id == 'Q99':
        return derive_q99(ctx)
    raise ValueError(f'unknown item {item_id}')
