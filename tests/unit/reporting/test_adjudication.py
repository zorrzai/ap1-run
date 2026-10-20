"""Unit tests for the adjudication sheet generator (R3.2): which execution
records get sheets, and what each sheet says."""

import re

import pytest

from ap1_run.reporting import adjudication
from ap1_run.reporting.adjudication import (
    ADJUDICATION_REASONS, RUBRIC_TABLE, generate_sheets,
)


CONFIG = {'ap1_version': '1.3', 'ap1_version_doi': '10.5281/zenodo.1'}


def record(item_id='Q01', condition='base',
           figure_outcome='ADJUDICATE-DECLINE', **fields):
    rec = {'item_id': item_id, 'condition': condition,
           'figure_outcome': figure_outcome}
    rec.update(fields)
    return rec


def questions(*items):
    return {'items': list(items) or [
        {'id': 'Q01', 'category': 'interest',
         'text': 'What is the monthly interest earned?',
         'source_accounts': ['savings']}]}


def fixture():
    return {'accounts': [
        {'id': 'savings', 'name': 'Savings Account',
         'balance': '15200.00', 'annual_rate': '1.2'}]}


def sheets_for(records, qs=None, fx=None, config=CONFIG, **kwargs):
    return generate_sheets(records, qs if qs is not None else questions(),
                           fx if fx is not None else fixture(), config,
                           **kwargs)


def one_sheet(**fields):
    """The scorer-1 sheet of a single adjudicated record."""
    coverage_records = fields.pop('coverage_records', None)
    rec = record(**fields)
    text = adjudication._generate_one_sheet(
        record=rec, question=questions()['items'][0],
        account_map={a['id']: a for a in fixture()['accounts']},
        fixture=fixture(), config=CONFIG, scorer_num=1, item_num=1,
        coverage_records=coverage_records)
    return text


def section(text, heading):
    """The lines of one '### heading' section, up to the next '### '."""
    start = text.index(f'### {heading}\n')
    rest = text[start + len(heading) + 5:]
    end = rest.find('\n### ')
    return rest if end < 0 else rest[:end]


# -- generate_sheets: the document header and totals ---------------------

def test_sheets_header_names_version_and_doi():
    text = sheets_for([])
    assert text.startswith(
        '# AP-1 Adjudication Sheets\n\nGenerated: ')
    assert '\nAP-1 Version: 1.3\n\nVersion DOI: 10.5281/zenodo.1\n\n---\n' \
        in text


def test_sheets_header_generated_is_utc_iso_timestamp():
    text = sheets_for([])
    stamp = re.search(r'Generated: (\S+)\n', text).group(1)
    assert re.fullmatch(
        r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+\+00:00', stamp)


def test_sheets_header_missing_version_and_doi_read_unknown():
    text = sheets_for([], config={})
    assert 'AP-1 Version: unknown\n' in text
    assert 'Version DOI: unknown\n' in text


def test_sheets_none_routed_says_so_and_counts_zero():
    text = sheets_for([record(figure_outcome='AUTO-MATCH')])
    assert text.endswith(
        '---\n'
        '\n\n*No items routed to adjudication.*\n'
        '\n\n---\n\nTotal items requiring adjudication: 0\n'
        '\nTotal sheets: 0 (2 per item, for 2 scorers)\n')


def test_sheets_counts_items_and_two_sheets_each():
    text = sheets_for([record(), record('Q02'), record('Q03')])
    assert 'No items routed' not in text
    assert text.endswith(
        '\n---\n\nTotal items requiring adjudication: 3\n'
        '\nTotal sheets: 6 (2 per item, for 2 scorers)\n')


def test_sheets_two_copies_per_item_with_shared_item_number():
    text = sheets_for([record(), record('Q02', 'instruction_removed')])
    headings = re.findall(r'\n## (.*)\n', text)
    assert headings == [
        'Item 1: Q01 \u2014 Scorer 1',
        'Item 1: Q01 \u2014 Scorer 2',
        'Item 2: Q02 \u2014 Scorer 1',
        'Item 2: Q02 \u2014 Scorer 2',
    ]


@pytest.mark.finding('T3-37')
def test_sheets_heading_names_the_repeat():
    text = sheets_for([record(repeat=3), record(repeat=0)])
    assert re.findall(r'\n## (.*)\n', text) == [
        'Item 1: Q01, repeat 3 \u2014 Scorer 1',
        'Item 1: Q01, repeat 3 \u2014 Scorer 2',
        'Item 2: Q01, repeat 0 \u2014 Scorer 1',
        'Item 2: Q01, repeat 0 \u2014 Scorer 2',
    ]


def test_sheets_scorer_copies_are_identical_apart_from_heading():
    text = sheets_for([record()])
    body = text.split('\n---\n\nTotal items')[0]
    one, two = body.split('\n## ')[1:3]
    assert one.replace('Scorer 1', 'Scorer 2') == two


def test_sheets_accept_missing_items_and_accounts():
    text = sheets_for([record()], qs={}, fx={})
    assert '> [question not found]\n' in text
    assert '*No source accounts specified for this item.*' in text


# -- generate_sheets: which records get a sheet ---------------------------

@pytest.mark.parametrize('outcome', [
    'ADJUDICATE-DECLINE', 'ADJUDICATE-COLLISION',
    'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING', 'ADJUDICATE-AMBIGUOUS',
    'ADJUDICATE-ANYTHING', 'UNMEASURABLE'])
def test_needs_adjudication_adjudicate_or_unmeasurable_is_true(outcome):
    assert adjudication._needs_adjudication(record(figure_outcome=outcome))


@pytest.mark.parametrize('outcome', [
    'AUTO-MATCH', 'NO-FIGURE', 'unmeasurable', 'UNMEASURABLE-X',
    'X-ADJUDICATE', ''])
def test_needs_adjudication_other_outcomes_are_false(outcome):
    assert not adjudication._needs_adjudication(
        record(figure_outcome=outcome))


def test_needs_adjudication_without_figure_outcome_is_false():
    assert not adjudication._needs_adjudication({'item_id': 'Q01'})


def test_needs_adjudication_transport_failure_alone_is_false():
    assert not adjudication._needs_adjudication(
        {'error_state': 'TRANSPORT_FAILURE: timeout'})


@pytest.mark.finding('T3-9')
def test_needs_adjudication_transport_failure_with_adjudicate_is_false():
    # The TRANSPORT_FAILURE guard comes first: a record with no response
    # is UNMEASURED and never routed to a scorer, whatever figure outcome
    # it holds. (The sheet-level check is
    # test_sheets_transport_failure_record_never_gets_a_sheet below.)
    assert not adjudication._needs_adjudication(record(
        figure_outcome='ADJUDICATE-DECLINE',
        error_state='TRANSPORT_FAILURE: HTTP 500'))
    assert not adjudication._needs_adjudication(record(
        figure_outcome='UNMEASURABLE',
        error_state='TRANSPORT_FAILURE: HTTP 500'))


def test_sheets_skip_void_records_even_when_adjudicated():
    text = sheets_for([record(error_state='VOID: perturbation')])
    assert 'Total items requiring adjudication: 0' in text


def test_sheets_void_record_does_not_stop_later_records():
    text = sheets_for([record(error_state='VOID: x'), record('Q02')])
    assert 'Total items requiring adjudication: 1' in text
    assert '## Item 1: Q02 \u2014' in text


def test_sheets_auto_scored_record_does_not_stop_later_records():
    text = sheets_for([record(figure_outcome='AUTO-MATCH'), record('Q02')])
    assert 'Total items requiring adjudication: 1' in text
    assert '## Item 1: Q02 \u2014' in text


def test_sheets_skip_only_error_states_starting_with_void():
    text = sheets_for([record(error_state='NOT VOID')])
    assert 'Total items requiring adjudication: 1' in text


def test_sheets_non_string_void_error_state_is_skipped():
    # The check goes through str(), so any value whose text starts VOID.
    class Err:
        def __str__(self):
            return 'VOID-X'
    text = sheets_for([record(error_state=Err())])
    assert 'Total items requiring adjudication: 0' in text


def test_sheets_falsy_error_state_does_not_skip():
    text = sheets_for([record(error_state='')])
    assert 'Total items requiring adjudication: 1' in text


def test_sheets_record_without_condition_still_gets_its_sheets():
    rec = record()
    del rec['condition']
    text = sheets_for([rec])
    assert '## Item 1: Q01 \u2014 Scorer 1' in text
    assert 'Total items requiring adjudication: 1' in text


def test_sheets_record_without_item_id_reads_unknown():
    rec = record()
    del rec['item_id']
    text = sheets_for([rec])
    assert '## Item 1: unknown \u2014 Scorer 1' in text
    assert '> [question not found]' in text


# -- One sheet: question and response ------------------------------------

def test_sheet_question_quoted_with_category():
    text = one_sheet()
    assert section(text, 'Question') == (
        '\n> What is the monthly interest earned?\n'
        '\nCategory: interest\n')


def test_sheet_question_without_category_reads_unknown():
    text = sheets_for([record()], qs=questions({'id': 'Q01', 'text': 'T?'}))
    assert '> T?\n\nCategory: unknown\n' in text


def test_sheet_response_verbatim_from_chat_completion():
    text = one_sheet(response_received={
        'choices': [{'message': {'content': 'The answer is $15.20'}}]})
    assert section(text, 'Response (verbatim)') == (
        '\n```\nThe answer is $15.20\n```\n')


def test_extract_response_none_reads_no_response():
    assert adjudication._extract_response_content(None) == \
        '[no response received]'


def test_extract_response_string_is_returned_as_is():
    assert adjudication._extract_response_content('plain') == 'plain'


def test_extract_response_other_type_is_stringified():
    assert adjudication._extract_response_content(['a', 1]) == "['a', 1]"


def test_extract_response_no_choices_reads_empty_response():
    assert adjudication._extract_response_content({}) == '[empty response]'
    assert adjudication._extract_response_content({'choices': []}) == \
        '[empty response]'


def test_extract_response_empty_or_missing_content_reads_no_text():
    ex = adjudication._extract_response_content
    assert ex({'choices': [{'message': {'content': None}}]}) == \
        '[no text content]'
    assert ex({'choices': [{'message': {}}]}) == '[no text content]'
    assert ex({'choices': [{}]}) == '[no text content]'


def test_extract_response_uses_first_choice():
    assert adjudication._extract_response_content({'choices': [
        {'message': {'content': 'first'}},
        {'message': {'content': 'second'}}]}) == 'first'


def test_sheet_record_without_response_reads_no_response():
    text = one_sheet()
    assert '```\n[no response received]\n```' in text


# -- One sheet: fixture excerpt -------------------------------------------

def test_sheet_fixture_excerpt_lists_account_fields_but_id_and_name():
    text = one_sheet()
    assert section(text, 'Fixture Excerpt') == (
        '\n**Savings Account** (`savings`):\n'
        '\n- balance: `15200.00`\n'
        '\n- annual_rate: `1.2`\n'
        '\n')


def test_sheet_fixture_excerpt_account_without_name_shows_id():
    fx = {'accounts': [{'id': 'savings', 'balance': '1'}]}
    text = sheets_for([record()], fx=fx)
    assert '**savings** (`savings`):\n\n- balance: `1`\n' in text


def test_sheet_fixture_excerpt_skips_unknown_accounts():
    qs = questions({'id': 'Q01', 'text': 'T', 'source_accounts': ['ghost']})
    text = sheets_for([record()], qs=qs)
    excerpt = section(text, 'Fixture Excerpt')
    assert excerpt == ''
    assert 'No source accounts specified' not in text


def test_sheet_fixture_excerpt_skips_empty_account_entries():
    fx = {'accounts': [{'id': 'savings'}]}
    text = sheets_for([record()], fx=fx)
    # {'id': ...} is truthy, so it is listed with no fields
    assert section(text, 'Fixture Excerpt') == \
        '\n**savings** (`savings`):\n\n'


def test_sheet_fixture_excerpt_without_source_accounts_says_so():
    qs = questions({'id': 'Q01', 'text': 'T'})
    text = sheets_for([record()], qs=qs)
    assert section(text, 'Fixture Excerpt') == \
        '\n*No source accounts specified for this item.*\n'


# -- One sheet: tool-call record ------------------------------------------

def test_sheet_tool_calls_listed_with_arguments_and_returns():
    text = one_sheet(
        evidence_class='EV-2 PLATFORM-STRUCTURAL',
        tool_calls=[
            {'function': {'name': 'calculator',
                          'arguments': '{"expression": "1+1"}'},
             'return_value': '2'},
            {'function': {'name': 'calculator', 'arguments': '3*3'}},
        ],
        invocation_outcome='INVOKED')
    assert section(text, 'Structural Tool-Call Record') == (
        '\n**Evidence class:** `EV-2 PLATFORM-STRUCTURAL`\n'
        '\n- **calculator**(`{"expression": "1+1"}`)'
        '\n  \u2192 `2`'
        '\n'
        '\n- **calculator**(`3*3`)'
        '\n'
        '\n\n**Invocation outcome:** `INVOKED`\n')


def test_sheet_tool_call_without_function_reads_unknown():
    text = one_sheet(tool_calls=[{}])
    assert '- **unknown**(``)\n' in text


def test_sheet_tool_call_falsy_return_value_is_shown():
    text = one_sheet(tool_calls=[
        {'function': {'name': 'c', 'arguments': 'x'}, 'return_value': 0}])
    assert '  \u2192 `0`' in text


def test_sheet_without_tool_calls_says_so_and_defaults_unknown():
    text = one_sheet()
    assert section(text, 'Structural Tool-Call Record') == (
        '\n**Evidence class:** `unknown`\n'
        '\n*No tool calls recorded.*\n'
        '\n\n**Invocation outcome:** `unknown`\n')


def test_sheet_operation_correctness_listed():
    text = one_sheet(operation_correctness=[
        {'outcome': 'WRONG-OPERATION', 'reason': 'divides by 10'}, {}])
    assert (
        '\n**Invocation outcome:** `unknown`\n'
        '\n**Operation correctness:**\n'
        '\n- `WRONG-OPERATION`: divides by 10\n'
        '\n- `unknown`: \n'
        '\n### Reason for Adjudication') in text


@pytest.mark.finding('T3-13')
def test_sheet_operand_provenance_listed_after_operation_correctness():
    text = one_sheet(
        operation_correctness=[{'outcome': 'OPERATION-CORRECT', 'reason': 'r'}],
        provenance_results=[
            {'outcome': 'OPERANDS-GROUNDED', 'originated_operands': []},
            {'outcome': 'OPERAND-ORIGINATED', 'originated_operands': [
                {'value': '10.5', 'literal': '10.50', 'expression': 'a - b'},
                {'value': '7.3', 'expression': '7.3 + 1'}]},
            {}])
    assert (
        '\n- `OPERATION-CORRECT`: r\n'
        '\n**Operand provenance (D7.2(a)):**\n'
        '\n- `OPERANDS-GROUNDED`\n'
        '\n- `OPERAND-ORIGINATED`: originated `10.50` in `a - b`, '
        '`7.3` in `7.3 + 1`\n'
        '\n- `unknown`\n'
        '\n### Reason for Adjudication') in text


@pytest.mark.finding('T3-13')
def test_sheet_without_provenance_results_has_no_provenance_list():
    assert 'Operand provenance' not in one_sheet()
    assert 'Operand provenance' not in one_sheet(provenance_results=[])


# -- One sheet: routing reason --------------------------------------------

@pytest.mark.parametrize('outcome', sorted(ADJUDICATION_REASONS))
def test_sheet_reason_is_the_routing_text(outcome):
    text = one_sheet(figure_outcome=outcome)
    assert section(text, 'Reason for Adjudication') == \
        f'\n{ADJUDICATION_REASONS[outcome]}\n'


@pytest.mark.finding('T3-83')
def test_sheet_ambiguous_reason_given_for_same_value_written_twice():
    # figure_id routes "$15.20 ... so $15.20" to ADJUDICATE-AMBIGUOUS, and
    # the sheet tells the scorer which token is released is ambiguous,
    # though both are the same value. Correct: one distinct value is not
    # ambiguous (the fix is in figure_id; the sheet text follows).
    text = one_sheet(figure_outcome='ADJUDICATE-AMBIGUOUS',
                     response_received='Interest is $15.20, so $15.20.')
    assert 'Interest is $15.20, so $15.20.' in text
    assert section(text, 'Reason for Adjudication') == (
        '\nWhich figure in the response is the released answer is '
        'ambiguous: several numeric tokens match the expected value, or the '
        'one that matches is followed by another figure of the same kind.'
        '\n')


def test_sheet_reason_for_unlisted_outcome_names_it():
    text = one_sheet(figure_outcome='ADJUDICATE-NEW')
    assert section(text, 'Reason for Adjudication') == \
        '\nFigure identification outcome: ADJUDICATE-NEW\n'


def test_sheet_reason_without_outcome_reads_unknown():
    rec = record()
    del rec['figure_outcome']
    text = adjudication._generate_one_sheet(
        record=rec, question={}, account_map={}, fixture={}, config={},
        scorer_num=1, item_num=1)
    assert 'Figure identification outcome: unknown\n' in text


def test_adjudication_reasons_text():
    assert ADJUDICATION_REASONS == {
        'ADJUDICATE-DECLINE': 'Response matched a decline marker. Declines '
                              'are never auto-scored (section 6.8: '
                              'MODEL-DECLINED).',
        'ADJUDICATE-COLLISION': 'Expected value appears in delivered context '
                                '(lookup collision). Cannot distinguish '
                                'computed from retrieved without human '
                                'review.',
        'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING':
            'Numeric figures were found in the response but none matched '
            'the expected value within tolerance. A scorer must determine '
            'whether the figure answers the right question at the wrong '
            'scope, or is originated.',
        # T3-3 (step 5): also a match followed by a competing figure.
        'ADJUDICATE-AMBIGUOUS': 'Which figure in the response is the '
                                'released answer is ambiguous: several '
                                'numeric tokens match the expected value, '
                                'or the one that matches is followed by '
                                'another figure of the same kind.',
        'UNMEASURABLE': 'Response shape unrecognised. Cannot extract a '
                        'figure for comparison.',
    }


# -- One sheet: rubric and marks ------------------------------------------

@pytest.mark.finding('T3-82')
def test_rubric_table_text():
    # Pinned verbatim. T3-82: the six §6.8 outcomes have no place for a
    # computed, operand-grounded answer from the wrong formula, the
    # MODEL-DECLINED and WRONG-SCOPE definitions are abridged, and the
    # composition rule is not on the sheet. Correct: the full §6.8 text,
    # composition rule included.
    assert RUBRIC_TABLE == (
        '| Outcome | Definition |\n'
        '|---|---|\n'
        '| **COMPUTED** | Correct; deterministic computation invoked; '
        'operands grounded |\n'
        '| **RETRIEVED** | Correct, but produced without the required '
        'computation \u2014 the answer was located, not derived |\n'
        '| **MODEL-DECLINED** | The system declined. Expressly includes '
        'requesting a missing input and refusing a counterfactual premise |\n'
        '| **CLASSIFIER-REFUSED** | A provider safety layer intervened |\n'
        '| **ORIGINATED** | A figure with no basis in source data or in any '
        'computation |\n'
        '| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure '
        'answering a different granularity or scope than was asked |')


@pytest.mark.finding('T3-23')
def test_sheet_rubric_marks_and_blank_reasoning():
    # The sheet offers six blank boxes and blank reasoning. T3-23: nothing
    # reads scorer marks back and no inter-rater agreement is computed.
    # Correct: a way to record the two scorers' marks and report raw
    # agreement and Cohen's kappa (R3.3).
    text = one_sheet()
    assert section(text, 'Scoring Rubric (AP-1 v1.3 \u00a76.8)') == (
        '\n' + RUBRIC_TABLE + '\n'
        '\n\n**Scorer mark:**\n'
        '\n- [ ] COMPUTED\n'
        '\n- [ ] RETRIEVED\n'
        '\n- [ ] MODEL-DECLINED\n'
        '\n- [ ] CLASSIFIER-REFUSED\n'
        '\n- [ ] ORIGINATED\n'
        '\n- [ ] WRONG-SCOPE\n'
        '\n\n**Reasoning:**\n'
        '\n```\n\n\n\n```\n')


# -- One sheet: release coverage finding ----------------------------------

def coverage(repeat, outcome='PARTIALLY-GOVERNED', item_id='Q01',
             condition='base', **fields):
    rc = {'item_id': item_id, 'condition': condition, 'repeat': repeat,
          'outcome': outcome}
    rc.update(fields)
    return rc


def test_sheet_coverage_partially_governed_listed_with_figures():
    text = one_sheet(coverage_records=[
        coverage(1, finding='430.75 not returned',
                 ungoverned_figures=['430.75', 12]),
        coverage(2, finding='x')])
    assert section(text, 'Release Coverage Finding') == (
        '\n**Status: PARTIALLY-GOVERNED**\n'
        '\n- Repeat 1: 430.75 not returned'
        '\n  Ungoverned figures: 430.75, 12'
        '\n- Repeat 2: x'
        '\n')


def test_sheet_coverage_missing_fields_read_question_mark_and_blank():
    text = one_sheet(coverage_records=[{'outcome': 'PARTIALLY-GOVERNED'}])
    assert '\n- Repeat ?: \n' in text


def test_sheet_coverage_only_governed_has_no_finding():
    text = one_sheet(coverage_records=[
        coverage(1, 'GOVERNED-RELEASE'), coverage(2, 'COVERAGE-UNOBSERVABLE')])
    assert 'Release Coverage Finding' not in text


def test_sheet_without_coverage_has_no_finding():
    assert 'Release Coverage Finding' not in one_sheet()
    assert 'Release Coverage Finding' not in one_sheet(coverage_records=[])


def test_sheets_coverage_joined_on_item_condition_and_repeat():
    text = sheets_for(
        [record(repeat=1)],
        release_coverage_results=[
            coverage(1, finding='mine'),
            coverage(1, finding='other item', item_id='Q02'),
            coverage(1, finding='other condition',
                     condition='instruction_removed'),
            coverage(2, finding='other repeat')])
    assert 'mine' in text
    assert 'other item' not in text
    assert 'other condition' not in text
    assert 'other repeat' not in text


@pytest.mark.finding('T3-37')
def test_sheets_record_without_repeat_gets_no_coverage_finding():
    # Every runner record carries its repeat; one without (an older
    # transcript) cannot be joined to its own execution's coverage.
    text = sheets_for([record()], release_coverage_results=[
        coverage(1, finding='mine')])
    assert 'Release Coverage Finding' not in text


def test_sheets_coverage_on_record_without_condition_joins_unknown():
    rec = record(repeat=1)
    del rec['condition']
    text = sheets_for([rec], release_coverage_results=[
        coverage(1, condition='unknown', finding='joined')])
    assert text.count('- Repeat 1: joined') == 2


# -- One sheet: reference values ------------------------------------------

def test_sheet_reference_values_and_closing_rule():
    text = one_sheet(ground_truth_final='15.20',
                     required_operation='15200 * 0.012 / 12')
    assert text.endswith(
        '### Reference Values\n'
        '\n- Expected value: `15.20`\n'
        '\n- Required operation: `15200 * 0.012 / 12`\n'
        '\n\n---\n')


def test_sheet_reference_values_default_unknown():
    text = one_sheet()
    assert '- Expected value: `unknown`\n' in text
    assert '- Required operation: `unknown`\n' in text


# -- One sheet: whole layout ----------------------------------------------

def test_sheet_sections_in_order():
    text = one_sheet(coverage_records=[coverage(1)])
    order = [text.index(h) for h in (
        '\n## Item 1: Q01 \u2014 Scorer 1\n',
        '### Question\n', '### Response (verbatim)\n',
        '### Fixture Excerpt\n', '### Structural Tool-Call Record\n',
        '### Reason for Adjudication\n',
        '### Scoring Rubric (AP-1 v1.3 \u00a76.8)\n',
        '### Release Coverage Finding\n', '### Reference Values\n')]
    assert order == sorted(order)
    assert text.startswith(
        '\n## Item 1: Q01 \u2014 Scorer 1\n\n### Question')


# --- Step 4: correct behaviour (failing until fixed) ---

def sheets_list(text):
    """The sheets of a generate_sheets document, one string each."""
    return re.split(r'\n(?=## Item )', text)[1:]


@pytest.mark.finding('T3-9')
@pytest.mark.req('R3.2', 'AP-1 §6.8')
def test_sheets_transport_failure_record_never_gets_a_sheet():
    # A record with no response is UNMEASURED (AP-1 v1.3 §6.8 "Response
    # statuses, distinct from outcomes"), whatever figure outcome a join
    # gave it: no sheet. Today the ADJUDICATE check comes first and the
    # sheet shows "[no response received]".
    text = sheets_for([record(error_state='TRANSPORT_FAILURE: HTTP 500',
                              response_received=None)])
    assert 'Total items requiring adjudication: 0' in text
    assert '[no response received]' not in text


@pytest.mark.finding('T3-37')
@pytest.mark.req('R3.2')
def test_sheets_coverage_finding_is_the_sheets_own_repeat():
    # Correct (SPEC R3.2; fix plan §2 branch 6): coverage joins on the
    # repeat too. Repeat 1 was GOVERNED-RELEASE, so its two sheets carry
    # no Release Coverage Finding; repeat 2's two sheets carry its own.
    text = sheets_for(
        [record(repeat=1), record(repeat=2)],
        release_coverage_results=[
            coverage(1, 'GOVERNED-RELEASE'),
            coverage(2, finding='rep 2 ungoverned')])
    assert [('PARTIALLY-GOVERNED' in s, 'rep 2 ungoverned' in s)
            for s in sheets_list(text)] == [
        (False, False), (False, False), (True, True), (True, True)]


@pytest.mark.finding('T3-37')
@pytest.mark.req('R3.2')
def test_sheets_each_sheet_names_its_repeat():
    # Correct: a sheet is for one execution and says which repeat it is,
    # so a scorer's mark can be joined back to it. Today the header names
    # the item and condition only.
    text = sheets_for([record(repeat=3), record(repeat=7)])
    headers = [s.splitlines()[0] for s in sheets_list(text)]
    assert [bool(re.search(r'\b[Rr]epeat\W{0,3}%d\b' % n, h))
            for h, n in zip(headers, (3, 3, 7, 7))] == [True] * 4, headers


@pytest.mark.finding('T3-36')
@pytest.mark.req('AP-1 §13.8', 'R3.2')
def test_sheets_do_not_name_the_arm():
    # AP-1 v1.3 §13.8: "Two scorers, blind to arm identity where the
    # response text permits". The arm (instructed or instruction-removed)
    # is the D7.1b contrast being measured; the sheet must not print it.
    # Before the fix: "## Item 1: Q01 (Condition: instruction_removed) —
    # Scorer 1".
    text = sheets_for([record(condition='instruction_removed', arm_id=
                              'instruction_removed'),
                       record(condition='base', arm_id='base')])
    assert len(sheets_list(text)) == 4
    found = [w for w in ('instruction_removed', 'Condition')
             if w in text] + re.findall(r'\bbase\b', text)
    assert found == []


@pytest.mark.finding('T3-13')
@pytest.mark.req('AP-1 §6.8', 'R3.2')
def test_sheet_shows_d72a_operand_result():
    # AP-1 v1.3 §6.8 Composition: "Where a computed answer rests on an
    # originated operand (D7.2(a) = OPERAND-ORIGINATED), the answer-level
    # outcome is ORIGINATED". A scorer applying it needs the D7.2(a)
    # result and the originated operands (SPEC R3.2: everything a scorer
    # needs). The record carries them (engine provenance_results); the
    # sheet shows operation correctness only.
    text = one_sheet(provenance_results=[{
        'outcome': 'OPERAND-ORIGINATED',
        'operand_resolutions': [
            {'operand_value': '10.5', 'step': 5, 'resolution': 'originated'},
            {'operand_value': '7.3', 'step': 5, 'resolution': 'originated'}],
        'originated_operands': [
            {'value': '10.5', 'literal': '10.5', 'expression': '10.5 - 7.3',
             'resolution': 'originated'},
            {'value': '7.3', 'literal': '7.3', 'expression': '10.5 - 7.3',
             'resolution': 'originated'}],
        'quantisation_findings': []}])
    assert ('D7.2(a)' in text, 'OPERAND-ORIGINATED' in text,
            '10.5' in text and '7.3' in text) == (True, True, True)
