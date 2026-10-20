"""Unit tests for the R3.1 declared-constants check (AST): every D("...")
literal in a derive function must be declared as a constant."""

import importlib.util
import json
import sys
import textwrap
from pathlib import Path

import pytest

from ap1_run.execution.seal import SealError
from ap1_run.execution.seal_constants import declared_constants_check

FIXTURE = {'accounts': [
    {'id': 'acct', 'name': 'Savings', 'balance': '100'},
    {'id': 'other', 'name': 'Other', 'balance': '7'},
]}

HEADER = '''\
from decimal import Decimal as D


def compute(item_id, ctx):
    return globals()['derive_' + item_id.lower()](ctx)


def result(final, *constants, **extra):
    out = {'final': final, 'intermediates': [
        {'inputs': [{'source': 'acct.balance'}]
         + [{'constant': c} for c in constants]}]}
    out.update(extra)
    return out
'''


@pytest.fixture
def gt_module(tmp_path, monkeypatch):
    """Write a ground-truth module to tmp_path and import it, so that
    inspect.getsource finds its derive functions."""
    counter = iter(range(1000))

    def load(*bodies):
        name = f'_s3_gt_{tmp_path.name}_{next(counter)}'
        path = tmp_path / f'{name}.py'
        source = '\n\n'.join(textwrap.dedent(b) for b in bodies)
        path.write_text(HEADER + '\n\n' + source, encoding='utf-8')
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        monkeypatch.setitem(sys.modules, name, module)
        spec.loader.exec_module(module)
        return module
    return load


def questions(*ids, accounts=('acct',)):
    return {'items': [{'id': i, 'source_accounts': list(accounts)}
                      for i in ids]}


# -- passing modules -----------------------------------------------------

def test_declared_constants_check_all_declared_returns_empty_list(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) / D("12"), "12")
    ''')
    assert declared_constants_check(mod, FIXTURE, questions('Q01')) == []


def test_declared_constants_check_declared_but_unused_passes(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']), "12", "4")
    ''')
    assert declared_constants_check(mod, FIXTURE, questions('Q01')) == []


def test_declared_constants_check_zero_literal_is_exempt(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return result(max(D("0"), D(ctx['acct']['balance'])))
    ''')
    assert declared_constants_check(mod, FIXTURE, questions('Q01')) == []


def test_declared_constants_check_zero_does_not_end_the_scan(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D("0") + D("4"))
    ''')
    with pytest.raises(SealError, match=r'Q01: D\("4"\)$'):
        declared_constants_check(mod, FIXTURE, questions('Q01'))


def test_declared_constants_check_no_items_returns_empty_list(gt_module):
    mod = gt_module('')
    assert declared_constants_check(mod, FIXTURE, {}) == []
    assert declared_constants_check(mod, FIXTURE, {'items': []}) == []


def test_declared_constants_check_non_literal_d_argument_ignored(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            rate = ctx['acct']['balance']
            return result(D(rate) + D())
    ''')
    assert declared_constants_check(mod, FIXTURE, questions('Q01')) == []


# -- refusals ------------------------------------------------------------

def test_declared_constants_check_undeclared_literal_raises(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) / D("4"), "12")
    ''')
    with pytest.raises(SealError) as exc:
        declared_constants_check(mod, FIXTURE, questions('Q01'))
    assert str(exc.value) == (
        'declared-constants check failed: undeclared numeric literals. '
        'Q01: D("4")')


def test_declared_constants_check_names_every_undeclared_literal(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D("4") * D("3"))

        def derive_q02(ctx):
            return result(D("5"))
    ''')
    with pytest.raises(SealError) as exc:
        declared_constants_check(mod, FIXTURE, questions('Q01', 'Q02'))
    assert str(exc.value).endswith(
        'literals. Q01: D("4"); Q01: D("3"); Q02: D("5")')


def test_declared_constants_check_constants_are_per_item(gt_module):
    # A constant declared by Q01 does not cover the same literal in Q02.
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D("12"), "12")

        def derive_q02(ctx):
            return result(D("12"))
    ''')
    with pytest.raises(SealError, match=r'literals\. Q02: D\("12"\)$'):
        declared_constants_check(mod, FIXTURE, questions('Q01', 'Q02'))


def test_declared_constants_check_comparison_is_by_text(gt_module):
    # D("12.0") is not covered by a declared "12": the literal and the
    # declaration are compared as strings, not as numbers (fails closed).
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D("12.0"), "12")
    ''')
    with pytest.raises(SealError, match=r'Q01: D\("12\.0"\)'):
        declared_constants_check(mod, FIXTURE, questions('Q01'))


def test_declared_constants_check_inputs_without_constant_key_ignored(gt_module):
    # 'source' inputs declare nothing, so the "100" here is undeclared.
    mod = gt_module('''
        def derive_q01(ctx):
            return {'final': D("100"), 'intermediates': [
                {'inputs': [{'source': '100'}, {'value': '100'}]}, {}]}
    ''')
    with pytest.raises(SealError, match=r'Q01: D\("100"\)'):
        declared_constants_check(mod, FIXTURE, questions('Q01'))


def test_declared_constants_check_no_intermediates_declares_nothing(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return {'final': D("2")}
    ''')
    with pytest.raises(SealError, match=r'Q01: D\("2"\)'):
        declared_constants_check(mod, FIXTURE, questions('Q01'))


def test_declared_constants_check_derivable_missing_counts_as_true(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D("9"))
    ''')
    with pytest.raises(SealError):
        declared_constants_check(mod, FIXTURE, questions('Q01'))


def test_declared_constants_check_derive_name_is_lowercased_item_id(gt_module):
    mod = gt_module('''
        def derive_ab_7(ctx):
            return result(D("9"))
    ''')
    with pytest.raises(SealError, match=r'AB_7: D\("9"\)'):
        declared_constants_check(mod, FIXTURE, questions('AB_7'))


# -- the context given to compute -----------------------------------------

def test_declared_constants_check_compute_sees_only_source_accounts(gt_module):
    mod = gt_module('''
        SEEN = []

        def derive_q01(ctx):
            SEEN.append(ctx)
            return result(D("1"), "1")
    ''')
    declared_constants_check(mod, FIXTURE, questions('Q01', accounts=['other']))
    assert mod.SEEN == [{'other': {'balance': '7'}}]


def test_declared_constants_check_item_without_source_accounts_empty_ctx(gt_module):
    mod = gt_module('''
        SEEN = []

        def derive_q01(ctx):
            SEEN.append(ctx)
            return result(D("1"))
    ''')
    with pytest.raises(SealError):
        declared_constants_check(mod, FIXTURE, {'items': [{'id': 'Q01'}]})
    assert mod.SEEN == [{}]


# -- skips (fail open, T3-54) ---------------------------------------------
# Each skip is followed by a failing item, so that a skip which stopped the
# loop (break for continue) would be noticed.

FAILING_Q09 = '''
    def derive_q09(ctx):
        return result(D("9"))
'''


def assert_only_q09_fails(mod, *ids):
    with pytest.raises(SealError) as exc:
        declared_constants_check(mod, FIXTURE, questions(*ids, 'Q09'))
    assert str(exc.value).endswith('literals. Q09: D("9")')


def test_declared_constants_check_not_derivable_item_skipped(gt_module):
    mod = gt_module('''
        def derive_q01(ctx):
            return result(D("4"), derivable=False)
    ''', FAILING_Q09)
    assert_only_q09_fails(mod, 'Q01')


@pytest.mark.finding('T3-54')
def test_declared_constants_check_compute_raises_item_skipped(gt_module):
    # Current behaviour: an item whose compute raises is skipped with no
    # failure recorded. Correct: refuse (fail closed), naming the item.
    mod = gt_module('''
        def derive_q01(ctx):
            D("4")
            raise ValueError('boom')
    ''', FAILING_Q09)
    assert_only_q09_fails(mod, 'Q01')


@pytest.mark.finding('T3-54')
def test_declared_constants_check_no_derive_function_item_skipped(gt_module):
    # Current behaviour: compute() works but there is no derive_<id>, so the
    # literals are never inspected. Correct: refuse, or inspect compute's
    # call graph.
    mod = gt_module('''
        def compute(item_id, ctx):
            if item_id == 'Q01':
                return result(D("4"))
            return derive_q09(ctx)
    ''', FAILING_Q09)
    assert_only_q09_fails(mod, 'Q01')


@pytest.mark.finding('T3-54')
def test_declared_constants_check_source_unavailable_item_skipped(gt_module):
    # Current behaviour: a derive function whose source cannot be read
    # (a builtin: TypeError; code made by exec: OSError) is skipped.
    # Correct: refuse, since the literals cannot be checked.
    mod = gt_module('''
        exec("def derive_q02(ctx):\\n    return result(D('4'))\\n")

        def compute(item_id, ctx):
            if item_id == 'Q09':
                return derive_q09(ctx)
            return result(D("4"))
    ''', FAILING_Q09)
    mod.derive_q01 = len
    assert_only_q09_fails(mod, 'Q01', 'Q02')


@pytest.mark.finding('T3-54')
def test_declared_constants_check_indented_source_item_skipped(gt_module):
    # Current behaviour: a derive function defined inside a class (or
    # nested) has indented source, ast.parse raises IndentationError and
    # the item is skipped. Correct: dedent before parsing, or refuse.
    mod = gt_module('''
        class Holder:
            @staticmethod
            def derive_q01(ctx):
                return result(D("4"))

        derive_q01 = Holder.derive_q01
    ''', FAILING_Q09)
    assert_only_q09_fails(mod, 'Q01')


@pytest.mark.finding('S3-G3-1')
def test_declared_constants_check_only_sees_string_d_calls(gt_module):
    # Current behaviour: only D("<str>") is inspected, although the module
    # docstring promises "every numeric literal". D(4), Decimal("4"), a bare
    # 4 and a literal in a helper the derive function calls all pass
    # undeclared. Correct: every numeric literal reachable from the derive
    # function is checked.
    mod = gt_module('''
        from decimal import Decimal

        def helper(x):
            return x * D("6")

        def derive_q01(ctx):
            b = D(ctx['acct']['balance'])
            return result(helper(b) / D(4) / Decimal("5") / 7)
    ''')
    assert declared_constants_check(mod, FIXTURE, questions('Q01')) == []


# -- the shipped example module --------------------------------------------
# Never called on a live run (T3-7); the only check that the example
# module declares its constants (it declares 4 for Q07 without using it).

def test_declared_constants_check_passes_example_module():
    example = Path(__file__).resolve().parents[3] / 'example'
    spec = importlib.util.spec_from_file_location(
        '_s3_g3_ground_truth_example_c', example / 'ground_truth_example.py')
    gt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gt)
    load = lambda name: json.loads(  # noqa: E731
        (example / name).read_text(encoding='utf-8'))
    assert declared_constants_check(
        gt, load('fixture.json'), load('questions.json')) == []


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g3-seal-guards; see inbox/2026-10-20_step4-g3-seal-guards-report.md.
# The D("0") exemption (also listed under T3-54) has no test here: whether
# 0 is a structural constant is the STRUCTURAL_CONSTANTS question awaiting
# Marcus (step-4 protocol, rule 6).

def refusal_of(mod, qs):
    """The SealError message, or None if the check passed. (Not
    pytest.raises, whose DID NOT RAISE is not an AssertionError.)"""
    try:
        declared_constants_check(mod, FIXTURE, qs)
    except SealError as exc:
        return str(exc)
    return None


@pytest.mark.finding('T3-54')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-54: compute raising skips the item silently')
def test_declared_constants_check_compute_raises_refused_naming_item(
        gt_module):
    # Correct (T3-54; SPEC R3.1, the E3 check fails closed): an item whose
    # literals cannot be checked because compute raises is a recorded
    # failure naming the item, not a silent skip.
    mod = gt_module('''
        def derive_q01(ctx):
            D("4")
            raise ValueError('boom')
    ''')
    msg = refusal_of(mod, questions('Q01'))
    assert msg is not None, 'compute raising passed the check'
    assert 'Q01' in msg


@pytest.mark.finding('T3-54')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-54: no derive_<id> function skips the item '
                          'silently')
def test_declared_constants_check_no_derive_function_refused_naming_item(
        gt_module):
    # Correct: a derivable item with no derive_<id> to inspect is a
    # recorded failure naming the item (or its literals are found some
    # other way: either way the undeclared D("4") does not pass).
    mod = gt_module('''
        def compute(item_id, ctx):
            return result(D("4"))
    ''')
    msg = refusal_of(mod, questions('Q01'))
    assert msg is not None, 'item with no derive function passed'
    assert 'Q01' in msg


@pytest.mark.finding('T3-54')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-54: unreadable derive source skips the item '
                          'silently')
def test_declared_constants_check_source_unavailable_refused_naming_items(
        gt_module):
    # Correct: a derive function whose source cannot be read (a builtin:
    # TypeError; code made by exec: OSError) cannot be checked, so each
    # such item is a recorded failure, named.
    mod = gt_module('''
        exec("def derive_q02(ctx):\\n    return result(D('4'))\\n")

        def compute(item_id, ctx):
            return result(D("4"))
    ''')
    mod.derive_q01 = len
    msg = refusal_of(mod, questions('Q01', 'Q02'))
    assert msg is not None, 'unreadable derive functions passed'
    assert 'Q01' in msg and 'Q02' in msg


@pytest.mark.finding('T3-54')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-54: indented derive source fails to parse and '
                          'the item is skipped silently')
def test_declared_constants_check_indented_source_checked(gt_module):
    # Correct: a derive function defined in a class or nested has indented
    # source; it is dedented and checked (or refused). Either way the
    # undeclared D("4") does not pass. Today ast.parse raises
    # IndentationError, which is swallowed.
    mod = gt_module('''
        class Holder:
            @staticmethod
            def derive_q01(ctx):
                return result(D("4"))

        derive_q01 = Holder.derive_q01
    ''')
    msg = refusal_of(mod, questions('Q01'))
    assert msg is not None, 'indented derive function passed'
    assert 'Q01' in msg


@pytest.mark.finding('S3-G3-1')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G3-1: only D("<str>") calls are inspected')
@pytest.mark.parametrize('body', [
    '''
    def derive_q01(ctx):
        return result(D(ctx['acct']['balance']) / D(4))
    ''',
    '''
    from decimal import Decimal

    def derive_q01(ctx):
        return result(D(ctx['acct']['balance']) / Decimal("4"))
    ''',
    '''
    def derive_q01(ctx):
        return result(D(ctx['acct']['balance']) / 4)
    ''',
    '''
    def helper(x):
        return x / D("4")

    def derive_q01(ctx):
        return result(helper(D(ctx['acct']['balance'])))
    ''',
], ids=['D-int', 'Decimal-str', 'bare-int', 'in-helper'])
def test_declared_constants_check_any_undeclared_numeric_literal_refused(
        gt_module, body):
    # Correct (the module's own docstring: "every numeric literal in a
    # derive function's body is a member of the declared constants set";
    # SPEC R3.1, the E3 defect): an undeclared 4 is refused whatever its
    # spelling, and also when it sits in a helper the derive function
    # calls. Today only D("<string>") calls in the derive function's own
    # source are seen.
    mod = gt_module(body)
    msg = refusal_of(mod, questions('Q01'))
    assert msg is not None, 'undeclared literal 4 passed'
    assert 'Q01' in msg and '4' in msg
