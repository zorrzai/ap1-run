"""Re-scoring: the scoring pass alone, on a run's transcript (SPEC §2).

A run's execution pass writes, before its first request,
pre_registration.json beside its transcript: the seal record (R1.1) and
the resolved configuration it sealed. rescore_transcript scores the
transcript again from those and the sealed inputs, with no endpoint and
no API key, and writes report.md, adjudication_sheets.md, DISCLAIMER.txt
and smoke_summary.json to another directory. It opens the transcript
read-only and never writes to it. A finished run's transcript gives the
run's own smoke_summary.json back; a partial one (an interrupted run)
reports its unreached executions NOT-RUN.

The inputs are read once. Before scoring, the run's seal (format 2) is
verified against the bytes read (execution/seal.py verify_seal, loaded),
not the files read again: the record's own seal_hash, the
config (with the values the runner resolved at run time, taken from the
pre-registration record), the fixture, questions, ground-truth and
calculator files, the AP-1 text hash the config declares, and the
expected values, which the ground-truth module computes again and which
must hash to the sealed ones. The runner's source hash is not compared:
a corrected scorer must be able to re-score. Every transcript record
must carry the seal hash. A mismatch is refused with SealError, naming
it. The executions are then scored from the same inputs, against the
sealed expected values, as in the run; the scoring pass names the
transcript it scored by the SHA-256 of its bytes.

From the command line: ap1-run --rescore <transcript> (README, "Scoring
a transcript again").
"""

import json
import os
from datetime import datetime, timezone

from ap1_run.execution.context import lookup_collisions
from ap1_run.execution.seal import verify_seal
from ap1_run.execution.sealed_inputs import (
    compute_expected_values, read_inputs, sealed_compute,
)
from ap1_run.execution.version import (
    compute_runner_source_hash, resolve_runner_version,
)
from ap1_run.foundation.config import load_config
from ap1_run.runner.outputs import OUTPUT_FILES
from ap1_run.runner.scoring_pass import score_run

PRE_REGISTRATION = 'pre_registration.json'

# The re-score's own record: when, of which run, by which scorer
RESCORE_RECORD = 'rescore.json'

# The repository root: this file is src/ap1_run/scoring/rescore.py.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

# The configuration values the runner resolves at run time, after loading
# the config file and before sealing it (run.py main()).
RUNTIME_FIELDS = ('runner_version_tag', 'runner_version_commit',
                  'runner_modified')


def write_pre_registration(output_dir, *, seal_record, config):
    """Write the run's pre-registration record (the seal record and the
    resolved configuration it sealed) to output_dir; return its path."""
    path = os.path.join(output_dir, PRE_REGISTRATION)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({'seal_record': seal_record, 'resolved_config': config},
                  f, indent=2, sort_keys=True, default=str,
                  ensure_ascii=False)
        f.write('\n')
    return path


# What a run or a re-score writes, which a re-score never replaces
WRITTEN_FILES = ('smoke_run.jsonl', PRE_REGISTRATION, RESCORE_RECORD) \
    + OUTPUT_FILES


def scorer_identity(base_dir):
    """The runner doing the scoring now: its source hash and version, the
    fields the seal records for the run's runner."""
    version = resolve_runner_version(base_dir)
    return {
        'runner_source_hash': compute_runner_source_hash(base_dir),
        'runner_version_tag': version['version_tag'],
        'runner_version_commit': version['version_commit'],
        'runner_modified': version.get('version_modified', False),
    }


def _same_directory(a, b):
    if os.path.realpath(a) == os.path.realpath(b):
        return True
    try:
        return os.path.samefile(a, b)
    except OSError:
        return False


def _check_output_dir(output_dir, run_dir):
    if _same_directory(output_dir, run_dir):
        raise ValueError(
            'the re-scored outputs must go to another directory than the '
            f'transcript\'s ({output_dir})')
    found = sorted(name for name in WRITTEN_FILES
                   if os.path.lexists(os.path.join(output_dir, name)))
    if found:
        raise ValueError(
            'the re-scored outputs must go to a directory that holds no '
            f'run or scoring output: {output_dir} holds {", ".join(found)}')


def rescore_transcript(transcript_path, *, config_path, fixture_dir,
                       output_dir, pre_registration_path=None,
                       base_dir=None):
    """Score the transcript again; return the summary (the content of
    smoke_summary.json after its '_disclaimer' line).

    config_path is the run's config file and fixture_dir holds its
    fixture.json, questions.json, ground_truth_example.py and
    calculator_tool.py.
    pre_registration_path defaults to pre_registration.json beside the
    transcript. The output files go to output_dir, which must not be the
    transcript's own directory, however it is named (a symlink, another
    case on a file system that ignores case), nor hold any run or scoring
    output, its own run's or another's, not even a symlink by that name:
    a correction is made by addition (AP-1 §13.12), and nothing already
    written is replaced. Refused with ValueError.

    The re-score is recorded (AP-1 §13.10, §13.11: a corrected scorer
    may re-score, so its figures must be traceable to it): when, the run's
    runner as sealed, and the scorer, the runner in base_dir (default:
    this repository). The report says so, the console prints both
    runners, and rescore.json in output_dir holds the record.
    """
    transcript_path = os.path.abspath(transcript_path)
    output_dir = os.path.abspath(output_dir)
    _check_output_dir(output_dir, os.path.dirname(transcript_path))
    if pre_registration_path is None:
        pre_registration_path = os.path.join(
            os.path.dirname(transcript_path), PRE_REGISTRATION)
    with open(pre_registration_path, encoding='utf-8') as f:
        pre_registration = json.load(f)
    seal_record = pre_registration['seal_record']
    resolved = pre_registration['resolved_config']

    config = load_config(config_path)
    for name in RUNTIME_FIELDS:
        if name in resolved:
            config[name] = resolved[name]

    # The inputs, read once (T3-72), and the expected values the
    # ground-truth module gives for them; all verified against the seal.
    inputs = read_inputs(fixture_dir)
    expected_values = compute_expected_values(
        inputs.ground_truth, inputs.fixture, inputs.questions)
    verify_seal(seal_record, config=config,
                fixture_path=inputs.paths['fixture'],
                questions_path=inputs.paths['questions'],
                ground_truth_path=inputs.paths['ground_truth'],
                calculator_path=inputs.paths['calculator'],
                expected_values=expected_values, loaded=inputs.data,
                lookup_collisions=lookup_collisions(
                    sealed_compute(expected_values), inputs.fixture,
                    inputs.questions))

    rescore = {
        'rescored_at': datetime.now(timezone.utc).isoformat(),
        'run': {
            'seal_hash': seal_record['seal_hash'],
            'runner_source_hash': seal_record.get('runner_source_hash'),
            'runner_version_tag': seal_record.get('runner_version_tag'),
            'runner_version_commit': seal_record.get('runner_version_commit'),
            'runner_modified': resolved.get('runner_modified'),
        },
        'scorer': scorer_identity(base_dir or BASE_DIR),
    }
    print(f"Run: runner source hash {rescore['run']['runner_source_hash']} "
          f"(sealed), version {rescore['run']['runner_version_tag']} "
          f"({rescore['run']['runner_version_commit']})")
    print(f"Scorer: runner source hash "
          f"{rescore['scorer']['runner_source_hash']}, version "
          f"{rescore['scorer']['runner_version_tag']} "
          f"({rescore['scorer']['runner_version_commit']})")

    os.makedirs(output_dir, exist_ok=True)
    summary = score_run(
        transcript_path, config=config, seal_record=seal_record,
        fixture=inputs.fixture, questions=inputs.questions,
        ground_truth_compute=sealed_compute(expected_values),
        output_dir=output_dir, rescore=rescore)
    with open(os.path.join(output_dir, RESCORE_RECORD), 'w',
              encoding='utf-8') as f:
        json.dump(dict(rescore, transcript=transcript_path,
                       scored_transcript=summary.get('scored_transcript')),
                  f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write('\n')
    return summary
