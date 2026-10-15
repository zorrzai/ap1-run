"""Unit tests for scoring/provenance/provenance_audit.py: the
originated-operand listing in the report (R2.4)."""

import pytest

from ap1_run.scoring.provenance.provenance_audit import build_audit_listing

NO_MATCH = 'no source, transformed source, or intermediate matched'


@pytest.mark.req('R2.4')
def test_audit_listing_one_entry_per_originated_operand():
    items = [{
        'item_id': 'Q03', 'condition': 'base', 'repeat': 2,
        'operation': 'calculator',
        'item_outcome': {'all_originated': [
            {'value': '0.05', 'expression': '15200 * 0.05'},
            {'value': '7', 'expression': '7 + 1'},
        ]},
    }]
    assert build_audit_listing(items) == [
        {'item_id': 'Q03', 'condition': 'base', 'repeat': 2,
         'operation': 'calculator', 'expression': '15200 * 0.05',
         'originated_operand': '0.05', 'resolution': NO_MATCH},
        {'item_id': 'Q03', 'condition': 'base', 'repeat': 2,
         'operation': 'calculator', 'expression': '7 + 1',
         'originated_operand': '7', 'resolution': NO_MATCH},
    ]


def test_audit_listing_items_in_order_and_grounded_items_add_nothing():
    items = [
        {'item_id': 'Q01', 'item_outcome': {'all_originated': []}},
        {'item_id': 'Q02', 'item_outcome': {'all_originated': [{'value': '1'}]}},
        {'item_id': 'Q05', 'item_outcome': {'all_originated': [{'value': '2'}]}},
    ]
    listing = build_audit_listing(items)
    assert [(e['item_id'], e['originated_operand']) for e in listing] == [
        ('Q02', '1'), ('Q05', '2')]


def test_audit_listing_missing_fields_are_none():
    listing = build_audit_listing([{'item_outcome': {'all_originated': [{}]}}])
    assert listing == [{'item_id': None, 'condition': None, 'repeat': None,
                        'operation': None, 'expression': None,
                        'originated_operand': None, 'resolution': NO_MATCH}]


def test_audit_listing_item_without_outcome_adds_nothing():
    assert build_audit_listing([{'item_id': 'Q01'}, {'item_outcome': {}}]) == []


def test_audit_listing_empty():
    assert build_audit_listing([]) == []
