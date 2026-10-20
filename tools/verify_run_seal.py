"""Verify a published run's seal from its report artifacts alone.

Usage:
    python tools/verify_run_seal.py output/run_a_mini
    python tools/verify_run_seal.py output/run_b_sol
    python tools/verify_run_seal.py --fixture-dir my/fixture \\
        --ap1-text my/ap1.md runs/today

Reads the seal record from report.md section 1 (Pre-Registration Record) and
the resolved configuration from report.md section 2 (Resolved Configuration).
Recomputes all component hashes and the seal_hash, and checks that every
line of the run's transcript carries the seal_hash and that the seal is
dated no later than the first transcript record. Reports each comparison
individually, pass or fail; what it cannot check, or what a reader should
know, is a warning, never a pass.

The inputs are read from example/ and the AP-1 text from reference/ (the
text of the run's ap1_version), unless --fixture-dir and --ap1-text name
them, as for the runner. Relative paths are taken from the working
directory.

A record with a seal_format field (runs since October 2026) is checked
under the current rules: the record holds every sealed field, seal_hash
covers the timestamp, the text inputs are hashed with LF line endings and
no BOM, and the expected values and the runner source hash are recomputed.
A record without one (the published runs) is checked under the rules it
was made with: raw bytes, and a seal_hash without the timestamp.

EXIT CODES:
    0 -- all checks pass
    1 -- at least one check failed

NOTE: The on-disk config files (example/config.json, example/config_mini.json)
contain placeholder values for model and endpoint_url. These are overwritten
with runtime values from environment variables BEFORE the seal is computed
(src/ap1_run/run.py, main()). The sealed config_hash therefore matches the
RESOLVED configuration in report.md section 2, NOT the on-disk config file.
A verifier who hashes config.json directly will get a mismatch -- that is
correct behaviour, not a failure.
"""

import argparse
import ast
import json
import os
import re
import sys
from datetime import datetime
from decimal import Decimal

# Determine base_dir (the repository root) from this file's location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    import ap1_run  # noqa: F401
except ImportError:  # not installed: run from a clone
    sys.path.insert(0, os.path.join(BASE_DIR, 'src'))

from ap1_run.execution.ap1_texts import ap1_text_entry  # noqa: E402
from ap1_run.execution.seal import (  # noqa: E402
    SEAL_FORMAT, SEALED_FIELDS, expected_values_hash, text_file_hash,
)
from ap1_run.execution.sealed_inputs import (  # noqa: E402
    INPUT_FILES, compute_expected_values, load_ground_truth, parse_json_input,
)
from ap1_run.execution.version import compute_runner_source_hash  # noqa: E402
from ap1_run.foundation.numeric import canonical_hash, file_hash  # noqa: E402


# -- Known errata for contextual reporting ---------------------------------

# Maps sealed ground-truth hashes to what is known about them. These do NOT
# change the exit code -- a mismatch is still a FAIL. Only a hash listed
# here gets a note; any other mismatch is reported as it is.
GROUND_TRUTH_ERRATA = {
    "dd3434bc62c4976af928798024d1446993ce59dd473e78cf4002832630314715": (
        "August seals. E3: constant '4' declared but never used in Q07's "
        "computation; removed in commit 85e8eeb. D7.2(a) figures withdrawn. "
        "F10/Q05: sign negation removed (commit 6be2d7b). The seal hashed "
        "the module of commit 203fef4 with CRLF line endings. "
        "See findings/FINDINGS_ERRATA.md."
    ),
    "033ce73d933d6e52a7d4f63b3888bdccfa492ce49cf49228ed2f3dda0d27a643": (
        "September seals: the module is unchanged since them (last commit "
        "ff8c051), but the seal hashed it with CRLF line endings; with CRLF "
        "restored the hash matches. See findings/FINDINGS_ERRATA.md, N2."
    ),
}

# How many offending transcript lines a failure lists.
SHOWN_LINES = 5


# -- Report parsing --------------------------------------------------------

def parse_seal_record(report_text):
    """Extract the seal record from report.md section 1 (markdown table)."""
    record = {}
    in_table = False
    for line in report_text.splitlines():
        if '## 1. Pre-Registration Record' in line:
            in_table = True
            continue
        if in_table and line.startswith('## '):
            break
        if not in_table:
            continue
        # Parse table rows: | `field` | `value` |
        m = re.match(r'\|\s*`([^`]+)`\s*\|\s*`([^`]*)`\s*\|', line)
        if m:
            key, val = m.group(1), m.group(2)
            record[key] = val
    return record


def parse_resolved_config(report_text):
    """Extract the resolved config JSON from report.md section 2: the first
    json block before the next section heading (S3-G8-1). Numbers with a
    fraction are read as Decimal, never float. Raises ValueError
    (json.JSONDecodeError) if the block is not JSON."""
    in_section = False
    in_json = False
    json_lines = []
    for line in report_text.splitlines():
        if '## 2. Resolved Configuration' in line:
            in_section = True
            continue
        if in_section and not in_json:
            if line.startswith('## '):
                break
            if line.strip().startswith('```json'):
                in_json = True
                continue
        if in_json:
            if line.strip().startswith('```'):
                break
            json_lines.append(line)
    if not json_lines:
        return None
    return json.loads('\n'.join(json_lines), parse_float=Decimal)


def rebuild_record(seal_record):
    """The sealed values, from their rendering in report.md: report.py
    writes str(value), so verification_keys is a Python list literal and
    ev3_implemented 'True' or 'False'; every other field is a string
    (T3-69). Raises ValueError for a value that cannot be read back."""
    record = dict(seal_record)
    if 'verification_keys' in record:
        try:
            keys = ast.literal_eval(record['verification_keys'])
        except (ValueError, SyntaxError) as e:
            raise ValueError('verification_keys %r: %s'
                             % (record['verification_keys'], e)) from e
        if not isinstance(keys, list):
            raise ValueError('verification_keys %r is not a list'
                             % record['verification_keys'])
        record['verification_keys'] = keys
    if 'ev3_implemented' in record:
        flag = record['ev3_implemented']
        if flag not in ('True', 'False'):
            raise ValueError('ev3_implemented %r is not True or False' % flag)
        record['ev3_implemented'] = flag == 'True'
    return record


def read_transcript(path):
    """The transcript's records, and a list of problems (line number and
    what is wrong): a blank line, a line that is not a JSON object."""
    records, problems = [], []
    with open(path, encoding='utf-8') as f:
        for n, line in enumerate(f, 1):
            if not line.strip():
                problems.append('line %d is blank' % n)
                continue
            try:
                record = json.loads(line)
            except ValueError as e:
                problems.append('line %d is not JSON (%s)' % (n, e))
                continue
            if not isinstance(record, dict):
                problems.append('line %d is not a JSON object' % n)
                continue
            records.append((n, record))
    return records, problems


def _listed(problems):
    shown = '; '.join(problems[:SHOWN_LINES])
    if len(problems) > SHOWN_LINES:
        shown += '; and %d more' % (len(problems) - SHOWN_LINES)
    return shown


def _timestamp(value):
    """An ISO-8601 timestamp with its zone as a datetime, or None."""
    try:
        stamp = datetime.fromisoformat(str(value))
    except ValueError:
        return None
    return stamp if stamp.tzinfo is not None else None


# -- Verification ----------------------------------------------------------

def _ap1_text_path(resolved_config, ap1_text):
    """The AP-1 text to compare: --ap1-text, else the text of the run's
    ap1_version under BASE_DIR (V12-4), else None."""
    if ap1_text:
        return ap1_text
    entry = ap1_text_entry(resolved_config.get('ap1_version', ''))
    return os.path.join(BASE_DIR, entry['path']) if entry else None


def _check_expected_values(seal_record, paths, checks, failures):
    """Recompute the expected values from the inputs (T3-48): load the
    ground-truth module from its file and run it on every item."""
    sealed = seal_record.get('expected_values_hash', '')
    if not sealed:
        failures.append(('expected_values_hash',
                         'the record seals no expected values'))
        return
    fixture_dir = os.path.dirname(paths['ground_truth'])
    sys.path.insert(0, fixture_dir)  # as the runner: for sibling modules
    try:
        data = {}
        for name, path in paths.items():
            with open(path, 'rb') as f:
                data[name] = f.read()
        module = load_ground_truth(paths['ground_truth'],
                                   data['ground_truth'])
        values = compute_expected_values(
            module, parse_json_input(data['fixture']),
            parse_json_input(data['questions']))
        computed = expected_values_hash(values)
    except Exception as e:  # any failure of the module is a failed check
        failures.append(('expected_values_hash', 'cannot recompute: %s: %s'
                         % (type(e).__name__, e)))
        return
    finally:
        sys.path.remove(fixture_dir)
    if computed == sealed:
        checks.append(('expected_values_hash', 'MATCH'))
    else:
        failures.append(('expected_values_hash', 'sealed=%s, recomputed=%s'
                         % (sealed, computed)))


def _check_transcript(output_dir, seal_record, checks, failures):
    """Every transcript line carries the report's seal_hash (T3-18); the
    seal is dated no later than the first transcript record (T3-47)."""
    sealed_seal_hash = seal_record.get('seal_hash', '')
    transcript_path = os.path.join(output_dir, 'smoke_run.jsonl')
    if not os.path.exists(transcript_path):
        failures.append(('transcript seal_hash',
                         'transcript not found: %s' % transcript_path))
        return
    records, problems = read_transcript(transcript_path)
    if not records and not problems:
        failures.append(('transcript seal_hash', 'the transcript is empty'))
        return
    for n, record in records:
        if record.get('seal_hash') != sealed_seal_hash:
            problems.append('line %d has seal_hash %r'
                            % (n, record.get('seal_hash')))
    problems.sort(key=lambda p: int(p.split()[1]))
    if problems:
        failures.append(('transcript seal_hash', 'report=%s; %s' % (
            sealed_seal_hash, _listed(problems))))
    else:
        checks.append(('transcript seal_hash',
                       'all %d lines match report' % len(records)))

    if not records:
        return
    sealed_at = _timestamp(seal_record.get('timestamp'))
    n, first = records[0]
    first_at = _timestamp(first.get('timestamp'))
    if sealed_at is None:
        failures.append(('seal timestamp', 'not an ISO-8601 time with a '
                         'zone: %r' % seal_record.get('timestamp')))
    elif first_at is None:
        failures.append(('seal timestamp', 'transcript line %d has no '
                         'ISO-8601 timestamp with a zone: %r'
                         % (n, first.get('timestamp'))))
    elif sealed_at > first_at:
        failures.append(('seal timestamp', '%s is after the first '
                         'transcript record (%s): the run was not sealed '
                         'before execution' % (seal_record['timestamp'],
                                               first['timestamp'])))
    else:
        checks.append(('seal timestamp', 'before the first transcript '
                       'record (%s)' % first['timestamp']))


def verify_run(output_dir, fixture_dir=None, ap1_text=None, warnings=None):
    """Verify one run's seal. Returns (checks, failures): the comparisons
    that passed and those that failed, each (name, detail). Notes that are
    neither (what is not checked, the runner reported as modified) are
    appended to `warnings` if a list is given."""
    checks = []
    failures = []
    if warnings is None:
        warnings = []
    if fixture_dir is None:
        fixture_dir = os.path.join(BASE_DIR, 'example')

    # 1. Read report.md
    report_path = os.path.join(output_dir, 'report.md')
    if not os.path.exists(report_path):
        failures.append(('report exists', 'report.md not found'))
        return checks, failures
    with open(report_path, encoding='utf-8') as f:
        report_text = f.read()

    # 2. Parse seal record and resolved config: preconditions, not checks
    seal_record = parse_seal_record(report_text)
    if not seal_record:
        failures.append(('seal record parsed',
                         'no seal record found in report.md section 1'))
        return checks, failures

    try:
        resolved_config = parse_resolved_config(report_text)
    except ValueError as e:
        failures.append(('resolved config parsed',
                         'report.md section 2 is not JSON: %s' % e))
        return checks, failures
    if resolved_config is None:
        failures.append(('resolved config parsed',
                         'no resolved config found in report.md section 2'))
        return checks, failures

    # The record's format decides the rules (see the module docstring).
    record_format = seal_record.get('seal_format')
    current_format = record_format is not None
    if current_format and record_format != SEAL_FORMAT:
        failures.append(('seal_format', 'unknown format %r (this verifier '
                         'reads %r)' % (record_format, SEAL_FORMAT)))
        return checks, failures
    if current_format:
        # T3-15: the record holds exactly the fields a seal binds
        missing = [f for f in SEALED_FIELDS if f not in seal_record]
        extra = sorted(set(seal_record) - set(SEALED_FIELDS)
                       - {'seal_hash'})
        if missing or extra:
            failures.append(('seal record fields', '; '.join(
                part for part in (
                    'missing ' + ', '.join(missing) if missing else '',
                    'not sealed by the runner ' + ', '.join(extra)
                    if extra else '') if part)))
        else:
            checks.append(('seal record fields',
                           'all %d sealed fields present'
                           % len(SEALED_FIELDS)))
    else:
        warnings.append(('seal_format', 'none: a record made before '
                         'October 2026, checked under the rules it was made '
                         'with (raw bytes, seal_hash without the timestamp)'))
    text_hash_of = text_file_hash if current_format else file_hash

    # 3. Recompute config_hash from resolved config
    sealed_config_hash = seal_record.get('config_hash', '')
    computed_config_hash = canonical_hash(resolved_config)
    if sealed_config_hash == computed_config_hash:
        checks.append(('config_hash', 'MATCH'))
    else:
        failures.append(('config_hash',
                         'sealed=%s, recomputed=%s' % (
                             sealed_config_hash, computed_config_hash)))

    # 3b. TRAP CHECK: warn if on-disk config would produce a different hash
    for cfg_name in ['config.json', 'config_mini.json']:
        cfg_path = os.path.join(BASE_DIR, 'example', cfg_name)
        if os.path.exists(cfg_path):
            with open(cfg_path, encoding='utf-8') as f:
                disk_config = json.load(f)
            disk_hash = canonical_hash(disk_config)
            if disk_hash == sealed_config_hash:
                checks.append(('on-disk %s' % cfg_name,
                                'matches seal (unexpected)'))
            else:
                checks.append(('on-disk %s' % cfg_name,
                                'does NOT match seal -- EXPECTED. '
                                'The on-disk config contains placeholder '
                                'model/endpoint that differ from the '
                                'runtime values. Use the RESOLVED config '
                                'from report.md section 2, not the on-disk '
                                'file.'))

    # 4. Recompute file hashes
    paths = {name: os.path.join(fixture_dir, filename)
             for name, filename in INPUT_FILES.items()}
    file_checks = [('%s_hash' % name, paths[name]) for name in INPUT_FILES]
    file_checks.append(('ap1_text_hash',
                        _ap1_text_path(resolved_config, ap1_text)))
    for field, filepath in file_checks:
        sealed_val = seal_record.get(field, '')
        if filepath is None:
            failures.append((field, 'no AP-1 text is known for ap1_version '
                             '%r; give it with --ap1-text'
                             % resolved_config.get('ap1_version', '')))
            continue
        if not os.path.exists(filepath):
            failures.append((field, 'file not found: %s' % filepath))
            continue
        # The AP-1 text is hashed as raw bytes (the publisher's deposit)
        computed_val = (file_hash(filepath) if field == 'ap1_text_hash'
                        else text_hash_of(filepath))
        if sealed_val == computed_val:
            checks.append((field, 'MATCH'))
        else:
            detail = 'sealed=%s, recomputed=%s' % (sealed_val, computed_val)
            # A known ground-truth hash gets its erratum (T3-49)
            if field == 'ground_truth_hash':
                erratum = GROUND_TRUTH_ERRATA.get(sealed_val)
                if erratum:
                    detail += '\n          NOTE: %s' % erratum
            failures.append((field, detail))

    # 4b. Expected values and runner source hash (current format only)
    if current_format:
        if all(os.path.exists(p) for p in paths.values()):
            _check_expected_values(seal_record, paths, checks, failures)
        sealed_source = seal_record.get('runner_source_hash', '')
        source_here = compute_runner_source_hash(BASE_DIR)
        if sealed_source == source_here:
            checks.append(('runner_source_hash', 'MATCH'))
        else:
            failures.append(('runner_source_hash', 'sealed=%s, this '
                             'checkout=%s: the run was made with other '
                             'runner code; verify it from a checkout of '
                             'its runner_version_commit (%s)' % (
                                 sealed_source, source_here,
                                 seal_record.get('runner_version_commit',
                                                 ''))))
    elif seal_record.get('runner_source_hash'):
        warnings.append(('runner_source_hash', 'not recomputed: a record '
                         'made before October 2026 hashed every .py file '
                         'of the clone; see docs/REPRODUCING.md'))
    if resolved_config.get('runner_modified') is True:
        warnings.append(('runner_modified', 'the run recorded '
                         'runner_modified: true (VERSION did not name git '
                         'HEAD, or the code had uncommitted changes); '
                         'runner_version_tag does not identify the code'))

    # 5. Reconstruct and verify seal_hash
    sealed_seal_hash = seal_record.get('seal_hash', '')
    # Rebuild the hashable record exactly as seal.py does: all fields
    # except 'seal_hash' (and, in an older record, 'timestamp')
    unhashed = ('seal_hash',) if current_format else ('timestamp',
                                                      'seal_hash')
    try:
        rebuilt = rebuild_record(seal_record)
    except ValueError as e:
        failures.append(('seal_hash', 'cannot read the record: %s' % e))
    else:
        hashable = {k: v for k, v in rebuilt.items() if k not in unhashed}
        computed_seal_hash = canonical_hash(hashable)
        if sealed_seal_hash == computed_seal_hash:
            checks.append(('seal_hash', 'MATCH'))
        else:
            failures.append(('seal_hash',
                             'sealed=%s, recomputed=%s' % (
                                 sealed_seal_hash, computed_seal_hash)))

    # 6. The transcript: every line, and the time of the seal
    _check_transcript(output_dir, seal_record, checks, failures)

    return checks, failures


# -- Entry point -----------------------------------------------------------

USAGE = ('Usage: python tools/verify_run_seal.py [--fixture-dir DIR] '
         '[--ap1-text FILE] <output_dir> [<output_dir2> ...]\n'
         '\n'
         'Example:\n'
         '  python tools/verify_run_seal.py output/run_a_mini '
         'output/run_b_sol')


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog='verify_run_seal.py',
        description='Verify runs\' seals from their report.md and '
                    'transcript. Relative paths are taken from the working '
                    'directory.')
    parser.add_argument(
        '--fixture-dir',
        help='the directory holding the run\'s fixture.json, questions.json '
             'and ground_truth_example.py, as given to the runner '
             '(default: example/)')
    parser.add_argument(
        '--ap1-text',
        help='the AP-1 text the run sealed, as given to the runner '
             '(default: the text of the run\'s ap1_version under '
             'reference/)')
    parser.add_argument('output_dirs', nargs='*', metavar='output_dir')
    args = parser.parse_args(argv)
    for name in ('fixture_dir', 'ap1_text'):
        if getattr(args, name):
            setattr(args, name, os.path.abspath(getattr(args, name)))
    return args


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if not args.output_dirs:
        print(USAGE)
        return 1

    total_passed = 0
    total_failed = 0
    total_warnings = 0

    for output_dir in args.output_dirs:
        # Relative to the working directory, as any command-line path
        output_dir = os.path.abspath(output_dir)

        print('=== Verifying: %s ===' % output_dir)
        print()

        warnings = []
        checks, failures = verify_run(output_dir, args.fixture_dir,
                                      args.ap1_text, warnings)

        for name, detail in checks:
            print('  PASS  %s: %s' % (name, detail))
        for name, detail in warnings:
            print('  WARN  %s: %s' % (name, detail))
        for name, detail in failures:
            print('  FAIL  %s: %s' % (name, detail))

        n_passed = len(checks)
        n_failed = len(failures)
        total_passed += n_passed
        total_failed += n_failed
        total_warnings += len(warnings)

        print()
        line = '  %d passed, %d failed' % (n_passed, n_failed)
        if warnings:
            line += ', %d warnings' % len(warnings)
        print(line)
        print()

    noted = ', %d warnings' % total_warnings if total_warnings else ''
    if total_failed > 0:
        print('RESULT: FAIL (%d failures%s)' % (total_failed, noted))
        return 1
    else:
        print('RESULT: PASS (%d checks%s)' % (total_passed, noted))
        return 0


if __name__ == '__main__':
    sys.exit(main())
