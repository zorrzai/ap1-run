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
# fails too, so the list cannot go stale. A field listed under
# "numeric_text_fields" is compared with every number in its strings read
# as a Decimal, for a fix that changes only how a value is written (an
# operand read from its literal text, '15.20', not through float, '15.2').
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
        'numeric_text_fields': listed.get('numeric_text_fields', []),
    }


_NUMBER = re.compile(r'-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?')


def numeric_text(value):
    """value with every number written in a string replaced by its
    canonical Decimal form, so '15.20', '15.2' and '15.200' read alike and
    '15.21' does not; dicts and lists are walked, other types kept."""
    if isinstance(value, str):
        return _NUMBER.sub(
            lambda m: format(decimal.Decimal(m.group()).normalize(), 'f'),
            value)
    if isinstance(value, list):
        return [numeric_text(v) for v in value]
    if isinstance(value, dict):
        return {k: numeric_text(v) for k, v in value.items()}
    return value


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
    seen = set()
    for i, (pub, rep) in enumerate(zip(pub_rows, rep_rows)):
        key = execution_key(pub)
        if key != execution_key(rep):
            problems.append(f'$.all_results[{i}]: {key} in the published '
                            f'run, {execution_key(rep)} in the replay')
            continue
        listed = moves.get(key, {})
        for field in sorted(set(pub) | set(rep)):
            where = f'$.all_results[{i}] ({key}).{field}'
            if field not in rep:
                problems.append(f'{where}: missing from the replay')
                continue
            if field not in pub:
                if field not in expected['new_execution_fields']:
                    problems.append(f'{where}: not in the published run')
                continue
            if field in listed:
                seen.add((key, field))
                if [pub[field], rep[field]] != listed[field]:
                    problems.append(
                        f'{where}: listed move {listed[field][0]!r} -> '
                        f'{listed[field][1]!r}, but {pub[field]!r} in the '
                        f'published run and {rep[field]!r} in the replay')
                continue
            want, got = pub[field], rep[field]
            if field in expected['numeric_text_fields']:
                want, got = numeric_text(want), numeric_text(got)
            found = first_difference(want, got, where)
            if found:
                problems.append(found)
    for key, fields in sorted(moves.items()):
        for field in sorted(fields):
            if (key, field) not in seen:
                problems.append(f'listed move {key}.{field} matches no '
                                f'execution field of the published run')
    return problems


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
        published = json.load(f)
    replayed = json.loads(raw['smoke_summary.json'])
    problems = replay_differences(published, replayed,
                                  load_replay_expected(run_dir))
    if problems:
        shown = '; '.join(problems[:5])
        more = f' (and {len(problems) - 5} more)' if len(problems) > 5 else ''
        raise HardCheckError(
            f'replay of {run_dir}: smoke_summary.json differs from the '
            f'published run, beyond replay_expected.json: {shown}{more}')
