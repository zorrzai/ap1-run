"""Runner version resolution and source integrity.

Reads the VERSION file (authoritative, present in clones and tarballs).
Cross-checks against git when available. Computes a hash over all .py
files in the runner for seal inclusion.

KNOWN LIMIT (scenario 3): a party who modifies the runner source and
distributes it as a zip without .git, without editing the VERSION file,
produces a run record that looks official. The runner_source_hash field
detects source changes (it will differ from the released hash), but
cannot prove the VERSION file is authentic. Detection of that case
requires out-of-band comparison against a published manifest.
"""

import hashlib
import os
import subprocess
import warnings


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

        if commit != 'unknown' and not git_commit.startswith(commit):
            result['version_modified'] = True
            result['git_commit'] = git_commit
            warnings.warn(
                f'VERSION file says {commit} but git HEAD is '
                f'{git_commit[:12]}. Runner may be modified.')

        # Check for uncommitted changes to .py files
        try:
            dirty = subprocess.check_output(
                ['git', 'status', '--porcelain', '--', '*.py'],
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


def compute_runner_source_hash(base_dir):
    """SHA-256 over all .py files in the runner, sorted by name.

    Deterministic: same source -> same hash, regardless of platform
    or file timestamps. Computed before seal() and included in the
    seal record so that a modified instrument is detectable.
    """
    h = hashlib.sha256()
    py_files = sorted(
        os.path.relpath(os.path.join(root, f), base_dir)
        for root, dirs, files in os.walk(base_dir)
        for f in files
        if f.endswith('.py')
        # Exclude output/, review_output*, and test scratch files
        and not os.path.relpath(os.path.join(root, f), base_dir)
            .startswith(('output', 'review_output', '__pycache__'))
    )
    for rel_path in py_files:
        abs_path = os.path.join(base_dir, rel_path)
        # Hash the relative path (so the hash is location-independent)
        h.update(rel_path.replace(os.sep, '/').encode('utf-8'))
        h.update(b'\x00')
        with open(abs_path, 'rb') as f:
            h.update(f.read())
        h.update(b'\x00')
    return h.hexdigest()
