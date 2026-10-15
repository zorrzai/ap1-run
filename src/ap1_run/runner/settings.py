"""The live runner's settings from the environment, and the R1.2 guard.

The endpoint, model and two sampling overrides come from AP1_SMOKE_*
environment variables; check_condition_guard refuses a run whose two
conditions differ in more than the system prompt.
"""

import hashlib
import os

from ap1_run.execution.perturbation_guard import (
    check_single_variable_perturbation,
)

DEFAULT_ENDPOINT = 'https://api.openai.com/v1/chat/completions'
DEFAULT_MODEL = 'gpt-4o-mini'


def endpoint_and_model(environ=os.environ):
    """The endpoint and model: not secrets, read from the environment or
    the defaults."""
    endpoint = environ.get('AP1_SMOKE_ENDPOINT', DEFAULT_ENDPOINT)
    model = environ.get('AP1_SMOKE_MODEL', DEFAULT_MODEL)
    return endpoint, model


def apply_sampling_overrides(config, environ=os.environ):
    """Apply AP1_SMOKE_TEMPERATURE and AP1_SMOKE_REASONING_EFFORT to the
    config's sampling block, printing what will be sent."""
    # -- Sampling override: AP1_SMOKE_TEMPERATURE --
    # gpt-5.6-sol rejects temperature=0 with HTTP 400 (verified 2026-09-07).
    # Its error says: "Only the default (1) value is supported."
    # gpt-4.1-mini accepts temperature=0 and temperature=1 (verified 2026-09-07).
    #
    # To keep both arms at the same temperature (1), the operator sets
    # AP1_SMOKE_TEMPERATURE=1 for mini. For sol, the env var is not set
    # and the structured omission (platform-rejected) is kept.
    #
    # This is a declared env-var override, not a model-name heuristic.
    # The resolved config in report.md §2 records what was actually sent.
    temp_override = environ.get('AP1_SMOKE_TEMPERATURE')
    if temp_override is not None:
        config['sampling']['temperature'] = temp_override
        print(f'  temperature={temp_override} '
              f'(AP1_SMOKE_TEMPERATURE override)')
    else:
        temp_val = config.get('sampling', {}).get('temperature')
        if isinstance(temp_val, dict) and temp_val.get('value') == 'omitted':
            print(f'  temperature omitted '
                  f'(reason: {temp_val.get("reason", "?")})')
        else:
            print(f'  temperature={temp_val}')

    # -- Sampling override: AP1_SMOKE_REASONING_EFFORT --
    # gpt-4.1-mini does not support reasoning_effort (HTTP 400:
    #   "Unrecognized request argument supplied: reasoning_effort").
    # gpt-5.6-sol requires it and accepts "none" for tool use.
    #
    # For mini: set AP1_SMOKE_REASONING_EFFORT=omit to remove it.
    # For sol:  leave unset, config value "none" is sent.
    re_override = environ.get('AP1_SMOKE_REASONING_EFFORT')
    if re_override == 'omit':
        config['sampling']['reasoning_effort'] = {
            'value': 'omitted',
            'reason': 'not-supported',
            'detail': 'gpt-4.1-mini does not recognize reasoning_effort',
        }
        print('  reasoning_effort omitted (AP1_SMOKE_REASONING_EFFORT=omit)')
    elif re_override is not None:
        config['sampling']['reasoning_effort'] = re_override
        print(f'  reasoning_effort={re_override} '
              f'(AP1_SMOKE_REASONING_EFFORT override)')
    else:
        re_val = config.get('sampling', {}).get('reasoning_effort')
        print(f'  reasoning_effort={re_val} (from config)')


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
