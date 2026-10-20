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
| D1 | Measured | 32 | Accuracy: 1 (auto-scored 20; 12 adjudicated not in rate) |
| D2 | Measured | N/A | See §9 D2 Mechanism Classes |
| D3 | **NOT MEASURED** | — | — |
| D4 | **NOT MEASURED** | — | — |
| D5 | **NOT MEASURED** | — | — |
| D6 | **NOT MEASURED** | — | — |
| D7 | Measured | 32 | See §4-7 D7 Figures |

## 4. D7 Figures by Evidence Class

> Figures resting on different evidence classes are not comparable (AP-1 v1.3 §6.4).

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

### A. Transcription Check

> Compares the LAST tool return value to the single 
> figure R2.0 identified as released (AUTO-MATCH items only).

| Outcome | Count | % |
|---|---|---|
| `TRANSCRIBED-EXACT` | 16 | 50.0% |
| `TRANSCRIBED-ALTERED` | 0 | 0.0% |
| `UNOBSERVABLE` | 16 | 50.0% |
| **Total** | **32** | |

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
| d7_invocation_base | 2 | 8 | 6/8 (75.0%) | *not computed (see §Declared Limitations)* | `EV-2 PLATFORM-STRUCTURAL` |
| d7_invocation_instruction_removed | 2 | 8 | 6/8 (75.0%) | *not computed (see §Declared Limitations)* | `EV-2 PLATFORM-STRUCTURAL` |

**Headline (AP-1 §6.2):**

- Deterministic computation was invoked on 75.0% of computable questions (6/8; 2 not invoked; upper bound on the failure rate not computed, see §Declared Limitations), under base, on evidence class EV-2 PLATFORM-STRUCTURAL.
- Deterministic computation was invoked on 75.0% of computable questions (6/8; 2 not invoked; upper bound on the failure rate not computed, see §Declared Limitations), under instruction_removed, on evidence class EV-2 PLATFORM-STRUCTURAL.

**Executions by evidence class:**

| Condition | Evidence Class | Executions | Questions | Questions in n | Unobservable Executions |
|---|---|---|---|---|---|
| base | `EV-2 PLATFORM-STRUCTURAL` | 16 | 8 | 8 | 0 |
| instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | 16 | 8 | 8 | 0 |

## 6. D7.2(a) Originated-Operand Audit

*No originated operands detected.*

## 7. D7.2(b) Operation Correctness

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

| Outcome | Count |
|---|---|
| OPERANDS-GROUNDED | 24 |
| OPERAND-ORIGINATED | 0 |

## 8. Scoring Proportions

### D1 Accuracy

- Auto-scored: 20
- Adjudicated: 12
- Total: 32
- Auto-scored proportion: 20/32 = 62.50%
- Accuracy rate: 1 (computed from 20 auto-scored items only; 12 adjudicated items are not represented in this rate)

### D7 Provenance

- Auto-scored: 20
- Adjudicated: 12
- Total: 32
- Auto-scored proportion: 20/32 = 62.50%

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

The following dimensions were **not measured** in this evaluation and require human adjudication:

- **D3**: Completeness of explanation — requires human adjudication
- **D4**: Appropriate caveats — requires human adjudication
- **D5**: Source attribution — requires human adjudication
- **D6**: Confidence calibration — requires human adjudication

## 13. Declared Limitations

### Clopper-Pearson Bound (k > 0)

An exact confidence bound for non-zero failure counts is not computed; AP-1 v1.3 D7.5 specifies the zero-failure form only. This is an author-identified defect in the standard, noted for resolution in the adopted version.

For non-zero failure counts, the point estimate is reported with n. The full Beta quantile would require an external dependency or a specification extension.
