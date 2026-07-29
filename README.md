# AP-1 Runner

A standalone evaluation runner implementing the AP-1 Assessment Standard.

## Status

**Phase A** — Foundation modules (R0.1–R0.4, R1.1) implemented and
verified. Phases B–E pending.

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
# Verify ground-truth examples
python example/ground_truth_example.py

# Run Phase A gate tests
python verify.py

# Run cross-platform hash verification
python verify_hashes.py
```

## Layout

```
ap1-runner/
├── SPEC.md              # Authoritative build specification (v0.3)
├── numeric.py           # R0.4  Decimal grammar, parsing, hashing
├── config.py            # R0.1  Config loader, validator
├── transcript.py        # R0.3  Append-only JSONL store
├── seal.py              # R1.1  Pre-registration and sealing
├── adapter.py           # R0.2  OpenAI chat-completions adapter
├── verify.py            # Phase A gate tests
├── verify_hashes.py     # Cross-platform hash reproducibility
├── example/
│   ├── config.json      # Example configuration
│   ├── fixture.json     # 5 personal-finance accounts
│   ├── questions.json   # 10 items (3 three-step chains)
│   ├── ground_truth_example.py   # Worked derivations
│   └── calculator_tool.py        # Calculator sandbox
└── reference/           # AP-1 text (supplied separately)
```

## Licence

Apache-2.0. This licence is provisional pending patent counsel review.
