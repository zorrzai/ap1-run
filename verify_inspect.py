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

    return {
        'evidence_class': ev_class,
        'invocation_outcome': inv_outcome,
        'figure_outcome': fig_result.get('outcome'),
        'accuracy_outcome': acc_result.get('outcome'),
        'operation_correctness': op_results,
        'provenance': prov_results,
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

            # Path A: runner direct
            runner_r = _classify(
                scenario, scenario['tool_calls'],
                scenario['final_response'])

            # Path B: through real Inspect ToolCall objects
            shimmed = []
            for tc in scenario['tool_calls']:
                real_tc = ToolCall(
                    id=tc['id'],
                    function=tc['function']['name'],
                    arguments=json.loads(tc['function']['arguments']),
                    type=tc.get('type', 'function'),
                )
                shimmed.append(
                    inspect_tc_to_runner(real_tc, turn=tc['turn']))

            # Build final response via shim
            shim_response = build_final_response(
                scenario['final_text'], tool_calls_present=False)

            shim_r = _classify(scenario, shimmed, shim_response)

            self._compare(item_id, runner_r, shim_r, 'inspect')
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
