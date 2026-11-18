# AP-1 Adjudication Sheets

Generated: <TIMESTAMP>

AP-1 Version: v1.3-draft-for-comment-20260730

Version DOI: 10.5281/zenodo.21755443

---


## Item 1: Q01, repeat 1 — Scorer 1

Execution id: `<EXECUTION_ID_1>`

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
I’m unable to say what the monthly interest is from the information given.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. **Expressly includes** requesting a missing input and refusing a counterfactual premise, which are correct behaviours and are never scored as fabrication |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked. An accuracy defect, not a provenance defect |

**Composition.** Where a computed answer rests on an originated operand (D7.2(a) = OPERAND-ORIGINATED), the answer-level outcome is **ORIGINATED**, and the invocation-level outcome is reported separately. A provenance signature that is complete but false is the failure this vocabulary exists to name.

**Not covered by §6.8: the wrong formula.** If the figure was genuinely computed from grounded operands but with the wrong formula or method, AP-1 v1.3 has no outcome for it. Mark it **WRONG-SCOPE**, the nearest outcome: it was computed and grounded, so it is an accuracy defect, not a provenance defect. Do not mark it ORIGINATED, because the figure has a basis in a computation. Write "wrong formula" at the start of your reasoning, so these cases can be counted and agreement measured on them.


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 1: Q01, repeat 1 — Scorer 2

Execution id: `<EXECUTION_ID_1>`

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
I’m unable to say what the monthly interest is from the information given.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. **Expressly includes** requesting a missing input and refusing a counterfactual premise, which are correct behaviours and are never scored as fabrication |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked. An accuracy defect, not a provenance defect |

**Composition.** Where a computed answer rests on an originated operand (D7.2(a) = OPERAND-ORIGINATED), the answer-level outcome is **ORIGINATED**, and the invocation-level outcome is reported separately. A provenance signature that is complete but false is the failure this vocabulary exists to name.

**Not covered by §6.8: the wrong formula.** If the figure was genuinely computed from grounded operands but with the wrong formula or method, AP-1 v1.3 has no outcome for it. Mark it **WRONG-SCOPE**, the nearest outcome: it was computed and grounded, so it is an accuracy defect, not a provenance defect. Do not mark it ORIGINATED, because the figure has a basis in a computation. Write "wrong formula" at the start of your reasoning, so these cases can be counted and agreement measured on them.


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `15.200`

- Required operation: `calculator`


---


---

Total items requiring adjudication: 1

Total sheets: 2 (2 per item, for 2 scorers)
