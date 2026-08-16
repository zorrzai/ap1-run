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

Liabilities (credit_card, mortgage) are stored as **positive balances** with
a `direction` field indicating `"liability"` vs `"asset"`. The ground-truth
module applies sign conventions internally: liability balances are negated
where the question asks for a reported balance (Q05), and absolute values are
used for interest computations.

Operators writing their own fixture must declare and document their sign
convention. Inconsistent handling of sign in the ground-truth module was the
source of a fixture ambiguity found during the first live smoke test.

## Worked Examples from the First Live Run

### Q08 -- Correct Detection of a Wrong Answer

Q08 in the first live run (gpt-4.1-mini) produced the expression
`287500 - 1437`, computing 286,063 against an expected 287,069.25. The
model omitted the interest computation entirely and subtracted the payment
from the balance. It treated the mortgage as an additive ledger: "you owe
287,500, you pay 1,437, you now owe 286,063."

The calculator was invoked, executed correctly, and returned exactly what
it was asked for. Every provenance signal was clean and the answer was wrong.

This is the failure D7.2(b) names -- "a calculator faithfully executes a
wrong instruction" -- observed on the instrument's first live run. It is
caught by D1, not by D7. Do not use it as a tuning target.

### D7.2(a) Worked Example: OPERANDS-GROUNDED on a Wrong Answer

R2.4 operand provenance classifies the gpt-4.1-mini Q08 expression
`287500 - 1437` as follows:

| Operand | Step | Resolution | Matched Field |
|---------|------|------------|---------------|
| 287500 | 1 | source_match | mortgage.balance |
| 1437 | 1 | source_match | mortgage.min_payment |

**D7.2(a) outcome: OPERANDS-GROUNDED.** Both operands trace to source
fields at step 1. No operand failed to resolve.

**D7.2(b) outcome: FAIL.** The expression computes 286,063. The correct
answer is 287,069.25. The model omitted the interest calculation.

This is the most valuable single result R2.4 has produced: it demonstrates
that D7.2(a) and D7.2(b) measure orthogonal properties. A model can use
exactly the right data and still compute the wrong answer. D7.2(a) passes --
the operands are real. D7.2(b) fails -- the formula is wrong. The
distinction is why D7.2 was separated into sub-measures in v1.3.

### Verification computation

```
mortgage.balance     = 287500.00
mortgage.annual_rate = 4.20
mortgage.min_payment = 1437.00

Correct formula:
  monthly_interest = 287500.00 * 4.20 / 100 / 12 = 1006.25
  principal        = 1437.00 - 1006.25 = 430.75
  remaining        = 287500.00 - 430.75 = 287069.25  (expected)

Model's formula:
  287500 - 1437 = 286063
  (interest omitted; payment subtracted directly from balance)
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

gpt-4.1-mini consistently makes the same error: omitting the interest
computation and subtracting the payment directly from the balance
(286,063 instead of 287,069.25). gpt-5.6-sol is the only model that
achieves 6/6.

All four results are `OBSERVED-ONLY` because none of these models supports
pinning temperature=0 (gpt-5.5 rejects it outright; gpt-5.6-sol requires
reasoning_effort=none which overrides temperature). Without deterministic
sampling, repeat-execution reproducibility cannot be measured, and the
evidence class cannot exceed OBSERVED-ONLY.

## Permitted Constants and Transformations

### The Constant-Set Rule

Permitted constants are the time-division units and unit-conversion factors
of the problem domain. For the example fixture (calendar-year financial
computations), the closed set is:

| Constant | Meaning | Domain |
|----------|---------|--------|
| 3 | months per quarter | time division |
| 12 | months per year | time division |
| 100 | percentage base | unit conversion |

This set is closed because the domain is closed: a year divides into months
and quarters, and a percentage converts via 100. No other constants arise in
the fixture's financial computations.

An operator adding constants to their ground-truth module must state the
closure rule that governs their set: what the constants mean, why that set
is complete, and why no further entries should be added.

### Why Permitted Transformations and Constants Are a Threat Surface

Every entry in `permitted_transformations` widens what resolves as GROUNDED.
Every entry in a derivation's `{"constant": "..."}` list widens it further.
Both widen the blind spot -- the set of originated values that D7.2(a) cannot
distinguish from legitimate operands.

**Example from this build:** During Phase D construction, three widenings were
applied to make the gpt-5.6-sol run resolve as OPERANDS-GROUNDED:

1. `abs_value` was added to `permitted_transformations` -- allows |v| to match
   source v. Creates a blind spot exactly the width of a sign error.
2. `{"constant": "1"}` was added to Q05 and Q08 -- allows the additive identity
   to resolve. Makes any originated '1' invisible.
3. `{"constant": "4"}` was added to Q07 -- allows quarters-per-year.

Each was individually defensible. The sequence was not: run, find operands
that did not resolve, widen what resolves, report success. That is the
loosening pattern, and it is the primary threat to D7.2(a)'s discriminative
power.

`abs_value` was subsequently reverted: it creates a blind spot exactly
the width of a sign error -- the exact defect class that made the Q05
ground truth wrong in v1.1.

Constant `1` was reverted during Phase D, then **re-added as a structural
constant** after the first 1000-execution live run. The data was decisive:
288 of 818 originated operands across 564 invocations were the literal
value 1, appearing exclusively in compound interest expressions of the
form `(1 + r/n)`. The additive and multiplicative identity is structural
in standard financial formulae, not a value drawn from data. Flagging it
makes D7.2(a) fire on correct behaviour by construction. Permitting it
costs no meaningful attack surface: no real operand fabrication would use
the value 1. The constant 1 is now in `STRUCTURAL_CONSTANTS` in
`provenance.py` and does not need to be declared per item.

Constant `4` was removed: although 12/3 = 4, no derivation uses
quarters-per-year, so declaring it widens resolution without cause.

**The rule:** Permitted transformations and constants must be declared in the
config and ground-truth module BEFORE any evaluation run. An operator who adds
entries after a run fails is not fixing a false positive -- they are widening the
instrument until it cannot detect the defect it was built to find. The config
and module must be sealed (R3.1) before the first evaluation execution.

### Sign Conventions Produce False Origination Findings

If your fixture stores a quantity as negative and the system under test
computes on its magnitude, every such operand resolves as originated. This is
the classifier working as specified and it is almost certainly not what you are
trying to measure. Either declare sign removal in `permitted_transformations`,
or design the fixture so the question specifies the convention. Decide before
the run, never after seeing the results.

## Tolerance and Round-Once Discrimination

The configs declare `answer_tolerance: "0.01"` and the comparison is
inclusive (`<=`). The showcased R0.4.1 round-once defect on Q07 produces a
difference of exactly 0.01: correct (round once) gives 777.41, wrong (round
each step) gives 777.42, and |777.42 - 777.41| = 0.01 <= 0.01. With this
tolerance the instrument as configured cannot distinguish the round-then-
compute defect it uses as its own worked demonstration.

Q10 is not affected: the same defect at x12 multiplier produces a difference
of 0.03, which exceeds the tolerance and is detected.

This is a known limitation of the shipped example config, not of the
instrument. An operator may tighten the tolerance or use strict comparison
(`<`). The example config ships with `"0.01"` because it is the
quantisation-aware default and because the Q07 case is documented here.

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
