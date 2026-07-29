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
