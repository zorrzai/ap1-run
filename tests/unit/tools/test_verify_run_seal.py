"""Unit tests for tools/verify_run_seal.py, the published-run seal verifier.

They pin what the tool does today, defects included. The seal record is
made by the runner's own seal() and rendered as report.py renders
sections 1 and 2, so a passing case is what a real run would give.

The tool reads the fixture, questions, ground truth and AP-1 text from
fixed paths under its BASE_DIR (the repository root). Each
test points BASE_DIR at a small tree under tmp_path.
"""

import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

import pytest

from ap1_run.execution import seal as seal_mod
from ap1_run.execution.seal import seal
from ap1_run.execution.version import compute_runner_source_hash
from ap1_run.foundation.numeric import canonical_hash, file_hash

TOOL = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))), 'tools',
    'verify_run_seal.py')

SOURCE_HASH = 'ab' * 32
# The runner source hash of the base tree, which holds no src/ap1_run/ and
# no VERSION: the hash of nothing.
TREE_SOURCE_HASH = hashlib.sha256(b'').hexdigest()


def load_tool():
    # Named as its path, tools.verify_run_seal, so a mutation tool can
    # map the functions to the file.
    spec = importlib.util.spec_from_file_location('tools.verify_run_seal',
                                                  TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def vrs():
    return load_tool()


# -- a repository tree and a run ------------------------------------------

AP1_TEXT = os.path.join('reference', 'AP-1_v1.3_DRAFT_FOR_COMMENT.md')


@pytest.fixture
def base(tmp_path, vrs, monkeypatch):
    """BASE_DIR: the example inputs and the AP-1 text."""
    root = tmp_path / 'repo'
    (root / 'example').mkdir(parents=True)
    (root / 'reference').mkdir()
    (root / 'example' / 'fixture.json').write_text('{"fixture": 1}\n')
    (root / 'example' / 'questions.json').write_text('{"items": []}\n')
    (root / 'example' / 'ground_truth_example.py').write_text('X = 1\n')
    (root / AP1_TEXT).write_text('# AP-1 text\n')
    monkeypatch.setattr(vrs, 'BASE_DIR', str(root))
    return root


# The hash of the AP-1 text the base tree holds: a sealed run declares it.
AP1_TEXT_HASH = hashlib.sha256(b'# AP-1 text\n').hexdigest()


def resolved_config(**extra):
    config = {'model': 'gpt-test', 'endpoint_url': 'https://example.test',
              'answer_tolerance': '0.01', 'repeat_count': 2,
              'ap1_version': 'v1.3-test', 'ap1_version_doi': '10.0/test',
              'ap1_text_hash': AP1_TEXT_HASH,
              'runner_version_tag': 'v1.3.1',
              'runner_version_commit': 'e0d9ec9', 'runner_modified': False}
    config.update(extra)
    return config


def make_record(base, config):
    """The seal record the runner makes for these inputs: the base tree's
    source hash, and the expected values of its empty question set."""
    return seal(config=config,
                fixture_path=base / 'example' / 'fixture.json',
                questions_path=base / 'example' / 'questions.json',
                ground_truth_path=base / 'example' / 'ground_truth_example.py',
                ap1_text_path=base / AP1_TEXT,
                runner_source_hash=TREE_SOURCE_HASH, expected_values={})


def reseal(record):
    """Recompute seal_hash over the record as seal() does: every field
    but the hash itself (T3-47: the timestamp included)."""
    record = dict(record)
    hashable = {k: v for k, v in record.items() if k != 'seal_hash'}
    record['seal_hash'] = canonical_hash(hashable)
    return record


def render_report(record, config):
    """Sections 1 and 2 as report.py writes them, with a section 3."""
    lines = ['# AP-1 Run Report', '', '## 1. Pre-Registration Record', '',
             '| Field | Value |', '|---|---|']
    lines += [f'| `{k}` | `{v}` |' for k, v in sorted(record.items())]
    lines += ['', '## 2. Resolved Configuration', '', '```json',
              json.dumps(config, indent=2, ensure_ascii=False,
                         sort_keys=True),
              '```', '', '## 3. Per-Dimension Results', '', 'text', '']
    return '\n'.join(lines)


def write_run(run_dir, record, config, transcript=True, report=None):
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / 'report.md').write_text(
        report if report is not None else render_report(record, config),
        encoding='utf-8')
    if transcript is True:
        # As the runner writes them: each line timestamped, no earlier
        # than the seal.
        stamp = record.get('timestamp')
        transcript = [{'seal_hash': record['seal_hash'], 'n': 1,
                       'timestamp': stamp},
                      {'seal_hash': record['seal_hash'], 'n': 2,
                       'timestamp': stamp}]
    if transcript:
        (run_dir / 'smoke_run.jsonl').write_text(
            ''.join(json.dumps(r) + '\n' for r in transcript))
    return run_dir


@pytest.fixture
def run(tmp_path, base):
    """A run directory whose report and transcript match the tree."""
    config = resolved_config()
    record = make_record(base, config)
    return write_run(tmp_path / 'run', record, config), record, config


def all_checks(record, lines=2):
    """Every check of a run that matches, in order."""
    return [
        ('seal record fields', 'all 18 sealed fields present'),
        ('config_hash', 'MATCH'),
        ('fixture_hash', 'MATCH'),
        ('questions_hash', 'MATCH'),
        ('ground_truth_hash', 'MATCH'),
        ('ap1_text_hash', 'MATCH'),
        ('expected_values_hash', 'MATCH'),
        ('runner_source_hash', 'MATCH'),
        ('seal_hash', 'MATCH'),
        ('transcript seal_hash', 'all %d lines match report' % lines),
        ('seal timestamp', 'before the first transcript record (%s)'
         % record['timestamp']),
    ]


def names(entries):
    return [name for name, _ in entries]


def without(entries, *dropped):
    return [e for e in entries if e[0] not in dropped]


# -- parse_seal_record ----------------------------------------------------

def test_parse_seal_record_reads_backticked_rows_of_section_1(vrs):
    text = ('## 1. Pre-Registration Record\n\n| Field | Value |\n|---|---|\n'
            '| `a` | `1` |\n| `b` | `x y` |\n')
    assert vrs.parse_seal_record(text) == {'a': '1', 'b': 'x y'}


def test_parse_seal_record_values_stay_strings(vrs):
    text = ('## 1. Pre-Registration Record\n| `flag` | `False` |\n'
            '| `keys` | `[]` |\n')
    assert vrs.parse_seal_record(text) == {'flag': 'False', 'keys': '[]'}


def test_parse_seal_record_empty_value_is_empty_string(vrs):
    text = '## 1. Pre-Registration Record\n| `doi` | `` |\n'
    assert vrs.parse_seal_record(text) == {'doi': ''}


def test_parse_seal_record_ignores_rows_outside_section_1(vrs):
    text = ('| `before` | `1` |\n## 1. Pre-Registration Record\n'
            '| `inside` | `2` |\n## 2. Resolved Configuration\n'
            '| `after` | `3` |\n')
    assert vrs.parse_seal_record(text) == {'inside': '2'}


def test_parse_seal_record_ignores_rows_without_backticks(vrs):
    text = ('## 1. Pre-Registration Record\n| Field | Value |\n|---|---|\n'
            '| `a` | plain |\n| `b` | `ok` |\n')
    assert vrs.parse_seal_record(text) == {'b': 'ok'}


def test_parse_seal_record_heading_matched_anywhere_in_line(vrs):
    text = '### ## 1. Pre-Registration Record (copy)\n| `a` | `1` |\n'
    assert vrs.parse_seal_record(text) == {'a': '1'}


def test_parse_seal_record_no_section_is_empty(vrs):
    assert vrs.parse_seal_record('# Report\n| `a` | `1` |\n') == {}


def test_parse_seal_record_duplicate_field_last_wins(vrs):
    # A report with a field twice is accepted silently; the later row
    # is the one verified.
    text = '## 1. Pre-Registration Record\n| `a` | `1` |\n| `a` | `2` |\n'
    assert vrs.parse_seal_record(text) == {'a': '2'}


# -- parse_resolved_config ------------------------------------------------

def test_parse_resolved_config_reads_json_block_of_section_2(vrs):
    text = ('## 2. Resolved Configuration\n\nprose\n```json\n'
            '{"model": "m",\n "n": 2}\n```\nafter\n')
    assert vrs.parse_resolved_config(text) == {'model': 'm', 'n': 2}


def test_parse_resolved_config_no_section_is_none(vrs):
    assert vrs.parse_resolved_config('```json\n{"a": 1}\n```\n') is None


def test_parse_resolved_config_empty_block_is_none(vrs):
    assert vrs.parse_resolved_config(
        '## 2. Resolved Configuration\n```json\n```\n') is None


def test_parse_resolved_config_reads_only_up_to_closing_fence(vrs):
    text = ('## 2. Resolved Configuration\n```json\n{"a": 1}\n```\n'
            '```json\n{"b": 2}\n```\n')
    assert vrs.parse_resolved_config(text) == {'a': 1}


def test_parse_resolved_config_heading_inside_the_block_is_json(vrs):
    # Section 2 ends at the next heading before its block, not inside it.
    text = ('## 2. Resolved Configuration\n```json\n{"a":\n'
            '"## 3"}\n```\n')
    assert vrs.parse_resolved_config(text) == {'a': '## 3'}


def test_parse_resolved_config_fraction_is_decimal(vrs):
    # S3-G8-3: never a float, which canonical hashing refuses.
    from decimal import Decimal
    value = vrs.parse_resolved_config(
        '## 2. Resolved Configuration\n```json\n{"t": 0.50}\n```\n')
    assert value == {'t': Decimal('0.50')}
    assert str(value['t']) == '0.50'


def test_parse_resolved_config_invalid_json_raises(vrs):
    with pytest.raises(json.JSONDecodeError):
        vrs.parse_resolved_config(
            '## 2. Resolved Configuration\n```json\n{oops}\n```\n')


# -- rebuild_record ---------------------------------------------------------

def test_rebuild_record_types_by_field(vrs):
    assert vrs.rebuild_record({'verification_keys': "['k1', 'k2']",
                               'ev3_implemented': 'True', 'a': 'False',
                               'b': '[]'}) == {
        'verification_keys': ['k1', 'k2'], 'ev3_implemented': True,
        'a': 'False', 'b': '[]'}
    assert vrs.rebuild_record({'ev3_implemented': 'False',
                               'verification_keys': '[]'}) == {
        'ev3_implemented': False, 'verification_keys': []}
    assert vrs.rebuild_record({}) == {}


@pytest.mark.parametrize('field, value, message', [
    ('verification_keys', 'not a list', "verification_keys 'not a list': "),
    ('verification_keys', "'k'", "verification_keys \"'k'\" is not a list"),
    ('verification_keys', '[', "verification_keys '[': "),
    ('ev3_implemented', 'yes', "ev3_implemented 'yes' is not True or False"),
])
def test_rebuild_record_unreadable_value(vrs, field, value, message):
    with pytest.raises(ValueError) as exc:
        vrs.rebuild_record({field: value})
    assert str(exc.value).startswith(message)


# -- verify_run: a run that matches ---------------------------------------

def test_verify_run_matching_run_passes_every_check(vrs, run):
    run_dir, record, _ = run
    warnings = []
    checks, failures = vrs.verify_run(str(run_dir), warnings=warnings)
    assert failures == [] and warnings == []
    assert checks == all_checks(record)


def test_verify_run_warnings_argument_is_optional(vrs, run):
    run_dir, record, _ = run
    assert vrs.verify_run(str(run_dir)) == (all_checks(record), [])


# -- verify_run: what is missing ------------------------------------------

def test_verify_run_without_report_fails_report_exists(vrs, tmp_path, base):
    checks, failures = vrs.verify_run(str(tmp_path / 'nothing'))
    assert checks == []
    assert failures == [('report exists', 'report.md not found')]


def test_verify_run_without_seal_record_stops(vrs, tmp_path, base):
    run_dir = write_run(tmp_path / 'run', {'seal_hash': 'x'}, {},
                        report='# Report\n\n## 2. Resolved Configuration\n')
    checks, failures = vrs.verify_run(str(run_dir))
    assert checks == []
    assert failures == [('seal record parsed',
                         'no seal record found in report.md section 1')]


def test_verify_run_without_resolved_config_stops(vrs, tmp_path, base):
    # Parsing is a precondition, never a passed check (T3-18).
    report = '## 1. Pre-Registration Record\n| `seal_hash` | `x` |\n'
    run_dir = write_run(tmp_path / 'run', {'seal_hash': 'x'}, {},
                        report=report)
    checks, failures = vrs.verify_run(str(run_dir))
    assert checks == []
    assert failures == [('resolved config parsed',
                         'no resolved config found in report.md section 2')]


def test_verify_run_resolved_config_not_json_stops(vrs, tmp_path, base):
    report = ('## 1. Pre-Registration Record\n| `seal_hash` | `x` |\n'
              '## 2. Resolved Configuration\n```json\n{oops}\n```\n')
    run_dir = write_run(tmp_path / 'run', {'seal_hash': 'x'}, {},
                        report=report)
    checks, failures = vrs.verify_run(str(run_dir))
    assert checks == []
    assert names(failures) == ['resolved config parsed']
    assert failures[0][1].startswith('report.md section 2 is not JSON: ')


@pytest.mark.parametrize('field, relpath', [
    ('fixture_hash', os.path.join('example', 'fixture.json')),
    ('questions_hash', os.path.join('example', 'questions.json')),
    ('ground_truth_hash', os.path.join('example', 'ground_truth_example.py')),
    ('ap1_text_hash', AP1_TEXT),
])
def test_verify_run_missing_input_file_fails_with_its_path(vrs, run, base,
                                                           field, relpath):
    run_dir, record, _ = run
    os.remove(base / relpath)
    checks, failures = vrs.verify_run(str(run_dir))
    path = os.path.join(str(base), relpath)
    assert failures == [(field, f'file not found: {path}')]
    # The other inputs are still checked; the expected values need all
    # three text inputs.
    skipped = ([field] if field == 'ap1_text_hash'
               else [field, 'expected_values_hash'])
    assert checks == without(all_checks(record), *skipped)


def test_verify_run_reads_these_paths(vrs, run, base, monkeypatch):
    # The exact files the verifier looks for (case included: on a
    # case-insensitive file system a wrong case would go unnoticed).
    run_dir, _, _ = run
    looked_up = []
    real_exists = os.path.exists

    def exists(path):
        looked_up.append(path)
        return real_exists(path)
    monkeypatch.setattr(vrs.os.path, 'exists', exists)
    vrs.verify_run(str(run_dir))
    b = str(base)
    inputs = [os.path.join(b, 'example', 'fixture.json'),
              os.path.join(b, 'example', 'questions.json'),
              os.path.join(b, 'example', 'ground_truth_example.py')]
    assert looked_up == [
        os.path.join(str(run_dir), 'report.md'),
        *inputs,
        os.path.join(b, 'reference', 'AP-1_v1.3_DRAFT_FOR_COMMENT.md'),
        *inputs,
        os.path.join(str(run_dir), 'smoke_run.jsonl'),
    ]


def test_verify_run_reads_text_files_as_utf8(vrs, run, monkeypatch):
    # Not the platform's default encoding (cp1252 on Windows); the inputs
    # for the expected values are read as bytes.
    run_dir, _, _ = run
    opened = []
    real_open = open

    def recording_open(path, *args, **kwargs):
        opened.append((os.path.basename(str(path)), args,
                       kwargs.get('encoding')))
        return real_open(path, *args, **kwargs)
    monkeypatch.setattr(vrs, 'open', recording_open, raising=False)
    vrs.verify_run(str(run_dir))
    assert opened == [
        ('report.md', (), 'utf-8'), ('fixture.json', ('rb',), None),
        ('questions.json', ('rb',), None),
        ('ground_truth_example.py', ('rb',), None),
        ('smoke_run.jsonl', (), 'utf-8')]


@pytest.mark.finding('F1', 'T3-79')
def test_verify_run_ignores_config_files_on_disk(vrs, run, base):
    # The sealed config is checked against report.md section 2 only; a
    # config file in example/, matching or not, changes nothing.
    run_dir, record, config = run
    (base / 'example' / 'config.json').write_text(json.dumps(config))
    (base / 'example' / 'config_mini.json').write_text('{"model": "x"}')
    checks, failures = vrs.verify_run(str(run_dir))
    assert (checks, failures) == (all_checks(record), [])


# -- verify_run: what is compared ------------------------------------------

def test_verify_run_config_hash_mismatch_fails_with_both_hashes(
        vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record,
                        resolved_config(model='other'))
    checks, failures = vrs.verify_run(str(run_dir))
    recomputed = canonical_hash(resolved_config(model='other'))
    assert failures == [('config_hash', 'sealed=%s, recomputed=%s' % (
        record['config_hash'], recomputed))]
    assert 'config_hash' not in names(checks)


@pytest.mark.parametrize('field', ['config_hash', 'fixture_hash'])
def test_verify_run_missing_hash_field_shows_empty_sealed_value(
        vrs, tmp_path, base, field):
    config = resolved_config()
    record = make_record(base, config)
    shown = reseal({k: v for k, v in record.items() if k != field})
    run_dir = write_run(tmp_path / 'run', shown, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [
        ('seal record fields', 'missing ' + field),
        (field, 'sealed=, recomputed=%s' % record[field])]


def test_verify_run_config_hash_is_canonical_json_sha256(vrs, tmp_path,
                                                         base):
    # The verifier hashes the resolved config as canonical JSON: sorted
    # keys, no whitespace, UTF-8. A seal over another serialisation fails.
    config = {'model': 'm', 'b': [1, 'é'], 'ap1_text_hash': AP1_TEXT_HASH}
    expected = hashlib.sha256(
        ('{"ap1_text_hash":"%s","b":[1,"é"],"model":"m"}' % AP1_TEXT_HASH
         ).encode('utf-8')).hexdigest()
    record = dict(make_record(base, config), config_hash=expected)
    run_dir = write_run(tmp_path / 'run', reseal(record), config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert ('config_hash', 'MATCH') in checks


@pytest.mark.parametrize('field, relpath', [
    ('fixture_hash', 'example/fixture.json'),
    ('questions_hash', 'example/questions.json'),
    ('ap1_text_hash', AP1_TEXT),
])
def test_verify_run_changed_input_fails_its_hash(vrs, run, base, field,
                                                  relpath):
    run_dir, record, _ = run
    (base / relpath).write_text('changed\n')
    checks, failures = vrs.verify_run(str(run_dir))
    assert (field, 'sealed=%s, recomputed=%s' % (
        record[field], file_hash(str(base / relpath)))) in failures
    assert field not in names(checks)


def legacy(record):
    """The record as a runner before the seal_format field made it: no
    seal_format, expected values or environment, and a seal_hash without
    the timestamp."""
    record = {k: v for k, v in record.items() if k not in (
        'seal_format', 'expected_values_hash', 'python_version', 'platform',
        'package_versions')}
    record['seal_hash'] = canonical_hash(
        {k: v for k, v in record.items()
         if k not in ('timestamp', 'seal_hash')})
    return record


LEGACY_WARNING = ('seal_format', 'none: a record made before October 2026, '
                  'checked under the rules it was made with (raw bytes, '
                  'seal_hash without the timestamp)')
LEGACY_SOURCE_WARNING = ('runner_source_hash', 'not recomputed: a record '
                         'made before October 2026 hashed every .py file of '
                         'the clone; see docs/REPRODUCING.md')


def test_verify_run_legacy_record_checked_under_its_rules(vrs, tmp_path,
                                                         base):
    # A record without seal_format: no field-set, expected-values or
    # source-hash check; seal_hash without the timestamp; a warning.
    config = resolved_config()
    record = legacy(make_record(base, config))
    run_dir = write_run(tmp_path / 'run', record, config)
    warnings = []
    checks, failures = vrs.verify_run(str(run_dir), warnings=warnings)
    assert failures == []
    assert checks == without(all_checks(record), 'seal record fields',
                             'expected_values_hash', 'runner_source_hash')
    assert warnings == [LEGACY_WARNING, LEGACY_SOURCE_WARNING]


def test_verify_run_legacy_record_without_source_hash_no_source_warning(
        vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    del record['runner_source_hash']
    run_dir = write_run(tmp_path / 'run', legacy(record), config)
    warnings = []
    assert vrs.verify_run(str(run_dir), warnings=warnings)[1] == []
    assert warnings == [LEGACY_WARNING]


def test_verify_run_legacy_record_hashes_raw_bytes(vrs, tmp_path, base):
    # Line endings count in a record made under the old rules.
    config = resolved_config()
    record = legacy(make_record(base, config))
    run_dir = write_run(tmp_path / 'run', record, config)
    (base / 'example' / 'fixture.json').write_bytes(b'{"fixture": 1}\r\n')
    _, failures = vrs.verify_run(str(run_dir))
    assert names(failures) == ['fixture_hash']


def test_verify_run_legacy_seal_hash_excludes_the_timestamp(vrs, tmp_path,
                                                           base):
    config = resolved_config()
    record = legacy(make_record(base, config))
    record['timestamp'] = '2000-01-01T00:00:00+00:00'
    run_dir = write_run(tmp_path / 'run', record, config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == [] and ('seal_hash', 'MATCH') in checks


def test_verify_run_unknown_seal_format_stops(vrs, tmp_path, base):
    config = resolved_config()
    record = reseal(dict(make_record(base, config), seal_format='3'))
    run_dir = write_run(tmp_path / 'run', record, config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert checks == []
    assert failures == [('seal_format',
                         "unknown format '3' (this verifier reads '2')")]


def test_verify_run_record_with_an_unsealed_field_fails(vrs, tmp_path, base):
    config = resolved_config()
    record = reseal(dict(make_record(base, config), zz='1', aa='2'))
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('seal record fields',
                         'not sealed by the runner aa, zz')]


def test_verify_run_record_missing_and_unsealed_fields(vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    del record['platform'], record['python_version']
    run_dir = write_run(tmp_path / 'run', reseal(dict(record, x='1')),
                        config)
    _, failures = vrs.verify_run(str(run_dir))
    assert ('seal record fields', 'missing python_version, platform; not '
            'sealed by the runner x') in failures


def test_verify_run_hashes_text_inputs_with_lf_and_no_bom(vrs, run, base):
    run_dir, _, _ = run
    (base / 'example' / 'fixture.json').write_bytes(
        b'\xef\xbb\xbf{"fixture": 1}\r\n')
    assert vrs.verify_run(str(run_dir))[1] == []


def test_verify_run_ap1_text_hashed_as_raw_bytes(vrs, run, base):
    run_dir, record, _ = run
    (base / AP1_TEXT).write_bytes(b'# AP-1 text\r\n')
    _, failures = vrs.verify_run(str(run_dir))
    assert names(failures) == ['ap1_text_hash']


def test_verify_run_ap1_text_of_the_runs_version(vrs, tmp_path, base):
    # V12-4: a v1.2 run is compared with the v1.2 text.
    v12 = base / 'reference' / 'AP-1_Admissibility_Protocol_v1.2.md'
    v12.write_text('# v1.2\n')
    config = resolved_config(ap1_version='v1.2',
                             ap1_text_hash=file_hash(str(v12)))
    record = seal(config=config,
                  fixture_path=base / 'example' / 'fixture.json',
                  questions_path=base / 'example' / 'questions.json',
                  ground_truth_path=base / 'example' /
                  'ground_truth_example.py',
                  ap1_text_path=v12, runner_source_hash=TREE_SOURCE_HASH,
                  expected_values={})
    run_dir = write_run(tmp_path / 'run', record, config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == [] and ('ap1_text_hash', 'MATCH') in checks


def test_verify_run_unknown_version_without_ap1_text_fails(vrs, tmp_path,
                                                          base):
    config = resolved_config(ap1_version='v9')
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('ap1_text_hash', "no AP-1 text is known for "
                         "ap1_version 'v9'; give it with --ap1-text")]
    other = tmp_path / 'other.md'
    other.write_text('# AP-1 text\n')
    assert vrs.verify_run(str(run_dir), ap1_text=str(other))[1] == []


def test_verify_run_inputs_from_the_fixture_dir_given(vrs, tmp_path, base):
    # S3-G8-4: the inputs of a run made with --fixture-dir.
    other = tmp_path / 'my_fixture'
    shutil.copytree(base / 'example', other)
    (other / 'fixture.json').write_text('{"fixture": "mine"}\n')
    config = resolved_config()
    record = seal(config=config, fixture_path=other / 'fixture.json',
                  questions_path=other / 'questions.json',
                  ground_truth_path=other / 'ground_truth_example.py',
                  ap1_text_path=base / AP1_TEXT,
                  runner_source_hash=TREE_SOURCE_HASH, expected_values={})
    run_dir = write_run(tmp_path / 'run', record, config)
    assert names(vrs.verify_run(str(run_dir))[1]) == ['fixture_hash']
    assert vrs.verify_run(str(run_dir), fixture_dir=str(other))[1] == []


GT = os.path.join('example', 'ground_truth_example.py')


def test_verify_run_known_ground_truth_hash_gets_its_note(vrs, tmp_path,
                                                         base):
    known = next(iter(vrs.GROUND_TRUTH_ERRATA))
    config = resolved_config()
    record = reseal(dict(make_record(base, config), ground_truth_hash=known))
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    computed = seal_mod.text_file_hash(str(base / GT))
    assert failures == [('ground_truth_hash',
                         'sealed=%s, recomputed=%s' % (known, computed)
                         + '\n          NOTE: '
                         + vrs.GROUND_TRUTH_ERRATA[known])]


def test_verify_run_errata_map(vrs):
    assert list(vrs.GROUND_TRUTH_ERRATA) == [
        'dd3434bc62c4976af928798024d1446993ce59dd473e78cf4002832630314715',
        '033ce73d933d6e52a7d4f63b3888bdccfa492ce49cf49228ed2f3dda0d27a643']
    for note in vrs.GROUND_TRUTH_ERRATA.values():
        assert 'FINDINGS_ERRATA.md' in note
        assert 'expected' not in note.lower()


# -- verify_run: expected values and the runner source hash --------------

def test_verify_run_expected_values_recomputed_from_the_module(
        vrs, tmp_path, base):
    # T3-48: the ground-truth module is run on every item.
    (base / 'example' / 'fixture.json').write_text('{"accounts": []}\n')
    (base / 'example' / 'questions.json').write_text(json.dumps(
        {'items': [{'id': 'Q01', 'source_accounts': []}]}))
    (base / 'example' / 'ground_truth_example.py').write_text(
        'def compute(item_id, ctx):\n    return {"final": "1.5"}\n')
    config = resolved_config()
    values = {'Q01': {'final': '1.5'}}
    record = seal(config=config,
                  fixture_path=base / 'example' / 'fixture.json',
                  questions_path=base / 'example' / 'questions.json',
                  ground_truth_path=base / GT, ap1_text_path=base / AP1_TEXT,
                  runner_source_hash=TREE_SOURCE_HASH, expected_values=values)
    run_dir = write_run(tmp_path / 'run', record, config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == [] and ('expected_values_hash', 'MATCH') in checks
    (base / 'example' / 'ground_truth_example.py').write_text(
        'def compute(item_id, ctx):\n    return {"final": "2"}\n')
    record = seal(config=config,
                  fixture_path=base / 'example' / 'fixture.json',
                  questions_path=base / 'example' / 'questions.json',
                  ground_truth_path=base / GT, ap1_text_path=base / AP1_TEXT,
                  runner_source_hash=TREE_SOURCE_HASH, expected_values=values)
    run_dir = write_run(tmp_path / 'run2', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('expected_values_hash', 'sealed=%s, recomputed=%s'
                         % (record['expected_values_hash'],
                            canonical_hash({'Q01': {'final': '2'}})))]


def test_verify_run_expected_values_module_may_import_its_neighbours(
        vrs, tmp_path, base):
    (base / 'example' / 'helper_g5.py').write_text('V = "7"\n')
    (base / 'example' / 'fixture.json').write_text('{"accounts": []}\n')
    (base / 'example' / 'questions.json').write_text(json.dumps(
        {'items': [{'id': 'Q01'}]}))
    (base / GT).write_text('import helper_g5\n'
                           'def compute(item_id, ctx):\n'
                           '    return {"final": helper_g5.V}\n')
    config = resolved_config()
    record = seal(config=config,
                  fixture_path=base / 'example' / 'fixture.json',
                  questions_path=base / 'example' / 'questions.json',
                  ground_truth_path=base / GT, ap1_text_path=base / AP1_TEXT,
                  runner_source_hash=TREE_SOURCE_HASH,
                  expected_values={'Q01': {'final': '7'}})
    run_dir = write_run(tmp_path / 'run', record, config)
    path_before = list(sys.path)
    try:
        assert vrs.verify_run(str(run_dir))[1] == []
    finally:
        sys.modules.pop('helper_g5', None)
    assert sys.path == path_before


def test_verify_run_expected_values_module_error_fails(vrs, tmp_path, base):
    (base / 'example' / 'fixture.json').write_text('{"accounts": []}\n')
    (base / 'example' / 'questions.json').write_text(json.dumps(
        {'items': [{'id': 'Q01'}]}))
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config)
    path_before = list(sys.path)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('expected_values_hash', "cannot recompute: "
                         "AttributeError: module 'ground_truth_example' has "
                         "no attribute 'compute'")]
    assert sys.path == path_before


def test_verify_run_record_without_expected_values_fails(vrs, tmp_path,
                                                        base):
    config = resolved_config()
    record = reseal(dict(make_record(base, config), expected_values_hash=''))
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('expected_values_hash',
                         'the record seals no expected values')]


def test_verify_run_runner_source_hash_of_this_checkout(vrs, tmp_path, base):
    # T3-19: compared with this checkout's code, named in the failure.
    (base / 'src' / 'ap1_run').mkdir(parents=True)
    (base / 'src' / 'ap1_run' / 'm.py').write_text('X = 1\n')
    here = compute_runner_source_hash(str(base))
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('runner_source_hash', 'sealed=%s, this checkout=%s: '
                         'the run was made with other runner code; verify '
                         'it from a checkout of its runner_version_commit '
                         '(e0d9ec9)' % (TREE_SOURCE_HASH, here))]


def test_verify_run_runner_modified_is_a_warning(vrs, tmp_path, base):
    config = resolved_config(runner_modified=True)
    run_dir = write_run(tmp_path / 'run', make_record(base, config), config)
    warnings = []
    checks, failures = vrs.verify_run(str(run_dir), warnings=warnings)
    assert failures == []
    assert warnings == [('runner_modified', 'the run recorded '
                         'runner_modified: true (VERSION did not name git '
                         'HEAD, or the code had uncommitted changes); '
                         'runner_version_tag does not identify the code')]


@pytest.mark.parametrize('value', [False, 'true', 1])
def test_verify_run_runner_modified_only_when_true(vrs, tmp_path, base,
                                                   value):
    config = resolved_config(runner_modified=value)
    run_dir = write_run(tmp_path / 'run', make_record(base, config), config)
    warnings = []
    vrs.verify_run(str(run_dir), warnings=warnings)
    assert warnings == []


# -- verify_run: seal_hash ------------------------------------------------------

def test_verify_run_seal_hash_mismatch_fails_with_both_hashes(
        vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    shown = dict(record, seal_hash='0' * 64)
    run_dir = write_run(tmp_path / 'run', shown, config, transcript=[
        {'seal_hash': '0' * 64, 'timestamp': record['timestamp']}])
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('seal_hash', 'sealed=%s, recomputed=%s' % (
        '0' * 64, record['seal_hash'])), ]


def test_verify_run_missing_seal_hash_field_fails(vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    shown = {k: v for k, v in record.items() if k != 'seal_hash'}
    run_dir = write_run(tmp_path / 'run', shown, config,
                        transcript=[{'seal_hash': '',
                                     'timestamp': record['timestamp']}])
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == [('seal_hash', 'sealed=, recomputed=%s' %
                         record['seal_hash'])]
    # The transcript's empty seal_hash "matches" the report's missing one.
    assert ('transcript seal_hash', 'all 1 lines match report') in checks


def test_verify_run_seal_with_true_ev3_flag_verifies(vrs, tmp_path, base):
    config = resolved_config()
    record = reseal(dict(make_record(base, config), ev3_implemented=True))
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == []


def test_verify_run_unreadable_record_value_fails_seal_hash(vrs, tmp_path,
                                                           base):
    config = resolved_config()
    record = make_record(base, config)
    report = render_report(record, config).replace(
        '| `ev3_implemented` | `False` |', '| `ev3_implemented` | `no` |')
    run_dir = write_run(tmp_path / 'run', record, config, report=report)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('seal_hash', "cannot read the record: "
                         "ev3_implemented 'no' is not True or False")]


# -- verify_run: the transcript ---------------------------------------------

def stamped(record, seal_hashes):
    return [{'seal_hash': h, 'timestamp': record['timestamp']}
            for h in seal_hashes]


def transcript_failure(vrs, tmp_path, base, lines=None, text=None):
    """The transcript failure of a run whose transcript is `lines` (or the
    raw `text`)."""
    config = resolved_config()
    record = make_record(base, config)
    if lines is not None:
        lines = lines(record)
    run_dir = write_run(tmp_path / 'run', record, config,
                        transcript=lines if lines is not None else None)
    if text is not None:
        (run_dir / 'smoke_run.jsonl').write_text(text)
    _, failures = vrs.verify_run(str(run_dir))
    return record, [f for f in failures if f[0] == 'transcript seal_hash']


def test_verify_run_missing_transcript_fails(vrs, tmp_path, base):
    _, failures = transcript_failure(vrs, tmp_path, base)
    path = os.path.join(str(tmp_path / 'run'), 'smoke_run.jsonl')
    assert failures == [('transcript seal_hash',
                         'transcript not found: %s' % path)]


def test_verify_run_empty_transcript_fails(vrs, tmp_path, base):
    _, failures = transcript_failure(vrs, tmp_path, base, text='')
    assert failures == [('transcript seal_hash', 'the transcript is empty')]


def test_verify_run_every_transcript_line_compared(vrs, tmp_path, base):
    record, failures = transcript_failure(
        vrs, tmp_path, base,
        lambda r: stamped(r, [r['seal_hash'], 'spliced', r['seal_hash'],
                              None]))
    assert failures == [('transcript seal_hash',
                         "report=%s; line 2 has seal_hash 'spliced'; line 4 "
                         "has seal_hash None" % record['seal_hash'])]


def test_verify_run_transcript_problems_in_line_order(vrs, tmp_path, base):
    record, failures = transcript_failure(
        vrs, tmp_path, base,
        text='{"seal_hash": "a"}\n\n[1]\nnot json\n')
    detail = failures[0][1]
    assert detail.startswith(
        "report=%s; line 1 has seal_hash 'a'; line 2 is blank; line 3 is "
        "not a JSON object; line 4 is not JSON (" % record['seal_hash'])


def test_verify_run_transcript_failure_lists_five_lines(vrs, tmp_path, base):
    record, failures = transcript_failure(
        vrs, tmp_path, base, lambda r: stamped(r, ['x'] * 7))
    assert failures[0][1] == (
        'report=%s; ' % record['seal_hash'] + '; '.join(
            "line %d has seal_hash 'x'" % n for n in range(1, 6))
        + '; and 2 more')


def test_verify_run_transcript_failure_lists_up_to_five_lines(
        vrs, tmp_path, base):
    record, failures = transcript_failure(
        vrs, tmp_path, base, lambda r: stamped(r, ['x'] * 5))
    assert failures[0][1].endswith("line 5 has seal_hash 'x'")


def test_verify_run_transcript_without_records_has_no_timestamp_check(
        vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config, transcript=None)
    (run_dir / 'smoke_run.jsonl').write_text('\n')
    _, failures = vrs.verify_run(str(run_dir))
    assert names(failures) == ['transcript seal_hash']


# -- verify_run: the time of the seal ------------------------------------------

def timestamp_failures(vrs, tmp_path, base, sealed_at, first_at):
    config = resolved_config()
    record = reseal(dict(make_record(base, config), timestamp=sealed_at))
    lines = [{'seal_hash': record['seal_hash'], 'timestamp': first_at},
             {'seal_hash': record['seal_hash']}]
    run_dir = write_run(tmp_path / 'run', record, config, transcript=lines)
    checks, failures = vrs.verify_run(str(run_dir))
    return ([c for c in checks if c[0] == 'seal timestamp'],
            [f for f in failures if f[0] == 'seal timestamp'])


@pytest.mark.parametrize('sealed_at, first_at', [
    ('2026-10-15T12:00:00+00:00', '2026-10-15T12:00:00+00:00'),
    ('2026-10-15T11:59:59.999999+00:00', '2026-10-15T12:00:00+00:00'),
    ('2026-10-15T13:00:00+02:00', '2026-10-15T12:00:00+00:00')])
def test_verify_run_seal_no_later_than_first_record_passes(
        vrs, tmp_path, base, sealed_at, first_at):
    checks, failures = timestamp_failures(vrs, tmp_path, base, sealed_at,
                                          first_at)
    assert failures == []
    assert checks == [('seal timestamp', 'before the first transcript '
                       'record (%s)' % first_at)]


def test_verify_run_seal_after_first_record_fails(vrs, tmp_path, base):
    _, failures = timestamp_failures(vrs, tmp_path, base,
                                     '2026-10-15T12:00:01+00:00',
                                     '2026-10-15T12:00:00+00:00')
    assert failures == [('seal timestamp', '2026-10-15T12:00:01+00:00 is '
                         'after the first transcript record '
                         '(2026-10-15T12:00:00+00:00): the run was not '
                         'sealed before execution')]


@pytest.mark.parametrize('sealed_at, first_at, detail', [
    ('yesterday', '2026-10-15T12:00:00+00:00',
     "not an ISO-8601 time with a zone: 'yesterday'"),
    ('2026-10-15T12:00:00', '2026-10-15T12:00:00+00:00',
     "not an ISO-8601 time with a zone: '2026-10-15T12:00:00'"),
    ('2026-10-15T12:00:00+00:00', None,
     'transcript line 1 has no ISO-8601 timestamp with a zone: None'),
    ('2026-10-15T12:00:00+00:00', '2026-10-15T12:00:00',
     "transcript line 1 has no ISO-8601 timestamp with a zone: "
     "'2026-10-15T12:00:00'")])
def test_verify_run_unreadable_timestamps_fail(vrs, tmp_path, base,
                                               sealed_at, first_at, detail):
    _, failures = timestamp_failures(vrs, tmp_path, base, sealed_at,
                                     first_at)
    assert failures == [('seal timestamp', detail)]




# -- main -------------------------------------------------------------------

def run_main(vrs, argv, monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['verify_run_seal.py'] + argv)
    code = vrs.main()
    return code, capsys.readouterr().out


def test_main_without_arguments_prints_usage_and_returns_1(vrs, monkeypatch,
                                                          capsys):
    code, out = run_main(vrs, [], monkeypatch, capsys)
    assert code == 1
    assert out == ('Usage: python tools/verify_run_seal.py [--fixture-dir DIR]'
                   ' [--ap1-text FILE] <output_dir> [<output_dir2> ...]\n'
                   '\nExample:\n'
                   '  python tools/verify_run_seal.py output/run_a_mini '
                   'output/run_b_sol\n')


def test_main_argv_argument(vrs, run, capsys):
    run_dir, _, _ = run
    assert vrs.main([str(run_dir)]) == 0
    assert capsys.readouterr().out.endswith('RESULT: PASS (11 checks)\n')


def test_main_passing_run_prints_each_check_and_counts_them(vrs, run,
                                                            monkeypatch,
                                                            capsys):
    run_dir, record, _ = run
    code, out = run_main(vrs, [str(run_dir)], monkeypatch, capsys)
    assert code == 0
    expected = ['=== Verifying: %s ===' % run_dir, '']
    expected += ['  PASS  %s: %s' % c for c in all_checks(record)]
    expected += ['', '  11 passed, 0 failed', '', 'RESULT: PASS (11 checks)',
                 '']
    assert out == '\n'.join(expected)


def test_main_prints_warnings_and_counts_them(vrs, tmp_path, base,
                                              monkeypatch, capsys):
    config = resolved_config(runner_modified=True)
    record = legacy(make_record(base, config))
    run_dir = write_run(tmp_path / 'run', record, config)
    code, out = run_main(vrs, [str(run_dir), str(run_dir)], monkeypatch,
                         capsys)
    assert code == 0
    lines = out.splitlines()
    assert [line.split(':')[0] for line in lines
            if line.startswith('  WARN')] == [
        '  WARN  seal_format', '  WARN  runner_source_hash',
        '  WARN  runner_modified'] * 2
    assert '  8 passed, 0 failed, 3 warnings' in lines
    assert lines[-1] == 'RESULT: PASS (16 checks, 6 warnings)'


def test_main_failures_print_after_checks_and_warnings(vrs, tmp_path, base,
                                                       monkeypatch, capsys):
    config = resolved_config(runner_modified=True)
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config,
                        transcript=[{'seal_hash': 'other',
                                     'timestamp': record['timestamp']}])
    (base / 'example' / 'fixture.json').write_text('changed\n')
    code, out = run_main(vrs, [str(run_dir)], monkeypatch, capsys)
    assert code == 1
    lines = out.splitlines()
    status = [line.split()[0] for line in lines if line.startswith('  ')
              and line.split()[0] in ('PASS', 'WARN', 'FAIL')]
    # Every PASS first, then every WARN, then every FAIL (the fixture,
    # the expected values computed from it, the transcript).
    assert status == ['PASS'] * 8 + ['WARN'] + ['FAIL'] * 3
    assert lines[-3:] == ['  8 passed, 3 failed, 1 warnings', '',
                          'RESULT: FAIL (3 failures, 1 warnings)']


def test_main_totals_over_several_runs(vrs, run, tmp_path, monkeypatch,
                                       capsys):
    run_dir, _, _ = run
    code, out = run_main(vrs, [str(run_dir), str(tmp_path / 'absent')],
                         monkeypatch, capsys)
    assert code == 1
    assert '=== Verifying: %s ===' % (tmp_path / 'absent') in out
    assert '  FAIL  report exists: report.md not found' in out
    assert '  0 passed, 1 failed' in out
    assert out.endswith('RESULT: FAIL (1 failures)\n')


def test_main_totals_passes_over_passing_runs(vrs, run, monkeypatch,
                                             capsys):
    run_dir, _, _ = run
    code, out = run_main(vrs, [str(run_dir), str(run_dir)], monkeypatch,
                         capsys)
    assert code == 0
    assert out.endswith('RESULT: PASS (22 checks)\n')


def test_main_totals_failures_over_failing_runs(vrs, tmp_path, base,
                                                monkeypatch, capsys):
    code, out = run_main(vrs, [str(tmp_path / 'a'), str(tmp_path / 'b')],
                         monkeypatch, capsys)
    assert code == 1
    assert out.endswith('RESULT: FAIL (2 failures)\n')


def test_main_relative_path_is_taken_from_the_working_directory(
        vrs, base, tmp_path, monkeypatch, capsys):
    # S3-G8-5: as any command-line path; not joined to the repository root.
    config = resolved_config()
    write_run(base / 'output' / 'run_x', make_record(base, config), config)
    monkeypatch.chdir(tmp_path)
    code, out = run_main(vrs, [os.path.join('output', 'run_x')],
                         monkeypatch, capsys)
    assert code == 1
    assert '=== Verifying: %s ===' % os.path.join(
        str(tmp_path), 'output', 'run_x') in out
    monkeypatch.chdir(base)
    code, out = run_main(vrs, [os.path.join('output', 'run_x')],
                         monkeypatch, capsys)
    assert code == 0


def test_main_options_relative_to_the_working_directory(
        vrs, tmp_path, base, monkeypatch, capsys):
    other = tmp_path / 'mine'
    shutil.copytree(base / 'example', other)
    config = resolved_config(ap1_version='v9')
    record = seal(config=config, fixture_path=other / 'fixture.json',
                  questions_path=other / 'questions.json',
                  ground_truth_path=other / 'ground_truth_example.py',
                  ap1_text_path=base / AP1_TEXT,
                  runner_source_hash=TREE_SOURCE_HASH, expected_values={})
    write_run(tmp_path / 'run', record, config)
    monkeypatch.chdir(tmp_path)
    code, out = run_main(vrs, ['--fixture-dir', 'mine', '--ap1-text',
                               os.path.relpath(base / AP1_TEXT), 'run'],
                         monkeypatch, capsys)
    assert code == 0, out


def test_main_help(vrs, monkeypatch, capsys):
    monkeypatch.setenv('COLUMNS', '200')  # one line per help string
    with pytest.raises(SystemExit) as exc:
        run_main(vrs, ['--help'], monkeypatch, capsys)
    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert out.startswith('usage: verify_run_seal.py [-h] [--fixture-dir '
                          'FIXTURE_DIR] [--ap1-text AP1_TEXT]')
    assert 'Relative paths are taken from the working directory.' in out


# -- module ----------------------------------------------------------------

def test_base_dir_is_the_repository_root(vrs):
    assert vrs.BASE_DIR == os.path.dirname(os.path.dirname(TOOL))


# --- Step 4: correct behaviour (failing until fixed) ---
#
# Fixing one finding adds comparisons (timestamp, runner_source_hash) that
# the small tree here may not satisfy, so these tests assert on the named
# check they are about, not on "no failures at all".

def good_config(base, **extra):
    """The resolved config of a run that seals after every fix: the AP-1
    text hash is declared (T3-68 makes it required)."""
    return resolved_config(ap1_text_hash=file_hash(str(base / AP1_TEXT)),
                           **extra)


def good_record(base, config, **kwargs):
    return seal(config=config,
                fixture_path=base / 'example' / 'fixture.json',
                questions_path=base / 'example' / 'questions.json',
                ground_truth_path=base / 'example' / 'ground_truth_example.py',
                ap1_text_path=base / AP1_TEXT,
                runner_source_hash=SOURCE_HASH, **kwargs)


@pytest.fixture
def good_run(tmp_path, base):
    config = good_config(base)
    record = good_record(base, config)
    return write_run(tmp_path / 'run', record, config), record, config


def outcome(vrs, run_dir):
    """verify_run's (checks, failures), or the exception it raised."""
    try:
        checks, failures = vrs.verify_run(str(run_dir))
    except Exception as e:  # a crash is the defect some tests look for
        return None, None, e
    return checks, failures, None


def reseal_all(record):
    """seal_hash over every field but seal_hash itself: the record as a
    seal that binds its timestamp (T3-47) computes it."""
    record = dict(record)
    record['seal_hash'] = canonical_hash(
        {k: v for k, v in record.items() if k != 'seal_hash'})
    return record


def named(entries, word):
    return [name for name, _ in entries if word in name]


@pytest.mark.finding('T3-18')
@pytest.mark.req('R1.1')
def test_verify_run_missing_transcript_fails(vrs, tmp_path, base):
    # Correct (SPEC R1.1 "The record's hash appears on every transcript
    # line"; T3-18): a run without its transcript cannot show that, so
    # the check fails.
    config = good_config(base)
    run_dir = write_run(tmp_path / 'run', good_record(base, config), config,
                        transcript=None)
    checks, failures, _ = outcome(vrs, run_dir)
    assert named(failures, 'transcript'), checks[-1]


@pytest.mark.finding('T3-18')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('bad_line', [2, 3])
def test_verify_run_any_transcript_line_with_other_seal_hash_fails(
        vrs, tmp_path, base, bad_line):
    # Correct (SPEC R1.1): every line's seal_hash is checked; a spliced or
    # misfiled line anywhere fails. (Line 1 is checked today:
    # test_verify_run_transcript_line_1_mismatch_fails.)
    config = good_config(base)
    record = good_record(base, config)
    lines = [{'seal_hash': record['seal_hash'], 'n': n} for n in (1, 2, 3)]
    lines[bad_line - 1]['seal_hash'] = 'spliced'
    run_dir = write_run(tmp_path / 'run', record, config, transcript=lines)
    _, failures, _ = outcome(vrs, run_dir)
    assert named(failures, 'transcript'), 'line %d spliced, no failure' \
        % bad_line


@pytest.mark.finding('T3-18')
def test_verify_run_passes_count_only_real_comparisons(vrs, good_run):
    # Correct (T3-18; Steven's F1 ruling, choices-for-marcus.md entry 5:
    # "verify_run_seal.py drops its two non-checks against on-disk
    # configs"): the passes are hash comparisons only. Parsing the report
    # is a precondition, not a check, and the on-disk configs are not
    # compared at all.
    run_dir, _, _ = good_run
    checks, _, _ = outcome(vrs, run_dir)
    not_comparisons = [name for name in names(checks)
                       if 'parsed' in name or name.startswith('on-disk')]
    assert not_comparisons == []


@pytest.mark.finding('T3-18')
def test_main_result_line_counts_only_real_comparisons(vrs, good_run, monkeypatch,
                                                       capsys):
    # The same at the command line: no PASS line for a parse step or an
    # on-disk notice, and the "N passed" count equals the PASS lines left.
    run_dir, _, _ = good_run
    code, out = run_main(vrs, [str(run_dir)], monkeypatch, capsys)
    passes = [line for line in out.splitlines() if line.startswith('  PASS')]
    assert not [p for p in passes if 'parsed' in p or 'on-disk' in p]
    assert int(re.search(r'(\d+) passed', out).group(1)) == len(passes)


@pytest.mark.finding('S3-G8-2', 'T3-18')
@pytest.mark.parametrize('text', ['', '\n', '\n{"seal_hash": "other"}\n'],
                         ids=['empty', 'blank', 'blank-then-other'])
def test_verify_run_empty_or_blank_transcript_fails(vrs, tmp_path, base,
                                                    text):
    config = good_config(base)
    run_dir = write_run(tmp_path / 'run', good_record(base, config), config,
                        transcript=None)
    (run_dir / 'smoke_run.jsonl').write_text(text)
    _, failures, _ = outcome(vrs, run_dir)
    assert named(failures, 'transcript')


@pytest.mark.finding('S3-G8-3')
def test_verify_run_unparseable_transcript_line_fails_without_crash(
        vrs, tmp_path, base):
    # Correct: a damaged transcript is a FAIL with a reason, not a
    # traceback.
    config = good_config(base)
    run_dir = write_run(tmp_path / 'run', good_record(base, config), config,
                        transcript=None)
    (run_dir / 'smoke_run.jsonl').write_text('not json\n')
    _, failures, crash = outcome(vrs, run_dir)
    assert crash is None, repr(crash)
    assert named(failures, 'transcript')


@pytest.mark.finding('S3-G8-3')
def test_verify_run_fractional_number_in_resolved_config_fails_without_crash(
        vrs, tmp_path, base):
    # Correct: no traceback. Section 2 here differs from the sealed config
    # (temperature added), so config_hash fails, whether the number is
    # read as Decimal or refused with a reason.
    config = good_config(base)
    run_dir = write_run(tmp_path / 'run', good_record(base, config),
                        good_config(base, temperature=0.5))
    _, failures, crash = outcome(vrs, run_dir)
    assert crash is None, repr(crash)
    assert named(failures, 'config')


@pytest.mark.finding('S3-G8-1')
def test_parse_resolved_config_json_block_of_later_section_ignored(vrs):
    text = ('## 2. Resolved Configuration\n\nnone here\n\n'
            '## 7. Something else\n```json\n{"other": true}\n```\n')
    assert vrs.parse_resolved_config(text) is None


@pytest.mark.finding('S3-G8-4')
def test_main_fixture_dir_and_ap1_text_options_name_the_inputs(
        vrs, tmp_path, base, monkeypatch, capsys):
    # Correct: a run made with the runner's --fixture-dir and --ap1-text
    # can be verified, by passing the same options to the verifier.
    other = tmp_path / 'my_fixture'
    other.mkdir()
    for name in ('fixture.json', 'questions.json', 'ground_truth_example.py'):
        (other / name).write_text('mine: %s\n' % name)
    text = tmp_path / 'my_ap1.md'
    text.write_text('# my AP-1 text\n')
    config = resolved_config(ap1_text_hash=file_hash(str(text)))
    record = seal(config=config, fixture_path=other / 'fixture.json',
                  questions_path=other / 'questions.json',
                  ground_truth_path=other / 'ground_truth_example.py',
                  ap1_text_path=text, runner_source_hash=SOURCE_HASH)
    run_dir = write_run(tmp_path / 'run', record, config)
    code, out = run_main(vrs, ['--fixture-dir', str(other), '--ap1-text',
                               str(text), str(run_dir)], monkeypatch, capsys)
    for field in ('fixture_hash', 'questions_hash', 'ground_truth_hash',
                  'ap1_text_hash'):
        assert '  PASS  %s: MATCH' % field in out, out


@pytest.mark.finding('S3-G8-5')
def test_main_relative_path_resolved_against_working_directory(
        vrs, good_run, tmp_path, monkeypatch, capsys):
    run_dir, _, _ = good_run
    monkeypatch.chdir(tmp_path)
    code, out = run_main(vrs, ['run'], monkeypatch, capsys)
    assert '=== Verifying: %s ===' % run_dir in out
    assert 'report.md not found' not in out


@pytest.mark.finding('T3-19')
def test_main_reports_runner_source_hash_mismatch(vrs, tmp_path, base,
                                                  monkeypatch, capsys):
    # Correct (version.py: the hash is sealed "so that a modified
    # instrument is detectable"; T3-19): the verifier recomputes the
    # runner source hash (or compares with a published value) and a
    # mismatch is reported, not passed in silence. 'f' * 64 matches no
    # source tree.
    config = good_config(base)
    record = reseal(dict(good_record(base, config),
                         runner_source_hash='f' * 64))
    run_dir = write_run(tmp_path / 'run', record, config)
    _, out = run_main(vrs, [str(run_dir)], monkeypatch, capsys)
    lines = [line for line in out.splitlines()
             if 'runner_source_hash' in line]
    assert lines, 'runner_source_hash not mentioned:\n' + out
    assert not any(line.startswith('  PASS') for line in lines)


@pytest.mark.finding('T3-19')
def test_main_reports_runner_modified(vrs, tmp_path, base, monkeypatch,
                                      capsys):
    # Correct (T3-19): a run whose sealed config says the runner was
    # modified gets at least a warning; it is not a clean PASS.
    config = good_config(base, runner_modified=True)
    run_dir = write_run(tmp_path / 'run', good_record(base, config), config)
    _, out = run_main(vrs, [str(run_dir)], monkeypatch, capsys)
    lines = [line for line in out.splitlines() if 'modified' in line]
    assert lines, 'runner_modified not mentioned:\n' + out
    assert not any(line.startswith('  PASS') for line in lines)


@pytest.mark.finding('T3-47')
@pytest.mark.req('R1.1')
def test_verify_run_edited_timestamp_fails(vrs, tmp_path, base):
    # Correct (AP-1 v1.3 §5.3, SPEC R1.1): the timestamp is bound by
    # seal_hash, so a timestamp edited in report.md fails verification.
    config = good_config(base)
    record = dict(good_record(base, config),
                  timestamp='2020-01-01T00:00:00+00:00')
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures, _ = outcome(vrs, run_dir)
    assert failures


@pytest.mark.finding('T3-47')
@pytest.mark.req('R1.1')
def test_verify_run_seal_timestamp_after_first_transcript_record_fails(
        vrs, tmp_path, base):
    # Correct (AP-1 v1.3 §5.3 "hashed and timestamped before execution";
    # the brief for step 4): the verifier compares the seal timestamp with
    # the first transcript record's. A seal dated after the first request
    # was not made before execution. seal_hash is consistent here (it
    # binds the timestamp), so the failure has to come from that
    # comparison.
    config = good_config(base)
    record = reseal_all(dict(good_record(base, config),
                             timestamp='2026-10-15T13:00:00+00:00'))
    lines = [{'seal_hash': record['seal_hash'],
              'timestamp': '2026-10-15T12:00:05+00:00'},
             {'seal_hash': record['seal_hash'],
              'timestamp': '2026-10-15T12:00:09+00:00'}]
    run_dir = write_run(tmp_path / 'run', record, config, transcript=lines)
    _, failures, _ = outcome(vrs, run_dir)
    assert named(failures, 'timestamp'), failures


@pytest.mark.finding('T3-49')
def test_verify_run_unknown_ground_truth_mismatch_not_called_expected(
        vrs, good_run, base):
    # Correct: only a sealed hash listed in the errata map gets the errata
    # note; an unknown change to the ground-truth module is a plain
    # failure, with no "expected" wording.
    run_dir, _, _ = good_run
    (base / 'example' / 'ground_truth_example.py').write_text('X = 2\n')
    _, failures, _ = outcome(vrs, run_dir)
    detail = dict(failures)['ground_truth_hash']
    assert 'expected' not in detail.lower(), detail


@pytest.mark.finding('T3-49')
@pytest.mark.skipif(shutil.which('git') is None, reason='needs git')
def test_errata_map_cites_only_commits_in_the_history(vrs):
    # Correct: every commit the errata note cites exists in the
    # repository (eadd862 and 8089923 do not).
    root = os.path.dirname(os.path.dirname(TOOL))
    cited = sorted({c for note in vrs.GROUND_TRUTH_ERRATA.values()
                    for c in re.findall(r'commit ([0-9a-f]{7,40})', note)})
    missing = [c for c in cited if subprocess.call(
        ['git', 'cat-file', '-e', c + '^{commit}'], cwd=root,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0]
    assert missing == []


@pytest.mark.finding('T3-69')
@pytest.mark.parametrize('keys', [['key-1'], ['k1', 'k2']])
def test_verify_run_seal_with_verification_keys_verifies(vrs, tmp_path, base,
                                                         keys):
    # Correct: a genuine seal with non-empty verification_keys verifies;
    # every sealed type is rebuilt (or the rendered form is sealed).
    config = good_config(base)
    record = good_record(base, config, verification_keys=keys)
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures, _ = outcome(vrs, run_dir)
    assert 'seal_hash' not in names(failures)


@pytest.mark.finding('T3-15')
@pytest.mark.req('R1.1')
def test_verify_run_record_missing_sealed_fields_fails(vrs, tmp_path, base):
    # Correct: the verifier knows which fields a seal binds; a record with
    # sealed fields deleted (and seal_hash recomputed over the rest) fails.
    config = good_config(base)
    record = good_record(base, config)
    for dropped in ('ap1_version', 'runner_source_hash', 'verification_keys',
                    'ev3_implemented'):
        del record[dropped]
    run_dir = write_run(tmp_path / 'run', reseal(record), config)
    _, failures, _ = outcome(vrs, run_dir)
    assert failures


@pytest.mark.finding('T3-50')
@pytest.mark.req('R0.4.3')
@pytest.mark.parametrize('field, relpath, data', [
    ('fixture_hash', os.path.join('example', 'fixture.json'),
     b'{"fixture": 1}\r\n'),
    ('questions_hash', os.path.join('example', 'questions.json'),
     b'\xef\xbb\xbf{"items": []}\n'),
    ('ground_truth_hash', os.path.join('example', 'ground_truth_example.py'),
     b'\xef\xbb\xbfX = 1\r\n')], ids=['crlf', 'bom', 'bom-crlf'])
def test_verify_run_same_text_other_line_endings_verifies(vrs, good_run, base,
                                                          field, relpath,
                                                          data):
    # Correct (SPEC R0.4.3 item 1; decision in test_seal.py's step-4
    # section): a checkout or editor that changes only line endings or
    # adds a BOM does not break verification of the sealed text inputs.
    run_dir, _, _ = good_run
    (base / relpath).write_bytes(data)
    checks, failures, _ = outcome(vrs, run_dir)
    assert (field, 'MATCH') in checks, failures


@pytest.mark.finding('F1', 'T3-79')
def test_verify_run_makes_no_check_against_on_disk_configs(vrs, run):
    # Steven's ruling (choices-for-marcus entry 5; decisions file, F1,
    # "Steven's Response 2"): verify_run_seal.py drops its two non-checks
    # against the on-disk files. They always print "does NOT match seal --
    # EXPECTED" and can never fail; once each run's config file is sealed
    # as it stands, they are also untrue.
    run_dir, _, _ = run
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert [name for name in names(checks) if name.startswith('on-disk')] \
        == []
