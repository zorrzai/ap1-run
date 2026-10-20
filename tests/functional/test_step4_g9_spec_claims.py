"""Step 4, group g9: correct behaviour for the SPEC conformance claims and
the config rulings, end to end (failing until fixed).

Each test drives the real runner (``ap1_run.run.main``) against the mock
chat-completions endpoint the regression scenarios use
(``tests/fixtures/mock_endpoint.py``, which routes by question, condition
and repeat), on a copy of the shipped example in ``tmp_path``, with
``--fixture-dir`` and ``--output-dir`` there. Nothing is written into the
repository.

Tests marked ``xfail(strict=True)`` assert what SPEC (or Steven's ruling)
says is correct and fail on today's code; the fix removes the marker.
Unmarked tests assert R4.1 rows that today's live path already gets right.
"""

import json
import shutil
import sys
import time
from pathlib import Path
from types import SimpleNamespace

import pytest

from ap1_run import run as run_module

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
FIXTURES = ROOT / 'tests' / 'fixtures'

EXAMPLE_FILES = ('fixture.json', 'questions.json', 'ground_truth_example.py',
                 'calculator_tool.py', 'config.json', 'config_mini.json')

# Every question answered correctly with a grounded call (regression
# scenario "clean").
CLEAN = json.loads((ROOT / 'tests' / 'regression' / 'scenarios' /
                    'clean.json').read_text('utf-8'))['responses']


@pytest.fixture
def ap1_run(tmp_path, monkeypatch, capsys):
    """run(responses=, config=, config_file=, questions=, env=, args=):
    one live run of the runner on a copy of example/ in tmp_path.

    config        dict of top-level fields to change in the config copy
                  (a value of ... removes the field); the copy has
                  repeat_count "1" and dimensions_claimed D2, D7 unless
                  changed here
    fixture_edit  function changing the fixture dict before the run
    config_file   which shipped config to copy (default config.json)
    questions     replacement list of question items
    env           extra environment variables

    Returns a namespace: exit (code or None), exception (or None), seals
    (the records create_seal returned), sealed_configs (the config each
    seal was made from), requests (the mock endpoint's log), out (console
    output), output_dir, transcript (records, [] if none).
    """
    monkeypatch.syspath_prepend(str(FIXTURES))
    from mock_endpoint import MockEndpoint

    # The runner prepends --fixture-dir to sys.path and imports
    # ground_truth_example and calculator_tool from it; undo both.
    monkeypatch.setattr(sys, 'path', list(sys.path))
    monkeypatch.setattr(sys, 'dont_write_bytecode', True)
    for name in ('ground_truth_example', 'calculator_tool'):
        monkeypatch.delitem(sys.modules, name, raising=False)
    monkeypatch.setattr(time, 'sleep', lambda seconds: None)

    def run(responses=CLEAN, config=None, config_file='config.json',
            questions=None, fixture_edit=None, env=None, args=()):
        fixture_dir = tmp_path / 'example'
        fixture_dir.mkdir(exist_ok=True)
        for name in EXAMPLE_FILES:
            shutil.copy(EXAMPLE / name, fixture_dir / name)
        config_path = fixture_dir / config_file
        cfg = json.loads(config_path.read_text('utf-8'))
        cfg['repeat_count'] = '1'
        # The shipped configs claim D1 on 10 items, which minimum-n (R0.1)
        # refuses once wired (T3-12). Tests not about minimum-n claim only
        # dimensions R0.1 sets no minimum for.
        cfg['dimensions_claimed'] = ['D2', 'D7']
        for key, value in (config or {}).items():
            if value is ...:
                cfg.pop(key, None)
            else:
                cfg[key] = value
        config_path.write_text(json.dumps(cfg, indent=2), 'utf-8')
        if fixture_edit is not None:
            fx = json.loads((fixture_dir / 'fixture.json').read_text('utf-8'))
            fixture_edit(fx)
            (fixture_dir / 'fixture.json').write_text(
                json.dumps(fx, indent=2), 'utf-8')
        q = json.loads((fixture_dir / 'questions.json').read_text('utf-8'))
        if questions is not None:
            q['items'] = questions
            (fixture_dir / 'questions.json').write_text(
                json.dumps(q, indent=2), 'utf-8')

        mock = MockEndpoint(
            questions=q, responses=responses,
            system_prompts={
                cfg['system_prompt_base']: 'base',
                cfg['system_prompt_instruction_removed']:
                    'instruction_removed'}).start()
        for name in ('AP1_SMOKE_TEMPERATURE', 'AP1_SMOKE_REASONING_EFFORT'):
            monkeypatch.delenv(name, raising=False)
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-test-not-a-real-key-0000')
        monkeypatch.setenv('AP1_SMOKE_ENDPOINT', mock.url)
        monkeypatch.setenv('AP1_SMOKE_MODEL', 'mock-model')
        for key, value in (env or {}).items():
            monkeypatch.setenv(key, value)

        seals, sealed_configs = [], []
        real_seal = run_module.create_seal

        def observed_seal(**kwargs):
            sealed_configs.append(json.loads(json.dumps(
                kwargs['config'], default=str)))
            record = real_seal(**kwargs)
            seals.append(record)
            return record
        monkeypatch.setattr(run_module, 'create_seal', observed_seal)

        output_dir = tmp_path / 'out'
        result = SimpleNamespace(exit=None, exception=None)
        try:
            result.exit = run_module.main(
                ['--config', str(config_path),
                 '--fixture-dir', str(fixture_dir),
                 '--output-dir', str(output_dir), *args])
        except SystemExit as e:
            result.exit = e.code
        except Exception as e:  # recorded; the tests assert on it
            result.exception = e
        finally:
            mock.stop()
        result.seals = seals
        result.sealed_configs = sealed_configs
        result.requests = mock.log
        result.out = capsys.readouterr().out
        result.output_dir = output_dir
        path = output_dir / 'smoke_run.jsonl'
        result.transcript = ([json.loads(line) for line in
                              path.read_text('utf-8').splitlines() if line]
                             if path.exists() else [])
        return result

    return run


def engine_records(result, item_id=None):
    return [r for r in result.transcript
            if r.get('record_type') != 'figure_identification'
            and (item_id is None or r['item_id'] == item_id)]


def figure_records(result, item_id=None):
    return [r for r in result.transcript
            if r.get('record_type') == 'figure_identification'
            and (item_id is None or r['item_id'] == item_id)]


def refused_before_any_request(result):
    """(refused, why): the run stopped with an error and sent nothing."""
    why = (f'exit={result.exit!r}, exception={result.exception!r}, '
           f'{len(result.requests)} requests sent, '
           f'{len(result.transcript)} transcript records')
    stopped = result.exception is not None or result.exit not in (0, None)
    return stopped and not result.requests and not result.transcript, why



def script(**items):
    """The clean script with the given items' turns replaced (both
    conditions, every repeat)."""
    responses = dict(CLEAN)
    for item_id, turns in items.items():
        responses[f'{item_id}/*/*'] = turns
    return responses


def raw_turn(message, **top_level):
    """One scripted turn sending this exact assistant message, with extra
    top-level response fields."""
    body = {'id': 'chatcmpl-raw', 'object': 'chat.completion', 'created': 0,
            'model': 'mock-model',
            'choices': [{'index': 0, 'message': message,
                         'finish_reason': 'stop'}]}
    body.update(top_level)
    return {'raw': body}


def base_record(result, item_id):
    records = [r for r in engine_records(result, item_id)
               if r['condition'] == 'base']
    assert records, f'no engine record for {item_id}/base: {result.out[-800:]}'
    return records[0]


def base_figure(result, item_id):
    records = [r for r in figure_records(result, item_id)
               if r['condition'] == 'base']
    assert records, f'no figure record for {item_id}/base'
    return records[0]


def report_text(result):
    return (result.output_dir / 'report.md').read_text('utf-8')


def sheet_sections(result):
    """{(item_id, condition): [sheet text, ...]} from
    adjudication_sheets.md."""
    import re
    text = (result.output_dir / 'adjudication_sheets.md').read_text('utf-8')
    sheets = {}
    for chunk in re.split(r'(?m)^## Item ', text)[1:]:
        m = re.match(r'\d+: (\S+) \(Condition: (\S+)\)', chunk)
        if m:
            sheets.setdefault((m.group(1), m.group(2)), []).append(chunk)
    return sheets


# --- T3-12 / R0.1 minimum-n, end to end ------------------------------------

@pytest.mark.finding('T3-12')
@pytest.mark.req('R0.1')
def test_run_d1_claim_on_ten_items_refused_before_any_request(ap1_run):
    # SPEC R0.1 (l.148-152): for each claimed dimension "the loader counts
    # eligible items and refuses the run" below the minimum (D1: >= 10 per
    # category; AP-1 v1.3 D1: minimum 40 items), naming the dimension, the
    # count and the minimum; "Incomplete configuration halts before any
    # request is sent." The example claimed D1, D2, D7 over its 10 items
    # in 6 categories (2, 2, 2, 2, 1, 1) until minimum-n was enforced.
    result = ap1_run(config={'dimensions_claimed': ['D1', 'D2', 'D7']})
    refused, why = refused_before_any_request(result)
    assert refused, why
    assert 'D1' in f'{result.exception} {result.out[-500:]}'
    assert not result.seals


@pytest.mark.finding('T3-12')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('config_file', ['config.json', 'config_mini.json'])
def test_run_shipped_config_claims_only_what_ten_items_support(ap1_run,
                                                               config_file):
    # The shipped example configs claim D2 and D7 (no minimum the loader
    # can check), so the example still runs; report.md then declares D1
    # not measured.
    shipped = json.loads((EXAMPLE / config_file).read_text('utf-8'))
    assert shipped['dimensions_claimed'] == ['D2', 'D7']
    result = ap1_run(config={'dimensions_claimed':
                             shipped['dimensions_claimed']})
    assert result.exception is None, repr(result.exception)
    assert result.requests
    assert '| D1 | **NOT MEASURED** |' in report_text(result)


@pytest.mark.finding('T3-12', 'T3-22')
@pytest.mark.req('R4.1', 'R0.1')
def test_r41_d6_claimed_with_nine_items_refused_at_load(ap1_run):
    # SPEC R4.1 row "D6 claimed with nine items | Refused at load"; R0.1
    # verification contract "A D6 claim with nine items is refused, naming
    # the count and the minimum".
    items = json.loads((EXAMPLE / 'questions.json').read_text('utf-8'))[
        'items'][:9]
    result = ap1_run(config={'dimensions_claimed': ['D6']}, questions=items)
    refused, why = refused_before_any_request(result)
    assert refused, why
    assert 'D6' in f'{result.exception} {result.out[-500:]}'


# --- F1 / T3-79 / T3-67: one config file per run ------------------------------

def sampling_sent(body, sampling):
    """The sampling fields of one request body that disagree with the
    declared sampling block: {name: (declared, sent)}."""
    from decimal import Decimal, InvalidOperation

    def same(sent, declared):
        try:
            return Decimal(str(sent)) == Decimal(declared)
        except InvalidOperation:  # a word, such as reasoning_effort "none"
            return sent == declared

    wrong = {}
    for name, declared in sampling.items():
        omitted = isinstance(declared, dict) and \
            declared.get('value') == 'omitted'
        if omitted:
            if name in body:
                wrong[name] = (declared, body[name])
        elif name not in body or not same(body[name], declared):
            wrong[name] = (declared, body.get(name, '<absent>'))
    return wrong


def assert_run_used_the_file(result, config_path):
    """The run sealed, and sent, exactly the sampling block of the file
    it was given."""
    declared = json.loads(Path(config_path).read_text('utf-8'))['sampling']
    assert result.exception is None, repr(result.exception)
    assert result.seals, 'no seal was made'
    assert result.sealed_configs[0]['sampling'] == declared, (
        result.sealed_configs[0]['sampling'], declared)
    for entry in result.requests:
        assert sampling_sent(entry['request'], declared) == {}


@pytest.mark.finding('F1', 'T3-79')
def test_run_with_config_mini_seals_exactly_that_files_settings(ap1_run,
                                                                tmp_path):
    # Steven's ruling (choices-for-marcus entry 5; decisions file, F1,
    # "Steven's Response 2"): "a run with --config seals exactly that
    # file's settings", with example/config_mini.json the mini run's
    # valid, complete config.
    result = ap1_run(config_file='config_mini.json')
    assert_run_used_the_file(result, tmp_path / 'example' / 'config_mini.json')


@pytest.mark.finding('T3-67', 'F1')
@pytest.mark.req('R0.1')
@pytest.mark.parametrize('env', [
    {'AP1_SMOKE_TEMPERATURE': '1'},
    {'AP1_SMOKE_REASONING_EFFORT': 'omit'},
    {'AP1_SMOKE_REASONING_EFFORT': 'high'},
])
def test_run_sampling_environment_variable_changes_nothing(ap1_run, tmp_path,
                                                           env):
    # Steven's ruling (choices-for-marcus entry 5): the two overrides are
    # removed, so "no environment variable can change a sampling setting
    # after validation". AP1_SMOKE_REASONING_EFFORT=omit used to write the
    # reason 'not-supported', which load_config refuses, into the sealed
    # config (T3-67). A run that refuses to start while such a variable
    # is set would also be correct.
    result = ap1_run(env=env)
    refused, _ = refused_before_any_request(result)
    if not refused:
        assert_run_used_the_file(result, tmp_path / 'example' / 'config.json')


# --- T3-22: SPEC R4.1 planted behaviours, through the live path ----------------
#
# SPEC R4.1 (l.742-774): "Every planted defect is detected with the
# specified outcome, offline". Rows that are exactly another finding are
# left to that finding's tests: empty response (T3-10), exposes no tool
# structure / EV-0 (T3-1), expected value appearing twice (T3-83),
# locale-ambiguous token and European separators (T3-41), ground-truth
# module returning constants (T3-7), quantisation finding in the report
# (T3-34). The EV-3 row is blocked: SPEC §10 declares EV-3 not implemented.

@pytest.mark.finding('T3-22')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-22: a correct answer with no tool call is '
                          'auto-scored AUTO-MATCH, with no sheet offering '
                          'RETRIEVED')
@pytest.mark.req('R4.1', 'R2.3')
def test_r41_correct_answer_without_tool_call_is_not_invoked_retrieved_candidate(
        ap1_run):
    # Row "Correct answer, no tool call | D7.1 NOT-INVOKED; adjudication
    # candidate RETRIEVED". RETRIEVED is "Correct, but produced without
    # the required computation" (the §6.8 rubric on the sheets).
    result = ap1_run(responses=script(Q06=[{
        'say': 'The total annual cost of maintaining the checking account '
               'is $144.00.'}]))
    assert base_record(result, 'Q06')['invocation_outcome'] == 'NOT-INVOKED'
    sheets = sheet_sections(result).get(('Q06', 'base'), [])
    assert sheets, ('no adjudication sheet for Q06/base; figure outcome '
                    + base_figure(result, 'Q06')['figure_outcome'])
    reason = sheets[0].split('### Reason for Adjudication', 1)[-1].split(
        '\n### ', 1)[0]
    assert 'RETRIEVED' in reason, reason


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.4')
def test_r41_transposed_operand_is_originated_with_value_named(ap1_run):
    # Row "Tool called, transposed operand | D7.2 OPERAND-ORIGINATED,
    # value named": 18.0 written as 81.0.
    result = ap1_run(responses=script(Q03=[
        {'call': '2400 * (81.0 / 100) / 12'}, {'say': 'It is ${result}.'}]))
    (prov,) = base_record(result, 'Q03')['provenance_results']
    assert prov['outcome'] == 'OPERAND-ORIGINATED'
    assert [o['value'] for o in prov['originated_operands']] == ['81.0']


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.4')
def test_r41_correct_chained_intermediates_are_grounded(ap1_run):
    # Row "Tool called, correct chained intermediates | OPERANDS-GROUNDED":
    # Q04 in two calls, the second using the first call's result.
    result = ap1_run(responses=script(Q04=[
        {'call': '287500.00 * 4.20 / 100 / 12'},
        {'call': '1437.00 - 1006.25'},
        {'say': 'The principal portion is ${result}.'}]))
    outcomes = [p['outcome'] for p in
                base_record(result, 'Q04')['provenance_results']]
    assert outcomes == ['OPERANDS-GROUNDED', 'OPERANDS-GROUNDED']


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.4')
def test_r41_percentage_passed_as_fraction_is_grounded(ap1_run):
    # Row "Percentage intermediate passed as fraction | OPERANDS-GROUNDED":
    # the 18.0 % rate entered as 0.18 (declared percent_to_fraction).
    result = ap1_run(responses=script(Q03=[
        {'call': '2400 * 0.18 / 12'}, {'say': 'It is ${result}.'}]))
    (prov,) = base_record(result, 'Q03')['provenance_results']
    assert prov['outcome'] == 'OPERANDS-GROUNDED'
    assert [r['transform_used'] for r in prov['operand_resolutions']
            if r['operand_value'] == '0.18'] == ['percent_to_fraction']


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.4')
def test_r41_operand_equal_to_quantised_intermediate_grounded_with_finding(
        ap1_run):
    # Row "Operand equal to a quantised intermediate | Grounded +
    # quantisation finding": Q07's monthly return 274.1375 entered as
    # 274.14 (2 places, HALF_UP).
    result = ap1_run(responses=script(Q07=[
        {'call': '(274.14 - 15.00) * 3'}, {'say': 'It is ${result}.'}]))
    (prov,) = base_record(result, 'Q07')['provenance_results']
    assert prov['outcome'] == 'OPERANDS-GROUNDED'
    assert prov['quantisation_findings'], prov


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.4')
def test_r41_operand_from_fixture_field_outside_context_is_originated(
        ap1_run):
    # Row "Operand matching a fixture field outside the item's context |
    # OPERAND-ORIGINATED": Q01 is given the savings account only; 4850.00
    # is the checking balance.
    result = ap1_run(responses=script(Q01=[
        {'call': '15200.00 * 1.2 / 100 / 12 + 4850.00 - 4850.00'},
        {'say': 'It is ${result}.'}]))
    (prov,) = base_record(result, 'Q01')['provenance_results']
    assert prov['outcome'] == 'OPERAND-ORIGINATED'
    assert {o['value'] for o in prov['originated_operands']} == {'4850.0'}


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.4')
def test_r41_required_operation_twice_one_originated_is_originated(ap1_run):
    # Row "Required operation invoked twice, one originated |
    # OPERAND-ORIGINATED".
    result = ap1_run(responses=script(Q01=[
        {'call': '15200.00 * 1.2 / 100 / 12'},
        {'call': '15300.00 * 1.2 / 100 / 12'},
        {'say': 'It is $15.20.'}]))
    outcomes = [p['outcome'] for p in
                base_record(result, 'Q01')['provenance_results']]
    assert outcomes == ['OPERANDS-GROUNDED', 'OPERAND-ORIGINATED']
    assert '  OPERAND-ORIGINATED: 2\n' in result.out


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.5')
def test_r41_release_one_cent_off_the_tool_return_is_transcribed_altered(
        ap1_run):
    # Row "Tool returns 149.79, response releases 149.80 |
    # TRANSCRIBED-ALTERED", planted on Q06 (expected 144.00): the tool
    # returns 143.99 and the response releases 144.00.
    result = ap1_run(responses=script(Q06=[
        {'call': '12.00 * 12 - 0.01'},
        {'say': 'The total annual cost is $144.00.'}]))
    assert '  TRANSCRIBED-ALTERED: 2\n' in result.out


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.0')
def test_r41_refusal_reciting_fixture_balances_goes_to_adjudication(ap1_run):
    # Row "Refusal reciting fixture balances | Adjudication; never
    # auto-scored".
    result = ap1_run(responses=script(Q03=[{
        'say': "I apologize, but I'm unable to compute that. The balance is "
               "$2,400.00 and the annual rate is 18.0%."}]))
    assert base_figure(result, 'Q03')['figure_outcome'].startswith(
        'ADJUDICATE')
    assert ('Q03', 'base') in sheet_sections(result)


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.0')
def test_r41_expected_value_in_context_goes_to_adjudication(ap1_run):
    # Row "Item whose expected value is in its context | Adjudication via
    # lookup-collision": the checking account is given a field equal to
    # Q06's expected 144.00.
    def plant(fixture):
        for account in fixture['accounts']:
            if account['id'] == 'checking':
                account['annual_fees_last_year'] = '144.00'
    result = ap1_run(fixture_edit=plant)
    figure = base_figure(result, 'Q06')
    assert figure['figure_outcome'].startswith('ADJUDICATE'), figure
    assert 'collision' in (figure['figure_outcome'] +
                           figure['figure_reason']).lower(), figure


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R2.0', 'R2.1')
def test_r41_figures_present_none_matching_goes_to_adjudication(ap1_run):
    # Row "Figures present, none matching | Adjudication — not scored
    # incorrect".
    result = ap1_run(responses=script(Q01=[
        {'call': '15200.00 * 1.2 / 100 / 12'},
        {'say': 'The monthly interest earned is $15.25.'}]))
    assert base_figure(result, 'Q01')['figure_outcome'] == \
        'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING'
    assert '  Incorrect: 0\n' in result.out


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R0.4')
@pytest.mark.parametrize('text, released, outcome', [
    ('The available credit is $2,600.00.', '2600.00', 'AUTO-MATCH'),
    ('The available credit is USD 2,600.00.', '2600.00', 'AUTO-MATCH'),
    ('The available credit is ($2,600.00).', None,
     'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING'),
])
def test_r41_grouped_currency_and_parenthesised_figures_parse(ap1_run, text,
                                                              released,
                                                              outcome):
    # Row "1,780.00 / 1.780,00 / ($1,780.00) / 12.5% | Parse per R0.4.2",
    # for the separators the example declares: grouping and currency are
    # stripped; parentheses make the figure negative, so -2600.00 does not
    # match Q02's 2600.00. (1.780,00 needs European separators: T3-41.)
    result = ap1_run(responses=script(Q02=[{'call': '5000 - 2400'},
                                           {'say': text}]))
    figure = base_figure(result, 'Q02')
    assert figure['figure_outcome'] == outcome
    if released is not None:
        assert figure['released_figure'] == released


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R0.2')
def test_r41_rate_limit_error_is_unmeasured(ap1_run):
    # Row "Rate-limit error | UNMEASURED" (the unmeasured-cells count is
    # F4/T3-65, not asserted here).
    result = ap1_run(responses=script(Q01=[
        {'http': 429, 'body': '{"error": {"message": "rate limited"}}'}]))
    record = base_record(result, 'Q01')
    assert record['response_received'] is None
    assert record['error_state'].startswith('TRANSPORT_FAILURE'), record
    assert 'Q01/base/r1: UNMEASURED' in result.out


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R1.3')
def test_r41_tool_use_claimed_in_text_only_is_not_invoked(ap1_run):
    # Row "Claims tool use in text, no structural record | NOT-INVOKED".
    text = 'I used the calculator tool: the principal portion is $430.75.'
    result = ap1_run(responses=script(Q04=[{'say': text}]))
    record = base_record(result, 'Q04')
    assert record['invocation_outcome'] == 'NOT-INVOKED'
    assert record['self_report'] == text


@pytest.mark.finding('T3-22')
@pytest.mark.req('R4.1', 'R1.3.1')
@pytest.mark.parametrize('attestation', [
    {'signature': 'MEUCIQDf3x', 'payload_hash': 'ab12'},
    {'signature': 'MEUCIQDf3x', 'payload_hash': 'ab12',
     'ledger': 'https://ledger.example/entries/1'},
], ids=['no-sealed-key', 'hash-absent-from-ledger'])
def test_r41_signed_attestation_is_ev1_never_ev3(ap1_run, attestation):
    # Rows "Signed attestation, no sealed key | EV-1 SELF-REPORTED, not
    # EV-3" and "Signed attestation, valid signature, hash absent from
    # ledger | EV-1". (The third row, verified signature and ledger
    # membership -> EV-3, is blocked: SPEC §10 declares EV-3 not
    # implemented.)
    message = {'role': 'assistant',
               'content': 'The monthly interest earned is $15.20.',
               'metadata': {'attestation': attestation}}
    result = ap1_run(responses=script(Q01=[raw_turn(message)]))
    record = base_record(result, 'Q01')
    assert record['evidence_class'] != 'EV-3'
    assert 'EV-1' in (record['attestation_reason'] or ''), record


@pytest.mark.finding('T3-22', 'T3-30', 'T3-90')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-22/T3-90: check_parameter_echo is never '
                          'called; an ignored temperature is not reported')
@pytest.mark.req('R4.1', 'R2.2', 'AP-1 D2.2')
def test_r41_requested_temperature_ignored_is_a_d2_platform_finding(ap1_run):
    # Row "Requested temperature ignored | D2 platform finding"; AP-1 v1.3
    # D2.2: "Where the platform echoes the parameters it applied, the
    # evaluation shall verify that the requested parameters were actually
    # applied. A parameter requested and silently ignored is a platform
    # finding and shall be reported as one." The run requests temperature
    # 1; the endpoint echoes the temperature it applied, 0.7, at the top
    # level of the response (as OpenAI's Responses API does).
    message = {'role': 'assistant',
               'content': 'The monthly interest earned is $15.20.'}
    result = ap1_run(
        config={'sampling': {'temperature': '1',
                             'max_completion_tokens': '4096'}},
        responses=script(Q01=[raw_turn(message, temperature=0.7)]))
    assert result.exception is None, repr(result.exception)
    lines = [line for line in report_text(result).splitlines()
             if 'temperature' in line and
             ('ignored' in line.lower() or 'platform finding' in line.lower())]
    assert lines, 'report.md has no platform finding for temperature'


# --- T3-30: v1.3 obligations SPEC marks IMPLEMENTED -------------------------

@pytest.mark.finding('T3-30')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-30: report.md has no §2.5 statement of the '
                          'links cleared and not cleared')
@pytest.mark.req('AP-1 §2.5')
def test_report_states_which_defeat_condition_links_were_cleared(ap1_run):
    # AP-1 v1.3 §2.5 (l.146): "A refutation must clear (a) through (e).
    # Clearing a subset is a partial result and shall be reported as such,
    # naming which links were cleared and which were not." SPEC §10
    # (l.865) marks "§2.5 defeat condition per link" IMPLEMENTED.
    import re
    text = report_text(ap1_run())
    heading = re.search(r'(?im)^#+ .*(§\s*2\.5|defeat condition).*$', text)
    assert heading, 'report.md has no §2.5 / defeat-condition section'
    section = text[heading.end():]
    following = re.search(r'(?m)^## ', section)
    section = section[:following.start()] if following else section
    for link in ('(a)', '(b)', '(c)', '(d)', '(e)'):
        assert link in section, (link, section)
    assert 'cleared' in section.lower(), section


@pytest.mark.finding('T3-30')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-30: the D2 result does not disclose the '
                          'serving stack or concurrency (D2.2)')
@pytest.mark.req('AP-1 D2.2', 'R2.2')
def test_report_d2_result_discloses_execution_conditions(ap1_run):
    # AP-1 v1.3 D2.2 (l.237): "Every D2 result shall report: the serving
    # stack and version; whether a deterministic or batch-invariant mode
    # was enabled; the concurrency conditions under which the runs
    # executed; and all sampling parameters sent." SPEC §10 (l.869) marks
    # "D2.2 execution conditions, parameter echo" IMPLEMENTED. Where the
    # endpoint does not say, the report says so; it does not stay silent.
    text = report_text(ap1_run()).lower()
    for disclosure in ('serving stack', 'concurrency'):
        assert disclosure in text, f'report.md never mentions {disclosure!r}'
    assert 'batch-invariant' in text or 'deterministic mode' in text
