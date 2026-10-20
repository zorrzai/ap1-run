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
| D1 | **NOT MEASURED** | — | — |
| D2 | Measured | N/A | See §9 D2 Mechanism Classes |
| D3 | **NOT MEASURED** | — | — |
| D4 | **NOT MEASURED** | — | — |
| D5 | **NOT MEASURED** | — | — |
| D6 | **NOT MEASURED** | — | — |
| D7 | Measured | 31 | See §4-7 D7 Figures |

## 4. D7 Figures by Evidence Class

> Figures resting on different evidence classes are not comparable (AP-1 v1.3 §6.4).

| Evidence Class | Count |
|---|---|
| `EV-0 UNOBSERVABLE` | 1 |
| `EV-2 PLATFORM-STRUCTURAL` | 30 |

### Per-Item Evidence Detail

| Item | Condition | Evidence Class | Outcome |
|---|---|---|---|
| Q01 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q01 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q02 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q02 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q03 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q04 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q06 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q07 | base | `EV-0 UNOBSERVABLE` | None |
| Q07 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q09 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q09 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q10 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q10 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q01 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q01 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q02 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q02 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q03 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q03 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q04 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q04 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q05 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q05 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q06 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q06 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q07 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q07 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
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
| `TRANSCRIBED-EXACT` | 30 | 96.8% |
| `TRANSCRIBED-ALTERED` | 0 | 0.0% |
| `UNOBSERVABLE` | 1 | 3.2% |
| **Total** | **31** | |

### B. Release Coverage

> Compares EVERY candidate figure in the response against 
> EVERY tool return value (ALL items including adjudicated).

| Outcome | Count | % |
|---|---|---|
| `GOVERNED-RELEASE` | 30 | 96.8% |
| `PARTIALLY-GOVERNED` | 0 | 0.0% |
| `COVERAGE-UNOBSERVABLE` | 1 | 3.2% |
| **Total** | **31** | |

## 5. Invocation Figures with Confidence Bounds

> AP-1 v1.3 D7.5: any invocation figure, including 100%, shall be reported with the exact one-sided 95% upper confidence bound.

| Metric | k (failures) | n | Rate | 95% Upper Bound |
|---|---|---|---|---|
| d7_invocation_base | 0 | 13 | 13/13 | 0.205817 (20.5817%) |
| d7_invocation_instruction_removed | 0 | 18 | 18/18 | 0.153318 (15.3318%) |

## 6. D7.2(a) Originated-Operand Audit

*No originated operands detected.*

## 7. D7.2(b) Operation Correctness

Total operations evaluated: 31

| Outcome | Count |
|---|---|
| OPERATION-CORRECT | 31 |
| WRONG-OPERATION | 0 |
| OPERATION-UNOBSERVABLE | 0 |

## 7b. D7.2(a) Operand Provenance Step Counts

> Each operand in each tool-call expression is resolved through the five-step hierarchy (AP-1 v1.3 D7.2(a)).

Total operands resolved: 129

| Step | Resolution | Count | % |
|---|---|---|---|
| 1 | Source match | 79 | 61.2% |
| 1 | Declared constant | 44 | 34.1% |
| 2 | Transformed source | 6 | 4.7% |
| 3 | Reference intermediate | 0 | 0.0% |
| 4 | Computed in session | 0 | 0.0% |
| 5 | Originated, sign-inverted from source | 0 | 0.0% |
| 5 | Originated, computed from ungrounded invocation | 0 | 0.0% |
| 5 | Originated, no traceable basis | 0 | 0.0% |

### Per-Invocation Outcomes

| Outcome | Count |
|---|---|
| OPERANDS-GROUNDED | 31 |
| OPERAND-ORIGINATED | 0 |

## 8. Scoring Proportions

### D1 Accuracy

- Auto-scored: 30
- Adjudicated: 0
- Total: 30
- Auto-scored proportion: 30/30 = 100.00%
- Accuracy rate: 1 (computed from 30 auto-scored items only; 0 adjudicated items are not represented in this rate)

### D7 Provenance

- Auto-scored: 30
- Adjudicated: 1
- Total: 31
- Auto-scored proportion: 30/31 = 96.77%

## 9. D2 Reproducibility Mechanism Classes

> **D2.2 cap: temperature was platform-rejected. Detail: OpenAI reasoning-model endpoint returned HTTP 400: Unsupported value: 'temperature' does not support 0 with this model. Only the default (1) value is supported.**

> *The platform-rejection detail above is the verbatim error recorded during config setup. The rejection is model-independent: it applies to any model run under this config.*

> D2 is auto-measured. STRUCTURAL and CONFIGURED are operator-declared; OBSERVED-ONLY and UNMEASURED are determined from evidence.

*No per-surface D2 data available.*


## 9b. D2.2 Execution Conditions

- Serving stack and version: not disclosed by the endpoint; the runner cannot observe it.
- Deterministic or batch-invariant mode: none requested by the runner; whether the endpoint enables one is not disclosed.
- Concurrency: one request at a time, sequentially, from a single process.
- Sampling parameters sent:
  - `max_completion_tokens`: `4096`
  - `reasoning_effort`: `none`
  - `temperature`: not sent (platform-rejected)
  - `top_p`: not sent (operator-declared)
- Parameter echo: `UNVERIFIED` (31 responses checked)

## 10. Non-Outcome Cells

> Every cell that is not a scoreable outcome is listed with its reason.

| Item | Condition | Status | Reason |
|---|---|---|---|
| Q03 | base | UNMEASURED | rate limited (HTTP 429): {"error": {"message": "Rate limit reached"}} |
| Q04 | base | UNMEASURED | HTTP 500: {"error": {"message": "server error"}} |
| Q05 | base | UNMEASURED | transport failure after 3 attempts: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')) |
| Q06 | base | UNMEASURED | response is not valid JSON: this is not json |
| Q08 | base | UNMEASURED | HTTP 401: {"error": {"message": "Incorrect API key provided: [REDACTED]"}} |
| Q08 | instruction_removed | UNMEASURED | HTTP 401: {"error": {"message": "Incorrect API key provided: [REDACTED]"}} |
| Q03 | base | TRANSPORT_FAILURE | TRANSPORT_FAILURE: rate limited (HTTP 429): {"error": {"message": "Rate limit reached"}} |
| Q03 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q04 | base | TRANSPORT_FAILURE | TRANSPORT_FAILURE: HTTP 500: {"error": {"message": "server error"}} |
| Q04 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q05 | base | TRANSPORT_FAILURE | TRANSPORT_FAILURE: transport failure after 3 attempts: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')) |
| Q05 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q06 | base | TRANSPORT_FAILURE | TRANSPORT_FAILURE: response is not valid JSON: this is not json |
| Q06 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q07 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q08 | base | TRANSPORT_FAILURE | TRANSPORT_FAILURE: HTTP 401: {"error": {"message": "Incorrect API key provided: [REDACTED]"}} |
| Q08 | base | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |
| Q08 | instruction_removed | TRANSPORT_FAILURE | TRANSPORT_FAILURE: HTTP 401: {"error": {"message": "Incorrect API key provided: [REDACTED]"}} |
| Q08 | instruction_removed | UNOBSERVABLE | Evidence class: EV-0 UNOBSERVABLE |

## 11. Quantisation and Near-Miss Findings

*No quantisation findings.*

## 12. Unmeasured Dimensions Declaration

> A dimension not measured is declared, never omitted.

The following dimensions were **not measured** in this evaluation and require human adjudication:

- **D1**: Accuracy — requires item-level scoring
- **D3**: Completeness of explanation — requires human adjudication
- **D4**: Appropriate caveats — requires human adjudication
- **D5**: Source attribution — requires human adjudication
- **D6**: Confidence calibration — requires human adjudication

## 13. Declared Limitations

### Clopper-Pearson Bound (k > 0)

An exact confidence bound for non-zero failure counts is not computed; AP-1 v1.3 D7.5 specifies the zero-failure form only. This is an author-identified defect in the standard, noted for resolution in the adopted version.

For non-zero failure counts, the point estimate is reported with n. The full Beta quantile would require an external dependency or a specification extension.
