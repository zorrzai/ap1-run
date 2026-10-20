# AP-1 Adjudication Sheets

Generated: <TIMESTAMP>

AP-1 Version: v1.3-draft-for-comment-20260730

Version DOI: 10.5281/zenodo.21755443

---


## Item 1: Q03, repeat 1 — Scorer 1

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


## Item 71: Q02, repeat 3 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** $5,000.00 − $2,400.00 = **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 71: Q02, repeat 3 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** $5,000.00 − $2,400.00 = **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 72: Q02, repeat 4 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit = Credit limit − Balance**

$5,000.00 − $2,400.00 = **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 72: Q02, repeat 4 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit = Credit limit − Balance**

$5,000.00 − $2,400.00 = **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 73: Q02, repeat 5 — Scorer 1

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


## Item 73: Q02, repeat 5 — Scorer 2

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


## Item 74: Q02, repeat 6 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 74: Q02, repeat 6 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 75: Q02, repeat 7 — Scorer 1

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


## Item 75: Q02, repeat 7 — Scorer 2

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


## Item 76: Q02, repeat 8 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = $5,000.00 − $2,400.00 = **$2,600.00**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 76: Q02, repeat 8 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = $5,000.00 − $2,400.00 = **$2,600.00**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 77: Q02, repeat 9 — Scorer 1

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


## Item 77: Q02, repeat 9 — Scorer 2

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


## Item 78: Q02, repeat 10 — Scorer 1

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


## Item 78: Q02, repeat 10 — Scorer 2

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


## Item 79: Q02, repeat 11 — Scorer 1

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


## Item 79: Q02, repeat 11 — Scorer 2

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


## Item 80: Q02, repeat 12 — Scorer 1

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


## Item 80: Q02, repeat 12 — Scorer 2

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


## Item 81: Q02, repeat 13 — Scorer 1

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


## Item 81: Q02, repeat 13 — Scorer 2

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


## Item 82: Q02, repeat 15 — Scorer 1

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


## Item 82: Q02, repeat 15 — Scorer 2

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


## Item 83: Q02, repeat 16 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 83: Q02, repeat 16 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 84: Q02, repeat 17 — Scorer 1

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


## Item 84: Q02, repeat 17 — Scorer 2

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


## Item 85: Q02, repeat 18 — Scorer 1

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


## Item 85: Q02, repeat 18 — Scorer 2

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


## Item 86: Q02, repeat 19 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = $5,000.00 − $2,400.00 = **$2,600.00**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 86: Q02, repeat 19 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = $5,000.00 − $2,400.00 = **$2,600.00**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 87: Q02, repeat 20 — Scorer 1

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


## Item 87: Q02, repeat 20 — Scorer 2

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


## Item 88: Q02, repeat 21 — Scorer 1

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


## Item 88: Q02, repeat 21 — Scorer 2

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


## Item 89: Q02, repeat 22 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 89: Q02, repeat 22 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 90: Q02, repeat 23 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 90: Q02, repeat 23 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 91: Q02, repeat 24 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 91: Q02, repeat 24 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 92: Q02, repeat 25 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** $5,000.00 − $2,400.00 = **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 92: Q02, repeat 25 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** $5,000.00 − $2,400.00 = **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 93: Q02, repeat 26 — Scorer 1

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


## Item 93: Q02, repeat 26 — Scorer 2

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


## Item 94: Q02, repeat 27 — Scorer 1

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


## Item 94: Q02, repeat 27 — Scorer 2

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


## Item 95: Q02, repeat 28 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = $5,000.00 − $2,400.00 = **$2,600.00**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 95: Q02, repeat 28 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = $5,000.00 − $2,400.00 = **$2,600.00**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 96: Q02, repeat 29 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 96: Q02, repeat 29 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 97: Q02, repeat 30 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 97: Q02, repeat 30 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 98: Q02, repeat 31 — Scorer 1

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


## Item 98: Q02, repeat 31 — Scorer 2

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


## Item 99: Q02, repeat 32 — Scorer 1

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


## Item 99: Q02, repeat 32 — Scorer 2

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


## Item 100: Q02, repeat 33 — Scorer 1

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


## Item 100: Q02, repeat 33 — Scorer 2

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


## Item 101: Q02, repeat 34 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 101: Q02, repeat 34 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 102: Q02, repeat 35 — Scorer 1

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


## Item 102: Q02, repeat 35 — Scorer 2

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


## Item 103: Q02, repeat 36 — Scorer 1

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


## Item 103: Q02, repeat 36 — Scorer 2

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


## Item 104: Q02, repeat 37 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 104: Q02, repeat 37 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 105: Q02, repeat 38 — Scorer 1

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


## Item 105: Q02, repeat 38 — Scorer 2

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


## Item 106: Q02, repeat 39 — Scorer 1

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


## Item 106: Q02, repeat 39 — Scorer 2

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


## Item 107: Q02, repeat 40 — Scorer 1

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


## Item 107: Q02, repeat 40 — Scorer 2

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


## Item 108: Q02, repeat 41 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 108: Q02, repeat 41 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 109: Q02, repeat 42 — Scorer 1

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


## Item 109: Q02, repeat 42 — Scorer 2

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


## Item 110: Q02, repeat 43 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** $5,000.00 − $2,400.00 = **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 110: Q02, repeat 43 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
**Available credit:** $5,000.00 − $2,400.00 = **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 111: Q02, repeat 44 — Scorer 1

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


## Item 111: Q02, repeat 44 — Scorer 2

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


## Item 112: Q02, repeat 45 — Scorer 1

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


## Item 112: Q02, repeat 45 — Scorer 2

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


## Item 113: Q02, repeat 46 — Scorer 1

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


## Item 113: Q02, repeat 46 — Scorer 2

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


## Item 114: Q02, repeat 48 — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 114: Q02, repeat 48 — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
Available credit = Credit limit − Balance  
= $5,000.00 − $2,400.00  
= **$2,600.00**
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 115: Q02, repeat 49 — Scorer 1

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


## Item 115: Q02, repeat 49 — Scorer 2

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


## Item 116: Q02, repeat 50 — Scorer 1

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


## Item 116: Q02, repeat 50 — Scorer 2

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


## Item 117: Q03, repeat 1 — Scorer 1

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


## Item 117: Q03, repeat 1 — Scorer 2

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


## Item 118: Q03, repeat 2 — Scorer 1

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


## Item 118: Q03, repeat 2 — Scorer 2

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


## Item 119: Q03, repeat 3 — Scorer 1

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


## Item 119: Q03, repeat 3 — Scorer 2

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


## Item 120: Q03, repeat 4 — Scorer 1

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


## Item 120: Q03, repeat 4 — Scorer 2

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


## Item 121: Q03, repeat 5 — Scorer 1

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


## Item 121: Q03, repeat 5 — Scorer 2

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


## Item 122: Q03, repeat 6 — Scorer 1

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


## Item 122: Q03, repeat 6 — Scorer 2

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


## Item 123: Q03, repeat 7 — Scorer 1

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


## Item 123: Q03, repeat 7 — Scorer 2

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


## Item 124: Q03, repeat 8 — Scorer 1

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


## Item 124: Q03, repeat 8 — Scorer 2

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


## Item 125: Q03, repeat 9 — Scorer 1

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


## Item 125: Q03, repeat 9 — Scorer 2

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


## Item 126: Q03, repeat 10 — Scorer 1

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


## Item 126: Q03, repeat 10 — Scorer 2

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


## Item 127: Q03, repeat 11 — Scorer 1

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


## Item 127: Q03, repeat 11 — Scorer 2

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


## Item 128: Q03, repeat 13 — Scorer 1

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


## Item 128: Q03, repeat 13 — Scorer 2

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


## Item 129: Q03, repeat 14 — Scorer 1

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


## Item 129: Q03, repeat 14 — Scorer 2

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


## Item 130: Q03, repeat 15 — Scorer 1

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


## Item 130: Q03, repeat 15 — Scorer 2

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


## Item 131: Q03, repeat 16 — Scorer 1

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


## Item 131: Q03, repeat 16 — Scorer 2

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


## Item 132: Q03, repeat 17 — Scorer 1

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


## Item 132: Q03, repeat 17 — Scorer 2

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


## Item 133: Q03, repeat 18 — Scorer 1

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


## Item 133: Q03, repeat 18 — Scorer 2

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


## Item 134: Q03, repeat 19 — Scorer 1

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


## Item 134: Q03, repeat 19 — Scorer 2

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


## Item 135: Q03, repeat 20 — Scorer 1

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


## Item 135: Q03, repeat 20 — Scorer 2

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


## Item 136: Q03, repeat 21 — Scorer 1

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


## Item 136: Q03, repeat 21 — Scorer 2

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


## Item 137: Q03, repeat 22 — Scorer 1

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


## Item 137: Q03, repeat 22 — Scorer 2

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


## Item 138: Q03, repeat 23 — Scorer 1

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


## Item 138: Q03, repeat 23 — Scorer 2

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


## Item 139: Q03, repeat 24 — Scorer 1

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


## Item 139: Q03, repeat 24 — Scorer 2

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


## Item 140: Q03, repeat 25 — Scorer 1

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


## Item 140: Q03, repeat 25 — Scorer 2

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


## Item 141: Q03, repeat 26 — Scorer 1

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


## Item 141: Q03, repeat 26 — Scorer 2

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


## Item 142: Q03, repeat 27 — Scorer 1

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


## Item 142: Q03, repeat 27 — Scorer 2

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


## Item 143: Q03, repeat 28 — Scorer 1

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


## Item 143: Q03, repeat 28 — Scorer 2

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


## Item 144: Q03, repeat 29 — Scorer 1

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


## Item 144: Q03, repeat 29 — Scorer 2

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


## Item 145: Q03, repeat 30 — Scorer 1

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


## Item 145: Q03, repeat 30 — Scorer 2

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


## Item 146: Q03, repeat 31 — Scorer 1

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


## Item 146: Q03, repeat 31 — Scorer 2

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


## Item 147: Q03, repeat 33 — Scorer 1

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


## Item 147: Q03, repeat 33 — Scorer 2

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


## Item 148: Q03, repeat 34 — Scorer 1

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


## Item 148: Q03, repeat 34 — Scorer 2

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


## Item 149: Q03, repeat 35 — Scorer 1

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


## Item 149: Q03, repeat 35 — Scorer 2

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


## Item 150: Q03, repeat 36 — Scorer 1

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


## Item 150: Q03, repeat 36 — Scorer 2

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


## Item 151: Q03, repeat 37 — Scorer 1

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


## Item 151: Q03, repeat 37 — Scorer 2

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


## Item 152: Q03, repeat 38 — Scorer 1

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


## Item 152: Q03, repeat 38 — Scorer 2

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


## Item 153: Q03, repeat 39 — Scorer 1

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


## Item 153: Q03, repeat 39 — Scorer 2

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


## Item 154: Q03, repeat 40 — Scorer 1

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


## Item 154: Q03, repeat 40 — Scorer 2

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


## Item 155: Q03, repeat 42 — Scorer 1

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


## Item 155: Q03, repeat 42 — Scorer 2

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


## Item 156: Q03, repeat 45 — Scorer 1

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


## Item 156: Q03, repeat 45 — Scorer 2

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


## Item 157: Q03, repeat 46 — Scorer 1

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


## Item 157: Q03, repeat 46 — Scorer 2

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


## Item 158: Q03, repeat 47 — Scorer 1

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


## Item 158: Q03, repeat 47 — Scorer 2

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


## Item 159: Q03, repeat 48 — Scorer 1

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


## Item 159: Q03, repeat 48 — Scorer 2

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


## Item 160: Q03, repeat 50 — Scorer 1

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


## Item 160: Q03, repeat 50 — Scorer 2

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


## Item 161: Q04, repeat 1 — Scorer 1

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


## Item 161: Q04, repeat 1 — Scorer 2

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


## Item 162: Q04, repeat 4 — Scorer 1

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


## Item 162: Q04, repeat 4 — Scorer 2

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


## Item 163: Q04, repeat 6 — Scorer 1

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


## Item 163: Q04, repeat 6 — Scorer 2

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


## Item 164: Q04, repeat 9 — Scorer 1

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


## Item 164: Q04, repeat 9 — Scorer 2

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


## Item 165: Q04, repeat 30 — Scorer 1

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


## Item 165: Q04, repeat 30 — Scorer 2

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


## Item 166: Q04, repeat 32 — Scorer 1

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


## Item 166: Q04, repeat 32 — Scorer 2

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


## Item 167: Q04, repeat 34 — Scorer 1

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


## Item 167: Q04, repeat 34 — Scorer 2

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


## Item 168: Q04, repeat 42 — Scorer 1

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


## Item 168: Q04, repeat 42 — Scorer 2

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


## Item 169: Q04, repeat 46 — Scorer 1

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


## Item 169: Q04, repeat 46 — Scorer 2

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


## Item 170: Q05, repeat 5 — Scorer 1

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


## Item 170: Q05, repeat 5 — Scorer 2

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


## Item 171: Q05, repeat 9 — Scorer 1

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


## Item 171: Q05, repeat 9 — Scorer 2

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


## Item 172: Q05, repeat 18 — Scorer 1

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


## Item 172: Q05, repeat 18 — Scorer 2

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


## Item 173: Q05, repeat 22 — Scorer 1

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


## Item 173: Q05, repeat 22 — Scorer 2

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


## Item 174: Q05, repeat 28 — Scorer 1

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


## Item 174: Q05, repeat 28 — Scorer 2

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


## Item 175: Q05, repeat 29 — Scorer 1

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


## Item 175: Q05, repeat 29 — Scorer 2

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


## Item 176: Q05, repeat 30 — Scorer 1

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


## Item 176: Q05, repeat 30 — Scorer 2

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


## Item 177: Q05, repeat 36 — Scorer 1

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


## Item 177: Q05, repeat 36 — Scorer 2

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


## Item 178: Q05, repeat 40 — Scorer 1

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


## Item 178: Q05, repeat 40 — Scorer 2

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


## Item 179: Q05, repeat 44 — Scorer 1

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


## Item 179: Q05, repeat 44 — Scorer 2

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


## Item 180: Q05, repeat 50 — Scorer 1

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


## Item 180: Q05, repeat 50 — Scorer 2

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


## Item 181: Q06, repeat 1 — Scorer 1

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


## Item 181: Q06, repeat 1 — Scorer 2

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


## Item 182: Q06, repeat 3 — Scorer 1

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


## Item 182: Q06, repeat 3 — Scorer 2

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


## Item 183: Q06, repeat 5 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 183: Q06, repeat 5 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 184: Q06, repeat 7 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 184: Q06, repeat 7 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 185: Q06, repeat 8 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 185: Q06, repeat 8 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 186: Q06, repeat 9 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 186: Q06, repeat 9 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 187: Q06, repeat 10 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 187: Q06, repeat 10 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 188: Q06, repeat 12 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 188: Q06, repeat 12 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 189: Q06, repeat 13 — Scorer 1

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


## Item 189: Q06, repeat 13 — Scorer 2

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


## Item 190: Q06, repeat 14 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**

Since the account earns 0% interest, there is no interest income to offset the fees.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 190: Q06, repeat 14 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**

Since the account earns 0% interest, there is no interest income to offset the fees.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 191: Q06, repeat 15 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 191: Q06, repeat 15 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 192: Q06, repeat 16 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 192: Q06, repeat 16 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 193: Q06, repeat 18 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 193: Q06, repeat 18 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 194: Q06, repeat 19 — Scorer 1

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


## Item 194: Q06, repeat 19 — Scorer 2

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


## Item 195: Q06, repeat 22 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12.00 × 12 = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 195: Q06, repeat 22 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12.00 × 12 = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 196: Q06, repeat 23 — Scorer 1

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


## Item 196: Q06, repeat 23 — Scorer 2

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


## Item 197: Q06, repeat 25 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12.00 × 12 = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 197: Q06, repeat 25 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12.00 × 12 = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 198: Q06, repeat 26 — Scorer 1

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


## Item 198: Q06, repeat 26 — Scorer 2

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


## Item 199: Q06, repeat 27 — Scorer 1

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


## Item 199: Q06, repeat 27 — Scorer 2

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


## Item 200: Q06, repeat 33 — Scorer 1

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


## Item 200: Q06, repeat 33 — Scorer 2

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


## Item 201: Q06, repeat 39 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 201: Q06, repeat 39 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 202: Q06, repeat 40 — Scorer 1

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


## Item 202: Q06, repeat 40 — Scorer 2

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


## Item 203: Q06, repeat 41 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 203: Q06, repeat 41 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 204: Q06, repeat 43 — Scorer 1

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


## Item 204: Q06, repeat 43 — Scorer 2

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


## Item 205: Q06, repeat 44 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 205: Q06, repeat 44 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost is:

**$12 × 12 months = $144 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 206: Q06, repeat 46 — Scorer 1

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


## Item 206: Q06, repeat 46 — Scorer 2

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


## Item 207: Q06, repeat 47 — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 207: Q06, repeat 47 — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The monthly fee is **$12.00**.

**Total annual cost:** $12 × 12 months = **$144.00 per year**.
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

The released figure matches the expected value, but the required computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. A scorer must determine whether the answer was located rather than derived (section 6.8: RETRIEVED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 208: Q07, repeat 1 — Scorer 1

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


## Item 208: Q07, repeat 1 — Scorer 2

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


## Item 209: Q07, repeat 2 — Scorer 1

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


## Item 209: Q07, repeat 2 — Scorer 2

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


## Item 210: Q07, repeat 3 — Scorer 1

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


## Item 210: Q07, repeat 3 — Scorer 2

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


## Item 211: Q07, repeat 4 — Scorer 1

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


## Item 211: Q07, repeat 4 — Scorer 2

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


## Item 212: Q07, repeat 5 — Scorer 1

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


## Item 212: Q07, repeat 5 — Scorer 2

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


## Item 213: Q07, repeat 7 — Scorer 1

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


## Item 213: Q07, repeat 7 — Scorer 2

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


## Item 214: Q07, repeat 8 — Scorer 1

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


## Item 214: Q07, repeat 8 — Scorer 2

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


## Item 215: Q07, repeat 9 — Scorer 1

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


## Item 215: Q07, repeat 9 — Scorer 2

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


## Item 216: Q07, repeat 10 — Scorer 1

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


## Item 216: Q07, repeat 10 — Scorer 2

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


## Item 217: Q07, repeat 11 — Scorer 1

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


## Item 217: Q07, repeat 11 — Scorer 2

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


## Item 218: Q07, repeat 12 — Scorer 1

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


## Item 218: Q07, repeat 12 — Scorer 2

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


## Item 219: Q07, repeat 13 — Scorer 1

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


## Item 219: Q07, repeat 13 — Scorer 2

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


## Item 220: Q07, repeat 14 — Scorer 1

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


## Item 220: Q07, repeat 14 — Scorer 2

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


## Item 221: Q07, repeat 15 — Scorer 1

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


## Item 221: Q07, repeat 15 — Scorer 2

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


## Item 222: Q07, repeat 16 — Scorer 1

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


## Item 222: Q07, repeat 16 — Scorer 2

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


## Item 223: Q07, repeat 17 — Scorer 1

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


## Item 223: Q07, repeat 17 — Scorer 2

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


## Item 224: Q07, repeat 18 — Scorer 1

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


## Item 224: Q07, repeat 18 — Scorer 2

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


## Item 225: Q07, repeat 19 — Scorer 1

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


## Item 225: Q07, repeat 19 — Scorer 2

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


## Item 226: Q07, repeat 21 — Scorer 1

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


## Item 226: Q07, repeat 21 — Scorer 2

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


## Item 227: Q07, repeat 22 — Scorer 1

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


## Item 227: Q07, repeat 22 — Scorer 2

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


## Item 228: Q07, repeat 23 — Scorer 1

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


## Item 228: Q07, repeat 23 — Scorer 2

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


## Item 229: Q07, repeat 24 — Scorer 1

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


## Item 229: Q07, repeat 24 — Scorer 2

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


## Item 230: Q07, repeat 25 — Scorer 1

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


## Item 230: Q07, repeat 25 — Scorer 2

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


## Item 231: Q07, repeat 26 — Scorer 1

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


## Item 231: Q07, repeat 26 — Scorer 2

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


## Item 232: Q07, repeat 27 — Scorer 1

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


## Item 232: Q07, repeat 27 — Scorer 2

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


## Item 233: Q07, repeat 28 — Scorer 1

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


## Item 233: Q07, repeat 28 — Scorer 2

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


## Item 234: Q07, repeat 29 — Scorer 1

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


## Item 234: Q07, repeat 29 — Scorer 2

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


## Item 235: Q07, repeat 30 — Scorer 1

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


## Item 235: Q07, repeat 30 — Scorer 2

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


## Item 236: Q07, repeat 32 — Scorer 1

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


## Item 236: Q07, repeat 32 — Scorer 2

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


## Item 237: Q07, repeat 33 — Scorer 1

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


## Item 237: Q07, repeat 33 — Scorer 2

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


## Item 238: Q07, repeat 35 — Scorer 1

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


## Item 238: Q07, repeat 35 — Scorer 2

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


## Item 239: Q07, repeat 36 — Scorer 1

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


## Item 239: Q07, repeat 36 — Scorer 2

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


## Item 240: Q07, repeat 37 — Scorer 1

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


## Item 240: Q07, repeat 37 — Scorer 2

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


## Item 241: Q07, repeat 38 — Scorer 1

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


## Item 241: Q07, repeat 38 — Scorer 2

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


## Item 242: Q07, repeat 40 — Scorer 1

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


## Item 242: Q07, repeat 40 — Scorer 2

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


## Item 243: Q07, repeat 41 — Scorer 1

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


## Item 243: Q07, repeat 41 — Scorer 2

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


## Item 244: Q07, repeat 42 — Scorer 1

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


## Item 244: Q07, repeat 42 — Scorer 2

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


## Item 245: Q07, repeat 46 — Scorer 1

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


## Item 245: Q07, repeat 46 — Scorer 2

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


## Item 246: Q07, repeat 48 — Scorer 1

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


## Item 246: Q07, repeat 48 — Scorer 2

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


## Item 247: Q07, repeat 49 — Scorer 1

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


## Item 247: Q07, repeat 49 — Scorer 2

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


## Item 248: Q07, repeat 50 — Scorer 1

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


## Item 248: Q07, repeat 50 — Scorer 2

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


## Item 249: Q08, repeat 1 — Scorer 1

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


## Item 249: Q08, repeat 1 — Scorer 2

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


## Item 250: Q08, repeat 16 — Scorer 1

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


## Item 250: Q08, repeat 16 — Scorer 2

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

Total items requiring adjudication: 250

Total sheets: 500 (2 per item, for 2 scorers)
