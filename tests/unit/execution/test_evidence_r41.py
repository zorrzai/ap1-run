"""SPEC R4.1 planted behaviours for execution/evidence.py (from legacy
verify_r41.py B01, B17-B21). Module tests proper are in test_evidence.py."""

from pathlib import Path

import pytest

from ap1_run.execution import evidence
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
    # (README, SPEC §10 §6.3(b) PARTIAL), and R4.1 now marks the row a
    # declared exception (see the test below); building EV-3 would turn
    # this into a test of EV-3.
    assert classify_attestation(
        {'signature': 'valid_sig', 'payload_hash': 'abc123',
         'ledger': ['abc123']},
        {'verification_keys': ['key1'], 'ev3_implemented': True},
    ) == (EV_1, V1_ATTESTATION_REASON)


@pytest.mark.req('R4.1')
def test_r41_b21_ev3_is_blocked_in_v1():
    with pytest.raises(EvidenceError):
        check_ev3_guard(EV_3)


SPEC = Path(__file__).resolve().parents[3] / 'docs' / 'SPEC.md'


def spec_section(text, heading, next_heading):
    start = text.index(heading)
    return text[start:text.index(next_heading, start)]


@pytest.mark.proposal(
    'T3-22: SPEC reading, decided in review: R4.1 lists three EV-3 rows '
    'as required while SPEC §10 declares EV-3 not built; §10 governs, so '
    'the three rows are declared exceptions')
@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R1.3.1')
def test_r41_ev3_rows_are_declared_exceptions_while_ev3_is_not_built():
    spec = SPEC.read_text(encoding='utf-8')
    r41 = spec_section(spec, '### R4.1', '### R4.2')
    rows = [line for line in r41.splitlines()
            if line.startswith('| **Signed attestation')]
    assert len(rows) == 3, rows
    assert all('declared exception' in row for row in rows), rows
    assert '**Declared exceptions: the three signed-attestation rows.**' \
        in r41
    # §10, the side that governs, still says EV-3 is not built ...
    assert '| §6.3(b) structural evidence | evidence.py EV-3 gated False ' \
        '| PARTIAL |' in spec_section(spec, '## 10.', '## 11.')
    # ... and so does the code: no attestation reaches EV-3.
    assert evidence._EV3_FORBIDDEN is True
    with pytest.raises(EvidenceError):
        check_ev3_guard(EV_3)
