"""The live runner's aggregation of per-execution results.

verify_invocation_consistency refuses a run whose invocation outcomes
contradict their own evidence; find_d2_cap and classify_reproducibility
give D2 per item and condition; build_summary assembles the summary that
report.generate_report() reads.
"""

from ap1_run.scoring.invocation import compute_dpr, measure_invocation

from ap1_run.scoring.reproducibility import classify_mechanism

_OUTCOME_OBSERVED = {'INVOKED': True, 'NOT-INVOKED': False}


def verify_invocation_consistency(results):
    """INVARIANT: INVOKED implies a call to the required operation;
    NOT-INVOKED implies none.

    A scoring outcome that contradicts its own evidence is not a finding,
    it is a defect. The instrument must refuse to report it.

    Calls to other tools (unoffered or hallucinated ones) are recorded and
    reported but do not affect D7.1 (SPEC R0.3, R2.3; T3-38): the row
    counts them in other_tool_calls_count (absent when there are none),
    and they are left out of the count checked here.

    Raises RuntimeError (FATAL) on the first mismatch, naming the item.
    """
    for r in results:
        if r.get('status') != 'EXECUTED':
            continue
        outcome = r.get('invocation_outcome', '')
        tc_count = r.get('tool_calls_count', 0) - \
            r.get('other_tool_calls_count', 0)
        item_id = r.get('item_id', '?')
        condition = r.get('condition', '?')
        repeat = r.get('repeat', '?')

        if outcome == 'INVOKED' and tc_count == 0:
            raise RuntimeError(
                f'FATAL: invocation consistency check failed. '
                f'{item_id}/{condition}/r{repeat}: '
                f'INVOKED but no call to the required operation. '
                f'A scoring outcome that contradicts its own evidence '
                f'is a defect, not a finding.')

        if outcome == 'NOT-INVOKED' and tc_count > 0:
            raise RuntimeError(
                f'FATAL: invocation consistency check failed. '
                f'{item_id}/{condition}/r{repeat}: '
                f'NOT-INVOKED but {tc_count} call(s) to the required '
                f'operation. '
                f'A scoring outcome that contradicts its own evidence '
                f'is a defect, not a finding.')


def measure_invocation_by_condition(all_results):
    """D7.1 per condition, from the runner's per-execution rows.

    Only EXECUTED rows count (UNMEASURED and VOID cells are in no
    denominator). Each row becomes a measure_invocation record: INVOKED
    and NOT-INVOKED are observations, any other outcome (None for EV-0)
    is UNOBSERVABLE. Returns {condition: measure_invocation(...)} in the
    order the conditions first appear, each with an extra 'executions'
    entry: {evidence_class: (executions, distinct questions)}.
    """
    by_condition = {}
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        by_condition.setdefault(r.get('condition', ''), []).append({
            'item_id': r.get('item_id'),
            'invoked': _OUTCOME_OBSERVED.get(r.get('invocation_outcome')),
            'evidence_class': r.get('evidence_class') or '',
        })
    measured = {}
    for cond, records in by_condition.items():
        m = measure_invocation(records)
        per_class = {}
        for rec in records:
            per_class.setdefault(rec['evidence_class'], []).append(
                rec['item_id'])
        m['executions'] = {ec: (len(ids), len(set(ids)))
                           for ec, ids in sorted(per_class.items())}
        measured[cond] = m
    return measured


def find_d2_cap(sampling):
    """The D2.2 cap reason, or None.

    If any sampling parameter was platform-rejected, the mechanism class
    is capped at OBSERVED-ONLY. The config encodes omissions inside the
    sampling block:
    {"temperature": {"value": "omitted", "reason": "platform-rejected", ...}}
    The first such parameter gives the reason.
    """
    d2_cap_reason = None
    for param_name, param_val in sampling.items():
        if not isinstance(param_val, dict):
            continue
        reason = param_val.get('reason', '')
        if 'platform-rejected' in reason.lower() or \
                'platform-unsupported' in reason.lower():
            detail = param_val.get('detail', reason)
            d2_cap_reason = (
                f'D2.2 cap: {param_name} was {reason}. '
                f'Detail: {detail}')
            break
    return d2_cap_reason


def classify_reproducibility(d2_responses, repeat_count, d2_cap_reason):
    """D2 mechanism class per (item, condition) and per surface.

    d2_responses maps (item_id, condition) to the responses of its
    repeats. Returns {'<item_id>/<condition>': {surface: mechanism}}.
    """
    d2_results = {}
    for (item_id, cond), responses in d2_responses.items():
        key = f'{item_id}/{cond}'
        d2_results[key] = {}
        for surface in ('figures', 'prose'):
            mech = classify_mechanism(
                responses,
                surface=surface,
                minimum_runs=repeat_count,
                operator_declared=None,
            )
            # D2.2 cap: platform-rejected -> cap at OBSERVED-ONLY
            if d2_cap_reason and mech['mechanism'] not in ('UNMEASURED',):
                mech['mechanism'] = 'OBSERVED-ONLY'
                mech['d2_cap'] = d2_cap_reason
            d2_results[key][surface] = mech
    return d2_results


def summarise_parameter_echo(checks):
    """The run's D2.2 parameter-echo result: MISMATCH if any response
    shows a requested parameter not applied, VERIFIED if every response
    echoed and matched, UNVERIFIED otherwise (including no responses);
    with each distinct finding once, in first-seen order."""
    statuses = {c['status'] for c in checks}
    if 'MISMATCH' in statuses:
        status = 'MISMATCH'
    elif statuses == {'VERIFIED'}:
        status = 'VERIFIED'
    else:
        status = 'UNVERIFIED'
    findings = []
    for c in checks:
        for f in c['findings']:
            if f not in findings:
                findings.append(f)
    return {'status': status, 'responses': len(checks),
            'findings': findings}


def build_summary(all_results, evidence_findings, *,
                  d1_summary=None, d2_results=None,
                  d2_cap_reason=None,
                  transcription_results=None,
                  release_coverage_results=None,
                  parameter_echo=None,
                  held_constant=None, served=None):
    """Build the summary dict that report.generate_report() expects.

    Aggregates per-item results into the structure report.py reads.
    held_constant names what the R1.2 guard held constant between the
    conditions (AP-1 D7.8), for the report. served counts the models and
    backend fingerprints the responses report (V12-8).
    """
    summary = {}
    if served is not None:
        summary['served'] = served
    summary['transcription_results'] = transcription_results or []
    summary['release_coverage_results'] = release_coverage_results or []

    # Evidence class counts
    ev_counts = {}
    for ef in evidence_findings:
        ec = ef.get('evidence_class', '')
        ev_counts[ec] = ev_counts.get(ec, 0) + 1
    summary['evidence_class_counts'] = ev_counts

    # Item evidence detail
    summary['item_evidence'] = evidence_findings

    # D7.1 invocation figures per condition and evidence class. The unit
    # is the computable question; EV-0 (UNOBSERVABLE) executions are not
    # in n and are listed per class in invocation_evidence.
    inv_figures = {}
    inv_evidence = {}
    for cond, m in measure_invocation_by_condition(all_results).items():
        classes = {ec: c for ec, c in m['per_class'].items() if c['n'] > 0}
        inv_evidence[cond] = {
            'classes': {ec: {'executions': m['executions'][ec][0],
                             'questions': m['executions'][ec][1],
                             'observed_questions': c['n'],
                             'unobservable_executions': c['unobservable']}
                        for ec, c in m['per_class'].items()},
            'cross_class_warning': m['cross_class_warning'],
        }
        if not classes:
            classes = {None: {'n': 0, 'not_invoked': 0}}
        for ec, c in classes.items():
            key = f'd7_invocation_{cond}'
            if len(classes) > 1:
                key += f' ({ec})'
            n, k = c['n'], c['not_invoked']
            inv_figures[key] = {
                'failures': k, 'n': n,
                'rate': f'{n - k}/{n}' if n > 0 else None,
                'condition': cond, 'evidence_class': ec,
                'unobservable': m['unobservable_n'],
            }
    summary['invocation_figures'] = inv_figures
    summary['invocation_evidence'] = inv_evidence

    # D7.8 contrast: what was held constant, and the drop-in-performance
    # ratio DPR = (I_base - I_removed) / I_base (R2.3; UNDEFINED where
    # I_base is zero or an arm has no observations)
    summary['held_constant'] = list(held_constant or [])
    no_figures = dict.fromkeys(('n', 'failures'), 0)
    arms = [inv_figures.get(f'd7_invocation_{cond}', no_figures)
            for cond in ('base', 'instruction_removed')]
    _, summary['dpr'] = compute_dpr(
        *[a['n'] - a['failures'] for a in arms], *[a['n'] for a in arms])

    # Operation correctness counts
    op_counts = {'OPERATION-CORRECT': 0, 'WRONG-OPERATION': 0,
                 'OPERATION-UNOBSERVABLE': 0}
    wrong_op_split = {'route_divergence': 0, 'item_wrong': 0, 'undetermined': 0,
                      'no_figure': 0}
    op_unobservable = []
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        fig = r.get('figure_outcome', '')
        for oc in r.get('operation_correctness', []):
            outcome = oc.get('outcome', 'OPERATION-UNOBSERVABLE')
            if outcome in op_counts:
                op_counts[outcome] += 1
            if outcome == 'OPERATION-UNOBSERVABLE':
                # a non-outcome cell, listed in report §10 (T3-35)
                op_unobservable.append(_cell(r, oc.get('detail')
                                             or oc.get('reason')))
            if outcome == 'WRONG-OPERATION':
                if fig == 'AUTO-MATCH':
                    wrong_op_split['route_divergence'] += 1
                elif fig.startswith('ADJUDICATE') or fig == 'UNMEASURABLE':
                    # UNMEASURABLE goes to adjudication and is never scored
                    # incorrect (SPEC R2.0 step 0; T3-63)
                    wrong_op_split['undetermined'] += 1
                elif fig == 'AUTO-NO-FIGURE':
                    # no figure released: D1 scores NO-FIGURE, not
                    # INCORRECT, so there is no item answer (T3-63)
                    wrong_op_split['no_figure'] += 1
                else:
                    wrong_op_split['item_wrong'] += 1
    summary['operation_correctness_counts'] = op_counts
    summary['operation_unobservable'] = op_unobservable
    summary['wrong_operation_split'] = wrong_op_split

    # Scoring proportions (D1 and D7)
    auto_n = sum(1 for r in all_results
                 if r.get('status') == 'EXECUTED' and
                 r.get('figure_outcome', '').startswith('AUTO'))
    adj_n = sum(1 for r in all_results
                if r.get('status') == 'EXECUTED' and
                (r.get('figure_outcome', '').startswith('ADJUDICATE') or
                 r.get('figure_outcome') == 'UNMEASURABLE'))
    total_executed = sum(1 for r in all_results
                        if r.get('status') == 'EXECUTED')
    summary['d7_results'] = {
        'n': total_executed,  # every executed response (any class)
        'auto_scored_n': auto_n,
        'adjudicated_n': adj_n,
    }

    # The evidence classes each D7 figure rests on (AP-1 D7.7; T3-29):
    # D7.2(b) on the executions with an evaluated operation, D7.3 on
    # every executed response
    d7_evidence = {'D7.2(b)': {}, 'D7.3': {}}
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        ec = r.get('evidence_class') or ''
        figures = ['D7.2(b)', 'D7.3'] if r.get('operation_correctness') \
            else ['D7.3']
        for figure in figures:
            d7_evidence[figure][ec] = d7_evidence[figure].get(ec, 0) + 1
    summary['d7_evidence'] = d7_evidence

    # D1 results
    if d1_summary:
        summary['d1_results'] = d1_summary

    # D2 results
    if d2_results:
        summary['d2_results'] = d2_results
    if d2_cap_reason:
        summary['d2_cap_reason'] = d2_cap_reason
    summary['parameter_echo'] = summarise_parameter_echo(parameter_echo or [])

    # Operand provenance step counts (D7.2(a))
    step_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    step_1_source = 0
    step_1_constant = 0
    step_5_sign_inverted = 0
    step_5_ungrounded_chain = 0
    step_5_untraceable = 0
    prov_outcomes = {'OPERANDS-GROUNDED': 0, 'OPERAND-ORIGINATED': 0,
                     'OPERANDS-UNOBSERVABLE': 0, 'UNMEASURABLE': 0}
    originated_audit = []
    unmeasurable = []
    operands_unobservable = []
    quantisation_findings = []
    near_miss_findings = []
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        reasons = []
        for prov in r.get('provenance_results', []):
            outcome = prov.get('outcome', '')
            if outcome in prov_outcomes:
                prov_outcomes[outcome] += 1
            if outcome == 'OPERANDS-UNOBSERVABLE':
                # a non-outcome cell, listed in report §10 (T3-35)
                operands_unobservable.append(_cell(r, prov.get('reason')))
            if outcome == 'UNMEASURABLE':
                # D7.2 is unmeasurable for the item (T3-42): its operands
                # are neither grounded nor originated findings.
                reasons.append(prov.get('reason'))
                continue
            for res in prov.get('operand_resolutions', []):
                step = res.get('step')
                if step in step_counts:
                    step_counts[step] += 1
                if step == 1:
                    if res.get('resolution') == 'constant':
                        step_1_constant += 1
                    else:
                        step_1_source += 1
                if step == 5:
                    if res.get('sign_inversion_finding'):
                        step_5_sign_inverted += 1
                    elif res.get('resolution') == 'computed_in_session_ungrounded':
                        step_5_ungrounded_chain += 1
                    else:
                        step_5_untraceable += 1
            # D7.2(a)(iii) quantisation findings and near misses, for
            # report §11 (T3-34)
            for qf in prov.get('quantisation_findings', []):
                quantisation_findings.append(dict(
                    _where(r), operand=qf.get('operand'),
                    finding=f'grounded via intermediate '
                            f'{qf.get("matched_intermediate")} only after '
                            f'quantisation, in `{qf.get("expression")}`'))
            for res in prov.get('operand_resolutions', []):
                if res.get('near_miss_finding'):
                    near_miss_findings.append(dict(
                        _where(r), **res['near_miss_finding']))
            for orig in prov.get('originated_operands', []):
                originated_audit.append({
                    'item_id': r.get('item_id'),
                    'condition': r.get('condition'),
                    'repeat': r.get('repeat'),
                    **orig,
                })
        if reasons:
            unmeasurable.append({'item_id': r.get('item_id'),
                                 'condition': r.get('condition'),
                                 'repeat': r.get('repeat'),
                                 'reason': reasons[0]})
    summary['operand_step_counts'] = step_counts
    summary['step_1_source'] = step_1_source
    summary['step_1_constant'] = step_1_constant
    summary['step_5_sign_inverted'] = step_5_sign_inverted
    summary['step_5_ungrounded_chain'] = step_5_ungrounded_chain
    summary['step_5_untraceable'] = step_5_untraceable
    summary['provenance_outcomes'] = prov_outcomes
    summary['originated_operand_audit'] = originated_audit
    summary['provenance_unmeasurable'] = unmeasurable
    summary['operands_unobservable'] = operands_unobservable
    summary['quantisation_findings'] = quantisation_findings
    summary['near_miss_findings'] = near_miss_findings

    # Non-outcome cells (NOT-RUN: a partial transcript's unreached
    # executions, R0.3)
    non_outcome = []
    for r in all_results:
        if r['status'] in ('UNMEASURED', 'VOID', 'NOT-RUN'):
            non_outcome.append({
                'item_id': r.get('item_id'),
                'condition': r.get('condition'),
                'repeat': r.get('repeat'),
                'status': r['status'],
                'reason': r.get('cause', r.get('reason', '')),
            })
    summary['non_outcome_cells'] = non_outcome

    return summary


def _where(result):
    """The execution a result belongs to."""
    return {'item_id': result.get('item_id'),
            'condition': result.get('condition'),
            'repeat': result.get('repeat')}


def _cell(result, reason):
    """A non-outcome cell of one execution: where it is, and why."""
    return dict(_where(result), reason=reason)
