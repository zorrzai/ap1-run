#!/usr/bin/env python3
"""
verify_findings.py — Verify FINDINGS.md matches generation from artifacts.

Regenerates from FINDINGS.template.md and the run artifacts, then diffs
against the committed FINDINGS.md. FAILs on any difference.

Part of the test suite (run_all_tests.py).
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
FINDINGS = os.path.join(ROOT, "FINDINGS.md")

# Import the generator
sys.path.insert(0, ROOT)
import generate_findings  # noqa: E402


def verify():
    """Regenerate and diff against committed FINDINGS.md."""
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
    sys.exit(verify())
