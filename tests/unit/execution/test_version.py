"""Unit tests for the runner version (VERSION file, git cross-check) and
the runner source hash. Every tree is a small fake under tmp_path; the
real repository is never hashed."""

import hashlib
import shutil
import subprocess
import warnings

import pytest

from ap1_run.execution import version
from ap1_run.execution.version import (
    compute_runner_source_hash, resolve_runner_version,
)

NOT_A_REPO = subprocess.CalledProcessError(128, ['git'])


class FakeGit:
    """Stands in for subprocess.check_output. `head` and `status` are the
    outputs of `git rev-parse HEAD` and `git status`, or an exception to
    raise."""

    def __init__(self, head=NOT_A_REPO, status=''):
        self.head = head
        self.status = status
        self.calls = []

    def __call__(self, args, **kwargs):
        self.calls.append((args, kwargs))
        out = self.head if args[1] == 'rev-parse' else self.status
        if isinstance(out, BaseException):
            raise out
        return out


@pytest.fixture
def git(monkeypatch):
    def install(**kwargs):
        fake = FakeGit(**kwargs)
        monkeypatch.setattr(version.subprocess, 'check_output', fake)
        return fake
    return install


def write_version(tmp_path, text):
    (tmp_path / 'VERSION').write_text(text, encoding='utf-8')


def resolve_quietly(base_dir):
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        return resolve_runner_version(str(base_dir))


# -- resolve_runner_version: the VERSION file -----------------------------

def test_resolve_version_no_file_no_git_is_unknown(tmp_path, git):
    git()
    assert resolve_quietly(tmp_path) == {
        'version_tag': 'unknown', 'version_commit': 'unknown',
        'version_modified': False}


def test_resolve_version_reads_tag_and_commit(tmp_path, git):
    git()
    write_version(tmp_path, 'v1.3.1 e0d9ec9\n')
    assert resolve_quietly(tmp_path) == {
        'version_tag': 'v1.3.1', 'version_commit': 'e0d9ec9',
        'version_modified': False}


def test_resolve_version_skips_comments_and_blank_lines(tmp_path, git):
    git()
    write_version(tmp_path, '# header\n\n   \n  # indented comment\n'
                            '  v2 abc  extra words\nv3 def\n')
    r = resolve_quietly(tmp_path)
    assert (r['version_tag'], r['version_commit']) == ('v2', 'abc')


def test_resolve_version_tag_only_commit_unknown(tmp_path, git):
    git()
    write_version(tmp_path, 'v2\n')
    r = resolve_quietly(tmp_path)
    assert (r['version_tag'], r['version_commit']) == ('v2', 'unknown')


def test_resolve_version_only_comments_is_unknown(tmp_path, git):
    git()
    write_version(tmp_path, '# nothing here\n')
    r = resolve_quietly(tmp_path)
    assert (r['version_tag'], r['version_commit']) == ('unknown', 'unknown')


def test_resolve_version_reads_utf8(tmp_path, git):
    git()
    write_version(tmp_path, 'v1-β abc\n')
    assert resolve_quietly(tmp_path)['version_tag'] == 'v1-β'


# -- resolve_runner_version: the git cross-check --------------------------

def test_resolve_version_git_commands_run_in_base_dir(tmp_path, git):
    fake = git(head='abc123\n')
    write_version(tmp_path, 'v1 abc\n')
    resolve_quietly(tmp_path)
    expected_kwargs = {'cwd': str(tmp_path), 'text': True,
                       'stderr': subprocess.DEVNULL}
    assert fake.calls == [
        (['git', 'rev-parse', 'HEAD'], expected_kwargs),
        (['git', 'status', '--porcelain', '--', '*.py'], expected_kwargs),
    ]


def test_resolve_version_head_matching_prefix_not_modified(tmp_path, git):
    git(head='abc123def\n')
    write_version(tmp_path, 'v1 abc123\n')
    assert resolve_quietly(tmp_path) == {
        'version_tag': 'v1', 'version_commit': 'abc123',
        'version_modified': False}


def test_resolve_version_head_differs_modified_with_warning(tmp_path, git):
    git(head='0123456789abcdef0123\n')
    write_version(tmp_path, 'v1 abc123\n')
    with pytest.warns(UserWarning) as rec:
        r = resolve_runner_version(str(tmp_path))
    assert r == {'version_tag': 'v1', 'version_commit': 'abc123',
                 'version_modified': True,
                 'git_commit': '0123456789abcdef0123'}
    assert [str(w.message) for w in rec] == [
        'VERSION file says abc123 but git HEAD is 0123456789ab. '
        'Runner may be modified.']


@pytest.mark.finding('S3-G3-2')
def test_resolve_version_one_character_commit_matches_any_head_with_it(
        tmp_path, git):
    # Current behaviour: the cross-check is a bare prefix test, so a
    # VERSION commit of 'a' accepts every HEAD starting with 'a'. Correct:
    # require a minimum prefix length (git's short SHA is 7).
    git(head='a' + 'f' * 39 + '\n')
    write_version(tmp_path, 'v1 a\n')
    assert resolve_quietly(tmp_path)['version_modified'] is False


def test_resolve_version_unknown_commit_skips_head_comparison(tmp_path, git):
    # With no commit in VERSION, any HEAD is accepted silently.
    git(head='0123456789\n')
    write_version(tmp_path, 'v1\n')
    assert resolve_quietly(tmp_path) == {
        'version_tag': 'v1', 'version_commit': 'unknown',
        'version_modified': False}


def test_resolve_version_dirty_py_files_mark_modified(tmp_path, git):
    # No warning and no git_commit: only the flag is set.
    git(head='abc123\n', status=' M src/x.py\n')
    write_version(tmp_path, 'v1 abc\n')
    assert resolve_quietly(tmp_path) == {
        'version_tag': 'v1', 'version_commit': 'abc',
        'version_modified': True}


def test_resolve_version_status_whitespace_only_is_clean(tmp_path, git):
    git(head='abc123\n', status='\n  \n')
    write_version(tmp_path, 'v1 abc\n')
    assert resolve_quietly(tmp_path)['version_modified'] is False


def test_resolve_version_dirty_check_runs_without_version_commit(
        tmp_path, git):
    git(head='abc123\n', status='?? scratch.py\n')
    assert resolve_quietly(tmp_path)['version_modified'] is True


@pytest.mark.parametrize('error', [
    subprocess.CalledProcessError(1, ['git']), FileNotFoundError()])
def test_resolve_version_status_failure_ignored(tmp_path, git, error):
    git(head='abc123\n', status=error)
    write_version(tmp_path, 'v1 abc\n')
    assert resolve_quietly(tmp_path)['version_modified'] is False


def test_resolve_version_no_git_binary_ignored(tmp_path, git):
    fake = git(head=FileNotFoundError())
    write_version(tmp_path, 'v1 abc\n')
    assert resolve_quietly(tmp_path)['version_commit'] == 'abc'
    assert len(fake.calls) == 1


def test_resolve_version_not_a_repository_skips_status(tmp_path, git):
    fake = git(head=NOT_A_REPO, status=' M x.py\n')
    write_version(tmp_path, 'v1 abc\n')
    assert resolve_quietly(tmp_path)['version_modified'] is False
    assert len(fake.calls) == 1


@pytest.mark.skipif(shutil.which('git') is None, reason='needs git')
def test_resolve_version_real_git_repository(tmp_path):
    # End to end against a real throwaway repository: VERSION names HEAD,
    # then an untracked .py file marks the runner modified.
    def run(*args):
        return subprocess.check_output(
            ['git', '-c', 'user.name=t', '-c', 'user.email=t@t',
             '-c', 'commit.gpgsign=false', *args],
            cwd=tmp_path, text=True, stderr=subprocess.DEVNULL).strip()
    run('init', '-q')
    (tmp_path / 'a.py').write_text('x = 1\n', encoding='utf-8')
    run('add', 'a.py')
    run('commit', '-q', '-m', 'one')
    head = run('rev-parse', 'HEAD')
    write_version(tmp_path, f'v9 {head[:7]}\n')
    assert resolve_quietly(tmp_path)['version_modified'] is False
    (tmp_path / 'scratch.py').write_text('', encoding='utf-8')
    assert resolve_quietly(tmp_path)['version_modified'] is True


# -- compute_runner_source_hash -------------------------------------------

def make_tree(root, files):
    for rel, content in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    return str(root)


def expected_hash(files):
    """The documented format: for each .py file in sorted relative-path
    order, path with '/', NUL, raw bytes, NUL."""
    h = hashlib.sha256()
    for rel in sorted(files):
        h.update(rel.encode('utf-8') + b'\x00' + files[rel] + b'\x00')
    return h.hexdigest()


def test_source_hash_empty_tree_is_sha256_of_nothing(tmp_path):
    assert compute_runner_source_hash(str(tmp_path)) == \
        hashlib.sha256(b'').hexdigest()


def test_source_hash_format_paths_and_contents_sorted(tmp_path):
    files = {'b.py': b'two\n', 'a.py': b'one\n', 'pkg/sub/c.py': b'\xffraw'}
    assert compute_runner_source_hash(make_tree(tmp_path, files)) == \
        expected_hash(files)


def test_source_hash_independent_of_location(tmp_path):
    files = {'a.py': b'1', 'pkg/b.py': b'2'}
    one = make_tree(tmp_path / 'one', files)
    two = make_tree(tmp_path / 'elsewhere' / 'two', files)
    assert compute_runner_source_hash(one) == compute_runner_source_hash(two)


def test_source_hash_changes_with_content(tmp_path):
    a = make_tree(tmp_path / 'a', {'x.py': b'1'})
    b = make_tree(tmp_path / 'b', {'x.py': b'2'})
    assert compute_runner_source_hash(a) != compute_runner_source_hash(b)


def test_source_hash_changes_with_file_name(tmp_path):
    a = make_tree(tmp_path / 'a', {'x.py': b'1'})
    b = make_tree(tmp_path / 'b', {'y.py': b'1'})
    assert compute_runner_source_hash(a) != compute_runner_source_hash(b)


@pytest.mark.finding('T3-70')
def test_source_hash_ignores_non_python_files(tmp_path):
    # Current behaviour: only .py files count, so VERSION, configs, the
    # fixture and data files can change without changing the hash.
    # Correct (T3-70): at least VERSION is part of the instrument.
    files = {'a.py': b'1'}
    root = make_tree(tmp_path, {**files, 'VERSION': b'v1 abc',
                                'example/config.json': b'{}',
                                'a.pyc': b'', 'a.py.bak': b''})
    assert compute_runner_source_hash(root) == expected_hash(files)


def test_source_hash_excludes_top_level_output_and_caches(tmp_path):
    files = {'a.py': b'1'}
    root = make_tree(tmp_path, {
        **files, 'output/run/x.py': b'', 'review_output_2/y.py': b'',
        '__pycache__/z.py': b''})
    assert compute_runner_source_hash(root) == expected_hash(files)


def test_source_hash_nested_output_directory_included(tmp_path):
    files = {'pkg/output/x.py': b'1', 'pkg/__pycache__/y.py': b'2'}
    assert compute_runner_source_hash(make_tree(tmp_path, files)) == \
        expected_hash(files)


@pytest.mark.finding('T3-70')
def test_source_hash_prefix_exclusion_drops_output_named_files(tmp_path):
    # Current behaviour: the exclusion is a string prefix, so a top-level
    # output_helpers.py or outputs/x.py is not hashed. Correct: exclude
    # the output/ directory only.
    files = {'a.py': b'1'}
    root = make_tree(tmp_path, {**files, 'output_helpers.py': b'2',
                                'outputs/x.py': b'3'})
    assert compute_runner_source_hash(root) == expected_hash(files)


@pytest.mark.finding('F2', 'T3-70')
def test_source_hash_includes_venv_tests_and_scratch_files(tmp_path):
    # Current behaviour (F2): every .py under the root is hashed: an
    # in-tree venv, the tests, and untracked scratch files, so a user
    # with a venv in the clone gets a different runner_source_hash.
    # Correct: hash the shipped runner (src/, plus whatever the release
    # defines), not the working tree.
    files = {'src/ap1_run/a.py': b'1',
             '.venv/lib/site-packages/pkg/m.py': b'2',
             'tests/unit/test_a.py': b'3', 'scratch.py': b'4'}
    assert compute_runner_source_hash(make_tree(tmp_path, files)) == \
        expected_hash(files)


# --- Step 4: correct behaviour (failing until fixed) ---

# F2 / T3-70, Steven's ruling (choices-for-marcus.md entry 6, step-4
# decisions "F2"): runner_source_hash covers src/ap1_run/ and VERSION only,
# not tests, tools/ or an in-tree venv. A test never runs during a
# measurement, so adding one must not make a run look like it used
# different code.

CLONE = {'src/ap1_run/__init__.py': b'',
         'src/ap1_run/run.py': b'def main(): pass\n',
         'src/ap1_run/scoring/accuracy.py': b'X = 1\n',
         'VERSION': b'v1.3.1 e0d9ec9\n',
         'smoke_test.py': b'from ap1_run.run import main\n',
         'tests/unit/test_run.py': b'def test_x(): pass\n',
         'tools/verify_run_seal.py': b'print(1)\n'}


def hash_after(tmp_path, change, files=CLONE):
    """The source hash of a clone, before and after `change` (a dict of
    relative path to new bytes) is written into it."""
    root = tmp_path / 'clone'
    make_tree(root, files)
    before = compute_runner_source_hash(str(root))
    make_tree(root, change)
    return before, compute_runner_source_hash(str(root))


@pytest.mark.finding('F2', 'T3-70')
@pytest.mark.parametrize('change', [
    {'tests/unit/test_run.py': b'def test_x(): assert 1\n'},
    {'tests/unit/test_new.py': b'def test_y(): pass\n'},
    {'tests/functional/conftest.py': b'X = 2\n'}],
    ids=['edit', 'add', 'other-dir'])
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='F2/T3-70: runner_source_hash covers the tests')
def test_source_hash_editing_tests_leaves_it_unchanged(tmp_path, change):
    before, after = hash_after(tmp_path, change)
    assert after == before


@pytest.mark.finding('F2', 'T3-70')
@pytest.mark.parametrize('change', [
    {'tools/verify_run_seal.py': b'print(2)\n'},
    {'tools/new_tool.py': b'print(3)\n'}], ids=['edit', 'add'])
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='F2/T3-70: runner_source_hash covers tools/')
def test_source_hash_editing_tools_leaves_it_unchanged(tmp_path, change):
    before, after = hash_after(tmp_path, change)
    assert after == before


@pytest.mark.finding('F2', 'T3-70')
@pytest.mark.parametrize('venv', ['.venv', 'venv'])
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='F2/T3-70: an in-tree venv changes '
                          'runner_source_hash')
def test_source_hash_venv_inside_clone_leaves_it_unchanged(tmp_path, venv):
    before, after = hash_after(tmp_path, {
        f'{venv}/lib/python3.12/site-packages/requests/api.py': b'x = 1\n',
        f'{venv}/bin/activate_this.py': b'pass\n'})
    assert after == before


@pytest.mark.finding('T3-70')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-70: untracked scratch files outside src/ap1_run '
                          'change runner_source_hash')
def test_source_hash_scratch_file_outside_package_leaves_it_unchanged(
        tmp_path):
    before, after = hash_after(tmp_path, {'scratch.py': b'print(1)\n',
                                          'output_helpers.py': b'x = 1\n'})
    assert after == before


@pytest.mark.finding('F2', 'T3-70')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-70: VERSION is not part of runner_source_hash')
def test_source_hash_editing_version_file_changes_it(tmp_path):
    before, after = hash_after(tmp_path, {'VERSION': b'v1.3.2 abcdef0\n'})
    assert after != before


@pytest.mark.finding('F2')
@pytest.mark.parametrize('change', [
    {'src/ap1_run/scoring/accuracy.py': b'X = 2\n'},
    {'src/ap1_run/scoring/new_module.py': b'Y = 1\n'}], ids=['edit', 'add'])
def test_source_hash_editing_package_module_changes_it(tmp_path, change):
    # Passes today and must keep passing after F2: the scope narrows to
    # src/ap1_run/ and VERSION, it does not drop the package.
    before, after = hash_after(tmp_path, change)
    assert after != before


@pytest.mark.finding('S3-G3-2')
@pytest.mark.parametrize('commit', ['a', 'a1', 'a1b2c3'])
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G3-2: a VERSION commit of fewer than 7 '
                          'characters matches any HEAD that starts with it')
def test_resolve_version_short_commit_prefix_is_modified(tmp_path, git,
                                                         commit):
    # Correct: the VERSION commit is a real abbreviated SHA (git's default
    # short form is 7 characters); a shorter one cannot identify HEAD, so
    # the runner is not taken to be the released version.
    git(head=commit + 'f' * (40 - len(commit)) + '\n')
    write_version(tmp_path, f'v1 {commit}\n')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        result = resolve_runner_version(str(tmp_path))
    assert result['version_modified'] is True
