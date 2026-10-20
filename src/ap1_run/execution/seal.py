"""R1.1 -- Pre-Registration and Sealing.

Spec: AP-1 Runner Build Spec v0.3, section 4 R1.1.

Before any request is sent, hash and timestamp the fixture, question set,
expected values, ground-truth module, resolved configuration, the AP-1
text version, and any public keys required to verify attestations.

A run that starts without a valid record is refused.
"""

import hashlib
from datetime import datetime, timezone
from pathlib import Path

from ap1_run.execution.version import runner_environment
from ap1_run.foundation.numeric import canonical_hash, file_hash

# The record format. A record without this field was made by an earlier
# runner, under the rules of tools/verify_run_seal.py's legacy mode: raw
# file bytes, a seal_hash that leaves out the timestamp, no expected
# values or environment.
SEAL_FORMAT = '2'

# The fields every record of this format carries. seal_hash covers all
# of them (T3-15, T3-47: the timestamp too).
SEALED_FIELDS = (
    'seal_format', 'timestamp',
    'fixture_hash', 'questions_hash', 'ground_truth_hash',
    'expected_values_hash', 'config_hash',
    'ap1_version', 'ap1_version_doi', 'ap1_text_hash',
    'runner_version_tag', 'runner_version_commit', 'runner_source_hash',
    'python_version', 'platform', 'package_versions',
    'verification_keys', 'ev3_implemented',
)

# The sealed text inputs, by name: the record field is '<name>_hash'.
TEXT_INPUTS = ('fixture', 'questions', 'ground_truth')

_BOM = b'\xef\xbb\xbf'


class SealError(Exception):
    """Seal validation failure."""


def text_hash(data):
    """SHA-256 of a sealed text input, with its line endings made LF and a
    leading UTF-8 byte-order mark dropped (T3-50), so the same text gives
    the same digest on every platform and in every editor. An LF file
    without a BOM hashes exactly as its raw bytes. The AP-1 text is not
    hashed this way: it must equal the publisher's deposit byte for byte.
    """
    if data.startswith(_BOM):
        data = data[len(_BOM):]
    data = data.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
    return hashlib.sha256(data).hexdigest()


def text_file_hash(path):
    """text_hash of a file's contents."""
    with open(path, 'rb') as f:
        return text_hash(f.read())


def expected_values_hash(expected_values):
    """The canonical hash of the expected values: what the ground-truth
    module returned for each item, {item_id: result} (R1.1, T3-48).
    Raises SealError if a result cannot be hashed (a float, or a value
    JSON cannot hold)."""
    try:
        return canonical_hash(expected_values)
    except (TypeError, ValueError) as e:
        raise SealError(f'expected values cannot be sealed: {e}') from e


def record_hash(record):
    """seal_hash: the canonical hash of every field but seal_hash itself,
    the timestamp included (T3-47)."""
    return canonical_hash({k: v for k, v in record.items()
                           if k != 'seal_hash'})


def _declared_ap1_hash(config):
    """The AP-1 text hash the config declares, or SealError if it declares
    none (T3-68: a blank or 'placeholder' hash checks nothing)."""
    declared = config.get('ap1_text_hash')
    if not declared or declared == 'placeholder':
        raise SealError(
            f'AP-1 text hash: the config declares {declared!r}; a sealed '
            f'run needs the SHA-256 of the AP-1 text it claims (R1.1)')
    return declared


def seal(*, config, fixture_path, questions_path, ground_truth_path,
         ap1_text_path=None, verification_keys=None,
         runner_source_hash=None, expected_values=None, loaded=None):
    """Create a pre-registration record. R1.1.

    Hashes all inputs and timestamps the record. The seal_hash covers
    every field, the timestamp included, and appears on every transcript
    line.

    The AP-1 text is required: SealError if ap1_text_path is not given or
    not found, if the config declares no hash for it (blank, missing or
    'placeholder'), or if the file's hash differs from the declared one
    (T3-68).

    expected_values: {item_id: ground-truth result}, computed before the
    seal (T3-48); its hash is sealed ('' if not given).
    loaded: {name: bytes} for 'fixture', 'questions' and 'ground_truth',
    the bytes the run read and executes. When given, these are hashed
    instead of the files being read again (T3-72: seal what is executed).

    Returns: dict with component hashes and seal_hash.
    """
    now = datetime.now(timezone.utc).isoformat()

    # AP-1 text hash -- R1.1 normative
    declared_hash = _declared_ap1_hash(config)
    if not ap1_text_path:
        raise SealError('AP-1 text: no file given; a sealed run hashes the '
                        'AP-1 text it claims (R1.1)')
    ap1_path = Path(ap1_text_path)
    if not ap1_path.exists():
        raise SealError(f'AP-1 text file not found: {ap1_path}')
    computed = file_hash(str(ap1_path))
    if declared_hash != computed:
        raise SealError(
            f'AP-1 text hash mismatch: config declares '
            f'{declared_hash!r}, file hashes to {computed!r}')

    loaded = loaded or {}
    paths = {'fixture': fixture_path, 'questions': questions_path,
             'ground_truth': ground_truth_path}
    hashes = {name: (text_hash(loaded[name]) if name in loaded
                     else text_file_hash(str(paths[name])))
              for name in TEXT_INPUTS}

    record = {
        'seal_format': SEAL_FORMAT,
        'timestamp': now,
        'fixture_hash': hashes['fixture'],
        'questions_hash': hashes['questions'],
        'ground_truth_hash': hashes['ground_truth'],
        'expected_values_hash': (
            '' if expected_values is None
            else expected_values_hash(expected_values)),
        'config_hash': canonical_hash(config),
        'ap1_version': config.get('ap1_version', ''),
        'ap1_version_doi': config.get('ap1_version_doi', ''),
        'ap1_text_hash': computed,
        'runner_version_tag': config.get('runner_version_tag', ''),
        'runner_version_commit': config.get('runner_version_commit', ''),
        'runner_source_hash': runner_source_hash or '',
        # The environment, outside runner_source_hash (F2)
        **runner_environment(),
        # Verification keys for EV-3 (not implemented in v1.0)
        'verification_keys': verification_keys or [],
        'ev3_implemented': False,
    }

    # Seal: hash the entire record, the timestamp included
    record['seal_hash'] = record_hash(record)

    return record


def verify_seal(record, *, config, fixture_path, questions_path,
                ground_truth_path, ap1_text_path=None,
                runner_source_hash=None, expected_values=None):
    """Verify a pre-registration record against current files.

    The scorer calls this before processing. Raises SealError naming
    every mismatch: a field missing from the record, a seal_hash that
    does not match the record (so a rewritten field of any kind is
    refused), and each component that differs from the current inputs:
    the three text inputs, the config, the AP-1 text (always compared
    with the config's declared hash, and with the file if its path is
    given), the DOI, and the runner source hash and expected values when
    given.
    """
    mismatches = []
    missing = [f for f in SEALED_FIELDS if f not in record]
    if missing:
        mismatches.append(f'record: missing {", ".join(missing)}')
    recomputed = record_hash(record)
    if record.get('seal_hash') != recomputed:
        mismatches.append(f'seal_hash: sealed={record.get("seal_hash")!r}, '
                          f'recomputed={recomputed!r}')

    checks = [
        ('fixture', record.get('fixture_hash'),
         text_file_hash(str(fixture_path))),
        ('questions', record.get('questions_hash'),
         text_file_hash(str(questions_path))),
        ('ground_truth', record.get('ground_truth_hash'),
         text_file_hash(str(ground_truth_path))),
        ('config', record.get('config_hash'),
         canonical_hash(config)),
        ('ap1_text', record.get('ap1_text_hash'),
         config.get('ap1_text_hash')),
    ]

    if ap1_text_path:
        checks.append(
            ('ap1_text', record.get('ap1_text_hash'),
             file_hash(str(ap1_text_path))))

    # Version DOI check: a DOI on one side only is a mismatch too
    checks.append(('ap1_version_doi', record.get('ap1_version_doi', ''),
                   config.get('ap1_version_doi', '')))

    if runner_source_hash is not None:
        checks.append(('runner_source_hash',
                       record.get('runner_source_hash'), runner_source_hash))
    if expected_values is not None:
        checks.append(('expected_values', record.get('expected_values_hash'),
                       expected_values_hash(expected_values)))

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

    Each declared numeric field of each derivable item is perturbed in
    turn (multiplied by the factor; a zero set to 1). Fails closed (T3-7):
    a derivable item is a failure if its final value is None, if compute
    raises, if it declares no source fields, if a declared field is not
    of the form account.field or is not in the delivered context, or if
    none of its declared fields is numeric (so nothing could be
    perturbed). Only an item that declares itself non-derivable is
    exempt.

    Args:
        ground_truth_module: module with compute(item_id, ctx) function
        fixture: the fixture dict
        questions: the questions dict
        perturbation_factor: Decimal multiplier (default 1.1)

    Returns: list of failure dicts, each with item_id and reason.
             Empty list = all items pass.

    Raises: SealError if any item fails, naming for each failure the
            item, the field and the perturbation or error (S3-G3-3).
    """
    from decimal import Decimal, InvalidOperation
    from ap1_run.execution.context import build_delivered_context

    if perturbation_factor is None:
        perturbation_factor = Decimal('1.1')

    failures = []

    def fail(item_id, reason):
        failures.append({'item_id': item_id, 'reason': reason})

    for item in questions.get('items', []):
        item_id = item['id']
        source_accounts = item.get('source_accounts', [])
        ctx = build_delivered_context(fixture, source_accounts)

        # Compute baseline
        try:
            baseline = ground_truth_module.compute(item_id, ctx)
        except Exception as exc:
            fail(item_id,
                 f'baseline computation raised {type(exc).__name__}: {exc}')
            continue

        if not baseline.get('derivable', True):
            continue

        baseline_final = baseline.get('final')
        if baseline_final is None:
            fail(item_id,
                 'final is None on an item declared derivable')
            continue

        declared = baseline.get('source_fields_consumed')
        if not declared:
            fail(item_id,
                 f'declares no source fields to perturb '
                 f'(source_fields_consumed is {declared!r})')
            continue

        # For each declared source field, perturb it and check
        perturbed_any = False
        non_numeric = []
        for field_spec in declared:
            parts = str(field_spec).split('.', 1)
            if len(parts) != 2:
                fail(item_id,
                     f'declared source field {field_spec!r} is not of '
                     f'the form account.field')
                continue
            acct_id, field_name = parts

            # Build a fresh context and perturb one field
            perturbed_ctx = build_delivered_context(fixture, source_accounts)
            if acct_id not in perturbed_ctx:
                fail(item_id,
                     f'declared source field {field_spec!r}: account '
                     f'{acct_id!r} is not in the delivered context')
                continue
            if field_name not in perturbed_ctx[acct_id]:
                fail(item_id,
                     f'declared source field {field_spec!r}: account '
                     f'{acct_id!r} has no field {field_name!r}')
                continue

            orig_val = perturbed_ctx[acct_id][field_name]
            try:
                numeric_val = Decimal(str(orig_val))
                if not numeric_val.is_finite():
                    raise InvalidOperation
                if numeric_val == 0:
                    perturbed_val = Decimal('1')  # additive for zero
                    perturbation = 'set from 0 to 1'
                else:
                    perturbed_val = numeric_val * perturbation_factor
                    perturbation = f'multiplied by {perturbation_factor}'
                perturbed_ctx[acct_id][field_name] = str(perturbed_val)
            except (InvalidOperation, ValueError):
                non_numeric.append(field_spec)
                continue  # non-numeric field: cannot be perturbed
            perturbed_any = True

            # Recompute with perturbed context
            try:
                perturbed = ground_truth_module.compute(item_id, perturbed_ctx)
            except Exception as exc:
                fail(item_id,
                     f'perturbed computation ({field_spec} {perturbation}) '
                     f'raised {type(exc).__name__}: {exc}')
                continue

            perturbed_final = perturbed.get('final')
            if perturbed_final == baseline_final:
                fail(item_id,
                     f'output unchanged when {field_spec} {perturbation}')

        if not perturbed_any and non_numeric:
            fail(item_id,
                 f'no declared source field could be perturbed: '
                 f'{", ".join(non_numeric)} not numeric')

    if failures:
        details = '; '.join(
            f'{f["item_id"]}: {f["reason"]}' for f in failures)
        raise SealError(
            f'perturbation check failed: the module\'s output does not '
            f'follow its declared source fields. {details}')

    return failures


def source_fields_check(ground_truth_module, fixture, questions):
    """R3.1: Verify that ground-truth module reads ONLY its declared
    source fields.

    A module reading a field NOT in source_fields_consumed is refused,
    with the field named. A module whose compute raises is refused, with
    the error named (S3-G3-3).

    Uses TrackingContext to instrument field access.

    Returns: list of failure dicts. Empty = pass.
    Raises: SealError if any undeclared access detected or compute
            raises.
    """
    from ap1_run.execution.context import build_delivered_context, TrackingContext

    failures = []

    for item in questions.get('items', []):
        item_id = item['id']
        source_accounts = item.get('source_accounts', [])
        ctx = build_delivered_context(fixture, source_accounts)

        # Wrap in tracking context
        tracking = TrackingContext(ctx)

        try:
            result = ground_truth_module.compute(item_id, tracking)
        except Exception as exc:
            failures.append({
                'item_id': item_id,
                'reason': f'compute raised {type(exc).__name__}: {exc}',
            })
            continue

        accessed = tracking.accessed_fields()
        declared = set(result.get('source_fields_consumed', []))

        undeclared = accessed - declared
        if undeclared:
            failures.append({
                'item_id': item_id,
                'reason': f'reads undeclared fields {sorted(undeclared)}',
            })

    if failures:
        details = '; '.join(
            f'{f["item_id"]}: {f["reason"]}' for f in failures)
        raise SealError(f'source fields check failed: {details}')

    return failures
