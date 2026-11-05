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

Before scoring, the run's seal (format 2) is verified against the inputs
given (execution/seal.py verify_seal): the record's own seal_hash, the
config (with the values the runner resolved at run time, taken from the
pre-registration record), the fixture, questions, ground-truth and
calculator files, the AP-1 text hash the config declares, and the
expected values, which the ground-truth module computes again and which
must hash to the sealed ones. The runner's source hash is not compared:
a corrected scorer must be able to re-score. Every transcript record
must carry the seal hash. A mismatch is refused with SealError, naming
it. The executions are then scored against the sealed expected values,
as in the run.

From the command line: ap1-run --rescore <transcript> (README, "Scoring
a transcript again").
"""

import json
import os

from ap1_run.execution.seal import verify_seal
from ap1_run.execution.sealed_inputs import (
    compute_expected_values, read_inputs, sealed_compute,
)
from ap1_run.foundation.config import load_config
from ap1_run.runner.outputs import OUTPUT_FILES
from ap1_run.runner.scoring_pass import score_run

PRE_REGISTRATION = 'pre_registration.json'

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
WRITTEN_FILES = ('smoke_run.jsonl', PRE_REGISTRATION) + OUTPUT_FILES


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
                       output_dir, pre_registration_path=None):
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
                expected_values=expected_values)

    os.makedirs(output_dir, exist_ok=True)
    return score_run(transcript_path, config=config, seal_record=seal_record,
                     fixture=inputs.fixture, questions=inputs.questions,
                     ground_truth_compute=sealed_compute(expected_values),
                     output_dir=output_dir)
