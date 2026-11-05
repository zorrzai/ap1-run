"""findings/FINDINGS.md is generated from the published run artifacts by
tools/generate_findings.py (from legacy verify_findings.py and
test_findings_mutation.py).

The published artifacts under output/ are read, never written: artifact
mutations are made on copies in tmp_path, with the generator's OUTPUT
pointed at them. (Legacy test_findings_mutation.py rewrote FINDINGS.md and
the sealed smoke_summary.json in place and restored them afterwards.)
End to end: regression scenario tool_generate_findings.
"""

import importlib.util
import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
FINDINGS = ROOT / 'findings' / 'FINDINGS.md'
ARTIFACTS = ['run_a_mini', 'run_b_sol', 'superseded/run_b_sol_pre_restructure']

missing = [a for a in ARTIFACTS
           if not (ROOT / 'output' / a / 'smoke_summary.json').exists()]
pytestmark = pytest.mark.skipif(
    bool(missing), reason=f'run artifacts not found: {missing}')


@pytest.fixture(scope='module')
def generator():
    spec = importlib.util.spec_from_file_location(
        'generate_findings', ROOT / 'tools' / 'generate_findings.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope='module')
def figures(generator):
    return generator.compute_figures()


@pytest.fixture(scope='module')
def committed():
    return FINDINGS.read_text(encoding='utf-8')


@pytest.fixture
def mutated_figures(generator, tmp_path, monkeypatch):
    """compute_figures() over copies of the artifacts, one of them
    changed by mutate(data)."""
    for rel in ARTIFACTS:
        (tmp_path / rel).mkdir(parents=True)
        shutil.copy(ROOT / 'output' / rel / 'smoke_summary.json',
                    tmp_path / rel / 'smoke_summary.json')

    def compute(rel, mutate):
        path = tmp_path / rel / 'smoke_summary.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        mutate(data)
        path.write_text(json.dumps(data), encoding='utf-8')
        monkeypatch.setattr(generator, 'OUTPUT', str(tmp_path))
        return generator.compute_figures()
    return compute


def changed_keys(before, after):
    return sorted(k for k in set(before) | set(after)
                  if before.get(k) != after.get(k))


# -- verify_findings -------------------------------------------------------

def test_committed_findings_equal_generation_from_artifacts(generator,
                                                            figures,
                                                            committed):
    assert generator.generate(figures) == committed


def test_artifacts_the_findings_cite_are_tracked_by_git():
    inside = subprocess.run(['git', 'rev-parse', '--git-dir'], cwd=ROOT,
                            capture_output=True).returncode == 0
    if not inside:
        pytest.skip('not a git working tree')
    for rel in ARTIFACTS:
        path = f'output/{rel}/smoke_summary.json'
        assert subprocess.run(['git', 'ls-files', '--error-unmatch', path],
                              cwd=ROOT, capture_output=True).returncode == 0


# -- test_findings_mutation: a changed document is detected ---------------

@pytest.mark.parametrize('old, new', [
    ('243 / 1,064', '999 / 1,064'),          # table figure
    ('62 sign-inversion findings', '99 sign-inversion findings'),  # prose
    ('22.8%', '33.3%'),                      # percentage
    ('524 of', '525 of'),                    # narrative figure
], ids=['table-figure-243', 'prose-figure-62-sign-inv', 'percentage-22.8',
        'narrative-figure-sup-524'])
def test_edited_figure_in_findings_differs_from_generation(generator, figures,
                                                           committed, old, new):
    edited = committed.replace(old, new, 1)
    assert edited != committed
    assert generator.generate(figures) != edited


# -- test_findings_mutation: a changed artifact changes the figures -------

def _not_invoked_to_invoked(data):
    for r in data['all_results']:
        if r['invocation_outcome'] == 'NOT-INVOKED':
            r['invocation_outcome'] = 'INVOKED'
            return


def _wrong_operation_to_correct(data):
    for r in data['all_results']:
        for op in r.get('operation_correctness', []):
            if op['outcome'] == 'WRONG-OPERATION':
                op['outcome'] = 'OPERATION-CORRECT'
                return


def _drop_one_sign_inversion(data):
    for r in data['all_results']:
        for p in r.get('provenance_results', []):
            for res in p.get('operand_resolutions', []):
                if res.get('sign_inversion_finding') not in (None, False):
                    res['sign_inversion_finding'] = None
                    return


@pytest.mark.parametrize('run, mutate, keys', [
    ('run_b_sol', _not_invoked_to_invoked,
     ['b_invoked_ir', 'b_ni_Q02', 'b_ni_pct', 'b_not_invoked_ir']),
    ('run_a_mini', _wrong_operation_to_correct,
     ['a_correct_ops', 'a_wo_adjudicated', 'a_wo_base', 'a_wo_base_pct',
      'a_wrong_ops']),
    ('run_a_mini', _drop_one_sign_inversion,
     ['a_excl_sign_originated', 'a_orig_item_Q09_sign_inv',
      'a_orig_item_Q09_untraceable', 'a_outcomes_sign_inv',
      'a_outcomes_untraceable', 'a_sign_inversions', 'a_untraceable',
      'combined_untraceable', 'f6_per_item_summary']),
], ids=['artifact-invocation-count', 'artifact-wrong-op-count',
        'artifact-sign-inv-count'])
def test_changed_artifact_changes_the_generated_findings(
        generator, figures, committed, mutated_figures, run, mutate, keys):
    after = mutated_figures(run, mutate)
    assert changed_keys(figures, after) == keys
    assert generator.generate(after) != committed


# -- F7 "0/468": the item-wrong count cannot be non-zero (T3-14) ----------

@pytest.mark.finding('T3-14')
def test_f7_counts_an_outcome_the_runner_never_emits(figures):
    # FINDINGS F7's "item answer incorrect" counts figure outcome
    # AUTO-MISMATCH, which figure identification never emits, so it is 0
    # by construction and the Clopper-Pearson bound measures a tautology.
    # Correct: count released figures that are wrong (after adjudication).
    for run in ('run_a_mini', 'run_b_sol'):
        data = json.loads((ROOT / 'output' / run / 'smoke_summary.json')
                          .read_text(encoding='utf-8'))
        outcomes = {r.get('figure_outcome') for r in data['all_results']}
        assert outcomes == {'AUTO-MATCH', 'ADJUDICATE-AMBIGUOUS',
                            'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING'}
    assert (figures['a_wo_item_wrong'], figures['a_wo_auto_wrong']) == (0, 0)
    assert figures['a_wo_item_wrong_cp'] == (
        '0/468 auto-scored (p_upper < 0.0064, 95% Clopper–Pearson)')
    assert figures['b_wo_item_wrong_cp'] == (
        '0/79 auto-scored (p_upper < 0.0372, 95% Clopper–Pearson)')


@pytest.mark.finding('T3-14')
def test_f7_item_wrong_count_stays_zero_when_a_figure_stops_matching(
        figures, mutated_figures):
    # An auto-matched WRONG-OPERATION result whose figure no longer
    # matches moves out of the auto-scored set; the "wrong" count stays 0.
    def unmatch(data):
        for r in data['all_results']:
            if r.get('figure_outcome') == 'AUTO-MATCH' and any(
                    op['outcome'] == 'WRONG-OPERATION'
                    for op in r.get('operation_correctness', [])):
                r['figure_outcome'] = 'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING'
                return
    after = mutated_figures('run_a_mini', unmatch)
    assert (after['a_wo_item_wrong'], after['a_wo_auto_wrong']) == (0, 0)
    assert after['a_wo_auto_scored'] < figures['a_wo_auto_scored']
