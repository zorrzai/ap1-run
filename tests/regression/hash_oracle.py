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
                   no float anywhere; UTF-8; SHA-256 hex
  file hashes      SHA-256 of the raw bytes
  config_hash      canonical hash of the resolved config, as passed to the
                   seal function (captured by driver.py before the call)
  seal_hash        canonical hash of the record without 'timestamp' (and
                   without 'seal_hash' itself)
  runner_source_hash
                   SHA-256 over every .py file under the runner's base
                   directory whose relative path does not start with
                   'output', 'review_output' or '__pycache__'; sorted by
                   relative path in the platform's own form; for each,
                   the path with '/' separators, NUL, the bytes, NUL

Version fields come from the VERSION file and git, and the scratch copy
has no .git, so they are checked for shape and against the config only.

Entry point: check_seals(), called by hard_checks.check() from
run_regression.collect() before normalisation.
"""

import hashlib
import json
import os
import re
import sys
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))

# Runner modules this process must never import.
_FORBIDDEN_MODULES = ('ap1_run', 'numeric', 'seal', 'version', 'smoke_test',
                      'verify_run_seal', 'generate_findings', 'tools')

_SOURCE_HASH_EXCLUDED = ('output', 'review_output', '__pycache__')

_HEX64 = re.compile(r'\A[0-9a-f]{64}\Z')
_TIMESTAMP = re.compile(
    r'\A\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?\+00:00\Z')
_VERSION_TAG = re.compile(r'\Av\d+(?:\.\d+)*\S*\Z')
_VERSION_COMMIT = re.compile(r'\A[0-9a-f]{7,40}\Z')

# The keys of a seal record, and nothing else.
SEAL_KEYS = frozenset({
    'timestamp', 'fixture_hash', 'questions_hash', 'ground_truth_hash',
    'config_hash', 'ap1_version', 'ap1_version_doi', 'runner_version_tag',
    'runner_version_commit', 'runner_source_hash', 'ap1_text_hash',
    'verification_keys', 'ev3_implemented', 'seal_hash'})


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


def _refuse_float(obj, path='$'):
    if isinstance(obj, float):
        raise HashCheckError(f'canonical JSON: float at {path}')
    if isinstance(obj, dict):
        for k, v in obj.items():
            _refuse_float(v, f'{path}.{k}')
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            _refuse_float(v, f'{path}[{i}]')


def canonical_json(obj):
    _refuse_float(obj)
    return json.dumps(obj, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, default=_exact_decimal)


def canonical_hash(obj):
    return hashlib.sha256(canonical_json(obj).encode('utf-8')).hexdigest()


def file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def source_hash_files(base_dir):
    """Relative paths (platform form, sorted) the source hash covers."""
    found = []
    for root, _dirs, files in os.walk(base_dir):
        for f in files:
            if not f.endswith('.py'):
                continue
            rel = os.path.relpath(os.path.join(root, f), base_dir)
            if rel.startswith(_SOURCE_HASH_EXCLUDED):
                continue
            found.append(rel)
    return sorted(found)


def runner_source_hash(base_dir):
    h = hashlib.sha256()
    for rel in source_hash_files(base_dir):
        h.update(rel.replace(os.sep, '/').encode('utf-8'))
        h.update(b'\x00')
        with open(os.path.join(base_dir, rel), 'rb') as f:
            h.update(f.read())
        h.update(b'\x00')
    return h.hexdigest()


# -- the driver's capture --------------------------------------------

def from_snapshot(node):
    """Rebuild a value from driver.snapshot()'s typed form."""
    kind = node[0]
    if kind in ('str', 'int', 'bool', 'none'):
        return node[1]
    if kind == 'decimal':
        return Decimal(node[1])
    if kind == 'float':
        return float(node[1])
    if kind == 'list':
        return [from_snapshot(v) for v in node[1]]
    if kind == 'dict':
        return {from_snapshot(k): from_snapshot(v) for k, v in node[1]}
    raise HashCheckError(f'seal input of unsupported type {node[1]}: '
                         f'{node[2]}')


def _contains_float(obj):
    try:
        _refuse_float(obj)
    except HashCheckError:
        return True
    return False


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


def expected_outcome(inputs):
    """What the contract says one seal call gives.

    Returns (record_without_timestamp, None) for a call that seals, or
    (None, reason) for a call that must be refused."""
    kw = {k: from_snapshot(v) for k, v in inputs['kwargs'].items()}
    cwd = inputs['cwd']
    config = kw['config']
    if _contains_float(config):
        return None, 'float in the resolved config (R0.4.1)'

    ap1_text_path = kw.get('ap1_text_path')
    declared = config.get('ap1_text_hash', '')
    if ap1_text_path:
        p = _path(cwd, ap1_text_path)
        if not os.path.exists(p):
            return None, f'AP-1 text file not found: {ap1_text_path}'
        ap1_text_hash = file_hash(p)
        if declared and declared != 'placeholder' and declared != ap1_text_hash:
            return None, 'AP-1 text hash mismatch'
    else:
        ap1_text_hash = declared

    record = {
        'fixture_hash': file_hash(_path(cwd, kw['fixture_path'])),
        'questions_hash': file_hash(_path(cwd, kw['questions_path'])),
        'ground_truth_hash': file_hash(_path(cwd, kw['ground_truth_path'])),
        'config_hash': canonical_hash(config),
        'ap1_version': config.get('ap1_version', ''),
        'ap1_version_doi': config.get('ap1_version_doi', ''),
        'runner_version_tag': config.get('runner_version_tag', ''),
        'runner_version_commit': config.get('runner_version_commit', ''),
        'runner_source_hash': kw.get('runner_source_hash') or '',
        'ap1_text_hash': ap1_text_hash,
        'verification_keys': kw.get('verification_keys') or [],
        'ev3_implemented': False,
    }
    record['seal_hash'] = canonical_hash(record)
    return record, None


def _check_record(got, want, source_hash):
    problems = []
    if set(got) != SEAL_KEYS:
        problems.append(
            f'seal record keys: missing {sorted(SEAL_KEYS - set(got))}, '
            f'unexpected {sorted(set(got) - SEAL_KEYS)}')
    # The runner's own source hash, recomputed from the tree it hashed.
    if want['runner_source_hash'] != source_hash:
        problems.append(
            f'runner_source_hash: passed to the seal '
            f'{want["runner_source_hash"]!r}, recomputed {source_hash!r}')
    for key in sorted(want):
        if key in got and not _strict_equal(got[key], want[key]):
            problems.append(f'{key}: sealed {got[key]!r}, '
                            f'recomputed {want[key]!r}')
    # The composite, also from the record as returned: a field added to
    # or dropped from both the record and the hash input shows here too.
    rest = {k: v for k, v in got.items() if k not in ('timestamp', 'seal_hash')}
    try:
        own = canonical_hash(rest)
    except HashCheckError as e:
        own = f'<{e}>'
    if got.get('seal_hash') != own:
        problems.append(f'seal_hash: sealed {got.get("seal_hash")!r}, '
                        f'recomputed from the record as returned {own!r}')
    if not _TIMESTAMP.match(str(got.get('timestamp', ''))):
        problems.append(f'timestamp: not ISO 8601 UTC: '
                        f'{got.get("timestamp")!r}')
    for key in ('fixture_hash', 'questions_hash', 'ground_truth_hash',
                'config_hash', 'runner_source_hash', 'ap1_text_hash',
                'seal_hash'):
        if not _HEX64.match(str(got.get(key, ''))):
            problems.append(f'{key}: not a SHA-256 hex digest: '
                            f'{got.get(key)!r}')
    if not _VERSION_TAG.match(str(got.get('runner_version_tag', ''))):
        problems.append(f'runner_version_tag: unexpected shape '
                        f'{got.get("runner_version_tag")!r}')
    if not _VERSION_COMMIT.match(str(got.get('runner_version_commit', ''))):
        problems.append(f'runner_version_commit: unexpected shape '
                        f'{got.get("runner_version_commit")!r}')
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


def _check_report(report, record):
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
    hashes = {v for k, v in record.items()
              if k.endswith('_hash') and isinstance(v, str)}
    for token in sorted(set(re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])',
                                       report))):
        if token not in hashes:
            problems.append(f'report: printed hash {token} is not in the seal')
    return problems


def _check_references(raw, record):
    """Every place the run printed or recorded a seal value agrees."""
    problems = []
    console = raw.get('console.txt', '')
    for label, key in (('Seal hash: ', 'seal_hash'),
                       ('AP-1 text hash: ', 'ap1_text_hash')):
        for m in re.finditer(re.escape(label) + r'(\S+)', console):
            if m.group(1) != record[key]:
                problems.append(f'console {label.strip()} {m.group(1)!r}, '
                                f'seal {record[key]!r}')
    for n, line in enumerate(raw.get('smoke_run.jsonl', '').splitlines(), 1):
        if line.strip():
            value = json.loads(line).get('seal_hash', record['seal_hash'])
            if value != record['seal_hash']:
                problems.append(f'smoke_run.jsonl line {n}: seal_hash '
                                f'{value!r}, seal {record["seal_hash"]!r}')
                break
    if 'smoke_summary.json' in raw:
        value = json.loads(raw['smoke_summary.json']).get('seal_hash')
        if value != record['seal_hash']:
            problems.append(f'smoke_summary.json seal_hash {value!r}, '
                            f'seal {record["seal_hash"]!r}')
    if 'report.md' in raw:
        problems += _check_report(raw['report.md'], record)
    return problems


_SOURCE_HASH_LINE = re.compile(r'Runner source hash: (\S+?)(?:\.\.\.)?$', re.M)


def check_seals(scenario, tree, result_dir, raw):
    """Check every seal the run made against the recomputed values.

    scenario  the scenario dict; 'seal_records' says how many seal records
              the run must make (0 for a run refused before or at sealing)
    tree      the directory the runner ran from (its base directory)
    raw       {file name: text} of what the run produced, before
              normalisation; 'console.txt' is its stdout
    Raises HashCheckError naming every mismatch."""
    check_independent()
    if not isinstance(scenario.get('seal_records'), int) \
            or isinstance(scenario.get('seal_records'), bool):
        raise HashCheckError(
            'scenario does not state "seal_records" (how many seal records '
            'the run makes)')
    with open(os.path.join(result_dir, 'seal.json'), encoding='utf-8') as f:
        seals = json.load(f)
    path = os.path.join(result_dir, 'seal_inputs.json')
    if not os.path.exists(path):
        raise HashCheckError('the driver captured no seal inputs')
    with open(path, encoding='utf-8') as f:
        attempts = json.load(f)

    problems = []
    if len(seals) != scenario['seal_records']:
        problems.append(f'seal records: the run made {len(seals)}, the '
                        f'scenario expects {scenario["seal_records"]}')
    if sum(1 for a in attempts if a['returned']) != len(seals):
        raise HashCheckError('seal capture: inputs and records do not pair '
                             'up')

    source_hash = runner_source_hash(tree)
    for m in _SOURCE_HASH_LINE.finditer(raw.get('console.txt', '')):
        if m.group(1) != source_hash[:16]:
            problems.append(f'console Runner source hash: printed '
                            f'{m.group(1)!r}, recomputed {source_hash[:16]!r}')

    records = iter(seals)
    for n, attempt in enumerate(attempts, 1):
        want, refusal = expected_outcome(attempt)
        if attempt['returned']:
            if refusal:
                problems.append(f'seal call {n}: sealed, but the contract '
                                f'refuses it ({refusal})')
                next(records)
                continue
            problems += [f'seal call {n}: {p}' for p in
                         _check_record(next(records), want, source_hash)]
        elif not refusal:
            problems.append(f'seal call {n}: refused, but the contract '
                            f'seals it')

    if seals and not problems:
        problems += _check_references(raw, seals[-1])
    if problems:
        raise HashCheckError('hash check failed:\n  ' + '\n  '.join(problems))
    return seals


check_independent()
