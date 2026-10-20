# AP-1 Adjudication Sheets

Generated: <TIMESTAMP>

AP-1 Version: v1.3-draft-for-comment-20260730

Version DOI: 10.5281/zenodo.21755443

---


## Item 1: Q01, repeat 1 (Condition: base) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": " 7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 1: Q01, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": " 7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 2: Q01, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": " 7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 2: Q01, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": " 7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 3: Q09, repeat 1 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 3: Q09, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 4: Q09, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 4: Q09, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 5: Q01, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": " 7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 5: Q01, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": " 7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 6: Q01, repeat 2 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": " 7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 6: Q01, repeat 2 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
The monthly interest earned on the savings account is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": " 7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 7: Q09, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 7: Q09, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 8: Q09, repeat 2 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 8: Q09, repeat 2 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income is $2333.10.
```

### Fixture Excerpt

**Savings Account** (`savings`):

- balance: `15200.00`

- direction: `asset`

- annual_rate: `1.2`

- monthly_fee: `0.00`


**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "7777 * 3"}`)
  → `{"result": "23331"}`

- **calculator**(`{"expression": "23331 * 1.2 / 12"}`)
  → `{"result": "2333.1"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `3.200`

- Required operation: `calculator`


---


---

Total items requiring adjudication: 8

Total sheets: 16 (2 per item, for 2 scorers)
