"""The live runner's aggregation of per-execution results.

verify_invocation_consistency refuses a run whose invocation outcomes
contradict their own evidence; find_d2_cap and classify_reproducibility
give D2 per item and condition; build_summary assembles the summary that
report.generate_report() reads.
"""

from ap1_run.scoring.invocation import compute_dpr
from ap1_run.scoring.reproducibility import classify_mechanism


def verify_invocation_consistency(results):
    """INVARIANT: INVOKED implies tool_calls present; NOT-INVOKED implies none.

    A scoring outcome that contradicts its own evidence is not a finding,
    it is a defect. The instrument must refuse to report it.

    Raises RuntimeError (FATAL) on the first mismatch, naming the item.
    """
    for r in results:
        if r.get('status') != 'EXECUTED':
            continue
        outcome = r.get('invocation_outcome', '')
        tc_count = r.get('tool_calls_count', 0)
        item_id = r.get('item_id', '?')
        condition = r.get('condition', '?')
        repeat = r.get('repeat', '?')

        if outcome == 'INVOKED' and tc_count == 0:
            raise RuntimeError(
                f'FATAL: invocation consistency check failed. '
                f'{item_id}/{condition}/r{repeat}: '
                f'INVOKED but tool_calls_count=0. '
                f'A scoring outcome that contradicts its own evidence '
                f'is a defect, not a finding.')

        if outcome == 'NOT-INVOKED' and tc_count > 0:
            raise RuntimeError(
                f'FATAL: invocation consistency check failed. '
                f'{item_id}/{condition}/r{repeat}: '
                f'NOT-INVOKED but tool_calls_count={tc_count}. '
                f'A scoring outcome that contradicts its own evidence '
                f'is a defect, not a finding.')


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


def build_summary(all_results, evidence_findings, *,
                  d1_summary=None, d2_results=None,
                  d2_cap_reason=None,
                  transcription_results=None,
                  release_coverage_results=None,
                  held_constant=None):
    """Build the summary dict that report.generate_report() expects.

    Aggregates per-item results into the structure report.py reads.
    held_constant names what the R1.2 guard held constant between the
    conditions (AP-1 D7.8), for the report.
    """
    summary = {}
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

    # Invocation figures per condition
    inv_figures = {}
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        cond = r.get('condition', '')
        key = f'd7_invocation_{cond}'
        if key not in inv_figures:
            inv_figures[key] = {'failures': 0, 'n': 0, 'rate': None}
        inv_figures[key]['n'] += 1
        if r.get('invocation_outcome') == 'NOT-INVOKED':
            inv_figures[key]['failures'] += 1
    for key, data in inv_figures.items():
        if data['n'] > 0:
            data['rate'] = f"{data['n'] - data['failures']}/{data['n']}"
    summary['invocation_figures'] = inv_figures

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
    wrong_op_split = {'route_divergence': 0, 'item_wrong': 0, 'undetermined': 0}
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        fig = r.get('figure_outcome', '')
        for oc in r.get('operation_correctness', []):
            outcome = oc.get('outcome', 'OPERATION-UNOBSERVABLE')
            if outcome in op_counts:
                op_counts[outcome] += 1
            if outcome == 'WRONG-OPERATION':
                if fig == 'AUTO-MATCH':
                    wrong_op_split['route_divergence'] += 1
                elif fig.startswith('ADJUDICATE'):
                    wrong_op_split['undetermined'] += 1
                else:
                    wrong_op_split['item_wrong'] += 1
    summary['operation_correctness_counts'] = op_counts
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
        'n': total_executed,  # every execution with observable evidence
        'auto_scored_n': auto_n,
        'adjudicated_n': adj_n,
    }

    # D1 results
    if d1_summary:
        summary['d1_results'] = d1_summary

    # D2 results
    if d2_results:
        summary['d2_results'] = d2_results
    if d2_cap_reason:
        summary['d2_cap_reason'] = d2_cap_reason

    # Operand provenance step counts (D7.2(a))
    step_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    step_1_source = 0
    step_1_constant = 0
    step_5_sign_inverted = 0
    step_5_ungrounded_chain = 0
    step_5_untraceable = 0
    prov_outcomes = {'OPERANDS-GROUNDED': 0, 'OPERAND-ORIGINATED': 0}
    originated_audit = []
    for r in all_results:
        if r.get('status') != 'EXECUTED':
            continue
        for prov in r.get('provenance_results', []):
            outcome = prov.get('outcome', '')
            if outcome in prov_outcomes:
                prov_outcomes[outcome] += 1
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
            for orig in prov.get('originated_operands', []):
                originated_audit.append({
                    'item_id': r.get('item_id'),
                    'condition': r.get('condition'),
                    **orig,
                })
    summary['operand_step_counts'] = step_counts
    summary['step_1_source'] = step_1_source
    summary['step_1_constant'] = step_1_constant
    summary['step_5_sign_inverted'] = step_5_sign_inverted
    summary['step_5_ungrounded_chain'] = step_5_ungrounded_chain
    summary['step_5_untraceable'] = step_5_untraceable
    summary['provenance_outcomes'] = prov_outcomes
    summary['originated_operand_audit'] = originated_audit

    # Non-outcome cells
    non_outcome = []
    for r in all_results:
        if r['status'] in ('UNMEASURED', 'VOID'):
            non_outcome.append({
                'item_id': r.get('item_id'),
                'condition': r.get('condition'),
                'status': r['status'],
                'reason': r.get('cause', r.get('reason', '')),
            })
    summary['non_outcome_cells'] = non_outcome

    return summary
