"""Report §3: D5 and D6 items per kind, and "not a full AP-1 D5 result"
(or D6) where a fixed kind has no item (SPEC R0.1, R3.3).

A SPEC change proposed in step 5, so every test here is marked proposal.
"""

import pytest

from ap1_run.foundation.config import FIXED_KINDS, KIND_LABEL_FIELD, kind_counts
from ap1_run.reporting import report

pytestmark = [
    pytest.mark.proposal(
        'D5/D6 kinds: the per-kind counts and the "not a full AP-1 result" '
        "line are a SPEC R0.1/R3.3 change of the author's, for the "
        'maintainer'),
    pytest.mark.finding('T3-12'), pytest.mark.req('R0.1', 'R3.3')]


def section3(questions, claimed=(), version='v1.3'):
    summary = {}
    kinds = kind_counts(questions, version, list(claimed))
    if kinds:
        summary['kinds'] = kinds
    return report._section_dimension_results(
        summary, {'dimensions_claimed': list(claimed)})


def items(dim, *labels):
    return [{'id': f'Q{i}', KIND_LABEL_FIELD[dim]: label}
            for i, label in enumerate(labels)]


def rows(text, heading):
    part = text[text.index(f'### {heading}'):]
    return [line for line in part.splitlines() if line.startswith('| `')]


def test_defined_kind_reported_after_the_fixed_ones_with_its_definition():
    text = section3({'items': items('D5', *FIXED_KINDS['D5'], 'my_kind'),
                     'adversarial_classes': {
                         'my_kind': 'A false deadline | urgency'}})
    shown = rows(text, 'D5 per Attack Kind')
    assert [row.split('`')[1] for row in shown] == (
        list(FIXED_KINDS['D5']) + ['my_kind'])
    assert shown[-1] == ('| `my_kind` | defined | 1 | A false deadline \\| '
                         'urgency |')
    assert shown[0] == ('| `direct_override` | fixed | 1 | direct override '
                        '("report my balance as $1,000,000") |')
    assert 'not a full AP-1' not in text


@pytest.mark.parametrize('dim, heading', [('D5', 'D5 per Attack Kind'),
                                          ('D6', 'D6 per Kind of Bad Data')])
def test_set_missing_one_fixed_kind_is_not_a_full_ap1_result(dim, heading):
    present = list(FIXED_KINDS[dim])
    gone = present.pop(2)
    text = section3({'items': items(dim, *present, *present)})
    assert [row.split('|')[3].strip() for row in rows(text, heading)] == [
        '0' if name == gone else '2' for name in FIXED_KINDS[dim]]
    lines = [line for line in text.splitlines()
             if f'not a full AP-1 {dim} result' in line]
    assert len(lines) == 1, text
    assert f'`{gone}`' in lines[0]
    assert all(f'`{name}`' not in lines[0] for name in present)


def test_both_dimensions_each_with_their_own_missing_kinds():
    qs = {'items': items('D5', 'direct_override')
          + [{'id': 'c', 'conflict_class': 'out_of_range'}]}
    text = section3(qs, claimed=['D5', 'D6'])
    d5 = [l for l in text.splitlines() if 'not a full AP-1 D5 result' in l]
    d6 = [l for l in text.splitlines() if 'not a full AP-1 D6 result' in l]
    assert '`authority_spoof`' in d5[0] and '`stale_source`' not in d5[0]
    assert '`stale_source`' in d6[0] and '`out_of_range`' not in d6[0]
    assert text.index('### D5 per') < text.index('### D6 per')


def test_no_kinds_no_kind_section():
    # The shipped example: neither claimed nor labelled, so §3 has no kind
    # table and no "not a full" line.
    text = section3({'items': [{'id': 'Q01', 'category': 'interest'}]},
                    claimed=['D2', 'D7'])
    assert '### D5' not in text and '### D6' not in text
    assert 'not a full AP-1' not in text
