# AP-1 v1.3 — Publisher’s Comment

**Filed by the publisher into the comment record for AP-1 v1.3**
**ZORRZ Financial Inc. · 5 August 2026**

---

## Status of this document

AP-1 v1.3 is published as a draft for public comment. The comment window closes **30 September 2026**. Under §10.5.1, every substantive comment is dispositioned in public — accepted, rejected or deferred, with reasoning — before adoption.

**This is a comment filed by the publisher.** It records defects and omissions identified in v1.3 after publication, by the author, through applying the standard rather than reading it. Each is stated here for disposition alongside comments received from others, and each is resolved in **v1.4** after the window closes.

**v1.3 is not edited.** §0.4 states that prior versions remain permanently citable and are not silently altered. A published version whose text changes after deposit is not a version.

Comments C-1 through C-8 and C-10 arise from constructing and executing the reference implementation. C-9 arises from a review of related work conducted on 5 August 2026.

---

## C-1 · D7.5 specifies a bound it does not supply

**Clause.** D7.5 requires that *“any invocation figure, including 100%, shall be reported with n and with the exact one-sided 95% upper confidence bound on the failure rate”*, then supplies `p_upper = 1 − α^(1/n)`.

**Defect.** That formula is the Clopper–Pearson bound at **zero** failures. The requirement is stated over *any* figure. For non-zero failure counts the bound requires the Beta quantile, which the clause does not specify.

**Effect.** An implementer must either compute a bound the standard does not define, or report none and be non-conformant on a literal reading.

**Proposed resolution for v1.4.** Restrict the requirement to zero-failure results, where the reported figure would otherwise be read as certainty, and state that non-zero counts are reported as a rate with n. Alternatively, specify the general Clopper–Pearson form. The first is preferred: the clause exists to prevent “100%” being read as impossibility, and that is the zero-failure case.

---

## C-2 · The resolution ladder has no place for declared constants

**Clause.** D7.2(a) step (i) covers *“a value present in the source data delivered for that item.”*

**Defect.** A constant declared in the ground-truth module — 12 for months in a year, 3 for a quarter, 100 for percentage conversion, 1 as the multiplicative identity in compound-interest form — is not in the delivered source data and matches no step. Every such operand resolves as originated.

**Evidence.** In a 1,000-execution run against the reference fixture, **288 of 818 step-5 operands were the constant 1 alone**, arising from the standard compound-interest form `(1 + r/n)`. The classification was correct under the clause and measured nothing about the system.

**Effect.** D7.2(a) fires on correct behaviour by construction wherever a domain formula contains a structural constant.

**Proposed resolution for v1.4.** Either extend step (i) to declared constants sealed alongside the fixture, or give constants their own step. The reference implementation resolves them at step 1 with a distinguishing resolution field, and declares this an interpretation rather than a requirement. The standard should also state whether the permitted constant set is bounded — an operator adding constants until a run passes is the failure mode.

---

## C-3 · Sign inversion has no outcome

**Clause.** D7.2(a) steps (i) through (v).

**Defect.** An operand equal to the arithmetic negation of a source value has a traceable basis but matches no step, and resolves at step (v) alongside genuinely untraceable values. The standard classifies both identically.

**Evidence.** Two mechanisms produce it, and only one is removable by fixture design.

A fixture encoding direction inside a magnitude — storing a liability as `-2400.00` — produces near-total false origination when a system computes interest on the magnitude. Observed: **524 of 530 step-5 operands** in a 1,000-execution run. Restructuring the fixture to represent magnitude and direction as separate fields removes it, consistent with how PDS4 represents quantities.

But a system expressing subtraction as addition of a negative — `15.2 + (−12)` rather than `15.2 − 12` — produces the same classification from a source field that is correctly positive. **No fixture design removes this.** Observed after restructuring: 62 operands across 1,000 executions.

**Proposed resolution for v1.4.** Sign inversion warrants its own outcome, distinguishing an operand with a traceable basis in the wrong form from one with no basis. Adding an outcome alters the ladder, which under §0.4 makes a successor protocol rather than a point release, so this is raised for AP-2 unless the comment period establishes that recording it as a finding alongside the existing outcome is sufficient. The reference implementation does the latter.

---

## C-4 · Step (iv) permits no quantisation where step (iii) does

**Clause.** D7.2(a) step (iii) grounds a reference intermediate *“quantised under the declared policy”*, recording a quantisation finding. Step (iv) requires exact equality with a prior invocation’s return value.

**Defect.** A system that receives `35.625` from a computation and submits `35.63` to the next call — standard commercial rounding — scores originated, indistinguishable from a fabricated value.

**Evidence.** Observed twice in a 1,000-execution run: `35.625` quantised HALF_UP to `35.63`, and `2435.9999999999995` rounded to `2436`.

**Proposed resolution for v1.4.** The asymmetry appears unintentional. Either step (iv) should permit a quantised prior return with a finding, matching step (iii), or the standard should state why the two are treated differently.

---

## C-5 · The declared constant set must anticipate alternative derivation routes

**Clause.** §11.9 and D7.2(a) step (iii).

**Defect.** A fixture author declares the constants their own reference derivation requires. A system reaching a correct answer by a different route may require constants the reference does not use.

**Evidence.** A system computing a quarterly figure by geometric series required the period index `2` in `(1+r)² + (1+r) + 1`. The reference derivation used simple multiplication by `3` and declared `3`. **Nine of fourteen untraceable operands** in one run were this single value.

**Proposed resolution for v1.4.** State that declared constants are the constants of the problem domain rather than of the reference derivation, and that a set anticipating only one derivation route will produce origination findings for valid alternatives.

---

## C-6 · D7.2(b) does not distinguish route divergence from wrong operation

**Clause.** D7.2(b) operation correctness.

**Defect.** The sub-measure resolves a submitted expression’s result against the expected value or a reference intermediate. For a multi-step derivation, a system taking a valid alternative route produces intermediates matching no reference intermediate, and every such call scores WRONG-OPERATION.

**Evidence.** On two fixture items, **100% of released figures were correct while 65–67% of invocations scored WRONG-OPERATION**. Across a 1,000-execution run the aggregate was 42.4%, essentially identical under both instruction conditions. Across two systems and 973 WRONG-OPERATION calls, **zero produced an incorrect released figure**.

**Effect.** The aggregate does not distinguish a system applying wrong arithmetic from one reaching a correct result by an unanticipated path. The second is not a defect.

**Proposed resolution for v1.4.** Either D7.2(b) gains an outcome for route divergence, or the standard states that it is meaningful only on the invocation producing the released figure. The reference implementation splits the reported outcome by whether the item’s released figure was correct.

---

## C-7 · Fixture revision invalidates prior transcripts, and §5.8 does not say so

**Clause.** §5.8 states that a question set is burned once run.

**Defect.** The standard is silent on what a fixture revision does to results already obtained. It is not the same as burning a set.

**Evidence.** Attempting to re-score stored transcripts against a revised fixture raised one system’s apparent origination rate from 19.0% to 38.2%. The systems had been given the earlier values in context and their expressions reflected what they received. The re-scoring measured the fixture revision, not the system.

**The distinction, which the standard should draw.** Transcripts are portable across **scoring** changes and not across **fixture** changes. A change to the declared constant set, the permitted transformations, or the ground-truth derivation alters how a stored response is scored, and re-analysis is valid. A change to the fixture alters what the system was given, and re-execution is required.

**Proposed resolution for v1.4.** Add the distinction to §5.8.

---

## C-8 · Sampling omissions require a reason

**Clause.** §5.11 requires sampling parameters to be reported per arm, including explicit omissions.

**Defect.** An omission reported without a reason is ambiguous between three cases with different consequences: the operator chose not to set it; the platform rejected it; nobody considered it. Only the second caps the D2 mechanism class.

**Evidence.** A frontier model rejects `temperature=0` and accepts only the default. Its D2 ceiling is therefore OBSERVED-ONLY by provider policy rather than by architecture. That is reportable only if the reason travels with the omission.

**Proposed resolution for v1.4.** Require a declared reason — operator-declared, platform-rejected, or platform-unsupported — and state that a platform rejection caps the D2 mechanism class with the cause reported.

---

## C-9 · Appendix B does not cite parameter-level provenance work

**Clause.** Appendix B, related work.

**Defect.** A body of work on parameter-level provenance in tool-using agents predates or closely follows v1.3 and is not cited.

- **Agent-Sentry** (arXiv:2603.22868) records a provenance graph capturing where every tool argument value came from, and learns the structural and provenance patterns of legitimate execution.
- **AuthGraph** (arXiv:2605.26497) states that it is *“the first agent security defense to structurally compare authorization specifications against execution provenance at the parameter-source level.”*
- **Auditing Provenance Sensitivity in LLM Agent Action Selection** (arXiv:2607.20827) opens on a premise adjacent to AP-1’s: *“evidence can be relevant without being authorized to determine a decision, so a correct action need not be grounded only in permitted evidence.”*
- **From Agent Traces to Trust** (arXiv:2606.04990) surveys the area and formalises parameter-level as a distinct tracing granularity.
- **FIDES** (arXiv:2505.23643), **CaMeL** (arXiv:2503.18813) and **NeuroTaint** (2026) apply information-flow control and taint tracking to constrain how untrusted data influences tool arguments.

**The distinction, which the citation must carry.** This work is **enforcement against untrusted sources**: a security threat model, applied at runtime, asking whether a value came from somewhere untrusted. D7.2(a) is **measurement of admissibility**: a provenance threat model, applied post-hoc, asking whether a value came from anywhere at all.

A figure the model fabricated passes every information-flow check, because taint propagates from origins and an invented number has none. The two are complementary and neither substitutes for the other — the same relationship v1.3 already draws with ToolGate.

**Also uncited and relevant.** ALUE (FAA and MITRE, 2025), the aerospace LLM evaluation benchmark; and the Trusted AI Framework (The Aerospace Corporation, adapted for space mission autonomy with JPL), the institutional AI assurance framework for that domain.

**Proposed resolution for v1.4.** Cite all of the above in Appendix B, with the enforcement-versus-measurement distinction stated explicitly rather than left for a reader to infer.

---

## C-10 · D7.2(a) does not distinguish a wrong source field from no source

**Clause.** D7.2(a) step (i) — *“a value present in the source data delivered for that item.”*

**Defect.** An operand that matches a delivered source field resolves as grounded even where the reference derivation required a different field. The clause asks whether the operand traces to source, and it does. It does not ask whether the correct source was selected.

**Effect.** A system reading `savings.balance` where the question required `checking.balance` scores OPERANDS-GROUNDED. The provenance signature is complete and the answer is wrong.

**Why this is arguably correct.** Field selection is an operation question, not a provenance question, and D7.2(b) is where it belongs. But the standard does not say so, and an implementer will have to derive it — as this one did.

**Evidence.** Distinguished in the reference implementation by testing a within-context transposition, which scores grounded, against an out-of-context value, which does not. Both were planted deliberately in the fault-injection suite for this reason.

**Proposed resolution for v1.4.** State explicitly that D7.2(a) measures whether an operand traces to source and not whether the correct source was selected, and that the wrong-field case is a D7.2(b) finding. Without it, two implementers will reasonably disagree about a common case.

---

## Note on origin

Comments C-1 through C-8 and C-10 were identified by building the reference implementation and executing it against live systems. None was anticipated when v1.3 was drafted. Each was found because the standard was applied rather than read.

C-9 was identified by a review of related work conducted after publication.

That these are the first entries in v1.3’s comment record is intentional. A standard whose author does not find defects in it has not applied it.

---

*Filed 5 August 2026 · Comment window closes 30 September 2026 · Resolution in AP-1 v1.4*
*ZORRZ Financial Inc. · mrupp@zorrz.com*
