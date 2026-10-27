# Retirement map, group G1 (foundation: numeric, config, transcript, adapter)

Legacy checks that exercise `src/ap1_run/foundation/`, and the new unit tests in
`tests/unit/foundation/` that cover the same behaviour. Test names are in
`test_numeric.py` (N), `test_config.py` (C), `test_transcript.py` (T) and
`test_adapter.py` (A). Checks about other modules (seal, ground truth, EV
classes, engine, release coverage) are left to their groups.

Suites mapped here: `verify.py`, `verify_phase_b.py`, `verify_phase_c.py`,
`verify_phase_d.py`, `verify_phase_e.py`, `verify_d72b.py`, `verify_e7_coverage.py`,
`verify_hashes.py`. `verify_phase_d.py` and `verify_d72b.py` have no check about
these modules (d72b only names a transcript file in a comment). The
`verify_conformance`, `verify_r41`, `verify_integration` and `verify_inspect`
checks on these modules are G7's to map.

| suite | function | check (short description or line) | new test(s) | note |
|---|---|---|---|---|
| verify.py | test_r04_parse | parse 1,780.00 | N test_parse_decimal_grouping_removed | |
| verify.py | test_r04_parse | parse 1780.00 | N test_parse_decimal_plain_value_returns_decimal_triple | |
| verify.py | test_r04_parse | parse $1,780.00 value, currency | N test_parse_decimal_leading_currency | |
| verify.py | test_r04_parse | parse 1.780,00 (EU) | N test_parse_decimal_european_separators | |
| verify.py | test_r04_parse | parse (1,780.00) | N test_parse_decimal_parenthesised_is_negative | |
| verify.py | test_r04_parse | parse ($1,780.00) value, currency | N test_parse_decimal_currency_inside_parentheses | |
| verify.py | test_r04_parse | parse 12.5% value, flag | N test_parse_decimal_percent_flag_and_value | |
| verify.py | test_r04_parse | parse -42.50 | N test_parse_decimal_hyphen_minus_is_negative | |
| verify.py | test_r04_parse | parse −42.50 | N test_parse_decimal_unicode_minus_is_negative | |
| verify.py | test_r04_parse | ambiguous 1.780 raises | N test_parse_decimal_same_separators_with_separator_is_ambiguous | |
| verify.py | test_r04_parse | empty string raises | N test_parse_decimal_empty_raises_with_message | |
| verify.py | test_r04_extract | extract $1,780.00 and 12.5% from prose | N test_extract_currency_led_with_space, test_extract_returns_named_tokens_with_positions, test_extract_run1_literal_mortgage_prose | same patterns, exact token lists |
| verify.py | test_r04_extract | extract 274.1375, 259.1375, 777.41 | N test_extract_several_values_in_order | new test pins the full list, including the step numbers 1 and 2 |
| verify.py | test_r04_extract | extract ($2,400.00) | N test_extract_parenthesised_negative | same sentence |
| verify.py | test_r04_no_float | canonical_json refuses float | N test_canonical_json_refuses_float_anywhere, test_check_no_float_top_level_float_refused_with_path | |
| verify.py | test_r04_no_float | canonical_json accepts Decimal | N test_canonical_json_sorted_compact_decimal_as_string | |
| verify.py | test_r04_no_float | parse returns Decimal | N test_parse_decimal_plain_value_returns_decimal_triple | checks type(v) is Decimal |
| verify.py | test_r04_no_float | nested float refused | N test_canonical_json_refuses_float_anywhere, test_check_no_float_paths_name_keys_and_indexes | |
| verify.py | test_r04_hash | deterministic hash | N test_canonical_hash_is_sha256_of_utf8_canonical_json, test_canonical_hash_known_digest_of_verify_hashes_input | a pinned digest implies determinism |
| verify.py | test_r04_hash | key order irrelevant | N test_canonical_hash_key_order_irrelevant | |
| verify.py | test_r04_round_once | step1/2/3 full precision (3 checks) | N test_quantise_once_differs_from_each_step | Decimal arithmetic itself, not numeric.py; the new test uses the same chain |
| verify.py | test_r04_round_once | round-once 777.41 (HALF_UP, HALF_EVEN) | N test_quantise_once_differs_from_each_step, test_quantise_half_even, test_quantise_default_is_half_up | |
| verify.py | test_r04_round_once | round-each 777.42; once != each; mock28 diff 0.01 (3 checks) | N test_quantise_once_differs_from_each_step | asserts both values, so their difference |
| verify.py | test_r01_config | valid example config loads; tolerance Decimal; repeat_count int (3 checks) | C test_load_config_example_config_loads, test_load_config_valid_parses_typed_fields | |
| verify.py | test_r01_config | missing field halts | C test_load_config_each_missing_required_field_refused | all 16 fields |
| verify.py | test_r01_config | bare float refused | C test_load_config_bare_float_refused | |
| verify.py | test_r01_config | bare int refused | C test_load_config_bare_int_refused | |
| verify.py | test_r01_minimum_n | D6 with 9 refused (message names 9 and 10) | C test_minimum_n_d6_below_minimum_refused | exact message |
| verify.py | test_r01_minimum_n | D6 with 10 accepted | C test_minimum_n_d6_at_minimum_accepted | |
| verify.py | test_r01_minimum_n | D1 category A with 9 refused | C test_minimum_n_d1_small_category_refused, test_minimum_n_d1_uncategorised_items_share_default_category | |
| verify.py | test_r11_seal | load_config of example config (setup) | C test_load_config_example_config_loads | the seal checks belong to the seal module's group |
| verify.py | test_r11_ap1_hash | file_hash of a temp file and the AP-1 text (setup for seal checks) | N test_file_hash_is_sha256_of_raw_bytes | the seal checks belong to the seal module's group |
| verify.py | test_ground_truth | (none: ground truth) | | not a foundation check |
| verify.py | test_ev3_guard | load_config (setup) | C test_load_config_example_config_loads | the EV-3 check is not G1's |
| verify.py | test_run1_literal_strings | parse_decimal of 8 run-1 literals, value and currency (16 checks) | N test_parse_decimal_leading_currency, test_parse_decimal_currency_after_sign, test_parse_decimal_sign_after_currency, test_parse_decimal_currency_inside_parentheses, test_parse_decimal_leading_currency_longest_symbol_first | '$2600.00', '$3109.65', '$1437.00', '$25' are the plain leading-currency case; '$286,063.00' adds grouping (test_extract_run1_literal_mortgage_prose); '-$2411.00', '$-2411.00', '($2,411.00)' have their own tests |
| verify.py | test_run1_literal_strings | extract from 4 run-1 prose answers (5 checks) | N test_extract_run1_literal_mortgage_prose, test_extract_sign_led_then_currency, test_extract_currency_led_then_sign | the two single-value sentences are the leading-currency case already covered |
| verify.py | test_a_omitted_without_reason_refused | raises ConfigError; names temperature; explains (3 checks) | C test_load_config_plain_omitted_refused | exact message |
| verify_hashes.py | main | digest of the known input equals the pinned EXPECTED_DIGEST (also written to hash_digest.txt) | N test_canonical_hash_known_digest_of_verify_hashes_input | the unit test pins the canonical text and the digest 831709b2...; `.github/workflows/hashes.yml` runs the script on three OSes and must be switched to the unit test before retiring |
| verify_hashes.py | main | same input gives same digest | N test_canonical_hash_known_digest_of_verify_hashes_input | |
| verify_hashes.py | main | key order does not change the digest | N test_canonical_hash_key_order_irrelevant | |
| verify_phase_b.py | test_underivable_item_void | transcript read_all returns the one VOID record | T test_read_all_round_trips_append, test_append_writes_one_sorted_json_line | the VOID routing is the engine's (other group) |
| verify_phase_c.py | _mock_extract (helper) | extract_numeric_tokens with defaults | | dropped: the helper is defined but never called |
| verify_phase_e.py | TestDOIRequired.test_doi_in_required_fields | ap1_version_doi in REQUIRED_FIELDS | C test_required_fields_are_the_sixteen_declared | |
| verify_phase_e.py | TestDOIRequired.test_missing_doi_refused | config without ap1_version_doi refused, naming it | C test_load_config_each_missing_required_field_refused[ap1_version_doi] | |
| verify_e7_coverage.py | test_b34_q04_acceptance_from_real_data | extract_numeric_tokens on the Q04 prose (setup) | N test_extract_subtraction_operand_read_as_negative | the coverage check is release_coverage's; the unit test pins the same 'a - b = c' prose |
| verify_e7_coverage.py | test_e3b_ast_check_allows_unused_constants | load_config of example config (setup) | C test_load_config_example_config_loads | the AST check is seal_constants' |
