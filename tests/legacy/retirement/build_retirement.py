"""Build tests/legacy/RETIREMENT.md: every legacy check, joined to the new
tests that cover the same behaviour (step 3, group G9).

    PYTHONPATH=src python tests/legacy/retirement/build_retirement.py

1. Inventory. A "check" is what run_all_tests.py counts. verify.py,
   verify_conformance.py and verify_spec.py count check() calls: they are
   run once with a profiler that records each call (function, line, name),
   so loops are counted as they run. test_findings_mutation.py counts the
   module-level calls of its two helpers (read from the AST, because running
   it rewrites FINDINGS.md and a sealed output/ file in place). The other
   suites count test functions; for each one the AST gives the line of every
   assert, self.assert* call and non-trivial return.
2. Join. The group maps in this folder (g1-...md to g7-...md) map checks to
   new tests; G9_ASSIGN and G9_ROWS below settle the rest. Every test name
   is looked up in tests/{unit,conformance,functional,inspect}; an unknown
   name stops the build.
3. Write RETIREMENT.md: header, summary, then one table per suite.

The totals per suite are checked against run_all_tests.SUITES.
"""

import ast
import contextlib
import glob
import io
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEGACY = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(LEGACY))
OUT = os.path.join(LEGACY, 'RETIREMENT.md')

TRACED = ['verify.py', 'verify_conformance.py', 'verify_spec.py']
ORDER = ['verify.py', 'verify_phase_b.py', 'verify_phase_c.py',
         'verify_phase_d.py', 'verify_phase_e.py', 'verify_d72b.py',
         'verify_e7_coverage.py', 'verify_integration.py', 'verify_r41.py',
         'verify_conformance.py', 'verify_spec.py', 'verify_findings.py',
         'test_findings_mutation.py', 'verify_inspect.py']


# -- 1. inventory ----------------------------------------------------------

def trace_checks(suite):
    path = os.path.join(LEGACY, suite)
    records = []

    def profile(frame, event, arg):
        if (event == 'call' and frame.f_code.co_name == 'check'
                and frame.f_code.co_filename == path):
            chain = []
            f = frame.f_back
            while f is not None:
                if f.f_code.co_filename == path:
                    chain.append((f.f_code.co_name, f.f_lineno))
                f = f.f_back
            records.append((chain, frame.f_locals.get('name')))

    cwd, argv = os.getcwd(), sys.argv
    os.chdir(REPO)
    sys.argv = [path]
    sys.setprofile(profile)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            runpy.run_path(path, run_name='__main__')
    except SystemExit:
        pass
    finally:
        sys.setprofile(None)
        os.chdir(cwd)
        sys.argv = argv
    rows = []
    for chain, name in records:
        tests = [(n, ln) for n, ln in chain if n.startswith('test_')]
        fn, line = tests[-1] if tests else chain[0]
        helper = '' if chain[0][0] == fn else f' (in {chain[0][0]}, l.{chain[0][1]})'
        rows.append({'suite': suite, 'function': fn, 'line': str(line),
                     'check': f'`{name}`{helper}'})
    return rows


def mutation_checks(suite):
    tree = ast.parse(open(os.path.join(LEGACY, suite), encoding='utf-8-sig').read())
    rows = []
    for node in tree.body:
        if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and getattr(node.value.func, 'id', '') in
                ('test_doc_mutation', 'test_artifact_mutation')):
            rows.append({'suite': suite, 'function': node.value.func.id,
                         'line': str(node.lineno),
                         'check': f'`{node.value.args[0].value}`'})
    return rows


def walk_own(fn):
    """ast.walk over a test function, not into functions nested in it (a
    return there is the helper's, not the test's)."""
    todo = list(ast.iter_child_nodes(fn))
    while todo:
        node = todo.pop()
        yield node
        if not isinstance(node, (ast.FunctionDef, ast.Lambda)):
            todo.extend(ast.iter_child_nodes(node))


def function_checks(suite):
    tree = ast.parse(open(os.path.join(LEGACY, suite), encoding='utf-8-sig').read())
    funcs = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
            funcs.append((node.name, node))
        if isinstance(node, ast.ClassDef):
            funcs += [(f'{node.name}.{s.name}', s) for s in node.body
                      if isinstance(s, ast.FunctionDef)
                      and s.name.startswith('test_')]
    rows = []
    for name, fn in funcs:
        lines = set()
        for n in walk_own(fn):
            if isinstance(n, ast.Assert):
                lines.add(n.lineno)
            elif (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                  and n.func.attr.startswith('assert')):
                lines.add(n.lineno)
            elif (isinstance(n, ast.Return) and n.value is not None
                  and not (isinstance(n.value, ast.Constant)
                           and n.value.value is True)):
                lines.add(n.lineno)
        doc = (ast.get_docstring(fn) or '').strip().split('\n')[0]
        where = str(fn.lineno)
        if lines:
            where += ': ' + ', '.join(map(str, sorted(lines)))
        rows.append({'suite': suite, 'function': name, 'line': where,
                     'check': doc or name})
    return rows


def inventory():
    rows = []
    for suite in ORDER:
        if suite in TRACED:
            rows += trace_checks(suite)
        elif suite == 'test_findings_mutation.py':
            rows += mutation_checks(suite)
        elif suite == 'verify_findings.py':
            rows.append({'suite': suite, 'function': 'verify',
                         'line': '33-112',
                         'check': 'FINDINGS.md equals the generation from the '
                                  'artifacts; the cited artifacts are tracked'})
        else:
            rows += function_checks(suite)
    return rows


# -- 2. group maps -----------------------------------------------------------

def group_rows():
    rows = []
    for path in sorted(glob.glob(os.path.join(HERE, 'g*.md'))):
        group = os.path.basename(path).split('-')[0].upper()
        section = None
        for line in open(path, encoding='utf-8'):
            if line.startswith('## '):
                section = line
            if not line.startswith('| ') or line.startswith('| suite'):
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) < 5 or (section and 'For G7' in section):
                continue
            rows.append({'group': group, 'suite': cells[0].replace('.py', ''),
                         'function': cells[1], 'check': cells[2],
                         'new': cells[3], 'note': '|'.join(cells[4:]).strip()})
    return rows


NO_TEST = re.compile(r'^\(?none\b|^none needed|^$', re.I)


def by_function(groups, suite, function):
    short = function.split('.')[-1]
    hits = [g for g in groups if g['suite'] == suite.replace('.py', '')
            and re.search(r'\b' + re.escape(short) + r'\b', g['function'])]
    useful = [g for g in hits if not NO_TEST.match(g['new'])
              and 'set-up only' not in g['note']
              and '(setup)' not in g['check']]
    return useful or hits


# verify.py: the check() calls in trace order, to the index of the group row
# (G1 or G3) among that function's rows, by check name.
VERIFY_NAMES = [
    # test_r04_parse
    ('parse 1,780.00', 'G1', 'parse 1,780.00'),
    ('parse 1780.00', 'G1', 'parse 1780.00'),
    ('parse $1,780.00 value', 'G1', 'parse $1,780.00 value, currency'),
    ('parse $1,780.00 currency', 'G1', 'parse $1,780.00 value, currency'),
    ('parse 1.780,00 (EU)', 'G1', 'parse 1.780,00 (EU)'),
    ('parse (1,780.00)', 'G1', 'parse (1,780.00)'),
    ('parse ($1,780.00) value', 'G1', 'parse ($1,780.00) value, currency'),
    ('parse ($1,780.00) currency', 'G1', 'parse ($1,780.00) value, currency'),
    ('parse 12.5% value', 'G1', 'parse 12.5% value, flag'),
    ('parse 12.5% flag', 'G1', 'parse 12.5% value, flag'),
    ('parse -42.50', 'G1', 'parse -42.50'),
    ('parse \\u221242.50', 'G1', 'parse \u221242.50'),  # name as printed
    ('ambiguous 1.780 raises', 'G1', 'ambiguous 1.780 raises'),
    ('empty string raises', 'G1', 'empty string raises'),
    # test_r04_extract
    ('extract $1,780.00', 'G1', 'extract $1,780.00 and 12.5% from prose'),
    ('extract 12.5%', 'G1', 'extract $1,780.00 and 12.5% from prose'),
    ('extract 274.1375', 'G1', 'extract 274.1375, 259.1375, 777.41'),
    ('extract 259.1375', 'G1', 'extract 274.1375, 259.1375, 777.41'),
    ('extract 777.41', 'G1', 'extract 274.1375, 259.1375, 777.41'),
    ('extract ($2,400.00)', 'G1', 'extract ($2,400.00)'),
    # test_r04_no_float, test_r04_hash
    ('canonical_json refuses float', 'G1', 'canonical_json refuses float'),
    ('canonical_json accepts Decimal', 'G1', 'canonical_json accepts Decimal'),
    ('parse returns Decimal', 'G1', 'parse returns Decimal'),
    ('nested float refused', 'G1', 'nested float refused'),
    ('deterministic hash', 'G1', 'deterministic hash'),
    ('key order irrelevant', 'G1', 'key order irrelevant'),
    # test_r04_round_once
    ('step1 full precision', 'G1', 'step1/2/3 full precision (3 checks)'),
    ('step2 full precision', 'G1', 'step1/2/3 full precision (3 checks)'),
    ('step3 full precision', 'G1', 'step1/2/3 full precision (3 checks)'),
    ('round-once gives 777.41', 'G1', 'round-once 777.41 (HALF_UP, HALF_EVEN)'),
    ('round-once HALF_EVEN also 777.41', 'G1',
     'round-once 777.41 (HALF_UP, HALF_EVEN)'),
    ('round-each gives 777.42', 'G1',
     'round-each 777.42; once != each; mock28 diff 0.01 (3 checks)'),
    ('round-once != round-each', 'G1',
     'round-each 777.42; once != each; mock28 diff 0.01 (3 checks)'),
    ('mock28: discrepancy detected', 'G1',
     'round-each 777.42; once != each; mock28 diff 0.01 (3 checks)'),
    # test_r01_config, test_r01_minimum_n
    ('valid config loads', 'G1',
     'valid example config loads; tolerance Decimal; repeat_count int (3 checks)'),
    ('answer_tolerance is Decimal', 'G1',
     'valid example config loads; tolerance Decimal; repeat_count int (3 checks)'),
    ('repeat_count is int', 'G1',
     'valid example config loads; tolerance Decimal; repeat_count int (3 checks)'),
    ('missing field halts', 'G1', 'missing field halts'),
    ('bare float refused', 'G1', 'bare float refused'),
    ('bare int refused', 'G1', 'bare int refused'),
    ('D6 with 9 items refused', 'G1', 'D6 with 9 refused (message names 9 and 10)'),
    ('D6 with 10 items accepted', 'G1', 'D6 with 10 accepted'),
    ('D1 category A with 9 refused', 'G1', 'D1 category A with 9 refused'),
    # test_r11_seal, test_r11_ap1_hash (G3)
    ('seal has seal_hash', 'G3', '`seal has seal_hash` (64 hex, l.341)'),
    ('seal has ev3_implemented=False', 'G3',
     '`seal has ev3_implemented=False` (l.345)'),
    ('fixture hash stable', 'G3', '`fixture hash stable` (l.356)'),
    ('questions hash stable', 'G3', '`questions hash stable` (l.358)'),
    ('config hash stable', 'G3', '`config hash stable` (l.360)'),
    ('verify_seal passes', 'G3', '`verify_seal passes` (l.371)'),
    ('placeholder hash accepted', 'G3', '`placeholder hash accepted` (l.407)'),
    ('ap1_text_hash computed', 'G3', '`ap1_text_hash computed` (l.408)'),
    ('wrong ap1 hash refused', 'G3', '`wrong ap1 hash refused` (l.423/425)'),
    ('real ap1 hash matches reference file', 'G3',
     '`real ap1 hash matches reference file` (l.442)'),
    ('all ground-truth items compute from fixture', 'G9', None),
    ('ev3_implemented is False', 'G3', '`ev3_implemented is False` (l.511)'),
]
RUN1_PARSE = 'parse_decimal of 8 run-1 literals, value and currency (16 checks)'
RUN1_EXTRACT = 'extract from 4 run-1 prose answers (5 checks)'
OMITTED = 'raises ConfigError; names temperature; explains (3 checks)'

# The group row for the run-1 literals names five tests for 21 checks; its
# note says which covers which. Per literal (G1's note, applied by G9):
RUN1_TESTS = {
    "'$2600.00'": ('test_parse_decimal_leading_currency',
                   'leading currency, as $1,780.00'),
    "'$3109.65'": ('test_parse_decimal_leading_currency',
                   'leading currency, as $1,780.00'),
    "'$286,063.00'": ('test_parse_decimal_leading_currency, '
                      'test_extract_run1_literal_mortgage_prose',
                      'leading currency with grouping; the literal itself '
                      'is pinned in the prose test'),
    "'-$2411.00'": ('test_parse_decimal_currency_after_sign', 'same literal'),
    "'$-2411.00'": ('test_parse_decimal_sign_after_currency', 'same literal'),
    "'($2,411.00)'": ('test_parse_decimal_currency_inside_parentheses',
                      'same shape ($1,780.00 in parentheses)'),
    "'$25'": ('test_parse_decimal_leading_currency',
              'leading currency; an integer parses as any digits'),
    "'$1437.00'": ('test_parse_decimal_leading_currency, '
                   'test_extract_run1_literal_mortgage_prose',
                   'the literal itself is pinned in the prose test'),
    'extract 2600.00': ('test_extract_run1_literal_mortgage_prose, '
                        'test_parse_decimal_leading_currency',
                        'one currency-led figure before the full stop, as in '
                        'the mortgage sentence'),
    'extract 3109.65': ('test_extract_run1_literal_mortgage_prose, '
                        'test_parse_decimal_leading_currency',
                        'as above'),
    'extract 1437.00': ('test_extract_run1_literal_mortgage_prose',
                        'same sentence, whole token list pinned'),
    'extract 286063.00': ('test_extract_run1_literal_mortgage_prose',
                          'same sentence, whole token list pinned'),
    'extract -2411.00': ('test_extract_sign_led_then_currency',
                         "same text ('is -$2411.00.')"),
}

SPEC_PATTERNS = [
    ('spec-table-not-empty', 'spec-table-not-empty'),
    ('spec-count-', 'spec-count-'),
    ('spec-no-stale-counts', 'spec-no-stale-counts'),
    ('instrument-modules-found', 'instrument-modules-found'),
    ('exception-still-breaches-', 'exception-still-breaches-'),
    ('constraint-', 'constraint-'),
    ('no-undeclared-breaches', 'no-undeclared-breaches'),
    ('no-stale-exceptions', 'no-stale-exceptions'),
]

# Checks no group mapped, settled by G9: (suite, function) -> (new, note).
# 'new' uses the same notation as the group maps; names are resolved below.
G9_ROWS = {
    ('verify.py', 'test_ground_truth'): (
        'test_example_ground_truth_every_item_derivable_with_its_final',
        'new (G9); stronger: the ten finals pinned'),
    ('verify_phase_d.py', 'test_d1_transposed_operand_originated'): (
        'test_r41_b02_transposed_operand_is_originated_and_named, '
        'test_classify_invocation_one_untraced_operand_is_originated',
        'same input as B02 (12500 for 15200); originated list pinned exactly'),
    ('verify_phase_d.py', 'test_d2_chained_intermediates_grounded'): (
        'test_r41_b03_correct_operands_are_grounded, '
        'test_classify_invocation_all_operands_traced_is_grounded',
        'every operand traced gives GROUNDED; steps pinned'),
    ('verify_phase_d.py', 'test_d3_percentage_as_fraction_grounded'): (
        'test_r41_b04_percentage_passed_as_fraction_is_grounded, '
        'test_resolve_step2_transformed_source',
        'same expression as B04; transform_used pinned'),
    ('verify_phase_d.py', 'test_d4_quantised_intermediate_grounded_with_finding'): (
        'test_r41_b05_quantised_intermediate_is_grounded_with_finding, '
        'test_classify_invocation_quantised_intermediate_is_a_finding, '
        'test_resolve_step3_quantised_intermediate_records_finding',
        'same intermediate (274.1375 as 274.14); finding pinned whole'),
    ('verify_phase_d.py', 'test_d5_originated_matching_undelivered_field'): (
        'test_r41_b06_operand_from_undelivered_account_is_originated',
        'legacy 2400 (credit_card, not delivered), B06 287500 (mortgage, not '
        'delivered): same branch'),
    ('verify_phase_d.py', 'test_d6_multi_invocation_one_originated'): (
        'test_r41_b07_two_invocations_one_originated_makes_item_originated, '
        'test_classify_item_grounded_only_if_every_invocation_is',
        'same inputs as B07; invocation_count pinned'),
    ('verify_phase_d.py', 'test_d7_empty_invocations_unobservable'): (
        'test_classify_item_without_invocations_is_unobservable',
        'whole result pinned'),
    ('verify_phase_d.py', 'test_d10_abs_without_transform_is_originated'): (
        'test_resolve_step5_sign_inverted_source_is_a_finding, '
        'test_resolve_step2_needs_the_transformation_permitted, '
        'test_r41_b28_magnitude_of_negative_source_without_abs_is_originated',
        '-2400 against a delivered 2400.00, no abs_value: step 5 with a '
        'SIGN-INVERSION finding'),
    ('verify_phase_d.py', 'test_d11_all_grounded_rollup'): (
        'test_r41_b29_all_invocations_grounded_makes_item_grounded, '
        'test_classify_item_all_grounded', ''),
    ('verify_phase_d.py', 'test_d12_negative_literal_extraction'): (
        'test_extract_operands_negative_literal_counted_once_as_negative',
        'same expression; whole list pinned'),
    ('verify_phase_d.py', 'test_d13_empty_invalid_expression'): (
        'test_extract_operands_syntax_error_gives_no_operands, '
        'test_extract_operands_statements_are_not_expressions',
        "legacy inputs '', 'not valid python +++', 'import os' all fail to "
        "parse in eval mode, the same branch"),
    ('verify_phase_d.py', 'test_d14_audit_listing_format'): (
        'test_audit_listing_one_entry_per_originated_operand',
        'every field and the resolution text pinned'),
    ('verify_phase_d.py', 'test_d18_computed_in_session_grounded'): (
        'test_r41_b25_operand_equal_to_grounded_prior_return_is_grounded, '
        'test_resolve_step4_grounded_prior_return, '
        'test_classify_invocation_passes_prior_returns_to_step4',
        'step 4 pinned'),
    ('verify_phase_d.py', 'test_d19_computed_in_session_ungrounded'): (
        'test_r41_b26_operand_equal_to_ungrounded_prior_return_is_originated, '
        'test_resolve_step4_ungrounded_prior_return_is_originated',
        'step 5 and resolution pinned'),
    ('verify_phase_d.py', 'test_d20_sequential_two_calls_second_uses_first'): (
        'test_sequential_grounded_return_grounds_the_next_call, '
        'test_r41_b30_sequential_classification_carries_grounded_returns; '
        'R: multi_round', ''),
    ('verify_phase_d.py', 'test_d21_prior_returns_none_backward_compat'): (
        'test_classify_invocation_passes_prior_returns_to_step4, '
        'test_classify_invocation_all_operands_traced_is_grounded, '
        'test_resolve_step5_untraceable',
        'without prior returns an untraced operand is step 5'),
    ('verify_phase_d.py', 'test_d22_origination_laundering_mandatory'): (
        'test_sequential_originated_return_originates_the_next_call, '
        'F/test_tool_loop.py::test_return_of_originated_call_stays_originated_in_next_call',
        'the second test runs it through the engine'),
    ('verify_phase_d.py', 'test_d23_unobservable_prior'): (
        'test_resolve_step4_ungrounded_prior_return_is_originated, '
        'test_r41_b26_operand_equal_to_ungrounded_prior_return_is_originated',
        'legacy simulates the unobservable prior as grounded=False, the same '
        'input as D19'),
    ('verify_phase_d.py', 'test_d24_sign_inversion_finding_recorded'): (
        'test_resolve_step5_sign_inverted_source_is_a_finding, '
        'test_classify_invocation_originated_entry_keeps_sign_inversion',
        'finding pinned whole, in the resolution and the originated entry'),
    ('verify_phase_d.py', 'test_d25_untraceable_no_sign_inversion'): (
        'test_resolve_step5_untraceable, '
        'test_classify_invocation_one_untraced_operand_is_originated',
        'sign_inversion_finding None pinned'),
    ('verify_e7_coverage.py', 'test_e3_q07_constant_4_resolves'): (
        'test_example_q07_operand_4_resolves_as_declared_constant, '
        'test_example_ground_truth_declared_constants_per_item',
        'new (G9): the shipped example ground truth'),
    ('verify_e7_coverage.py', 'test_q09_negative_12_resolves_to_constant'): (
        'test_resolve_step1_negated_constant_matches_by_magnitude; '
        'R: t3_5_constant_magnitude',
        'finding T3-5 (pinned as today\'s behaviour)'),
    ('verify_e7_coverage.py', 'test_q09_positive_12_still_resolves'): (
        'test_resolve_step1_declared_constant, '
        'test_resolve_step1_exact_constant_wins_over_magnitude', ''),
    ('verify_e7_coverage.py', 'test_q09_q05_unaffected'): (
        'test_example_declared_constants_resolve_at_step1[100-Q05], '
        'test_example_declared_constants_resolve_at_step1[12-Q05]',
        'new (G9)'),
    ('verify_e7_coverage.py', 'test_q09_q08_unaffected'): (
        'test_example_declared_constants_resolve_at_step1[100-Q08], '
        'test_example_declared_constants_resolve_at_step1[12-Q08]',
        'new (G9)'),
    ('verify_d72b.py', 'test_t11_wrong_op_split_route_divergence'): (
        'test_summary_operation_correctness_and_wrong_operation_split, '
        'test_summary_counts_accumulate_after_non_executed_rows, '
        'test_run_report_with_results',
        'legacy computed the split inline in the test (test defect: it '
        'tested a copy); the new tests run the runner\'s split in '
        'runner/summary.py and runner/console.py'),
}

# Checks dropped on purpose by a group (no test), with the reason.
DROPPED = {
    ('verify_phase_b.py', 'test_void_excluded_from_denominator'):
        'the check filters a list inside the test and calls no '
        'production code. The runner\'s own handling of VOID rows is pinned in '
        'U/runner/test_summary.py::test_summary_counts_accumulate_after_non_executed_rows',
}


# -- test name resolution ------------------------------------------------------

def test_index():
    index = {}
    for path in glob.glob(os.path.join(REPO, 'tests', '*', '**', 'test_*.py'),
                          recursive=True):
        rel = os.path.relpath(path, os.path.join(REPO, 'tests'))
        if rel.split(os.sep)[0] not in ('unit', 'conformance', 'functional',
                                        'inspect'):
            continue
        for m in re.finditer(r'^\s*def (test_\w+)', open(path, encoding='utf-8').read(),
                             re.M):
            index.setdefault(m.group(1), set()).add(rel)
    return index


SCENARIOS = {os.path.basename(p)[:-5] for p in
             glob.glob(os.path.join(REPO, 'tests', 'regression', 'scenarios',
                                    '*.json'))}
TEST_RE = re.compile(r'(test_\w+?)(\*|\[[^\]]*\])?(?=[^\w\[*]|$)')


def resolve(text, index, missing):
    """The test names in a group-map cell, as path::name, plus regression
    scenarios, in order of appearance."""
    out = []
    for m in TEST_RE.finditer(text):
        name, suffix = m.group(1), m.group(2) or ''
        if text[max(0, m.start() - 1)] in '/.' or name.endswith('_r41.py'):
            pass
        if suffix == '*' or name.endswith('_'):
            files = {f for n, fs in index.items() if n.startswith(name)
                     for f in fs}
            ref = f'{name}*'
        else:
            files = index.get(name, set())
            ref = name + suffix
        if not files:
            if name.endswith('.py') or text[m.end():m.end() + 3] == '.py':
                continue
            missing.append(text)
            continue
        out.append(f'`{sorted(files)[0]}::{ref}`' if len(files) == 1
                   else f'`{ref}` ({", ".join(sorted(files))})')
    for scen in re.findall(r'R: (\w+)|regression `(\w+)`|scenarios? `(\w+)`|, `(\w+)` pins',
                           text):
        s = next(x for x in scen if x)
        if s in SCENARIOS:
            out.append(f'R:`{s}`')
    for s in re.findall(r'`(\w+)`', text):
        if s in SCENARIOS and f'R:`{s}`' not in out:
            out.append(f'R:`{s}`')
    seen = []
    for o in out:
        if o not in seen:
            seen.append(o)
    return seen


# -- 3. join and write ---------------------------------------------------------

def join(inv, groups):
    index = test_index()
    missing = []
    verify_i = 0
    conf_used = set()
    for row in inv:
        suite, fn = row['suite'], row['function']
        new_text, note, status, src = '', '', 'mapped', ''
        key = (suite, fn)
        if suite == 'verify.py':
            name = row['check'].split('`')[1]
            if fn == 'test_run1_literal_strings':
                want = RUN1_EXTRACT if name.startswith('extract') else RUN1_PARSE
                grp = 'G1'
                literal = next(k for k in RUN1_TESTS if k in name)
            elif fn == 'test_a_omitted_without_reason_refused':
                want, grp = OMITTED, 'G1'
            else:
                exp, grp, want = VERIFY_NAMES[verify_i]
                verify_i += 1
                assert exp == name, (exp, name)
            if grp == 'G9':
                new_text, note = G9_ROWS[key]
                src = 'G9'
            else:
                g = [x for x in groups if x['group'] == grp
                     and x['suite'] == 'verify' and x['function'] == fn
                     and x['check'] == want]
                assert len(g) == 1, (fn, want, g)
                new_text, note, src = g[0]['new'], g[0]['note'], grp
                if fn == 'test_run1_literal_strings':
                    new_text, note = RUN1_TESTS[literal]
        elif suite == 'verify_conformance.py':
            name = row['check'].strip('`')
            g = [i for i, x in enumerate(groups)
                 if x['suite'] == 'verify_conformance' and i not in conf_used
                 and (x['check'] == name or x['check'].startswith(name + ' ('))]
            conf_used.add(g[0])
            x = groups[g[0]]
            new_text, note, src = x['new'], x['note'], x['group']
        elif suite == 'verify_spec.py':
            name = row['check'].strip('`')
            pat = next(p for n, p in SPEC_PATTERNS if name.startswith(n))
            x = next(x for x in groups if x['suite'] == 'verify_spec'
                     and x['check'].startswith(pat))
            new_text, src = '', x['group']
            note = ("dropped by Steven's ruling, 2026-10-20: SPEC's line-count "
                    "table (§12.10) and 300-line limit (§12.9) are not tested; "
                    "their removal from SPEC is proposed to Marcus")
            status = 'dropped'
        elif suite == 'test_findings_mutation.py':
            name = row['check'].strip('`')
            x = next(x for x in groups if x['suite'] == 'test_findings_mutation'
                     and x['check'] == name)
            new_text, note, src = x['new'], x['note'], x['group']
        elif key in G9_ROWS:
            new_text, note = G9_ROWS[key]
            src = 'G9'
        elif key in DROPPED:
            note, status, src = DROPPED[key], 'dropped', 'G2'
        else:
            hits = by_function(groups, suite, fn)
            assert hits, ('unmapped', suite, fn)
            new_text = '; '.join(h['new'] for h in hits)
            notes = [h['note'] for h in hits if h['note']]
            note = ' / '.join(dict.fromkeys(notes))
            src = '+'.join(dict.fromkeys(h['group'] for h in hits))
        refs = resolve(new_text, index, missing) if new_text else []
        if status == 'mapped' and not refs:
            raise SystemExit(f'no test resolved for {suite} {fn} {row["check"]}: '
                             f'{new_text!r}')
        row.update(new=refs, note=note, status=status, src=src)
    if missing:
        raise SystemExit('unknown test names in:\n' + '\n'.join(missing))
    return inv


def md_escape(text):
    return text.replace('|', '\\|').replace('\n', ' ')


def write(rows, header_path):
    sys.path.insert(0, REPO)
    import run_all_tests
    expected = {s[0]: s[3] for s in run_all_tests.SUITES}
    lines = [open(header_path, encoding='utf-8').read().rstrip('\n'), '']
    lines += ['## Summary', '',
              '| suite | checks (run_all_tests) | checks found | mapped | '
              'dropped on purpose | pending ruling |',
              '|---|---|---|---|---|---|']
    totals = [0, 0, 0, 0, 0]
    for suite in ORDER:
        rs = [r for r in rows if r['suite'] == suite]
        n = [expected[suite], len(rs),
             sum(r['status'] == 'mapped' for r in rs),
             sum(r['status'] == 'dropped' for r in rs),
             sum(r['status'] == 'pending' for r in rs)]
        assert n[0] == n[1], (suite, n)
        totals = [a + b for a, b in zip(totals, n)]
        lines.append(f'| {suite} | ' + ' | '.join(map(str, n)) + ' |')
    lines.append('| **total** | ' + ' | '.join(f'**{t}**' for t in totals) + ' |')
    lines += ['', '`verify_hashes.py` (run by CI only, not by run_all_tests.py) is '
              'in its own section at the end.', '']
    for suite in ORDER:
        rs = [r for r in rows if r['suite'] == suite]
        plural = 's' if len(rs) != 1 else ''
        lines += [f'## {suite} ({len(rs)} check{plural})', '',
                  '| function | line | check | new test(s) | note |',
                  '|---|---|---|---|---|']
        for r in rs:
            status = {'mapped': '', 'dropped': '**dropped**: ',
                      'pending': '**pending ruling**: '}[r['status']]
            src = f' ({r["src"]})' if r['src'] else ''
            lines.append(
                f'| {r["function"]} | {r["line"]} | {md_escape(r["check"])} | '
                f'{"<br>".join(r["new"]) or "none"} | '
                f'{status}{md_escape(r["note"])}{src} |')
        lines.append('')
    lines.append(open(header_path.replace('_header', '_footer'),
                      encoding='utf-8').read().rstrip('\n'))
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    return totals


def main():
    rows = join(inventory(), group_rows())
    totals = write(rows, os.path.join(HERE, 'retirement_header.md'))
    print(f'{OUT}: {totals[1]} checks, {totals[2]} mapped, {totals[3]} dropped, '
          f'{totals[4]} pending')


if __name__ == '__main__':
    main()
