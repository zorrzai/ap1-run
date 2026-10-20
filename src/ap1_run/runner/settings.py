"""The live runner's settings, and the R1.2 guard.

Where the inputs and outputs are comes from the command line
(parse_args); the endpoint and model come from AP1_SMOKE_* environment
variables; print_sampling shows the sampling settings the config
declares, which nothing overrides; check_condition_guard refuses a run
whose two conditions differ in more than the system prompt.
"""

import argparse
import hashlib
import os

from ap1_run.execution.perturbation_guard import (
    check_single_variable_perturbation,
)

DEFAULT_ENDPOINT = 'https://api.openai.com/v1/chat/completions'
DEFAULT_MODEL = 'gpt-4o-mini'


AP1_TEXT = os.path.join('reference', 'AP-1_v1.3_DRAFT_FOR_COMMENT.md')


def parse_args(argv, base_dir):
    """The command-line options, as absolute paths.

    Every option defaults to the path the runner has always used under
    base_dir (the repository root), so a run without options is unchanged.
    """
    example_dir = os.path.join(base_dir, 'example')
    parser = argparse.ArgumentParser(
        prog='ap1-run',
        description='Run the AP-1 instrument smoke test against a live '
                    'endpoint. The endpoint, model and API key come from '
                    'the AP1_SMOKE_* environment variables.')
    parser.add_argument(
        '--config', default=os.path.join(example_dir, 'config.json'),
        help='the run configuration (default: example/config.json)')
    parser.add_argument(
        '--fixture-dir', default=example_dir,
        help='the directory holding fixture.json, questions.json and '
             'ground_truth_example.py (default: example/)')
    parser.add_argument(
        '--output-dir', default=os.path.join(base_dir, 'output'),
        help='where the transcript, report and summary are written; files '
             'of the same name there are replaced (default: output/)')
    parser.add_argument(
        '--ap1-text', default=os.path.join(base_dir, AP1_TEXT),
        help='the AP-1 text to seal; its hash must match the one the '
             'runner expects (default: ' + AP1_TEXT + ')')
    args = parser.parse_args(argv)
    for name in ('config', 'fixture_dir', 'output_dir', 'ap1_text'):
        setattr(args, name, os.path.abspath(getattr(args, name)))
    return args


def endpoint_and_model(environ=os.environ):
    """The endpoint and model: not secrets, read from the environment or
    the defaults."""
    endpoint = environ.get('AP1_SMOKE_ENDPOINT', DEFAULT_ENDPOINT)
    model = environ.get('AP1_SMOKE_MODEL', DEFAULT_MODEL)
    return endpoint, model


def print_sampling(config):
    """Print the temperature and reasoning_effort the run will send, as
    the config declares them. No environment variable changes a sampling
    setting: the config file that is loaded, validated and sealed is the
    only source (F1)."""
    sampling = config.get('sampling', {})
    for name, suffix in (('temperature', ''),
                         ('reasoning_effort', ' (from config)')):
        value = sampling.get(name)
        if isinstance(value, dict) and value.get('value') == 'omitted':
            print(f'  {name} omitted (reason: {value.get("reason", "?")})')
        else:
            print(f'  {name}={value}{suffix}')


def check_condition_guard(config, fixture_path, system_prompt_base,
                          system_prompt_removed, tools, sampling):
    """R1.2: refuse the run if the two conditions differ in anything but
    the system prompt (raises PerturbationRefusal)."""
    _fixture_bytes = open(fixture_path, 'rb').read()
    _fixture_hash = hashlib.sha256(_fixture_bytes).hexdigest()
    _base_guard = {
        'system_prompt': system_prompt_base,
        'tools': tools,
        'tool_choice': config.get('tool_choice'),
        'sampling': sampling,
        'fixture_hash': _fixture_hash,
        'message_template': config.get('message_template'),
    }
    _removed_guard = dict(_base_guard)
    _removed_guard['system_prompt'] = system_prompt_removed
    check_single_variable_perturbation(_base_guard, _removed_guard)
    print('Perturbation guard: PASSED (single-variable: system_prompt only)')
    print()
