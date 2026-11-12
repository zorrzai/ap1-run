"""Checks a run must pass before its output is normalised or compared.

run_regression.run_scenario() calls before_run() once the scratch tree
exists and before the runner starts; run_regression.collect() calls check()
once per runner scenario, before normalisation. A failure raises, so the
harness stops: it is never a golden difference, and --update cannot write
over it or around it.

Command scenarios (a "command" in the scenario) run an entry point
directly and get none of these checks. None of them seals today; a command
scenario that seals needs the driver's capture first.

  check_transport          the mock refused no request (wrong method,
                           path or credential)
  hash_oracle.check_seals  every seal value recomputed independently
  check_replay             a replay re-scores its published run exactly,
                           apart from the differences replay_expected.json
                           lists execution by execution
"""

import decimal
import json
import os
import re
import time

import hash_oracle

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))

# The only top-level smoke_summary.json key a replay may change freely: the
# seal covers the mock's endpoint, the runner's source and the
# timestamp-free record, none of which can equal the published run's.
REPLAY_SUMMARY_EXCLUDED = ('seal_hash',)

# Every other difference between a replay and its published run is one a
# fix makes on purpose, and is listed in this file: per published run, the
# fields new in the replay, and each execution's moves as
# [published value, replayed value]. A listed move that does not happen
# fails too, so the list cannot go stale. A new execution field must be
# in every replayed execution and must have an expectation here
# (NEW_FIELD_EXPECTATIONS): its value for each execution is computed by
# this module from the published run's own fields, with the listed moves
# applied, and the scoring config; never read from the replay being
# checked. For a fix that changes only how a value is written (an operand
# read from its literal text, '15.20', not through float, '15.2'),
# "numeric_paths" names the leaf strings compared as numbers
# ('field[].key.key'), and "numeric_text_paths" the free-text leaves whose
# standalone numbers are so compared, the rest of the text verbatim; the
# only respelling accepted is trailing zeros. Every other value,
# identifiers included, is compared as is. Both summaries are read with
# JSON numbers as exact Decimals.
# Any other difference is investigated, never added to the list by
# explanation alone.
REPLAY_EXPECTED = os.path.join(HERE, 'replay_expected.json')


# Expectations frozen before each run, by tree.
_FROZEN = {}


class HardCheckError(Exception):
    """A run broke an invariant the golden files cannot express."""


def before_run(tree):
    """Freeze what the run must agree with, before the runner starts: the
    source hash of the tree it will run from, and the start time."""
    _FROZEN[os.path.realpath(tree)] = {
        'source_hash': hash_oracle.runner_source_hash(tree),
        'started': time.time(),
    }


def check(scenario, tree, result_dir, raw):
    """Raise if the run in `tree` breaks a hard check.

    raw is {file name: text} of what the run produced, before
    normalisation; 'console.txt' is its stdout."""
    frozen = _FROZEN.pop(os.path.realpath(tree), None)
    if frozen is None:
        raise HardCheckError('before_run() was not called for this run')
    frozen['finished'] = time.time()
    check_transport(result_dir)
    hash_oracle.check_seals(scenario, tree, result_dir, raw, frozen)
    if 'replay' in scenario:
        check_replay(scenario, raw)


def check_transport(result_dir):
    """Every request kept the mock's transport contract: a POST to the
    chat completions path with the driver's bearer credential."""
    path = os.path.join(result_dir, 'transport_violations.json')
    if not os.path.exists(path):
        raise HardCheckError('the driver recorded no transport check')
    with open(path, encoding='utf-8') as f:
        violations = json.load(f)
    if violations:
        counts = {}
        for v in violations:
            what = f'{v["method"]} ' if 'method' in v else ''
            key = f'{v["kind"]} ({what}{v["path"]})'
            counts[key] = counts.get(key, 0) + 1
        raise HardCheckError(
            f'the mock refused {len(violations)} request(s) outside its '
            f'transport contract: '
            + '; '.join(f'{k} x{n}' for k, n in counts.items()))


def first_difference(want, got, path='$'):
    """The first JSON path where two values differ, type-aware (True is
    not 1, 1 is not 1.0), or None."""
    if type(want) is not type(got):
        return (f'{path}: {type(want).__name__} {want!r} in the published '
                f'run, {type(got).__name__} {got!r} in the replay')
    if isinstance(want, dict):
        for k in sorted(set(want) | set(got)):
            if k not in got:
                return f'{path}.{k}: missing from the replay'
            if k not in want:
                return f'{path}.{k}: not in the published run'
            found = first_difference(want[k], got[k], f'{path}.{k}')
            if found:
                return found
        return None
    if isinstance(want, list):
        for i, (w, g) in enumerate(zip(want, got)):
            found = first_difference(w, g, f'{path}[{i}]')
            if found:
                return found
        if len(want) != len(got):
            return (f'{path}: {len(want)} entries in the published run, '
                    f'{len(got)} in the replay')
        return None
    if want != got:
        return f'{path}: {want!r} in the published run, {got!r} in the replay'
    return None


def load_replay_expected(run_dir, path=None):
    """The listed differences for the published run in run_dir, with
    empty defaults."""
    with open(path or REPLAY_EXPECTED, encoding='utf-8') as f:
        listed = json.load(f).get(run_dir, {})
    return {
        'new_top_level_keys': listed.get('new_top_level_keys', []),
        'new_execution_fields': listed.get('new_execution_fields', []),
        'moves': listed.get('moves', {}),
        'numeric_paths': listed.get('numeric_paths', []),
        'numeric_text_paths': listed.get('numeric_text_paths', []),
    }


# A standalone number: not part of an identifier ('acct01', 'acct-01')
# or of a longer number.
_NUMBER = re.compile(r'(?<![\w.-])-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?(?![\w.])')
# The one respelling accepted: plain ASCII decimal digits.
_PLAIN = re.compile(r'-?[0-9]+(?:\.[0-9]+)?')


def _same_number(want, got):
    """Two plain decimal strings ('-?digits[.digits]') with the same
    value and sign, compared exactly (Decimal equality does not round;
    normalize() would): '15.2' and '15.20' alike, ' 15.2', '1.52E+1' and
    '-0.0' for '0.0' not."""
    if not (isinstance(want, str) and isinstance(got, str)
            and _PLAIN.fullmatch(want) and _PLAIN.fullmatch(got)):
        return False
    a, b = decimal.Decimal(want), decimal.Decimal(got)
    return a == b and a.is_signed() == b.is_signed()


def load_summary(text):
    """A smoke_summary.json, with JSON numbers read as exact Decimals."""
    return json.loads(text, parse_float=decimal.Decimal)


# -- expected values of the new execution fields --------------------------
# The AP-1 v1.3 section 6.8 answer outcome (scoring/answer_outcome.py),
# stated again here from the published fields, as hash_oracle.py states
# the seal: figure identification, D7.1 invocation, the D7.2(a) outcome of
# each call, and D1 (the released figure against the expected value,
# both quantised under the scoring config, within the answer tolerance).

_ROUTED = 'routed to adjudication: the scorers assign the outcome'


def _d1_correct(row, scoring):
    places = decimal.Decimal(1).scaleb(-int(scoring['places']))
    rounding = getattr(decimal, scoring['rounding'])
    try:
        released = decimal.Decimal(str(row['released_figure']))
        expected = decimal.Decimal(str(row['expected']))
    except (KeyError, decimal.InvalidOperation):
        return False
    gap = (released.quantize(places, rounding=rounding)
           - expected.quantize(places, rounding=rounding))
    return abs(gap) <= decimal.Decimal(str(scoring['answer_tolerance']))


def expected_answer_outcome(row, scoring):
    """(outcome, reason) for one published execution, moves applied."""
    figure = row.get('figure_outcome')
    if figure == 'AUTO-NO-FIGURE':
        return None, ('no figure released: the record does not decide the '
                      'outcome')
    if figure != 'AUTO-MATCH':
        return None, _ROUTED
    if row.get('invocation_outcome') != 'INVOKED':
        return None, ('correct figure, required computation not shown '
                      'invoked: a RETRIEVED candidate (SPEC R4.1)')
    outcomes = [p.get('outcome') for p in row.get('provenance_results', [])]
    correct = _d1_correct(row, scoring)
    if 'OPERAND-ORIGINATED' in outcomes:
        return 'ORIGINATED', (f'{"correct" if correct else "matched"} '
                              f'figure computed from an originated operand '
                              f'(D7.2(a) OPERAND-ORIGINATED)')
    if not (outcomes and all(o == 'OPERANDS-GROUNDED' for o in outcomes)):
        return None, 'operands not shown grounded (D7.2(a))'
    if not correct:
        return None, 'figure matched, but D1 scores it INCORRECT: not COMPUTED'
    return 'COMPUTED', 'correct figure; computation invoked; operands grounded'


NEW_FIELD_EXPECTATIONS = {
    'answer_outcome': lambda row, scoring: expected_answer_outcome(
        row, scoring)[0],
    'answer_outcome_reason': lambda row, scoring: expected_answer_outcome(
        row, scoring)[1],
}


def _same_numeric_text(want, got):
    """Two strings alike but for how their standalone numbers are
    written: the text between numbers verbatim, each number exactly."""
    if _NUMBER.split(want) != _NUMBER.split(got):
        return False
    a, b = _NUMBER.findall(want), _NUMBER.findall(got)
    return len(a) == len(b) and all(map(_same_number, a, b))


def compare_at_paths(want, got, where, path, numeric, numeric_text):
    """first_difference, except at the leaf paths listed as numeric
    (exact Decimal) or numeric text; `path` is the field-relative path
    ('field[].key')."""
    if isinstance(want, str) and isinstance(got, str):
        if path in numeric:
            return None if _same_number(want, got) else (
                f'{where}: {want!r} in the published run, {got!r} in the '
                f'replay (compared as exact Decimals)')
        if path in numeric_text:
            return None if _same_numeric_text(want, got) else (
                f'{where}: {want!r} in the published run, {got!r} in the '
                f'replay (numbers compared as exact Decimals)')
    if isinstance(want, dict) and isinstance(got, dict):
        for k in sorted(set(want) | set(got)):
            if k not in got:
                return f'{where}.{k}: missing from the replay'
            if k not in want:
                return f'{where}.{k}: not in the published run'
            found = compare_at_paths(want[k], got[k], f'{where}.{k}',
                                     f'{path}.{k}', numeric, numeric_text)
            if found:
                return found
        return None
    if isinstance(want, list) and isinstance(got, list):
        if len(want) != len(got):
            return (f'{where}: {len(want)} entries in the published run, '
                    f'{len(got)} in the replay')
        for i, (w, g) in enumerate(zip(want, got)):
            found = compare_at_paths(w, g, f'{where}[{i}]', f'{path}[]',
                                     numeric, numeric_text)
            if found:
                return found
        return None
    return first_difference(want, got, where)


def execution_key(result):
    return f"{result['item_id']}/{result['condition']}/r{result['repeat']}"


def replay_differences(published, replayed, expected):
    """Each difference between a published and a replayed summary that
    `expected` does not list, and each listed move that did not happen,
    as a list of messages (empty when the replay is as listed)."""
    problems = []
    for key in REPLAY_SUMMARY_EXCLUDED:
        published.pop(key, None)
        replayed.pop(key, None)
    for key in sorted(set(replayed) - set(published)):
        if key not in expected['new_top_level_keys']:
            problems.append(f'$.{key}: not in the published run')
    for key in sorted(set(published)):
        if key not in replayed:
            problems.append(f'$.{key}: missing from the replay')
        elif key != 'all_results':
            found = first_difference(published[key], replayed[key], f'$.{key}')
            if found:
                problems.append(found)
    pub_rows = published.get('all_results', [])
    rep_rows = replayed.get('all_results', [])
    if len(pub_rows) != len(rep_rows):
        problems.append(f'$.all_results: {len(pub_rows)} entries in the '
                        f'published run, {len(rep_rows)} in the replay')
        return problems
    moves = expected['moves']
    new_fields = expected['new_execution_fields']
    for field in new_fields:
        if field not in NEW_FIELD_EXPECTATIONS:
            problems.append(f'new execution field {field}: no expectation '
                            f'in hard_checks.NEW_FIELD_EXPECTATIONS')
    scoring = expected.get('scoring', {})
    numeric = set(expected['numeric_paths'])
    numeric_text = set(expected['numeric_text_paths'])
    seen = set()
    for i, (pub, rep) in enumerate(zip(pub_rows, rep_rows)):
        key = execution_key(pub)
        if key != execution_key(rep):
            problems.append(f'$.all_results[{i}]: {key} in the published '
                            f'run, {execution_key(rep)} in the replay')
            continue
        listed = moves.get(key, {})
        moved = dict(pub, **{f: v[1] for f, v in listed.items()})
        for field in new_fields:
            if field not in rep:
                problems.append(f'$.all_results[{i}] ({key}).{field}: '
                                f'listed as new, missing from the replay')
            elif field in NEW_FIELD_EXPECTATIONS:
                want = NEW_FIELD_EXPECTATIONS[field](moved, scoring)
                found = first_difference(want, rep[field],
                                         f'$.all_results[{i}] ({key}).{field}')
                if found:
                    problems.append(found + ' (expected from the published '
                                    'fields)')
        for field in sorted(set(pub) | set(rep)):
            where = f'$.all_results[{i}] ({key}).{field}'
            if field not in rep:
                if field not in new_fields:     # reported above
                    problems.append(f'{where}: missing from the replay')
                continue
            if field not in pub:
                if field not in new_fields:
                    problems.append(f'{where}: not in the published run')
                continue
            if field in listed:
                seen.add((key, field))
                if first_difference(list(listed[field]),
                                    [pub[field], rep[field]]):
                    problems.append(
                        f'{where}: listed move {listed[field][0]!r} -> '
                        f'{listed[field][1]!r}, but {pub[field]!r} in the '
                        f'published run and {rep[field]!r} in the replay')
                continue
            found = compare_at_paths(pub[field], rep[field], where, field,
                                     numeric, numeric_text)
            if found:
                problems.append(found)
    for key, fields in sorted(moves.items()):
        for field in sorted(fields):
            if (key, field) not in seen:
                problems.append(f'listed move {key}.{field} matches no '
                                f'execution field of the published run')
    return problems


def replay_scoring(scenario):
    """The answer tolerance and quantisation the replay scores under: the
    shipped example config, with the scenario's config changes."""
    with open(os.path.join(REPO, 'example', 'config.json'),
              encoding='utf-8') as f:
        config = json.load(f)
    config.update(scenario.get('config', {}))
    quantisation = config.get('quantisation', {})
    return {'answer_tolerance': config['answer_tolerance'],
            'places': quantisation.get('places', 2),
            'rounding': quantisation.get('rounding', 'ROUND_HALF_UP')}


def check_replay(scenario, raw):
    """The replayed smoke_summary.json equals the published run's, except
    the top-level keys in REPLAY_SUMMARY_EXCLUDED and the differences
    replay_expected.json lists for that run."""
    run_dir = os.path.dirname(scenario['replay'])
    published_path = os.path.join(REPO, *run_dir.split('/'),
                                  'smoke_summary.json')
    if 'smoke_summary.json' not in raw:
        raise HardCheckError(f'replay of {run_dir}: the run wrote no '
                             f'smoke_summary.json')
    with open(published_path, encoding='utf-8') as f:
        published = load_summary(f.read())
    replayed = load_summary(raw['smoke_summary.json'])
    expected = load_replay_expected(run_dir)
    expected['scoring'] = replay_scoring(scenario)
    problems = replay_differences(published, replayed, expected)
    if problems:
        shown = '; '.join(problems[:5])
        more = f' (and {len(problems) - 5} more)' if len(problems) > 5 else ''
        raise HardCheckError(
            f'replay of {run_dir}: smoke_summary.json differs from the '
            f'published run, beyond replay_expected.json: {shown}{more}')
