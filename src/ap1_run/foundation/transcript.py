"""R0.3 -- Transcript Store.

Spec: AP-1 Runner Build Spec v0.3, section 3 R0.3.

Owns run.jsonl: append-only, one line per interaction, never rewritten.
"""

import json
import warnings
from datetime import datetime, timezone
from pathlib import Path


class TranscriptError(Exception):
    """Transcript operation failure."""


def append(path, *, item_id, arm_id, condition, request_sent,
           response_received, tool_calls, evidence_class,
           error_state, seal_hash, **extra):
    """Append one record to the transcript.

    The file is opened in append mode. No update, no delete.
    Each record carries all fields required by R0.3.

    If the transcript cannot be written, raises TranscriptError
    and the run must halt. The store stamps the record: a 'timestamp'
    extra is refused (S3-G1-16).
    """
    if 'timestamp' in extra:
        raise TranscriptError(
            'timestamp is set by the transcript store, not by the caller')
    record = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'item_id': item_id,
        'arm_id': arm_id,
        'condition': condition,
        'request_sent': request_sent,
        'response_received': response_received,
        'tool_calls': tool_calls or [],
        'evidence_class': evidence_class,
        'error_state': error_state,
        'seal_hash': seal_hash,
    }
    record.update(extra)

    path = Path(path)
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(record, default=str, sort_keys=True,
                               ensure_ascii=False) + '\n')
    except OSError as e:
        raise TranscriptError(f'cannot write transcript: {e}') from e


def read_all(path):
    """Read all records from a transcript. Read-only.

    Returns list of dicts. The scorer opens this read-only.
    An interrupted run leaves a valid partial transcript;
    unreached items are not-run, never failures. A run killed during a
    write can leave a last line without its newline that is not valid
    JSON: that torn line is left out with a warning, and the complete
    records before it are returned (S3-G1-17). Invalid JSON anywhere
    else raises TranscriptError.
    """
    path = Path(path)
    if not path.exists():
        return []

    records = []
    with open(path, 'r', encoding='utf-8') as f:
        for line_num, raw_line in enumerate(f, 1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                if not raw_line.endswith('\n'):
                    warnings.warn(
                        f'transcript {path}: line {line_num} is incomplete '
                        f'(interrupted write) and was left out: {e}')
                    break
                raise TranscriptError(
                    f'invalid JSON at line {line_num}: {e}') from e

    return records
