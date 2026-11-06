"""Measure what the safety net executes: the pytest suite plus the
regression scenarios, with per-test contexts, combined.

    python tests/regression/coverage_report.py OUTDIR

Writes OUTDIR/coverage.txt (per-file line and branch coverage, keyed by
file name so the numbers can be compared across the file move) and
OUTDIR/htmlcov/ (coverage.py's HTML, with "show contexts" for which
test ran each line). Needs the dev extra (`pip install -e '.[dev]'`):
pytest and coverage.

The pytest run and the scenario runs log to OUTDIR/pytest.log and
OUTDIR/regression.log. If either fails, the script prints the end of its
log and exits non-zero without writing a report, so a report never lacks
a part silently.
"""

import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


def main():
    out = os.path.abspath(sys.argv[1])
    data = os.path.join(out, 'data')
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(data)
    rc = os.path.join(out, '.coveragerc')
    with open(rc, 'w') as f:
        f.write('[paths]\nsource =\n'
                f'    {REPO}/\n'
                '    */ap1rt-*/repo/\n'
                '[run]\nbranch = True\n'
                '[report]\nomit =\n'
                '    */tests/*\n    */test_*.py\n'
                # Files a scenario writes into its scratch copy (cli_paths
                # copies example/ to inputs/my_example/); they have no
                # source in the clone.
                '    */inputs/*\n')
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
               PYTHONIOENCODING='utf-8')

    _run_logged(
        'pytest', os.path.join(out, 'pytest.log'),
        [sys.executable, '-m', 'coverage', 'run', '--branch',
         f'--data-file={os.path.join(data, ".coverage.pytest")}',
         '--context=pytest', f'--source={REPO}', '-m', 'pytest', '-q',
         '-p', 'no:cacheprovider'],
        cwd=REPO, env=env)

    _run_logged('regression scenarios', os.path.join(out, 'regression.log'),
                [sys.executable, os.path.join(HERE, 'run_regression.py'),
                 '--coverage', data], env=env)

    combined = os.path.join(out, '.coverage')
    cov = [sys.executable, '-m', 'coverage']
    subprocess.run(cov + ['combine', f'--rcfile={rc}',
                          f'--data-file={combined}', '-q', data], check=True)
    report = subprocess.run(
        cov + ['report', f'--rcfile={rc}', f'--data-file={combined}'],
        capture_output=True, text=True, check=True).stdout
    subprocess.run(cov + ['html', f'--rcfile={rc}', f'--data-file={combined}',
                          '--show-contexts', '-q',
                          f'--directory={os.path.join(out, "htmlcov")}'],
                   check=True)
    report = report.replace(REPO + os.sep, '')
    with open(os.path.join(out, 'coverage.txt'), 'w') as f:
        f.write(report)
    print(report)


def _run_logged(what, log, cmd, **kwargs):
    """Run cmd with its output in log; on a non-zero exit, print the end
    of the log and exit with that code."""
    with open(log, 'w', encoding='utf-8') as f:
        rc = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT,
                            **kwargs).returncode
    if rc != 0:
        with open(log, encoding='utf-8', errors='replace') as f:
            tail = f.read().splitlines()[-20:]
        print('\n'.join(tail))
        sys.exit(f'coverage_report: the {what} run failed (exit {rc}); '
                 f'no report written. Full log: {log}')


if __name__ == '__main__':
    main()
