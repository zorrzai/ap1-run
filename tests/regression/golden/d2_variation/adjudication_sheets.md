# AP-1 Adjudication Sheets

Generated: <TIMESTAMP>

AP-1 Version: v1.3-draft-for-comment-20260730

Version DOI: 10.5281/zenodo.21755443

---


## Item 1: Q01 (Condition: base) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
About $15.20 per month.
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 1: Q01 (Condition: base) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
About $15.20 per month.
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 2: Q02 (Condition: base) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
You have $2500.00 of credit left.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 - 2500"}`)
  → `{"result": "2500"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 2: Q02 (Condition: base) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
You have $2500.00 of credit left.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 - 2500"}`)
  → `{"result": "2500"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 3: Q01 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
About $15.20 per month.
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 3: Q01 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
About $15.20 per month.
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 4: Q02 (Condition: instruction_removed) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
You have $2500.00 of credit left.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 - 2500"}`)
  → `{"result": "2500"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2600.00`

- Required operation: `calculator`


---


## Item 4: Q02 (Condition: instruction_removed) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
You have $2500.00 of credit left.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 - 2500"}`)
  → `{"result": "2500"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2600.00`

- Required operation: `calculator`


---


---

Total items requiring adjudication: 4

Total sheets: 8 (2 per item, for 2 scorers)
