"""Step 4, group g3-seal-guards: end-to-end tests of the correct behaviour
of the seal-time ground-truth guards (SPEC R3.1) and the condition guard
(SPEC R1.2, AP-1 v1.3 D7.8). They fail on today's code and are marked
xfail(strict); see inbox/2026-10-20_step4-g3-seal-guards-report.md.

Each test runs the real runner (ap1_run.run.main) in-process against the
mock endpoint the regression scenarios use (tests/fixtures/
mock_endpoint.py), on a copy of example/ in tmp_path (--fixture-dir,
--config, --output-dir), trimmed to two items and one repeat. Nothing is
written under the repository.

A precondition that does not hold (an edit to the copied example that did
not apply) raises RuntimeError, not AssertionError, so it cannot be
mistaken for the expected failure.
"""

import json
import os
import re
import shutil
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from ap1_run import run

REPO = Path(__file__).resolve().parents[2]

pytestmark = pytest.mark.filterwarnings('ignore:VERSION file says')

# The model's answers: the base arm calls the calculator, the
# instruction_removed arm answers from the context without it.
TOOL_IN_BASE_ONLY = {
    'Q01/base/*': [{'call': '15200.00 * 1.2 / 100 / 12'},
                   {'say': 'The monthly interest is ${result}.'}],
    'Q02/base/*': [{'call': '5000 - 2400'},
                   {'say': 'The available credit is ${result}.'}],
    'Q01/instruction_removed/*': [{'say': 'The monthly interest is $15.20.'}],
    'Q02/instruction_removed/*': [{'say': 'The available credit is $2600.00.'}],
}
# Neither arm calls the calculator: I_base is zero.
TOOL_IN_NEITHER = {
    'Q01/*/*': [{'say': 'The monthly interest is $15.20.'}],
    'Q02/*/*': [{'say': 'The available credit is $2600.00.'}],
}


@pytest.fixture
def fx(tmp_path, monkeypatch):
    """A copy of example/ with two items and one repeat; sys.path and the
    ground_truth_example module restored afterwards."""
    path = tmp_path / 'example'
    shutil.copytree(REPO / 'example', path)
    questions = json.loads((path / 'questions.json').read_text('utf-8'))
    questions['items'] = questions['items'][:2]
    (path / 'questions.json').write_text(json.dumps(questions), 'utf-8')
    edit_config(path, repeat_count='1')
    monkeypatch.setattr(sys, 'path', list(sys.path))
    saved = sys.modules.pop('ground_truth_example', None)
    yield path
    sys.modules.pop('ground_truth_example', None)
    if saved is not None:
        sys.modules['ground_truth_example'] = saved


def edit_config(path, **changes):
    config = json.loads((path / 'config.json').read_text('utf-8'))
    config.update(changes)
    (path / 'config.json').write_text(json.dumps(config), 'utf-8')


def edit_ground_truth(path, old=None, new=None, within=None, append=''):
    """Change the copied ground-truth module: replace `old` by `new`
    (exactly once, inside the function `within` if given) and/or append
    source at the end."""
    gt = path / 'ground_truth_example.py'
    text = gt.read_text('utf-8')
    if old is not None:
        start = text.index(f'def {within}(') if within else 0
        end = text.find('\ndef ', start + 1) if within else len(text)
        end = len(text) if end < 0 else end
        part = text[start:end]
        if part.count(old) != 1:
            raise RuntimeError(f'ground-truth edit did not apply: {old!r}')
        text = text[:start] + part.replace(old, new) + text[end:]
    gt.write_text(text + append, 'utf-8')


def run_example(path, tmp_path, monkeypatch, capsys,
                responses=TOOL_IN_BASE_ONLY):
    """Run the runner on the copied example; return the exit code, the
    exception (if any), the console, the mock's request log and the
    output directory."""
    sys.path.insert(0, str(REPO / 'tests' / 'fixtures'))
    from mock_endpoint import MockEndpoint
    questions = json.loads((path / 'questions.json').read_text('utf-8'))
    config = json.loads((path / 'config.json').read_text('utf-8'))
    prompts = {config['system_prompt_instruction_removed']:
               'instruction_removed',
               config['system_prompt_base']: 'base'}
    mock = MockEndpoint(questions=questions, system_prompts=prompts,
                        responses=responses).start()
    for name in list(os.environ):
        if name.startswith('AP1_SMOKE_'):
            monkeypatch.delenv(name)
    monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-test')
    monkeypatch.setenv('AP1_SMOKE_ENDPOINT', mock.url)
    monkeypatch.setenv('AP1_SMOKE_MODEL', 'mock-model')
    monkeypatch.setattr(run.time, 'sleep', lambda s: None)
    out = tmp_path / 'out'
    code, error = None, None
    try:
        code = run.main(['--config', str(path / 'config.json'),
                         '--fixture-dir', str(path),
                         '--output-dir', str(out)])
    except Exception as exc:  # a refusal is an exception today (SealError)
        error = exc
    finally:
        mock.stop()
    console = capsys.readouterr().out
    return SimpleNamespace(code=code, error=error, console=console,
                           log=mock.log, out=out,
                           text=console + (f'\n{type(error).__name__}: '
                                           f'{error}' if error else ''))


def assert_refused_before_any_request(result):
    """Refused: no request reached the endpoint, and the run ended with an
    exception or a non-zero exit code."""
    assert len(result.log) == 0, (
        f'{len(result.log)} requests were sent; the run was not refused')
    assert result.error is not None or result.code not in (0, None)


def report(result):
    """report.md of a completed run (RuntimeError if there is none, so a
    run that did not complete is not mistaken for the expected failure)."""
    path = result.out / 'report.md'
    if result.error is not None or not path.exists():
        raise RuntimeError(f'run did not complete: {result.error!r}')
    return path.read_text('utf-8')


# -- T3-7 / T3-8: the R3.1 ground-truth guards at seal time ----------------

CONSTANT_FINAL = '''

# Test edit: return a literal for every derivable item, whatever the
# context (the E3 defect class). The declarations are unchanged, so
# Q01 still declares savings.balance and savings.annual_rate.
_derived_compute = compute


def compute(item_id, delivered_context):
    out = dict(_derived_compute(item_id, delivered_context))
    if out.get('derivable', True):
        out['final'] = D('15.20')
    return out
'''


@pytest.mark.finding('T3-7')
@pytest.mark.req('R3.1', 'R1.1')
def test_run_constant_ground_truth_module_refused_before_any_request(
        fx, tmp_path, monkeypatch, capsys):
    # Correct (SPEC R3.1 l.686-694, "A constant-returning module is
    # refused, perturbation named"; phase-D gate l.797; README "the run is
    # refused"): at seal time the runner perturbs the declared fields, the
    # output does not move, and the run is refused before any request,
    # naming the perturbed field. Today the guards are not called: the
    # run seals the module and sends every request.
    edit_ground_truth(fx, append=CONSTANT_FINAL)
    result = run_example(fx, tmp_path, monkeypatch, capsys)
    assert_refused_before_any_request(result)
    assert re.search(r'savings\.(balance|annual_rate)', result.text)


@pytest.mark.finding('T3-8', 'T3-7')
@pytest.mark.req('R3.1', 'R1.1')
def test_run_undeclared_field_read_through_get_refused_before_any_request(
        fx, tmp_path, monkeypatch, capsys):
    # Correct (R3.1 via source_fields_check: "A module reading a field NOT
    # in source_fields_consumed is refused, with the field named"): Q01
    # declares savings.balance and savings.annual_rate, and its answer also
    # depends on savings.monthly_fee, read with .get(). The run is refused
    # at seal, naming savings.monthly_fee. Today it runs. This stays
    # failing if T3-7 is fixed (guards wired) without T3-8 (tracking only
    # sees subscripts).
    edit_ground_truth(fx, append='''

# Test edit: Q01 also depends on savings.monthly_fee, read with .get()
# and not declared.
_derived_compute = compute


def compute(item_id, delivered_context):
    out = dict(_derived_compute(item_id, delivered_context))
    if item_id == 'Q01':
        fee = delivered_context['savings'].get('monthly_fee')
        out['final'] = out['final'] - D(fee)
    return out
''')
    result = run_example(fx, tmp_path, monkeypatch, capsys)
    assert_refused_before_any_request(result)
    assert 'savings.monthly_fee' in result.text


@pytest.mark.finding('T3-7')
@pytest.mark.req('R3.1', 'R1.1')
def test_run_undeclared_constant_refused_before_any_request(
        fx, tmp_path, monkeypatch, capsys):
    # Correct (R3.1, the declared-constants check, the E3 defect class):
    # Q01 uses D("12") (months per year) but no longer declares it as a
    # constant. The run is refused at seal, naming the literal. Today the
    # check is not called and the run proceeds.
    edit_ground_truth(fx, old='''                    {"constant": "100"},
                    {"constant": "12"},''',
                      new='''                    {"constant": "100"},''',
                      within='derive_q01')
    result = run_example(fx, tmp_path, monkeypatch, capsys)
    assert_refused_before_any_request(result)
    assert 'D("12")' in result.text or "D('12')" in result.text


# -- T3-46: the condition guard, what is held constant, DPR -----------------

@pytest.mark.finding('T3-46')
@pytest.mark.req('R1.2', 'AP-1 D7.8')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-46: identical prompts pass the live guard and '
                          'both arms run as a contrast')
def test_run_identical_prompts_refused_before_any_request(
        fx, tmp_path, monkeypatch, capsys):
    # Correct (AP-1 v1.3 D7.8, "vary the instruction and nothing else";
    # SPEC R1.2 l.316-321): with identical prompts nothing is varied, so
    # there is no contrast to report; the run is refused before execution,
    # naming the system prompt. Today it prints "Perturbation guard:
    # PASSED" and runs both arms.
    config = json.loads((fx / 'config.json').read_text('utf-8'))
    edit_config(fx, system_prompt_instruction_removed=config[
        'system_prompt_base'])
    result = run_example(fx, tmp_path, monkeypatch, capsys)
    assert 'Perturbation guard: PASSED' not in result.console
    assert_refused_before_any_request(result)
    assert 'system_prompt' in result.text


@pytest.mark.finding('T3-46')
@pytest.mark.req('R1.2', 'AP-1 D7.8', 'AP-1 §13.9')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-46: the report never states what was held '
                          'constant between the conditions')
def test_run_report_states_what_was_held_constant(fx, tmp_path, monkeypatch,
                                                  capsys):
    # Correct (AP-1 v1.3 D7.8: "what is held constant shall be reported";
    # §13.9): report.md says what was held constant between base and
    # instruction_removed: at least the tool declarations, the sampling
    # parameters and the fixture (data). Today report.md has no such
    # statement.
    text = report(run_example(fx, tmp_path, monkeypatch, capsys))
    match = re.search(r'held constant', text, re.I)
    assert match, 'report.md does not say what was held constant'
    section = text[match.start():].split('\n#', 1)[0].lower()
    assert 'tool' in section and 'sampling' in section
    assert 'fixture' in section or 'data' in section


def dpr_lines(text):
    return [line for line in text.splitlines()
            if re.search(r'\bDPR\b|drop-in', line, re.I)]


@pytest.mark.finding('T3-46')
@pytest.mark.req('R2.3', 'AP-1 D7.8')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-46: DPR is never computed on a live run '
                          '(compute_dpr has no caller)')
def test_run_report_gives_dpr(fx, tmp_path, monkeypatch, capsys):
    # Correct (SPEC R2.3 l.546-547; AP-1 v1.3 D7.8): the report gives the
    # drop-in-performance ratio DPR = (I_base - I_removed) / I_base. Here
    # the base arm invokes on 2 of 2 and the removed arm on 0 of 2, so
    # DPR = 1, a 100 % drop. Today report.md has no DPR.
    text = report(run_example(fx, tmp_path, monkeypatch, capsys))
    lines = dpr_lines(text)
    assert lines, 'report.md has no DPR'
    assert any(re.search(r'\b100(\.0+)?\s*%|DPR\W+1(\.0+)?\b', line)
               for line in lines), lines


@pytest.mark.finding('T3-46')
@pytest.mark.req('R2.3', 'AP-1 D7.8')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-46: DPR is never computed on a live run, so a '
                          'zero base rate is never reported UNDEFINED')
def test_run_report_dpr_undefined_when_base_rate_zero(fx, tmp_path,
                                                      monkeypatch, capsys):
    # Correct (SPEC R2.3: "Where I_base is zero the ratio is UNDEFINED,
    # never 1.0"; AP-1 v1.3 D7.8 "shall be declared undefined"): neither
    # arm invokes the calculator, so the report gives DPR as UNDEFINED.
    # Today report.md has no DPR.
    text = report(run_example(fx, tmp_path, monkeypatch, capsys,
                              responses=TOOL_IN_NEITHER))
    lines = dpr_lines(text)
    assert lines, 'report.md has no DPR'
    assert any('UNDEFINED' in line for line in lines), lines
