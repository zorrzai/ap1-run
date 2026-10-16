# Legacy checks mapped to unit tests: group G4 (scoring-a)

Modules: `scoring/invocation.py`, `scoring/accuracy.py`, `scoring/figure_id.py`,
`scoring/operation_correctness.py`. Suites mapped here (step-3 protocol, rule 5): the
module-level suites `verify_phase_c.py`, `verify_d72b.py` and `verify_e7_coverage.py`, for the
checks about these modules. No other module-level suite (`verify.py`, `verify_phase_b.py`,
`verify_phase_d.py`, `verify_phase_e.py`, `verify_hashes.py`) calls them. Checks in those suites
about other modules (reproducibility, transcription, seal, release coverage, ...) are left to
their groups. Unit test files: `tests/unit/scoring/test_<module>.py`.

| suite | function | check (short description or line) | new test(s) | note |
|---|---|---|---|---|
| verify_phase_c.py | test_exact_bound_in_range | bound in (0, 1] for n = 1..200 | test_invocation.py::test_exact_upper_bound_is_in_open_unit_interval | same range, plus n = 10 000; asserts the stricter < 1 |
| verify_phase_c.py | test_exact_bound_n1 | format_rate(0, 1) contains 95.0% | test_invocation.py::test_format_rate_zero_failures_n1_states_95_percent_bound, test_exact_upper_bound_n1_is_one_minus_alpha | whole string pinned |
| verify_phase_c.py | test_exact_bound_n49 | format_rate(0, 49) contains 5.9% | test_invocation.py::test_format_rate_bound_rounds_half_even_down_at_n49 | pinned as T3-61 (an upper bound rounded down) |
| verify_phase_c.py | test_exact_bound_n100 | format_rate(0, 100) contains 3.0% | test_invocation.py::test_format_rate_zero_failures_n100_states_3_percent_bound | |
| verify_phase_c.py | test_100pct_never_printed_alone | no '100%' for n = 1..200 | test_invocation.py::test_format_rate_zero_failures_never_prints_100_percent | |
| verify_phase_c.py | test_exact_and_rule_of_three_agree_above_30 | exact bound within 1 pp of 3/n, n = 30..200 | test_invocation.py::test_exact_upper_bound_within_1pp_of_rule_of_three_from_n30 | |
| verify_phase_c.py | test_nonzero_failures_prints_percentage | format_rate(3, 50) has 3/50 and 6.0% | test_invocation.py::test_format_rate_nonzero_failures_prints_count_and_percent | |
| verify_phase_c.py | test_dpr_zero_base_undefined | zero base: None, UNDEFINED, no '1.0' | test_invocation.py::test_compute_dpr_zero_base_rate_is_undefined_never_one | exact tuple pinned |
| verify_phase_c.py | test_dpr_nonzero_base | 45/50 vs 10/50 gives 77.8% | test_invocation.py::test_compute_dpr_relative_drop_in_rate | value and string pinned |
| verify_phase_c.py | test_cross_class_aggregate_warning | EV-2 + EV-0 warns 'not comparable' | test_invocation.py::test_measure_invocation_two_classes_warn_not_comparable_in_sorted_order | whole warning pinned |
