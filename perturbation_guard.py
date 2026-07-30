"""Single-variable perturbation guard.

Spec: AP-1 Runner Build Spec v0.3, R1.2 perturbation discipline.

The 'instruction_removed' condition alters the system prompt AND
NOTHING ELSE. Tool declarations, tool availability, fixture content,
sampling parameters and message structure are held constant.

A run in which more than one quantity differs is REFUSED (not
reported), with the diff emitted naming every changed quantity.
"""

import json


class PerturbationRefusal(Exception):
    """More than one quantity differs between conditions."""


def check_single_variable_perturbation(base_config, removed_config):
    """Verify instruction_removed differs from base in exactly
    one quantity: the system prompt.

    Compares: system_prompt, tools, tool_choice, sampling parameters,
    fixture content, message structure template.

    Returns: list of differences found (empty if valid).
    Raises: PerturbationRefusal if more than one quantity differs,
            with the diff naming every changed quantity.
    """
    diffs = []

    # System prompt SHOULD differ
    if base_config.get('system_prompt') == removed_config.get('system_prompt'):
        diffs.append({
            'field': 'system_prompt',
            'issue': 'system prompts are IDENTICAL — '
                     'instruction_removed must alter the system prompt',
        })

    # Tool declarations MUST NOT differ
    if _canonical(base_config.get('tools')) != \
            _canonical(removed_config.get('tools')):
        diffs.append({
            'field': 'tools',
            'issue': 'tool declarations differ between conditions',
            'base': _summarise(base_config.get('tools')),
            'removed': _summarise(removed_config.get('tools')),
        })

    # tool_choice MUST NOT differ
    if base_config.get('tool_choice') != removed_config.get('tool_choice'):
        diffs.append({
            'field': 'tool_choice',
            'issue': 'tool_choice differs between conditions',
            'base': base_config.get('tool_choice'),
            'removed': removed_config.get('tool_choice'),
        })

    # Sampling MUST NOT differ
    if _canonical(base_config.get('sampling', {})) != \
            _canonical(removed_config.get('sampling', {})):
        diffs.append({
            'field': 'sampling',
            'issue': 'sampling parameters differ between conditions',
            'base': base_config.get('sampling'),
            'removed': removed_config.get('sampling'),
        })

    # Fixture content MUST NOT differ
    if base_config.get('fixture_hash') != \
            removed_config.get('fixture_hash'):
        diffs.append({
            'field': 'fixture_content',
            'issue': 'fixture content differs between conditions',
        })

    # Message template MUST NOT differ
    if _canonical(base_config.get('message_template')) != \
            _canonical(removed_config.get('message_template')):
        diffs.append({
            'field': 'message_template',
            'issue': 'message structure template differs',
        })

    # Count non-system-prompt violations
    violations = [d for d in diffs if d['field'] != 'system_prompt']
    if violations:
        # Total changed = system_prompt (the allowed one) + violations
        total = len(violations) + 1
        raise PerturbationRefusal(
            f'instruction_removed condition changes '
            f'{total} quantities (must be exactly 1: '
            f'system_prompt). Changed quantities:\n'
            + '\n'.join(
                f'  - {d["field"]}: {d["issue"]}'
                for d in [{'field': 'system_prompt',
                           'issue': 'the one allowed change'}]
                + violations
            )
        )

    return diffs


def _canonical(obj):
    """Canonical JSON for comparison."""
    if obj is None:
        return 'null'
    return json.dumps(obj, sort_keys=True, default=str)


def _summarise(obj):
    """Short summary for diff messages."""
    s = json.dumps(obj, sort_keys=True, default=str)
    return s[:200] + '...' if len(s) > 200 else s
