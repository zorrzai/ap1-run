"""Unit tests for the R1.1 pre-registration seal, its verifier, and the
R3.1 seal-time ground-truth guards (perturbation and source fields)."""

import hashlib
import importlib.util
import json
from datetime import timezone
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

import pytest

from ap1_run.execution import seal as seal_mod
from ap1_run.execution.context import TrackingContext
from ap1_run.execution.seal import (
    SealError, perturbation_check, seal, source_fields_check, verify_seal,
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canon(obj):
    """The canonical-JSON hash, written out independently (R0.4.3)."""
    text = json.dumps(obj, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False)
    return sha(text.encode('utf-8'))


def text_sha(data):
    """A sealed text input's hash, written out independently (T3-50): LF
    line endings, no UTF-8 byte-order mark."""
    if data.startswith(b'\xef\xbb\xbf'):
        data = data[3:]
    return sha(data.replace(b'\r\n', b'\n').replace(b'\r', b'\n'))


class FrozenDatetime:
    calls = []

    @classmethod
    def now(cls, tz=None):
        cls.calls.append(tz)
        return SimpleNamespace(isoformat=lambda: '2026-10-15T12:00:00+00:00')


ENVIRONMENT = {'python_version': 'CPython 3.0.0', 'platform': 'TestOS-1',
               'package_versions': 'ap1-run 0.0, requests 0.0'}


@pytest.fixture
def frozen(monkeypatch):
    """A fixed clock and a fixed environment."""
    FrozenDatetime.calls = []
    monkeypatch.setattr(seal_mod, 'datetime', FrozenDatetime)
    monkeypatch.setattr(seal_mod, 'runner_environment',
                        lambda: dict(ENVIRONMENT))
    return FrozenDatetime


AP1_TEXT = b'AP-1 \xe2\x80\x94 text\n'

CONFIG = {'ap1_version': '1.3', 'ap1_version_doi': '10.5281/z.1',
          'ap1_text_hash': sha(AP1_TEXT),
          'runner_version_tag': 'v1', 'runner_version_commit': 'abc',
          'n': 3}


@pytest.fixture
def files(tmp_path):
    contents = {'fixture': b'{"accounts": []}\r\n', 'questions': b'{"items":[]}',
                'ground_truth': b'def compute(i, c): pass\n',
                'ap1_text': AP1_TEXT}
    paths = {}
    for name, data in contents.items():
        paths[name] = tmp_path / f'{name}.bin'
        paths[name].write_bytes(data)
    hashes = {k: text_sha(v) for k, v in contents.items()}
    hashes['ap1_text'] = sha(AP1_TEXT)  # raw bytes
    return SimpleNamespace(
        paths=paths, hashes=hashes,
        kwargs={'fixture_path': paths['fixture'],
                'questions_path': paths['questions'],
                'ground_truth_path': paths['ground_truth']})


def make_seal(files, config=CONFIG, **kwargs):
    """seal() over the files, with the AP-1 text unless kwargs say."""
    kwargs = {'ap1_text_path': files.paths['ap1_text'], **kwargs}
    return seal(config=config, **files.kwargs, **kwargs)


# -- seal(): the record --------------------------------------------------

def test_seal_record(files, frozen):
    record = make_seal(files, runner_source_hash='f' * 64)
    body = {
        'seal_format': '2',
        'timestamp': '2026-10-15T12:00:00+00:00',
        'fixture_hash': files.hashes['fixture'],
        'questions_hash': files.hashes['questions'],
        'ground_truth_hash': files.hashes['ground_truth'],
        'expected_values_hash': '',
        'config_hash': canon(CONFIG),
        'ap1_version': '1.3',
        'ap1_version_doi': '10.5281/z.1',
        'ap1_text_hash': sha(AP1_TEXT),
        'runner_version_tag': 'v1',
        'runner_version_commit': 'abc',
        'runner_source_hash': 'f' * 64,
        **ENVIRONMENT,
        'verification_keys': [],
        'ev3_implemented': False,
    }
    # seal_hash covers every field, the timestamp included (T3-47).
    assert record == {**body, 'seal_hash': canon(body)}
    assert frozen.calls == [timezone.utc]
    assert sorted(record) == sorted(seal_mod.SEALED_FIELDS + ('seal_hash',))


def test_seal_records_the_real_environment(files, monkeypatch):
    # Not frozen: the fields are runner_environment's (F2).
    from ap1_run.execution.version import runner_environment
    record = make_seal(files)
    env = runner_environment()
    assert {k: record[k] for k in env} == env


def test_seal_config_without_optional_fields_gives_blank_fields(files,
                                                                frozen):
    config = {'ap1_text_hash': sha(AP1_TEXT)}
    record = make_seal(files, config=config)
    for key in ('ap1_version', 'ap1_version_doi', 'runner_version_tag',
                'runner_version_commit', 'runner_source_hash'):
        assert record[key] == ''
    assert record['config_hash'] == canon(config)


def test_seal_records_verification_keys(files, frozen):
    record = make_seal(files, verification_keys=['k1'])
    assert record['verification_keys'] == ['k1']
    assert record['ev3_implemented'] is False


def test_seal_accepts_string_paths(files, frozen):
    by_str = seal(config=CONFIG, fixture_path=str(files.paths['fixture']),
                  questions_path=str(files.paths['questions']),
                  ground_truth_path=str(files.paths['ground_truth']),
                  ap1_text_path=str(files.paths['ap1_text']))
    assert by_str == make_seal(files, ap1_text_path=files.paths['ap1_text'])


@pytest.mark.req('R1.1')
@pytest.mark.parametrize('change', [
    'fixture_path', 'questions_path', 'ground_truth_path', 'config',
    'runner_source_hash', 'verification_keys', 'expected_values'])
def test_seal_hash_binds_each_component(files, frozen, tmp_path, change):
    # T3-15 asks for this: seal_hash changes when any one component does.
    other = tmp_path / 'other.bin'
    other.write_bytes(b'changed')
    kwargs = {'config': CONFIG, **files.kwargs,
              'ap1_text_path': files.paths['ap1_text']}
    base = seal(**kwargs)
    kwargs[change] = {'config': {**CONFIG, 'n': 4},
                      'runner_source_hash': 'x',
                      'verification_keys': ['k'],
                      'expected_values': {'Q01': {'final': Decimal('1')}},
                      }.get(change, other)
    assert seal(**kwargs)['seal_hash'] != base['seal_hash']


@pytest.mark.parametrize('field', ['python_version', 'platform',
                                   'package_versions'])
def test_seal_hash_binds_the_environment(files, frozen, monkeypatch, field):
    base = make_seal(files)
    monkeypatch.setattr(seal_mod, 'runner_environment',
                        lambda: {**ENVIRONMENT, field: 'other'})
    assert make_seal(files)['seal_hash'] != base['seal_hash']


@pytest.mark.req('R1.1')
def test_seal_expected_values_hashed_canonically(files, frozen):
    # T3-48: the ground-truth results, Decimals as their exact strings.
    values = {'Q02': {'final': Decimal('1.50'), 'derivable': True},
              'Q01': {'final': None, 'derivable': False}}
    record = make_seal(files, expected_values=values)
    assert record['expected_values_hash'] == canon(
        {'Q01': {'derivable': False, 'final': None},
         'Q02': {'derivable': True, 'final': '1.50'}})


def test_seal_empty_expected_values_are_sealed_as_such(files, frozen):
    assert make_seal(files, expected_values={})['expected_values_hash'] \
        == canon({})


@pytest.mark.parametrize('bad', [1.5, object()])
def test_seal_unhashable_expected_values_refused(files, frozen, bad):
    with pytest.raises(SealError) as exc:
        make_seal(files, expected_values={'Q01': {'final': bad}})
    assert str(exc.value).startswith('expected values cannot be sealed: ')


def test_seal_hashes_the_loaded_bytes_not_the_files(files, frozen):
    # T3-72: what the run read and executes is what is sealed; the files
    # are not read again.
    loaded = {'fixture': b'{"a": 1}\n', 'questions': b'q\r\n',
              'ground_truth': b'\xef\xbb\xbfg\n'}
    for path in files.paths.values():
        if path != files.paths['ap1_text']:
            path.write_bytes(b'changed on disk')
    record = make_seal(files, loaded=loaded)
    assert record['fixture_hash'] == sha(b'{"a": 1}\n')
    assert record['questions_hash'] == sha(b'q\n')
    assert record['ground_truth_hash'] == sha(b'g\n')


def test_seal_reads_a_file_not_in_loaded(files, frozen):
    record = make_seal(files, loaded={'fixture': b'x'})
    assert record['fixture_hash'] == sha(b'x')
    assert record['questions_hash'] == files.hashes['questions']


# -- text_hash, record_hash --------------------------------------------------

@pytest.mark.parametrize('data, same_as', [
    (b'a\nb\n', b'a\nb\n'), (b'a\r\nb\r\n', b'a\nb\n'),
    (b'a\rb\r', b'a\nb\n'), (b'a\r\r\nb', b'a\n\nb'),
    (b'\xef\xbb\xbfa\n', b'a\n'), (b'a\xef\xbb\xbf', b'a\xef\xbb\xbf'),
    (b'\xef\xbb\xbf\xef\xbb\xbfa', b'\xef\xbb\xbfa'), (b'', b'')])
def test_text_hash_lf_and_no_leading_bom(data, same_as):
    assert seal_mod.text_hash(data) == sha(same_as)


def test_text_file_hash_reads_the_file(tmp_path):
    path = tmp_path / 'f'
    path.write_bytes(b'x\r\n')
    assert seal_mod.text_file_hash(str(path)) == sha(b'x\n')


def test_record_hash_is_every_field_but_seal_hash():
    record = {'timestamp': 't', 'a': [1], 'seal_hash': 'anything'}
    assert seal_mod.record_hash(record) == canon({'timestamp': 't',
                                                  'a': [1]})


# -- seal(): the AP-1 text hash -------------------------------------------

def test_seal_ap1_text_matching_declared_hash_recorded(files, frozen):
    record = make_seal(files, ap1_text_path=files.paths['ap1_text'])
    assert record['ap1_text_hash'] == files.hashes['ap1_text']


def test_seal_ap1_text_hashed_as_raw_bytes(files, frozen):
    # The AP-1 text must equal the publisher's deposit: no normalisation.
    crlf = b'AP-1\r\n'
    files.paths['ap1_text'].write_bytes(crlf)
    record = make_seal(files, config={**CONFIG, 'ap1_text_hash': sha(crlf)})
    assert record['ap1_text_hash'] == sha(crlf) != text_sha(crlf)


@pytest.mark.req('R1.1')
def test_seal_ap1_text_mismatch_raises(files, frozen):
    config = {**CONFIG, 'ap1_text_hash': 'deadbeef'}
    with pytest.raises(SealError) as exc:
        make_seal(files, config=config, ap1_text_path=files.paths['ap1_text'])
    assert str(exc.value) == (
        "AP-1 text hash mismatch: config declares 'deadbeef', "
        f"file hashes to {files.hashes['ap1_text']!r}")


def test_seal_ap1_text_missing_file_raises(files, frozen, tmp_path):
    missing = tmp_path / 'nope.md'
    with pytest.raises(SealError) as exc:
        make_seal(files, ap1_text_path=missing)
    assert str(exc.value) == f'AP-1 text file not found: {missing}'


@pytest.mark.parametrize('declared', ['placeholder', '', None])
def test_seal_no_declared_ap1_hash_message(files, frozen, declared):
    config = {k: v for k, v in CONFIG.items() if k != 'ap1_text_hash'}
    if declared is not None:
        config['ap1_text_hash'] = declared
    with pytest.raises(SealError) as exc:
        make_seal(files, config=config)
    assert str(exc.value) == (
        f'AP-1 text hash: the config declares {declared!r}; a sealed run '
        f'needs the SHA-256 of the AP-1 text it claims (R1.1)')


def test_seal_no_ap1_text_path_message(files, frozen):
    with pytest.raises(SealError) as exc:
        make_seal(files, ap1_text_path=None)
    assert str(exc.value) == ('AP-1 text: no file given; a sealed run '
                              'hashes the AP-1 text it claims (R1.1)')


# -- verify_seal() ----------------------------------------------------------

def verify(record, files, config=CONFIG, **kwargs):
    return verify_seal(record, config=config, **files.kwargs, **kwargs)


def test_verify_seal_unchanged_inputs_returns_true(files, frozen):
    record = make_seal(files, ap1_text_path=files.paths['ap1_text'])
    assert verify(record, files, ap1_text_path=files.paths['ap1_text']) is True


def test_verify_seal_same_text_other_line_endings_returns_true(files, frozen):
    record = make_seal(files)
    files.paths['fixture'].write_bytes(b'\xef\xbb\xbf{"accounts": []}\r')
    assert verify(record, files) is True


@pytest.mark.req('R1.1')
@pytest.mark.parametrize('name', ['fixture', 'questions', 'ground_truth'])
def test_verify_seal_changed_file_raises_naming_it(files, frozen, name):
    record = make_seal(files)
    files.paths[name].write_bytes(b'tampered')
    with pytest.raises(SealError) as exc:
        verify(record, files)
    assert str(exc.value) == (
        f"seal verification failed:\n  {name}: "
        f"sealed={files.hashes[name]!r}, current={sha(b'tampered')!r}")


def test_verify_seal_changed_config_raises(files, frozen):
    record = make_seal(files)
    with pytest.raises(SealError) as exc:
        verify(record, files, config={**CONFIG, 'n': 4})
    assert str(exc.value) == (
        f"seal verification failed:\n  config: sealed={canon(CONFIG)!r}, "
        f"current={canon({**CONFIG, 'n': 4})!r}")


def test_verify_seal_changed_ap1_text_raises(files, frozen, tmp_path):
    record = make_seal(files, ap1_text_path=files.paths['ap1_text'])
    other = tmp_path / 'other.md'
    other.write_bytes(b'x')
    with pytest.raises(SealError) as exc:
        verify(record, files, ap1_text_path=other)
    assert str(exc.value) == (
        f"seal verification failed:\n  ap1_text: "
        f"sealed={files.hashes['ap1_text']!r}, current={sha(b'x')!r}")


def test_verify_seal_ap1_text_compared_with_declared_hash(files, frozen):
    # Without a path, the sealed text hash is still compared with the
    # hash the config declares.
    record = make_seal(files)
    config = {**CONFIG, 'ap1_text_hash': 'e' * 64}
    with pytest.raises(SealError) as exc:
        verify(record, files, config=config)
    assert f"  ap1_text: sealed={sha(AP1_TEXT)!r}, current={'e' * 64!r}" \
        in str(exc.value).split('\n')


def test_verify_seal_lists_every_mismatch_in_order(files, frozen):
    record = make_seal(files)
    files.paths['fixture'].write_bytes(b'1')
    files.paths['ground_truth'].write_bytes(b'2')
    config = {**CONFIG, 'n': 9, 'ap1_version_doi': 'other'}
    with pytest.raises(SealError) as exc:
        verify(record, files, config=config)
    lines = str(exc.value).split('\n')
    assert lines[0] == 'seal verification failed:'
    assert [line.split(':')[0] for line in lines[1:]] == [
        '  fixture', '  ground_truth', '  config', '  ap1_version_doi']
    assert lines[4] == "  ap1_version_doi: sealed='10.5281/z.1', current='other'"


def test_verify_seal_missing_record_fields_are_mismatches(files):
    with pytest.raises(SealError) as exc:
        verify({}, files)
    msg = str(exc.value)
    assert msg.split('\n')[1] == (
        '  record: missing ' + ', '.join(seal_mod.SEALED_FIELDS))
    assert msg.split('\n')[2] == (
        f"  seal_hash: sealed=None, recomputed={canon({})!r}")
    for name in ('fixture', 'questions', 'ground_truth', 'config'):
        assert f'  {name}: sealed=None, current=' in msg


def test_verify_seal_rewritten_field_names_the_seal_hash(files, frozen):
    record = make_seal(files)
    record['ap1_version'] = '9.9'
    with pytest.raises(SealError) as exc:
        verify(record, files)
    assert str(exc.value) == (
        f"seal verification failed:\n  seal_hash: "
        f"sealed={record['seal_hash']!r}, "
        f"recomputed={seal_mod.record_hash(record)!r}")


def test_verify_seal_doi_missing_on_both_sides_matches(files, frozen):
    config = {k: v for k, v in CONFIG.items() if k != 'ap1_version_doi'}
    record = make_seal(files, config=config)
    assert verify(record, files, config=config) is True


def test_verify_seal_record_without_doi_named_once(files, frozen):
    # The missing field is named; with no DOI in the config either, there
    # is no DOI mismatch line besides.
    config = {k: v for k, v in CONFIG.items() if k != 'ap1_version_doi'}
    record = make_seal(files, config=config)
    del record['ap1_version_doi']
    with pytest.raises(SealError) as exc:
        verify(record, files, config=config)
    assert str(exc.value).split('\n')[1:] == [
        '  record: missing ap1_version_doi',
        f"  seal_hash: sealed={record['seal_hash']!r}, "
        f"recomputed={seal_mod.record_hash(record)!r}"]


def test_verify_seal_runner_source_hash_compared_when_given(files, frozen):
    record = make_seal(files, runner_source_hash='a' * 64)
    assert verify(record, files, runner_source_hash='a' * 64) is True
    with pytest.raises(SealError) as exc:
        verify(record, files, runner_source_hash='b' * 64)
    assert str(exc.value) == (
        "seal verification failed:\n  runner_source_hash: "
        f"sealed={'a' * 64!r}, current={'b' * 64!r}")


def test_verify_seal_expected_values_compared_when_given(files, frozen):
    values = {'Q01': {'final': Decimal('2')}}
    record = make_seal(files, expected_values=values)
    assert verify(record, files, expected_values=values) is True
    other = {'Q01': {'final': Decimal('3')}}
    with pytest.raises(SealError) as exc:
        verify(record, files, expected_values=other)
    assert str(exc.value) == (
        "seal verification failed:\n  expected_values: "
        f"sealed={canon({'Q01': {'final': '2'}})!r}, "
        f"current={canon({'Q01': {'final': '3'}})!r}")


# -- perturbation_check -----------------------------------------------------

FIXTURE = {'accounts': [
    {'id': 'acct', 'name': 'Savings', 'balance': '100', 'rate': '0',
     'kind': 'savings', 'dotted.f': '5'},
    {'id': 'other', 'name': 'Other', 'balance': '7'},
]}


def questions(*ids, accounts=('acct',)):
    return {'items': [{'id': i, 'source_accounts': list(accounts)}
                      for i in ids]}


def module(compute):
    return SimpleNamespace(compute=compute)


def recording(fn):
    """A ground-truth module whose compute records (item_id, ctx copy)."""
    seen = []

    def compute(item_id, ctx):
        seen.append((item_id, {k: dict(v) for k, v in ctx.items()}))
        return fn(item_id, ctx)
    mod = module(compute)
    mod.seen = seen
    return mod


def honest(fields):
    """final = sum of the declared fields."""
    def compute(item_id, ctx):
        total = sum(Decimal(ctx[f.split('.')[0]][f.split('.')[1]])
                    for f in fields)
        return {'final': total, 'source_fields_consumed': list(fields)}
    return compute


def constant(fields, final=Decimal('42')):
    def compute(item_id, ctx):
        return {'final': final, 'source_fields_consumed': list(fields)}
    return compute


PERTURBATION_REFUSED = ("perturbation check failed: the module's output "
                        "does not follow its declared source fields. ")
UNCHANGED = 'output unchanged when {} multiplied by 1.1'


def test_perturbation_check_honest_module_returns_empty_list():
    mod = module(honest(['acct.balance']))
    assert perturbation_check(mod, FIXTURE, questions('Q01')) == []


@pytest.mark.req('R3.1')
def test_perturbation_check_constant_module_raises_naming_field():
    mod = module(constant(['acct.balance']))
    with pytest.raises(SealError) as exc:
        perturbation_check(mod, FIXTURE, questions('Q01'))
    assert str(exc.value) == (
        PERTURBATION_REFUSED + 'Q01: ' + UNCHANGED.format('acct.balance'))


def test_perturbation_check_names_every_field_across_items():
    mod = module(constant(['acct.balance', 'acct.rate']))
    with pytest.raises(SealError) as exc:
        perturbation_check(mod, FIXTURE, questions('Q01', 'Q02'))
    assert str(exc.value) == PERTURBATION_REFUSED + (
        'Q01: output unchanged when acct.balance multiplied by 1.1; '
        'Q01: output unchanged when acct.rate set from 0 to 1; '
        'Q02: output unchanged when acct.balance multiplied by 1.1; '
        'Q02: output unchanged when acct.rate set from 0 to 1')


def test_perturbation_check_default_factor_is_1_1():
    mod = recording(honest(['acct.balance']))
    perturbation_check(mod, FIXTURE, questions('Q01'))
    assert [ctx['acct']['balance'] for _, ctx in mod.seen] == ['100', '110.0']


def test_perturbation_check_custom_factor():
    mod = recording(honest(['acct.balance']))
    perturbation_check(mod, FIXTURE, questions('Q01'),
                       perturbation_factor=Decimal('3'))
    assert mod.seen[1][1]['acct']['balance'] == '300'


def test_perturbation_check_zero_field_set_to_one():
    mod = recording(honest(['acct.rate']))
    perturbation_check(mod, FIXTURE, questions('Q01'),
                       perturbation_factor=Decimal('5'))
    assert mod.seen[1][1]['acct']['rate'] == '1'


def test_perturbation_check_zero_field_with_constant_module_raises():
    with pytest.raises(SealError, match='Q01: output unchanged when '
                                        'acct.rate set from 0 to 1$'):
        perturbation_check(module(constant(['acct.rate'])), FIXTURE,
                           questions('Q01'))


def test_perturbation_check_each_field_perturbed_alone_on_fresh_context():
    mod = recording(honest(['acct.balance', 'acct.rate']))
    perturbation_check(mod, FIXTURE, questions('Q01'))
    assert [ctx['acct'] for _, ctx in mod.seen] == [
        {'balance': '100', 'rate': '0', 'kind': 'savings', 'dotted.f': '5'},
        {'balance': '110.0', 'rate': '0', 'kind': 'savings', 'dotted.f': '5'},
        {'balance': '100', 'rate': '1', 'kind': 'savings', 'dotted.f': '5'},
    ]


def test_perturbation_check_context_has_only_source_accounts():
    mod = recording(honest(['other.balance']))
    perturbation_check(mod, FIXTURE, questions('Q01', accounts=['other']))
    assert mod.seen[0] == ('Q01', {'other': {'balance': '7'}})


def test_perturbation_check_field_spec_split_at_first_dot():
    mod = recording(lambda i, ctx: {
        'final': Decimal(ctx['acct']['dotted.f']),
        'source_fields_consumed': ['acct.dotted.f']})
    assert perturbation_check(mod, FIXTURE, questions('Q01')) == []
    assert mod.seen[1][1]['acct']['dotted.f'] == '5.5'


def test_perturbation_check_item_without_source_accounts_gets_empty_ctx():
    mod = recording(constant([], final=Decimal('1')))
    with pytest.raises(SealError):  # it declares nothing to perturb (T3-7)
        perturbation_check(mod, FIXTURE, {'items': [{'id': 'Q01'}]})
    assert mod.seen == [('Q01', {})]


def test_perturbation_check_no_items_returns_empty_list():
    mod = module(constant(['acct.balance']))
    assert perturbation_check(mod, FIXTURE, {}) == []


@pytest.mark.req('R3.1')
def test_perturbation_check_baseline_raising_is_a_failure():
    def compute(item_id, ctx):
        raise KeyError('x')
    with pytest.raises(SealError) as exc:
        perturbation_check(module(compute), FIXTURE, questions('Q01'))
    assert str(exc.value) == (
        PERTURBATION_REFUSED
        + "Q01: baseline computation raised KeyError: 'x'")


def test_perturbation_check_baseline_failure_does_not_stop_later_items():
    def compute(item_id, ctx):
        if item_id == 'Q01':
            raise KeyError('x')
        return constant(['acct.balance'])(item_id, ctx)
    with pytest.raises(SealError) as exc:
        perturbation_check(module(compute), FIXTURE, questions('Q01', 'Q02'))
    assert str(exc.value).endswith(
        "Q01: baseline computation raised KeyError: 'x'; "
        'Q02: ' + UNCHANGED.format('acct.balance'))


def test_perturbation_check_perturbed_raising_is_a_failure():
    def compute(item_id, ctx):
        if ctx['acct']['balance'] != '100':
            raise ValueError('no')
        return {'final': Decimal('1'),
                'source_fields_consumed': ['acct.balance', 'acct.rate']}
    # balance: perturbed run raises; rate: unchanged output. Both named.
    with pytest.raises(SealError) as exc:
        perturbation_check(module(compute), FIXTURE, questions('Q01'))
    assert str(exc.value) == PERTURBATION_REFUSED + (
        'Q01: perturbed computation (acct.balance multiplied by 1.1) raised '
        'ValueError: no; '
        'Q01: output unchanged when acct.rate set from 0 to 1')


# The vacuous paths of T3-7 are failures now. Each is followed by a
# failing item Q09, so that a failure which ended the loop would be noticed.

def assert_q01_refused_and_q09_checked(compute_q01, *ids):
    def compute(item_id, ctx):
        if item_id == 'Q09':
            return constant(['other.balance'])(item_id, ctx)
        return compute_q01(item_id, ctx)
    qs = questions(*ids, 'Q09', accounts=['acct', 'other'])
    with pytest.raises(SealError) as exc:
        perturbation_check(module(compute), FIXTURE, qs)
    assert str(exc.value).startswith(PERTURBATION_REFUSED + 'Q01: ')
    assert str(exc.value).endswith(
        '; Q09: ' + UNCHANGED.format('other.balance'))
    return str(exc.value)


@pytest.mark.finding('T3-7')
@pytest.mark.parametrize('declared, reason', [
    (None, 'declares no source fields to perturb '
           '(source_fields_consumed is None)'),
    ([], 'declares no source fields to perturb '
         '(source_fields_consumed is [])'),
    (['nope.balance'], "declared source field 'nope.balance': account "
                       "'nope' is not in the delivered context"),
    (['acct.nope'], "declared source field 'acct.nope': account 'acct' "
                    "has no field 'nope'"),
    (['balance'], "declared source field 'balance' is not of the form "
                  "account.field"),
    (['acct.kind'], 'no declared source field could be perturbed: '
                    'acct.kind not numeric'),
], ids=['missing-key', 'none', 'unknown-account', 'unknown-field', 'no-dot',
        'non-numeric'])
def test_perturbation_check_vacuous_declaration_refused_with_reason(
        declared, reason):
    def compute(item_id, ctx):
        out = {'final': Decimal('42')}
        if declared is not None:
            out['source_fields_consumed'] = list(declared)
        return out
    msg = assert_q01_refused_and_q09_checked(compute, 'Q01')
    assert msg == PERTURBATION_REFUSED + f'Q01: {reason}; Q09: ' + \
        UNCHANGED.format('other.balance')


@pytest.mark.finding('T3-7')
def test_perturbation_check_final_none_refused_with_reason():
    msg = assert_q01_refused_and_q09_checked(
        constant(['acct.balance'], final=None), 'Q01')
    assert 'Q01: final is None on an item declared derivable; Q09' in msg


@pytest.mark.parametrize('vacuous', [
    'nope.balance', 'acct.nope', 'balance', 'acct.kind'])
def test_perturbation_check_vacuous_field_does_not_stop_later_fields(vacuous):
    with pytest.raises(SealError) as exc:
        perturbation_check(module(constant([vacuous, 'acct.balance'])),
                           FIXTURE, questions('Q01'))
    assert str(exc.value).endswith(
        'Q01: ' + UNCHANGED.format('acct.balance'))


def test_perturbation_check_non_numeric_field_beside_a_numeric_one_passes():
    # acct.kind cannot be perturbed, but acct.balance was, and moved the
    # output: the item passes.
    mod = module(lambda i, ctx: {
        'final': Decimal(ctx['acct']['balance']),
        'source_fields_consumed': ['acct.kind', 'acct.balance']})
    assert perturbation_check(mod, FIXTURE, questions('Q01')) == []


@pytest.mark.finding('T3-7')
@pytest.mark.parametrize('value', ['NaN', 'Infinity', '-inf', 'sNaN'])
def test_perturbation_check_non_finite_fields_are_not_numeric(value):
    # Decimal parses these, but no perturbation of them is meaningful.
    fixture = {'accounts': [{'id': 'acct', 'x': value, 'y': 'text'}]}
    mod = module(constant(['acct.x', 'acct.y']))
    with pytest.raises(SealError) as exc:
        perturbation_check(mod, fixture, questions('Q01'))
    assert str(exc.value) == PERTURBATION_REFUSED + (
        'Q01: no declared source field could be perturbed: '
        'acct.x, acct.y not numeric')


@pytest.mark.finding('T3-7')
@pytest.mark.parametrize('result', [
    {'derivable': False},
    {'derivable': False, 'final': Decimal('42'),
     'source_fields_consumed': ['acct.balance']},
])
def test_perturbation_check_non_derivable_item_exempt(result):
    # Only an item declared non-derivable is exempt; it is computed once
    # and not perturbed. Q09 is still checked.
    mod = recording(lambda i, ctx: dict(result) if i == 'Q01'
                    else constant(['other.balance'])(i, ctx))
    qs = questions('Q01', 'Q09', accounts=['acct', 'other'])
    with pytest.raises(SealError) as exc:
        perturbation_check(mod, FIXTURE, qs)
    assert str(exc.value) == PERTURBATION_REFUSED + \
        'Q09: ' + UNCHANGED.format('other.balance')
    assert [i for i, _ in mod.seen].count('Q01') == 1


# -- source_fields_check ----------------------------------------------------

def reads(*fields, declared=None, via_get=()):
    def compute(item_id, ctx):
        for f in fields:
            acct, name = f.split('.', 1)
            ctx[acct][name]
        for f in via_get:
            acct, name = f.split('.', 1)
            ctx[acct].get(name)
        out = {'final': Decimal('1')}
        if declared is not None:
            out['source_fields_consumed'] = list(declared)
        return out
    return compute


def test_source_fields_check_declared_reads_return_empty_list():
    mod = module(reads('acct.balance', declared=['acct.balance', 'acct.rate']))
    assert source_fields_check(mod, FIXTURE, questions('Q01')) == []


@pytest.mark.req('R3.1')
def test_source_fields_check_undeclared_read_raises_naming_fields():
    mod = module(reads('acct.rate', 'acct.balance', 'acct.kind',
                       declared=['acct.balance']))
    with pytest.raises(SealError) as exc:
        source_fields_check(mod, FIXTURE, questions('Q01'))
    assert str(exc.value) == (
        "source fields check failed: Q01: reads undeclared fields "
        "['acct.kind', 'acct.rate']")


def test_source_fields_check_no_declaration_means_every_read_undeclared():
    mod = module(reads('acct.balance'))
    with pytest.raises(SealError, match=r"Q01: reads undeclared fields \['acct.balance'\]$"):
        source_fields_check(mod, FIXTURE, questions('Q01'))


def test_source_fields_check_items_joined():
    mod = module(reads('acct.balance', declared=[]))
    with pytest.raises(SealError) as exc:
        source_fields_check(mod, FIXTURE, questions('Q01', 'Q02'))
    assert str(exc.value) == (
        "source fields check failed: "
        "Q01: reads undeclared fields ['acct.balance']; "
        "Q02: reads undeclared fields ['acct.balance']")


def test_source_fields_check_compute_gets_tracking_context_of_sources():
    seen = []

    def compute(item_id, ctx):
        seen.append(ctx)
        return {'final': 1, 'source_fields_consumed': []}
    source_fields_check(module(compute), FIXTURE,
                        questions('Q01', accounts=['other']))
    assert isinstance(seen[0], TrackingContext)
    assert seen[0] == {'other': {'balance': '7'}}


def test_source_fields_check_item_without_source_accounts():
    seen = []

    def compute(item_id, ctx):
        seen.append(dict(ctx))
        return {'source_fields_consumed': []}
    assert source_fields_check(module(compute), FIXTURE,
                               {'items': [{'id': 'Q01'}]}) == []
    assert seen == [{}]


def test_source_fields_check_no_items_returns_empty_list():
    assert source_fields_check(module(reads('acct.balance')), FIXTURE, {}) == []


def test_source_fields_check_raising_item_does_not_stop_later_items():
    def compute(item_id, ctx):
        if item_id == 'Q01':
            raise ZeroDivisionError('boom')
        return reads('acct.rate', declared=[])(item_id, ctx)
    with pytest.raises(SealError) as exc:
        source_fields_check(module(compute), FIXTURE, questions('Q01', 'Q02'))
    assert str(exc.value) == (
        "source fields check failed: "
        "Q01: compute raised ZeroDivisionError: boom; "
        "Q02: reads undeclared fields ['acct.rate']")


# -- the shipped example module --------------------------------------------
# The live run calls the guards before sealing (T3-7); these check the
# example ground-truth module directly. Read only.

EXAMPLE = Path(__file__).resolve().parents[3] / 'example'


@pytest.fixture(scope='module')
def example():
    spec = importlib.util.spec_from_file_location(
        '_s3_g3_ground_truth_example', EXAMPLE / 'ground_truth_example.py')
    gt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gt)
    load = lambda name: json.loads(  # noqa: E731
        (EXAMPLE / name).read_text(encoding='utf-8'))
    return gt, load('fixture.json'), load('questions.json')


def test_perturbation_check_passes_example_module(example):
    assert perturbation_check(*example) == []


def test_source_fields_check_passes_example_module(example):
    assert source_fields_check(*example) == []


# --- Step 4: correct behaviour (failing until fixed) ---
# Group g3-seal-guards. Each test asserts the correct behaviour and is
# xfail(strict) until the fix; see inbox/2026-10-20_step4-g3-seal-guards-report.md.

def refusal_of(check, *args, **kwargs):
    """The SealError message of a guard, or None if the guard passed.
    (Not pytest.raises: its DID NOT RAISE is not an AssertionError, and
    these tests must fail at their assertion.)"""
    try:
        check(*args, **kwargs)
    except SealError as exc:
        return str(exc)
    return None


@pytest.mark.finding('T3-7')
@pytest.mark.req('R3.1')
@pytest.mark.parametrize('declared', [
    None, [], ['nope.balance'], ['acct.nope'], ['balance'], ['acct.kind']],
    ids=['missing-key', 'none', 'unknown-account', 'unknown-field', 'no-dot',
         'non-numeric'])
def test_perturbation_check_vacuous_declaration_refused(declared):
    # Correct (SPEC R3.1, l.686-694: "A constant-returning module is
    # refused, perturbation named"): a derivable item whose declaration
    # gives the check nothing to perturb (no fields, an account or field
    # not in the delivered context, a spec with no dot, a non-numeric
    # field) cannot be shown to compute its answer, so it is refused, and
    # the refusal names the declaration it could not perturb. Today every
    # one of these is skipped with a silent `continue` and the module
    # returning Decimal('42') passes.
    def compute(item_id, ctx):
        out = {'final': Decimal('42'), 'derivable': True}
        if declared is not None:
            out['source_fields_consumed'] = list(declared)
        return out
    msg = refusal_of(perturbation_check, module(compute), FIXTURE,
                     questions('Q01'))
    assert msg is not None, 'constant module passed perturbation_check'
    for spec in declared or []:
        assert spec in msg


@pytest.mark.finding('T3-7')
@pytest.mark.req('R3.1')
def test_perturbation_check_final_none_on_derivable_item_refused():
    # Correct: only an item declared non-derivable may be exempt (SPEC
    # R1.2 "item selection"; R3.1). A derivable item with no final value
    # has no expected value to score against, so the module is refused,
    # naming the item. Today `if baseline_final is None: continue`.
    def compute(item_id, ctx):
        return {'final': None, 'derivable': True,
                'source_fields_consumed': ['acct.balance']}
    msg = refusal_of(perturbation_check, module(compute), FIXTURE,
                     questions('Q01'))
    assert msg is not None, 'final None on a derivable item passed'
    assert 'Q01' in msg


@pytest.mark.finding('T3-8')
@pytest.mark.req('R3.1')
@pytest.mark.parametrize('read', [
    lambda acct: acct.get('rate'),
    lambda acct: [v for k, v in acct.items() if k == 'rate'],
    lambda acct: list(acct.values()),
    lambda acct: acct.copy()['rate'],
    lambda acct: dict(acct)['rate'],
    lambda acct: {**acct}['rate'],
], ids=['get', 'items', 'values', 'copy', 'dict', 'unpack'])
def test_source_fields_check_undeclared_read_by_any_path_refused_naming_field(
        read):
    # Correct (source_fields_check's own contract, R3.1: "A module reading
    # a field NOT in source_fields_consumed is refused, with the field
    # named"): every path that hands the module a field's value counts as
    # a read. The module declares acct.balance and also reads acct.rate,
    # through a path other than a subscript. Today only __getitem__ is
    # tracked and the check returns [].
    def compute(item_id, ctx):
        acct = ctx['acct']
        acct['balance']
        read(acct)
        return {'final': Decimal('1'),
                'source_fields_consumed': ['acct.balance']}
    msg = refusal_of(source_fields_check, module(compute), FIXTURE,
                     questions('Q01'))
    assert msg is not None, 'undeclared read of acct.rate passed'
    assert 'acct.rate' in msg


@pytest.mark.finding('S3-G3-3')
@pytest.mark.req('R3.1')
def test_source_fields_check_compute_raising_refused_naming_the_error():
    # Correct: the refusal says what went wrong. A compute that raises is
    # refused (fail closed, as today) with the exception named, not as a
    # module that "reads undeclared fields ... accessed []". The reason is
    # built in the failure dict today and then dropped.
    def compute(item_id, ctx):
        raise ZeroDivisionError('boom')
    msg = refusal_of(source_fields_check, module(compute), FIXTURE,
                     questions('Q01'))
    assert msg is not None
    assert 'ZeroDivisionError' in msg and 'boom' in msg
    assert 'reads undeclared fields' not in msg


@pytest.mark.finding('S3-G3-3')
@pytest.mark.req('R3.1')
@pytest.mark.parametrize('when', ['baseline', 'perturbed'])
def test_perturbation_check_compute_raising_refused_naming_the_error(when):
    # Correct: a compute that raises (on the baseline or on the perturbed
    # context) is refused with the exception named. Today the refusal says
    # "constant-returning module detected. Fields that had no effect:
    # (baseline)" or names the field, and the exception text is dropped.
    def compute(item_id, ctx):
        if when == 'baseline' or ctx['acct']['balance'] != '100':
            raise KeyError('missing-input')
        return {'final': Decimal(ctx['acct']['balance']),
                'source_fields_consumed': ['acct.balance']}
    msg = refusal_of(perturbation_check, module(compute), FIXTURE,
                     questions('Q01'))
    assert msg is not None
    assert 'KeyError' in msg and 'missing-input' in msg


@pytest.mark.finding('S3-G3-3')
@pytest.mark.req('R3.1')
def test_perturbation_check_constant_module_refusal_names_the_perturbation():
    # Correct (SPEC R3.1, l.688-694: refused "with the perturbation
    # named"): the refusal says which item, which field and what was done
    # to it (the factor). Today the failure dict's reason ("output
    # unchanged when acct.balance perturbed by factor 1.1") is dropped and
    # the message names the field only.
    msg = refusal_of(perturbation_check, module(constant(['acct.balance'])),
                     FIXTURE, questions('Q01'))
    assert msg is not None
    assert 'Q01' in msg and 'acct.balance' in msg and '1.1' in msg


def full_seal(files, config=CONFIG, **kwargs):
    """A seal that is valid after every fix: the AP-1 text is passed and
    its hash declared (T3-68 makes both required)."""
    config = {**config, 'ap1_text_hash': files.hashes['ap1_text']}
    return seal(config=config, **files.kwargs,
                ap1_text_path=files.paths['ap1_text'], **kwargs)


def full_verify(record, files, config=CONFIG, **kwargs):
    config = {**config, 'ap1_text_hash': files.hashes['ap1_text']}
    return verify_seal(record, config=config, **files.kwargs, **kwargs)


def _refused(fn):
    """Call fn; return the SealError it raises, or None if it returned."""
    try:
        fn()
    except SealError as e:
        return e
    return None


@pytest.mark.finding('T3-47')
@pytest.mark.req('R1.1')
def test_seal_hash_two_timestamps_give_two_hashes(files, monkeypatch):
    # Correct (AP-1 v1.3 §5.3 "hashed and timestamped before execution";
    # SPEC R1.1 "hash and timestamp"): the timestamp is bound by seal_hash,
    # so a backdated timestamp no longer matches the hash.
    stamps = iter(['2020-01-01T00:00:00+00:00', '2026-10-15T00:00:00+00:00'])

    class Clock:
        @staticmethod
        def now(tz=None):
            return SimpleNamespace(isoformat=lambda s=next(stamps): s)
    monkeypatch.setattr(seal_mod, 'datetime', Clock)
    first, second = full_seal(files), full_seal(files)
    assert first['seal_hash'] != second['seal_hash']


@pytest.mark.finding('T3-68')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('declared', ['placeholder', '', None])
def test_seal_placeholder_or_blank_declared_ap1_hash_refused(
        files, frozen, declared):
    # Correct (SPEC R1.1 verification item 3: "A run claiming conformance
    # to an AP-1 text whose hash is absent from the record is refused"):
    # without a real declared hash there is nothing to check the text
    # against, so the seal is refused.
    config = {k: v for k, v in CONFIG.items() if k != 'ap1_text_hash'}
    if declared is not None:
        config['ap1_text_hash'] = declared
    error = _refused(lambda: make_seal(
        files, config=config, ap1_text_path=files.paths['ap1_text']))
    assert error is not None, 'sealed with declared hash %r' % declared
    assert 'AP-1 text' in str(error)


@pytest.mark.finding('T3-68')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('path', [None, ''])
def test_seal_without_ap1_text_path_refused(files, frozen, path):
    # Correct (SPEC R1.1 verification item 3): the AP-1 text is a required
    # sealed input; a declared hash that no file was hashed against is
    # refused.
    config = {**CONFIG, 'ap1_text_hash': files.hashes['ap1_text']}
    error = _refused(lambda: make_seal(files, config=config,
                                       ap1_text_path=path))
    assert error is not None, 'sealed without an AP-1 text file'


SEALED_FIELDS = [
    ('seal_hash', '0' * 64), ('timestamp', '1970-01-01T00:00:00+00:00'),
    ('runner_source_hash', 'f' * 64), ('verification_keys', ['k']),
    ('ev3_implemented', True), ('ap1_version', '9.9'),
    ('runner_version_tag', 'v9'), ('runner_version_commit', 'fff'),
    ('ap1_text_hash', 'a' * 64)]
# A rewritten ap1_version_doi is refused today (both sides set), so it is
# only in the deletion test.


@pytest.mark.finding('T3-17', 'T3-19', 'T3-47')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('field, value', SEALED_FIELDS)
def test_verify_seal_any_rewritten_field_refused_naming_it(
        files, frozen, field, value):
    # Correct (SPEC R1.1: "Modifying any sealed input causes the scorer to
    # refuse, naming the mismatch"): verify_seal recomputes seal_hash over
    # the record and refuses a record any field of which was rewritten,
    # naming the field or the seal_hash mismatch. Here the inputs are
    # unchanged and no AP-1 text path is passed.
    record = full_seal(files)
    record[field] = value
    error = _refused(lambda: full_verify(record, files))
    assert error is not None, '%s rewritten, verify_seal returned True' % field
    assert field in str(error) or 'seal_hash' in str(error)


@pytest.mark.finding('T3-17')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('field', [k for k, _ in SEALED_FIELDS
                                   if k != 'seal_hash'] + ['ap1_version_doi'])
def test_verify_seal_deleted_field_refused(files, frozen, field):
    # Correct: a record missing a field the seal always writes is not a
    # valid record (SPEC R1.1 "A run that starts without a valid record is
    # refused"); seal_hash no longer matches.
    record = full_seal(files)
    del record[field]
    assert _refused(lambda: full_verify(record, files)) is not None, \
        '%s deleted, verify_seal returned True' % field


@pytest.mark.finding('T3-17')
@pytest.mark.req('R1.1')
@pytest.mark.parametrize('sealed, current', [('', 'doi'), ('doi', '')])
def test_verify_seal_doi_on_one_side_only_named_as_mismatch(
        files, frozen, sealed, current):
    # Correct: a DOI present on one side only is a DOI mismatch, named as
    # such (today only the config hash line appears).
    config = {**CONFIG, 'ap1_version_doi': sealed}
    record = full_seal(files, config=config)
    error = _refused(lambda: full_verify(
        record, files, config={**config, 'ap1_version_doi': current}))
    assert error is not None
    assert 'ap1_version_doi' in str(error)


# T3-50: sealed file hashes and line endings. Decision (step 4, g5): the
# sealed text inputs (fixture, questions, ground-truth module) are hashed
# after normalising line endings to LF and dropping a UTF-8 byte-order
# mark, so the same content gives the same digest on every platform and in
# every editor (SPEC R0.4.3 verification item 1: "on two platforms, yields
# identical digests"; README "LF on all sealed files"). An LF file without
# a BOM hashes exactly as today. The AP-1 text is the exception: it is
# byte-significant, its hash must equal the publisher's deposit
# (.gitattributes: "reference/** -text"), so it stays raw bytes.

LF_TEXT = b'{"accounts": [\n  "a"\n]}\n'
VARIANTS = {'crlf': LF_TEXT.replace(b'\n', b'\r\n'),
            'cr': LF_TEXT.replace(b'\n', b'\r'),
            'bom': b'\xef\xbb\xbf' + LF_TEXT,
            'bom_crlf': b'\xef\xbb\xbf' + LF_TEXT.replace(b'\n', b'\r\n')}


@pytest.mark.finding('T3-50')
@pytest.mark.req('R0.4.3')
@pytest.mark.parametrize('name', ['fixture', 'questions', 'ground_truth'])
@pytest.mark.parametrize('variant', sorted(VARIANTS))
def test_seal_text_input_hash_independent_of_line_endings_and_bom(
        files, frozen, name, variant):
    files.paths[name].write_bytes(LF_TEXT)
    lf = full_seal(files)['%s_hash' % name]
    files.paths[name].write_bytes(VARIANTS[variant])
    assert full_seal(files)['%s_hash' % name] == lf == sha(LF_TEXT)


# -- Step 5 (report-honesty): lookup collisions recorded at seal (T3-75) --

@pytest.mark.finding('T3-75')
@pytest.mark.req('R3.1')
@pytest.mark.parametrize('collisions, text', [
    ([('Q09', 'checking.atm_fee')], 'Q09 (checking.atm_fee)'),
    ([('Q01', 'a.x'), ('Q04', 'b.y')], 'Q01 (a.x); Q04 (b.y)'),
    ([], 'none')])
def test_seal_records_lookup_collisions_in_the_hash(files, frozen,
                                                    collisions, text):
    record = make_seal(files, lookup_collisions=collisions)
    assert record['lookup_collisions'] == text
    assert record['seal_hash'] == seal_mod.record_hash(record)
    assert record['seal_hash'] != make_seal(files)['seal_hash']


def test_seal_without_lookup_collisions_has_no_field(files, frozen):
    assert 'lookup_collisions' not in make_seal(files)
