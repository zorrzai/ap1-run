"""Mutation scores per module, with a ratchet.

Runs mutmut on one module at a time, against that module's unit tests
only, in a scratch copy of the repository (the repository itself is
never modified). Compares each score with the one recorded in
scores.json: a score may rise, never fall.

    python tests/mutation/run_mutation.py                 # every recorded module
    python tests/mutation/run_mutation.py execution/seal  # chosen modules
    python tests/mutation/run_mutation.py --record execution/seal
    python tests/mutation/run_mutation.py --survivors execution/seal

A module is named by its path under src/ap1_run/, without '.py'. Its
tests are the mirrored file tests/unit/<path>/test_<name>.py, unless
scores.json lists others under "tests".

The score is killed / (killed + survived + no tests + timeout): a mutant
that no test runs counts as a survivor. --record writes the measured
score to scores.json (and creates the entry), even if it fell. --survivors
prints the diff of each surviving mutant, for review and for the notes in
scores.json.

Exit code 0 if no score fell (or --record), 1 otherwise.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SCORES = os.path.join(HERE, 'scores.json')

_SKIP_TOP = {'.git', '.venv', 'output', 'mutants', '.pytest_cache',
             'graphify-out', 'review_output'}

# mutmut 3 copies only the mutated files; the rest of the package must be
# copied too (also_copy), and src/ must come first on the path, or the
# editable install of the repository would be imported instead. Tests
# that run the runner end to end also need the example, the AP-1 text,
# VERSION and the mock endpoint.
_CONFIG = '''
[tool.mutmut]
source_paths = [{source}]
also_copy = ["src/", "example/", "reference/", "docs/", "VERSION", "tests/fixtures/"]
pytest_add_cli_args_test_selection = [{tests}]
'''


def _ignore(directory, names):
    skipped = {n for n in names if n == '__pycache__' or n.endswith('.pyc')}
    if os.path.abspath(directory) == REPO:
        skipped |= _SKIP_TOP & set(names)
    return skipped


def load_scores():
    with open(SCORES, encoding='utf-8') as f:
        return json.load(f)


def save_scores(scores):
    with open(SCORES, 'w', encoding='utf-8') as f:
        json.dump(scores, f, indent=2, sort_keys=True)
        f.write('\n')


def tests_for(module, entry):
    if entry and entry.get('tests'):
        return entry['tests']
    layer, _, name = module.rpartition('/')
    path = os.path.join('tests', 'unit', layer, f'test_{name}.py')
    return [path.replace(os.sep, '/')]


def measure(module, tests, show_survivors=False):
    """Run mutmut on one module. Returns a dict of counts and the score."""
    source = f'src/ap1_run/{module}.py'
    if not os.path.exists(os.path.join(REPO, source)):
        raise SystemExit(f'no such module: {source}')
    for t in tests:
        if not os.path.exists(os.path.join(REPO, t)):
            raise SystemExit(f'no such test file: {t}')
    work = tempfile.mkdtemp(prefix='ap1mut-')
    tree = os.path.join(work, 'repo')
    try:
        shutil.copytree(REPO, tree, ignore=_ignore)
        with open(os.path.join(tree, 'pyproject.toml'), 'a',
                  encoding='utf-8') as f:
            f.write(_CONFIG.format(
                source=json.dumps(source),
                tests=', '.join(json.dumps(t) for t in tests)))
        env = dict(os.environ, PYTHONPATH='src')
        cmd = [sys.executable, '-m', 'mutmut', 'run']
        if os.environ.get('AP1_MUTMUT_MAX_CHILDREN'):
            cmd += ['--max-children', os.environ['AP1_MUTMUT_MAX_CHILDREN']]
        run = subprocess.run(cmd,
                             cwd=tree, env=env, capture_output=True,
                             text=True)
        results = subprocess.run(
            [sys.executable, '-m', 'mutmut', 'results', '--all', 'true'],
            cwd=tree, env=env, capture_output=True, text=True)
        counts = {}
        survivors = []
        for line in results.stdout.splitlines():
            m = re.match(r'\s*(\S+): (.+)$', line)
            if m:
                status = m.group(2).strip()
                counts[status] = counts.get(status, 0) + 1
                if status != 'killed':
                    survivors.append((m.group(1), status))
        if not counts:
            raise SystemExit(
                f'mutmut produced no results for {module}:\n'
                f'{run.stdout[-2000:]}\n{run.stderr[-2000:]}')
        if show_survivors:
            for name, status in survivors:
                shown = subprocess.run(
                    [sys.executable, '-m', 'mutmut', 'show', name],
                    cwd=tree, env=env, capture_output=True, text=True)
                print(f'## {status}')
                print(shown.stdout)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    total = sum(counts.values())
    killed = counts.get('killed', 0)
    return {
        'mutants': total,
        'killed': killed,
        'counts': dict(sorted(counts.items())),
        'score': round(killed / total, 4) if total else None,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('modules', nargs='*')
    parser.add_argument('--record', action='store_true',
                        help='write the measured scores to scores.json')
    parser.add_argument('--survivors', action='store_true',
                        help="print each surviving mutant's diff")
    parser.add_argument('--tests', action='append', metavar='FILE',
                        help='run this test file (repeatable) instead of the recorded '
                             'ones, e.g. legacy suites, to compare their '
                             'strength; cannot be combined with --record')
    args = parser.parse_args(argv)
    if args.tests and args.record:
        parser.error('--tests cannot be combined with --record')

    scores = load_scores()
    modules = args.modules or sorted(scores)
    if not modules:
        print('No modules recorded in scores.json, and none named.')
        return 0

    fell = []
    for module in modules:
        entry = scores.get(module)
        tests = args.tests or tests_for(module, entry)
        result = measure(module, tests, show_survivors=args.survivors)
        recorded = entry.get('score') if entry else None
        line = (f'{module}: {result["killed"]}/{result["mutants"]} killed, '
                f'score {result["score"]}')
        unchecked = result['counts'].get('not checked', 0)
        if unchecked:
            line += (f' [{unchecked} not checked: no test reached the '
                     f'mutated code, or the tests failed in the copy]')
        if recorded is not None and args.tests:
            line += f' (its own tests: {recorded})'
        elif recorded is not None:
            line += f' (recorded {recorded})'
            if result['score'] < recorded:
                line += '  FELL'
                fell.append(module)
        print(line, flush=True)
        if args.record:
            new = dict(entry or {})
            new.update(score=result['score'], mutants=result['mutants'],
                       killed=result['killed'])
            if tests != tests_for(module, None):
                new['tests'] = tests
            scores[module] = new
    if args.record:
        save_scores(scores)
    if fell:
        print(f'\nScore fell for: {", ".join(fell)}')
        if args.record:
            print('Recorded anyway (--record): account for the survivors '
                  'in the notes.')
            return 0
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
