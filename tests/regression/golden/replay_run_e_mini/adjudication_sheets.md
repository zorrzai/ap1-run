# AP-1 Adjudication Sheets

Generated: <TIMESTAMP>

AP-1 Version: v1.3-draft-for-comment-20260730

Version DOI: 10.5281/zenodo.21755443

---


## Item 1: Q04, repeat 1 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. The total minimum payment is $1437.00. 

To find the principal portion of the first mortgage payment, subtract the interest portion from the total minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"(287500.00 * 4.20) / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 1: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 1: Q04, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. The total minimum payment is $1437.00. 

To find the principal portion of the first mortgage payment, subtract the interest portion from the total minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"(287500.00 * 4.20) / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 1: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 2: Q04, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first payment, subtract the interest portion from the total minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 2: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 2: Q04, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first payment, subtract the interest portion from the total minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 2: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 3: Q04, repeat 4 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 
The principal portion is the total monthly payment minus the interest portion:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 4: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 3: Q04, repeat 4 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 
The principal portion is the total monthly payment minus the interest portion:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 4: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 4: Q04, repeat 7 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the total minimum payment is $1437.00, the principal portion is:

$1437.00 - $1006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 7: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 4: Q04, repeat 7 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the total minimum payment is $1437.00, the principal portion is:

$1437.00 - $1006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 7: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 5: Q04, repeat 9 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1,006.25.

The total minimum payment is $1,437.00.

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 9: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 5: Q04, repeat 9 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1,006.25.

The total minimum payment is $1,437.00.

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 9: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 6: Q04, repeat 12 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first mortgage payment, subtract the interest portion from the total minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 12: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 6: Q04, repeat 12 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first mortgage payment, subtract the interest portion from the total minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 12: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 7: Q04, repeat 14 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the minimum payment is $1437.00, the principal portion of the first mortgage payment is calculated by subtracting the interest portion from the total payment:

Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 14: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 7: Q04, repeat 14 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the minimum payment is $1437.00, the principal portion of the first mortgage payment is calculated by subtracting the interest portion from the total payment:

Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 14: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 8: Q04, repeat 15 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total monthly payment is $1437.00. 

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 15: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 8: Q04, repeat 15 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total monthly payment is $1437.00. 

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 15: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 9: Q04, repeat 18 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum payment is $1437.00.

To find the principal portion of the first mortgage payment, subtract the interest portion from the total payment:
1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 18: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 9: Q04, repeat 18 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum payment is $1437.00.

To find the principal portion of the first mortgage payment, subtract the interest portion from the total payment:
1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 18: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 10: Q04, repeat 21 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. The minimum monthly payment is $1437.00. 

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total monthly payment:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 21: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 10: Q04, repeat 21 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. The minimum monthly payment is $1437.00. 

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total monthly payment:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 21: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 11: Q04, repeat 23 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the total minimum payment is $1437.00, the principal portion of the first mortgage payment is calculated by subtracting the interest portion from the total minimum payment:

Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 23: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 11: Q04, repeat 23 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the total minimum payment is $1437.00, the principal portion of the first mortgage payment is calculated by subtracting the interest portion from the total minimum payment:

Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 23: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 12: Q04, repeat 24 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is calculated by subtracting the interest portion from the total minimum payment. The interest portion is the mortgage balance multiplied by the annual interest rate divided by 12 months.

Interest portion = $287,500.00 * 4.20% / 12 = $1006.25

The principal portion is then:

Principal portion = Minimum payment - Interest portion = $1437.00 - $1006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * 0.042 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 24: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 12: Q04, repeat 24 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The principal portion of the first mortgage payment is calculated by subtracting the interest portion from the total minimum payment. The interest portion is the mortgage balance multiplied by the annual interest rate divided by 12 months.

Interest portion = $287,500.00 * 4.20% / 12 = $1006.25

The principal portion is then:

Principal portion = Minimum payment - Interest portion = $1437.00 - $1006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * 0.042 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 24: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 13: Q04, repeat 31 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25.

To find the principal portion of the first mortgage payment, subtract the interest portion from the minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100 / 12)"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 31: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 13: Q04, repeat 31 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25.

To find the principal portion of the first mortgage payment, subtract the interest portion from the minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100 / 12)"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 31: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 14: Q04, repeat 32 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. The principal portion is the total minimum payment minus the interest portion:

Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 32: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 14: Q04, repeat 32 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. The principal portion is the total minimum payment minus the interest portion:

Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 32: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 15: Q04, repeat 36 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first mortgage payment, subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 36: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 15: Q04, repeat 36 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first mortgage payment, subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 36: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 16: Q04, repeat 37 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first mortgage payment, subtract the interest portion from the total minimum payment:

Principal portion = Min Payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 0.042 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 37: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 16: Q04, repeat 37 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first mortgage payment, subtract the interest portion from the total minimum payment:

Principal portion = Min Payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 0.042 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 37: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 17: Q04, repeat 38 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25.

The principal portion of the first mortgage payment is calculated as:
Min Payment - Interest portion = 1437.00 - 1006.25 = $430.75.

Therefore, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 38: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 17: Q04, repeat 38 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25.

The principal portion of the first mortgage payment is calculated as:
Min Payment - Interest portion = 1437.00 - 1006.25 = $430.75.

Therefore, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 38: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 18: Q04, repeat 39 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion, subtract the interest portion from the total minimum payment:
Principal portion = Minimum payment - Interest portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 0.042 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 39: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 18: Q04, repeat 39 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion, subtract the interest portion from the total minimum payment:
Principal portion = Minimum payment - Interest portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 0.042 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 39: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 19: Q04, repeat 41 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first payment, subtract the interest portion from the minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 41: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 19: Q04, repeat 41 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first payment, subtract the interest portion from the minimum payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 41: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 20: Q04, repeat 42 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25.
The total minimum payment is $1437.00.
The principal portion of the first mortgage payment is the total payment minus the interest portion:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 42: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 20: Q04, repeat 42 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25.
The total minimum payment is $1437.00.
The principal portion of the first mortgage payment is the total payment minus the interest portion:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 42: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 21: Q04, repeat 43 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion, subtract the interest from the minimum payment:
1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 43: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 21: Q04, repeat 43 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion, subtract the interest from the minimum payment:
1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 43: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 22: Q04, repeat 44 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum payment is $1437.00.

To find the principal portion, we subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 44: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 22: Q04, repeat 44 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum payment is $1437.00.

To find the principal portion, we subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 44: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 23: Q04, repeat 45 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Since the minimum payment is $1437.00, the principal portion of the first mortgage payment can be calculated as:
1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 45: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 23: Q04, repeat 45 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Since the minimum payment is $1437.00, the principal portion of the first mortgage payment can be calculated as:
1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 45: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 24: Q04, repeat 46 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum monthly payment is $1437.00.

To find the principal portion of the first payment, subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 46: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 24: Q04, repeat 46 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum monthly payment is $1437.00.

To find the principal portion of the first payment, subtract the interest portion from the total payment:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 46: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 25: Q04, repeat 48 (Condition: base) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Since the minimum payment is $1437.00, the principal portion of the first mortgage payment is the difference between the minimum payment and the interest portion:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20/100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 48: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 25: Q04, repeat 48 (Condition: base) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Since the minimum payment is $1437.00, the principal portion of the first mortgage payment is the difference between the minimum payment and the interest portion:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20/100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 48: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 26: Q05, repeat 15 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made, the credit card balance after one month will be $2410.63. This is because the remaining balance accrues interest at the monthly rate based on the annual rate of 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400.00 - 25.00"}`)
  → `{"result": "2375.0"}`

- **calculator**(`{"expression":"2375.0 * (18.0 / 100) / 12"}`)
  → `{"result": "35.625"}`

- **calculator**(`{"expression":"2375.0 + 35.625"}`)
  → `{"result": "2410.625"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 26: Q05, repeat 15 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made, the credit card balance after one month will be $2410.63. This is because the remaining balance accrues interest at the monthly rate based on the annual rate of 18.0%.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400.00 - 25.00"}`)
  → `{"result": "2375.0"}`

- **calculator**(`{"expression":"2375.0 * (18.0 / 100) / 12"}`)
  → `{"result": "35.625"}`

- **calculator**(`{"expression":"2375.0 + 35.625"}`)
  → `{"result": "2410.625"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 27: Q05, repeat 22 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The credit card balance after one month, if only the minimum payment of $25.00 is made, would be $2375.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 - 25"}`)
  → `{"result": "2375"}`


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 27: Q05, repeat 22 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The credit card balance after one month, if only the minimum payment of $25.00 is made, would be $2375.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 - 25"}`)
  → `{"result": "2375"}`


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 28: Q05, repeat 28 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month, if only the minimum payment of 25.00 is made, the credit card balance will be 2410.63. This includes the remaining balance after payment plus the interest accrued for the month.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression": "(2400 - 25) * (18.0 / 100) / 12"}`)
  → `{"result": "35.625"}`

- **calculator**(`{"expression":"2375 + 35.625"}`)
  → `{"result": "2410.625"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 28: Q05, repeat 28 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month, if only the minimum payment of 25.00 is made, the credit card balance will be 2410.63. This includes the remaining balance after payment plus the interest accrued for the month.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression": "(2400 - 25) * (18.0 / 100) / 12"}`)
  → `{"result": "35.625"}`

- **calculator**(`{"expression":"2375 + 35.625"}`)
  → `{"result": "2410.625"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 29: Q05, repeat 30 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month, if only the minimum payment of $25 is made, the credit card balance will be $2410.63. This takes into account the deducted payment and the interest accrued for the month.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression":"2375 * (18 / 100) / 12"}`)
  → `{"result": "35.625"}`

- **calculator**(`{"expression":"2375 + 35.625"}`)
  → `{"result": "2410.625"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 29: Q05, repeat 30 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month, if only the minimum payment of $25 is made, the credit card balance will be $2410.63. This takes into account the deducted payment and the interest accrued for the month.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression":"2375 * (18 / 100) / 12"}`)
  → `{"result": "35.625"}`

- **calculator**(`{"expression":"2375 + 35.625"}`)
  → `{"result": "2410.625"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 30: Q05, repeat 36 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made after one month, the credit card balance will be $2411.00. This is because the interest for one month (at an 18% annual rate) is $36.00, which when added to the reduced balance after payment ($2375.00), results in a new balance of $2411.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression":"2375 + 36"}`)
  → `{"result": "2411"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 30: Q05, repeat 36 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made after one month, the credit card balance will be $2411.00. This is because the interest for one month (at an 18% annual rate) is $36.00, which when added to the reduced balance after payment ($2375.00), results in a new balance of $2411.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression":"2375 + 36"}`)
  → `{"result": "2411"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 31: Q05, repeat 41 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made, the credit card balance after one month would be $2375.00. However, this calculation does not include interest added for the month. Would you like me to calculate the balance including the interest for the month as well?
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 - 25"}`)
  → `{"result": "2375"}`


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 31: Q05, repeat 41 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made, the credit card balance after one month would be $2375.00. However, this calculation does not include interest added for the month. Would you like me to calculate the balance including the interest for the month as well?
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 - 25"}`)
  → `{"result": "2375"}`


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 32: Q05, repeat 46 (Condition: base) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made after one month, the new credit card balance would be $2375.00. However, this calculation does not yet include the interest accrued over the month. Would you like me to calculate the balance including the interest as well?
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 - 25"}`)
  → `{"result": "2375"}`


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 32: Q05, repeat 46 (Condition: base) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made after one month, the new credit card balance would be $2375.00. However, this calculation does not yet include the interest accrued over the month. Would you like me to calculate the balance including the interest as well?
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400 - 25"}`)
  → `{"result": "2375"}`


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 33: Q07, repeat 44 (Condition: base) — Scorer 1

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-0 UNOBSERVABLE`

- **calculator**(`{"expression": "7.8 / 4"}`)
  → `{"result": "1.95"}`

- **calculator**(`{"expression": "42175.00 * (7.8 / 4) / 100"}`)
  → `{"result": "822.4125"}`

- **calculator**(`{"expression": "15.00 * 3"}`)
  → `{"result": "45.0"}`

- **calculator**(`{"expression":"822.4125 - 45.0"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `None`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 33: Q07, repeat 44 (Condition: base) — Scorer 2

### Question

> What is the quarterly net growth of the investment account after fees?

Category: growth

### Response (verbatim)

```
[no text content]
```

### Fixture Excerpt

**Investment Account** (`investment`):

- balance: `42175.00`

- direction: `asset`

- annual_rate: `7.8`

- monthly_fee: `15.00`


### Structural Tool-Call Record

**Evidence class:** `EV-0 UNOBSERVABLE`

- **calculator**(`{"expression": "7.8 / 4"}`)
  → `{"result": "1.95"}`

- **calculator**(`{"expression": "42175.00 * (7.8 / 4) / 100"}`)
  → `{"result": "822.4125"}`

- **calculator**(`{"expression": "15.00 * 3"}`)
  → `{"result": "45.0"}`

- **calculator**(`{"expression":"822.4125 - 45.0"}`)
  → `{"result": "777.4125"}`


**Invocation outcome:** `None`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

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

- Expected value: `777.4125`

- Required operation: `calculator`


---


## Item 34: Q08, repeat 1 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 34: Q08, repeat 1 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 35: Q08, repeat 2 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 35: Q08, repeat 2 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 36: Q08, repeat 3 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 36: Q08, repeat 3 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 37: Q08, repeat 4 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 37: Q08, repeat 4 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 38: Q08, repeat 5 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 38: Q08, repeat 5 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 39: Q08, repeat 6 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 39: Q08, repeat 6 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 40: Q08, repeat 7 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 40: Q08, repeat 7 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 41: Q08, repeat 8 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 41: Q08, repeat 8 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 42: Q08, repeat 9 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 42: Q08, repeat 9 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 43: Q08, repeat 10 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 43: Q08, repeat 10 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 44: Q08, repeat 11 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of 1437.00 will be 286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 44: Q08, repeat 11 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of 1437.00 will be 286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 45: Q08, repeat 12 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 45: Q08, repeat 12 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 46: Q08, repeat 13 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 would be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 46: Q08, repeat 13 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 would be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 47: Q08, repeat 14 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 47: Q08, repeat 14 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 48: Q08, repeat 15 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of 1437.00 will be 286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 48: Q08, repeat 15 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of 1437.00 will be 286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 49: Q08, repeat 16 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 49: Q08, repeat 16 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 50: Q08, repeat 17 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 50: Q08, repeat 17 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 51: Q08, repeat 18 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 51: Q08, repeat 18 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 52: Q08, repeat 19 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 52: Q08, repeat 19 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 53: Q08, repeat 20 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 53: Q08, repeat 20 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 54: Q08, repeat 21 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 54: Q08, repeat 21 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 55: Q08, repeat 22 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 55: Q08, repeat 22 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 56: Q08, repeat 23 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 56: Q08, repeat 23 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 57: Q08, repeat 24 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 57: Q08, repeat 24 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 58: Q08, repeat 25 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 58: Q08, repeat 25 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 59: Q08, repeat 26 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 59: Q08, repeat 26 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 60: Q08, repeat 27 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
After the first monthly payment of $1437, the remaining mortgage balance would be $286,063.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 60: Q08, repeat 27 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
After the first monthly payment of $1437, the remaining mortgage balance would be $286,063.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 61: Q08, repeat 28 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 61: Q08, repeat 28 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 62: Q08, repeat 29 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 62: Q08, repeat 29 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 63: Q08, repeat 30 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 63: Q08, repeat 30 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 64: Q08, repeat 31 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 64: Q08, repeat 31 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 65: Q08, repeat 32 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 65: Q08, repeat 32 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 66: Q08, repeat 33 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 66: Q08, repeat 33 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 67: Q08, repeat 34 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 67: Q08, repeat 34 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 68: Q08, repeat 35 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 68: Q08, repeat 35 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 69: Q08, repeat 36 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 69: Q08, repeat 36 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 70: Q08, repeat 37 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 70: Q08, repeat 37 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 71: Q08, repeat 38 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 71: Q08, repeat 38 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 72: Q08, repeat 39 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 72: Q08, repeat 39 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 73: Q08, repeat 40 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 73: Q08, repeat 40 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 74: Q08, repeat 41 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 74: Q08, repeat 41 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 75: Q08, repeat 42 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 75: Q08, repeat 42 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 76: Q08, repeat 43 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 76: Q08, repeat 43 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 77: Q08, repeat 44 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 77: Q08, repeat 44 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 78: Q08, repeat 45 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 78: Q08, repeat 45 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 79: Q08, repeat 46 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 79: Q08, repeat 46 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 80: Q08, repeat 47 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 80: Q08, repeat 47 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 81: Q08, repeat 48 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 81: Q08, repeat 48 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 82: Q08, repeat 49 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 82: Q08, repeat 49 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 83: Q08, repeat 50 (Condition: base) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 83: Q08, repeat 50 (Condition: base) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 84: Q09, repeat 4 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. The monthly fee for the checking account is 12.00. 

To find the net monthly income from the savings account after deducting checking account fees:

Net monthly income = Savings account monthly interest - Checking account monthly fee
= 15.20 - 12.00
= 3.20

The net monthly income from the savings account after deducting checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2/100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 4: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 84: Q09, repeat 4 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. The monthly fee for the checking account is 12.00. 

To find the net monthly income from the savings account after deducting checking account fees:

Net monthly income = Savings account monthly interest - Checking account monthly fee
= 15.20 - 12.00
= 3.20

The net monthly income from the savings account after deducting checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2/100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 4: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 85: Q09, repeat 5 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is $15.20.
The monthly fee for the checking account is $12.00.

The net monthly income from the savings account after deducting the checking account fees is calculated as:
15.20 - 12.00 = 3.20

So, the net monthly income is $3.20.
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

- **calculator**(`{"expression": "15200 * 1.2 / 12 / 100"}`)
  → `{"result": "15.2"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 5: reported figure 3.20 was not returned by any tool call; observed returns: [15.2, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 85: Q09, repeat 5 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is $15.20.
The monthly fee for the checking account is $12.00.

The net monthly income from the savings account after deducting the checking account fees is calculated as:
15.20 - 12.00 = 3.20

So, the net monthly income is $3.20.
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

- **calculator**(`{"expression": "15200 * 1.2 / 12 / 100"}`)
  → `{"result": "15.2"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 5: reported figure 3.20 was not returned by any tool call; observed returns: [15.2, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 86: Q09, repeat 23 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. After deducting the checking account fee of 12.00, the net monthly income is 15.20 - 12.00 = 3.20.

The net monthly income from the savings account after deducting checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12.00"}`)
  → `{"result": "-12.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 23: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12.0]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 86: Q09, repeat 23 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. After deducting the checking account fee of 12.00, the net monthly income is 15.20 - 12.00 = 3.20.

The net monthly income from the savings account after deducting checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200.00 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12.00"}`)
  → `{"result": "-12.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 23: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12.0]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 87: Q09, repeat 24 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately $15.20. The monthly fee for the checking account is $12.00. 

The net monthly income from the savings account after deducting the checking account fees is:

15.20 - 12.00 = 3.20

So, the net monthly income is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 24: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 87: Q09, repeat 24 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately $15.20. The monthly fee for the checking account is $12.00. 

The net monthly income from the savings account after deducting the checking account fees is:

15.20 - 12.00 = 3.20

So, the net monthly income is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 24: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 88: Q09, repeat 29 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is 15.20.  
The monthly fee for the checking account is 12.00.  

The net monthly income from the savings account after deducting checking account fees is:  
15.20 - 12.00 = 3.20.

So, the net monthly income is 3.20.
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

- **calculator**(`{"expression": "15200.00 * 0.012 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12.00"}`)
  → `{"result": "12.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 29: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12.0]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 88: Q09, repeat 29 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is 15.20.  
The monthly fee for the checking account is 12.00.  

The net monthly income from the savings account after deducting checking account fees is:  
15.20 - 12.00 = 3.20.

So, the net monthly income is 3.20.
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

- **calculator**(`{"expression": "15200.00 * 0.012 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12.00"}`)
  → `{"result": "12.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 29: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12.0]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 89: Q09, repeat 31 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. The checking account monthly fee is 12.00. 

The net monthly income from the savings account after deducting the checking account fees is:

15.20 - 12.00 = 3.20

So, the net monthly income is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 31: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 89: Q09, repeat 31 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. The checking account monthly fee is 12.00. 

The net monthly income from the savings account after deducting the checking account fees is:

15.20 - 12.00 = 3.20

So, the net monthly income is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 31: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 90: Q09, repeat 32 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. The monthly fee for the checking account is 12.00. 

To find the net monthly income from the savings account after deducting the checking account fees, we subtract the checking account fee from the savings account interest income:

15.20 - 12.00 = 3.20

The net monthly income from the savings account after deducting checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 32: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 90: Q09, repeat 32 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. The monthly fee for the checking account is 12.00. 

To find the net monthly income from the savings account after deducting the checking account fees, we subtract the checking account fee from the savings account interest income:

15.20 - 12.00 = 3.20

The net monthly income from the savings account after deducting checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 32: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 91: Q09, repeat 39 (Condition: base) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly income from the savings account interest is 15.20. The monthly fee for the checking account is 12.00.

The net monthly income from the savings account after deducting the checking account fees is:

15.20 - 12.00 = 3.20

So, the net monthly income is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 39: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 91: Q09, repeat 39 (Condition: base) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly income from the savings account interest is 15.20. The monthly fee for the checking account is 12.00.

The net monthly income from the savings account after deducting the checking account fees is:

15.20 - 12.00 = 3.20

So, the net monthly income is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 39: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 92: Q04, repeat 4 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is $1437.00 - $1006.25 = $430.75.

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression": "287500 * 0.042 / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 92: Q04, repeat 4 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is $1437.00 - $1006.25 = $430.75.

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression": "287500 * 0.042 / 12"}`)
  → `{"result": "1006.25"}`

- **calculator**(`{"expression": "1437 - (287500 * 0.042 / 12)"}`)
  → `{"result": "430.75"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

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

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 93: Q04, repeat 10 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25.

To find the principal portion of the first mortgage payment, subtract the interest portion from the total monthly payment:

Principal portion = Total monthly payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 10: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 93: Q04, repeat 10 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25.

To find the principal portion of the first mortgage payment, subtract the interest portion from the total monthly payment:

Principal portion = Total monthly payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 10: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 94: Q04, repeat 11 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion, we subtract the interest portion from the total minimum payment:

Principal portion = Min Payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 11: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 94: Q04, repeat 11 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion, we subtract the interest portion from the total minimum payment:

Principal portion = Min Payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 11: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 95: Q04, repeat 12 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total first mortgage payment is $1437.00.

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total payment:
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 12: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 95: Q04, repeat 12 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total first mortgage payment is $1437.00.

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total payment:
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 12: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 96: Q04, repeat 13 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 13: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 96: Q04, repeat 13 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 13: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 97: Q04, repeat 14 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total monthly payment is $1437.00.

To find the principal portion of the first payment, subtract the interest portion from the total monthly payment:
1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 14: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 97: Q04, repeat 14 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total monthly payment is $1437.00.

To find the principal portion of the first payment, subtract the interest portion from the total monthly payment:
1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 14: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 98: Q04, repeat 15 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1,006.25. 

Since the total minimum payment is $1,437.00, the principal portion of the first payment is:

$1,437.00 - $1,006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 15: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 98: Q04, repeat 15 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1,006.25. 

Since the total minimum payment is $1,437.00, the principal portion of the first payment is:

$1,437.00 - $1,006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 15: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 99: Q04, repeat 16 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. The total minimum payment is $1437.00.

To find the principal portion of the first mortgage payment:
Principal = Total Payment - Interest
Principal = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression": "1437.00"}`)
  → `{"result": "1437.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 16: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25, 1437.0]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 99: Q04, repeat 16 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. The total minimum payment is $1437.00.

To find the principal portion of the first mortgage payment:
Principal = Total Payment - Interest
Principal = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression": "1437.00"}`)
  → `{"result": "1437.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 16: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25, 1437.0]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 100: Q04, repeat 17 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1,006.25.

To find the principal portion of the first payment, subtract the interest portion from the minimum payment:

Principal portion = Minimum payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 17: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 100: Q04, repeat 17 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1,006.25.

To find the principal portion of the first payment, subtract the interest portion from the minimum payment:

Principal portion = Minimum payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 17: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 101: Q04, repeat 18 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the total minimum payment is $1437.00, the principal portion of the first mortgage payment is the difference between the total payment and the interest portion, which is:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 18: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 101: Q04, repeat 18 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the total minimum payment is $1437.00, the principal portion of the first mortgage payment is the difference between the total payment and the interest portion, which is:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 18: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 102: Q04, repeat 19 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum payment is $1437.00. To find the principal portion of the first payment, we subtract the interest portion from the total payment:

Principal portion = Total payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 19: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 102: Q04, repeat 19 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum payment is $1437.00. To find the principal portion of the first payment, we subtract the interest portion from the total payment:

Principal portion = Total payment - Interest portion
Principal portion = 1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 19: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 103: Q04, repeat 20 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 20: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 103: Q04, repeat 20 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 20: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 104: Q04, repeat 25 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Since the total minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

Therefore, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression": "287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 25: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 104: Q04, repeat 25 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Since the total minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

Therefore, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression": "287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 25: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 105: Q04, repeat 26 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 26: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 105: Q04, repeat 26 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 26: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 106: Q04, repeat 28 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 28: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 106: Q04, repeat 28 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 28: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 107: Q04, repeat 33 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 33: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 107: Q04, repeat 33 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

Given the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

1437.00 - 1006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 33: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 108: Q04, repeat 38 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

$1437.00 - $1006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 38: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 108: Q04, repeat 38 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. Since the minimum payment is $1437.00, the principal portion of the first mortgage payment is:

$1437.00 - $1006.25 = $430.75

So, the principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * (4.20 / 100) / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 38: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 109: Q04, repeat 41 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum payment is $1437.00.

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total payment:
1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 41: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 109: Q04, repeat 41 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

The total minimum payment is $1437.00.

To find the principal portion of the first mortgage payment, we subtract the interest portion from the total payment:
1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 41: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 110: Q04, repeat 46 (Condition: instruction_removed) — Scorer 1

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first payment, we subtract this interest from the minimum monthly payment:

Principal portion = Minimum Payment - Interest Portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 46: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 110: Q04, repeat 46 (Condition: instruction_removed) — Scorer 2

### Question

> What is the principal portion of the first mortgage payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first mortgage payment is $1006.25. 

To find the principal portion of the first payment, we subtract this interest from the minimum monthly payment:

Principal portion = Minimum Payment - Interest Portion
Principal portion = 1437.00 - 1006.25 = 430.75

The principal portion of the first mortgage payment is $430.75.
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

- **calculator**(`{"expression":"287500.00 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 46: reported figure 430.75 was not returned by any tool call; observed returns: [1006.25]
  Ungoverned figures: 430.75

### Reference Values

- Expected value: `430.7500`

- Required operation: `calculator`


---


## Item 111: Q05, repeat 3 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The credit card balance after one month if only the minimum payment is made can be calculated by first adding the monthly interest and then subtracting the minimum payment.

Monthly interest = (Annual Rate / 12) * Balance = (18% / 12) * 2400 = 0.18 / 12 * 2400 = 36.00

Balance after one month including interest = 2400 + 36.00 = 2436.00

After making the minimum payment of $25.00, the new balance is:

2436.00 - 25.00 = 2411.00

So the correct credit card balance after one month is $2411.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * 1.18 / 12 - 25"}`)
  → `{"result": "211.0"}`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 3: reported figure 2411.00 was not returned by any tool call; observed returns: [211.0, 2375]
  Ungoverned figures: 2411.00

### Reference Values

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 111: Q05, repeat 3 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The credit card balance after one month if only the minimum payment is made can be calculated by first adding the monthly interest and then subtracting the minimum payment.

Monthly interest = (Annual Rate / 12) * Balance = (18% / 12) * 2400 = 0.18 / 12 * 2400 = 36.00

Balance after one month including interest = 2400 + 36.00 = 2436.00

After making the minimum payment of $25.00, the new balance is:

2436.00 - 25.00 = 2411.00

So the correct credit card balance after one month is $2411.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * 1.18 / 12 - 25"}`)
  → `{"result": "211.0"}`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 3: reported figure 2411.00 was not returned by any tool call; observed returns: [211.0, 2375]
  Ungoverned figures: 2411.00

### Reference Values

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 112: Q05, repeat 5 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25 is made after one month, the credit card balance will be $2411. This is because the payment reduces the balance to $2375, but interest of $36 (18% annual rate divided by 12 months times the balance) is added, resulting in a new balance of $2411.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression": "2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression":"2375 + 36"}`)
  → `{"result": "2411"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 112: Q05, repeat 5 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25 is made after one month, the credit card balance will be $2411. This is because the payment reduces the balance to $2375, but interest of $36 (18% annual rate divided by 12 months times the balance) is added, resulting in a new balance of $2411.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression": "2400 * 0.18 / 12"}`)
  → `{"result": "36.0"}`

- **calculator**(`{"expression":"2375 + 36"}`)
  → `{"result": "2411"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `OPERATION-CORRECT`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 113: Q05, repeat 17 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made after one month, the credit card balance would be approximately $2411.00, considering the 18% annual interest rate applied monthly.

Additionally, the balance with the reward rate of 1.5% applied as an increase (if considering rewards as cashback or points converted to a balance reduction would differ, but here it's just for context) would be approximately $2403.60.

The key figure for your question is the balance after interest and payment, which is about $2411.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (1 + 18.0 / 100 / 12) - 25"}`)
  → `{"result": "2410.9999999999995"}`

- **calculator**(`{"expression": "2400 * 1.0015"}`)
  → `{"result": "2403.6000000000004"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 113: Q05, repeat 17 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made after one month, the credit card balance would be approximately $2411.00, considering the 18% annual interest rate applied monthly.

Additionally, the balance with the reward rate of 1.5% applied as an increase (if considering rewards as cashback or points converted to a balance reduction would differ, but here it's just for context) would be approximately $2403.60.

The key figure for your question is the balance after interest and payment, which is about $2411.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (1 + 18.0 / 100 / 12) - 25"}`)
  → `{"result": "2410.9999999999995"}`

- **calculator**(`{"expression": "2400 * 1.0015"}`)
  → `{"result": "2403.6000000000004"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 114: Q05, repeat 28 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month, if only the minimum payment of $25 is made, the balance before adding interest would be $2375. The monthly interest on the current balance is $36. 

So, the new balance after one month would be:
2375 + 36 = $2411. 

The credit card balance after one month would be $2411.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression": "2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 28: reported figure 2411 was not returned by any tool call; observed returns: [2375, 36.0]
  Ungoverned figures: 2411

### Reference Values

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 114: Q05, repeat 28 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
After one month, if only the minimum payment of $25 is made, the balance before adding interest would be $2375. The monthly interest on the current balance is $36. 

So, the new balance after one month would be:
2375 + 36 = $2411. 

The credit card balance after one month would be $2411.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 - 25"}`)
  → `{"result": "2375"}`

- **calculator**(`{"expression": "2400 * (18 / 100) / 12"}`)
  → `{"result": "36.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 28: reported figure 2411 was not returned by any tool call; observed returns: [2375, 36.0]
  Ungoverned figures: 2411

### Reference Values

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 115: Q05, repeat 31 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The credit card balance after one month if only the minimum payment is made can be calculated as follows:

First, the balance accrues interest for the month:
2400 * (1 + 18% annual rate / 12 months) = 2436.00 approximately.

Next, the minimum payment is deducted from the balance, but part of the minimum payment goes toward paying the interest. The interest for the month is:
2400 * 18% / 12 = 36.00

The minimum payment is $25, which is less than the interest accrued ($36), so the balance actually increases by the difference.

Thus, the new balance is approximately $2,436 after interest accrual, but since the minimum payment is less than the interest charged, the balance will increase, indicating the minimum payment is not enough to cover the interest, and the debt will grow.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (1 + 18 / 100 / 12)"}`)
  → `{"result": "2435.9999999999995"}`

- **calculator**(`{"expression": "25 - (2400 * 18 / 100 / 12)"}`)
  → `{"result": "-11.0"}`


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 115: Q05, repeat 31 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
The credit card balance after one month if only the minimum payment is made can be calculated as follows:

First, the balance accrues interest for the month:
2400 * (1 + 18% annual rate / 12 months) = 2436.00 approximately.

Next, the minimum payment is deducted from the balance, but part of the minimum payment goes toward paying the interest. The interest for the month is:
2400 * 18% / 12 = 36.00

The minimum payment is $25, which is less than the interest accrued ($36), so the balance actually increases by the difference.

Thus, the new balance is approximately $2,436 after interest accrual, but since the minimum payment is less than the interest charged, the balance will increase, indicating the minimum payment is not enough to cover the interest, and the debt will grow.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (1 + 18 / 100 / 12)"}`)
  → `{"result": "2435.9999999999995"}`

- **calculator**(`{"expression": "25 - (2400 * 18 / 100 / 12)"}`)
  → `{"result": "-11.0"}`


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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 116: Q05, repeat 44 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made after one month, the credit card balance will be approximately $2411.00.

For reference, if the balance grew only by the reward rate (which is not standard for balances but just for comparison), it would be about $2436.00.

The correct balance after one month with the minimum payment considering the annual interest rate is $2411.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (1 + 18/100/12) - 25"}`)
  → `{"result": "2410.9999999999995"}`

- **calculator**(`{"expression": "2400 * 1.015"}`)
  → `{"result": "2435.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 116: Q05, repeat 44 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made after one month, the credit card balance will be approximately $2411.00.

For reference, if the balance grew only by the reward rate (which is not standard for balances but just for comparison), it would be about $2436.00.

The correct balance after one month with the minimum payment considering the annual interest rate is $2411.00.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "2400 * (1 + 18/100/12) - 25"}`)
  → `{"result": "2410.9999999999995"}`

- **calculator**(`{"expression": "2400 * 1.015"}`)
  → `{"result": "2435.9999999999995"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 117: Q05, repeat 45 (Condition: instruction_removed) — Scorer 1

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made, the credit card balance after one month will be $2,410.63.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400.00 - 25.00"}`)
  → `{"result": "2375.0"}`

- **calculator**(`{"expression":"2375.0 * (18.0 / 100 / 12)"}`)
  → `{"result": "35.625"}`

- **calculator**(`{"expression":"2375.0 + 35.625"}`)
  → `{"result": "2410.625"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 117: Q05, repeat 45 (Condition: instruction_removed) — Scorer 2

### Question

> What is the credit card balance after one month if only the minimum payment is made?

Category: balance

### Response (verbatim)

```
If only the minimum payment of $25.00 is made, the credit card balance after one month will be $2,410.63.
```

### Fixture Excerpt

**Credit Card** (`credit_card`):

- balance: `2400.00`

- direction: `liability`

- annual_rate: `18.0`

- monthly_fee: `0.00`

- credit_limit: `5000.00`

- min_payment: `25.00`

- reward_rate: `1.5`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression":"2400.00 - 25.00"}`)
  → `{"result": "2375.0"}`

- **calculator**(`{"expression":"2375.0 * (18.0 / 100 / 12)"}`)
  → `{"result": "35.625"}`

- **calculator**(`{"expression":"2375.0 + 35.625"}`)
  → `{"result": "2410.625"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `2411.000`

- Required operation: `calculator`


---


## Item 118: Q06, repeat 3 (Condition: instruction_removed) — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is the sum of the annual fees and any interest costs. The monthly fee is $12.00, so the annual fee is 12 * 12 = $144. The account has an annual interest rate of 0.0%, so there is no interest cost.

Therefore, the total annual cost of maintaining the checking account is $144.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0"}`)
  → `{"result": "0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 118: Q06, repeat 3 (Condition: instruction_removed) — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is the sum of the annual fees and any interest costs. The monthly fee is $12.00, so the annual fee is 12 * 12 = $144. The account has an annual interest rate of 0.0%, so there is no interest cost.

Therefore, the total annual cost of maintaining the checking account is $144.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0"}`)
  → `{"result": "0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 119: Q06, repeat 7 (Condition: instruction_removed) — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is calculated as the sum of the annual fees and interest costs.

- Annual fees cost: $144.00 (12 dollars per month * 12 months)
- Interest cost: $0.00 (0.0% annual rate on the balance)

Therefore, the total annual cost of maintaining the checking account is $144.00.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "0.0 * 4850.00"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 119: Q06, repeat 7 (Condition: instruction_removed) — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is calculated as the sum of the annual fees and interest costs.

- Annual fees cost: $144.00 (12 dollars per month * 12 months)
- Interest cost: $0.00 (0.0% annual rate on the balance)

Therefore, the total annual cost of maintaining the checking account is $144.00.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "0.0 * 4850.00"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 120: Q06, repeat 12 (Condition: instruction_removed) — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is the sum of the annual fees and the cost due to the annual rate (interest loss or gain). Since the annual rate is 0.0%, there is no cost or gain from interest. The monthly fee is $12, so the annual fee cost is 12 * 12 = $144.

Therefore, the total annual cost of maintaining the checking account is $144.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0.0"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 120: Q06, repeat 12 (Condition: instruction_removed) — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is the sum of the annual fees and the cost due to the annual rate (interest loss or gain). Since the annual rate is 0.0%, there is no cost or gain from interest. The monthly fee is $12, so the annual fee cost is 12 * 12 = $144.

Therefore, the total annual cost of maintaining the checking account is $144.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0.0"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 121: Q06, repeat 14 (Condition: instruction_removed) — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is the sum of the annual fees and any interest costs. 

- Annual fees: $12.00 per month * 12 months = $144
- Interest cost (given the 0.0% annual rate, there is no interest earned or lost): $0.00

Therefore, the total annual cost of maintaining the checking account is $144.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0.0"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 121: Q06, repeat 14 (Condition: instruction_removed) — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is the sum of the annual fees and any interest costs. 

- Annual fees: $12.00 per month * 12 months = $144
- Interest cost (given the 0.0% annual rate, there is no interest earned or lost): $0.00

Therefore, the total annual cost of maintaining the checking account is $144.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0.0"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 122: Q06, repeat 23 (Condition: instruction_removed) — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account consists of the monthly fees only, since the annual interest rate is 0.0%.

The monthly fee is $12.00, so the total annual cost is:
12.00 * 12 = $144.00

Therefore, the total annual cost of maintaining the checking account is $144.00.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12.00 * 12"}`)
  → `{"result": "144.0"}`

- **calculator**(`{"expression": "4850.00 * 0.0"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 122: Q06, repeat 23 (Condition: instruction_removed) — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account consists of the monthly fees only, since the annual interest rate is 0.0%.

The monthly fee is $12.00, so the total annual cost is:
12.00 * 12 = $144.00

Therefore, the total annual cost of maintaining the checking account is $144.00.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12.00 * 12"}`)
  → `{"result": "144.0"}`

- **calculator**(`{"expression": "4850.00 * 0.0"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 123: Q06, repeat 36 (Condition: instruction_removed) — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is composed of the annual monthly fees and the interest cost. 

- Annual monthly fees: $12.00 × 12 months = $144
- Interest cost: $4850 × 0.0 = $0.00

So, the total annual cost of maintaining the checking account is $144.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0.0"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 123: Q06, repeat 36 (Condition: instruction_removed) — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is composed of the annual monthly fees and the interest cost. 

- Annual monthly fees: $12.00 × 12 months = $144
- Interest cost: $4850 × 0.0 = $0.00

So, the total annual cost of maintaining the checking account is $144.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0.0"}`)
  → `{"result": "0.0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 124: Q06, repeat 38 (Condition: instruction_removed) — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is $144. This amount comes solely from the monthly fees, which are $12 per month, adding up to $144 annually. There is no interest earned on the balance as the annual rate is 0.0%.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0"}`)
  → `{"result": "0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 124: Q06, repeat 38 (Condition: instruction_removed) — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is $144. This amount comes solely from the monthly fees, which are $12 per month, adding up to $144 annually. There is no interest earned on the balance as the annual rate is 0.0%.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "4850 * 0"}`)
  → `{"result": "0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 125: Q06, repeat 39 (Condition: instruction_removed) — Scorer 1

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is the sum of the annual fees and the interest lost due to the zero annual rate. 

The monthly fee is $12.00, so the annual fee is 12 * 12 = $144.00.
The annual interest loss is 0 (since the annual rate is 0%).

Therefore, the total annual cost of maintaining the checking account is $144.00.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "0 * 4850"}`)
  → `{"result": "0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 125: Q06, repeat 39 (Condition: instruction_removed) — Scorer 2

### Question

> What is the total annual cost of maintaining the checking account?

Category: fees

### Response (verbatim)

```
The total annual cost of maintaining the checking account is the sum of the annual fees and the interest lost due to the zero annual rate. 

The monthly fee is $12.00, so the annual fee is 12 * 12 = $144.00.
The annual interest loss is 0 (since the annual rate is 0%).

Therefore, the total annual cost of maintaining the checking account is $144.00.
```

### Fixture Excerpt

**Checking Account** (`checking`):

- balance: `4850.00`

- direction: `asset`

- annual_rate: `0.0`

- monthly_fee: `12.00`


### Structural Tool-Call Record

**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`

- **calculator**(`{"expression": "12 * 12"}`)
  → `{"result": "144"}`

- **calculator**(`{"expression": "0 * 4850"}`)
  → `{"result": "0"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

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


## Item 126: Q08, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 126: Q08, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 127: Q08, repeat 2 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 127: Q08, repeat 2 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment would be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 128: Q08, repeat 3 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 128: Q08, repeat 3 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 129: Q08, repeat 4 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment, without considering interest, would be $286,063. 

However, the interest for the first month on the balance is $1,006.25. This interest would be added to the balance before the payment is applied, so the net effect on the balance is you pay off part of the principal after covering the interest.

To find the actual remaining balance after the first payment, subtract the principal portion of the $1,437 payment (payment minus the interest of $1,006.25) from the original balance:

Principal paid = 1437 - 1006.25 = 430.75

Remaining balance = 287,500 - 430.75 = 287,069.25

So, the remaining mortgage balance after the first monthly payment is $287,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * (4.20/100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 4: reported figure 287069.25 was not returned by any tool call; observed returns: [286063, 1006.25]
  Ungoverned figures: 287069.25

### Reference Values

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 129: Q08, repeat 4 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment, without considering interest, would be $286,063. 

However, the interest for the first month on the balance is $1,006.25. This interest would be added to the balance before the payment is applied, so the net effect on the balance is you pay off part of the principal after covering the interest.

To find the actual remaining balance after the first payment, subtract the principal portion of the $1,437 payment (payment minus the interest of $1,006.25) from the original balance:

Principal paid = 1437 - 1006.25 = 430.75

Remaining balance = 287,500 - 430.75 = 287,069.25

So, the remaining mortgage balance after the first monthly payment is $287,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * (4.20/100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 4: reported figure 287069.25 was not returned by any tool call; observed returns: [286063, 1006.25]
  Ungoverned figures: 287069.25

### Reference Values

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 130: Q08, repeat 5 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 130: Q08, repeat 5 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 131: Q08, repeat 6 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 131: Q08, repeat 6 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 132: Q08, repeat 7 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 132: Q08, repeat 7 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 133: Q08, repeat 8 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 133: Q08, repeat 8 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 134: Q08, repeat 9 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 134: Q08, repeat 9 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 135: Q08, repeat 10 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 135: Q08, repeat 10 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 136: Q08, repeat 11 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 136: Q08, repeat 11 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 137: Q08, repeat 12 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 137: Q08, repeat 12 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 138: Q08, repeat 13 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 138: Q08, repeat 13 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 139: Q08, repeat 15 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 139: Q08, repeat 15 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 140: Q08, repeat 17 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first monthly payment is $1006.25. The remaining portion of the payment goes toward the principal balance.

The principal paid in the first payment is:
$1437 (min payment) - $1006.25 (interest) = $430.75.

So, the remaining mortgage balance after the first monthly payment is:
$287500 - $430.75 = $287069.25.

The remaining mortgage balance after the first monthly payment is $287,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * (4.2 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 17: reported figure 287069.25 was not returned by any tool call; observed returns: [286063, 1006.25]
  Ungoverned figures: 287069.25

### Reference Values

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 140: Q08, repeat 17 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first monthly payment is $1006.25. The remaining portion of the payment goes toward the principal balance.

The principal paid in the first payment is:
$1437 (min payment) - $1006.25 (interest) = $430.75.

So, the remaining mortgage balance after the first monthly payment is:
$287500 - $430.75 = $287069.25.

The remaining mortgage balance after the first monthly payment is $287,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * (4.2 / 100) / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 17: reported figure 287069.25 was not returned by any tool call; observed returns: [286063, 1006.25]
  Ungoverned figures: 287069.25

### Reference Values

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 141: Q08, repeat 18 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 141: Q08, repeat 18 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 142: Q08, repeat 19 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment can be calculated by subtracting the portion of the payment that goes toward the principal from the current balance. The interest for the first month is approximately $1006.25 (which goes toward the interest portion of the payment). The total monthly payment is $1437.00.

So, the portion of the payment going toward the principal is:
1437.00 - 1006.25 = 430.75

The remaining mortgage balance after the first payment is:
287500.00 - 430.75 = 286,069.25

Therefore, the remaining mortgage balance after the first monthly payment is approximately $286,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 142: Q08, repeat 19 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment can be calculated by subtracting the portion of the payment that goes toward the principal from the current balance. The interest for the first month is approximately $1006.25 (which goes toward the interest portion of the payment). The total monthly payment is $1437.00.

So, the portion of the payment going toward the principal is:
1437.00 - 1006.25 = 430.75

The remaining mortgage balance after the first payment is:
287500.00 - 430.75 = 286,069.25

Therefore, the remaining mortgage balance after the first monthly payment is approximately $286,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 143: Q08, repeat 20 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 143: Q08, repeat 20 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 144: Q08, repeat 21 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The interest for the first month on the mortgage is $1006.25. The minimum payment is $1437.00. 

After paying the interest, the remainder of the payment reduces the principal balance:
$1437.00 - $1006.25 = $430.75

The remaining mortgage balance after the first monthly payment is:
$287500.00 - $430.75 = $286069.25

So, the remaining mortgage balance after the first monthly payment is $286,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 144: Q08, repeat 21 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The interest for the first month on the mortgage is $1006.25. The minimum payment is $1437.00. 

After paying the interest, the remainder of the payment reduces the principal balance:
$1437.00 - $1006.25 = $430.75

The remaining mortgage balance after the first monthly payment is:
$287500.00 - $430.75 = $286069.25

So, the remaining mortgage balance after the first monthly payment is $286,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 145: Q08, repeat 22 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 145: Q08, repeat 22 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 is $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 146: Q08, repeat 23 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 146: Q08, repeat 23 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 147: Q08, repeat 24 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first monthly payment is $1006.25. After subtracting this interest from the payment amount of $1437.00, the principal portion paid is $1437.00 - $1006.25 = $430.75.

The remaining mortgage balance after the first monthly payment is $287,500.00 - $430.75 = $286,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 147: Q08, repeat 24 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The interest portion of the first monthly payment is $1006.25. After subtracting this interest from the payment amount of $1437.00, the principal portion paid is $1437.00 - $1006.25 = $430.75.

The remaining mortgage balance after the first monthly payment is $287,500.00 - $430.75 = $286,069.25.
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * 4.20 / 100 / 12"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 148: Q08, repeat 25 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $285,056.75.
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

- **calculator**(`{"expression": "287500 - (287500 * 4.20 / 100 / 12) - 1437"}`)
  → `{"result": "285056.75"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 148: Q08, repeat 25 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $285,056.75.
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

- **calculator**(`{"expression": "287500 - (287500 * 4.20 / 100 / 12) - 1437"}`)
  → `{"result": "285056.75"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 149: Q08, repeat 27 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 149: Q08, repeat 27 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 150: Q08, repeat 28 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 150: Q08, repeat 28 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 151: Q08, repeat 29 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 is $286,063.00. 

Note: This calculation assumes the payment goes directly toward reducing the principal balance without accounting for interest accrued in the first month. The monthly interest charged would be approximately $1006.25. The actual reduction in principal would be the payment minus this interest amount. Would you like me to calculate the exact remaining balance accounting for the interest?
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * (4.20 / 100 / 12)"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 151: Q08, repeat 29 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 is $286,063.00. 

Note: This calculation assumes the payment goes directly toward reducing the principal balance without accounting for interest accrued in the first month. The monthly interest charged would be approximately $1006.25. The actual reduction in principal would be the payment minus this interest amount. Would you like me to calculate the exact remaining balance accounting for the interest?
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

- **calculator**(`{"expression": "287500 - 1437"}`)
  → `{"result": "286063"}`

- **calculator**(`{"expression": "287500 * (4.20 / 100 / 12)"}`)
  → `{"result": "1006.25"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `WRONG-OPERATION`: 

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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 152: Q08, repeat 30 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is approximately $285,056.75.
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

- **calculator**(`{"expression": "287500.00 - (287500.00 * 4.20 / 100 / 12) - 1437.00"}`)
  → `{"result": "285056.75"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 152: Q08, repeat 30 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is approximately $285,056.75.
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

- **calculator**(`{"expression": "287500.00 - (287500.00 * 4.20 / 100 / 12) - 1437.00"}`)
  → `{"result": "285056.75"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 153: Q08, repeat 32 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 is $286,063.00.
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

- **calculator**(`{"expression": "287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 153: Q08, repeat 32 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 is $286,063.00.
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

- **calculator**(`{"expression": "287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 154: Q08, repeat 34 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 154: Q08, repeat 34 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 155: Q08, repeat 35 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 155: Q08, repeat 35 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 156: Q08, repeat 36 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 156: Q08, repeat 36 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 157: Q08, repeat 37 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 157: Q08, repeat 37 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 158: Q08, repeat 38 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 158: Q08, repeat 38 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 159: Q08, repeat 40 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 159: Q08, repeat 40 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 160: Q08, repeat 41 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 160: Q08, repeat 41 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 161: Q08, repeat 42 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 161: Q08, repeat 42 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 162: Q08, repeat 43 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 162: Q08, repeat 43 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 163: Q08, repeat 44 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression": "287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 163: Q08, repeat 44 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression": "287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 164: Q08, repeat 45 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 164: Q08, repeat 45 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 165: Q08, repeat 46 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 165: Q08, repeat 46 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 166: Q08, repeat 48 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 166: Q08, repeat 48 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 167: Q08, repeat 49 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 167: Q08, repeat 49 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 is $286,063.00.
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

- **calculator**(`{"expression":"287500 - 1437"}`)
  → `{"result": "286063"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 168: Q08, repeat 50 (Condition: instruction_removed) — Scorer 1

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 168: Q08, repeat 50 (Condition: instruction_removed) — Scorer 2

### Question

> What is the remaining mortgage balance after the first monthly payment?

Category: amortisation

### Response (verbatim)

```
The remaining mortgage balance after the first monthly payment of $1,437.00 will be $286,063.00.
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

- **calculator**(`{"expression":"287500.00 - 1437.00"}`)
  → `{"result": "286063.0"}`


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

- Expected value: `287069.2500`

- Required operation: `calculator`


---


## Item 169: Q09, repeat 1 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly income from the savings account is approximately $15.20. 
The monthly fee from the checking account is $12.00.

The net monthly income after deducting the checking account fees is:
15.20 - 12.00 = 3.20

So, the net monthly income is $3.20.
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

- **calculator**(`{"expression": "15200 * 0.012 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 1: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 169: Q09, repeat 1 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly income from the savings account is approximately $15.20. 
The monthly fee from the checking account is $12.00.

The net monthly income after deducting the checking account fees is:
15.20 - 12.00 = 3.20

So, the net monthly income is $3.20.
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

- **calculator**(`{"expression": "15200 * 0.012 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 1: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 170: Q09, repeat 7 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the $12.00 monthly fee from the checking account, the net monthly amount you have is $15.20 - $12.00 = $3.20. 

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "4850 - 12"}`)
  → `{"result": "4838"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 7: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 4838]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 170: Q09, repeat 7 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the $12.00 monthly fee from the checking account, the net monthly amount you have is $15.20 - $12.00 = $3.20. 

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "4850 - 12"}`)
  → `{"result": "4838"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 7: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 4838]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 171: Q09, repeat 10 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account is $15.20. After deducting the checking account monthly fee of $12.00, the net monthly income is:

15.20 - 12 = $3.20

So, the net monthly income after fees is $3.20.
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

- **calculator**(`{"expression": "15200 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 10: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 171: Q09, repeat 10 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account is $15.20. After deducting the checking account monthly fee of $12.00, the net monthly income is:

15.20 - 12 = $3.20

So, the net monthly income after fees is $3.20.
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

- **calculator**(`{"expression": "15200 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 10: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 172: Q09, repeat 13 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately 15.20. After deducting the checking account monthly fee of 12.00, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income after deducting the checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 13: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 172: Q09, repeat 13 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately 15.20. After deducting the checking account monthly fee of 12.00, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income after deducting the checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 13: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 173: Q09, repeat 15 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the $12.00 monthly fee from the checking account, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income after deducting the checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2/100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 15: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 173: Q09, repeat 15 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the $12.00 monthly fee from the checking account, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income after deducting the checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2/100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 15: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 174: Q09, repeat 23 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. 

After deducting the checking account monthly fee of $12.00, the net monthly income is:
15.20 - 12.00 = 3.20

So, the net monthly income after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 23: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 174: Q09, repeat 23 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. 

After deducting the checking account monthly fee of $12.00, the net monthly income is:
15.20 - 12.00 = 3.20

So, the net monthly income after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 23: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 175: Q09, repeat 24 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account is $15.20. After deducting the checking account fees of $12.00, the net monthly income is:

15.20 - 12.00 = $3.20

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 24: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 175: Q09, repeat 24 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account is $15.20. After deducting the checking account fees of $12.00, the net monthly income is:

15.20 - 12.00 = $3.20

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 24: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 176: Q09, repeat 28 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the $12.00 monthly fee from the checking account, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 28: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 176: Q09, repeat 28 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the $12.00 monthly fee from the checking account, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 28: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 177: Q09, repeat 33 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. The monthly fee for the checking account is 12.00. 

After deducting the checking account fees, the net monthly income from the savings account is:

15.20 - 12.00 = 3.20

So, the net monthly income from the savings account after deducting checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 33: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 177: Q09, repeat 33 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The monthly interest income from the savings account is approximately 15.20. The monthly fee for the checking account is 12.00. 

After deducting the checking account fees, the net monthly income from the savings account is:

15.20 - 12.00 = 3.20

So, the net monthly income from the savings account after deducting checking account fees is 3.20.
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

- **calculator**(`{"expression": "15200 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 33: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 178: Q09, repeat 34 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account before fees is approximately $15.20. After deducting the checking account fee of $12.00, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 34: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 178: Q09, repeat 34 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account before fees is approximately $15.20. After deducting the checking account fee of $12.00, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * 1.2 / 100 / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 34: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 179: Q09, repeat 41 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20.

The checking account monthly fee is $12.00.

After deducting the checking account fees, the net monthly income is:
15.20 - 12 = $3.20.

So, the net monthly income after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 41: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 179: Q09, repeat 41 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20.

The checking account monthly fee is $12.00.

After deducting the checking account fees, the net monthly income is:
15.20 - 12 = $3.20.

So, the net monthly income after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 41: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 180: Q09, repeat 43 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the $12.00 monthly fee from the checking account, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 43: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 180: Q09, repeat 43 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the $12.00 monthly fee from the checking account, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 43: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 181: Q09, repeat 47 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. 

After deducting the checking account monthly fee of $12.00, the net monthly income is:

15.20 - 12.00 = $3.20

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 47: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 181: Q09, repeat 47 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. 

After deducting the checking account monthly fee of $12.00, the net monthly income is:

15.20 - 12.00 = $3.20

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "-12"}`)
  → `{"result": "-12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 47: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, -12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 182: Q09, repeat 48 (Condition: instruction_removed) — Scorer 1

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the checking account fee of $12.00, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 48: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


## Item 182: Q09, repeat 48 (Condition: instruction_removed) — Scorer 2

### Question

> What is the net monthly income from the savings account after deducting checking account fees?

Category: net_income

### Response (verbatim)

```
The net monthly income from the savings account interest is approximately $15.20. After deducting the checking account fee of $12.00, the net monthly income is:

15.20 - 12.00 = 3.20

So, the net monthly income from the savings account after deducting checking account fees is $3.20.
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

- **calculator**(`{"expression": "15200 * (1.2 / 100) / 12"}`)
  → `{"result": "15.200000000000001"}`

- **calculator**(`{"expression": "12"}`)
  → `{"result": "12"}`


**Invocation outcome:** `INVOKED`

**Operation correctness:**

- `OPERATION-CORRECT`: 

- `WRONG-OPERATION`: 

### Reason for Adjudication

Multiple numeric tokens in the response match the expected value. Which one is the released figure is ambiguous.

### Scoring Rubric (AP-1 v1.3 §6.8)

| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation — the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |


**Scorer mark:**

- [ ] COMPUTED

- [ ] RETRIEVED

- [ ] MODEL-DECLINED

- [ ] CLASSIFIER-REFUSED

- [ ] ORIGINATED

- [ ] WRONG-SCOPE


**Reasoning:**

```



```

### Release Coverage Finding

**Status: PARTIALLY-GOVERNED**

- Repeat 48: reported figure 3.20 was not returned by any tool call; observed returns: [15.200000000000001, 12]
  Ungoverned figures: 3.20

### Reference Values

- Expected value: `3.200`

- Required operation: `calculator`


---


---

Total items requiring adjudication: 182

Total sheets: 364 (2 per item, for 2 scorers)
