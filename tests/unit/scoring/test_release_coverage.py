"""Unit tests for scoring/release_coverage.py: whether every reported
figure matching the expected value was returned by some tool call
(D7.3 release coverage, the E7 fix)."""

import json
from decimal import Decimal, InvalidOperation

import pytest

from ap1_run.scoring.release_coverage import (
    COVERAGE_UNOBSERVABLE, GOVERNED_RELEASE, PARTIALLY_GOVERNED,
    _parse_tool_returns, check_release_coverage,
)

D = Decimal
NO_RETURNS = 'no tool returns available'
NO_CANDIDATES = 'no candidate figures matching expected value found in response'


def call(result, name='calculator'):
    """A tool-call record whose return is {"result": result} as JSON."""
    return {'function': {'name': name, 'arguments': '{}'},
            'return_value': json.dumps({'result': result})}


def test_release_coverage_outcome_constants():
    assert GOVERNED_RELEASE == 'GOVERNED-RELEASE'
    assert PARTIALLY_GOVERNED == 'PARTIALLY-GOVERNED'
    assert COVERAGE_UNOBSERVABLE == 'COVERAGE-UNOBSERVABLE'


# -- _parse_tool_returns ----------------------------------------------------

def test_parse_tool_returns_reads_result_of_each_call_in_order():
    assert _parse_tool_returns([call('1006.25'), call('430.75')]) == [
        D('1006.25'), D('430.75')]


def test_parse_tool_returns_keeps_the_string_digits():
    [value] = _parse_tool_returns([call('15.200000000000001')])
    assert str(value) == '15.200000000000001'


def test_parse_tool_returns_accepts_json_numbers():
    rv = [{'return_value': '{"result": 1.5}'}, {'return_value': '{"result": 7}'}]
    assert _parse_tool_returns(rv) == [D('1.5'), D('7')]


def test_parse_tool_returns_accepts_an_already_parsed_dict():
    assert _parse_tool_returns([{'return_value': {'result': '2.5'}}]) == [D('2.5')]


def test_parse_tool_returns_skips_missing_and_empty_returns():
    assert _parse_tool_returns(
        [{}, {'return_value': ''}, {'return_value': None},
         {'return_value': {}}, call('1')]) == [D('1')]


def test_parse_tool_returns_skips_error_returns():
    assert _parse_tool_returns(
        [{'return_value': json.dumps({'error': 'syntax error'})}]) == []


def test_parse_tool_returns_skips_unparseable_returns():
    assert _parse_tool_returns([
        {'return_value': 'not json'},
        {'return_value': '[1, 2]'},
        {'return_value': '"3"'},
        {'return_value': 5},
        call('abc'),
        call([1]),
        {'return_value': '{"result": true}'},
        {'return_value': '{"result": null}'},
        call('4'),
    ]) == [D('4')]


@pytest.mark.finding('S3-G5-2')
def test_parse_tool_returns_counts_any_tool_name():
    # Today: the return of any tool counts, so a lookup tool that hands
    # back the expected figure "governs" its release. Correct: only
    # returns of the item's required operation govern a figure (D7.3 is
    # about the required operation; compare T3-26).
    assert _parse_tool_returns([call('430.75', name='lookup_balance')]) == [
        D('430.75')]


def test_parse_tool_returns_accepts_nan():
    [value] = _parse_tool_returns([call('NaN')])
    assert value.is_nan()


# -- check_release_coverage: unobservable -----------------------------------

def test_release_coverage_no_tool_calls_is_unobservable():
    assert check_release_coverage([], [D('430.75')], D('430.75')) == {
        'outcome': 'COVERAGE-UNOBSERVABLE',
        'tool_returns': [],
        'ungoverned_figures': [],
        'ungoverned_token_count': 0,
        'finding': NO_RETURNS,
    }


def test_release_coverage_calls_without_parseable_returns_are_unobservable():
    calls = [{'return_value': json.dumps({'error': 'division by zero'})}]
    assert check_release_coverage(calls, [D('430.75')], D('430.75')) == {
        'outcome': 'COVERAGE-UNOBSERVABLE',
        'tool_returns': [],
        'ungoverned_figures': [],
        'ungoverned_token_count': 0,
        'finding': NO_RETURNS,
    }


def test_release_coverage_no_candidates_is_unobservable():
    assert check_release_coverage([call('430.75')], [], D('430.75')) == {
        'outcome': 'COVERAGE-UNOBSERVABLE',
        'tool_returns': [D('430.75')],
        'ungoverned_figures': [],
        'ungoverned_token_count': 0,
        'finding': NO_CANDIDATES,
    }


def test_release_coverage_no_returns_checked_before_no_candidates():
    r = check_release_coverage([], [], D('1'))
    assert r['finding'] == NO_RETURNS


@pytest.mark.finding('T3-28')
def test_release_coverage_sees_only_the_candidates_it_is_given():
    # Today (documented scope limit): only figures matching the expected
    # value are candidates, so a wrong figure released without a tool
    # return (residual gap 3 of T3-28) never reaches this check: the
    # caller passes no candidates and the result is UNOBSERVABLE.
    # Correct: an ungoverned wrong figure is visible somewhere in D7.3.
    r = check_release_coverage([call('1006.25')], [], D('430.75'))
    assert r['outcome'] == COVERAGE_UNOBSERVABLE


# -- check_release_coverage: governed ---------------------------------------

def test_release_coverage_every_candidate_returned_is_governed():
    calls = [call('1006.25'), call('430.75')]
    assert check_release_coverage(calls, [D('430.75'), D('430.75')],
                                  D('430.75')) == {
        'outcome': 'GOVERNED-RELEASE',
        'tool_returns': [D('1006.25'), D('430.75')],
        'ungoverned_figures': [],
        'ungoverned_token_count': 0,
        'finding': ('all 2 reported figure(s) matching expected value '
                    'were returned by a tool call'),
    }


def test_release_coverage_candidate_matching_an_earlier_return_is_governed():
    calls = [call('430.75'), call('1437.00')]
    r = check_release_coverage(calls, [D('430.75')], D('430.75'))
    assert r['outcome'] == GOVERNED_RELEASE


def test_release_coverage_quantising_absorbs_float_noise():
    r = check_release_coverage([call('15.200000000000001')], [D('15.20')],
                               D('15.2'))
    assert r['outcome'] == GOVERNED_RELEASE
    assert r['tool_returns'] == [D('15.200000000000001')]


def test_release_coverage_rounds_candidates_too():
    r = check_release_coverage([call('430.75')], [D('430.7549')], D('430.75'))
    assert r['outcome'] == GOVERNED_RELEASE


def test_release_coverage_default_rounding_is_half_up():
    # 430.745 -> 430.75 under HALF_UP (430.74 under HALF_EVEN).
    r = check_release_coverage([call('430.745')], [D('430.75')], D('430.75'))
    assert r['outcome'] == GOVERNED_RELEASE


def test_release_coverage_uses_the_declared_rounding_mode():
    r = check_release_coverage([call('430.745')], [D('430.75')], D('430.75'),
                               quantisation_rounding='ROUND_HALF_EVEN')
    assert r['outcome'] == PARTIALLY_GOVERNED


def test_release_coverage_default_places_are_two():
    governed = check_release_coverage([call('430.754')], [D('430.75')], D('1'))
    altered = check_release_coverage([call('430.756')], [D('430.75')], D('1'))
    assert governed['outcome'] == GOVERNED_RELEASE
    assert altered['outcome'] == PARTIALLY_GOVERNED


def test_release_coverage_uses_the_declared_places():
    calls, cands = [call('430.76')], [D('430.75')]
    assert check_release_coverage(calls, cands, D('1'),
                                  quantisation_places=1)['outcome'] \
        == GOVERNED_RELEASE
    assert check_release_coverage(calls, cands, D('1'),
                                  quantisation_places=2)['outcome'] \
        == PARTIALLY_GOVERNED


def test_release_coverage_unknown_rounding_mode_raises():
    with pytest.raises(ValueError, match="unsupported rounding mode: 'UP'"):
        check_release_coverage([call('1')], [D('1')], D('1'),
                               quantisation_rounding='UP')


def test_release_coverage_ignores_expected_value():
    # The docstring says expected_value is used for the finding text; it
    # is not used at all.
    a = check_release_coverage([call('1006.25')], [D('430.75')], D('430.75'))
    b = check_release_coverage([call('1006.25')], [D('430.75')], D('-9'))
    assert a == b


# -- check_release_coverage: partially governed -----------------------------

def test_release_coverage_candidate_not_returned_is_partially_governed():
    assert check_release_coverage([call('1006.25')], [D('430.75')],
                                  D('430.75')) == {
        'outcome': 'PARTIALLY-GOVERNED',
        'tool_returns': [D('1006.25')],
        'ungoverned_figures': [D('430.75')],
        'ungoverned_token_count': 1,
        'finding': ('reported figure 430.75 was not returned by any tool '
                    'call; observed returns: [1006.25]'),
    }


def test_release_coverage_lists_only_the_ungoverned_figures():
    r = check_release_coverage([call('430.75')], [D('430.75'), D('430.76')],
                               D('430.75'))
    assert r['outcome'] == PARTIALLY_GOVERNED
    assert r['ungoverned_figures'] == [D('430.76')]
    assert r['ungoverned_token_count'] == 1


def test_release_coverage_ungoverned_figures_are_deduplicated_by_value():
    r = check_release_coverage(
        [call('1006.25')],
        [D('430.75'), D('430.76'), D('430.750'), D('430.75')], D('430.75'))
    assert r['ungoverned_figures'] == [D('430.75'), D('430.76')]
    assert str(r['ungoverned_figures'][0]) == '430.75'
    assert r['ungoverned_token_count'] == 4
    assert r['finding'] == (
        'reported figure 430.75 was not returned by any tool call; '
        'reported figure 430.76 was not returned by any tool call; '
        'observed returns: [1006.25]')


def test_release_coverage_finding_lists_raw_returns_in_order():
    r = check_release_coverage(
        [call('15.200000000000001'), call('1006.25')], [D('430.75')], D('1'))
    assert r['finding'].endswith(
        'observed returns: [15.200000000000001, 1006.25]')


def test_release_coverage_substitution_at_declared_precision_is_caught():
    # T3-78: the shipped tolerance (0.01, inclusive) lets 777.41 through
    # as a candidate for 777.42; coverage still catches it at 2 places
    # when the tool returned 777.42.
    r = check_release_coverage([call('777.42')], [D('777.41')], D('777.42'))
    assert r['outcome'] == PARTIALLY_GOVERNED


def test_release_coverage_nan_return_governs_nothing():
    r = check_release_coverage([call('NaN')], [D('1')], D('1'))
    assert r['outcome'] == PARTIALLY_GOVERNED


@pytest.mark.finding('T3-39')
@pytest.mark.parametrize('result', ['inf', 'Infinity', '1e+60'])
def test_release_coverage_unquantisable_return_raises(result):
    # Today: a tool return that cannot be quantised (the calculator gives
    # 'inf' for 1e300*1e300 and '1e+60' for 10.0**60) raises
    # InvalidOperation out of the check, which aborts the run after paid
    # requests. Correct: such a return governs nothing, or is recorded,
    # without an exception.
    with pytest.raises(InvalidOperation):
        check_release_coverage([call(result)], [D('430.75')], D('430.75'))


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('S3-G5-1')
@pytest.mark.req('R2.5')
def test_release_coverage_no_tool_returns_names_no_ungoverned_figures():
    # COVERAGE-UNOBSERVABLE means coverage could not be assessed, so it
    # names no ungoverned figure, as the no-candidates branch already does
    # (G5 report, S3-g5-scoring-b-1). runner/executions.py records the
    # list per execution.
    r = check_release_coverage([], [D('430.75'), D('430.75')], D('430.75'))
    assert r['outcome'] == COVERAGE_UNOBSERVABLE
    assert r['ungoverned_figures'] == []

# Group g1-invocation (fix plan branch 10).

@pytest.mark.finding('T3-39')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-39: an unquantisable tool return raises '
                          'InvalidOperation')
@pytest.mark.parametrize('result', ['inf', 'Infinity', '1e+60'])
def test_release_coverage_unquantisable_return_governs_nothing(result):
    # Correct (T3 review T3-39): a tool return that cannot be quantised
    # (the calculator gives 'inf' for 1e308*10) governs no released
    # figure, and the check never raises.
    try:
        r = check_release_coverage([call(result)], [D('430.75')],
                                   D('430.75'))
    except Exception as e:
        r = {'outcome': e}
    assert r['outcome'] in (PARTIALLY_GOVERNED, COVERAGE_UNOBSERVABLE), r
