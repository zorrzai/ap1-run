#!/usr/bin/env python3
"""
verify_findings.py — Verify FINDINGS.md matches generation from artifacts.

Regenerates from FINDINGS.template.md and the run artifacts, then diffs
against the committed FINDINGS.md. FAILs on any difference.

If the run artifacts are absent, reports SKIPPED (exit 0).
The artifact-existence check below FAILs separately if committed artifacts
are missing — so a clone where the artifacts were never committed reports
FAIL on that check, while the generation test itself SKIPs.

Part of the test suite (run_all_tests.py).
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
FINDINGS = os.path.join(ROOT, "FINDINGS.md")

REQUIRED_ARTIFACTS = [
    os.path.join(ROOT, "output", "run_a_mini", "smoke_summary.json"),
    os.path.join(ROOT, "output", "run_b_sol", "smoke_summary.json"),
    os.path.join(ROOT, "output", "superseded",
                 "run_b_sol_pre_restructure", "smoke_summary.json"),
]


def artifacts_committed():
    """Assert that all artifacts referenced by generate_findings.py exist.

    In a git working tree: checks that each artifact is tracked (committed).
    Outside git (archive, tarball): checks that each artifact file exists.

    Returns a list of missing/untracked artifact paths (empty = all good).
    """
    import subprocess
    # Detect whether we are inside a git repository
    is_git = subprocess.run(
        ['git', 'rev-parse', '--git-dir'],
        capture_output=True, text=True, cwd=ROOT,
    ).returncode == 0

    missing = []
    for p in REQUIRED_ARTIFACTS:
        relpath = os.path.relpath(p, ROOT)
        if is_git:
            # In a git repo: check the file is tracked
            result = subprocess.run(
                ['git', 'ls-files', '--error-unmatch', relpath],
                capture_output=True, text=True, cwd=ROOT,
            )
            if result.returncode != 0:
                missing.append(relpath)
        else:
            # Outside git: check the file exists on disk
            if not os.path.exists(p):
                missing.append(relpath)
    return missing


def verify():
    """Regenerate and diff against committed FINDINGS.md."""
    # Check artifacts exist
    missing = [p for p in REQUIRED_ARTIFACTS if not os.path.exists(p)]
    if missing:
        print("SKIPPED: run artifacts not found, cannot regenerate FINDINGS.md")
        for p in missing:
            print(f"  missing: {os.path.relpath(p, ROOT)}")
        print("\n0 passed, 0 failed, 1 skipped")
        return 0  # exit 0 — not a test failure

    # Import the generator
    sys.path.insert(0, ROOT)
    import generate_findings  # noqa: E402

    # Generate from template + artifacts
    values = generate_findings.compute_figures()
    generated = generate_findings.generate(values)

    # Read committed
    with open(FINDINGS, "r", encoding="utf-8") as f:
        committed = f.read()

    # Diff
    gen_lines = generated.splitlines()
    com_lines = committed.splitlines()

    diffs = []
    max_lines = max(len(gen_lines), len(com_lines))
    for i in range(max_lines):
        gen_line = gen_lines[i] if i < len(gen_lines) else "<missing>"
        com_line = com_lines[i] if i < len(com_lines) else "<missing>"
        if gen_line != com_line:
            diffs.append((i + 1, gen_line, com_line))

    passed = 1 if not diffs else 0
    failed = 0 if not diffs else 1

    if diffs:
        print(f"FINDINGS.md does not match generation from artifacts:")
        for line_no, gen_line, com_line in diffs[:20]:
            print(f"  L{line_no}:")
            print(f"    generated:  {gen_line[:120]}")
            print(f"    committed:  {com_line[:120]}")
        if len(diffs) > 20:
            print(f"  ... and {len(diffs) - 20} more differences")
    else:
        print(f"FINDINGS.md matches generation from artifacts")

    print(f"\n{passed} passed, {failed} failed")
    return 0 if not diffs else 1


if __name__ == "__main__":
    # First: assert artifacts are committed (FAIL if not)
    uncommitted = artifacts_committed()
    if uncommitted:
        print("FAIL: FINDINGS.md references artifacts not tracked by git:")
        for p in uncommitted:
            print(f"  not committed: {p}")
        print("\nThe repository claims figures derived from these artifacts")
        print("but a clone will not contain them.")
        print("\n0 passed, 1 failed")
        sys.exit(1)

    sys.exit(verify())
