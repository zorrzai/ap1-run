"""R1.1 -- the sealed inputs, read once.

A run reads each of its inputs from the fixture directory exactly once:
the bytes it reads are the bytes it seals and the bytes it executes
(T3-72). The ground-truth module and the calculator tool are loaded from
those bytes, from the files named ground_truth_example.py and
calculator_tool.py themselves, never through Python's import path, where a
package directory of the same name beside the file would win. The
calculator produces every tool result the model sees, so it is sealed as
an executed input like the ground truth.

The expected values are what the ground-truth module returns for each
item. They are computed once, before the seal, sealed (T3-48), and the
run scores against that sealed copy.
"""

import copy
import importlib.machinery
import importlib.util
import io
import json
import linecache
import os
import sys
import tokenize

from ap1_run.execution.context import build_delivered_context
from ap1_run.execution.seal import SealError

# The input files of a fixture directory, by sealed-input name.
INPUT_FILES = {
    'fixture': 'fixture.json',
    'questions': 'questions.json',
    'ground_truth': 'ground_truth_example.py',
    'calculator': 'calculator_tool.py',
}

GROUND_TRUTH_MODULE = 'ground_truth_example'
CALCULATOR_MODULE = 'calculator_tool'


class SealedInputs:
    """The inputs of one run: for each name in INPUT_FILES, its path and
    the bytes read from it; the parsed fixture and questions; the loaded
    ground-truth and calculator modules."""

    def __init__(self, paths, data):
        self.paths = paths
        self.data = data
        self.fixture = parse_json_input(data['fixture'])
        self.questions = parse_json_input(data['questions'])
        self.ground_truth = load_ground_truth(paths['ground_truth'],
                                              data['ground_truth'])
        self.calculator = load_sealed_module(
            CALCULATOR_MODULE, paths['calculator'], data['calculator'])


def parse_json_input(data):
    """A JSON input from its bytes: UTF-8, a leading byte-order mark
    allowed, as the seal hashes it without one (T3-50)."""
    return json.loads(data.decode('utf-8-sig'))


def read_inputs(fixture_dir):
    """Read the fixture, questions, ground-truth module and calculator
    from fixture_dir once, and load them (SealedInputs)."""
    paths = {name: os.path.join(fixture_dir, filename)
             for name, filename in INPUT_FILES.items()}
    data = {}
    for name, path in paths.items():
        with open(path, 'rb') as f:
            data[name] = f.read()
    return SealedInputs(paths, data)


class _SealedSourceLoader(importlib.machinery.SourceFileLoader):
    """Loads a module from source bytes already read, not from the file:
    no second read, and no bytecode cache read or written."""

    def __init__(self, fullname, path, data):
        super().__init__(fullname, path)
        self._data = data

    def get_data(self, path):
        if path == self.path:
            return self._data
        return super().get_data(path)

    def path_stats(self, path):
        # No source stats: the bytecode cache is neither used nor written.
        raise OSError('sealed source has no file stats')


def load_ground_truth(path, data):
    """Load the ground-truth module from `data`, the bytes read from
    `path`, as the module ground_truth_example (load_sealed_module)."""
    return load_sealed_module(GROUND_TRUTH_MODULE, path, data)


def load_sealed_module(name, path, data):
    """Load a module from `data`, the bytes read from `path`, as module
    `name` (in sys.modules, with __file__ = path), so an import of the
    name finds it. linecache is primed with the same source, so inspect
    (used by the R3.1 declared-constants guard) reads the source that
    runs, not the file as it is later."""
    path = str(path)
    encoding, _ = tokenize.detect_encoding(io.BytesIO(data).readline)
    lines = data.decode(encoding).splitlines(True)
    # mtime None: linecache.checkcache never discards the entry.
    linecache.cache[path] = (len(data), None, lines, path)
    loader = _SealedSourceLoader(name, path, data)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        loader.exec_module(module)
    except BaseException:
        sys.modules.pop(name, None)
        raise
    return module


def compute_expected_values(ground_truth_module, fixture, questions):
    """{item_id: result} of the ground-truth module for every item of the
    question set, each on the item's delivered context: the expected
    values the seal binds (R1.1, T3-48)."""
    return {
        item['id']: ground_truth_module.compute(
            item['id'],
            build_delivered_context(fixture, item.get('source_accounts', [])))
        for item in questions.get('items', [])}


class GroundTruthNotReproducible(SealError):
    """The ground-truth module gave different results for the same item
    and context (SPEC R3.1, T3-48)."""


def check_reproducible(ground_truth_module, fixture, questions):
    """The expected values, computed twice on the same delivered contexts;
    GroundTruthNotReproducible, naming the items, if any result differs
    between the two computations (SPEC R3.1 "reproducible across two
    executions"). Called before the seal and before any request."""
    first = compute_expected_values(ground_truth_module, fixture, questions)
    second = compute_expected_values(ground_truth_module, fixture, questions)

    def text(result):
        return json.dumps(result, default=str, sort_keys=True)
    changed = [item_id for item_id in first
               if text(first[item_id]) != text(second.get(item_id))]
    if changed:
        raise GroundTruthNotReproducible(
            'ground truth not reproducible (R3.1): the module gave a '
            'different result when computed again on the same context for '
            + ', '.join(changed))
    return first


def sealed_compute(expected_values):
    """A compute(item_id, ctx) that returns the sealed expected value of
    the item (a copy, so a caller cannot change the sealed values), in
    place of calling the module again: the run scores against what was
    sealed."""
    def compute(item_id, delivered_context):
        return copy.deepcopy(expected_values[item_id])
    return compute
