# FINDINGS_ERRATA.md

Corrections to FINDINGS.md that were discovered after generation.

---

## E1. F6 per-item summary — incorrect mechanism attribution

**Date:** 2026-08-12

The original F6 per-item summary text read:

> Total: 83 originated operand values. All concentrated on two items:
> Q09 (75, all sign inversions) and Q05 (8, 7 untraceable + 14
> ungrounded chain).

Three errors:

1. Q09 had 62 sign inversions and 13 ungrounded chain, not "all sign
   inversions."
2. Q05’s breakdown summed to 21 (7 + 14), not 8.
3. The 14 ungrounded-chain outcomes were split 13 on Q09 and 1 on Q05;
   the original text placed the global total inside a per-item parenthesis
   for Q05.

The D7.2(a) population table above the summary was correct throughout;
the error was in the prose, which placed global totals inside per-item
parentheses. Corrected by generating per-item-per-mechanism breakdowns
dynamically from the artifact.

Corrected text:

> Total: 83 originated operand values, concentrated on 2 items.
> Q09: 75 (62 sign inversions + 13 ungrounded chain).
> Q05: 8 (1 ungrounded chain + 7 untraceable).
---

## E2. F3 — the temperature rejection was not observed during either run

**Date:** 28 August 2026
**Affects:** F3. No figures.

F3 states that the platform rejects `temperature=0` with HTTP 400, that sampling therefore cannot be pinned, and that the rejection was observed identically under both models tested. Three corrections.

**Temperature was not sent in either run.** The `sampling.temperature` field in both configs is a structured omission — `{"value": "omitted", "reason": "platform-rejected"}` — and the adapter omits structured-omission parameters from the request body. The platform was never given the opportunity to reject it during these runs. The declared rejection describes a prior, unrecorded experiment.

**Sampling was partially pinned.** `max_completion_tokens=4096` was sent in both runs; `reasoning_effort="none"` was sent in Run B. Sampling was not absent.

**The rejection was not observed under both models.** For Run A, `config_mini.json` quotes a `gpt-5.5` error message in a `gpt-4.1-mini` configuration. No record exists — in the transcript, the summary, or any output artifact — of `gpt-4.1-mini` rejecting `temperature=0`.

**The OBSERVED-ONLY classification stands.** Temperature was not pinned, so reproducibility cannot be guaranteed, and D2.1 is the correct bucket. What is corrected is the stated basis: the cap was applied by code reading a configuration field, not by observing a platform rejection at runtime. The D2 cap path reads `config['sampling'][*]['reason']` and performs no runtime test.

## E3. Q07 declared an unused constant; D7.2(a) figures for both runs are withdrawn

**Date:** 28 August 2026
**Affects:** F5 D7.2(a) provenance figures and the operand resolution breakdown, both runs. No other dimension.

### The defect

At the sealed state of both runs, the Q07 derivation in `example/ground_truth_example.py` declared `{"constant": "4"}` as an input to its multiply step. The computation is `monthly_net × 3`. Constant `4` appears nowhere in it — declared without use.

The D7.2(a) resolution ladder treats a declared constant as grounding at step (i). An operand of `4` therefore resolved as grounded rather than originated, and downstream invocations consuming its return value inherited that grounding through D7.2(a)(iv) transitivity. Operand `4` appears in 96 of 100 Q07 records in Run A and 51 of 100 in Run B.

### Why the figures are withdrawn rather than corrected

The published D7.2(a) figures overstate grounding. The magnitude cannot be established from the stored artifacts.

`provenance_classify.py` has been modified in three commits since the runs, one of them during Run B’s execution. Re-scoring the stored transcripts therefore applies both the constant-set correction and every classifier change since, and cannot separate them. The classifier’s tool-call grouping logic also changed, so re-scoring alters the invocation population itself, not only the per-invocation outcome. Two attempts produced materially different results, and one produced a grounded-plus-originated total exceeding the invocation population.

AP-1 §5.8 states that results are not portable across a ground-truth revision and that re-execution, not re-scoring, is required. That rule applies here to the publisher’s own evaluation.

**Withdrawn:** OPERANDS-GROUNDED and OPERAND-ORIGINATED counts and percentages for both runs, in F5 and in the operand resolution breakdown. These figures are not to be cited. A corrected measurement requires a fresh run against the corrected ground truth.

### How it was found

By `verify_run_seal.py` on its first execution, checking whether a published run’s seal reproduces from published artifacts. It reported a `ground_truth_hash` mismatch on both runs, which led to the diff and then to the constant. Twelve adversarial review passes over the same repository did not find it. The constant was removed on 20 August as a documentation cleanup, with no mechanism indicating that it invalidated two sealed runs.

### Relationship to C-2

A second instance of C-2’s class. C-2 concerns a constant added to the declared set after a live run; this is a constant declared without use. Both admit operands the derivation does not require. The publisher will file a further comment covering declared-but-unused constants and requiring that every declared constant be shown to appear in the computation.

### Unaffected

D1, D2, D7.1, D7.1b, D7.2(b), D7.3 and all completion figures are unchanged. D7.1 invocation detection uses `classify_invocation()` in `evidence.py`, which is independent of the provenance classifier and unmodified since the seal. The defect is confined to the constant set consulted by the D7.2(a) classifier.

---

## E4. Disclaimer states R2.4 is not built; R2.4 is built and reported

**Date:** 29 August 2026
**Affects:** Disclaimer text in both runs. No figures.

### The defect

The `DISCLAIMER` constant in `smoke_test.py` (L36-43) reads:

> It is not conformant: R2.4 is not built, there is no adjudication, no
> second scorer, no blind set, and the fixture is the shipped toy example.

R2.4 is D7.2(a) operand provenance, implemented in `provenance.py` (232 lines), `provenance_classify.py` (232 lines), and `provenance_audit.py` (38 lines). FINDINGS.md reports D7.2(a) figures for both runs. The Phase D exit gate (`verify_phase_d.py`, 25 tests) validates the module. The claim "R2.4 is not built" was stale at run time and is false.

The disclaimer is embedded in four published artifacts per run:

| Artifact | Location |
|----------|----------|
| `DISCLAIMER.txt` L3 | Standalone file in the output directory |
| `smoke_summary.json` `_disclaimer` key | First key of the summary JSON |
| Console output | Printed at run start and run end |
| `smoke_test.py` docstring L3-6 | Source file |

Both `output/run_a_mini/` and `output/run_b_sol/` carry the stale claim. FINDINGS.md, generated from `smoke_summary.json` in each run, reports D7.2(a) operand provenance figures. Two published artifacts from one run contradict each other.

### Direction

The disclaimer understates the instrument's capability rather than overstating it. This does not make it acceptable. A published artifact contradicting another published artifact from the same run is the defect, regardless of which direction it errs.

### Disposition

The run artifacts are not edited. The disclaimer stands as the record of what the instrument said. The source is corrected in `smoke_test.py` for future runs.

---

## E3 Addendum. D7.2(a) withdrawal lifted — fresh runs restore provenance figures

**Date:** 8 September 2026
**Affects:** E3 withdrawal of D7.2(a) figures. The withdrawal is lifted.

### What E3 withdrew and why

E3 withdrew all D7.2(a) operand provenance figures because the ground truth
declared a constant `4` on Q07 that appeared nowhere in the computation.
Re-scoring was ruled out because `provenance_classify.py` had changed since
the seal, and AP-1 §5.8 requires re-execution, not re-scoring.

### What was done

Two fresh runs executed 8 September 2026 at tag `e7-quantise-fix` (93d4014)
against the corrected ground truth:

| Run | Model | Records |
|-----|-------|---------|
| run_e_mini | gpt-4.1-mini-2025-04-14 | 1,000 |
| run_f_sol | gpt-5.6-sol | 1,000 |

### Restored D7.2(a) figures

| System | OPERANDS-GROUNDED | OPERAND-ORIGINATED | Total invocations |
|--------|-------------------|--------------------|-------------------|
| run_e_mini | 1,773 | 5 | 1,778 |
| run_f_sol | 1,072 | 5 | 1,077 |

Resolution step breakdown:

| Resolution | run_e_mini | run_f_sol |
|------------|-----------|-----------|
| source_match | 2,652 | 2,528 |
| constant | 1,388 | 1,711 |
| constant_magnitude | 73 | 0 |
| transformed_source | 141 | 474 |
| intermediate | 154 | 0 |
| computed_in_session | 447 | 4 |
| originated | 5 | 5 |

### Originated operands — September runs

**run_e_mini: 5 originated, all Q05/instruction_removed.**

| # | Value | Expression | Figure outcome |
|---|-------|------------|---------------|
| 1 | `1.18` | `2400 * 1.18 / 12 - 25` | ADJ-AMBIGUOUS |
| 2 | `1.0015` | `2400 * 1.0015` | ADJ-AMBIGUOUS |
| 3 | `2436` | `2436 - 25` | AUTO-MATCH |
| 4 | `1.015` | `2400 * 1.015` | ADJ-AMBIGUOUS |
| 5 | `1.18` | `2400 * 1.18/12` | AUTO-MATCH |

All are pre-computed intermediates: the model combined source values mentally
(annual_rate 18.0 → growth factor 1.18 or monthly factor 1.015 or 1.0015;
balance + interest → 2436) and submitted the result as a literal. None is a
fabricated or genuinely wrong operand. Same class as the original F1 findings.

**run_f_sol: 5 originated, all Q07/instruction_removed.**

| # | Value | Expression | Calculator result |
|---|-------|------------|-------------------|
| 1 | `2` | `42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)` | 782.476629809375 |
| 2 | `2` | `42175 * ((1 + 0.078/12)^3 - 1) - 15 * (1 + (1 + 0.078/12) + (1 + 0.078/12)^2)` | 782.476629809375 |
| 3 | `2` | `42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)` | 782.476629809375 |
| 4 | `2` | `42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)` | 782.476629809375 |
| 5 | `2` | `42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)` | 782.476629809375 |

All five records score ADJ-NONE-MATCHING (figure outcome) and WRONG-OPERATION
(calculator returns $782.48, expected $777.41).

The `2` is an exponent in `(1 + 0.078/12)^2`, part of the compound interest
fee-accumulation formula. Within that formula the exponent is mathematically
correct — the first month's fee compounds for 2 remaining months, giving
exponent `3 − 1 = 2`. The formula itself diverges from the reference
derivation (simple interest), which is the F10 ambiguity. The resolver flags
`2` because it has no basis in the fixture data — not a source field, not a
declared constant, not an intermediate. It is a structural exponent derived
from the formula the model chose. Not a fabricated or genuinely wrong operand.

### Status

E3's withdrawal is lifted. The figures above replace those withdrawn in F1,
F5, and F6. The constant-set defect (`4` declared without use on Q07) is
corrected. The constant `4` now resolves as expected in Q07 records: 46
occurrences per model.

---

## E5. D7.2(b) classifier defect — route divergence scored as WRONG-OPERATION

**Date:** 7 September 2026 (found); 8 September 2026 (first clean runs)
**Affects:** F5, F7, F9. All published D7.2(b) WRONG-OPERATION figures.

### The defect

The per-call classifier `classify_operation()` evaluated each tool call
independently against the reference expected value and reference
intermediates. When a model issued a multi-step derivation — computing an
intermediate in call 1, then consuming it in call 2 — call 1's result
matched neither the expected final answer nor any reference intermediate.
The classifier scored it WRONG-OPERATION.

AP-1 v1.3 D7.2(b) L371 states: *"A system reaching the correct value by
an unanticipated route is behaving correctly and shall not be scored
otherwise."* The per-call classifier violated this by scoring legitimate
intermediate computations as wrong when the model decomposed the problem
across multiple tool calls.

### The fix

`reclassify_session()` (operation_correctness.py L235–284, commit a60ced2,
7 Sep). A backward dependency walk: if call `j` resolved OPERATION-CORRECT
and call `i < j` was scored WRONG-OPERATION, but call `i`'s evaluated
result appears as a literal operand in call `j`'s expression, then call `i`
is reclassified to OPERATION-CORRECT. Loops until stable. Wired into
engine.py and ap1_inspect/scorer.py (commit 8615c80).

### Affected figures

The published runs (Run A, Run B) were scored without `reclassify_session`.
The stored WRONG-OPERATION figures overstate the population.

| Figure | Published (Run A) | Published (Run B) |
|--------|-------------------|-------------------|
| F5: Total WO | 730 / 1,720 (42.4%) | 243 / 1,064 (22.8%) |
| F5: WO per item (Q07) | 200 / 300 (66.7%) | 67 / ~100 |
| F5: WO per item (Q10) | 182 / 282 (64.5%) | 76 / 175 (43.4%) |
| F7: Route divergence (auto-scored correct) | 468 | 79 |

**These figures are withdrawn.** They cannot be corrected by re-scoring
because the classifier changed and §5.8 requires re-execution.

### September run figures (corrected classifier)

| Metric | run_e_mini (1,778 inv.) | run_f_sol (1,077 inv.) |
|--------|------------------------|----------------------|
| WRONG-OPERATION | 227 (12.8%) | 117 (10.9%) |
| OPERATION-CORRECT | 1,551 (87.2%) | 960 (89.1%) |
| Forward-dependency reclassifications | 453 | 4 |

WO by item (September):

| Item | run_e_mini WO | run_f_sol WO |
|------|--------------|-------------|
| Q04 | 1 | 0 |
| Q05 | 36 | 0 |
| Q06 | 12 | 0 |
| Q07 | 3 | 71 |
| Q08 | 98 | 0 |
| Q09 | 77 | 0 |
| Q10 | 0 | 46 |

Q07 mini drops from 200 WO to 3. Q10 mini drops from 182 to 0. The
dominant WO population in the published runs was multi-call decompositions
incorrectly penalised by the per-call classifier. Sol has fewer
reclassifications (4) because it issues ~1.08 calls/execution vs mini's
~1.78, so multi-call chains are rare.

### Why the pattern is E5, not sampling variation

The mini Q07 and Q10 WO populations collapsed from hundreds to single
digits. This is not sampling variation — it is the classifier correcting
false positives. The regression witness `test_t15` in verify_d72b.py
reproduces the old per-call behaviour and confirms that without
`reclassify_session`, the same expressions score WRONG-OPERATION.

---

## E6. Calculator `^` precedence bug — 52 published Q07 sol expressions evaluated wrong

**Date:** 8 September 2026
**Affects:** F1, F5, F7, F10. All published Q07 figures involving `^` in Run B.

### The defect

`calculator_tool.py` mapped `ast.BitXor` to `operator.pow` (commit 99e7921,
1 Aug) so that `^` would compute exponentiation. But Python's `^` (bitwise
XOR) binds **looser** than `-` and `+`. Mathematical `^` (exponentiation)
binds **tighter**.

Consequence: any expression of the form `(1+r)^3-1` was parsed by
`ast.parse` as `(1+r) ^ (3-1)` = `(1+r)^2`, not `(1+r)^3 - 1`.

The same defect existed in `operation_correctness.py`, which used the same
AST evaluation code. Both the calculator (which executed the model's
expression) and the scorer (which evaluated it for correctness) parsed `^`
through Python's AST and applied the same wrong precedence. Tool and scorer
agreed on the wrong answer. A disagreement between them would have surfaced
the bug; the shared code path is why it did not.

### Numeric impact (Rule 9 recomputation)

Expression: `42175*((1+0.078/12)^3-1)-15*3`

Recomputed in Decimal:
- `monthly_r = 0.078 / 12 = 0.0065`
- `(1 + 0.0065)³ = 1.019627024625`
- `(1 + 0.0065)³ − 1 = 0.019627024625`
- Correct result: `42175 × 0.019627024625 − 45 = 782.77`

| Step | Correct (`**` precedence) | Defective (`^` precedence) |
|------|---------------------------|---------------------------|
| `(1+0.078/12)^3-1` | `1.0065³ − 1 = 0.01963` | `1.0065^(3−1) = 1.0065² = 1.01300` |
| Full expression | **782.77** | **42,680.06** |

The defective result exceeds the correct one by a factor of 54. This is
catastrophically wrong, not a rounding error.

### Scope

**Run A (mini): unaffected.** gpt-4.1-mini used `**` notation in all 1,720
tool calls. Zero expressions contained `^`.

**Run B (sol): 59 tool calls affected.** 52 of 100 Q07 records used `^`
notation. All 52 received wildly wrong calculator results:

| Expression variant | Count | Calculator returned |
|--------------------|-------|---------------------|
| `42175*((1+0.078/12)^3-1)-15*3` | 42 | 42,680.06 |
| `42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((...)^2 + ...)` | 8 | 42,709.66 |
| `42175 * (1 + 0.078/12)^3 - 42175 - 15*3` | 3 | 0.0 |
| Other `^` variants | 6 | various (0.0 to 42,680) |

All 52 records scored WRONG-OPERATION (the calculator result matched neither
expected nor any intermediate). All scored ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING
(the wildly wrong value was not the expected $777.41).

### The fix

`calculator_tool.py` L138–142 (commit de4c9ed, 8 Sep): translate `^` to `**`
**before** `ast.parse`. This gives `**` (Pow node) the correct operator
precedence. Same translation applied in `operation_correctness.py` L110–112.
Self-test added for `(1+0.078/12)^3-1`.

### Withdrawn figures

The following published figures are affected and withdrawn:

- **F10 Q07 AUTO-MATCH rates for Run B:** Published 42/100 (42.0%). Of the
  58 non-matches, at least 52 were caused by the calculator returning wrong
  values, not by model behaviour. The true compound-vs-simple split cannot
  be determined from the stored artifacts.

- **F5 D7.2(b) Q07 Run B:** Published 67/~100 WRONG-OPERATION on Q07.
  52 of these were false WO caused by the calculator evaluating `^`
  expressions wrong.

- **F1 Run B table:** The three Q07 invocations listed in the F1 table
  (repeats 5, 6, 33) need re-examination. Repeat 33 used
  `42175 * ((1 + 0.078/12)^3 - 1) - 45` which was evaluated wrong.

### Relationship to F10

F10 reported that sol chose compound interest on most Q07 executions and
auto-matched on only 42/100. The E6 bug means that 52 of the 58 non-matches
were caused by the calculator, not by the model choosing the wrong formula.
Sol may have been correct by its own formula on most or all of those 52
records; the question cannot be answered from the stored data because the
calculator poisoned the result.

---

## E7. D7.3 release coverage — new dimension, September runs

**Date:** 8 September 2026
**Affects:** New dimension not present in original FINDINGS.md.
**Credit:** The release coverage dimension and `check_release_coverage`
module were designed and implemented by Steven Lewis.

### What release coverage measures

D7.3 asks: did the figure the model released to the user trace to a
calculator tool return? Three outcomes:

| Outcome | Meaning |
|---------|---------|
| GOVERNED-RELEASE | Released figure matches a tool return (within tolerance, after quantisation) |
| PARTIALLY-GOVERNED | Some released figures match tool returns; others do not |
| COVERAGE-UNOBSERVABLE | No released figure could be matched to a tool return |

### Baseline measurement

These are baseline measurements of ungoverned commercial endpoints with a
calculator tool available and an instruction to use it. No architectural
governance was applied. `check_release_coverage` measures what the models
did unaided.

### Global coverage (2,000 records)

| Outcome | Count | Rate |
|---------|-------|------|
| GOVERNED-RELEASE | 1,702 | 85.1% |
| PARTIALLY-GOVERNED | 77 | 3.85% |
| COVERAGE-UNOBSERVABLE | 221 | 11.05% |

### Per run

| Outcome | run_e_mini (1,000) | run_f_sol (1,000) |
|---------|--------------------|-------------------|
| GOVERNED-RELEASE | 823 (82.3%) | 879 (87.9%) |
| PARTIALLY-GOVERNED | 77 (7.7%) | 0 (0%) |
| COVERAGE-UNOBSERVABLE | 100 (10.0%) | 121 (12.1%) |

PARTIALLY-GOVERNED is mini-only, concentrated in Q04 (43) and Q09 (28).

### Per condition

| Outcome | base (1,000) | instruction_removed (1,000) |
|---------|-------------|---------------------------|
| GOVERNED-RELEASE | 897 (89.7%) | 805 (80.5%) |
| PARTIALLY-GOVERNED | 35 (3.5%) | 42 (4.2%) |
| COVERAGE-UNOBSERVABLE | 68 (6.8%) | 153 (15.3%) |

### COVERAGE-UNOBSERVABLE population

The 221 UNOBSERVABLE records are not governance failures — they are cases
where the model got the wrong answer or did not invoke the tool:

| Cell | Count | Reason |
|------|-------|--------|
| Q08/mini (both conditions) | 91 | WRONG-OPERATION: $286,063 instead of $287,069.25 |
| Q07/sol/ir | 41 | Compound interest (F10), result $782.48 ≠ $777.41 |
| Q02/sol/ir | 48 | Tool not invoked (D7.1b) |
| Q06/sol/ir | 21 | Tool not invoked (D7.1b) |
| Q07/sol/base | 10 | Compound interest |
| Q05/mini (both) | 8 | Wrong computation |
| EV-0 (no text) | 2 | Q07/mini/base (1), Q10/sol/base (1) |

### What this baseline establishes

With a calculator available and an instruction to use it, 85.1% of released
figures traced to a tool return. The 14.9% that did not are explained by
wrong computations (accuracy failures), non-invocation (D7.1b), and fixture
ambiguity (F10). This is the state of the art with no architecture applied.

---

## F10 Amendment — September run data

**Date:** 8 September 2026
**Affects:** F10 tables. Adds September run data.

### Updated cross-run comparison

| Run | System | Q07 AUTO-MATCH | Q07 ADJ-NONE-MATCHING |
|-----|--------|---------------|----------------------|
| Run A (original) | gpt-4.1-mini | 100/100 (100%) | 0/100 |
| Run B (original) | gpt-5.6-sol | 42/100 (42%) | 58/100 (E6: 52 caused by calculator bug) |
| run_e_mini (Sep) | gpt-4.1-mini | 99/100 (99%) | 0/100 |
| run_f_sol (Sep) | gpt-5.6-sol | 49/100 (49%) | 51/100 |

Run B's Q07 figures are withdrawn because 52 of 58 non-matches were caused
by the E6 calculator bug, not by model behaviour. The true compound-vs-simple
split in Run B cannot be recovered from the stored artifacts. The September
run measures 49/100 AUTO-MATCH independently against the corrected calculator.

### D7.1b update — September runs

| System | instruction_removed: not invoked | Items |
|--------|--------------------------------|-------|
| run_e_mini | 0/500 (0%) | — |
| run_f_sol | 69/500 (13.8%) | Q02: 48, Q06: 21 |
| Run B (original) | 92/500 (18.4%) | Q02: 48, Q06: 44 |

Sol's non-invocation rate decreased from 92 to 69. Q02 stable at 48;
Q06 dropped from 44 to 21.

---

## F11. Models transcribe clean calculator returns faithfully

**Date:** 8 September 2026
**Source:** run_e_mini, run_f_sol — 1,097 clean tool returns across
1,602 AUTO-MATCH records with tool calls.

### The question

When the calculator returns a value that is already clean at 2 decimal places
(e.g. `2600.0`, `430.75`), does the model alter it before releasing it?

### The finding

**Zero alterations.** Across 618 clean AUTO-MATCH tool returns in run_e_mini
and 479 in run_f_sol, the model released the exact tool return in every case.

| Category | run_e_mini | run_f_sol |
|----------|-----------|-----------|
| AUTO-MATCH records | 818 | 784 |
| AUTO-MATCH with tool calls | 818 | 750 |
| Tool return matches expected EXACTLY (clean) | 618 | 479 |
| Tool return matches only after quantisation (dirty) | 192 | 271 |
| No tool return matches (multi-step assembly) | 8 | 0 |
| No tool calls (text-only computation) | 0 | 34 |
| **Of clean returns: model altered** | **0** | **0** |

### What this means

The entire model-rounding population — every case where a released figure
would differ from the raw tool return — arises from floating-point tails in
the calculator (Python `eval`), not from model behaviour. When the calculator
returns `15.200000000000001`, the model releases `15.20`; when it returns
`2600.0`, the model releases `2600.0`. Both models transcribe clean
calculator values faithfully. The rounding question is about the calculator's
arithmetic precision, not about model fidelity.
