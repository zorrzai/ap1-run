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
  5a. What was held constant between the conditions, and DPR (D7.8)
  6.  D7.2(a) originated-operand listing
  7.  D7.2(b) operation-correctness counts
  8.  Proportion auto-scored vs adjudicated, per dimension
  9.  D2 mechanism classes per surface
  10. Every UNMEASURED, UNOBSERVABLE, UNMEASURABLE and VOID cell with reason
  11. Quantisation and near-miss findings
  12. DECLARATION of which dimensions were NOT measured

Clopper-Pearson (AP-1 v1.3 D7.5; scoring/invocation.py):
  k=0 (closed form): p_upper = 1 - alpha^(1/n), alpha = 0.05.
  k>0: the exact bound, the 1 - alpha quantile of Beta(k+1, n-k), the
  general form DISPOSITION C-1 adopts. Computed in Decimal and shown
  rounded up, so a displayed bound is never below the exact one.

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
from decimal import ROUND_DOWN, Decimal

from ap1_run.scoring.invocation import (
    _exact_upper_bound, clopper_pearson_upper, round_up,
)


# -- All seven dimensions per AP-1 v1.3 --------------------------------

ALL_DIMENSIONS = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']

# Dimensions the runner auto-measures
AUTO_MEASURED = {'D1', 'D2', 'D7'}

# Dimensions requiring human adjudication
HUMAN_ADJUDICATED = {'D3', 'D4', 'D5', 'D6'}


# The README's statement (T3-45): report.md is the artifact most likely
# to be forwarded, so it says what a run is before its first section.
DEMONSTRATION_STATEMENT = (
    '> **Demonstration run, not a conformance result.** ap1-run implements '
    'the AP-1 v1.3 Draft for Comment; v1.2 remains the version in force. '
    'A run of this instrument is a demonstration run, not a conformance '
    'result under either version (README, "Which version of AP-1").\n')


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
    sections.append(DEMONSTRATION_STATEMENT)
    sections.append('---\n')

    # 1. Pre-registration record
    sections.append(_section_preregistration(seal_record))

    # 2. Resolved configuration
    sections.append(_section_configuration(config))

    # 3. Per-dimension results with n
    sections.append(_section_dimension_results(summary, config))

    # 4. D7 figures with evidence class
    sections.append(_section_d7_figures(summary))

    # 4b. D7.3 Transcription fidelity (E7 fix)
    sections.append(_section_d73(summary))

    # 5. Zero-failure Clopper-Pearson bounds
    sections.append(_section_clopper_pearson(summary))

    # 5a. D7.8 instruction-removal contrast: held constant, DPR
    sections.append(_section_condition_contrast(summary))

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
    sections.append(_section_unmeasured_dimensions(config, summary))

    # Declared limitations
    sections.append(_section_declared_limitations())

    return '\n'.join(sections)


# -- Section generators ------------------------------------------------

def _section_preregistration(seal_record):
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
            if dim_data and dim == 'D7':
                lines.extend(_d7_rows(summary, dim_data))
            elif dim_data and dim == 'D2':
                questions = {key.split('/')[0] for key in dim_data}
                lines.append(f'| D2 | Measured | {len(questions)} | '
                             f'{_d2_class_counts(dim_data)} (§9) |')
            elif dim_data:
                n = dim_data.get('n', dim_data.get('auto_scored_n', 'N/A'))
                result = _format_dim_result(dim, dim_data)
                lines.append(f'| {dim} | Measured | {n} | {result} |')
            else:
                lines.append(f'| {dim} | Claimed but no results | — | — |')
        else:
            lines.append(f'| {dim} | **NOT MEASURED** | — | — |')

    lines.append('')
    return '\n'.join(lines)


def _d7_rows(summary, d7):
    """§3 rows for a claimed D7: one per sub-dimension (AP-1 v1.3 D7
    "Report all four"; T3-29). D7.4 is never measured; D7.3 is partly
    unobservable when any execution has no single released figure."""
    tr = summary.get('transcription_results', [])
    unobservable = sum(1 for r in tr if r.get('outcome') == 'UNOBSERVABLE')
    d73_status = (f'Partly measured ({unobservable} of {len(tr)} '
                  f'UNOBSERVABLE)' if unobservable else 'Measured')
    return [
        f'| D7 | Partly measured | {d7.get("n", "N/A")} | D7.1-D7.3 '
        f'measured, D7.4 not measured (§12) |',
        '| D7.1 | Measured | see §5 | Invocation rate per condition: §5 |',
        '| D7.2 | Measured | see §6-7b | Operand provenance §6, §7b; '
        'operation correctness §7 |',
        f'| D7.3 | {d73_status} | {len(tr)} | Transcription fidelity: '
        f'D7.3 section |',
        '| D7.4 | **NOT MEASURED** | — | Invocation under pressure (§12) |',
    ]


def _evidence_line(summary, figure):
    """The evidence classes a D7 figure rests on (AP-1 v1.3 D7.7: every
    D7 figure with its evidence class; SPEC R3.3), or None. Uses the
    figure's own executions where the summary has them
    (d7_evidence[figure]), otherwise the run's evidence class counts."""
    classes = (summary.get('d7_evidence', {}).get(figure)
               or summary.get('evidence_class_counts'))
    if not classes:
        return None
    listed = ', '.join(f'`{ec}` ({c})' for ec, c in sorted(classes.items()))
    line = f'Evidence class (AP-1 D7.7), executions: {listed}.'
    if len(classes) > 1:
        line += ' Figures resting on different classes are not comparable.'
    return line + '\n'


def _section_d7_figures(summary):
    """Section 4: Every D7 figure with its evidence class.

    Figures resting on different evidence classes are not comparable
    (AP-1 v1.3 D7.7).
    """
    lines = ['## 4. D7 Figures by Evidence Class\n']
    lines.append('> Figures resting on different evidence classes are not '
                 'comparable (AP-1 v1.3 D7.7).\n')

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



def _section_d73(summary):
    """Section: D7.3 Transcription fidelity and Release coverage.

    Renders two labelled sub-sections:
    A. Transcription check  (check_transcription -- AUTO-MATCH items only),
       with the count of EXACT results rounded under the declared policy
    B. Release coverage     (check_release_coverage -- ALL items)
    """
    lines = ['## D7.3 Transcription Fidelity\n']
    evidence = _evidence_line(summary, 'D7.3')
    if evidence:
        lines.append(evidence)

    # -- A. Transcription Check --
    lines.append('### A. Transcription Check\n')
    lines.append('> Compares EVERY return of the required operation to the single ')
    lines.append('> figure R2.0 identified as released (AUTO-MATCH items only), ')
    lines.append('> under the declared quantisation policy (places and rounding mode).\n')

    tr_results = summary.get('transcription_results', [])
    if not tr_results:
        lines.append('*No transcription data available.*\n')
    else:
        from collections import Counter
        counts = Counter(r['outcome'] for r in tr_results)
        total = len(tr_results)

        lines.append('| Outcome | Count | % |')
        lines.append('|---|---|---|')
        for outcome in ['TRANSCRIBED-EXACT', 'TRANSCRIBED-ALTERED', 'UNOBSERVABLE']:
            c = counts.get(outcome, 0)
            pct = f'{100*c/total:.1f}' if total > 0 else '\u2014'
            lines.append(f'| `{outcome}` | {c} | {pct}% |')
        lines.append(f'| **Total** | **{total}** | |')

        rounded = sum(1 for r in tr_results
                      if r['outcome'] == 'TRANSCRIBED-EXACT'
                      and r.get('rounded_under_declared_policy'))
        lines.append(
            f'\nOf the {counts.get("TRANSCRIBED-EXACT", 0)} '
            f'`TRANSCRIBED-EXACT`, {rounded} were rounded under the declared '
            f'quantisation policy (licensed rounding, EXACT under AP-1 '
            f'v1.3; subtract them for a strict v1.2 "match" count).')

        altered = [r for r in tr_results if r['outcome'] == 'TRANSCRIBED-ALTERED']
        if altered:
            lines.append('\n#### Altered Transcriptions\n')
            lines.append('| Item | Condition | Rep | Difference | Reason |')
            lines.append('|---|---|---|---|---|')
            for r in altered[:20]:
                lines.append(
                    f'| {r.get("item_id", "?")} '
                    f'| {r.get("condition", "?")} '
                    f'| {r.get("repeat", "?")} '
                    f'| {r.get("difference", "?")} '
                    f'| {r.get("reason", "?")} |')
            if len(altered) > 20:
                lines.append(f'| ... | ... | ... | ... | ({len(altered)-20} more) |')
        lines.append('')

    # -- B. Release Coverage --
    lines.append('### B. Release Coverage\n')
    lines.append('> Compares EVERY candidate figure in the response against ')
    lines.append('> EVERY tool return value (ALL items including adjudicated).\n')

    rc_results = summary.get('release_coverage_results', [])
    if not rc_results:
        lines.append('*No release coverage data available.*\n')
    else:
        from collections import Counter
        rc_counts = Counter(r['outcome'] for r in rc_results)
        rc_total = len(rc_results)

        lines.append('| Outcome | Count | % |')
        lines.append('|---|---|---|')
        for outcome in ['GOVERNED-RELEASE', 'PARTIALLY-GOVERNED',
                        'COVERAGE-UNOBSERVABLE']:
            c = rc_counts.get(outcome, 0)
            pct = f'{100*c/rc_total:.1f}' if rc_total > 0 else '\u2014'
            lines.append(f'| `{outcome}` | {c} | {pct}% |')
        lines.append(f'| **Total** | **{rc_total}** | |')

        pg = [r for r in rc_results if r['outcome'] == 'PARTIALLY-GOVERNED']
        if pg:
            lines.append('\n#### Partially-Governed Findings\n')
            lines.append('| Item | Condition | Rep | Finding |')
            lines.append('|---|---|---|---|')
            for r in pg[:20]:
                lines.append(
                    f'| {r.get("item_id", "?")} '
                    f'| {r.get("condition", "?")} '
                    f'| {r.get("repeat", "?")} '
                    f'| {r.get("finding", "?")} |')
            if len(pg) > 20:
                lines.append(f'| ... | ... | ... | ({len(pg)-20} more) |')
        lines.append('')

    return '\n'.join(lines)

def _section_clopper_pearson(summary):
    """Section 5: D7.1 invocation figures with their bounds.

    n is the number of computable questions with an observed outcome
    (AP-1 v1.3 D7.1; a question fails if any repeat is NOT-INVOKED).
    Every figure has its exact one-sided 95% upper bound on the failure
    rate (k=0: 1 - 0.05^(1/n); k>0: Clopper-Pearson), rounded up. The
    rate is printed as a percentage with k/n
    and the bound, never "100%" alone (SPEC R2.3), and each condition
    gets the AP-1 \u00a76.2 headline. EV-0 (UNOBSERVABLE) executions are
    listed per evidence class and are in no n (SPEC R1.3.1, R2.3).
    """
    lines = ['## 5. Invocation Figures with Confidence Bounds\n']
    lines.append('> AP-1 v1.3 D7.5: any invocation figure, including 100%, '
                 'shall be reported with the exact one-sided 95% upper '
                 'confidence bound.\n')

    inv_figures = summary.get('invocation_figures', {})
    if not inv_figures:
        lines.append('*No invocation figures available.*\n')
        return '\n'.join(lines)

    lines.append('> D7.1 n counts the computable questions that have an '
                 'observed outcome, not the executions: the '
                 'repeats of a question are not independent trials. A '
                 'question counts as a failure if any of its repeats is '
                 'NOT-INVOKED. UNOBSERVABLE executions (EV-0) are neither '
                 'successes nor failures and are in no n (SPEC R2.3, '
                 'R1.3.1).\n')

    lines.append('| Metric | k (failures) | n | Rate | 95% Upper Bound '
                 '| Evidence Class |')
    lines.append('|---|---|---|---|---|---|')

    headlines = []
    for metric, data in sorted(inv_figures.items()):
        k = data.get('failures', 0)
        n = data.get('n', 0)
        ec = data.get('evidence_class')
        ec_str = f'`{ec}`' if ec else '\u2014'
        cond = data.get('condition', metric)

        if n == 0:
            lines.append(f'| {metric} | {k} | {n} | \u2014 | \u2014 '
                         f'| {ec_str} |')
            headlines.append(
                f'- Under {cond}: no computable question has an observed '
                f'invocation outcome; D7.1 is not measured.')
            continue

        pct = _percent(n - k, n)
        rate_str = f'{n - k}/{n} ({pct}%)'

        # Exact Clopper-Pearson bound in Decimal, rounded up (T3-61,
        # T3-81): k=0 is 1 - 0.05^(1/n), k>0 the Beta(k+1, n-k) quantile
        p_upper = clopper_pearson_upper(k, n)
        bound_pct = round_up(p_upper * 100, Decimal('0.0001'))
        bound_str = (f'{round_up(p_upper, Decimal("0.000001"))} '
                     f'({bound_pct}%)')
        bound_text = (f'one-sided 95% upper bound on the failure rate '
                      f'{bound_pct}%')
        lines.append(f'| {metric} | {k} | {n} | {rate_str} | {bound_str} '
                     f'| {ec_str} |')
        headlines.append(
            f'- Deterministic computation was invoked on {pct}% of '
            f'computable questions ({n - k}/{n}; {k} not invoked; '
            f'{bound_text}), under {cond}'
            + (f', on evidence class {ec}' if ec else '') + '.')

    lines.append('')
    lines.append('**Headline (AP-1 \u00a76.2):**\n')
    lines.extend(headlines)
    lines.append('')

    evidence = summary.get('invocation_evidence', {})
    if evidence:
        lines.append('**Executions by evidence class:**\n')
        lines.append('| Condition | Evidence Class | Executions | Questions '
                     '| Questions in n | Unobservable Executions |')
        lines.append('|---|---|---|---|---|---|')
        warnings = []
        for cond, data in evidence.items():
            for ec, c in data['classes'].items():
                lines.append(
                    f'| {cond} | `{ec}` | {c["executions"]} '
                    f'| {c["questions"]} | {c["observed_questions"]} '
                    f'| {c["unobservable_executions"]} |')
            if data.get('cross_class_warning'):
                warnings.append(f'> {cond}: {data["cross_class_warning"]}; '
                                f'only observed outcomes are in n.')
        lines.append('')
        for w in warnings:
            lines.append(w)
            lines.append('')

    return '\n'.join(lines)


def _percent(part, whole):
    """part/whole as a percentage string with one decimal, rounded down
    so that an invocation rate below 100% never prints as 100.0%."""
    return str((Decimal(part) / Decimal(whole) * 100).quantize(
        Decimal('0.1'), rounding=ROUND_DOWN))

def _section_condition_contrast(summary):
    """Section 5a: what was held constant between the conditions, and
    the drop-in-performance ratio (AP-1 D7.8; SPEC R1.2, R2.3)."""
    lines = ['### 5a. Instruction-Removal Contrast (D7.8)\n']
    held = summary.get('held_constant')
    if held:
        lines.append(f'Held constant between base and instruction_removed '
                     f'(compared before execution, R1.2): '
                     f'{", ".join(held)}. Varied: the system prompt only.\n')
    else:
        lines.append('Held constant between base and instruction_removed: '
                     'not recorded.\n')
    lines.append(f'DPR (drop-in-performance ratio, '
                 f'(I_base - I_removed) / I_base): '
                 f'{summary.get("dpr", "not computed")}\n')
    return '\n'.join(lines)


def _section_d72a_audit(summary):
    """Section 6: D7.2(a) originated-operand listing."""
    lines = ['## 6. D7.2(a) Originated-Operand Audit\n']

    audit = summary.get('originated_operand_audit', [])
    if not audit:
        lines.append('*No originated operands detected.*\n')
        return '\n'.join(lines)

    # The entries are build_summary's (T3-64): the operand is its literal
    # as written in the call (else its value); a missing field reads '—'
    lines.append('| Item | Condition | Repeat | Originated Operand | '
                 'Expression | Resolution |')
    lines.append('|---|---|---|---|---|---|')
    for entry in audit:
        operand = entry.get('literal') or entry.get('value') or '—'
        lines.append(
            f'| {entry.get("item_id") or "—"} '
            f'| {entry.get("condition") or "—"} '
            f'| {entry.get("repeat") or "—"} '
            f'| `{operand}` '
            f'| `{entry.get("expression") or "—"}` '
            f'| {entry.get("resolution") or "—"} |')

    lines.append('')
    return '\n'.join(lines)


def _section_d72b_counts(summary):
    """Section 7: D7.2(b) operation-correctness counts."""
    lines = ['## 7. D7.2(b) Operation Correctness\n']

    op_counts = summary.get('operation_correctness_counts', {})
    if not op_counts:
        lines.append('*No operation correctness data available.*\n')
        return '\n'.join(lines)

    evidence = _evidence_line(summary, 'D7.2(b)')
    if evidence:
        lines.append(evidence)
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
        lines.append(f'| No figure released (no item answer) | '
                     f'{wo_split.get("no_figure", 0)} |')

    lines.append('')
    return '\n'.join(lines)


def _section_scoring_proportions(summary):
    """Section 8: Proportion auto-scored vs adjudicated, per dimension."""
    lines = ['## 8. Scoring Proportions\n']

    d1 = summary.get('d1_results', {})
    if d1:
        auto = d1.get('auto_scored_n', 0)
        adj = d1.get('adjudicated_n', 0)
        unmeasurable = d1.get('unmeasurable_n', 0)
        # One D1 n (T3-66): every scored execution is auto-scored,
        # adjudicated or UNMEASURABLE (adjudicated with a reason)
        total = auto + adj + unmeasurable
        lines.append('### D1 Accuracy\n')
        lines.append(f'- Auto-scored: {auto}')
        lines.append(f'- Adjudicated: {adj}')
        lines.append(f'- Unmeasurable: {unmeasurable} (response unreadable, '
                     f'routed to adjudication)')
        lines.append(f'- Total: {total}')
        if total > 0:
            lines.append(f'- Auto-scored proportion: '
                         f'{auto}/{total} = {auto/total:.2%}')
        rate = d1.get('accuracy_rate')
        pending = adj + unmeasurable
        if rate is not None and pending:
            lines.append(f'- Accuracy rate: not computed: {pending} items '
                         f'await adjudication, and R2.0 routes every wrong '
                         f'figure there, so a rate over the {auto} '
                         f'auto-scored items alone would leave the wrong '
                         f'answers out (T3-3)')
        elif rate is not None:
            lines.append(f'- Accuracy rate: {rate} '
                         f'(computed from {auto} auto-scored items only; '
                         f'{adj} adjudicated items are not represented '
                         f'in this rate)')
        lines.append('')

    d7 = summary.get('d7_results', {})
    if d7:
        lines.append('### D7 Computation invocation\n')
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

    # The live shape (T3-4): {'<item>/<condition>': {surface: class}},
    # one class per surface per question and condition (SPEC R2.2)
    lines.append(f'Classes per surface, over question-conditions: '
                 f'{_d2_class_counts(d2)}.\n')
    lines.append('| Question | Condition | Surface | Mechanism Class | Basis '
                 '| Distinct Values | Runs | Parameter Echo |')
    lines.append('|---|---|---|---|---|---|---|---|')
    for key, surfaces in sorted(d2.items()):
        item, _, condition = key.partition('/')
        for surface_name, data in sorted(surfaces.items()):
            basis = ('operator-declared' if data.get('operator_declared')
                     else 'evidence')
            lines.append(
                f'| {item} | {_cell(condition)} | {surface_name} '
                f'| `{data.get("mechanism", "unknown")}` | {basis} '
                f'| {_cell(data.get("distinct_values"))} '
                f'| {_cell(data.get("successful_runs"))} '
                f'| `{data.get("parameter_echo_status", "UNVERIFIED")}` |')

    lines.append('')
    return '\n'.join(lines)


def _d2_class_counts(d2):
    """'figures: OBSERVED-ONLY 9, UNMEASURED 1; prose: ...': how many
    question-conditions have each class, per surface."""
    counts = {}
    for surfaces in d2.values():
        for surface_name, data in surfaces.items():
            per = counts.setdefault(surface_name, {})
            mechanism = data.get('mechanism', 'unknown')
            per[mechanism] = per.get(mechanism, 0) + 1
    return '; '.join(
        f'{surface_name}: ' + ', '.join(
            f'{m} {c}' for m, c in sorted(per.items()))
        for surface_name, per in sorted(counts.items()))


def _section_unmeasured_cells(summary, transcript_records):
    """Section 10: every UNMEASURED, UNOBSERVABLE, UNMEASURABLE and VOID
    cell with its reason (SPEC R3.3; T3-35).

    A cell is one execution's result for one measurement. Execution-level
    cells (UNMEASURED and VOID from the summary, a transcript record's
    error state, else its EV-0 class) are one row per execution: a
    transport failure is one row, whatever records it left. Each
    measurement that has no outcome for an execution adds its own row:
    the R2.0 figure (UNMEASURABLE), D7.2(a) (OPERANDS-UNOBSERVABLE, or
    UNMEASURABLE for the execution), D7.2(b) (OPERATION-UNOBSERVABLE,
    per call), D7.3 transcription (UNOBSERVABLE) and D7.3 release
    coverage (COVERAGE-UNOBSERVABLE). Nothing is de-duplicated across
    repeats, and the summary is not changed.
    """
    lines = ['## 10. Non-Outcome Cells\n']
    lines.append('> Every cell that is not a scoreable outcome is listed '
                 'with its reason.\n')

    rows = []
    seen = set()

    def add(source, status, reason, measurement, execution=False):
        repeat = source.get('repeat')
        key = (source.get('item_id'), source.get('condition'), repeat)
        if execution and repeat is not None:
            if key in seen:
                return
            seen.add(key)
        rows.append((source.get('item_id'), source.get('condition'), status,
                     reason, repeat, measurement))

    for cell in summary.get('non_outcome_cells', []):
        add(cell, cell.get('status'), cell.get('reason'), 'execution',
            execution=True)
    records = [r for r in transcript_records or []
               if r.get('record_type') != 'figure_identification']
    for rec in records:
        error = rec.get('error_state')
        evidence = str(rec.get('evidence_class'))
        if error:
            text = str(error)
            add(rec, text.split(':')[0], text, 'execution', execution=True)
        elif 'UNOBSERVABLE' in evidence:
            add(rec, 'UNOBSERVABLE', f'Evidence class: {evidence}',
                'D7.1 invocation', execution=True)
    for rec in records:
        if rec.get('figure_outcome') == 'UNMEASURABLE':
            add(rec, 'UNMEASURABLE', 'response could not be read; routed '
                'to adjudication', 'R2.0 figure')
    for cell in summary.get('provenance_unmeasurable', []):
        add(cell, 'UNMEASURABLE', cell.get('reason'), 'D7.2(a) provenance')
    for cell in summary.get('operands_unobservable', []):
        add(cell, 'OPERANDS-UNOBSERVABLE', cell.get('reason'),
            'D7.2(a) provenance')
    for cell in summary.get('operation_unobservable', []):
        add(cell, 'OPERATION-UNOBSERVABLE', cell.get('reason'),
            'D7.2(b) operation')
    for r in summary.get('transcription_results', []):
        if r.get('outcome') == 'UNOBSERVABLE':
            reason = r.get('reason') or ''
            if reason.startswith('R2.0 outcome is'):
                # its figure outcome has its own row or sheet
                reason = 'no released figure to compare (not auto-matched)'
            add(r, 'UNOBSERVABLE', reason, 'D7.3 transcription')
    for r in summary.get('release_coverage_results', []):
        if r.get('outcome') == 'COVERAGE-UNOBSERVABLE':
            add(r, 'COVERAGE-UNOBSERVABLE', r.get('finding'),
                'D7.3 release coverage')

    if not rows:
        lines.append('*No non-outcome cells.*\n')
        lines.append('')
        return '\n'.join(lines)

    counts = {}
    for row in rows:
        counts[row[5]] = counts.get(row[5], 0) + 1
    lines.append(f'{len(rows)} cells: ' + '; '.join(
        f'{measurement} {count}' for measurement, count in counts.items())
        + '.\n')
    lines.append('| Item | Condition | Status | Reason | Repeat | '
                 'Measurement |')
    lines.append('|---|---|---|---|---|---|')
    for row in rows:
        lines.append('| ' + ' | '.join(_cell(v) for v in row) + ' |')
    lines.append('')
    return '\n'.join(lines)


def _cell(value):
    """A value as a markdown table cell: '—' if missing, on one line,
    with any '|' escaped."""
    if value is None or value == '':
        return '—'
    return ' '.join(str(value).split()).replace('|', '\\|')


def _section_quantisation(summary):
    """Section 11: Quantisation and near-miss findings (D7.2(a)(iii);
    SPEC R2.4, R3.3; T3-34).

    A quantisation finding is an operand grounded on a reference
    intermediate only after the declared quantisation. A near miss is an
    operand equal to an earlier call's return only after quantisation:
    it stays ORIGINATED, with the finding recorded.
    """
    lines = ['## 11. Quantisation and Near-Miss Findings\n']

    quant = summary.get('quantisation_findings', [])
    if quant:
        lines.append('| Item | Condition | Repeat | Operand | Finding |')
        lines.append('|---|---|---|---|---|')
        for qf in quant:
            lines.append(
                f'| {_cell(qf.get("item_id"))} '
                f'| {_cell(qf.get("condition"))} '
                f'| {_cell(qf.get("repeat"))} '
                f'| `{_cell(qf.get("operand"))}` '
                f'| {_cell(qf.get("finding"))} |')
    else:
        lines.append('*No quantisation findings.*')

    near_miss = summary.get('near_miss_findings', [])
    if near_miss:
        lines.append('\n### Near-Miss Findings\n')
        lines.append('> Operand equal to an earlier return only after '
                     'quantisation: ORIGINATED, with this finding.\n')
        lines.append('| Item | Condition | Repeat | Operand | Prior Return '
                     '| Quantised To | Prior Call Grounded |')
        lines.append('|---|---|---|---|---|---|---|')
        for nm in near_miss:
            lines.append(
                f'| {_cell(nm.get("item_id"))} '
                f'| {_cell(nm.get("condition"))} '
                f'| {_cell(nm.get("repeat"))} '
                f'| `{_cell(nm.get("operand"))}` '
                f'| `{_cell(nm.get("prior_return"))}` '
                f'| `{_cell(nm.get("quantised_to"))}` '
                f'| {_cell(nm.get("grounded"))} |')

    lines.append('')
    return '\n'.join(lines)


def _section_unmeasured_dimensions(config, summary=None):
    """Section 12: Declaration of which dimensions were NOT measured.

    A dimension not measured is declared, never omitted. With D7
    claimed, the parts of D7 not measured are declared too: D7.4 always,
    and D7.3 where some executions are UNOBSERVABLE (T3-29).
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
                     'evaluation:\n')
        for dim in unmeasured:
            reason = _unmeasured_reason(dim)
            lines.append(f'- **{dim}**: {reason}')
    else:
        lines.append('All seven dimensions were claimed for measurement.')

    if 'D7' in dims_claimed:
        lines.append('\nD7 is claimed, but not all of it was measured (AP-1 '
                     'v1.3 D7: "Report all four"):\n')
        tr = (summary or {}).get('transcription_results', [])
        unobservable = sum(1 for r in tr
                           if r.get('outcome') == 'UNOBSERVABLE')
        if unobservable:
            lines.append(f'- **D7.3**: Transcription fidelity \u2014 partly '
                         f'measured: {unobservable} of {len(tr)} executions '
                         f'are UNOBSERVABLE (no single released figure to '
                         f'compare: routed to adjudication, or no return of '
                         f'the required operation)')
        lines.append('- **D7.4**: Invocation under pressure \u2014 not '
                     'measured: the runner sends each item once, with no '
                     'rephrasing, casual framing, escalating pressure or '
                     'adversarial input')

    lines.append('')
    return '\n'.join(lines)


def _section_declared_limitations():
    """Declared limitations section."""
    lines = ['## 13. Declared Limitations\n']

    lines.append('### Clopper-Pearson Bound (k > 0)\n')
    lines.append('AP-1 v1.3 D7.5 requires the exact one-sided 95% upper '
                 'bound for any invocation figure but states its formula '
                 'for zero failures only. For k > 0 failures the report '
                 'gives the exact Clopper-Pearson bound, the 0.95 quantile '
                 'of Beta(k+1, n-k), the general form DISPOSITION C-1 '
                 'adopts for the next version. It is computed in Decimal '
                 '(bisection on the binomial distribution) and every bound '
                 'is shown rounded up.\n')

    return '\n'.join(lines)



PROVENANCE_OUTCOMES = ['OPERANDS-GROUNDED', 'OPERAND-ORIGINATED',
                       'OPERANDS-UNOBSERVABLE', 'UNMEASURABLE']


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

    # Invocation-level outcomes, each with its proportion: the
    # unobservable case is declared and its proportion reported (AP-1 v1.3
    # D7.2(a); T3-16).
    total_inv = sum(prov_outcomes.values())
    if total_inv > 0:
        lines.append('### Per-Invocation Outcomes\n')
        lines.append('> OPERANDS-UNOBSERVABLE: a calculator call whose '
                     'operands could not be read (malformed arguments or an '
                     'unreadable expression); declared, never grounded. '
                     'UNMEASURABLE: a call in a chained item whose ground '
                     'truth declares no intermediates (SPEC R2.4); its '
                     'operands are not counted in the step table.\n')
        lines.append('| Outcome | Count | % |')
        lines.append('|---|---|---|')
        for outcome in PROVENANCE_OUTCOMES:
            count = prov_outcomes.get(outcome, 0)
            lines.append(f'| {outcome} | {count} | '
                         f'{100*count/total_inv:.1f}% |')
        lines.append('')

    # Executions for which D7.2 is UNMEASURABLE, with the reason (R3.3)
    unmeasurable = summary.get('provenance_unmeasurable')
    if unmeasurable:
        lines.append('### D7.2 UNMEASURABLE Executions\n')
        lines.append('| Item | Condition | Repeat | Reason |')
        lines.append('|---|---|---|---|')
        for entry in unmeasurable:
            lines.append(f'| {entry.get("item_id", "?")} '
                         f'| {entry.get("condition", "?")} '
                         f'| {entry.get("repeat", "?")} '
                         f'| {entry.get("reason", "?")} |')
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

def clopper_pearson_upper_k0(n, alpha=Decimal('0.05')):
    """Exact one-sided 95% Clopper-Pearson upper bound for k=0 failures.

    Formula: p_upper = 1 - alpha^(1/n)
    Source: AP-1 v1.3 D7.5. The one Decimal implementation,
    invocation._exact_upper_bound (T3-61): never float (SPEC R0.4.1).

    Args:
        n: int -- total number of trials
        alpha: Decimal (or a number, read from its text) -- significance
            level (default 0.05 for 95%)

    Returns:
        Decimal -- upper bound on failure probability; NaN if n <= 0
    """
    if n <= 0:
        return Decimal(math.nan)  # not a number: no bound without trials
    return _exact_upper_bound(n, Decimal(str(alpha)))


def _format_dim_result(dim, data):
    """Format a dimension result for the table."""
    if dim == 'D1':
        rate = data.get('accuracy_rate')
        auto = data.get('auto_scored_n', 0)
        adj = data.get('adjudicated_n', 0)
        pending = adj + data.get('unmeasurable_n', 0)
        if rate is not None and pending:
            # Every wrong figure is among the items awaiting
            # adjudication (SPEC R2.0), so no rate is printed (T3-3)
            return (f'No rate: {pending} items await adjudication '
                    f'(auto-scored {auto}: {data.get("correct", 0)} '
                    f'correct, {data.get("incorrect", 0)} incorrect, '
                    f'{data.get("no_figure", 0)} no figure)')
        if rate is not None:
            return (f'Accuracy: {rate} '
                    f'(auto-scored {auto}; {adj} adjudicated not in rate)')
        return 'No rate computed'
    return str(data)


def _unmeasured_reason(dim):
    """Return the reason a dimension is not measured.

    Names are AP-1 v1.3 §4's (T3-33), except D2, which SPEC and this
    runner call Reproducibility (AP-1 v1.3: Determinism). D1, D2 and D7
    are measured by the runner when claimed; only D3-D6 need human
    adjudication (SPEC §1.1, §1.2; S3-G6-2).
    """
    not_claimed = 'not claimed in this configuration'
    adjudicated = 'requires human adjudication; the runner does not measure it'
    reasons = {
        'D1': f'Accuracy — {not_claimed} (the runner auto-scores it)',
        'D2': f'Reproducibility — {not_claimed} (the runner measures it '
              f'from repeated runs)',
        'D3': f'Provenance — {adjudicated}',
        'D4': f'Refusal integrity — {adjudicated}',
        'D5': f'Adversarial resistance — {adjudicated}',
        'D6': f'Conflicting input — {adjudicated}',
        'D7': f'Computation invocation — {not_claimed} (the runner '
              f'measures D7.1-D7.3 from tool-call evidence)',
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
