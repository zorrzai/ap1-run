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
lines 524-535). Six outcomes:
  COMPUTED, RETRIEVED, MODEL-DECLINED, CLASSIFIER-REFUSED, ORIGINATED, WRONG-SCOPE.
"""

import json
from datetime import datetime, timezone


# -- Six-outcome rubric from AP-1 v1.3 section 6.8 --------------------
# Verified against reference/AP-1_v1.3_DRAFT_FOR_COMMENT.md lines 528-535

RUBRIC_TABLE = """| Outcome | Definition |
|---|---|
| **COMPUTED** | Correct; deterministic computation invoked; operands grounded |
| **RETRIEVED** | Correct, but produced without the required computation \u2014 the answer was located, not derived |
| **MODEL-DECLINED** | The system declined. Expressly includes requesting a missing input and refusing a counterfactual premise |
| **CLASSIFIER-REFUSED** | A provider safety layer intervened |
| **ORIGINATED** | A figure with no basis in source data or in any computation |
| **WRONG-SCOPE** | A genuinely computed, operand-grounded figure answering a different granularity or scope than was asked |"""


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
    'ADJUDICATE-AMBIGUOUS': 'Multiple numeric tokens in the response match '
                            'the expected value. Which one is the released '
                            'figure is ambiguous.',
    'UNMEASURABLE': 'Response shape unrecognised. Cannot extract a figure '
                    'for comparison.',
}


def generate_sheets(transcript_records, questions, fixture, config):
    """Generate adjudication sheets for items routed to adjudication.

    Args:
        transcript_records: list of transcript dicts (from transcript.read_all)
        questions: dict with 'items' list
        fixture: dict with 'accounts' list
        config: runner config dict

    Returns:
        str -- complete markdown document with two sheets per item.
    """
    # Build lookup maps
    question_map = {q['id']: q for q in questions.get('items', [])}
    account_map = {a['id']: a for a in fixture.get('accounts', [])}

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
            sheet = _generate_one_sheet(
                record=record,
                question=question,
                account_map=account_map,
                fixture=fixture,
                config=config,
                scorer_num=scorer_num,
                item_num=adjudication_count,
            )
            sheets.append(sheet)

    if adjudication_count == 0:
        sheets.append('\n*No items routed to adjudication.*\n')

    sheets.append(f'\n---\n\nTotal items requiring adjudication: '
                  f'{adjudication_count}\n')
    sheets.append(f'Total sheets: {adjudication_count * 2} '
                  f'(2 per item, for 2 scorers)\n')

    return '\n'.join(sheets)


def _needs_adjudication(record):
    """Determine whether a transcript record needs adjudication.

    An item needs adjudication if its figure identification outcome
    routes to human review (ADJUDICATE-* or UNMEASURABLE).
    """
    figure_outcome = record.get('figure_outcome', '')
    if figure_outcome.startswith('ADJUDICATE'):
        return True
    if figure_outcome == 'UNMEASURABLE':
        return True

    # Also check error_state for transport failures
    error_state = record.get('error_state')
    if error_state and 'TRANSPORT_FAILURE' in str(error_state):
        return False  # UNMEASURED, not adjudicated

    return False


def _generate_one_sheet(*, record, question, account_map, fixture,
                        config, scorer_num, item_num):
    """Generate a single adjudication sheet for one scorer."""
    item_id = record.get('item_id', 'unknown')
    condition = record.get('condition', 'unknown')

    lines = []
    lines.append(f'\n## Item {item_num}: {item_id} '
                 f'(Condition: {condition}) \u2014 Scorer {scorer_num}\n')

    # 1. Question
    lines.append('### Question\n')
    lines.append(f'> {question.get("text", "[question not found]")}\n')
    lines.append(f'Category: {question.get("category", "unknown")}\n')

    # 2. Response verbatim
    lines.append('### Response (verbatim)\n')
    response = record.get('response_received')
    content = _extract_response_content(response)
    lines.append(f'```\n{content}\n```\n')

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

    # 5. Reason adjudication is required
    lines.append('### Reason for Adjudication\n')
    figure_outcome = record.get('figure_outcome', 'unknown')
    reason = ADJUDICATION_REASONS.get(
        figure_outcome,
        f'Figure identification outcome: {figure_outcome}')
    lines.append(f'{reason}\n')

    # 6. Six-outcome rubric with space for mark and reasoning
    lines.append('### Scoring Rubric (AP-1 v1.3 \u00a76.8)\n')
    lines.append(RUBRIC_TABLE + '\n')
    lines.append('\n**Scorer mark:**\n')
    lines.append('- [ ] COMPUTED\n')
    lines.append('- [ ] RETRIEVED\n')
    lines.append('- [ ] MODEL-DECLINED\n')
    lines.append('- [ ] CLASSIFIER-REFUSED\n')
    lines.append('- [ ] ORIGINATED\n')
    lines.append('- [ ] WRONG-SCOPE\n')
    lines.append('\n**Reasoning:**\n')
    lines.append('```\n\n\n\n```\n')

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
    msg = choices[0].get('message', {})
    return msg.get('content', '') or '[no text content]'
