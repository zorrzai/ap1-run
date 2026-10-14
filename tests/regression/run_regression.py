"""Regression baseline: run every scenario and compare with its golden output.

Each scenario (scenarios/<name>.json) drives the real runner
(smoke_test.main) end to end against a mock endpoint with canned model
responses, so every run is deterministic. What the run produces is
normalised and compared exactly with golden/<name>/.

The golden files pin CURRENT behaviour, right or wrong. Known defects
(T3-1, T3-2, ...) appear in them as they are today. A change that alters
behaviour must change golden files in the same commit, with the reason.

Usage:
    python tests/regression/run_regression.py              # compare all
    python tests/regression/run_regression.py clean t3_1   # some
    python tests/regression/run_regression.py --update     # rewrite goldens
    python tests/regression/run_regression.py --runs 3     # determinism
    python tests/regression/run_regression.py --coverage DIR
                                       # also write coverage data to DIR

Each run happens in a scratch copy of the repository (without .git and
output/), so the runner writes to the copy's output/, never to the
published runs under output/.

Normalisation (in the comparison, never in the runner):
  - line endings to LF
  - the scratch copy's path, and the mock endpoint's address and port
  - ISO timestamps, and the adapter's epoch timestamps
  - this run's seal_hash, config_hash and runner_source_hash, read from
    the seal the run actually made (the config hash covers the mock's
    port; the source hash covers the code, and changes when files move)
"""

import argparse
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SCENARIOS = os.path.join(HERE, 'scenarios')
GOLDEN = os.path.join(HERE, 'golden')
DRIVER = os.path.join(HERE, 'driver.py')

# Not copied into the scratch tree.
_SKIP_TOP = {'.git', '.venv', 'output', 'graphify-out', 'review_output'}

# Files the runner writes to output/.
_OUTPUTS = ['report.md', 'adjudication_sheets.md', 'smoke_summary.json',
            'smoke_run.jsonl', 'DISCLAIMER.txt']


# -- scratch copy ----------------------------------------------------

def _ignore(directory, names):
    skipped = {n for n in names if n == '__pycache__' or n.endswith('.pyc')}
    if os.path.abspath(directory) == REPO:
        skipped |= _SKIP_TOP & set(names)
    if os.path.abspath(directory) == HERE:
        skipped |= {'golden'} & set(names)
    return skipped


def _deep_merge(base, overrides):
    for k, v in overrides.items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            _deep_merge(base[k], v)
        else:
            base[k] = v


def make_copy(scenario):
    copy_dir = tempfile.mkdtemp(prefix='ap1rt-')
    tree = os.path.join(copy_dir, 'repo')
    shutil.copytree(REPO, tree, ignore=_ignore)
    os.makedirs(os.path.join(tree, 'output'))
    for sub in scenario.get('copy_output', []):
        shutil.copytree(os.path.join(REPO, 'output', sub),
                        os.path.join(tree, 'output', sub))
    config_path = os.path.join(tree, 'example', 'config.json')
    if 'config_file' in scenario:
        shutil.copyfile(os.path.join(tree, scenario['config_file']),
                        config_path)
    if 'config' in scenario:
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
        _deep_merge(config, scenario['config'])
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
            f.write('\n')
    return copy_dir, tree


# -- one run ---------------------------------------------------------

def load_scenario(name):
    """Load a scenario, resolving "extends": the named scenario's config,
    env and responses are the base; this one's entries override them."""
    with open(os.path.join(SCENARIOS, f'{name}.json'), encoding='utf-8') as f:
        scenario = json.load(f)
    parent = scenario.pop('extends', None)
    if parent:
        base = load_scenario(parent)
        for key in ('config', 'env', 'responses'):
            merged = json.loads(json.dumps(base.get(key, {})))
            if key == 'config':
                _deep_merge(merged, scenario.get(key, {}))
            else:
                merged.update(scenario.get(key, {}))
            if merged:
                scenario[key] = merged
    return scenario


def run_scenario(name, coverage_dir=None):
    """Run one scenario. Returns {golden file name: normalised text}."""
    scenario = load_scenario(name)
    copy_dir, tree = make_copy(scenario)
    result_dir = os.path.join(copy_dir, 'result')
    os.makedirs(result_dir)
    path = os.path.join(copy_dir, 'scenario.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(scenario, f, indent=2)
    try:
        if 'command' in scenario:
            return run_command(name, scenario, tree, result_dir, coverage_dir)
        cmd = [sys.executable]
        if coverage_dir:
            cmd += ['-m', 'coverage', 'run', '--branch',
                    f'--data-file={os.path.join(coverage_dir, ".coverage." + name)}',
                    f'--context=regression:{name}', f'--source={tree}']
        cmd += [DRIVER, tree, path, result_dir, REPO]
        env = dict(os.environ, PYTHONHASHSEED='0', PYTHONIOENCODING='utf-8',
                   PYTHONDONTWRITEBYTECODE='1')
        proc = subprocess.run(cmd, cwd=tree, env=env, capture_output=True,
                              text=True, encoding='utf-8', timeout=3600)
        if not os.path.exists(os.path.join(result_dir, 'exit.json')):
            raise RuntimeError(f'driver failed for {name}:\n{proc.stderr}')
        return collect(scenario, tree, result_dir, proc)
    finally:
        shutil.rmtree(copy_dir, ignore_errors=True)


def run_command(name, scenario, tree, result_dir, coverage_dir):
    """A command scenario: run one entry point in the scratch copy and
    pin its console, exit code and the files it writes."""
    cmd = [sys.executable]
    args = list(scenario['command'])
    if coverage_dir:
        cmd += ['-m', 'coverage', 'run', '--branch',
                f'--data-file={os.path.join(coverage_dir, ".coverage." + name)}',
                f'--context=regression:{name}', f'--source={tree}']
    env = {k: v for k, v in os.environ.items()
           if not k.startswith('AP1_SMOKE_')}
    env.update(PYTHONHASHSEED='0', PYTHONIOENCODING='utf-8',
               PYTHONDONTWRITEBYTECODE='1')
    env.update(scenario.get('env', {}))
    proc = subprocess.run(cmd + args, cwd=tree, env=env, capture_output=True,
                          text=True, encoding='utf-8', timeout=3600)
    raw = {
        'console.txt': proc.stdout,
        'stderr.txt': proc.stderr,
        'exit.json': json.dumps({'exit_code': proc.returncode}, indent=2) + '\n',
    }
    for rel in scenario.get('collect', []):
        p = os.path.join(tree, rel)
        key = rel.replace('/', '__')
        raw[key] = _read(p) if os.path.exists(p) else '(not written)\n'
    return {k: normalise(v, tree, []) for k, v in raw.items()}


def _read(path):
    with open(path, encoding='utf-8', newline='') as f:
        return f.read()


def collect(scenario, tree, result_dir, proc):
    raw = {
        'console.txt': proc.stdout,
        'stderr.txt': proc.stderr,
        'exit.json': _read(os.path.join(result_dir, 'exit.json')),
        'requests.jsonl': _read(os.path.join(result_dir, 'requests.jsonl')),
    }
    produced = []
    for name in _OUTPUTS:
        p = os.path.join(tree, 'output', name)
        if os.path.exists(p):
            produced.append(name)
            raw[name] = _read(p)
    raw['files.txt'] = ''.join(f'{n}\n' for n in produced)
    if 'smoke_run.jsonl' in raw:
        raw['outcomes.jsonl'] = outcome_table(raw['smoke_run.jsonl'])

    seals = json.loads(_read(os.path.join(result_dir, 'seal.json')))
    out = {k: normalise(v, tree, seals) for k, v in raw.items()}

    # Large outputs: keep a digest; the details stay in outcomes.jsonl.
    for name in scenario.get('digest_only', []):
        if name in out:
            text = out.pop(name)
            digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
            out[name + '.sha256'] = f'{digest}  {name} (normalised)\n'
    return out


def outcome_table(transcript_text):
    """One line per execution: what the runner decided about it."""
    engine, figures = [], {}
    for line in transcript_text.splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        key = (rec.get('item_id'), rec.get('condition'))
        if rec.get('record_type') == 'figure_identification':
            figures.setdefault(key, []).append(rec)
        else:
            engine.append(rec)
    rows, seen = [], {}
    for rec in engine:
        key = (rec.get('item_id'), rec.get('condition'))
        n = seen.get(key, 0)
        seen[key] = n + 1
        fig = (figures.get(key) or [None] * (n + 1))
        fig = fig[n] if n < len(fig) else None
        rows.append({
            'item': key[0], 'condition': key[1], 'n': n + 1,
            'error_state': rec.get('error_state'),
            'evidence_class': rec.get('evidence_class'),
            'invocation': rec.get('invocation_outcome'),
            'tool_calls': len(rec.get('tool_calls') or []),
            'provenance': [p.get('outcome') for p in
                           rec.get('provenance_results') or []],
            'operation': [o.get('outcome') for o in
                          rec.get('operation_correctness') or []],
            'figure': fig.get('figure_outcome') if fig else None,
            'released': fig.get('released_figure') if fig else None,
        })
    return ''.join(json.dumps(r, sort_keys=True) + '\n' for r in rows)


_ISO = re.compile(
    r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:\+00:00|Z)')
_EPOCH = re.compile(r'("timestamp":\s*)\d{9,}(?:\.\d+)?')
_MOCK = re.compile(r'http://127\.0\.0\.1:\d+')
# Printed before the seal exists, so not covered by the seal's values.
_SOURCE_HASH_LINE = re.compile(r'(Runner source hash: )[0-9a-f]+')


def normalise(text, tree, seals):
    text = text.replace('\r\n', '\n')
    for p in sorted({tree, os.path.realpath(tree)}, key=len, reverse=True):
        text = text.replace(p, '<RUNDIR>')
        text = text.replace(json.dumps(p)[1:-1], '<RUNDIR>')
    text = _MOCK.sub('<MOCK>', text)
    text = _ISO.sub('<TIMESTAMP>', text)
    text = _EPOCH.sub(r'\1"<EPOCH>"', text)
    text = _SOURCE_HASH_LINE.sub(r'\1<RUNNER_SOURCE_HASH>', text)
    for seal in seals:
        for field, label in (('seal_hash', '<SEAL_HASH>'),
                             ('config_hash', '<CONFIG_HASH>'),
                             ('runner_source_hash', '<RUNNER_SOURCE_HASH>')):
            value = seal.get(field) or ''
            if len(value) >= 16:
                text = text.replace(value, label)
                # Shortened forms printed by the runner.
                text = re.sub(re.escape(value[:12]) + r'[0-9a-f]*', label,
                              text)
    return text


# -- compare / update ------------------------------------------------

def compare(name, produced):
    golden_dir = os.path.join(GOLDEN, name)
    problems = []
    expected = set(os.listdir(golden_dir)) if os.path.isdir(golden_dir) else set()
    if not expected:
        return [f'{name}: no golden output (run with --update)']
    for fname in sorted(expected | set(produced)):
        if fname not in produced:
            problems.append(f'{name}/{fname}: expected but not produced')
            continue
        if fname not in expected:
            problems.append(f'{name}/{fname}: produced but not in golden')
            continue
        want = _read(os.path.join(golden_dir, fname))
        got = produced[fname]
        if want != got:
            diff = difflib.unified_diff(
                want.splitlines(), got.splitlines(),
                f'golden/{name}/{fname}', f'run/{name}/{fname}', lineterm='',
                n=1)
            lines = list(diff)
            shown = '\n'.join(lines[:40])
            more = f'\n  ... {len(lines) - 40} more diff lines' if len(lines) > 40 else ''
            problems.append(f'{name}/{fname}: differs\n{shown}{more}')
    return problems


def update(name, produced):
    golden_dir = os.path.join(GOLDEN, name)
    if os.path.isdir(golden_dir):
        shutil.rmtree(golden_dir)
    os.makedirs(golden_dir)
    for fname, text in produced.items():
        with open(os.path.join(golden_dir, fname), 'w', encoding='utf-8',
                  newline='\n') as f:
            f.write(text)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('scenarios', nargs='*')
    ap.add_argument('--update', action='store_true',
                    help='rewrite the golden output from this run')
    ap.add_argument('--runs', type=int, default=1,
                    help='run each scenario N times (determinism check)')
    ap.add_argument('--coverage', metavar='DIR',
                    help='write coverage data files to DIR')
    args = ap.parse_args(argv)

    names = args.scenarios or sorted(
        f[:-5] for f in os.listdir(SCENARIOS) if f.endswith('.json'))
    if args.coverage:
        os.makedirs(args.coverage, exist_ok=True)

    failures = 0
    for name in names:
        for run in range(1, args.runs + 1):
            produced = run_scenario(
                name, coverage_dir=args.coverage if run == 1 else None)
            label = f'{name}' + (f' (run {run})' if args.runs > 1 else '')
            if args.update and run == 1:
                update(name, produced)
                print(f'  UPDATED  {label}')
                continue
            problems = compare(name, produced)
            if problems:
                failures += 1
                print(f'  FAIL     {label}')
                for p in problems:
                    print('    ' + p.replace('\n', '\n    '))
            else:
                print(f'  PASS     {label}')
        sys.stdout.flush()

    total = len(names) * args.runs
    print(f'\n{total - failures}/{total} scenario runs match golden output'
          if not args.update else f'\n{len(names)} scenarios updated')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
