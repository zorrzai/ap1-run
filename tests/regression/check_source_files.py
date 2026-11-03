"""Check the list of files the runner's source hash covers.

runner_source_hash covers every .py file under the runner's base directory
except output*, review_output* and __pycache__ (hash_oracle.py has the rule).
source_hash_files.txt lists the tracked files that rule covers, tests
included, so a change to the set (a move, a new module, a deletion) shows
as a reviewed diff of that list. The hash oracle checks the hash itself on
every scenario; this checks the list.

    python tests/regression/check_source_files.py           # compare
    python tests/regression/check_source_files.py --update  # rewrite the list

Uses `git ls-files`, so untracked files (a local venv, scratch files) never
appear. Exit status: 0 the list matches, 1 it differs, 2 no git checkout.
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


def tracked_source_files():
    try:
        out = subprocess.run(['git', 'ls-files', '-z'], cwd=REPO, check=True,
                             capture_output=True).stdout
    except (OSError, subprocess.CalledProcessError) as e:
        print(f'check_source_files: git ls-files failed: {e}', file=sys.stderr)
        raise SystemExit(2)
    paths = [p for p in out.decode('utf-8').split('\0') if p]
    return sorted(p for p in paths if p.endswith('.py')
                  and not p.startswith(hash_oracle.SOURCE_HASH_EXCLUDED))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--update', action='store_true',
                    help='rewrite source_hash_files.txt from the tracked files')
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
        listed, current, 'source_hash_files.txt', 'git ls-files', n=0))
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
