"""Unit tests for the per-version AP-1 text table (V12-4)."""

import hashlib
import os

import pytest

from ap1_run.execution.ap1_texts import (
    AP1_TEXTS, ap1_text_entry, check_ap1_text_version, resolve_ap1_text,
)
from ap1_run.execution.seal import SealError

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

V13 = '48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56'
V12 = '14659fc1c2a3357c22081a9109841475861c34f2b315ee7eb546e80fecbb58a5'


def test_table_versions_paths_and_hashes():
    assert AP1_TEXTS == {
        'v1.3': {'path': os.path.join('reference',
                                      'AP-1_v1.3_DRAFT_FOR_COMMENT.md'),
                 'sha256': V13},
        'v1.2': {'path': os.path.join('reference',
                                      'AP-1_Admissibility_Protocol_v1.2.md'),
                 'sha256': V12}}


@pytest.mark.parametrize('version', sorted(AP1_TEXTS))
def test_table_hash_is_the_hash_of_the_file_in_the_repository(version):
    entry = AP1_TEXTS[version]
    with open(os.path.join(REPO, entry['path']), 'rb') as f:
        assert hashlib.sha256(f.read()).hexdigest() == entry['sha256']


@pytest.mark.parametrize('version, key', [
    ('v1.3', 'v1.3'), ('v1.3-draft-for-comment-20260730', 'v1.3'),
    ('v1.2', 'v1.2'), ('v1.2-', 'v1.2'), ('v1.2-final', 'v1.2'),
    ('v1.3x', None), ('v1.30', None), ('v1', None), ('1.3', None),
    ('', None), ('V1.3', None), (None, None), ('v1.4', None)])
def test_ap1_text_entry(version, key):
    assert ap1_text_entry(version) == (AP1_TEXTS[key] if key else None)


def test_resolve_explicit_path_wins(tmp_path):
    # Whatever the version, an explicit --ap1-text is the text sealed (the
    # seal checks it against the declared hash; check_ap1_text_version
    # against the table).
    for version in ('v1.2', 'v9'):
        assert resolve_ap1_text({'ap1_version': version}, '/x/t.md',
                                '/repo') == '/x/t.md'


@pytest.mark.parametrize('version, rel', [
    ('v1.2', 'AP-1_Admissibility_Protocol_v1.2.md'),
    ('v1.3-draft-for-comment-20260730', 'AP-1_v1.3_DRAFT_FOR_COMMENT.md')])
def test_resolve_table_path_under_base_dir(version, rel):
    assert resolve_ap1_text({'ap1_version': version}, None, '/repo') == \
        os.path.join('/repo', 'reference', rel)
    assert resolve_ap1_text({'ap1_version': version}, '', '/repo') == \
        os.path.join('/repo', 'reference', rel)


@pytest.mark.parametrize('config, shown', [
    ({'ap1_version': 'v2.0'}, "'v2.0'"), ({}, "''")])
def test_resolve_unknown_version_without_path_refused(config, shown):
    with pytest.raises(SealError) as exc:
        resolve_ap1_text(config, None, '/repo')
    assert str(exc.value) == (
        f'AP-1 text: no text is known for ap1_version {shown} '
        f'(known: v1.3, v1.2); give it with --ap1-text')


@pytest.mark.parametrize('version, sealed', [
    ('v1.2', V12), ('v1.3-draft', V13), ('v9.9', 'a' * 64), ('', 'b')])
def test_check_version_matching_or_unknown_passes(version, sealed):
    assert check_ap1_text_version({'ap1_version': version},
                                  {'ap1_text_hash': sealed}) is None


def test_check_version_label_over_another_text_refused():
    with pytest.raises(SealError) as exc:
        check_ap1_text_version({'ap1_version': 'v1.2'},
                               {'ap1_text_hash': V13})
    assert str(exc.value) == (
        f"AP-1 text: the sealed text hashes to {V13!r}, which is not the "
        f"AP-1 v1.2 text ({V12!r})")


def test_check_version_record_without_text_hash_refused():
    with pytest.raises(SealError, match="hashes to None"):
        check_ap1_text_version({'ap1_version': 'v1.3'}, {})
