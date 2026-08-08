# Run artifacts

Aggregated per-item outcomes from the shakedown runs, retained so that
every figure in FINDINGS.md can be verified against its evidence.
generate_findings.py reads these; verify_findings.py regenerates from them
and diffs against the committed FINDINGS.md.

    run_a_mini/                     current fixture, 1,000 executions
    run_b_sol/                      current fixture, 1,000 executions
    superseded/run_b_sol_pre_restructure/
                                    the fixture that encoded direction inside
                                    the magnitude, retained so F2's historical
                                    figures remain verifiable

Each file contains per-item outcome classifications, resolved figures, and
the mathematical expressions submitted to the calculator. They contain no
response prose, no provider response objects and no API metadata.

Every run recorded here is an instrument shakedown and not an AP-1
evaluation. Each file carries that disclaimer in its _disclaimer field.
