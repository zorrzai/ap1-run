"""Unit tests for the R0.3 transcript store (foundation/transcript.py)."""

import json
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from ap1_run.foundation import transcript
from ap1_run.foundation.transcript import TranscriptError, append, read_all

FIELDS = dict(item_id='Q01', arm_id='arm-a', condition='base',
              request_sent={'messages': []},
              response_received={'choices': []},
              tool_calls=[{'id': 'c1'}], evidence_class='EV-2',
              error_state=None, seal_hash='abc')


class FixedDatetime:
    """Stands in for datetime: now(tz) returns a fixed time in tz."""
    calls = []

    @classmethod
    def now(cls, tz=None):
        cls.calls.append(tz)
        return datetime(2026, 10, 15, 12, 0, 0, tzinfo=tz)


@pytest.fixture
def fixed_time(monkeypatch):
    FixedDatetime.calls = []
    monkeypatch.setattr(transcript, 'datetime', FixedDatetime)
    return FixedDatetime


def lines(path):
    return path.read_text(encoding='utf-8').split('\n')


# -- append ---------------------------------------------------------------

@pytest.mark.req('R0.3')
def test_append_writes_one_sorted_json_line(tmp_path, fixed_time):
    p = tmp_path / 'run.jsonl'
    append(p, **FIELDS)
    assert lines(p) == [
        '{"arm_id": "arm-a", "condition": "base", "error_state": null, '
        '"evidence_class": "EV-2", "item_id": "Q01", '
        '"request_sent": {"messages": []}, '
        '"response_received": {"choices": []}, "seal_hash": "abc", '
        '"timestamp": "2026-10-15T12:00:00+00:00", '
        '"tool_calls": [{"id": "c1"}]}',
        '']


def test_append_timestamp_is_utc(tmp_path, fixed_time):
    append(tmp_path / 'run.jsonl', **FIELDS)
    assert fixed_time.calls == [timezone.utc]


def test_append_real_timestamp_is_iso_utc(tmp_path):
    p = tmp_path / 'run.jsonl'
    append(p, **FIELDS)
    ts = json.loads(lines(p)[0])['timestamp']
    assert datetime.fromisoformat(ts).utcoffset().total_seconds() == 0


@pytest.mark.req('R0.3')
def test_append_appends_never_rewrites(tmp_path, fixed_time):
    p = tmp_path / 'run.jsonl'
    p.write_text('{"earlier": 1}\n', encoding='utf-8')
    append(p, **FIELDS)
    append(p, **dict(FIELDS, item_id='Q02'))
    out = lines(p)
    assert out[0] == '{"earlier": 1}'
    assert [json.loads(x)['item_id'] for x in out[1:3]] == ['Q01', 'Q02']
    assert out[3] == ''


def test_append_creates_missing_file(tmp_path, fixed_time):
    p = tmp_path / 'new.jsonl'
    append(str(p), **FIELDS)
    assert p.exists()


@pytest.mark.parametrize('empty', [None, [], ''])
def test_append_missing_tool_calls_written_as_empty_list(tmp_path, empty):
    p = tmp_path / 'run.jsonl'
    append(p, **dict(FIELDS, tool_calls=empty))
    assert json.loads(lines(p)[0])['tool_calls'] == []


def test_append_extra_fields_added(tmp_path):
    p = tmp_path / 'run.jsonl'
    append(p, **FIELDS, figure_outcome='AUTO-MATCH', repeat=2)
    rec = json.loads(lines(p)[0])
    assert rec['figure_outcome'] == 'AUTO-MATCH'
    assert rec['repeat'] == 2


@pytest.mark.finding('S3-G1-16')
def test_append_extra_timestamp_overrides_the_clock(tmp_path, fixed_time):
    # Current behaviour: extras are merged last, so a caller's
    # 'timestamp' replaces the store's own. Correct: the store owns the
    # timestamp; refuse or rename a colliding extra.
    p = tmp_path / 'run.jsonl'
    append(p, **FIELDS, timestamp='1999-01-01')
    assert json.loads(lines(p)[0])['timestamp'] == '1999-01-01'


def test_append_non_json_values_written_with_str(tmp_path):
    p = tmp_path / 'run.jsonl'
    append(p, **dict(FIELDS, response_received={'v': Decimal('1.50')}))
    assert json.loads(lines(p)[0])['response_received'] == {'v': '1.50'}


def test_append_non_ascii_written_as_utf8(tmp_path):
    p = tmp_path / 'run.jsonl'
    append(p, **dict(FIELDS, item_id='−é'))
    assert '"item_id": "−é"' in p.read_bytes().decode('utf-8')


def test_append_unwritable_path_raises_transcript_error(tmp_path):
    with pytest.raises(TranscriptError) as e:
        append(tmp_path / 'no-such-dir' / 'run.jsonl', **FIELDS)
    assert str(e.value).startswith('cannot write transcript: [Errno 2] ')
    assert isinstance(e.value.__cause__, OSError)


def test_append_directory_path_raises_transcript_error(tmp_path):
    with pytest.raises(TranscriptError, match='^cannot write transcript: '):
        append(tmp_path, **FIELDS)


def test_append_unserialisable_record_raises_value_error(tmp_path):
    # Only OSError is translated; a circular structure escapes as is, and
    # nothing is written.
    loop = []
    loop.append(loop)
    p = tmp_path / 'run.jsonl'
    with pytest.raises(ValueError, match='Circular reference'):
        append(p, **dict(FIELDS, tool_calls=loop))
    assert p.read_text(encoding='utf-8') == ''


def test_append_fields_are_keyword_only(tmp_path):
    with pytest.raises(TypeError):
        append(tmp_path / 'run.jsonl', 'Q01')


# -- read_all -------------------------------------------------------------

def test_read_all_missing_file_is_empty(tmp_path):
    assert read_all(tmp_path / 'absent.jsonl') == []


def test_read_all_returns_records_in_order(tmp_path):
    p = tmp_path / 'run.jsonl'
    p.write_text('{"a": 1}\n{"a": 2}\n', encoding='utf-8')
    assert read_all(str(p)) == [{'a': 1}, {'a': 2}]


def test_read_all_round_trips_append(tmp_path, fixed_time):
    p = tmp_path / 'run.jsonl'
    append(p, **FIELDS)
    [rec] = read_all(p)
    assert rec == dict(FIELDS, timestamp='2026-10-15T12:00:00+00:00')


def test_read_all_skips_blank_and_whitespace_lines(tmp_path):
    p = tmp_path / 'run.jsonl'
    p.write_text('\n  {"a": 1}  \n\n \t\n{"a": 2}', encoding='utf-8')
    assert read_all(p) == [{'a': 1}, {'a': 2}]


def test_read_all_reads_utf8(tmp_path):
    p = tmp_path / 'run.jsonl'
    p.write_bytes('{"s": "−é"}\n'.encode('utf-8'))
    assert read_all(p) == [{'s': '−é'}]


def test_read_all_invalid_line_raises_with_line_number(tmp_path):
    p = tmp_path / 'run.jsonl'
    p.write_text('{"a": 1}\n\n{"a": \n', encoding='utf-8')
    with pytest.raises(TranscriptError) as e:
        read_all(p)
    assert str(e.value).startswith('invalid JSON at line 3: Expecting value')
    assert isinstance(e.value.__cause__, json.JSONDecodeError)


@pytest.mark.finding('S3-G1-17')
def test_read_all_interrupted_last_line_raises(tmp_path):
    # Current behaviour: a run killed mid-write leaves a truncated last
    # line, and read_all refuses the whole transcript. Correct (per its
    # docstring, "an interrupted run leaves a valid partial transcript"):
    # report the torn final line and return the complete records.
    p = tmp_path / 'run.jsonl'
    p.write_text('{"a": 1}\n{"a": 2', encoding='utf-8')
    with pytest.raises(TranscriptError, match='^invalid JSON at line 2'):
        read_all(p)


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('S3-G1-16')
@pytest.mark.req('R0.3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-16: an extra timestamp= replaces the '
                          "store's own clock")
def test_append_store_owns_the_timestamp(tmp_path, fixed_time):
    # The transcript store stamps each record (R0.3); a caller cannot
    # backdate it. A colliding extra is refused, or the store's time wins.
    p = tmp_path / 'run.jsonl'
    try:
        append(p, **FIELDS, timestamp='1999-01-01')
        written = json.loads(lines(p)[0])['timestamp']
    except (TranscriptError, TypeError, ValueError):
        written = 'refused'
    assert written in ('refused', '2026-10-15T12:00:00+00:00')


@pytest.mark.finding('S3-G1-17')
@pytest.mark.req('R0.3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-17: a torn last line makes read_all refuse '
                          'the whole transcript')
def test_read_all_interrupted_last_line_keeps_complete_records(tmp_path):
    # read_all's docstring: "An interrupted run leaves a valid partial
    # transcript; unreached items are not-run, never failures." A run
    # killed mid-write leaves a torn final line; the complete records
    # before it are returned (the torn line reported, not parsed).
    p = tmp_path / 'run.jsonl'
    p.write_text('{"a": 1}\n{"a": 2', encoding='utf-8')
    try:
        records = read_all(p)
    except TranscriptError as e:
        records = f'raised TranscriptError: {e}'
    assert records[:1] == [{'a': 1}], records
