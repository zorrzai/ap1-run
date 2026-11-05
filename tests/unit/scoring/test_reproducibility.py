"""Unit tests for scoring/reproducibility.py: the D2 mechanism class per
surface and the parameter-echo check (R2.2)."""

from decimal import Decimal as D
from fractions import Fraction

import pytest

from ap1_run.scoring.reproducibility import (
    CONFIGURED, OBSERVED_ONLY, STRUCTURAL, UNMEASURED, VALID_CLASSES,
    ReproducibilityError, _extract_surface_values, _is_error_or_limited,
    check_parameter_echo, classify_mechanism, distinct_figures_shown,
)


def response(content, tool_calls=None):
    """A minimal OpenAI-shaped response."""
    message = {'role': 'assistant', 'content': content}
    if tool_calls is not None:
        message['tool_calls'] = tool_calls
    return {'choices': [{'message': message}]}


def tool_call(arguments):
    return {'id': 'c1', 'type': 'function',
            'function': {'name': 'calculator', 'arguments': arguments}}


LIMITED = {'error': True, 'status_code': 429, 'rate_limited': True}


def test_mechanism_constants():
    assert (STRUCTURAL, CONFIGURED, OBSERVED_ONLY, UNMEASURED) == (
        'STRUCTURAL', 'CONFIGURED', 'OBSERVED-ONLY', 'UNMEASURED')
    assert VALID_CLASSES == frozenset(
        {'STRUCTURAL', 'CONFIGURED', 'OBSERVED-ONLY', 'UNMEASURED'})


def test_reproducibility_error_is_an_exception():
    # Defined but raised nowhere.
    assert issubclass(ReproducibilityError, Exception)


# -- classify_mechanism: minimum runs ---------------------------------------

@pytest.mark.req('R2.2')
def test_classify_mechanism_below_minimum_is_unmeasured():
    assert classify_mechanism([response('$15.20')] * 2, surface='prose',
                              minimum_runs=3) == {
        'mechanism': 'UNMEASURED',
        'operator_declared': False,
        'distinct_values': None,
        'successful_runs': 2,
        'reason': '2 successful runs below minimum 3 — UNMEASURED',
    }


@pytest.mark.req('R2.2')
def test_classify_mechanism_rate_limited_runs_do_not_count():
    responses = [LIMITED] * 49 + [response('The answer is $15.20.')]
    r = classify_mechanism(responses, surface='prose', minimum_runs=3)
    assert r['mechanism'] == UNMEASURED
    assert r['successful_runs'] == 1
    assert r['reason'] == '1 successful runs below minimum 3 — UNMEASURED'


def test_classify_mechanism_exactly_minimum_is_measured():
    r = classify_mechanism([response('a')] * 3, surface='prose', minimum_runs=3)
    assert r['mechanism'] == OBSERVED_ONLY
    assert r['successful_runs'] == 3


def test_classify_mechanism_below_minimum_ignores_operator_declaration():
    r = classify_mechanism([response('a')], surface='prose', minimum_runs=2,
                           operator_declared=STRUCTURAL)
    assert r['mechanism'] == UNMEASURED
    assert r['operator_declared'] is False


@pytest.mark.finding('S3-G5-3')
def test_classify_mechanism_no_responses_with_zero_minimum_is_unmeasured():
    # Fixed (S3-G5-3): with minimum_runs=0 an empty pool used to be
    # OBSERVED-ONLY from 0 runs; no observations is UNMEASURED.
    assert classify_mechanism([], surface='prose', minimum_runs=0) == {
        'mechanism': 'UNMEASURED',
        'operator_declared': False,
        'distinct_values': None,
        'successful_runs': 0,
        'reason': '0 successful runs — UNMEASURED',
    }


def test_classify_mechanism_only_errored_runs_with_zero_minimum_is_unmeasured():
    r = classify_mechanism([{'error': 'boom'}], surface='figures',
                           minimum_runs=0)
    assert (r['mechanism'], r['successful_runs']) == (UNMEASURED, 0)


def test_classify_mechanism_arguments_are_keyword_only():
    with pytest.raises(TypeError):
        classify_mechanism([], 'prose', 0)


# -- classify_mechanism: operator declaration --------------------------------

@pytest.mark.req('R2.2')
def test_classify_mechanism_operator_declared_structural_is_marked():
    responses = [response('$15.20')] * 4 + [response('$15.21')]
    assert classify_mechanism(responses, surface='figures', minimum_runs=3,
                              operator_declared=STRUCTURAL) == {
        'mechanism': 'STRUCTURAL',
        'operator_declared': True,
        'distinct_values': 2,
        'successful_runs': 5,
        'reason': 'operator-declared STRUCTURAL for figures',
    }


def test_classify_mechanism_operator_declared_configured_is_marked():
    r = classify_mechanism([response('a')] * 3, surface='prose',
                           minimum_runs=3, operator_declared=CONFIGURED)
    assert r['mechanism'] == CONFIGURED
    assert r['operator_declared'] is True
    assert r['reason'] == 'operator-declared CONFIGURED for prose'


def test_classify_mechanism_other_declarations_are_ignored():
    for declared in (OBSERVED_ONLY, UNMEASURED, 'structural', 'bogus'):
        r = classify_mechanism([response('a')] * 3, surface='prose',
                               minimum_runs=3, operator_declared=declared)
        assert r['mechanism'] == OBSERVED_ONLY
        assert r['operator_declared'] is False


# -- classify_mechanism: from evidence ---------------------------------------

def test_classify_mechanism_one_distinct_value_is_observed_only():
    assert classify_mechanism([response('$15.20')] * 5, surface='prose',
                              minimum_runs=3) == {
        'mechanism': 'OBSERVED-ONLY',
        'operator_declared': False,
        'distinct_values': 1,
        'successful_runs': 5,
        'reason': '5 runs, 1 distinct value — OBSERVED-ONLY',
    }


@pytest.mark.finding('T3-4')
def test_classify_mechanism_many_distinct_values_is_also_observed_only():
    # Both branches return OBSERVED-ONLY, so 5 identical and 5 different
    # answers get the same class; only distinct_values differs. This is
    # correct (AP-1 D2.1; step-4 g7 report): from evidence the runner can
    # only tell OBSERVED-ONLY from UNMEASURED. The distinct values per
    # question and surface reach report §9 (T3-4).
    responses = [response(f'${v}') for v in ('1', '2', '3', '4', '5')]
    assert classify_mechanism(responses, surface='prose', minimum_runs=3) == {
        'mechanism': 'OBSERVED-ONLY',
        'operator_declared': False,
        'distinct_values': 5,
        'successful_runs': 5,
        'reason': '5 runs, 5 distinct values — OBSERVED-ONLY',
    }


def test_classify_mechanism_errored_runs_are_left_out_of_the_values():
    responses = [response('a'), {'error': 'boom'}, response('a'), response('a')]
    r = classify_mechanism(responses, surface='prose', minimum_runs=3)
    assert r['successful_runs'] == 3
    assert r['distinct_values'] == 1


# -- distinct_figures_shown (T3-4) --------------------------------------------

@pytest.mark.finding('T3-4')
def test_distinct_figures_shown_lists_each_value_as_first_stated():
    # AP-1 D2: "distinct numeric answers per question". 15.2 and 15.20 are
    # one figure (as classify_mechanism counts them), shown as first
    # written; errored and rate-limited runs are left out.
    responses = [response('It is $2,600.00 after 5% growth.'),
                 LIMITED,
                 response('The answer: 2500.00'),
                 response('2600.0 after 5.0% growth'),
                 {'error': 'boom'},
                 response('I cannot say.'),
                 response('2500 again')]
    assert distinct_figures_shown(responses) == [
        '2600.00, 5%', '2500.00', 'no figures']


@pytest.mark.finding('T3-4')
def test_distinct_figures_shown_count_matches_the_classifier():
    responses = [response(f'${v}') for v in ('1', '2', '2.0', '3', '1')]
    shown = distinct_figures_shown(responses)
    r = classify_mechanism(responses, surface='figures', minimum_runs=3)
    assert shown == ['1', '2', '3']
    assert len(shown) == r['distinct_values']


def test_distinct_figures_shown_of_nothing():
    assert distinct_figures_shown([]) == []


@pytest.mark.finding('S3-G5-3')
def test_classify_mechanism_unknown_surface_message_names_it():
    # Fixed (S3-G5-3): an unknown surface used to be OBSERVED-ONLY with 0
    # distinct values; it is refused, before any response is looked at.
    with pytest.raises(ReproducibilityError,
                       match=r"unknown surface 'Figures'; expected one of "
                             r"\('figures', 'prose'\)"):
        classify_mechanism([], surface='Figures', minimum_runs=3)


# -- _extract_surface_values -------------------------------------------------

def test_surface_values_prose_is_the_content():
    assert _extract_surface_values(
        [response('a'), response(None), {'choices': []}, {}],
        'prose') == ['a', '', '', '']


def test_surface_values_prose_ignores_tool_calls():
    assert _extract_surface_values(
        [response('a', [tool_call('{"expression": "1+1"}')])],
        'prose') == ['a']


def test_surface_values_prose_message_without_content_is_empty():
    assert _extract_surface_values([{'choices': [{'message': {}}]},
                                    {'choices': [{}]}], 'prose') == ['', '']


def test_surface_values_unknown_surface_is_empty():
    assert _extract_surface_values([response('a')], 'other') == []


# -- _is_error_or_limited ----------------------------------------------------

def test_is_error_or_limited_non_dict_is_an_error():
    assert _is_error_or_limited(None) is True
    assert _is_error_or_limited('text') is True
    assert _is_error_or_limited([]) is True


def test_is_error_or_limited_error_field():
    assert _is_error_or_limited({'error': 'boom'}) is True
    assert _is_error_or_limited({'error': True}) is True
    assert _is_error_or_limited({'error': None}) is False
    assert _is_error_or_limited({'error': ''}) is False


def test_is_error_or_limited_http_429():
    assert _is_error_or_limited({'status_code': 429}) is True


def test_is_error_or_limited_other_status_codes_are_not_errors():
    assert _is_error_or_limited({'status_code': 500}) is False
    assert _is_error_or_limited({'status_code': 200}) is False


def test_is_error_or_limited_rate_limited_flag():
    assert _is_error_or_limited({'rate_limited': True}) is True
    assert _is_error_or_limited({'rate_limited': False}) is False


def test_is_error_or_limited_plain_response_is_not():
    assert _is_error_or_limited(response('a')) is False
    assert _is_error_or_limited({}) is False


# -- check_parameter_echo ----------------------------------------------------

@pytest.mark.req('R2.2')
def test_parameter_echo_no_echo_is_unverified():
    assert check_parameter_echo({'temperature': '0.0'}, None) == {
        'verified': False, 'findings': [], 'status': 'UNVERIFIED',
        'not_echoed': ['temperature']}


def test_parameter_echo_all_applied_is_verified():
    assert check_parameter_echo(
        {'temperature': '0.0', 'top_p': 1},
        {'temperature': '0.0', 'top_p': '1', 'seed': 7}) == {
        'verified': True, 'findings': [], 'status': 'VERIFIED',
        'not_echoed': []}


def test_parameter_echo_nothing_requested_is_verified():
    assert check_parameter_echo({}, {})['status'] == 'VERIFIED'


@pytest.mark.req('R2.2', 'AP-1 D2.2')
def test_parameter_echo_changed_parameter_is_a_finding_unechoed_is_not():
    # AP-1 v1.3 D2.2: "a parameter requested and silently ignored is a
    # platform finding". One not echoed was not shown ignored: it is
    # unverified, not a finding.
    assert check_parameter_echo(
        {'temperature': '0.0', 'top_p': '1.0'}, {'temperature': '0.7'}) == {
        'verified': False,
        'findings': [
            "parameter 'temperature': requested='0.0', applied='0.7' "
            '— silently ignored',
        ],
        'status': 'MISMATCH',
        'not_echoed': ['top_p'],
    }


@pytest.mark.req('R2.2', 'AP-1 D2.2')
def test_parameter_echo_some_echoed_and_matching_is_unverified_not_mismatch():
    # The sampling of example/config_mini.json, with
    # only temperature echoed (a token limit named otherwise by the API).
    r = check_parameter_echo({'temperature': '1', 'max_completion_tokens':
                              '4096'}, {'temperature': 1})
    assert r == {'verified': False, 'findings': [], 'status': 'UNVERIFIED',
                 'not_echoed': ['max_completion_tokens']}


def test_parameter_echo_echoed_none_counts_as_not_echoed():
    r = check_parameter_echo({'seed': 7}, {'seed': None})
    assert (r['findings'], r['not_echoed'], r['status']) == (
        [], ['seed'], 'UNVERIFIED')


@pytest.mark.finding('S3-G5-4')
@pytest.mark.parametrize('requested, echoed, status', [
    ('1', 1.0, 'VERIFIED'), ('0', 0.0, 'VERIFIED'), ('0.10', 0.1, 'VERIFIED'),
    (0, 0.0, 'VERIFIED'), ('1', 0.7, 'MISMATCH'), ('0.1', 0.10000001,
                                                   'MISMATCH'),
    # compared with what was sent: this request goes out as the float 0.1
    ('0.10000000000000001', 0.1, 'VERIFIED')])
def test_parameter_echo_compares_numbers_as_numbers(requested, echoed,
                                                   status):
    assert check_parameter_echo({'temperature': requested},
                                {'temperature': echoed})['status'] == status


def test_parameter_echo_non_numbers_compare_as_text():
    assert check_parameter_echo({'effort': 'low'}, {'effort': 'low'})[
        'status'] == 'VERIFIED'
    assert check_parameter_echo({'effort': 'low'}, {'effort': 'high'})[
        'status'] == 'MISMATCH'


def test_parameter_echo_compares_as_strings():
    assert check_parameter_echo({'t': 0.0}, {'t': '0.0'})['status'] == 'VERIFIED'


# --- Step 4: correct behaviour (failing until fixed) ---
# xfail(strict=True) until the fix.

def _answer(text):
    return {'choices': [{'message': {'role': 'assistant', 'content': text}}]}


@pytest.mark.finding('T3-4')
def test_classify_mechanism_figures_surface_counts_numeric_answers():
    # SPEC R2.2: classes per surface, "separately for computed figures and
    # for surrounding prose"; AP-1 D2 Method: "the number of distinct
    # numeric answers per question". Correct: the same figure worded twice
    # is one distinct value on the figures surface, two on prose.
    responses = [_answer('The monthly interest is $15.20.'),
                 _answer('Interest per month: $15.20')]
    figures = classify_mechanism(responses, surface='figures',
                                 minimum_runs=2)
    prose = classify_mechanism(responses, surface='prose', minimum_runs=2)
    assert prose['distinct_values'] == 2
    assert figures['distinct_values'] == 1, figures


@pytest.mark.finding('S3-G5-4')
def test_parameter_echo_numerically_equal_values_verified():
    # SPEC R2.2: "a parameter requested and silently ignored is a platform
    # finding". 0 and 0.0 are the same temperature. Correct: numbers are
    # compared as numbers (exactly, as Decimal of their text).
    r = check_parameter_echo({'temperature': 0}, {'temperature': 0.0})
    assert r['status'] == 'VERIFIED', r['findings']
    assert r['findings'] == []


@pytest.mark.finding('S3-G5-3')
@pytest.mark.req('R2.2')
def test_classify_mechanism_unknown_surface_is_refused():
    # The surfaces are 'figures' and 'prose' (docstring). Any other name
    # is a caller error: refuse it with ReproducibilityError (defined for
    # this, never raised), rather than classify zero values.
    try:
        r = classify_mechanism([response('a')] * 3, surface='Figures',
                               minimum_runs=3)
        outcome = r['mechanism']
    except ReproducibilityError:
        outcome = 'refused'
    assert outcome == 'refused'


@pytest.mark.finding('S3-G5-3')
@pytest.mark.req('R2.2')
def test_classify_mechanism_no_observations_is_unmeasured():
    # Zero successful runs say nothing about the mechanism: UNMEASURED,
    # whatever the minimum. SPEC R2.2: the runner tells OBSERVED-ONLY from
    # UNMEASURED "from evidence"; its contract case (49 rate-limited runs
    # and one success is UNMEASURED) is the same rule with one run.
    r = classify_mechanism([], surface='prose', minimum_runs=0)
    assert r['mechanism'] == UNMEASURED


@pytest.mark.finding('S3-G5-4')
@pytest.mark.parametrize('requested, echoed, status', [
    ('0.70', 0.7, 'VERIFIED'),          # equal as numbers
    (1, '1.0', 'VERIFIED'),
    ('auto', 'auto', 'VERIFIED'),       # equal as text
    ('auto', 'none', 'MISMATCH'),       # text, not numbers
    (True, 1, 'MISMATCH'),              # a bool is not the number 1
    (0.5, 'high', 'MISMATCH'),          # one side not a number
    ('sNaN', 'sNaN', 'VERIFIED'),       # same text, never compared as numbers
    ('sNaN', '0', 'MISMATCH'),          # a signalling NaN never raises out
    (0.7, 0.70001, 'MISMATCH'),
])
def test_parameter_echo_compares_numbers_as_decimals_else_text(
        requested, echoed, status):
    r = check_parameter_echo({'p': requested}, {'p': echoed})
    assert r['status'] == status
    assert r['verified'] is (status == 'VERIFIED')


# -- The figures surface (T3-4) ------------------------------------------

@pytest.mark.finding('T3-4')
@pytest.mark.req('R2.2', 'AP-1 D2')
def test_surface_values_figures_are_the_stated_numbers():
    # The set of numeric figures in the text, each its exact value, with
    # its percent flag: order, repetition and wording don't matter; tool
    # calls in the message are not figures; no text is no figures.
    responses = [
        response('$15.20 at 1.2%'),
        response('At 1.2%, it is 15.2, so 15.20.'),
        response('$182.40', [tool_call('{"expression": "15200 * 0.012"}')]),
        response(None), {'choices': []}, {}, {'choices': [{}]},
        response('1.2 and 1.2%'),
    ]
    F = Fraction
    assert _extract_surface_values(responses, 'figures') == [
        ((F('1.2'), True), (F('15.2'), False)),
        ((F('1.2'), True), (F('15.2'), False)),
        ((F('182.4'), False),),
        (), (), (), (),
        ((F('1.2'), False), (F('1.2'), True)),
    ]


@pytest.mark.finding('T3-4')
@pytest.mark.parametrize('error', ['AmbiguousLocaleError', 'ArithmeticError',
                                   'ValueError'])
def test_surface_values_figures_unreadable_text_is_its_own_value(
        monkeypatch, error):
    import builtins
    from ap1_run.scoring import reproducibility
    exc = getattr(reproducibility, error, None) or getattr(builtins, error)

    def refuse(text):
        raise exc(text)
    monkeypatch.setattr(reproducibility, 'extract_numeric_tokens', refuse)
    assert _extract_surface_values([response('1.780')], 'figures') == \
        [('unreadable', '1.780')]


@pytest.mark.finding('T3-4')
def test_classify_mechanism_figures_distinct_values_count_answers():
    responses = [response('It is $2600.00.'), response('$2,600 left.'),
                 response('It is $2500.00.')]
    r = classify_mechanism(responses, surface='figures', minimum_runs=3)
    assert (r['distinct_values'], r['successful_runs']) == (2, 3)


# A response whose shape cannot be read has no
# surface value, as one without choices; never an exception (S3-G2-1).

@pytest.mark.finding('S3-G2-1')
@pytest.mark.parametrize('surface', ['figures', 'prose'])
def test_surface_values_unreadable_shape_is_empty(surface):
    assert _extract_surface_values(
        ['text', {'choices': ['x']}, {'choices': [{'message': None}]},
         {'choices': {'a': 1}},
         {'choices': [{'message': {'content': ['x']}}]},
         {'choices': [{'message': {'tool_calls': ['x']}}]}],
        surface) == ([()] if surface == 'figures' else ['']) * 6
    # (figures: no text states no figures, T3-4)


# -- The figures surface is the released figure (T3-4; AP-1 D2) -------------

UNREADABLE = {'choices': []}


@pytest.mark.finding('T3-4')
@pytest.mark.req('R2.2')
def test_figures_surface_is_the_released_figure_not_every_number():
    # AP-1 D2: "the number of distinct numeric answers per question". The
    # same answer with different working is one answer.
    responses = [response('The available credit is 2600.00.'),
                 response('5000 - 2400 = 2600.00, so it is 2600.00.')]
    r = classify_mechanism(responses, surface='figures', minimum_runs=2,
                           figures=[D('2600.00'), D('2600.00')])
    assert (r['mechanism'], r['distinct_values'], r['successful_runs']) == (
        OBSERVED_ONLY, 1, 2)
    assert distinct_figures_shown(responses, [D('2600.00'),
                                              D('2600.0')]) == ['2600.00']


@pytest.mark.finding('T3-4')
@pytest.mark.req('R2.2')
def test_figures_surface_counts_different_released_figures():
    responses = [response('15.20'), response('182.40')]
    r = classify_mechanism(responses, surface='figures', minimum_runs=2,
                           figures=[D('15.20'), D('182.40')])
    assert r['distinct_values'] == 2
    assert distinct_figures_shown(responses, [D('15.20'), D('182.40')]) == [
        '15.20', '182.40']


@pytest.mark.finding('T3-4')
@pytest.mark.req('AP-1 D2', 'R2.2', 'R2.0')
def test_figures_surface_unresolved_answer_is_not_a_value():
    # An unresolved answer (None) is counted apart, never a value: one
    # beside 15.20 is neither a second value nor agreement with it.
    # (It was a value of its own, "no single figure", before.)
    responses = [response('15.20 or 182.40'), response('15.20')]
    r = classify_mechanism(responses, surface='figures', minimum_runs=2,
                           figures=[None, D('15.20')])
    assert (r['mechanism'], r['successful_runs'], r['distinct_values'],
            r['unresolved']) == (UNMEASURED, 2, None, 1)
    assert distinct_figures_shown(responses, [None, D('15.20')]) == [
        '15.20']


@pytest.mark.finding('T3-4', 'S3-G2-1')
@pytest.mark.req('R2.2', 'R2.0')
@pytest.mark.parametrize('surface', ['figures', 'prose'])
def test_unreadable_response_is_not_a_run(surface):
    # SPEC R2.0 step 0: nothing is concluded about a response that could
    # not be read. It is left out like an error, and counted.
    only = classify_mechanism([UNREADABLE, UNREADABLE], surface=surface,
                              minimum_runs=2, figures=[None, None])
    assert (only['mechanism'], only['successful_runs']) == (UNMEASURED, 0)
    assert '2 unreadable' in only['reason']
    mixed = classify_mechanism([UNREADABLE, response('2600.00')],
                               surface=surface, minimum_runs=1,
                               figures=[None, D('2600.00')])
    assert (mixed['distinct_values'], mixed['successful_runs']) == (1, 1)


@pytest.mark.finding('T3-4')
@pytest.mark.req('R0.4.1', 'R2.2')
def test_figures_identity_is_exact_whatever_the_context():
    # 15.20 and 15.21 are two answers at any Decimal precision, and so
    # are two values that differ beyond 28 digits.
    from decimal import localcontext
    long_a = D('1.' + '0' * 30 + '1')
    long_b = D('1.' + '0' * 30 + '2')
    with localcontext() as ctx:
        ctx.prec = 2
        r = classify_mechanism([response('a'), response('b')],
                               surface='figures', minimum_runs=2,
                               figures=[D('15.20'), D('15.21')])
        assert r['distinct_values'] == 2
        assert distinct_figures_shown(
            [response('a'), response('b')],
            [D('15.20'), D('15.21')]) == ['15.20', '15.21']
    r = classify_mechanism([response('a'), response('b')],
                           surface='figures', minimum_runs=2,
                           figures=[long_a, long_b])
    assert r['distinct_values'] == 2
