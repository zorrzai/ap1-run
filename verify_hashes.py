"""Cross-platform canonical hash verification.

Run by CI on ubuntu-latest, macos-latest, windows-latest.
Produces hash_digest.txt with a deterministic digest from known inputs.
CI compares the three digests -- they must be identical.
"""

import sys
import os

# Ensure UTF-8 output on Windows (cp1252 cannot encode all Unicode)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from decimal import Decimal
from numeric import canonical_hash, canonical_json


def main():
    # Known input -- the same on every platform
    test_obj = {
        'z_last': 'should sort last',
        'a_first': 'should sort first',
        'decimal_value': Decimal('274.1375'),
        'nested': {
            'inner_b': Decimal('777.4125'),
            'inner_a': [Decimal('15.20'), Decimal('3109.65')],
        },
        'empty_list': [],
        'unicode': '\u2212',  # minus sign
    }

    # Canonical JSON must be deterministic
    json_text = canonical_json(test_obj)
    digest = canonical_hash(test_obj)

    print(f'Canonical JSON: {json_text}')
    print(f'SHA-256 digest: {digest}')

    # Write digest to file for CI comparison
    digest_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'hash_digest.txt')
    with open(digest_path, 'w', encoding='utf-8') as f:
        f.write(digest)

    # Self-check: same input produces same hash
    digest2 = canonical_hash(test_obj)
    assert digest == digest2, f'Non-deterministic: {digest} != {digest2}'

    # Self-check: key order does not matter
    reordered = {
        'unicode': '\u2212',
        'nested': {
            'inner_a': [Decimal('15.20'), Decimal('3109.65')],
            'inner_b': Decimal('777.4125'),
        },
        'z_last': 'should sort last',
        'empty_list': [],
        'decimal_value': Decimal('274.1375'),
        'a_first': 'should sort first',
    }
    digest3 = canonical_hash(reordered)
    assert digest == digest3, f'Key-order sensitive: {digest} != {digest3}'

    print('PASS: all hash checks passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
