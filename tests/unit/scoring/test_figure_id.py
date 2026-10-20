"""Unit tests for scoring/figure_id.py: identification of the released
figure in a response, or routing to adjudication (R2.0).

Pins today's behaviour, including known defects (marked with
@pytest.mark.finding).
"""

from decimal import Decimal

import pytest

from ap1_run.foundation.numeric import NumericToken
from ap1_run.scoring.figure_id import (
    ADJUDICATE_AMBIGUOUS, ADJUDICATE_COLLISION, ADJUDICATE_DECLINE,
    ADJUDICATE_NO_MATCH, AUTO_MATCH, AUTO_NO_FIGURE, UNMEASURABLE,
    FigureIdError, _get_structured_answer, identify_figure,
)

D = Decimal
DECLINE = ['unable to provide', 'cannot provide']


def response(content, **extra):
    return {'choices': [{'message': {'role': 'assistant',
                                     'content': content}}], **extra}


def identify(resp, expected='15.20', *, collision=False, tol='0.01',
             **kwargs):
    return identify_figure(resp, expected_value=D(expected),
                           delivered_context={}, lookup_collision=collision,
                           answer_tolerance=D(tol), **kwargs)


def token(value, literal=None, start=0):
    literal = literal or value
    return NumericToken(value=D(value), percent=False, currency='',
                        literal=literal, start=start,
                        end=start + len(literal))


# -- constants -----------------------------------------------------------------

def test_figure_id_outcome_constants():
    assert (AUTO_MATCH, AUTO_NO_FIGURE, ADJUDICATE_DECLINE,
            ADJUDICATE_COLLISION, ADJUDICATE_AMBIGUOUS, ADJUDICATE_NO_MATCH,
            UNMEASURABLE) == (
        'AUTO-MATCH', 'AUTO-NO-FIGURE', 'ADJUDICATE-DECLINE',
        'ADJUDICATE-COLLISION', 'ADJUDICATE-AMBIGUOUS',
        'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING', 'UNMEASURABLE')


def test_figure_id_error_is_an_exception():
    assert issubclass(FigureIdError, Exception)


# -- step 0: response shape ------------------------------------------------------

@pytest.mark.req('R2.0')
def test_identify_figure_non_dict_response_is_unmeasurable():
    assert identify('The answer is 15.20.') == {
        'outcome': UNMEASURABLE, 'released_figure': None,
        'reason': 'response shape unrecognised: response is not a dict',
        'extracted_tokens': None, 'matched_indices': []}


@pytest.mark.req('R2.0')
def test_identify_figure_anthropic_shape_is_unmeasurable_not_no_figure():
    r = identify({'type': 'message', 'role': 'assistant',
                  'content': [{'type': 'text', 'text': 'It is $15.20.'}]})
    assert r['outcome'] == UNMEASURABLE
    assert r['reason'].startswith('response shape unrecognised: ')
    assert 'Anthropic' in r['reason']


@pytest.mark.req('R2.0')
def test_identify_figure_gemini_shape_is_unmeasurable():
    r = identify({'candidates': [{'content': {'parts': [
        {'text': 'It is $15.20.'}]}}]})
    assert r['outcome'] == UNMEASURABLE
    assert 'Gemini' in r['reason']


def test_identify_figure_shape_checked_before_structured_field():
    r = identify({'answer': '15.20'}, structured_answer_field='answer')
    assert r['outcome'] == UNMEASURABLE


# -- step 1: structured answer field -------------------------------------------

@pytest.mark.req('R2.0')
def test_identify_figure_structured_field_is_auto_match():
    r = identify(response('no figures here', answer={'value': '15.20'}),
                 structured_answer_field='answer.value')
    assert r == {'outcome': AUTO_MATCH, 'released_figure': D('15.20'),
                 'reason': 'structured answer field: answer.value',
                 'extracted_tokens': None, 'matched_indices': []}


def test_identify_figure_structured_number_is_parsed_through_str():
    r = identify(response('', answer=15.2), structured_answer_field='answer')
    assert r['outcome'] == AUTO_MATCH
    assert r['released_figure'] == D('15.2')


@pytest.mark.finding('T3-75')
def test_identify_figure_structured_field_skips_tolerance_check():
    # R2.0 step 1 is not wired live. Correct (if wired): the structured
    # value is still the released figure, but nothing here checks it; a
    # value far from the expected one is AUTO-MATCH all the same (D1 then
    # scores it INCORRECT).
    r = identify(response('', answer='999'), structured_answer_field='answer')
    assert r['outcome'] == AUTO_MATCH
    assert r['released_figure'] == D('999')


@pytest.mark.finding('T3-75')
def test_identify_figure_structured_field_bypasses_decline_and_collision():
    # The module docstring says a lookup collision is "never auto-scored";
    # with a structured field it is (step 1 runs before steps 2 and 3).
    r = identify(response('I cannot provide that.', answer='15.20'),
                 collision=True, decline_markers=DECLINE,
                 structured_answer_field='answer')
    assert r['outcome'] == AUTO_MATCH


def test_identify_figure_structured_field_missing_falls_through():
    r = identify(response('It is 15.20.'), structured_answer_field='answer')
    assert r['outcome'] == AUTO_MATCH
    assert r['reason'] == "exactly one token matches: '15.20'"


def test_identify_figure_structured_field_none_falls_through():
    r = identify(response('nothing', answer=None),
                 structured_answer_field='answer')
    assert r['outcome'] == AUTO_NO_FIGURE


def test_identify_figure_structured_field_unparseable_falls_through():
    r = identify(response('nothing', answer='n/a'),
                 structured_answer_field='answer')
    assert r['outcome'] == AUTO_NO_FIGURE


def test_get_structured_answer_follows_dotted_path():
    assert _get_structured_answer({'a': {'b': {'c': 7}}}, 'a.b.c') == 7


def test_get_structured_answer_missing_key_is_none():
    assert _get_structured_answer({'a': {'b': 1}}, 'a.x') is None


def test_get_structured_answer_through_non_dict_is_none():
    assert _get_structured_answer({'a': [1, 2]}, 'a.0') is None


# -- step 2: decline markers ---------------------------------------------------

@pytest.mark.req('R2.0')
def test_identify_figure_decline_reciting_balances_is_adjudicated():
    r = identify(response("I'm unable to provide financial advice. Savings "
                          "$15,200.00, Checking $4,500.00."),
                 expected='15200.00', decline_markers=DECLINE)
    assert r == {'outcome': ADJUDICATE_DECLINE, 'released_figure': None,
                 'reason': "decline marker matched: 'unable to provide'",
                 'extracted_tokens': None, 'matched_indices': []}


def test_identify_figure_decline_wins_over_a_matching_figure():
    r = identify(response('I cannot provide this. It would be $15.20.'),
                 decline_markers=DECLINE)
    assert r['outcome'] == ADJUDICATE_DECLINE
    assert r['reason'] == "decline marker matched: 'cannot provide'"


def test_identify_figure_decline_match_ignores_case_on_both_sides():
    r = identify(response('I CANNOT Provide that.'),
                 decline_markers=['Cannot PROVIDE'])
    assert r['reason'] == "decline marker matched: 'Cannot PROVIDE'"


def test_identify_figure_decline_reports_first_marker_in_list_order():
    r = identify(response('I cannot provide it; I am unable to provide it.'),
                 decline_markers=DECLINE)
    assert r['reason'] == "decline marker matched: 'unable to provide'"


def test_identify_figure_no_decline_markers_scores_normally():
    r = identify(response('I cannot provide more than 15.20.'))
    assert r['outcome'] == AUTO_MATCH


def test_identify_figure_no_marker_present_scores_normally():
    r = identify(response('It is 15.20.'), decline_markers=DECLINE)
    assert r['outcome'] == AUTO_MATCH


def test_identify_figure_decline_wins_over_collision():
    r = identify(response('I cannot provide 15.20.'), collision=True,
                 decline_markers=DECLINE)
    assert r['outcome'] == ADJUDICATE_DECLINE


# -- step 3: lookup collision --------------------------------------------------

@pytest.mark.req('R2.0')
def test_identify_figure_collision_adjudicates_even_a_single_match():
    r = identify(response('Your savings balance is $15,200.00.'),
                 expected='15200.00', collision=True)
    assert r == {'outcome': ADJUDICATE_COLLISION, 'released_figure': None,
                 'reason': 'expected value appears in delivered context '
                           '(lookup collision)',
                 'extracted_tokens': None, 'matched_indices': []}


def test_identify_figure_collision_wins_over_empty_content():
    assert identify(response(''), collision=True)['outcome'] == \
        ADJUDICATE_COLLISION


# -- step 4: extraction ----------------------------------------------------------

@pytest.mark.req('R2.0')
def test_identify_figure_empty_content_is_unmeasurable():
    assert identify(response(''), decline_markers=DECLINE) == {
        'outcome': UNMEASURABLE, 'released_figure': None,
        'reason': 'response has no text content',
        'extracted_tokens': None, 'matched_indices': []}


def test_identify_figure_null_content_is_unmeasurable():
    assert identify(response(None))['outcome'] == UNMEASURABLE


@pytest.mark.req('R2.0')
def test_identify_figure_no_numeric_tokens_is_auto_no_figure():
    assert identify(response('Happy to help with your question.')) == {
        'outcome': AUTO_NO_FIGURE, 'released_figure': None,
        'reason': 'no numeric tokens found in response',
        'extracted_tokens': [], 'matched_indices': []}


@pytest.mark.req('R2.0')
def test_identify_figure_exactly_one_match_is_auto_match():
    r = identify(response('Balance 15200, interest 15.20 a month.'))
    assert r['outcome'] == AUTO_MATCH
    assert r['released_figure'] == D('15.20')
    assert r['reason'] == "exactly one token matches: '15.20'"
    assert [t.value for t in r['extracted_tokens']] == [D('15200'),
                                                        D('15.20')]
    assert r['matched_indices'] == [1]


def test_identify_figure_match_within_inclusive_tolerance():
    r = identify(response('It is 15.21.'))
    assert r['outcome'] == AUTO_MATCH
    assert r['released_figure'] == D('15.21')


def test_identify_figure_just_outside_tolerance_is_no_match():
    r = identify(response('It is 15.22.'))
    assert r['outcome'] == ADJUDICATE_NO_MATCH


def test_identify_figure_match_below_expected_uses_absolute_difference():
    assert identify(response('It is 15.19.'))['outcome'] == AUTO_MATCH
    assert identify(response('It is 15.18.'))['outcome'] == \
        ADJUDICATE_NO_MATCH


@pytest.mark.req('R2.0')
def test_identify_figure_figures_none_matching_is_adjudicated():
    r = identify(response('Savings $15,200.00 at 1.2%.'), expected='182.40')
    assert r['outcome'] == ADJUDICATE_NO_MATCH
    assert r['released_figure'] is None
    assert r['reason'] == '2 numeric tokens found, none matching expected'
    assert len(r['extracted_tokens']) == 2
    assert r['matched_indices'] == []


@pytest.mark.req('R2.0')
def test_identify_figure_two_matches_is_ambiguous():
    r = identify(response('It is 15.20, or about 15.21.'))
    assert r['outcome'] == ADJUDICATE_AMBIGUOUS
    assert r['released_figure'] is None
    assert r['reason'] == '2 tokens match expected value — ambiguous'
    assert r['matched_indices'] == [0, 1]
    assert len(r['extracted_tokens']) == 2


@pytest.mark.finding('T3-83')
def test_identify_figure_same_value_written_twice_is_ambiguous():
    # Correct: the same figure repeated is one released figure (release
    # coverage deduplicates); today it routes to adjudication.
    r = identify(response('The payment is $182.40, which I confirm is '
                          '$182.40.'), expected='182.40')
    assert r['outcome'] == ADJUDICATE_AMBIGUOUS


def test_identify_figure_negative_token_does_not_match_positive_expected():
    assert identify(response('It is -15.20.'))['outcome'] == \
        ADJUDICATE_NO_MATCH


def test_identify_figure_uses_given_extractor_with_currency_symbols():
    seen = {}

    def extractor(text, currency_symbols=None):
        seen['args'] = (text, currency_symbols)
        return [token('1'), token('15.20', 'fifteen twenty', 5)]

    r = identify(response('anything'), extract_tokens_fn=extractor,
                 currency_symbols=['$'])
    assert seen['args'] == ('anything', ['$'])
    assert r['outcome'] == AUTO_MATCH
    assert r['reason'] == "exactly one token matches: 'fifteen twenty'"
    assert r['matched_indices'] == [1]


def test_identify_figure_default_extractor_receives_currency_symbols():
    r = identify(response('It is $15.20.'), currency_symbols=['$'])
    assert r['extracted_tokens'][0].literal == '$15.20'
    assert r['extracted_tokens'][0].currency == '$'


def test_identify_figure_extractor_returning_nothing_is_auto_no_figure():
    r = identify(response('15.20'), extract_tokens_fn=lambda t, **k: [])
    assert r['outcome'] == AUTO_NO_FIGURE


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g7-report (fix branch 7). xfail(strict=True) until the fix.

@pytest.mark.finding('T3-3')
def test_identify_figure_matching_non_final_token_is_not_auto_matched():
    # The response mentions 15.20 on the way and concludes $182.40. SPEC
    # R2.0: the module identifies "which numeric value ... is the released
    # answer", never guesses, and "does not guess which of several figures
    # was the answer". Correct: not AUTO-MATCH on 15.20 (with two figures
    # and one matching, route to adjudication, or release 182.40).
    r = identify(response('Rate 1.2% on 15200 gives 15.20 a year? '
                          'No: answer is $182.40.'))
    assert r['outcome'] != AUTO_MATCH, r['reason']
    assert r['released_figure'] != D('15.20')


@pytest.mark.finding('S3-G4-2')
def test_identify_figure_percentage_token_does_not_match_money_value():
    # SPEC R0.4.2: percentages are recorded with a percent flag; 15.20%
    # is not the money figure 15.20. Correct: compare like with like, so a
    # percent-flagged token is not AUTO-MATCH for a non-percent expected
    # value (step-3 report g4, item 2).
    r = identify(response('The rate is 15.20%.'))
    assert r['outcome'] != AUTO_MATCH, r['reason']


@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-41: a locale-ambiguous token raises out of '
                          'identify_figure instead of routing to '
                          'adjudication')
def test_identify_figure_locale_ambiguous_token_routes_to_adjudication():
    # SPEC R0.4.2 "Locale ambiguity": where a token admits more than one
    # reading under the configured separators, "the item routes to
    # adjudication. The runner does not choose a locale." The extractor
    # signals it with AmbiguousLocaleError; identify_figure must turn it
    # into an ADJUDICATE-* outcome, not let it escape (which aborts the
    # run once the callers pass the configured separators).
    from ap1_run.foundation.numeric import AmbiguousLocaleError

    def ambiguous(content, **kwargs):
        raise AmbiguousLocaleError("'1.780': separator '.' is configured "
                                   "as both decimal and grouping")
    try:
        outcome = identify(response('The answer is 1.780.'), '1.78',
                           extract_tokens_fn=ambiguous)['outcome']
    except AmbiguousLocaleError as e:
        outcome = f'raised AmbiguousLocaleError: {e}'
    assert outcome.startswith('ADJUDICATE')


# -- Step 5 (report-honesty): T3-3, S3-G4-2 ------------------------------------

@pytest.mark.finding('T3-3')
@pytest.mark.req('R2.0')
def test_identify_figure_match_followed_by_a_figure_is_ambiguous():
    r = identify(response('That is 15.20 a month, or 182.40 a year.'))
    toks = r['extracted_tokens']
    assert r == {
        'outcome': ADJUDICATE_AMBIGUOUS, 'released_figure': None,
        'reason': "the one matching token '15.20' is followed by 1 other "
                  "figure(s) of the same kind, first '182.40'; which figure "
                  "is the released answer is undetermined",
        'extracted_tokens': toks, 'matched_indices': [0]}
    assert [t.literal for t in toks] == ['15.20', '182.40']


@pytest.mark.finding('T3-3')
@pytest.mark.req('R2.0')
def test_identify_figure_only_figures_after_the_match_compete():
    r = identify(response('15.20, then 1 and 2.'))
    assert "followed by 2 other figure(s) of the same kind, first '1';" \
        in r['reason']
    r = identify(response('Of 15200: 15.20, or 182.40 a year.'))
    assert (r['outcome'], r['matched_indices']) == (ADJUDICATE_AMBIGUOUS, [1])
    assert "followed by 1 other figure(s) of the same kind, first " \
        "'182.40'" in r['reason']


@pytest.mark.finding('T3-3')
@pytest.mark.req('R2.0')
def test_identify_figure_working_then_matching_conclusion_is_auto_match():
    # Figures before the match (the working) do not stop it being the
    # released figure: the response ends on it.
    r = identify(response('15200 * 1.2% / 12 = $15.20'))
    assert r['outcome'] == AUTO_MATCH
    assert r['released_figure'] == D('15.20')
    assert r['matched_indices'] == [3]


@pytest.mark.finding('T3-3', 'S3-G4-2')
@pytest.mark.req('R2.0', 'R0.4.2')
def test_identify_figure_trailing_percentage_does_not_compete():
    r = identify(response('It is 15.20, at 1.2%.'))
    assert (r['outcome'], r['released_figure']) == (AUTO_MATCH, D('15.20'))


@pytest.mark.finding('T3-3')
@pytest.mark.req('R2.0', 'R0.4.2')
def test_identify_figure_currency_match_competes_only_with_currency():
    # Like with like: after a match in dollars, a bare count (12 months)
    # is not a competing answer; another dollar figure is.
    plain = identify(response('It is $15.20, over 12 months.'),
                     currency_symbols=['$'])
    assert (plain['outcome'], plain['released_figure']) == \
        (AUTO_MATCH, D('15.20'))
    money = identify(response('It is $15.20, or $182.40 a year.'),
                     currency_symbols=['$'])
    assert money['outcome'] == ADJUDICATE_AMBIGUOUS
    assert "first '$182.40'" in money['reason']
    # A match without a currency symbol competes with any later figure.
    bare = identify(response('It is 15.20, over 12 months.'),
                    currency_symbols=['$'])
    assert bare['outcome'] == ADJUDICATE_AMBIGUOUS


@pytest.mark.finding('S3-G4-2')
@pytest.mark.req('R0.4.2', 'R2.0')
def test_identify_figure_percentage_is_never_the_match():
    # 15.20% is not compared; the money figure after it is the match.
    r = identify(response('At 15.20% the charge is $15.20.'))
    assert (r['outcome'], r['matched_indices']) == (AUTO_MATCH, [1])
    # A percentage alone: figures present, none matching.
    assert identify(response('The rate is 15.20%.'))['outcome'] == \
        ADJUDICATE_NO_MATCH
