"""Run one regression scenario: the real runner against the mock endpoint.

Invoked by run_regression.py in a fresh subprocess, inside a scratch copy
of the repository (so the runner's output/ directory is the copy's, never
the repository's published output/):

    python driver.py <copy_dir> <scenario.json> <result_dir> <repo_dir>

The runner's console output is this process's stdout. Driver messages go
to stderr. The result directory receives:
    exit.json       exit code, or the exception type and message
    seal.json       the seal record(s) the run created
    requests.jsonl  every request the mock endpoint received
"""

import json
import os
import sys
import time


def main():
    copy_dir, scenario_path, result_dir, repo_dir = sys.argv[1:5]
    with open(scenario_path, encoding='utf-8') as f:
        scenario = json.load(f)

    sys.path.insert(0, os.path.join(repo_dir, 'tests', 'fixtures'))
    from mock_endpoint import MockEndpoint

    with open(os.path.join(copy_dir, 'example', 'questions.json'),
              encoding='utf-8') as f:
        questions = json.load(f)
    with open(os.path.join(copy_dir, 'example', 'config.json'),
              encoding='utf-8') as f:
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
                        responses=scenario.get('responses'),
                        replay_records=replay_records).start()

    # Only what the scenario sets; nothing inherited from the shell.
    for name in list(os.environ):
        if name.startswith('AP1_SMOKE_'):
            del os.environ[name]
    os.environ['AP1_SMOKE_API_KEY'] = 'sk-regression-not-a-real-key-0000'
    os.environ['AP1_SMOKE_ENDPOINT'] = mock.url
    os.environ['AP1_SMOKE_MODEL'] = 'mock-model'
    os.environ.update(scenario.get('env', {}))

    # The runner sleeps 0.5 s per execution, and the adapter 1 s between
    # transport retries. Neither changes behaviour; skip them.
    time.sleep = lambda seconds: None

    os.chdir(copy_dir)
    if os.path.isdir(os.path.join(copy_dir, 'src')):
        sys.path.insert(0, os.path.join(copy_dir, 'src'))
    sys.path.insert(0, copy_dir)

    outcome = {}
    seals = []
    try:
        import smoke_test
        # smoke_test.py may be a shim; patch the module main() lives in.
        runner = sys.modules[smoke_test.main.__module__]

        # Observe the seal the run makes (unchanged), so the comparison
        # can replace this run's own hash values by name.
        real_seal = runner.create_seal

        def observed_seal(**kwargs):
            record = real_seal(**kwargs)
            seals.append(record)
            return record
        runner.create_seal = observed_seal

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
    with open(os.path.join(result_dir, 'requests.jsonl'), 'w',
              encoding='utf-8') as f:
        for entry in mock.log:
            f.write(json.dumps(entry, sort_keys=True, ensure_ascii=False))
            f.write('\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
