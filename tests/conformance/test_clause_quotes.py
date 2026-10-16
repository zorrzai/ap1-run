"""The clause quotes in test_ap1_clauses.py are verbatim.

Each quote ("> " lines, "[...]" for an elision) must occur in
reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md within the lines cited, ignoring
Markdown emphasis, blockquote markers, line breaks and dash or quote
typography. Legacy verify_conformance.py claimed verbatim quotes, but nine
of its nineteen were paraphrased or cited the wrong lines.
"""

import ast
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT / 'reference' / 'AP-1_v1.3_DRAFT_FOR_COMMENT.md'
CLAUSE_TESTS = Path(__file__).with_name('test_ap1_clauses.py')
CITATION = re.compile(r'\(AP-1 v1\.3 (?P<clause>[^,]+), L(?P<lo>\d+)'
                      r'(?:-(?P<hi>\d+))?\)')


def normalise(text):
    text = re.sub(r'^\s*>\s?', '', text, flags=re.MULTILINE)
    for a, b in (('**', ''), ('*', ''), ('`', ''), ('—', '-'),
                 ('–', '-'), ('−', '-'), ('“', '"'),
                 ('”', '"'), ('’', "'")):
        text = text.replace(a, b)
    return re.sub(r'\s+', ' ', text).strip()


def quoted_tests():
    tree = ast.parse(CLAUSE_TESTS.read_text(encoding='utf-8'))
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        doc = ast.get_docstring(node) or ''
        cite = CITATION.search(doc)
        if not cite:
            continue
        lines = doc.splitlines()
        segments, current = [], []
        for line in lines:
            if line.startswith('> '):
                current.append(line[2:])
            elif line.strip() == '[...]':
                segments.append(' '.join(current))
                current = []
        segments.append(' '.join(current))
        lo = int(cite['lo'])
        hi = int(cite['hi'] or lo)
        yield pytest.param(node.name, [s for s in segments if s.strip()],
                           lo, hi, id=node.name)


QUOTED = list(quoted_tests())


def test_every_clause_test_module_quote_is_found():
    assert len(QUOTED) == 22


@pytest.mark.parametrize('name, segments, lo, hi', QUOTED)
def test_clause_quote_is_verbatim_at_cited_lines(name, segments, lo, hi):
    lines = REFERENCE.read_text(encoding='utf-8').splitlines()
    window = normalise('\n'.join(lines[lo - 1:hi]))
    assert segments
    for segment in segments:
        assert normalise(segment) in window, (name, segment)
