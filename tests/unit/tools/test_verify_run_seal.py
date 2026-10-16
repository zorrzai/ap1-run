"""Unit tests for tools/verify_run_seal.py, the published-run seal verifier.

They pin what the tool does today, defects included. The seal record is
made by the runner's own seal() and rendered as report.py renders
sections 1 and 2, so a passing case is what a real run would give.

The tool reads the fixture, questions, ground truth, AP-1 text and on-disk
configs from fixed paths under its BASE_DIR (the repository root). Each
test points BASE_DIR at a small tree under tmp_path.
"""

import hashlib
import importlib.util
import json
import os
import sys

import pytest

from ap1_run.execution.seal import seal
from ap1_run.foundation.numeric import canonical_hash, file_hash

TOOL = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))), 'tools',
    'verify_run_seal.py')

SOURCE_HASH = 'ab' * 32


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
    """BASE_DIR: the example inputs, the AP-1 text and the two on-disk
    configs, with placeholder model and endpoint."""
    root = tmp_path / 'repo'
    (root / 'example').mkdir(parents=True)
    (root / 'reference').mkdir()
    (root / 'example' / 'fixture.json').write_text('{"fixture": 1}\n')
    (root / 'example' / 'questions.json').write_text('{"items": []}\n')
    (root / 'example' / 'ground_truth_example.py').write_text('X = 1\n')
    (root / AP1_TEXT).write_text('# AP-1 text\n')
    for name in ('config.json', 'config_mini.json'):
        (root / 'example' / name).write_text(json.dumps(
            {'model': 'REPLACE', 'endpoint_url': 'REPLACE'}))
    monkeypatch.setattr(vrs, 'BASE_DIR', str(root))
    return root


def resolved_config(**extra):
    config = {'model': 'gpt-test', 'endpoint_url': 'https://example.test',
              'answer_tolerance': '0.01', 'repeat_count': 2,
              'ap1_version': 'v1.3-test', 'ap1_version_doi': '10.0/test',
              'runner_version_tag': 'v1.3.1',
              'runner_version_commit': 'e0d9ec9', 'runner_modified': False}
    config.update(extra)
    return config


def make_record(base, config):
    """The seal record the runner makes for these inputs."""
    return seal(config=config,
                fixture_path=base / 'example' / 'fixture.json',
                questions_path=base / 'example' / 'questions.json',
                ground_truth_path=base / 'example' / 'ground_truth_example.py',
                ap1_text_path=base / AP1_TEXT,
                runner_source_hash=SOURCE_HASH)


def reseal(record):
    """Recompute seal_hash over the record as seal() does: every field
    but the timestamp and the hash itself."""
    record = dict(record)
    hashable = {k: v for k, v in record.items()
                if k not in ('timestamp', 'seal_hash')}
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
        transcript = [{'seal_hash': record['seal_hash'], 'n': 1},
                      {'seal_hash': record['seal_hash'], 'n': 2}]
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


ON_DISK_EXPECTED = ('does NOT match seal -- EXPECTED. The on-disk config '
                    'contains placeholder model/endpoint that differ from '
                    'the runtime values. Use the RESOLVED config from '
                    'report.md section 2, not the on-disk file.')

ALL_CHECKS = [
    ('seal record parsed', '14 fields'),
    ('resolved config parsed', "model='gpt-test'"),
    ('config_hash', 'MATCH'),
    ('on-disk config.json', ON_DISK_EXPECTED),
    ('on-disk config_mini.json', ON_DISK_EXPECTED),
    ('fixture_hash', 'MATCH'),
    ('questions_hash', 'MATCH'),
    ('ground_truth_hash', 'MATCH'),
    ('ap1_text_hash', 'MATCH'),
    ('seal_hash', 'MATCH'),
    ('transcript seal_hash', 'matches report'),
]


def names(entries):
    return [name for name, _ in entries]


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


@pytest.mark.finding('S3-G8-1')
def test_parse_resolved_config_takes_json_block_of_a_later_section(vrs):
    # Section 2 does not end at the next heading: with no block in
    # section 2, a json block in any later section is read as the
    # resolved configuration. Correct: only section 2's block, else None.
    text = ('## 2. Resolved Configuration\n\nnone here\n\n'
            '## 7. Something else\n```json\n{"other": true}\n```\n')
    assert vrs.parse_resolved_config(text) == {'other': True}


def test_parse_resolved_config_invalid_json_raises(vrs):
    with pytest.raises(json.JSONDecodeError):
        vrs.parse_resolved_config(
            '## 2. Resolved Configuration\n```json\n{oops}\n```\n')


# -- verify_run: a run that matches ---------------------------------------

def test_verify_run_matching_run_passes_every_check(vrs, run):
    run_dir, _, _ = run
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert checks == ALL_CHECKS


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
    report = '## 1. Pre-Registration Record\n| `seal_hash` | `x` |\n'
    run_dir = write_run(tmp_path / 'run', {'seal_hash': 'x'}, {},
                        report=report)
    checks, failures = vrs.verify_run(str(run_dir))
    assert checks == [('seal record parsed', '1 fields')]
    assert failures == [('resolved config parsed',
                         'no resolved config found in report.md section 2')]


@pytest.mark.parametrize('field, relpath', [
    ('fixture_hash', os.path.join('example', 'fixture.json')),
    ('questions_hash', os.path.join('example', 'questions.json')),
    ('ground_truth_hash', os.path.join('example', 'ground_truth_example.py')),
    ('ap1_text_hash', AP1_TEXT),
])
def test_verify_run_missing_input_file_fails_with_its_path(vrs, run, base,
                                                           field, relpath):
    run_dir, _, _ = run
    os.remove(base / relpath)
    checks, failures = vrs.verify_run(str(run_dir))
    path = os.path.join(str(base), relpath)
    assert failures == [(field, f'file not found: {path}')]
    # The other inputs are still checked.
    assert checks == [c for c in ALL_CHECKS if c[0] != field]


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
    assert looked_up == [
        os.path.join(str(run_dir), 'report.md'),
        os.path.join(b, 'example', 'config.json'),
        os.path.join(b, 'example', 'config_mini.json'),
        os.path.join(b, 'example', 'fixture.json'),
        os.path.join(b, 'example', 'questions.json'),
        os.path.join(b, 'example', 'ground_truth_example.py'),
        os.path.join(b, 'reference', 'AP-1_v1.3_DRAFT_FOR_COMMENT.md'),
        os.path.join(str(run_dir), 'smoke_run.jsonl'),
    ]


def test_verify_run_reads_text_files_as_utf8(vrs, run, monkeypatch):
    # Not the platform's default encoding (cp1252 on Windows).
    run_dir, _, _ = run
    encodings = []
    real_open = open

    def recording_open(path, *args, **kwargs):
        encodings.append(kwargs.get('encoding'))
        return real_open(path, *args, **kwargs)
    monkeypatch.setattr(vrs, 'open', recording_open, raising=False)
    vrs.verify_run(str(run_dir))
    # report.md, the two on-disk configs, the transcript.
    assert len(encodings) == 4
    assert all(e is not None and e.lower() == 'utf-8' for e in encodings)


def test_verify_run_missing_on_disk_configs_are_not_mentioned(vrs, run, base):
    run_dir, _, _ = run
    os.remove(base / 'example' / 'config.json')
    os.remove(base / 'example' / 'config_mini.json')
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert names(checks) == [n for n in names(ALL_CHECKS)
                             if not n.startswith('on-disk')]


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


def test_verify_run_missing_config_hash_field_shows_empty_sealed_value(
        vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    shown = reseal({k: v for k, v in record.items() if k != 'config_hash'})
    run_dir = write_run(tmp_path / 'run', shown, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('config_hash', 'sealed=, recomputed=%s'
                         % record['config_hash'])]


def test_verify_run_missing_file_hash_field_shows_empty_sealed_value(
        vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    shown = reseal({k: v for k, v in record.items() if k != 'fixture_hash'})
    run_dir = write_run(tmp_path / 'run', shown, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('fixture_hash', 'sealed=, recomputed=%s'
                         % record['fixture_hash'])]


def test_verify_run_config_hash_is_canonical_json_sha256(vrs, tmp_path,
                                                         base):
    # The verifier hashes the resolved config as canonical JSON: sorted
    # keys, no whitespace, UTF-8. A seal over another serialisation fails.
    config = {'model': 'm', 'b': [1, 'é']}
    expected = hashlib.sha256(
        '{"b":[1,"é"],"model":"m"}'.encode('utf-8')).hexdigest()
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
    assert failures == [(field, 'sealed=%s, recomputed=%s' % (
        record[field], file_hash(str(base / relpath))))]
    assert field not in names(checks)


def test_verify_run_hashes_raw_bytes_line_endings_count(vrs, run, base):
    run_dir, _, _ = run
    (base / 'example' / 'fixture.json').write_bytes(b'{"fixture": 1}\r\n')
    _, failures = vrs.verify_run(str(run_dir))
    assert names(failures) == ['fixture_hash']


GT_EXPECTED_NOTE = (
    '\n          NOTE: This mismatch is expected. The ground-truth module '
    'was modified after the sealed runs: E3 removed an unused constant '
    'from Q07, and the Q05 sign-convention correction removed the '
    'negation (F10). All other sealed hashes reproduce on any platform.')


def test_verify_run_ground_truth_known_erratum_adds_both_notes(
        vrs, tmp_path, base):
    known = next(iter(vrs.GROUND_TRUTH_ERRATA))
    config = resolved_config()
    record = reseal(dict(make_record(base, config), ground_truth_hash=known))
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    computed = file_hash(str(base / 'example' / 'ground_truth_example.py'))
    assert failures == [('ground_truth_hash',
                         'sealed=%s, recomputed=%s' % (known, computed)
                         + '\n          NOTE: '
                         + vrs.GROUND_TRUTH_ERRATA[known]
                         + GT_EXPECTED_NOTE)]


@pytest.mark.finding('T3-49')
def test_verify_run_any_ground_truth_mismatch_is_called_expected(vrs, run,
                                                                 base):
    # A ground-truth module changed for any reason is labelled "expected"
    # and blamed on E3/F10. Correct: the NOTE only for a known erratum.
    run_dir, record, _ = run
    (base / 'example' / 'ground_truth_example.py').write_text('X = 2\n')
    _, failures = vrs.verify_run(str(run_dir))
    computed = file_hash(str(base / 'example' / 'ground_truth_example.py'))
    assert failures == [('ground_truth_hash',
                         'sealed=%s, recomputed=%s' % (
                             record['ground_truth_hash'], computed)
                         + GT_EXPECTED_NOTE)]


def test_verify_run_errata_map_today(vrs):
    assert list(vrs.GROUND_TRUTH_ERRATA) == [
        'dd3434bc62c4976af928798024d1446993ce59dd473e78cf4002832630314715']


def test_verify_run_seal_hash_mismatch_fails_with_both_hashes(
        vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    shown = dict(record, seal_hash='0' * 64)
    run_dir = write_run(tmp_path / 'run', shown, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('seal_hash', 'sealed=%s, recomputed=%s' % (
        '0' * 64, record['seal_hash'])), ]


def test_verify_run_missing_seal_hash_field_fails(vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    shown = {k: v for k, v in record.items() if k != 'seal_hash'}
    run_dir = write_run(tmp_path / 'run', shown, config,
                        transcript=[{'seal_hash': ''}])
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == [('seal_hash', 'sealed=, recomputed=%s' %
                         record['seal_hash'])]
    # The transcript's empty seal_hash "matches" the report's missing one.
    assert ('transcript seal_hash', 'matches report') in checks


@pytest.mark.finding('T3-69')
def test_verify_run_rebuilds_only_true_false_and_empty_list(vrs, tmp_path,
                                                            base):
    # The record is read back as strings; only 'True', 'False' and '[]'
    # get their types back. A genuine seal with non-empty
    # verification_keys fails the seal_hash check. Correct: rebuild every
    # sealed type (or seal the rendered form).
    config = resolved_config()
    record = make_record(base, config)
    record['verification_keys'] = ['key-1']
    record = reseal(record)
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert names(failures) == ['seal_hash']


def test_verify_run_true_string_is_rebuilt_as_boolean(vrs, tmp_path, base):
    config = resolved_config()
    record = reseal(dict(make_record(base, config), ev3_implemented=True))
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == []


# -- verify_run: what is not compared (defects) ------------------------------

@pytest.mark.finding('T3-47')
def test_verify_run_changed_timestamp_still_passes(vrs, tmp_path, base):
    # The timestamp is outside seal_hash, and nothing compares it with
    # the transcript. Correct: a backdated timestamp is detected.
    config = resolved_config()
    record = dict(make_record(base, config),
                  timestamp='2020-01-01T00:00:00+00:00')
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == []


@pytest.mark.finding('T3-19')
def test_verify_run_runner_source_hash_is_never_compared(vrs, tmp_path,
                                                         base):
    # Any runner_source_hash passes, provided seal_hash is recomputed: the
    # verifier never hashes the runner source. Correct: recompute it (or
    # compare with a published value) and report a mismatch.
    config = resolved_config()
    record = reseal(dict(make_record(base, config),
                         runner_source_hash='f' * 64))
    run_dir = write_run(tmp_path / 'run', record, config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert 'runner_source_hash' not in names(checks)


@pytest.mark.finding('T3-19')
def test_verify_run_is_silent_about_runner_modified(vrs, tmp_path, base):
    # The resolved config says the runner was modified; the verifier
    # passes without a word. Correct: at least a warning.
    config = resolved_config(runner_modified=True)
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert checks == ALL_CHECKS
    assert not any('modified' in detail for _, detail in checks)


@pytest.mark.finding('T3-15')
def test_verify_run_seal_hash_recomputed_from_record_itself(vrs, tmp_path,
                                                             base):
    # seal_hash is recomputed from whatever fields the report shows, so a
    # record with a sealed field deleted (and seal_hash recomputed) passes.
    # Correct: the verifier knows which fields a seal must bind.
    config = resolved_config()
    record = make_record(base, config)
    for dropped in ('ap1_version', 'ap1_version_doi', 'runner_version_tag',
                    'runner_version_commit', 'runner_source_hash',
                    'verification_keys', 'ev3_implemented'):
        del record[dropped]
    record = reseal(record)
    run_dir = write_run(tmp_path / 'run', record, config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert ('seal record parsed', '7 fields') in checks


@pytest.mark.finding('T3-18')
def test_verify_run_missing_transcript_counts_as_a_pass(vrs, tmp_path, base):
    # Correct: a run without its transcript fails the check.
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config, transcript=None)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert checks[-1] == ('transcript seal_hash',
                          'transcript not found (skipped)')


@pytest.mark.finding('T3-18')
def test_verify_run_compares_transcript_line_1_only(vrs, tmp_path, base):
    # Correct: R1.1 puts the seal_hash on every line; every line checked.
    config = resolved_config()
    record = make_record(base, config)
    lines = [{'seal_hash': record['seal_hash']}, {'seal_hash': 'spliced'}]
    run_dir = write_run(tmp_path / 'run', record, config, transcript=lines)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert checks[-1] == ('transcript seal_hash', 'matches report')


def test_verify_run_transcript_line_1_mismatch_fails(vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config,
                        transcript=[{'seal_hash': 'other'}])
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('transcript seal_hash', 'report=%s, transcript=%s'
                         % (record['seal_hash'], 'other'))]


def test_verify_run_transcript_line_1_without_seal_hash_fails(
        vrs, tmp_path, base):
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config,
                        transcript=[{'n': 1}])
    _, failures = vrs.verify_run(str(run_dir))
    assert failures == [('transcript seal_hash', 'report=%s, transcript='
                         % record['seal_hash'])]


@pytest.mark.finding('S3-G8-2')
def test_verify_run_blank_first_transcript_line_skips_check_silently(
        vrs, tmp_path, base):
    # An empty transcript (or a blank first line) gives neither a pass
    # nor a failure: the check just disappears. Correct: a failure.
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config, transcript=None)
    (run_dir / 'smoke_run.jsonl').write_text(
        '\n' + json.dumps({'seal_hash': 'other'}) + '\n')
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert 'transcript seal_hash' not in names(checks)
    assert len(checks) == len(ALL_CHECKS) - 1


@pytest.mark.finding('S3-G8-3')
def test_verify_run_unparseable_first_transcript_line_raises(vrs, tmp_path,
                                                             base):
    # The verifier crashes with a traceback instead of reporting a FAIL.
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config, transcript=None)
    (run_dir / 'smoke_run.jsonl').write_text('not json\n')
    with pytest.raises(json.JSONDecodeError):
        vrs.verify_run(str(run_dir))


@pytest.mark.finding('S3-G8-3')
def test_verify_run_float_in_resolved_config_raises(vrs, tmp_path, base):
    # canonical_hash refuses floats; a report whose section 2 holds a
    # JSON number with a fraction crashes the verifier. Correct: a FAIL
    # (or parse numbers as Decimal, as the runner's config loader does).
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record,
                        resolved_config(temperature=0.5))
    with pytest.raises(Exception):
        vrs.verify_run(str(run_dir))


@pytest.mark.finding('T3-18')
def test_verify_run_on_disk_config_matching_seal_is_a_pass(vrs, tmp_path,
                                                           base):
    # The on-disk notices are reported as passed checks, whichever way
    # they go: "matches seal (unexpected)" is a PASS too. Correct: they
    # are notes, not checks, and not counted.
    config = resolved_config()
    (base / 'example' / 'config.json').write_text(json.dumps(config))
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config)
    checks, failures = vrs.verify_run(str(run_dir))
    assert failures == []
    assert ('on-disk config.json', 'matches seal (unexpected)') in checks


@pytest.mark.finding('S3-G8-4')
def test_verify_run_reads_inputs_from_base_dir_not_the_run(vrs, tmp_path,
                                                           base):
    # The inputs are always BASE_DIR/example and BASE_DIR/reference. A run
    # made with --fixture-dir / --ap1-text elsewhere cannot be verified;
    # there is no option to name its inputs. Correct: options matching
    # the runner's (or inputs recorded in the run).
    other = tmp_path / 'my_fixture'
    other.mkdir()
    (other / 'fixture.json').write_text('{"fixture": "mine"}\n')
    config = resolved_config()
    record = seal(config=config, fixture_path=other / 'fixture.json',
                  questions_path=base / 'example' / 'questions.json',
                  ground_truth_path=base / 'example' /
                  'ground_truth_example.py',
                  ap1_text_path=base / AP1_TEXT,
                  runner_source_hash=SOURCE_HASH)
    run_dir = write_run(tmp_path / 'run', record, config)
    _, failures = vrs.verify_run(str(run_dir))
    assert names(failures) == ['fixture_hash']


# -- main -------------------------------------------------------------------

def run_main(vrs, argv, monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['verify_run_seal.py'] + argv)
    code = vrs.main()
    return code, capsys.readouterr().out


def test_main_without_arguments_prints_usage_and_returns_1(vrs, monkeypatch,
                                                          capsys):
    code, out = run_main(vrs, [], monkeypatch, capsys)
    assert code == 1
    assert out == ('Usage: python tools/verify_run_seal.py <output_dir> '
                   '[<output_dir2> ...]\n\nExample:\n'
                   '  python tools/verify_run_seal.py output/run_a_mini '
                   'output/run_b_sol\n')


@pytest.mark.finding('T3-18')
def test_main_passing_run_prints_each_check_and_counts_them(vrs, run,
                                                            monkeypatch,
                                                            capsys):
    # "11 checks" counts the two parse steps and the two on-disk notices
    # as passed checks (T3-18).
    run_dir, _, _ = run
    code, out = run_main(vrs, [str(run_dir)], monkeypatch, capsys)
    assert code == 0
    expected = ['=== Verifying: %s ===' % run_dir, '']
    expected += ['  PASS  %s: %s' % c for c in ALL_CHECKS]
    expected += ['', '  11 passed, 0 failed', '', 'RESULT: PASS (11 checks)',
                 '']
    assert out == '\n'.join(expected)


def test_main_failures_print_after_checks_and_return_1(vrs, tmp_path, base,
                                                       monkeypatch, capsys):
    config = resolved_config()
    record = make_record(base, config)
    run_dir = write_run(tmp_path / 'run', record, config,
                        transcript=[{'seal_hash': 'other'}])
    (base / 'example' / 'fixture.json').write_text('changed\n')
    code, out = run_main(vrs, [str(run_dir)], monkeypatch, capsys)
    assert code == 1
    lines = out.splitlines()
    status = [line.split()[0] for line in lines if line.startswith('  ')
              and line.split()[0] in ('PASS', 'FAIL')]
    # Every PASS first, then every FAIL, whatever the order of the checks.
    assert status == ['PASS'] * 9 + ['FAIL'] * 2
    assert lines[-3:] == ['  9 passed, 2 failed', '', 'RESULT: FAIL (2 failures)']


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


@pytest.mark.finding('S3-G8-5')
def test_main_relative_path_is_resolved_against_base_dir_not_cwd(
        vrs, run, base, tmp_path, monkeypatch, capsys):
    # A relative argument is joined to the repository root, not to the
    # working directory: from elsewhere, a path that exists is "not
    # found". Correct: relative to the working directory (as the usage
    # line implies when run from the root).
    run_dir, _, _ = run
    monkeypatch.chdir(tmp_path)
    code, out = run_main(vrs, ['run'], monkeypatch, capsys)
    assert code == 1
    assert '=== Verifying: %s ===' % os.path.join(str(base), 'run') in out
    assert 'report.md not found' in out


def test_main_relative_path_under_base_dir_is_found(vrs, base, monkeypatch,
                                                    capsys):
    config = resolved_config()
    record = make_record(base, config)
    write_run(base / 'output' / 'run_x', record, config)
    code, out = run_main(vrs, [os.path.join('output', 'run_x')],
                         monkeypatch, capsys)
    assert code == 0
    assert out.endswith('RESULT: PASS (11 checks)\n')


# -- module ----------------------------------------------------------------

def test_base_dir_is_the_repository_root(vrs):
    assert vrs.BASE_DIR == os.path.dirname(os.path.dirname(TOOL))
