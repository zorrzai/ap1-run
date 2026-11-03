"""Checks a run must pass before its output is normalised or compared.

run_regression.collect() calls check() once per runner scenario, before
normalisation. A failure raises, so the harness stops: it is never a
golden difference, and --update cannot write over it or around it.

  check_transport          the mock refused no request (wrong path or
                           credential)
  hash_oracle.check_seals  every seal value recomputed independently
  check_replay             a replay re-scores its published run exactly
"""

import json
import os

import hash_oracle

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))

# The only top-level smoke_summary.json key a replay may change: the seal
# covers the mock's endpoint, the runner's source and the timestamp-free
# record, none of which can equal the published run's. Any other
# difference is investigated, never added here by explanation alone.
REPLAY_SUMMARY_EXCLUDED = ('seal_hash',)


class HardCheckError(Exception):
    """A run broke an invariant the golden files cannot express."""


def check(scenario, tree, result_dir, raw):
    """Raise if the run in `tree` breaks a hard check.

    raw is {file name: text} of what the run produced, before
    normalisation; 'console.txt' is its stdout."""
    check_transport(result_dir)
    hash_oracle.check_seals(scenario, tree, result_dir, raw)
    if 'replay' in scenario:
        check_replay(scenario, raw)


def check_transport(result_dir):
    """Every request kept the mock's transport contract: the chat
    completions path and the driver's bearer credential."""
    path = os.path.join(result_dir, 'transport_violations.json')
    if not os.path.exists(path):
        raise HardCheckError('the driver recorded no transport check')
    with open(path, encoding='utf-8') as f:
        violations = json.load(f)
    if violations:
        counts = {}
        for v in violations:
            key = f'{v["kind"]} ({v["path"]})'
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


def check_replay(scenario, raw):
    """The replayed smoke_summary.json equals the published run's, except
    the top-level keys in REPLAY_SUMMARY_EXCLUDED."""
    run_dir = os.path.dirname(scenario['replay'])
    published_path = os.path.join(REPO, *run_dir.split('/'),
                                  'smoke_summary.json')
    if 'smoke_summary.json' not in raw:
        raise HardCheckError(f'replay of {run_dir}: the run wrote no '
                             f'smoke_summary.json')
    with open(published_path, encoding='utf-8') as f:
        published = json.load(f)
    replayed = json.loads(raw['smoke_summary.json'])
    for summary in (published, replayed):
        for key in REPLAY_SUMMARY_EXCLUDED:
            summary.pop(key, None)
    found = first_difference(published, replayed)
    if found:
        raise HardCheckError(
            f'replay of {run_dir}: smoke_summary.json differs from the '
            f'published run at {found}')
