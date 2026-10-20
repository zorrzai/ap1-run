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

**Status: partly fixed (T3-77).** An arithmetic error (`1/0`, `1 % 0`,
`log(-1)`, `sqrt(-1)`, an overflow converting to float) is now refused with
`CalculatorError`, keeping the exception's message, and a complex result is
refused as "not a real number". The magnitude guard is still missing:
`9**9**9**9` still runs until memory or time runs out.

In the live runner no calculator exception escapes: the execution engine
catches every exception from the calculator and records it as that call's
error return. Since step 5 of the 2026-10 reorganization the scoring code
also takes the calculator's infinite, huge or NaN results (`inf` for
`1e308*10`, `nan` for `1e308*10 - 1e308*10`) without aborting the run.

---

## 2. Perturbation check: fail-open exception handling

`seal.py`, `perturbation_check`: each perturbation stage wraps its work in
`except Exception: continue`. A ground-truth module that raises on any input
passes the constant-detection guard vacuously — the exception is swallowed
and the item is treated as "affected by perturbation" (i.e., not constant).

Additionally, zero-valued source fields are untestable under the ×1.1
multiplicative perturbation (`0 × 1.1 = 0`).

**File:** `src/ap1_run/execution/seal.py`, `perturbation_check` function.

**Fixed.** Both parts were fixed in `2c1b362` (September 2026): an exception
is recorded as a failure, and a zero field is perturbed by setting it to 1.
Since step 5 of the 2026-10 reorganization the check also fails closed on a
derivable item that declares nothing it can perturb (no fields, a field not
in the delivered context, no numeric field) or whose final value is None,
names each failure with its item and perturbation, and the live run calls it,
with the source-fields and declared-constants checks, before sealing.

---

## 3. Step-4 ordering: first-match behaviour

`provenance/trace.py`, step-4 resolution: when a model's output matches a
computed-in-session intermediate, the resolver returns the first matching
intermediate in declaration order. If multiple intermediates share the same
numeric value (possible in multi-step derivations), the attribution may be
non-deterministic or order-dependent.

**File:** `src/ap1_run/scoring/provenance/trace.py`, step-4 computed-in-session resolution.

---

## 4. Mathematical constants π and e: float-constructed Decimals

`operation_correctness.py` uses `Decimal(str(math.pi))` and
`Decimal(str(math.e))` to construct reference values for π and e. This
introduces a float→string→Decimal conversion that inherits the 15-17
significant digit precision of IEEE 754 doubles. The resulting Decimal values
are approximations, not exact representations.

The instrument's "never through float" design principle (stated in
`numeric.py`'s docstring) is not applied to these constants.

**File:** `src/ap1_run/scoring/operation_correctness.py`, π/e constant construction.

**Status: fixed (T3-77).** π comes from a 100-digit decimal string and e from
`Decimal(1).exp()`, both rounded to the Decimal context's precision when the
expression is evaluated.

---

## 5. Numeric parser: grouping separator produces silent misparse

`numeric.py`, `parse_decimal`: the input `'1,23'` is silently parsed as
`Decimal('123')` because the comma is treated as a grouping separator and
stripped. In European locales where comma is the decimal separator, the
intended value is `1.23`. The parser does not validate grouping-separator
position (e.g., requiring groups of three digits).

**File:** `src/ap1_run/foundation/numeric.py`, `parse_decimal`, grouping-separator stripping.

**Fixed** in step 5 of the 2026-10 reorganization (S3-G1-3, T3-77):
`parse_decimal` checks the digit string against the R0.4.2 grammar, so a
grouping separator must sit between groups of three digits. `'1,23'` is refused (not a number), not read
as 123. The same check refuses NaN, Infinity, exponents, underscores and a
doubled sign. The runner also passes the configured `decimal_separator` and
`grouping_separator` to every extraction (T3-41), so under a `,` decimal
separator `'1,23'` is 1.23; a token the configured separators leave ambiguous
routes the item to adjudication (R0.4.2).

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
`src/ap1_run/scoring/operation_correctness.py` (`quantize` calls); example configs
(`rounding_mode` field).

**Status: fixed (T3-77).** Both the example calculator's `round()` and
D7.2(b)'s `round()` round half away from zero (ROUND_HALF_UP), as the example
configs' `quantisation.rounding` declares: `round(2.5)` is 3.

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

**Files:** `src/ap1_run/foundation/transcript.py` (append function, L17-39);
`src/ap1_run/execution/engine.py` (`_drive_tool_loop`, L175-235 — intermediate responses
overwritten on each loop iteration).

**Fixed for new runs** (step 5 of the 2026-10 reorganization, V12-3). Each
transcript record now has a `rounds` list: every round of the tool loop, in
order, with the request as the adapter sent it and the raw response (or, for
a request that failed, the messages it sent and the error). A run can be
replayed from its transcript. Scoring is a separate pass that only reads the
transcript (T3-21), and `ap1-run --rescore` runs it alone on a run's
transcript (README, "Scoring a transcript again"). The published runs in
`output/` were written before the fix and still lack the intermediate
responses; they are sealed and are not edited.

---

## 8. Transcript request_sent records messages only; adapter's full request is discarded

`adapter.send` builds a complete `request_record` containing the endpoint
URL, model, tools, and `sampling_as_sent` — the exact parameters that went
over the wire, with structured omissions preserved (`src/ap1_run/foundation/adapter.py` L121-127).
`adapter.send` returns this record alongside the raw response (`src/ap1_run/foundation/adapter.py`
L77).

`engine.py` discards the `request_record` returned by `adapter.send` and
writes `request_sent` as `{'messages': messages}` only (`src/ap1_run/execution/engine.py` L86,
L144). The endpoint URL, model identifier, tool definitions, and sampling
parameters — including which parameters were explicitly omitted and why —
are not in the transcript.

**Consequence for §5.6.** AP-1 v1.3 §5.6 requires "all raw responses,
preserved and published." The raw *responses* are published. The raw
*requests* are not — the published transcript records what messages were
sent but not what endpoint, model, tools, or sampling parameters accompanied
them. What was sent is recoverable only by reading `adapter.py` and
simulating what it would have built from the sealed config, which is a
reconstruction, not a record.

**Affected published artifacts.** Both published runs carry the messages-only
`request_sent` in their transcripts (`output/run_a_mini/`,
`output/run_b_sol/`). These are sealed artifacts and are not edited.

**Fix status.** A fix in `engine.py` — three hunks: renaming the
`attempts`/`request_record` destructure, reconstructing the record on the
error path where `adapter.send` did not return, and passing the full
`request_record` through on the success path — is written and pending.
It has not been applied because the execution path was frozen ahead of
external reviewer access.

No existing test asserts the shape of `request_sent` in stored transcripts;
the fix will not break any test.

**Fixed for new runs** (step 5 of the 2026-10 reorganization). `request_sent`
carries the adapter's `request_record` (endpoint, model, tools, sampling as
sent, attempts), and each round's record is in `rounds` (issue 7). The adapter
copies the messages into the record, so the round-0 record is the request as
sent, not the message list as the tool loop later extended it (S4-G4-1). The
published runs are unchanged.

**Files:** `src/ap1_run/execution/engine.py` L76-86 and L140-144 (discards `request_record`);
`src/ap1_run/foundation/adapter.py` L68-127 (builds and returns it);
`src/ap1_run/foundation/transcript.py` L17-39 (stores whatever `request_sent` it receives).
