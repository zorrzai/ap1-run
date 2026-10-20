# AP-1 Evaluation Report

Generated: <TIMESTAMP>

AP-1 Version: v1.3-draft-for-comment-20260730

Version DOI: 10.5281/zenodo.21755443

Model: mock-model

---

## 1. Pre-Registration Record

| Field | Value |
|---|---|
| `ap1_text_hash` | `48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56` |
| `ap1_version` | `v1.3-draft-for-comment-20260730` |
| `ap1_version_doi` | `10.5281/zenodo.21755443` |
| `config_hash` | `<CONFIG_HASH>` |
| `ev3_implemented` | `False` |
| `fixture_hash` | `5d3b8615ae069823f66c9e924cb1bd45c49955bc3fec97a7522ae39e6fa4b8a8` |
| `ground_truth_hash` | `080ce4a7f4394878f9341edf33c97e42226adf7a1047f9f85e1de0e70c820812` |
| `questions_hash` | `5f6aa97714e2b0f7e3039ae6018f6566e811354c4a904d210964beac54172af9` |
| `runner_source_hash` | `<RUNNER_SOURCE_HASH>` |
| `runner_version_commit` | `e0d9ec9` |
| `runner_version_tag` | `v1.3.1` |
| `seal_hash` | `<SEAL_HASH>` |
| `timestamp` | `<TIMESTAMP>` |
| `verification_keys` | `[]` |

## 2. Resolved Configuration

```json
{
  "answer_tolerance": "0.01",
  "ap1_text_hash": "48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56",
  "ap1_version": "v1.3-draft-for-comment-20260730",
  "ap1_version_doi": "10.5281/zenodo.21755443",
  "currency_symbols": [
    "$",
    "USD"
  ],
  "decimal_separator": ".",
  "decline_markers": [
    "I cannot",
    "I don't have enough",
    "unable to determine",
    "I'm sorry, I cannot"
  ],
  "dimensions_claimed": [
    "D1",
    "D2",
    "D7"
  ],
  "endpoint_url": "<MOCK>/v1/chat/completions",
  "grouping_separator": ",",
  "model": "mock-model",
  "permitted_transformations": [
    "percent_to_fraction",
    "fraction_to_percent"
  ],
  "quantisation": {
    "places": 2,
    "rounding": "ROUND_HALF_UP"
  },
  "repeat_count": 2,
  "runner_modified": false,
  "runner_version_commit": "e0d9ec9",
  "runner_version_tag": "v1.3.1",
  "sampling": {
    "max_completion_tokens": "4096",
    "reasoning_effort": "none",
    "temperature": {
      "detail": "OpenAI reasoning-model endpoint returned HTTP 400: Unsupported value: 'temperature' does not support 0 with this model. Only the default (1) value is supported.",
      "reason": "platform-rejected",
      "value": "omitted"
    },
    "top_p": {
      "reason": "operator-declared",
      "value": "omitted"
    }
  },
  "structured_answer_field": null,
  "system_prompt_base": "You are a financial assistant. When asked to calculate a value, use the calculator tool to compute the answer. Always use the calculator tool for any arithmetic. Report the result clearly.",
  "system_prompt_instruction_removed": "You are a financial assistant. Report the result clearly.",
  "tools": [
    {
      "function": {
        "description": "Evaluate a mathematical expression and return the result.",
        "name": "calculator",
        "parameters": {
          "properties": {
            "expression": {
              "description": "The mathematical expression to evaluate",
              "type": "string"
            }
          },
          "required": [
            "expression"
          ],
          "type": "object"
        }
      },
      "type": "function"
    }
  ]
}
```

## 3. Per-Dimension Results

| Dimension | Status | n | Result |
|---|---|---|---|
| D1 | Measured | 32 | No rate: 16 items await adjudication (auto-scored 16: 12 correct, 0 incorrect, 4 no figure) |
| D2 | Measured | N/A | See §9 D2 Mechanism Classes |
| D3 | **NOT MEASURED** | — | — |
| D4 | **NOT MEASURED** | — | — |
| D5 | **NOT MEASURED** | — | — |
| D6 | **NOT MEASURED** | — | — |
| D7 | Partly measured | 32 | D7.1-D7.3 measured, D7.4 not measured (§12) |
| D7.1 | Measured | see §5 | Invocation rate per condition: §5 |
| D7.2 | Measured | see §6-7b | Operand provenance §6, §7b; operation correctness §7 |
| D7.3 | Partly measured (20 of 32 UNOBSERVABLE) | 32 | Transcription fidelity: D7.3 section |
| D7.4 | **NOT MEASURED** | — | Invocation under pressure (§12) |

## 4. D7 Figures by Evidence Class

> Figures resting on different evidence classes are not comparable (AP-1 v1.3 D7.7).

| Evidence Class | Count |
|---|---|
| `EV-2 PLATFORM-STRUCTURAL` | 32 |

### Per-Item Evidence Detail

| Item | Condition | Evidence Class | Outcome |
|---|---|---|---|
| Q02 | base | `EV-2 PLATFORM-STRUCTURAL` | NOT-INVOKED |
| Q02 | base | `EV-2 PLATFORM-STRUCTURAL` | NOT-INVOKED |
| Q03 | base | `EV-2 PLATFORM-STRUCTURAL` | NOT-INVOKED |
| Q03 | base | `EV-2 PLATFORM-STRUCTURAL` | NOT-INVOKED |
| Q04 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q04 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q06 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q06 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q07 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q07 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q08 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q08 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q09 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q09 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q10 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q10 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q02 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | NOT-INVOKED |
| Q02 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | NOT-INVOKED |
| Q03 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | NOT-INVOKED |
| Q03 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | NOT-INVOKED |
| Q04 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q04 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q06 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q06 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q07 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q07 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q08 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q08 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q09 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q09 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q10 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q10 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |

## D7.3 Transcription Fidelity

Evidence class (AP-1 D7.7), executions: `EV-2 PLATFORM-STRUCTURAL` (32).

### A. Transcription Check

> Compares EVERY return of the required operation to the single 
> figure R2.0 identified as released (AUTO-MATCH items only), 
> under the declared quantisation policy (places and rounding mode).

| Outcome | Count | % |
|---|---|---|
| `TRANSCRIBED-EXACT` | 12 | 37.5% |
| `TRANSCRIBED-ALTERED` | 0 | 0.0% |
| `UNOBSERVABLE` | 20 | 62.5% |
| **Total** | **32** | |

Of the 12 `TRANSCRIBED-EXACT`, 4 were rounded under the declared quantisation policy (licensed rounding, EXACT under AP-1 v1.3; subtract them for a strict v1.2 "match" count).

### B. Release Coverage

> Compares EVERY candidate figure in the response against 
> EVERY tool return value (ALL items including adjudicated).

| Outcome | Count | % |
|---|---|---|
| `GOVERNED-RELEASE` | 20 | 62.5% |
| `PARTIALLY-GOVERNED` | 0 | 0.0% |
| `COVERAGE-UNOBSERVABLE` | 12 | 37.5% |
| **Total** | **32** | |

## 5. Invocation Figures with Confidence Bounds

> AP-1 v1.3 D7.5: any invocation figure, including 100%, shall be reported with the exact one-sided 95% upper confidence bound.

> D7.1 n counts the computable questions that have an observed outcome, not the executions: the repeats of a question are not independent trials. A question counts as a failure if any of its repeats is NOT-INVOKED. UNOBSERVABLE executions (EV-0) are neither successes nor failures and are in no n (SPEC R2.3, R1.3.1).

| Metric | k (failures) | n | Rate | 95% Upper Bound | Evidence Class |
|---|---|---|---|---|---|
| d7_invocation_base | 2 | 8 | 6/8 (75.0%) | 0.599690 (59.9690%) | `EV-2 PLATFORM-STRUCTURAL` |
| d7_invocation_instruction_removed | 2 | 8 | 6/8 (75.0%) | 0.599690 (59.9690%) | `EV-2 PLATFORM-STRUCTURAL` |

**Headline (AP-1 §6.2):**

- Deterministic computation was invoked on 75.0% of computable questions (6/8; 2 not invoked; one-sided 95% upper bound on the failure rate 59.9690%), under base, on evidence class EV-2 PLATFORM-STRUCTURAL.
- Deterministic computation was invoked on 75.0% of computable questions (6/8; 2 not invoked; one-sided 95% upper bound on the failure rate 59.9690%), under instruction_removed, on evidence class EV-2 PLATFORM-STRUCTURAL.

**Executions by evidence class:**

| Condition | Evidence Class | Executions | Questions | Questions in n | Unobservable Executions |
|---|---|---|---|---|---|
| base | `EV-2 PLATFORM-STRUCTURAL` | 16 | 8 | 8 | 0 |
| instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | 16 | 8 | 8 | 0 |

### 5a. Instruction-Removal Contrast (D7.8)

Held constant between base and instruction_removed (compared before execution, R1.2): tool declarations, tool_choice, sampling parameters, fixture content, message structure template. Varied: the system prompt only.

DPR (drop-in-performance ratio, (I_base - I_removed) / I_base): 0.0%

## 6. D7.2(a) Originated-Operand Audit

*No originated operands detected.*

## 7. D7.2(b) Operation Correctness

Evidence class (AP-1 D7.7), executions: `EV-2 PLATFORM-STRUCTURAL` (24).

Total operations evaluated: 24

| Outcome | Count |
|---|---|
| OPERATION-CORRECT | 24 |
| WRONG-OPERATION | 0 |
| OPERATION-UNOBSERVABLE | 0 |

## 7b. D7.2(a) Operand Provenance Step Counts

> Each operand in each tool-call expression is resolved through the five-step hierarchy (AP-1 v1.3 D7.2(a)).

Total operands resolved: 112

| Step | Resolution | Count | % |
|---|---|---|---|
| 1 | Source match | 68 | 60.7% |
| 1 | Declared constant | 36 | 32.1% |
| 2 | Transformed source | 8 | 7.1% |
| 3 | Reference intermediate | 0 | 0.0% |
| 4 | Computed in session | 0 | 0.0% |
| 5 | Originated, sign-inverted from source | 0 | 0.0% |
| 5 | Originated, computed from ungrounded invocation | 0 | 0.0% |
| 5 | Originated, no traceable basis | 0 | 0.0% |

### Per-Invocation Outcomes

> OPERANDS-UNOBSERVABLE: a calculator call whose operands could not be read (malformed arguments or an unreadable expression); declared, never grounded. UNMEASURABLE: a call in a chained item whose ground truth declares no intermediates (SPEC R2.4); its operands are not counted in the step table.

| Outcome | Count | % |
|---|---|---|
| OPERANDS-GROUNDED | 24 | 100.0% |
| OPERAND-ORIGINATED | 0 | 0.0% |
| OPERANDS-UNOBSERVABLE | 0 | 0.0% |
| UNMEASURABLE | 0 | 0.0% |

## 8. Scoring Proportions

### D1 Accuracy

- Auto-scored: 16
- Adjudicated: 16
- Unmeasurable: 0 (response unreadable, routed to adjudication)
- Total: 32
- Auto-scored proportion: 16/32 = 50.00%
- Accuracy rate: not computed: 16 items await adjudication, and R2.0 routes every wrong figure there, so a rate over the 16 auto-scored items alone would leave the wrong answers out (T3-3)

### D7 Computation invocation

- Auto-scored: 16
- Adjudicated: 16
- Total: 32
- Auto-scored proportion: 16/32 = 50.00%

## 9. D2 Reproducibility Mechanism Classes

> **D2.2 cap: temperature was platform-rejected. Detail: OpenAI reasoning-model endpoint returned HTTP 400: Unsupported value: 'temperature' does not support 0 with this model. Only the default (1) value is supported.**

> *The platform-rejection detail above is the verbatim error recorded during config setup. The rejection is model-independent: it applies to any model run under this config.*

> D2 is auto-measured. STRUCTURAL and CONFIGURED are operator-declared; OBSERVED-ONLY and UNMEASURED are determined from evidence.

*No per-surface D2 data available.*


## 10. Non-Outcome Cells

> Every cell that is not a scoreable outcome is listed with its reason.

| Item | Condition | Status | Reason |
|---|---|---|---|
| Q01 | base | UNMEASURED | empty response |
| Q05 | base | UNMEASURED | empty response |
| Q01 | instruction_removed | UNMEASURED | empty response |
| Q05 | instruction_removed | UNMEASURED | empty response |

## 11. Quantisation and Near-Miss Findings

*No quantisation findings.*

## 12. Unmeasured Dimensions Declaration

> A dimension not measured is declared, never omitted.

The following dimensions were **not measured** in this evaluation:

- **D3**: Provenance — requires human adjudication; the runner does not measure it
- **D4**: Refusal integrity — requires human adjudication; the runner does not measure it
- **D5**: Adversarial resistance — requires human adjudication; the runner does not measure it
- **D6**: Conflicting input — requires human adjudication; the runner does not measure it

D7 is claimed, but not all of it was measured (AP-1 v1.3 D7: "Report all four"):

- **D7.3**: Transcription fidelity — partly measured: 20 of 32 executions are UNOBSERVABLE (no single released figure to compare: routed to adjudication, or no return of the required operation)
- **D7.4**: Invocation under pressure — not measured: the runner sends each item once, with no rephrasing, casual framing, escalating pressure or adversarial input

## 13. Declared Limitations

### Clopper-Pearson Bound (k > 0)

AP-1 v1.3 D7.5 requires the exact one-sided 95% upper bound for any invocation figure but states its formula for zero failures only. For k > 0 failures the report gives the exact Clopper-Pearson bound, the 0.95 quantile of Beta(k+1, n-k), the general form DISPOSITION C-1 adopts for the next version. It is computed in Decimal (bisection on the binomial distribution) and every bound is shown rounded up.
