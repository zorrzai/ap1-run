"""The live runner's console report.

print_run_report prints sections 3a to 3i once every execution has run;
print_scoring_report prints 3j to 3l once D1 and D2 are aggregated and
the summary is built. The text is pinned by the regression baseline,
including its known flaws (the literal backslash-n before 3h2).
"""

from collections import Counter

from ap1_run.runner.summary import measure_invocation_by_condition
from ap1_run.scoring.invocation import format_rate


def print_run_report(all_results, conditions, *, disclaimer, grammar_issues,
                     decline_findings, tool_call_structures,
                     evidence_findings, unmeasured_cells,
                     transcription_results, release_coverage_results):
    """Sections 3a-3i: completion, figure identification, grammar,
    declines, tool-call structures, evidence classes, unmeasured cells,
    D7.1 invocation, D7.3 transcription and release coverage, D7.2(b)."""
    print()
    print('=' * 60)
    print('SMOKE TEST REPORT')
    print('=' * 60)
    print()
    print(disclaimer)

    # 3a. Completion
    executed = [r for r in all_results if r['status'] == 'EXECUTED']
    unmeasured = [r for r in all_results if r['status'] == 'UNMEASURED']
    void = [r for r in all_results if r['status'] == 'VOID']
    not_run = [r for r in all_results if r['status'] == 'NOT-RUN']
    print(f'\n3a. COMPLETION: {len(executed)} executed, {len(unmeasured)} unmeasured, {len(void)} void'
          + (f', {len(not_run)} not run (the transcript ends before them)'
             if not_run else ''))

    # 3b. Figure identification
    print('\n3b. FIGURE IDENTIFICATION:')
    outcomes = {}
    for r in executed:
        o = r.get('figure_outcome', 'unknown')
        outcomes[o] = outcomes.get(o, 0) + 1
    for o, c in sorted(outcomes.items()):
        print(f'  {o}: {c}')
    auto_scored = sum(c for o, c in outcomes.items()
                      if o in ('AUTO-MATCH', 'AUTO-NO-FIGURE'))
    adjudicated = sum(c for o, c in outcomes.items()
                      if o.startswith('ADJUDICATE') or o == 'UNMEASURABLE')
    total = auto_scored + adjudicated
    if total > 0:
        print(f'  Auto-scored: {auto_scored}/{total} ({100*auto_scored/total:.0f}%)')
        print(f'  Adjudicated: {adjudicated}/{total} ({100*adjudicated/total:.0f}%)')

    # Per-item detail
    print('\n  Per item (base condition, first repeat):')
    for r in executed:
        if r['condition'] == 'base' and r['repeat'] == 1:
            print(f'    {r["item_id"]}: {r["figure_outcome"]} — {r.get("figure_reason", "")}')

    # 3c. Grammar issues
    print(f'\n3c. NUMERIC GRAMMAR: {len(grammar_issues)} issues')

    # 3d. Decline findings
    print(f'\n3d. DECLINE MARKERS: {len(decline_findings)} unrecognised declines')

    # 3e. Tool-call structures
    print(f'\n3e. TOOL-CALL ARGUMENT STRUCTURES: {len(tool_call_structures)} calls')

    # 3f. Evidence classes
    print(f'\n3f. EVIDENCE CLASSES:')
    ev_counts = {}
    for ef in evidence_findings:
        ec = ef['evidence_class']
        ev_counts[ec] = ev_counts.get(ec, 0) + 1
    for ec, c in sorted(ev_counts.items()):
        print(f'  {ec}: {c}')

    # 3g. Unmeasured cells
    print(f'\n3g. UNMEASURED CELLS: {len(unmeasured_cells)}')

    # 3h. Invocation under both conditions. n counts computable questions
    # with an observed outcome; a question fails if any repeat is
    # NOT-INVOKED; UNOBSERVABLE (EV-0) executions are in no n.
    print(f'\n3h. D7.1 INVOCATION (n = questions; a question fails if any '
          f'repeat is NOT-INVOKED; UNOBSERVABLE not in n):')
    measured = measure_invocation_by_condition(all_results)
    for cond in conditions:
        m = measured.get(cond, {'per_class': {}, 'cross_class_warning': None})
        observed = {ec: c for ec, c in m['per_class'].items() if c['n'] > 0}
        invoked = sum(c['invoked'] for c in observed.values())
        not_invoked = sum(c['not_invoked'] for c in observed.values())
        n = sum(c['n'] for c in observed.values())
        print(f'  {cond}: invoked={invoked} not_invoked={not_invoked} n={n}')
        for ec, c in m['per_class'].items():
            if c['unobservable']:
                print(f'    {ec or "no evidence class"} executions: '
                      f'{c["unobservable"]} UNOBSERVABLE, not in n')
        if m['cross_class_warning']:
            print(f'    {m["cross_class_warning"]}')
        if len(observed) > 1:
            for ec, c in observed.items():
                print(f'    failure rate ({ec}): {c["failure_rate"]}')
        else:
            rate_str = format_rate(not_invoked, n)
            print(f'    failure rate: {rate_str}')

    # 3h2. D7.3 Transcription
    print(f'\\n3h2. D7.3 TRANSCRIPTION:')
    tr_counts = Counter(r['outcome'] for r in transcription_results)
    for outcome in ['TRANSCRIBED-EXACT', 'TRANSCRIBED-ALTERED', 'UNOBSERVABLE']:
        print(f'  {outcome}: {tr_counts.get(outcome, 0)}')

    # 3h3. D7.3 Release Coverage
    print(f'\n3h3. D7.3 RELEASE COVERAGE:')
    rc_counts = Counter(r['outcome'] for r in release_coverage_results)
    for outcome in ['GOVERNED-RELEASE', 'PARTIALLY-GOVERNED',
                    'COVERAGE-UNOBSERVABLE']:
        print(f'  {outcome}: {rc_counts.get(outcome, 0)}')
    pg_items = [r for r in release_coverage_results
                if r['outcome'] == 'PARTIALLY-GOVERNED']
    if pg_items:
        print(f'  PARTIALLY-GOVERNED findings:')
        for r in pg_items:
            print(f'    {r["item_id"]}/{r["condition"]}/r{r["repeat"]}: {r["finding"]}')

    # 3i. D7.2(b) operation correctness
    print(f'\n3i. D7.2(b) OPERATION CORRECTNESS:')
    op_counts = {'OPERATION-CORRECT': 0, 'WRONG-OPERATION': 0,
                 'OPERATION-UNOBSERVABLE': 0}
    wo_split = {'route_divergence': 0, 'item_wrong': 0, 'undetermined': 0,
                'no_figure': 0}
    for r in executed:
        fig = r.get('figure_outcome', '')
        for oc in r.get('operation_correctness', []):
            outcome = oc.get('outcome', 'OPERATION-UNOBSERVABLE')
            if outcome in op_counts:
                op_counts[outcome] += 1
            if outcome == 'WRONG-OPERATION':
                if fig == 'AUTO-MATCH':
                    wo_split['route_divergence'] += 1
                elif fig.startswith('ADJUDICATE') or fig == 'UNMEASURABLE':
                    # UNMEASURABLE goes to adjudication and is never scored
                    # incorrect (SPEC R2.0 step 0; T3-63)
                    wo_split['undetermined'] += 1
                elif fig == 'AUTO-NO-FIGURE':
                    # no figure released: D1 scores NO-FIGURE, not
                    # INCORRECT, so there is no item answer (T3-63)
                    wo_split['no_figure'] += 1
                else:
                    wo_split['item_wrong'] += 1
    for outcome in ['OPERATION-CORRECT', 'WRONG-OPERATION', 'OPERATION-UNOBSERVABLE']:
        print(f'  {outcome}: {op_counts[outcome]}')
    wo_total = sum(wo_split.values())
    if wo_total > 0:
        print(f'    of which:')
        print(f'      route divergence (item answer correct):      {wo_split["route_divergence"]}')
        print(f'      item answer incorrect:                       {wo_split["item_wrong"]}')
        print(f'      item answer undetermined (adjudicated):      {wo_split["undetermined"]}')
        print(f'      no figure released (no item answer):         {wo_split["no_figure"]}')


def print_scoring_report(d1_summary, d2_results, d2_cap_reason, summary):
    """Sections 3j-3l: D1 accuracy, D2 reproducibility, D7.2(a) operand
    provenance."""
    # 3j. D1 Accuracy
    print(f'\n3j. D1 ACCURACY:')
    if d1_summary:
        print(f'  Auto-scored: {d1_summary.get("auto_scored_n", 0)}')
        print(f'  Adjudicated: {d1_summary.get("adjudicated_n", 0)}')
        print(f'  Correct: {d1_summary.get("correct", 0)}')
        print(f'  Incorrect: {d1_summary.get("incorrect", 0)}')
        print(f'  No figure: {d1_summary.get("no_figure", 0)}')
        rate = d1_summary.get('accuracy_rate')
        if rate is not None:
            print(f'  Accuracy rate: {rate}')

    # 3k. D2 Reproducibility
    print(f'\n3k. D2 REPRODUCIBILITY:')
    if d2_cap_reason:
        print(f'  CAP: {d2_cap_reason}')
    d2_mechs = {}
    for key, surfaces in d2_results.items():
        for surface, mech in surfaces.items():
            m = mech['mechanism']
            d2_mechs[m] = d2_mechs.get(m, 0) + 1
    for m, c in sorted(d2_mechs.items()):
        print(f'  {m}: {c}')

    # 3l. Operand provenance step counts
    print(f'\n3l. D7.2(a) OPERAND PROVENANCE:')
    step_counts = summary.get('operand_step_counts', {})
    s1_src = summary.get('step_1_source', 0)
    s1_const = summary.get('step_1_constant', 0)
    step_names = {2: 'transformed source',
                  3: 'reference intermediate', 4: 'computed in session'}
    print(f'  step 1 (source match):       {s1_src}')
    print(f'  step 1 (declared constant):  {s1_const}')
    for step in range(2, 5):
        print(f'  step {step} ({step_names[step]}): {step_counts.get(step, 0)}')
    s5_si = summary.get('step_5_sign_inverted', 0)
    s5_uc = summary.get('step_5_ungrounded_chain', 0)
    s5_ut = summary.get('step_5_untraceable', 0)
    print(f'  step 5 (originated, sign-inverted from source):          {s5_si}')
    print(f'  step 5 (originated, computed from ungrounded invocation): {s5_uc}')
    print(f'  step 5 (originated, no traceable basis):                  {s5_ut}')
    prov_out = summary.get('provenance_outcomes', {})
    print(f'  OPERANDS-GROUNDED: {prov_out.get("OPERANDS-GROUNDED", 0)}')
    print(f'  OPERAND-ORIGINATED: {prov_out.get("OPERAND-ORIGINATED", 0)}')
    print(f'  OPERANDS-UNOBSERVABLE: '
          f'{prov_out.get("OPERANDS-UNOBSERVABLE", 0)}')
    print(f'  UNMEASURABLE: {prov_out.get("UNMEASURABLE", 0)}')
