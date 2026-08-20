# Known Issues

Issues identified during the pre-publication adversarial review (August 2026).
Each is a known limitation of the reference implementation, not a defect in the
AP-1 v1.3 standard. None affects the correctness of the published FINDINGS.md
figures; each affects the instrument's behaviour on inputs outside the shipped
example's tested range.

---

## 1. Calculator: uncaught exceptions and missing magnitude guard

`example/calculator_tool.py` wraps only `SyntaxError`. Division by zero
(`1/0`), domain errors (`log(-1)`, `sqrt(-1)`), and huge-integer overflow
(`9**9**9**9`) escape the `CalculatorError` contract and propagate into the
runner as unhandled exceptions. The 500-character input limit does not prevent
expressions that exhaust memory within that budget.

Additionally, `(-8) ** 0.5` returns a complex number; `str(result)` emits it
without warning.

**File:** `example/calculator_tool.py`, expression evaluation block.

---

## 2. Perturbation check: fail-open exception handling

`seal.py`, `perturbation_check`: each perturbation stage wraps its work in
`except Exception: continue`. A ground-truth module that raises on any input
passes the constant-detection guard vacuously — the exception is swallowed
and the item is treated as "affected by perturbation" (i.e., not constant).

Additionally, zero-valued source fields are untestable under the ×1.1
multiplicative perturbation (`0 × 1.1 = 0`).

**File:** `seal.py`, `perturbation_check` function.

---

## 3. Step-4 ordering: first-match behaviour

`provenance.py`, step-4 resolution: when a model's output matches a
computed-in-session intermediate, the resolver returns the first matching
intermediate in declaration order. If multiple intermediates share the same
numeric value (possible in multi-step derivations), the attribution may be
non-deterministic or order-dependent.

**File:** `provenance.py`, step-4 computed-in-session resolution.

---

## 4. Mathematical constants π and e: float-constructed Decimals

`operation_correctness.py` uses `Decimal(str(math.pi))` and
`Decimal(str(math.e))` to construct reference values for π and e. This
introduces a float→string→Decimal conversion that inherits the 15-17
significant digit precision of IEEE 754 doubles. The resulting Decimal values
are approximations, not exact representations.

The instrument's "never through float" design principle (stated in
`numeric.py`'s docstring) is not applied to these constants.

**File:** `operation_correctness.py`, π/e constant construction.

---

## 5. Numeric parser: grouping separator produces silent misparse

`numeric.py`, `parse_decimal`: the input `'1,23'` is silently parsed as
`Decimal('123')` because the comma is treated as a grouping separator and
stripped. In European locales where comma is the decimal separator, the
intended value is `1.23`. The parser does not validate grouping-separator
position (e.g., requiring groups of three digits).

**File:** `numeric.py`, `parse_decimal`, grouping-separator stripping.

---

## 6. Rounding mode: HALF_EVEN in code vs ROUND_HALF_UP in configs

The example configs (`config.json`, `config.demo.json`, `config_mini.json`)
all seal `"rounding_mode": "ROUND_HALF_UP"`. The calculator tool
(`calculator_tool.py`) uses Python's built-in `round()`, which applies
HALF_EVEN (banker's rounding). The operation_correctness module's reference
comparisons also use `ROUND_HALF_EVEN` via `Decimal.quantize`.

Both the tool and the scorer apply the same (wrong) rounding mode, so the
mismatch is invisible to tool-vs-scorer consistency checks. It is visible
only when a specific input hits the 0.5 ULP boundary — e.g., `2.5` rounds
to `2` under HALF_EVEN but `3` under HALF_UP.

**Files:** `example/calculator_tool.py` (`round()`);
`operation_correctness.py` (`quantize` calls); example configs
(`rounding_mode` field).

---

## 7. Transcript does not store intermediate API responses

The runner's transcript (R0.3) stores the final API response and the
accumulated tool-call records, but not the intermediate API responses
that contained tool_calls during the tool loop. This means:

- **Re-scoring is possible.** A third party can re-run the classifier
  on the stored tool-call records and verify that classification is
  deterministic and reproducible.

- **Replay is not possible.** The conversation cannot be replayed
  through a different framework (e.g. Inspect) or a mock model,
  because the intermediate model responses that drove the tool loop
  are not available. Independent reproduction requires a fresh run
  against the same model, which is non-deterministic.

This bounds what "independent reproduction" means for AP-1: it means
re-scoring from the stored record, not replaying the model
conversation. The standard draws this distinction explicitly (v1.3
§6.7: "the raw responses are published (§5.6) so any party may
re-score").

**Files:** `transcript.py` (append function, L17-39);
`engine.py` (`_drive_tool_loop`, L175-235 — intermediate responses
overwritten on each loop iteration).
