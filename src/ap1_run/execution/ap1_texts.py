"""The AP-1 texts, per version (V12-4).

The AP-1 text a run seals is chosen by the config's ap1_version, from a
table: one entry per AP-1 version, with the text's path under the
repository root and its SHA-256 (the publisher's deposit, byte for
byte). A run that
declares a version of the table seals that version's text, and only that
text: the seal never puts a version label over another version's text.
"""

import os

from ap1_run.execution.seal import SealError

# Version -> the AP-1 text. The v1.2 text is AP-1_Admissibility_Protocol_
# v1.2.md and the v1.3 draft AP-1_v1.3_DRAFT_FOR_COMMENT.md, as published
# in github.com/zorrzai/admissibility-protocol.
AP1_TEXTS = {
    'v1.3': {
        'path': os.path.join('reference', 'AP-1_v1.3_DRAFT_FOR_COMMENT.md'),
        'sha256': ('48e7826fc7807880ab98694b394bd020'
                   'da070fb1d9c212e383f7c70bd819cf56'),
    },
    'v1.2': {
        'path': os.path.join('reference', 'AP-1_Admissibility_Protocol_v1.2.md'),
        'sha256': ('14659fc1c2a3357c22081a9109841475'
                   '861c34f2b315ee7eb546e80fecbb58a5'),
    },
}


def ap1_text_entry(ap1_version):
    """The table entry of an ap1_version: the version itself ('v1.3'), or
    the version followed by '-' and a qualifier
    ('v1.3-draft-for-comment-20260730'). None for any other version."""
    for version, entry in AP1_TEXTS.items():
        if ap1_version == version or str(ap1_version).startswith(
                version + '-'):
            return entry
    return None


def resolve_ap1_text(config, explicit_path, base_dir):
    """The path of the AP-1 text to seal: explicit_path (--ap1-text) if
    given, else the table's text for the config's ap1_version, under
    base_dir. SealError if neither names a text."""
    if explicit_path:
        return explicit_path
    version = config.get('ap1_version', '')
    entry = ap1_text_entry(version)
    if entry is None:
        raise SealError(
            f'AP-1 text: no text is known for ap1_version {version!r} '
            f'(known: {", ".join(AP1_TEXTS)}); give it with --ap1-text')
    return os.path.join(base_dir, entry['path'])


def check_ap1_text_version(config, record):
    """SealError if the sealed AP-1 text is not the text of the declared
    version: for a version in the table, the sealed hash must be the
    table's. A version outside the table is the operator's to vouch for
    (the text was given with --ap1-text and matched the declared hash)."""
    version = config.get('ap1_version')
    entry = ap1_text_entry(version)
    if entry is not None and record.get('ap1_text_hash') != entry['sha256']:
        raise SealError(
            f'AP-1 text: the sealed text hashes to '
            f'{record.get("ap1_text_hash")!r}, which is not the AP-1 '
            f'{version} text ({entry["sha256"]!r})')
