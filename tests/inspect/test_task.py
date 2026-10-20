"""ap1_inspect/task.py: the seal and the dataset of the two Inspect tasks
(from legacy verify_inspect.py test_seal_refusal_on_wrong_hash).

T3-44 / F7: the task seals docs/SPEC.md as "the AP-1 text", so it refuses
with every shipped config; with SPEC.md's hash it seals the wrong document;
without SPEC.md it seals no text; the record is discarded either way.
"""

import hashlib
from pathlib import Path

import pytest

pytest.importorskip('inspect_ai')

from ap1_inspect import task  # noqa: E402
from ap1_run.execution.seal import SealError  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SPEC_HASH = hashlib.sha256((ROOT / 'docs' / 'SPEC.md').read_bytes()).hexdigest()
AP1_HASH = hashlib.sha256(
    (ROOT / 'reference' / 'AP-1_v1.3_DRAFT_FOR_COMMENT.md').read_bytes()
).hexdigest()


@pytest.fixture
def loaded():
    return task._load_fixture()


def test_wrong_ap1_text_hash_is_refused(loaded):
    config, fixture, questions, fp, qp, gp = loaded
    with pytest.raises(SealError, match='^AP-1 text hash mismatch: '):
        task._create_seal(dict(config, ap1_text_hash='deadbeef' * 8),
                          fp, qp, gp)


@pytest.mark.finding('T3-44', 'F7')
def test_shipped_config_with_the_real_ap1_hash_is_refused(loaded):
    # The example config declares the hash of the AP-1 v1.3 text, which
    # is what a run should seal; the task hashes SPEC.md instead and
    # refuses. (The legacy wrong-hash test passed for this reason too.)
    # Correct: hash the AP-1 text in reference/.
    config, fixture, questions, fp, qp, gp = loaded
    assert config['ap1_text_hash'] == AP1_HASH
    with pytest.raises(SealError) as exc:
        task._create_seal(config, fp, qp, gp)
    assert str(exc.value) == (
        f"AP-1 text hash mismatch: config declares '{AP1_HASH}', "
        f"file hashes to '{SPEC_HASH}'")


@pytest.mark.finding('T3-44', 'F7')
def test_seal_with_spec_hash_records_spec_as_the_ap1_text(loaded):
    config, fixture, questions, fp, qp, gp = loaded
    record = task._create_seal(dict(config, ap1_text_hash=SPEC_HASH),
                               fp, qp, gp)
    assert record['ap1_text_hash'] == SPEC_HASH != AP1_HASH


@pytest.mark.finding('F7', 'T3-68')
def test_seal_without_spec_md_refused(loaded, tmp_path, monkeypatch):
    # With no docs/SPEC.md the task seals with ap1_text_path=None, which
    # seal() refuses since T3-68: the AP-1 text is a required sealed input.
    # (F7, the task hashing SPEC.md, is not fixed here.)
    config, fixture, questions, fp, qp, gp = loaded
    monkeypatch.setattr(task, '_RUNNER_DIR', str(tmp_path))
    with pytest.raises(SealError, match='^AP-1 text: no file given'):
        task._create_seal(dict(config, ap1_text_hash='not-a-hash'),
                          fp, qp, gp)


@pytest.mark.finding('T3-44')
def test_both_tasks_refuse_with_the_shipped_config():
    for make in (task.ap1_base, task.ap1_instruction_removed):
        with pytest.raises(SealError, match='^AP-1 text hash mismatch'):
            make()


def _dataset(loaded, condition):
    config, fixture, questions, *_ = loaded
    return task._build_dataset(questions, fixture, config,
                               condition=condition)


def test_dataset_has_one_sample_per_derivable_item(loaded):
    samples = list(_dataset(loaded, 'base'))
    assert [s.id for s in samples] == [f'Q{i:02d}' for i in range(1, 11)]
    first = samples[0]
    assert first.input.startswith('Here is the financial information:\n\n'
                                  'Savings Account:\n  Balance: 15200.00\n')
    assert first.input.endswith('\n\nQuestion: ' + loaded[2][0]['text'])
    assert first.target == '15.200'


@pytest.mark.finding('T3-44')
def test_samples_carry_no_seal_hash(loaded):
    # The seal record is discarded; nothing ties a sample to a seal.
    sample = list(_dataset(loaded, 'base'))[0]
    assert sorted(sample.metadata) == ['ap1_condition', 'ap1_config',
                                       'ap1_context', 'ap1_ground_truth',
                                       'ap1_item_id']


@pytest.mark.finding('S3-G7-4')
def test_instruction_removed_samples_are_identical_to_base(loaded):
    # The two tasks differ only in the condition label: same inputs, same
    # solver, and neither sends a system prompt, so the D7.1b contrast
    # measures nothing. Correct: base sends system_prompt_base and the
    # removed condition system_prompt_instruction_removed.
    base = list(_dataset(loaded, 'base'))
    removed = list(_dataset(loaded, 'instruction_removed'))
    assert [s.input for s in base] == [s.input for s in removed]
    assert {s.metadata['ap1_condition'] for s in removed} == \
        {'instruction_removed'}
    assert all('system_prompt' not in s.input for s in base)
