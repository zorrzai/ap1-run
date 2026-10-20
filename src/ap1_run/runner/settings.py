"""The live runner's settings, and the R1.2 guard.

Where the inputs and outputs are comes from the command line
(parse_args); every run setting, the endpoint and model included, comes
from the config file alone; print_sampling shows the sampling settings it
declares; check_condition_guard refuses a run whose two conditions differ
in more than the system prompt.
"""

import argparse
import hashlib
import os

from ap1_run.execution.perturbation_guard import (
    check_single_variable_perturbation,
)


def parse_args(argv, base_dir):
    """The command-line options, as absolute paths.

    Every option defaults to the path the runner has always used under
    base_dir (the repository root), so a run without options is unchanged;
    --ap1-text defaults to None: the text is then chosen by the config's
    ap1_version (execution/ap1_texts.py, V12-4).
    """
    example_dir = os.path.join(base_dir, 'example')
    parser = argparse.ArgumentParser(
        prog='ap1-run',
        description='Run the AP-1 instrument smoke test against a live '
                    'endpoint. The endpoint, the model and every other '
                    'setting come from the config; only the API key comes '
                    'from the environment (AP1_SMOKE_API_KEY).')
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
    # No default path: None, and the run takes the text of the config's
    # ap1_version.
    parser.add_argument(
        '--ap1-text',
        help='the AP-1 text to seal; its hash must match the config\'s '
             'ap1_text_hash (default: the text of the config\'s '
             'ap1_version under reference/)')
    parser.add_argument(
        '--rescore', metavar='TRANSCRIPT',
        help='instead of running, score a run\'s transcript again (no '
             'endpoint, no key), with the run\'s --config and --fixture-dir, '
             'into another --output-dir')
    args = parser.parse_args(argv)
    for name in ('config', 'fixture_dir', 'output_dir', 'ap1_text',
                 'rescore'):
        if getattr(args, name) is not None:
            setattr(args, name, os.path.abspath(getattr(args, name)))
    return args


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


def condition_request(config, fixture_hash, system_prompt, tools, sampling):
    """What one condition sends, as the R1.2 guard compares it.

    The runner builds both conditions with this, checks them against
    each other, and gives the engine each condition's own system prompt
    and tools from the result, so that the guard compares what each arm
    is actually run with (T3-46).
    """
    return {
        'system_prompt': system_prompt,
        'tools': tools,
        'tool_choice': config.get('tool_choice'),
        'sampling': sampling,
        'fixture_hash': fixture_hash,
        'message_template': config.get('message_template'),
    }


def check_condition_guard(config, fixture_path, system_prompt_base,
                          system_prompt_removed, tools, sampling):
    """R1.2: refuse the run if the two conditions differ in anything but
    the system prompt, or if the system prompts are identical (raises
    PerturbationRefusal).

    Returns {condition: condition_request(...)} for 'base' and
    'instruction_removed'.
    """
    with open(fixture_path, 'rb') as f:
        fixture_hash = hashlib.sha256(f.read()).hexdigest()
    arms = {
        condition: condition_request(config, fixture_hash, prompt, tools,
                                     sampling)
        for condition, prompt in (('base', system_prompt_base),
                                  ('instruction_removed',
                                   system_prompt_removed))}
    check_single_variable_perturbation(arms['base'],
                                       arms['instruction_removed'])
    print('Perturbation guard: PASSED (single-variable: system_prompt only)')
    print()
    return arms
