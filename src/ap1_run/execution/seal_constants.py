"""R3.1 -- Declared-Constants Check (AST).

Verifies that every numeric literal in a derive function's body
is a member of the declared constants set.  A constant used but
not declared is a silent dependency the perturbation check cannot
detect.  This is the defect that caused E3.

A numeric literal is a number in the source (4, 12.5), or a string
passed to D(...), Decimal(...), int(...) or float(...) ("12", or "1" +
".05" folded).  Literals are compared with the declared constants as
text.  The literal 0 is exempt.

What is read for an item is what its computation runs: every top-level
statement of the module that executes while compute(item) runs (compute
itself, the function it dispatches to, helpers however they are called,
a class whose method runs), the derive_<id> function, and the
module-level assignments those statements read, followed through other
module-level names.  A constant defined at module level is charged to
each item whose computation reads it.

The check fails closed (T3-54): an item whose literals cannot be
checked (compute raises, there is no derive_<id> function, or the
module's source cannot be read or parsed) is a failure, named.

Not caught (registered residue): a number made without a numeric
literal (len("abcdefghijkl"), True + True), a string built other than by
"+" of string literals (f-strings, join), code outside the module's own
file, and a module that evades the field tracking deliberately
(TrackingAccount, T3-8).

Separated from seal.py under SPEC §12.9's former 300-line module limit
(removed in November 2026).
"""

import ast
import inspect
import sys

from ap1_run.execution.seal import SealError

DECIMAL_NAMES = ('D', 'Decimal', 'int', 'float')


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
            gt, executed = _compute_recording_lines(
                ground_truth_module, item_id, ctx)
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
            derive_fn, ground_truth_module, executed)
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


def _module_file(module):
    try:
        return inspect.getsourcefile(module)
    except TypeError:
        return None


def _compute_recording_lines(module, item_id, ctx):
    """compute(item_id, ctx); the lines of the module's own file that ran
    during it (sys.settrace; frames of other files are not traced); and
    the names of functions the module called whose code has no source
    file (made by exec or compile)."""
    filename = _module_file(module)
    executed, unreadable = set(), []

    def local(frame, event, arg):
        executed.add(frame.f_lineno)
        return local

    def tracer(frame, event, arg):
        code = frame.f_code
        if code.co_filename != filename:
            caller = frame.f_back
            if (code.co_filename.startswith('<') and caller is not None
                    and caller.f_code.co_filename == filename
                    and code.co_name not in unreadable):
                unreadable.append(code.co_name)
            return None
        executed.add(frame.f_lineno)
        return local

    previous = sys.gettrace()
    sys.settrace(tracer)
    try:
        gt = module.compute(item_id, ctx)
    finally:
        sys.settrace(previous)
    return gt, (executed, unreadable)


# The fields of a statement that hold nested statements.
_BLOCKS = ('body', 'orelse', 'handlers', 'finalbody', 'cases')


def _all_statements(stmts):
    """Every statement in stmts, nested blocks included."""
    for stmt in stmts:
        yield stmt
        for field in _BLOCKS:
            for child in getattr(stmt, field, None) or []:
                if isinstance(child, ast.stmt):
                    yield from _all_statements([child])
                else:                       # ExceptHandler, match_case
                    yield from _all_statements(child.body)


def _span(stmt):
    start = min([stmt.lineno] + [d.lineno for d in
                                 getattr(stmt, 'decorator_list', [])])
    return start, stmt.end_lineno


def _own_nodes(stmt):
    """The nodes of stmt without its nested statement blocks: for
    `if x > D("4"):` the test, not the branches; for a def its
    decorators and defaults, not its body."""
    nodes, pending = [], [stmt]
    while pending:
        node = pending.pop()
        nodes.append(node)
        for field, value in ast.iter_fields(node):
            if node is stmt and field in _BLOCKS:
                continue
            for child in value if isinstance(value, list) else [value]:
                if isinstance(child, ast.AST) and not isinstance(child,
                                                                 ast.stmt):
                    pending.append(child)
    return nodes


def _numeric_literals(derive_fn, module, executed=((), ())):
    """The numeric literals the item's computation read, as (literal
    text, source text) pairs in source order, and the names of what could
    not be read. Read: each statement of the module that ran (its own
    expressions, not the blocks nested in it); derive_fn's whole
    definition if it did not run; and the module-level assignments all
    of these read, followed through other module-level names."""
    executed_lines, unreadable = executed
    try:
        source = inspect.getsource(module)
        tree = ast.parse(source)
        derive_line = inspect.getsourcelines(derive_fn)[1]
    except (TypeError, OSError, SyntaxError):
        name = getattr(derive_fn, '__name__', None) or repr(derive_fn)
        return [], [name] + list(unreadable)
    statements = list(_all_statements(tree.body))
    nodes = {}
    derive_stmt = [s for s in tree.body
                   if _span(s)[0] <= derive_line <= _span(s)[1]]
    ran_derive = any(_span(s)[0] <= line <= _span(s)[1]
                     for s in derive_stmt for line in executed_lines)
    if not ran_derive:
        # derive_<id> did not run (compute dispatched elsewhere, or it is
        # not a function): its whole definition is read as written
        for stmt in derive_stmt:
            for node in ast.walk(stmt):
                nodes[id(node)] = node
    for line in executed_lines:
        containing = [s for s in statements
                      if _span(s)[0] <= line <= _span(s)[1]]
        if containing:
            innermost = min(containing,
                            key=lambda s: (_span(s)[1] - _span(s)[0],
                                           -_span(s)[0]))
            for node in _own_nodes(innermost):
                nodes[id(node)] = node
    bindings = {}
    for stmt in tree.body:
        targets = []
        if isinstance(stmt, ast.Assign):
            targets = stmt.targets
        elif isinstance(stmt, (ast.AnnAssign, ast.AugAssign)):
            targets = [stmt.target]
        for target in targets:
            for node in ast.walk(target):
                if isinstance(node, ast.Name):
                    bindings.setdefault(node.id, []).append(stmt)
    read, pending = set(), list(nodes.values())
    while pending:
        node = pending.pop()
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            for bound in bindings.get(node.id, []):
                if id(bound) not in read:
                    read.add(id(bound))
                    for inner in ast.walk(bound):
                        if id(inner) not in nodes:
                            nodes[id(inner)] = inner
                            pending.append(inner)
    return _literals_in_nodes(nodes.values(), source), list(unreadable)


def _folded_string(node):
    """The value of a string literal, or of '+' over string literals;
    None for anything else."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left, right = _folded_string(node.left), _folded_string(node.right)
        if left is not None and right is not None:
            return left + right
    return None


def _literals_in_nodes(nodes, source):
    """(literal text, source text) for each numeric literal among nodes,
    in source order."""
    found, inside_call = [], set()
    nodes = [n for n in nodes if hasattr(n, 'lineno')]
    for node in nodes:
        if (isinstance(node, ast.Call)
                and _called_name(node.func) in DECIMAL_NAMES
                and node.args
                and _folded_string(node.args[0]) is not None):
            found.append(((node.lineno, node.col_offset),
                          _folded_string(node.args[0]),
                          ast.get_source_segment(source, node)))
            inside_call.update(id(n) for n in ast.walk(node.args[0]))
    for node in nodes:
        if (isinstance(node, ast.Constant)
                and isinstance(node.value, (int, float, complex))
                and not isinstance(node.value, bool)
                and id(node) not in inside_call):
            text = ast.get_source_segment(source, node)
            found.append(((node.lineno, node.col_offset), text, text))
    return [(literal, text) for _, literal, text in sorted(found)]


def _called_name(func):
    """The name a call is made through: D(...) -> 'D',
    decimal.Decimal(...) -> 'Decimal'."""
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None
