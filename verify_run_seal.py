"""Verify a published run's seal from its report artifacts alone.

Usage:
    python verify_run_seal.py output/run_a_mini
    python verify_run_seal.py output/run_b_sol

Reads the seal record from report.md section 1 (Pre-Registration Record) and
the resolved configuration from report.md section 2 (Resolved Configuration).
Recomputes all component hashes and the seal_hash. Reports each
comparison individually, pass or fail.

EXIT CODES:
    0 -- all checks pass
    1 -- at least one check failed

NOTE: The on-disk config files (example/config.json, example/config_mini.json)
contain placeholder values for model and endpoint_url. These are overwritten
with runtime values from environment variables BEFORE the seal is computed
(smoke_test.py L358-359). The sealed config_hash therefore matches the
RESOLVED configuration in report.md section 2, NOT the on-disk config file.
A verifier who hashes config.json directly will get a mismatch -- that is
correct behaviour, not a failure.
"""

import json
import os
import re
import sys

# Determine base_dir (ap1-runner root) from this file's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from numeric import canonical_hash, file_hash  # noqa: E402


# -- Known errata for contextual reporting ---------------------------------

# Maps sealed hash values to erratum references. These do NOT change the
# exit code — a mismatch is still a FAIL. They provide context so a reader
# sees that the mismatch is accounted for.
GROUND_TRUTH_ERRATA = {
    "dd3434bc62c4976af928798024d1446993ce59dd473e78cf4002832630314715": (
        "E3: constant '4' declared but never used in Q07 computation; "
        "removed in commit eadd862. D7.2(a) figures withdrawn. "
        "See FINDINGS_ERRATA.md."
    ),
}


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
    """Extract the resolved config JSON from report.md section 2."""
    in_section = False
    in_json = False
    json_lines = []
    for line in report_text.splitlines():
        if '## 2. Resolved Configuration' in line:
            in_section = True
            continue
        if in_section and not in_json:
            if line.strip().startswith('```json'):
                in_json = True
                continue
        if in_json:
            if line.strip().startswith('```'):
                break
            json_lines.append(line)
    if not json_lines:
        return None
    return json.loads('\n'.join(json_lines))


# -- Verification ----------------------------------------------------------

def verify_run(output_dir):
    """Verify one run's seal. Returns (checks, failures)."""
    checks = []
    failures = []

    # 1. Read report.md
    report_path = os.path.join(output_dir, 'report.md')
    if not os.path.exists(report_path):
        failures.append(('report exists', 'report.md not found'))
        return checks, failures
    with open(report_path, encoding='utf-8') as f:
        report_text = f.read()

    # 2. Parse seal record and resolved config
    seal_record = parse_seal_record(report_text)
    if not seal_record:
        failures.append(('seal record parsed',
                         'no seal record found in report.md section 1'))
        return checks, failures
    checks.append(('seal record parsed',
                    '%d fields' % len(seal_record)))

    resolved_config = parse_resolved_config(report_text)
    if resolved_config is None:
        failures.append(('resolved config parsed',
                         'no resolved config found in report.md section 2'))
        return checks, failures
    checks.append(('resolved config parsed',
                    'model=%r' % resolved_config.get('model')))

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
    file_checks = [
        ('fixture_hash',
         os.path.join(BASE_DIR, 'example', 'fixture.json')),
        ('questions_hash',
         os.path.join(BASE_DIR, 'example', 'questions.json')),
        ('ground_truth_hash',
         os.path.join(BASE_DIR, 'example', 'ground_truth_example.py')),
        ('ap1_text_hash',
         os.path.join(BASE_DIR, 'reference',
                      'AP-1_v1.3_DRAFT_FOR_COMMENT.md')),
    ]
    for field, filepath in file_checks:
        sealed_val = seal_record.get(field, '')
        if not os.path.exists(filepath):
            failures.append((field, 'file not found: %s' % filepath))
            continue
        computed_val = file_hash(filepath)
        if sealed_val == computed_val:
            checks.append((field, 'MATCH'))
        else:
            detail = 'sealed=%s, recomputed=%s' % (sealed_val, computed_val)
            # For ground_truth_hash, add erratum context if known
            if field == 'ground_truth_hash':
                erratum = GROUND_TRUTH_ERRATA.get(sealed_val)
                if erratum:
                    detail += '\n          NOTE: %s' % erratum
                detail += ('\n          NOTE: This mismatch is expected. '
                           'The ground-truth module was modified after '
                           'the sealed runs (see FINDINGS_ERRATA.md E3). '
                           'All other sealed hashes reproduce on any platform.')
            failures.append((field, detail))

    # 5. Reconstruct and verify seal_hash
    sealed_seal_hash = seal_record.get('seal_hash', '')
    # Rebuild the hashable record exactly as seal.py does:
    # all fields except 'timestamp' and 'seal_hash'
    hashable = {}
    for k, v in seal_record.items():
        if k in ('timestamp', 'seal_hash'):
            continue
        # Parse stringified values back to their original types
        if v == 'False':
            hashable[k] = False
        elif v == 'True':
            hashable[k] = True
        elif v == '[]':
            hashable[k] = []
        else:
            hashable[k] = v

    computed_seal_hash = canonical_hash(hashable)
    if sealed_seal_hash == computed_seal_hash:
        checks.append(('seal_hash', 'MATCH'))
    else:
        failures.append(('seal_hash',
                         'sealed=%s, recomputed=%s' % (
                             sealed_seal_hash, computed_seal_hash)))

    # 6. Cross-check: seal_hash in transcript matches report
    transcript_path = os.path.join(output_dir, 'smoke_run.jsonl')
    if os.path.exists(transcript_path):
        with open(transcript_path, encoding='utf-8') as f:
            first_line = f.readline()
        if first_line.strip():
            first_rec = json.loads(first_line)
            transcript_seal = first_rec.get('seal_hash', '')
            if transcript_seal == sealed_seal_hash:
                checks.append(('transcript seal_hash',
                                'matches report'))
            else:
                failures.append(('transcript seal_hash',
                                 'report=%s, transcript=%s' % (
                                     sealed_seal_hash, transcript_seal)))
    else:
        checks.append(('transcript seal_hash',
                        'transcript not found (skipped)'))

    return checks, failures


# -- Entry point -----------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print('Usage: python verify_run_seal.py <output_dir> '
              '[<output_dir2> ...]')
        print()
        print('Example:')
        print('  python verify_run_seal.py output/run_a_mini '
              'output/run_b_sol')
        return 1

    total_passed = 0
    total_failed = 0

    for output_dir in sys.argv[1:]:
        # Resolve relative to BASE_DIR if not absolute
        if not os.path.isabs(output_dir):
            output_dir = os.path.join(BASE_DIR, output_dir)

        print('=== Verifying: %s ===' % output_dir)
        print()

        checks, failures = verify_run(output_dir)

        for name, detail in checks:
            print('  PASS  %s: %s' % (name, detail))
        for name, detail in failures:
            print('  FAIL  %s: %s' % (name, detail))

        n_passed = len(checks)
        n_failed = len(failures)
        total_passed += n_passed
        total_failed += n_failed

        print()
        print('  %d passed, %d failed' % (n_passed, n_failed))
        print()

    if total_failed > 0:
        print('RESULT: FAIL (%d failures)' % total_failed)
        return 1
    else:
        print('RESULT: PASS (%d checks)' % total_passed)
        return 0


if __name__ == '__main__':
    sys.exit(main())
