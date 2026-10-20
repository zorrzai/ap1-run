"""SPEC R4.1 planted behaviour for scoring/transcription.py (legacy
verify_r41.py B08)."""

from decimal import Decimal

import pytest

from ap1_run.scoring.figure_id import AUTO_MATCH
from ap1_run.scoring.transcription import TRANSCRIBED_ALTERED, check_transcription


@pytest.mark.req('R4.1', 'R2.5')
def test_r41_b08_tool_returns_14979_response_releases_14980_is_altered():
    assert check_transcription(
        tool_return_value=Decimal('149.79'),
        released_figure=Decimal('149.80'),
        figure_outcome=AUTO_MATCH,
    ) == {'outcome': TRANSCRIBED_ALTERED, 'tool_return': Decimal('149.79'),
          'released_figure': Decimal('149.80'),
          'difference': Decimal('0.01'), 'reason': 'altered by 0.01',
          'rounded_under_declared_policy': False}
