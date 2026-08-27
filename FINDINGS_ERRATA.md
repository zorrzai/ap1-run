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
