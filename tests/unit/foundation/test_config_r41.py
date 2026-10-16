"""SPEC R4.1 planted behaviour for foundation/config.py (legacy
verify_r41.py B24)."""

import pytest

from ap1_run.foundation.config import ConfigError, validate_minimum_n


@pytest.mark.finding('T3-12')
@pytest.mark.req('R4.1', 'R0.1')
def test_r41_b24_d6_claimed_with_nine_items_is_refused():
    # The validator refuses, but the runner never calls it (T3-12), so
    # R4.1's "refused at load" holds for the unit only.
    with pytest.raises(ConfigError) as exc:
        validate_minimum_n({'dimensions_claimed': ['D6']},
                           [{'id': str(i)} for i in range(9)])
    assert str(exc.value) == 'D6: 9 items, minimum 10 required'
