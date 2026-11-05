"""The live runner's API key (Rule 0c).

The key comes from the AP1_SMOKE_API_KEY environment variable or, on
Windows only, from the Credential Manager. It is never printed, logged
or written to any file.
"""

import os
import sys


# Credential target for the API key
CRED_TARGET = 'ap1-smoke:openai'


def read_credential_windows(target):
    """Read a credential from Windows Credential Manager via ctypes.

    Only called on Windows when AP1_SMOKE_API_KEY is not set.
    Returns the credential blob as a string, or None if not found.
    """
    try:
        import ctypes
        import ctypes.wintypes
    except ImportError:
        return None

    CRED_TYPE_GENERIC = 1

    class CREDENTIAL(ctypes.Structure):
        _fields_ = [
            ("Flags", ctypes.wintypes.DWORD),
            ("Type", ctypes.wintypes.DWORD),
            ("TargetName", ctypes.c_wchar_p),
            ("Comment", ctypes.c_wchar_p),
            ("LastWritten", ctypes.wintypes.FILETIME),
            ("CredentialBlobSize", ctypes.wintypes.DWORD),
            ("CredentialBlob", ctypes.c_void_p),
            ("Persist", ctypes.wintypes.DWORD),
            ("AttributeCount", ctypes.wintypes.DWORD),
            ("Attributes", ctypes.c_void_p),
            ("TargetAlias", ctypes.c_wchar_p),
            ("UserName", ctypes.c_wchar_p),
        ]

    pcred = ctypes.POINTER(CREDENTIAL)()
    ok = ctypes.windll.advapi32.CredReadW(
        target, CRED_TYPE_GENERIC, 0, ctypes.byref(pcred))

    if not ok:
        return None

    blob = ctypes.string_at(
        pcred.contents.CredentialBlob, pcred.contents.CredentialBlobSize)
    # Decode UTF-16LE (Windows credential store encoding)
    value = blob.decode('utf-16-le').rstrip('\x00')
    ctypes.windll.advapi32.CredFree(pcred)
    return value


def get_api_key():
    """Resolve the API key. Never prints, logs, or writes the value.

    Priority:
      1. AP1_SMOKE_API_KEY environment variable (all platforms)
      2. Windows Credential Manager (Windows only, target: ap1-smoke:openai)

    Raises SystemExit with platform-appropriate setup instructions if
    neither source provides a key.
    """
    key = os.environ.get('AP1_SMOKE_API_KEY')
    if key:
        return key

    # Windows-only fallback: Credential Manager
    if sys.platform == 'win32':
        key = read_credential_windows(CRED_TARGET)
        if key:
            return key

    # Neither source provided a key -- error with setup instructions
    print('ERROR: API key not found.')
    print()
    print('Set the AP1_SMOKE_API_KEY environment variable:')
    print()
    if sys.platform == 'win32':
        print('  cmd:         set AP1_SMOKE_API_KEY=<key>')
        print("  PowerShell:  $env:AP1_SMOKE_API_KEY = '<key>'")
        print()
        print('Or store in Windows Credential Manager:')
        print(f'  Target: {CRED_TARGET}')
        print('  User name: ap1-smoke')
        print('  Password: <the API key>')
    else:
        print('  export AP1_SMOKE_API_KEY=<key>')
    print()
    print('The key is never printed, logged, or written to any file.')
    sys.exit(1)
