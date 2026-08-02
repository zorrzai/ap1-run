# AP-1 Runner

A standalone evaluation runner implementing the AP-1 Assessment Standard.

## Status

**Phase E complete** -- 198 assertions across 135 test functions in 7 suites.
All dimensions through D7 implemented. Report generator and adjudication
sheet generator operational.

## Running the Tests

```bash
python run_all_tests.py
```

This invokes every verification suite in its native form and reports
per-suite results:

```
AP-1 runner -- full test suite

  suite                           functions   checks  result
  ------------------------------------------------------------
  verify.py (Phase A)                    13       76  PASS
  verify_phase_b.py                      25       25  PASS
  verify_phase_c.py                      28       28  PASS
  verify_integration.py                   7        7  PASS
  verify_phase_d.py                      23       23  PASS
  verify_d72b.py                         10       10  PASS
  verify_phase_e.py                      29       29  PASS
  ------------------------------------------------------------
  TOTAL                                 135      198  PASS
```

`verify.py` groups multiple checks per test function, so "functions"
(what `pytest` reports) and "checks" (what the native runner reports)
differ for that suite. Both numbers are correct; this runner reports both.

Exit code is non-zero if any suite fails.

## Evidence Classes (v1.0)

| Class | Implemented | Description |
|-------|-------------|-------------|
| EV-0 UNOBSERVABLE | Yes | No tool-call signal available |
| EV-1 SELF-REPORTED | Yes | System reports about itself |
| EV-2 PLATFORM-STRUCTURAL | Yes | Tool-call record from serving layer |
| EV-3 EXTERNALLY-VERIFIABLE | **No** | Requires signature verification against a pre-sealed public key and ledger membership under an external trust anchor. **Neither is implemented in v1.0.** No run may claim EV-3. Any attestation encountered is classified EV-1 with reason "attestation verification not implemented in runner v1.0". |

## Dependencies

- Python 3.11+
- `requests` (the only external dependency)
- Standard library only otherwise

## Quick Start

```bash
# Run all tests (one command)
python run_all_tests.py

# Verify ground-truth examples
python example/ground_truth_example.py

# Run individual suites
python verify.py              # Phase A gate (76 checks)
python verify_phase_b.py      # Phase B seal/perturbation (25)
python verify_phase_c.py      # Phase C figure/accuracy (28)
python verify_integration.py  # Integration (7)
python verify_phase_d.py      # Phase D provenance (23)
python verify_d72b.py         # D7.2b operation correctness (10)
python verify_phase_e.py      # Phase E adjudication/report (29)
```

## Layout

```
ap1-runner/
|-- SPEC.md              # Authoritative build specification (v0.3)
|-- run_all_tests.py     # Unified test entry point
|-- numeric.py           # R0.4  Decimal grammar, parsing, hashing
|-- config.py            # R0.1  Config loader, validator
|-- transcript.py        # R0.3  Append-only JSONL store
|-- seal.py              # R1.1  Pre-registration and sealing
|-- adapter.py           # R0.2  OpenAI chat-completions adapter
|-- engine.py            # R1.2  Execution engine
|-- evidence.py          # Evidence class classification
|-- invocation.py        # Tool invocation classification
|-- figure_id.py         # Released figure identification
|-- accuracy.py          # D1 accuracy scoring
|-- provenance.py        # D7.2a operand provenance
|-- operation_correctness.py  # D7.2b operation correctness
|-- transcription.py     # D7.3 transcription fidelity
|-- reproducibility.py   # D2 reproducibility classification
|-- adjudication.py      # R3.2 adjudication sheet generator
|-- report.py            # R3.3 report generator
|-- example/
|   |-- config.json      # Example configuration
|   |-- fixture.json     # 5 personal-finance accounts
|   |-- questions.json   # 10 items (3 three-step chains)
|   |-- ground_truth_example.py   # Worked derivations
|   +-- calculator_tool.py        # Calculator sandbox
+-- reference/           # AP-1 text (supplied separately)
```

## Licence

Apache-2.0. This licence is provisional pending patent counsel review.
