"""Unit tests for the runner's API-key resolution (Rule 0c): the
environment variable, then (Windows only) the Credential Manager."""

import sys
import types

import pytest

from ap1_run.runner import credentials as module
from ap1_run.runner.credentials import (
    CRED_TARGET, get_api_key, read_credential_windows,
)


@pytest.fixture
def no_key(monkeypatch):
    monkeypatch.delenv('AP1_SMOKE_API_KEY', raising=False)


def test_credential_target_name():
    assert CRED_TARGET == 'ap1-smoke:openai'


def test_get_api_key_from_environment(monkeypatch, capsys):
    monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-test-123')
    assert get_api_key() == 'sk-test-123'
    assert capsys.readouterr().out == ''


def test_get_api_key_empty_environment_value_counts_as_missing(
        monkeypatch, capsys):
    monkeypatch.setenv('AP1_SMOKE_API_KEY', '')
    monkeypatch.setattr(sys, 'platform', 'linux')
    with pytest.raises(SystemExit):
        get_api_key()


def test_get_api_key_missing_prints_instructions_and_exits_1(
        no_key, monkeypatch, capsys):
    monkeypatch.setattr(sys, 'platform', 'linux')
    monkeypatch.setattr(module, 'read_credential_windows',
                        lambda target: pytest.fail('not on Windows'))
    with pytest.raises(SystemExit) as exc:
        get_api_key()
    assert exc.value.code == 1
    assert capsys.readouterr().out == (
        'ERROR: API key not found.\n'
        '\n'
        'Set the AP1_SMOKE_API_KEY environment variable:\n'
        '\n'
        '  export AP1_SMOKE_API_KEY=<key>\n'
        '\n'
        'The key is never printed, logged, or written to any file.\n')


def test_get_api_key_windows_reads_credential_manager(
        no_key, monkeypatch, capsys):
    monkeypatch.setattr(sys, 'platform', 'win32')
    seen = []

    def fake_read(target):
        seen.append(target)
        return 'sk-from-store'
    monkeypatch.setattr(module, 'read_credential_windows', fake_read)
    assert get_api_key() == 'sk-from-store'
    assert seen == ['ap1-smoke:openai']
    assert capsys.readouterr().out == ''


def test_get_api_key_windows_missing_prints_windows_instructions(
        no_key, monkeypatch, capsys):
    monkeypatch.setattr(sys, 'platform', 'win32')
    monkeypatch.setattr(module, 'read_credential_windows', lambda t: None)
    with pytest.raises(SystemExit) as exc:
        get_api_key()
    assert exc.value.code == 1
    assert capsys.readouterr().out == (
        'ERROR: API key not found.\n'
        '\n'
        'Set the AP1_SMOKE_API_KEY environment variable:\n'
        '\n'
        '  cmd:         set AP1_SMOKE_API_KEY=<key>\n'
        "  PowerShell:  $env:AP1_SMOKE_API_KEY = '<key>'\n"
        '\n'
        'Or store in Windows Credential Manager:\n'
        '  Target: ap1-smoke:openai\n'
        '  User name: ap1-smoke\n'
        '  Password: <the API key>\n'
        '\n'
        'The key is never printed, logged, or written to any file.\n')


def test_get_api_key_environment_wins_over_credential_manager(
        monkeypatch):
    monkeypatch.setenv('AP1_SMOKE_API_KEY', 'sk-env')
    monkeypatch.setattr(sys, 'platform', 'win32')
    monkeypatch.setattr(module, 'read_credential_windows',
                        lambda target: pytest.fail('env var comes first'))
    assert get_api_key() == 'sk-env'


# -- _read_credential_windows, against a fake ctypes ----------------------

WIN32_CREDENTIAL_FIELDS = [
    ('Flags', 'DWORD'), ('Type', 'DWORD'), ('TargetName', 'c_wchar_p'),
    ('Comment', 'c_wchar_p'), ('LastWritten', 'FILETIME'),
    ('CredentialBlobSize', 'DWORD'), ('CredentialBlob', 'c_void_p'),
    ('Persist', 'DWORD'), ('AttributeCount', 'DWORD'),
    ('Attributes', 'c_void_p'), ('TargetAlias', 'c_wchar_p'),
    ('UserName', 'c_wchar_p'),
]


class FakeCtypes:
    """Just enough of ctypes for _read_credential_windows, recording the
    calls it makes."""

    def __init__(self, stored=None):
        self.stored = stored  # bytes of the blob, or None: not found
        self.calls = []
        self.structure = None
        ctypes_mod = types.ModuleType('ctypes')
        wintypes = types.ModuleType('ctypes.wintypes')
        wintypes.DWORD = 'DWORD'
        wintypes.FILETIME = 'FILETIME'
        ctypes_mod.wintypes = wintypes
        ctypes_mod.c_wchar_p = 'c_wchar_p'
        ctypes_mod.c_void_p = 'c_void_p'
        ctypes_mod.Structure = type('Structure', (), {})
        ctypes_mod.POINTER = self.pointer
        ctypes_mod.byref = lambda obj: ('byref', obj)
        ctypes_mod.string_at = self.string_at
        advapi32 = types.SimpleNamespace(CredReadW=self.cred_read,
                                         CredFree=self.cred_free)
        ctypes_mod.windll = types.SimpleNamespace(advapi32=advapi32)
        self.modules = {'ctypes': ctypes_mod, 'ctypes.wintypes': wintypes}

    def pointer(self, structure):
        self.structure = structure
        return lambda: types.SimpleNamespace(contents=None)

    def cred_read(self, target, cred_type, flags, ref):
        self.calls.append(('CredReadW', target, cred_type, flags))
        if self.stored is None:
            return 0
        ref[1].contents = types.SimpleNamespace(
            CredentialBlob='blob-address',
            CredentialBlobSize=len(self.stored))
        return 1

    def string_at(self, address, size):
        self.calls.append(('string_at', address, size))
        return self.stored[:size]

    def cred_free(self, pcred):
        self.calls.append(('CredFree', pcred.contents.CredentialBlob))


def test_read_credential_windows_decodes_utf16_and_frees(monkeypatch):
    # Only trailing NULs are stripped (a key may end in any character).
    fake = FakeCtypes(stored='sk-storedX\x00'.encode('utf-16-le'))
    for name, mod in fake.modules.items():
        monkeypatch.setitem(sys.modules, name, mod)
    assert read_credential_windows('ap1-smoke:openai') == 'sk-storedX'
    assert fake.calls == [
        ('CredReadW', 'ap1-smoke:openai', 1, 0),
        ('string_at', 'blob-address', 22),
        ('CredFree', 'blob-address'),
    ]
    assert fake.structure.__name__ == 'CREDENTIAL'
    assert fake.structure._fields_ == WIN32_CREDENTIAL_FIELDS


def test_read_credential_windows_not_found_is_none(monkeypatch):
    fake = FakeCtypes(stored=None)
    for name, mod in fake.modules.items():
        monkeypatch.setitem(sys.modules, name, mod)
    assert read_credential_windows('other-target') is None
    assert fake.calls == [('CredReadW', 'other-target', 1, 0)]


def test_read_credential_windows_without_ctypes_is_none(monkeypatch):
    monkeypatch.setitem(sys.modules, 'ctypes', None)
    assert read_credential_windows('ap1-smoke:openai') is None


def test_read_credential_windows_without_wintypes_is_none(monkeypatch):
    fake = FakeCtypes()
    monkeypatch.setitem(sys.modules, 'ctypes', fake.modules['ctypes'])
    monkeypatch.setitem(sys.modules, 'ctypes.wintypes', None)
    assert read_credential_windows('ap1-smoke:openai') is None
