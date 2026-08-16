"""AP-1 Inspect Scorer.

Imports evidence, provenance, provenance_classify, operation_correctness,
figure_id, and accuracy FROM THE RUNNER. Calls the runner's classifiers.
Returns Score with all AP-1 outcomes in metadata.

NO MEASUREMENT LOGIC IS IMPLEMENTED HERE.
"""

import json
import sys
import os

from inspect_ai.scorer import Score, Target, scorer, CORRECT, INCORRECT

# Ensure the runner modules are importable
_RUNNER_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_EXAMPLE_DIR = os.path.join(_RUNNER_DIR, 'example')
for p in [_RUNNER_DIR, _EXAMPLE_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

# Runner imports - every classification call goes here
from evidence import classify_invocation, check_ev3_guard, EV_0, EV_2
from figure_id import identify_figure, AUTO_MATCH
from context import check_lookup_collision
from accuracy import score_accuracy
from operation_correctness import classify_operation
from provenance_classify import classify_invocations_sequential


@scorer(metrics=[])
def ap1_scorer():
    """Score a single AP-1 sample using the runner's classifiers."""

    async def score(state, target: Target) -> Score:
        tool_calls = state.metadata.get('ap1_tool_calls', [])
        round_shapes = state.metadata.get('ap1_round_shapes', [])
        final_response = state.metadata.get('ap1_final_response', {})
        final_text = state.metadata.get('ap1_final_text', '')
        tools_offered = state.metadata.get('ap1_tools_offered', True)

        gt = state.metadata.get('ap1_ground_truth', {})
        ctx = state.metadata.get('ap1_context', {})
        config = state.metadata.get('ap1_config', {})
        required_operation = gt.get('required_operation', 'calculator')

        # -- Evidence & invocation --
        round_shapes_tuples = [
            (s[0], s[1]) if isinstance(s, (list, tuple)) else (s, '')
            for s in round_shapes
        ]
        ev_class, invocation_outcome, self_report = classify_invocation(
            final_response,
            tools_offered=tools_offered,
            accumulated_tool_calls=tool_calls,
            round_shapes=round_shapes_tuples,
            required_operation=required_operation,
        )
        check_ev3_guard(ev_class)

        # -- Figure identification & accuracy --
        expected = gt.get('final')
        expected_str = str(expected) if expected is not None else ''
        answer_tolerance = config.get('answer_tolerance', '0.01')

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

        # -- Operation correctness --
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
                        'reason': f'{type(e).__name__}: {e}',
                    })

        # -- Provenance --
        prov_results = classify_invocations_sequential(
            tool_calls, ctx, gt, config,
        )

        # -- Build Score --
        is_correct = (fig_result.get('outcome') == AUTO_MATCH)

        metadata = {
            'evidence_class': ev_class,
            'invocation_outcome': invocation_outcome,
            'self_report': self_report,
            'figure_outcome': fig_result.get('outcome'),
            'accuracy': acc_result,
            'operation_correctness': op_results,
            'provenance': prov_results,
            'item_id': gt.get('id', state.sample_id),
            'condition': state.metadata.get('ap1_condition', 'base'),
        }

        return Score(
            value=CORRECT if is_correct else INCORRECT,
            answer=str(fig_result.get('released_figure', '')),
            explanation=f'{ev_class}, {invocation_outcome or "N/A"}',
            metadata=metadata,
        )

    return score
