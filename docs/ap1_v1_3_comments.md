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
