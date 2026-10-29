# Regression baseline

The safety net for restructuring the repository. It pins what the instrument
does today, right or wrong, so that a change which alters behaviour is
detected. Nothing here judges whether the behaviour is correct: known defects
(T3-1, T3-2, T3-5, T3-16, T3-38, T3-39, ...) appear in the golden output as
they are today. A fix changes the golden files in the same commit, and the
commit says why.

## How it works

The model is the only source of randomness in a live run. Here it is replaced
by a mock endpoint that serves canned responses, which is the equivalent of
fixing an RNG seed. The runner itself runs unmodified, end to end, through the
real adapter and HTTP transport:

- `../fixtures/mock_endpoint.py`: a local HTTP server that speaks the
  chat-completions API. It serves scripted turns per question, condition,
  repeat and round, or it replays a published transcript.
- `driver.py`: runs `smoke_test.main()` in a scratch copy of the repository,
  so the runner writes to the copy's `output/`, never to the published runs.
- `run_regression.py`: runs each scenario, normalises the output and compares
  it exactly with `golden/<scenario>/`.
- `scenarios/*.json`: one scenario per file. A scenario can `extend` another
  and override its config, environment or scripted responses. A command
  scenario runs one entry point instead of the runner.

What is compared for each scenario:
- the console output, stderr and exit code (or the exception);
- `report.md`, `adjudication_sheets.md`, `smoke_summary.json`, `smoke_run.jsonl`
  and `DISCLAIMER.txt`, plus the list of files written;
- every request the mock received;
- `outcomes.jsonl`, a per-execution table of what the runner decided about each
  execution.

For the two replays, the large files are kept as a digest only, and
`outcomes.jsonl` carries the detail. Storing them in full would add about
25 MB. When a digest differs, `--keep DIR` writes the full normalised files;
run it at both commits and diff the two directories.

**Normalisation** happens in the comparison, never in the runner. It covers:
- line endings;
- the scratch path and the mock's address and port;
- ISO and epoch timestamps;
- this run's `seal_hash`, `config_hash` and `runner_source_hash`, read from
  the seal the run actually made. The config hash covers the mock's port. The
  source hash covers the code, so it changes whenever files move.

The fixture, questions, ground-truth and AP-1 text hashes are kept, and so
they are pinned.

## Running it

```
python tests/regression/run_regression.py              # compare everything
python tests/regression/run_regression.py clean t3_1_unrecognised_shape
python tests/regression/run_regression.py --runs 3     # determinism check
python tests/regression/run_regression.py --update     # rewrite golden output
python tests/regression/run_regression.py --keep DIR replay_run_e_mini
                                                       # full output, digested files too
python tests/regression/check_imports.py               # every module imports
python tests/regression/coverage_report.py OUTDIR      # legacy suites + scenarios
```

It needs `requests`, and `coverage` for the coverage report. The golden files
were made on macOS with Python 3.11; CI runs this harness on Ubuntu with
Python 3.11 and 3.12 (`regression.yml`). A full comparison of all scenarios
takes about 30 seconds.

The harness is deliberately **not** registered in `run_all_tests.py`, so the
legacy suite counts (226 test functions, 406 checks) stay the same across the
restructure.

## Scenarios

| scenario | what it pins |
|---|---|
| `clean` | all ten questions correct with grounded calls, both conditions: the main path, every scorer, the report |
| `wrong_answers` | wrong final figure, wrong operation, transposed operand, no tool call |
| `multi_round` | chained intermediates over several rounds, several calls per round, intermediate assistant text (V12-3: not kept) |
| `d2_variation` | answers that vary across repeats (D2) |
| `non_answers` | empty, declined, unrecognised decline, refusal reciting balances, two candidates, null content, no figure |
| `transport_errors` | 429, 500 and 401 in round 0 and mid-loop, a dropped connection with retries, a non-JSON body |
| `t3_1_unrecognised_shape` | **T3-1**: EV-0 (Anthropic- and Responses-shaped bodies, mid-loop failure) counted as invoked; an all-EV-0 arm prints 0/20 failures |
| `t3_2_leading_whitespace` | **T3-2**: a leading space or tab makes the call OPERANDS-GROUNDED; a chained launder, with the no-space contrast |
| `t3_16_malformed_calls` | **T3-16**: malformed or wrongly keyed calls are INVOKED but vanish from D7.2(a)/(b); a calculator error |
| `t3_5_constant_magnitude` | **T3-5**: `-12` and `-1` grounded by `constant_magnitude`; a sign-inverted source field for contrast |
| `t3_38_unknown_tool` | **T3-38**: an unoffered tool trips the FATAL consistency check; no report |
| `t3_39_crash` | **T3-39**: a non-string expression crashes the run |
| `seal_refused` | AP-1 text hash mismatch: SealError before any request |
| `config_no_tools` | config without tools: exit 1 |
| `mini_config` | the shipped `example/config_mini.json` is refused at load today (`model-unsupported` is not a permitted omission reason) |
| `replay_run_e_mini` | the published gpt-4.1-mini run, 1,000 executions, replayed through today's runner |
| `replay_run_f_sol` | the published gpt-5.6-sol run, 1,000 executions, replayed |
| `tool_verify_run_seal` | `verify_run_seal.py` on the four published runs |
| `tool_verify_run_seal_usage` | `verify_run_seal.py` with no arguments |
| `tool_generate_findings` | `generate_findings.py`; its output equals the committed `FINDINGS.md` |
| `smoke_no_api_key` | `smoke_test.py` with no key: instructions, exit 1 |

**About the replays:** the recorded final responses are served as they were.
The intermediate rounds survive only as assistant messages (V12-3), so each
one is wrapped in a standard envelope. A recorded loop that ended mid-way
(EV-0) is replayed as a failure of the next request.

The replayed `report.md` files agree with the published `output/run_e_mini`
and `output/run_f_sol` reports in every scored figure. Only run metadata
differs: model name, endpoint, hashes, timestamps and runner commit.

## Coverage (at `77514b4`, Python 3.11, with inspect-ai installed)

| | lines and branches |
|---|---|
| `smoke_test.py`, legacy suites alone | 7 % |
| `smoke_test.py`, legacy + regression | 90 % |
| all production code, legacy + regression | 80 % |

Every production module is executed, except that the Inspect wrapper
(`ap1_inspect/compare, metrics, scorer, solver, task`) is only imported:
`check_imports.py` covers it at import level. `perturbation.py` is dead code
(8 %).
