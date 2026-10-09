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

---

## Corrections by addition - 3 October 2026

**Date:** 3 October 2026
**Affects:** Two counts in this file. No figure, verdict or withdrawal changes. The original lines are left as published and corrected here.

### C1. E3, line 62: Run B count is 51 occurrences in 49 records, not "51 of 100" records

E3 states: "Operand `4` appears in 96 of 100 Q07 records in Run A and 51 of 100 in Run B."

The Run A figure is correct: 96 records, 96 occurrences. The Run B figure counts occurrences as if they were records. Two Run B records each carry operand `4` twice.

| Run | Q07 invocation records | Records containing operand `4` | Occurrences |
|-----|------------------------|--------------------------------|-------------|
| Run A (`run_a_mini`) | 100 | 96 | 96 |
| Run B (`run_b_sol`) | 100 | **49** | 51 |

**Correction:** for "51 of 100 in Run B" read "49 of 100 in Run B (51 occurrences)".

Command, run from the repository root (counts invocation records only; `smoke_run.jsonl` interleaves invocation and figure-identification records):

```
python -c "import json; R=[json.loads(l) for l in open('output/run_b_sol/smoke_run.jsonl',encoding='utf-8')]; Q=[r for r in R if r.get('record_type')!='figure_identification' and r['item_id']=='Q07']; H=[sum(1 for p in r['provenance_results'] for o in p['operand_resolutions'] if o['operand_value']=='4') for r in Q]; print(len(Q), sum(h>0 for h in H), sum(H))"
```

Output: `100 49 51` (Q07 records, records containing `4`, occurrences). Replacing `run_b_sol` with `run_a_mini` gives `100 96 96`.

### C2. E7, COVERAGE-UNOBSERVABLE table: the sol EV-0 record is Q08, not Q10

The E7 row reads: `EV-0 (no text) | 2 | Q07/mini/base (1), Q10/sol/base (1)`.

The count of 2 and the mini record are correct. The sol record is item **Q08**, not Q10.

**Correction:** for "Q10/sol/base (1)" read "Q08/sol/base (1)".

Command, run from the repository root:

```
python -c "import json; [print(run, [(r['item_id'], r['condition']) for r in map(json.loads, open(f'output/{run}/smoke_run.jsonl',encoding='utf-8')) if r.get('record_type')!='figure_identification' and str(r.get('evidence_class')).startswith('EV-0')]) for run in ('run_e_mini','run_f_sol')]"
```

Output:

```
run_e_mini [('Q07', 'base')]
run_f_sol [('Q08', 'base')]
```

---

## Corrections by addition - 3 October 2026 (second set)

**Date:** 3 October 2026
**Affects:** Three statements in this file: one in E6 and two in the September sections (F11, E3 Addendum). No count, figure, verdict or withdrawal changes. The original lines are left as published and are corrected here. Each command runs from the repository root.

### C3. E6, line 348: one of the 52 Run B records was AUTO-MATCH, not NONE-MATCHING

E6 states (lines 347-348): "All 52 records scored WRONG-OPERATION ... All scored ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING".

The first sentence holds: each of the 52 records has at least one WRONG-OPERATION call, and 49 have only WRONG-OPERATION calls. The second sentence holds for 51 of the 52. One record (Q07, base, repeat 7) is AUTO-MATCH. Its first call used `^` and returned `42709.66242644786`. A second call, `42175 * 0.078 / 4 - 15 * 3`, returned `777.4125`, and the record released `777.41`.

**Correction:** for "All scored ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING" read "51 scored ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING. One (Q07, base, repeat 7) scored AUTO-MATCH after a second, simple-reading calculation". The 59 affected calls, the withdrawn figures and the fix are unchanged.

```
python - <<'EOF'
import json
S = json.load(open('output/run_b_sol/smoke_summary.json', encoding='utf-8'))['all_results']
I = [r for r in map(json.loads, open('output/run_b_sol/smoke_run.jsonl', encoding='utf-8')) if r.get('record_type') != 'figure_identification']
C = [(s['condition'], s['repeat'], s['figure_outcome']) for s, i in zip(S, I)
     if s['item_id'] == 'Q07' and any('^' in t['function']['arguments'] for t in i['tool_calls'] or [])]
print(len(C), [c for c in C if c[2] != 'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING'])
EOF
```

Output: `52 [('base', 7, 'AUTO-MATCH')]`

### C4. F11, line 507: "the exact tool return in every case" holds at the declared precision, not at full precision

F11 states (lines 506-507): "Across 618 clean AUTO-MATCH tool returns in run_e_mini and 479 in run_f_sol, the model released the exact tool return in every case."

The counts 618 and 479 are correct, and so is the table row "Of clean returns: model altered 0 / 0" at the declared two-decimal precision. At full precision the released figure differs from the clean return in 99 run_e_mini records and 49 run_f_sol records. All 148 are Q07: the expected value, and the calculator's return, is `777.4125`, and the model released `777.41`. That is rounding to the declared precision, not an alteration.

**Correction:** for "the model released the exact tool return in every case" read "the released figure equalled the tool return at the declared two-decimal precision in every case. At full precision, 99 (run_e_mini) and 49 (run_f_sol) Q07 releases rounded the return `777.4125` to `777.41`".

```
python - <<'EOF'
import json
from decimal import Decimal, InvalidOperation

def load(run):
    S = json.load(open(f'output/{run}/smoke_summary.json', encoding='utf-8'))['all_results']
    I = [json.loads(l) for l in open(f'output/{run}/smoke_run.jsonl', encoding='utf-8')]
    return S, [r for r in I if r.get('record_type') != 'figure_identification']

def returns(rec):
    out = []
    for t in rec['tool_calls'] or []:
        try:
            out.append(Decimal(str(json.loads(t.get('return_value') or '{}').get('result'))))
        except (InvalidOperation, ValueError, AttributeError):
            pass
    return out

q2 = lambda d: d.quantize(Decimal('0.01'))
for run in ('run_e_mini', 'run_f_sol'):
    S, I = load(run)
    clean = at2 = full = 0
    for s, i in zip(S, I):
        if s['figure_outcome'] != 'AUTO-MATCH' or s['tool_calls_count'] == 0:
            continue
        hit = [r for r in returns(i) if r == Decimal(str(s['expected']))]
        if hit:
            rel = Decimal(str(s['released_figure']))
            clean += 1
            at2 += q2(rel) != q2(hit[0])
            full += rel != hit[0]
    print(run, clean, at2, full)
EOF
```

Output (run, clean returns, released differs at 2 dp, released differs at full precision):

```
run_e_mini 618 0 99
run_f_sol 479 0 49
```

### C5. E3 Addendum, lines 177-179: 1.0015 is not a valid derivation from the fixture

The Addendum states (lines 177-179): "(annual_rate 18.0 → growth factor 1.18 or monthly factor 1.015 or 1.0015; ...) ... None is a fabricated or genuinely wrong operand."

The fixture's `credit_card` record has `annual_rate` `18.0`, `balance` `2400.00` and `reward_rate` `1.5`. The monthly factor is 1 + 18.0/100/12 = 1.015. Four of the five run_e_mini originated operands follow from these fields: 1.18 (twice), 1.015, and 2436 = 2400 × 1.015. The fifth, `1.0015` (Q05, instruction_removed, repeat 17, expression `2400 * 1.0015`), is not the monthly factor. Numerically it equals 1 + 1.5/1000, where 1.5 is both the reward rate and 18.0/12. Converting a percentage to a fraction divides by 100, which gives 1.015. No valid derivation of 1.0015 from the fixture was found. This record's figure outcome is ADJUDICATE-AMBIGUOUS.

**Correction:** for "monthly factor 1.015 or 1.0015" read "monthly factor 1.015". For "None is a fabricated or genuinely wrong operand" read "Four are pre-computed intermediates derived from the fixture. The fifth, 1.0015, has no valid derivation from the fixture that was found."

```
python - <<'EOF'
import json
a = [x for x in json.load(open('example/fixture.json', encoding='utf-8'))['accounts'] if 'credit' in json.dumps(x).lower()]
print(json.dumps(a)[:400])
S = json.load(open('output/run_e_mini/smoke_summary.json', encoding='utf-8'))['all_results']
print([(s['repeat'], o['operand_value'], o['expression']) for s in S for p in s['provenance_results']
       for o in p['operand_resolutions'] if o['resolution'] == 'originated'])
EOF
```

Output:

```
[{"id": "credit_card", "name": "Credit Card", "balance": "2400.00", "direction": "liability", "annual_rate": "18.0", "monthly_fee": "0.00", "credit_limit": "5000.00", "min_payment": "25.00", "reward_rate": "1.5"}]
[(3, '1.18', '2400 * 1.18 / 12 - 25'), (17, '1.0015', '2400 * 1.0015'), (21, '2436', '2436 - 25'), (44, '1.015', '2400 * 1.015'), (50, '1.18', '2400 * 1.18/12')]
```

---

## Correction by addition - 3 October 2026 (third set)

**Date:** 3 October 2026
**Affects:** One count in F11's source line. No figure, verdict or withdrawal changes. The original lines are left as published and corrected here. The command runs from the repository root.

### C6. F11, lines 496-497: 1,602 is all AUTO-MATCH records, not those with tool calls

F11 states (lines 496-497): "1,097 clean tool returns across 1,602 AUTO-MATCH records with tool calls."

1,602 is the number of AUTO-MATCH records: 818 (run_e_mini) + 784 (run_f_sol). The number with tool calls is 818 + 750 = 1,568, as F11's own table gives at lines 511-512. The 1,097 clean tool returns (618 + 479) are drawn from those 1,568.

**Correction:** for "across 1,602 AUTO-MATCH records with tool calls" read "across 1,568 AUTO-MATCH records with tool calls (1,602 AUTO-MATCH records in all)".

```
python - <<'EOF'
import json
for run in ('run_e_mini', 'run_f_sol'):
    S = json.load(open(f'output/{run}/smoke_summary.json', encoding='utf-8'))['all_results']
    A = [s for s in S if s['figure_outcome'] == 'AUTO-MATCH']
    print(run, len(A), sum(1 for s in A if s['tool_calls_count'] > 0))
EOF
```

Output (run, AUTO-MATCH records, of which with tool calls):

```
run_e_mini 818 818
run_f_sol 784 750
```

## Note by addition - 3 October 2026: restoring the original ground-truth module

**Date:** 3 October 2026
**Affects:** No figure, verdict or withdrawal. Nothing above is edited. This note adds a verification step for the original seals.

The original seals of `run_a_mini` and `run_b_sol` bind `ground_truth_hash` `dd3434bc62c4976af928798024d1446993ce59dd473e78cf4002832630314715`. The module was corrected after execution (E3; F10), so on the current tree `verify_run_seal.py` reports a mismatch on that one field and exits non-zero.

The module bound by the original seals is in this repository's history: `example/ground_truth_example.py` as committed in `203fef4` (5 August 2026) and left unchanged until `4f737ce` (7 August 2026). Git stores it with LF line endings. The sealed hash is that of the same file with CRLF line endings. Restoring them reproduces the sealed hash, and both original seals then pass in full.

From the root of a clean clone, in a POSIX shell (the last line puts the current module back):

```
git show 203fef4:example/ground_truth_example.py | sed 's/$/\r/' \
    > example/ground_truth_example.py
sha256sum example/ground_truth_example.py
python verify_run_seal.py output/run_a_mini
python verify_run_seal.py output/run_b_sol
git checkout -- example/ground_truth_example.py
```

Output, from a clean clone at `5ff8cd8` (the closing lines of each verification shown):

```
dd3434bc62c4976af928798024d1446993ce59dd473e78cf4002832630314715  example/ground_truth_example.py
  11 passed, 0 failed
RESULT: PASS (11 checks)
  11 passed, 0 failed
RESULT: PASS (11 checks)
```

Each verification lists eleven PASS lines, including `ground_truth_hash: MATCH`. On Windows, Git Bash's `sha256sum` prints `*` before the file name.

---

## Corrections and notes by addition - 9 October 2026

**Date:** 9 October 2026
**Affects:** Two statements in E3 (C7), and how four published records are to be read (N1-N4). No count, figure, verdict or withdrawal changes. Nothing above is edited. Each command runs from the root of a clean clone.

### C7. E3, line 68: `provenance_classify.py` was not modified "in three commits since the runs"

E3 states (line 68): "`provenance_classify.py` has been modified in three commits since the runs, one of them during Run B's execution."

The file has three commits in its whole history. Two precede both August runs. One was made while Run B was executing. None follows the runs.

| Commit | Date (UTC) | Relative to the runs | Change to `provenance_classify.py` |
|--------|------------|----------------------|------------------------------------|
| `b7c9027` | 2026-08-03 04:53 | before Run A | file created |
| `d0ec05e` | 2026-08-06 20:33 | before Run A (started 23:27) | one line: step 5 split into traceable and untraceable |
| `9df67e9` | 2026-08-07 05:31 | during Run B (05:01-06:16) | one line: `res['expression'] = expression_str` |

`9df67e9` records the calculator expression in each operand-resolution record. It changes no classification logic. Run B's records do not carry the field (0 of 4,750 operand resolutions), so Run B executed the module as it stood before that commit. The September runs carry it in every resolution.

No change to tool-call grouping appears in this file's history. E3's separate statement on grouping is taken up at the end of this entry.

**Correction:** for "has been modified in three commits since the runs, one of them during Run B's execution" read "has three commits in its history: two before Run A started, and one (`9df67e9`) during Run B's execution, which added the `expression` field to each operand-resolution record and changed no classification logic. No commit to it follows the runs." The rest of E3, including the withdrawal and its lifting in the E3 Addendum, is unchanged.

```
git log --format='%h %ad %s' --date=iso -- provenance_classify.py
git show --format= 9df67e9 -- provenance_classify.py
python - <<'EOF'
import json
for run in ('run_a_mini', 'run_b_sol', 'run_e_mini', 'run_f_sol'):
    R = [json.loads(l) for l in open(f'output/{run}/smoke_run.jsonl', encoding='utf-8')]
    O = [o for r in R if r.get('record_type') != 'figure_identification'
         for p in r.get('provenance_results') or [] for o in p['operand_resolutions']]
    print(run, min(r['timestamp'] for r in R), max(r['timestamp'] for r in R), len(O), sum('expression' in o for o in O))
EOF
```

Output:

```
9df67e9 2026-08-07 07:31:33 +0200 Add expression to provenance record + step (iv) quantisation comment
d0ec05e 2026-08-06 22:33:46 +0200 Sign-inversion finding: step 5 split into traceable and untraceable
b7c9027 2026-08-03 06:53:33 +0200 provenance split + SPEC.md 12.9/12.10 against actual state
@@ -54,6 +54,7 @@ def classify_invocation(expression_str, delivered_context, ground_truth,
+        res['expression'] = expression_str
run_a_mini 2026-08-06T23:27:18.391715+00:00 2026-08-07T00:35:06.496266+00:00 4799 0
run_b_sol 2026-08-07T05:01:03.772854+00:00 2026-08-07T06:16:07.305094+00:00 4750 0
run_e_mini 2026-09-08T11:19:36.654125+00:00 2026-09-08T12:42:06.184054+00:00 4860 4860
run_f_sol 2026-09-08T12:42:12.213568+00:00 2026-09-08T14:30:34.402375+00:00 4722 4722
```

(The `git show` output is abbreviated to its hunk header and the added line.)

**E3, line 68, second statement.** E3 also states: "The classifier's tool-call grouping logic also changed, so re-scoring alters the invocation population itself, not only the per-invocation outcome."

No commit supports this. Commits dated 1 to 28 August 2026 were searched for messages naming grouping, deduplication, the invocation population or count, or denominators, and for diffs adding or removing the word "group" in `provenance*.py`, `smoke_test.py`, `evidence.py` and `report.py`. Three commits match, and none changes how the classifier groups tool calls:

- `01bae16` (3 August, before Run A) removes a diagnostic printout in `smoke_test.py` that grouped tool-call argument structures for display.
- `ddf0968` (11 August) removes the withdrawn D7.1b invocation-count computations from `generate_findings.py`, a report generator.
- `7e19b5a` (13 August) changes the D7.5 denominators in `generate_findings.py`.

The same search over the pre-split private history returns only the pre-split counterparts of these three commits, with identical messages and dates. That history is not public, and the search cannot be rerun from this repository.

**Correction:** the sentence "The classifier's tool-call grouping logic also changed, so re-scoring alters the invocation population itself, not only the per-invocation outcome." is withdrawn. The withdrawal of the D7.2(a) figures does not depend on it. It rests on AP-1 §5.8 (E3, line 70): after a ground-truth revision, re-execution is required, not re-scoring.

```
git log --format='%h %ad %s' --date=iso --since=2026-08-01 --until=2026-08-29 -i -E --grep='group|dedup|invocation (population|count)|denominator'
git log --format='%h %ad %s' --date=iso --since=2026-08-01 --until=2026-08-29 -i -G 'group' -- '*provenance*.py' smoke_test.py evidence.py report.py
git show --stat --format='%h %s' 7e19b5a | grep -E '7e19b5a|\.py'
```

Output:

```
7e19b5a 2026-08-13 08:59:54 +0200 Wire D7.5 Clopper-Pearson bounds with correct denominators
ddf0968 2026-08-11 15:06:45 +0200 fix: remove withdrawn D7.1b claims, add gap declarations
01bae16 2026-08-03 09:21:29 +0200 Unify code paths: smoke_test calls engine.execute_item, seal, report.py, adjudication.py
7e19b5a Wire D7.5 Clopper-Pearson bounds with correct denominators
 generate_findings.py | 41 +++++++++++++++++++++++++++++++----------
```

The first command prints the first two lines and the second command prints the third. `ddf0968` matches on its message body ("generate_findings.py: D7.1b invocation count computations").

### N1. The 30 TRANSCRIBED-ALTERED labels in the September runs

In this note, System A is `run_a_mini` and `run_e_mini`, and System B is `run_b_sol` and `run_f_sol`. The D7.3 tables in `output/run_e_mini/report.md` and `output/run_f_sol/report.md` (line 1147) report 22 System A and 8 System B records as `TRANSCRIBED-ALTERED`.

The label comes from a comparison with the **last** tool return only. `smoke_test.py` (lines 644-658) takes the last calculator return in the record. `check_transcription()` in `transcription.py` (line 26) labels the record `TRANSCRIBED-ALTERED` when that return differs from the released figure (lines 105-109). The label therefore covers two different cases:

- **22 of the 30 release a figure equal to an earlier tool return** in the same record, at two decimal places: 14 System A (`run_e_mini`: Q05 instruction_removed 10, Q06 instruction_removed 4) and 8 System B (`run_f_sol`: Q07 base 5, Q05 instruction_removed 3). No tool return was changed. All 22 have release coverage `GOVERNED-RELEASE`.
- **8, all System A (`run_e_mini`), match no tool return, because the system did the last step itself:** Q09 ×6 (base 2, instruction_removed 4), Q05 ×1 and Q08 ×1 (both instruction_removed). In the Q09 records the calculator returned `15.200000000000001` and `12` (or `-12`, or `4838.0`), and the system released `3.20`. In Q05 it released `2411.00` from returns `2375` and `36.0`. In Q08 it released `287069.25` from returns `286063` and `1006.25`.
- **Release coverage classes all 8 `PARTIALLY-GOVERNED`:** a candidate figure appears in no tool return (`release_coverage.py`, lines 15-16). These 8 are ungoverned releases, and the `PARTIALLY-GOVERNED` finding for them stands.

In these runs `TRANSCRIBED-ALTERED` means "the last tool return differs from the released figure". It does not separate the two cases. The August runs carry no such labels.

```
python - <<'EOF'
import json
from collections import Counter
from decimal import Decimal, InvalidOperation
def ret(t):
    try:
        return Decimal(str(json.loads(t.get('return_value') or '{}').get('result'))).quantize(Decimal('0.01'))
    except (InvalidOperation, ValueError, AttributeError, TypeError):
        return None
for run in ('run_a_mini', 'run_b_sol', 'run_e_mini', 'run_f_sol'):
    S = json.load(open(f'output/{run}/smoke_summary.json', encoding='utf-8'))['all_results']
    I = [r for r in map(json.loads, open(f'output/{run}/smoke_run.jsonl', encoding='utf-8'))
         if r.get('record_type') != 'figure_identification']
    A = [(s, i) for s, i in zip(S, I) if s.get('transcription_outcome') == 'TRANSCRIBED-ALTERED']
    k = Counter()
    for s, i in A:
        rel = Decimal(str(s['released_figure'])).quantize(Decimal('0.01'))
        R = [ret(t) for t in i['tool_calls'] or []]
        k[('earlier-return-matches' if rel in R[:-1] else 'no-return-matches',
           s['item_id'], s['condition'], s.get('release_coverage_outcome'))] += 1
    print(run, len(A), sorted(k.items()))
EOF
```

Output:

```
run_a_mini 0 []
run_b_sol 0 []
run_e_mini 22 [(('earlier-return-matches', 'Q05', 'instruction_removed', 'GOVERNED-RELEASE'), 10), (('earlier-return-matches', 'Q06', 'instruction_removed', 'GOVERNED-RELEASE'), 4), (('no-return-matches', 'Q05', 'instruction_removed', 'PARTIALLY-GOVERNED'), 1), (('no-return-matches', 'Q08', 'instruction_removed', 'PARTIALLY-GOVERNED'), 1), (('no-return-matches', 'Q09', 'base', 'PARTIALLY-GOVERNED'), 2), (('no-return-matches', 'Q09', 'instruction_removed', 'PARTIALLY-GOVERNED'), 4)]
run_f_sol 8 [(('earlier-return-matches', 'Q05', 'instruction_removed', 'GOVERNED-RELEASE'), 3), (('earlier-return-matches', 'Q07', 'base', 'GOVERNED-RELEASE'), 5)]
```

The 8 records with no matching return, with every tool return in each:

```
python - <<'EOF'
import json
from decimal import Decimal, InvalidOperation
def ret(t):
    try:
        return Decimal(str(json.loads(t.get('return_value') or '{}').get('result')))
    except (InvalidOperation, ValueError, AttributeError, TypeError):
        return None
q = lambda d: d.quantize(Decimal('0.01'))
for run in ('run_e_mini', 'run_f_sol'):
    S = json.load(open(f'output/{run}/smoke_summary.json', encoding='utf-8'))['all_results']
    I = [r for r in map(json.loads, open(f'output/{run}/smoke_run.jsonl', encoding='utf-8'))
         if r.get('record_type') != 'figure_identification']
    for s, i in zip(S, I):
        if s.get('transcription_outcome') != 'TRANSCRIBED-ALTERED':
            continue
        rel = Decimal(str(s['released_figure']))
        R = [r for r in map(ret, i['tool_calls'] or []) if r is not None]
        if any(q(r) == q(rel) for r in R):
            continue
        print(run, s['item_id'], s['condition'], s['repeat'], 'released', rel,
              'returns', [str(r) for r in R], s.get('release_coverage_outcome'))
EOF
```

Output:

```
run_e_mini Q09 base 22 released 3.20 returns ['15.200000000000001', '-12'] PARTIALLY-GOVERNED
run_e_mini Q09 base 28 released 3.20 returns ['15.200000000000001', '12'] PARTIALLY-GOVERNED
run_e_mini Q05 instruction_removed 30 released 2411.00 returns ['2375', '36.0'] PARTIALLY-GOVERNED
run_e_mini Q08 instruction_removed 33 released 287069.25 returns ['286063', '1006.25'] PARTIALLY-GOVERNED
run_e_mini Q09 instruction_removed 8 released 3.20 returns ['15.200000000000001', '-12'] PARTIALLY-GOVERNED
run_e_mini Q09 instruction_removed 17 released 3.20 returns ['15.200000000000001', '12'] PARTIALLY-GOVERNED
run_e_mini Q09 instruction_removed 35 released 3.20 returns ['15.200000000000001', '4838.0'] PARTIALLY-GOVERNED
run_e_mini Q09 instruction_removed 42 released 3.20 returns ['15.200000000000001', '12'] PARTIALLY-GOVERNED
```

### N2. September seals: `ground_truth_hash` fails on a clean clone only because of line endings

On a clean clone, `verify_run_seal.py` reports 10 passed, 1 failed for `run_e_mini` and `run_f_sol`. The failing field is `ground_truth_hash`: sealed `033ce73d933d6e52a7d4f63b3888bdccfa492ce49cf49228ed2f3dda0d27a643`, recomputed `080ce4a7f4394878f9341edf33c97e42226adf7a1047f9f85e1de0e70c820812`.

The module has not changed since the September runs. Its last commit, `ff8c051`, is dated 2026-09-08 10:48 UTC, before `run_e_mini` started at 11:19 UTC. The repository checks it out with LF line endings (`.gitattributes`: `*.py text eol=lf`). The sealed hash is that of the same content with CRLF line endings. With CRLF restored, both September seals pass in full.

The NOTE that `verify_run_seal.py` prints after every `ground_truth_hash` mismatch (lines 184-189) gives the wrong cause for these two seals. It reads: "The ground-truth module was modified after the sealed runs: E3 removed an unused constant from Q07, and the Q05 sign-convention correction removed the negation (F10)." Both corrections precede the September runs: `85e8eeb` (16 August 2026) removed the unused constants and `6be2d7b` (7 September 2026) removed the Q05 negation. The NOTE describes the August seals. For the September seals the cause is line endings only. Separately, the erratum entry in the same script (lines 42-49) cites commits `eadd862` and `8089923`, which are not in this repository's history; the corresponding public commits are `85e8eeb` and `6be2d7b`. `verify_run_seal.py` is not edited by this note.

From the root of a clean clone, in a POSIX shell (the last line puts the module back):

```
python verify_run_seal.py output/run_e_mini
python verify_run_seal.py output/run_f_sol
sed -i 's/$/\r/' example/ground_truth_example.py
sha256sum example/ground_truth_example.py
python verify_run_seal.py output/run_e_mini
python verify_run_seal.py output/run_f_sol
git checkout -- example/ground_truth_example.py
```

Output, from a clean clone at `5bbcfc3` (the `ground_truth_hash` line and closing lines of each verification shown):

```
  FAIL  ground_truth_hash: sealed=033ce73d933d6e52a7d4f63b3888bdccfa492ce49cf49228ed2f3dda0d27a643, recomputed=080ce4a7f4394878f9341edf33c97e42226adf7a1047f9f85e1de0e70c820812
  10 passed, 1 failed
RESULT: FAIL (1 failures)
  FAIL  ground_truth_hash: sealed=033ce73d933d6e52a7d4f63b3888bdccfa492ce49cf49228ed2f3dda0d27a643, recomputed=080ce4a7f4394878f9341edf33c97e42226adf7a1047f9f85e1de0e70c820812
  10 passed, 1 failed
RESULT: FAIL (1 failures)
033ce73d933d6e52a7d4f63b3888bdccfa492ce49cf49228ed2f3dda0d27a643  example/ground_truth_example.py
  PASS  ground_truth_hash: MATCH
  11 passed, 0 failed
RESULT: PASS (11 checks)
  PASS  ground_truth_hash: MATCH
  11 passed, 0 failed
RESULT: PASS (11 checks)
```

On Windows, Git Bash's `sha256sum` prints `*` before the file name.

### N3. The `reference/` copy of the v1.3 draft carries wording corrected elsewhere

`reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md` carries the v1.3 draft as published. Its lines 9, 38, 607, 609, 617, 633, 638 and 771 name ZORRZ as the author of AP-1 and state in the present tense that ZORRZ submits its own systems to AP-1. That wording is corrected, editorially and with no normative effect, in `ERRATA.md` entry E-2 of the admissibility-protocol repository. Marcus Rupp is the author and ZORRZ Financial Inc. the publisher.

The copy here is not edited. Its SHA-256 is the `ap1_text_hash` sealed in the runs and declared in both configs.

```
sha256sum reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md
grep -n ap1_text_hash example/config.json example/config_mini.json
```

Output:

```
48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56  reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md
example/config.json:46:  "ap1_text_hash": "48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56",
example/config_mini.json:50:  "ap1_text_hash": "48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56",
```

### N4. E2's statement on temperature covers the August runs only

E2 states (line 45): "Temperature was not sent in either run." It refers to Runs A and B. No document in this repository states that neither temperature nor top_p was sent in any run.

The September runs record sampling as sent in each invocation's request record (`request_sent.request_record.sampling_as_sent`). The adapter sends every value not marked omitted (`adapter.py`, lines 92-126). `run_e_mini` sent `temperature` = `1` in all 1,000 requests. `run_f_sol` omitted temperature in all 1,000 (reason `platform-rejected`). Both omitted `top_p` in all 1,000, with reason `operator-declared` and no further detail recorded. The August records carry no request record.

```
python - <<'EOF'
import json, collections
for run in ('run_a_mini', 'run_b_sol', 'run_e_mini', 'run_f_sol'):
    I = [r for r in map(json.loads, open(f'output/{run}/smoke_run.jsonl', encoding='utf-8'))
         if r.get('record_type') != 'figure_identification']
    T, P = collections.Counter(), collections.Counter()
    for r in I:
        s = ((r.get('request_sent') or {}).get('request_record') or {}).get('sampling_as_sent')
        if s is None:
            T['no request_record'] += 1
            continue
        t = s.get('temperature')
        T[t if isinstance(t, str) else t.get('reason')] += 1
        P[s['top_p'].get('reason') + ' / detail=' + repr(s['top_p'].get('detail'))] += 1
    print(run, dict(T), dict(P))
EOF
```

Output:

```
run_a_mini {'no request_record': 1000} {}
run_b_sol {'no request_record': 1000} {}
run_e_mini {'1': 1000} {"operator-declared / detail=''": 1000}
run_f_sol {'platform-rejected': 1000} {"operator-declared / detail=''": 1000}
```
