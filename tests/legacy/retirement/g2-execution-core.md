# Legacy checks mapped to unit tests: G2 (execution core)

Modules: `execution/context.py`, `execution/evidence.py`, `execution/engine.py`.
New tests: `tests/unit/execution/test_context.py`, `test_evidence.py`, `test_engine.py`
(abbreviated `ctx::`, `ev::`, `eng::` below).

Suites mapped here (the module-level suites that execute these modules): `verify_phase_b.py`,
`verify_phase_c.py`, `verify_phase_d.py`, `verify_d72b.py`, `verify_e7_coverage.py`.
`verify.py`, `verify_phase_e.py` and `verify_hashes.py` do not execute any of the three modules
(checked with coverage). `verify_integration`, `verify_r41`, `verify_inspect` and
`verify_conformance` also execute them but are G7's to map.

| suite | function | check (short description or line) | new test(s) | note |
|---|---|---|---|---|
| verify_phase_b | test_build_delivered_context | only named accounts; `id`, `name` excluded | ctx::test_build_delivered_context_named_accounts_only, ctx::test_build_delivered_context_id_and_name_dropped_other_fields_kept | |
| verify_phase_b | test_lookup_collision_detected | final equal to a context value gives `(True, 'savings.balance')` | ctx::test_check_lookup_collision_value_present_names_field | |
| verify_phase_b | test_lookup_collision_not_present | no collision when final differs | ctx::test_check_lookup_collision_value_absent_none | |
| verify_phase_d | test_d15_tracking_context_records_access | subscript reads recorded, exactly two | ctx::test_tracking_context_subscript_reads_recorded | |
| verify_phase_d | (most functions) | `build_delivered_context(MINI_FIXTURE, ...)` as input set-up | ctx::test_build_delivered_context_* | set-up, not a check of context.py; the checks are about provenance/seal (other groups) |
| verify_d72b | test_t16_declared_constants_check_catches_undeclared | context built inside `seal_constants.declared_constants_check` | ctx::test_build_delivered_context_* | set-up only |
| verify_e7_coverage | test_* using q05/q07/q08 | `build_delivered_context(fixture, ...)` as set-up | ctx::test_build_delivered_context_* | set-up only; checks are about release coverage (other group) |
