# ap1-run

**A reference instrument for The Admissibility Protocol (AP-1).**

It measures whether the numbers a deployed AI system produces can be traced back to where they came from.

---

> ### Status: not independently run
>
> No party unconnected to the author has executed this instrument. Independent
> runnability is a stated gate in the build specification (R4.2) and it has not
> been met. **Do not describe this as independently validated.**
>
> If you run it and something breaks, that is the report we most want. Open an
> issue.

---

## What it does

It runs a question set against a deployed AI system and asks, for every numeric
answer:

| | Question | Automated |
|---|---|---|
| **D1** | Was the answer correct? | Yes, where unambiguous |
| **D2** | Is it reproducible — and by what mechanism? | Yes |
| **D7.1** | Did the required computation actually run? | Yes |
| **D7.2(a)** | Did every operand entering it come from the source data? | **Yes** |
| **D7.2(b)** | Was the formula the one the question required? | Yes |
| **D7.3** | Is the released figure the one the computation returned? | Yes |
| **D3–D6** | Provenance, refusal integrity, adversarial resistance, degraded data | No — human adjudication |

**D7.2(a) is the distinguishing measurement.** It resolves each operand
against the source values and the legitimate intermediates of a reference
derivation.

D3, D4, D5 and D6 are all scored by human adjudication. The instrument enforces
the minimum-item counts for D5 and D6 at load, and generates adjudication sheets
for all four, but scores none of them.

### The finding it exists to surface

Not *this system is wrong*. This:

> **The system gave the right answer and cannot show you why.**

or, harder:

> **It invoked the correct calculator, the arithmetic was exact, and one of the
> inputs came from nowhere.**

Both have been observed. See [`example/README.md`](example/README.md) for the
second, taken from a live run against a frontier model.

---

## Requirements

**Python 3.11 or later.**

**One dependency:** `requests`. Everything else is standard library.
The optional Inspect integration (`ap1_inspect/`) additionally requires
`inspect-ai` and is not needed to run AP-1 directly.

**Operating system:** Linux, macOS or Windows. The instrument and all thirteen test
suites are platform-independent — no OS-specific calls exist in any instrument
module.

**No GPU, no container, no database, no cloud account, no admin rights.** The
instrument makes no network call except to the endpoint under test.

### For the worked example only

An **OpenAI-compatible chat-completions endpoint with tool calling**, and an API
key.

```bash
export AP1_SMOKE_API_KEY=<key>        # Linux, macOS
set AP1_SMOKE_API_KEY=<key>           # Windows
```

On Windows the key may optionally be read from the Credential Manager instead;
see [`SECURITY.md`](SECURITY.md). Never place a key in a file, a config, or a
command line.

Running the test suites requires none of this — they are offline.

### What it will not run against

- A **retrieval system** with no computation to observe. D7 returns
  unobservable, correctly.
- An endpoint exposing a **response shape other than OpenAI-compatible chat
  completions**. Declared unobservable with a diagnostic, never scored.
- A **non-language-model estimator**. Out of reach entirely.

---

## Quick start

```bash
git clone <this repo>
cd <clone directory>
pip install -e .              # the ap1_run package and its one dependency, requests
python run_all_tests.py       # offline, reports its own totals
```

Then run the worked example against your own endpoint:

```bash
export AP1_SMOKE_API_KEY=<key>
ap1-run                       # or: python smoke_test.py
```

`python smoke_test.py` still works, even without the install step: it is a
shim for the runner, which now lives in `src/ap1_run/run.py`. The runner reads
`example/` and `reference/` and writes `output/` relative to the clone, so run
it from a clone (an editable install), not from a wheel.

`run_all_tests.py` reports two columns. `verify.py` counts individual
assertions; the other suites count test functions. Running `pytest` directly
reports the function count only — both numbers are shown so neither is mistaken
for the other.

---

## What it deliberately does not do

- **The instrument executes no language model.** The system under test
  does — that is what is being measured. Fixtures and expected values are
  static, scoring is regex extraction and float comparison within declared
  tolerance, figure identification is deterministic numeric matching, and
  re-running against the same fixture yields identical ground truth.
  The fixtures and expected values were authored by an AI coding agent, not
  derived from an independent source.
- **No guessing.** Where automated identification is ambiguous, the item goes to
  a human. A response that declines is never auto-scored as a figure.
- **No automation of D3–D6.** Judging whether a refusal was correct means
  judging meaning, and the only available automation is a language model.
  Using one would place a model in the scoring loop for dimensions that
  require human judgement. Human adjudication is the design, not a gap
  awaiting better tooling.
- **No network egress** beyond the endpoint under test.
- **No telemetry, no analytics, no hosted service.** If the author ran it for
  you, it would be the author's result again.

### What it cannot measure

It measures systems that **compute**. A system that retrieves an answer from a
corpus rather than deriving it returns unobservable results on D7 — correctly,
since there is no computation to observe.

It reaches **one interface class**. Systems exposing other response shapes are
declared `UNOBSERVABLE` with a diagnostic naming the shape, never scored.

It cannot reach a **non-language-model estimator** at all. AP-1's dimensions are
defined over any system in which a statistical component participates in
numerical output; this instrument's reach is narrower than the standard's scope.

---

## How operand provenance works

For every numeric operand passed to a computation, five steps, in order:

1. **Source value** — equals a value in the item's delivered context, exactly, at
   full precision.
2. **Transformed source** — equals a source value under a transformation declared
   before the run.
3. **Reference intermediate** — equals an intermediate of the reference
   derivation; raw, transformed, or quantised under the declared policy.
4. **Computed in session** — equals the return value of a prior invocation,
   **and that invocation was itself operands-grounded.**
5. Otherwise — **originated**.

**Step 4 carries a condition, and it matters.** Without it, origination
launders: a fabricated value passed into a computation returns a result that
would then resolve as grounded, and everything derived from it inherits a clean
signature over false provenance. Provenance does not propagate through an
unresolved computation.

**Step 3 is why intermediates are required.** A legitimate intermediate in a
multi-step derivation appears nowhere in the source. Checking against the source
alone would flag every correct chained calculation — and would still pass an
invented value that coincides with an unrelated field.

**Matching is exact, not tolerant.** An operand that came from a source *is* the
source value. A tolerance would silently admit originated values that fall near
one, which is the precise failure being measured.

---

## Invocation evidence

Graded by independence and verifiability, never by richness or format:

| Class | Meaning | Admissible for a control claim |
|---|---|---|
| `EV-0` | No signal available | No |
| `EV-1` | The system's own report about itself, unverified — **including a signed attestation whose signature was not checked** | No |
| `EV-2` | A tool-call record from the serving layer, a third party to the model | Yes, as an observed rate |
| `EV-3` | An attestation verified against a pre-sealed key and an anchored ledger | Yes, per the standard — but see C-15 |

**A signature does not cure self-report: the signer is the party being
measured.** `EV-1` ranks below `EV-2`.

The standard treats a verified attestation as admissible structural
evidence. The publisher has filed C-15 against that definition: signature
validity and ledger membership establish that an attestation existed
unaltered, not that it truthfully describes what executed. The runner
cannot emit EV-3 in any case.

**`EV-3` is defined but not implemented in this version.** The runner cannot
emit it, and a module-level guard raises if any code path attempts to construct
one. An attestation encountered is classified `EV-1` with the reason recorded.

---

## Writing your own fixture

The instrument is domain-agnostic. Nothing in it is financial; the worked
example simply happens to be.

You supply four things:

**A fixture** — synthetic source data in your domain. No real customer data.

**A question set** — questions answerable from the fixture alone. Use chained
derivations: three or more operations over six or fewer fields. Trivial
one-step questions cannot exercise operand provenance.

**A ground-truth module** — derivation *logic*, not values. It reads the fixture
and returns the expected value **and every intermediate**, each with the
operation that produced it and typed inputs identifying a source field, a prior
intermediate, or a declared constant.

> The runner refuses a module that returns literals it did not compute. At seal
> time it perturbs each declared source field and re-executes; if the output
> does not move, the module is returning constants and the run is refused.

**A config** — endpoint, model, sampling parameters (each with a value or an
explicit declared omission and its reason), tolerance, quantisation policy,
permitted transformations, decline markers, and the AP-1 text hash and version
DOI the run claims conformance to.

This is days of work and it needs someone who knows the domain. That is not
friction to be removed — it is what makes the result mean anything.

**Two traps the worked example documents.** Do not encode direction inside a
magnitude. A fixture storing a liability as `-2400.00` uses the sign to carry
meaning, and a system computing interest on the magnitude then passes `2400`,
which appears nowhere in the delivered context and resolves as originated. Two
thousand executions across two systems produced 524 such operands from this
cause alone. Represent the quantity and its direction as separate fields —
`{"balance": 2400.00, "direction": "liability"}`. And every permitted transformation and declared constant
widens what resolves as grounded: declare them before the run, never add one
after seeing a result.

---

## Reading the output

A **profile**, not a grade. Each dimension separately, with n, with the class of
evidence it rests on, and with every unmeasured, unobservable and void cell
declared alongside its reason.

**Zero failures is reported as an estimate, never as certainty.** A perfect
result on a sample is still a sample, so the runner prints the exact one-sided
95% upper bound on the failure rate — `1 − 0.05^(1/n)`, the Clopper–Pearson
bound at zero failures. Forty-nine items with no failures reads *"0/49; upper
bound 5.9%"*, not *"100%"*. The familiar 3/n rule is its large-n approximation
and is shown only for n ≥ 30; below that it overstates, and at n < 3 it returns
a value above 1, which is not a rate.

**There is no pass mark.** AP-1 has no threshold, no certificate, no seal and no
registry, and the runner cannot output one. A supervisor reads the profile and
decides whether it is adequate for their use.

---

## Conformance

> **AP-1 v1.3 is a draft for public comment and is not adopted.** v1.2 remains
> the version in force. This instrument targets the v1.3 draft because it
> incorporates requirements arising from documented defects in the v1.2
> reference evaluation. Conformance will be re-verified against the adopted
> text.

The runner claims conformance to specific clauses of AP-1 v1.3. That claim is
executable:

```bash
python tests/legacy/verify_conformance.py
```

One test per clause. Each names the clause, quotes it verbatim from the sealed
standard text with line numbers, and asserts the behaviour it requires. Clauses
the runner **cannot** enforce — independent key implementation and authorship
disclosure, both process obligations — have tests asserting the runner *declares*
the limitation rather than staying silent.

```bash
python tests/legacy/verify_spec.py
```

The build specification records line counts and a size constraint. This suite
parses those claims and compares them against the files, so the specification
cannot drift from the code without failing.

**This instrument alone cannot produce a conformance claim.** AP-1 v1.3 §4
states that a system may not claim compliance having omitted any dimension. D3
through D6 require human adjudication by design, and §13 imposes process
obligations — independent key implementation, two blind scorers — that no
instrument can supply. What this produces is a profile; a conformance claim
additionally requires those.

**The standard text is sealed.** `reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md` is
hashed into the pre-registration record, and a run declaring a mismatched hash
is refused.

AP-1 v1.3: [10.5281/zenodo.21755443](https://doi.org/10.5281/zenodo.21755443) ·
concept DOI [10.5281/zenodo.21324954](https://doi.org/10.5281/zenodo.21324954) ·
[standard repository](https://github.com/zorrzai/admissibility-protocol)

---

## Layout

The package follows the layers of the build specification (docs/SPEC.md).

```
pyproject.toml               package metadata; `pip install -e .`; the `ap1-run` command
run_all_tests.py             one command, all legacy suites
smoke_test.py                shim: `python smoke_test.py` runs ap1_run.run

src/ap1_run/
  run.py                     drives a live endpoint (was smoke_test.py)
  runner/                    the parts run.py drives
    credentials.py           the API key: environment, or Windows Credential Manager
  foundation/                SPEC Layer 0
    config.py                configuration; refuses defaults that affect a result
    adapter.py               HTTP transport; records the request as sent
    transcript.py            append-only run log
    numeric.py               Decimal arithmetic, token grammar, canonical hashing
  execution/                 SPEC Layer 1
    seal.py                  pre-registration: hash and timestamp before any request
    seal_constants.py        declared-constant checks on the ground-truth module
    version.py               runner version and source hash
    engine.py                execution loop
    context.py               delivered-context construction
    perturbation_guard.py    refuses a condition that varies more than one quantity
    evidence.py              invocation evidence classification
  scoring/                   SPEC Layer 2
    figure_id.py             which figure in the response is the answer
    accuracy.py              D1
    reproducibility.py       D2
    invocation.py            D7.1
    operation_correctness.py D7.2(b)
    transcription.py         D7.3
    release_coverage.py      D7.3 release coverage
    provenance/              D7.2(a)
      trace.py               the five-step resolution ladder
      classify.py            invocation, item and sequential classification
      audit.py               originated-operand listing
  reporting/                 SPEC Layer 3
    adjudication.py          printable sheets for the human-scored dimensions
    report.py                the result artifact

tools/
  verify_run_seal.py         verifies a published run's seal from report.md
  generate_findings.py       regenerates findings/FINDINGS.md from the published runs

tests/
  legacy/                    the original verify_*.py suites, run by run_all_tests.py
  regression/                the regression baseline: canned model responses, golden output
  fixtures/                  mock endpoint and test modules

ap1_inspect/                 the optional Inspect wrapper (its own package)
docs/                        build specification (SPEC.md), KNOWN_ISSUES.md,
                             RELATED_WORK_REVIEW.md, REPRODUCING.md, the publisher's comments
findings/                    FINDINGS.md (generated from FINDINGS.template.md), FINDINGS_ERRATA.md
example/                     a worked fixture, questions, ground truth and config
reference/                   the sealed AP-1 text
```

Instrument modules are kept at or under 300 lines so a reviewer can read
the instrument in an afternoon, with one declared exception recorded in
the build specification. Test suites, the worked example and the smoke
test sit outside that constraint by design and are longer.

Full architecture, verification contracts per module, threat model and
conformance mapping: [`docs/SPEC.md`](docs/SPEC.md).

### Where the files used to be

Until October 2026 every module sat at the repository root. Published runs,
FINDINGS_ERRATA and the paper refer to those paths, at their own commits;
those records are not edited. To follow such a reference today:

| old path | new path |
|---|---|
| `smoke_test.py` | `src/ap1_run/run.py` (the root `smoke_test.py` is now a shim) |
| `config.py`, `adapter.py`, `transcript.py`, `numeric.py` | `src/ap1_run/foundation/` |
| `seal.py`, `seal_constants.py`, `version.py`, `engine.py`, `context.py`, `perturbation_guard.py`, `evidence.py` | `src/ap1_run/execution/` |
| `perturbation.py` | deleted (it was never used; the seal's own `perturbation_check` is the one that runs) |
| `figure_id.py`, `accuracy.py`, `reproducibility.py`, `invocation.py`, `operation_correctness.py`, `transcription.py`, `release_coverage.py` | `src/ap1_run/scoring/` |
| `provenance.py`, `provenance_classify.py`, `provenance_audit.py` | `src/ap1_run/scoring/provenance/`, renamed in step 2 to `trace.py`, `classify.py`, `audit.py` |
| `report.py`, `adjudication.py` | `src/ap1_run/reporting/` |
| `generate_findings.py`, `verify_run_seal.py` | `tools/` |
| `verify*.py`, `test_findings_mutation.py` | `tests/legacy/` |
| `_t16_mock_gt.py` | `tests/fixtures/` |
| `SPEC.md`, `KNOWN_ISSUES.md`, `RELATED_WORK_REVIEW.md`, `REPRODUCING.md` | `docs/` |
| `FINDINGS.md`, `FINDINGS.template.md`, `FINDINGS_ERRATA.md` | `findings/` |

Line numbers inside the moved modules are unchanged, except in `run.py`, the
tools and the test suites. To reproduce a published run at the code it was
sealed against, see [`docs/REPRODUCING.md`](docs/REPRODUCING.md).

---

## Verifying a run's seal

The pre-registration seal (§5.3) binds the **resolved** configuration —
after environment variables have been written into the config dict — not
the config file on disk. The on-disk `example/config.json` and
`example/config_mini.json` contain placeholder values for `model` and
`endpoint_url` that are overwritten at runtime by `AP1_SMOKE_MODEL` and
`AP1_SMOKE_ENDPOINT` (see `src/ap1_run/run.py` L352-370).

To verify a run's seal:

```bash
python tools/verify_run_seal.py output/run_a_mini
python tools/verify_run_seal.py output/run_b_sol
```

This reads the seal record from `report.md` §1 and the resolved
configuration from `report.md` §2, then recomputes and compares all five
component hashes and the composite `seal_hash`. It reports each check
individually and exits non-zero if any check fails.

**Do not** hash `example/config.json` directly — it will not match the
sealed `config_hash` because it contains the placeholder model, not the
runtime model. This is expected behaviour, not a failure.

**Ground truth module.** `example/ground_truth_example.py` has been
modified since both published runs. The sealed `ground_truth_hash` no
longer matches the current file. Erratum E3 in
[FINDINGS_ERRATA.md](findings/FINDINGS_ERRATA.md) records why: constant `4` was
declared in Q07's derivation metadata but never used in the computation.
The correction was made for cause; the sealed state is not restored.
The verifier reports this mismatch with the E3 reference and exits
non-zero.

**Line endings.** `file_hash()` hashes raw bytes. `.gitattributes` forces
LF on all sealed files; the sealed hashes were computed against LF bytes
and reproduce on any platform.

| Hash | Source | Proves |
|------|--------|--------|
| `config_hash` | `report.md` §2 resolved config | Config as executed |
| `fixture_hash` | `example/fixture.json` | Financial data unchanged |
| `questions_hash` | `example/questions.json` | Question set unchanged |
| `ground_truth_hash` | `example/ground_truth_example.py` | Ground-truth module unchanged (see E3) |
| `ap1_text_hash` | `reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md` | AP-1 standard text unchanged |
| `seal_hash` | All of the above | Composite integrity |

---

## Security

The instrument makes no network call except to the endpoint under test. It reads
credentials from the OS credential store and never writes them to disk, a
command line, or a log. Error bodies are masked for credential-shaped
substrings before being stored.

The example calculator uses an AST evaluator with an explicit allow-list of node
types. There is no `eval`, `exec` or `compile` anywhere in the runner.

See [`SECURITY.md`](SECURITY.md) for the threat model and how to report a
vulnerability.

---

## Licence

This runner is licensed under the MIT Licence. See [LICENSE](LICENSE).

The AP-1 standard itself is published separately under Creative Commons
Attribution 4.0 International (DOI 10.5281/zenodo.21324954).

"AP-1" and "The Admissibility Protocol" are trademarks of the publisher.
See [NOTICE](NOTICE).

---

*Comments and defects: open an issue, or mrupp@zorrz.com*
