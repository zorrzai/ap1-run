"""Unit tests for the sealed inputs: read once, the ground-truth module
loaded from the bytes read, and the expected values (R1.1, T3-48, T3-72)."""

import inspect
import json
import linecache
import sys
from decimal import Decimal

import pytest

from ap1_run.execution import sealed_inputs
from ap1_run.execution.sealed_inputs import (
    compute_expected_values, load_ground_truth, read_inputs, sealed_compute,
)

GT_SOURCE = (b'from decimal import Decimal\n'
             b'def compute(item_id, ctx):\n'
             b'    return {"final": Decimal(ctx["acct"]["balance"]),\n'
             b'            "item": item_id, "seen": sorted(ctx)}\n')


@pytest.fixture(autouse=True)
def clean_module(monkeypatch):
    """No ground_truth_example or calculator_tool module or linecache entry
    leaks out."""
    monkeypatch.delitem(sys.modules, 'ground_truth_example', raising=False)
    monkeypatch.delitem(sys.modules, 'calculator_tool', raising=False)
    monkeypatch.setattr(linecache, 'cache', dict(linecache.cache))
    monkeypatch.setattr(sys, 'dont_write_bytecode', False)
    yield
    sys.modules.pop('ground_truth_example', None)
    sys.modules.pop('calculator_tool', None)


CALC_SOURCE = b'def execute_calculator(expression):\n    return "7"\n'


def write_dir(root, fixture=b'{"accounts": []}\n',
              questions=b'{"items": []}\n', gt=GT_SOURCE, calc=CALC_SOURCE):
    root.mkdir(exist_ok=True)
    (root / 'fixture.json').write_bytes(fixture)
    (root / 'questions.json').write_bytes(questions)
    (root / 'ground_truth_example.py').write_bytes(gt)
    (root / 'calculator_tool.py').write_bytes(calc)
    return root


# -- read_inputs ------------------------------------------------------------

def test_read_inputs_paths_bytes_and_parsed_values(tmp_path):
    root = write_dir(tmp_path / 'fx', fixture=b'{"accounts": [1]}\n',
                     questions='{"items": ["é"]}\n'.encode('utf-8'))
    inputs = read_inputs(str(root))
    assert inputs.paths == {
        'fixture': str(root / 'fixture.json'),
        'questions': str(root / 'questions.json'),
        'ground_truth': str(root / 'ground_truth_example.py'),
        'calculator': str(root / 'calculator_tool.py')}
    assert inputs.data == {'fixture': b'{"accounts": [1]}\n',
                           'questions': '{"items": ["é"]}\n'.encode('utf-8'),
                           'ground_truth': GT_SOURCE,
                           'calculator': CALC_SOURCE}
    assert inputs.fixture == {'accounts': [1]}
    assert inputs.questions == {'items': ['é']}
    assert inputs.ground_truth.__file__ == str(root / 'ground_truth_example.py')


def test_read_inputs_json_with_a_byte_order_mark(tmp_path):
    # T3-50: the seal hashes a JSON input without its BOM, so the run
    # reads it too (it was a JSONDecodeError before).
    root = write_dir(tmp_path / 'fx', fixture=b'\xef\xbb\xbf{"a": "\xc3\xa9"}',
                     questions=b'\xef\xbb\xbf{"items": []}')
    inputs = read_inputs(str(root))
    assert inputs.fixture == {'a': 'é'}
    assert inputs.questions == {'items': []}


@pytest.mark.parametrize('data', [b'\xff{}', b'{oops}'])
def test_parse_json_input_refuses_what_is_not_utf8_json(data):
    with pytest.raises(ValueError):
        sealed_inputs.parse_json_input(data)


def test_read_inputs_reads_each_file_once(tmp_path, monkeypatch):
    root = write_dir(tmp_path / 'fx')
    opened = []
    real_open = open

    def recording_open(path, *args, **kwargs):
        opened.append((str(path), args, kwargs))
        return real_open(path, *args, **kwargs)
    monkeypatch.setattr(sealed_inputs, 'open', recording_open, raising=False)
    read_inputs(str(root))
    assert opened == [(str(root / name), ('rb',), {}) for name in
                      ('fixture.json', 'questions.json',
                       'ground_truth_example.py', 'calculator_tool.py')]


# -- load_ground_truth ------------------------------------------------------

def test_load_ground_truth_runs_the_bytes_given(tmp_path):
    path = tmp_path / 'ground_truth_example.py'
    path.write_bytes(b'X = "on disk"\n')
    module = load_ground_truth(path, b'X = "sealed"\n')
    assert module.X == 'sealed'
    assert module.__name__ == 'ground_truth_example'
    assert module.__file__ == str(path)
    assert sys.modules['ground_truth_example'] is module


def test_load_ground_truth_ignores_a_shadowing_package(tmp_path, monkeypatch):
    # T3-72: a package ground_truth_example/ beside the file would win an
    # import; the loader never imports by name.
    (tmp_path / 'ground_truth_example').mkdir()
    (tmp_path / 'ground_truth_example' / '__init__.py').write_text('X = 2\n')
    path = tmp_path / 'ground_truth_example.py'
    path.write_bytes(b'X = 1\n')
    monkeypatch.syspath_prepend(str(tmp_path))
    assert load_ground_truth(path, path.read_bytes()).X == 1


def test_load_ground_truth_writes_no_bytecode(tmp_path):
    path = tmp_path / 'ground_truth_example.py'
    path.write_bytes(b'X = 1\n')
    load_ground_truth(path, b'X = 1\n')
    assert sorted(p.name for p in tmp_path.iterdir()) == [
        'ground_truth_example.py']


def test_load_ground_truth_ignores_a_stale_bytecode_cache(tmp_path):
    import py_compile
    path = tmp_path / 'ground_truth_example.py'
    path.write_bytes(b'X = "compiled"\n')
    py_compile.compile(str(path))
    assert load_ground_truth(path, b'X = "sealed"\n').X == 'sealed'


def test_load_ground_truth_reads_another_file_from_disk(tmp_path):
    # Only the module's own source is replaced.
    path = tmp_path / 'ground_truth_example.py'
    other = tmp_path / 'other.txt'
    other.write_bytes(b'data')
    module = load_ground_truth(path, b'X = 1\n')
    assert module.__loader__.get_data(str(other)) == b'data'
    assert module.__loader__.get_data(str(path)) == b'X = 1\n'


def test_load_ground_truth_source_seen_by_inspect_is_the_sealed_one(
        tmp_path):
    # The R3.1 declared-constants guard reads the source with inspect.
    path = tmp_path / 'ground_truth_example.py'
    path.write_bytes(b'def f():\n    return 1  # on disk\n')
    module = load_ground_truth(
        path, b'\xef\xbb\xbfdef f():\n    return 2  # sealed\n')
    linecache.checkcache(str(path))
    assert inspect.getsource(module.f) == 'def f():\n    return 2  # sealed\n'
    assert module.f() == 2


def test_load_ground_truth_source_with_coding_cookie(tmp_path):
    path = tmp_path / 'ground_truth_example.py'
    data = '# -*- coding: latin-1 -*-\nS = "é"\n'.encode('latin-1')
    module = load_ground_truth(path, data)
    assert module.S == 'é'
    assert linecache.cache[str(path)] == (
        len(data), None, ['# -*- coding: latin-1 -*-\n', 'S = "é"\n'],
        str(path))


def test_load_ground_truth_failure_leaves_no_module(tmp_path):
    path = tmp_path / 'ground_truth_example.py'
    with pytest.raises(ZeroDivisionError):
        load_ground_truth(path, b'X = 1 / 0\n')
    assert 'ground_truth_example' not in sys.modules


def test_load_ground_truth_accepts_a_path_object_or_string(tmp_path):
    path = tmp_path / 'ground_truth_example.py'
    assert load_ground_truth(str(path), b'X = 1\n').__file__ == str(path)


# -- compute_expected_values, sealed_compute ------------------------------

FIXTURE = {'accounts': [{'id': 'acct', 'name': 'A', 'balance': '10.50'},
                        {'id': 'other', 'name': 'B', 'balance': '1'}]}


def test_compute_expected_values_every_item_on_its_context(tmp_path):
    module = load_ground_truth(tmp_path / 'g.py', GT_SOURCE)
    questions = {'items': [{'id': 'Q01', 'source_accounts': ['acct']},
                           {'id': 'Q02',
                            'source_accounts': ['acct', 'other']}]}
    assert compute_expected_values(module, FIXTURE, questions) == {
        'Q01': {'final': Decimal('10.50'), 'item': 'Q01', 'seen': ['acct']},
        'Q02': {'final': Decimal('10.50'), 'item': 'Q02',
                'seen': ['acct', 'other']}}


def test_compute_expected_values_item_without_accounts_gets_empty_context():
    class Module:
        @staticmethod
        def compute(item_id, ctx):
            return {'ctx': dict(ctx)}
    assert compute_expected_values(
        Module, FIXTURE, {'items': [{'id': 'Q01'}]}) == {'Q01': {'ctx': {}}}


def test_compute_expected_values_no_items():
    assert compute_expected_values(None, FIXTURE, {}) == {}


def test_sealed_compute_returns_a_copy_of_the_sealed_value():
    values = {'Q01': {'final': Decimal('1'), 'steps': [{'v': 1}]}}
    compute = sealed_compute(values)
    first = compute('Q01', {'ignored': {}})
    assert first == values['Q01']
    first['steps'][0]['v'] = 99
    assert compute('Q01', {})['steps'][0]['v'] == 1
    with pytest.raises(KeyError):
        compute('Q02', {})


@pytest.mark.finding('T3-72')
@pytest.mark.req('R1.1')
def test_read_inputs_loads_the_calculator_from_the_bytes_read(tmp_path):
    # The calculator that runs is the one read and sealed: import of
    # calculator_tool finds it, not the file as it is later, and not a
    # package calculator_tool/ beside it.
    root = write_dir(tmp_path / 'fx')
    package = root / 'calculator_tool'
    package.mkdir()
    (package / '__init__.py').write_text(
        'def execute_calculator(expression):\n    return "1"\n')
    inputs = read_inputs(str(root))
    (root / 'calculator_tool.py').write_bytes(
        b'def execute_calculator(expression):\n    return "2"\n')
    import calculator_tool
    assert calculator_tool is inputs.calculator
    assert calculator_tool.execute_calculator('x') == '7'


class _Module:
    def __init__(self, compute):
        self.compute = compute


QS = {'items': [{'id': 'Q01', 'source_accounts': []}]}


@pytest.mark.finding('T3-48')
@pytest.mark.req('R3.1')
def test_check_reproducible_compares_snapshots_not_shared_objects():
    # A module that returns the same dict each time and changes it in
    # place gives different results on the two computations; comparing the
    # two references would see one object twice.
    state = {'final': Decimal('1'), 'derivable': True}

    def compute(item_id, ctx):
        state['final'] += 1
        return state
    with pytest.raises(sealed_inputs.GroundTruthNotReproducible,
                       match='Q01'):
        sealed_inputs.check_reproducible(_Module(compute), {'accounts': []},
                                         QS)


@pytest.mark.finding('T3-48')
@pytest.mark.req('R3.1')
def test_check_reproducible_compares_the_whole_result():
    # SPEC R3.1 "intermediates reproducible across two executions": a
    # change in an intermediate alone, the final unchanged, is refused.
    calls = []

    def compute(item_id, ctx):
        calls.append(1)
        return {'final': Decimal('1'), 'intermediates': [
            {'label': 'a', 'value': Decimal(len(calls))}]}
    with pytest.raises(sealed_inputs.GroundTruthNotReproducible):
        sealed_inputs.check_reproducible(_Module(compute), {'accounts': []},
                                         QS)


def test_check_reproducible_returns_a_snapshot():
    # The values sealed are what was computed, not an object the module
    # keeps and may change later.
    state = {'final': Decimal('1')}
    values = sealed_inputs.check_reproducible(
        _Module(lambda i, c: state), {'accounts': []}, QS)
    state['final'] = Decimal('9')
    assert values == {'Q01': {'final': Decimal('1')}}
