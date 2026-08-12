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
