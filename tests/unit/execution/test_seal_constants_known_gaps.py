"""Known gaps of the R3.1 declared-constants check (seal_constants.py).

Each test is a ground-truth module of an ordinary shape on which the
check is wrong today, as a strict xfail:

- a bypass: the module's expected value carries the undeclared constant
  1.05 (or 7), and the check lets it through. Correct: refused, naming
  the item and the literal;
- a false refusal: a legitimate module, refused. Correct: it passes.

How the check should close these is an open design question, so the
logic is unchanged and each case stays xfail until it is decided. The
same shapes are listed as known gaps in README.md and in the module's
docstring.
"""

import importlib.util
import sys
import textwrap

import pytest

from ap1_run.execution.seal import (
    SealError, perturbation_check, source_fields_check,
)
from ap1_run.execution.seal_constants import declared_constants_check

FIXTURE = {'accounts': [{'id': 'acct', 'name': 'Savings', 'balance': '100'}]}

HEADER = '''\
from decimal import Decimal as D


def compute(item_id, ctx):
    return globals()['derive_' + item_id.lower()](ctx)


def result(final, *constants):
    return {'final': final, 'intermediates': [
        {'inputs': [{'source': 'acct.balance'}]
         + [{'constant': c} for c in constants]}],
        'source_fields_consumed': ['acct.balance']}
'''


@pytest.fixture
def load(tmp_path, monkeypatch):
    """Write a ground-truth module to tmp_path and import it fresh."""
    counter = iter(range(1000))

    def load(body):
        name = f'_gap_gt_{tmp_path.name}_{next(counter)}'
        path = tmp_path / f'{name}.py'
        path.write_text(HEADER + '\n\n' + textwrap.dedent(body),
                        encoding='utf-8')
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        monkeypatch.setitem(sys.modules, name, module)
        spec.loader.exec_module(module)
        return module
    return load


def questions(*ids):
    return {'items': [{'id': i, 'source_accounts': ['acct']} for i in ids]}


def refused(module, qs, *, run_order=False):
    """The refusal text, or None if the check let the module through.
    run_order: run the other two R3.1 guards first, as run.py does."""
    if run_order:
        perturbation_check(module, FIXTURE, qs)
        source_fields_check(module, FIXTURE, qs)
    try:
        declared_constants_check(module, FIXTURE, qs)
    except SealError as exc:
        return str(exc)
    return None


# -- bypasses: an undeclared constant the check lets through ---------------

BYPASSES = {
    # same line as a compound header, or after a ';'
    'one_line_helper_def': '''
        def rate(): return D("1.05")

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * rate())
    ''',
    'one_line_derive': '''
        def derive_q01(ctx): return result(D(ctx['acct']['balance']) * D("1.05"))
    ''',
    'second_statement_after_semicolon': '''
        def derive_q01(ctx):
            b = D(ctx['acct']['balance']); r = D("1.05")
            return result(b * r)
    ''',
    'statement_after_exempt_zero_on_one_line': '''
        def derive_q01(ctx):
            unused = 0; return result(D(ctx['acct']['balance']) * 7)
    ''',
    'one_line_if_body': '''
        def derive_q01(ctx):
            r = D(ctx['acct']['balance'])
            if r: r = r * D("1.05")
            return result(r)
    ''',
    'one_line_for_body': '''
        def derive_q01(ctx):
            r = D(ctx['acct']['balance'])
            for _ in "x": r = r * D("1.05")
            return result(r)
    ''',
    # module-level values bound other than by a plain top-level assignment
    'constant_assigned_in_module_try': '''
        try:
            RATE = D("1.05")
        except Exception:
            RATE = None

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * RATE)
    ''',
    'constant_assigned_in_module_if': '''
        if True:
            RATE = D("1.05")

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * RATE)
    ''',
    'class_attribute_constant': '''
        class Rates:
            VAT = D("1.05")

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * Rates.VAT)
    ''',
    'constant_computed_by_a_module_function': '''
        def _make_rate():
            return D("1.05")
        RATE = _make_rate()

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * RATE)
    ''',
    'global_set_by_an_init_function': '''
        def _init():
            global RATE
            RATE = D("1.05")
        _init()

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * RATE)
    ''',
    'module_walrus_binding': '''
        (RATE := D("1.05"))

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * RATE)
    ''',
    'module_for_binding': '''
        for RATE in [D("1.05")]:
            pass

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * RATE)
    ''',
    'globals_subscript_lookup': '''
        _RATE = D("1.05")

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * globals()['_RATE'])
    ''',
    # a numeric string that reaches Decimal other than as D("...")
    'numeric_string_in_a_module_name': '''
        RATE = "1.05"

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * D(RATE))
    ''',
    'numeric_string_in_a_local_name': '''
        def derive_q01(ctx):
            r = "1.05"
            return result(D(ctx['acct']['balance']) * D(r))
    ''',
    'aliased_decimal_constructor': '''
        from decimal import Decimal as Money

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * Money("1.05"))
    ''',
    'numeric_string_by_keyword': '''
        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * D(value="1.05"))
    ''',
    'numeric_string_through_str': '''
        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * D(str("1.05")))
    ''',
    # code the trace does not follow
    'helper_run_in_a_thread_pool': '''
        import concurrent.futures

        def rate():
            return D("1.05")

        def derive_q01(ctx):
            with concurrent.futures.ThreadPoolExecutor() as ex:
                r = ex.submit(rate).result()
            return result(D(ctx['acct']['balance']) * r)
    ''',
    'worker_thread': '''
        from threading import Thread

        def worker(ctx, out):
            out.append(D(ctx['acct']['balance']) * 7)

        def derive_q01(ctx):
            out = []
            thread = Thread(target=worker, args=(ctx, out))
            thread.start()
            thread.join()
            return result(out.pop())
    ''',
}

# Cache or memo state: run in run.py's order, the helper is warm by the
# time the constants check runs, so its body never executes under it.
WARM_BYPASSES = {
    'lru_cache_helper_warmed_by_the_earlier_guards': '''
        import functools

        @functools.lru_cache(maxsize=None)
        def rate():
            return D("1.05")

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * rate())
    ''',
    'memo_dict_helper_warmed_by_the_earlier_guards': '''
        _CACHE = {}

        def rate():
            if 'r' not in _CACHE:
                _CACHE['r'] = D("1.05")
            return _CACHE['r']

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * rate())
    ''',
}


@pytest.mark.finding('S3-G3-1')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G3-1: a known gap of the constants check')
@pytest.mark.parametrize('shape', sorted(BYPASSES))
def test_constants_check_refuses_shape(load, shape):
    text = refused(load(BYPASSES[shape]), questions('Q01'))
    assert text is not None and ('Q01: ' in text), text


@pytest.mark.finding('S3-G3-1')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G3-1: a known gap of the constants check')
@pytest.mark.parametrize('shape', sorted(WARM_BYPASSES))
def test_constants_check_refuses_shape_in_run_order(load, shape):
    text = refused(load(WARM_BYPASSES[shape]), questions('Q01'),
                   run_order=True)
    assert text is not None and 'Q01: ' in text, text


@pytest.mark.finding('S3-G3-1')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G3-1: the result depends on the item order')
def test_constants_check_memo_shared_across_items_is_order_independent(load):
    # Q01 declares 1.05; Q02 reuses the memoised 1.05 without declaring it.
    # Q02 is refused only when it runs first: the verdict must not depend
    # on the order of the items.
    body = '''
        _CACHE = {}

        def rate():
            if 'r' not in _CACHE:
                _CACHE['r'] = D("1.05")
            return _CACHE['r']

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * rate(), "1.05")

        def derive_q02(ctx):
            return result(D(ctx['acct']['balance']) * rate())
    '''
    first = refused(load(body), questions('Q01', 'Q02'))
    second = refused(load(body), questions('Q02', 'Q01'))
    assert first is not None and 'Q02: ' in first, (first, second)


@pytest.mark.finding('T3-54')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-54: exec code with a file-like name is read as '
                          'if it had a source file')
def test_constants_check_fails_closed_on_exec_with_a_file_like_name(load):
    # Code compiled under a name that is not a file on disk ("consts.py")
    # has no source the check can read: it must be named unreadable, as
    # code compiled under "<string>" is.
    text = refused(load('''
        def derive_q01(ctx):
            g = {'D': D}
            exec(compile("def r():\\n    return D('1.05')\\n", "consts.py",
                         "exec"), g)
            return result(D(ctx['acct']['balance']) * g['r']())
    '''), questions('Q01'))
    assert text is not None and 'Q01: ' in text, text


# -- false refusals: a legitimate module the check refuses -----------------

LEGITIMATE = {
    'local_name_shadows_a_module_constant': '''
        RATE = 7       # unused by the computation

        def derive_q01(ctx):
            RATE = D(ctx['acct']['balance'])
            return result(RATE)
    ''',
    'compute_slices_the_item_id': '''
        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * D("12"), "12")

        def compute2(item_id, ctx):
            return globals()['derive_q' + item_id[1:]](ctx)
        compute = compute2
    ''',
    'decorator_argument': '''
        import functools

        @functools.lru_cache(maxsize=128)
        def bal(ctx_balance):
            return D(ctx_balance)

        def derive_q01(ctx):
            return result(bal(ctx['acct']['balance']) * D("12"), "12")
    ''',
    'dataclass_with_a_declared_default': '''
        import dataclasses

        @dataclasses.dataclass
        class Months:
            count: D = D("12")

        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * Months().count, "12")
    ''',
    'declared_negative_constant': '''
        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * -1, "-1")
    ''',
    'zero_written_with_decimals': '''
        def derive_q01(ctx):
            b = D(ctx['acct']['balance'])
            return result(max(b, D("0.00")) * D("12"), "12")
    ''',
    'declared_constant_written_with_a_trailing_zero': '''
        def derive_q01(ctx):
            return result(D(ctx['acct']['balance']) * D("12.0"), "12")
    ''',
}


@pytest.mark.finding('S3-G3-1')
@pytest.mark.req('R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G3-1: a known false refusal of the constants '
                          'check')
@pytest.mark.parametrize('shape', sorted(LEGITIMATE))
def test_constants_check_passes_legitimate_shape(load, shape):
    assert refused(load(LEGITIMATE[shape]), questions('Q01')) is None
