"""Check that the root entry points use their own clone's src/, nothing else.

A pass/fail check, not a golden comparison:

    python tests/regression/check_own_src.py

`smoke_test.py`, `tools/verify_run_seal.py` and `tools/generate_findings.py`
must put this clone's `src/` first on the path before they import `ap1_run`.
Otherwise, in an environment where another clone is installed (or is on
PYTHONPATH), they silently run the other clone's code, and `smoke_test.py`
then writes into the other clone's `output/`.

The check copies the tree to a scratch directory (so nothing is written to
this clone), puts a decoy `ap1_run` package first on PYTHONPATH, and for each
entry point, in a fresh interpreter:
  1. executes the script's top level (everything except `main()`) and
     requires `ap1_run` to come from the copy's `src/`, not the decoy;
  2. runs the script as a command whose arguments make it stop without
     writing anything, and requires the decoy never to be imported.
"""

import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))

# script, argv for a run that stops before writing anything
ENTRY_POINTS = [
    ('smoke_test.py', []),                  # no API key: instructions, exit 1
    ('tools/verify_run_seal.py', []),       # usage, exit 1
    ('tools/generate_findings.py', None),   # writes FINDINGS.md: top level only
]

DECOY_MARK = 'DECOY-ap1_run-IMPORTED'
_IGNORE = shutil.ignore_patterns('.git', 'output', 'review_output*',
                                 '__pycache__', '.venv*', 'build', '*.egg-info')

# Execute a script's top level without running main(): run_path with a
# run_name other than '__main__' skips the `if __name__ == '__main__'` block.
_TOP_LEVEL = (
    'import runpy, sys\n'
    'runpy.run_path(sys.argv[1], run_name="check_own_src")\n'
    'import ap1_run\n'
    'print("AP1_RUN_FILE=" + ap1_run.__file__)\n'
)


def _make_decoy(root):
    pkg = os.path.join(root, 'ap1_run')
    os.makedirs(pkg)
    with open(os.path.join(pkg, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(f'import sys\nsys.stderr.write({DECOY_MARK!r} + "\\n")\n')


def main():
    failures = []
    with tempfile.TemporaryDirectory(prefix='ap1-own-src-') as tmp:
        clone = os.path.join(tmp, 'clone')
        shutil.copytree(REPO, clone, ignore=_IGNORE)
        decoy = os.path.join(tmp, 'decoy')
        _make_decoy(decoy)
        neutral = os.path.join(tmp, 'cwd')
        os.makedirs(neutral)

        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
                   PYTHONIOENCODING='utf-8')
        env['PYTHONPATH'] = os.pathsep.join(
            [decoy] + [p for p in env.get('PYTHONPATH', '').split(os.pathsep)
                       if p])
        for name in ('AP1_SMOKE_API_KEY', 'OPENAI_API_KEY'):
            env.pop(name, None)
        expected = os.path.normcase(os.path.realpath(
            os.path.join(clone, 'src', 'ap1_run', '__init__.py')))

        for script, argv in ENTRY_POINTS:
            path = os.path.join(clone, script)

            proc = subprocess.run([sys.executable, '-c', _TOP_LEVEL, path],
                                  cwd=neutral, env=env, capture_output=True,
                                  text=True, encoding='utf-8', timeout=120)
            got = [line[len('AP1_RUN_FILE='):] for line in
                   proc.stdout.splitlines() if line.startswith('AP1_RUN_FILE=')]
            ok = (proc.returncode == 0 and DECOY_MARK not in proc.stderr
                  and len(got) == 1
                  and os.path.normcase(os.path.realpath(got[0])) == expected)
            detail = got[0] if got else (proc.stderr.strip().splitlines()
                                         or ['?'])[-1]
            print(f'  {"ok  " if ok else "FAIL"}  {script} (top level): '
                  f'ap1_run from {detail}')
            if not ok:
                failures.append(f'{script} top level')

            if argv is None:
                continue
            proc = subprocess.run([sys.executable, path] + argv, cwd=clone,
                                  env=env, capture_output=True, text=True,
                                  encoding='utf-8', timeout=120)
            ok = DECOY_MARK not in proc.stderr and proc.returncode == 1
            print(f'  {"ok  " if ok else "FAIL"}  {script} (command): '
                  f'exit {proc.returncode}, decoy '
                  f'{"imported" if DECOY_MARK in proc.stderr else "not imported"}')
            if not ok:
                failures.append(f'{script} command')

        if os.path.exists(os.path.join(clone, 'output')):
            failures.append('a command wrote output/')
            print('  FAIL  a command wrote output/ in the scratch copy')

    print(f'\n{len(failures)} failed' if failures else '\nall entry points use '
          'their own src/')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
