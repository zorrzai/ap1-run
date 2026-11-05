"""SPEC R4.1 planted behaviour for scoring/reproducibility.py (legacy
verify_r41.py B22)."""

import pytest

from ap1_run.scoring.reproducibility import check_parameter_echo


@pytest.mark.req('R4.1', 'R2.2')
def test_r41_b22_ignored_temperature_is_a_mismatch_finding():
    assert check_parameter_echo(
        requested_params={'temperature': 0},
        echoed_params={'temperature': 1},
    ) == {'verified': False, 'status': 'MISMATCH', 'findings': [
        "parameter 'temperature': requested=0, applied=1 — "
        'silently ignored']}
