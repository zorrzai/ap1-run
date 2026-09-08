"""E7/E6/E3/Q09/Guard -- Tests for errata fixes.

Covers:
  B31: partial tool use -> PARTIALLY-GOVERNED (release_coverage)
  B32: same scenario, auto-matchable -> also TRANSCRIBED-ALTERED
  B33: two-call case -> GOVERNED-RELEASE
  B34: Q04 base repeat 2 acceptance from real run data
  E6:  caret (^) precedence in calculator/operation_correctness
  E3:  Q07 constant 4 resolves as declared
  E3b: AST check does not refuse declared-unused constants
  Guard: PerturbationRefusal on non-system-prompt diff
  Q09: negative magnitude matching for declared constants
  B35: ungoverned figures deduplicated by value
  B36: float noise absorbed by quantisation -> GOVERNED-RELEASE
  B37: substitution at 2nd decimal preserved -> PARTIALLY-GOVERNED

Run:
    python verify_e7_coverage.py
"""

import json
import os
import sys
from decimal import Decimal

_RUNNER_DIR = os.path.dirname(os.path.abspath(__file__))
_EXAMPLE_DIR = os.path.join(_RUNNER_DIR, 'example')
sys.path.insert(0, _RUNNER_DIR)
sys.path.insert(0, _EXAMPLE_DIR)

from provenance import resolve_operand, extract_operands
from context import build_delivered_context
from transcription import (
    check_transcription, TRANSCRIBED_EXACT,
    TRANSCRIBED_ALTERED, UNOBSERVABLE_TRANSCRIPTION,
)
from perturbation_guard import (
    check_single_variable_perturbation, PerturbationRefusal,
)
import ground_truth_example as gt_module


# -- Helpers for release_coverage tests ---------------------------------

def _make_tool_calls(returns):
    """Build mock tool_calls list from return values."""
    tcs = []
    for i, rv in enumerate(returns):
        tcs.append({
            'turn': i + 1,
            'id': f'call_{i}',
            'type': 'function',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps({'expression': f'expr_{i}'}),
            },
            'return_value': json.dumps({'result': str(rv)}),
        })
    return tcs


# ======================================================================
# B31: partial tool use -> PARTIALLY-GOVERNED
# Model reports 430.75 but tool only returned 1006.25
# ======================================================================
def test_b31_partial_tool_use_partially_governed():
    """One tool return (1006.25), model reports 430.75 -> PARTIALLY-GOVERNED."""
    from release_coverage import check_release_coverage

    tool_calls = _make_tool_calls([Decimal('1006.25')])
    candidate_figures = [Decimal('430.75')]
    expected = Decimal('430.75')

    result = check_release_coverage(tool_calls, candidate_figures, expected)
    assert result['outcome'] == 'PARTIALLY-GOVERNED', \
        f"Expected PARTIALLY-GOVERNED, got {result['outcome']}"
    assert Decimal('430.75') in result['ungoverned_figures'], \
        f"430.75 should be ungoverned, got {result['ungoverned_figures']}"
    assert '430.75' in result['finding'], \
        f"Finding should mention 430.75: {result['finding']}"
    assert '1006.25' in result['finding'], \
        f"Finding should mention tool return 1006.25: {result['finding']}"
    return True


# ======================================================================
# B32: auto-matchable -> TRANSCRIBED-ALTERED alongside coverage
# ======================================================================
def test_b32_auto_matchable_also_transcribed_altered():
    """check_transcription on same scenario returns TRANSCRIBED-ALTERED."""
    # Tool returned 1006.25, but released figure is 430.75 (AUTO-MATCH)
    result = check_transcription(
        tool_return_value=Decimal('1006.25'),
        released_figure=Decimal('430.75'),
        figure_outcome='AUTO-MATCH',
        quantisation_digits=2,
    )
    assert result['outcome'] == TRANSCRIBED_ALTERED, \
        f"Expected TRANSCRIBED-ALTERED, got {result['outcome']}"
    return True


# ======================================================================
# B33: two-call case -> GOVERNED-RELEASE
# ======================================================================
def test_b33_two_call_governed_release():
    """Two tool returns [1006.25, 430.75], model reports 430.75 -> GOVERNED-RELEASE."""
    from release_coverage import check_release_coverage

    tool_calls = _make_tool_calls([Decimal('1006.25'), Decimal('430.75')])
    candidate_figures = [Decimal('430.75')]
    expected = Decimal('430.75')

    result = check_release_coverage(tool_calls, candidate_figures, expected)
    assert result['outcome'] == 'GOVERNED-RELEASE', \
        f"Expected GOVERNED-RELEASE, got {result['outcome']}"
    assert len(result['ungoverned_figures']) == 0, \
        f"No figures should be ungoverned: {result['ungoverned_figures']}"
    return True


# ======================================================================
# B34: Q04 base repeat 2 acceptance from real run data
# ======================================================================
def test_b34_q04_acceptance_from_real_data():
    """Q04 base repeat 2 from run_a_mini returns PARTIALLY-GOVERNED.

    Real data: tool returns [1006.25], response contains 430.75 twice.
    The response text is:
      'The interest portion of the first mortgage payment is $1006.25.
       ...
       Principal portion = 1437.00 - 1006.25 = 430.75
       ...
       The principal portion of the first mortgage payment is $430.75.'
    """
    from release_coverage import check_release_coverage
    from numeric import extract_numeric_tokens

    # Real response content from Q04 base repeat 2
    response_content = (
        'The interest portion of the first mortgage payment is $1006.25. \n'
        '\n'
        'To find the principal portion, we subtract the interest from '
        'the minimum payment:\n'
        '\n'
        'Principal portion = Minimum payment - Interest portion\n'
        'Principal portion = 1437.00 - 1006.25 = 430.75\n'
        '\n'
        'The principal portion of the first mortgage payment is $430.75.'
    )

    # Real tool calls: one call returning 1006.25
    tool_calls = [{
        'turn': 1,
        'id': 'call_Q04_1',
        'type': 'function',
        'function': {
            'name': 'calculator',
            'arguments': json.dumps({'expression': '287500 * (4.20/100 / 12)'}),
        },
        'return_value': json.dumps({'result': '1006.25'}),
    }]

    expected = Decimal('430.7500')
    tolerance = Decimal('0.01')

    # Extract candidate figures from response matching expected
    tokens = extract_numeric_tokens(response_content, currency_symbols=['$'])
    candidates = [t.value for t in tokens
                  if abs(t.value - expected) <= tolerance]

    result = check_release_coverage(tool_calls, candidates, expected)

    assert result['outcome'] == 'PARTIALLY-GOVERNED', \
        f"Expected PARTIALLY-GOVERNED, got {result['outcome']}"
    assert '430.75' in result['finding'], \
        f"Finding should mention 430.75: {result['finding']}"
    assert '1006.25' in result['finding'], \
        f"Finding should mention tool return 1006.25: {result['finding']}"
    return True


def test_b35_dedup_ungoverned_by_value():
    """Duplicate candidate values are deduplicated in ungoverned_figures.

    A response containing the same ungoverned value N times yields
    one entry in ungoverned_figures (not N). The raw token count
    is preserved in ungoverned_token_count.
    """
    from release_coverage import check_release_coverage

    # Two candidates with value 430.75, one tool return of 1006.25
    tool_calls = [{
        'return_value': json.dumps({'result': '1006.25'}),
    }]
    candidates = [Decimal('430.75'), Decimal('430.75')]
    expected = Decimal('430.75')

    result = check_release_coverage(tool_calls, candidates, expected)

    assert result['outcome'] == 'PARTIALLY-GOVERNED', \
        f"Expected PARTIALLY-GOVERNED, got {result['outcome']}"

    # One distinct figure, not two
    assert len(result['ungoverned_figures']) == 1, \
        f"Expected 1 ungoverned figure, got {len(result['ungoverned_figures'])}"
    assert result['ungoverned_figures'][0] == Decimal('430.75')

    # Token count preserves the raw count
    assert result['ungoverned_token_count'] == 2, \
        f"Expected 2 token occurrences, got {result['ungoverned_token_count']}"

    # Finding text mentions the figure once, not twice
    finding = result['finding']
    count = finding.count('reported figure 430.75')
    assert count == 1, \
        f"Expected 1 mention of 430.75 in finding, got {count}: {finding}"

    # Expected finding text
    assert 'reported figure 430.75 was not returned by any tool call' in finding
    assert 'observed returns: [1006.25]' in finding
    return True


def test_b36_float_noise_governed_after_quantise():
    """IEEE 754 float noise is absorbed by quantisation.

    Tool returns 15.200000000000001 (float noise), model reports 15.20.
    After quantising both to 2 decimal places, they are equal.
    """
    from release_coverage import check_release_coverage

    tool_calls = [{
        'return_value': json.dumps({'result': '15.200000000000001'}),
    }]
    candidates = [Decimal('15.20')]
    expected = Decimal('15.200')

    result = check_release_coverage(tool_calls, candidates, expected,
                                    quantisation_places=2,
                                    quantisation_rounding='ROUND_HALF_UP')

    assert result['outcome'] == 'GOVERNED-RELEASE', \
        f"Float noise should be GOVERNED-RELEASE, got {result['outcome']}"
    return True


def test_b37_substitution_at_2nd_decimal_stays_partially_governed():
    """A substitution at the declared precision stays PARTIALLY-GOVERNED.

    Tool returned 430.75, model reported 430.76.  After quantising
    both to 2 decimal places, they are NOT equal (real substitution).
    """
    from release_coverage import check_release_coverage

    tool_calls = [{
        'return_value': json.dumps({'result': '430.75'}),
    }]
    candidates = [Decimal('430.76')]
    expected = Decimal('430.76')

    result = check_release_coverage(tool_calls, candidates, expected,
                                    quantisation_places=2,
                                    quantisation_rounding='ROUND_HALF_UP')

    assert result['outcome'] == 'PARTIALLY-GOVERNED', \
        f"Substitution should be PARTIALLY-GOVERNED, got {result['outcome']}"
    assert len(result['ungoverned_figures']) == 1
    assert result['ungoverned_figures'][0] == Decimal('430.76')
    return True


# ======================================================================
# E6: caret precedence
# ======================================================================
def test_e6_caret_precedence():
    """(1+0.078/12)^3-1 evaluates as ((1+0.078/12)**3)-1."""
    from operation_correctness import evaluate_expression

    # The correct computation:
    # 1 + 0.078/12 = 1.0065
    # 1.0065 ** 3 = 1.01962... (approximately)
    # 1.01962... - 1 = 0.01962...
    result = evaluate_expression('(1+0.078/12)^3-1')
    expected_approx = Decimal('0.0196')

    # Must be close to 0.0196, NOT close to 1.013 (XOR result)
    assert abs(result - expected_approx) < Decimal('0.001'), \
        f"Expected ~0.0196, got {result}"
    # Must NOT be the XOR interpretation
    assert abs(result - Decimal('1.013')) > Decimal('0.1'), \
        f"Got XOR result {result}, caret not fixed"
    return True


# ======================================================================
# E3: Q07 constant 4 resolves as declared
# ======================================================================
def test_e3_q07_constant_4_resolves():
    """Operand 4 in Q07 resolves at step 1 as declared constant."""
    with open(os.path.join(_EXAMPLE_DIR, 'fixture.json'), 'r',
              encoding='utf-8') as f:
        fixture = json.load(f)
    with open(os.path.join(_EXAMPLE_DIR, 'questions.json'), 'r',
              encoding='utf-8') as f:
        questions = json.load(f)

    q07 = next(q for q in questions['items'] if q['id'] == 'Q07')
    ctx = build_delivered_context(fixture, q07.get('source_accounts', []))
    gt = gt_module.compute('Q07', ctx)

    from provenance import _collect_constants
    constants = _collect_constants(gt)

    assert Decimal('4') in constants, \
        f"4 not in declared constants: {constants}"

    # Resolve operand 4
    intermediates = []
    for inter in gt.get('intermediates', []):
        val = inter['value']
        if not isinstance(val, Decimal):
            val = Decimal(str(val))
        intermediates.append({'label': inter['label'], 'value': val})

    result = resolve_operand(
        Decimal('4'), ctx, intermediates, constants,
        permitted_transforms=[], quant_config={'places': 2, 'rounding': 'ROUND_HALF_UP'})

    assert result['step'] == 1, \
        f"Expected step 1 (constant), got step {result['step']}"
    assert result['resolution'] == 'constant', \
        f"Expected resolution 'constant', got {result['resolution']}"
    return True


# ======================================================================
# E3b: AST check does not refuse declared-unused constants
# ======================================================================
def test_e3b_ast_check_allows_unused_constants():
    """Q07 declares constant 4 but derive_q07 does not use D('4').
    The AST check must NOT refuse this."""
    from seal_constants import declared_constants_check
    from config import load_config

    config = load_config(os.path.join(_EXAMPLE_DIR, 'config.json'))
    with open(os.path.join(_EXAMPLE_DIR, 'fixture.json'), 'r',
              encoding='utf-8') as f:
        fixture = json.load(f)
    with open(os.path.join(_EXAMPLE_DIR, 'questions.json'), 'r',
              encoding='utf-8') as f:
        questions = json.load(f)

    # Should NOT raise SealError
    failures = declared_constants_check(gt_module, fixture, questions)
    assert len(failures) == 0, \
        f"AST check should not refuse declared-unused constants: {failures}"
    return True


# ======================================================================
# Guard: PerturbationRefusal on non-system-prompt diff
# ======================================================================
def test_guard_perturbation_refusal():
    """Config differing in tool_choice raises PerturbationRefusal."""
    base = {
        'system_prompt': 'You are a financial calculator assistant.',
        'tools': [{'type': 'function', 'function': {'name': 'calculator'}}],
        'tool_choice': 'auto',
        'sampling': {'temperature': 0},
        'fixture_hash': 'abc123',
        'message_template': None,
    }
    removed = dict(base)
    removed['system_prompt'] = 'You are an assistant.'  # allowed change
    removed['tool_choice'] = 'none'  # FORBIDDEN change

    try:
        check_single_variable_perturbation(base, removed)
        return False  # Should have raised
    except PerturbationRefusal as e:
        assert 'tool_choice' in str(e), \
            f"Error should mention tool_choice: {e}"
        return True


# ======================================================================
# Q09: negative magnitude matching for declared constants
# ======================================================================
def test_q09_negative_12_resolves_to_constant():
    """Operand -12 with declared constant 12 resolves at step 1."""
    constants = {Decimal('100'), Decimal('12'), Decimal('1')}
    result = resolve_operand(
        Decimal('-12'),
        delivered_context={},  # empty - no source match
        intermediates=[],
        constants=constants,
        permitted_transforms=[],
        quant_config={'places': 2, 'rounding': 'ROUND_HALF_UP'},
    )
    # This should resolve as constant (magnitude match)
    assert result['step'] == 1, \
        f"Expected step 1 (constant), got step {result['step']}: {result}"
    assert 'constant' in result['resolution'], \
        f"Expected constant resolution, got {result['resolution']}"
    return True


def test_q09_positive_12_still_resolves():
    """Operand 12 with declared constant 12 still resolves at step 1."""
    constants = {Decimal('100'), Decimal('12'), Decimal('1')}
    result = resolve_operand(
        Decimal('12'),
        delivered_context={},
        intermediates=[],
        constants=constants,
        permitted_transforms=[],
        quant_config={'places': 2, 'rounding': 'ROUND_HALF_UP'},
    )
    assert result['step'] == 1, \
        f"Expected step 1, got step {result['step']}"
    assert result['resolution'] == 'constant', \
        f"Expected 'constant', got {result['resolution']}"
    return True


def test_q09_q05_unaffected():
    """Q05's operands still resolve correctly after magnitude matching."""
    with open(os.path.join(_EXAMPLE_DIR, 'fixture.json'), 'r',
              encoding='utf-8') as f:
        fixture = json.load(f)
    with open(os.path.join(_EXAMPLE_DIR, 'questions.json'), 'r',
              encoding='utf-8') as f:
        questions = json.load(f)

    q05 = next(q for q in questions['items'] if q['id'] == 'Q05')
    ctx = build_delivered_context(fixture, q05.get('source_accounts', []))
    gt = gt_module.compute('Q05', ctx)

    from provenance import _collect_constants
    constants = _collect_constants(gt)

    # Q05 uses: balance(2400), rate(18.0), min_payment(25), 100, 12
    # No negative operands expected in standard derivation
    # Verify 100 and 12 resolve as constants
    for c in [Decimal('100'), Decimal('12')]:
        r = resolve_operand(c, ctx, [], constants, [], {'places': 2, 'rounding': 'ROUND_HALF_UP'})
        assert r['step'] == 1, f"Q05 constant {c} should resolve step 1, got {r['step']}"
    return True


def test_q09_q08_unaffected():
    """Q08's operands still resolve correctly after magnitude matching."""
    with open(os.path.join(_EXAMPLE_DIR, 'fixture.json'), 'r',
              encoding='utf-8') as f:
        fixture = json.load(f)
    with open(os.path.join(_EXAMPLE_DIR, 'questions.json'), 'r',
              encoding='utf-8') as f:
        questions = json.load(f)

    q08 = next(q for q in questions['items'] if q['id'] == 'Q08')
    ctx = build_delivered_context(fixture, q08.get('source_accounts', []))
    gt = gt_module.compute('Q08', ctx)

    from provenance import _collect_constants
    constants = _collect_constants(gt)

    for c in [Decimal('100'), Decimal('12')]:
        r = resolve_operand(c, ctx, [], constants, [], {'places': 2, 'rounding': 'ROUND_HALF_UP'})
        assert r['step'] == 1, f"Q08 constant {c} should resolve step 1, got {r['step']}"
    return True


# ======================================================================
# Test registry
# ======================================================================

ALL_TESTS = [
    test_b31_partial_tool_use_partially_governed,
    test_b32_auto_matchable_also_transcribed_altered,
    test_b33_two_call_governed_release,
    test_b34_q04_acceptance_from_real_data,
    test_e6_caret_precedence,
    test_e3_q07_constant_4_resolves,
    test_e3b_ast_check_allows_unused_constants,
    test_guard_perturbation_refusal,
    test_q09_negative_12_resolves_to_constant,
    test_q09_positive_12_still_resolves,
    test_q09_q05_unaffected,
    test_q09_q08_unaffected,
    test_b35_dedup_ungoverned_by_value,
    test_b36_float_noise_governed_after_quantise,
    test_b37_substitution_at_2nd_decimal_stays_partially_governed,
]


def main():
    print('=' * 60)
    print('E7/E6/E3/Q09/GUARD TEST SUITE')
    print('=' * 60)
    passed = 0
    failed = 0
    for test_fn in ALL_TESTS:
        name = test_fn.__name__
        try:
            result = test_fn()
            if result:
                passed += 1
                print('  PASS  ' + name)
            else:
                failed += 1
                print('  FAIL  ' + name)
        except Exception as e:
            failed += 1
            import traceback
            print('  FAIL  ' + name)
            print('         ' + str(e))
            traceback.print_exc()
    print()
    total = len(ALL_TESTS)
    print('Results: ' + str(passed) + ' passed, '
          + str(failed) + ' failed, ' + str(total) + ' total')
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
