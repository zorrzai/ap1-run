"""Unit tests for scoring/reproducibility.py: the D2 mechanism class per
surface and the parameter-echo check (R2.2)."""

import pytest

from ap1_run.scoring.reproducibility import (
    CONFIGURED, OBSERVED_ONLY, STRUCTURAL, UNMEASURED, VALID_CLASSES,
    ReproducibilityError, _extract_surface_values, _is_error_or_limited,
    check_parameter_echo, classify_mechanism,
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
    # Today: both branches return OBSERVED-ONLY, so 5 identical and 5
    # different answers get the same class; only distinct_values differs.
    # Correct (AP-1 D2 method): the result reports the distinct answers
    # and their spread, and the class reflects them.
    responses = [response(f'${v}') for v in ('1', '2', '3', '4', '5')]
    assert classify_mechanism(responses, surface='prose', minimum_runs=3) == {
        'mechanism': 'OBSERVED-ONLY',
        'operator_declared': False,
        'distinct_values': 5,
        'successful_runs': 5,
        'reason': '5 runs, 5 distinct values — OBSERVED-ONLY',
    }


@pytest.mark.finding('T3-4')
def test_classify_mechanism_figures_surface_is_the_whole_content():
    # Today: without tool calls the "figures" surface is the whole
    # message text, so two wordings of the same figure count as two
    # distinct figures. Correct: the figures surface is the released
    # figure (two values here: one).
    responses = [response('The answer is $15.20.'), response('$15.20 a year.'),
                 response('The answer is $15.20.')]
    r = classify_mechanism(responses, surface='figures', minimum_runs=3)
    assert r['distinct_values'] == 2


def test_classify_mechanism_errored_runs_are_left_out_of_the_values():
    responses = [response('a'), {'error': 'boom'}, response('a'), response('a')]
    r = classify_mechanism(responses, surface='prose', minimum_runs=3)
    assert r['successful_runs'] == 3
    assert r['distinct_values'] == 1


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


def test_surface_values_figures_without_tool_calls_is_the_content():
    assert _extract_surface_values(
        [response('$15.20'), response('$1', []), response('$2', None),
         response(None), {'choices': []}, {}, {'choices': [{}]}],
        'figures') == ['$15.20', '$1', '$2', '', '', '', '']


@pytest.mark.finding('T3-4')
def test_surface_values_figures_with_tool_calls_is_first_call_arguments():
    # Today: when the response carries tool calls, the "figure" is the
    # first call's arguments string, not a figure. Correct: the figure
    # surface is the released figure.
    calls = [tool_call('{"expression": "15200 * 0.012"}'),
             tool_call('{"expression": "2"}')]
    assert _extract_surface_values([response('$182.40', calls)],
                                   'figures') == ['{"expression": "15200 * 0.012"}']


def test_surface_values_figures_tool_call_without_arguments_is_empty():
    assert _extract_surface_values(
        [response('x', [{'function': {}}]), response('x', [{}])],
        'figures') == ['', '']


def test_surface_values_figures_arguments_are_stringified():
    assert _extract_surface_values(
        [response('x', [{'function': {'arguments': {'expression': '1'}}}])],
        'figures') == ["{'expression': '1'}"]


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
        'verified': False, 'findings': [], 'status': 'UNVERIFIED'}


def test_parameter_echo_all_applied_is_verified():
    assert check_parameter_echo(
        {'temperature': '0.0', 'top_p': 1},
        {'temperature': '0.0', 'top_p': '1', 'seed': 7}) == {
        'verified': True, 'findings': [], 'status': 'VERIFIED'}


def test_parameter_echo_nothing_requested_is_verified():
    assert check_parameter_echo({}, {})['status'] == 'VERIFIED'


@pytest.mark.req('R2.2')
def test_parameter_echo_changed_and_missing_parameters_are_findings():
    assert check_parameter_echo(
        {'temperature': '0.0', 'top_p': '1.0'}, {'temperature': '0.7'}) == {
        'verified': False,
        'findings': [
            "parameter 'temperature': requested='0.0', applied='0.7' "
            '— silently ignored',
            "parameter 'top_p' requested but not echoed",
        ],
        'status': 'MISMATCH',
    }


def test_parameter_echo_echoed_none_counts_as_not_echoed():
    r = check_parameter_echo({'seed': 7}, {'seed': None})
    assert r['findings'] == ["parameter 'seed' requested but not echoed"]


def test_parameter_echo_compares_as_strings():
    assert check_parameter_echo({'t': 0.0}, {'t': '0.0'})['status'] == 'VERIFIED'


@pytest.mark.finding('S3-G5-4')
def test_parameter_echo_numerically_equal_values_can_mismatch():
    # Today: values are compared as strings, so temperature 0 requested
    # and 0.0 echoed is reported as "silently ignored". Correct: compare
    # numbers as numbers. (No live caller today; see T3-90.)
    r = check_parameter_echo({'temperature': 0}, {'temperature': 0.0})
    assert r['status'] == 'MISMATCH'
    assert r['findings'] == [
        "parameter 'temperature': requested=0, applied=0.0 — silently ignored"]


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g7-report (fix branch 7). xfail(strict=True) until the fix.

def _answer(text):
    return {'choices': [{'message': {'role': 'assistant', 'content': text}}]}


@pytest.mark.finding('T3-4')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-4: the "figures" surface is the whole prose, '
                          'so one figure in two wordings is two values')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G5-4: echo compared as strings; 0 requested, '
                          '0.0 applied is reported silently ignored')
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


# Step 5 (run-robustness): a response whose shape cannot be read has no
# surface value, as one without choices; never an exception (S3-G2-1).

@pytest.mark.finding('S3-G2-1')
@pytest.mark.parametrize('surface', ['figures', 'prose'])
def test_surface_values_unreadable_shape_is_empty(surface):
    assert _extract_surface_values(
        ['text', {'choices': ['x']}, {'choices': [{'message': None}]},
         {'choices': {'a': 1}},
         {'choices': [{'message': {'content': ['x']}}]},
         {'choices': [{'message': {'tool_calls': ['x']}}]}],
        surface) == [''] * 6
