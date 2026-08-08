# push_ap1_run.ps1 — Push ap1-runner/ to zorrzai/ap1-run via subtree split
#
# This script is the ONLY correct way to update ap1-run. Do not push by hand.
# `git push origin master` pushes to PILVI, not to ap1-run.
#
# What it does:
#   1. Asserts clean working tree
#   2. Asserts current branch is master, origin is zorrzai/pilvi
#   3. Runs subtree split from the PARENT directory (not from inside ap1-runner)
#   4. Asserts ap1-run/main is an ancestor of the split (fast-forward safe)
#   5. Pushes split:main to ap1-run
#   6. Verifies with git ls-remote ap1-run
#
# Usage:
#   From anywhere inside the repository:
#     powershell -File scripts/push_ap1_run.ps1
#
# Options:
#   -DryRun   Show what would happen without pushing

param(
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

# --- Locate the repository root ---
$RepoRoot = git rev-parse --show-toplevel 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "FATAL: not inside a git repository."
    exit 1
}

# The parent repo root (aegis-mobile), not ap1-runner
# If we're inside ap1-runner, go up
$ParentRoot = $RepoRoot
Write-Host "Repository root: $ParentRoot"

# --- 1. Assert clean working tree ---
# Check modified/staged only; untracked files in parent repo are expected
$Status = git -C $ParentRoot status --porcelain -uno
if ($Status) {
    Write-Error "FATAL: working tree has uncommitted changes. Commit or stash first."
    Write-Host $Status
    exit 1
}
Write-Host "[OK] Working tree is clean (no uncommitted changes)."

# --- 2. Assert current branch is master, origin is pilvi ---
$Branch = git -C $ParentRoot rev-parse --abbrev-ref HEAD
if ($Branch -ne "master") {
    Write-Error "FATAL: current branch is '$Branch', expected 'master'."
    exit 1
}
Write-Host "[OK] Branch is master."

$OriginUrl = git -C $ParentRoot remote get-url origin 2>&1
if ($OriginUrl -notlike "*zorrzai/pilvi*") {
    Write-Error "FATAL: origin is '$OriginUrl', expected zorrzai/pilvi."
    exit 1
}
Write-Host "[OK] origin is $OriginUrl"

# Check ap1-run remote exists
$Ap1RunUrl = git -C $ParentRoot remote get-url ap1-run 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "FATAL: remote 'ap1-run' is not configured. Add it with: git remote add ap1-run https://github.com/zorrzai/ap1-run.git"
    exit 1
}
if ($Ap1RunUrl -notlike "*zorrzai/ap1-run*") {
    Write-Error "FATAL: ap1-run remote is '$Ap1RunUrl', expected zorrzai/ap1-run."
    exit 1
}
Write-Host "[OK] ap1-run remote is $Ap1RunUrl"

# --- 3. Subtree split ---
# Delete stale split branch if it exists (a prior split may have left one,
# and the second split produces a different SHA from the first)
$BranchExists = git -C $ParentRoot branch --list ap1-run-split
if ($BranchExists) {
    Write-Host "Deleting stale ap1-run-split branch..."
    git -C $ParentRoot branch -D ap1-run-split 2>&1 | Out-Null
}

Write-Host "Running subtree split --prefix=ap1-runner ..."
$SplitSha = git -C $ParentRoot subtree split --prefix=ap1-runner -b ap1-run-split 2>&1 | Select-Object -Last 1
if ($LASTEXITCODE -ne 0) {
    Write-Error "FATAL: subtree split failed."
    exit 1
}
$SplitTip = git -C $ParentRoot rev-parse ap1-run-split
Write-Host "[OK] Split branch tip: $SplitTip"

# --- 4. Assert fast-forward ---
# Fetch ap1-run to get current main
Write-Host "Fetching ap1-run..."
git -C $ParentRoot fetch ap1-run 2>&1 | Out-Null

git -C $ParentRoot merge-base --is-ancestor ap1-run/main ap1-run-split 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "FATAL: ap1-run/main is NOT an ancestor of the split branch. This would require a force-push. STOPPING."
    Write-Host "ap1-run/main: $(git -C $ParentRoot rev-parse ap1-run/main)"
    Write-Host "split tip:    $SplitTip"
    exit 1
}
Write-Host "[OK] ap1-run/main is an ancestor of split. Fast-forward is safe."

# --- 5. Push ---
if ($DryRun) {
    Write-Host ""
    Write-Host "DRY RUN: would execute: git push ap1-run ap1-run-split:main"
    Write-Host "DRY RUN: split tip is $SplitTip"
    Write-Host ""
    Write-Host "ap1-run/main would advance to $SplitTip."
    Write-Host "Verify with a fresh clone before granting access."
    exit 0
}

Write-Host ""
Write-Host "Pushing to ap1-run (https://github.com/zorrzai/ap1-run.git) ..."
git -C $ParentRoot push ap1-run ap1-run-split:main 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "FATAL: push to ap1-run failed."
    exit 1
}

# --- 6. Verify ---
Write-Host ""
Write-Host "Verifying from ap1-run (NOT from origin)..."
$LsRemote = git -C $ParentRoot ls-remote ap1-run refs/heads/main 2>&1
Write-Host $LsRemote

$RemoteSha = ($LsRemote -split "\t")[0]
Write-Host ""
Write-Host "============================================================"
Write-Host "ap1-run/main is now $RemoteSha."
Write-Host "Repository: https://github.com/zorrzai/ap1-run"
Write-Host "Verify with a fresh clone before granting access."
Write-Host "============================================================"
