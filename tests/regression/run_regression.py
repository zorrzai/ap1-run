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
    python tests/regression/run_regression.py --keep DIR replay_run_e_mini
                                       # also write the full output to DIR,
                                       # including files kept only as digests

Most scenarios run from the real tree: the runner gets the scenario's
config (written to a temporary directory) with --config and a temporary
--output-dir, so it never writes under the repository. A scenario that
sets "scratch_copy" (with the reason) runs instead in a scratch copy of
the repository (without .git and output/): one that writes files at fixed
repository paths, or checks that the default output/ stays untouched.
Either way git is hidden from the run (GIT_DIR points nowhere), as in a
copy without .git, so the result does not depend on the checkout's state.

Normalisation (in the comparison, never in the runner):
  - line endings to LF
  - the scratch copy's path (or the repository's and the temporary run
    directory's), and the mock endpoint's address and port
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
_SKIP_TOP = {'.git', '.venv', 'output', 'graphify-out', 'review_output',
             'mutants', '.pytest_cache'}

# Files the runner writes to output/.
_OUTPUTS = ['report.md', 'adjudication_sheets.md', 'smoke_summary.json',
            'smoke_run.jsonl', 'DISCLAIMER.txt']


# -- inputs ----------------------------------------------------------

def write_config(scenario, base_path, config_path):
    """The scenario's config: base_path with the scenario's "config"
    entries merged in, written to config_path."""
    with open(base_path, encoding='utf-8') as f:
        config = json.load(f)
    _deep_merge(config, scenario.get('config', {}))
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write('\n')


def scenario_config(scenario, directory):
    """The config file a real-tree run uses: the shipped one, or a merged
    copy in directory when the scenario changes it."""
    base = os.path.join(REPO, scenario.get('config_file',
                                           os.path.join('example',
                                                        'config.json')))
    if 'config' not in scenario:
        return base
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, 'config.json')
    write_config(scenario, base, path)
    return path


def _env(*, runner_env=False):
    """The environment of a run: nothing AP1_SMOKE_* inherited for a
    command, fixed hashing and encoding, no bytecode, and no git."""
    env = dict(os.environ)
    if not runner_env:  # the driver clears and sets these itself
        env = {k: v for k, v in env.items() if not k.startswith('AP1_SMOKE_')}
    env.update(PYTHONHASHSEED='0', PYTHONIOENCODING='utf-8',
               PYTHONDONTWRITEBYTECODE='1',
               # The runner cross-checks VERSION against git HEAD. The
               # golden output pins a run without git (as in a copy
               # without .git); a checkout on any branch must give it.
               GIT_DIR=os.path.join(tempfile.gettempdir(),
                                    'ap1rt-no-git', 'none'))
    return env


def snapshot(directory):
    """Every file under directory, with its size and mtime."""
    found = {}
    for root, dirs, files in os.walk(directory):
        for f in files:
            p = os.path.join(root, f)
            st = os.stat(p)
            found[os.path.relpath(p, directory)] = (st.st_size,
                                                    st.st_mtime_ns)
    return found


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
        write_config(scenario, config_path, config_path)
    # Copies inside the tree, after the config edits (for the runner's
    # path options): {"from": "to"}, a file or a directory.
    for src, dst in scenario.get('copy_paths', {}).items():
        src, dst = os.path.join(tree, src), os.path.join(tree, dst)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copyfile(src, dst)
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
    if scenario.get('scratch_copy'):
        return run_in_copy(name, scenario, coverage_dir)
    # The published runs must come out of a real-tree run untouched.
    published = snapshot(os.path.join(REPO, 'output'))
    try:
        return run_in_tree(name, scenario, coverage_dir)
    finally:
        if snapshot(os.path.join(REPO, 'output')) != published:
            raise RuntimeError(f'{name}: the run changed {REPO}/output')


def _coverage(name, coverage_dir, source):
    if not coverage_dir:
        return []
    return ['-m', 'coverage', 'run', '--branch',
            f'--data-file={os.path.join(coverage_dir, ".coverage." + name)}',
            f'--context=regression:{name}', f'--source={source}']


def run_in_tree(name, scenario, coverage_dir):
    """Run from the repository itself. The runner reads its inputs from
    the tree (the config from a temporary copy when the scenario edits
    it) and writes to a temporary run directory, which stands where the
    scratch copy's root stood: <RUNDIR>/output/."""
    copy_only = {'copy_paths', 'output_dir', 'copy_output'} & set(scenario)
    if copy_only:
        raise RuntimeError(f'{name}: {", ".join(sorted(copy_only))} '
                           'need "scratch_copy"')
    work = tempfile.mkdtemp(prefix='ap1rt-')
    try:
        if 'command' in scenario:
            return run_command(name, scenario, REPO, coverage_dir)
        run_dir = os.path.join(work, 'run')
        output_dir = os.path.join(run_dir, 'output')
        os.makedirs(output_dir)
        config_path = scenario_config(scenario, os.path.join(work, 'inputs'))
        scenario = dict(scenario, args=['--config', config_path,
                                        '--output-dir', output_dir]
                        + scenario.get('args', []))
        proc, result_dir = _drive(name, scenario, REPO, work, coverage_dir)
        return collect(proc, result_dir, output_dir, [REPO, run_dir])
    finally:
        shutil.rmtree(work, ignore_errors=True)


def run_in_copy(name, scenario, coverage_dir):
    """Run in a scratch copy of the repository (see "scratch_copy")."""
    copy_dir, tree = make_copy(scenario)
    try:
        if 'command' in scenario:
            return run_command(name, scenario, tree, coverage_dir)
        proc, result_dir = _drive(name, scenario, tree, copy_dir,
                                  coverage_dir)
        output_dir = os.path.join(tree, scenario.get('output_dir', 'output'))
        default_output = os.path.join(tree, 'output')
        return collect(proc, result_dir, output_dir, [tree],
                       default_output=(default_output
                                       if output_dir != default_output
                                       else None))
    finally:
        shutil.rmtree(copy_dir, ignore_errors=True)


def _drive(name, scenario, code_dir, work, coverage_dir):
    """The runner under the driver, from code_dir; results under work."""
    result_dir = os.path.join(work, 'result')
    os.makedirs(result_dir)
    path = os.path.join(work, 'scenario.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(scenario, f, indent=2)
    cmd = ([sys.executable] + _coverage(name, coverage_dir, code_dir)
           + [DRIVER, code_dir, path, result_dir, REPO])
    proc = subprocess.run(cmd, cwd=code_dir, env=_env(runner_env=True),
                          capture_output=True, text=True, encoding='utf-8',
                          timeout=3600)
    if not os.path.exists(os.path.join(result_dir, 'exit.json')):
        raise RuntimeError(f'driver failed for {name}:\n{proc.stderr}')
    return proc, result_dir


def run_command(name, scenario, tree, coverage_dir):
    """A command scenario: run one entry point from tree (the repository
    or a scratch copy) and pin its console, exit code and the files it
    writes."""
    cmd = [sys.executable] + _coverage(name, coverage_dir, tree)
    args = list(scenario['command'])
    env = _env()
    if os.path.isdir(os.path.join(tree, 'src')):
        # The tree's package, not an installed one.
        env['PYTHONPATH'] = os.path.join(tree, 'src')
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
    return {k: normalise(v, [tree], []) for k, v in raw.items()}


def _read(path):
    with open(path, encoding='utf-8', newline='') as f:
        return f.read()


def collect(proc, result_dir, output_dir, roots, default_output=None):
    """What a runner scenario produced. roots are the paths that become
    <RUNDIR>; default_output, when the runner was pointed elsewhere, is
    the default output/ that must stay as the copy made it."""
    raw = {
        'console.txt': proc.stdout,
        'stderr.txt': proc.stderr,
        'exit.json': _read(os.path.join(result_dir, 'exit.json')),
        'requests.jsonl': _read(os.path.join(result_dir, 'requests.jsonl')),
    }
    produced = []
    for name in _OUTPUTS:
        p = os.path.join(output_dir, name)
        if os.path.exists(p):
            produced.append(name)
            raw[name] = _read(p)
    raw['files.txt'] = ''.join(f'{n}\n' for n in produced)
    if default_output:
        raw['default_output.txt'] = ''.join(
            f'{n}\n' for n in sorted(os.listdir(default_output)))
    if 'smoke_run.jsonl' in raw:
        raw['outcomes.jsonl'] = outcome_table(raw['smoke_run.jsonl'])

    seals = json.loads(_read(os.path.join(result_dir, 'seal.json')))
    return {k: normalise(v, roots, seals) for k, v in raw.items()}


def digest_large(scenario, produced):
    """Large outputs: keep a digest; the details stay in outcomes.jsonl.
    The full files are available with --keep."""
    out = dict(produced)
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
# The environment fields of the seal (F2) in report.md section 1: they
# depend on the machine, not on the code.
_ENVIRONMENT_ROW = re.compile(
    r'(\| `(?:python_version|platform|package_versions)` \| `)[^`]*(` \|)')


def normalise(text, roots, seals):
    text = text.replace('\r\n', '\n')
    paths = set(roots) | {os.path.realpath(r) for r in roots}
    for p in sorted(paths, key=len, reverse=True):
        text = text.replace(p, '<RUNDIR>')
        text = text.replace(json.dumps(p)[1:-1], '<RUNDIR>')
    text = _MOCK.sub('<MOCK>', text)
    text = _ISO.sub('<TIMESTAMP>', text)
    text = _EPOCH.sub(r'\1"<EPOCH>"', text)
    text = _SOURCE_HASH_LINE.sub(r'\1<RUNNER_SOURCE_HASH>', text)
    text = _ENVIRONMENT_ROW.sub(r'\1<ENVIRONMENT>\2', text)
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


def write_dir(directory, produced):
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)
    for fname, text in produced.items():
        with open(os.path.join(directory, fname), 'w', encoding='utf-8',
                  newline='\n') as f:
            f.write(text)


def update(name, produced):
    write_dir(os.path.join(GOLDEN, name), produced)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('scenarios', nargs='*')
    ap.add_argument('--update', action='store_true',
                    help='rewrite the golden output from this run')
    ap.add_argument('--runs', type=int, default=1,
                    help='run each scenario N times (determinism check)')
    ap.add_argument('--coverage', metavar='DIR',
                    help='write coverage data files to DIR')
    ap.add_argument('--keep', metavar='DIR',
                    help='also write the full normalised output of each '
                         'scenario to DIR/<scenario>/, including files the '
                         'golden output keeps only as a digest')
    args = ap.parse_args(argv)

    names = args.scenarios or sorted(
        f[:-5] for f in os.listdir(SCENARIOS) if f.endswith('.json'))
    if args.coverage:
        os.makedirs(args.coverage, exist_ok=True)

    failures = 0
    for name in names:
        for run in range(1, args.runs + 1):
            full = run_scenario(
                name, coverage_dir=args.coverage if run == 1 else None)
            if args.keep and run == 1:
                write_dir(os.path.join(args.keep, name), full)
            produced = digest_large(load_scenario(name), full)
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
