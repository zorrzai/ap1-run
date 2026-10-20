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

Before scoring, the inputs are checked against the seal: the config
(with the values the runner resolved at run time, taken from the
pre-registration record) and the fixture, questions and ground-truth
files must hash to the sealed values, and every transcript record must
carry the seal hash. A mismatch is refused with SealError, naming it.

From the command line: ap1-run --rescore <transcript> (README, "Scoring
a transcript again").
"""

import importlib.util
import json
import os
import sys

from ap1_run.execution.seal import SealError, seal
from ap1_run.foundation.config import load_config
from ap1_run.runner.scoring_pass import score_run

PRE_REGISTRATION = 'pre_registration.json'

# The configuration values the runner resolves at run time, after loading
# the config file and before sealing it (run.py main()).
RUNTIME_FIELDS = ('endpoint_url', 'model', 'sampling', 'runner_version_tag',
                  'runner_version_commit', 'runner_modified')

# The sealed hashes the re-scorer recomputes from its inputs.
CHECKED_HASHES = ('config_hash', 'fixture_hash', 'questions_hash',
                  'ground_truth_hash')


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


def _load_ground_truth(path):
    """The ground-truth module at path, loaded under its own name without
    touching sys.modules or writing bytecode."""
    spec = importlib.util.spec_from_file_location('ground_truth_example',
                                                  path)
    module = importlib.util.module_from_spec(spec)
    saved = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = saved
    return module


def _check_against_seal(seal_record, *, config, fixture_path,
                        questions_path, ground_truth_path):
    """Refuse (SealError) inputs that do not hash to the sealed values."""
    resealed = seal(config=config, fixture_path=fixture_path,
                    questions_path=questions_path,
                    ground_truth_path=ground_truth_path)
    mismatched = [name for name in CHECKED_HASHES
                  if resealed[name] != seal_record.get(name)]
    if mismatched:
        raise SealError(
            'the inputs given do not match the run\'s seal: '
            + ', '.join(f'{name} sealed {seal_record.get(name)!r}, '
                        f'recomputed {resealed[name]!r}'
                        for name in mismatched))


def rescore_transcript(transcript_path, *, config_path, fixture_dir,
                       output_dir, pre_registration_path=None):
    """Score the transcript again; return the summary (the content of
    smoke_summary.json after its '_disclaimer' line).

    config_path is the run's config file and fixture_dir holds its
    fixture.json, questions.json and ground_truth_example.py.
    pre_registration_path defaults to pre_registration.json beside the
    transcript. The output files go to output_dir, which must not be the
    transcript's own directory (the run's outputs there are not replaced).
    """
    transcript_path = os.path.abspath(transcript_path)
    output_dir = os.path.abspath(output_dir)
    if output_dir == os.path.dirname(transcript_path):
        raise ValueError(
            'the re-scored outputs must go to another directory than the '
            f'transcript\'s ({output_dir})')
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

    fixture_path = os.path.join(fixture_dir, 'fixture.json')
    questions_path = os.path.join(fixture_dir, 'questions.json')
    ground_truth_path = os.path.join(fixture_dir, 'ground_truth_example.py')
    _check_against_seal(seal_record, config=config,
                        fixture_path=fixture_path,
                        questions_path=questions_path,
                        ground_truth_path=ground_truth_path)

    with open(fixture_path, encoding='utf-8') as f:
        fixture = json.load(f)
    with open(questions_path, encoding='utf-8') as f:
        questions = json.load(f)
    gt_module = _load_ground_truth(ground_truth_path)

    os.makedirs(output_dir, exist_ok=True)
    return score_run(transcript_path, config=config, seal_record=seal_record,
                     fixture=fixture, questions=questions,
                     gt_module=gt_module, output_dir=output_dir)
