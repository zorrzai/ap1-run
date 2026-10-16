"""ap1_inspect/ is a top-level package beside src/, not installed: put the
repository root on sys.path so it imports. Tests that need inspect-ai
(scorer, solver, task, metrics) skip with pytest.importorskip; the shim and
the cross-condition comparison need only the standard library and run
everywhere. Run the full set in the ap1-run-inspect environment."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
