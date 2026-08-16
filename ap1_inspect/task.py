"""AP-1 Inspect Task definitions.

Two @task functions: ap1_base and ap1_instruction_removed.
Both load the fixture, create the seal, build the dataset.

R1.1: seal.seal() is called before any sample runs. If the AP-1 text
hash mismatches, it raises SealError and the task refuses to run.
"""

import json
import sys
import os

from inspect_ai import Task, task
from inspect_ai.dataset import Sample, MemoryDataset

# Ensure the runner modules are importable
_RUNNER_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_EXAMPLE_DIR = os.path.join(_RUNNER_DIR, 'example')
if _RUNNER_DIR not in sys.path:
    sys.path.insert(0, _RUNNER_DIR)
if _EXAMPLE_DIR not in sys.path:
    sys.path.insert(0, _EXAMPLE_DIR)

from seal import seal as create_seal, SealError
from config import load_config
from context import build_delivered_context, format_fixture_context
import ground_truth_example as gt_module

from .solver import ap1_solver
from .scorer import ap1_scorer


def _load_fixture(config_path=None):
    """Load fixture, questions, and config."""
    if config_path is None:
        config_path = os.path.join(_EXAMPLE_DIR, 'config.json')
    config = load_config(config_path)

    fixture_path = os.path.join(_EXAMPLE_DIR, 'fixture.json')
    questions_path = os.path.join(_EXAMPLE_DIR, 'questions.json')
    gt_path = os.path.join(_EXAMPLE_DIR, 'ground_truth_example.py')

    with open(fixture_path, 'r', encoding='utf-8') as f:
        fixture = json.load(f)
    with open(questions_path, 'r', encoding='utf-8') as f:
        questions_data = json.load(f)
    questions = questions_data['items']

    return config, fixture, questions, fixture_path, questions_path, gt_path


def _create_seal(config, fixture_path, questions_path, gt_path):
    """Create the pre-registration seal. R1.1.

    Raises SealError if the AP-1 text hash mismatches.
    """
    ap1_text_path = None
    spec_path = os.path.join(_RUNNER_DIR, 'SPEC.md')
    if os.path.exists(spec_path):
        ap1_text_path = spec_path

    seal_record = create_seal(
        config=config,
        fixture_path=fixture_path,
        questions_path=questions_path,
        ground_truth_path=gt_path,
        ap1_text_path=ap1_text_path,
    )
    return seal_record


def _build_dataset(questions, fixture, config, *, condition):
    """Build an Inspect Dataset from the ground-truth questions."""
    samples = []
    for q in questions:
        item_id = q['id']
        source_accounts = q.get('source_accounts', [])
        ctx = build_delivered_context(fixture, source_accounts)
        gt = gt_module.compute(item_id, ctx)

        if not gt.get('derivable', True):
            continue

        context_text = format_fixture_context(fixture, q)
        prompt = f'{context_text}\n\nQuestion: {q["text"]}'

        samples.append(Sample(
            id=item_id,
            input=prompt,
            target=str(gt['final']),
            metadata={
                'ap1_ground_truth': gt,
                'ap1_context': ctx,
                'ap1_config': config,
                'ap1_condition': condition,
                'ap1_item_id': item_id,
            },
        ))

    return MemoryDataset(samples=samples)


def _build_tools():
    """Build the calculator tool definition for Inspect."""
    from inspect_ai.tool import tool

    @tool
    def calculator():
        """Evaluate a mathematical expression and return the result."""
        async def execute(expression: str) -> str:
            """Evaluate a mathematical expression.

            Args:
                expression: A mathematical expression to evaluate.
            """
            try:
                sys.path.insert(0, _EXAMPLE_DIR)
                import calculator_tool
                result = calculator_tool.execute_calculator(expression)
                return json.dumps({'result': result})
            except Exception as e:
                return json.dumps({'error': str(e)})
        return execute

    return [calculator()]


@task
def ap1_base(config_path=None):
    """AP-1 evaluation — base condition.

    Runs the standard AP-1 measurement with all tools available.
    """
    config, fixture, questions, fp, qp, gp = _load_fixture(config_path)
    _create_seal(config, fp, qp, gp)

    return Task(
        dataset=_build_dataset(questions, fixture, config, condition='base'),
        solver=ap1_solver(tools=_build_tools()),
        scorer=ap1_scorer(),
    )


@task
def ap1_instruction_removed(config_path=None):
    """AP-1 evaluation — instruction_removed condition (D7.1b).

    Same items, same tools, but with the calculator instruction
    removed from the system prompt. Measures whether the model
    invokes tools without being instructed to.
    """
    config, fixture, questions, fp, qp, gp = _load_fixture(config_path)
    _create_seal(config, fp, qp, gp)

    # The instruction_removed condition uses the same dataset
    # but the solver will use a modified system prompt
    return Task(
        dataset=_build_dataset(
            questions, fixture, config, condition='instruction_removed'),
        solver=ap1_solver(tools=_build_tools()),
        scorer=ap1_scorer(),
    )
