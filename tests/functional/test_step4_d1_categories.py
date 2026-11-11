"""Step 4, D1 per category end to end (T3-32), on a question set that meets
D1's minimum, so the test stays reachable once minimum-n is enforced
(T3-12): 40 items, 20 in each of two categories (SPEC R0.1: at least 10
per category; AP-1 v1.3 D1: at least 40 items).

The inputs are built in tmp_path: one savings account per item, a
ground-truth module with one derive function per item (monthly interest,
constants 100 and 12 declared), and the mock endpoint answers every item
correctly through the calculator, in both conditions, one repeat. The
expected counts, results and intervals are computed here from that
script, not read from the run.
"""

import json
import os
import re
import shutil
import sys
import time
from decimal import Decimal
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / 'example'
FIXTURES = ROOT / 'tests' / 'fixtures'
CATEGORIES = {'interest': range(1, 21), 'savings_growth': range(21, 41)}
KEY = 'sk-step4-not-a-real-key-0000'


def _item(n):
    return f'Q{n:02d}'


def _account(n):
    return {'id': f'acct{n:02d}', 'name': f'Savings Account {n}',
            'balance': f'{1000 + 37 * n}.00', 'direction': 'asset',
            'annual_rate': f'{1 + n % 5}.5', 'monthly_fee': '0.00'}


DERIVE = '''

def derive_{lower}(ctx):
    bal = D(ctx["{acct}"]["balance"])
    rate = D(ctx["{acct}"]["annual_rate"])
    monthly_interest = bal * rate / D("100") / D("12")
    return {{
        "final": monthly_interest,
        "derivable": True,
        "required_operation": "calculator",
        "intermediates": [{{
            "label": "monthly_interest", "value": monthly_interest,
            "operation": "multiply_then_divide",
            "inputs": [{{"source": "{acct}.balance"}},
                       {{"source": "{acct}.annual_rate"}},
                       {{"constant": "100"}}, {{"constant": "12"}}]}}],
        "source_fields_consumed": ["{acct}.balance", "{acct}.annual_rate"],
    }}
'''


def _inputs(path):
    numbers = [n for ns in CATEGORIES.values() for n in ns]
    accounts = [_account(n) for n in numbers]
    (path / 'fixture.json').write_text(
        json.dumps({'accounts': accounts}, indent=2), 'utf-8')
    items = [{'id': _item(n), 'category': category,
              'text': f'What is the monthly interest earned on savings '
                      f'account {n}?',
              'source_accounts': [f'acct{n:02d}']}
             for category, ns in CATEGORIES.items() for n in ns]
    (path / 'questions.json').write_text(
        json.dumps({'questions_version': 'd1-test', 'items': items},
                   indent=2), 'utf-8')
    module = ['"""Ground truth for the D1 per-category test."""\n',
              'from decimal import Decimal as D\n']
    module += [DERIVE.format(lower=_item(n).lower(), acct=f'acct{n:02d}')
               for n in numbers]
    module.append('\n\nDERIVATIONS = {%s}\n' % ', '.join(
        f'"{_item(n)}": derive_{_item(n).lower()}' for n in numbers))
    module.append('\n\ndef compute(item_id, delivered_context):\n'
                  '    return DERIVATIONS[item_id](delivered_context)\n')
    (path / 'ground_truth_example.py').write_text(''.join(module), 'utf-8')
    shutil.copyfile(EXAMPLE / 'calculator_tool.py',
                    path / 'calculator_tool.py')
    script = {}
    for n in numbers:
        a = _account(n)
        script[f'{_item(n)}/*/*'] = [
            {'call': f"{a['balance']} * {a['annual_rate']} / 100 / 12"},
            {'say': 'The monthly interest earned is ${result}.'}]
    return items, script


@pytest.fixture(scope='module')
def d1_run(tmp_path_factory):
    tmp = tmp_path_factory.mktemp('d1run')
    fixture_dir = tmp / 'inputs'
    fixture_dir.mkdir()
    items, script = _inputs(fixture_dir)
    config = json.loads((EXAMPLE / 'config.json').read_text('utf-8'))
    config.update(repeat_count='1', dimensions_claimed=['D1', 'D2', 'D7'])
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
            api_key=KEY, questions={'items': items},
            system_prompts={config['system_prompt_base']: 'base',
                            config['system_prompt_instruction_removed']:
                                'instruction_removed'},
            responses=script).start()
        try:
            for name in list(os.environ):
                if name.startswith('AP1_SMOKE_'):
                    mp.delenv(name)
            mp.setenv('AP1_SMOKE_API_KEY', KEY)
            mp.setenv('AP1_SMOKE_ENDPOINT', mock.url)
            mp.setenv('AP1_SMOKE_MODEL', 'mock-model')
            mp.setattr(time, 'sleep', lambda seconds: None)
            from ap1_run import run as runner
            code = runner.main(['--config', str(config_path),
                                '--fixture-dir', str(fixture_dir),
                                '--output-dir', str(output_dir)])
        finally:
            mock.stop()
            for name in ('ground_truth_example', 'calculator_tool'):
                sys.modules.pop(name, None)
    if code != 0:
        # Not an AssertionError: this dataset meets D1's minimum, so a run
        # that does not complete is a defect of its own, not this test's.
        raise RuntimeError(f'the D1 run did not complete (exit {code})')
    return (output_dir / 'report.md').read_text('utf-8')


def _two_sided_clopper_pearson_all_correct(n):
    """The 95 % Clopper-Pearson interval for n of n: [0.025^(1/n), 1]."""
    return Decimal('0.025') ** (Decimal(1) / n), Decimal(1)


def _shown(value):
    out = set()
    for scale, places in ((100, 1), (1, 3)):
        v = value * scale
        q = Decimal(10) ** -places
        for rounding in ('ROUND_HALF_UP', 'ROUND_FLOOR', 'ROUND_CEILING'):
            out.add(str(v.quantize(q, rounding=rounding)))
    return out


@pytest.mark.proposal(
    'T3-32: D1 n per category is the scored responses (both conditions) or '
    'the items; the unit is not decided (as T3-11 for D7.1), and the 95 % '
    'interval is Clopper-Pearson; both are the author\'s proposal')
@pytest.mark.finding('T3-32')
@pytest.mark.req('AP-1 D1', 'R3.3', 'R0.1')
@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='T3-32: D1 is one pooled rate, not per category '
                          'with a 95 % interval')
def test_run_report_d1_per_category_with_n_result_and_interval(d1_run):
    # AP-1 v1.3 D1: "Results reported per category, with 95% confidence
    # intervals, and with n stated." Every item here is answered
    # correctly in both conditions, so each category's result is 100 %;
    # its n is 20 items or 40 responses, and its interval is the one for
    # n of n. Section 3 gives, per category, a row stating n, the result
    # and both bounds.
    s3 = d1_run[d1_run.index('## 3.'):]
    s3 = s3[:s3.index('\n## ', 1)]
    bad = []
    for category, ns in CATEGORIES.items():
        rows = [line for line in s3.splitlines()
                if re.search(rf'\b{category}\b', line)]
        ok = []
        for n in (len(ns), 2 * len(ns)):
            lo, hi = _two_sided_clopper_pearson_all_correct(n)
            ok += [line for line in rows
                   if re.search(rf'(\bn\s*=\s*|\|\s*){n}\b', line)
                   and re.search(r'\b100(\.0+)?\s*%|\b1\.000\b|\b'
                                 rf'{n}\s*/\s*{n}\b', line)
                   and any(s in line for s in _shown(lo))
                   and any(s in line for s in _shown(hi))]
        if not ok:
            bad.append((category, rows))
    assert bad == [], s3
