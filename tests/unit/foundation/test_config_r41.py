"""SPEC R4.1 planted behaviour for foundation/config.py (legacy
verify_r41.py B24)."""

import pytest

from ap1_run.foundation.config import ConfigError, validate_minimum_n


@pytest.mark.finding('T3-12')
@pytest.mark.req('R4.1', 'R0.1')
def test_r41_b24_d6_claimed_with_nine_items_is_refused():
    # The runner calls the validator before any request (T3-12); the
    # end-to-end row is test_step4_g9_spec_claims.py::
    # test_r41_d6_claimed_with_nine_items_refused_at_load.
    with pytest.raises(ConfigError) as exc:
        validate_minimum_n({'dimensions_claimed': ['D6'],
                            'ap1_version': 'v1.3'},
                           [{'id': str(i), 'conflict_class': 'x'}
                            for i in range(9)])
    assert str(exc.value) == ('D6: 9 eligible items (conflict_class set), '
                              'minimum 10 required')
