"""R1.1 -- the sealed inputs, read once.

A run reads each of its inputs from the fixture directory exactly once:
the bytes it reads are the bytes it seals and the bytes it executes
(T3-72). The ground-truth module is loaded from those bytes, from the file
named ground_truth_example.py itself, never through Python's import path,
where a package directory ground_truth_example/ beside the file would win.

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

# The input files of a fixture directory, by sealed-input name.
INPUT_FILES = {
    'fixture': 'fixture.json',
    'questions': 'questions.json',
    'ground_truth': 'ground_truth_example.py',
}

GROUND_TRUTH_MODULE = 'ground_truth_example'


class SealedInputs:
    """The inputs of one run: for each name in INPUT_FILES, its path and
    the bytes read from it; the parsed fixture and questions; the loaded
    ground-truth module."""

    def __init__(self, paths, data):
        self.paths = paths
        self.data = data
        self.fixture = json.loads(data['fixture'].decode('utf-8'))
        self.questions = json.loads(data['questions'].decode('utf-8'))
        self.ground_truth = load_ground_truth(paths['ground_truth'],
                                              data['ground_truth'])


def read_inputs(fixture_dir):
    """Read the fixture, questions and ground-truth module from
    fixture_dir once, and load them (SealedInputs)."""
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
    `path`, as the module ground_truth_example (in sys.modules, with
    __file__ = path). linecache is primed with the same source, so
    inspect (used by the R3.1 declared-constants guard) reads the source
    that runs, not the file as it is later."""
    path = str(path)
    encoding, _ = tokenize.detect_encoding(io.BytesIO(data).readline)
    lines = data.decode(encoding).splitlines(True)
    # mtime None: linecache.checkcache never discards the entry.
    linecache.cache[path] = (len(data), None, lines, path)
    loader = _SealedSourceLoader(GROUND_TRUTH_MODULE, path, data)
    spec = importlib.util.spec_from_file_location(
        GROUND_TRUTH_MODULE, path, loader=loader)
    module = importlib.util.module_from_spec(spec)
    sys.modules[GROUND_TRUTH_MODULE] = module
    try:
        loader.exec_module(module)
    except BaseException:
        sys.modules.pop(GROUND_TRUTH_MODULE, None)
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


def sealed_compute(expected_values):
    """A compute(item_id, ctx) that returns the sealed expected value of
    the item (a copy, so a caller cannot change the sealed values), in
    place of calling the module again: the run scores against what was
    sealed."""
    def compute(item_id, delivered_context):
        return copy.deepcopy(expected_values[item_id])
    return compute
