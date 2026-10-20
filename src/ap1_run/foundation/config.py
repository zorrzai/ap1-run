"""R0.1 -- Configuration and Declaration.

Spec: AP-1 Runner Build Spec v0.3, section 3 R0.1.
Classification: DETERMINISTIC.

Loads config.json. Every field required; no defaults for anything
affecting a result. A missing field is an error, not a fallback.

All numeric configuration values are QUOTED STRINGS parsed to Decimal.
A bare numeric literal in config.json is refused at load.
"""

import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

from ap1_run.foundation.adapter import BODY_FIELDS
from ap1_run.foundation.numeric import ROUNDING_MODES


class ConfigError(Exception):
    """Configuration validation failure. Names the field and reason."""


# Every field required per spec R0.1
REQUIRED_FIELDS = [
    'endpoint_url', 'model', 'sampling', 'answer_tolerance',
    'quantisation', 'permitted_transformations', 'decline_markers',
    'decimal_separator', 'grouping_separator', 'currency_symbols',
    'dimensions_claimed', 'repeat_count', 'structured_answer_field',
    'ap1_version', 'ap1_text_hash', 'ap1_version_doi',
]

# Optional top-level fields used by engine.py and perturbation_guard.py
OPTIONAL_FIELDS = [
    'tools', 'tool_choice', 'system_prompt',
    'system_prompt_base', 'system_prompt_instruction_removed',
    'fixture_hash', 'message_template',
    'runner_version_tag', 'runner_version_commit',
    'runner_modified',
]

# The dimensions AP-1 defines (v1.2 and v1.3 alike).
DIMENSIONS = ('D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7')

# Minimum-n per dimension, per AP-1 version (SPEC R0.1). A dimension
# with no entry has no minimum the loader can check (D2's 10 x 50 is
# not in SPEC R0.1 yet).
#   per_category  every category of the question set has at least this
#   total         the eligible items number at least this
#   eligible      the item field that makes an item eligible: D5 counts
#                 items with an adversarial_class (AP-1 v1.3 §11.5), D6
#                 items with a conflict_class (§11.6); D1 counts every item
# v1.3: D1 l.204 and §11.1 (40 items, no category claim under 10), D5
# l.279 (20), D6 l.301 (10). v1.2: D1 l.111 and §11.1 (the same), D5
# l.149 (5), D6 §11.6 l.292 ("at least one item").
MINIMUM_N = {
    'v1.3': {
        'D1': {'per_category': 10, 'total': 40},
        'D5': {'eligible': 'adversarial_class', 'total': 20},
        'D6': {'eligible': 'conflict_class', 'total': 10},
    },
    'v1.2': {
        'D1': {'per_category': 10, 'total': 40},
        'D5': {'eligible': 'adversarial_class', 'total': 5},
        'D6': {'eligible': 'conflict_class', 'total': 1},
    },
}

# Fields whose values are parsed from string to Decimal
DECIMAL_FIELDS = ['answer_tolerance']

# Known sampling parameter names — used to suggest the sampling sub-dict
# when a config places one at top level.
KNOWN_SAMPLING_PARAMS = {
    'temperature', 'top_p', 'seed', 'max_tokens',
    'max_completion_tokens', 'top_k', 'presence_penalty',
    'frequency_penalty', 'stop', 'reasoning_effort',
}


def load_config(path):
    """Load and validate config.json per R0.1.

    Returns a dict with numeric string values parsed to Decimal.
    Raises ConfigError on any validation failure.
    """
    path = Path(path)
    if not path.exists():
        raise ConfigError(f'config file not found: {path}')

    with open(path, 'r', encoding='utf-8') as f:
        try:
            raw = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(f'invalid JSON in {path}: {e}') from e

    if not isinstance(raw, dict):
        raise ConfigError(f'config must be a JSON object, got {type(raw).__name__}')

    # 1. Check required fields
    for field in REQUIRED_FIELDS:
        if field not in raw:
            raise ConfigError(f'missing required field: {field!r}')

    # 1b. Refuse unknown top-level keys
    _refuse_unknown_fields(raw)

    # 1c. Every claimed dimension is one AP-1 defines
    _validate_dimensions(raw['dimensions_claimed'])

    # 2. Validate sampling omission reasons (before bare-numeric check)
    _validate_sampling(raw.get('sampling', {}))

    # 3. Refuse bare numeric literals anywhere in the tree
    _refuse_bare_numerics(raw)

    # 4. Parse numeric string fields to Decimal
    config = dict(raw)
    for field in DECIMAL_FIELDS:
        config[field] = _parse_decimal_field(raw, field)

    # 5. Parse quantisation sub-object
    q = raw.get('quantisation', {})
    if not isinstance(q, dict):
        raise ConfigError('quantisation must be an object')
    # Both parts are required: no default places or rounding mode (R0.1).
    for part in ('places', 'rounding'):
        if part not in q:
            raise ConfigError(f'missing required field: quantisation.{part}')
    rounding = q['rounding']
    if not isinstance(rounding, str) or rounding not in ROUNDING_MODES:
        raise ConfigError(
            f'quantisation.rounding: unknown rounding mode {rounding!r}. '
            f'Permitted: {", ".join(sorted(ROUNDING_MODES))}')
    config['quantisation'] = {
        'places': _parse_places(q['places']),
        'rounding': rounding,
    }

    # 6. Parse repeat_count
    rc = raw['repeat_count']
    if not isinstance(rc, str):
        raise ConfigError(
            f'repeat_count: expected quoted string, got {type(rc).__name__}')
    try:
        config['repeat_count'] = int(rc)
    except ValueError:
        raise ConfigError(f'repeat_count: cannot parse as integer: {rc!r}')
    if config['repeat_count'] < 1:
        raise ConfigError(f'repeat_count: must be at least 1: {rc!r}')

    # 7. Validate structured_answer_field
    saf = raw['structured_answer_field']
    config['structured_answer_field'] = None if saf == 'none' else saf

    return config



PERMITTED_OMISSION_REASONS = {
    'operator-declared',
    'platform-rejected',
    'platform-unsupported',
}


def _refuse_unknown_fields(raw):
    """Refuse any top-level key not in REQUIRED_FIELDS.

    An unknown field is the same category of error as a missing field:
    a configuration mistake, not a harmless extra. Where the key name
    matches a known sampling parameter, the error suggests the sampling
    sub-dict.
    """
    permitted = sorted(set(REQUIRED_FIELDS) | set(OPTIONAL_FIELDS))
    for key in raw:
        if key not in permitted:
            if key in KNOWN_SAMPLING_PARAMS:
                raise ConfigError(
                    f'unrecognised top-level field: {key!r}. '
                    f'Sampling parameters belong inside the '
                    f'"sampling" sub-dict, e.g. '
                    f'{{"sampling": {{"{key}": ...}}}}. '
                    f'Permitted top-level fields: {permitted}')
            raise ConfigError(
                f'unrecognised top-level field: {key!r}. '
                f'Permitted top-level fields: {permitted}')


def _validate_sampling(sampling_dict):
    """Validate sampling parameters per R0.1. sampling is an object
    (S3-G1-14). A key may not name a request body field (model,
    messages, tools; S3-G1-21), and a numeric value must be finite
    (S3-G1-19): the adapter would otherwise send NaN, which is not JSON.

    A sampling parameter may be:
    - A quoted numeric string (e.g. "0", "4096") — sent to the endpoint.
    - A structured omission dict: {"value": "omitted", "reason": "...", "detail": "..."}.
    - A plain string "omitted" WITHOUT a reason is REFUSED.

    Permitted reason values:
        operator-declared      — the operator chose not to set it
        platform-rejected      — the endpoint refused the value; detail required
        platform-unsupported   — the endpoint does not accept the parameter; detail required
    """
    if not isinstance(sampling_dict, dict):
        raise ConfigError(
            f'sampling must be an object, got '
            f'{type(sampling_dict).__name__}: {sampling_dict!r}')
    for k, v in sampling_dict.items():
        if k in BODY_FIELDS:
            raise ConfigError(
                f'sampling.{k}: a request body field, not a sampling '
                f'parameter')
        if isinstance(v, str) and _non_finite(v):
            raise ConfigError(f'sampling.{k}: must be a finite number: {v!r}')
        if isinstance(v, str) and v == 'omitted':
            raise ConfigError(
                f'sampling.{k}: omitted without a reason. '
                f'Use {{"value": "omitted", "reason": "...", "detail": "..."}}. '
                f'Permitted reasons: {", ".join(sorted(PERMITTED_OMISSION_REASONS))}')
        if isinstance(v, dict) and v.get('value') == 'omitted':
            reason = v.get('reason')
            if reason not in PERMITTED_OMISSION_REASONS:
                raise ConfigError(
                    f'sampling.{k}: invalid or missing reason {reason!r}. '
                    f'Permitted reasons: {", ".join(sorted(PERMITTED_OMISSION_REASONS))}')
            if reason in ('platform-rejected', 'platform-unsupported') and not v.get('detail'):
                raise ConfigError(
                    f'sampling.{k}: detail is required when reason is {reason!r}')


def _non_finite(text):
    """True if text reads as a Decimal that is NaN or infinite."""
    try:
        return not Decimal(text).is_finite()
    except InvalidOperation:
        return False


def _refuse_bare_numerics(obj, path=''):
    """Walk the JSON tree and refuse any int or float value.

    Every numeric configuration value must be a quoted string.
    A bare numeric literal is a configuration error.
    """
    if isinstance(obj, bool):
        return  # JSON booleans are not numeric values
    if isinstance(obj, (int, float)):
        raise ConfigError(
            f'bare numeric literal at {path or "root"}: {obj!r} -- '
            f'numeric values must be quoted strings, '
            f'e.g. "{obj}" not {obj}')
    if isinstance(obj, dict):
        # Omission objects are walked too: they hold strings only
        # (S3-G1-13).
        for k, v in obj.items():
            _refuse_bare_numerics(v, f'{path}.{k}' if path else k)
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            _refuse_bare_numerics(v, f'{path}[{i}]')


def _parse_decimal_field(raw, field):
    """Parse a config field from string to Decimal."""
    val = raw[field]
    if not isinstance(val, str):
        raise ConfigError(
            f'{field}: expected quoted string, got {type(val).__name__}: {val!r}')
    try:
        value = Decimal(val)
    except InvalidOperation:
        raise ConfigError(f'{field}: cannot parse as Decimal: {val!r}')
    if not value.is_finite() or value < 0:
        raise ConfigError(
            f'{field}: must be a finite, non-negative number: {val!r}')
    return value


def _parse_places(val):
    """quantisation.places: a quoted non-negative integer (S3-G1-10)."""
    if not isinstance(val, str):
        raise ConfigError(
            f'quantisation.places: expected quoted string, got '
            f'{type(val).__name__}: {val!r}')
    try:
        places = int(val)
    except ValueError:
        raise ConfigError(
            f'quantisation.places: cannot parse as integer: {val!r}')
    if places < 0:
        raise ConfigError(
            f'quantisation.places: must be a non-negative integer: {val!r}')
    return places


def _validate_dimensions(dims):
    """Refuse a dimensions_claimed that is not a list of D1-D7 (R0.1: a
    claim no fixture can support is refused at load)."""
    if not isinstance(dims, list):
        raise ConfigError(
            f'dimensions_claimed: expected a list, got {type(dims).__name__}')
    for dim in dims:
        if dim not in DIMENSIONS:
            raise ConfigError(
                f'dimensions_claimed: {dim!r} is not an AP-1 dimension. '
                f'Defined: {", ".join(DIMENSIONS)}')


def minimum_n_table(ap1_version):
    """The minimum-n table of the declared AP-1 version: 'v1.3' and
    'v1.2', alone or followed by '-' and a qualifier (as in
    'v1.3-draft-for-comment-20260730')."""
    for version, table in MINIMUM_N.items():
        if ap1_version == version or (
                isinstance(ap1_version, str)
                and ap1_version.startswith(version + '-')):
            return table
    raise ConfigError(
        f'ap1_version {ap1_version!r}: no minimum-n table for this version. '
        f'Known: {", ".join(MINIMUM_N)}')


def validate_minimum_n(config, question_set):
    """Enforce minimum-n requirements per R0.1.

    For each entry in dimensions_claimed, count eligible items and
    refuse the run where the count falls below the minimum of the
    declared AP-1 version. Names the dimension, count found, and
    minimum required.
    """
    dims = config.get('dimensions_claimed', [])
    _validate_dimensions(dims)
    if not dims:
        return
    table = minimum_n_table(config.get('ap1_version'))

    for dim in dims:
        rule = table.get(dim)
        if rule is None:
            continue

        if 'per_category' in rule:
            # D1: each category must meet the minimum
            categories = {}
            for q in question_set:
                cat = q.get('category', 'default')
                categories.setdefault(cat, 0)
                categories[cat] += 1
            for cat, count in categories.items():
                if count < rule['per_category']:
                    raise ConfigError(
                        f'{dim} category {cat!r}: {count} items, '
                        f'minimum {rule["per_category"]} required')

        field = rule.get('eligible')
        if field is None:
            count = len(question_set)
            if count < rule['total']:
                raise ConfigError(
                    f'{dim}: {count} items, '
                    f'minimum {rule["total"]} required')
        else:
            count = sum(1 for q in question_set if q.get(field))
            if count < rule['total']:
                raise ConfigError(
                    f'{dim}: {count} eligible items ({field} set), '
                    f'minimum {rule["total"]} required')
