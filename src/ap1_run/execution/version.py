"""Runner version resolution and source integrity.

Reads the VERSION file (authoritative, present in clones and tarballs).
Cross-checks against git when available. Computes a hash over the code
that runs (the .py files of the ap1_run package under src/, and VERSION)
for seal inclusion. Tests, tools, examples and anything else in the clone
(an in-tree venv, scratch files) are outside it (F2, T3-70); the Python
version, platform and package versions are recorded as separate seal
fields (runner_environment).

KNOWN LIMIT (scenario 3): a party who modifies the runner source and
distributes it as a zip without .git, without editing the VERSION file,
produces a run record that looks official. The runner_source_hash field
detects source changes (it will differ from the released hash), but
cannot prove the VERSION file is authentic. Detection of that case
requires out-of-band comparison against a published manifest.
"""

import hashlib
import importlib.metadata
import os
import platform
import subprocess
import warnings

# The shortest VERSION commit taken to identify HEAD: git's default
# abbreviated SHA. A shorter prefix matches too many commits (S3-G3-2).
MIN_COMMIT_PREFIX = 7

# What runner_source_hash covers, relative to the repository root.
SOURCE_PACKAGE = os.path.join('src', 'ap1_run')
VERSION_FILE = 'VERSION'

# The packages whose versions the seal records (F2): the runner's own
# distribution and its runtime dependencies (pyproject.toml).
RECORDED_PACKAGES = ('ap1-run', 'requests')


def resolve_runner_version(base_dir):
    """Read VERSION file, cross-check against git if available.

    Returns dict with keys:
        version_tag      -- tag from VERSION file, or 'unknown'
        version_commit   -- commit from VERSION file, or 'unknown'
        version_modified -- True if git HEAD differs from VERSION
        git_commit       -- actual git HEAD (if available and different)
    """
    version_path = os.path.join(base_dir, 'VERSION')
    tag = 'unknown'
    commit = 'unknown'
    modified = False
    result = {}

    if os.path.exists(version_path):
        with open(version_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    tag = parts[0] if parts else 'unknown'
                    commit = parts[1] if len(parts) > 1 else 'unknown'
                    break

    result = {
        'version_tag': tag,
        'version_commit': commit,
        'version_modified': False,
    }

    # Cross-check against git if available
    try:
        git_commit = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'],
            cwd=base_dir, text=True,
            stderr=subprocess.DEVNULL).strip()

        # A commit shorter than git's abbreviated SHA cannot identify
        # HEAD, so the runner is not taken to be the released version.
        if commit != 'unknown' and (len(commit) < MIN_COMMIT_PREFIX or
                                    not git_commit.startswith(commit)):
            result['version_modified'] = True
            result['git_commit'] = git_commit
            warnings.warn(
                f'VERSION file says {commit} but git HEAD is '
                f'{git_commit[:12]}. Runner may be modified.')

        # Check for uncommitted changes to the package's code (a test or
        # tool edit does not modify the runner, F2; VERSION itself is
        # compared with HEAD above)
        try:
            dirty = subprocess.check_output(
                ['git', 'status', '--porcelain', '--',
                 SOURCE_PACKAGE.replace(os.sep, '/')],
                cwd=base_dir, text=True,
                stderr=subprocess.DEVNULL).strip()
            if dirty:
                result['version_modified'] = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

    except (FileNotFoundError, subprocess.CalledProcessError):
        # No git -- cannot cross-check. VERSION file is authoritative.
        pass

    return result


def _source_files(base_dir):
    """The files runner_source_hash covers, as sorted relative paths: every
    .py file of the package under src/ap1_run/ (not __pycache__), and
    VERSION if present."""
    package = os.path.join(base_dir, SOURCE_PACKAGE)
    files = []
    for root, dirs, names in os.walk(package):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        files.extend(os.path.relpath(os.path.join(root, name), base_dir)
                     for name in names if name.endswith('.py'))
    if os.path.isfile(os.path.join(base_dir, VERSION_FILE)):
        files.append(VERSION_FILE)
    return sorted(f.replace(os.sep, '/') for f in files)


def compute_runner_source_hash(base_dir):
    """SHA-256 over the runner's code: the .py files of src/ap1_run/ and
    the VERSION file, sorted by relative path.

    Deterministic: same source -> same hash, regardless of platform
    or file timestamps. Computed before seal() and included in the
    seal record so that a modified instrument is detectable. Tests,
    tools/ and anything else in the clone are not hashed: they do not run
    during a measurement (F2).
    """
    h = hashlib.sha256()
    for rel_path in _source_files(base_dir):
        # Hash the relative path (so the hash is location-independent)
        h.update(rel_path.encode('utf-8'))
        h.update(b'\x00')
        with open(os.path.join(base_dir, rel_path), 'rb') as f:
            h.update(f.read())
        h.update(b'\x00')
    return h.hexdigest()


def runner_environment():
    """The environment a run executes in, recorded in the seal as fields
    of their own, outside runner_source_hash (F2): the Python
    implementation and version, the platform, and the installed versions
    of RECORDED_PACKAGES ('<name> <version>', or '<name> not installed')."""
    packages = []
    for name in RECORDED_PACKAGES:
        try:
            packages.append(f'{name} {importlib.metadata.version(name)}')
        except importlib.metadata.PackageNotFoundError:
            packages.append(f'{name} not installed')
    return {
        'python_version': (f'{platform.python_implementation()} '
                           f'{platform.python_version()}'),
        'platform': platform.platform(),
        'package_versions': ', '.join(packages),
    }
