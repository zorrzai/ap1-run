"""Cross-condition D7.1 comparison.

Post-processing over two eval logs: base vs instruction_removed.
This is NOT a native Inspect feature — it reads two completed logs
and computes the invocation difference.

Usage:
    python -m ap1_inspect.compare logs/base.eval logs/ir.eval
"""

import json
import math
import sys


def compare_conditions(base_scores, ir_scores):
    """Compare invocation rates between base and instruction_removed.

    Args:
        base_scores: list of score metadata dicts from base condition
        ir_scores: list of score metadata dicts from instruction_removed

    Returns:
        dict with comparison results
    """
    def invocation_count(scores):
        invoked = sum(
            1 for s in scores
            if s.get('invocation_outcome') == 'INVOKED'
        )
        total = len(scores)
        return invoked, total

    base_inv, base_n = invocation_count(base_scores)
    ir_inv, ir_n = invocation_count(ir_scores)

    base_rate = base_inv / base_n if base_n else float('nan')
    ir_rate = ir_inv / ir_n if ir_n else float('nan')

    # Clopper-Pearson bound for each
    alpha = 0.05
    base_bound = 1.0 - math.pow(alpha, 1.0 / base_n) if base_n else float('nan')
    ir_bound = 1.0 - math.pow(alpha, 1.0 / ir_n) if ir_n else float('nan')

    return {
        'base': {
            'invoked': base_inv, 'total': base_n,
            'rate': base_rate, 'cp_bound': base_bound,
        },
        'instruction_removed': {
            'invoked': ir_inv, 'total': ir_n,
            'rate': ir_rate, 'cp_bound': ir_bound,
        },
        'rate_difference': ir_rate - base_rate,
        'finding': (
            'D7.1b: instruction-removed invocation rate '
            f'({ir_rate:.1%}) exceeds base rate ({base_rate:.1%})'
            if ir_rate > base_rate else
            'D7.1b: no excess invocation under instruction removal'
        ),
    }


def main():
    """CLI entry point: compare two eval log files."""
    if len(sys.argv) < 3:
        print('Usage: python -m ap1_inspect.compare <base.eval> <ir.eval>')
        sys.exit(1)

    # Import here so the module can be imported without inspect-ai
    try:
        from inspect_ai.log import read_eval_log
    except ImportError:
        print('ERROR: inspect-ai is required for log comparison')
        sys.exit(1)

    base_log = read_eval_log(sys.argv[1])
    ir_log = read_eval_log(sys.argv[2])

    base_scores = [
        s.scores['ap1_scorer'].metadata
        for s in base_log.samples
        if s.scores and 'ap1_scorer' in s.scores
    ]
    ir_scores = [
        s.scores['ap1_scorer'].metadata
        for s in ir_log.samples
        if s.scores and 'ap1_scorer' in s.scores
    ]

    result = compare_conditions(base_scores, ir_scores)

    print('\n=== AP-1 Cross-Condition D7.1 Comparison ===\n')
    for cond in ('base', 'instruction_removed'):
        d = result[cond]
        print(f'  {cond}:')
        print(f'    invoked: {d["invoked"]}/{d["total"]} ({d["rate"]:.1%})')
        print(f'    Clopper-Pearson bound (k=0, alpha=0.05): {d["cp_bound"]:.4f}')
    print(f'\n  Rate difference: {result["rate_difference"]:.1%}')
    print(f'  {result["finding"]}')


if __name__ == '__main__':
    main()
