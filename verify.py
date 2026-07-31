"""Phase A gate verification.

Tests all R0.1-R0.4 and R1.1 verification contracts.
Exit 0 if all pass, exit 1 if any fail.

Phase A exit gate per spec section 8:
  1. Sealed run against the mock
  2. Cross-platform hash reproducibility (CI)
  3. Numeric grammar cases pass
  4. No float on any comparison path
  5. Minimum-n refusal demonstrated
  6. Quoted-string numeric config enforced
"""

import json
import os
import sys

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import tempfile
from decimal import Decimal
from pathlib import Path

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from numeric import (
    parse_decimal, extract_numeric_tokens, quantise,
    canonical_hash, canonical_json, file_hash,
    AmbiguousLocaleError, NumericParseError,
)
from config import load_config, ConfigError, validate_minimum_n
from seal import seal, verify_seal, SealError


_passed = 0
_failed = 0
_base = Path(__file__).parent


def check(name, condition, detail=''):
    global _passed, _failed
    if condition:
        _passed += 1
        print(f'  PASS  {name}')
    else:
        _failed += 1
        print(f'  FAIL  {name}: {detail}')


# =====================================================================
# R0.4.2 â€” Numeric Token Grammar
# =====================================================================

def test_r04_parse():
    print('\n=== R0.4.2 Numeric Token Grammar ===')

    # US format with grouping
    v, pct, cur = parse_decimal('1,780.00')
    check('parse 1,780.00', v == Decimal('1780.00'), f'got {v}')

    # Plain decimal
    v, pct, cur = parse_decimal('1780.00')
    check('parse 1780.00', v == Decimal('1780.00'), f'got {v}')

    # Currency prefix
    v, pct, cur = parse_decimal('$1,780.00', currency_symbols=['$'])
    check('parse $1,780.00 value', v == Decimal('1780.00'), f'got {v}')
    check('parse $1,780.00 currency', cur == '$', f'got {cur!r}')

    # European separators
    v, pct, cur = parse_decimal('1.780,00',
                                 decimal_sep=',', grouping_sep='.')
    check('parse 1.780,00 (EU)', v == Decimal('1780.00'), f'got {v}')

    # Parenthesised negative
    v, pct, cur = parse_decimal('(1,780.00)')
    check('parse (1,780.00)', v == Decimal('-1780.00'), f'got {v}')

    # Parenthesised with currency
    v, pct, cur = parse_decimal('($1,780.00)', currency_symbols=['$'])
    check('parse ($1,780.00) value', v == Decimal('-1780.00'), f'got {v}')
    check('parse ($1,780.00) currency', cur == '$', f'got {cur!r}')

    # Percentage
    v, pct, cur = parse_decimal('12.5%')
    check('parse 12.5% value', v == Decimal('12.5'), f'got {v}')
    check('parse 12.5% flag', pct is True, f'got pct={pct}')

    # Negative with sign
    v, pct, cur = parse_decimal('-42.50')
    check('parse -42.50', v == Decimal('-42.50'), f'got {v}')

    # Unicode minus
    v, pct, cur = parse_decimal('\u221242.50')
    check('parse \\u221242.50', v == Decimal('-42.50'), f'got {v}')

    # Ambiguous token (same separator for both roles)
    try:
        parse_decimal('1.780', decimal_sep='.', grouping_sep='.')
        check('ambiguous 1.780 raises', False, 'should have raised')
    except AmbiguousLocaleError:
        check('ambiguous 1.780 raises', True)

    # Empty string
    try:
        parse_decimal('')
        check('empty string raises', False, 'should have raised')
    except NumericParseError:
        check('empty string raises', True)


# =====================================================================
# R0.4.2 â€” Extraction from free text
# =====================================================================

def test_r04_extract():
    print('\n=== R0.4.2 Token Extraction ===')

    text = 'The balance is $1,780.00 and the rate is 12.5%.'
    tokens = extract_numeric_tokens(text, currency_symbols=['$'])
    values = [(t.value, t.percent, t.currency) for t in tokens]

    check('extract $1,780.00',
          any(v == Decimal('1780.00') and c == '$'
              for v, p, c in values),
          f'got {values}')
    check('extract 12.5%',
          any(v == Decimal('12.5') and p is True
              for v, p, c in values),
          f'got {values}')

    # Multiple values in response
    text2 = 'Step 1: 274.1375, Step 2: 259.1375, Final: 777.41'
    tokens2 = extract_numeric_tokens(text2)
    nums = [t.value for t in tokens2]
    check('extract 274.1375', Decimal('274.1375') in nums, f'got {nums}')
    check('extract 259.1375', Decimal('259.1375') in nums, f'got {nums}')
    check('extract 777.41', Decimal('777.41') in nums, f'got {nums}')

    # Parenthesised negative in text
    text3 = 'The loss was ($2,400.00) this quarter.'
    tokens3 = extract_numeric_tokens(text3, currency_symbols=['$'])
    check('extract ($2,400.00)',
          any(t.value == Decimal('-2400.00') for t in tokens3),
          f'got {[(t.value, t.currency) for t in tokens3]}')


# =====================================================================
# R0.4.1 â€” No float on comparison paths
# =====================================================================

def test_r04_no_float():
    print('\n=== R0.4.1 No Float ===')

    # canonical_json refuses float
    try:
        canonical_json({'value': 1.5})
        check('canonical_json refuses float', False, 'should have raised')
    except TypeError as e:
        check('canonical_json refuses float', 'float' in str(e).lower())

    # canonical_json accepts Decimal
    result = canonical_json({'value': Decimal('1.5')})
    check('canonical_json accepts Decimal', '"1.5"' in result, f'got {result}')

    # parse_decimal never returns float
    v, _, _ = parse_decimal('1234.56')
    check('parse returns Decimal', isinstance(v, Decimal),
          f'got {type(v).__name__}')

    # Nested float refused
    try:
        canonical_json({'outer': {'inner': [1, 2, 3.0]}})
        check('nested float refused', False, 'should have raised')
    except TypeError as e:
        check('nested float refused', 'float' in str(e).lower())


# =====================================================================
# R0.4.3 â€” Canonical hashing
# =====================================================================

def test_r04_hash():
    print('\n=== R0.4.3 Canonical Hashing ===')

    obj = {'b': 'two', 'a': 'one', 'c': Decimal('3.0')}
    h1 = canonical_hash(obj)
    h2 = canonical_hash(obj)
    check('deterministic hash', h1 == h2)

    # Key order irrelevant
    obj1 = {'b': 'two', 'a': 'one'}
    obj2 = {'a': 'one', 'b': 'two'}
    check('key order irrelevant',
          canonical_hash(obj1) == canonical_hash(obj2))


# =====================================================================
# R0.4.1 â€” Round-once vs round-each (the defect)
# =====================================================================

def test_r04_round_once():
    print('\n=== R0.4.1 Round-Once vs Round-Each ===')

    a = Decimal('42175.00') * Decimal('7.8') / Decimal('100') / Decimal('12')
    check('step1 full precision', a == Decimal('274.1375'), f'got {a}')

    b = a - Decimal('15.00')
    check('step2 full precision', b == Decimal('259.1375'), f'got {b}')

    c = b * Decimal('3')
    check('step3 full precision', c == Decimal('777.4125'), f'got {c}')

    # CORRECT: quantise once at end
    correct = quantise(c, 2, 'ROUND_HALF_UP')
    check('round-once gives 777.41', correct == Decimal('777.41'),
          f'got {correct}')

    # Also correct under HALF_EVEN
    correct_even = quantise(c, 2, 'ROUND_HALF_EVEN')
    check('round-once HALF_EVEN also 777.41',
          correct_even == Decimal('777.41'), f'got {correct_even}')

    # WRONG: round each step
    wrong_s1 = quantise(a, 2, 'ROUND_HALF_UP')      # 274.14
    wrong_s2 = quantise(wrong_s1 - Decimal('15.00'), 2, 'ROUND_HALF_UP')  # 259.14
    wrong_s3 = quantise(wrong_s2 * Decimal('3'), 2, 'ROUND_HALF_UP')      # 777.42
    check('round-each gives 777.42', wrong_s3 == Decimal('777.42'),
          f'got {wrong_s3}')

    # The two differ
    check('round-once != round-each', correct != wrong_s3)

    # Mock behaviour 28: the runner must detect this discrepancy
    check('mock28: discrepancy detected',
          wrong_s3 - correct == Decimal('0.01'),
          f'diff = {wrong_s3 - correct}')


# =====================================================================
# R0.1 â€” Configuration
# =====================================================================

def test_r01_config():
    print('\n=== R0.1 Configuration ===')

    # Test: load valid example config
    example_config = _base / 'example' / 'config.json'
    if example_config.exists():
        config = load_config(str(example_config))
        check('valid config loads', config is not None)
        check('answer_tolerance is Decimal',
              isinstance(config['answer_tolerance'], Decimal),
              f'got {type(config["answer_tolerance"]).__name__}')
        check('repeat_count is int',
              isinstance(config['repeat_count'], int),
              f'got {type(config["repeat_count"]).__name__}')
    else:
        check('example config exists', False, str(example_config))

    # Test: missing required field
    _test_config_error(
        {'endpoint_url': 'test'},
        'missing field halts',
        'missing')

    # Test: bare numeric refused (float)
    _test_config_error(
        _valid_config_with(answer_tolerance=0.01),
        'bare float refused',
        'bare numeric')

    # Test: bare numeric refused (int)
    _test_config_error(
        _valid_config_with(repeat_count=50),
        'bare int refused',
        'bare numeric')


def test_r01_minimum_n():
    print('\n=== R0.1 Minimum-n ===')

    # D6 with only 9 items -> refused
    questions = [{'id': str(i)} for i in range(9)]
    config = {'dimensions_claimed': ['D6']}
    try:
        validate_minimum_n(config, questions)
        check('D6 with 9 items refused', False, 'should have raised')
    except ConfigError as e:
        check('D6 with 9 items refused',
              '9' in str(e) and '10' in str(e), str(e))

    # D6 with 10 items -> accepted
    questions10 = [{'id': str(i)} for i in range(10)]
    try:
        validate_minimum_n(config, questions10)
        check('D6 with 10 items accepted', True)
    except ConfigError as e:
        check('D6 with 10 items accepted', False, str(e))

    # D1 per-category with insufficient category
    config_d1 = {'dimensions_claimed': ['D1']}
    questions_d1 = [{'id': str(i), 'category': 'A'} for i in range(9)]
    try:
        validate_minimum_n(config_d1, questions_d1)
        check('D1 category A with 9 refused', False, 'should have raised')
    except ConfigError as e:
        check('D1 category A with 9 refused', 'D1' in str(e), str(e))


# =====================================================================
# R1.1 â€” Sealing
# =====================================================================

def test_r11_seal():
    print('\n=== R1.1 Sealing ===')

    example_dir = _base / 'example'
    config_path = example_dir / 'config.json'
    fixture_path = example_dir / 'fixture.json'
    questions_path = example_dir / 'questions.json'
    gt_path = example_dir / 'ground_truth_example.py'

    for p in [config_path, fixture_path, questions_path, gt_path]:
        if not p.exists():
            check(f'{p.name} exists', False)
            return

    config = load_config(str(config_path))

    # Create seal
    record = seal(
        config=config,
        fixture_path=fixture_path,
        questions_path=questions_path,
        ground_truth_path=gt_path,
    )

    check('seal has seal_hash',
          'seal_hash' in record and len(record['seal_hash']) == 64,
          f'got {record.get("seal_hash", "MISSING")}')

    check('seal has ev3_implemented=False',
          record.get('ev3_implemented') is False)

    # Component hashes are stable
    record2 = seal(
        config=config,
        fixture_path=fixture_path,
        questions_path=questions_path,
        ground_truth_path=gt_path,
    )

    check('fixture hash stable',
          record['fixture_hash'] == record2['fixture_hash'])
    check('questions hash stable',
          record['questions_hash'] == record2['questions_hash'])
    check('config hash stable',
          record['config_hash'] == record2['config_hash'])

    # Verify seal succeeds with same files
    try:
        verify_seal(
            record, config=config,
            fixture_path=fixture_path,
            questions_path=questions_path,
            ground_truth_path=gt_path,
        )
        check('verify_seal passes', True)
    except SealError as e:
        check('verify_seal passes', False, str(e))


# =====================================================================
# R1.1 â€” AP-1 text hash enforcement
# =====================================================================

def test_r11_ap1_hash():
    print('\n=== R1.1 AP-1 Text Hash ===')

    example_dir = _base / 'example'
    config = load_config(str(example_dir / 'config.json'))

    # Create a fake AP-1 text file
    tmp = tempfile.NamedTemporaryFile(
        mode='w', suffix='.md', delete=False,
        dir=str(_base))
    try:
        tmp.write('AP-1 v1.3 Draft for Comment\n')
        tmp.close()

        real_hash = file_hash(tmp.name)

        # Config says 'placeholder' -- seal should accept
        record = seal(
            config=config,
            fixture_path=example_dir / 'fixture.json',
            questions_path=example_dir / 'questions.json',
            ground_truth_path=example_dir / 'ground_truth_example.py',
            ap1_text_path=tmp.name,
        )
        check('placeholder hash accepted', True)
        check('ap1_text_hash computed',
              record['ap1_text_hash'] == real_hash,
              f'expected {real_hash}, got {record["ap1_text_hash"]}')

        # Config with wrong hash -- seal should refuse
        config_wrong = dict(config)
        config_wrong['ap1_text_hash'] = 'wrong_hash_value'
        try:
            seal(
                config=config_wrong,
                fixture_path=example_dir / 'fixture.json',
                questions_path=example_dir / 'questions.json',
                ground_truth_path=example_dir / 'ground_truth_example.py',
                ap1_text_path=tmp.name,
            )
            check('wrong ap1 hash refused', False, 'should have raised')
        except SealError as e:
            check('wrong ap1 hash refused', 'mismatch' in str(e).lower())
    finally:
        os.unlink(tmp.name)


# =====================================================================
# Ground-truth verification
# =====================================================================

def test_ground_truth():
    print('\n=== Ground-Truth Verification ===')

    gt_path = _base / 'example' / 'ground_truth_example.py'
    if not gt_path.exists():
        check('ground_truth_example.py exists', False)
        return

    # Import and use C8.5 compute() interface
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'ground_truth_example', str(gt_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Load fixture and questions
    import json
    example_dir = _base / 'example'
    with open(example_dir / 'fixture.json', 'r', encoding='utf-8') as f:
        fixture = json.load(f)
    with open(example_dir / 'questions.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)

    accounts = {a['id']: a for a in fixture['accounts']}
    all_ok = True
    failures = {}

    for item in questions['items']:
        item_id = item['id']
        ctx = {}
        for acct_id in item['source_accounts']:
            acct = accounts[acct_id]
            ctx[acct_id] = {
                k: v for k, v in acct.items() if k not in ('id', 'name')
            }
        result = mod.compute(item_id, ctx)
        if result['final'] is None or not result.get('derivable', True):
            all_ok = False
            failures[item_id] = 'not derivable or no final value'

    check('all ground-truth items compute from fixture', all_ok,
          str(failures) if failures else '')


# =====================================================================
# EV-3 guard â€” runner must never emit EV-3
# =====================================================================

def test_ev3_guard():
    print('\n=== EV-3 Guard ===')

    # The seal record should mark ev3 as not implemented
    example_dir = _base / 'example'
    config = load_config(str(example_dir / 'config.json'))
    record = seal(
        config=config,
        fixture_path=example_dir / 'fixture.json',
        questions_path=example_dir / 'questions.json',
        ground_truth_path=example_dir / 'ground_truth_example.py',
    )
    check('ev3_implemented is False',
          record['ev3_implemented'] is False)


# =====================================================================
# Helpers
# =====================================================================

def _valid_config_with(**overrides):
    """Return a valid config dict with specific overrides."""
    base = {
        'endpoint_url': 'http://test', 'model': 'test',
        'sampling': {'temperature': '0', 'top_p': 'omitted',
                     'max_tokens': '4096'},
        'answer_tolerance': '0.01',
        'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
        'permitted_transformations': [],
        'decline_markers': [], 'decimal_separator': '.',
        'grouping_separator': ',', 'currency_symbols': [],
        'dimensions_claimed': [], 'repeat_count': '1',
        'structured_answer_field': 'none',
        'ap1_version': 'test', 'ap1_text_hash': 'test',
    }
    base.update(overrides)
    return base


def _test_config_error(config_dict, test_name, expected_substr):
    """Write config_dict to a temp file, load it, expect ConfigError."""
    tmp = tempfile.NamedTemporaryFile(
        mode='w', suffix='.json', delete=False,
        dir=str(_base))
    try:
        json.dump(config_dict, tmp)
        tmp.close()
        try:
            load_config(tmp.name)
            check(test_name, False, 'should have raised ConfigError')
        except ConfigError as e:
            check(test_name, expected_substr.lower() in str(e).lower(),
                  str(e))
    finally:
        os.unlink(tmp.name)


# =====================================================================
# Main
# =====================================================================


def test_run1_literal_strings():
    """Regression tests using LITERAL STRINGS from the first live run.

    These strings are the exact model output that exposed the currency
    stripping and regex splitting defects. They must remain as-is.
    """
    # --- parse_decimal tests ---
    cases = [
        # (input, currency_symbols, expected_value, expected_currency)
        ('$2600.00',     ['$', 'USD'], Decimal('2600.00'),  '$'),
        ('$3109.65',     ['$', 'USD'], Decimal('3109.65'),  '$'),
        ('$286,063.00',  ['$', 'USD'], Decimal('286063.00'), '$'),
        ('-$2411.00',    ['$', 'USD'], Decimal('-2411.00'), '$'),
        ('$-2411.00',    ['$', 'USD'], Decimal('-2411.00'), '$'),
        ('($2,411.00)',  ['$', 'USD'], Decimal('-2411.00'), '$'),
        ('$25',          ['$', 'USD'], Decimal('25'),       '$'),
        ('$1437.00',     ['$', 'USD'], Decimal('1437.00'),  '$'),
    ]

    for text, syms, expected_val, expected_cur in cases:
        try:
            val, pct, cur = parse_decimal(text, currency_symbols=syms)
            check(f'parse_decimal({text!r})',
                  val == expected_val,
                  f'expected {expected_val}, got {val}')
            check(f'parse_decimal({text!r}) currency',
                  cur == expected_cur,
                  f'expected {expected_cur!r}, got {cur!r}')
        except Exception as e:
            check(f'parse_decimal({text!r})', False, f'raised {e}')

    # --- extract_numeric_tokens from prose (actual model outputs) ---
    prose_cases = [
        ('The available credit remaining on the credit card is $2600.00.',
         ['$', 'USD'],
         [Decimal('2600.00')]),
        ('The annual net growth of the investment account after all fees is $3109.65.',
         ['$', 'USD'],
         [Decimal('3109.65')]),
        ('The remaining mortgage balance after the first monthly payment of $1437.00 will be $286,063.00.',
         ['$', 'USD'],
         [Decimal('1437.00'), Decimal('286063.00')]),
        ('The credit card balance after one month will be -$2411.00.',
         ['$', 'USD'],
         [Decimal('-2411.00')]),
    ]

    for prose, syms, expected_vals in prose_cases:
        tokens = extract_numeric_tokens(prose, currency_symbols=syms)
        values = [t.value for t in tokens]
        for ev in expected_vals:
            found = any(abs(v - ev) < Decimal('0.001') for v in values)
            check(f'extract {ev} from "{prose[:50]}..."',
                  found,
                  f'expected {ev} in {values}')


def main():
    test_r04_parse()
    test_r04_extract()
    test_r04_no_float()
    test_r04_hash()
    test_r04_round_once()
    test_r01_config()
    test_r01_minimum_n()
    test_r11_seal()
    test_r11_ap1_hash()
    test_ground_truth()
    test_ev3_guard()
    test_run1_literal_strings()

    print(f'\n{"=" * 50}')
    print(f'Phase A Gate Results: {_passed} passed, {_failed} failed')
    print(f'{"=" * 50}')

    return 0 if _failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
