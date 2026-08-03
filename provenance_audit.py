"""Originated-operand audit listing for the report.

Spec: AP-1 Runner Build Spec v0.3, section 5 R2.4.
Classification: DETERMINISTIC.
"""


# -- Build the audit listing for the report ----------------------------

def build_audit_listing(item_results):
    """Build the originated-operand audit listing for the report.

    Per R2.4: the report lists, per originated operand: its value,
    the item, the operation, the full argument set, and the fact that
    no source or intermediate matched.

    Args:
        item_results: list of dicts with item_id, condition, repeat,
            operation, item_outcome dict

    Returns: list of audit entry dicts
    """
    entries = []
    for item in item_results:
        item_outcome = item.get('item_outcome', {})
        for orig in item_outcome.get('all_originated', []):
            entries.append({
                'item_id': item.get('item_id'),
                'condition': item.get('condition'),
                'repeat': item.get('repeat'),
                'operation': item.get('operation'),
                'expression': orig.get('expression'),
                'originated_operand': orig.get('value'),
                'resolution': 'no source, transformed source, '
                              'or intermediate matched',
            })
    return entries

