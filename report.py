"""R3.3 -- Report Generator.

Spec: AP-1 Runner Build Spec v0.3, section 6 R3.3.

Produce the evaluation report as a markdown document. The report is the
evaluation artifact: it is what the operator publishes and what a reviewer
reads to assess the evaluation.

Contents (SPEC.md R3.3 interface):
  1.  Pre-registration record (all hashes, AP-1 text hash, version DOI)
  2.  Resolved configuration verbatim
  3.  Per-dimension results with n
  4.  Every D7 figure with its evidence class
  5.  Zero-failure results with exact one-sided 95% Clopper-Pearson bound
  6.  D7.2(a) originated-operand listing
  7.  D7.2(b) operation-correctness counts
  8.  Proportion auto-scored vs adjudicated, per dimension
  9.  D2 mechanism classes per surface
  10. Every UNMEASURED, UNOBSERVABLE, UNMEASURABLE and VOID cell with reason
  11. Quantisation and near-miss findings
  12. DECLARATION of which dimensions were NOT measured

Clopper-Pearson:
  k=0 only (closed form): p_upper = 1 - alpha^(1/n), alpha = 0.05.
  For k>0: point estimate with n, no bound. AP-1 v1.3 D7.5 specifies
  the zero-failure form only. This is a declared limitation, not a
  silent omission.

D2 Mechanism Classes:
  D2 is auto-measured. Per surface, report: mechanism class,
  whether determined from evidence or operator-declared,
  parameter-echo verification result (or UNVERIFIED where endpoint
  echoes nothing).

Classification: DETERMINISTIC. No model, no network.
"""

import json
import math
from datetime import datetime, timezone
from decimal import Decimal


# -- All seven dimensions per AP-1 v1.3 --------------------------------

ALL_DIMENSIONS = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']

# Dimensions the runner auto-measures
AUTO_MEASURED = {'D1', 'D2', 'D7'}

# Dimensions requiring human adjudication
HUMAN_ADJUDICATED = {'D3', 'D4', 'D5', 'D6'}


def generate_report(*, summary, config, seal_record, transcript_records=None):
    """Generate the evaluation report.

    Args:
        summary: dict -- the run summary (from the scorer)
        config: dict -- resolved configuration
        seal_record: dict -- pre-registration record from seal
        transcript_records: list of transcript dicts (optional, for
            cell-level detail)

    Returns:
        str -- complete markdown report.
    """
    sections = []

    # Header
    sections.append('# AP-1 Evaluation Report\n')
    sections.append(f'Generated: {datetime.now(timezone.utc).isoformat()}\n')
    sections.append(f'AP-1 Version: {config.get("ap1_version", "unknown")}\n')
    sections.append(f'Version DOI: {config.get("ap1_version_doi", "unknown")}\n')
    sections.append(f'Model: {config.get("model", "unknown")}\n')
    sections.append('---\n')

    # 1. Pre-registration record
    sections.append(_section_preregistration(seal_record, config))

    # 2. Resolved configuration
    sections.append(_section_configuration(config))

    # 3. Per-dimension results with n
    sections.append(_section_dimension_results(summary, config))

    # 4. D7 figures with evidence class
    sections.append(_section_d7_figures(summary))

    # 5. Zero-failure Clopper-Pearson bounds
    sections.append(_section_clopper_pearson(summary))

    # 6. D7.2(a) originated-operand listing
    sections.append(_section_d72a_audit(summary))

    # 7. D7.2(b) operation-correctness counts
    sections.append(_section_d72b_counts(summary))

    # 7b. D7.2(a) operand provenance step counts
    sections.append(_section_operand_provenance(summary))

    # 8. Auto-scored vs adjudicated proportions
    sections.append(_section_scoring_proportions(summary))

    # 9. D2 mechanism classes per surface
    sections.append(_section_d2_mechanisms(summary))

    # 10. UNMEASURED / UNOBSERVABLE / UNMEASURABLE / VOID cells
    sections.append(_section_unmeasured_cells(summary, transcript_records))

    # 11. Quantisation and near-miss findings
    sections.append(_section_quantisation(summary))

    # 12. Declaration of unmeasured dimensions
    sections.append(_section_unmeasured_dimensions(config))

    # Declared limitations
    sections.append(_section_declared_limitations())

    return '\n'.join(sections)


# -- Section generators ------------------------------------------------

def _section_preregistration(seal_record, config):
    """Section 1: Pre-registration record."""
    lines = ['## 1. Pre-Registration Record\n']
    if seal_record:
        lines.append('| Field | Value |')
        lines.append('|---|---|')
        for k, v in sorted(seal_record.items()):
            lines.append(f'| `{k}` | `{v}` |')
    else:
        lines.append('*No seal record available.*')
    lines.append('')
    return '\n'.join(lines)


def _section_configuration(config):
    """Section 2: Resolved configuration verbatim."""
    lines = ['## 2. Resolved Configuration\n']
    # Serialise with Decimal handling
    safe = _make_json_safe(config)
    lines.append('```json')
    lines.append(json.dumps(safe, indent=2, ensure_ascii=False, sort_keys=True))
    lines.append('```\n')
    return '\n'.join(lines)


def _section_dimension_results(summary, config):
    """Section 3: Per-dimension results with n."""
    lines = ['## 3. Per-Dimension Results\n']
    dims_claimed = config.get('dimensions_claimed', [])

    lines.append('| Dimension | Status | n | Result |')
    lines.append('|---|---|---|---|')

    for dim in ALL_DIMENSIONS:
        if dim in dims_claimed:
            dim_data = summary.get(f'{dim.lower()}_results', {})
            if dim_data:
                n = dim_data.get('n', dim_data.get('auto_scored_n', 'N/A'))
                result = _format_dim_result(dim, dim_data)
                lines.append(f'| {dim} | Measured | {n} | {result} |')
            else:
                lines.append(f'| {dim} | Claimed but no results | — | — |')
        else:
            lines.append(f'| {dim} | **NOT MEASURED** | — | — |')

    lines.append('')
    return '\n'.join(lines)


def _section_d7_figures(summary):
    """Section 4: Every D7 figure with its evidence class.

    Figures resting on different evidence classes are not comparable
    (AP-1 v1.3 section 6.4).
    """
    lines = ['## 4. D7 Figures by Evidence Class\n']
    lines.append('> Figures resting on different evidence classes are not '
                 'comparable (AP-1 v1.3 §6.4).\n')

    ev_counts = summary.get('evidence_class_counts', {})
    if ev_counts:
        lines.append('| Evidence Class | Count |')
        lines.append('|---|---|')
        for ec, count in sorted(ev_counts.items()):
            lines.append(f'| `{ec}` | {count} |')
    else:
        lines.append('*No evidence class data available.*')

    # Per-item evidence detail
    item_evidence = summary.get('item_evidence', [])
    if item_evidence:
        lines.append('\n### Per-Item Evidence Detail\n')
        lines.append('| Item | Condition | Evidence Class | Outcome |')
        lines.append('|---|---|---|---|')
        for ie in item_evidence:
            lines.append(
                f'| {ie.get("item_id", "?")} '
                f'| {ie.get("condition", "?")} '
                f'| `{ie.get("evidence_class", "?")}` '
                f'| {ie.get("invocation_outcome", "?")} |')

    lines.append('')
    return '\n'.join(lines)


def _section_clopper_pearson(summary):
    """Section 5: Zero-failure Clopper-Pearson bounds.

    k=0 only: p_upper = 1 - 0.05^(1/n).
    k>0: point estimate, no bound, with declared limitation.
    """
    lines = ['## 5. Invocation Figures with Confidence Bounds\n']
    lines.append('> AP-1 v1.3 D7.5: any invocation figure, including 100%, '
                 'shall be reported with the exact one-sided 95% upper '
                 'confidence bound.\n')

    inv_figures = summary.get('invocation_figures', {})
    if not inv_figures:
        lines.append('*No invocation figures available.*\n')
        return '\n'.join(lines)

    lines.append('| Metric | k (failures) | n | Rate | 95% Upper Bound |')
    lines.append('|---|---|---|---|---|')

    for metric, data in sorted(inv_figures.items()):
        k = data.get('failures', 0)
        n = data.get('n', 0)
        rate = data.get('rate')

        if n == 0:
            lines.append(f'| {metric} | {k} | {n} | — | — |')
            continue

        rate_str = f'{rate}' if rate is not None else '—'

        if k == 0:
            # Exact closed-form Clopper-Pearson: p_upper = 1 - alpha^(1/n)
            alpha = 0.05
            p_upper = 1.0 - alpha ** (1.0 / n)
            lines.append(
                f'| {metric} | 0 | {n} | {n}/{n} | '
                f'{p_upper:.6f} ({p_upper*100:.4f}%) |')
        else:
            # k > 0: report point estimate only
            point = k / n if n > 0 else 0
            lines.append(
                f'| {metric} | {k} | {n} | {rate_str} | '
                f'*not computed (see §Declared Limitations)* |')

    lines.append('')
    return '\n'.join(lines)


def _section_d72a_audit(summary):
    """Section 6: D7.2(a) originated-operand listing."""
    lines = ['## 6. D7.2(a) Originated-Operand Audit\n']

    audit = summary.get('originated_operand_audit', [])
    if not audit:
        lines.append('*No originated operands detected.*\n')
        return '\n'.join(lines)

    lines.append('| Item | Condition | Operation | Originated Operand | '
                 'Expression | Resolution |')
    lines.append('|---|---|---|---|---|---|')
    for entry in audit:
        lines.append(
            f'| {entry.get("item_id", "?")} '
            f'| {entry.get("condition", "?")} '
            f'| {entry.get("operation", "?")} '
            f'| `{entry.get("originated_operand", "?")}` '
            f'| `{entry.get("expression", "?")}` '
            f'| {entry.get("resolution", "?")} |')

    lines.append('')
    return '\n'.join(lines)


def _section_d72b_counts(summary):
    """Section 7: D7.2(b) operation-correctness counts."""
    lines = ['## 7. D7.2(b) Operation Correctness\n']

    op_counts = summary.get('operation_correctness_counts', {})
    if not op_counts:
        lines.append('*No operation correctness data available.*\n')
        return '\n'.join(lines)

    total = sum(op_counts.values())
    lines.append(f'Total operations evaluated: {total}\n')
    lines.append('| Outcome | Count |')
    lines.append('|---|---|')
    for outcome in ['OPERATION-CORRECT', 'WRONG-OPERATION',
                    'OPERATION-UNOBSERVABLE']:
        count = op_counts.get(outcome, 0)
        lines.append(f'| {outcome} | {count} |')

    # WRONG-OPERATION split by item-level correctness
    wo_split = summary.get('wrong_operation_split', {})
    wo_total = sum(wo_split.values())
    if wo_total > 0:
        lines.append('')
        lines.append('### WRONG-OPERATION by Item Outcome\n')
        lines.append('| Population | Count |')
        lines.append('|---|---|')
        rd = wo_split.get('route_divergence', 0)
        iw = wo_split.get('item_wrong', 0)
        ud = wo_split.get('undetermined', 0)
        lines.append(f'| Route divergence (item answer correct) | {rd} |')
        lines.append(f'| Item answer incorrect | {iw} |')
        lines.append(f'| Item answer undetermined (adjudicated) | {ud} |')

    lines.append('')
    return '\n'.join(lines)


def _section_scoring_proportions(summary):
    """Section 8: Proportion auto-scored vs adjudicated, per dimension."""
    lines = ['## 8. Scoring Proportions\n']

    d1 = summary.get('d1_results', {})
    if d1:
        auto = d1.get('auto_scored_n', 0)
        adj = d1.get('adjudicated_n', 0)
        total = auto + adj
        lines.append('### D1 Accuracy\n')
        lines.append(f'- Auto-scored: {auto}')
        lines.append(f'- Adjudicated: {adj}')
        lines.append(f'- Total: {total}')
        if total > 0:
            lines.append(f'- Auto-scored proportion: '
                         f'{auto}/{total} = {auto/total:.2%}')
        rate = d1.get('accuracy_rate')
        if rate is not None:
            lines.append(f'- Accuracy rate: {rate} '
                         f'(computed from {auto} auto-scored items only; '
                         f'{adj} adjudicated items are not represented '
                         f'in this rate)')
        lines.append('')

    d7 = summary.get('d7_results', {})
    if d7:
        lines.append('### D7 Provenance\n')
        auto = d7.get('auto_scored_n', 0)
        adj = d7.get('adjudicated_n', 0)
        total = auto + adj
        lines.append(f'- Auto-scored: {auto}')
        lines.append(f'- Adjudicated: {adj}')
        lines.append(f'- Total: {total}')
        if total > 0:
            lines.append(f'- Auto-scored proportion: '
                         f'{auto}/{total} = {auto/total:.2%}')
        lines.append('')

    if not d1 and not d7:
        lines.append('*No scoring proportion data available.*\n')

    return '\n'.join(lines)


def _section_d2_mechanisms(summary):
    """Section 9: D2 mechanism classes per surface.

    D2 is auto-measured. Per surface, report:
      - the mechanism class
      - whether determined from evidence or operator-declared
      - parameter-echo verification result, or UNVERIFIED
    """
    lines = ['## 9. D2 Reproducibility Mechanism Classes\n']
    # D2.2 cap display
    d2_cap = summary.get('d2_cap_reason')
    if d2_cap:
        lines.append(f'> **{d2_cap}**\n')
        lines.append('> *The platform-rejection detail above is the verbatim '
                     'error recorded during config setup. The rejection is '
                     'model-independent: it applies to any model run under '
                     'this config.*\n')

    lines.append('> D2 is auto-measured. STRUCTURAL and CONFIGURED are '
                 'operator-declared; OBSERVED-ONLY and UNMEASURED are '
                 'determined from evidence.\n')

    d2 = summary.get('d2_results', {})
    if not d2:
        lines.append('*No D2 results available.*\n')
        return '\n'.join(lines)

    surfaces = d2.get('surfaces', {})
    if surfaces:
        lines.append('| Surface | Mechanism Class | Basis | Distinct Values | '
                     'Runs | Parameter Echo |')
        lines.append('|---|---|---|---|---|---|')

        for surface_name, data in sorted(surfaces.items()):
            mechanism = data.get('mechanism', 'unknown')
            is_op_decl = data.get('operator_declared', False)
            basis = 'operator-declared' if is_op_decl else 'evidence'
            distinct = data.get('distinct_values', '—')
            runs = data.get('successful_runs', '—')
            echo = data.get('parameter_echo_status', 'UNVERIFIED')
            lines.append(
                f'| {surface_name} | `{mechanism}` | {basis} | '
                f'{distinct} | {runs} | `{echo}` |')
    else:
        lines.append('*No per-surface D2 data available.*\n')

    lines.append('')
    return '\n'.join(lines)


def _section_unmeasured_cells(summary, transcript_records):
    """Section 10: Every UNMEASURED/UNOBSERVABLE/UNMEASURABLE/VOID cell."""
    lines = ['## 10. Non-Outcome Cells\n']
    lines.append('> Every cell that is not a scoreable outcome is listed '
                 'with its reason.\n')

    cells = summary.get('non_outcome_cells', [])

    # Also extract from transcript if available
    if transcript_records:
        for rec in transcript_records:
            error = rec.get('error_state')
            if error:
                cells.append({
                    'item_id': rec.get('item_id', '?'),
                    'condition': rec.get('condition', '?'),
                    'status': error.split(':')[0] if ':' in str(error)
                              else str(error),
                    'reason': str(error),
                })
            ev = rec.get('evidence_class', '')
            if ev and 'UNOBSERVABLE' in str(ev):
                cells.append({
                    'item_id': rec.get('item_id', '?'),
                    'condition': rec.get('condition', '?'),
                    'status': 'UNOBSERVABLE',
                    'reason': f'Evidence class: {ev}',
                })

    if cells:
        lines.append('| Item | Condition | Status | Reason |')
        lines.append('|---|---|---|---|')
        seen = set()
        for cell in cells:
            key = (cell.get('item_id'), cell.get('condition'),
                   cell.get('status'))
            if key in seen:
                continue
            seen.add(key)
            lines.append(
                f'| {cell.get("item_id", "?")} '
                f'| {cell.get("condition", "?")} '
                f'| {cell.get("status", "?")} '
                f'| {cell.get("reason", "?")} |')
    else:
        lines.append('*No non-outcome cells.*\n')

    lines.append('')
    return '\n'.join(lines)


def _section_quantisation(summary):
    """Section 11: Quantisation and near-miss findings."""
    lines = ['## 11. Quantisation and Near-Miss Findings\n']

    quant = summary.get('quantisation_findings', [])
    if quant:
        lines.append('| Item | Operand | Finding |')
        lines.append('|---|---|---|')
        for qf in quant:
            lines.append(
                f'| {qf.get("item_id", "?")} '
                f'| `{qf.get("operand", "?")}` '
                f'| {qf.get("finding", "?")} |')
    else:
        lines.append('*No quantisation findings.*')

    near_miss = summary.get('near_miss_findings', [])
    if near_miss:
        lines.append('\n### Near-Miss Findings\n')
        for nm in near_miss:
            lines.append(f'- {nm}')

    lines.append('')
    return '\n'.join(lines)


def _section_unmeasured_dimensions(config):
    """Section 12: Declaration of which dimensions were NOT measured.

    A dimension not measured is declared, never omitted.
    """
    lines = ['## 12. Unmeasured Dimensions Declaration\n']
    lines.append('> A dimension not measured is declared, never omitted.\n')

    dims_claimed = set(config.get('dimensions_claimed', []))

    unmeasured = []
    for dim in ALL_DIMENSIONS:
        if dim not in dims_claimed:
            unmeasured.append(dim)

    if unmeasured:
        lines.append('The following dimensions were **not measured** in this '
                     'evaluation and require human adjudication:\n')
        for dim in unmeasured:
            reason = _unmeasured_reason(dim)
            lines.append(f'- **{dim}**: {reason}')
    else:
        lines.append('All seven dimensions were claimed for measurement.')

    lines.append('')
    return '\n'.join(lines)


def _section_declared_limitations():
    """Declared limitations section."""
    lines = ['## 13. Declared Limitations\n']

    lines.append('### Clopper-Pearson Bound (k > 0)\n')
    lines.append('An exact confidence bound for non-zero failure counts is '
                 'not computed; AP-1 v1.3 D7.5 specifies the zero-failure '
                 'form only. This is an author-identified defect in the '
                 'standard, noted for resolution in the adopted version.\n')
    lines.append('For non-zero failure counts, the point estimate is '
                 'reported with n. The full Beta quantile would require '
                 'an external dependency or a specification extension.\n')

    return '\n'.join(lines)



def _section_operand_provenance(summary):
    """Section 7b: D7.2(a) operand provenance step counts."""
    lines = ['## 7b. D7.2(a) Operand Provenance Step Counts\n']
    lines.append('> Each operand in each tool-call expression is resolved '
                 'through the five-step hierarchy (AP-1 v1.3 D7.2(a)).\n')

    step_counts = summary.get('operand_step_counts', {})
    prov_outcomes = summary.get('provenance_outcomes', {})

    if not step_counts and not prov_outcomes:
        lines.append('*No operand provenance data available.*\n')
        return '\n'.join(lines)

    step_names = {
        2: 'Transformed source',
        3: 'Reference intermediate',
        4: 'Computed in session',
    }

    total_operands = sum(step_counts.values())
    lines.append(f'Total operands resolved: {total_operands}\n')

    s1_src = summary.get('step_1_source', step_counts.get(1, 0))
    s1_const = summary.get('step_1_constant', 0)

    lines.append('| Step | Resolution | Count | % |')
    lines.append('|---|---|---|---|')
    # Step 1 broken out: source match and declared constant
    if total_operands > 0:
        pct_src = f'{100*s1_src/total_operands:.1f}'
        pct_const = f'{100*s1_const/total_operands:.1f}'
    else:
        pct_src = pct_const = '—'
    lines.append(f'| 1 | Source match | {s1_src} | {pct_src}% |')
    lines.append(f'| 1 | Declared constant | {s1_const} | {pct_const}% |')
    for step in range(2, 5):
        count = step_counts.get(step, 0)
        pct = f'{100*count/total_operands:.1f}' if total_operands > 0 else '—'
        lines.append(f'| {step} | {step_names[step]} | {count} | {pct}% |')
    # Step 5 split: sign-inverted, ungrounded-chain, untraceable
    s5_si = summary.get('step_5_sign_inverted', 0)
    s5_uc = summary.get('step_5_ungrounded_chain', 0)
    s5_ut = summary.get('step_5_untraceable', 0)
    if total_operands > 0:
        pct_si = f'{100*s5_si/total_operands:.1f}'
        pct_uc = f'{100*s5_uc/total_operands:.1f}'
        pct_ut = f'{100*s5_ut/total_operands:.1f}'
    else:
        pct_si = pct_uc = pct_ut = '—'
    lines.append(f'| 5 | Originated, sign-inverted from source | {s5_si} | {pct_si}% |')
    lines.append(f'| 5 | Originated, computed from ungrounded invocation | {s5_uc} | {pct_uc}% |')
    lines.append(f'| 5 | Originated, no traceable basis | {s5_ut} | {pct_ut}% |')

    lines.append('')

    # Invocation-level outcomes
    total_inv = sum(prov_outcomes.values())
    if total_inv > 0:
        lines.append('### Per-Invocation Outcomes\n')
        lines.append('| Outcome | Count |')
        lines.append('|---|---|')
        for outcome in ['OPERANDS-GROUNDED', 'OPERAND-ORIGINATED']:
            count = prov_outcomes.get(outcome, 0)
            lines.append(f'| {outcome} | {count} |')
        lines.append('')

    # Originated operand audit
    audit = summary.get('originated_operand_audit', [])
    if audit:
        lines.append('### Originated Operand Audit\n')
        lines.append('| Item | Condition | Value | Expression | Resolution |')
        lines.append('|---|---|---|---|---|')
        for entry in audit:
            lines.append(
                f'| {entry.get("item_id", "?")} '
                f'| {entry.get("condition", "?")} '
                f'| `{entry.get("value", "?")}` '
                f'| `{entry.get("expression", "?")}` '
                f'| {entry.get("resolution", "?")} |')
        lines.append('')

    return '\n'.join(lines)


# -- Helpers -----------------------------------------------------------

def clopper_pearson_upper_k0(n, alpha=0.05):
    """Exact one-sided 95% Clopper-Pearson upper bound for k=0 failures.

    Formula: p_upper = 1 - alpha^(1/n)
    Source: AP-1 v1.3 D7.5.

    Args:
        n: int -- total number of trials
        alpha: float -- significance level (default 0.05 for 95%)

    Returns:
        float -- upper bound on failure probability
    """
    if n <= 0:
        return float('nan')
    return 1.0 - alpha ** (1.0 / n)


def _format_dim_result(dim, data):
    """Format a dimension result for the table."""
    if dim == 'D1':
        rate = data.get('accuracy_rate')
        auto = data.get('auto_scored_n', 0)
        adj = data.get('adjudicated_n', 0)
        if rate is not None:
            return (f'Accuracy: {rate} '
                    f'(auto-scored {auto}; {adj} adjudicated not in rate)')
        return 'No rate computed'
    elif dim == 'D2':
        return 'See §9 D2 Mechanism Classes'
    elif dim == 'D7':
        return 'See §4-7 D7 Figures'
    return str(data)


def _unmeasured_reason(dim):
    """Return the reason a dimension is not measured."""
    reasons = {
        'D1': 'Accuracy — requires item-level scoring',
        'D2': 'Reproducibility — requires repeated runs',
        'D3': 'Completeness of explanation — requires human adjudication',
        'D4': 'Appropriate caveats — requires human adjudication',
        'D5': 'Source attribution — requires human adjudication',
        'D6': 'Confidence calibration — requires human adjudication',
        'D7': 'Provenance — requires tool-call observation',
    }
    return reasons.get(dim, 'Reason not specified')


def _make_json_safe(obj):
    """Convert Decimal and other non-JSON types to strings."""
    if isinstance(obj, Decimal):
        return str(obj)
    if isinstance(obj, dict):
        return {k: _make_json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_make_json_safe(v) for v in obj]
    return obj
