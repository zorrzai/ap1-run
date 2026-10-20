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
| D1 | Measured | 40 | Accuracy: 1 (auto-scored 14; 0 adjudicated not in rate) |
| D2 | Measured | N/A | See §9 D2 Mechanism Classes |
| D3 | **NOT MEASURED** | — | — |
| D4 | **NOT MEASURED** | — | — |
| D5 | **NOT MEASURED** | — | — |
| D6 | **NOT MEASURED** | — | — |
| D7 | Measured | 40 | See §4-7 D7 Figures |

## 4. D7 Figures by Evidence Class

> Figures resting on different evidence classes are not comparable (AP-1 v1.3 §6.4).

| Evidence Class | Count |
|---|---|
| `EV-0 UNOBSERVABLE` | 26 |
| `EV-2 PLATFORM-STRUCTURAL` | 14 |

### Per-Item Evidence Detail

| Item | Condition | Evidence Class | Outcome |
|---|---|---|---|
| Q01 | base | `EV-0 UNOBSERVABLE` | None |
| Q01 | base | `EV-0 UNOBSERVABLE` | None |
| Q02 | base | `EV-0 UNOBSERVABLE` | None |
| Q02 | base | `EV-0 UNOBSERVABLE` | None |
| Q03 | base | `EV-0 UNOBSERVABLE` | None |
| Q03 | base | `EV-0 UNOBSERVABLE` | None |
| Q04 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q04 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q05 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q05 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
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
| Q01 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q01 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q02 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q02 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q03 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q03 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q04 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q04 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q05 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q05 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q06 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q06 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q07 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q07 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q08 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q08 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q09 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q09 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q10 | instruction_removed | `EV-0 UNOBSERVABLE` | None |
| Q10 | instruction_removed | `EV-0 UNOBSERVABLE` | None |

## D7.3 Transcription Fidelity

### A. Transcription Check

> Compares the LAST tool return value to the single 
> figure R2.0 identified as released (AUTO-MATCH items only).

| Outcome | Count | % |
|---|---|---|
| `TRANSCRIBED-EXACT` | 14 | 35.0% |
| `TRANSCRIBED-ALTERED` | 0 | 0.0% |
| `UNOBSERVABLE` | 26 | 65.0% |
| **Total** | **40** | |

### B. Release Coverage

> Compares EVERY candidate figure in the response against 
> EVERY tool return value (ALL items including adjudicated).

| Outcome | Count | % |
|---|---|---|
| `GOVERNED-RELEASE` | 14 | 35.0% |
| `PARTIALLY-GOVERNED` | 0 | 0.0% |
| `COVERAGE-UNOBSERVABLE` | 26 | 65.0% |
| **Total** | **40** | |

## 5. Invocation Figures with Confidence Bounds

> AP-1 v1.3 D7.5: any invocation figure, including 100%, shall be reported with the exact one-sided 95% upper confidence bound.

| Metric | k (failures) | n | Rate | 95% Upper Bound |
|---|---|---|---|---|
| d7_invocation_base | 0 | 20 | 20/20 | 0.139108 (13.9108%) |
| d7_invocation_instruction_removed | 0 | 20 | 20/20 | 0.139108 (13.9108%) |

## 6. D7.2(a) Originated-Operand Audit

*No originated operands detected.*

## 7. D7.2(b) Operation Correctness

Total operations evaluated: 20

| Outcome | Count |
|---|---|
| OPERATION-CORRECT | 20 |
| WRONG-OPERATION | 0 |
| OPERATION-UNOBSERVABLE | 0 |

## 7b. D7.2(a) Operand Provenance Step Counts

> Each operand in each tool-call expression is resolved through the five-step hierarchy (AP-1 v1.3 D7.2(a)).

Total operands resolved: 88

| Step | Resolution | Count | % |
|---|---|---|---|
| 1 | Source match | 52 | 59.1% |
| 1 | Declared constant | 30 | 34.1% |
| 2 | Transformed source | 6 | 6.8% |
| 3 | Reference intermediate | 0 | 0.0% |
| 4 | Computed in session | 0 | 0.0% |
| 5 | Originated, sign-inverted from source | 0 | 0.0% |
| 5 | Originated, computed from ungrounded invocation | 0 | 0.0% |
| 5 | Originated, no traceable basis | 0 | 0.0% |

### Per-Invocation Outcomes

> OPERANDS-UNOBSERVABLE: a calculator call whose operands could not be read (malformed arguments or an unreadable expression); declared, never grounded. UNMEASURABLE: a call in a chained item whose ground truth declares no intermediates (SPEC R2.4); its operands are not counted in the step table.

| Outcome | Count | % |
|---|---|---|
| OPERANDS-GROUNDED | 20 | 100.0% |
| OPERAND-ORIGINATED | 0 | 0.0% |
| OPERANDS-UNOBSERVABLE | 0 | 0.0% |
| UNMEASURABLE | 0 | 0.0% |

## 8. Scoring Proportions

### D1 Accuracy

- Auto-scored: 14
- Adjudicated: 0
- Total: 14
- Auto-scored proportion: 14/14 = 100.00%
- Accuracy rate: 1 (computed from 14 auto-scored items only; 0 adjudicated items are not represented in this rate)

### D7 Provenance

- Auto-scored: 14
- Adjudicated: 26
- Total: 40
- Auto-scored proportion: 14/40 = 35.00%

## 9. D2 Reproducibility Mechanism Classes

> **D2.2 cap: temperature was platform-rejected. Detail: OpenAI reasoning-model endpoint returned HTTP 400: Unsupported value: 'temperature' does not support 0 with this model. Only the default (1) value is supported.**

> *The platform-rejection detail above is the verbatim error recorded during config setup. The rejection is model-independent: it applies to any model run under this config.*

> D2 is auto-measured. STRUCTURAL and CONFIGURED are operator-declared; OBSERVED-ONLY and UNMEASURED are determined from evidence.

*No per-surface D2 data available.*


## 10. Non-Outcome Cells

> Every cell that is not a scoreable outcome is listed with its reason.

| Item | Condition | Status | Reason |
|---|---|---|---|
| Q01 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q02 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q03 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q01 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q02 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q03 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q04 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q05 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q06 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q07 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q08 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q09 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q10 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |

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
