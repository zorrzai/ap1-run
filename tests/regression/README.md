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
  repeat and round, or it replays a published transcript. It refuses a
  request with any method but POST (405), to any path but
  `/v1/chat/completions` (404) or without
  `Authorization: Bearer <the driver's test key>` (401), without advancing
  its script.
- `driver.py`: runs the runner's `main()` from the repository itself. The
  runner gets the scenario's config with `--config` (a temporary copy, merged
  when the scenario edits it, with `endpoint_url` and `model` pointed at the
  mock, since the runner reads both from the config alone) and a temporary
  `--output-dir`, so it never writes under the repository;
  `run_regression.py` checks that `output/` is
  unchanged after every real-tree scenario. It imports `smoke_test`, or
  `ap1_run.run` when the tree has no `smoke_test.py`.
- `run_regression.py`: runs each scenario, normalises the output and compares
  it exactly with `golden/<scenario>/`.
- `scenarios/*.json`: one scenario per file. A scenario can `extend` another
  and override its config, environment or scripted responses. A command
  scenario runs one entry point instead of the runner. A scenario can also
  give the runner command-line `args`, make `copy_paths` inside the copy
  (`{"from": "to"}`, after the config edits), and name the `output_dir` the
  outputs are read from; the default `output/` must then stay empty
  (`default_output.txt`). `crlf_paths` lists files given CRLF line endings
  in the copy, made at setup so that git's line-ending handling cannot
  change them. `copy_paths`, `output_dir`, `copy_output` (published runs
  copied into the copy's `output/`) and `crlf_paths` need a scratch copy.
- **Scratch copy.** A scenario that sets `"scratch_copy"` (its value says
  why) runs in a scratch copy of the repository, without `.git` and
  `output/`, instead of the real tree. Four do: `cli_paths` (it checks that
  the default `output/` stays empty, which needs a disposable one),
  `tool_generate_findings` (the tool writes `findings/FINDINGS.md` at a
  fixed path) and `clean_no_options` (with no options the runner reads
  `example/config.json` and writes to the default `output/`, so the config
  edit and the outputs need a disposable tree) and `crlf_sealed_inputs` (it
  turns tracked files to CRLF).
- **No git.** Every run gets `GIT_DIR` pointing nowhere. The runner
  cross-checks `VERSION` against git `HEAD` and records `runner_modified`;
  the golden output pins a run without git (as in a copy without `.git`),
  so it does not depend on the branch the checkout is on.

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
- the run's root path (the scratch copy, or the repository and the
  temporary run directory whose `output/` the runner writes to) and the
  mock's address and port;
- ISO and epoch timestamps;
- this run's `seal_hash`, `config_hash` and `runner_source_hash`, read from
  the seal the run actually made. The config hash covers the mock's port. The
  source hash covers the code, so it changes whenever files move.

The fixture, questions, ground-truth and AP-1 text hashes are kept, and so
they are pinned.

**Hard checks** run on each runner scenario before normalisation
(`hard_checks.py`). A failure stops the harness with a message; it is never a
golden difference, and `--update` cannot write over it.
- `hash_oracle.py` recomputes the seal the run made, from the inputs the seal
  function was given (`driver.py` captures them before the call): the file
  hashes, `config_hash` from the resolved config, the version fields from
  the tree's `VERSION` file, and `seal_hash` from the expected record. The
  record must have exactly the expected fields and values, and a timestamp
  that falls within the run. Each path the seal was given must be the file
  of its role (`seal_paths` in a scenario that moves them). The source hash
  is frozen before the runner starts (`before_run`), over the tree the
  runner runs from (the repository itself for a real-tree scenario, the
  copy for a scratch-copy one): the one passed to every seal call, refused
  or not, must equal it, and so must the tree's after the run. The printed
  `Runner source hash:` prefix (once per run that calls the seal), the
  console's seal and AP-1 text hashes (once per record), every transcript
  record's `seal_hash` (which must be present), the summary's `seal_hash`
  and report §1 must agree with it, and report §2's resolved config must
  hash to `config_hash`. Other 64-hex text in a report is not read as a
  seal reference. The oracle is standard library only and fails if any
  runner module has been imported into the harness process.
- The mock refused no request (`check_transport`): a request with any
  method but POST, to the wrong path or without the driver's bearer
  credential fails the run.
- A replay must re-score its published run exactly, apart from what the
  fixes change on purpose: the replayed `smoke_summary.json` equals
  `output/run_*/smoke_summary.json` in every key, value, type and list
  order, except the top-level `seal_hash` and the differences
  `replay_expected.json` lists (`check_replay`). That file lists, per
  published run, the fields new in the replay and each execution's moves as
  [published value, replayed value]; a listed move that does not happen
  fails as well, and a listed move is compared type-aware. A new
  execution field must be in every replayed execution, and its value in
  each one must equal the one `hard_checks.py` computes from that
  execution's published fields, with the listed moves applied, and the
  scoring config (`NEW_FIELD_EXPECTATIONS`; for the AP-1 v1.3 §6.8
  `answer_outcome` and its reason); nothing is read from the replay being
  checked. The leaves listed under `numeric_paths` (`field[].key`) are
  compared as numbers, and those under `numeric_text_paths` with their
  standalone numbers so compared and the rest of the text verbatim, for a
  fix that changes only how a value is written: the one respelling
  accepted is trailing zeros in plain ASCII decimals (`15.20` for `15.2`;
  not padding, an exponent, other digits or a sign of zero). Identifiers
  such as `acct01` or `acct-01` are never read as numbers. Both summaries
  are read with JSON numbers as exact Decimals. A difference is investigated before it is listed, never
  added by explanation alone, and the commit that lists it says which fix
  makes it.
- Each runner scenario states `"seal_attempts"`, how many times the run calls
  the seal function, and `"seal_records"`, how many records it makes: 1 and
  1 for a run that seals, 1 and 0 for a refused seal, 0 and 0 for a run that
  stops before sealing. A refused seal must be one the contract refuses,
  with the exception the contract names. A run that seals must write
  `report.md`, `smoke_run.jsonl` and `smoke_summary.json`, unless the
  scenario states otherwise in `"sealed_outputs"` (`t3_38_unknown_tool`, which stops early).
- **Command scenarios** (`"command"`) run an entry point directly and get
  none of these checks. None of them seals today; a command scenario that
  seals needs the driver's capture first.

`python tests/regression/selftest.py` tests these checks directly, with known
answers. One of them recomputes the published September `runner_source_hash`
(`da0739eb…`, docs/REPRODUCING.md) with the oracle's rule from the tag
`e7-quantise-fix`, so the clone needs its tags (`git fetch --tags`; CI checks
out full history). That tree is nearly flat (no `tests/` or `src/`), so this
pins how the files are read, framed and sorted; `check_source_files.py` pins
which files are in scope.

**The files the source hash covers** are listed in `source_hash_files.txt`:
the files the hash oracle's rule (`hash_oracle.source_hash_files()`) finds in
the checkout, tests included, less any that git does not track (named on
stderr, not listed). `check_source_files.py` compares the list with the tree
and runs as its own CI step, so a move, a new module or a
deletion shows as a reviewed diff of the list. It is checked at each PR head;
a commit that changes the set updates the list (`--update`).

## Running it

```
python tests/regression/run_regression.py              # compare everything
python tests/regression/run_regression.py clean t3_1_unrecognised_shape
python tests/regression/run_regression.py --runs 3     # determinism check
python tests/regression/run_regression.py --update     # rewrite golden output
python tests/regression/run_regression.py --keep DIR replay_run_e_mini
                                                       # full output, digested files too
python tests/regression/check_imports.py               # every module imports
python tests/regression/check_source_files.py          # source-hash file list
python tests/regression/selftest.py                    # the harness's own checks
python tests/regression/check_own_src.py               # entry points use their own src/
python tests/regression/verify_hashes.py               # pinned canonical-hash digest (hashes.yml)
python tests/regression/coverage_report.py OUTDIR      # pytest suite + scenarios
```

It needs `requests`; the coverage report also needs pytest and `coverage`
(`pip install -e '.[dev]'`), and fails if its pytest or scenario run fails. CI pins
`requests` and `urllib3` with `constraints.txt`, because the
`transport_errors` golden output contains urllib3's own error text. The
golden files were made on macOS with Python 3.11; CI runs this harness on
Ubuntu with Python 3.11 and 3.12 (`regression.yml`). A full comparison of
all scenarios takes about 1.5 to 2 minutes on a laptop and about 2.5 minutes
in CI; the two replays take most of it, about 40 seconds each.

The harness runs separately from pytest (`python -m pytest` does not collect
it). The original verify_*.py suites it was built beside (`tests/legacy/`,
run by `run_all_tests.py`) are retired; `tests/RETIREMENT.md` records where
each of their checks went.

## Scenarios

| scenario | what it pins |
|---|---|
| `clean` | all ten questions correct with grounded calls, both conditions: the main path, every scorer, the report |
| `wrong_answers` | wrong final figure, wrong operation, transposed operand, no tool call |
| `multi_round` | chained intermediates over several rounds, several calls per round, intermediate assistant text (V12-3: not kept) |
| `d2_variation` | answers that vary across repeats (D2) |
| `non_answers` | empty and null content (UNMEASURED, T3-10), declined, unrecognised decline, refusal reciting balances, two candidates, no figure |
| `transport_errors` | 429, 500 and 401 in round 0 and mid-loop, a dropped connection with retries, a non-JSON body |
| `t3_1_unrecognised_shape` | **T3-1** (fixed): EV-0 (Anthropic- and Responses-shaped bodies, mid-loop failure) is UNOBSERVABLE, out of the D7.1 n and listed per evidence class; an all-EV-0 arm has no D7.1 figure |
| `t3_2_leading_whitespace` | **T3-2**: a leading space or tab before the expression; since the fix it is stripped and read, so the chained launder is ORIGINATED, ORIGINATED, as the no-space contrast |
| `t3_16_malformed_calls` | **T3-16**: malformed or wrongly keyed calls are INVOKED; since the fix they are OPERANDS-/OPERATION-UNOBSERVABLE in D7.2(a)/(b), not dropped; a call with a name the calculator does not know (`2400 * rate / 12`), which errors and, since the unknown-name fix, is OPERANDS-UNOBSERVABLE, not grounded |
| `t3_5_constant_magnitude` | **T3-5**: `-12` and `-1` grounded by `constant_magnitude`; a sign-inverted source field for contrast |
| `t3_38_unknown_tool` | **T3-38**: an unoffered tool trips the FATAL consistency check; no report |
| `t3_39_crash` | **T3-39**: a non-string calculator expression; since the fix its operands are unreadable and the run completes |
| `non_ascii_config` | a decline marker with U+2019 in the resolved config: the config hash's UTF-8 rule through the real seal |
| `crlf_sealed_inputs` | `clean` with the fixture, questions, ground-truth module and AP-1 text in CRLF bytes (the config declares the CRLF text's hash): a runner that read any sealed input, or its source files, in text mode fails the hash oracle; `ground_truth_hash` is the September seals' (`033ce73d…`) |
| `decimal_trailing_zero` | `answer_tolerance` `"0.010"` in the resolved config: the config hash keeps a Decimal's exact string (a runner that normalised it to `0.01` fails the hash oracle) |
| `decimal_two_trailing_zeros` | the same with `"0.0100"` (exponent -4), so a normaliser limited to some exponents fails one of the two |
| `decimal_integral` | `answer_tolerance` `"10"`: the same for an integral Decimal (a runner that wrote it as `1E+1` or through float as `10.0` fails the hash oracle) |
| `seal_refused` | AP-1 text hash mismatch: SealError before any request |
| `config_no_tools` | config without tools: exit 1 |
| `mini_config` | the shipped `example/config_mini.json`, the mini run's config: temperature 1 sent, `reasoning_effort` omitted as platform-unsupported |
| `replay_run_e_mini` | the published gpt-4.1-mini run, 1,000 executions, replayed through today's runner with `example/config_mini.json` |
| `replay_run_f_sol` | the published gpt-5.6-sol run, 1,000 executions, replayed with `example/config_sol.json` |
| `tool_verify_run_seal` | `verify_run_seal.py` on the four published runs |
| `tool_verify_run_seal_usage` | `verify_run_seal.py` with no arguments |
| `tool_generate_findings` | `generate_findings.py`; its output equals the committed `findings/FINDINGS.md` |
| `smoke_no_api_key` | `python -m ap1_run.run` with no key: instructions, exit 1 |
| `smoke_test_shim_no_api_key` | the root `smoke_test.py` shim with no key: the same golden output as `smoke_no_api_key` |
| `clean_no_options` | `clean` with a bare `ap1-run`, no `--config` or `--output-dir`: the runner's default config and output paths, end to end; the same golden output as `clean` |
| `cli_paths` | `clean` with `--config`, `--fixture-dir`, `--output-dir` and `--ap1-text` pointing at copies: every output equals `clean`'s, only the printed paths differ |
| `cli_help` | `ap1-run --help`: the options and their defaults |

**About the replays:** the recorded final responses are served as they were.
The intermediate rounds survive only as assistant messages (V12-3), so each
one is wrapped in a standard envelope. The envelope names the model the
execution's recorded final response names (the published runs did not keep
the intermediate rounds' own model field), and a replay is configured with
the model the published run's requests name. So a replay's served and
configured models are the run's, not the mock's `mock-model`, which only
scripted turns name. A recorded loop that ended mid-way (EV-0) is replayed
as a failure of the next request.

The replayed `smoke_summary.json` files equal the published ones except the
top-level `seal_hash`, the moves listed in `replay_expected.json`, and its two
allowances (the new per-execution fields, checked against values computed from
the published fields, and the respelled numeric leaves), and the harness checks
this on every run (above). The replayed `report.md` files agree
with the published `output/run_e_mini` and `output/run_f_sol` reports in every
scored figure except those step 5 corrected: the D7.1 figures of §5 (and
console 3h) (T3-1, T3-11, V12-5), where n is now the 10 computable questions,
not the 500 executions, and the one EV-0 execution per run is out of n and
listed per evidence class; and the D7.3 counts the listed moves feed (T3-26).
Otherwise only run metadata differs: model name, endpoint, hashes,
timestamps, runner commit and `runner_modified`.

## Coverage (at `77514b4`, Python 3.11, with inspect-ai installed)

| | lines and branches |
|---|---|
| `smoke_test.py`, legacy suites alone | 7 % |
| `smoke_test.py`, legacy + regression | 90 % |
| all production code, legacy + regression | 80 % |

Every production module is executed, except that the Inspect wrapper
(`ap1_inspect/compare, metrics, scorer, solver, task`) is only imported:
`check_imports.py` covers it at import level. `perturbation.py` was dead code
(8 %) and was deleted in step 2.
