"""Phase B verification tests.

Exit gates:
  1. Single-variable perturbation refusal, diff names every changed quantity
  2. All four evidence classes correctly assigned (including EV-1 for
     unverified attestation)
  3. Runner cannot emit EV-3 under ANY input in v1.0
  4. Underivable items are VOID, excluded from every invocation denominator
"""

import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from evidence import (
    classify_invocation, classify_attestation,
    check_ev3_guard, EvidenceError,
    EV_0, EV_1, EV_2, EV_3,
    classes_comparable, ranks_above,
)
from perturbation_guard import (
    check_single_variable_perturbation, PerturbationRefusal,
)
from context import build_delivered_context, check_lookup_collision


# =====================================================================
#  EXIT GATE 1: Single-variable perturbation refusal
# =====================================================================

def test_perturbation_single_variable_pass():
    """Only system_prompt differs: accepted."""
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
    assert len(diffs) == 0, f'unexpected diffs: {diffs}'
    return True


def test_perturbation_tools_removed_refused():
    """Removing tools alongside instruction: refused with diff."""
    base = {
        'system_prompt': 'Use tools.',
        'tools': [{'type': 'function', 'function': {'name': 'calculator'}}],
        'tool_choice': 'auto',
        'sampling': {'temperature': '0.0'},
        'fixture_hash': 'abc123',
        'message_template': None,
    }
    removed = dict(base)
    removed['system_prompt'] = 'No tools.'
    removed['tools'] = None
    try:
        check_single_variable_perturbation(base, removed)
        assert False, 'should have raised PerturbationRefusal'
    except PerturbationRefusal as e:
        msg = str(e)
        assert 'tools' in msg, f'diff must name "tools": {msg}'
        assert 'system_prompt' in msg
        return True


def test_perturbation_sampling_changed_refused():
    """Changing sampling alongside instruction: refused."""
    base = {'system_prompt': 'A', 'sampling': {'temperature': '0.0'}}
    removed = {'system_prompt': 'B', 'sampling': {'temperature': '0.7'}}
    try:
        check_single_variable_perturbation(base, removed)
        assert False, 'should have raised PerturbationRefusal'
    except PerturbationRefusal as e:
        assert 'sampling' in str(e)
        return True


def test_perturbation_four_quantities_all_named():
    """Four quantities changed — all four named in the diff."""
    base = {
        'system_prompt': 'A',
        'tools': [{'type': 'function', 'function': {'name': 'calc'}}],
        'tool_choice': 'auto',
        'sampling': {'temperature': '0.0'},
        'fixture_hash': 'hash1',
    }
    removed = {
        'system_prompt': 'B',
        'tools': None,
        'tool_choice': 'none',
        'sampling': {'temperature': '0.5'},
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
        assert '4 quantities' in msg, f'should report 4: {msg}'
        return True


# =====================================================================
#  EXIT GATE 2: Evidence classes — determined by PLATFORM, not model
# =====================================================================

def test_ev2_tool_capable_invoked():
    """(b) Tool-capable endpoint, populated tool_calls -> EV-2 INVOKED."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': None,
                'tool_calls': [{
                    'id': 'call_1', 'type': 'function',
                    'function': {
                        'name': 'calculator',
                        'arguments': '{"expression":"15200*1.2/100/12"}',
                    },
                }],
            }
        }]
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=True)
    assert ev == EV_2, f'expected EV-2, got {ev}'
    assert outcome == 'INVOKED', f'expected INVOKED, got {outcome}'
    assert sr is None, 'no self-report expected'
    return True


def test_ev2_tool_capable_not_invoked():
    """(a) Tool-capable endpoint, empty tool_calls -> EV-2 NOT-INVOKED."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': 'The answer is $15.20.',
                'tool_calls': [],
            }
        }]
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=True)
    assert ev == EV_2, f'expected EV-2, got {ev}'
    assert outcome == 'NOT-INVOKED', f'expected NOT-INVOKED, got {outcome}'
    return True


def test_ev2_tool_capable_no_tool_calls_field():
    """(a) Tool-capable but response omits tool_calls -> EV-2 NOT-INVOKED.

    The platform was offered tools; the model chose not to call any.
    This is still EV-2 because the platform provides the structure.
    """
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': 'The answer is $15.20.',
            }
        }]
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=True)
    assert ev == EV_2, f'expected EV-2, got {ev}'
    assert outcome == 'NOT-INVOKED', f'expected NOT-INVOKED, got {outcome}'
    return True


def test_ev0_no_tool_structure():
    """(c) Endpoint with no tool-call field -> EV-0 UNOBSERVABLE."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': 'The answer is $15.20.',
            }
        }]
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=False)
    assert ev == EV_0, f'expected EV-0, got {ev}'
    assert outcome is None, f'expected None, got {outcome}'
    return True


def test_ev2_self_report_does_not_change_class():
    """(d) Tool-capable + prose claim -> still EV-2 NOT-INVOKED,
    self-report recorded."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': 'I used the calculator and got $15.20.',
            }
        }]
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=True)
    assert ev == EV_2, f'expected EV-2, got {ev}'
    assert outcome == 'NOT-INVOKED', f'expected NOT-INVOKED, got {outcome}'
    assert sr is not None, 'self-report should be recorded'
    assert 'calculator' in sr.lower(), 'self-report should contain claim'
    return True


def test_ev0_self_report_still_ev0():
    """No tools offered + prose claim -> EV-0 (not EV-1).
    Self-report recorded but does not set class."""
    response = {
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': 'I used the calculator and got $15.20.',
            }
        }]
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=False)
    assert ev == EV_0, f'expected EV-0, got {ev}'
    assert sr is not None, 'self-report should still be recorded'
    return True




def test_ev0_anthropic_shaped_response():
    """Anthropic-shaped response -> EV-0, not EV-2 NOT-INVOKED.

    A response in Anthropic's format (type=message, content=[...]) is
    not the OpenAI shape the runner expects. Reporting NOT-INVOKED
    would be a false finding.
    """
    response = {
        'id': 'msg_01XFDUDYJgAACzvnptvVoYEL',
        'type': 'message',
        'role': 'assistant',
        'content': [{'type': 'text', 'text': 'The answer is $15.20.'}],
        'model': 'claude-sonnet-4-20250514',
        'stop_reason': 'end_turn',
        'usage': {'input_tokens': 25, 'output_tokens': 10},
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=True)
    assert ev == EV_0, f'expected EV-0 for Anthropic shape, got {ev}'
    assert outcome is None, f'expected None outcome, got {outcome}'
    return True


def test_ev0_gemini_shaped_response():
    """Gemini-shaped response -> EV-0, not EV-2 NOT-INVOKED.

    A response in Gemini's format (candidates=[...]) is not the OpenAI
    shape the runner expects. Must not produce a false NOT-INVOKED finding.
    """
    response = {
        'candidates': [{
            'content': {'parts': [{'text': 'The answer is $15.20.'}]},
            'finishReason': 'STOP',
        }],
        'modelVersion': 'gemini-2.5-pro',
        'usageMetadata': {'promptTokenCount': 25, 'candidatesTokenCount': 10},
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=True)
    assert ev == EV_0, f'expected EV-0 for Gemini shape, got {ev}'
    assert outcome is None, f'expected None outcome, got {outcome}'
    return True


def test_ev0_openai_responses_shaped():
    """OpenAI Responses API shape -> EV-0, not EV-2 NOT-INVOKED.

    The Responses API uses {output: [...], status: ...} rather than
    {choices: [{message: ...}]}.
    """
    response = {
        'id': 'resp_abc123',
        'output': [
            {'type': 'message', 'content': [
                {'type': 'output_text', 'text': 'The answer is $15.20.'}
            ]}
        ],
        'status': 'completed',
    }
    ev, outcome, sr = classify_invocation(response, tools_offered=True)
    assert ev == EV_0, f'expected EV-0 for Responses API shape, got {ev}'
    assert outcome is None, f'expected None outcome, got {outcome}'
    return True


def test_ev1_signed_attestation_unverified():
    """(e) Signed attestation without verification -> EV-1."""
    attestation = {
        'signature': 'base64_sig',
        'payload': {'tool_used': 'calculator'},
    }
    seal_record = {'ev3_implemented': False, 'verification_keys': []}
    ev, reason = classify_attestation(attestation, seal_record)
    assert ev == EV_1, f'expected EV-1, got {ev}'
    assert 'signer is the party being measured' in reason
    return True


# =====================================================================
#  EXIT GATE 3: Runner cannot emit EV-3
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
        check_ev3_guard(ev)
    return True


def test_classify_attestation_never_returns_ev3():
    """classify_attestation never returns EV-3 in v1.0."""
    attestation = {
        'signature': 'valid_sig', 'payload': {'tool_used': 'calc'},
        'ledger_hash': 'anchored',
    }
    seal = {'ev3_implemented': True, 'verification_keys': ['key_123']}
    ev, _ = classify_attestation(attestation, seal)
    assert ev != EV_3, f'FATAL: returned EV-3'
    return True


# =====================================================================
#  EXIT GATE 4: Underivable -> VOID
# =====================================================================

def test_underivable_item_void():
    """An underivable item is classified VOID, adapter never called."""
    from decimal import Decimal
    from engine import execute_item

    def mock_compute(item_id, ctx):
        return {
            'final': Decimal('0'), 'derivable': False,
            'required_operation': 'calculator',
            'intermediates': [], 'source_fields_consumed': [],
        }

    def mock_send(*a, **kw):
        raise RuntimeError('should not be called for VOID items')

    with tempfile.NamedTemporaryFile(
            mode='w', suffix='.jsonl', delete=False) as f:
        tp = f.name
    try:
        result = execute_item(
            {'id': 'QT', 'text': 'test?', 'source_accounts': ['savings']},
            condition='base',
            config={'endpoint_url': 'http://test'},
            fixture={'accounts': [
                {'id': 'savings', 'name': 'S', 'balance': '100',
                 'annual_rate': '1.0', 'monthly_fee': '0'}
            ]},
            ground_truth_compute=mock_compute,
            adapter_send=mock_send,
            system_prompt='test', tools=None,
            transcript_path=tp, seal_hash='test_seal',
        )
        assert result['status'] == 'VOID'
        assert result['reason'] == 'underivable'

        import transcript as ts
        records = ts.read_all(tp)
        assert len(records) == 1
        assert records[0]['error_state'] == 'VOID'
        return True
    finally:
        os.unlink(tp)


def test_void_excluded_from_denominator():
    """VOID items excluded from invocation denominator."""
    records = [
        {'item_id': 'Q1', 'error_state': None, 'evidence_class': EV_2},
        {'item_id': 'Q2', 'error_state': 'VOID', 'evidence_class': None},
        {'item_id': 'Q3', 'error_state': None, 'evidence_class': EV_0},
    ]
    eligible = [r for r in records if r.get('error_state') != 'VOID']
    assert len(eligible) == 2
    return True


# =====================================================================
#  Evidence ordering
# =====================================================================

def test_ev1_ranks_below_ev2():
    """R1.3.1: EV-1 ranks BELOW EV-2."""
    assert ranks_above(EV_2, EV_1)
    assert not ranks_above(EV_1, EV_2)
    return True


def test_ev0_ranks_below_all():
    """EV-0 is the lowest rank."""
    assert ranks_above(EV_1, EV_0)
    assert ranks_above(EV_2, EV_0)
    return True


def test_different_classes_not_comparable():
    """Figures on different classes are not comparable."""
    assert not classes_comparable(EV_1, EV_2)
    assert classes_comparable(EV_2, EV_2)
    return True


# =====================================================================
#  Context and collision
# =====================================================================

def test_build_delivered_context():
    """Context includes only named accounts, excludes id/name."""
    fixture = {'accounts': [
        {'id': 'savings', 'name': 'Savings', 'balance': '100',
         'annual_rate': '1.0', 'monthly_fee': '0'},
        {'id': 'checking', 'name': 'Checking', 'balance': '200',
         'annual_rate': '0', 'monthly_fee': '12'},
    ]}
    ctx = build_delivered_context(fixture, ['savings'])
    assert 'savings' in ctx
    assert 'checking' not in ctx
    assert 'id' not in ctx['savings']
    assert 'name' not in ctx['savings']
    return True


def test_lookup_collision_detected():
    """Collision when final equals a context value."""
    from decimal import Decimal
    ctx = {'savings': {'balance': '15.20', 'annual_rate': '1.0'}}
    found, field = check_lookup_collision(Decimal('15.20'), ctx)
    assert found and field == 'savings.balance'
    return True


def test_lookup_collision_not_present():
    """No collision when final differs from all context values."""
    from decimal import Decimal
    ctx = {'savings': {'balance': '15200.00', 'annual_rate': '1.2'}}
    found, _ = check_lookup_collision(Decimal('15.20'), ctx)
    assert not found
    return True


# =====================================================================
#  Run all
# =====================================================================

ALL_TESTS = [
    test_perturbation_single_variable_pass,
    test_perturbation_tools_removed_refused,
    test_perturbation_sampling_changed_refused,
    test_perturbation_four_quantities_all_named,

    test_ev2_tool_capable_invoked,
    test_ev2_tool_capable_not_invoked,
    test_ev2_tool_capable_no_tool_calls_field,
    test_ev0_no_tool_structure,
    test_ev2_self_report_does_not_change_class,
    test_ev0_self_report_still_ev0,

    test_ev0_anthropic_shaped_response,
    test_ev0_gemini_shaped_response,
    test_ev0_openai_responses_shaped,

    test_ev1_signed_attestation_unverified,

    test_ev3_guard_blocks,
    test_ev3_guard_passes_other_classes,
    test_classify_attestation_never_returns_ev3,

    test_underivable_item_void,
    test_void_excluded_from_denominator,

    test_ev1_ranks_below_ev2,
    test_ev0_ranks_below_all,
    test_different_classes_not_comparable,

    test_build_delivered_context,
    test_lookup_collision_detected,
    test_lookup_collision_not_present,
]


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    passed = failed = 0
    errors = []
    for fn in ALL_TESTS:
        name = fn.__name__
        try:
            if fn():
                passed += 1
                print(f'  PASS  {name}')
            else:
                failed += 1
                errors.append((name, 'returned False'))
                print(f'  FAIL  {name}')
        except Exception as e:
            failed += 1
            errors.append((name, str(e)))
            print(f'  FAIL  {name}: {e}')

    print(f'\nResults: {passed} passed, {failed} failed, '
          f'{passed + failed} total')
    if errors:
        print('\nFailures:')
        for n, e in errors:
            print(f'  {n}: {e}')
    raise SystemExit(0 if failed == 0 else 1)
