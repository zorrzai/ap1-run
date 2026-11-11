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
  9b. D2.2 execution conditions, sampling parameters sent, parameter echo
  10. Every UNMEASURED, UNOBSERVABLE, UNMEASURABLE and VOID cell with reason
  11. Quantisation and near-miss findings
  12. DECLARATION of which dimensions were NOT measured

Clopper-Pearson (AP-1 v1.3 D7.5; scoring/invocation.py):
  k=0 (closed form): p_upper = 1 - alpha^(1/n), alpha = 0.05.
  k>0: the exact bound, the 1 - alpha quantile of Beta(k+1, n-k), the
  general form DISPOSITION C-1 adopts. Computed in Decimal and shown
  rounded up, so a displayed bound is never below the exact one.
  k>0: the exact two-sided 95% interval beside it, as the published
  paper prints it, its ends rounded outward.

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
from decimal import MAX_PREC, ROUND_DOWN, ROUND_HALF_UP, Decimal, localcontext

from ap1_run.foundation.transcript import error_state_text
from ap1_run.runner.executions import LOOP_EXHAUSTED
from ap1_run.scoring.accuracy import (
    CATEGORY_MINIMUM_N, clopper_pearson_interval,
)
from ap1_run.scoring.invocation import (
    _exact_upper_bound, clopper_pearson_upper, format_failing_questions,
    round_up,
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


def generate_report(*, summary, config, seal_record, transcript_records=None,
                    scored_transcript=None, rescore=None):
    """Generate the evaluation report.

    Args:
        summary: dict -- the run summary (from the scorer)
        config: dict -- resolved configuration
        seal_record: dict -- pre-registration record from seal
        transcript_records: list of transcript dicts (optional, for
            cell-level detail)
        scored_transcript: {'sha256', 'records'} of the transcript the
            scoring pass read (optional), shown under section 1
        rescore: a re-score's record (scoring/rescore.py), if this is one:
            section 1 says so and names the run's runner and the scorer

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
    if 'served' in summary:
        sections.append(_served_lines(summary['served']))
    sections.append(DEMONSTRATION_STATEMENT)
    sections.append('---\n')

    # 1. Pre-registration record
    sections.append(_section_preregistration(seal_record, scored_transcript,
                                             rescore))

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

    # 9b. D2.2 execution conditions and parameter echo
    sections.append(_section_d2_conditions(summary, config,
                                           transcript_records))

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

def _served_lines(served):
    """What the responses say served them: model snapshots and backend
    fingerprints, with how many responses each, and the freeze status
    (V12-8; AP-1 §5.2 asks for confirmation that the system was frozen
    for the run)."""
    def listed(counts):
        return ', '.join(f'{value} ({n})' for value, n in
                         sorted(counts.items())) or 'not reported'
    models, fingerprints = served['models'], served['fingerprints']
    return (f'Served model (as the responses report it, with responses): '
            f'{listed(models)}\n\n'
            f'Backend fingerprints (system_fingerprint): '
            f'{listed(fingerprints)}\n\n'
            f'> Freezing (AP-1 \u00a75.2): {_freeze_status(served)}\n')


def _freeze_status(served):
    """Whether the responses show the system frozen, always stated: not
    shown (more than one model or fingerprint), not verified (an
    identifier missing from some or all responses), or consistent with a
    frozen system (one model and one fingerprint in every response). The
    runner sees only what the endpoint reports, so it never says the
    system was frozen."""
    models, fingerprints = served['models'], served['fingerprints']
    total = served.get('responses')
    if len(models) > 1 or len(fingerprints) > 1:
        return ('not shown: more than one served model or backend '
                'fingerprint; the run does not show that the system under '
                'test was frozen for its duration.')
    if total is None:
        return 'not verified: the number of responses is not recorded.'
    if total == 0:
        return 'not verified: no response was received.'
    gaps = []
    for counts, name in ((models, 'served model'),
                         (fingerprints, 'backend fingerprint')):
        missing = total - sum(counts.values())
        if missing == total:
            gaps.append(f'the responses report no {name}')
        elif missing:
            gaps.append(f'{missing} of {total} responses report no {name}')
    if gaps:
        return f'not verified: {"; ".join(gaps)}.'
    return (f'not verified by the runner; consistent with a frozen system: '
            f'all {total} responses report one served model and one '
            f'backend fingerprint.')


_RUNNER_FIELDS = ('runner_version_tag', 'runner_version_commit',
                  'runner_modified', 'runner_source_hash')


def _section_preregistration(seal_record, scored_transcript=None,
                             rescore=None):
    """Section 1: Pre-registration record, the transcript scored, and,
    for a re-score, that it is one and which runner scored it."""
    lines = ['## 1. Pre-Registration Record\n']
    if seal_record:
        lines.append('| Field | Value |')
        lines.append('|---|---|')
        for k, v in sorted(seal_record.items()):
            lines.append(f'| `{k}` | `{v}` |')
    else:
        lines.append('*No seal record available.*')
    lines.append('')
    if scored_transcript:
        lines.append(
            f'Transcript scored: SHA-256 `{scored_transcript["sha256"]}`, '
            f'{scored_transcript["records"]} records.')
        lines.append('')
    if rescore:
        lines.append(
            f'**Re-scored** on {rescore["rescored_at"]}: the figures in '
            f'this report were computed by a re-score of the run\'s '
            f'transcript, not by the run.')
        lines.append('')
        lines.append('| | ' + ' | '.join(_RUNNER_FIELDS) + ' |')
        lines.append('|---' * (len(_RUNNER_FIELDS) + 1) + '|')
        for label, key in (('the run (sealed)', 'run'),
                           ('the scorer', 'scorer')):
            lines.append(f'| {label} | ' + ' | '.join(
                f'`{rescore[key].get(f)}`' for f in _RUNNER_FIELDS) + ' |')
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

    d1 = summary.get('d1_results', {})
    by_category = d1.get('by_category')
    uncategorised = d1.get('uncategorised') or []
    if 'D1' in dims_claimed and (by_category or uncategorised):
        lines.extend(_d1_category_rows(by_category or {}, uncategorised))

    lines.append('')
    return '\n'.join(lines)


def _d1_category_rows(by_category, uncategorised=()):
    """D1 per category with n and a 95% interval (AP-1 v1.3 D1; T3-32).
    Base condition only; n counts questions; a question is correct if all
    its base executions are. The questions with no category are listed
    under the table, with their count, so none is dropped silently."""
    lines = ['\n### D1 per Category\n',
             '> AP-1 v1.3 D1: results per category, with 95% confidence '
             'intervals and n stated; no category claim where n < 10. '
             'Base condition only; the instruction-removed repeats '
             'measure D7. n counts questions; a question is correct only '
             'if every base execution of it is. Interval: exact two-sided '
             '95% Clopper-Pearson.\n',
             '| Category | n (questions) | Executions | Correct | Incorrect '
             '| No Figure | Awaiting Adjudication | Accuracy (95% CI) |',
             '|---|---|---|---|---|---|---|---|']
    for category, c in by_category.items():
        if c['interval'] is not None:
            lower, upper = c['interval']
            result = (f'{c["correct_questions"]}/{c["n"]} '
                      f'({_percent(c["correct_questions"], c["n"])}%; 95% '
                      f'CI {_round_down(lower * 100)}%-'
                      f'{round_up(upper * 100, Decimal("0.1"))}%)')
        elif c['n'] < CATEGORY_MINIMUM_N:
            result = 'no category claim: n < 10'
        else:
            result = (f'no rate: {c["pending"]} executions await '
                      f'adjudication')
        lines.append(f'| {category} | {c["n"]} | {c["executions"]} '
                     f'| {c["correct"]} | {c["incorrect"]} '
                     f'| {c["no_figure"]} | {c["pending"]} | {result} |')
    if uncategorised:
        count = len(uncategorised)
        lines.append(
            f'\nNot in any category: {count} '
            f'question{"" if count == 1 else "s"} '
            f'({", ".join(f"`{q}`" for q in uncategorised)}). '
            f'{"It is" if count == 1 else "They are"} in no row above and '
            f'in no category\'s n.')
    return lines


def _round_down(value):
    """A lower bound shown to 0.1, rounded down so it stays a bound."""
    return value.quantize(Decimal('0.1'), rounding=ROUND_DOWN)


def _interval_text(failures, n):
    """'two-sided 95% interval [L%, U%]': the exact two-sided 95%
    Clopper-Pearson interval on a failure rate, 0 <= failures <= n, as
    percentages to 0.01% (as the published paper prints it), the lower
    end rounded down and the upper end up, so the interval shown contains
    the exact one."""
    lower, upper = clopper_pearson_interval(failures, n)
    with localcontext() as ctx:
        ctx.prec = MAX_PREC  # exact: only the quantize rounds
        low = (lower * 100).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        high = round_up(upper * 100, Decimal('0.01'))
    return f'two-sided 95% interval [{low}%, {high}%]'


# What a run measured of each part of D7 (AP-1 v1.3 D7 "Report all
# four"; T3-29): a part is measured when every observation it needs was
# made, partly measured when some were not, and not measured when none
# was. Each status follows from the counts the run computed, per arm and
# evidence class, never from the part being claimed.
MEASURED, PARTLY, NOT_MEASURED = 'measured', 'partly measured', 'not measured'
_STATUS_CELL = {MEASURED: 'Measured', PARTLY: 'Partly measured',
                NOT_MEASURED: '**NOT MEASURED**'}

# The two arms of D7.1 (AP-1 D7.1 and D7.6, with the instruction removed)
D7_ARMS = ('base', 'instruction_removed')


def _status_of(statuses):
    """The status of a part made of parts with these statuses."""
    if all(s == MEASURED for s in statuses):
        return MEASURED
    if all(s == NOT_MEASURED for s in statuses):
        return NOT_MEASURED
    return PARTLY


# Outcomes that are an observation of invocation (D7.1), and the
# statuses of a planned computable execution never observed
_OBSERVED_INVOCATION = ('INVOKED', 'NOT-INVOKED')
_NOT_OBSERVED = ('UNMEASURED', 'NOT-RUN')


def _never_observed(summary, cond=None):
    """The planned computable executions (of arm cond, or of the run)
    with no response observed: UNMEASURED (transport failure, rate
    limit, interrupted) or NOT-RUN. VOID items are not computable."""
    return sum(1 for c in summary.get('non_outcome_cells', [])
               if c.get('status') in _NOT_OBSERVED
               and (cond is None or c.get('condition') == cond))


def _arm_questions(summary, cond):
    """(computable questions, questions with an observed outcome) of an
    arm, from the per-execution evidence and the cells never observed;
    None if the summary has no per-execution evidence."""
    evidence = summary.get('item_evidence')
    if not evidence:
        return None
    seen = [e for e in evidence if e.get('condition') == cond]
    computable = {e.get('item_id') for e in seen} | {
        c.get('item_id') for c in summary.get('non_outcome_cells', [])
        if c.get('status') in _NOT_OBSERVED and c.get('condition') == cond}
    observed = {e.get('item_id') for e in seen
                if e.get('invocation_outcome') in _OBSERVED_INVOCATION}
    return computable, observed


def _d71_arms(summary):
    """D7.1 per arm: [(status, text)]. An arm is measured only if every
    planned computable execution of it was observed: its questions in n
    per evidence class (§5), its UNOBSERVABLE executions, its executions
    never observed (UNMEASURED or not run), and the computable questions
    left out of n."""
    evidence = summary.get('invocation_evidence', {})
    figures = summary.get('invocation_figures', {}).values()
    arms = []
    for cond in list(D7_ARMS) + [c for c in evidence if c not in D7_ARMS]:
        classes = evidence.get(cond, {}).get('classes', {}).values()
        executions = sum(c['executions'] for c in classes)
        unobservable = sum(c['unobservable_executions'] for c in classes)
        never = _never_observed(summary, cond)
        observed = [f'n = {f["n"]}, {f.get("evidence_class") or "no class"}'
                    for f in figures
                    if f.get('condition') == cond and f.get('n')]
        if len(observed) > 1:
            observed.append('not comparable')
        gaps = []
        if unobservable:
            gaps.append(f'{unobservable} of {executions} executions '
                        f'UNOBSERVABLE')
        if never:
            gaps.append(f'{_executions(never)} UNMEASURED or not run')
        questions = _arm_questions(summary, cond)
        if questions and len(questions[1]) < len(questions[0]):
            computable, seen = questions
            gaps.append(f'{len(computable) - len(seen)} of '
                        f'{len(computable)} computable questions not in n')
        if not executions and not never:
            status, text = NOT_MEASURED, 'no executions'
        elif not observed:
            status, text = NOT_MEASURED, '; '.join(
                ['no observed outcome'] + gaps)
        elif gaps:
            status, text = PARTLY, '; '.join(observed + gaps)
        else:
            status, text = MEASURED, '; '.join(observed)
        arms.append((status, f'{cond} {status} ({text})'))
    return arms


def _inventory_gap(summary):
    """'call inventory incomplete for k executions (...)' where calls may
    have gone unseen: EV-0 executions (no invocation signal, AP-1 D7.7)
    and executions never observed; None if there are none."""
    ev0 = sum(c for ec, c in summary.get('evidence_class_counts',
                                         {}).items()
              if ec.startswith('EV-0'))
    never = _never_observed(summary)
    if not ev0 and not never:
        return None
    why = ([f'{ev0} EV-0 UNOBSERVABLE'] if ev0 else []) + (
        [f'{never} UNMEASURED or not run'] if never else [])
    return (f'call inventory incomplete for {_executions(ev0 + never)} '
            f'({", ".join(why)})')


def _executions(count):
    """'1 execution', '2 executions'."""
    return f'{count} execution{"" if count == 1 else "s"}'


def _d72_parts(summary):
    """D7.2(a) and (b): [(status, text, where)], from the calls whose
    operands could not be read and the operations not observed."""
    parts = []
    for label, counts, unread_as, unit, where in (
            ('(a) operand provenance', summary.get('provenance_outcomes', {}),
             ('OPERANDS-UNOBSERVABLE', 'UNMEASURABLE'), 'calls',
             '\u00a76, \u00a77b'),
            ('(b) operation correctness',
             summary.get('operation_correctness_counts', {}),
             ('OPERATION-UNOBSERVABLE',), 'operations', '\u00a77')):
        total = sum(counts.values())
        unread = sum(counts.get(name, 0) for name in unread_as)
        names = ' or '.join(unread_as)
        if not total:
            status, text = NOT_MEASURED, f'no {unit[:-1]} evaluated'
        elif unread == total:
            status, text = NOT_MEASURED, f'all {total} {unit} {names}'
        elif unread:
            status, text = PARTLY, f'{unread} of {total} {unit} {names}'
        else:
            status, text = MEASURED, f'{total} {unit}'
        parts.append((status, f'{label} {status}: {text}', where))
    return parts


def _d72_status(summary, parts):
    """D7.2's status: its parts', and at most partly measured where the
    call inventory is incomplete."""
    status = _status_of([s for s, _, _ in parts])
    if status == MEASURED and _inventory_gap(summary):
        return PARTLY
    return status


def _d73_part(summary):
    """D7.3: (status, text), from its UNOBSERVABLE executions and the
    executions never observed (UNMEASURED or not run)."""
    tr = summary.get('transcription_results', [])
    unobservable = sum(1 for r in tr if r.get('outcome') == 'UNOBSERVABLE')
    never = _never_observed(summary)
    unread = [f'{_executions(never)} UNMEASURED or not run'] if never else []
    if not tr:
        return NOT_MEASURED, '; '.join(['no executions'] + unread)
    if unobservable == len(tr):
        return NOT_MEASURED, '; '.join(
            [f'all {len(tr)} executions UNOBSERVABLE'] + unread)
    if unobservable:
        return PARTLY, '; '.join(
            [f'{unobservable} of {len(tr)} executions UNOBSERVABLE'] + unread)
    if unread:
        return PARTLY, '; '.join(unread)
    return MEASURED, f'{len(tr)} executions'


def _classes_note(summary, figures, where):
    """'; on k evidence classes, not comparable ...' where the counts of
    these figures rest on more than one class (AP-1 D7.7), else ''."""
    by_class = summary.get('d7_outcomes_by_class', {})
    classes = {ec for figure in figures for ec in by_class.get(figure, {})}
    if len(classes) < 2:
        return ''
    return (f'; on {len(classes)} evidence classes, not comparable (per '
            f'class: {where})')


def _d7_rows(summary, d7):
    """§3 rows for a claimed D7: one per sub-dimension (AP-1 v1.3 D7
    "Report all four"; T3-29). D7.4 is never measured; the status of
    D7.1-D7.3 follows from what was computed for each arm and class."""
    arms = _d71_arms(summary)
    d71 = _status_of([status for status, _ in arms])
    d72_parts = _d72_parts(summary)
    d72 = _d72_status(summary, d72_parts)
    d73, d73_text = _d73_part(summary)
    measured = (d71, d72, d73)
    whole = (NOT_MEASURED if all(s == NOT_MEASURED for s in measured)
             else PARTLY)
    (_, a, a_where), (_, b, b_where) = d72_parts
    gap = _inventory_gap(summary)
    tr = summary.get('transcription_results', [])
    return [
        f'| D7 | {_STATUS_CELL[whole]} | {d7.get("n", "N/A")} | D7.1 '
        f'{d71}, D7.2 {d72}, D7.3 {d73}; D7.4 not measured (\u00a712) |',
        f'| D7.1 | {_STATUS_CELL[d71]} | see \u00a75 | Invocation rate per '
        f'condition (\u00a75): {"; ".join(text for _, text in arms)} |',
        f'| D7.2 | {_STATUS_CELL[d72]} | see \u00a76-7b | {a} ({a_where}); '
        f'{b} ({b_where})' + (f'; {gap}' if gap else '') +
        f'{_classes_note(summary, ("D7.2(a)", "D7.2(b)"), "§7, §7b")} |',
        f'| D7.3 | {_STATUS_CELL[d73]} | {len(tr)} | Transcription fidelity '
        f'(D7.3 section): {d73}: {d73_text}'
        f'{_classes_note(summary, ("D7.3",), "D7.3 section")} |',
        '| D7.4 | **NOT MEASURED** | \u2014 | Invocation under pressure '
        '(\u00a712) |',
    ]


def _per_class_table(summary, figure, outcomes, label=str):
    """The outcome counts of a D7 figure per evidence class, where they
    rest on more than one (AP-1 D7.7: not comparable across classes);
    [] otherwise. label gives an outcome's row name."""
    by_class = summary.get('d7_outcomes_by_class', {}).get(figure, {})
    if len(by_class) < 2:
        return []
    classes = sorted(by_class)
    lines = ['Per evidence class (AP-1 D7.7: not comparable across '
             'classes):\n',
             '| Outcome | ' + ' | '.join(f'`{ec or "no class"}`'
                                       for ec in classes) + ' |',
             '|---' * (len(classes) + 1) + '|']
    for outcome in outcomes:
        lines.append(f'| {label(outcome)} | ' + ' | '.join(
            str(by_class[ec].get(outcome, 0)) for ec in classes) + ' |')
    lines.append('| Total | ' + ' | '.join(
        str(sum(by_class[ec].values())) for ec in classes) + ' |\n')
    return lines


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
            pct = _share(c, total) if total > 0 else '\u2014'
            lines.append(f'| `{outcome}` | {c} | {pct}% |')
        lines.append(f'| **Total** | **{total}** | |')
        per_class = _per_class_table(
            summary, 'D7.3', ['TRANSCRIBED-EXACT', 'TRANSCRIBED-ALTERED',
                              'UNOBSERVABLE'], label=lambda o: f'`{o}`')
        if per_class:
            lines.append('')
            lines.extend(per_class[:-1] + [per_class[-1].rstrip('\n')])

        rounded = [r for r in tr_results
                   if r['outcome'] == 'TRANSCRIBED-EXACT'
                   and r.get('rounded_under_declared_policy')]
        artefacts = sum(1 for r in rounded if r.get('float_artefact'))
        chosen = len(rounded) - artefacts
        lines.append(
            f'\nOf the {counts.get("TRANSCRIBED-EXACT", 0)} '
            f'`TRANSCRIBED-EXACT`, {len(rounded)} were rounded under the '
            f'declared quantisation policy (licensed rounding, EXACT under '
            f'AP-1 v1.3). Of these: roundings of the tool\'s return to the '
            f'declared places, {chosen}; float artefacts of the tool (the '
            f'return differs from the release only past a binary float\'s 15 '
            f'significant digits, such as 15.200000000000001 for 15.20), '
            f'{artefacts}. A strict v1.2 "match" count subtracts the '
            f'roundings, or all {len(rounded)} for the strictest reading.')

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
            pct = _share(c, rc_total) if rc_total > 0 else '\u2014'
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
    rate (k=0: 1 - 0.05^(1/n); k>0: Clopper-Pearson), rounded up; for
    k>0 the exact two-sided 95% interval beside it, as the published
    paper prints it (to 0.01%, rounded outward). Beside k, each failing
    question with its NOT-INVOKED repeats out of its observed repeats
    ("2 (Q02 48/50, Q06 21/50)"). The rate is printed as a percentage
    with k/n
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
                 'NOT-INVOKED; beside k, each failing question with its '
                 'NOT-INVOKED repeats out of its observed repeats (EV-0 '
                 'repeats are in neither). UNOBSERVABLE executions (EV-0) are neither '
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
        if 0 < k <= n:
            # Beside D7.5's bound, the two-sided interval the published
            # paper prints for k > 0
            interval = _interval_text(k, n)
            bound_str += f'; {interval}'
            bound_text += f'; {interval}'
        failing = data.get('failing_questions')
        k_str = f'{k} ({format_failing_questions(failing)})' if failing else k
        lines.append(f'| {metric} | {k_str} | {n} | {rate_str} | {bound_str} '
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


def _share(part, whole):
    """part/whole as a percentage to one decimal, in Decimal and rounded
    half up, the default declared rounding (SPEC R0.4.1: no binary float
    where a value is reported). 1/400 is '0.3', not float's '0.2'."""
    return str((Decimal(part) / Decimal(whole) * 100).quantize(
        Decimal('0.1'), rounding=ROUND_HALF_UP))


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
    op_outcomes = ['OPERATION-CORRECT', 'WRONG-OPERATION',
                   'OPERATION-UNOBSERVABLE']
    for outcome in op_outcomes:
        count = op_counts.get(outcome, 0)
        lines.append(f'| {outcome} | {count} |')
    per_class = _per_class_table(summary, 'D7.2(b)', op_outcomes)
    if per_class:
        lines.append('')
        lines.extend(per_class[:-1] + [per_class[-1].rstrip('\n')])

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
        lines.append('### D1 Accuracy (base condition only)\n')
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
    lines.append('> Figures surface: each run\'s identified answer, its '
                 'released figure or else the one value it states. An '
                 'answer not identified (a decline, no figure, several '
                 'figures) is unresolved: counted, never a value, and never '
                 'evidence that the answers were stable. A question-'
                 'condition with one is UNMEASURED unless its identified '
                 'answers already differ, counted then as at least that '
                 'many.\n')

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
            lines.append(
                f'| {item} | {_cell(condition)} | {surface_name} '
                f'| `{data.get("mechanism", "unknown")}` | {_d2_basis(data)} '
                f'| {_d2_distinct(data)} '
                f'| {_cell(data.get("successful_runs"))} '
                f'| `{data.get("parameter_echo_status", "UNVERIFIED")}` |')

    lines.append('')
    return '\n'.join(lines)


def _d2_basis(data):
    """The evidence basis of a D2 class (SPEC R3.3 "with evidence basis
    and operator-declared marking"; T3-4): operator-declared, or what was
    observed and that the class is not operator-declared."""
    if data.get('operator_declared'):
        return 'operator-declared'
    runs = data.get('successful_runs')
    if runs is None:
        return 'evidence: no runs recorded; not operator-declared'
    return (f'evidence: observed over {runs} run{"" if runs == 1 else "s"}; '
            f'not operator-declared')


def _d2_distinct(data):
    """The number of distinct values and, on the figures surface, the
    values themselves (AP-1 D2 "distinct numeric answers per question";
    T3-4): '2: 2600.00; 2500.00'. Answers not identified are counted
    apart, never as a value: 'at least 2: 2600.00; 2500.00; 3
    unresolved', or '—: 144.00; 14 unresolved' where they leave the
    count unknown."""
    count = data.get('distinct_values')
    values = list(data.get('values') or [])
    unresolved = data.get('unresolved')
    if unresolved:
        values.append(f'{unresolved} unresolved')
    if not values:
        return _cell(count)
    shown = _cell(count)
    if unresolved and count is not None:
        shown = f'at least {count}'
    return f'{shown}: ' + _cell('; '.join(values))


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


def _serving_line(transcript_records):
    """What the recorded responses say served them: the 'model' and
    'system_fingerprint' of each response body, with counts."""
    models, fingerprints = {}, {}
    for rec in transcript_records or []:
        body = rec.get('response_received')
        if not isinstance(body, dict):
            continue
        for key, counts in (('model', models),
                            ('system_fingerprint', fingerprints)):
            value = body.get(key)
            if value:
                counts[str(value)] = counts.get(str(value), 0) + 1
    if not models and not fingerprints:
        return ('- Serving stack and version: not disclosed by the '
                'endpoint; the runner cannot observe it.')

    def listed(counts):
        return ', '.join(f'{value} ({n})' for value, n in
                         sorted(counts.items())) or 'not reported'
    return (f'- Serving stack and version: as the responses report it, '
            f'model {listed(models)}; backend fingerprints '
            f'(system_fingerprint) {listed(fingerprints)}; the runner '
            f'observes nothing more.')


def _section_d2_conditions(summary, config, transcript_records=None):
    """Section 9b: the D2.2 disclosures.

    AP-1 v1.3 D2.2: every D2 result reports the serving stack and
    version, whether a deterministic or batch-invariant mode was enabled,
    the concurrency conditions, and all sampling parameters sent; where
    the platform echoes the parameters it applied, a parameter requested
    and silently ignored is a platform finding. What the endpoint does not
    disclose is said, not left out.
    """
    lines = ['## 9b. D2.2 Execution Conditions\n']
    lines.append(_serving_line(transcript_records))
    sampling = config.get('sampling') or {}
    seed = sampling.get('seed')
    if seed is not None and not isinstance(seed, dict):
        lines.append(f'- Deterministic or batch-invariant mode: none '
                     f'requested by the runner beyond the `seed` sent '
                     f'(`{seed}`); whether the endpoint honours it, or '
                     f'enables such a mode, is not disclosed.')
    else:
        lines.append('- Deterministic or batch-invariant mode: none '
                     'requested by the runner; whether the endpoint enables '
                     'one is not disclosed.')
    lines.append('- Concurrency: one request at a time, sequentially, from '
                 'a single process.')
    lines.append('- Sampling parameters sent:')
    for name, value in sorted(sampling.items()):
        if isinstance(value, dict) and value.get('value') == 'omitted':
            lines.append(f'  - `{name}`: not sent ({value.get("reason")})')
        else:
            lines.append(f'  - `{name}`: `{value}`')
    if not sampling:
        lines.append('  - none')
    echo = summary.get('parameter_echo') or {}
    lines.append(f'- Parameter echo: `{echo.get("status", "UNVERIFIED")}` '
                 f'({echo.get("responses", 0)} responses checked)')
    for finding in echo.get('findings', []):
        lines.append(f'  - Platform finding (D2.2): {finding}')
    lines.append('')
    return '\n'.join(lines)


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

    A tool loop stopped by the turn limit (T3-67) is a flag on an
    executed, scored execution, not a status of its own: it is the reason
    beside its R2.0 figure's UNMEASURABLE cell and its EV-0 invocation
    cell when it has them, and no cell otherwise.
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
    flags = {}
    for rec in records:
        # An EV-0 state is structured (T3-35); its text is derived.
        error = error_state_text(rec.get('error_state'))
        evidence = str(rec.get('evidence_class'))
        # The loop flag is apart from invocation observability: an
        # exhausted loop keeps its EV-0 cell, the flag beside its reason.
        flag = error if error.startswith(LOOP_EXHAUSTED) else None
        if flag:
            flags[(rec.get('item_id'), rec.get('condition'),
                   rec.get('repeat'))] = flag
        elif error:
            add(rec, error.split(':')[0], error, 'execution', execution=True)
            continue
        if 'UNOBSERVABLE' in evidence:
            reason = f'Evidence class: {evidence}'
            add(rec, 'UNOBSERVABLE', f'{reason}; {flag}' if flag else reason,
                'D7.1 invocation', execution=True)
    for rec in records:
        if rec.get('figure_outcome') == 'UNMEASURABLE':
            reason = 'response could not be read; routed to adjudication'
            flag = flags.get((rec.get('item_id'), rec.get('condition'),
                              rec.get('repeat')))
            add(rec, 'UNMEASURABLE', f'{reason}; {flag}' if flag else reason,
                'R2.0 figure')
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
    claimed, the parts of D7 not fully measured are declared too: D7.4
    always, and D7.1-D7.3 by what the run computed for them (T3-29).
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
        summary = summary or {}
        lines.append('\nD7 is claimed, but not all of it was measured (AP-1 '
                     'v1.3 D7: "Report all four"):\n')
        arms = _d71_arms(summary)
        d71 = _status_of([status for status, _ in arms])
        if d71 != MEASURED:
            lines.append(f'- **D7.1**: Invocation rate \u2014 {d71}: ' +
                         '; '.join(text for status, text in arms
                                   if status != MEASURED))
        parts = _d72_parts(summary)
        d72 = _d72_status(summary, parts)
        if d72 != MEASURED:
            gap = _inventory_gap(summary)
            lines.append(f'- **D7.2**: Computation correctness \u2014 '
                         f'{d72}: ' + '; '.join(
                             [text for status, text, _ in parts
                              if status != MEASURED] + ([gap] if gap
                                                        else [])))
        tr = summary.get('transcription_results', [])
        unobservable = sum(1 for r in tr
                           if r.get('outcome') == 'UNOBSERVABLE')
        never = _never_observed(summary)
        why = ('(no single released figure to compare: routed to '
               'adjudication, or no return of the required operation)')
        d73 = []
        if not tr:
            d73.append('no executions')
        elif unobservable == len(tr):
            d73.append(f'all {len(tr)} executions are UNOBSERVABLE {why}')
        elif unobservable:
            d73.append(f'{unobservable} of {len(tr)} executions are '
                       f'UNOBSERVABLE {why}')
        if never:
            d73.append(f'{_executions(never)} UNMEASURED or not run')
        if d73:
            lines.append(f'- **D7.3**: Transcription fidelity \u2014 '
                         f'{_d73_part(summary)[0]}: ' + '; '.join(d73))
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
                 'is shown rounded up. Beside it, for k > 0, the report '
                 'gives the exact two-sided 95% Clopper-Pearson interval, '
                 'as the published paper prints it, with its ends rounded '
                 'outward.\n')

    lines.append('### Percentage Answers\n')
    lines.append('In a response\'s text, a figure written with % is never '
                 'compared with the expected value: SPEC R0.4.2 records the '
                 'percent flag, and 15.20% is not the money figure 15.20 '
                 '(S3-G4-2). The expected value has no unit (SPEC R3.1: '
                 'final is a Decimal), so the runner cannot tell an answer '
                 'that is a rate from one that is an amount. For an item '
                 'whose answer is a rate (18.5): "18.5%" is not compared, so '
                 'it routes to adjudication as figures present, none '
                 'matching; the same rate written without % ("18.5", "18.5 '
                 'percent") is compared as a plain figure and can be '
                 'auto-scored; a configured structured answer is compared '
                 'whatever its unit; and a figure glued to letters '
                 '("18.5pct") is not read, so the response is auto-scored as '
                 'having no figure.\n')

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
        pct_src = _share(s1_src, total_operands)
        pct_const = _share(s1_const, total_operands)
    else:
        pct_src = pct_const = '—'
    lines.append(f'| 1 | Source match | {s1_src} | {pct_src}% |')
    lines.append(f'| 1 | Declared constant | {s1_const} | {pct_const}% |')
    for step in range(2, 5):
        count = step_counts.get(step, 0)
        pct = _share(count, total_operands) if total_operands > 0 else '—'
        lines.append(f'| {step} | {step_names[step]} | {count} | {pct}% |')
    # Step 5 split: sign-inverted, ungrounded-chain, untraceable
    s5_si = summary.get('step_5_sign_inverted', 0)
    s5_uc = summary.get('step_5_ungrounded_chain', 0)
    s5_ut = summary.get('step_5_untraceable', 0)
    if total_operands > 0:
        pct_si = _share(s5_si, total_operands)
        pct_uc = _share(s5_uc, total_operands)
        pct_ut = _share(s5_ut, total_operands)
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
        lines.append('| Outcome | Count | Proportion |')
        lines.append('|---|---|---|')
        for outcome in PROVENANCE_OUTCOMES:
            count = prov_outcomes.get(outcome, 0)
            # The proportion with its denominator, every calculator
            # invocation (T3-16).
            lines.append(f'| {outcome} | {count} | {count}/{total_inv} '
                         f'({_share(count, total_inv)}%) |')
        lines.append('')
        lines.extend(_per_class_table(summary, 'D7.2(a)',
                                      PROVENANCE_OUTCOMES))

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
                    f'(base condition only; auto-scored {auto}: '
                    f'{data.get("correct", 0)} '
                    f'correct, {data.get("incorrect", 0)} incorrect, '
                    f'{data.get("no_figure", 0)} no figure)')
        if rate is not None:
            return (f'Accuracy: {rate} '
                    f'(base condition only; auto-scored {auto}; {adj} '
                    f'adjudicated not in rate)')
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
