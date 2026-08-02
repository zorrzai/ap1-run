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

# Minimum-n per dimension (AP-1 v1.3 section 4.5, 4.6)
MINIMUM_N = {
    'D1': {'type': 'per_category', 'min': 10},
    'D5': {'type': 'total', 'min': 20},
    'D6': {'type': 'total', 'min': 10},
}

# Fields whose values are parsed from string to Decimal
DECIMAL_FIELDS = ['answer_tolerance']


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
    config['quantisation'] = {
        'places': int(q.get('places', '2')),
        'rounding': q.get('rounding', 'ROUND_HALF_UP'),
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

    # 7. Validate structured_answer_field
    saf = raw['structured_answer_field']
    config['structured_answer_field'] = None if saf == 'none' else saf

    return config



PERMITTED_OMISSION_REASONS = {
    'operator-declared',
    'platform-rejected',
    'platform-unsupported',
}


def _validate_sampling(sampling_dict):
    """Validate sampling parameters per R0.1.

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
        return
    for k, v in sampling_dict.items():
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
        # Skip structured omission objects (validated by _validate_sampling)
        if obj.get('value') == 'omitted' and 'reason' in obj:
            return
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
        return Decimal(val)
    except InvalidOperation:
        raise ConfigError(f'{field}: cannot parse as Decimal: {val!r}')


def validate_minimum_n(config, question_set):
    """Enforce minimum-n requirements per R0.1.

    For each entry in dimensions_claimed, count eligible items and
    refuse the run where the count falls below the minimum.
    Names the dimension, count found, and minimum required.
    """
    dims = config.get('dimensions_claimed', [])

    for dim in dims:
        if dim not in MINIMUM_N:
            continue

        rule = MINIMUM_N[dim]

        if rule['type'] == 'per_category':
            # D1: count per category, each must meet minimum
            categories = {}
            for q in question_set:
                cat = q.get('category', 'default')
                categories.setdefault(cat, 0)
                categories[cat] += 1
            for cat, count in categories.items():
                if count < rule['min']:
                    raise ConfigError(
                        f'{dim} category {cat!r}: {count} items, '
                        f'minimum {rule["min"]} required')

        elif rule['type'] == 'total':
            count = len(question_set)
            if count < rule['min']:
                raise ConfigError(
                    f'{dim}: {count} items, '
                    f'minimum {rule["min"]} required')
