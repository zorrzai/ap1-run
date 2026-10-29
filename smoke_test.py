"""Compatibility shim: the live runner is now ap1_run.run (src/ap1_run/run.py).

`python smoke_test.py` keeps working, as documented in older material and
in the published runs. The installed command is `ap1-run`.

If the package is not installed (`pip install -e .`), src/ is put on the
path so that a fresh clone still runs.
"""

import os
import sys

try:
    import ap1_run  # noqa: F401
except ImportError:
    sys.path.insert(0, os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'src'))

from ap1_run.run import main  # noqa: E402

if __name__ == '__main__':
    raise SystemExit(main())
