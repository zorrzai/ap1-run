"""verify_inspect.py -- AP-1 Inspect wrapper agreement test.

GATES THE WRAPPER. Same fixture through both paths, assert identical
outcomes on every item and every dimension.

Test structure:
  test_shim_unit -- MockTC round-trip. Runs when wrapper is built.
      Tests shim field access. Does NOT require inspect-ai.
  test_inspect_wrapper_agrees_with_runner -- THE GATING TEST.
      REQUIRES inspect-ai. Uses real inspect_ai.tool.ToolCall objects.
      SKIPS with reason when inspect-ai is not importable.
  test_seal_refusal_on_wrong_hash -- Seal enforcement.
      Runs when wrapper is built.

FAILS naming the item and dimension on any disagreement.
"""

import json
import os
import sys
import unittest

_RUNNER_DIR = os.path.abspath(os.path.dirname(__file__))
_EXAMPLE_DIR = os.path.join(_RUNNER_DIR, 'example')
if _RUNNER_DIR not in sys.path:
    sys.path.insert(0, _RUNNER_DIR)
if _EXAMPLE_DIR not in sys.path:
    sys.path.insert(0, _EXAMPLE_DIR)

from evidence import classify_invocation, EV_0, EV_2
from operation_correctness import classify_operation
from provenance_classify import classify_invocations_sequential
from figure_id import identify_figure, AUTO_MATCH
from accuracy import score_accuracy
from context import build_delivered_context, check_lookup_collision
from transcription import check_transcription
from provenance_classify import _parse_return_value
import ground_truth_example as gt_module

WRAPPER_EXISTS = os.path.exists(
    os.path.join(_RUNNER_DIR, 'ap1_inspect', 'shim.py'))

try:
    import inspect_ai
    HAS_INSPECT = True
    INSPECT_VERSION = getattr(inspect_ai, '__version__', 'unknown')
except ImportError:
    HAS_INSPECT = False
    INSPECT_VERSION = None


def _build_mock_scenario(item_id, fixture, questions, config):
    """Build a mock scenario for one item."""
    question = next(q for q in questions if q['id'] == item_id)
    source_accounts = question.get('source_accounts', [])
    ctx = build_delivered_context(fixture, source_accounts)
    gt = gt_module.compute(item_id, ctx)

    if not gt.get('derivable', True):
        return None

    expected = gt['final']
    required_op = gt.get('required_operation', 'calculator')
    expr = gt.get('reference_expression', str(expected))

    tc_record = [{
        'turn': 1,
        'id': f'call_{item_id}_1',
        'type': 'function',
        'function': {
            'name': 'calculator',
            'arguments': json.dumps({'expression': expr}),
        },
    }]

    final_text = f'The answer is {expected}.'
    final_response = {
        'choices': [{
            'message': {
                'content': final_text,
                'role': 'assistant',
                'tool_calls': None,
            }
        }]
    }

    return {
        'gt': gt, 'ctx': ctx, 'config': config,
        'tool_calls': tc_record, 'final_text': final_text,
        'final_response': final_response,
        'required_operation': required_op,
        'expected': expected,
    }


def _build_chained_scenario(item_id, fixture, questions, config):
    """Build a scenario that chains tool calls, matching live run shape.

    Uses the ground-truth module's intermediates to build the exact
    sequence of calculator calls the derivation implies. Each call's
    return_value is attached in engine.py's shape: a JSON string like
    '{"result": "286063"}'.
    """
    import calculator_tool

    question = next(q for q in questions if q['id'] == item_id)
    source_accounts = question.get('source_accounts', [])
    ctx = build_delivered_context(fixture, source_accounts)
    gt = gt_module.compute(item_id, ctx)

    if not gt.get('derivable', True):
        return None

    expected = gt['final']
    required_op = gt.get('required_operation', 'calculator')

    # Build the derivation chain from intermediates
    intermediates = gt.get('intermediates', [])
    tc_records = []
    computed_values = {}  # label -> value

    for idx, inter in enumerate(intermediates):
        # Build expression from typed inputs
        parts = []
        for inp in inter.get('inputs', []):
            if 'source' in inp:
                # Direct source reference
                field_path = inp['source']
                acct_id, field_name = field_path.rsplit('.', 1)
                val = ctx.get(acct_id, {}).get(field_name)
                if val is not None:
                    parts.append(str(val))
            elif 'intermediate' in inp:
                label = inp['intermediate']
                val = computed_values.get(label)
                if val is not None:
                    parts.append(str(val))
            elif 'constant' in inp:
                parts.append(str(inp['constant']))

        if not parts:
            continue

        # Build expression based on operation
        operation = inter.get('operation', 'unknown')
        if operation == 'multiply':
            expr = ' * '.join(parts)
        elif operation == 'divide':
            expr = ' / '.join(parts)
        elif operation == 'subtract':
            expr = ' - '.join(parts)
        elif operation == 'add':
            expr = ' + '.join(parts)
        elif operation == 'multiply_then_divide':
            # a * b / c / d ... -- first two multiply, rest divide
            if len(parts) >= 2:
                expr = parts[0] + ' * ' + parts[1]
                for p in parts[2:]:
                    expr += ' / ' + p
            else:
                expr = parts[0]
        elif operation == 'sign_from_direction':
            # balance - min_payment + interest (direction-dependent)
            # Use the ground-truth value directly as the expression
            # result, since sign_from_direction is not a simple
            # arithmetic expression but depends on account direction.
            inter_val = inter.get('value')
            if inter_val is not None:
                expr = str(inter_val)
            else:
                expr = ' + '.join(parts)
        else:
            # Unknown operation -- fail loudly so it is not silently
            # skipped.
            raise ValueError(
                'unknown operation in chained scenario: '
                + repr(operation) + ' for ' + repr(inter.get('label')))

        # Execute to get return value
        try:
            result_val = calculator_tool.execute_calculator(expr)
            return_value = json.dumps({'result': result_val})
        except Exception:
            return_value = json.dumps({'error': f'failed: {expr}'})
            result_val = None

        turn = idx + 1
        tc_records.append({
            'turn': turn,
            'id': f'call_{item_id}_{turn}',
            'type': 'function',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps({'expression': expr}),
            },
            'return_value': return_value,
        })

        # Track computed value for chaining
        if result_val is not None:
            computed_values[inter['label']] = result_val

    if not tc_records:
        # Fall back to single-call
        return None

    final_text = f'The answer is {expected}.'
    final_response = {
        'choices': [{
            'message': {
                'content': final_text,
                'role': 'assistant',
                'tool_calls': None,
            }
        }]
    }

    return {
        'gt': gt, 'ctx': ctx, 'config': config,
        'tool_calls': tc_records, 'final_text': final_text,
        'final_response': final_response,
        'required_operation': required_op,
        'expected': expected,
        'call_count': len(tc_records),
    }



def _build_step4_scenarios(fixture, questions, config):
    """Build deliberate step-4 scenarios for agreement testing.

    These scenarios simulate model behaviour where a computed intermediate
    is quantised (rounded) before being reused in a subsequent call. The
    rounded value does not match the declared reference intermediate, so
    it misses step 3 and must resolve at step 4 (computed_in_session)
    through prior_returns.

    This is what live models do: they quantise, round, or take a different
    route. Run A produced 424 step-4 resolutions; the reference-derived
    chained scenarios produce near-zero because the values match the
    intermediates exactly.

    Returns a list of (label, scenario_dict) tuples.
    """
    from context import build_delivered_context

    scenarios = []

    # --- Scenario A: Q07-variant (quantised monthly_return) ---
    # Reference: monthly_return = 42175 * 7.8 / 100 / 12 = 274.1375
    # Model rounds to 274.14 before reusing.
    # 274.14 - 15 = 259.14 (not the declared intermediate 259.1375)
    # 259.14 * 3 = 777.42 (not the declared intermediate 777.4125)
    q07 = next(q for q in questions if q['id'] == 'Q07')
    ctx_q07 = build_delivered_context(fixture, q07.get('source_accounts', []))
    gt_q07 = gt_module.compute('Q07', ctx_q07)

    # Model truncates 274.1375 to 274.13 (drops last digit instead
    # of rounding). 274.13 misses the raw intermediate (274.1375)
    # AND its 2dp quantised form (274.14), so it cannot resolve at
    # step 3. It IS the prior return value, so it resolves at step 4.
    # Downstream: 274.13 - 15 = 259.13, 259.13 * 3 = 777.39 -- both
    # also miss step 3 and resolve at step 4.
    tc_q07 = [
        {
            'turn': 1,
            'id': 'call_Q07s4_1',
            'type': 'function',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps(
                    {'expression': '42175.00 * 7.8 / 100 / 12'}),
            },
            'return_value': json.dumps({'result': '274.13'}),
        },
        {
            'turn': 2,
            'id': 'call_Q07s4_2',
            'type': 'function',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps(
                    {'expression': '274.13 - 15.00'}),
            },
            'return_value': json.dumps({'result': '259.13'}),
        },
        {
            'turn': 3,
            'id': 'call_Q07s4_3',
            'type': 'function',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps(
                    {'expression': '259.13 * 3'}),
            },
            'return_value': json.dumps({'result': '777.39'}),
        },
    ]
    final_text_q07 = 'The answer is 777.39.'
    scenarios.append(('Q07_step4', {
        'gt': gt_q07, 'ctx': ctx_q07, 'config': config,
        'tool_calls': tc_q07,
        'final_text': final_text_q07,
        'final_response': {
            'choices': [{'message': {
                'content': final_text_q07,
                'role': 'assistant',
                'tool_calls': None,
            }}]},
        'required_operation': gt_q07.get('required_operation', 'calculator'),
        'expected': gt_q07['final'],
        'call_count': 3,
    }))

    # --- Scenario B: Q04-variant (quantised monthly_interest) ---
    # Reference: monthly_interest = 287500 * 4.20 / 100 / 12 = 1006.25
    # Model gets 1006.25 (exact), principal = 1437 - 1006.25 = 430.75.
    # But 430.75 IS the declared intermediate. So: use a DIFFERENT
    # rounding: model uses 1006.3 instead of 1006.25.
    # 1437 - 1006.3 = 430.7 (not 430.75 declared intermediate)
    # 430.7 resolves at step 4 (matches prior return of 1006.3? no,
    # but we need TWO calls where the SECOND uses the FIRST's return).
    # Actually: 1006.3 itself in call[1] is not an intermediate either
    # (intermediate is 1006.25). And 1006.3 matches call[0]'s return.
    # So call[1] operand 1006.3 -> step 4.
    q04 = next(q for q in questions if q['id'] == 'Q04')
    ctx_q04 = build_delivered_context(fixture, q04.get('source_accounts', []))
    gt_q04 = gt_module.compute('Q04', ctx_q04)

    tc_q04 = [
        {
            'turn': 1,
            'id': 'call_Q04s4_1',
            'type': 'function',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps(
                    {'expression': '287500 * 4.20 / 100 / 12'}),
            },
            'return_value': json.dumps({'result': '1006.3'}),
        },
        {
            'turn': 2,
            'id': 'call_Q04s4_2',
            'type': 'function',
            'function': {
                'name': 'calculator',
                'arguments': json.dumps(
                    {'expression': '1437 - 1006.3'}),
            },
            'return_value': json.dumps({'result': '430.7'}),
        },
    ]
    final_text_q04 = 'The answer is 430.7.'
    scenarios.append(('Q04_step4', {
        'gt': gt_q04, 'ctx': ctx_q04, 'config': config,
        'tool_calls': tc_q04,
        'final_text': final_text_q04,
        'final_response': {
            'choices': [{'message': {
                'content': final_text_q04,
                'role': 'assistant',
                'tool_calls': None,
            }}]},
        'required_operation': gt_q04.get('required_operation', 'calculator'),
        'expected': gt_q04['final'],
        'call_count': 2,
    }))

    return scenarios


def _classify(scenario, tool_calls, final_response):
    """Run all runner classifiers on the given inputs."""
    gt = scenario['gt']
    ctx = scenario['ctx']
    config = scenario['config']
    required_op = scenario['required_operation']
    expected = scenario['expected']
    answer_tolerance = config.get('answer_tolerance', '0.01')

    round_shapes = [(True, 'structural response')]
    ev_class, inv_outcome, self_report = classify_invocation(
        final_response, tools_offered=True,
        accumulated_tool_calls=tool_calls,
        round_shapes=round_shapes,
        required_operation=required_op,
    )

    collision, _ = check_lookup_collision(expected, ctx)
    fig_result = identify_figure(
        final_response,
        expected_value=expected,
        delivered_context=ctx,
        lookup_collision=collision,
        answer_tolerance=answer_tolerance,
    )

    acc_result = score_accuracy(
        fig_result,
        expected_value=expected,
        answer_tolerance=answer_tolerance,
        quantisation_digits=int(
            config.get('quantisation', {}).get('places', 2)),
    )

    op_results = []
    for tc in tool_calls:
        func = tc.get('function', {})
        if func.get('name') == 'calculator':
            try:
                args = json.loads(func.get('arguments', '{}'))
                expr = args.get('expression')
                if expr:
                    oc = classify_operation(expr, gt, config)
                    op_results.append(oc)
            except Exception as e:
                op_results.append({
                    'outcome': 'OPERATION-UNOBSERVABLE',
                    'reason': str(e),
                })

    prov_results = classify_invocations_sequential(
        tool_calls, ctx, gt, config)

    # D7.3: transcription — compare tool return against released figure
    transcription_result = None
    if tool_calls:
        last_calc = None
        for tc in reversed(tool_calls):
            if tc.get('function', {}).get('name') == 'calculator':
                last_calc = tc
                break
        if last_calc is not None:
            tool_return_val = _parse_return_value(
                last_calc.get('return_value'))
            released = fig_result.get('released_figure')
            transcription_result = check_transcription(
                tool_return_val, released,
                figure_outcome=fig_result.get('outcome'),
                quantisation_digits=int(
                    config.get('quantisation', {}).get('places', 2)),
            )

    return {
        'evidence_class': ev_class,
        'invocation_outcome': inv_outcome,
        'figure_outcome': fig_result.get('outcome'),
        'accuracy_outcome': acc_result.get('outcome'),
        'operation_correctness': op_results,
        'provenance': prov_results,
        'transcription': transcription_result,
    }


class TestInspectWrapperAgreement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from config import load_config
        cls.config = load_config(
            os.path.join(_EXAMPLE_DIR, 'config.json'))
        with open(os.path.join(_EXAMPLE_DIR, 'fixture.json'), 'r',
                  encoding='utf-8') as f:
            cls.fixture = json.load(f)
        with open(os.path.join(_EXAMPLE_DIR, 'questions.json'), 'r',
                  encoding='utf-8') as f:
            cls.questions = json.load(f)['items']

    def _compare(self, item_id, runner_r, other_r, path_name):
        for dim in ['evidence_class', 'invocation_outcome',
                    'figure_outcome', 'accuracy_outcome']:
            self.assertEqual(
                runner_r[dim], other_r[dim],
                f'DISAGREE on {item_id}/{dim}: '
                f'runner={runner_r[dim]}, {path_name}={other_r[dim]}')

        r_ops = runner_r.get('operation_correctness', [])
        o_ops = other_r.get('operation_correctness', [])
        self.assertEqual(len(r_ops), len(o_ops),
            f'DISAGREE on {item_id}/op_correctness count')
        for i, (r_op, o_op) in enumerate(zip(r_ops, o_ops)):
            self.assertEqual(
                r_op.get('outcome'), o_op.get('outcome'),
                f'DISAGREE on {item_id}/op_correctness[{i}]')

        r_prov = runner_r.get('provenance', {})
        o_prov = other_r.get('provenance', {})
        if isinstance(r_prov, dict) and isinstance(o_prov, dict):
            for key in sorted(set(list(r_prov.keys()) + list(o_prov.keys()))):
                if key.startswith('_'):
                    continue
                self.assertEqual(
                    r_prov.get(key), o_prov.get(key),
                    f'DISAGREE on {item_id}/provenance/{key}')

        # D7.3: transcription
        r_trans = runner_r.get('transcription')
        o_trans = other_r.get('transcription')
        if r_trans is not None or o_trans is not None:
            r_out = r_trans.get('outcome') if r_trans else None
            o_out = o_trans.get('outcome') if o_trans else None
            self.assertEqual(
                r_out, o_out,
                f'DISAGREE on {item_id}/transcription: '
                f'runner={r_out}, {path_name}={o_out}')

    # ------------------------------------------------------------------
    # Test 1: Shim unit test — MockTC objects, no inspect-ai required
    # ------------------------------------------------------------------
    @unittest.skipUnless(WRAPPER_EXISTS,
        'ap1_inspect wrapper not built -- skipping shim unit test')
    def test_shim_unit(self):
        """Shim field-access round-trip using MockTC objects.

        Does NOT require inspect-ai. Tests only that the shim's
        inspect_tc_to_runner function correctly maps field names.
        This is a unit test of the shim, not an agreement test.
        """
        from ap1_inspect.shim import inspect_tc_to_runner

        tc = {'turn': 1, 'id': 'call_1', 'type': 'function',
              'function': {'name': 'calculator',
                           'arguments': '{"expression": "1+1"}'}}

        class MockTC:
            id = 'call_1'
            function = 'calculator'
            arguments = {'expression': '1+1'}
            type = 'function'

        result = inspect_tc_to_runner(MockTC(), turn=1)
        self.assertEqual(result['id'], tc['id'])
        self.assertEqual(result['function']['name'],
                         tc['function']['name'])
        self.assertEqual(
            json.loads(result['function']['arguments']),
            json.loads(tc['function']['arguments']))

    # ------------------------------------------------------------------
    # Test 2: Agreement test — REQUIRES inspect-ai
    # ------------------------------------------------------------------
    @unittest.skipUnless(WRAPPER_EXISTS,
        'ap1_inspect wrapper not built -- skipping agreement test')
    @unittest.skipUnless(HAS_INSPECT,
        'inspect-ai is not installed -- agreement test requires '
        'inspect-ai to construct real ToolCall objects')
    def test_inspect_wrapper_agrees_with_runner(self):
        """Same fixture, both paths, identical outcomes on every
        item and every dimension.

        THE GATING TEST. Uses real inspect_ai.tool.ToolCall objects,
        not MockTC. If inspect-ai is absent, this test SKIPS.

        Chained scenarios (Q04, Q05, Q07, Q08, Q09, Q10) are derived
        from the ground-truth module's reference intermediates, not
        replayed from a live run. Both paths receive the same
        synthetic tool-call records. This tests that the two paths
        CLASSIFY identically given identical records; it does not
        reproduce the model's actual call sequence from any run.
        """
        from inspect_ai.tool import ToolCall
        from ap1_inspect.shim import inspect_tc_to_runner, build_final_response

        tested = 0
        for q in self.questions:
            item_id = q['id']
            scenario = _build_mock_scenario(
                item_id, self.fixture, self.questions, self.config)
            if scenario is None:
                continue

            # Try chained scenario first, fall back to single-call
            chained = _build_chained_scenario(
                item_id, self.fixture, self.questions, self.config)
            use_scenario = chained if chained else scenario

            # Path A: runner direct
            runner_r = _classify(
                use_scenario, use_scenario['tool_calls'],
                use_scenario['final_response'])

            # Path B: through real Inspect ToolCall objects
            shimmed = []
            for tc in use_scenario['tool_calls']:
                real_tc = ToolCall(
                    id=tc['id'],
                    function=tc['function']['name'],
                    arguments=json.loads(tc['function']['arguments']),
                    type=tc.get('type', 'function'),
                )
                shimmed.append(
                    inspect_tc_to_runner(
                        real_tc, turn=tc['turn'],
                        return_value=tc.get('return_value')))

            # Build final response via shim
            shim_response = build_final_response(
                use_scenario['final_text'], tool_calls_present=False)

            shim_r = _classify(use_scenario, shimmed, shim_response)

            self._compare(item_id, runner_r, shim_r, 'inspect')
            tested += 1

        # Deliberate step-4 scenarios: quantised intermediates that
        # miss step 3 and must resolve through prior_returns.
        step4_scenarios = _build_step4_scenarios(
            self.fixture, self.questions, self.config)
        for label, s4_scenario in step4_scenarios:
            # Path A: runner direct
            s4_runner = _classify(
                s4_scenario, s4_scenario['tool_calls'],
                s4_scenario['final_response'])

            # Path B: through real Inspect ToolCall objects
            s4_shimmed = []
            for tc in s4_scenario['tool_calls']:
                real_tc = ToolCall(
                    id=tc['id'],
                    function=tc['function']['name'],
                    arguments=json.loads(tc['function']['arguments']),
                    type=tc.get('type', 'function'),
                )
                s4_shimmed.append(
                    inspect_tc_to_runner(
                        real_tc, turn=tc['turn'],
                        return_value=tc.get('return_value')))

            s4_shim_response = build_final_response(
                s4_scenario['final_text'], tool_calls_present=False)
            s4_shim_r = _classify(
                s4_scenario, s4_shimmed, s4_shim_response)

            self._compare(label, s4_runner, s4_shim_r, 'inspect')
            tested += 1

        self.assertGreater(tested, 0,
            'No items tested -- fixture may be empty')

    # ------------------------------------------------------------------
    # Test 3: Seal enforcement
    # ------------------------------------------------------------------
    @unittest.skipUnless(WRAPPER_EXISTS,
        'ap1_inspect wrapper not built -- skipping seal test')
    def test_seal_refusal_on_wrong_hash(self):
        """Task with a wrong AP-1 text hash refuses to run."""
        from seal import seal as create_seal, SealError

        bad_config = dict(self.config)
        bad_config['ap1_text_hash'] = 'deadbeef' * 8

        spec_path = os.path.join(_RUNNER_DIR, 'SPEC.md')
        if not os.path.exists(spec_path):
            self.skipTest('SPEC.md not found')

        with self.assertRaises(SealError) as cm:
            create_seal(
                config=bad_config,
                fixture_path=os.path.join(_EXAMPLE_DIR, 'fixture.json'),
                questions_path=os.path.join(_EXAMPLE_DIR, 'questions.json'),
                ground_truth_path=os.path.join(
                    _EXAMPLE_DIR, 'ground_truth_example.py'),
                ap1_text_path=spec_path,
            )
        self.assertIn('mismatch', str(cm.exception).lower())


def run_tests():
    """Entry point for run_all_tests.py integration."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestInspectWrapperAgreement)
    # Run with verbosity=0 to suppress default unittest output
    import io
    runner = unittest.TextTestRunner(verbosity=0, stream=io.StringIO())
    result = runner.run(suite)

    failed = len(result.failures) + len(result.errors)
    skipped = len(result.skipped)
    passed = result.testsRun - failed - skipped

    print(f'{passed} passed, {failed} failed, {skipped} skipped')

    return result


if __name__ == '__main__':
    result = run_tests()
    failed = len(result.failures) + len(result.errors)
    raise SystemExit(1 if failed else 0)
