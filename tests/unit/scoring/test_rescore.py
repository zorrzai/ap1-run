"""Unit tests for the re-scorer (scoring/rescore.py, T3-21).

rescore_transcript checks its inputs against the run's seal and hands
them to the scoring pass, which is replaced here by a recording fake (it
has its own tests, tests/unit/runner/test_scoring_pass.py). The inputs
are copies of the shipped example in a temporary directory, sealed with
the real seal(). The re-scorer end to end, on a real run's transcript, is
in tests/unit/test_run.py and tests/functional/test_step4_g4_transcript.py.
"""

import json
import os
import shutil
import sys
from decimal import Decimal

import pytest

from ap1_run.execution.seal import SealError, seal
from ap1_run.foundation.config import load_config
from ap1_run.scoring import rescore
from ap1_run.scoring.rescore import (
    CHECKED_HASHES, PRE_REGISTRATION, RUNTIME_FIELDS, rescore_transcript,
    write_pre_registration,
)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
INPUTS = ('config.json', 'fixture.json', 'questions.json',
          'ground_truth_example.py')
RUNTIME = {'endpoint_url': 'http://mock/v1', 'model': 'mock-model',
           'runner_version_tag': 'v9', 'runner_version_commit': 'abc',
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
        config['sampling'] = dict(config['sampling'], temperature='1')
        self.config = config
        self.seal_record = seal(
            config=config, fixture_path=self.fx / 'fixture.json',
            questions_path=self.fx / 'questions.json',
            ground_truth_path=self.fx / 'ground_truth_example.py',
            runner_source_hash='feed' * 16)
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


@pytest.fixture
def r(tmp_path, monkeypatch):
    return Run(tmp_path, monkeypatch)


def test_constants():
    assert PRE_REGISTRATION == 'pre_registration.json'
    assert RUNTIME_FIELDS == ('endpoint_url', 'model', 'sampling',
                              'runner_version_tag', 'runner_version_commit',
                              'runner_modified')
    assert CHECKED_HASHES == ('config_hash', 'fixture_hash', 'questions_hash',
                              'ground_truth_hash')


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
    for name in RUNTIME:
        assert kw['config'][name] == RUNTIME[name]
    assert kw['config']['sampling']['temperature'] == '1'
    assert kw['config']['answer_tolerance'] == r.config['answer_tolerance']
    with open(r.fx / 'fixture.json', encoding='utf-8') as f:
        assert kw['fixture'] == json.load(f)
    with open(r.fx / 'questions.json', encoding='utf-8') as f:
        assert kw['questions'] == json.load(f)
    assert kw['gt_module'].compute('Q01', {'savings': {
        'balance': '15200.00', 'annual_rate': '1.2'}})['final'] == \
        Decimal('15.20')
    assert kw['output_dir'] == str(r.out)
    assert r.out.is_dir()


def test_rescore_ground_truth_loaded_from_the_fixture_dir_only(r,
                                                               monkeypatch):
    decoy = type(sys)('ground_truth_example')
    monkeypatch.setitem(sys.modules, 'ground_truth_example', decoy)
    r.rescore()
    gt_module = r.scored[0][1]['gt_module']
    assert gt_module is not decoy
    assert gt_module.__file__ == str(r.fx / 'ground_truth_example.py')
    assert gt_module.__name__ == 'ground_truth_example'
    assert sys.modules['ground_truth_example'] is decoy
    assert not (r.fx / '__pycache__').exists()


def test_rescore_dont_write_bytecode_restored(r, monkeypatch):
    monkeypatch.setattr(sys, 'dont_write_bytecode', False)
    r.rescore()
    assert sys.dont_write_bytecode is False


def test_rescore_into_an_existing_directory(r):
    r.out.mkdir()
    (r.out / 'report.md').write_text('old')
    assert r.rescore() == {'smoke': 'summary'}


def test_rescore_every_mismatch_named(r):
    for name in ('fixture.json', 'questions.json'):
        path = r.fx / name
        path.write_text(path.read_text('utf-8') + '\n', 'utf-8')
    with pytest.raises(SealError) as e:
        r.rescore()
    fixture, questions = str(e.value).split("seal: ", 1)[1].split(', q')
    assert fixture.startswith("fixture_hash sealed '")
    assert questions.startswith("uestions_hash sealed '")


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
    ('config.json', lambda c: c.replace('"repeat_count": "50"',
                                        '"repeat_count": "49"'),
     'config_hash'),
    ('fixture.json', lambda c: c.replace('15200.00', '15200.01'),
     'fixture_hash'),
    ('questions.json', lambda c: c + '\n', 'questions_hash'),
    ('ground_truth_example.py', lambda c: c + '\n# edited\n',
     'ground_truth_hash'),
])
def test_rescore_input_not_matching_the_seal_refused(r, name, edit, field):
    # SPEC R1.1: modifying any sealed input makes the scorer refuse,
    # naming the mismatch.
    path = r.fx / name
    text = path.read_text('utf-8')
    assert edit(text) != text
    path.write_text(edit(text), 'utf-8')
    with pytest.raises(SealError, match=(
            "^the inputs given do not match the run's seal: "
            f"{field} sealed '{r.seal_record[field]}', recomputed '")) as e:
        r.rescore()
    assert str(e.value).count('sealed') == 1
    assert r.scored == []


def test_rescore_runtime_field_missing_from_the_record_not_overlaid(r):
    # A field the record does not hold is taken from the config file
    # (and so must match the seal as it is).
    with open(r.run_dir / PRE_REGISTRATION, encoding='utf-8') as f:
        record = json.load(f)
    del record['resolved_config']['runner_modified']
    with open(r.run_dir / PRE_REGISTRATION, 'w', encoding='utf-8') as f:
        json.dump(record, f)
    with pytest.raises(SealError, match='config_hash'):
        r.rescore()
