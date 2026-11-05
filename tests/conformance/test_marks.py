"""The test marks are used as pyproject.toml describes them.

- ``proposal(reason)``: one non-empty reason string, on a test that also
  names its finding, so ``pytest -m proposal`` lists every expectation that
  rests on the author's proposal rather than SPEC, AP-1 or a maintainer
  decision.
- A strict xfail is a test of the correct behaviour for a finding, so it
  carries a ``finding`` mark.

The marks are read from a collection of the whole suite in a subprocess
(marks_plugin.py), not from this session's items, so a run of one file, a
-k or a -m selection still checks every test. Floors on the counts make a
collection that finds nothing (a broken plugin, a path error) fail.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]

# Counts at the time of writing, without inspect-ai (its test files skip
# whole). New tests raise them; a fall below means marks were lost.
MIN_PROPOSAL_FUNCTIONS = 40
MIN_STRICT_XFAIL_CASES = 430


@pytest.fixture(scope='module')
def collected(tmp_path_factory):
    dump = tmp_path_factory.mktemp('marks') / 'marks.json'
    env = dict(os.environ, AP1_MARKS_DUMP=str(dump),
               PYTHONPATH=os.pathsep.join(
                   [str(ROOT / 'tests' / 'conformance'), str(ROOT / 'src'),
                    os.environ.get('PYTHONPATH', '')]))
    result = subprocess.run(
        [sys.executable, '-B', '-m', 'pytest', '--collect-only', '-q',
         '-p', 'no:cacheprovider', '-p', 'marks_plugin'],
        cwd=ROOT, env=env, capture_output=True, text=True)
    assert dump.exists(), result.stdout[-2000:] + result.stderr[-2000:]
    return json.loads(dump.read_text('utf-8'))


def test_marks_collection_covers_the_suite(collected):
    proposal = {t['nodeid'].split('[')[0] for t in collected if t['proposal']}
    strict = [t for t in collected if t['strict_xfail']]
    assert len(proposal) >= MIN_PROPOSAL_FUNCTIONS, sorted(proposal)
    assert len(strict) >= MIN_STRICT_XFAIL_CASES, len(strict)


def test_proposal_marks_have_a_reason_and_a_finding(collected):
    bad = []
    for t in collected:
        for mark in t['proposal']:
            args = mark['args']
            if (len(args) != 1 or not isinstance(args[0], str)
                    or not args[0].strip() or mark['kwargs']):
                bad.append((t['nodeid'], 'reason'))
        if t['proposal'] and not t['finding']:
            bad.append((t['nodeid'], 'no finding mark'))
    assert bad == []


def test_strict_xfails_name_their_finding(collected):
    bad = [t['nodeid'] for t in collected
           if t['strict_xfail'] and not t['finding']]
    assert bad == []
