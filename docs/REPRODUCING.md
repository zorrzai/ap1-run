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
- **`4cfe283`** is the commit that shipped the September run artifacts. The
  paper cites it. Its Python files are the same code as `e7-quantise-fix`
  apart from line endings, so they hash differently. Use the tag to
  reproduce the seal.
- **`ap1-runner-v1.0.0`** (29 August 2026) is the first licensed release. It
  precedes the September runs and is not the code of any published run.
- **`pre-reorg`** marks the last commit in the flat layout, `77514b4`. It is a
  local tag until the maintainers publish it.

A clean checkout of `e7-quantise-fix` reproduces the September seals'
`runner_source_hash` byte for byte (checked again on 13 October 2026).

## Running the code of a published run

At those commits there is no package, so there is no install step beyond
`requests`:

```bash
git clone https://github.com/zorrzai/ap1-run && cd ap1-run
git checkout e7-quantise-fix
python -m venv .venv && . .venv/bin/activate   # keep the venv out of the
pip install requests                           # hash: see the note below
python run_all_tests.py
```

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

**Keep virtual environments outside the clone, or name them so that they are
excluded.** `compute_runner_source_hash` hashes every `.py` file under the
repository root except `output/`, `review_output*` and `__pycache__/`. A
`.venv/` inside the clone therefore changes `runner_source_hash`.

## Checking a seal

At the run's commit:

```bash
python verify_run_seal.py output/run_e_mini
python verify_run_seal.py output/run_f_sol
```

On the current layout, the same script is `python tools/verify_run_seal.py`.

**Expected mismatch.** `ground_truth_hash` fails on a clean clone, and only
because of line endings. The repository checks `.py` files out with LF; the
seals hashed the file with CRLF. With CRLF restored, the September seals pass
in full. FINDINGS_ERRATA N2 gives the details and the recipe. For the August
seals, restore the module from `203fef4` with CRLF; see FINDINGS_ERRATA,
"Note by addition - 3 October 2026: restoring the original ground-truth module".

## What differs on the current layout

- **`runner_source_hash` is different.** The hash covers the path and content
  of every `.py` file, and the files moved. That is expected. It is not a
  change in behaviour.
- **Behaviour is unchanged by the move.** The regression baseline
  (`tests/regression/`) pins the runner's behaviour end to end and gave
  identical output before and after it. It includes both September runs
  replayed through the runner from their recorded responses, and those replays
  reproduce the published `report.md` figures exactly:

  ```bash
  pip install -e .
  python tests/regression/run_regression.py replay_run_e_mini replay_run_f_sol
  ```

- **Commands:** `python smoke_test.py` still works; it is now a shim for
  `ap1_run.run`, also available as the `ap1-run` command. The original test suites
  were retired in October 2026 (`tests/RETIREMENT.md` maps each check to its
  replacement); `python run_all_tests.py` now runs pytest. At the commits named
  above, `python run_all_tests.py` runs the original suites.
