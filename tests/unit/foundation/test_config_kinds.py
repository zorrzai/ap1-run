"""D5's kinds of attack and D6's kinds of bad data (SPEC R0.1): AP-1's
fixed kinds, kinds a questions file defines, undefined labels refused at
load, and the per-kind counts the report shows (foundation/config.py).

The fixed names, the defined kinds and the "not a full AP-1 result" rule
are a SPEC change proposed in step 5, so every test here is marked
proposal. Each fixed kind's definition is checked against the AP-1 v1.3
line it quotes.
"""

import json
import re
from pathlib import Path

import pytest

from ap1_run.foundation.config import (
    DEFINED_KINDS_FIELD, FIXED_KINDS, KIND_LABEL_FIELD, REQUIRED_KINDS,
    ConfigError, kind_counts, validate_kinds,
)

REPO = Path(__file__).resolve().parents[3]
AP1_V13 = REPO / 'reference' / 'AP-1_v1.3_DRAFT_FOR_COMMENT.md'

KINDS = pytest.mark.proposal(
    'D5/D6 kinds: the fixed names, kinds defined in the questions file, '
    'refusal of undefined labels and the "not a full AP-1 result" line are '
    "a SPEC R0.1 change of the author's, for the maintainer")

pytestmark = [KINDS, pytest.mark.finding('T3-12'), pytest.mark.req('R0.1')]

# Each fixed kind's AP-1 v1.3 line (reference/), for D5 its entry in D5's
# list, for D6 its row of D6's class table.
AP1_LINES = {
    'direct_override': 281, 'authority_spoof': 282,
    'data_embedded_injection': 283,
    'multi_turn_false_premise_persuasion': 284,
    'control_plane_injection': 285, 'tool_description_injection': 286,
    'stale_source': 305, 'partial_receipt': 306,
    'internal_contradiction': 307, 'cross_source_disagreement': 308,
    'out_of_range': 309,
}


def items(dim, *labels):
    field = KIND_LABEL_FIELD[dim]
    return [{'id': f'Q{i}', field: label} for i, label in enumerate(labels)]


def test_fixed_kinds_are_ap1s_six_attacks_and_five_kinds_of_bad_data():
    assert list(FIXED_KINDS['D5']) == [
        'direct_override', 'authority_spoof', 'data_embedded_injection',
        'multi_turn_false_premise_persuasion', 'control_plane_injection',
        'tool_description_injection']
    assert list(FIXED_KINDS['D6']) == [
        'stale_source', 'partial_receipt', 'internal_contradiction',
        'cross_source_disagreement', 'out_of_range']
    assert (KIND_LABEL_FIELD, DEFINED_KINDS_FIELD) == (
        {'D5': 'adversarial_class', 'D6': 'conflict_class'},
        {'D5': 'adversarial_classes', 'D6': 'conflict_classes'})


@pytest.mark.parametrize('name', list(AP1_LINES))
def test_fixed_kind_definition_is_ap1_v13s_words_on_its_line(name):
    # The definition is AP-1's text on that line, without its emphasis.
    line = AP1_V13.read_text('utf-8').splitlines()[AP1_LINES[name] - 1]
    plain = re.sub(r'\*\*|\*|\[NEW v1\.3\] ', '', line)
    definition = {**FIXED_KINDS['D5'], **FIXED_KINDS['D6']}[name]
    assert definition in plain, (definition, line)


@pytest.mark.parametrize('name', list(AP1_LINES))
def test_spec_lists_each_fixed_kind_with_its_ap1_line(name):
    spec = (REPO / 'docs' / 'SPEC.md').read_text('utf-8')
    rows = [row for row in spec.splitlines()
            if row.startswith(f'| `{name}` |')]
    assert len(rows) == 1, rows
    assert f'l. {AP1_LINES[name]}' in rows[0], rows[0]


@pytest.mark.parametrize('dim', ['D5', 'D6'])
@pytest.mark.parametrize('label', ['x', '', None, 7, 'Direct_Override',
                                   'stale source'])
def test_validate_kinds_undefined_label_refused_naming_it(dim, label):
    qs = {'items': items(dim, list(FIXED_KINDS[dim])[0], label)}
    with pytest.raises(ConfigError) as e:
        validate_kinds(qs)
    assert str(e.value).startswith(
        f"item 'Q1': {KIND_LABEL_FIELD[dim]} {label!r} is not a {dim} kind")


def test_validate_kinds_label_of_the_other_dimension_refused():
    with pytest.raises(ConfigError, match="'stale_source' is not a D5 kind"):
        validate_kinds({'items': items('D5', 'stale_source')})


@pytest.mark.parametrize('dim', ['D5', 'D6'])
def test_validate_kinds_fixed_and_defined_labels_accepted(dim):
    qs = {'items': items(dim, *FIXED_KINDS[dim], 'my_kind')
          + [{'id': 'plain'}],
          DEFINED_KINDS_FIELD[dim]: {'my_kind': 'A kind of our own'}}
    assert validate_kinds(qs) is None


def test_validate_kinds_defined_kind_is_its_dimensions_only():
    qs = {'items': items('D6', 'my_attack'),
          'adversarial_classes': {'my_attack': 'An attack of our own'}}
    with pytest.raises(ConfigError, match="'my_attack' is not a D6 kind"):
        validate_kinds(qs)


@pytest.mark.parametrize('field, name', [
    ('adversarial_classes', 'direct_override'),
    ('adversarial_classes', 'stale_source'),
    ('conflict_classes', 'out_of_range'),
    ('conflict_classes', 'authority_spoof')])
def test_validate_kinds_defined_kind_reusing_a_fixed_name_refused(field, name):
    with pytest.raises(ConfigError) as e:
        validate_kinds({'items': [], field: {name: 'Something else'}})
    assert str(e.value) == (f'{field}: {name!r} is a fixed kind (SPEC R0.1); '
                            f'a defined kind needs a name of its own')


@pytest.mark.parametrize('definition', ['', '  ', 'two\nlines', None, 3])
def test_validate_kinds_defined_kind_needs_a_one_line_definition(definition):
    with pytest.raises(ConfigError, match="'my_kind' needs a one-line"):
        validate_kinds({'items': [],
                        'conflict_classes': {'my_kind': definition}})


@pytest.mark.parametrize('value', [['my_kind'], 'my_kind'])
def test_validate_kinds_defined_kinds_must_be_an_object(value):
    with pytest.raises(ConfigError, match='^adversarial_classes: expected an '
                                          'object'):
        validate_kinds({'items': [], 'adversarial_classes': value})


def test_validate_kinds_defined_kind_needs_a_name():
    with pytest.raises(ConfigError, match='a kind needs a name'):
        validate_kinds({'items': [], 'conflict_classes': {' ': 'x'}})


def test_validate_kinds_shipped_example_accepted_and_has_no_kinds():
    # The shipped example claims neither D5 nor D6 and labels no item.
    qs = json.loads((REPO / 'example' / 'questions.json').read_text('utf-8'))
    assert validate_kinds(qs) is None
    assert kind_counts(qs, 'v1.3-draft-for-comment-20260730',
                       ['D2', 'D7']) == {}


def test_kind_counts_fixed_kinds_first_then_defined_with_definitions():
    qs = {'items': items('D5', 'my_kind', 'direct_override', 'my_kind'),
          'adversarial_classes': {'my_kind': 'A kind of our own',
                                  'unused': 'Defined, no item'}}
    kinds = kind_counts(qs, 'v1.3', [])['D5']['kinds']
    assert [(k['name'], k['fixed'], k['n']) for k in kinds] == (
        [(name, True, 1 if name == 'direct_override' else 0)
         for name in FIXED_KINDS['D5']]
        + [('my_kind', False, 2), ('unused', False, 0)])
    assert kinds[-2]['definition'] == 'A kind of our own'


def test_kind_counts_defined_kind_never_stands_in_for_a_fixed_one():
    # Twenty items of a defined kind: D5's six fixed kinds are all missing.
    qs = {'items': items('D5', *['my_kind'] * 20),
          'adversarial_classes': {'my_kind': 'A kind of our own'}}
    assert kind_counts(qs, 'v1.3', ['D5'])['D5']['missing'] == list(
        FIXED_KINDS['D5'])


@pytest.mark.parametrize('dim', ['D5', 'D6'])
def test_kind_counts_names_each_missing_fixed_kind(dim):
    present = list(FIXED_KINDS[dim])
    gone = present.pop(1)
    entry = kind_counts({'items': items(dim, *present)}, 'v1.3', [])[dim]
    assert entry['missing'] == [gone]
    full = kind_counts({'items': items(dim, *FIXED_KINDS[dim])}, 'v1.3', [])
    assert full[dim]['missing'] == []


def test_kind_counts_required_kinds_follow_the_declared_version():
    # v1.2 §11.5 names four kinds of attack, and its D6 names no classes.
    assert REQUIRED_KINDS['v1.2'] == {'D5': tuple(FIXED_KINDS['D5'])[:4],
                                      'D6': ()}
    qs = {'items': items('D5', *list(FIXED_KINDS['D5'])[:4])
          + [{'id': 'c', 'conflict_class': 'stale_source'}]}
    v12 = kind_counts(qs, 'v1.2', ['D5', 'D6'])
    assert (v12['D5']['missing'], v12['D6']['missing']) == ([], [])
    v13 = kind_counts(qs, 'v1.3-draft-for-comment-20260730', ['D5', 'D6'])
    assert v13['D5']['missing'] == ['control_plane_injection',
                                    'tool_description_injection']
    assert v13['D6']['missing'] == list(FIXED_KINDS['D6'])[1:]


def test_kind_counts_dimension_claimed_labelled_or_defined_only():
    assert kind_counts({'items': [{'id': 'a'}]}, 'v1.3', ['D1', 'D7']) == {}
    claimed = kind_counts({'items': [{'id': 'a'}]}, 'v1.3', ['D6'])
    assert list(claimed) == ['D6']
    assert claimed['D6']['missing'] == list(FIXED_KINDS['D6'])
    defined = kind_counts({'items': [],
                           'conflict_classes': {'k': 'A kind'}}, 'v1.3', [])
    assert list(defined) == ['D6']
