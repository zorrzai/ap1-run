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
| verify_phase_b | test_ev2_tool_capable_invoked | populated tool_calls, tools offered: EV-2 INVOKED, no self-report | ev::test_classify_invocation_no_accumulated_reads_final_response, ev::test_classify_invocation_no_required_operation_any_call_invoked | |
| verify_phase_b | test_ev2_tool_capable_not_invoked | `tool_calls: []`: EV-2 NOT-INVOKED | ev::test_classify_invocation_no_calls_not_invoked, ev::test_classify_invocation_tool_calls_field_absent_not_invoked | |
| verify_phase_b | test_ev2_tool_capable_no_tool_calls_field | no `tool_calls` key: EV-2 NOT-INVOKED | ev::test_classify_invocation_tool_calls_field_absent_not_invoked | |
| verify_phase_b | test_ev0_no_tool_structure | tools not offered: EV-0, outcome None | ev::test_classify_invocation_tools_not_offered_ev0_no_outcome | |
| verify_phase_b | test_ev2_self_report_does_not_change_class | prose claim: EV-2 NOT-INVOKED, claim recorded | ev::test_classify_invocation_each_marker_recorded_not_class | |
| verify_phase_b | test_ev0_self_report_still_ev0 | no tools + claim: EV-0, claim recorded | ev::test_classify_invocation_tools_not_offered_self_report_recorded | |
| verify_phase_b | test_ev0_anthropic_shaped_response | Anthropic shape: EV-0, None | ev::test_classify_invocation_no_round_shapes_final_shape_unrecognised_ev0 | |
| verify_phase_b | test_ev0_gemini_shaped_response | Gemini shape: EV-0, None | ev::test_classify_invocation_no_round_shapes_other_shapes_ev0[gemini] | |
| verify_phase_b | test_ev0_openai_responses_shaped | Responses-API shape: EV-0, None | ev::test_classify_invocation_no_round_shapes_other_shapes_ev0[responses] | |
| verify_phase_b | test_ev1_signed_attestation_unverified | EV-1, reason names "signer is the party being measured" | ev::test_classify_attestation_always_ev1 | exact reason pinned |
| verify_phase_b | test_ev3_guard_blocks | EvidenceError for EV-3, message says forbidden | ev::test_check_ev3_guard_ev3_raises | exact message pinned |
| verify_phase_b | test_ev3_guard_passes_other_classes | EV-0/1/2 pass | ev::test_check_ev3_guard_other_values_pass | |
| verify_phase_b | test_classify_attestation_never_returns_ev3 | `ev3_implemented: True` in the seal record still not EV-3 | ev::test_classify_attestation_always_ev1, ev::test_classify_attestation_ev3_allowed_still_ev1 | |
| verify_phase_b | test_ev1_ranks_below_ev2 | ranks_above(EV-2, EV-1) and not the reverse | ev::test_ranks_above_normative_order | |
| verify_phase_b | test_ev0_ranks_below_all | EV-1 and EV-2 above EV-0 | ev::test_ranks_above_normative_order | |
| verify_phase_b | test_different_classes_not_comparable | EV-1 vs EV-2 not comparable; EV-2 vs EV-2 comparable | ev::test_classes_comparable_same_class_only | |
| verify_phase_b | test_void_excluded_from_denominator | list comprehension over hand-made records | (none) | dropped on purpose: the check filters a list inside the test and calls no production code |
| verify_phase_c | test_anthropic_shape_unmeasurable_not_auto_no_figure | reason mentions Anthropic (string from `evidence._diagnose_shape` via `_extract_content`) | ev::test_extract_shape_unrecognised_reason[anthropic] | the UNMEASURABLE outcome is figure_id's (other group) |
| verify_phase_c | test_gemini_shape_unmeasurable_not_auto_no_figure | reason mentions Gemini | ev::test_extract_shape_unrecognised_reason[gemini] | as above |
| verify_phase_c | test_cross_class_aggregate_warning, test_49_limited_1_success_unmeasured | use `EV_0`, `EV_2` constants as input | ev::test_evidence_class_constants_exact_labels | the checks are about scoring/invocation (other group) |
| verify_e7_coverage | (whole suite) | `evidence.py` is only imported (through `scoring.release_coverage` -> `figure_id`); its 11 % coverage is module load | (none needed) | no check of evidence.py |
| verify_phase_b | test_underivable_item_void | underivable item: VOID, reason underivable, adapter never called, one transcript record with `error_state` VOID | eng::test_execute_item_underivable_void_without_request | the new test pins the whole record |

`engine.py` is executed by no other module-level suite. Its live wiring (the tool loop over HTTP,
mid-loop failures, transport errors) is also exercised by G7's `verify_integration.py` and end to
end by the regression scenarios `clean`, `multi_round`, `transport_errors`,
`t3_1_unrecognised_shape`, `t3_16_malformed_calls`, `t3_38_unknown_tool` and `t3_39_crash`; every
line and branch of the three modules is also executed by the new unit tests (100 % branch coverage).
