# AP-1 v1.3 — Implementation Comment-Window Items

> Findings identified during runner implementation that belong in the AP-1
> comment window (disposition record) rather than in the runner itself. Filed
> here so they are not lost before the formal comment is submitted.

---

## D7.2(a) — Within-Context Transposition

An operand that matches a delivered source field resolves as GROUNDED even
where the reference derivation expected a different field. This is correct:
D7.2(a) measures whether operands trace to source, not whether the correct
field was selected. The wrong-field case is a D7.2(b) WRONG-OPERATION
finding.

The standard does not state this explicitly and an implementer will have to
derive it.

**Runner behaviour:** `resolve_operand` matches at step 1 (source field
match) regardless of which field name the reference derivation used. The
wrong-field case is caught by `check_operation_correctness` under D7.2(b).

---

## D7.5 — Incomplete Bound Specification

The clause requires an exact bound for "any invocation figure" but supplies
only the zero-failure form ($k = 0$). For $k > 0$ the Beta quantile is needed
and is not specified in v1.3.

The runner implements $k = 0$ and declares the limitation: when $k > 0$, the
Clopper-Pearson interval is computed but the confidence bound is reported
with a caveat that the $k > 0$ form is an implementation choice, not a
standard-specified formula.

**Runner behaviour:** `accuracy.py` computes the Clopper-Pearson lower bound.
For $k = 0$, this reduces to $1 - \alpha^{1/n}$, which matches the standard.
For $k > 0$, the Beta quantile is used, and the report includes a note that
this form is not specified in v1.3.

---

## D7.2(a) and Sign Inversion

An operand equal to the arithmetic negation of a source value has a traceable
basis but does not match any resolution step, and falls to step 5 alongside
genuinely untraceable values. The standard classifies both identically.

Two mechanisms produce it. A fixture encoding direction inside a magnitude —
removable by representing magnitude and direction separately, consistent with
PDS4. And a system expressing subtraction as addition of a negative,
`a + (-b)` rather than `a - b` — which no fixture design removes, because the
source field is correctly positive.

Measured: in a 100-execution validation run against a restructured fixture
(positive magnitudes, explicit direction field), 8 of 476 operands resolved
at step 5, all 8 sign inversions of a positive source value, none
untraceable. The reference implementation records SIGN-INVERSION as a finding
alongside the outcome without altering the classification.

A standard measuring numerical admissibility should say whether sign
inversion warrants its own outcome. Adding one changes the ladder, which
under §0.4 makes a successor protocol, so it is raised as a proposal for
AP-2 rather than for v1.3.

Found by running the instrument. The fixture-convention mechanism was
identified first (524 of 530 step-5 operands in the original fixture);
the expression-style mechanism survived the fixture restructure and
constitutes the irreducible case.


---

## Fixture Revision Invalidates Prior Runs

§5.8 states that a question set is burned once run, but says nothing about
what a fixture revision does to prior results. Transcripts are not portable
across fixture revisions: a system that received a signed balance and
submitted a signed operand will score as originated when that transcript is
scored against a fixture declaring the unsigned magnitude. The transcript
reflects the context the system received, not the context the fixture now
declares.

Measured: the original fixture used negative balances for liabilities
(`credit_card.balance = "-2400.00"`). The restructured fixture uses positive
magnitudes (`balance = "2400.00"`, `direction = "liability"`). Attempting to
re-score the original transcripts against the restructured fixture produced
invalid figures because the resolver does not implement step 4 (computed in
session) and the operand values reflected the old sign convention.

An evaluation that revises its fixture must re-execute rather than re-score.
The standard should state this.

Found by attempting to re-score transcripts after a fixture restructure.

---

## D7.2(a) and Declared Constants

The five-step ladder has no place for a constant declared in the ground-truth
module — 12 for months, 3 for a quarter, 100 for percentage conversion, 1 as
the multiplicative identity in compound-interest form. Every such operand
would otherwise resolve at step 5 as originated, and in a 1000-execution run
288 of 818 originated operands were the constant 1 alone.

The reference implementation resolves them at step 1 as authoritative by
declaration. The standard should say whether that is correct, whether
constants warrant their own step, and whether the permitted set should be
bounded — an operator adding constants until a run passes is the failure
mode.

Found by running the instrument.
