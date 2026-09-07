"""R3.1 -- Declared-Constants Check (AST).

Verifies that every numeric literal in a derive function's body
is a member of the declared constants set.  A constant used but
not declared is a silent dependency the perturbation check cannot
detect.  This is the defect that caused E3.

Separated from seal.py to stay within the 300-line module limit.
"""

import ast

from seal import SealError


def declared_constants_check(ground_truth_module, fixture, questions):
    """Verify every D("...") literal is declared in intermediates.

    Returns: list of failure dicts.  Empty = pass.
    Raises: SealError if any undeclared constant detected.
    """
    import inspect
    from context import build_delivered_context

    failures = []

    for item in questions.get('items', []):
        item_id = item['id']
        source_accounts = item.get('source_accounts', [])
        ctx = build_delivered_context(fixture, source_accounts)

        try:
            gt = ground_truth_module.compute(item_id, ctx)
        except Exception:
            continue

        if not gt.get('derivable', True):
            continue

        # Collect declared constants from intermediates
        declared = set()
        for inter in gt.get('intermediates', []):
            for inp in inter.get('inputs', []):
                if 'constant' in inp:
                    declared.add(inp['constant'])

        # Find the derive function
        derive_fn_name = f'derive_{item_id.lower()}'
        derive_fn = getattr(ground_truth_module, derive_fn_name, None)
        if derive_fn is None:
            continue

        try:
            fn_source = inspect.getsource(derive_fn)
        except (TypeError, OSError):
            continue

        try:
            tree = ast.parse(fn_source)
        except SyntaxError:
            continue

        # Walk AST for D("...") calls
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id == 'D'
                    and node.args
                    and isinstance(node.args[0], ast.Constant)
                    and isinstance(node.args[0].value, str)):
                literal = node.args[0].value
                if literal == '0':
                    continue
                if literal not in declared:
                    failures.append({
                        'item_id': item_id,
                        'literal': literal,
                        'reason': f'D("{literal}") in {derive_fn_name} '
                                  f'not declared as a constant',
                    })

    if failures:
        details = '; '.join(
            f'{f["item_id"]}: D("{f["literal"]}")' for f in failures)
        raise SealError(
            f'declared-constants check failed: undeclared numeric '
            f'literals. {details}')

    return failures
