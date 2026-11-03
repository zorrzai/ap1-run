"""Checks a run must pass before its output is normalised or compared.

run_regression.collect() calls check() once per runner scenario, before
normalisation. A failure raises, so the harness stops: it is never a
golden difference, and --update cannot write over it or around it.

  hash_oracle.check_seals  every seal value recomputed independently
"""

import hash_oracle


def check(scenario, tree, result_dir, raw):
    """Raise if the run in `tree` breaks a hard check.

    raw is {file name: text} of what the run produced, before
    normalisation; 'console.txt' is its stdout."""
    hash_oracle.check_seals(scenario, tree, result_dir, raw)
