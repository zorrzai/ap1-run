"""ap1_inspect/scorer.py: one sample scored with the runner's classifiers
(from legacy verify_inspect.py test_multi_call_decomposition_all_oc, which
ran its own copy of this scorer, and the scoring half of
test_inspect_wrapper_agrees_with_runner).

Pins where the Inspect path diverges from the runner today (T3-43).
"""

import asyncio
import importlib.util
import json
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

import pytest

pytest.importorskip('inspect_ai')

from inspect_ai.scorer import CORRECT, INCORRECT, Target  # noqa: E402

from ap1_inspect.scorer import ap1_scorer  # noqa: E402
from ap1_inspect.shim import build_final_response  # noqa: E402
from ap1_run.execution.context import build_delivered_context  # noqa: E402
from ap1_run.foundation.config import load_config  # noqa: E402
from ap1_run.foundation.numeric import extract_numeric_tokens  # noqa: E402
from ap1_run.scoring.figure_id import identify_figure  # noqa: E402

EXAMPLE = Path(__file__).resolve().parents[2] / 'example'


@pytest.fixture(scope='module')
def example():
    # The shipped module, loaded from its file under a private name: other
    # tests may leave a different module registered as ground_truth_example
    # in sys.modules (the runner registers the sealed one there).
    spec = importlib.util.spec_from_file_location(
        '_inspect_test_ground_truth', EXAMPLE / 'ground_truth_example.py')
    ground_truth_example = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ground_truth_example)
    config = load_config(EXAMPLE / 'config.json')
    fixture = json.loads((EXAMPLE / 'fixture.json').read_text('utf-8'))
    items = {q['id']: q for q in json.loads(
        (EXAMPLE / 'questions.json').read_text('utf-8'))['items']}

    def item(item_id):
        ctx = build_delivered_context(fixture, items[item_id]['source_accounts'])
        return ctx, ground_truth_example.compute(item_id, ctx)
    return SimpleNamespace(config=config, item=item)


def call(turn, expression, result):
    return {'turn': turn, 'id': f'c{turn}', 'type': 'function',
            'function': {'name': 'calculator',
                         'arguments': json.dumps({'expression': expression})},
            'return_value': json.dumps({'result': result})}


@pytest.fixture
def score(example):
    def run(text, tool_calls, item_id='Q01',
            shapes=((True, 'structural response'),)):
        ctx, gt = example.item(item_id)
        state = SimpleNamespace(sample_id=item_id, metadata={
            'ap1_tool_calls': list(tool_calls),
            'ap1_round_shapes': [list(s) for s in shapes],
            'ap1_final_response': build_final_response(
                text, tool_calls_present=False),
            'ap1_final_text': text, 'ap1_tools_offered': True,
            'ap1_ground_truth': gt, 'ap1_context': ctx,
            'ap1_config': example.config, 'ap1_condition': 'base'})
        return asyncio.run(ap1_scorer()(state, Target(str(gt['final']))))
    return run


Q01_CALL = [call(1, '15200.00 * 1.2 / 100 / 12', '15.20')]


def test_auto_match_scores_correct_with_runner_outcomes(score):
    s = score('The monthly interest is $15.20.', Q01_CALL)
    assert (s.value, s.answer, s.explanation) == \
        (CORRECT, '15.20', 'EV-2 PLATFORM-STRUCTURAL, INVOKED')
    assert sorted(s.metadata) == [
        'accuracy', 'condition', 'evidence_class', 'figure_outcome',
        'invocation_outcome', 'item_id', 'operation_correctness',
        'provenance', 'release_coverage', 'self_report']
    assert (s.metadata['figure_outcome'], s.metadata['item_id'],
            s.metadata['condition']) == ('AUTO-MATCH', 'Q01', 'base')
    assert [p['outcome'] for p in s.metadata['provenance']] == \
        ['OPERANDS-GROUNDED']


def test_unrecognised_round_gives_ev0_without_outcome(score):
    s = score('The monthly interest is $15.20.', Q01_CALL,
              shapes=[(False, 'no matching response')])
    assert (s.metadata['evidence_class'], s.metadata['invocation_outcome'],
            s.explanation) == ('EV-0 UNOBSERVABLE', None,
                               'EV-0 UNOBSERVABLE, N/A')


def test_three_call_decomposition_is_operation_correct_after_session_rule(
        score, example):
    # Calls 1 and 2 produce values absent from the reference
    # intermediates; reclassify_session makes all three correct.
    import calculator_tool
    exprs = ['42175 * 7.8 / 100 / 4', '15 * 3', '822.4125 - 45']
    calls = [call(i + 1, e, calculator_tool.execute_calculator(e))
             for i, e in enumerate(exprs)]
    _, gt = example.item('Q07')
    s = score(f'The answer is {gt["final"]}.', calls, item_id='Q07')
    assert [o['outcome'] for o in s.metadata['operation_correctness']] == \
        ['OPERATION-CORRECT'] * 3


@pytest.mark.finding('T3-43')
def test_decline_without_figures_is_auto_no_figure_not_decline(score,
                                                               example):
    # The scorer passes no decline markers to identify_figure, so a decline
    # the runner routes to adjudication is auto-scored NO-FIGURE here.
    # Correct: the config's decline markers, as the runner uses them.
    text = 'I cannot determine that.'
    s = score(text, Q01_CALL)
    assert (s.value, s.metadata['figure_outcome']) == \
        (INCORRECT, 'AUTO-NO-FIGURE')
    ctx, gt = example.item('Q01')
    runner = identify_figure(
        build_final_response(text, tool_calls_present=False),
        expected_value=gt['final'], delivered_context=ctx,
        lookup_collision=False,
        answer_tolerance=example.config['answer_tolerance'],
        decline_markers=example.config['decline_markers'],
        currency_symbols=example.config['currency_symbols'],
        extract_tokens_fn=extract_numeric_tokens)
    assert runner['outcome'] == 'ADJUDICATE-DECLINE'


@pytest.mark.finding('T3-43')
def test_adjudication_routed_response_is_logged_incorrect(score):
    # Correct only on AUTO-MATCH: a response the runner sends to a human
    # (here ambiguous) is scored INCORRECT. Correct: unscored until
    # adjudicated.
    s = score('It is 15.20 or 15.20.', Q01_CALL)
    assert (s.value, s.answer, s.metadata['figure_outcome']) == \
        (INCORRECT, 'None', 'ADJUDICATE-AMBIGUOUS')


@pytest.mark.finding('T3-43')
def test_transcription_is_not_checked(score):
    # The tool returned 15.21 and the response released 15.20: the runner
    # records TRANSCRIBED-ALTERED (D7.3); the scorer has no transcription
    # result at all. Correct: call check_transcription as the runner does.
    s = score('The monthly interest is $15.20.',
              [call(1, '15200.00 * 1.2 / 100 / 12', '15.21')])
    assert s.value == CORRECT
    assert 'transcription' not in s.metadata


@pytest.mark.finding('S3-G7-3')
def test_scorer_registers_no_metrics():
    # The custom metrics (clopper_pearson_zero_bound, invocation_rate)
    # exist but ap1_scorer is declared with metrics=[], so an eval never
    # computes them. Correct: attach them, or remove them.
    from inspect_ai._util.registry import registry_info
    assert registry_info(ap1_scorer).metadata.get('metrics') == []


def test_answer_is_the_released_figure_as_text(score):
    s = score('The monthly interest is $15.200.', Q01_CALL)
    assert s.answer == str(Decimal('15.200'))


# --- Step 4: correct behaviour (failing until fixed) ---

@pytest.mark.finding('S3-G7-3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='S3-G7-3: ap1_scorer is declared with metrics=[]; '
                          'the metrics in ap1_inspect.metrics never run; '
                          'blocked: attach (exposes T3-43) or remove is '
                          "Steven's call while Inspect is unsupported")
def test_scorer_attaches_every_metric_the_package_defines():
    # The correct behaviour is either of the two in the step-3 pin:
    # attach the metrics, or remove them. Both satisfy "no metric is
    # defined and never computed". (Inspect is unsupported for now,
    # Marcus 2026-10-16; attaching them exposes T3-43's metric defects.)
    import ap1_inspect.metrics as metrics_module
    from inspect_ai._util.registry import is_registry_object, registry_info
    defined = {registry_info(obj).name
               for obj in vars(metrics_module).values()
               if callable(obj) and is_registry_object(obj, type='metric')}
    attached = {registry_info(m).name
                for m in registry_info(ap1_scorer).metadata.get('metrics', [])
                if is_registry_object(m)}
    assert defined <= attached, sorted(defined - attached)
