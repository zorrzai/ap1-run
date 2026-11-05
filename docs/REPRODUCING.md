# Reproducing the published runs

The repository was reorganised in October 2026: the modules moved from the
root into the `src/ap1_run/` package (see the path map in the README). The
published runs were made with the earlier, flat layout. This page says which
code each run was made with, and how to get it back.

A live run cannot be repeated exactly, because the model's answers vary. What
can be reproduced is the code, its seal, and the scoring of the recorded
responses.

## Which code made which run

| run | executed | code | `runner_source_hash` in the seal |
|---|---|---|---|
| `output/run_a_mini`, `output/run_b_sol` | August 2026 | **not identifiable**, as the paper states. The ground-truth module the seals bind is `example/ground_truth_example.py` at `203fef4` (see FINDINGS_ERRATA, "Note by addition - 3 October 2026: restoring the original ground-truth module") | none: the August seals have no `runner_source_hash` field |
| `output/run_e_mini`, `output/run_f_sol` | 8 September 2026 | tag **`e7-quantise-fix`** (pre-split commit `93d4014`; the seals record `runner_version_commit` `dd4c3e8` from the VERSION file) | `da0739eb396e65468d33adb7953aa828fdde9bee6ec1c78e56c83c345defd795` |

Other references you may meet:
- **`4cfe283`** is the commit that shipped the September run artifacts. Its
  Python files are the same code as `e7-quantise-fix` apart from line
  endings, so they hash differently. Use the tag to reproduce the seal.
- **`ap1-runner-v1.0.0`** (29 August 2026) is the first licensed release. It
  precedes the September runs and is not the code of any published run.
- **`paper-2026-10`** marks `b4d41e2`, the repository state the AP-1 paper
  cites (October 2026). It is in the flat layout.
- **`pre-reorg`** marks the last commit in the flat layout, `c8df9ca`: `main`
  just before the reorganisation. It differs from `paper-2026-10` only in the
  README.

A clean checkout of `e7-quantise-fix` reproduces the September seals'
`runner_source_hash` byte for byte (checked again on 13 October and
2 November 2026, with the recipe below).

## Reproducing the source hash

This recipe rebuilds the code of the September runs and recomputes their
`runner_source_hash`. At `e7-quantise-fix` there is no package, so there is
no install step beyond `requests`. The virtual environment goes **outside**
the clone (see the note below):

```bash
git clone https://github.com/zorrzai/ap1-run && cd ap1-run
git checkout e7-quantise-fix
python -m venv ../ap1-venv && . ../ap1-venv/bin/activate
pip install requests
python -c "import os, version; print(version.compute_runner_source_hash(os.getcwd()))"
python run_all_tests.py
```

On Windows, activate with `..\ap1-venv\Scripts\activate`. The hash printed
is `da0739eb396e65468d33adb7953aa828fdde9bee6ec1c78e56c83c345defd795`, the
value in both September seals (`report.md` §1 of `run_e_mini` and `run_f_sol`),
and `run_all_tests.py` reports 226 test functions and 406 checks, `PASS`.
Running the tests writes only `__pycache__/` directories, which the hash
excludes, so the hash is the same before and after.

**Keep virtual environments outside the clone, or name them so that they are
excluded.** `compute_runner_source_hash` hashes every `.py` file under the
repository root except `output/`, `review_output*` and `__pycache__/`. A
`.venv/` inside the clone therefore changes `runner_source_hash`. The same
goes for the `build/` directory that a non-editable `pip install .` leaves in
the clone on the current layout (see the README: only `pip install -e .` is
supported).

### Running the code of a published run

From the same checkout and environment:

- **Python:** 3.11 or later. CI runs 3.11 and 3.12.
- **Configuration:** both September runs used `example/config.json` with
  `repeat_count` 50 and the model set by `AP1_SMOKE_MODEL`. Each run's
  `report.md` §2 shows the resolved configuration as sent.
  - `run_e_mini`: `AP1_SMOKE_MODEL=gpt-4.1-mini`, `AP1_SMOKE_TEMPERATURE=1`,
    `AP1_SMOKE_REASONING_EFFORT=omit`.
  - `run_f_sol`: `AP1_SMOKE_MODEL=gpt-5.6-sol`, with no sampling overrides.
- **Endpoint:** `AP1_SMOKE_ENDPOINT`, by default the OpenAI chat-completions
  URL. The key goes in `AP1_SMOKE_API_KEY` (see SECURITY.md).
- Then run `python smoke_test.py`.

## Verifying the published artifacts

This recipe checks the September run directories against their seals. The
directories are not in the `e7-quantise-fix` tree: they arrived in
`4cfe283`. Use either a checkout of `4cfe283` or the current tree; both have
them. Any environment with `requests` will do, for example the one above.

At `4cfe283`, from a clone (the flat layout, script at the root):

```bash
git checkout 4cfe283
python verify_run_seal.py output/run_e_mini
python verify_run_seal.py output/run_f_sol
```

On the current tree, the script is in `tools/` and needs no install:

```bash
python tools/verify_run_seal.py output/run_e_mini
python tools/verify_run_seal.py output/run_f_sol
```

**Expected mismatch.** Each run reports `10 passed, 1 failed`: only
`ground_truth_hash` fails, and only because of line endings. The repository
checks `.py` files out with LF; the seals hashed the ground-truth module with
CRLF (FINDINGS_ERRATA N2). The `NOTE` the script prints after this mismatch
names the August corrections; for the September seals the cause is line
endings only. To check the module too, restore CRLF, verify again, and put
the module back. The first line turns every line ending into CRLF, so
running it twice does no harm.

At `4cfe283`:

```bash
python -c "p='example/ground_truth_example.py'; b=open(p,'rb').read(); open(p,'wb').write(b.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n'))"
python verify_run_seal.py output/run_e_mini
python verify_run_seal.py output/run_f_sol
git checkout -- example/ground_truth_example.py
```

On the current tree:

```bash
python -c "p='example/ground_truth_example.py'; b=open(p,'rb').read(); open(p,'wb').write(b.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n'))"
python tools/verify_run_seal.py output/run_e_mini
python tools/verify_run_seal.py output/run_f_sol
git checkout -- example/ground_truth_example.py
```

With CRLF the module hashes to `033ce73d…`, the sealed value, and each run
reports `11 passed, 0 failed` and `RESULT: PASS (11 checks)`. Both ways give
the same results.

For the August seals (`run_a_mini`, `run_b_sol`), restore the module from
`203fef4` with CRLF; see FINDINGS_ERRATA, "Note by addition - 3 October 2026:
restoring the original ground-truth module".

## What differs on the current layout

- **`runner_source_hash` is different.** The hash covers the path and content
  of every `.py` file, and the files moved. That is expected. It is not a
  change in behaviour.
- **Behaviour is unchanged by the move.** The regression baseline
  (`tests/regression/`) pins the runner's behaviour end to end and gave
  identical output before and after it. It includes both September runs
  replayed through the runner from their recorded responses, and at the move
  those replays reproduced the published `report.md` figures exactly. The
  fixes since then (the findings in `docs/REVIEW_FINDINGS.md`) move some of
  them on purpose: `tests/regression/replay_expected.json` lists every
  execution whose scored outcome moves, and the harness fails a replay that
  differs in anything else:

  ```bash
  pip install -e .
  python tests/regression/run_regression.py replay_run_e_mini replay_run_f_sol
  ```

- **Commands:** `python smoke_test.py` still works; it is now a shim for
  `ap1_run.run`, also available as the `ap1-run` command. The original test
  suites moved to `tests/legacy/` and were later retired, with
  `run_all_tests.py`: `python -m pytest` runs their replacements, and
  `tests/RETIREMENT.md` maps each old check to its new test. At the
  September runs' commit, `python run_all_tests.py` still works as shown
  above.
