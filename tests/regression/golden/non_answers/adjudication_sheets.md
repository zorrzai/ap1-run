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
[no text content]
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 1: Q01, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
[no text content]
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 2: Q01, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
[no text content]
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 2: Q01, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
[no text content]
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 3: Q02, repeat 1 (Condition: base) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
I cannot determine the available credit from this information.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 3: Q02, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
I cannot determine the available credit from this information.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 4: Q02, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
I cannot determine the available credit from this information.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 4: Q02, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
I cannot determine the available credit from this information.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 5: Q03, repeat 1 (Condition: base) — Scorer 1

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
I apologize, but I'm unable to compute that. The balance is $2,400.00 and the annual rate is 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 5: Q03, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
I apologize, but I'm unable to compute that. The balance is $2,400.00 and the annual rate is 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 6: Q03, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
I apologize, but I'm unable to compute that. The balance is $2,400.00 and the annual rate is 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 6: Q03, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
I apologize, but I'm unable to compute that. The balance is $2,400.00 and the annual rate is 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 7: Q05, repeat 1 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 7: Q05, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 8: Q05, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 8: Q05, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 9: Q07, repeat 1 (Condition: base) — Scorer 1

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Quarterly growth: 777.4125 (that is, $777.41).
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (0.078 / 4) - (15 * 3)"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 9: Q07, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Quarterly growth: 777.4125 (that is, $777.41).
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (0.078 / 4) - (15 * 3)"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 10: Q07, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Quarterly growth: 777.4125 (that is, $777.41).
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (0.078 / 4) - (15 * 3)"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 10: Q07, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Quarterly growth: 777.4125 (that is, $777.41).
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (0.078 / 4) - (15 * 3)"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 11: Q01, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
[no text content]
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 11: Q01, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
[no text content]
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 12: Q01, repeat 2 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
[no text content]
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 12: Q01, repeat 2 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest earned on the savings account?

Category: interest

### Response (verbatim)

```
[no text content]
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

- Expected value: `15.200`

- Required operation: `calculator`


---


## Item 13: Q02, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
I cannot determine the available credit from this information.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 13: Q02, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
I cannot determine the available credit from this information.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 14: Q02, repeat 2 (Condition: instruction_removed) — Scorer 1

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
I cannot determine the available credit from this information.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 14: Q02, repeat 2 (Condition: instruction_removed) — Scorer 2

### Question

> What is the available credit remaining on the credit card?

Category: balance

### Response (verbatim)

```
I cannot determine the available credit from this information.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Response matched a decline marker. Declines are never auto-scored (section 6.8: MODEL-DECLINED).

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 15: Q03, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
I apologize, but I'm unable to compute that. The balance is $2,400.00 and the annual rate is 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 15: Q03, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
I apologize, but I'm unable to compute that. The balance is $2,400.00 and the annual rate is 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 16: Q03, repeat 2 (Condition: instruction_removed) — Scorer 1

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
I apologize, but I'm unable to compute that. The balance is $2,400.00 and the annual rate is 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 16: Q03, repeat 2 (Condition: instruction_removed) — Scorer 2

### Question

> What is the monthly interest charge on the credit card?

Category: interest

### Response (verbatim)

```
I apologize, but I'm unable to compute that. The balance is $2,400.00 and the annual rate is 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

Numeric figures were found in the response but none matched the expected value within tolerance. A scorer must determine whether the figure answers the right question at the wrong scope, or is originated.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Reference Values

- Expected value: `36.000`

- Required operation: `calculator`


---


## Item 17: Q05, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 17: Q05, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 18: Q05, repeat 2 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 18: Q05, repeat 2 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 19: Q07, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Quarterly growth: 777.4125 (that is, $777.41).
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (0.078 / 4) - (15 * 3)"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 19: Q07, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Quarterly growth: 777.4125 (that is, $777.41).
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (0.078 / 4) - (15 * 3)"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 20: Q07, repeat 2 (Condition: instruction_removed) — Scorer 1

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Quarterly growth: 777.4125 (that is, $777.41).
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (0.078 / 4) - (15 * 3)"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 20: Q07, repeat 2 (Condition: instruction_removed) — Scorer 2

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
Quarterly growth: 777.4125 (that is, $777.41).
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "42175 * (0.078 / 4) - (15 * 3)"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


---

Total items requiring adjudication: 20

Total sheets: 40 (2 per item, for 2 scorers)
