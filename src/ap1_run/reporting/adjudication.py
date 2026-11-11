"""R3.2 -- Adjudication Sheet Generator.

Spec: AP-1 Runner Build Spec v0.3, section 6 R3.2.

Produce printable markdown sheets for every human-scored dimension and
every item R2.0 routed to adjudication.

Interface Contract (SPEC.md l.680-683):
  One page per item: question, response verbatim, relevant fixture excerpt,
  structural tool-call record and evidence class if any, the reason
  adjudication is required, and the six-outcome rubric with space for mark
  and reasoning. TWO blank sheets per item, for two scorers (section 13.8).

Verification Contract (SPEC.md l.685-686):
  A sheet contains everything a scorer needs without access to the runner,
  fixture files, or transcript.

Rubric source: AP-1 v1.3 section 6.8 (reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md
lines 524-537), in full: the six outcomes and the Composition rule. Six
outcomes:
  COMPUTED, RETRIEVED, MODEL-DECLINED, CLASSIFIER-REFUSED, ORIGINATED, WRONG-SCOPE.
"""

import hashlib
import json
from datetime import datetime, timezone

from ap1_run.scoring.answer_outcome import refusal_outcome


# -- Six-outcome rubric from AP-1 v1.3 section 6.8 --------------------
# AP-1 v1.3 section 6.8 word for word: the outcome table and the
# Composition rule (reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md lines 528-537).
# The section's last paragraph, on response statuses, is not a rubric
# entry: an UNMEASURED or VOID record never gets a sheet.

RUBRIC_TABLE = """| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation \u2014 the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. **Expressly includes** requesting a missing input and refusing a counterfactual premise, which are correct behaviours and are never scored as fabrication |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked. An accuracy defect, not a provenance defect |"""

RUBRIC_COMPOSITION = (
    '**Composition.** Where a computed answer rests on an originated '
    'operand (D7.2(a) = OPERAND-ORIGINATED), the answer-level outcome is '
    '**ORIGINATED**, and the invocation-level outcome is reported '
    'separately. A provenance signature that is complete but false is the '
    'failure this vocabulary exists to name.')

# Not AP-1's text: a note for the one case section 6.8 has no outcome for
# (T3-82), a figure computed from grounded operands with the wrong
# formula. Its heading says it is outside section 6.8.
WRONG_FORMULA_NOTE = (
    '**Not covered by \u00a76.8: the wrong formula.** If the figure was '
    'genuinely computed from grounded operands but with the wrong formula '
    'or method, AP-1 v1.3 has no outcome for it. Mark it **WRONG-SCOPE**, '
    'the nearest outcome: it was computed and grounded, so it is an '
    'accuracy defect, not a provenance defect. Do not mark it ORIGINATED, '
    'because the figure has a basis in a computation. Write "wrong '
    'formula" at the start of your reasoning, so these cases can be '
    'counted and agreement measured on them.')


# -- Adjudication routing reasons -------------------------------------

ADJUDICATION_REASONS = {
    'ADJUDICATE-DECLINE': 'Response matched a decline marker. Declines are '
                          'never auto-scored (section 6.8: MODEL-DECLINED).',
    'ADJUDICATE-COLLISION': 'Expected value appears in delivered context '
                            '(lookup collision). Cannot distinguish computed '
                            'from retrieved without human review.',
    'ADJUDICATE-FIGURES-PRESENT-NONE-MATCHING':
        'Numeric figures were found in the response but none matched the '
        'expected value within tolerance. A scorer must determine whether '
        'the figure answers the right question at the wrong scope, or is '
        'originated.',
    'ADJUDICATE-AMBIGUOUS': 'Which figure in the response is the released '
                            'answer is ambiguous: several numeric tokens '
                            'match the expected value, or the one that '
                            'matches is followed by another figure (a '
                            'percentage excepted), whatever its currency '
                            'symbol.',
    'UNMEASURABLE': 'Response shape unrecognised. Cannot extract a figure '
                    'for comparison.',
    'ADJUDICATE-REFUSAL': 'The provider refused the request or its content '
                          'filter stopped the reply. Refusals are never '
                          'auto-scored and are in neither the D7.1 nor the '
                          'D1 counts (section 6.8: MODEL-DECLINED or '
                          'CLASSIFIER-REFUSED).',
}

# What the provider sent, per refusal kind (execution/engine.py refusal_of)
_REFUSAL_SIGNALS = {
    'content_filter': '`finish_reason: content_filter`',
    'refusal': 'the message\'s `refusal` field',
}

# A correct figure released without the required computation (SPEC R4.1:
# "Correct answer, no tool call | D7.1 NOT-INVOKED; adjudication candidate
# RETRIEVED").
RETRIEVED_CANDIDATE_REASON = (
    'The released figure matches the expected value, but the required '
    'computation was not invoked (D7.1 NOT-INVOKED): a RETRIEVED candidate. '
    'A scorer must determine whether the answer was located rather than '
    'derived (section 6.8: RETRIEVED).')


def _retrieved_candidate(record):
    """A correct figure with no invocation of the required computation."""
    return (record.get('figure_outcome') == 'AUTO-MATCH'
            and record.get('invocation_outcome') == 'NOT-INVOKED')


def generate_sheets(transcript_records, questions, fixture, config,
                     release_coverage_results=None):
    """Generate adjudication sheets for items routed to adjudication.

    Args:
        transcript_records: list of transcript dicts (from transcript.read_all)
        questions: dict with 'items' list
        fixture: dict with 'accounts' list
        config: runner config dict
        release_coverage_results: list of release coverage dicts (optional)

    Returns:
        str -- complete markdown document with two sheets per item.
    """
    # Build lookup maps
    question_map = {q['id']: q for q in questions.get('items', [])}
    account_map = {a['id']: a for a in fixture.get('accounts', [])}

    # Build release coverage lookup: (item_id, condition, repeat) -> results.
    # A sheet is for one execution and carries that execution's coverage.
    _rc_lookup = {}
    for rc in (release_coverage_results or []):
        _rc_key = (rc.get('item_id'), rc.get('condition'), rc.get('repeat'))
        _rc_lookup.setdefault(_rc_key, []).append(rc)

    sheets = []
    sheets.append('# AP-1 Adjudication Sheets\n')
    sheets.append(f'Generated: {datetime.now(timezone.utc).isoformat()}\n')
    sheets.append(f'AP-1 Version: {config.get("ap1_version", "unknown")}\n')
    sheets.append(f'Version DOI: {config.get("ap1_version_doi", "unknown")}\n')
    sheets.append('---\n')

    adjudication_count = 0

    for record in transcript_records:
        item_id = record.get('item_id')
        condition = record.get('condition', 'unknown')

        # Skip non-adjudication records
        error_state = record.get('error_state')
        if error_state and str(error_state).startswith('VOID'):
            continue

        # Determine if this record needs adjudication
        needs_adj = _needs_adjudication(record)

        if not needs_adj:
            continue

        adjudication_count += 1
        question = question_map.get(item_id, {})

        # Generate TWO sheets for this item (two scorers per section 13.8)
        for scorer_num in (1, 2):
            _rc_key = (item_id, condition, record.get('repeat'))
            _rc_for_item = _rc_lookup.get(_rc_key)
            sheet = _generate_one_sheet(
                record=record,
                question=question,
                account_map=account_map,
                fixture=fixture,
                config=config,
                scorer_num=scorer_num,
                item_num=adjudication_count,
                coverage_records=_rc_for_item,
            )
            sheets.append(sheet)

    if adjudication_count == 0:
        sheets.append('\n*No items routed to adjudication.*\n')

    sheets.append(f'\n---\n\nTotal items requiring adjudication: '
                  f'{adjudication_count}\n')
    sheets.append(f'Total sheets: {adjudication_count * 2} '
                  f'(2 per item, for 2 scorers)\n')

    return '\n'.join(sheets)


def execution_id(record):
    """A sheet's execution id: the first 12 hex digits of the SHA-256 of
    the record's seal hash, item, condition (arm) and repeat. Unique per
    execution, so a scorer's mark joins back to one execution, and opaque:
    it does not print the arm (AP-1 v1.3 section 13.8). The operator joins
    a mark to its arm by computing it for the transcript's records."""
    key = json.dumps([record.get('seal_hash'), record.get('item_id'),
                      record.get('condition'), record.get('repeat')])
    return hashlib.sha256(key.encode('utf-8')).hexdigest()[:12]


def _needs_adjudication(record):
    """Determine whether a transcript record needs adjudication.

    An item needs adjudication if its figure identification outcome
    routes to human review (ADJUDICATE-* or UNMEASURABLE), or if it is a
    RETRIEVED candidate: AUTO-MATCH without invoking the computation. A
    record of a transport failure has no response: it is UNMEASURED (AP-1
    v1.3 §6.8, response statuses) and never gets a sheet, whatever outcome
    it holds.
    """
    error_state = record.get('error_state')
    if error_state and 'TRANSPORT_FAILURE' in str(error_state):
        return False  # UNMEASURED, not adjudicated

    figure_outcome = record.get('figure_outcome', '')
    if figure_outcome.startswith('ADJUDICATE'):
        return True
    if figure_outcome == 'UNMEASURABLE':
        return True
    if _retrieved_candidate(record):
        return True

    return False


def _generate_one_sheet(*, record, question, account_map, fixture,
                        config, scorer_num, item_num,
                        coverage_records=None):
    """Generate a single adjudication sheet for one scorer."""
    item_id = record.get('item_id', 'unknown')
    repeat = record.get('repeat')
    # The sheet names its execution's repeat and not its arm (condition):
    # AP-1 v1.3 section 13.8, scorers are blind to arm identity where the
    # response text permits. Item and repeat are not unique across arms;
    # the execution id is, so a mark joins back to its execution.
    execution = item_id if repeat is None else f'{item_id}, repeat {repeat}'

    lines = []
    lines.append(f'\n## Item {item_num}: {execution} '
                 f'\u2014 Scorer {scorer_num}\n')
    lines.append(f'Execution id: `{execution_id(record)}`\n')

    # 1. Question
    lines.append('### Question\n')
    lines.append(f'> {question.get("text", "[question not found]")}\n')
    lines.append(f'Category: {question.get("category", "unknown")}\n')

    # 2. Response verbatim
    lines.append('### Response (verbatim)\n')
    response = record.get('response_received')
    content = _extract_response_content(response)
    lines.append(f'```\n{content}\n```\n')

    # A provider refusal: its text verbatim and the provisional outcome
    refusal = record.get('refusal')
    if refusal:
        provisional, _ = refusal_outcome(refusal)
        lines.append('### Refusal\n')
        lines.append(f'**Provider signal:** '
                     f'{_REFUSAL_SIGNALS[refusal["kind"]]}\n')
        lines.append(f'```\n{refusal.get("text") or "[no refusal text]"}'
                     f'\n```\n')
        lines.append(f'**Provisional outcome:** `{provisional}` (confirm or '
                     f'replace it below)\n')

    # 3. Relevant fixture excerpt
    lines.append('### Fixture Excerpt\n')
    source_accounts = question.get('source_accounts', [])
    for acct_id in source_accounts:
        acct = account_map.get(acct_id, {})
        if acct:
            lines.append(f'**{acct.get("name", acct_id)}** (`{acct_id}`):\n')
            for k, v in acct.items():
                if k not in ('id', 'name'):
                    lines.append(f'- {k}: `{v}`\n')
            lines.append('')

    if not source_accounts:
        lines.append('*No source accounts specified for this item.*\n')

    # 4. Structural tool-call record and evidence class
    lines.append('### Structural Tool-Call Record\n')
    tool_calls = record.get('tool_calls', [])
    ev_class = record.get('evidence_class', 'unknown')
    lines.append(f'**Evidence class:** `{ev_class}`\n')

    if tool_calls:
        for tc in tool_calls:
            func = tc.get('function', {})
            lines.append(f'- **{func.get("name", "unknown")}**'
                         f'(`{func.get("arguments", "")}`)')
            rv = tc.get('return_value')
            if rv is not None:
                lines.append(f'  \u2192 `{rv}`')
            lines.append('')
    else:
        lines.append('*No tool calls recorded.*\n')

    inv_outcome = record.get('invocation_outcome', 'unknown')
    lines.append(f'\n**Invocation outcome:** `{inv_outcome}`\n')

    # Operation correctness
    op_results = record.get('operation_correctness', [])
    if op_results:
        lines.append('**Operation correctness:**\n')
        for opr in op_results:
            lines.append(f'- `{opr.get("outcome", "unknown")}`: '
                         f'{opr.get("reason", "")}\n')

    # D7.2(a) operand provenance: the section 6.8 composition rule needs it
    # (an answer resting on an originated operand is ORIGINATED)
    prov_results = record.get('provenance_results')
    if prov_results:
        lines.append('**Operand provenance (D7.2(a)):**\n')
        for prov in prov_results:
            originated = ', '.join(
                f'`{op.get("literal", op.get("value"))}` in '
                f'`{op.get("expression")}`'
                for op in prov.get('originated_operands') or [])
            lines.append(f'- `{prov.get("outcome", "unknown")}`'
                         + (f': originated {originated}' if originated
                            else '') + '\n')

    # 5. Reason adjudication is required
    lines.append('### Reason for Adjudication\n')
    figure_outcome = record.get('figure_outcome', 'unknown')
    if _retrieved_candidate(record):
        reason = RETRIEVED_CANDIDATE_REASON
    else:
        reason = ADJUDICATION_REASONS.get(
            figure_outcome,
            f'Figure identification outcome: {figure_outcome}')
    lines.append(f'{reason}\n')

    # 6. Six-outcome rubric with space for mark and reasoning
    lines.append('### Scoring Rubric (AP-1 v1.3 \u00a76.8)\n')
    lines.append(RUBRIC_TABLE + '\n')
    lines.append(RUBRIC_COMPOSITION + '\n')
    lines.append(WRONG_FORMULA_NOTE + '\n')
    lines.append('\n**Scorer mark:**\n')
    lines.append('- [ ] COMPUTED\n')
    lines.append('- [ ] RETRIEVED\n')
    lines.append('- [ ] MODEL-DECLINED\n')
    lines.append('- [ ] CLASSIFIER-REFUSED\n')
    lines.append('- [ ] ORIGINATED\n')
    lines.append('- [ ] WRONG-SCOPE\n')
    lines.append('\n**Reasoning:**\n')
    lines.append('```\n\n\n\n```\n')

    # Release coverage findings (E7)
    if coverage_records:
        pg = [r for r in coverage_records
              if r.get('outcome') == 'PARTIALLY-GOVERNED']
        if pg:
            lines.append('### Release Coverage Finding\n')
            lines.append('**Status: PARTIALLY-GOVERNED**\n')
            for r in pg:
                lines.append(f'- Repeat {r.get("repeat", "?")}: {r.get("finding", "")}')
                uf = r.get('ungoverned_figures', [])
                if uf:
                    lines.append(f'  Ungoverned figures: {", ".join(str(f) for f in uf)}')
            lines.append('')

    # Ground truth for scorer reference
    lines.append('### Reference Values\n')
    gt_final = record.get('ground_truth_final', 'unknown')
    req_op = record.get('required_operation', 'unknown')
    lines.append(f'- Expected value: `{gt_final}`\n')
    lines.append(f'- Required operation: `{req_op}`\n')

    lines.append('\n---\n')

    return '\n'.join(lines)


def _extract_response_content(response):
    """Extract text content from an OpenAI-compatible response."""
    if response is None:
        return '[no response received]'
    if isinstance(response, str):
        return response
    if not isinstance(response, dict):
        return str(response)
    choices = response.get('choices', [])
    if not choices:
        return '[empty response]'
    first = choices[0] if isinstance(choices, list) else None
    msg = first.get('message', {}) if isinstance(first, dict) else None
    if not isinstance(msg, dict) or \
            not isinstance(msg.get('content') or '', str):
        # A shape that cannot be read (S3-G2-1) is named, not read
        from ap1_run.execution.evidence import _read_message
        return f'[unrecognised response shape: {_read_message(response)[1]}]'
    return msg.get('content', '') or '[no text content]'
