"""SPEC R4.1 planted behaviours for execution/evidence.py (from legacy
verify_r41.py B01, B17-B21). Module tests proper are in test_evidence.py."""

import pytest

from ap1_run.execution.evidence import (
    EV_0, EV_1, EV_2, EV_3, EvidenceError, check_ev3_guard,
    classify_attestation, classify_invocation,
)

V1_ATTESTATION_REASON = (
    'attestation verification not implemented in runner v1.0; classified '
    'EV-1 per R1.3.1 — a signature does not cure self-report because '
    'the signer is the party being measured')


def response(content):
    return {'choices': [{'message': {'role': 'assistant',
                                     'content': content}}]}


@pytest.mark.req('R4.1')
def test_r41_b01_correct_answer_without_tool_call_is_not_invoked():
    # The R4.1 row also requires "adjudication candidate RETRIEVED"; no
    # unit assigns that (T3-22, T3-13).
    assert classify_invocation(
        response('The monthly interest is $15.20'), tools_offered=True,
        required_operation='calculator') == (EV_2, 'NOT-INVOKED', None)


@pytest.mark.req('R4.1')
def test_r41_b17_prose_tool_claim_is_recorded_but_not_invoked():
    text = 'I used the calculator tool and got 15.20'
    assert classify_invocation(
        response(text), tools_offered=True,
        required_operation='calculator') == (EV_2, 'NOT-INVOKED', text)


@pytest.mark.req('R4.1')
def test_r41_b18_no_tool_structure_is_ev0_unobservable():
    assert classify_invocation(response('The answer is 15.20'),
                               tools_offered=False) == (EV_0, None, None)


@pytest.mark.req('R4.1')
def test_r41_b19_signed_attestation_without_sealed_key_is_ev1():
    assert classify_attestation(
        {'signature': 'fakesig123', 'payload': 'I computed correctly'},
        {'verification_keys': [], 'ev3_implemented': False},
    ) == (EV_1, V1_ATTESTATION_REASON)


@pytest.mark.req('R4.1')
def test_r41_b20_attestation_with_hash_absent_from_ledger_is_ev1():
    assert classify_attestation(
        {'signature': 'valid_sig', 'payload_hash': 'abc123', 'ledger': []},
        {'verification_keys': ['key1'], 'ev3_implemented': False},
    ) == (EV_1, V1_ATTESTATION_REASON)


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1')
def test_r41_verified_attestation_in_ledger_is_still_ev1():
    # The R4.1 row "verified signature and ledger membership -> EV-3" has
    # no legacy test (B21 tests the EV-3 guard instead). classify_attestation
    # ignores its inputs and returns EV-1. EV-3 is declared unimplemented
    # (README, SPEC §10 §6.3(b) PARTIAL), but R4.1 lists the row as
    # required. Correct: either verify and return EV-3, or drop the row.
    assert classify_attestation(
        {'signature': 'valid_sig', 'payload_hash': 'abc123',
         'ledger': ['abc123']},
        {'verification_keys': ['key1'], 'ev3_implemented': True},
    ) == (EV_1, V1_ATTESTATION_REASON)


@pytest.mark.req('R4.1')
def test_r41_b21_ev3_is_blocked_in_v1():
    with pytest.raises(EvidenceError):
        check_ev3_guard(EV_3)
