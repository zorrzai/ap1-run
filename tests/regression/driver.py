"""Run one regression scenario: the real runner against the mock endpoint.

Invoked by run_regression.py in a fresh subprocess, from the code tree the
runner is imported from: the repository itself (the scenario's args then
include --config and a temporary --output-dir, so nothing is written under
the repository), or a scratch copy of it:

    python driver.py <code_dir> <scenario.json> <result_dir> <repo_dir>

The mock endpoint reads the questions and system prompts from the files the
runner will use: --config and --fixture-dir in the scenario's args, or the
defaults under <code_dir>/example/.

The runner's console output is this process's stdout. Driver messages go
to stderr. The result directory receives:
    exit.json       exit code, or the exception type and message
    seal.json       the seal record(s) the run created
    seal_inputs.json  what each call to the seal function was given
                    (see snapshot()), for the hash oracle
    transport_violations.json
                    requests the mock refused as outside its transport
                    contract (wrong path or credential); must be empty
    requests.jsonl  every request the mock endpoint received
"""

import argparse
import json
import os
import sys
import time
from decimal import Decimal

# The credential the runner is given, and the mock requires.
API_KEY = 'sk-regression-not-a-real-key-0000'

# The seal function's path arguments, captured as strings; every other
# argument is captured as it is.
PATH_ARGS = ('fixture_path', 'questions_path', 'ground_truth_path',
             'ap1_text_path')


def snapshot(value):
    """A typed copy of a value, safe to write as JSON: [type, payload].

    Taken before the seal function runs, so nothing it or the runner does
    later can change the evidence. Decimals keep their exact string; a
    float or any other type is recorded as such, and the oracle refuses it.
    """
    if isinstance(value, bool):
        return ['bool', value]
    if value is None:
        return ['none', None]
    if isinstance(value, str):
        return ['str', value]
    if isinstance(value, int):
        return ['int', value]
    if isinstance(value, Decimal):
        return ['decimal', str(value)]
    if isinstance(value, float):
        return ['float', repr(value)]
    if isinstance(value, (list, tuple)):
        return ['list', [snapshot(v) for v in value]]
    if isinstance(value, dict):
        return ['dict', [[snapshot(k), snapshot(v)] for k, v in value.items()]]
    return ['other', type(value).__name__, repr(value)]


def input_paths(code_dir, args):
    """The config and fixture directory the runner will read: the
    scenario's --config and --fixture-dir (relative to code_dir, the
    runner's working directory), or the runner's defaults."""
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('--config',
                    default=os.path.join('example', 'config.json'))
    ap.add_argument('--fixture-dir', default='example')
    known, _ = ap.parse_known_args(args)
    known.config = os.path.join(code_dir, known.config)
    known.fixture_dir = os.path.join(code_dir, known.fixture_dir)
    return known


def main():
    code_dir, scenario_path, result_dir, repo_dir = sys.argv[1:5]
    with open(scenario_path, encoding='utf-8') as f:
        scenario = json.load(f)

    sys.path.insert(0, os.path.join(repo_dir, 'tests', 'fixtures'))
    from mock_endpoint import MockEndpoint

    paths = input_paths(code_dir, scenario.get('args', []))
    with open(os.path.join(paths.fixture_dir, 'questions.json'),
              encoding='utf-8') as f:
        questions = json.load(f)
    with open(paths.config, encoding='utf-8') as f:
        config = json.load(f)
    system_prompts = {
        config['system_prompt_base']: 'base',
        config['system_prompt_instruction_removed']: 'instruction_removed',
    }

    replay_records = None
    if 'replay' in scenario:
        with open(os.path.join(repo_dir, scenario['replay']),
                  encoding='utf-8') as f:
            replay_records = [json.loads(line) for line in f if line.strip()]

    mock = MockEndpoint(questions=questions, system_prompts=system_prompts,
                        api_key=API_KEY, responses=scenario.get('responses'),
                        replay_records=replay_records).start()

    # Only what the scenario sets; nothing inherited from the shell.
    for name in list(os.environ):
        if name.startswith('AP1_SMOKE_'):
            del os.environ[name]
    os.environ['AP1_SMOKE_API_KEY'] = API_KEY
    os.environ['AP1_SMOKE_ENDPOINT'] = mock.url
    os.environ['AP1_SMOKE_MODEL'] = 'mock-model'
    os.environ.update(scenario.get('env', {}))

    # The runner sleeps 0.5 s per execution, and the adapter 1 s between
    # transport retries. Neither changes behaviour; skip them.
    time.sleep = lambda seconds: None

    os.chdir(code_dir)
    if os.path.isdir(os.path.join(code_dir, 'src')):
        sys.path.insert(0, os.path.join(code_dir, 'src'))
    sys.path.insert(0, code_dir)

    outcome = {}
    seals = []
    seal_inputs = []
    try:
        if os.path.exists(os.path.join(code_dir, 'smoke_test.py')):
            import smoke_test
        else:  # the runner has moved, and there is no shim (yet)
            import ap1_run.run as smoke_test
        # smoke_test.py may be a shim; patch the module main() lives in.
        runner = sys.modules[smoke_test.main.__module__]

        # Observe the seal the run makes (unchanged), so the comparison
        # can replace this run's own hash values by name.
        real_seal = runner.create_seal

        def observed_seal(**kwargs):
            seal_inputs.append({
                'cwd': os.getcwd(),
                'kwargs': {k: snapshot(os.fspath(v) if k in PATH_ARGS
                                       and v is not None else v)
                           for k, v in kwargs.items()},
                'returned': False})
            try:
                record = real_seal(**kwargs)
            except BaseException as e:
                seal_inputs[-1]['error'] = f'{type(e).__name__}: {e}'
                raise
            seals.append(record)
            seal_inputs[-1]['returned'] = True
            return record
        runner.create_seal = observed_seal

        # The runner reads its options from sys.argv; give it the
        # scenario's, not this driver's.
        sys.argv = ['ap1-run'] + scenario.get('args', [])
        outcome['exit_code'] = smoke_test.main()
    except SystemExit as e:
        outcome['exit_code'] = e.code
    except BaseException as e:  # pinned as behaviour, not re-raised
        outcome['exit_code'] = None
        outcome['exception'] = f'{type(e).__name__}: {e}'
    finally:
        sys.stdout.flush()
        mock.stop()

    with open(os.path.join(result_dir, 'exit.json'), 'w',
              encoding='utf-8') as f:
        json.dump(outcome, f, indent=2)
        f.write('\n')
    with open(os.path.join(result_dir, 'seal.json'), 'w',
              encoding='utf-8') as f:
        json.dump(seals, f, indent=2, sort_keys=True)
        f.write('\n')
    with open(os.path.join(result_dir, 'seal_inputs.json'), 'w',
              encoding='utf-8') as f:
        json.dump(seal_inputs, f, indent=2, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(result_dir, 'transport_violations.json'), 'w',
              encoding='utf-8') as f:
        json.dump(mock.violations, f, indent=2)
        f.write('\n')
    with open(os.path.join(result_dir, 'requests.jsonl'), 'w',
              encoding='utf-8') as f:
        for entry in mock.log:
            f.write(json.dumps(entry, sort_keys=True, ensure_ascii=False))
            f.write('\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
