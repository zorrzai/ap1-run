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

## D7.2(a) and Sign Conventions

Where a fixture represents liabilities as negative and a system computes
interest on magnitudes, every such operand resolves at step 5 as originated.
Observed at scale: 525 of 818 originated operands in a 1000-execution run,
across two systems, arising from seven unique values.

The classifier is behaving as specified — sign removal is not a declared
transformation. But the finding is a property of the fixture's sign
convention rather than of the system under test, and the standard offers no
guidance. Options: permit sign removal as a standard transformation; require
fixtures to declare a sign convention and questions to specify it; or leave
it to the operator's `permitted_transformations` with the risk that results
are not comparable across evaluations.

Found by running the instrument, not by reading the standard.


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
