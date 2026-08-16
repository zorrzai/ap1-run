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

## What Has Not Been Tested

Declared before a reviewer finds them:

- **The agreement test covers shim.py and scorer.py only.** solver.py,
  task.py, metrics.py and compare.py are not exercised by it. Those
  modules are used only inside `inspect eval`, which is not part of the
  agreement test path.

- **No end-to-end `inspect eval` has been run and compared against an
  engine.py run.** The agreement test uses mock scenarios, not a live
  model call through both paths with output comparison.

- **The fixture is 10 items.** All 10 are derivable and all 10 are covered
  by the agreement test. This is the example fixture, not a sealed
  evaluation set.

- **EV-2 on the Inspect path is argued structurally and is NOT mechanically
  verified by verify_conformance.py.** The conformance suite tests runner
  internals; it does not trace the Inspect provider-to-scorer chain.
  The argument below (in Evidence Class) is a prose argument, not a
  machine-checked proof.

## Architecture

```
ap1_inspect/
  shim.py     Inspect ToolCall → runner dict shape. ~15 lines.
  solver.py   Custom solver wrapping generate_loop().
  scorer.py   Imports runner classifiers, calls them through shim.
  task.py     @task functions with R1.1 seal enforcement.
  metrics.py  Clopper-Pearson as a custom Inspect metric.
  compare.py  Post-processing for cross-condition D7.1.
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
        → shim.inspect_tc_to_runner (field access only)
          → runner's classify_invocation
```

Inspect is a third party to both the model and to the runner. An
intermediary that preserves a record without interpreting it does not
change its evidence class.
