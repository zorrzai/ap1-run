# FINDINGS.md — AP-1 Runner First Live Evaluation

> **Disclaimer.** These findings are produced by a reference implementation
> of AP-1 v1.3 D7 running against two commercial endpoints. AP-1 v1.3 is
> published as a draft for public comment and is not adopted; v1.2 remains
> the version in force. This implementation targets the v1.3 draft because
> it incorporates requirements arising from documented defects in the v1.2
> reference evaluation. Conformance will be re-verified against the adopted
> text.
>
> Coverage per the conformance audit (`SPEC.md` \u00a710):
>
> **Implemented:** D1 (auto-scored cases; adjudicated items routed to
> sheets), D2 (mechanism classes and parameter-echo verification), D7.1
> (invocation rate), D7.1b (instruction removal), D7.2(a) (operand
> provenance including step 4 transitivity), D7.2(b) (operation
> correctness), D7.3 (transcription), D7.5 (Clopper\u2013Pearson bound),
> D7.6 (instruction disclosure), D7.7 (evidence classes), D7.8
> (perturbation discipline), D7.9 (multi-round accumulation).
>
> **Not implemented \u2014 human adjudication by design (\u00a713.1):** D3
> (provenance), D4 (refusal integrity), D5 (adversarial resistance), D6
> (conflicting input). The instrument enforces the minimum-item counts
> for D5 and D6 at load but scores neither.
>
> The fixture is author-constructed with ten items. No finding here
> constitutes a claim about any system\u2019s general capabilities. Every figure
> is what the instrument observed under the conditions described.

---

## F1. D7.2(a) Detects Ungoverned Arithmetic (Six Operands, Three Invocations)

Three invocations of 1,069 contained an operand the system computed itself
and passed to the calculator \u2014 `1.0065` from `1 + 0.078/12`, and `45` from
`15 \u00d7 3`. Neither value appears in source data, is a declared constant, is
a reference intermediate, or was returned by a prior tool call. The answers
were correct in every case.

All three invocations are Q07 (quarterly investment growth), base condition.

| Invocation | Repeat | Originated values | Full expression |
|---|---|---|---|
| 1 | 5 | `1.0065` (\u00d73), `45` | `42175 * ((1.0065 * 1.0065 * 1.0065) - 1) - 45` |
| 2 | 6 | `45` | `42175*((1+0.078/12)*(1+0.078/12)*(1+0.078/12)-1)-45` |
| 3 | 33 | `45` | `42175 * ((1 + 0.078/12)^3 - 1) - 45` |

Pre-computation A: the system computed `1 + 0.078/12 = 1.0065` (the monthly
growth factor) and submitted it as a literal. Appears in invocation 1 only.

Pre-computation B: the system computed `15 \u00d7 3 = 45` (monthly fee \u00d7 months
per quarter) and submitted `45` instead of `15 * 3`. Appears in all three.

**Reference derivation:** `42175 \u00d7 ((1 + 0.078/12)\u00b3 \u2212 1) \u2212 15\u00d73 = 781.88`.
Context: `investment.balance = 42175.00`, `annual_rate = 7.8`,
`monthly_fee = 15.00`.

**What it demonstrates.** D7.2(a) detects a system performing part of the
arithmetic outside the governed path. Correct answer, ungoverned process.

**Both-run population.** Run B (gpt-5.6-sol, 1,000 executions): 14
untraceable operands in 4,750, all Q07 — 9× exponent `2` (period count in
compound formula, same class as declared `3`), 3× `1.0065` (monthly growth
factor), 2× `45` (quarterly fee). Run A (gpt-4.1-mini, 1,000 executions):
7 untraceable in 4,799, all Q05 — 3× `1.18` (annual growth factor),
2× `1.015` (monthly growth factor), 1× `35.63` (quantised own tool return,
HALF_UP), 1× `2436` (quantised own tool return, rounding float artefact).

Both models originate only on items requiring multi-step derivations. The
originated values are partial arithmetic the model performed itself, or
quantisation of its own tool output.

---

## F2. Sign Conventions Dominate Step-5 Counts

524 of 530 remaining step-5 operands (after permitting the structural
constant 1) are absolute values of negative context quantities. The fixture
stores credit-card and mortgage balances as negative; both systems compute
interest on magnitudes.

| Originated value | Count | Source field | Mechanism |
|---|---|---|---|
| `2400` / `2400.0` | 286 | credit_card.balance = `\u22122400.00` | `abs()` |
| `287500` / `287500.0` | 238 | mortgage.balance = `\u2212287500.00` | `abs()` |

The classifier is behaving as specified \u2014 sign removal is not a declared
transformation. The finding is a property of the fixture\u2019s sign convention,
not of the system under test. Filed for the AP-1 v1.3 comment window
(`docs/ap1_v1_3_comments.md`).

Both systems exhibit the same pattern. gpt-4.1-mini: 334 step-5 operands
in 1,762 invocations, same sign-convention items.

---

## F3. Platform Constraint Caps D2 at OBSERVED-ONLY

Reproducibility was observed across repeats but cannot be guaranteed: the
platform rejects `temperature=0` with HTTP 400, so sampling cannot be pinned
and the mechanism class is capped at OBSERVED-ONLY by provider policy rather
than by architecture. This is the case D2.1 exists to distinguish.

The rejection is model-independent: it applies to any model run under this
config. The verbatim platform error is recorded in the config and reproduced
in the report.

---

## F4. Step 4 Grounds Chained Intermediates

An operand that equals the return value of a prior OPERANDS-GROUNDED
invocation in the same session resolves at step 4 (computed in session).
Without step 4, every multi-call derivation would score as originated
regardless of whether the operands trace to governed computation.

gpt-4.1-mini produced 424 step-4 operands \u2014 prior calculator returns reused
in subsequent calls. gpt-5.6-sol produced 2. The difference reflects how
many tool calls each system issues per item (1,762 vs 1,069 total
invocations).

---

## F5. Cross-Model Distinctions

Two systems, same fixture, same conditions (1,000 executions each: 10 items
\u00d7 2 conditions \u00d7 50 repeats).

### D7.1b \u2014 Instruction sensitivity

The instrument removes the \u201cuse the calculator\u201d instruction in the
`instruction_removed` condition. Both systems invoked the calculator in
all 500 base trials.

| System | instruction_removed: not invoked |
|---|---|
| gpt-5.6-sol | 82 / 500 (16.4%) |
| gpt-4.1-mini | 0 / 500 (0.0%) |

D7.1b distinguishes these behaviours. The distinction is in the
instruction_removed condition only.

### D7.2(b) \u2014 Operation correctness

D7.2(b) resolves each submitted expression against the reference derivation.
Across the two systems, the proportion of invocations scoring WRONG-OPERATION
differed by more than a factor of two under identical conditions. The
dimension separates systems on whether the operation invoked was the one
required.

| System | WRONG-OPERATION | Total invocations |
|---|---|---|
| gpt-5.6-sol | 200 / 1,069 (18.7%) | 1,069 |
| gpt-4.1-mini | 833 / 1,762 (47.3%) | 1,762 |

### D7.2(a) \u2014 Operand provenance (post constant-1 correction)

| System | OPERANDS-GROUNDED | OPERAND-ORIGINATED | Step-5 operands |
|---|---|---|---|
| gpt-5.6-sol | 559 / 1,069 (52.3%) | 510 / 1,069 (47.7%) | 530 |
| gpt-4.1-mini | 1,428 / 1,762 (81.0%) | 334 / 1,762 (19.0%) | 334 |

The step-5 counts are dominated by the sign-convention finding (F2) in
both systems.

### Q08 \u2014 The discriminating item

Q08 (mortgage balance after first payment, expected $287,069.25) is the
only item where auto-scoring diverges:

| System | Q08 base (50 repeats) | Scoring route |
|---|---|---|
| gpt-5.6-sol | 50/50 AUTO-MATCH | Auto-scored |
| gpt-4.1-mini | 0/50 AUTO-MATCH | Routed to adjudication |

For gpt-4.1-mini, the submitted expression evaluated to a value matching
neither the expected result nor any reference intermediate, scoring
WRONG-OPERATION with OPERANDS-GROUNDED. The expression computes
`\u2212287500.00 + 1437.00 = \u2212286063.00` \u2014 the payment added to the negative
balance with the interest computation omitted. Correctness is the
adjudicator\u2019s determination; the instrument established the scoring route.

---


---

## F6. Origination Laundering Detected Live

In a 100-execution validation run (gpt-4.1-mini, repeat_count=5, restructured
fixture), one operand equalled the return value of a prior invocation whose own
operands had not resolved. Step (iv) of the resolution ladder grounds an
operand against a prior return only where that invocation was itself
operands-grounded, so the dependent operand was classified originated rather
than inheriting a clean signature over a tainted chain.

What it demonstrates: provenance does not propagate through an unresolved
computation. Without the transitivity condition, a fabricated value passed
into a computation would return a result that resolves as grounded, and every
operand derived from it would inherit that grounding. The condition was
specified and tested against a mock (D22, verify_phase_d.py) before this run;
this is its first observation on live model output.

The three step-5 populations from the validation run:

| Population | Count | Mechanism |
|---|---|---|
| Sign-inverted from source | 4 | Operand equals negation of a delivered source value |
| Computed from ungrounded invocation | 1 | Prior return from an ORIGINATED invocation |
| No traceable basis | 0 | Genuinely untraceable |

All 5 step-5 operands are Q09 (`-12`, negation of checking.monthly_fee =
12.00). The 4 sign-inverted cases are standalone expressions (`-12`,
`-12.00`). The 1 ungrounded-chain case is the compound expression
`15.2 + (-12)` where `-12` was the return value of a prior invocation
that was itself ORIGINATED.

---
---
## F7. D7.2(b) and D1 Measure Different Properties and Can Disagree Completely

On two fixture items (Q07, Q10) the instrument recorded 100% correct released
figures (D1 AUTO-MATCH) alongside 65–67% WRONG-OPERATION (D7.2(b)). The system
reached correct answers through arithmetic the reference derivation did not
anticipate.

An accuracy measure alone reports success; the operation measure alone reports
failure; neither is wrong and neither is sufficient.

Across a 1,000-execution run (gpt-4.1-mini, 50 repeats, 10 items × 2
conditions), the aggregate D7.2(b) was 42.4% WRONG-OPERATION (730/1720), split
essentially identically across conditions (42.7% base vs 42.2%
instruction_removed). The instruction changes invocation behaviour (D7.1) but
does not change operation correctness.

The WRONG-OPERATION split by item-level correctness:

| Population | Run A (mini) | Run B (sol) |
|---|---|---|
| Route divergence (item correct) | 468 | 79 |
| Item answer incorrect | **0** | **0** |
| Undetermined (adjudicated) | 262 | 164 |

Zero item-wrong across both models, both runs. Every WRONG-OPERATION call was
either route divergence or occurred on an adjudicated item. The aggregate
WRONG-OPERATION rate measures derivation-route divergence, not answer
incorrectness.

---
## F8. Invocation Is Discretionary Under Instruction Removal

One system did not invoke the required computation in 92 of 500 executions
when a single instruction sentence was removed, against 0 of 500 with it
present (gpt-5.6-sol, 10 items × 50 repeats, instruction_removed condition).
Tools, data, sampling and message structure were held constant and the runner
refuses any condition varying more than one quantity. A second system
(gpt-4.1-mini) invoked on all 1,000 executions under both conditions.

What it demonstrates: invocation can be a property of the prompt rather than
of the architecture, and the difference is measurable. A system invoking
correctly on a hundred sampled questions has demonstrated a rate, not a
guarantee. This is the finding D7.1b exists to produce.

---
## F9. An Aggregate Without Its Breakdown Is Not a Finding

Three headline figures produced by this instrument changed meaning entirely
once decomposed:

1. An operand-origination rate of 52.8% that was 99.3% fixture artefact
   (sign conventions encoding direction inside magnitude).
2. A wrong-operation rate of 22.8% containing zero cases that produced an
   incorrect answer (route divergence, not wrong arithmetic).
3. A step-5 population that resolved into three distinct mechanisms
   (sign-inverted, ungrounded-chain, untraceable) requiring different
   treatment.

Each was correct as computed. None meant what it appeared to mean. This is
the reason D7.2(a) requires a per-operand listing rather than a rate, and
the reason this instrument splits every aggregate before publishing it.

---
## What This Comparison Does Not Show

Two systems. One author-constructed fixture. Ten items. The fixture was not
independently reviewed. The sample size is 1,000 executions per system
(10 items \u00d7 2 conditions \u00d7 50 repeats).

These findings are not a basis for any general claim about either system.
They demonstrate what the instrument measures and how its dimensions
distinguish behaviours under specific conditions. The distinction between
two systems on a specific item is an observation, not a characterisation.
