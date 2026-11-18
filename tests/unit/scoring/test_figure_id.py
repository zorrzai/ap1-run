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


@pytest.mark.finding('S3-G1-7')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.parametrize('content', [
    'The answer is \u0661\u0665.\u0662\u0660.',       # Arabic-Indic 15.20
    'The answer is \u06f1\u06f5.\u06f2\u06f0.',       # Extended (Persian)
    'The answer is \u0967\u096b.\u0968\u0966.',       # Devanagari
    'The answer is \uff11\uff15.\uff12\uff10.',       # full-width
], ids=['arabic-indic', 'extended-arabic-indic', 'devanagari', 'full-width'])
def test_identify_figure_non_ascii_digits_route_to_adjudication(content):
    # The review of #13: R0.4.2's digits are ASCII 0-9 only, so such
    # a reply holds no numeric token; but it states a figure, so it must
    # go to a person, not score AUTO-NO-FIGURE (wrong, with no look).
    r = identify(response(content))
    assert r['outcome'] == ADJUDICATE_NO_MATCH, r
    assert r['released_figure'] is None
    assert r['extracted_tokens'] == []
    assert 'ASCII' in r['reason']


@pytest.mark.finding('S3-G1-7')
@pytest.mark.req('R2.0')
@pytest.mark.parametrize('content', [
    'Happy to help, see \u00b2 and \u00bd.',        # superscript, fraction
    '\u5341\u4e94 dollars',                           # CJK numerals (No/Lo)
])
def test_identify_figure_non_digit_number_characters_stay_no_figure(content):
    # Only Unicode decimal digits (category Nd) route; superscripts,
    # vulgar fractions and CJK numerals are not digits of any script.
    assert identify(response(content))['outcome'] == AUTO_NO_FIGURE


@pytest.mark.finding('S3-G1-7')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-7: digits of another script are checked only '
                          'when no ASCII token was found')
@pytest.mark.parametrize('content, expected', [
    ('Step: 430.75 was wrong; final answer '
     '\u0664\u0662\u0660\u066b\u0660\u0660', '430.75'),
    ('Step: 430.75 was wrong; final answer \uff14\uff12\uff10.00',
     '430.75'),
    ('The answer is 15.20, or \u0967\u096b.\u0968\u0966', '15.20'),
], ids=['arabic-indic-final-answer', 'full-width-final-answer',
        'devanagari-beside-match'])
def test_identify_figure_non_ascii_digits_beside_a_match_route_to_adjudication(
        content, expected):
    # The review of #13: 'Step: 430.75 was wrong; final answer
    # \u0664\u0662\u0660\u066b\u0660\u0660' (420.00 in Arabic-Indic digits)
    # AUTO-MATCHed an expected 430.75 on the step it calls wrong, since the
    # other-script check ran only when extraction found no ASCII token. Any
    # Unicode decimal digit other than ASCII 0-9 anywhere in the reply now
    # sends an automatic outcome to a person.
    r = identify(response(content), expected=expected)
    assert r['outcome'] == ADJUDICATE_NO_MATCH, r
    assert r['released_figure'] is None
    assert 'ASCII' in r['reason']


@pytest.mark.finding('S3-G1-7')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.parametrize('content, expected, outcome', [
    ('15.20 or 15.20, or \u0661\u0665.\u0662\u0660', '15.20',
     ADJUDICATE_AMBIGUOUS),
    ('It is 9.99, or \u0661\u0665.\u0662\u0660', '15.20',
     ADJUDICATE_NO_MATCH),
], ids=['two-matches-stay-ambiguous', 'no-match-stays-none-matching'])
def test_identify_figure_non_ascii_digits_leave_adjudicated_outcomes_alone(
        content, expected, outcome):
    # An outcome that already goes to a person keeps its own reason.
    assert identify(response(content), expected=expected)['outcome'] \
        == outcome


@pytest.mark.finding('S3-G1-5')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G1-5: \'12 $-575.50\' reads 12 $ and +575.50')
@pytest.mark.parametrize('content, expected, outcome', [
    ('For month 12 $-575.50 was paid', '575.50', ADJUDICATE_NO_MATCH),
    ('For month 12 $-575.50 was paid', '-575.50', AUTO_MATCH),
], ids=['wrong-sign-not-matched', 'negative-matched'])
def test_identify_figure_currency_before_a_signed_figure_keeps_the_sign(
        content, expected, outcome):
    # The review of #13, with example/config.json's currency_symbols: at
    # 70d3744a the first AUTO-MATCHes (a wrong-sign answer scored correct)
    # and the second goes to adjudication.
    r = identify(response(content), expected=expected,
                 currency_symbols=['$', 'USD'])
    assert r['outcome'] == outcome, r


@pytest.mark.finding('S3-G1-5')
@pytest.mark.req('R0.4.2', 'R2.0')
@pytest.mark.parametrize('content, expected, outcome', [
    ('month 12 -575.50', '575.50', ADJUDICATE_NO_MATCH),
    ('month 12 -575.50', '-575.50', AUTO_MATCH),
    ('In 2024 -12.5% was the change', '12.5', ADJUDICATE_NO_MATCH),
    ('In 2024 -12.5% was the change', '-12.5', AUTO_MATCH),
], ids=['wrong-sign-not-matched', 'negative-matched',
        'year-wrong-sign-not-matched', 'year-negative-matched'])
def test_identify_figure_sign_after_label_number_is_kept(
        content, expected, outcome):
    # The review of #13: at 3803f542 the first and third
    # AUTO-MATCH (a wrong-sign answer scored correct) and the second and
    # fourth go to adjudication.
    r = identify(response(content), expected=expected)
    assert r['outcome'] == outcome, r


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


@pytest.mark.finding('T3-3')
def test_identify_figure_takes_matching_token_over_the_conclusion():
    # Correct: the released figure is what the response concludes
    # (182.40), not the one token that happens to equal the expected value.
    r = identify(response('Rate 1.2% on 15200 gives 15.20 a year? '
                          'No: answer is $182.40.'))
    assert r['outcome'] == AUTO_MATCH
    assert r['released_figure'] == D('15.20')


@pytest.mark.finding('S3-G4-2')
def test_identify_figure_percentage_token_matches_a_money_value():
    # The token's percent flag is ignored: '15.20%' matches an expected
    # $15.20. Correct: a percentage is not the released money figure
    # (route to adjudication, or compare like with like).
    r = identify(response('The rate is 15.20%.'))
    assert r['outcome'] == AUTO_MATCH
    assert r['extracted_tokens'][0].percent is True


def test_identify_figure_negative_token_does_not_match_positive_expected():
    assert identify(response('It is -15.20.'))['outcome'] == \
        ADJUDICATE_NO_MATCH


def test_identify_figure_uses_given_extractor_with_currency_symbols():
    # T3-41: the extractor also receives the separators (defaults '.'
    # and ',' when none are given).
    seen = {}

    def extractor(text, currency_symbols=None, decimal_sep=None,
                  grouping_sep=None):
        seen['args'] = (text, currency_symbols, decimal_sep, grouping_sep)
        return [token('1'), token('15.20', 'fifteen twenty', 5)]

    r = identify(response('anything'), extract_tokens_fn=extractor,
                 currency_symbols=['$'])
    assert seen['args'] == ('anything', ['$'], '.', ',')
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
# xfail(strict=True) until the fix.

@pytest.mark.proposal(
    'T3-3: R2.0 step 4 changed (one matching token that is not the final '
    'answer is not AUTO-MATCH); needs a SPEC change the maintainer has '
    'not decided')
@pytest.mark.finding('T3-3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-3: a matching non-final token is taken as the '
                          'released figure (AUTO-MATCH 15.20; the response '
                          'concludes 182.40)')
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
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G4-2: "15.20%" AUTO-MATCHes an expected money '
                          'value of 15.20')
def test_identify_figure_percentage_token_does_not_match_money_value():
    # SPEC R0.4.2: percentages are recorded with a percent flag; 15.20%
    # is not the money figure 15.20. Correct: compare like with like, so a
    # percent-flagged token is not AUTO-MATCH for a non-percent expected
    # value (step-3 report g4, item 2).
    r = identify(response('The rate is 15.20%.'))
    assert r['outcome'] != AUTO_MATCH, r['reason']


@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2', 'R2.0')
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


# --- The configured separators (T3-41) ---

@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2')
def test_identify_figure_default_extractor_uses_configured_separators():
    r = identify(response('Die Zinsen betragen 1.006,25 $.'), '1006.25',
                 decimal_separator=',', grouping_separator='.')
    assert (r['outcome'], r['released_figure']) == (AUTO_MATCH, D('1006.25'))


@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2')
def test_identify_figure_structured_answer_uses_configured_separators():
    r = identify(response('', answer='1.006,25'), '1006.25',
                 structured_answer_field='answer',
                 decimal_separator=',', grouping_separator='.')
    assert (r['outcome'], r['released_figure']) == (AUTO_MATCH, D('1006.25'))


@pytest.mark.finding('T3-41')
@pytest.mark.req('R0.4.2', 'R2.0')
def test_identify_figure_real_locale_ambiguity_routes_to_adjudication():
    r = identify(response('The answer is 1.780.'), '1.78',
                 decimal_separator='.', grouping_separator='.')
    assert r == {
        'outcome': ADJUDICATE_AMBIGUOUS, 'released_figure': None,
        'reason': "locale-ambiguous token under the configured separators: "
                  "'1.780': separator '.' is configured as both decimal "
                  "and grouping -- cannot disambiguate",
        'extracted_tokens': None, 'matched_indices': []}
