"""Compatibility shim: the live runner is now ap1_run.run (src/ap1_run/run.py).

`python smoke_test.py` keeps working, as documented in older material and
in the published runs. The installed command is `ap1-run`.

This clone's src/ always goes first on the path, so the shim runs this
clone's code even when another clone's ap1_run is installed in the same
environment or is on PYTHONPATH. A fresh clone runs without installing.
"""

import os
import sys

# This clone's src/ first, before any ap1_run import.
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'src'))

from ap1_run.run import main  # noqa: E402

if __name__ == '__main__':
    raise SystemExit(main())
