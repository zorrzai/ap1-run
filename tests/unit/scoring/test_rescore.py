"""Unit tests for the re-scorer (scoring/rescore.py, T3-21).

rescore_transcript verifies the run's seal (format 2) against its inputs
and hands them to the scoring pass, which is replaced here by a recording
fake (it has its own tests, tests/unit/runner/test_scoring_pass.py). The
inputs are copies of the shipped example in a temporary directory, sealed
with the real seal(), as run.py seals them. The re-scorer end to end, on a
real run's transcript, is in tests/unit/test_run.py and
tests/functional/test_step4_g4_transcript.py.
"""

import json
import os
import shutil
from decimal import Decimal

import pytest

from ap1_run.execution.ap1_texts import resolve_ap1_text
from ap1_run.execution.seal import SealError, seal
from ap1_run.execution.sealed_inputs import (
    compute_expected_values, read_inputs,
)
from ap1_run.foundation.config import load_config
from ap1_run.scoring import rescore
from ap1_run.scoring.rescore import (
    PRE_REGISTRATION, RUNTIME_FIELDS, rescore_transcript,
    write_pre_registration,
)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
INPUTS = ('config.json', 'fixture.json', 'questions.json',
          'ground_truth_example.py')
RUNTIME = {'runner_version_tag': 'v9', 'runner_version_commit': 'abc',
           'runner_modified': True}


class Run:
    """A sealed run of the example: its inputs, its pre-registration
    record and an (empty) transcript; score_run replaced by a fake."""

    def __init__(self, tmp_path, monkeypatch):
        self.fx = tmp_path / 'fx'
        self.fx.mkdir()
        for name in INPUTS:
            shutil.copy(os.path.join(REPO, 'example', name), self.fx / name)
        self.run_dir = tmp_path / 'run'
        self.run_dir.mkdir()
        self.transcript = self.run_dir / 'smoke_run.jsonl'
        self.transcript.write_text('')
        self.out = tmp_path / 'rescored'
        config = load_config(self.fx / 'config.json')
        config.update(RUNTIME)
        self.config = config
        inputs = read_inputs(str(self.fx))
        self.expected_values = compute_expected_values(
            inputs.ground_truth, inputs.fixture, inputs.questions)
        self.seal_record = seal(
            config=config, fixture_path=inputs.paths['fixture'],
            questions_path=inputs.paths['questions'],
            ground_truth_path=inputs.paths['ground_truth'],
            ap1_text_path=resolve_ap1_text(config, None, REPO),
            runner_source_hash='feed' * 16,
            expected_values=self.expected_values, loaded=inputs.data)
        write_pre_registration(str(self.run_dir),
                               seal_record=self.seal_record, config=config)
        self.scored = []
        monkeypatch.setattr(rescore, 'score_run', self.score_run)

    def score_run(self, transcript_path, **kwargs):
        self.scored.append((transcript_path, kwargs))
        return {'smoke': 'summary'}

    def rescore(self, **kwargs):
        args = dict(config_path=self.fx / 'config.json',
                    fixture_dir=str(self.fx), output_dir=str(self.out))
        args.update(kwargs)
        return rescore_transcript(str(self.transcript), **args)

    def edit_record(self, change):
        path = self.run_dir / PRE_REGISTRATION
        with open(path, encoding='utf-8') as f:
            record = json.load(f)
        change(record)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(record, f)


@pytest.fixture
def r(tmp_path, monkeypatch):
    return Run(tmp_path, monkeypatch)


def test_constants():
    assert PRE_REGISTRATION == 'pre_registration.json'
    assert RUNTIME_FIELDS == ('runner_version_tag', 'runner_version_commit',
                              'runner_modified')


# -- write_pre_registration ------------------------------------------------

def test_write_pre_registration_seal_and_resolved_config(tmp_path):
    path = write_pre_registration(
        str(tmp_path), seal_record={'seal_hash': 'h', 'b': [1]},
        config={'z': Decimal('0.01'), 'a': 'é'})
    assert path == os.path.join(str(tmp_path), 'pre_registration.json')
    text = open(path, encoding='utf-8').read()
    assert text == json.dumps(
        {'resolved_config': {'a': 'é', 'z': '0.01'},
         'seal_record': {'b': [1], 'seal_hash': 'h'}},
        indent=2, ensure_ascii=False) + '\n'


# -- rescore_transcript ----------------------------------------------------

@pytest.mark.finding('T3-21')
def test_rescore_scores_with_the_sealed_run_s_inputs(r):
    assert r.rescore() == {'smoke': 'summary'}
    ((path, kw),) = r.scored
    assert path == str(r.transcript)
    assert kw['seal_record'] == r.seal_record
    # the config file, with the values the runner resolved at run time
    assert kw['config'] == r.config
    with open(r.fx / 'fixture.json', encoding='utf-8') as f:
        assert kw['fixture'] == json.load(f)
    with open(r.fx / 'questions.json', encoding='utf-8') as f:
        assert kw['questions'] == json.load(f)
    assert kw['output_dir'] == str(r.out)
    assert r.out.is_dir()


@pytest.mark.finding('T3-21')
@pytest.mark.req('R1.1')
def test_rescore_scores_against_the_sealed_expected_values(r):
    # T3-48: the scoring pass gets the sealed expected values (copies),
    # not the module to call again.
    r.rescore()
    compute = r.scored[0][1]['ground_truth_compute']
    for item_id, value in r.expected_values.items():
        got = compute(item_id, {'ignored': True})
        assert got == value
        assert got is not value
    got['final'] = Decimal('0')
    assert compute(item_id, {}) == r.expected_values[item_id]


def test_rescore_relative_paths(r, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    rescore_transcript('run/smoke_run.jsonl', config_path='fx/config.json',
                       fixture_dir='fx', output_dir='rescored')
    assert r.scored[0][0] == str(r.transcript)
    assert r.scored[0][1]['output_dir'] == str(r.out)


def test_rescore_given_pre_registration_path(r, tmp_path):
    elsewhere = tmp_path / 'records'
    elsewhere.mkdir()
    os.rename(r.run_dir / PRE_REGISTRATION, elsewhere / PRE_REGISTRATION)
    r.rescore(pre_registration_path=str(elsewhere / PRE_REGISTRATION))
    assert r.scored[0][1]['seal_record'] == r.seal_record


def test_rescore_into_an_existing_directory(r):
    r.out.mkdir()
    (r.out / 'report.md').write_text('old')
    assert r.rescore() == {'smoke': 'summary'}


def test_rescore_without_pre_registration_record_refused(r):
    os.remove(r.run_dir / PRE_REGISTRATION)
    with pytest.raises(FileNotFoundError):
        r.rescore()
    assert r.scored == []


def test_rescore_into_the_transcript_s_own_directory_refused(r):
    with pytest.raises(ValueError, match=(
            '^the re-scored outputs must go to another directory than the '
            "transcript's")):
        r.rescore(output_dir=str(r.run_dir))
    assert r.scored == []


@pytest.mark.finding('T3-21')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('name, edit, field', [
    ('config.json', lambda c: c.replace('"decline_markers": [',
                                        '"decline_markers": ["new", '),
     'config'),
    ('fixture.json', lambda c: c.replace('15200.00', '15200.01'),
     'fixture'),
    ('questions.json', lambda c: c + '\n\n', 'questions'),
    ('ground_truth_example.py', lambda c: c + '\n# edited\n',
     'ground_truth'),
])
def test_rescore_input_not_matching_the_seal_refused(r, name, edit, field):
    # SPEC R1.1: modifying any sealed input makes the scorer refuse,
    # naming the mismatch (verify_seal).
    path = r.fx / name
    text = path.read_text('utf-8')
    assert edit(text) != text
    path.write_text(edit(text), 'utf-8')
    with pytest.raises(SealError, match=(
            f'seal verification failed:\n  (.*\n  )*{field}: sealed=')):
        r.rescore()
    assert r.scored == []


@pytest.mark.finding('T3-48')
@pytest.mark.req('R1.1')
def test_rescore_ground_truth_giving_other_values_refused(r):
    # A ground-truth module that now computes other values: the expected
    # values computed again no longer hash to the sealed ones (and the
    # file's hash differs too).
    path = r.fx / 'ground_truth_example.py'
    text = path.read_text('utf-8')
    edited = text.replace(
        '    return DERIVATIONS[item_id](delivered_context)',
        '    result = DERIVATIONS[item_id](delivered_context)\n'
        '    return dict(result, final=result["final"] + 1)')
    assert edited != text
    path.write_text(edited, 'utf-8')
    with pytest.raises(SealError, match='expected_values: sealed='):
        r.rescore()


def test_rescore_rewritten_record_refused(r):
    # A field of the record changed after sealing: its seal_hash no
    # longer matches (T3-47).
    r.edit_record(lambda rec: rec['seal_record'].update(
        python_version='0.0'))
    with pytest.raises(SealError, match='seal_hash: sealed='):
        r.rescore()


def test_rescore_runtime_field_missing_from_the_record_not_overlaid(r):
    # A field the record does not hold is taken from the config file
    # (and so must match the seal as it is).
    r.edit_record(lambda rec: rec['resolved_config'].pop('runner_modified'))
    with pytest.raises(SealError, match='config: sealed='):
        r.rescore()


def test_rescore_runner_source_hash_not_compared(r):
    # A corrected scorer must be able to re-score: the runner code that
    # scores need not be the code that ran.
    assert r.seal_record['runner_source_hash'] == 'feed' * 16
    assert r.rescore() == {'smoke': 'summary'}
