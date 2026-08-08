# Superseded Run Artifact

This directory contains the smoke_summary.json from a 1,000-execution
gpt-5.6-sol run against the **original fixture**, which encoded direction
inside the magnitude (e.g. `credit_card.balance = -2400.00`).

The fixture was subsequently restructured to represent magnitude and direction
as separate fields (`{"balance": 2400.00, "direction": "liability"}`). The
current runs (`run_a_mini/`, `run_b_sol/`) use the restructured fixture.

This artifact is retained because F2 in FINDINGS.md reports figures from it.
Those figures are verified by `verify_findings.py` against this file.

## Key figures from this artifact

- 818 total originated operand values
- 288 constant-1 operands (removed by constant-set declaration)
- 530 remaining step-5 operands (post constant-1 correction)
- 524 of 530 are absolute values of negative fixture quantities (sign-convention)
- 6 remaining: 3× `1.0065`, 3× `45` (same pre-computations as current run)
