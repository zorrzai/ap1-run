# Example Fixture and Ground-Truth Module

## Fixture Properties

### Mode-Independence

All ten items are **mode-independent**: HALF_UP and HALF_EVEN produce
identical quantised results for every item. No reference answer depends
on the declared rounding mode.

This holds because no intermediate or final value has a remainder of
exactly 0.005 at the quantisation point. The closest case is Q07
(remainder 0.0025, which rounds DOWN under both modes).

An operator choosing a different rounding mode should know this property
holds for this example fixture. A production fixture may not share it;
mode-dependence in a production fixture must be disclosed per R0.4.1.

### Perturbation Check

All ten derivations pass the three-way perturbation check at seal time:
every declared source field affects the result, no undeclared field
affects the result, and no derivation returns constants.

## Phase D Notes (Do Not Change Now)

### Q06 Ambiguity for D7.2

Q06 computes `12.00 * 12` (monthly_fee times months-in-year). The
operand `12` resolves both as a source field value (checking.monthly_fee
= "12.00") and as a permitted constant (months in a year). This item can
never detect origination at that position. **Do not use Q06 as a positive
or negative case for D7.2 operand-resolution tests.**

### Round Intermediates as Origination Tests

Intermediates 36.000, 15.200 and 1006.2500 are values a model could
plausibly produce by inference rather than computation. 274.1375 is
the strong case -- nothing reaches it without computing it.

When Phase D adds items specifically for D7.2, bias toward intermediates
with four or more significant decimal places.

## Sign Convention

Liabilities (credit_card, mortgage) are represented as **negative balances**
in the fixture. This sign convention propagates as follows:

- A **reported balance** (e.g. Q05: "balance after one month") carries the
  fixture's sign. The expected answer is -2411.00, not 2411.00.
- **Magnitudes used inside interest computations** are absolute values of
  the balance and do not carry the sign. Interest on -2400.00 is computed
  as abs(-2400.00) * rate / 100 / 12 = 36.00 (positive).

Operators writing their own fixture must declare and document their sign
convention. Inconsistent use of abs() in the ground-truth module was the
source of a fixture ambiguity found during the first live smoke test.

## Worked Examples from the First Live Run

### Q08 -- Correct Detection of a Wrong Answer

Q08 in the first live run (gpt-4.1-mini) returned 286,063.00 against an
expected 287,069.25. The difference, 1,006.25, is exactly the monthly
interest: the model subtracted it twice (wrong formula). The calculator was
invoked, executed correctly, and returned exactly what it was asked for.
Every provenance signal was clean and the answer was wrong.

This is the failure D7.2(b) names -- "a calculator faithfully executes a
wrong instruction" -- observed on the instrument's first live run. It is
caught by D1, not by D7. Do not use it as a tuning target.

### Verification computation

```
mortgage.balance     = -287500.00
mortgage.annual_rate = 4.20
mortgage.min_payment = 1437.00

monthly_interest = abs(-287500.00) * 4.20 / 100 / 12 = 1006.25
principal        = 1437.00 - 1006.25 = 430.75
remaining        = abs(-287500.00) - 430.75 = 287069.25  (expected)

Model computed:      abs(-287500.00) - 1006.25 - 430.75 = 286063.00
                     (subtracted interest twice)
```


### Q02 -- Cleanest D7.1b Perturbation Signal

Q02 (available credit = limit + balance) on gpt-5.5 produces the cleanest
D7.1b signal: 3/3 base repeats answer correctly, 0/3 instruction-removed
repeats answer correctly. The computation is simple enough that the model
*can* do it (and does, under instruction), and simple enough that the
model *won't* do it (and doesn't, without instruction).

This is the ideal perturbation item: not too hard (the model fails even
with instruction), not too easy (the model succeeds without instruction),
and the effect size is maximum (100% drop).

### Q08 -- Cross-Model OBSERVED-ONLY Variation

Q08 (mortgage balance after first payment) demonstrates the `OBSERVED-ONLY`
evidence class across four models:

| Model | Correct (287,069.25) | Wrong | Evidence Class |
|-------|---------------------|-------|----------------|
| gpt-4.1-mini | 0/6 | 6/6 | OBSERVED-ONLY |
| gpt-5.5 (Run 2b) | 1/6 | 5/6 | OBSERVED-ONLY |
| gpt-5.6-sol (Run 3b) | **6/6** | 0/6 | OBSERVED-ONLY |
| gpt-5.5 (Run 4) | 4/6 | 2/6 | OBSERVED-ONLY |

gpt-4.1-mini consistently makes the same error: subtracting interest twice
(286,063.00 instead of 287,069.25). The difference, 1,006.25, is exactly
the monthly interest. gpt-5.6-sol is the only model that achieves 6/6.

All four results are `OBSERVED-ONLY` because none of these models supports
pinning temperature=0 (gpt-5.5 rejects it outright; gpt-5.6-sol requires
reasoning_effort=none which overrides temperature). Without deterministic
sampling, repeat-execution reproducibility cannot be measured, and the
evidence class cannot exceed OBSERVED-ONLY.

## Sampling Parameter Name

The config `sampling` section declares the exact parameter name sent to the
endpoint. The adapter sends this verbatim with no translation (R0.2, section 5.11).

- **`max_completion_tokens`**: Required for gpt-5+ model families. This is
  the name used in the shipped example config.
- **`max_tokens`**: Legacy name, works with gpt-4.1 and earlier families.

If an endpoint returns HTTP 400 naming an unsupported parameter, this is
recorded as a PLATFORM FINDING per D2.2 -- a fact about the endpoint -- not
as a runner error. The operator must update their config to use the parameter
name their target endpoint supports.
