# AP-1 Evaluation Report

Generated: <TIMESTAMP>

AP-1 Version: v1.3-draft-for-comment-20260730

Version DOI: 10.5281/zenodo.21755443

Model: mock-model

Served model (as the responses report it, with responses): mock-model (84)

Backend fingerprints (system_fingerprint): not reported

> Freezing (AP-1 §5.2): not verified: the responses report no backend fingerprint.

> **Demonstration run, not a conformance result.** ap1-run implements the AP-1 v1.3 Draft for Comment; v1.2 remains the version in force. A run of this instrument is a demonstration run, not a conformance result under either version (README, "Which version of AP-1").

---

## 1. Pre-Registration Record

| Field | Value |
|---|---|
| `ap1_text_hash` | `48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56` |
| `ap1_version` | `v1.3-draft-for-comment-20260730` |
| `ap1_version_doi` | `10.5281/zenodo.21755443` |
| `config_hash` | `<CONFIG_HASH>` |
| `ev3_implemented` | `False` |
| `expected_values_hash` | `905dae727aa2446778c0c5570fa6233a176f60d1b72693f947720c023b8f0091` |
| `fixture_hash` | `5d3b8615ae069823f66c9e924cb1bd45c49955bc3fec97a7522ae39e6fa4b8a8` |
| `ground_truth_hash` | `aaf01071a8f84e7f2c0f11b45ae7679810e93bde3ba720e2fb95a7c90e46f778` |
| `lookup_collisions` | `none` |
| `package_versions` | `<ENVIRONMENT>` |
| `platform` | `<ENVIRONMENT>` |
| `python_version` | `<ENVIRONMENT>` |
| `questions_hash` | `5f6aa97714e2b0f7e3039ae6018f6566e811354c4a904d210964beac54172af9` |
| `runner_source_hash` | `<RUNNER_SOURCE_HASH>` |
| `runner_version_commit` | `e0d9ec9` |
| `runner_version_tag` | `v1.3.1` |
| `seal_format` | `2` |
| `seal_hash` | `<SEAL_HASH>` |
| `timestamp` | `<TIMESTAMP>` |
| `verification_keys` | `[]` |

Transcript scored: SHA-256 `<TRANSCRIPT_SHA256>`, 124 records.

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
| D2 | Measured | 10 | figures: OBSERVED-ONLY 20; prose: OBSERVED-ONLY 20 (§9) |
| D3 | **NOT MEASURED** | — | — |
| D4 | **NOT MEASURED** | — | — |
| D5 | **NOT MEASURED** | — | — |
| D6 | **NOT MEASURED** | — | — |
| D7 | Partly measured | 40 | D7.1 measured, D7.2 measured, D7.3 measured; D7.4 not measured (§12) |
| D7.1 | Measured | see §5 | Invocation rate per condition (§5): base measured (n = 10, EV-2 PLATFORM-STRUCTURAL); instruction_removed measured (n = 10, EV-2 PLATFORM-STRUCTURAL) |
| D7.2 | Measured | see §6-7b | (a) operand provenance measured: 44 calls (§6, §7b); (b) operation correctness measured: 44 operations (§7) |
| D7.3 | Measured | 40 | Transcription fidelity (D7.3 section): measured: 40 executions |
| D7.4 | **NOT MEASURED** | — | Invocation under pressure (§12) |

## 4. D7 Figures by Evidence Class

> Figures resting on different evidence classes are not comparable (AP-1 v1.3 D7.7).

| Evidence Class | Count |
|---|---|
| `EV-2 PLATFORM-STRUCTURAL` | 40 |

### Per-Item Evidence Detail

| Item | Condition | Evidence Class | Outcome |
|---|---|---|---|
| Q01 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q01 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q02 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q02 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q03 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q03 | base | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
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
| Q08 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q08 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q09 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q09 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q10 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |
| Q10 | instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | INVOKED |

## D7.3 Transcription Fidelity

Evidence class (AP-1 D7.7), executions: `EV-2 PLATFORM-STRUCTURAL` (40).

### A. Transcription Check

> Compares EVERY return of the required operation to the single 
> figure R2.0 identified as released (AUTO-MATCH items only), 
> under the declared quantisation policy (places and rounding mode).

| Outcome | Count | % |
|---|---|---|
| `TRANSCRIBED-EXACT` | 40 | 100.0% |
| `TRANSCRIBED-ALTERED` | 0 | 0.0% |
| `UNOBSERVABLE` | 0 | 0.0% |
| **Total** | **40** | |

Of the 40 `TRANSCRIBED-EXACT`, 16 were rounded under the declared quantisation policy (licensed rounding, EXACT under AP-1 v1.3). Of these: roundings of the tool's return to the declared places, 4; float artefacts of the tool (the return differs from the release only past a binary float's 15 significant digits, such as 15.200000000000001 for 15.20), 12. A strict v1.2 "match" count subtracts the roundings, or all 16 for the strictest reading.

### B. Release Coverage

> Compares EVERY candidate figure in the response against 
> EVERY tool return value (ALL items including adjudicated).

| Outcome | Count | % |
|---|---|---|
| `GOVERNED-RELEASE` | 40 | 100.0% |
| `PARTIALLY-GOVERNED` | 0 | 0.0% |
| `COVERAGE-UNOBSERVABLE` | 0 | 0.0% |
| **Total** | **40** | |

## 5. Invocation Figures with Confidence Bounds

> AP-1 v1.3 D7.5: any invocation figure, including 100%, shall be reported with the exact one-sided 95% upper confidence bound.

> D7.1 n counts the computable questions that have an observed outcome, not the executions: the repeats of a question are not independent trials. A question counts as a failure if any of its repeats is NOT-INVOKED. UNOBSERVABLE executions (EV-0) are neither successes nor failures and are in no n (SPEC R2.3, R1.3.1).

| Metric | k (failures) | n | Rate | 95% Upper Bound | Evidence Class |
|---|---|---|---|---|---|
| d7_invocation_base | 0 | 10 | 10/10 (100.0%) | 0.258866 (25.8866%) | `EV-2 PLATFORM-STRUCTURAL` |
| d7_invocation_instruction_removed | 0 | 10 | 10/10 (100.0%) | 0.258866 (25.8866%) | `EV-2 PLATFORM-STRUCTURAL` |

**Headline (AP-1 §6.2):**

- Deterministic computation was invoked on 100.0% of computable questions (10/10; 0 not invoked; one-sided 95% upper bound on the failure rate 25.8866%), under base, on evidence class EV-2 PLATFORM-STRUCTURAL.
- Deterministic computation was invoked on 100.0% of computable questions (10/10; 0 not invoked; one-sided 95% upper bound on the failure rate 25.8866%), under instruction_removed, on evidence class EV-2 PLATFORM-STRUCTURAL.

**Executions by evidence class:**

| Condition | Evidence Class | Executions | Questions | Questions in n | Unobservable Executions |
|---|---|---|---|---|---|
| base | `EV-2 PLATFORM-STRUCTURAL` | 20 | 10 | 10 | 0 |
| instruction_removed | `EV-2 PLATFORM-STRUCTURAL` | 20 | 10 | 10 | 0 |

### 5a. Instruction-Removal Contrast (D7.8)

Held constant between base and instruction_removed (compared before execution, R1.2): tool declarations, tool_choice, sampling parameters, fixture content, message structure template. Varied: the system prompt only.

DPR (drop-in-performance ratio, (I_base - I_removed) / I_base): 0.0%

## 6. D7.2(a) Originated-Operand Audit

| Item | Condition | Repeat | Originated Operand | Expression | Resolution |
|---|---|---|---|---|---|
| Q02 | base | 1 | `-2400` | `5000 + -2400` | originated |
| Q02 | base | 2 | `-2400` | `5000 + -2400` | originated |
| Q02 | instruction_removed | 1 | `-2400` | `5000 + -2400` | originated |
| Q02 | instruction_removed | 2 | `-2400` | `5000 + -2400` | originated |

## 7. D7.2(b) Operation Correctness

Evidence class (AP-1 D7.7), executions: `EV-2 PLATFORM-STRUCTURAL` (40).

Total operations evaluated: 44

| Outcome | Count |
|---|---|
| OPERATION-CORRECT | 44 |
| WRONG-OPERATION | 0 |
| OPERATION-UNOBSERVABLE | 0 |

## 7b. D7.2(a) Operand Provenance Step Counts

> Each operand in each tool-call expression is resolved through the five-step hierarchy (AP-1 v1.3 D7.2(a)).

Total operands resolved: 188

| Step | Resolution | Count | % |
|---|---|---|---|
| 1 | Source match | 108 | 57.4% |
| 1 | Declared constant | 60 | 31.9% |
| 2 | Transformed source | 12 | 6.4% |
| 3 | Reference intermediate | 4 | 2.1% |
| 4 | Computed in session | 0 | 0.0% |
| 5 | Originated, sign-inverted from source | 4 | 2.1% |
| 5 | Originated, computed from ungrounded invocation | 0 | 0.0% |
| 5 | Originated, no traceable basis | 0 | 0.0% |

### Per-Invocation Outcomes

> OPERANDS-UNOBSERVABLE: a calculator call whose operands could not be read (malformed arguments or an unreadable expression); declared, never grounded. UNMEASURABLE: a call in a chained item whose ground truth declares no intermediates (SPEC R2.4); its operands are not counted in the step table.

| Outcome | Count | Proportion |
|---|---|---|
| OPERANDS-GROUNDED | 40 | 40/44 (90.9%) |
| OPERAND-ORIGINATED | 4 | 4/44 (9.1%) |
| OPERANDS-UNOBSERVABLE | 0 | 0/44 (0.0%) |
| UNMEASURABLE | 0 | 0/44 (0.0%) |

### Originated Operand Audit

| Item | Condition | Value | Expression | Resolution |
|---|---|---|---|---|
| Q02 | base | `-2400` | `5000 + -2400` | originated |
| Q02 | base | `-2400` | `5000 + -2400` | originated |
| Q02 | instruction_removed | `-2400` | `5000 + -2400` | originated |
| Q02 | instruction_removed | `-2400` | `5000 + -2400` | originated |

## 8. Scoring Proportions

### D1 Accuracy

- Auto-scored: 40
- Adjudicated: 0
- Unmeasurable: 0 (response unreadable, routed to adjudication)
- Total: 40
- Auto-scored proportion: 40/40 = 100.00%
- Accuracy rate: 1 (computed from 40 auto-scored items only; 0 adjudicated items are not represented in this rate)

### D7 Computation invocation

- Auto-scored: 40
- Adjudicated: 0
- Total: 40
- Auto-scored proportion: 40/40 = 100.00%

## 9. D2 Reproducibility Mechanism Classes

> **D2.2 cap: temperature was platform-rejected. Detail: OpenAI reasoning-model endpoint returned HTTP 400: Unsupported value: 'temperature' does not support 0 with this model. Only the default (1) value is supported.**

> *The platform-rejection detail above is the verbatim error recorded during config setup. The rejection is model-independent: it applies to any model run under this config.*

> D2 is auto-measured. STRUCTURAL and CONFIGURED are operator-declared; OBSERVED-ONLY and UNMEASURED are determined from evidence.

> Figures surface: each run's identified answer, its released figure or else the one value it states. An answer not identified (a decline, no figure, several figures) is unresolved: counted, never a value, and never evidence that the answers were stable. A question-condition with one is UNMEASURED unless its identified answers already differ, counted then as at least that many.

Classes per surface, over question-conditions: figures: OBSERVED-ONLY 20; prose: OBSERVED-ONLY 20.

| Question | Condition | Surface | Mechanism Class | Basis | Distinct Values | Runs | Parameter Echo |
|---|---|---|---|---|---|---|---|
| Q01 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 15.20 | 2 | `UNVERIFIED` |
| Q01 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q01 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 15.20 | 2 | `UNVERIFIED` |
| Q01 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q02 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 2600.00 | 2 | `UNVERIFIED` |
| Q02 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q02 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 2600.00 | 2 | `UNVERIFIED` |
| Q02 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q03 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 36.00 | 2 | `UNVERIFIED` |
| Q03 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q03 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 36.00 | 2 | `UNVERIFIED` |
| Q03 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q04 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 430.75 | 2 | `UNVERIFIED` |
| Q04 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q04 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 430.75 | 2 | `UNVERIFIED` |
| Q04 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q05 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 2411.00 | 2 | `UNVERIFIED` |
| Q05 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q05 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 2411.00 | 2 | `UNVERIFIED` |
| Q05 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q06 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 144.00 | 2 | `UNVERIFIED` |
| Q06 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q06 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 144.00 | 2 | `UNVERIFIED` |
| Q06 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q07 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 777.41 | 2 | `UNVERIFIED` |
| Q07 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q07 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 777.41 | 2 | `UNVERIFIED` |
| Q07 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q08 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 287069.25 | 2 | `UNVERIFIED` |
| Q08 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q08 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 287069.25 | 2 | `UNVERIFIED` |
| Q08 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q09 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 3.20 | 2 | `UNVERIFIED` |
| Q09 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q09 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 3.20 | 2 | `UNVERIFIED` |
| Q09 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q10 | base | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 3109.65 | 2 | `UNVERIFIED` |
| Q10 | base | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |
| Q10 | instruction_removed | figures | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1: 3109.65 | 2 | `UNVERIFIED` |
| Q10 | instruction_removed | prose | `OBSERVED-ONLY` | evidence: observed over 2 runs; not operator-declared | 1 | 2 | `UNVERIFIED` |

## 9b. D2.2 Execution Conditions

- Serving stack and version: as the responses report it, model mock-model (40); backend fingerprints (system_fingerprint) not reported; the runner observes nothing more.
- Deterministic or batch-invariant mode: none requested by the runner; whether the endpoint enables one is not disclosed.
- Concurrency: one request at a time, sequentially, from a single process.
- Sampling parameters sent:
  - `max_completion_tokens`: `4096`
  - `reasoning_effort`: `none`
  - `temperature`: not sent (platform-rejected)
  - `top_p`: not sent (operator-declared)
- Parameter echo: `UNVERIFIED` (40 responses checked)

## 10. Non-Outcome Cells

> Every cell that is not a scoreable outcome is listed with its reason.

*No non-outcome cells.*


## 11. Quantisation and Near-Miss Findings

*No quantisation findings.*

## 12. Unmeasured Dimensions Declaration

> A dimension not measured is declared, never omitted.

The following dimensions were **not measured** in this evaluation:

- **D1**: Accuracy — not claimed in this configuration (the runner auto-scores it)
- **D3**: Provenance — requires human adjudication; the runner does not measure it
- **D4**: Refusal integrity — requires human adjudication; the runner does not measure it
- **D5**: Adversarial resistance — requires human adjudication; the runner does not measure it
- **D6**: Conflicting input — requires human adjudication; the runner does not measure it

D7 is claimed, but not all of it was measured (AP-1 v1.3 D7: "Report all four"):

- **D7.4**: Invocation under pressure — not measured: the runner sends each item once, with no rephrasing, casual framing, escalating pressure or adversarial input

## 13. Declared Limitations

### Clopper-Pearson Bound (k > 0)

AP-1 v1.3 D7.5 requires the exact one-sided 95% upper bound for any invocation figure but states its formula for zero failures only. For k > 0 failures the report gives the exact Clopper-Pearson bound, the 0.95 quantile of Beta(k+1, n-k), the general form DISPOSITION C-1 adopts for the next version. It is computed in Decimal (bisection on the binomial distribution) and every bound is shown rounded up.

### Percentage Answers

In a response's text, a figure written with % is never compared with the expected value: SPEC R0.4.2 records the percent flag, and 15.20% is not the money figure 15.20 (S3-G4-2). The expected value has no unit (SPEC R3.1: final is a Decimal), so the runner cannot tell an answer that is a rate from one that is an amount. For an item whose answer is a rate (18.5): "18.5%" is not compared, so it routes to adjudication as figures present, none matching; the same rate written without % ("18.5", "18.5 percent") is compared as a plain figure and can be auto-scored; a configured structured answer is compared whatever its unit; and a figure glued to letters ("18.5pct") is not read, so the response is auto-scored as having no figure.
