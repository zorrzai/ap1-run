# AP-1 Inspect Wrapper

Thin integration layer that runs AP-1 evaluations inside the
[UK AI Security Institute's Inspect framework](https://inspect.aisi.org.uk/).

**No measurement logic lives here.** Every classification call — evidence,
invocation, accuracy, operation correctness, provenance — goes to the
runner's existing modules.

## Dependencies

The **runner core** requires one dependency: `requests`. Its dependency surface
is readable by an information-security function in minutes.

The **optional Inspect integration** (this directory) additionally requires
`inspect-ai` and is not needed to run AP-1 directly.

```
pip install -r ap1_inspect/requirements.txt
```

## Usage

These are the intended invocations; they have not been executed end-to-end,
and the modules they drive are listed under "What Has Not Been Tested".

```bash
# Base condition
inspect eval ap1_inspect/task.py@ap1_base --model openai/gpt-5.6-sol

# Instruction-removed condition
inspect eval ap1_inspect/task.py@ap1_instruction_removed --model openai/gpt-5.6-sol

# Both conditions via eval-set
inspect eval-set ap1_inspect/task.py@ap1_base ap1_inspect/task.py@ap1_instruction_removed \
    --model openai/gpt-5.6-sol --log-dir logs/run-1

# Cross-condition D7.1 comparison (post-processing)
python -m ap1_inspect.compare logs/run-1/base.eval logs/run-1/ir.eval
```

## What This Enables

AP-1 running inside Inspect inherits every model provider Inspect supports:
OpenAI, Anthropic, Google, Bedrock, Azure, vLLM, and others. An evaluation
standard that speaks only one provider's API shape is not a general standard.

## Known Limitations

These are stated plainly before anyone finds them:

- **D3 to D6** require human adjudication regardless of framework. No
  automation changes this — adjudication is a normative requirement of the
  standard, not a limitation of the instrument.

- **Cross-condition D7.1** (the instruction-removal finding) is
  post-processing over two eval logs, not a native Inspect feature. Both
  conditions must be run as separate tasks, and comparison is computed
  afterward by `compare.py`.

- **D2 reproducibility** is classified by a custom metric reading unreduced
  epoch scores. Run with `epochs=N` and use `--no-epochs-reducer` to preserve
  per-epoch scores for D2 classification.

## What Has Been Verified

- **Shim and classifier path: verified against live run data.** The shim
  and classifier pipeline (shim.py → classify_invocations_sequential)
  has been tested against 500 base-condition Run A records with 170
  step-4 (computed in session) resolutions and zero classification
  disagreements between the runner and Inspect paths. This covers all
  10 items, both single- and multi-call sequences, and chained
  provenance with return-value propagation.

## What Has Not Been Tested

Declared before a reviewer finds them:

- **solver.py, task.py, metrics.py and compare.py remain unexercised.**
  The comparison was classifier-level: both paths received the same
  tool-call records with return values and classified them
  independently. The modules that construct those records inside
  `inspect eval` (solver.py), define the Inspect task (task.py),
  compute metrics (metrics.py), and compare conditions (compare.py)
  are not part of the agreement test path.

- **No end-to-end `inspect eval` has been compared against an engine.py
  run.** This would require replaying recorded API responses through
  Inspect's model interface. The runner's transcript stores only the
  final API response and the accumulated tool-call records; it does not
  store the intermediate API responses (those containing tool_calls)
  that drive the tool loop. No existing run can be replayed through
  Inspect without a fresh recording run that captures all intermediate
  responses.

- **The fixture is 10 items.** All 10 are derivable and all 10 are
  covered by the agreement test, plus two derived step-4 scenarios
  that simulate model quantisation. This is the example fixture, not
  a sealed evaluation set.

- **EV-2 on the Inspect path is argued structurally and is NOT
  mechanically verified by verify_conformance.py.** The conformance
  suite tests runner internals; it does not trace the Inspect
  provider-to-scorer chain. The argument below (in Evidence Class) is
  a prose argument, not a machine-checked proof. The EV-2 claim is
  scoped to the OpenAI Responses chain at inspect-ai 0.3.255;
  provider-agnostic execution does not mean equivalent evidence quality
  across all providers.

- **Replay blind spot.** The agreement test constructs tool-call records
  and classifies them; it does not replay a model conversation through
  Inspect's generate loop. If solver.py's message-walk produces a
  different tool-call record from the same model output (e.g. a bug in
  turn numbering or tool-call pairing), the agreement test cannot
  detect it. This gap is closed only by a full `inspect eval` run
  compared against engine.py output on the same model responses.

## Defects Found During Verification

### Shim dropped return_value (found by audit, fixed pre-release)

The shim (`inspect_tc_to_runner`) did not carry the tool return value
from `ChatMessageTool.content` to the runner's `return_value` field.
This meant `prior_returns` was always empty on the Inspect path, and
every step-4 operand fell through to step 5 (ORIGINATED).

**Impact on the shipped fixture:** against Run A (1,000 executions,
4,799 operand resolutions), the runner classifies 83 operands as
ORIGINATED. With `prior_returns` empty, every operand that should
resolve at step 4 (computed_in_session) instead falls through to
ORIGINATED, inflating the count from 83 to 507 of 4,799 — from 1.7%
to 10.6%, a six-fold inflation on the dimension AP-1 exists to measure.

**How it was found:** by code audit of the shim against engine.py's
`_drive_tool_loop`, not by the agreement test. The agreement test
could not have found it: every scenario was a single tool call with no
return value to propagate, so both paths received `None` for
`return_value` and agreed.

**What the agreement test's passing result meant before the fix:**
field-name conversion (`ToolCall.function` → `function.name`) and
single-turn provenance agreement, not chained provenance with
return-value propagation.

**Fix:** solver.py now extracts `ChatMessageTool.text` (handling both
`str` and `list[Content]`) and passes it through the shim with JSON
validation. The shim raises `ShimError` if the return value is not a
valid JSON string, matching engine.py's `EngineError` on the same
failure.

**Verification:** 500 Run A records, 170 step-4 resolutions, zero
disagreements between runner and Inspect paths.

## Architecture

```
ap1_inspect/
  shim.py      87 lines. ToolCall → runner dict, JSON validation, ShimError.
  solver.py   124 lines. Custom solver wrapping generate_loop().
  scorer.py   128 lines. Imports runner classifiers, calls them through shim.
  task.py     163 lines. @task functions with R1.1 seal enforcement.
  metrics.py   44 lines. Clopper-Pearson as a custom Inspect metric.
  compare.py  104 lines. Post-processing for cross-condition D7.1.
```

The dependency runs one way only: wrapper imports runner. Nothing in
the runner core imports from ap1_inspect.

## Evidence Class

Tool-call records on the Inspect path are EV-2 PLATFORM-STRUCTURAL.
The chain from provider API to scorer is structural at every hop:

```
Provider API response (structured field)
  → OpenAI SDK ResponseFunctionToolCall (typed dataclass)
    → Inspect parse_tool_call (json.loads on arguments string)
      → Inspect ToolCall dataclass
        → shim.inspect_tc_to_runner (field access + JSON validation;
            raises ShimError on malformed input, never degrades silently)
          → runner's classify_invocation
```

Validation that rejects malformed input is structural: it preserves or
refuses the record, never reinterprets it. The evidence class is unchanged.
