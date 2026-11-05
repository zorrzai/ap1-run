"""Check the list of files the runner's source hash covers.

runner_source_hash covers every .py file under the runner's base directory
except output*, review_output* and __pycache__. source_hash_files.txt lists
the tracked files that rule covers, tests included, so a change to the set
(a move, a new module, a deletion) shows as a reviewed diff of that list.
The hash oracle checks the hash itself on every scenario; this checks the
list.

The list comes from hash_oracle.source_hash_files(), the oracle's own rule
over the checkout, not from a second copy of the rule here, so a change to
the rule shows in this list too. `git ls-files` only drops what the rule
finds but git does not track (a local venv, scratch files); those are named
on stderr, as they change this checkout's source hash, but do not fail it.

    python tests/regression/check_source_files.py           # compare
    python tests/regression/check_source_files.py --update  # rewrite the list

Exit status: 0 the list matches, 1 it differs, 2 no git checkout.
"""

import argparse
import difflib
import os
import subprocess
import sys

import hash_oracle

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
LIST = os.path.join(HERE, 'source_hash_files.txt')


def tracked_files():
    """The tracked .py files, as '/'-separated paths."""
    try:
        out = subprocess.run(['git', 'ls-files', '-z'], cwd=REPO, check=True,
                             capture_output=True).stdout
    except (OSError, subprocess.CalledProcessError) as e:
        print(f'check_source_files: git ls-files failed: {e}', file=sys.stderr)
        raise SystemExit(2)
    # Filter on bytes first: a tracked file whose name is not UTF-8 is
    # not this check's business unless it is a .py file.
    py = [p for p in out.split(b'\0') if p.endswith(b'.py')]
    try:
        return {p.decode('utf-8') for p in py}
    except UnicodeDecodeError as e:
        print(f'check_source_files: a tracked .py file name is not UTF-8, '
              f'which the source hash cannot encode either: {e}',
              file=sys.stderr)
        raise SystemExit(1)


def tracked_source_files():
    """The files hash_oracle.source_hash_files() finds in the checkout,
    '/'-separated and sorted, less those git does not track (named on
    stderr)."""
    tracked = tracked_files()
    covered = [p.replace(os.sep, '/')
               for p in hash_oracle.source_hash_files(REPO)]
    untracked = [p for p in covered if p not in tracked]
    if untracked:
        print(f'check_source_files: {len(untracked)} untracked file(s) the '
              f'source hash covers in this checkout, not listed: '
              + ', '.join(untracked[:10])
              + (' ...' if len(untracked) > 10 else ''), file=sys.stderr)
    return sorted(p for p in covered if p in tracked)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--update', action='store_true',
                    help='rewrite source_hash_files.txt from the oracle\'s rule')
    args = ap.parse_args(argv)
    current = [f'{p}\n' for p in tracked_source_files()]
    if args.update:
        with open(LIST, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(current)
        print(f'source_hash_files.txt: {len(current)} files')
        return 0
    listed = []
    if os.path.exists(LIST):
        with open(LIST, encoding='utf-8') as f:
            listed = f.readlines()
    if listed == current:
        print(f'OK: source_hash_files.txt matches the {len(current)} tracked '
              f'files the source hash covers')
        return 0
    print('source_hash_files.txt differs from the tracked files the source '
          'hash covers (review the change, then run with --update):')
    sys.stdout.writelines(difflib.unified_diff(
        listed, current, 'source_hash_files.txt',
        'hash_oracle.source_hash_files()', n=0))
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
