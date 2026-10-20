"""Measure what the safety net executes: the pytest suite plus the
regression scenarios, with per-test contexts, combined.

    python tests/regression/coverage_report.py OUTDIR

Writes OUTDIR/coverage.txt (per-file line and branch coverage, keyed by
file name so the numbers can be compared across the file move) and
OUTDIR/htmlcov/ (coverage.py's HTML, with "show contexts" for which
test ran each line). Needs the coverage package.
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
                '    */tests/*\n    */verify*.py\n    */test_*.py\n'
                '    */run_all_tests.py\n')
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
               PYTHONIOENCODING='utf-8')

    subprocess.run(
        [sys.executable, '-m', 'coverage', 'run', '--branch',
         f'--data-file={os.path.join(data, ".coverage.pytest")}',
         '--context=pytest', f'--source={REPO}', '-m', 'pytest', '-q',
         '-p', 'no:cacheprovider'],
        cwd=REPO, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    subprocess.run([sys.executable, os.path.join(HERE, 'run_regression.py'),
                    '--coverage', data], env=env, stdout=subprocess.DEVNULL)

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


if __name__ == '__main__':
    main()
