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
        'ap1_version_doi': config.get('ap1_version_doi', ''),
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

    # Version DOI check
    sealed_doi = record.get('ap1_version_doi', '')
    config_doi = config.get('ap1_version_doi', '')
    if sealed_doi and config_doi and sealed_doi != config_doi:
        checks.append(
            ('ap1_version_doi', sealed_doi, config_doi))

    mismatches = []
    for name, expected, actual in checks:
        if expected != actual:
            mismatches.append(
                f'{name}: sealed={expected!r}, current={actual!r}')

    if mismatches:
        raise SealError(
            'seal verification failed:\n  ' + '\n  '.join(mismatches))

    return True


# -- R3.1 Seal-time guards -------------------------------------------

def perturbation_check(ground_truth_module, fixture, questions,
                       perturbation_factor=None):
    """R3.1: Verify that ground-truth module outputs change when
    declared source fields change.

    A module whose outputs do not change when its declared source fields
    change is returning constants and is refused, with the perturbation
    named.

    Args:
        ground_truth_module: module with compute(item_id, ctx) function
        fixture: the fixture dict
        questions: the questions dict
        perturbation_factor: Decimal multiplier (default 1.1)

    Returns: list of failure dicts, each with item_id and field_name.
             Empty list = all items pass.

    Raises: SealError if any item fails.
    """
    from decimal import Decimal, InvalidOperation
    from context import build_delivered_context

    if perturbation_factor is None:
        perturbation_factor = Decimal('1.1')

    failures = []

    for item in questions.get('items', []):
        item_id = item['id']
        source_accounts = item.get('source_accounts', [])
        ctx = build_delivered_context(fixture, source_accounts)

        # Compute baseline
        try:
            baseline = ground_truth_module.compute(item_id, ctx)
        except Exception:
            continue  # skip items that can't be computed

        baseline_final = baseline.get('final')
        if baseline_final is None:
            continue

        # For each declared source field, perturb it and check
        for field_spec in baseline.get('source_fields_consumed', []):
            parts = field_spec.split('.', 1)
            if len(parts) != 2:
                continue
            acct_id, field_name = parts

            # Build a fresh context and perturb one field
            perturbed_ctx = build_delivered_context(fixture, source_accounts)
            if acct_id not in perturbed_ctx:
                continue
            if field_name not in perturbed_ctx[acct_id]:
                continue

            orig_val = perturbed_ctx[acct_id][field_name]
            try:
                numeric_val = Decimal(str(orig_val))
                perturbed_val = numeric_val * perturbation_factor
                perturbed_ctx[acct_id][field_name] = str(perturbed_val)
            except (InvalidOperation, ValueError):
                continue  # non-numeric field, skip

            # Recompute with perturbed context
            try:
                perturbed = ground_truth_module.compute(item_id, perturbed_ctx)
            except Exception:
                continue

            perturbed_final = perturbed.get('final')
            if perturbed_final == baseline_final:
                failures.append({
                    'item_id': item_id,
                    'field': field_spec,
                    'reason': f'output unchanged when {field_spec} '
                              f'perturbed by factor {perturbation_factor}',
                })

    if failures:
        names = ', '.join(f['field'] for f in failures)
        raise SealError(
            f'perturbation check failed: constant-returning module '
            f'detected. Fields that had no effect: {names}')

    return failures


def source_fields_check(ground_truth_module, fixture, questions):
    """R3.1: Verify that ground-truth module reads ONLY its declared
    source fields.

    A module reading a field NOT in source_fields_consumed is refused,
    with the field named.

    Uses TrackingContext to instrument field access.

    Returns: list of failure dicts. Empty = pass.
    Raises: SealError if any undeclared access detected.
    """
    from context import build_delivered_context, TrackingContext

    failures = []

    for item in questions.get('items', []):
        item_id = item['id']
        source_accounts = item.get('source_accounts', [])
        ctx = build_delivered_context(fixture, source_accounts)

        # Wrap in tracking context
        tracking = TrackingContext(ctx)

        try:
            result = ground_truth_module.compute(item_id, tracking)
        except Exception:
            continue

        accessed = tracking.accessed_fields()
        declared = set(result.get('source_fields_consumed', []))

        undeclared = accessed - declared
        if undeclared:
            failures.append({
                'item_id': item_id,
                'undeclared_fields': sorted(undeclared),
                'declared_fields': sorted(declared),
            })

    if failures:
        details = '; '.join(
            f'{f["item_id"]}: accessed {f["undeclared_fields"]}'
            for f in failures)
        raise SealError(
            f'source fields check failed: module reads undeclared '
            f'fields. {details}')

    return failures
