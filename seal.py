"""R1.1 -- Pre-Registration and Sealing.

Spec: AP-1 Runner Build Spec v0.3, section 4 R1.1.

Before any request is sent, hash and timestamp the fixture, question set,
expected values, ground-truth module, resolved configuration, the AP-1
text version, and any public keys required to verify attestations.

A run that starts without a valid record is refused.
"""

from datetime import datetime, timezone
from pathlib import Path

from numeric import canonical_hash, file_hash


class SealError(Exception):
    """Seal validation failure."""


def seal(*, config, fixture_path, questions_path, ground_truth_path,
         ap1_text_path=None, verification_keys=None):
    """Create a pre-registration record. R1.1.

    Hashes all inputs and timestamps the record. The seal_hash
    appears on every transcript line.

    If ap1_text_path is provided and its hash does not match
    config['ap1_text_hash'], raises SealError.

    Returns: dict with component hashes and seal_hash.
    """
    now = datetime.now(timezone.utc).isoformat()

    record = {
        'timestamp': now,
        'fixture_hash': file_hash(str(fixture_path)),
        'questions_hash': file_hash(str(questions_path)),
        'ground_truth_hash': file_hash(str(ground_truth_path)),
        'config_hash': canonical_hash(config),
        'ap1_version': config.get('ap1_version', ''),
    }

    # AP-1 text hash -- R1.1 normative
    declared_hash = config.get('ap1_text_hash', '')
    if ap1_text_path:
        ap1_path = Path(ap1_text_path)
        if not ap1_path.exists():
            raise SealError(f'AP-1 text file not found: {ap1_path}')
        computed = file_hash(str(ap1_path))
        if declared_hash and declared_hash != 'placeholder' and \
                declared_hash != computed:
            raise SealError(
                f'AP-1 text hash mismatch: config declares '
                f'{declared_hash!r}, file hashes to {computed!r}')
        record['ap1_text_hash'] = computed
    else:
        record['ap1_text_hash'] = declared_hash

    # Verification keys for EV-3 (not implemented in v1.0)
    record['verification_keys'] = verification_keys or []
    record['ev3_implemented'] = False

    # Seal: hash the entire record so far
    # (timestamp excluded from hash to allow re-sealing check
    #  on component hashes only)
    hashable = {k: v for k, v in record.items() if k != 'timestamp'}
    record['seal_hash'] = canonical_hash(hashable)

    return record


def verify_seal(record, *, config, fixture_path, questions_path,
                ground_truth_path, ap1_text_path=None):
    """Verify a pre-registration record against current files.

    The scorer calls this before processing. Raises SealError
    if any component hash does not match, naming the mismatch.
    """
    checks = [
        ('fixture', record.get('fixture_hash'),
         file_hash(str(fixture_path))),
        ('questions', record.get('questions_hash'),
         file_hash(str(questions_path))),
        ('ground_truth', record.get('ground_truth_hash'),
         file_hash(str(ground_truth_path))),
        ('config', record.get('config_hash'),
         canonical_hash(config)),
    ]

    if ap1_text_path:
        checks.append(
            ('ap1_text', record.get('ap1_text_hash'),
             file_hash(str(ap1_text_path))))

    mismatches = []
    for name, expected, actual in checks:
        if expected != actual:
            mismatches.append(
                f'{name}: sealed={expected!r}, current={actual!r}')

    if mismatches:
        raise SealError(
            'seal verification failed:\n  ' + '\n  '.join(mismatches))

    return True
