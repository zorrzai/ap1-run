#!/usr/bin/env python3
"""
test_findings_mutation.py — Mutation tests for verify_findings pipeline.

Tests two directions:
  1. Document mutation: alter FINDINGS.md, verify the diff catches it
  2. Artifact mutation: alter a copy of an artifact, regenerate, verify output changes

Ensures neither the generator nor the verifier is vacuous.

Part of the test suite (run_all_tests.py).
"""
import json
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import generate_findings  # noqa: E402

FINDINGS = os.path.join(ROOT, "FINDINGS.md")
TEMPLATE = os.path.join(ROOT, "FINDINGS.template.md")
RUN_A = os.path.join(ROOT, "output", "run_a_mini", "smoke_summary.json")
RUN_B = os.path.join(ROOT, "output", "run_b_sol", "smoke_summary.json")

# Check artifacts exist — skip gracefully if absent
_REQUIRED = [RUN_A, RUN_B]
_missing = [p for p in _REQUIRED if not os.path.exists(p)]
if _missing:
    print("SKIPPED: run artifacts not found, cannot run mutation tests")
    for p in _missing:
        print(f"  missing: {os.path.relpath(p, ROOT)}")
    print("\n0 passed, 0 failed, 7 skipped")
    sys.exit(0)


def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _write(path, content):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


passed = 0
failed = 0


def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print(f"  PASS  {name}")
    else:
        failed += 1
        print(f"  FAIL  {name}")


# =========================================================================
# Test 1: Document mutation — alter FINDINGS.md, verify catches it
# =========================================================================
print("--- Document mutation tests ---")

# Save original
original = _read(FINDINGS)

def test_doc_mutation(name, old, new):
    """Mutate FINDINGS.md, run verify, assert it detects the change."""
    mutated = original.replace(old, new, 1)
    if mutated == original:
        check(name, False)
        print(f"    Pattern not found: {old!r}")
        return
    _write(FINDINGS, mutated)
    try:
        # Regenerate fresh and compare
        values = generate_findings.compute_figures()
        generated = generate_findings.generate(values)
        differs = generated != mutated
        check(name, differs)
        if not differs:
            print(f"    DANGER: mutation passed silently!")
    finally:
        _write(FINDINGS, original)


# 1a: Table figure
test_doc_mutation(
    "table-figure-243",
    "243 / 1,064",
    "999 / 1,064",
)

# 1b: Prose figure
test_doc_mutation(
    "prose-figure-62-sign-inv",
    "62 sign-inversion findings",
    "99 sign-inversion findings",
)

# 1c: Percentage
test_doc_mutation(
    "percentage-22.8",
    "22.8%",
    "33.3%",
)

# 1d: Narrative figure (the ones that were previously unverified)
test_doc_mutation(
    "narrative-figure-sup-524",
    "524 of",
    "525 of",
)


# =========================================================================
# Test 2: Artifact mutation — alter artifact, regenerate, output changes
# =========================================================================
print("\n--- Artifact mutation tests ---")

def test_artifact_mutation(name, artifact_path, mutate_fn):
    """Alter a copy of an artifact, regenerate, assert output differs."""
    # Read original artifact
    with open(artifact_path, "r", encoding="utf-8") as f:
        artifact_original = json.load(f)

    # Mutate
    artifact_mutated = json.loads(json.dumps(artifact_original))  # deep copy
    mutate_fn(artifact_mutated)

    # Write mutated artifact
    backup = artifact_path + ".bak"
    shutil.copy2(artifact_path, backup)
    try:
        with open(artifact_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(artifact_mutated, f)

        # Regenerate
        values_mutated = generate_findings.compute_figures()
        generated_mutated = generate_findings.generate(values_mutated)

        # Compare against committed
        differs = generated_mutated != original
        check(name, differs)
        if not differs:
            print(f"    DANGER: artifact mutation did not change output!")
    finally:
        shutil.copy2(backup, artifact_path)
        os.remove(backup)


# 2a: Change Run B's not-invoked count
def mutate_invocation(data):
    """Remove a NOT-INVOKED result from Run B to change the count."""
    for r in data["all_results"]:
        if r["invocation_outcome"] == "NOT-INVOKED":
            r["invocation_outcome"] = "INVOKED"
            break

test_artifact_mutation("artifact-invocation-count", RUN_B, mutate_invocation)


# 2b: Change Run A's wrong-op count
def mutate_operation(data):
    """Change a WRONG-OPERATION to OPERATION-CORRECT to alter the count."""
    for r in data["all_results"]:
        for op in r.get("operation_correctness", []):
            if op["outcome"] == "WRONG-OPERATION":
                op["outcome"] = "OPERATION-CORRECT"
                return

test_artifact_mutation("artifact-wrong-op-count", RUN_A, mutate_operation)


# 2c: Change Run A's sign-inversion count
def mutate_sign_inv(data):
    """Remove one sign-inversion finding to alter the count."""
    for r in data["all_results"]:
        for p in r.get("provenance_results", []):
            for res in p.get("operand_resolutions", []):
                if res.get("sign_inversion_finding") not in (None, False):
                    res["sign_inversion_finding"] = None
                    return

test_artifact_mutation("artifact-sign-inv-count", RUN_A, mutate_sign_inv)


# =========================================================================
# Summary
# =========================================================================
print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
