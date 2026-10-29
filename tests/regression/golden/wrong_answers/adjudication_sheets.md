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
The monthly interest earned on the savings account is $15.25.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 1: Q01 (Condition: base) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $15.25.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 2: Q01 (Condition: base) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $15.25.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 2: Q01 (Condition: base) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $15.25.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 3: Q02 (Condition: base) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit remaining on the credit card is $7400.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 + 2400"}`)
  → `{"result": "7400"}`


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


## Item 3: Q02 (Condition: base) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit remaining on the credit card is $7400.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 + 2400"}`)
  → `{"result": "7400"}`


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


## Item 4: Q02 (Condition: base) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit remaining on the credit card is $7400.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 + 2400"}`)
  → `{"result": "7400"}`


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


## Item 4: Q02 (Condition: base) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit remaining on the credit card is $7400.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 + 2400"}`)
  → `{"result": "7400"}`


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


## Item 5: Q03 (Condition: base) — Scorer 1

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge on the credit card is $162.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (81.0 / 100) / 12"}`)
  → `{"result": "162.00000000000003"}`


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 5: Q03 (Condition: base) — Scorer 2

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge on the credit card is $162.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (81.0 / 100) / 12"}`)
  → `{"result": "162.00000000000003"}`


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 6: Q03 (Condition: base) — Scorer 1

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge on the credit card is $162.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (81.0 / 100) / 12"}`)
  → `{"result": "162.00000000000003"}`


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 6: Q03 (Condition: base) — Scorer 2

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge on the credit card is $162.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (81.0 / 100) / 12"}`)
  → `{"result": "162.00000000000003"}`


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 7: Q04 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is $1006.25.
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

- **calculator**(`{"expression": "287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 7: Q04 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is $1006.25.
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

- **calculator**(`{"expression": "287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 8: Q04 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is $1006.25.
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

- **calculator**(`{"expression": "287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 8: Q04 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is $1006.25.
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

- **calculator**(`{"expression": "287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 9: Q01 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $15.25.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 9: Q01 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $15.25.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 10: Q01 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $15.25.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 10: Q01 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $15.25.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 11: Q02 (Condition: instruction_removed) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit remaining on the credit card is $7400.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 + 2400"}`)
  → `{"result": "7400"}`


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


## Item 11: Q02 (Condition: instruction_removed) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit remaining on the credit card is $7400.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 + 2400"}`)
  → `{"result": "7400"}`


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


## Item 12: Q02 (Condition: instruction_removed) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit remaining on the credit card is $7400.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 + 2400"}`)
  → `{"result": "7400"}`


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


## Item 12: Q02 (Condition: instruction_removed) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
The available credit remaining on the credit card is $7400.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "5000 + 2400"}`)
  → `{"result": "7400"}`


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


## Item 13: Q03 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge on the credit card is $162.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (81.0 / 100) / 12"}`)
  → `{"result": "162.00000000000003"}`


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 13: Q03 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge on the credit card is $162.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (81.0 / 100) / 12"}`)
  → `{"result": "162.00000000000003"}`


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 14: Q03 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge on the credit card is $162.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (81.0 / 100) / 12"}`)
  → `{"result": "162.00000000000003"}`


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 14: Q03 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
The monthly interest charge on the credit card is $162.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (81.0 / 100) / 12"}`)
  → `{"result": "162.00000000000003"}`


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

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 15: Q04 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is $1006.25.
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

- **calculator**(`{"expression": "287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 15: Q04 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is $1006.25.
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

- **calculator**(`{"expression": "287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 16: Q04 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is $1006.25.
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

- **calculator**(`{"expression": "287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 16: Q04 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is $1006.25.
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

- **calculator**(`{"expression": "287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 17: Q08 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance is approximately $287,069.
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

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 17: Q08 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance is approximately $287,069.
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

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 18: Q08 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance is approximately $287,069.
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

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 18: Q08 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance is approximately $287,069.
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

*No tool calls recorded.*


**Invocation outcome:** `NOT-INVOKED`

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


---

Total items requiring adjudication: 18

Total sheets: 36 (2 per item, for 2 scorers)
