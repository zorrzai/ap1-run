# Legacy checks mapped to new unit tests: G3 (execution/seal)

Modules: `execution/seal.py`, `execution/seal_constants.py`, `execution/version.py`,
`execution/perturbation_guard.py`. New tests are in `tests/unit/execution/`
(`test_seal.py`, `test_seal_constants.py`, `test_version.py`, `test_perturbation_guard.py`);
names below omit the file where it is obvious from the prefix (`test_seal_*`, `test_verify_seal_*`,
`test_perturbation_check_*` and `test_source_fields_check_*` are in `test_seal.py`).

No legacy suite imports `version.py`; nothing to map for it.

| suite | function | check (short description or line) | new test(s) | note |
|---|---|---|---|---|
| verify.py | test_r11_seal | `<file> exists` for config, fixture, questions, ground truth (l.326-329) | none | dropped: a precondition on the example files, not seal behaviour; regression `clean` fails if they are missing |
| verify.py | test_r11_seal | `seal has seal_hash` (64 hex, l.341) | test_seal_record_without_ap1_text | new test pins the exact seal_hash (canonical hash of the record minus timestamp) |
| verify.py | test_r11_seal | `seal has ev3_implemented=False` (l.345) | test_seal_record_without_ap1_text, test_seal_records_verification_keys | |
| verify.py | test_r11_seal | `fixture hash stable` (l.356) | test_seal_record_without_ap1_text, test_seal_accepts_string_paths | hash pinned to an independent SHA-256 of the bytes; two seals compared equal |
| verify.py | test_r11_seal | `questions hash stable` (l.358) | test_seal_record_without_ap1_text, test_seal_accepts_string_paths | as above |
| verify.py | test_r11_seal | `config hash stable` (l.360) | test_seal_record_without_ap1_text, test_seal_empty_config_gives_blank_fields | config hash pinned to an independent canonical-JSON SHA-256 |
| verify.py | test_r11_seal | `verify_seal passes` (l.371) | test_verify_seal_unchanged_inputs_returns_true | refusal paths, untested in legacy (T3-17), now in test_verify_seal_changed_* and test_verify_seal_lists_every_mismatch_in_order |
| verify.py | test_r11_ap1_hash | `placeholder hash accepted` (l.407) | test_seal_ap1_text_placeholder_or_blank_declared_hash_accepted[placeholder] | finding T3-68 |
| verify.py | test_r11_ap1_hash | `ap1_text_hash computed` (l.408) | test_seal_ap1_text_placeholder_or_blank_declared_hash_accepted, test_seal_ap1_text_matching_declared_hash_recorded | |
| verify.py | test_r11_ap1_hash | `wrong ap1 hash refused` (l.423/425) | test_seal_ap1_text_mismatch_raises | exact message |
| verify.py | test_r11_ap1_hash | `real ap1 hash matches reference file` (l.442) | regression `clean`, `seal_refused` | a data check (shipped config vs `reference/`): `clean` seals with the real text and declared hash and would be refused on a mismatch; `seal_refused` pins the refusal |
| verify.py | test_ev3_guard | `ev3_implemented is False` (l.511) | test_seal_record_without_ap1_text | |
| verify_phase_b.py | test_perturbation_single_variable_pass | only system_prompt differs: no diffs | test_guard_only_system_prompt_differs_returns_empty_list | `test_perturbation_guard.py` |
| verify_phase_b.py | test_perturbation_tools_removed_refused | tools None: refused, message names tools and system_prompt | test_guard_one_other_change_refused_naming_it[tools], test_guard_every_change_named_in_order | exact message |
| verify_phase_b.py | test_perturbation_sampling_changed_refused | sampling changed: refused, named | test_guard_one_other_change_refused_naming_it[sampling] | |
| verify_phase_b.py | test_perturbation_four_quantities_all_named | names tools, tool_choice, sampling; "4 quantities" | test_guard_every_change_named_in_order, test_guard_one_other_change_refused_naming_it | count = violations + 1, pinned at 2 and 6 |
| verify_phase_d.py | test_d8_constant_returning_module_refused | constant module: SealError mentions perturbation and names `savings.balance` | test_perturbation_check_constant_module_raises_naming_field | exact message |
| verify_phase_d.py | test_d9_undeclared_field_access_refused | undeclared subscript read: SealError names `annual_rate` | test_source_fields_check_undeclared_read_raises_naming_fields | exact message; the `.get()` bypass is pinned in test_source_fields_check_misses_reads_through_get (T3-8) |
| verify_phase_d.py | test_d16_perturbation_passes_real_module | example module passes perturbation_check (MINI_FIXTURE) | test_perturbation_check_passes_example_module | new test uses the shipped `example/fixture.json` |
| verify_phase_d.py | test_d17_source_fields_passes_real_module | example module passes source_fields_check (MINI_FIXTURE) | test_source_fields_check_passes_example_module | as above |
| verify_phase_e.py | TestDOISeal.test_doi_recorded_in_seal | `ap1_version_doi` copied from config into the record | test_seal_record_without_ap1_text | the DOI branch of verify_seal: test_verify_seal_lists_every_mismatch_in_order, test_verify_seal_doi_skipped_* (T3-17) |
| verify_d72b.py | test_t16_declared_constants_check_catches_undeclared | undeclared D("4") (fixture `_t16_mock_gt.py`): SealError mentions Q99 | test_declared_constants_check_undeclared_literal_raises | `test_seal_constants.py`; exact message. `tests/fixtures/_t16_mock_gt.py` is then unused by G3's tests |
| verify_e7_coverage.py | test_e3b_ast_check_allows_unused_constants | example module (declares 4 for Q07 without using it) passes | test_declared_constants_check_passes_example_module, test_declared_constants_check_declared_but_unused_passes | |
| verify_e7_coverage.py | test_guard_perturbation_refusal | tool_choice changed: refused, named | test_guard_one_other_change_refused_naming_it[tool_choice] | |

`verify_hashes.py` and `verify_phase_c.py` hold no checks on G3's modules.

## For G7 (suites G7 maps in full; listed here only to help)

| suite | function | G3 test(s) that cover the same behaviour | note |
|---|---|---|---|
| verify_conformance.py | test_d7_8_perturbation_discipline | test_guard_empty_configs_with_different_prompts_pass, test_guard_one_other_change_refused_naming_it[sampling] | under pytest its `check()` never raises, so it kills no mutant (score 0.0) |
| verify_conformance.py | (l.559-567, returns list of diffs) | test_guard_only_system_prompt_differs_returns_empty_list, test_guard_identical_prompts_returned_not_refused | |
| verify_integration.py | test_perturbation_guard_passes_on_config_prompts | none needed | does not call `check_single_variable_perturbation`; it re-implements a one-field diff inline (tautological, cf. T3-46). Kills no guard mutant |
| verify_r41.py | test_b23_constant_ground_truth_refused (l.595) | test_perturbation_check_constant_module_raises_naming_field | |
| verify_inspect.py | test_seal_refusal_on_wrong_hash (l.678-690) | test_seal_ap1_text_mismatch_raises | |
