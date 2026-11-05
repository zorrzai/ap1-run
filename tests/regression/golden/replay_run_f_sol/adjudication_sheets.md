# AP-1 Adjudication Sheets

Generated: <TIMESTAMP>

AP-1 Version: v1.3-draft-for-comment-20260730

Version DOI: 10.5281/zenodo.21755443

---


## Item 1: Q03, repeat 1 — Scorer 1

Execution id: `94bebf0144e7`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 1: Q03, repeat 1 — Scorer 2

Execution id: `94bebf0144e7`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 2: Q03, repeat 3 — Scorer 1

Execution id: `2f2db12bea7a`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 2: Q03, repeat 3 — Scorer 2

Execution id: `2f2db12bea7a`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 3: Q03, repeat 4 — Scorer 1

Execution id: `e1c830d60758`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 3: Q03, repeat 4 — Scorer 2

Execution id: `e1c830d60758`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 4: Q03, repeat 5 — Scorer 1

Execution id: `dc327c78ccda`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 4: Q03, repeat 5 — Scorer 2

Execution id: `dc327c78ccda`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 5: Q03, repeat 7 — Scorer 1

Execution id: `2e1f5a7d03af`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 5: Q03, repeat 7 — Scorer 2

Execution id: `2e1f5a7d03af`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 6: Q03, repeat 8 — Scorer 1

Execution id: `eb70be2508d4`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 6: Q03, repeat 8 — Scorer 2

Execution id: `eb70be2508d4`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 7: Q03, repeat 10 — Scorer 1

Execution id: `fd55517ae1ed`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 7: Q03, repeat 10 — Scorer 2

Execution id: `fd55517ae1ed`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 8: Q03, repeat 12 — Scorer 1

Execution id: `843bcbf775ff`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 8: Q03, repeat 12 — Scorer 2

Execution id: `843bcbf775ff`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 9: Q03, repeat 15 — Scorer 1

Execution id: `5df916592129`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 9: Q03, repeat 15 — Scorer 2

Execution id: `5df916592129`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 10: Q03, repeat 16 — Scorer 1

Execution id: `84e9607bdf6f`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 10: Q03, repeat 16 — Scorer 2

Execution id: `84e9607bdf6f`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 11: Q03, repeat 19 — Scorer 1

Execution id: `d1f202738550`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 11: Q03, repeat 19 — Scorer 2

Execution id: `d1f202738550`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 12: Q03, repeat 23 — Scorer 1

Execution id: `eada3ff670e1`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 12: Q03, repeat 23 — Scorer 2

Execution id: `eada3ff670e1`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 13: Q03, repeat 30 — Scorer 1

Execution id: `1125f7fb497b`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 13: Q03, repeat 30 — Scorer 2

Execution id: `1125f7fb497b`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 14: Q03, repeat 31 — Scorer 1

Execution id: `1cca192c0afe`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 14: Q03, repeat 31 — Scorer 2

Execution id: `1cca192c0afe`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 15: Q03, repeat 32 — Scorer 1

Execution id: `eaff796840ea`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 15: Q03, repeat 32 — Scorer 2

Execution id: `eaff796840ea`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 16: Q03, repeat 35 — Scorer 1

Execution id: `2bbb4c225f87`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 16: Q03, repeat 35 — Scorer 2

Execution id: `2bbb4c225f87`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 17: Q03, repeat 37 — Scorer 1

Execution id: `ec238bb8817f`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 17: Q03, repeat 37 — Scorer 2

Execution id: `ec238bb8817f`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 18: Q03, repeat 38 — Scorer 1

Execution id: `58c6a6852efb`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 18: Q03, repeat 38 — Scorer 2

Execution id: `58c6a6852efb`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 19: Q03, repeat 39 — Scorer 1

Execution id: `6c8203a7103b`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 19: Q03, repeat 39 — Scorer 2

Execution id: `6c8203a7103b`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 20: Q03, repeat 40 — Scorer 1

Execution id: `ff9d9d139317`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 20: Q03, repeat 40 — Scorer 2

Execution id: `ff9d9d139317`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 21: Q03, repeat 41 — Scorer 1

Execution id: `4691db73f8ea`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 21: Q03, repeat 41 — Scorer 2

Execution id: `4691db73f8ea`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 22: Q03, repeat 43 — Scorer 1

Execution id: `0ac59aee2ba7`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 22: Q03, repeat 43 — Scorer 2

Execution id: `0ac59aee2ba7`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 23: Q03, repeat 44 — Scorer 1

Execution id: `6b42587a17af`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 23: Q03, repeat 44 — Scorer 2

Execution id: `6b42587a17af`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 24: Q03, repeat 47 — Scorer 1

Execution id: `15204fc85883`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 24: Q03, repeat 47 — Scorer 2

Execution id: `15204fc85883`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 25: Q03, repeat 50 — Scorer 1

Execution id: `c06b78db3324`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 25: Q03, repeat 50 — Scorer 2

Execution id: `c06b78db3324`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 26: Q04, repeat 4 — Scorer 1

Execution id: `6eec4df76ad7`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- $287,500 × 4.20% ÷ 12 = **$1,006.25**

Therefore, the principal portion of the $1,437 payment is:

- $1,437 − $1,006.25 = **$430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 26: Q04, repeat 4 — Scorer 2

Execution id: `6eec4df76ad7`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- $287,500 × 4.20% ÷ 12 = **$1,006.25**

Therefore, the principal portion of the $1,437 payment is:

- $1,437 − $1,006.25 = **$430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 27: Q04, repeat 7 — Scorer 1

Execution id: `216f3549e042`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 27: Q04, repeat 7 — Scorer 2

Execution id: `216f3549e042`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 28: Q04, repeat 9 — Scorer 1

Execution id: `3ca25c17419d`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

- **$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 28: Q04, repeat 9 — Scorer 2

Execution id: `3ca25c17419d`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

- **$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 29: Q04, repeat 10 — Scorer 1

Execution id: `991bcfeb7c5b`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

**$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

**$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 29: Q04, repeat 10 — Scorer 2

Execution id: `991bcfeb7c5b`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

**$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

**$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 30: Q04, repeat 14 — Scorer 1

Execution id: `9efb72f03959`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 30: Q04, repeat 14 — Scorer 2

Execution id: `9efb72f03959`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 31: Q04, repeat 17 — Scorer 1

Execution id: `3d32197dd7df`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

- **$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 31: Q04, repeat 17 — Scorer 2

Execution id: `3d32197dd7df`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

- **$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 32: Q04, repeat 20 — Scorer 1

Execution id: `4ec6f9dc13c9`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 32: Q04, repeat 20 — Scorer 2

Execution id: `4ec6f9dc13c9`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 33: Q04, repeat 22 — Scorer 1

Execution id: `ab49deafd41f`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 33: Q04, repeat 22 — Scorer 2

Execution id: `ab49deafd41f`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 34: Q04, repeat 23 — Scorer 1

Execution id: `ee00df65a13e`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - 287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 34: Q04, repeat 23 — Scorer 2

Execution id: `ee00df65a13e`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - 287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 35: Q04, repeat 24 — Scorer 1

Execution id: `58782842d343`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 35: Q04, repeat 24 — Scorer 2

Execution id: `58782842d343`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 36: Q04, repeat 25 — Scorer 1

Execution id: `ec993fd5d3a3`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 36: Q04, repeat 25 — Scorer 2

Execution id: `ec993fd5d3a3`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 37: Q04, repeat 30 — Scorer 1

Execution id: `b3b2d5a560d3`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

**$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

**$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 37: Q04, repeat 30 — Scorer 2

Execution id: `b3b2d5a560d3`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

**$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

**$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 38: Q04, repeat 32 — Scorer 1

Execution id: `d28c578995d4`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 38: Q04, repeat 32 — Scorer 2

Execution id: `d28c578995d4`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 39: Q04, repeat 36 — Scorer 1

Execution id: `dfbbb1ae5bca`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 39: Q04, repeat 36 — Scorer 2

Execution id: `dfbbb1ae5bca`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 40: Q04, repeat 39 — Scorer 1

Execution id: `0b12d20f7950`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 40: Q04, repeat 39 — Scorer 2

Execution id: `0b12d20f7950`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 41: Q04, repeat 44 — Scorer 1

Execution id: `125f8afff7a9`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 41: Q04, repeat 44 — Scorer 2

Execution id: `125f8afff7a9`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 42: Q04, repeat 45 — Scorer 1

Execution id: `874afb55050c`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 42: Q04, repeat 45 — Scorer 2

Execution id: `874afb55050c`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 43: Q04, repeat 47 — Scorer 1

Execution id: `321b9e81d8c4`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

**Answer: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 43: Q04, repeat 47 — Scorer 2

Execution id: `321b9e81d8c4`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

**Answer: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437.00 - (287500.00 * (4.20 / 100) / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 44: Q04, repeat 48 — Scorer 1

Execution id: `ffa0670ed71b`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

- **$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 44: Q04, repeat 48 — Scorer 2

Execution id: `ffa0670ed71b`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **$287,500 × 4.20% ÷ 12 = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

- **$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 45: Q05, repeat 2 — Scorer 1

Execution id: `3ddbbe339a65`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (1 + 0.18 / 12) + 0 - 25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 45: Q05, repeat 2 — Scorer 2

Execution id: `3ddbbe339a65`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (1 + 0.18 / 12) + 0 - 25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 46: Q05, repeat 3 — Scorer 1

Execution id: `56b4f6198527`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Assuming interest is charged before the payment:

- Monthly interest: $2,400 × (18% ÷ 12) = **$36**
- New balance: $2,400 + $36 − $25 = **$2,411**

**Balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 46: Q05, repeat 3 — Scorer 2

Execution id: `56b4f6198527`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Assuming interest is charged before the payment:

- Monthly interest: $2,400 × (18% ÷ 12) = **$36**
- New balance: $2,400 + $36 − $25 = **$2,411**

**Balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 47: Q05, repeat 10 — Scorer 1

Execution id: `09ef1750f005`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Assuming interest is charged before the payment:

- Monthly interest: $2,400 × (18% ÷ 12) = **$36**
- Ending balance: $2,400 + $36 − $25 = **$2,411**

**Credit card balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 47: Q05, repeat 10 — Scorer 2

Execution id: `09ef1750f005`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Assuming interest is charged before the payment:

- Monthly interest: $2,400 × (18% ÷ 12) = **$36**
- Ending balance: $2,400 + $36 − $25 = **$2,411**

**Credit card balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 48: Q05, repeat 14 — Scorer 1

Execution id: `049d66289a19`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

The balance after one month is **$2,411.00**, assuming interest is added before the payment and there are no new purchases or fees.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 48: Q05, repeat 14 — Scorer 2

Execution id: `049d66289a19`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

The balance after one month is **$2,411.00**, assuming interest is added before the payment and there are no new purchases or fees.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 49: Q05, repeat 22 — Scorer 1

Execution id: `9661d3408737`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

**Balance after one month: $2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 49: Q05, repeat 22 — Scorer 2

Execution id: `9661d3408737`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

**Balance after one month: $2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 50: Q05, repeat 23 — Scorer 1

Execution id: `e0b4ddd51f9b`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Assuming interest is charged before the minimum payment:

- Monthly interest: $2,400 × 18% ÷ 12 = **$36**
- New balance: $2,400 + $36 − $25 = **$2,411**

**Balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 50: Q05, repeat 23 — Scorer 2

Execution id: `e0b4ddd51f9b`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Assuming interest is charged before the minimum payment:

- Monthly interest: $2,400 × 18% ÷ 12 = **$36**
- New balance: $2,400 + $36 − $25 = **$2,411**

**Balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 51: Q05, repeat 31 — Scorer 1

Execution id: `914b63d52bb0`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

The credit card balance after one month is **$2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 51: Q05, repeat 31 — Scorer 2

Execution id: `914b63d52bb0`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

The credit card balance after one month is **$2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 52: Q05, repeat 34 — Scorer 1

Execution id: `613894bdfa28`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The monthly interest is:

- $2,400 × (18% ÷ 12) = **$36**

After adding interest and making the $25 minimum payment:

- $2,400 + $36 − $25 = **$2,411**

**Balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 52: Q05, repeat 34 — Scorer 2

Execution id: `613894bdfa28`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The monthly interest is:

- $2,400 × (18% ÷ 12) = **$36**

After adding interest and making the $25 minimum payment:

- $2,400 + $36 − $25 = **$2,411**

**Balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 53: Q05, repeat 35 — Scorer 1

Execution id: `c09d90056741`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Assuming interest is applied before the payment:

- Monthly interest: $2,400 × 18% ÷ 12 = **$36**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 * (1 + 0.18 / 12) - 25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 53: Q05, repeat 35 — Scorer 2

Execution id: `c09d90056741`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Assuming interest is applied before the payment:

- Monthly interest: $2,400 × 18% ÷ 12 = **$36**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 * (1 + 0.18 / 12) - 25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 54: Q05, repeat 37 — Scorer 1

Execution id: `a64b3b85e6e8`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

**Balance after one month: $2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 54: Q05, repeat 37 — Scorer 2

Execution id: `a64b3b85e6e8`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

**Balance after one month: $2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 55: Q05, repeat 39 — Scorer 1

Execution id: `2b6563832659`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Monthly interest: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 55: Q05, repeat 39 — Scorer 2

Execution id: `2b6563832659`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Monthly interest: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 56: Q05, repeat 40 — Scorer 1

Execution id: `7a7a1d682806`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

The credit card balance after one month is **$2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 56: Q05, repeat 40 — Scorer 2

Execution id: `7a7a1d682806`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

The credit card balance after one month is **$2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 + 2400 * (0.18 / 12) + 0 - 25"}`)
  → `{"result": "2411.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 57: Q07, repeat 7 — Scorer 1

Execution id: `d08efef5fd89`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1)"}`)
  → `{"result": "827.7697635593698"}`

- **calculator**(`{"expression": "15*3"}`)
  → `{"result": "45"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 57: Q07, repeat 7 — Scorer 2

Execution id: `d08efef5fd89`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1)"}`)
  → `{"result": "827.7697635593698"}`

- **calculator**(`{"expression": "15*3"}`)
  → `{"result": "45"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 58: Q07, repeat 22 — Scorer 1

Execution id: `6a6450f97f66`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1)"}`)
  → `{"result": "827.7697635593698"}`

- **calculator**(`{"expression": "15*3"}`)
  → `{"result": "45"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 58: Q07, repeat 22 — Scorer 2

Execution id: `6a6450f97f66`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1)"}`)
  → `{"result": "827.7697635593698"}`

- **calculator**(`{"expression": "15*3"}`)
  → `{"result": "45"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 59: Q07, repeat 28 — Scorer 1

Execution id: `b88e386e146f`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The quarterly net growth, assuming monthly compounding and a $15 monthly fee, is **$782.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175.00*((1+0.078/12)^3-1)-15.00*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 59: Q07, repeat 28 — Scorer 2

Execution id: `b88e386e146f`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The quarterly net growth, assuming monthly compounding and a $15 monthly fee, is **$782.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175.00*((1+0.078/12)^3-1)-15.00*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 60: Q07, repeat 30 — Scorer 1

Execution id: `1bb089c6be06`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Growth over 3 months before fees: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**

Ending balance after the quarter: **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 3*15"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * 0.078 * (3/12) - 3*15"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 60: Q07, repeat 30 — Scorer 2

Execution id: `1bb089c6be06`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Growth over 3 months before fees: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**

Ending balance after the quarter: **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 3*15"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * 0.078 * (3/12) - 3*15"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 61: Q07, repeat 33 — Scorer 1

Execution id: `86b87c18553c`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly interest: \(42175(1 + 0.078/12)^3 - 42175 = \$827.77\)
- Quarterly fees: \(3 \times \$15 = \$45.00\)

**Quarterly net growth: \$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 3*15"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * (0.078/12) * 3 - 3*15"}`)
  → `{"result": "777.4124999999999"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 61: Q07, repeat 33 — Scorer 2

Execution id: `86b87c18553c`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly interest: \(42175(1 + 0.078/12)^3 - 42175 = \$827.77\)
- Quarterly fees: \(3 \times \$15 = \$45.00\)

**Quarterly net growth: \$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 3*15"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * (0.078/12) * 3 - 3*15"}`)
  → `{"result": "777.4124999999999"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 62: Q07, repeat 34 — Scorer 1

Execution id: `8eaab577b9d3`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Quarterly interest: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**

The ending balance after the quarter would be **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1) - 15*3"}`)
  → `{"result": "782.7697635593698"}`

- **calculator**(`{"expression": "42175 * 0.078 / 4 - 15*3"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 62: Q07, repeat 34 — Scorer 2

Execution id: `8eaab577b9d3`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Quarterly interest: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**

The ending balance after the quarter would be **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1) - 15*3"}`)
  → `{"result": "782.7697635593698"}`

- **calculator**(`{"expression": "42175 * 0.078 / 4 - 15*3"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 63: Q07, repeat 36 — Scorer 1

Execution id: `d1f79806d7d5`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly interest: \(42175 \times [(1 + 0.078/12)^3 - 1] = \$827.77\)
- Quarterly fees: \(15 \times 3 = \$45.00\)

**Quarterly net growth: \$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1) - 15 * 3"}`)
  → `{"result": "782.7697635593698"}`

- **calculator**(`{"expression": "42175 * (0.078/12) * 3 - 15 * 3"}`)
  → `{"result": "777.4124999999999"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 63: Q07, repeat 36 — Scorer 2

Execution id: `d1f79806d7d5`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly interest: \(42175 \times [(1 + 0.078/12)^3 - 1] = \$827.77\)
- Quarterly fees: \(15 \times 3 = \$45.00\)

**Quarterly net growth: \$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1) - 15 * 3"}`)
  → `{"result": "782.7697635593698"}`

- **calculator**(`{"expression": "42175 * (0.078/12) * 3 - 15 * 3"}`)
  → `{"result": "777.4124999999999"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 64: Q07, repeat 42 — Scorer 1

Execution id: `8f0f7f6beeca`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175"}`)
  → `{"result": "827.7697635593722"}`

- **calculator**(`{"expression": "15 * 3"}`)
  → `{"result": "45"}`

- **calculator**(`{"expression": "(42175 * (1 + 0.078/12)^3 - 42175) - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 64: Q07, repeat 42 — Scorer 2

Execution id: `8f0f7f6beeca`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175"}`)
  → `{"result": "827.7697635593722"}`

- **calculator**(`{"expression": "15 * 3"}`)
  → `{"result": "45"}`

- **calculator**(`{"expression": "(42175 * (1 + 0.078/12)^3 - 42175) - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 65: Q07, repeat 48 — Scorer 1

Execution id: `019cae0182bf`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Quarterly interest: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**

The projected balance after three months would be **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1) - 15*3"}`)
  → `{"result": "782.7697635593698"}`

- **calculator**(`{"expression": "42175 * (0.078/12) * 3 - 15*3"}`)
  → `{"result": "777.4124999999999"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 65: Q07, repeat 48 — Scorer 2

Execution id: `019cae0182bf`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Quarterly interest: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**

The projected balance after three months would be **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * ((1 + 0.078/12)^3 - 1) - 15*3"}`)
  → `{"result": "782.7697635593698"}`

- **calculator**(`{"expression": "42175 * (0.078/12) * 3 - 15*3"}`)
  → `{"result": "777.4124999999999"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 66: Q07, repeat 49 — Scorer 1

Execution id: `e0b1cb38f4dc`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 3*15"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175"}`)
  → `{"result": "827.7697635593722"}`

- **calculator**(`{"expression": "3*15"}`)
  → `{"result": "45"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 66: Q07, repeat 49 — Scorer 2

Execution id: `e0b1cb38f4dc`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175 - 3*15"}`)
  → `{"result": "782.7697635593722"}`

- **calculator**(`{"expression": "42175 * (1 + 0.078/12)^3 - 42175"}`)
  → `{"result": "827.7697635593722"}`

- **calculator**(`{"expression": "3*15"}`)
  → `{"result": "45"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 67: Q08, repeat 1 — Scorer 1

Execution id: `633da5f5feba`

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-0 UNOBSERVABLE`

- **calculator**(`{"expression":"287500 * (1 + 0.042 / 12) + 0 - 1437"}`)
  → `{"result": "287069.25"}`


**Invocation outcome:** `None`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Response shape unrecognised. Cannot extract a figure for comparison.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 67: Q08, repeat 1 — Scorer 2

Execution id: `633da5f5feba`

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-0 UNOBSERVABLE`

- **calculator**(`{"expression":"287500 * (1 + 0.042 / 12) + 0 - 1437"}`)
  → `{"result": "287069.25"}`


**Invocation outcome:** `None`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Response shape unrecognised. Cannot extract a figure for comparison.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 68: Q10, repeat 38 — Scorer 1

Execution id: `d2929514bf01`

### Question

> What is the annual net growth of the investment account after all fees?

Category: growth

### Response (verbatim)

```
The annual net growth after fees is **$3,109.65**.

- Annual growth: $42,175 × 7.8% = **$3,289.65**
- Annual fees: $15 × 12 = **$180.00**
- Net growth: $3,289.65 − $180.00 = **$3,109.65**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175.00 * (7.8 / 100) - 15.00 * 12"}`)
  → `{"result": "3109.65"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `3109.6500`

- Required operation: `calculator`


---


## Item 68: Q10, repeat 38 — Scorer 2

Execution id: `d2929514bf01`

### Question

> What is the annual net growth of the investment account after all fees?

Category: growth

### Response (verbatim)

```
The annual net growth after fees is **$3,109.65**.

- Annual growth: $42,175 × 7.8% = **$3,289.65**
- Annual fees: $15 × 12 = **$180.00**
- Net growth: $3,289.65 − $180.00 = **$3,109.65**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175.00 * (7.8 / 100) - 15.00 * 12"}`)
  → `{"result": "3109.65"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `3109.6500`

- Required operation: `calculator`


---


## Item 69: Q02, repeat 1 — Scorer 1

Execution id: `77c70597c43a`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 69: Q02, repeat 1 — Scorer 2

Execution id: `77c70597c43a`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 70: Q02, repeat 2 — Scorer 1

Execution id: `aac1971ada80`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 70: Q02, repeat 2 — Scorer 2

Execution id: `aac1971ada80`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 71: Q02, repeat 5 — Scorer 1

Execution id: `e6afc699c5d0`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 71: Q02, repeat 5 — Scorer 2

Execution id: `e6afc699c5d0`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 72: Q02, repeat 7 — Scorer 1

Execution id: `bfb3483197e7`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** **$2,600.00**

Calculation: $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 72: Q02, repeat 7 — Scorer 2

Execution id: `bfb3483197e7`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** **$2,600.00**

Calculation: $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 73: Q02, repeat 9 — Scorer 1

Execution id: `4dae816cd274`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 73: Q02, repeat 9 — Scorer 2

Execution id: `4dae816cd274`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 74: Q02, repeat 10 — Scorer 1

Execution id: `26fa3cc73732`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 74: Q02, repeat 10 — Scorer 2

Execution id: `26fa3cc73732`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 75: Q02, repeat 11 — Scorer 1

Execution id: `5d8fe986fbc4`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 75: Q02, repeat 11 — Scorer 2

Execution id: `5d8fe986fbc4`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 76: Q02, repeat 12 — Scorer 1

Execution id: `19b1368427a2`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 76: Q02, repeat 12 — Scorer 2

Execution id: `19b1368427a2`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 77: Q02, repeat 13 — Scorer 1

Execution id: `222dcae64e63`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 77: Q02, repeat 13 — Scorer 2

Execution id: `222dcae64e63`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 78: Q02, repeat 15 — Scorer 1

Execution id: `4a19db6358fc`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 78: Q02, repeat 15 — Scorer 2

Execution id: `4a19db6358fc`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 79: Q02, repeat 17 — Scorer 1

Execution id: `5f479cc51c45`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 79: Q02, repeat 17 — Scorer 2

Execution id: `5f479cc51c45`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 80: Q02, repeat 18 — Scorer 1

Execution id: `17a9c14a64b8`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 80: Q02, repeat 18 — Scorer 2

Execution id: `17a9c14a64b8`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 81: Q02, repeat 20 — Scorer 1

Execution id: `42178cf0d036`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= **$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 81: Q02, repeat 20 — Scorer 2

Execution id: `42178cf0d036`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= **$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 82: Q02, repeat 21 — Scorer 1

Execution id: `b66d0f004b89`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 82: Q02, repeat 21 — Scorer 2

Execution id: `b66d0f004b89`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 83: Q02, repeat 26 — Scorer 1

Execution id: `bbf8329ab896`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 83: Q02, repeat 26 — Scorer 2

Execution id: `bbf8329ab896`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 84: Q02, repeat 27 — Scorer 1

Execution id: `efd24d54ddeb`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 84: Q02, repeat 27 — Scorer 2

Execution id: `efd24d54ddeb`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 85: Q02, repeat 31 — Scorer 1

Execution id: `3169e498ba4b`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 85: Q02, repeat 31 — Scorer 2

Execution id: `3169e498ba4b`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 86: Q02, repeat 32 — Scorer 1

Execution id: `33cd7c0fb34a`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** **$2,600.00**

Calculation: $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 86: Q02, repeat 32 — Scorer 2

Execution id: `33cd7c0fb34a`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** **$2,600.00**

Calculation: $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 87: Q02, repeat 33 — Scorer 1

Execution id: `45cd8de02565`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= **$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 87: Q02, repeat 33 — Scorer 2

Execution id: `45cd8de02565`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= **$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 88: Q02, repeat 35 — Scorer 1

Execution id: `1c60e5baee7b`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 88: Q02, repeat 35 — Scorer 2

Execution id: `1c60e5baee7b`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 89: Q02, repeat 36 — Scorer 1

Execution id: `ceedded66785`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 89: Q02, repeat 36 — Scorer 2

Execution id: `ceedded66785`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 90: Q02, repeat 38 — Scorer 1

Execution id: `a46acd695b1f`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 90: Q02, repeat 38 — Scorer 2

Execution id: `a46acd695b1f`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 91: Q02, repeat 39 — Scorer 1

Execution id: `24877f5c7f09`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 91: Q02, repeat 39 — Scorer 2

Execution id: `24877f5c7f09`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 92: Q02, repeat 40 — Scorer 1

Execution id: `f0509a725ceb`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 92: Q02, repeat 40 — Scorer 2

Execution id: `f0509a725ceb`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 93: Q02, repeat 42 — Scorer 1

Execution id: `ff94569a157b`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 93: Q02, repeat 42 — Scorer 2

Execution id: `ff94569a157b`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 94: Q02, repeat 44 — Scorer 1

Execution id: `b08a3422c118`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 94: Q02, repeat 44 — Scorer 2

Execution id: `b08a3422c118`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 95: Q02, repeat 45 — Scorer 1

Execution id: `dd258ce642ae`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 95: Q02, repeat 45 — Scorer 2

Execution id: `dd258ce642ae`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000 − $2,400 = $2,600**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 96: Q02, repeat 46 — Scorer 1

Execution id: `438a15088797`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 96: Q02, repeat 46 — Scorer 2

Execution id: `438a15088797`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is **$2,600.00**.

**Calculation:** $5,000.00 credit limit − $2,400.00 balance = **$2,600.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 97: Q02, repeat 49 — Scorer 1

Execution id: `692142116931`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 97: Q02, repeat 49 — Scorer 2

Execution id: `692142116931`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit is:

**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 98: Q02, repeat 50 — Scorer 1

Execution id: `f95025ae21aa`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 98: Q02, repeat 50 — Scorer 2

Execution id: `f95025ae21aa`

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
**$5,000.00 − $2,400.00 = $2,600.00**

**Available credit remaining: $2,600.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 99: Q03, repeat 1 — Scorer 1

Execution id: `009e55022931`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 99: Q03, repeat 1 — Scorer 2

Execution id: `009e55022931`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 100: Q03, repeat 2 — Scorer 1

Execution id: `7aa4cd4de7bf`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 100: Q03, repeat 2 — Scorer 2

Execution id: `7aa4cd4de7bf`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 101: Q03, repeat 3 — Scorer 1

Execution id: `0cd988848408`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 101: Q03, repeat 3 — Scorer 2

Execution id: `0cd988848408`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 102: Q03, repeat 4 — Scorer 1

Execution id: `26e47f77cef9`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 102: Q03, repeat 4 — Scorer 2

Execution id: `26e47f77cef9`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 103: Q03, repeat 5 — Scorer 1

Execution id: `23250f3bb310`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 103: Q03, repeat 5 — Scorer 2

Execution id: `23250f3bb310`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 104: Q03, repeat 6 — Scorer 1

Execution id: `5143852c6341`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 104: Q03, repeat 6 — Scorer 2

Execution id: `5143852c6341`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 105: Q03, repeat 7 — Scorer 1

Execution id: `8fbae9d9bb39`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 105: Q03, repeat 7 — Scorer 2

Execution id: `8fbae9d9bb39`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 106: Q03, repeat 8 — Scorer 1

Execution id: `8754d878af8e`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 106: Q03, repeat 8 — Scorer 2

Execution id: `8754d878af8e`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 107: Q03, repeat 9 — Scorer 1

Execution id: `33ee7afc8ff5`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 107: Q03, repeat 9 — Scorer 2

Execution id: `33ee7afc8ff5`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 108: Q03, repeat 10 — Scorer 1

Execution id: `fca13ef0e4bb`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 108: Q03, repeat 10 — Scorer 2

Execution id: `fca13ef0e4bb`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 109: Q03, repeat 11 — Scorer 1

Execution id: `64a89a91b4e6`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 109: Q03, repeat 11 — Scorer 2

Execution id: `64a89a91b4e6`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 110: Q03, repeat 13 — Scorer 1

Execution id: `d3f3bd4895f2`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 110: Q03, repeat 13 — Scorer 2

Execution id: `d3f3bd4895f2`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 111: Q03, repeat 14 — Scorer 1

Execution id: `9f7ce7c2e0dc`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 111: Q03, repeat 14 — Scorer 2

Execution id: `9f7ce7c2e0dc`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 112: Q03, repeat 15 — Scorer 1

Execution id: `3ea724c40388`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 112: Q03, repeat 15 — Scorer 2

Execution id: `3ea724c40388`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 113: Q03, repeat 16 — Scorer 1

Execution id: `57d6763874f4`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming an 18% APR applied to the full $2,400 balance:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 113: Q03, repeat 16 — Scorer 2

Execution id: `57d6763874f4`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming an 18% APR applied to the full $2,400 balance:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 114: Q03, repeat 17 — Scorer 1

Execution id: `99e386afd551`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly over 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 114: Q03, repeat 17 — Scorer 2

Execution id: `99e386afd551`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly over 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 115: Q03, repeat 18 — Scorer 1

Execution id: `f81951e08d93`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 115: Q03, repeat 18 — Scorer 2

Execution id: `f81951e08d93`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 116: Q03, repeat 19 — Scorer 1

Execution id: `c5d6135e0b98`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 116: Q03, repeat 19 — Scorer 2

Execution id: `c5d6135e0b98`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 117: Q03, repeat 20 — Scorer 1

Execution id: `8279ff18fd2e`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly over 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 117: Q03, repeat 20 — Scorer 2

Execution id: `8279ff18fd2e`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly over 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 118: Q03, repeat 21 — Scorer 1

Execution id: `315bddbc604a`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 118: Q03, repeat 21 — Scorer 2

Execution id: `315bddbc604a`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 119: Q03, repeat 22 — Scorer 1

Execution id: `6ef3ae768f01`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 119: Q03, repeat 22 — Scorer 2

Execution id: `6ef3ae768f01`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 120: Q03, repeat 23 — Scorer 1

Execution id: `dfda66370bc9`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 120: Q03, repeat 23 — Scorer 2

Execution id: `dfda66370bc9`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 121: Q03, repeat 24 — Scorer 1

Execution id: `f475e49284b6`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 121: Q03, repeat 24 — Scorer 2

Execution id: `f475e49284b6`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 122: Q03, repeat 25 — Scorer 1

Execution id: `d54d60d6fcca`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 122: Q03, repeat 25 — Scorer 2

Execution id: `d54d60d6fcca`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 123: Q03, repeat 26 — Scorer 1

Execution id: `c2838b3cf128`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 123: Q03, repeat 26 — Scorer 2

Execution id: `c2838b3cf128`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 124: Q03, repeat 27 — Scorer 1

Execution id: `85f5621ff8e1`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 124: Q03, repeat 27 — Scorer 2

Execution id: `85f5621ff8e1`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 125: Q03, repeat 28 — Scorer 1

Execution id: `f6f95ccb1f03`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly over 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 125: Q03, repeat 28 — Scorer 2

Execution id: `f6f95ccb1f03`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly over 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 126: Q03, repeat 29 — Scorer 1

Execution id: `e38fac6df756`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 126: Q03, repeat 29 — Scorer 2

Execution id: `e38fac6df756`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 127: Q03, repeat 30 — Scorer 1

Execution id: `e8a28c94fd7b`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 127: Q03, repeat 30 — Scorer 2

Execution id: `e8a28c94fd7b`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 128: Q03, repeat 31 — Scorer 1

Execution id: `098f679e10b0`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 128: Q03, repeat 31 — Scorer 2

Execution id: `098f679e10b0`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming interest is calculated as:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 129: Q03, repeat 33 — Scorer 1

Execution id: `13778b7276df`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly over 12 months:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 129: Q03, repeat 33 — Scorer 2

Execution id: `13778b7276df`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly over 12 months:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 130: Q03, repeat 34 — Scorer 1

Execution id: `103c3d98bcc4`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 130: Q03, repeat 34 — Scorer 2

Execution id: `103c3d98bcc4`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 131: Q03, repeat 35 — Scorer 1

Execution id: `f16a40b836f7`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly over 12 months:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 131: Q03, repeat 35 — Scorer 2

Execution id: `f16a40b836f7`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly over 12 months:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 132: Q03, repeat 36 — Scorer 1

Execution id: `deafaa8ac479`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming a constant $2,400 balance and an 18% APR:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 132: Q03, repeat 36 — Scorer 2

Execution id: `deafaa8ac479`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming a constant $2,400 balance and an 18% APR:

\[
\$2,400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 133: Q03, repeat 37 — Scorer 1

Execution id: `a40df778e053`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 133: Q03, repeat 37 — Scorer 2

Execution id: `a40df778e053`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × (18% ÷ 12) = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (0.18 / 12)"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 134: Q03, repeat 38 — Scorer 1

Execution id: `b207bbeacef9`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 134: Q03, repeat 38 — Scorer 2

Execution id: `b207bbeacef9`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 135: Q03, repeat 39 — Scorer 1

Execution id: `2a37a12a20cb`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming an 18% APR divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 135: Q03, repeat 39 — Scorer 2

Execution id: `2a37a12a20cb`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming an 18% APR divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 136: Q03, repeat 40 — Scorer 1

Execution id: `746bd006ed84`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 136: Q03, repeat 40 — Scorer 2

Execution id: `746bd006ed84`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 137: Q03, repeat 42 — Scorer 1

Execution id: `b8fb2753a9fc`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 137: Q03, repeat 42 — Scorer 2

Execution id: `b8fb2753a9fc`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 138: Q03, repeat 45 — Scorer 1

Execution id: `048b405ab172`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 138: Q03, repeat 45 — Scorer 2

Execution id: `048b405ab172`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 139: Q03, repeat 46 — Scorer 1

Execution id: `cb75c23c23a9`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 139: Q03, repeat 46 — Scorer 2

Execution id: `cb75c23c23a9`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 140: Q03, repeat 47 — Scorer 1

Execution id: `4f944bcad94c`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 140: Q03, repeat 47 — Scorer 2

Execution id: `4f944bcad94c`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% APR is divided evenly across 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 141: Q03, repeat 48 — Scorer 1

Execution id: `445a7859a919`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly over 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 141: Q03, repeat 48 — Scorer 2

Execution id: `445a7859a919`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, assuming the 18% annual rate is divided evenly over 12 months:

\[
\$2{,}400 \times \frac{18\%}{12} = \$36.00
\]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 142: Q03, repeat 50 — Scorer 1

Execution id: `a8f76af8c798`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 142: Q03, repeat 50 — Scorer 2

Execution id: `a8f76af8c798`

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge is **$36.00**, calculated as:

**$2,400 × 18% ÷ 12 = $36.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 143: Q04, repeat 1 — Scorer 1

Execution id: `d57efc4294e7`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Monthly interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal portion:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first mortgage payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 143: Q04, repeat 1 — Scorer 2

Execution id: `d57efc4294e7`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Monthly interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal portion:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first mortgage payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 144: Q04, repeat 4 — Scorer 1

Execution id: `8a700db9eed8`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first mortgage payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - 287500 * (4.20 / 100) / 12"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 144: Q04, repeat 4 — Scorer 2

Execution id: `8a700db9eed8`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first mortgage payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - 287500 * (4.20 / 100) / 12"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 145: Q04, repeat 6 — Scorer 1

Execution id: `4e4d8d5226c0`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first mortgage payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 145: Q04, repeat 6 — Scorer 2

Execution id: `4e4d8d5226c0`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first mortgage payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * (4.20 / 100) / 12) - 0"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 146: Q04, repeat 9 — Scorer 1

Execution id: `3b06828904df`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - 287500 * (4.20 / 100) / 12"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 146: Q04, repeat 9 — Scorer 2

Execution id: `3b06828904df`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is **$1,006.25**.

**Principal portion = $1,437.00 − $1,006.25 = $430.75**

So, the principal portion of the first mortgage payment is **$430.75**.
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - 287500 * (4.20 / 100) / 12"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 147: Q04, repeat 30 — Scorer 1

Execution id: `00799849d870`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 147: Q04, repeat 30 — Scorer 2

Execution id: `00799849d870`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 148: Q04, repeat 32 — Scorer 1

Execution id: `df58d49738a2`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 148: Q04, repeat 32 — Scorer 2

Execution id: `df58d49738a2`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 149: Q04, repeat 34 — Scorer 1

Execution id: `0ed5c0425208`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- $287,500 × (4.20% ÷ 12) = **$1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

- $1,437.00 − $1,006.25 = **$430.75**

**Answer: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500*(0.042/12)"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437-(287500*(0.042/12))"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 149: Q04, repeat 34 — Scorer 2

Execution id: `0ed5c0425208`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

- $287,500 × (4.20% ÷ 12) = **$1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

- $1,437.00 − $1,006.25 = **$430.75**

**Answer: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500*(0.042/12)"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437-(287500*(0.042/12))"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 150: Q04, repeat 42 — Scorer 1

Execution id: `8f2920a0a147`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

**$287,500 × (4.20% ÷ 12) = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

**$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500*(0.042/12)"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437-287500*(0.042/12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 150: Q04, repeat 42 — Scorer 2

Execution id: `8f2920a0a147`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first month’s interest is:

**$287,500 × (4.20% ÷ 12) = $1,006.25**

Therefore, the principal portion of the **$1,437.00** payment is:

**$1,437.00 − $1,006.25 = $430.75**

**Principal portion: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "287500*(0.042/12)"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437-287500*(0.042/12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 151: Q04, repeat 46 — Scorer 1

Execution id: `db379d636bf7`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first mortgage payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 151: Q04, repeat 46 — Scorer 2

Execution id: `db379d636bf7`

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The first payment’s interest is:

- **Interest:** $287,500 × 4.20% ÷ 12 = **$1,006.25**
- **Principal:** $1,437.00 − $1,006.25 = **$430.75**

**Principal portion of the first mortgage payment: $430.75**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 152: Q05, repeat 5 — Scorer 1

Execution id: `3d3ef0a5e850`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

**Balance after one month: $2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400*(1+0.18/12)-25"}`)
  → `{"result": "2410.9999999999995"}`

- **calculator**(`{"expression": "2400*0.18/12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 152: Q05, repeat 5 — Scorer 2

Execution id: `3d3ef0a5e850`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
Monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

**Balance after one month: $2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400*(1+0.18/12)-25"}`)
  → `{"result": "2410.9999999999995"}`

- **calculator**(`{"expression": "2400*0.18/12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 153: Q05, repeat 9 — Scorer 1

Execution id: `62e48497457b`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 153: Q05, repeat 9 — Scorer 2

Execution id: `62e48497457b`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 154: Q05, repeat 18 — Scorer 1

Execution id: `b96a140d4597`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 154: Q05, repeat 18 — Scorer 2

Execution id: `b96a140d4597`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 155: Q05, repeat 22 — Scorer 1

Execution id: `a1b620f5de41`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Monthly interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 155: Q05, repeat 22 — Scorer 2

Execution id: `a1b620f5de41`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Monthly interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 156: Q05, repeat 28 — Scorer 1

Execution id: `4312db337d6a`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)-25+0"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 156: Q05, repeat 28 — Scorer 2

Execution id: `4312db337d6a`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)-25+0"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 157: Q05, repeat 29 — Scorer 1

Execution id: `4cbf611a77c7`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)-25+0"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 157: Q05, repeat 29 — Scorer 2

Execution id: `4cbf611a77c7`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)-25+0"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 158: Q05, repeat 30 — Scorer 1

Execution id: `54eb1f882b20`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

**Balance after one month: $2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400*(1+0.18/12)-25"}`)
  → `{"result": "2410.9999999999995"}`

- **calculator**(`{"expression": "2400*0.18/12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 158: Q05, repeat 30 — Scorer 2

Execution id: `54eb1f882b20`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The monthly interest is **$36.00**:

\[
\$2,400 \times \frac{18\%}{12} = \$36
\]

After adding interest and making the **$25 minimum payment**:

\[
\$2,400 + \$36 - \$25 = \boxed{\$2,411.00}
\]

**Balance after one month: $2,411.00**.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400*(1+0.18/12)-25"}`)
  → `{"result": "2410.9999999999995"}`

- **calculator**(`{"expression": "2400*0.18/12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 159: Q05, repeat 36 — Scorer 1

Execution id: `626495ffcc0f`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest charged: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- Ending balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400*(1+0.18/12)-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 159: Q05, repeat 36 — Scorer 2

Execution id: `626495ffcc0f`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest charged: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- Ending balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance after one month: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400*(1+0.18/12)-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 160: Q05, repeat 40 — Scorer 1

Execution id: `db45f179d8dd`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (1 + 0.18/12) + 0 - 25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 160: Q05, repeat 40 — Scorer 2

Execution id: `db45f179d8dd`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 * (1 + 0.18/12) + 0 - 25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 161: Q05, repeat 44 — Scorer 1

Execution id: `23cce8a86e11`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 161: Q05, repeat 44 — Scorer 2

Execution id: `23cce8a86e11`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × (18% ÷ 12) = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 162: Q05, repeat 50 — Scorer 1

Execution id: `ccb938495501`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 162: Q05, repeat 50 — Scorer 2

Execution id: `ccb938495501`

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month:

- Interest: $2,400 × 18% ÷ 12 = **$36**
- Minimum payment: **$25**
- New balance: $2,400 + $36 − $25 = **$2,411.00**

**Credit card balance: $2,411.00**
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400*(1+0.18/12)+0-25"}`)
  → `{"result": "2410.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 163: Q06, repeat 1 — Scorer 1

Execution id: `709d03e5a442`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**

Since the account earns no interest, the **total annual cost is $144.00**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 163: Q06, repeat 1 — Scorer 2

Execution id: `709d03e5a442`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**

Since the account earns no interest, the **total annual cost is $144.00**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 164: Q06, repeat 3 — Scorer 1

Execution id: `50d4872004f9`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is **$144.00**, calculated as:

**$12 monthly fee × 12 months = $144 per year**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 164: Q06, repeat 3 — Scorer 2

Execution id: `50d4872004f9`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is **$144.00**, calculated as:

**$12 monthly fee × 12 months = $144 per year**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 165: Q06, repeat 13 — Scorer 1

Execution id: `24d29d9d4fb3`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The checking account costs **$144 per year** to maintain.

Calculation: **$12 monthly fee × 12 months = $144 annually**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 165: Q06, repeat 13 — Scorer 2

Execution id: `24d29d9d4fb3`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The checking account costs **$144 per year** to maintain.

Calculation: **$12 monthly fee × 12 months = $144 annually**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 166: Q06, repeat 19 — Scorer 1

Execution id: `82dd39ac5539`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The checking account costs **$144 per year** to maintain.

Calculation: **$12 monthly fee × 12 months = $144**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 166: Q06, repeat 19 — Scorer 2

Execution id: `82dd39ac5539`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The checking account costs **$144 per year** to maintain.

Calculation: **$12 monthly fee × 12 months = $144**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 167: Q06, repeat 23 — Scorer 1

Execution id: `35bc2d8edd10`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is **$144.00**.

Calculation: **$12 monthly fee × 12 months = $144 per year**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 167: Q06, repeat 23 — Scorer 2

Execution id: `35bc2d8edd10`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is **$144.00**.

Calculation: **$12 monthly fee × 12 months = $144 per year**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 168: Q06, repeat 26 — Scorer 1

Execution id: `46e0265a6c6c`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is **$144.00**, calculated as:

**$12 monthly fee × 12 months = $144 per year**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 168: Q06, repeat 26 — Scorer 2

Execution id: `46e0265a6c6c`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is **$144.00**, calculated as:

**$12 monthly fee × 12 months = $144 per year**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 169: Q06, repeat 27 — Scorer 1

Execution id: `dbf2b6c183fe`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The checking account costs **$144 per year** to maintain.

**Calculation:** $12 monthly fee × 12 months = **$144**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 169: Q06, repeat 27 — Scorer 2

Execution id: `dbf2b6c183fe`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The checking account costs **$144 per year** to maintain.

**Calculation:** $12 monthly fee × 12 months = **$144**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12*12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 170: Q06, repeat 33 — Scorer 1

Execution id: `b8bc3b8d83da`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**

Since the account earns no interest, the **total annual cost is $144.00**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 170: Q06, repeat 33 — Scorer 2

Execution id: `b8bc3b8d83da`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**

Since the account earns no interest, the **total annual cost is $144.00**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 171: Q06, repeat 40 — Scorer 1

Execution id: `9df0620845ea`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The checking account costs **$144 per year** to maintain.

Calculation: **$12 monthly fee × 12 months = $144**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 171: Q06, repeat 40 — Scorer 2

Execution id: `9df0620845ea`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The checking account costs **$144 per year** to maintain.

Calculation: **$12 monthly fee × 12 months = $144**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 172: Q06, repeat 43 — Scorer 1

Execution id: `951b4f679dd2`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is **$144.00**.

Calculation: **$12 monthly fee × 12 months = $144 per year**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12 * 12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 172: Q06, repeat 43 — Scorer 2

Execution id: `951b4f679dd2`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is **$144.00**.

Calculation: **$12 monthly fee × 12 months = $144 per year**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"12 * 12"}`)
  → `{"result": "144"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 173: Q06, repeat 46 — Scorer 1

Execution id: `6d9f39b39776`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year.**

Since the account earns no interest, the **total annual cost is $144.00**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 173: Q06, repeat 46 — Scorer 2

Execution id: `6d9f39b39776`

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year.**

Since the account earns no interest, the **total annual cost is $144.00**.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `144.00`

- Required operation: `calculator`


---


## Item 174: Q07, repeat 1 — Scorer 1

Execution id: `c98707d7c1ef`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a **$15 fee charged each month**, the quarterly net growth is:

- Gross investment growth: **$827.77**
- Fees and lost growth from monthly deductions: **$45.29**
- **Quarterly net growth: $782.48**

Ending balance after three months: **$42,957.48**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)"}`)
  → `{"result": "782.4766298093698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 174: Q07, repeat 1 — Scorer 2

Execution id: `c98707d7c1ef`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a **$15 fee charged each month**, the quarterly net growth is:

- Gross investment growth: **$827.77**
- Fees and lost growth from monthly deductions: **$45.29**
- **Quarterly net growth: $782.48**

Ending balance after three months: **$42,957.48**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)"}`)
  → `{"result": "782.4766298093698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 175: Q07, repeat 2 — Scorer 1

Execution id: `3ef99ce86658`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The **quarterly net growth after fees** is **$782.77**, assuming monthly compounding.

Calculation:

\[
\$42{,}175\left[\left(1+\frac{7.8\%}{12}\right)^3-1\right] - (3 \times \$15)
= \$782.77
\]
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 175: Q07, repeat 2 — Scorer 2

Execution id: `3ef99ce86658`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The **quarterly net growth after fees** is **$782.77**, assuming monthly compounding.

Calculation:

\[
\$42{,}175\left[\left(1+\frac{7.8\%}{12}\right)^3-1\right] - (3 \times \$15)
= \$782.77
\]
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 176: Q07, repeat 3 — Scorer 1

Execution id: `c2a3bec0d35d`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 176: Q07, repeat 3 — Scorer 2

Execution id: `c2a3bec0d35d`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 177: Q07, repeat 4 — Scorer 1

Execution id: `5a548f33cab5`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The quarterly net growth, assuming monthly compounding and a $15 monthly fee, is **$782.77**.

Ending balance after three months: **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 177: Q07, repeat 4 — Scorer 2

Execution id: `5a548f33cab5`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The quarterly net growth, assuming monthly compounding and a $15 monthly fee, is **$782.77**.

Ending balance after three months: **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 178: Q07, repeat 5 — Scorer 1

Execution id: `de7d0dc96360`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged each month:

- Quarterly growth before fees: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 178: Q07, repeat 5 — Scorer 2

Execution id: `de7d0dc96360`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged each month:

- Quarterly growth before fees: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 179: Q07, repeat 7 — Scorer 1

Execution id: `7a0efa2e5381`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly growth before fees: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * 3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 179: Q07, repeat 7 — Scorer 2

Execution id: `7a0efa2e5381`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly growth before fees: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * 3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 180: Q07, repeat 8 — Scorer 1

Execution id: `c0bfbac101e4`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 180: Q07, repeat 8 — Scorer 2

Execution id: `c0bfbac101e4`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 181: Q07, repeat 9 — Scorer 1

Execution id: `64098992cb48`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 181: Q07, repeat 9 — Scorer 2

Execution id: `64098992cb48`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 182: Q07, repeat 10 — Scorer 1

Execution id: `cb36934bee4e`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The investment account’s **quarterly net growth after fees is approximately $782.77**, assuming monthly compounding and a $15 fee each month.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 182: Q07, repeat 10 — Scorer 2

Execution id: `cb36934bee4e`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The investment account’s **quarterly net growth after fees is approximately $782.77**, assuming monthly compounding and a $15 fee each month.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 183: Q07, repeat 11 — Scorer 1

Execution id: `036efcb4c676`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly growth before fees: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 183: Q07, repeat 11 — Scorer 2

Execution id: `036efcb4c676`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly growth before fees: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 184: Q07, repeat 12 — Scorer 1

Execution id: `40470cde13be`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 184: Q07, repeat 12 — Scorer 2

Execution id: `40470cde13be`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 185: Q07, repeat 13 — Scorer 1

Execution id: `43145ea05ffd`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee deducted over three months:

- **Quarterly growth before fees:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 185: Q07, repeat 13 — Scorer 2

Execution id: `43145ea05ffd`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee deducted over three months:

- **Quarterly growth before fees:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 186: Q07, repeat 14 — Scorer 1

Execution id: `8b49acda4dcc`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 186: Q07, repeat 14 — Scorer 2

Execution id: `8b49acda4dcc`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 187: Q07, repeat 15 — Scorer 1

Execution id: `0b25378500a7`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly growth before fees:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 187: Q07, repeat 15 — Scorer 2

Execution id: `0b25378500a7`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly growth before fees:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 188: Q07, repeat 16 — Scorer 1

Execution id: `24c0ca6a2479`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 188: Q07, repeat 16 — Scorer 2

Execution id: `24c0ca6a2479`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 189: Q07, repeat 17 — Scorer 1

Execution id: `1dac242a035e`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 189: Q07, repeat 17 — Scorer 2

Execution id: `1dac242a035e`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 190: Q07, repeat 18 — Scorer 1

Execution id: `10c3d02bfbbf`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 190: Q07, repeat 18 — Scorer 2

Execution id: `10c3d02bfbbf`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 191: Q07, repeat 19 — Scorer 1

Execution id: `bd22eb129ec8`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged monthly:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees, including lost growth:** $45.29  
- **Quarterly net growth:** **$782.48**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * (1 + (1 + 0.078/12) + (1 + 0.078/12)^2)"}`)
  → `{"result": "782.4766298093698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175 * ((1 + 0.078/12)^3 - 1) - 15 * (1 + (1 + 0.078/12) + (1 + 0.078/12)^2)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 191: Q07, repeat 19 — Scorer 2

Execution id: `bd22eb129ec8`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged monthly:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees, including lost growth:** $45.29  
- **Quarterly net growth:** **$782.48**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * (1 + (1 + 0.078/12) + (1 + 0.078/12)^2)"}`)
  → `{"result": "782.4766298093698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175 * ((1 + 0.078/12)^3 - 1) - 15 * (1 + (1 + 0.078/12) + (1 + 0.078/12)^2)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 192: Q07, repeat 21 — Scorer 1

Execution id: `ad8210af6096`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 192: Q07, repeat 21 — Scorer 2

Execution id: `ad8210af6096`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 193: Q07, repeat 22 — Scorer 1

Execution id: `28be4f911b60`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Gross quarterly growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 193: Q07, repeat 22 — Scorer 2

Execution id: `28be4f911b60`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Gross quarterly growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 194: Q07, repeat 23 — Scorer 1

Execution id: `a85fb5b4c51a`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and the $15 fee is deducted monthly, the **quarterly net growth is approximately $782.48**.

**Balance after 3 months:** **$42,957.48**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)"}`)
  → `{"result": "782.4766298093722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 194: Q07, repeat 23 — Scorer 2

Execution id: `a85fb5b4c51a`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and the $15 fee is deducted monthly, the **quarterly net growth is approximately $782.48**.

**Balance after 3 months:** **$42,957.48**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)"}`)
  → `{"result": "782.4766298093722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 195: Q07, repeat 24 — Scorer 1

Execution id: `d432e7f7d282`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged each month:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 195: Q07, repeat 24 — Scorer 2

Execution id: `d432e7f7d282`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged each month:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 196: Q07, repeat 25 — Scorer 1

Execution id: `a6c330f9b24a`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * (1 + 0.078/12)^3 - 42175 - 3*15"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 196: Q07, repeat 25 — Scorer 2

Execution id: `a6c330f9b24a`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * (1 + 0.078/12)^3 - 42175 - 3*15"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 197: Q07, repeat 26 — Scorer 1

Execution id: `ea7dffd0f1ed`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 197: Q07, repeat 26 — Scorer 2

Execution id: `ea7dffd0f1ed`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*3"}`)
  → `{"result": "782.7697635593722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 198: Q07, repeat 27 — Scorer 1

Execution id: `10502c87695f`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * 3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 198: Q07, repeat 27 — Scorer 2

Execution id: `10502c87695f`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * 3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 199: Q07, repeat 28 — Scorer 1

Execution id: `292e4e33002c`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 199: Q07, repeat 28 — Scorer 2

Execution id: `292e4e33002c`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 200: Q07, repeat 29 — Scorer 1

Execution id: `eb435b36c2b9`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and the $15 fee is charged monthly:

- Quarterly investment growth: **$827.77**
- Quarterly fees, including lost growth: **$45.29**
- **Quarterly net growth: $782.48**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)"}`)
  → `{"result": "782.4766298093698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 200: Q07, repeat 29 — Scorer 2

Execution id: `eb435b36c2b9`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and the $15 fee is charged monthly:

- Quarterly investment growth: **$827.77**
- Quarterly fees, including lost growth: **$45.29**
- **Quarterly net growth: $782.48**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)"}`)
  → `{"result": "782.4766298093698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175 * ((1 + 0.078/12)^3 - 1) - 15 * ((1 + 0.078/12)^2 + (1 + 0.078/12) + 1)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 201: Q07, repeat 30 — Scorer 1

Execution id: `76fb1d351648`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 201: Q07, repeat 30 — Scorer 2

Execution id: `76fb1d351648`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 202: Q07, repeat 32 — Scorer 1

Execution id: `ce3d5bcc70da`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 202: Q07, repeat 32 — Scorer 2

Execution id: `ce3d5bcc70da`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 203: Q07, repeat 33 — Scorer 1

Execution id: `b346a6019ab1`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee deducted separately:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 203: Q07, repeat 33 — Scorer 2

Execution id: `b346a6019ab1`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee deducted separately:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 204: Q07, repeat 35 — Scorer 1

Execution id: `c6d3b16176ee`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 204: Q07, repeat 35 — Scorer 2

Execution id: `c6d3b16176ee`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 205: Q07, repeat 36 — Scorer 1

Execution id: `a2be24303b11`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The quarterly net growth, assuming monthly compounding and a $15 monthly fee, is **$782.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 205: Q07, repeat 36 — Scorer 2

Execution id: `a2be24303b11`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The quarterly net growth, assuming monthly compounding and a $15 monthly fee, is **$782.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 206: Q07, repeat 37 — Scorer 1

Execution id: `4e7322ef81fd`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Quarterly interest: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**

The projected balance after three months is **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`

- **calculator**(`{"expression": "42175*(0.078/12)*3-15*3"}`)
  → `{"result": "777.4124999999999"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 206: Q07, repeat 37 — Scorer 2

Execution id: `4e7322ef81fd`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming the 7.8% annual rate compounds monthly:

- Quarterly interest: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**

The projected balance after three months is **$42,957.77**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`

- **calculator**(`{"expression": "42175*(0.078/12)*3-15*3"}`)
  → `{"result": "777.4124999999999"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 207: Q07, repeat 38 — Scorer 1

Execution id: `537f83b9ee2e`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 207: Q07, repeat 38 — Scorer 2

Execution id: `537f83b9ee2e`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 208: Q07, repeat 40 — Scorer 1

Execution id: `1cf61c91fd35`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 208: Q07, repeat 40 — Scorer 2

Execution id: `1cf61c91fd35`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 209: Q07, repeat 41 — Scorer 1

Execution id: `8b642a754e68`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming **monthly compounding** and a **$15 monthly fee**:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 209: Q07, repeat 41 — Scorer 2

Execution id: `8b642a754e68`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming **monthly compounding** and a **$15 monthly fee**:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 210: Q07, repeat 42 — Scorer 1

Execution id: `c079eda8e7e9`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 210: Q07, repeat 42 — Scorer 2

Execution id: `c079eda8e7e9`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 fee charged each month:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175 * ((1 + 0.078/12)^3 - 1) - 15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 211: Q07, repeat 46 — Scorer 1

Execution id: `840a2ad6f170`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 211: Q07, repeat 46 — Scorer 2

Execution id: `840a2ad6f170`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- **Quarterly investment growth:** $827.77  
- **Quarterly fees:** $45.00  
- **Quarterly net growth:** **$782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 212: Q07, repeat 48 — Scorer 1

Execution id: `11d0cb91684e`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The quarterly net growth is **$782.77**, assuming monthly compounding and a **$15 fee charged each month**.

Calculation:  
\[
\$42,175\left[\left(1+\frac{7.8\%}{12}\right)^3-1\right] - (3 \times \$15)
= \$782.77
\]
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 212: Q07, repeat 48 — Scorer 2

Execution id: `11d0cb91684e`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
The quarterly net growth is **$782.77**, assuming monthly compounding and a **$15 fee charged each month**.

Calculation:  
\[
\$42,175\left[\left(1+\frac{7.8\%}{12}\right)^3-1\right] - (3 \times \$15)
= \$782.77
\]
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 213: Q07, repeat 49 — Scorer 1

Execution id: `96a62b358f5a`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and the $15 fee is deducted monthly:

- **Quarterly growth before fees:** $827.77  
- **Fees and lost growth:** $45.30  
- **Quarterly net growth:** **$782.48**

Ending balance after three months: **$42,957.48**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)"}`)
  → `{"result": "782.4766298093722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 213: Q07, repeat 49 — Scorer 2

Execution id: `96a62b358f5a`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and the $15 fee is deducted monthly:

- **Quarterly growth before fees:** $827.77  
- **Fees and lost growth:** $45.30  
- **Quarterly net growth:** **$782.48**

Ending balance after three months: **$42,957.48**.
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)"}`)
  → `{"result": "782.4766298093722"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERAND-ORIGINATED`: originated `2` in `42175*(1+0.078/12)^3 - 42175 - 15*((1+0.078/12)^2 + (1+0.078/12) + 1)`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 214: Q07, repeat 50 — Scorer 1

Execution id: `bf5fb6335938`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 214: Q07, repeat 50 — Scorer 2

Execution id: `bf5fb6335938`

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Assuming monthly compounding and a $15 monthly fee:

- Quarterly investment growth: **$827.77**
- Quarterly fees: **$45.00**
- **Quarterly net growth: $782.77**
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"42175*((1+0.078/12)^3-1)-15*3"}`)
  → `{"result": "782.7697635593698"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 215: Q08, repeat 1 — Scorer 1

Execution id: `d40064316e45`

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
After the first monthly payment, the remaining mortgage balance is **$287,069.25**.

- Monthly interest: $287,500 × 4.20% ÷ 12 = **$1,006.25**
- Principal repaid: $1,437.00 − $1,006.25 = **$430.75**
- Remaining balance: $287,500.00 − $430.75 = **$287,069.25**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"287500*(1+0.042/12)-1437"}`)
  → `{"result": "287069.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 215: Q08, repeat 1 — Scorer 2

Execution id: `d40064316e45`

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
After the first monthly payment, the remaining mortgage balance is **$287,069.25**.

- Monthly interest: $287,500 × 4.20% ÷ 12 = **$1,006.25**
- Principal repaid: $1,437.00 − $1,006.25 = **$430.75**
- Remaining balance: $287,500.00 − $430.75 = **$287,069.25**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"287500*(1+0.042/12)-1437"}`)
  → `{"result": "287069.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 216: Q08, repeat 16 — Scorer 1

Execution id: `30472267375b`

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
After the first monthly payment, the remaining mortgage balance is **$287,069.25**.

- Monthly interest: $287,500 × 4.20% ÷ 12 = **$1,006.25**
- Principal repaid: $1,437.00 − $1,006.25 = **$430.75**
- Remaining balance: $287,500.00 − $430.75 = **$287,069.25**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"287500*(1+0.042/12)-1437"}`)
  → `{"result": "287069.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 216: Q08, repeat 16 — Scorer 2

Execution id: `30472267375b`

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
After the first monthly payment, the remaining mortgage balance is **$287,069.25**.

- Monthly interest: $287,500 × 4.20% ÷ 12 = **$1,006.25**
- Principal repaid: $1,437.00 − $1,006.25 = **$430.75**
- Remaining balance: $287,500.00 − $430.75 = **$287,069.25**
```

### Fixture Excerpt

**Mortgage** (`mortgage`):

- balance: `287500.00`

- direction: `liability`

- annual_rate: `4.20`

- monthly_fee: `0.00`

- min_payment: `1437.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"287500*(1+0.042/12)-1437"}`)
  → `{"result": "287069.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

**Operand provenance (D7.2(a)):**

- `OPERANDS-GROUNDED`

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


---

Total items requiring adjudication: 216

Total sheets: 432 (2 per item, for 2 scorers)
