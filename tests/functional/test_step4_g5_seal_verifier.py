"""Step 4, group g5 (seal and seal verifier): failing tests of the correct
behaviour where the defect is in the wiring, not in one function.

Each test drives the real runner (ap1_run.run.main) in this process against
the scripted mock endpoint the regression scenarios use
(tests/fixtures/mock_endpoint.py), with --config, --fixture-dir and
--output-dir under tmp_path, so nothing is written into the repository.
The fixture directory is a copy of example/, edited per test.

Unit-level tests for the same findings are in the step-4 sections of
tests/unit/execution/test_seal.py, test_version.py and
tests/unit/tools/test_verify_run_seal.py.
"""

import ast
import hashlib
import importlib.util
import json
import os
import platform
import re
import shutil
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from ap1_run import run as run_mod
from ap1_run.execution.seal import SealError

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
SRC = ROOT / 'src' / 'ap1_run'
CLEAN = json.loads((ROOT / 'tests' / 'regression' / 'scenarios' /
                    'clean.json').read_text(encoding='utf-8'))['responses']

# The AP-1 texts (shasum -a 256): v1.3 draft in reference/, v1.2 as
# published in zorrzai/admissibility-protocol (AP-1_Admissibility_Protocol_
# v1.2.md); v1.2 DOI from that repository's CITATION.cff.
V13_HASH = '48e7826fc7807880ab98694b394bd020da070fb1d9c212e383f7c70bd819cf56'
V12_HASH = '14659fc1c2a3357c22081a9109841475861c34f2b315ee7eb546e80fecbb58a5'
V12_DOI = '10.5281/zenodo.21324954'


def load_mock_endpoint():
    spec = importlib.util.spec_from_file_location(
        '_g5_mock_endpoint', ROOT / 'tests' / 'fixtures' / 'mock_endpoint.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.MockEndpoint


@pytest.fixture
def fixture_dir(tmp_path):
    """A copy of example/ to edit."""
    target = tmp_path / 'fixture'
    shutil.copytree(EXAMPLE, target,
                    ignore=shutil.ignore_patterns('__pycache__'))
    return target


@pytest.fixture
def runner(tmp_path, monkeypatch, capsys):
    """runner(fixture_dir, config=..., args=..., hooks=...) runs the real
    runner once and returns what it did: exit code, the SealError it
    raised (or None), the seal records it made, the console output and the
    output directory."""
    MockEndpoint = load_mock_endpoint()

    def go(fixture_dir, config=None, args=(), hooks=None):
        base = json.loads((EXAMPLE / 'config.json').read_text('utf-8'))
        # The shipped config claims D1 on 10 items, which minimum-n (R0.1)
        # refuses once wired (T3-12); claim only dimensions R0.1 sets no
        # minimum for, as tests/functional/test_step4_g9_spec_claims.py does.
        base.update({'repeat_count': '1', 'dimensions_claimed': ['D2', 'D7']},
                    **(config or {}))
        config_path = tmp_path / 'config.json'
        config_path.write_text(json.dumps(base, indent=2), encoding='utf-8')
        out = tmp_path / 'out'

        questions = json.loads(
            (Path(fixture_dir) / 'questions.json').read_text('utf-8'))
        mock = MockEndpoint(
            api_key='sk-g5-not-a-real-key-0000',
            questions=questions,
            system_prompts={base['system_prompt_base']: 'base',
                            base['system_prompt_instruction_removed']:
                                'instruction_removed'},
            responses=CLEAN).start()

        for name in list(os.environ):
            if name.startswith('AP1_SMOKE_'):
                monkeypatch.delenv(name)
        monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-g5-not-a-real-key-0000')
        monkeypatch.setenv('AP1_SMOKE_ENDPOINT', mock.url)
        monkeypatch.setenv('AP1_SMOKE_MODEL', 'mock-model')
        monkeypatch.setattr(run_mod.time, 'sleep', lambda seconds: None)
        # As the regression driver does: git fails, so the version check
        # is the same on every checkout (no "runner may be modified").
        monkeypatch.setenv('GIT_DIR', str(tmp_path / 'no-git'))
        # The runner puts the fixture directory on sys.path and imports
        # ground_truth_example and calculator_tool from it.
        monkeypatch.setattr(sys, 'path', list(sys.path))
        # No __pycache__ in the fixture directory (example/ for one test).
        monkeypatch.setattr(sys, 'dont_write_bytecode', True)
        for name in ('ground_truth_example', 'calculator_tool'):
            monkeypatch.delitem(sys.modules, name, raising=False)

        seals = []
        real_seal = run_mod.create_seal

        def observed_seal(**kwargs):
            record = real_seal(**kwargs)
            seals.append(record)
            if hooks and 'after_seal' in hooks:
                hooks['after_seal'](record)
            return record
        monkeypatch.setattr(run_mod, 'create_seal', observed_seal)
        if hooks and 'before_seal' in hooks:
            real_source_hash = run_mod.compute_runner_source_hash

            def source_hash_then_hook(base_dir):
                # Called after the inputs are loaded, before the seal.
                hooks['before_seal']()
                return real_source_hash(base_dir)
            monkeypatch.setattr(run_mod, 'compute_runner_source_hash',
                                source_hash_then_hook)

        refusal = code = None
        executed = {}
        try:
            code = run_mod.main(['--config', str(config_path),
                                 '--fixture-dir', str(fixture_dir),
                                 '--output-dir', str(out), *args])
        except SealError as e:
            refusal = e
        finally:
            mock.stop()
            module = sys.modules.get('ground_truth_example')
            executed['ground_truth'] = getattr(module, '__file__', None)
            for name in ('ground_truth_example', 'calculator_tool'):
                sys.modules.pop(name, None)
        return SimpleNamespace(code=code, refusal=refusal, seals=seals,
                               out=out, console=capsys.readouterr().out,
                               executed=executed)
    return go


def refused_naming(result, word):
    """True if the run was refused (SealError, or a non-zero exit) with a
    message that names `word`."""
    if result.refusal is not None:
        return word in str(result.refusal)
    return result.code not in (0, None) and word in result.console


def digests(data):
    """The SHA-256 of these bytes, raw and as T3-50's fix hashes text
    (LF line endings, no UTF-8 BOM): a sealed text hash is one of them."""
    text = data[3:] if data.startswith(b'\xef\xbb\xbf') else data
    text = text.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
    return {hashlib.sha256(data).hexdigest(), hashlib.sha256(text).hexdigest()}


def report_seal_record(out):
    """Section 1 of report.md, as the published-run verifier reads it."""
    record, inside = {}, False
    for line in (out / 'report.md').read_text('utf-8').splitlines():
        if line.startswith('## 1. Pre-Registration Record'):
            inside = True
            continue
        if inside and line.startswith('## '):
            break
        m = re.match(r'\|\s*`([^`]+)`\s*\|\s*`([^`]*)`\s*\|', line)
        if inside and m:
            record[m.group(1)] = m.group(2)
    return record


# -- T3-17: the seal is never re-verified ----------------------------------

@pytest.mark.finding('T3-17')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('name, word', [
    ('fixture.json', 'fixture'), ('questions.json', 'questions'),
    ('ground_truth_example.py', 'ground_truth')])
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-17: verify_seal is never called; a sealed input '
                          'changed after sealing goes unnoticed')
def test_run_sealed_input_changed_after_seal_refused_naming_it(
        runner, fixture_dir, name, word):
    # Correct (SPEC R1.1 verification item 1: "Modifying any sealed input
    # causes the scorer to refuse, naming the mismatch"; §9 threat
    # "Fixture altered after sealing"): the scorer re-verifies the seal
    # before it scores, and refuses, naming the input. Here the file is
    # changed on disk just after the seal is made (one byte appended).
    path = fixture_dir / name

    def tamper(record):
        with open(path, 'ab') as f:
            f.write(b'\n')
    result = runner(fixture_dir, hooks={'after_seal': tamper})
    assert result.seals, 'no seal was made'
    assert refused_naming(result, word), (
        'not refused: exit %r, refusal %r' % (result.code, result.refusal))


# -- T3-48: no expected-values component -----------------------------------

@pytest.mark.finding('T3-48')
@pytest.mark.req('R1.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-48: the seal has no expected-values component')
def test_run_seal_record_binds_expected_values(runner):
    # Correct (SPEC R1.1: "hash and timestamp the fixture, question set,
    # expected values, ground-truth module, ..."; AP-1 v1.3 §13.4): the
    # expected values are computed before the seal and hashed into it.
    # The field's name is the fix's choice (it contains 'expected'); its
    # value is a SHA-256 digest, and it is bound: editing it in report.md
    # makes the published-run verifier fail where it passed before. A
    # field added to the record but left out of the composite fails the
    # unedited check already. The run reads example/ in place, so the
    # verifier's fixed input paths match.
    result = runner(EXAMPLE)
    assert result.code == 0, result.console[-2000:]
    record = report_seal_record(result.out)
    fields = [k for k in record if 'expected' in k]
    assert len(fields) == 1, sorted(record)
    digest = record[fields[0]]
    assert re.fullmatch(r'[0-9a-f]{64}', digest), digest
    vrs = load_verifier()
    _, before = vrs.verify_run(str(result.out))
    report = result.out / 'report.md'
    report.write_text(report.read_text('utf-8').replace(digest, '0' * 64),
                      'utf-8')
    _, after = vrs.verify_run(str(result.out))
    new = {name for name, _ in after} - {name for name, _ in before}
    assert any('seal_hash' in n or 'expected' in n for n in new), \
        (before, after)


@pytest.mark.finding('T3-48')
@pytest.mark.req('R1.1', 'R3.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-48: a ground-truth module whose values change '
                          'between computations runs unnoticed')
def test_run_ground_truth_values_changing_between_computations_refused(
        runner, fixture_dir):
    # Correct (SPEC R3.1 "Intermediates reproducible across two
    # executions", in T3-48's Breaks; R1.1 expected values sealed): a
    # module that returns a different value when asked again for the same
    # item and context is caught before any request. Here every repeated
    # call (same item, same context) adds 1 to the final value. Today the
    # run computes expected values per execution, after the seal, and
    # scores the two conditions against different values.
    path = fixture_dir / 'ground_truth_example.py'
    path.write_text(path.read_text('utf-8') + (
        '\n\n_seen = {}\n_compute = compute\n\n\n'
        'def compute(item_id, delivered_context):\n'
        '    result = _compute(item_id, delivered_context)\n'
        '    key = (item_id, repr(sorted(delivered_context.items())))\n'
        '    _seen[key] = _seen.get(key, 0) + 1\n'
        '    if _seen[key] > 1:\n'
        '        result = dict(result, final=result["final"] + 1)\n'
        '    return result\n'), 'utf-8')
    result = runner(fixture_dir)
    refused = result.refusal is not None or result.code not in (0, None)
    assert refused, 'the run completed: exit %r' % (result.code,)


# -- T3-72: what is sealed is not what is executed -------------------------

@pytest.mark.finding('T3-72')
@pytest.mark.req('R1.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-72: the seal re-reads the fixture from disk '
                          'after the run has loaded it')
def test_run_fixture_changed_between_load_and_seal_sealed_as_executed(
        runner, fixture_dir):
    # Correct (SPEC R1.1, seal what is executed): the fixture hash in the
    # seal is the hash of the bytes the run loaded and executes, or the
    # run is refused. Here the file is rewritten after it is loaded and
    # before the seal (in the window T3-72 describes).
    path = fixture_dir / 'fixture.json'
    loaded = path.read_bytes()

    def rewrite():
        data = json.loads(loaded)
        data['_g5_note'] = 'rewritten after load'
        path.write_text(json.dumps(data), encoding='utf-8')
    result = runner(fixture_dir, hooks={'before_seal': rewrite})
    if result.refusal is not None or result.code not in (0, None):
        return  # refusing is correct too
    assert result.seals[0]['fixture_hash'] in digests(loaded)


@pytest.mark.finding('T3-72')
@pytest.mark.req('R1.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-72: gt_module.__file__ is never compared with '
                          'the sealed ground-truth path')
def test_run_ground_truth_executed_from_other_file_refused_or_sealed(
        runner, fixture_dir):
    # Correct (SPEC R1.1; T3-72): the ground-truth module the run executes
    # is the file it sealed. A package directory ground_truth_example/
    # beside ground_truth_example.py wins Python's import, so the run
    # executes the package and seals the .py. Correct: refuse, or seal
    # the file actually executed.
    package = fixture_dir / 'ground_truth_example'
    package.mkdir()
    shutil.copy(fixture_dir / 'ground_truth_example.py',
                package / '__init__.py')
    with open(package / '__init__.py', 'a', encoding='utf-8') as f:
        f.write('\n# the executed copy\n')
    result = runner(fixture_dir)
    if result.refusal is not None or result.code not in (0, None):
        return
    executed = result.executed['ground_truth']
    assert result.seals[0]['ground_truth_hash'] in \
        digests(Path(executed).read_bytes()), (
            'executed %s, sealed %s' % (
                executed, fixture_dir / 'ground_truth_example.py'))


# -- T3-30: the environment is recorded in the seal ---------------------------

@pytest.mark.proposal(
    'T3-30/T3-70: the environment recorded in the seal as separate '
    'fields; a proposed design')
@pytest.mark.finding('T3-30', 'T3-70')
@pytest.mark.req('R1.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-30: the seal records no Python version, '
                          'platform or package versions')
def test_run_seal_record_carries_environment_fields(runner, fixture_dir):
    # Correct (T3-30; AP-1 v1.3 §1.5.1, the declared environment): Python
    # version, platform and package versions are recorded in the seal as
    # separate fields, outside runner_source_hash. Field names are the
    # fix's choice; they contain 'python', 'platform' and 'package'.
    result = runner(fixture_dir)
    assert result.code == 0, result.console[-2000:]
    record = report_seal_record(result.out)
    python = [v for k, v in record.items() if 'python' in k.lower()]
    assert any(platform.python_version() in v for v in python), sorted(record)
    assert [k for k in record if 'platform' in k.lower()], sorted(record)
    assert [k for k in record if 'package' in k.lower()], sorted(record)


# -- V12-4: the AP-1 text is chosen per version ----------------------------

@pytest.mark.proposal(
    "V12-n: v1.2 behaviour alongside v1.3 is the author's proposal; field "
    "and key names are the fix's")
@pytest.mark.finding('V12-4')
@pytest.mark.req('R1.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='V12-4: the AP-1 text path is hard-coded to the '
                          'v1.3 draft; the fix adds a version table entry '
                          'for v1.2 (text 14659fc1..., DOI)')
def test_run_v12_config_seals_the_v12_text(runner, fixture_dir):
    # Correct (V12-4; AP-1 v1.2 §0.4 "A claim of compliance
    # must cite the specific version evaluated against"): the AP-1 text is
    # a per-version table entry, so a run whose config declares v1.2 and
    # the v1.2 text's hash seals the v1.2 text, without --ap1-text.
    result = runner(fixture_dir, config={'ap1_version': 'v1.2',
                                         'ap1_text_hash': V12_HASH,
                                         'ap1_version_doi': V12_DOI})
    assert result.refusal is None, str(result.refusal)
    assert result.seals[0]['ap1_text_hash'] == V12_HASH


@pytest.mark.proposal(
    "V12-n: v1.2 behaviour alongside v1.3 is the author's proposal; field "
    "and key names are the fix's")
@pytest.mark.finding('V12-4', 'T3-68')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('declared', ['placeholder', ''])
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='V12-4: a v1.2 label is sealed over the v1.3 text '
                          'when the declared hash is blank or placeholder')
def test_run_v12_label_never_sealed_over_v13_text(runner, fixture_dir,
                                                  declared):
    # Correct (V12-4): the seal never says "v1.2" over the v1.3 text. The
    # run is refused, or seals the v1.2 text.
    result = runner(fixture_dir, config={'ap1_version': 'v1.2',
                                         'ap1_text_hash': declared,
                                         'ap1_version_doi': V12_DOI})
    if result.refusal is not None or not result.seals:
        return
    assert result.seals[0]['ap1_text_hash'] != V13_HASH


# -- T3-18: the published-run verifier on a real run -----------------------

def load_verifier():
    spec = importlib.util.spec_from_file_location(
        '_g5_verify_run_seal', ROOT / 'tools' / 'verify_run_seal.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.finding('T3-18')
@pytest.mark.req('R1.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-18: verify_run_seal.py passes a run whose '
                          'transcript is missing')
def test_verifier_on_real_run_without_transcript_fails(runner, monkeypatch,
                                                       capsys):
    # End to end: a genuine run of the example (inputs read in place, so
    # the verifier's fixed paths match), then the transcript removed.
    # Correct (SPEC R1.1 "The record's hash appears on every transcript
    # line"; README: the tool third parties are told to use): exit 1.
    result = runner(EXAMPLE)
    assert result.code == 0, result.console[-2000:]
    os.remove(result.out / 'smoke_run.jsonl')
    vrs = load_verifier()
    monkeypatch.setattr(sys, 'argv', ['verify_run_seal.py', str(result.out)])
    code = vrs.main()
    out = capsys.readouterr().out
    assert code == 1, out


# -- T3-20: the "no float" static check (SPEC R0.4.3 item 2) ---------------

# Modules outside the comparison and reporting paths, and why.
FLOAT_EXEMPT = {
    'foundation/adapter.py': 'transport: sampling values sent as JSON '
                             'numbers, and the retry delay',
    'run.py': 'the 0.5 s pause between requests',
}


def float_uses(path):
    """Float literals, float() calls and math/statistics imports."""
    tree = ast.parse(path.read_text(encoding='utf-8-sig'))
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and type(node.value) is float:
            found.append('%d: float literal %r' % (node.lineno, node.value))
        elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
              and node.func.id == 'float'):
            found.append('%d: float() call' % node.lineno)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in ('math', 'statistics'):
                    found.append('%d: import %s' % (node.lineno, alias.name))
        elif isinstance(node, ast.ImportFrom) and \
                node.module in ('math', 'statistics'):
            found.append('%d: from %s import' % (node.lineno, node.module))
    return found


@pytest.mark.finding('T3-20')
@pytest.mark.req('R0.4.1', 'R0.4.3')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-20: the "no float" static check does not exist; '
                          'report.py computes the D7.5 bound in float, '
                          'operation_correctness.py takes pi and e from math')
def test_static_check_no_float_on_comparison_or_reporting_path():
    # Correct (SPEC R0.4.3 verification item 2: "Static check demonstrates
    # no float literal or float-producing operation on a comparison path";
    # R0.4.1: binary floating point "is prohibited anywhere a value is
    # compared, quantised, or reported"): no module of the package outside
    # FLOAT_EXEMPT has a float literal, a float() call, or imports math or
    # statistics (whose functions return floats). A static check cannot
    # see the type of '/', so true division of ints is not covered.
    offenders = {}
    for path in sorted(SRC.rglob('*.py')):
        rel = path.relative_to(SRC).as_posix()
        if rel in FLOAT_EXEMPT:
            continue
        uses = float_uses(path)
        if uses:
            offenders[rel] = uses
    assert offenders == {}
