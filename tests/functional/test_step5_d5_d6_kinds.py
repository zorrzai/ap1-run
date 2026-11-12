"""Step 5, D5 and D6 kinds end to end (SPEC R0.1, R3.3): the shipped
example's inputs, copied to tmp_path, with D5 and D6 labels added to its
questions, run against the mock endpoint (one repeat, every item answered
in text). An undefined label is refused before the seal and before any
request; a set with labels runs, and its report gives the items per kind
and says "not a full AP-1 D5 result" (and D6) with the missing kinds.

A SPEC change proposed in step 5, so every test here is marked proposal.
"""

import json
import os
import shutil
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
FIXTURES = ROOT / 'tests' / 'fixtures'
KEY = 'sk-step5-not-a-real-key-0000'

pytestmark = [
    pytest.mark.proposal(
        'D5/D6 kinds: refusal of undefined labels at load, the per-kind '
        'counts and the "not a full AP-1 result" line are a SPEC R0.1/R3.3 '
        "change of the author's, for the maintainer"),
    pytest.mark.finding('T3-12'), pytest.mark.req('R0.1', 'R3.3')]

# Q01-Q05 carry D5 kinds (one defined, and no authority_spoof or
# tool_description_injection); Q06-Q09 carry four D6 kinds (no
# partial_receipt).
LABELS = {
    'Q01': ('adversarial_class', 'direct_override'),
    'Q02': ('adversarial_class', 'data_embedded_injection'),
    'Q03': ('adversarial_class', 'multi_turn_false_premise_persuasion'),
    'Q04': ('adversarial_class', 'control_plane_injection'),
    'Q05': ('adversarial_class', 'false_deadline'),
    'Q06': ('conflict_class', 'stale_source'),
    'Q07': ('conflict_class', 'internal_contradiction'),
    'Q08': ('conflict_class', 'cross_source_disagreement'),
    'Q09': ('conflict_class', 'out_of_range'),
}
DEFINED = {'false_deadline': 'A false deadline pressing for a quick figure'}


def _run(tmp, questions, older_loader=False):
    """Run the example with these questions; return (exit code, output
    directory, requests the mock received). older_loader stands for a
    runner from before undefined labels were refused: the run goes ahead
    and is sealed with them."""
    fixture_dir = tmp / 'inputs'
    shutil.copytree(EXAMPLE, fixture_dir,
                    ignore=shutil.ignore_patterns('__pycache__'))
    (fixture_dir / 'questions.json').write_text(
        json.dumps(questions, indent=2), 'utf-8')
    config = json.loads((EXAMPLE / 'config.json').read_text('utf-8'))
    config.update(repeat_count='1')
    config_path = tmp / 'config.json'
    config_path.write_text(json.dumps(config, indent=2), 'utf-8')
    output_dir = tmp / 'output'
    with pytest.MonkeyPatch.context() as mp:
        mp.syspath_prepend(str(FIXTURES))
        mp.setattr(sys, 'path', list(sys.path))
        mp.setattr(sys, 'dont_write_bytecode', True)
        for name in ('ground_truth_example', 'calculator_tool',
                     'mock_endpoint'):
            mp.delitem(sys.modules, name, raising=False)
        from mock_endpoint import MockEndpoint
        mock = MockEndpoint(
            api_key=KEY, questions=questions,
            system_prompts={config['system_prompt_base']: 'base',
                            config['system_prompt_instruction_removed']:
                                'instruction_removed'},
            responses={'*/*/*': [{'say': 'The answer is 1.00.'}]}).start()
        try:
            for name in list(os.environ):
                if name.startswith('AP1_SMOKE_'):
                    mp.delenv(name)
            mp.setenv('AP1_SMOKE_API_KEY', KEY)
            mock.point_config(config_path)
            mp.setattr(time, 'sleep', lambda seconds: None)
            from ap1_run import run as runner
            if older_loader:
                mp.setattr(runner, 'validate_kinds', lambda questions: None)
            try:
                code = runner.main(['--config', str(config_path),
                                    '--fixture-dir', str(fixture_dir),
                                    '--output-dir', str(output_dir)])
            except Exception as e:  # the refusal, returned for the test
                code = e
        finally:
            mock.stop()
            for name in ('ground_truth_example', 'calculator_tool'):
                sys.modules.pop(name, None)
    return code, output_dir, mock.log


def _labelled(**extra):
    questions = json.loads((EXAMPLE / 'questions.json').read_text('utf-8'))
    for item in questions['items']:
        if item['id'] in LABELS:
            field, label = LABELS[item['id']]
            item[field] = label
    questions.update(extra)
    return questions


@pytest.fixture(scope='module')
def kinds_report(tmp_path_factory):
    code, output_dir, _ = _run(tmp_path_factory.mktemp('kinds'),
                               _labelled(adversarial_classes=DEFINED))
    if code != 0:
        raise RuntimeError(f'the labelled run did not complete ({code!r})')
    return (output_dir / 'report.md').read_text('utf-8')


def test_run_undefined_label_refused_before_seal_and_requests(tmp_path):
    # Q05's defined kind is not defined here: the run is refused at load,
    # naming the item and the label, and nothing is sealed or sent.
    from ap1_run.foundation.config import ConfigError
    code, output_dir, log = _run(tmp_path, _labelled())
    assert isinstance(code, ConfigError), code
    assert str(code).startswith("item 'Q05': adversarial_class "
                                "'false_deadline' is not a D5 kind")
    assert log == []
    assert not (output_dir / 'pre_registration.json').exists()


def test_run_report_counts_per_kind_fixed_first_then_defined(kinds_report):
    s3 = kinds_report[kinds_report.index('## 3.'):]
    s3 = s3[:s3.index('\n## ', 1)]
    d5 = s3[s3.index('### D5 per Attack Kind'):s3.index('### D6 per')]
    names = [line.split('`')[1] for line in d5.splitlines()
             if line.startswith('| `')]
    assert names == ['direct_override', 'authority_spoof',
                     'data_embedded_injection',
                     'multi_turn_false_premise_persuasion',
                     'control_plane_injection', 'tool_description_injection',
                     'false_deadline']
    assert ('| `false_deadline` | defined | 1 | A false deadline pressing '
            'for a quick figure |') in d5
    assert '| `authority_spoof` | fixed | 0 |' in d5


def test_run_report_not_a_full_d5_or_d6_result_names_missing(kinds_report):
    lines = kinds_report.splitlines()
    d5 = [line for line in lines if 'not a full AP-1 D5 result' in line]
    d6 = [line for line in lines if 'not a full AP-1 D6 result' in line]
    assert len(d5) == 1 and len(d6) == 1, (d5, d6)
    assert ('`authority_spoof`, `tool_description_injection`' in d5[0]
            and 'false_deadline' not in d5[0]), d5
    assert '`partial_receipt`' in d6[0] and '`stale_source`' not in d6[0]


def test_rescore_of_older_run_lists_its_undefined_labels(tmp_path):
    # A run sealed before the loader refused undefined labels: Q05's
    # 'false_deadline' is not defined. Re-scored, the report counts it for
    # no kind and says so, with the label and its count; nothing is dropped
    # silently.
    code, output_dir, _ = _run(tmp_path, _labelled(), older_loader=True)
    assert code == 0, code
    with pytest.MonkeyPatch.context() as mp:
        mp.syspath_prepend(str(FIXTURES))
        mp.setattr(sys, 'path', list(sys.path))
        mp.setattr(sys, 'dont_write_bytecode', True)
        for name in ('ground_truth_example', 'calculator_tool'):
            mp.delitem(sys.modules, name, raising=False)
        from ap1_run.scoring.rescore import rescore_transcript
        try:
            rescore_transcript(
                output_dir / 'smoke_run.jsonl',
                config_path=tmp_path / 'config.json',
                fixture_dir=tmp_path / 'inputs',
                output_dir=tmp_path / 'rescored')
        finally:
            for name in ('ground_truth_example', 'calculator_tool'):
                sys.modules.pop(name, None)
    report = (tmp_path / 'rescored' / 'report.md').read_text('utf-8')
    lines = [line for line in report.splitlines()
             if 'labels naming no fixed or defined kind' in line]
    assert lines == [
        '**D5: labels naming no fixed or defined kind (counted for no '
        'kind):** `false_deadline` (1). The loader refuses such a label; '
        'this run was sealed without that check.'], lines
    d5 = report[report.index('### D5 per Attack Kind'):
                report.index('### D6 per')]
    counts = [int(line.split('|')[3]) for line in d5.splitlines()
              if line.startswith('| `')]
    assert sum(counts) + 1 == 5  # Q01-Q05: four counted, one listed
