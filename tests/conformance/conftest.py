"""Shared helpers for the conformance tests."""

import json

import pytest


def minimal_config(**overrides):
    """A config dict with every R0.1 required field, as legacy
    verify_conformance.py builds it. Keyword overrides replace or add
    fields; an override of None deletes the field."""
    cfg = {
        'endpoint_url': 'http://test', 'model': 'test',
        'sampling': {}, 'answer_tolerance': '0.01',
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
        'permitted_transformations': [], 'decline_markers': [],
        'decimal_separator': '.', 'grouping_separator': ',',
        'currency_symbols': ['$'], 'dimensions_claimed': [],
        'repeat_count': '3', 'structured_answer_field': 'none',
        'ap1_version': 'v1.3',
        'ap1_text_hash': 'abc', 'ap1_version_doi': 'doi:test',
    }
    for key, value in overrides.items():
        if value is None:
            cfg.pop(key, None)
        else:
            cfg[key] = value
    return cfg


@pytest.fixture
def write_config(tmp_path):
    """Write minimal_config(**overrides) to a file and return its path."""
    def write(**overrides):
        path = tmp_path / 'config.json'
        path.write_text(json.dumps(minimal_config(**overrides)),
                        encoding='utf-8')
        return path
    return write
