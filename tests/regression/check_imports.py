"""Import every Python module of the instrument, each in a fresh interpreter.

A pass/fail check, not a golden comparison: module names change when files
move, but every module must still import. Modules are discovered, not
listed, so a file the move forgets to fix up is still caught.

    python tests/regression/check_imports.py

Discovery: every .py file outside tests/, the legacy test scripts
(verify*.py, test_*.py, run_all_tests.py), output/ and virtual
environments. Names:
  - under src/: the dotted path below src/ (src layout);
  - inside a directory with __init__.py: the dotted path from the root;
  - otherwise: the file's stem, with its directory on sys.path.
Modules that need inspect-ai are skipped when it is not installed.
"""

import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_SKIP_DIRS = {'.git', 'tests', 'output', 'graphify-out', '__pycache__',
              'review_output'}


def _is_legacy_test(name, rel_dir):
    return rel_dir == '' and (name.startswith(('verify', 'test_'))
                              or name == 'run_all_tests.py')


def discover():
    found = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = sorted(d for d in dirs if d not in _SKIP_DIRS
                         and not d.startswith('.venv'))
        rel_dir = os.path.relpath(root, REPO)
        rel_dir = '' if rel_dir == '.' else rel_dir
        for f in sorted(files):
            if not f.endswith('.py') or _is_legacy_test(f, rel_dir):
                continue
            found.append(module_for(rel_dir, f))
    return found


def module_for(rel_dir, filename):
    stem = filename[:-3]
    parts = rel_dir.split(os.sep) if rel_dir else []
    if parts[:1] == ['src']:
        dotted = parts[1:] + ([] if stem == '__init__' else [stem])
        return '.'.join(dotted), os.path.join(REPO, 'src')
    # Walk up while the directory is a package.
    pkg = []
    d = rel_dir
    while d and os.path.exists(os.path.join(REPO, d, '__init__.py')):
        pkg.insert(0, os.path.basename(d))
        d = os.path.dirname(d)
    if pkg:
        dotted = pkg + ([] if stem == '__init__' else [stem])
        return '.'.join(dotted), os.path.join(REPO, d) if d else REPO
    return stem, os.path.join(REPO, rel_dir) if rel_dir else REPO


def main():
    have_inspect = importlib.util.find_spec('inspect_ai') is not None
    failures, skipped, passed = [], [], 0
    for name, path_dir in discover():
        code = (f'import sys; sys.path[:0] = [{path_dir!r}, {REPO!r}]; '
                f'import importlib; importlib.import_module({name!r})')
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        proc = subprocess.run([sys.executable, '-c', code], cwd=REPO,
                              env=env, capture_output=True, text=True)
        if proc.returncode == 0:
            passed += 1
            print(f'  ok    {name}')
        elif not have_inspect and 'inspect_ai' in proc.stderr:
            skipped.append(name)
            print(f'  skip  {name} (inspect-ai not installed)')
        else:
            failures.append(name)
            last = proc.stderr.strip().splitlines()[-1:] or ['?']
            print(f'  FAIL  {name}: {last[0]}')
    print(f'\n{passed} imported, {len(skipped)} skipped, '
          f'{len(failures)} failed')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
