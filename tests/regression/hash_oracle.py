"""Hash oracle: recompute the seal a regression run made, independently.

The golden files cannot pin seal_hash, config_hash or runner_source_hash
(the config covers the mock's port; the source hash changes whenever a
file moves), so normalisation replaces them by placeholders. Before it
does, this module recomputes every value in the seal record from the
inputs the run actually used, and fails if any differs. A change in how
the runner computes a hash then fails the run, also under --update.

It is standard library only, and imports nothing from the runner (not
numeric, seal, version or tools/): an oracle that called the code under
test would agree with it whatever it did. The rules below are written out
from the contract (SPEC R0.4.3 and R1.1, as implemented at the time of
writing):

  canonical JSON   json.dumps(sort_keys=True, separators=(',', ':'),
                   ensure_ascii=False), Decimal as its exact string,
                   no float anywhere, string keys only; UTF-8; SHA-256 hex
  text inputs      fixture, questions and ground-truth module: SHA-256 of
                   the bytes with a leading UTF-8 byte-order mark dropped
                   and CRLF and CR made LF (T3-50); the bytes the run
                   passes to the seal as `loaded` must be the files' bytes
  AP-1 text        SHA-256 of the raw bytes, required, and equal to the
                   config's declared ap1_text_hash (T3-68)
  config_hash      canonical hash of the resolved config, as passed to the
                   seal function (captured by driver.py before the call)
  expected_values_hash
                   canonical hash of {item: final} of the expected values
                   passed to the seal ('' if none; None for a result
                   without a final); the values themselves are pinned by
                   the goldens, which print this hash (T3-48)
  environment      python_version, platform and package_versions of this
                   interpreter (the driver runs on the same one), outside
                   runner_source_hash (T3-30, T3-70)
  seal_hash        canonical hash of every field but 'seal_hash' itself,
                   the timestamp included (seal_format 2; T3-47)
  runner_source_hash
                   SHA-256 over the runner's code: every .py file under
                   src/ap1_run/ outside a __pycache__ directory, and the
                   VERSION file if it is a file (T3-70); sorted by
                   relative path with '/' separators; for each, that
                   path, NUL, the bytes, NUL

There are two source-hash rules. source_hash_files() is the rule above,
the runner's since T3-70; check_source_files.py lists the tracked files it
finds, so a change to the set shows as a reviewed diff of that list, and
every scenario checks the hash under it. source_hash_files_september() is
the rule before T3-70: every .py file of the clone (tests, an in-tree venv
and scratch files included) less a prefix match on 'output',
'review_output' and '__pycache__', sorted in the platform's own form;
VERSION not hashed. No run is sealed under it any more. It is kept only
so that selftest.py can recompute the September runs' published hash
(da0739eb..., docs/REPRODUCING.md) from the tag e7-quantise-fix, which
shows those seals can still be reproduced. That tree is nearly flat (no
tests/ or src/), so the tag check pins how files are read, framed and
sorted under the old rule; the file list pins which files the current
rule takes in.

Version fields: the tag and commit are read from the tree's VERSION file
here, independently (first line that is not blank or a comment; 'unknown'
when the file or a field is missing), and must equal the config's and the
record's. Git can only set runner_modified, which is not checked.

Expected values are frozen before the runner starts: hard_checks
.before_run() records the source hash of the tree the runner runs from
(the repository itself for a real-tree scenario, the scratch copy
otherwise; run_regression passes the same tree to before_run() and
check()) and the start time, so source the run changes or removes, or a
timestamp from outside the run, fails.

Entry point: check_seals(), called by hard_checks.check() from
run_regression.collect() before normalisation.
"""

import hashlib
import importlib.metadata
import json
import os
import platform
import re
import sys
from datetime import datetime, timedelta
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))

# Runner modules this process must never import.
_FORBIDDEN_MODULES = ('ap1_run', 'numeric', 'seal', 'version', 'smoke_test',
                      'verify_run_seal', 'generate_findings', 'tools')

# What runner_source_hash covers (T3-70): the ap1_run package's .py files
# and VERSION. Tests, tools/, examples and anything else in the clone (an
# in-tree venv, scratch files) are outside it.
SOURCE_PACKAGE = 'src/ap1_run/'
SOURCE_VERSION_FILE = 'VERSION'

# The rule before T3-70, for source_hash_files_september() only.
SEPTEMBER_SOURCE_HASH_EXCLUDED = ('output', 'review_output', '__pycache__')

_HEX64 = re.compile(r'\A[0-9a-f]{64}\Z')
_TIMESTAMP = re.compile(
    r'\A\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?\+00:00\Z')

# The seal timestamp must fall within the run, give or take this much.
CLOCK_TOLERANCE_S = 5

# What the runner seals, relative to its base directory. A scenario that
# points the runner elsewhere states its own in "seal_paths".
SEAL_PATHS = {
    'fixture_path': 'example/fixture.json',
    'questions_path': 'example/questions.json',
    'ground_truth_path': 'example/ground_truth_example.py',
    'calculator_path': 'example/calculator_tool.py',
    'ap1_text_path': 'reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md',
}

# Outputs that carry the seal, written by a run that seals and finishes.
# A scenario whose run stops early states its own in "sealed_outputs".
SEALED_OUTPUTS = ('report.md', 'smoke_run.jsonl', 'smoke_summary.json')

# The keys of a seal record, and nothing else (seal_format 2).
SEAL_FORMAT = '2'
SEAL_KEYS = frozenset({
    'seal_format', 'timestamp', 'fixture_hash', 'questions_hash',
    'ground_truth_hash', 'calculator_hash', 'expected_values_hash',
    'config_hash', 'ap1_version', 'ap1_version_doi', 'ap1_text_hash',
    'runner_version_tag',
    'runner_version_commit', 'runner_source_hash', 'python_version',
    'platform', 'package_versions', 'verification_keys', 'ev3_implemented',
    'seal_hash'})

# The packages whose versions a record names, in this order.
RECORDED_PACKAGES = ('ap1-run', 'requests')

# The text inputs a run may pass to the seal as bytes, by name.
TEXT_INPUTS = {'fixture': 'fixture_path', 'questions': 'questions_path',
               'ground_truth': 'ground_truth_path',
               'calculator': 'calculator_path'}


class HashCheckError(Exception):
    """A recomputed hash, or the seal record's shape, does not match."""


# -- independence ----------------------------------------------------

def check_independent():
    """Fail if any runner module has been imported into this process."""
    found = []
    tests_dir = os.path.join(os.path.realpath(REPO), 'tests') + os.sep
    repo_dir = os.path.realpath(REPO) + os.sep
    for name, module in list(sys.modules.items()):
        if name.split('.')[0] in _FORBIDDEN_MODULES:
            found.append(name)
            continue
        path = getattr(module, '__file__', None)
        if path:
            real = os.path.realpath(path)
            parts = real[len(repo_dir):].split(os.sep)
            # A virtual environment inside the clone is not the runner.
            if (real.startswith(repo_dir) and not real.startswith(tests_dir)
                    and not any(p.startswith('.') or p == 'site-packages'
                                for p in parts[:-1])):
                found.append(f'{name} ({real})')
    if found:
        raise HashCheckError(
            'hash oracle is not independent: runner modules imported into '
            'the harness process: ' + ', '.join(sorted(found)))


# -- the rules -------------------------------------------------------

def _exact_decimal(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise HashCheckError(
        f'canonical JSON: unsupported type {type(obj).__name__}')


def canonical_refusal(obj, path='$'):
    """Why canonical JSON refuses obj (a float, or a key that is not a
    string, anywhere in it), or None."""
    if isinstance(obj, float):
        return f'float at {path}'
    if isinstance(obj, dict):
        for k, v in obj.items():
            if not isinstance(k, str):
                return f'{type(k).__name__} key {k!r} at {path}'
            found = canonical_refusal(v, f'{path}.{k}')
            if found:
                return found
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            found = canonical_refusal(v, f'{path}[{i}]')
            if found:
                return found
    return None


def canonical_json(obj):
    refused = canonical_refusal(obj)
    if refused:
        raise HashCheckError(f'canonical JSON: {refused}')
    return json.dumps(obj, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, default=_exact_decimal)


def canonical_hash(obj):
    return hashlib.sha256(canonical_json(obj).encode('utf-8')).hexdigest()


def file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def text_hash(data):
    if data[:3] == b'\xef\xbb\xbf':
        data = data[3:]
    return hashlib.sha256(
        data.replace(b'\r\n', b'\n').replace(b'\r', b'\n')).hexdigest()


def environment():
    """The environment fields of a record made by this interpreter."""
    packages = []
    for name in RECORDED_PACKAGES:
        try:
            packages.append(f'{name} {importlib.metadata.version(name)}')
        except importlib.metadata.PackageNotFoundError:
            packages.append(f'{name} not installed')
    return {
        'python_version': (f'{platform.python_implementation()} '
                           f'{platform.python_version()}'),
        'platform': platform.platform(),
        'package_versions': ', '.join(packages),
    }


def source_hash_covers(rel):
    """Whether runner_source_hash covers the file at rel, a path relative
    to the base directory with '/' separators."""
    if rel == SOURCE_VERSION_FILE:
        return True
    return (rel.startswith(SOURCE_PACKAGE) and rel.endswith('.py')
            and '__pycache__' not in rel.split('/'))


def source_hash_files(base_dir):
    """Relative paths ('/' separators, sorted) the source hash covers:
    every file under base_dir the rule takes in."""
    found = []
    for root, _dirs, files in os.walk(base_dir):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), base_dir)
            rel = rel.replace(os.sep, '/')
            if source_hash_covers(rel):
                found.append(rel)
    return sorted(found)


def source_hash_files_september(base_dir):
    """The pre-T3-70 rule, kept only to show that the September runs'
    published runner_source_hash (da0739eb..., docs/REPRODUCING.md) can
    still be recomputed from the tag e7-quantise-fix (selftest.py,
    PublishedSourceHash). Nothing else uses it.

    Relative paths ('/' separators) of every .py file under base_dir whose
    relative path does not start with 'output', 'review_output' or
    '__pycache__', in the order the September runner hashed them: sorted
    in the platform's own path form."""
    found = []
    for root, _dirs, files in os.walk(base_dir):
        for f in files:
            if not f.endswith('.py'):
                continue
            rel = os.path.relpath(os.path.join(root, f), base_dir)
            if rel.startswith(SEPTEMBER_SOURCE_HASH_EXCLUDED):
                continue
            found.append(rel)
    return [rel.replace(os.sep, '/') for rel in sorted(found)]


def source_hash_over(base_dir, rels):
    """SHA-256 over the files rels ('/' separators) under base_dir, in the
    order given: for each, the path, NUL, the bytes, NUL."""
    h = hashlib.sha256()
    for rel in rels:
        h.update(rel.encode('utf-8'))
        h.update(b'\x00')
        with open(os.path.join(base_dir, rel), 'rb') as f:
            h.update(f.read())
        h.update(b'\x00')
    return h.hexdigest()


def runner_source_hash(base_dir):
    """runner_source_hash under the current rule (source_hash_files())."""
    return source_hash_over(base_dir, source_hash_files(base_dir))


def runner_source_hash_september(base_dir):
    """runner_source_hash under the pre-T3-70 rule
    (source_hash_files_september()), for the published-hash check only."""
    return source_hash_over(base_dir, source_hash_files_september(base_dir))


def version_file_fields(base_dir):
    """(tag, commit) from base_dir/VERSION: the first line that is not
    blank or a comment, split on whitespace; 'unknown' for what is
    missing."""
    tag = commit = 'unknown'
    path = os.path.join(base_dir, 'VERSION')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    tag = parts[0]
                    commit = parts[1] if len(parts) > 1 else 'unknown'
                    break
    return tag, commit


# -- the driver's capture --------------------------------------------

def from_snapshot(node):
    """Rebuild a value from driver.snapshot()'s typed form."""
    kind = node[0]
    if kind in ('str', 'int', 'bool', 'none'):
        return node[1]
    if kind == 'decimal':
        return Decimal(node[1])
    if kind == 'bytes':
        return bytes.fromhex(node[1])
    if kind == 'float':
        return float(node[1])
    if kind == 'list':
        return [from_snapshot(v) for v in node[1]]
    if kind == 'dict':
        return {from_snapshot(k): from_snapshot(v) for k, v in node[1]}
    raise HashCheckError(f'seal input of unsupported type {node[1]}: '
                         f'{node[2]}')


def _strict_equal(a, b):
    """Equal values of the same types (True is not 1)."""
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(
            _strict_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(
            _strict_equal(x, y) for x, y in zip(a, b))
    return a == b


# -- the check -------------------------------------------------------

def _path(cwd, p):
    return p if os.path.isabs(p) else os.path.join(cwd, p)


def _kwargs(inputs):
    return {k: from_snapshot(v) for k, v in inputs['kwargs'].items()}


def check_inputs(inputs, tree, scenario, source_hash):
    """What one seal call was given, checked before its outcome: each
    path is the file of its role, and the source hash is the one frozen
    before the run."""
    problems = []
    kw = _kwargs(inputs)
    want_paths = dict(SEAL_PATHS, **scenario.get('seal_paths', {}))
    for key, rel in sorted(want_paths.items()):
        got = kw.get(key)
        want = os.path.join(tree, *rel.split('/'))
        if not isinstance(got, str) or os.path.realpath(
                _path(inputs['cwd'], got)) != os.path.realpath(want):
            problems.append(f'{key}: the seal was given {got!r}, expected '
                            f'{rel}')
    if kw.get('runner_source_hash') != source_hash:
        problems.append(
            f'runner_source_hash: passed to the seal '
            f'{kw.get("runner_source_hash")!r}, recomputed {source_hash!r}')
    return problems


# The exception the runner raises for each kind of refusal.
_REFUSAL_ERRORS = {'float': 'TypeError', 'ap1': 'SealError'}


def expected_outcome(inputs, tree):
    """What the contract says one seal call gives.

    Returns (record without timestamp and seal_hash, None, None) for a call
    that seals, or (None, reason, expected exception name or None) for a
    call that must be refused."""
    kw = _kwargs(inputs)
    cwd = inputs['cwd']
    config = kw['config']
    refused = canonical_refusal(config)
    if refused:
        kind = 'float' if refused.startswith('float') else None
        return None, f'resolved config: {refused}', _REFUSAL_ERRORS.get(kind)

    declared = config.get('ap1_text_hash')
    if not declared or declared == 'placeholder':
        return (None, f'AP-1 text hash declared as {declared!r}',
                _REFUSAL_ERRORS['ap1'])
    ap1_text_path = kw.get('ap1_text_path')
    if not ap1_text_path:
        return None, 'no AP-1 text given', _REFUSAL_ERRORS['ap1']
    p = _path(cwd, ap1_text_path)
    if not os.path.exists(p):
        return (None, f'AP-1 text file not found: {ap1_text_path}',
                _REFUSAL_ERRORS['ap1'])
    ap1_text_hash = file_hash(p)
    if declared != ap1_text_hash:
        return None, 'AP-1 text hash mismatch', _REFUSAL_ERRORS['ap1']

    hashes = {}
    for name, key in TEXT_INPUTS.items():
        with open(_path(cwd, kw[key]), 'rb') as f:
            hashes[name] = text_hash(f.read())
    expected_values = kw.get('expected_values')
    tag, commit = version_file_fields(tree)
    record = {
        'seal_format': SEAL_FORMAT,
        'fixture_hash': hashes['fixture'],
        'questions_hash': hashes['questions'],
        'ground_truth_hash': hashes['ground_truth'],
        'calculator_hash': hashes['calculator'],
        'expected_values_hash': ('' if expected_values is None
                                 else canonical_hash({
                                     k: (v.get('final') if isinstance(v, dict)
                                         else v)
                                     for k, v in expected_values.items()})),
        'config_hash': canonical_hash(config),
        'ap1_version': config.get('ap1_version', ''),
        'ap1_version_doi': config.get('ap1_version_doi', ''),
        'ap1_text_hash': ap1_text_hash,
        'runner_version_tag': tag,
        'runner_version_commit': commit,
        'runner_source_hash': kw.get('runner_source_hash') or '',
        **environment(),
        'verification_keys': kw.get('verification_keys') or [],
        'ev3_implemented': False,
    }
    return record, None, None


def check_loaded(inputs):
    """The bytes the run passed to the seal as `loaded` (what it executes,
    T3-72) are the bytes of the files at the sealed paths."""
    kw = _kwargs(inputs)
    problems = []
    for name, data in sorted((kw.get('loaded') or {}).items()):
        key = TEXT_INPUTS.get(name)
        if key is None:
            problems.append(f'loaded: unexpected input {name!r}')
            continue
        with open(_path(inputs['cwd'], kw[key]), 'rb') as f:
            on_disk = f.read()
        if data != on_disk:
            problems.append(f'loaded {name}: the bytes passed to the seal '
                            f'differ from {kw[key]}')
    return problems


def _check_timestamp(value, window):
    if not _TIMESTAMP.match(str(value)):
        return [f'timestamp: not ISO 8601 UTC: {value!r}']
    try:
        when = datetime.fromisoformat(value)
    except ValueError:
        return [f'timestamp: not a valid date and time: {value!r}']
    if when.utcoffset() != timedelta(0):
        return [f'timestamp: not UTC: {value!r}']
    started, finished = window
    if not (started - CLOCK_TOLERANCE_S <= when.timestamp()
            <= finished + CLOCK_TOLERANCE_S):
        return [f'timestamp: {value!r} is outside the run '
                f'({datetime.fromtimestamp(started).astimezone().isoformat()}'
                f' to '
                f'{datetime.fromtimestamp(finished).astimezone().isoformat()}'
                f', tolerance {CLOCK_TOLERANCE_S} s)']
    return []


def _check_record(got, want, config, window):
    problems = []
    if set(got) != SEAL_KEYS:
        problems.append(
            f'seal record keys: missing {sorted(SEAL_KEYS - set(got))}, '
            f'unexpected {sorted(set(got) - SEAL_KEYS)}')
    for key in ('runner_version_tag', 'runner_version_commit'):
        if config.get(key) != want[key]:
            problems.append(f'{key}: the config says {config.get(key)!r}, '
                            f'VERSION says {want[key]!r}')
    for key in sorted(want):
        if key in got and not _strict_equal(got[key], want[key]):
            problems.append(f'{key}: sealed {got[key]!r}, '
                            f'recomputed {want[key]!r}')
    # seal_hash from the recomputed fields and the record's timestamp
    # (checked against the run's window below), and from the record as
    # returned: a field added to or dropped from both the record and the
    # hash input shows in the second.
    try:
        recomputed = canonical_hash(dict(want, timestamp=got.get('timestamp')))
    except HashCheckError as e:
        recomputed = f'<{e}>'
    rest = {k: v for k, v in got.items() if k != 'seal_hash'}
    try:
        own = canonical_hash(rest)
    except HashCheckError as e:
        own = f'<{e}>'
    if got.get('seal_hash') != recomputed:
        problems.append(f'seal_hash: sealed {got.get("seal_hash")!r}, '
                        f'recomputed {recomputed!r}')
    if got.get('seal_hash') != own:
        problems.append(f'seal_hash: sealed {got.get("seal_hash")!r}, '
                        f'recomputed from the record as returned {own!r}')
    problems += _check_timestamp(got.get('timestamp'), window)
    for key in ('fixture_hash', 'questions_hash', 'ground_truth_hash',
                'calculator_hash', 'config_hash', 'runner_source_hash',
                'ap1_text_hash',
                'seal_hash') + (('expected_values_hash',)
                                if want.get('expected_values_hash') else ()):
        if not _HEX64.match(str(got.get(key, ''))):
            problems.append(f'{key}: not a SHA-256 hex digest: '
                            f'{got.get(key)!r}')
    return problems


_REPORT_S1_ROW = re.compile(r'^\| `([^`]+)` \| `(.*)` \|$')


def _report_sections(report):
    """{section number: text} for the '## N. Title' sections."""
    sections, current = {}, None
    for line in report.splitlines():
        m = re.match(r'^## (\d+)\. ', line)
        if m:
            current = int(m.group(1))
            sections[current] = []
        elif line.startswith('## '):
            current = None
        elif current is not None:
            sections[current].append(line)
    return {n: '\n'.join(lines) for n, lines in sections.items()}


def check_report(report, record):
    """Report §1 prints exactly the seal record, and §2's resolved config
    hashes to its config_hash. Only these identified fields are read:
    other 64-hex text in a report (a config value, quoted model output)
    is not a seal reference."""
    problems = []
    sections = _report_sections(report)
    rows = {}
    for line in sections.get(1, '').splitlines():
        m = _REPORT_S1_ROW.match(line)
        if m:
            rows[m.group(1)] = m.group(2)
    want_rows = {k: str(v) for k, v in record.items()}
    if rows != want_rows:
        for k in sorted(set(rows) | set(want_rows)):
            if rows.get(k) != want_rows.get(k):
                problems.append(f'report §1 {k}: printed {rows.get(k)!r}, '
                                f'seal {want_rows.get(k)!r}')
    block = re.search(r'```json\n(.*?)\n```', sections.get(2, ''), re.S)
    if not block:
        problems.append('report §2: no resolved configuration block')
    else:
        try:
            resolved = json.loads(block.group(1), parse_float=Decimal)
            got = canonical_hash(resolved)
        except (ValueError, HashCheckError) as e:
            got = f'<{e}>'
        if got != record['config_hash']:
            problems.append(f'report §2 resolved config hashes to {got!r}, '
                            f'config_hash is {record["config_hash"]!r}')
    return problems


def _check_references(raw, record, scenario):
    """Every output that carries the seal exists and agrees with it."""
    problems = []
    want = set(scenario.get('sealed_outputs', SEALED_OUTPUTS))
    have = {n for n in SEALED_OUTPUTS if n in raw}
    if have != want:
        problems.append(f'outputs carrying the seal: the run wrote '
                        f'{sorted(have)}, the scenario expects {sorted(want)}')
    for n, line in enumerate(raw.get('smoke_run.jsonl', '').splitlines(), 1):
        if line.strip():
            rec = json.loads(line)
            if 'seal_hash' not in rec or rec['seal_hash'] != record['seal_hash']:
                problems.append(f'smoke_run.jsonl line {n}: seal_hash '
                                f'{rec.get("seal_hash", "(missing)")!r}, '
                                f'seal {record["seal_hash"]!r}')
                break
    if 'smoke_summary.json' in raw:
        summary = json.loads(raw['smoke_summary.json'])
        if summary.get('seal_hash', '(missing)') != record['seal_hash']:
            problems.append(f'smoke_summary.json seal_hash '
                            f'{summary.get("seal_hash", "(missing)")!r}, '
                            f'seal {record["seal_hash"]!r}')
    if 'report.md' in raw:
        problems += check_report(raw['report.md'], record)
    return problems


_SOURCE_HASH_LINE = re.compile(r'Runner source hash: (\S+?)(?:\.\.\.)?$', re.M)


def _stated_count(scenario, key, meaning):
    value = scenario.get(key)
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise HashCheckError(f'scenario does not state "{key}" ({meaning})')
    return value


def check_seals(scenario, tree, result_dir, raw, frozen):
    """Check every seal the run made against the recomputed values.

    scenario  the scenario dict. It states "seal_attempts", how many times
              the run calls the seal function, and "seal_records", how
              many records it makes (fewer when a call is refused); and,
              where they differ from the defaults, "seal_paths" and
              "sealed_outputs"
    tree      the directory the runner ran from (its base directory)
    raw       {file name: text} of what the run produced, before
              normalisation; 'console.txt' is its stdout
    frozen    {'source_hash', 'started', 'finished'}: the tree's source
              hash before the runner started, and the run's time window
    Raises HashCheckError naming every mismatch."""
    check_independent()
    n_attempts = _stated_count(scenario, 'seal_attempts',
                               'how many times the run calls the seal')
    n_records = _stated_count(scenario, 'seal_records',
                              'how many seal records the run makes')
    with open(os.path.join(result_dir, 'seal.json'), encoding='utf-8') as f:
        seals = json.load(f)
    path = os.path.join(result_dir, 'seal_inputs.json')
    if not os.path.exists(path):
        raise HashCheckError('the driver captured no seal inputs')
    with open(path, encoding='utf-8') as f:
        attempts = json.load(f)

    problems = []
    if len(attempts) != n_attempts:
        problems.append(f'seal calls: the run made {len(attempts)}, the '
                        f'scenario expects {n_attempts}')
    if len(seals) != n_records:
        problems.append(f'seal records: the run made {len(seals)}, the '
                        f'scenario expects {n_records}')
    if sum(1 for a in attempts if a['returned']) != len(seals):
        raise HashCheckError('seal capture: inputs and records do not pair '
                             'up')

    source_hash = frozen['source_hash']
    after = runner_source_hash(tree)
    if after != source_hash:
        problems.append(f'source the hash covers changed during the run: '
                        f'{source_hash!r} before, {after!r} after')

    console = raw.get('console.txt', '')
    printed = _SOURCE_HASH_LINE.findall(console)
    if attempts and len(printed) != 1:
        problems.append(f'console Runner source hash: printed '
                        f'{len(printed)} times in a run that calls the seal')
    for value in printed:
        if value != source_hash[:16]:
            problems.append(f'console Runner source hash: printed '
                            f'{value!r}, recomputed {source_hash[:16]!r}')
    for label in ('Seal hash: ', 'AP-1 text hash: '):
        found = len(re.findall('^' + re.escape(label), console, re.M))
        if found != len(seals):
            problems.append(f'console {label.strip()} printed {found} '
                            f'times for {len(seals)} seal record(s)')

    records = iter(seals)
    window = (frozen['started'], frozen['finished'])
    for n, attempt in enumerate(attempts, 1):
        problems += [f'seal call {n}: {p}' for p in
                     check_inputs(attempt, tree, scenario, source_hash)
                     + check_loaded(attempt)]
        want, refusal, error = expected_outcome(attempt, tree)
        if attempt['returned']:
            record = next(records)
            if refusal:
                problems.append(f'seal call {n}: sealed, but the contract '
                                f'refuses it ({refusal})')
                continue
            problems += [f'seal call {n}: {p}' for p in _check_record(
                record, want, _kwargs(attempt)['config'], window)]
        elif not refusal:
            problems.append(f'seal call {n}: refused '
                            f'({attempt.get("error")}), but the contract '
                            f'seals it')
        elif error and not str(attempt.get('error', '')).startswith(
                error + ':'):
            problems.append(f'seal call {n}: refused with '
                            f'{attempt.get("error")!r}, the contract refuses '
                            f'it with {error} ({refusal})')

    if seals and not problems:
        record = seals[-1]
        problems += _check_references(raw, record, scenario)
        for label, key in (('Seal hash: ', 'seal_hash'),
                           ('AP-1 text hash: ', 'ap1_text_hash')):
            for m in re.finditer('^' + re.escape(label) + r'(\S+)', console,
                                 re.M):
                if m.group(1) != record[key]:
                    problems.append(f'console {label.strip()} '
                                    f'{m.group(1)!r}, seal {record[key]!r}')
    if problems:
        raise HashCheckError('hash check failed:\n  ' + '\n  '.join(problems))
    return seals


check_independent()
