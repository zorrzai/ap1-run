"""AP-1 runner -- run the test suite.

    python run_all_tests.py [pytest options]

Runs pytest over tests/unit, tests/conformance, tests/functional and
tests/inspect (as configured in pyproject.toml); extra arguments go to pytest.
Needs the development extras: pip install -e .[dev].

The original verify_*.py suites that this script used to run were retired in
October 2026; tests/RETIREMENT.md maps each of their 410 checks to the tests
that replace it. The regression baseline runs separately:
python tests/regression/run_regression.py.

Exit code: pytest's (0 when every test passes).
"""

import os
import subprocess
import sys


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    args = sys.argv[1:] if argv is None else argv
    return subprocess.call([sys.executable, '-m', 'pytest', *args], cwd=here)


if __name__ == '__main__':
    sys.exit(main())
