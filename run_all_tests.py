"""AP-1 runner -- full test suite.

Single entry point that invokes each verification suite in its native form
and reports a combined result with both function counts and check counts.

Usage:
    python run_all_tests.py

Exit code 0 if all suites pass, 1 if any fail.
A new suite is added by appending one entry to the SUITES list.
"""

import os
import re
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Suite registry
#
# Each entry: (script, label, expected_functions, expected_checks)
#
# expected_functions: number of test_* functions/methods pytest discovers
# expected_checks:    number of individual pass/fail assertions the
#                     native runner reports (equals expected_functions
#                     except where a single function contains multiple
#                     check() calls, as in verify.py)
#
# To add a new suite, append one tuple.
# ---------------------------------------------------------------------------

SUITES = [
    ('verify.py',             'verify.py (Phase A)',   13, 79),
    ('verify_phase_b.py',     'verify_phase_b.py',     25, 25),
    ('verify_phase_c.py',     'verify_phase_c.py',     28, 28),
    ('verify_integration.py', 'verify_integration.py',  7,  7),
    ('verify_phase_d.py',     'verify_phase_d.py',     23, 23),
    ('verify_d72b.py',        'verify_d72b.py',        10, 10),
    ('verify_phase_e.py',     'verify_phase_e.py',     29, 29),
    ('verify_r41.py',          'verify_r41.py (R4.1)',  30, 30),
    ('verify_spec.py',          'verify_spec.py (Spec)',   2, 51),
    ('verify_conformance.py',   'verify_conformance.py',  27, 69),
]


def _parse_check_count(output):
    """Extract passed and failed counts from suite output.

    Handles two output formats:
      Custom runners:  "N passed, M failed"
      unittest/pytest: "Ran N tests" + "OK" or "FAILED"

    Returns (passed, failed) or (None, None) if unparseable.
    """
    # Custom runner format: '76 passed, 0 failed'
    m = re.search(r'(\d+)\s+passed,\s+(\d+)\s+failed', output)
    if m:
        return int(m.group(1)), int(m.group(2))

    # unittest format: 'Ran 29 tests in 0.08s' + 'OK' or 'FAILED (...)'
    m = re.search(r'Ran\s+(\d+)\s+test', output)
    if m:
        total = int(m.group(1))
        fm = re.search(
            r'FAILED\s*\('
            r'(?:failures=(\d+))?'
            r'(?:,\s*)?'
            r'(?:errors=(\d+))?'
            r'\)',
            output,
        )
        if fm:
            failures = int(fm.group(1) or 0) + int(fm.group(2) or 0)
            return total - failures, failures
        if re.search(r'\bOK\b', output):
            return total, 0

    return None, None


def main():
    base = Path(__file__).parent
    python = sys.executable

    print()
    print('AP-1 runner -- full test suite')
    print()

    # Column widths
    w_label = 30
    w_func = 9
    w_check = 7
    w_result = 6

    header = (f'  {"suite":<{w_label}s}  '
              f'{"functions":>{w_func}s}  '
              f'{"checks":>{w_check}s}  '
              f'{"result":<{w_result}s}')
    sep = '  ' + '-' * (w_label + w_func + w_check + w_result + 8)

    print(header)
    print(sep)

    total_functions = 0
    total_checks = 0
    any_failed = False
    failed_output = []

    for script, label, exp_functions, exp_checks in SUITES:
        script_path = base / script

        # Run the suite in its native form
        proc = subprocess.run(
            [python, str(script_path)],
            capture_output=True, text=True, timeout=120,
            cwd=str(base),
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
        )

        combined = proc.stdout + '\n' + proc.stderr
        passed, failed = _parse_check_count(combined)

        suite_ok = proc.returncode == 0

        if passed is not None:
            observed_checks = passed + (failed or 0)
        else:
            observed_checks = None
            suite_ok = False  # unparseable output is a failure

        # Assert expected check count
        count_note = ''
        if observed_checks is not None:
            if observed_checks < exp_checks:
                suite_ok = False
                count_note = (f'    *** FEWER CHECKS THAN EXPECTED: '
                              f'{observed_checks} < {exp_checks}')
            elif observed_checks > exp_checks:
                count_note = (f'    (new: {observed_checks} checks, '
                              f'expected {exp_checks} -- update SUITES)')

        if failed and failed > 0:
            suite_ok = False

        result_str = 'PASS' if suite_ok else 'FAIL'
        if not suite_ok:
            any_failed = True
            failed_output.append((label, combined))

        checks_str = (str(observed_checks)
                      if observed_checks is not None else '?')

        print(f'  {label:<{w_label}s}  '
              f'{exp_functions:>{w_func}d}  '
              f'{checks_str:>{w_check}s}  '
              f'{result_str:<{w_result}s}')
        if count_note:
            print(count_note)

        total_functions += exp_functions
        total_checks += observed_checks if observed_checks is not None else 0

    print(sep)
    final_str = 'PASS' if not any_failed else 'FAIL'
    print(f'  {"TOTAL":<{w_label}s}  '
          f'{total_functions:>{w_func}d}  '
          f'{total_checks:>{w_check}d}  '
          f'{final_str:<{w_result}s}')
    print()

    # Explanatory note
    print('  The "checks" column counts what each suite reports. verify.py')
    print('  uses a check() counter and reports individual assertions; the')
    print('  other suites report test-function outcomes. verify.py is the')
    print('  only suite where checks and functions differ. Both columns are')
    print('  shown so neither number is mistaken for the other.')
    print()

    # Detail for any failed suites
    if any_failed:
        print('=' * 60)
        print('FAILED SUITE OUTPUT:')
        for label, output in failed_output:
            print(f'\n--- {label} ---')
            lines = output.strip().split('\n')
            for line in lines[-30:]:
                print(f'  {line}')
        print()

    print('=' * 60)
    print(f'RESULT: {final_str}')
    print('=' * 60)

    return 0 if not any_failed else 1


if __name__ == '__main__':
    sys.exit(main())
