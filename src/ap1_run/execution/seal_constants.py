"""R3.1 -- Declared-Constants Check (AST).

Verifies that every numeric literal in a derive function's body
is a member of the declared constants set.  A constant used but
not declared is a silent dependency the perturbation check cannot
detect.  This is the defect that caused E3.

A numeric literal is a number in the source (4, 12.5) or a string
passed to D(...) or Decimal(...) ("12").  Literals are compared with
the declared constants as text.  The literal 0 is exempt.  Functions
of the ground-truth module that the derive function calls are checked
too, as part of the item.

The check fails closed (T3-54): an item whose literals cannot be
checked (compute raises, there is no derive_<id> function, or a
function's source cannot be read or parsed) is a failure, named.
"""

import ast
import inspect
import textwrap

from ap1_run.execution.seal import SealError

DECIMAL_NAMES = ('D', 'Decimal')


def declared_constants_check(ground_truth_module, fixture, questions):
    """Verify every numeric literal is declared in intermediates.

    Returns: list of failure dicts.  Empty = pass.
    Raises: SealError if any undeclared constant is found or an item
            cannot be checked, naming the item and the literal or reason.
    """
    from ap1_run.execution.context import build_delivered_context

    failures = []

    for item in questions.get('items', []):
        item_id = item['id']
        source_accounts = item.get('source_accounts', [])
        ctx = build_delivered_context(fixture, source_accounts)

        try:
            gt = ground_truth_module.compute(item_id, ctx)
        except Exception as exc:
            failures.append(f'{item_id}: cannot check (compute raised '
                            f'{type(exc).__name__}: {exc})')
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
            failures.append(f'{item_id}: cannot check (no function '
                            f'{derive_fn_name})')
            continue

        literals, unreadable = _numeric_literals(
            derive_fn, ground_truth_module)
        for name in unreadable:
            failures.append(f'{item_id}: cannot check (source of {name} '
                            f'unreadable)')
        for literal, text in literals:
            if literal == '0':
                continue
            if literal not in declared:
                failures.append(f'{item_id}: {text}')

    if failures:
        raise SealError(
            f'declared-constants check failed: undeclared numeric '
            f'literals. {"; ".join(failures)}')

    return failures


def _numeric_literals(derive_fn, module):
    """The numeric literals of derive_fn and of the module's functions
    it calls, as (literal text, source text) pairs, and the names of the
    functions whose source could not be read."""
    literals, unreadable = [], []
    _collect(derive_fn, module, literals, unreadable, set())
    return literals, unreadable


def _collect(fn, module, literals, unreadable, seen):
    """Add fn's literals, then those of each module function it calls
    (each function once)."""
    if fn in seen:
        return
    seen.add(fn)
    try:
        source = textwrap.dedent(inspect.getsource(fn))
        tree = ast.parse(source)
    except (TypeError, OSError, SyntaxError):
        unreadable.append(getattr(fn, '__name__', repr(fn)))
        return
    literals.extend(_literals_in(tree, source))
    namespace = vars(module)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            callee = namespace.get(node.func.id)
            if (inspect.isfunction(callee)
                    and callee.__module__ == module.__name__):
                _collect(callee, module, literals, unreadable, seen)


def _literals_in(tree, source):
    """(literal text, source text) for each numeric literal in tree,
    in source order."""
    found = []
    nodes = sorted((n for n in ast.walk(tree) if hasattr(n, 'lineno')),
                   key=lambda n: (n.lineno, n.col_offset))
    for node in nodes:
        if (isinstance(node, ast.Call)
                and _called_name(node.func) in DECIMAL_NAMES
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)):
            found.append((node.args[0].value,
                          ast.get_source_segment(source, node)))
        elif (isinstance(node, ast.Constant)
                and isinstance(node.value, (int, float, complex))
                and not isinstance(node.value, bool)):
            found.append((ast.get_source_segment(source, node),
                          ast.get_source_segment(source, node)))
    return found


def _called_name(func):
    """The name a call is made through: D(...) -> 'D',
    decimal.Decimal(...) -> 'Decimal'."""
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None
