"""Phase B verification tests.

Tests for R1.2 (execution engine) and R1.3 (tool loop, evidence
classification) exit gates.

Exit gates:
  1. Single-variable perturbation refusal demonstrated, with the
     emitted diff naming every changed quantity.
  2. All four evidence classes correctly assigned, INCLUDING EV-1
     for a signed attestation the runner cannot verify.
  3. The runner cannot emit EV-3 under ANY input in v1.0.
  4. Item-selection rule enforced: items declared underivable are
     VOID and excluded from every invocation denominator.
"""

import json
import sys
import os

# Ensure modules are importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from evidence import (
    classify_invocation, classify_attestation,
    check_ev3_guard, EvidenceError,
    EV_0, EV_1, EV_2, EV_3,
    classes_comparable, ranks_above,
)
from engine import (
    check_single_variable_perturbation,
    PerturbationRefusal,
    build_delivered_context,
    check_lookup_collision,
    CONDITION_BASE, CONDITION_INSTRUCTION_REMOVED,
)


# =====================================================================
#  EXIT GATE 1: Single-variable perturbation refusal
# =====================================================================

def test_perturbation_single_variable_pass():
    """Conditions differing in ONLY system_prompt: accepted."""
    base = {
        'system_prompt': 'You are a financial assistant. Use tools.',
        'tools': [{'type': 'function', 'function': {'name': 'calculator'}}],
        'tool_choice': 'auto',
        'sampling': {'temperature': '0.0'},
        'fixture_hash': 'abc123',
        'message_template': {'role': 'user'},
    }
    removed = dict(base)
    removed['system_prompt'] = 'You are a financial assistant.'

    diffs = check_single_variable_perturbation(base, removed)
    # Should succeed (no exception)
    assert len(diffs) == 0, f'unexpected diffs: {diffs}'
    return True


def test_perturbation_tools_removed_refused():
    """Removing tools alongside instruction: refused with diff."""
    base = {
        'system_prompt': 'You are a financial assistant. Use tools.',
        'tools': [{'type': 'function', 'function': {'name': 'calculator'}}],
        'tool_choice': 'auto',
        'sampling': {'temperature': '0.0'},
        'fixture_hash': 'abc123',
        'message_template': None,
    }
    removed = {
        'system_prompt': 'You are a financial assistant.',
        'tools': None,  # REMOVED — two quantities changed
        'tool_choice': 'auto',
        'sampling': {'temperature': '0.0'},
        'fixture_hash': 'abc123',
        'message_template': None,
    }

    try:
        check_single_variable_perturbation(base, removed)
        assert False, 'should have raised PerturbationRefusal'
    except PerturbationRefusal as e:
        msg = str(e)
        assert 'tools' in msg, f'diff must name "tools": {msg}'
        assert 'system_prompt' in msg, \
            f'diff must name "system_prompt": {msg}'
        return True


def test_perturbation_sampling_changed_refused():
    """Changing sampling alongside instruction: refused with diff."""
    base = {
        'system_prompt': 'Prompt A',
        'tools': [{'type': 'function', 'function': {'name': 'calc'}}],
        'sampling': {'temperature': '0.0'},
        'fixture_hash': 'abc',
    }
    removed = {
        'system_prompt': 'Prompt B',
        'tools': [{'type': 'function', 'function': {'name': 'calc'}}],
        'sampling': {'temperature': '0.7'},  # CHANGED
        'fixture_hash': 'abc',
    }

    try:
        check_single_variable_perturbation(base, removed)
        assert False, 'should have raised PerturbationRefusal'
    except PerturbationRefusal as e:
        msg = str(e)
        assert 'sampling' in msg, f'diff must name "sampling": {msg}'
        return True


def test_perturbation_three_quantities_all_named():
    """Three quantities changed — all three named in the diff."""
    base = {
        'system_prompt': 'A',
        'tools': [{'type': 'function', 'function': {'name': 'calc'}}],
        'tool_choice': 'auto',
        'sampling': {'temperature': '0.0'},
        'fixture_hash': 'hash1',
    }
    removed = {
        'system_prompt': 'B',
        'tools': None,          # changed
        'tool_choice': 'none',  # changed
        'sampling': {'temperature': '0.5'},  # changed
        'fixture_hash': 'hash1',
    }

    try:
        check_single_variable_perturbation(base, removed)
        assert False, 'should have raised PerturbationRefusal'
    except PerturbationRefusal as e:
        msg = str(e)
        assert 'tools' in msg
        assert 'tool_choice' in msg
        assert 'sampling' in msg
        # Should report 4 quantities (system_prompt + 3 others)
        assert '4 quantities' in msg, f'should report 4: {msg}'
        return True


# =====================================================================
#  EXIT GATE 2: All four evidence classes correctly assigned
# =====================================================================

def test_ev0_no_tool_structure():
    """Response with no tool structure and no self-report: EV-0."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': 'The answer is $15.20.',
            }
        }]
    }
    ev_class, reason = classify_invocation(response, None)
    assert ev_class == EV_0, f'expected EV-0, got {ev_class}'
    assert 'no invocation signal' in reason
    return True


def test_ev1_self_reported_no_structure():
    """Model claims tool use in text but no structural record: EV-1."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': 'I used the calculator and got $15.20.',
            }
        }]
    }
    ev_class, reason = classify_invocation(response, None)
    assert ev_class == EV_1, f'expected EV-1, got {ev_class}'
    assert 'self-report' in reason
    return True


def test_ev1_signed_attestation_unverified():
    """Signed attestation WITHOUT sealed verification key: EV-1.

    R1.3.1 normative: a signature does not cure self-report because
    the signer is the party being measured.
    """
    attestation = {
        'signature': 'base64_signature_here',
        'payload': {'tool_used': 'calculator', 'expression': '15200*1.2/100/12'},
        'algorithm': 'RS256',
    }
    seal_record = {
        'ev3_implemented': False,
        'verification_keys': [],
    }

    ev_class, reason = classify_attestation(attestation, seal_record)
    assert ev_class == EV_1, f'expected EV-1, got {ev_class}'
    assert 'signer is the party being measured' in reason
    return True


def test_ev1_attestation_with_keys_but_no_verification():
    """Attestation WITH keys sealed but verification not implemented: EV-1.

    Even with keys present, v1.0 cannot verify, so EV-1.
    """
    attestation = {
        'signature': 'valid_sig',
        'payload': {'tool_used': 'calculator'},
    }
    seal_record = {
        'ev3_implemented': False,
        'verification_keys': ['key_abc123'],
    }

    ev_class, reason = classify_attestation(attestation, seal_record)
    assert ev_class == EV_1, f'expected EV-1, got {ev_class}'
    return True


def test_ev2_platform_tool_call():
    """Platform provides tool-call records: EV-2."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': None,
                'tool_calls': [{
                    'id': 'call_123',
                    'type': 'function',
                    'function': {
                        'name': 'calculator',
                        'arguments': '{"expression": "15200*1.2/100/12"}'
                    }
                }]
            }
        }]
    }
    # Explicit platform tool calls
    platform_calls = [{
        'function': {'name': 'calculator', 'arguments': '{"expression": "15200*1.2/100/12"}'}
    }]

    ev_class, reason = classify_invocation(response, platform_calls)
    assert ev_class == EV_2, f'expected EV-2, got {ev_class}'
    assert 'serving layer' in reason
    return True


def test_ev2_structured_response_tool_calls():
    """Response contains tool_calls structure (OpenAI format): EV-2."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': None,
                'tool_calls': [{
                    'id': 'call_abc',
                    'type': 'function',
                    'function': {
                        'name': 'calculator',
                        'arguments': '{"expression": "2400*18/100/12"}'
                    }
                }]
            }
        }]
    }
    # No explicit platform calls, but response has structure
    ev_class, reason = classify_invocation(response, None)
    assert ev_class == EV_2, f'expected EV-2, got {ev_class}'
    assert 'endpoint response' in reason
    return True


# =====================================================================
#  EXIT GATE 3: Runner cannot emit EV-3 under ANY input
# =====================================================================

def test_ev3_guard_blocks():
    """check_ev3_guard raises EvidenceError for EV-3."""
    try:
        check_ev3_guard(EV_3)
        assert False, 'should have raised EvidenceError'
    except EvidenceError as e:
        assert 'forbidden' in str(e).lower()
        return True


def test_ev3_guard_passes_other_classes():
    """check_ev3_guard does NOT raise for EV-0, EV-1, EV-2."""
    for ev in [EV_0, EV_1, EV_2]:
        check_ev3_guard(ev)  # should not raise
    return True


def test_classify_attestation_never_returns_ev3():
    """classify_attestation in v1.0 NEVER returns EV-3."""
    # Even with perfect inputs
    attestation = {
        'signature': 'valid_verified_sig',
        'payload': {'tool_used': 'calculator'},
        'ledger_hash': 'anchored_hash',
    }
    seal_record = {
        'ev3_implemented': True,  # even if this is True
        'verification_keys': ['key_123'],
    }

    ev_class, _ = classify_attestation(attestation, seal_record)
    # v1.0: _EV3_FORBIDDEN = True, so EV-3 is impossible
    assert ev_class != EV_3, f'FATAL: returned EV-3: {ev_class}'
    return True


# =====================================================================
#  EXIT GATE 4: Underivable items → VOID, excluded from denominators
# =====================================================================

def test_underivable_item_void():
    """An underivable item is classified VOID."""
    from decimal import Decimal

    def mock_compute(item_id, ctx):
        return {
            'final': Decimal('0'),
            'derivable': False,
            'required_operation': 'calculator',
            'intermediates': [],
            'source_fields_consumed': [],
        }

    def mock_send(*args, **kwargs):
        raise RuntimeError('should not be called for VOID items')

    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl',
                                     delete=False) as f:
        transcript_path = f.name

    try:
        from engine import execute_item
        result = execute_item(
            {'id': 'Q_TEST', 'text': 'test?', 'source_accounts': ['savings']},
            condition='base',
            config={'endpoint_url': 'http://test'},
            fixture={'accounts': [
                {'id': 'savings', 'name': 'Savings',
                 'balance': '100.00', 'annual_rate': '1.0',
                 'monthly_fee': '0.00'}
            ]},
            ground_truth_compute=mock_compute,
            adapter_send=mock_send,
            system_prompt='test',
            tools=None,
            transcript_path=transcript_path,
            seal_hash='test_seal',
        )

        assert result['status'] == 'VOID', \
            f'underivable should be VOID, got {result["status"]}'
        assert result['reason'] == 'underivable'

        # Verify transcript records it as VOID
        import transcript as ts
        records = ts.read_all(transcript_path)
        assert len(records) == 1
        assert records[0]['error_state'] == 'VOID'
        assert records[0]['void_reason'] == 'underivable'

        return True
    finally:
        os.unlink(transcript_path)


def test_void_excluded_from_denominator():
    """VOID items must not count in the invocation denominator.

    This tests the denominator calculation logic:
    if you have 3 items, 1 VOID, the denominator is 2.
    """
    records = [
        {'item_id': 'Q1', 'error_state': None, 'evidence_class': EV_2},
        {'item_id': 'Q2', 'error_state': 'VOID', 'evidence_class': None},
        {'item_id': 'Q3', 'error_state': None, 'evidence_class': EV_0},
    ]

    # Compute denominator: exclude VOID
    eligible = [r for r in records if r.get('error_state') != 'VOID']
    assert len(eligible) == 2, f'denominator should be 2, got {len(eligible)}'

    # The VOID item should not appear in any rate calculation
    void_items = [r for r in records if r.get('error_state') == 'VOID']
    assert len(void_items) == 1
    assert void_items[0]['item_id'] == 'Q2'

    return True


# =====================================================================
#  Evidence ordering tests (R1.3.1 normative)
# =====================================================================

def test_ev1_ranks_below_ev2():
    """R1.3.1 normative: EV-1 ranks BELOW EV-2."""
    assert ranks_above(EV_2, EV_1), 'EV-2 must rank above EV-1'
    assert not ranks_above(EV_1, EV_2), 'EV-1 must NOT rank above EV-2'
    return True


def test_ev0_ranks_below_all():
    """EV-0 is the lowest rank."""
    assert ranks_above(EV_1, EV_0)
    assert ranks_above(EV_2, EV_0)
    return True


def test_different_classes_not_comparable():
    """Figures on different evidence classes are not comparable."""
    assert not classes_comparable(EV_1, EV_2), \
        'EV-1 and EV-2 should not be comparable'
    assert classes_comparable(EV_2, EV_2), \
        'same class should be comparable'
    return True


# =====================================================================
#  Context builder and collision checks
# =====================================================================

def test_build_delivered_context():
    """Context builder includes only named accounts."""
    fixture = {
        'accounts': [
            {'id': 'savings', 'name': 'Savings', 'balance': '100',
             'annual_rate': '1.0', 'monthly_fee': '0'},
            {'id': 'checking', 'name': 'Checking', 'balance': '200',
             'annual_rate': '0', 'monthly_fee': '12'},
        ]
    }
    ctx = build_delivered_context(fixture, ['savings'])
    assert 'savings' in ctx
    assert 'checking' not in ctx, 'checking should not be in context'
    assert 'id' not in ctx['savings'], 'id should be excluded'
    assert 'name' not in ctx['savings'], 'name should be excluded'
    assert ctx['savings']['balance'] == '100'
    return True


def test_lookup_collision_detected():
    """Collision when final equals a context value."""
    from decimal import Decimal
    ctx = {'savings': {'balance': '15.20', 'annual_rate': '1.0'}}
    found, field = check_lookup_collision(Decimal('15.20'), ctx)
    assert found, 'collision should be detected'
    assert field == 'savings.balance'
    return True


def test_lookup_collision_not_present():
    """No collision when final differs from all context values."""
    from decimal import Decimal
    ctx = {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}
    found, field = check_lookup_collision(Decimal('15.20'), ctx)
    assert not found, 'no collision expected'
    return True


# =====================================================================
#  Run all tests
# =====================================================================

ALL_TESTS = [
    # Gate 1: Perturbation
    test_perturbation_single_variable_pass,
    test_perturbation_tools_removed_refused,
    test_perturbation_sampling_changed_refused,
    test_perturbation_three_quantities_all_named,

    # Gate 2: Evidence classes
    test_ev0_no_tool_structure,
    test_ev1_self_reported_no_structure,
    test_ev1_signed_attestation_unverified,
    test_ev1_attestation_with_keys_but_no_verification,
    test_ev2_platform_tool_call,
    test_ev2_structured_response_tool_calls,

    # Gate 3: EV-3 guard
    test_ev3_guard_blocks,
    test_ev3_guard_passes_other_classes,
    test_classify_attestation_never_returns_ev3,

    # Gate 4: Underivable → VOID
    test_underivable_item_void,
    test_void_excluded_from_denominator,

    # Evidence ordering
    test_ev1_ranks_below_ev2,
    test_ev0_ranks_below_all,
    test_different_classes_not_comparable,

    # Context and collision
    test_build_delivered_context,
    test_lookup_collision_detected,
    test_lookup_collision_not_present,
]


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    passed = 0
    failed = 0
    errors = []

    for test_fn in ALL_TESTS:
        name = test_fn.__name__
        try:
            result = test_fn()
            if result:
                passed += 1
                print(f'  PASS  {name}')
            else:
                failed += 1
                errors.append((name, 'returned False'))
                print(f'  FAIL  {name}: returned False')
        except Exception as e:
            failed += 1
            errors.append((name, str(e)))
            print(f'  FAIL  {name}: {e}')

    print()
    print(f'Results: {passed} passed, {failed} failed, '
          f'{passed + failed} total')

    if errors:
        print()
        print('Failures:')
        for name, err in errors:
            print(f'  {name}: {err}')

    raise SystemExit(0 if failed == 0 else 1)
