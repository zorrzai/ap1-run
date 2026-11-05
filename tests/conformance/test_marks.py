"""The test marks are used as pyproject.toml describes them.

- ``proposal(reason)``: one non-empty reason string, on a test that also
  names its finding, so ``pytest -m proposal`` lists every expectation that
  rests on the author's proposal rather than SPEC, AP-1 or a maintainer
  decision.
- A strict xfail is a test of the correct behaviour for a finding, so it
  carries a ``finding`` mark.
"""


def _items(request):
    return [item for item in request.session.items]


def test_proposal_marks_have_a_reason_and_a_finding(request):
    bad = []
    for item in _items(request):
        for mark in item.iter_markers('proposal'):
            if (len(mark.args) != 1 or not isinstance(mark.args[0], str)
                    or not mark.args[0].strip() or mark.kwargs):
                bad.append((item.nodeid, 'reason'))
            if item.get_closest_marker('finding') is None:
                bad.append((item.nodeid, 'no finding mark'))
    assert bad == []


def test_strict_xfails_name_their_finding(request):
    bad = [item.nodeid for item in _items(request)
           if any(m.kwargs.get('strict') for m in item.iter_markers('xfail'))
           and item.get_closest_marker('finding') is None]
    assert bad == []
