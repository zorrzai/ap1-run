# Review findings register

This register defines the finding IDs used in the test suites, commit messages and pull requests
of `ap1-run`. It is a record of what was found: an entry's ID, severity, location and clause do not
change once published. What became of a finding is recorded in its "Addressed by" field (see
[Addressed by](#addressed-by)); the fixes themselves are tracked in the issues and the fix PRs.

People are named by role ("the maintainer"), and decisions are cited as "maintainer decision DEC-n"
([Maintainer decisions](#maintainer-decisions)).

**Code snapshot.** Locations are given as `file.py:line` at `c8df9ca` (`main`, flat layout). The
production code there is byte-identical to `77514b4`, the commit the October 2026 review examined;
`c8df9ca` changes only `README.md` and `FINDINGS_ERRATA.md`. Findings made later, in the
`src/ap1_run/` layout, concern code that already exists at `c8df9ca`, so they are located there too.
The exception is the REORG series, which concerns code that does not exist at `c8df9ca`; each of
its entries gives its location at the head of the pull request that adds the code.

**After the reorg.** Each entry that points into code also gives, under "After the reorg", where
that code is once the reorganisation is complete: `file.py:line` in the `src/ap1_run/` layout (or
`tools/`, `tests/legacy/`, `ap1_inspect/`, `example/`), with the function or module-level name.
It holds from the end of the last reorganisation pull request that moves code; later changes are
not tracked in it, so the function name is the better guide once lines shift. The location at
`c8df9ca` stays the anchor. Once a finding is fixed, its "Addressed by" field takes over, and its
"After the reorg" location may be left blank.

## ID schemes

| prefix | meaning |
|---|---|
| `T3-n` | the October 2026 review of `main` at `77514b4`, judged against AP-1 v1.3 (the draft for comment, read with the editorial errata in `ERRATA.md` of the admissibility-protocol repository) and the instrument's own claims (SPEC.md, README, KNOWN_ISSUES, FINDINGS) |
| `V12-n` | gaps against AP-1 v1.2, the version in force, found when the same code was re-judged against v1.2 |
| `S3-G<group>-<n>` | defects found while writing tests that pin the current behaviour, by test group |
| `S4-G<group>-<n>` | defects found while writing failing-first tests of the correct behaviour, by test group |
| `REORG-n` | defects in the tooling added by the reorganisation pull requests (regression harness, CI), found while reviewing them |

Labels from other documents are not IDs of this register: FINDINGS.md's findings (F1–F10, and
F11 in FINDINGS_ERRATA.md), FINDINGS_ERRATA.md's entries (E1–E7, C1–C10, N1–N4), and the comments
in the AP-1 v1.3 publisher's comment and disposition record (C-1, GH-5, …). Below they are written
with the document's name, for example "FINDINGS.md F7".

## Severity

| level | meaning |
|---|---|
| critical | on the live path, the instrument can report an admissible or clean result for an execution it could not observe or check (an unobservable case counted as a success, or a check that fails open), or a seal or provenance check can be passed, with nothing reported, by an input it exists to refuse. Offline verifiers such as `verify_run_seal.py` are not the live path |
| high | a measured dimension is wrong, or unmeasured while claimed measured; or a breach that, under the AP-1 §5 preamble, makes any claim of AP-1 evaluation invalid |
| medium | wrong in edge cases a real run can meet, or misleading output |
| low | robustness or clarity, or wrong only on inputs a real run is unlikely to produce |
| info | worth knowing, not a defect of the code: a declared limitation, a gap or tension in the standard, or a documentation or test matter that changes no result |

T3 critical and high ratings were checked by a second, adversarial pass over the code that tried to
disprove each one, and some were moved; the rating shown is the final one. T3 ratings below high,
and all S3, S4 and REORG ratings, are the finder's estimate. Where a finder gave a split or
off-scale rating, the entry shows the lower level and keeps the finder's wording in brackets, for
example "low (medium-low)". "Latent" means the defect does not fire on the shipped example or in
the published runs.

## Addressed by

Each entry gets an "Addressed by" line once something has been decided or done about it. An entry
without one has not been dispositioned yet. The line is a status word, the references that status
requires, and an optional note:

```
Addressed by: <status>; <reference>; …; note: <free text>
```

| status | required references |
|---|---|
| `fixed` | `commits <sha>, …`; a test marked with the ID that passes; optionally `PR #n` |
| `fixed in docs` | `commits <sha>, …`, touching a documentation file; optionally `PR #n` |
| `partly fixed` | `commits <sha>, …`; and a strict-xfail test marked with the ID for what remains, or `open: DEC-n` / `open: issue #n` |
| `open` | `DEC-n` or `issue #n`; and a strict-xfail test marked with the ID, if the finding can be tested |
| `deferred` | `reason: v1.4`, `reason: needs-design` or `reason: out-of-scope`; optionally `issue #n` |
| `not a defect` | `reason: info`, `reason: withdrawn` or `reason: duplicate-of <ID>`, where the ID is in this register |

For example: `Addressed by: fixed; commits 1a2b3c4; PR #12; note: …`. The references are what a
test can check offline: that each commit exists in the history, that a DEC-n or ID exists in this
register, and that every ID has either a `finding` mark on a test or a status that says why it has
none. Whether the note makes sense stays a matter for review.

## Finding the tests for a finding

Tests carry a pytest mark, which can name several IDs (`finding('T3-43', 'T3-1')`), so

```
git grep -n -E "finding\([^)]*'T3-1'"
```

lists every test pinned to `T3-1`. Regression scenarios carry the ID in their name
(`t3_38_unknown_tool`), so `git grep -n -i "t3_38"` finds those. Commit messages cite IDs too:
`git log --oneline -E --grep "T3-1([^0-9]|$)"`.

## Terms used below

- **Live path:** what `smoke_test.py` runs to produce a published report, as opposed to functions
  that only the test suites call.
- **Published runs:** the run directories under `output/` (`run_a_mini`, `run_b_sol`, `run_e_mini`,
  `run_f_sol`).
- **Steps 1–5** of D7.2(a) operand resolution are the ladder in `provenance.py`: 1 source match or
  declared constant (1b a constant's magnitude), 2 transformed source, 3 reference intermediate (3b
  under a permitted transformation), 4 a prior return computed in the session, 5 originated, with
  sign-inversion detection.
- **Grounded, originated, released figure, release coverage.** An operand is *grounded* when
  steps 1–4 resolve it and *originated* when none does. The *released figure* is the number figure
  identification (SPEC R2.0) takes as the response's answer. *Release coverage* asks whether that
  figure equals a tool return (FINDINGS_ERRATA.md E7).
- **Section numbers** always name their document: "report §5" is a section of the generated
  `report.md` (§1 pre-registration record … §12 unmeasured dimensions, §13 declared limitations),
  "SPEC §10" a section of SPEC.md, and "AP-1 v1.3 §6.8" (or "AP-1 §5" where both versions agree) a
  clause of the standard.
- **R-numbers** (R0.1 … R4.2) are SPEC.md requirements, written "SPEC R2.4". **D1–D7** are AP-1
  dimensions and D7.1–D7.9 their sub-clauses; **EV-0 … EV-3** are the evidence classes of SPEC
  R1.3. Upper-case hyphenated words (OPERANDS-GROUNDED, AUTO-MATCH, …) are outcome labels the code
  emits.
- **Mutant:** a deliberate small change to the code. "The mutant passes" means every suite stayed
  green with the change in place when the review ran it at `77514b4`, so no test detects the
  defect it simulates.

---

## T3: review of `main` at `77514b4`

92 findings: 2 critical, 13 high, 1 disputed between high and medium, 40 medium, 24 low, 12 info.
Grouped by severity, in ID order.

### Critical

**T3-1 · critical · EV-0 executions are counted as successful invocations in the D7.1 rate and its bound**
- What's wrong: an unrecognised response shape, or an adapter failure on any request after the
  first, gives evidence class EV-0 with outcome `None`, and the summary counts that execution in
  `n` as a success; only NOT-INVOKED counts as a failure. An endpoint the runner can never read
  prints `| 0 | 50 | 50/50 | 0.058155 (5.8155%) |`. Report §5 has no evidence-class column;
  `invocation.measure_invocation` has a per-class split but is never called live, and it too keeps
  unobservable records in n (S3-G7-1).
- Where: `smoke_test.py:216-233` (`_build_summary`); `report.py:318-335` (report §5);
  `evidence.py:93-106`; `smoke_test.py:161-192` (consistency check ignores `None`)
- After the reorg: `src/ap1_run/runner/summary.py:116-133` (`build_summary`);
  `src/ap1_run/reporting/report.py:318-335` (`_section_clopper_pearson`);
  `src/ap1_run/execution/evidence.py:93-106` (`classify_invocation`);
  `src/ap1_run/runner/summary.py:12-43` (`verify_invocation_consistency`)
- Breaks: AP-1 v1.3 D7.7, D7.9, D7.5; SPEC R2.3

**T3-2 · critical · Leading whitespace in a calculator expression makes D7.2(a) vacuously grounded, and step 4 then launders the return**
- What's wrong: the expression is parsed unstripped, so `" 1520 * 0.01"` raises `IndentationError`,
  which `extract_operands` catches as a `SyntaxError` and returns no operands (the calculator itself
  strips the expression and returns a normal result), and the invocation is OPERANDS-GROUNDED. With
  fabricated operands that happen to give the right value, every D7 sub-dimension is clean, and the
  fabricated return then grounds later calls (`[' 7777 * 3', '23331 * 1.2 / 12']` gives GROUNDED,
  GROUNDED instead of ORIGINATED, ORIGINATED). Any accepted expression with no numeric literals is
  grounded the same way. None of the 5,639 calculator expressions in the published runs has leading
  whitespace, so the published figures are unaffected.
- Where: `provenance.py:62-65`; `provenance_classify.py:76-79`, `:223-229`
- After the reorg: `src/ap1_run/scoring/provenance/trace.py:62-65` (`extract_operands`);
  `src/ap1_run/scoring/provenance/classify.py:76-79` (`classify_invocation`), `:223-229`
  (`classify_invocations_sequential`)
- Breaks: AP-1 v1.3 D7.2(a)(iv) ("fails closed at the first unresolved link") and D7.2(a) ("the
  unobservable case is declared, never silently skipped"); SPEC R2.4

### High

**T3-3 · high · On the live path, D1 auto-scored accuracy is structurally 1, and a wrong final answer can score CORRECT**
- What's wrong: on the free-text path the runner uses (it passes no structured answer field,
  T3-75), AUTO-MATCH requires exactly one token within tolerance; any wrong figure routes to
  adjudication, whose results the runner never reads back, so `correct/(correct+incorrect)` is 1
  whenever it is defined and report §3 prints "D1 | Measured | Accuracy: 1". `figure_id` also
  takes the one token matching the expected value as the released figure whatever the response
  concludes, so `"… gives 15.20 a year? No: answer is $182.40."` is AUTO-MATCH / CORRECT. On this
  path INCORRECT is reachable only at the exact tolerance boundary (see T3-27); the unused
  structured-answer path can score INCORRECT. The token-selection rule is SPEC R2.0 step 4's, so
  changing it needs a SPEC change.
- Where: `figure_id.py:142-176` (structured path `:80-92`); `accuracy.py:80-102`, `:129-132`;
  `report.py:427-430`, `:736-737`
- After the reorg: `src/ap1_run/scoring/figure_id.py:142-176`, `:80-92` (`identify_figure`);
  `src/ap1_run/scoring/accuracy.py:80-102` (`score_accuracy`), `:129-132` (`summarise_accuracy`);
  `src/ap1_run/reporting/report.py:427-430` (`_section_scoring_proportions`), `:736-737`
  (`_format_dim_result`)
- Breaks: AP-1 v1.3 D1; SPEC R2.1

**T3-4 · high · D2 is reported "Measured", but the per-surface D2 results never reach the report**
- What's wrong: `d2_results` is keyed `"Q01/base"` while the report reads `d2['surfaces']`, which is
  never present, so every published report prints `D2 | Measured | N/A` and "No per-surface D2 data
  available" (only the D2.2 cap reason reaches report §9); a test fixture uses the report's shape,
  so the suite stays green. The live caller passes no operator declaration, so it can report only
  OBSERVED-ONLY or UNMEASURED, never CONFIGURED or STRUCTURAL; that both identical and differing
  figures classify OBSERVED-ONLY is SPEC's rule (the runner cannot establish the other two classes
  from outside, `SPEC.md:514-517`), and the distinct-value count records the difference. The
  "figures" surface is the whole message text when there are no tool calls, and the minimum is the
  configured repeat count.
- Where: `smoke_test.py:954-968` (`operator_declared=None` at `:962`); `report.py:478-497`,
  `:162-167`; `reproducibility.py:70-101`, `:166-189`
- After the reorg: `src/ap1_run/runner/summary.py:77-91`, `:85` (`classify_reproducibility`);
  `src/ap1_run/reporting/report.py:478-497` (`_section_d2_mechanisms`), `:162-167`
  (`_section_dimension_results`); `src/ap1_run/scoring/reproducibility.py:70-101`
  (`classify_mechanism`), `:166-189` (`_extract_surface_values`)
- Breaks: AP-1 v1.3 D2 Method, D2.1, D2.2; SPEC R2.2, R3.3

**T3-6 · high · A pass-through calculator call that echoes the answer gets a fully clean D7 signature**
- What's wrong: on Q01, `calculator("15.20")`, `"15.2 * 1"` or `"15.2 + 0"` scores INVOKED,
  OPERANDS-GROUNDED, OPERATION-CORRECT, GOVERNED-RELEASE and TRANSCRIBED-EXACT, the signature of a
  computed figure for one no computation produced (1 is a structural constant; 0 matches
  `savings.monthly_fee` "0.00"). It grounds mainly because the example ground truth lists the final
  value as an intermediate, even on single-step Q01. None of the 190 single-literal calls (one
  numeric literal in the expression) in the published runs echoes the final answer. Rated high,
  not critical: the provenance check runs and fails closed; the rule it applies, step 3's match to
  a reference intermediate, is too permissive.
- Where: `provenance.py:193-212`; `example/ground_truth_example.py:68-84`;
  `operation_correctness.py:149-156`; `release_coverage.py:130-143`
- After the reorg: `src/ap1_run/scoring/provenance/trace.py:193-212` (`resolve_operand`);
  `example/ground_truth_example.py:68-84` (`derive_q01`);
  `src/ap1_run/scoring/operation_correctness.py:149-156` (`classify_operation`);
  `src/ap1_run/scoring/release_coverage.py:130-143` (`check_release_coverage`)
- Breaks: AP-1 v1.3 §3.2 link 2, §3.2.1, D7.2 ("Why a membership check is insufficient"), D7.2(b)

**T3-7 · high · The seal-time ground-truth guards are never called live, and pass vacuously when called**
- What's wrong: `perturbation_check`, `source_fields_check` and `declared_constants_check` are called
  only from test suites, never from `seal()`, `smoke_test.py`, `engine.py` or the Inspect task, so a
  live run seals and scores any ground-truth module, including one returning literals. When called,
  `perturbation_check` loops only over the declared `source_fields_consumed`, so a module returning
  `Decimal('42')` passes if it declares no fields, a field that does not exist, a field with no dot
  or a non-numeric field, or returns `final: None`. The shipped module declares real fields on all
  10 items, so the published runs are unaffected.
- Where: `seal.py:124-225` (`perturbation_check`; silent `continue`s at `:170-171`, `:177`,
  `:183-187`, `:195-196`), `seal.py:228-282` (`source_fields_check`), `seal_constants.py:16`
- After the reorg: `src/ap1_run/execution/seal.py:124-225`, `:170-171`, `:177`, `:183-187`,
  `:195-196` (`perturbation_check`), `:228-282` (`source_fields_check`);
  `src/ap1_run/execution/seal_constants.py:16` (`declared_constants_check`)
- Breaks: SPEC R3.1 ("A constant-returning module is refused, perturbation named") and the SPEC §10
  rows for AP-1 v1.3 §11.9, §13.4, §13.5 marked IMPLEMENTED; README ("the run is refused")

**T3-8 · high (critical once the guards are wired) · `source_fields_check` misses undeclared reads made other than by subscript**
- What's wrong: `TrackingAccount` overrides only `__getitem__`, so reads through `.get()`,
  `.items()`, `.values()`, `.copy()`, `dict()` or `{**a}` go unrecorded; a module that declares
  `savings.balance` and reads `savings.annual_rate` that way passes both guards. Latent: the guards
  have no live caller (T3-7) and the example module uses subscripts throughout.
- Where: `context.py:111-121`; used by `seal.py:228-282`
- After the reorg: `src/ap1_run/execution/context.py:111-121` (`TrackingAccount`);
  `src/ap1_run/execution/seal.py:228-282` (`source_fields_check`)
- Breaks: `source_fields_check`'s own contract (`seal.py:232-233`: "A module reading a field NOT
  in source_fields_consumed is refused, with the field named"); SPEC R3.1

**T3-9 · high · Figure outcomes are joined to transcript records by position, so after a first-request failure the adjudication sheets show the wrong responses**
- What's wrong: a first-request transport failure writes a transcript record but no figure record,
  and no record carries a repeat index, so `figs.pop(0)` gives each later record the next repeat's
  outcome. A response then appears under another repeat's routing reason, the response that needed a
  human appears on no sheet, and a "[no response received]" record can get a sheet. Console and
  `smoke_summary.json` are unaffected, so the artifacts disagree silently. The published runs have
  no transport failures.
- Where: `smoke_test.py:1030-1048`; `engine.py:78-93`; `adjudication.py:145-154`
- After the reorg: `src/ap1_run/runner/outputs.py:23-40` (`attach_figure_outcomes`);
  `src/ap1_run/execution/engine.py:78-93` (`execute_item`);
  `src/ap1_run/reporting/adjudication.py:145-154` (`_needs_adjudication`)
- Breaks: SPEC R3.2; AP-1 v1.3 §13.1, §13.8

**T3-10 · high · An empty response is scored EXECUTED / NOT-INVOKED and enters the D7.1 denominator as a failure**
- What's wrong: `content: ''` with no tool calls classifies EV-2 NOT-INVOKED, a false
  non-invocation against the system (10 empty responses give `0/10`). Reasoning models can return
  empty content when they hit `max_completion_tokens`. The scoring-proportion count also lumps it
  with adjudicated responses. Under AP-1 v1.2, which has no empty-response rule, this is medium.
- Where: `engine.py:94-108`; `smoke_test.py:218-231`, `:261-264`
- After the reorg: `src/ap1_run/execution/engine.py:94-108` (`execute_item`);
  `src/ap1_run/runner/summary.py:118-131`, `:161-164` (`build_summary`)
- Breaks: AP-1 v1.3 §13.2 ("An empty … response shall never be counted as an answer"); SPEC R0.2;
  SPEC R4.1 row "Empty response → UNMEASURED"

**T3-11 · high · The D7.1 bound pools 50 repeats of 10 questions as n = 500**
- What's wrong: the headline `0/500 → 0.597 %` treats repeats as independent items, and states no
  sampling unit. The same zero gives 5.82 % per item over 50 repeats, and 25.89 % with the question
  as the unit (n = 10); these are different analyses, but the pooled bound is about 10× to 43×
  narrower than either, in the optimistic direction. Under AP-1 v1.2, which has no D7 bound, this
  is medium.
- Where: `smoke_test.py:218-231`; SPEC R2.3 (`SPEC.md:540`, n undefined); report §5
- After the reorg: `src/ap1_run/runner/summary.py:118-131` (`build_summary`)
- Breaks: AP-1 v1.3 D7.1 ("proportion of computable *questions*"), D7.5; the same point is comment
  GH-5 in the AP-1 v1.3 disposition record (`DISPOSITION_RECORD_v1.3.md`, admissibility-protocol
  repository), accepted for v1.4

**T3-12 · high · Minimum-n is never enforced live, and the validator miscounts where it is called**
- What's wrong: `validate_minimum_n` is called only by tests, so every report shows D1 "Measured"
  over 10 items in 6 categories, below the D1 minimum of 40. Where it is called, unknown dimensions
  are skipped (`dimensions_claimed: ['D99']` loads), D5 and D6 count every question (20 ordinary
  questions satisfy a D5+D6 claim), and no D1 total of 40 is checked.
- Where: `config.py:224-257` (`:234-235` skip, `:253` count)
- After the reorg: `src/ap1_run/foundation/config.py:224-257`, `:234-235`, `:253`
  (`validate_minimum_n`)
- Breaks: SPEC R0.1 and the SPEC §9 threat "Under-powered claim reported as a result"; AP-1 D1, D5, D6
  minimums; README ("enforces the minimum-item counts for D5 and D6 at load")

**T3-13 · high · AP-1 v1.3 §6.8 outcomes are marked IMPLEMENTED, but no code assigns them, and the sheets omit the D7.2(a) result**
- What's wrong: auto-scored responses get CORRECT / INCORRECT / NO-FIGURE, never an AP-1 §6.8
  outcome (COMPUTED, RETRIEVED, WRONG-SCOPE and the others occur only in sheet rubric text). A
  correct figure built on originated operands has no answer-level ORIGINATED anywhere, and
  adjudicators cannot apply the composition rule because the sheet shows operation correctness but
  not D7.2(a). AP-1 §6.8 exists only in v1.3, so this is not a defect against AP-1 v1.2; the false
  IMPLEMENTED rows in SPEC §10 remain a SPEC finding.
- Where: `SPEC.md:891-892`; `adjudication.py:217-223`; `verify_conformance.py:466-497`
- After the reorg: `src/ap1_run/reporting/adjudication.py:217-223` (`_generate_one_sheet`);
  `tests/legacy/verify_conformance.py:466-497` (`test_6_8_six_outcome_vocabulary`)
- Breaks: AP-1 v1.3 §6.8 and its composition rule; SPEC §10

**T3-14 · high · FINDINGS.md finding F7's "0/468 (p_upper < 0.0064)" bounds a count that can never be non-zero, and the related claim in the publisher's comment is false**
- What's wrong: `generate_findings.py` counts `fig == "AUTO-MISMATCH"`, an outcome that does not
  exist, and an auto-scored item cannot be wrong anyway (T3-3), so the bound measures a tautology;
  468 is exactly the AUTO-MATCH population, and the trials are tool calls, not independent items.
  The publisher's comment says "Across two systems and 973 WRONG-OPERATION calls, zero produced an
  incorrect released figure", but Run A has 9 Q05 executions (10 calls) that release $2375 instead
  of $2411. The AP-1 v1.3 disposition record (`DISPOSITION_RECORD_v1.3.md:117` in the
  admissibility-protocol repository) says "among auto-scored items" but keeps "973", which is
  either self-contradictory (547 were auto-scored) or vacuous.
- Where: `generate_findings.py:144`, `:348`; `FINDINGS.md:356-362`;
  `docs/AP-1_v1.3_PUBLISHERS_COMMENT.md:92`
- After the reorg: `tools/generate_findings.py:150` (`compute_figures.run_core`), `:354`
  (`compute_figures`)
- Breaks: AP-1 v1.3 D7.5, §6.5

**T3-16 · high · OPERANDS-UNOBSERVABLE is never emitted live; malformed calls count as INVOKED and vanish from D7.2**
- What's wrong: a call whose arguments are not JSON, or are wrongly keyed (`{"expr": …}`), counts as
  INVOKED in D7.1 but is skipped by `continue` in D7.2(a) and dropped from D7.2(b) instead of
  scoring OPERATION-UNOBSERVABLE (which the engine does emit for expressions it can extract but not
  evaluate), and no unobservable proportion is reported; unparseable expressions are scored
  grounded (T3-2). Changing that `continue` to `break` survives the tests, so one malformed call
  could drop every later invocation unnoticed. Does not occur in the published runs. Rated high
  because the case reproduces end to end: the calculator errors, the model states the figure
  itself, and the call is reported invoked. Not critical: the tool was in fact called, so INVOKED
  is right for D7.1, and D7.2 drops the call rather than scoring it grounded. The defect is a
  missing unobservable count, not an unobservable case reported as a success.
- Where: `provenance_classify.py:213-216`, `:76-79`, `:111-117` (`classify_item`, no live caller);
  `engine.py:122-135`; `report.py:688-690`
- After the reorg: `src/ap1_run/scoring/provenance/classify.py:213-216`
  (`classify_invocations_sequential`), `:76-79` (`classify_invocation`), `:111-117`
  (`classify_item`); `src/ap1_run/execution/engine.py:122-135` (`execute_item`);
  `src/ap1_run/reporting/report.py:688-690` (`_section_operand_provenance`)
- Breaks: AP-1 v1.3 D7.2(a) ("never silently skipped, and its proportion reported"), D7.2(b)
  OPERATION-UNOBSERVABLE; AP-1 v1.2 7.1; SPEC R2.4

**T3-52 · high · Intermediate rounds of the tool loop are overwritten, and the SPEC R0.2/R0.3 transport and transcript contracts have no tests**
- What's wrong: intermediate rounds are overwritten (KNOWN_ISSUES #7), which is the lost-response
  defect V12-3 describes, judged here against SPEC; that is why it is rated high like V12-3. None of
  egress to a single host, a read-only scorer, an interrupted run, an unmodified response, or every
  round recorded is demonstrated by a test, and the single-host egress claim rests on a library
  default that follows redirects.
- Where: `adapter.py:11`; `engine.py:172-236` (`_drive_tool_loop`)
- After the reorg: `src/ap1_run/foundation/adapter.py:11` (module docstring);
  `src/ap1_run/execution/engine.py:172-236` (`_drive_tool_loop`)
- Breaks: SPEC R0.2, R0.3 verification contracts; AP-1 v1.3 §5.6

### Disputed (high or medium)

**T3-17 · medium / high (disputed) · `verify_seal()` is never called, checks only part of the record, and its refusal path is untested**
- What's wrong: nothing calls `verify_seal` before or during scoring (the separate offline check
  is `verify_run_seal.py`, T3-18), and the docstring "The scorer calls this before processing" is
  false. If called, `verify_seal` ignores `seal_hash`, `runner_source_hash`, `verification_keys`,
  `ev3_implemented` and `ap1_version`, skips the DOI check when either side is blank, and compares
  the AP-1 text only when the caller passes its path (`:97-100`). (`seal()` itself accepts
  `'placeholder'`, T3-68.) Mutants that make it never raise, or disable its checks, pass the
  suites. It does refuse a changed file when called. Against high: no concrete wrong result can be
  built today, because inputs are loaded before sealing and there is no second-process scorer (the
  real window is T3-72).
- Where: `seal.py:79-119` (`:97-100`, `:105`, docstring `:83`); only caller `verify.py:366-374`
- After the reorg: `src/ap1_run/execution/seal.py:79-119`, `:97-100`, `:105`, `:83` (`verify_seal`);
  `tests/legacy/verify.py:365-373` (`test_r11_seal`)
- Breaks: SPEC R1.1 verification contract ("Modifying any sealed input causes the scorer to refuse,
  naming the mismatch"); SPEC §9 threat "Fixture altered after sealing"

### Medium

**T3-5 · medium · Undocumented step 1b `constant_magnitude` grounds sign-inverted values that coincide with any declared constant**
- Settled by DEC-4 (see "Maintainer decisions" at the end).
- What's wrong: step 1b grounds `-x` whenever `x` is a declared constant, before step 2 and before
  the step-5 SIGN-INVERSION check, and overrides the step-4 transitivity guard. On Q09 `-12` grounds
  only because 12 is also the months constant, `-1` grounds on every item through the structural
  constant 1, and `-100`, `-3` and `-4` ground the same way; matched to a source field, the same
  value would be ORIGINATED with a SIGN-INVERSION finding. The rule is in the published figures:
  `run_e_mini` has 73 `constant_magnitude` resolutions, all on Q09 (`-12` ×42, `-12.0` ×30, `-1` ×1),
  all stored GROUNDED; `run_f_sol` has none. Those 73 are the Q09 checking fee written as `-12` or
  `15.2 + (-12)`, which are the right inputs, so `run_e_mini`'s published "5 originated" is not
  inflated; what remains is an undocumented rule that grounds by coincidence.
- Where: `provenance.py:153-168` (added in `ff8c051`); step 5 at `provenance.py:300-320`
- After the reorg: `src/ap1_run/scoring/provenance/trace.py:153-168`, `:300-320` (`resolve_operand`)
- Breaks: AP-1 v1.3 D7.2(a)(i)–(ii) (transformations declared in advance; negation is not among
  `permitted_transformations`); SPEC R2.4 steps 1–2

**T3-15 · medium (a test gap) · The suites never check what `seal_hash` covers**
- What's wrong: the only assertion on `seal_hash` is its length, so a `seal_hash` over the
  timestamp alone, over `None` or over `{}` leaves every suite green, and fields such as
  `ap1_version`, `runner_version_*`, `runner_source_hash` and `verification_keys` can be dropped
  unseen. The code is correct today, so this is rated like the other test gaps.
- Where: `seal.py:70-74`; `verify.py:342-344`
- After the reorg: `src/ap1_run/execution/seal.py:70-74` (`seal`); `tests/legacy/verify.py:341-343`
  (`test_r11_seal`)
- Breaks: SPEC R1.1; AP-1 v1.3 §5.3

**T3-18 · medium (high arguable) · `verify_run_seal.py` reports PASS when the transcript is missing, compares only line 1, and counts non-checks as passes**
- What's wrong: with no transcript it prints `transcript … not found (skipped)` and then
  `RESULT: PASS (11 checks)`; lines 2..N can carry any `seal_hash`, so spliced or misfiled
  transcripts verify. "11/11" is 6 hash comparisons, 1 transcript-line comparison and 4
  non-comparisons. The script is not in `run_all_tests.py` `SUITES` and has 0 % coverage.
- Where: `verify_run_seal.py:218-235` (`:221-222` reads line 1 only), `:270` (`n_passed =
  len(checks)`)
- After the reorg: `tools/verify_run_seal.py:221-238`, `:224-225` (`verify_run`), `:273` (`main`)
- Breaks: SPEC R1.1 ("The record's hash appears on every transcript line"); README seal-verification
  section

**T3-19 · medium · `runner_source_hash` is never verified, and the verifier is silent about `runner_modified: true`**
- What's wrong: the only instrument-provenance field is computed and sealed but no tool recomputes
  it, so it can be replaced and the composite recomputed. `run_e_mini` and `run_f_sol` seal
  `runner_source_hash da0739eb…` with `"runner_modified": true` (their `report.md:25`, `:68`), and
  `verify_run_seal.py` mentions neither field. The hash supports the manual comparison against a
  published release that `version.py:7-12` describes (those runs' `CLARIFICATION.txt` names the
  tag that reproduces it), but no tool performs it. The README speaks of "five component hashes";
  a sixth is sealed and never compared.
- Where: `version.py:84-109`; `seal.py:47`; `README.md:385-386`
- After the reorg: `src/ap1_run/execution/version.py:84-109` (`compute_runner_source_hash`);
  `src/ap1_run/execution/seal.py:47` (`seal`)
- Breaks: `version.py`'s own claim ("so that a modified instrument is detectable"), which holds only
  out of band; AP-1 v1.3 §13.11 requires disclosure only

**T3-20 · medium · The cross-platform hash CI compares nothing, nothing pins the canonical-JSON format, and the "no float" static check does not exist**
- What's wrong: each OS job runs `verify_hashes.py`, which overwrites the tracked
  `hash_digest.txt`; nothing compares the digests, despite the docstring. A change of separators or
  `ensure_ascii` passes all suites and CI. The test never hashes checked-out files, which is where
  the real CRLF failure happened (T3-50). The "static check" is only a runtime refusal inside
  `canonical_json`.
- Where: `.github/workflows/hashes.yml` (three platforms); `verify_hashes.py:3-5`, `:43-48`;
  `numeric.py:286-287`; `operation_correctness.py:40-41`, `:61`
- After the reorg: `tests/legacy/verify_hashes.py:1-7` (module docstring), `:52-57` (`main`);
  `src/ap1_run/foundation/numeric.py:286-287` (`canonical_json`);
  `src/ap1_run/scoring/operation_correctness.py:40-41` (`_ALLOWED_NAMES`), `:61` (`_eval_decimal`)
- Breaks: SPEC R0.4.3 verification items 1 and 2; SPEC Phase A exit criterion (`SPEC.md:794`)

**T3-21 · medium · The two-pass architecture SPEC calls a conformance requirement is not realised**
- What's wrong: D7.2(a)/(b) are computed before the transcript write and stored in the record, the
  scorer appends `figure_identification` records to `run.jsonl`, and no standalone re-scorer
  exists, so a defective scorer cannot be re-run over a burned set without re-running the model.
  For the D7 evidence class this is impossible, because round shapes and intermediate rounds are not
  recorded.
- Where: `engine.py:118-160`; `smoke_test.py:612-642`
- After the reorg: `src/ap1_run/execution/engine.py:118-160` (`execute_item`);
  `src/ap1_run/runner/executions.py:72-99` (`score_execution`)
- Breaks: SPEC §2 ("The separation is a conformance requirement"), SPEC §5, R0.2, R0.3 ("opens the
  transcript read-only"); SPEC §10 rows for AP-1 v1.3 §13.1, §13.10

**T3-22 · medium · The R4.1 "mock endpoint with planted defects" is a unit-test catalogue that bypasses the live path**
- What's wrong: `verify_r41.py` B01–B30 call units directly (its docstring says 33 checks; it runs
  30). Only `verify_integration.py` drives the engine against an HTTP mock, and its scenarios
  (laundering through step 4, an unrecognised later round) touch only a few R4.1 rows. B15/B16
  call `identify_figure` directly and so miss the engine's own handling of empty responses and
  rate limits (T3-10, T3-65); B22, B23 and B24 test units the live path never calls. That is how
  T3-2, T3-4, T3-7, T3-10 and T3-12 coexist with a green suite. B01 omits its RETRIEVED half, the
  R4.1 table lags the tests, and the EV-3 row is listed as required although EV-3 is declared
  unimplemented.
- Where: `verify_r41.py`; `evidence.py:146-153`
- After the reorg: `tests/legacy/verify_r41.py`; `src/ap1_run/execution/evidence.py:146-153`
  (`classify_attestation`)
- Breaks: SPEC R4.1 ("Every planted defect is detected with the specified outcome, offline")

**T3-23 · medium · Inter-rater agreement is specified and claimed, but nothing implements it**
- What the report must say is settled by DEC-3 (see "Maintainer decisions" at the end).
- What's wrong: SPEC R3.3 specifies raw agreement and Cohen's κ and the Phase E gate claims it, but
  SPEC also marks it "NOT BUILT by design", no `.py` computes κ, and nothing reads scorer marks back,
  so the 18–31 % of executions per published run that are routed to adjudication never become
  measured outcomes.
- Where: `SPEC.md:729-734`, `:798`, `:890`; `verify_phase_e.py:10`; `adjudication.py:236`
- After the reorg: `tests/legacy/verify_phase_e.py:10` (module docstring);
  `src/ap1_run/reporting/adjudication.py:236` (`_generate_one_sheet`)
- Breaks: AP-1 v1.3 §6.6.1, §13.8; SPEC internal consistency

**T3-24 · medium · The live report §6 originated-operand listing is untested and can be emptied with every suite green**
- What's wrong: the mutant `prov.get('originated_operands')` → `prov.get('XX')` makes report §6
  print "No originated operands detected" and passes `run_all_tests.py`.
- Where: `smoke_test.py:300-330` (`:315`)
- After the reorg: `src/ap1_run/runner/summary.py:200-230`, `:215` (`build_summary`)
- Breaks: SPEC R2.4, R3.3 (originated-operand listing)

**T3-25 · medium · D7.2(a)(iii) step 3b (intermediate under a permitted transformation) is never exercised**
- What's wrong: step 3b can be switched off, `fraction_to_percent` can divide instead of multiply,
  `abs_value` can return None, and step numbers can be misreported, all with green suites.
  `transformed_intermediate` and `fraction_to_percent` never occur in the published runs.
- Where: `provenance.py:214-228` (`:219`); `TRANSFORMATIONS` at `provenance.py:38-42`
- After the reorg: `src/ap1_run/scoring/provenance/trace.py:214-228`, `:219` (`resolve_operand`),
  `:38-42` (`TRANSFORMATIONS`)
- Breaks: AP-1 v1.3 D7.2(a)(ii)/(iii); SPEC R2.4

**T3-26 · medium · D7.3 transcription compares the last return of any tool, and the production wiring is untested**
- What's wrong: the live path takes the last call with a non-empty return, whatever the function
  name, and stops even on an error return. A correct release of an earlier return is labelled
  TRANSCRIBED-ALTERED while coverage says GOVERNED-RELEASE, and if the last call errored the
  execution is UNOBSERVABLE even when an earlier return matches. The D7.3 wiring is copied in
  `smoke_test.py`, `verify_inspect.py` (which, unlike the live copy, takes the last *calculator*
  return) and, for release coverage only, `ap1_inspect/scorer.py`; no test exercises the live copy.
  FINDINGS_ERRATA.md N1 says "last calculator return"; the code takes the last return of any tool.
- Where: `smoke_test.py:644-674` (untested `:644-708`); `verify_inspect.py:430-447`;
  `ap1_inspect/scorer.py:119-143`
- After the reorg: `src/ap1_run/runner/executions.py:101-131`, `:101-165` (`score_execution`);
  `tests/legacy/verify_inspect.py:431-448` (`_classify`); `ap1_inspect/scorer.py:119-143`
  (`ap1_scorer.score`)
- Breaks: AP-1 v1.3 D7.3; SPEC R2.5

**T3-27 · medium · Default HALF_EVEN quantisation in `transcription.py` and `accuracy.py` contradicts the declared HALF_UP policy**
- What's wrong: `.quantize` is called with no `rounding=`, so a tool return of 430.745 released as
  430.74 is EXACT and as 430.75 (correct HALF_UP) is ALTERED, and the two D7.3 sub-checks disagree
  at the boundary. In `accuracy.py` a within-tolerance match at the boundary scores INCORRECT
  (`2.005` vs `2.015`, tolerance 0.01). `release_coverage.py` uses the declared mode. KNOWN_ISSUES
  #6 names only the calculator and `operation_correctness.py`.
- Where: `transcription.py:81-85`; `accuracy.py:82-87`; compare `release_coverage.py:127-128`
- After the reorg: `src/ap1_run/scoring/transcription.py:81-85` (`check_transcription`);
  `src/ap1_run/scoring/accuracy.py:82-87` (`score_accuracy`);
  `src/ap1_run/scoring/release_coverage.py:127-128` (`check_release_coverage._q`)
- Breaks: AP-1 v1.3 D7.3 ("rounding not licensed by the declared quantisation policy"), AP-1 v1.3
  §6.9; SPEC R0.4.1

**T3-28 · medium · The D7.3 checks now run live, with residual gaps**
- What's wrong: `check_transcription` and `check_release_coverage` now run live (`ff8c051`,
  `5dc6155`); the adjudication sheets show the release-coverage finding but no transcription
  result. Residual gaps: (1) last-return selection (T3-26); (2) the D7.3-unobservable population is
  not declared in report §12 (T3-29); (3) a wrong ungoverned figure is invisible to coverage,
  and Q04-style answers still count D1 CORRECT and OPERATION-CORRECT; (4) the R4.1 table was not
  extended for B31–B37; (5) the Inspect path does not call `check_transcription`, although the
  `ff8c051` message says "wired into all 3 scoring paths"; (6) sheets mix findings from all repeats
  (T3-37).
- Where: `smoke_test.py:641-708`; `release_coverage.py`; `adjudication.py:246-258`;
  `ap1_inspect/scorer.py`
- After the reorg: `src/ap1_run/runner/executions.py:98-165` (`score_execution`);
  `src/ap1_run/scoring/release_coverage.py`; `src/ap1_run/reporting/adjudication.py:246-258`
  (`_generate_one_sheet`); `ap1_inspect/scorer.py`
- Breaks: AP-1 v1.3 D7.3, AP-1 v1.3 §3.2.1 link 4; SPEC R2.5, R4.1

**T3-29 · medium · The report says "D7 Measured", but D7.4 is not measured, the unmeasured part of D7.3 is not declared, and D7.2/D7.3 tables carry no evidence class**
- What's wrong: `run_e_mini/report.md` reads `| D7 | Measured | 1000 |`, yet no
  invocation-under-pressure measurement exists, and report §12 declares only unclaimed dimensions.
  SPEC §1.1 lists D7.1–D7.3 honestly; the generated report does not.
- Where: `report.py:153-175`, `:580-605`, `:214-297`, `:625-708`
- After the reorg: `src/ap1_run/reporting/report.py:153-175` (`_section_dimension_results`),
  `:580-605` (`_section_unmeasured_dimensions`), `:214-297` (`_section_d73`), `:625-708`
  (`_section_operand_provenance`)
- Breaks: AP-1 v1.3 D7 ("Report all four"), D7.7

**T3-30 · medium · SPEC omits AP-1 v1.3 obligations the instrument could at least declare, and SPEC §10 marks several IMPLEMENTED**
- What's wrong: D7.4, the AP-1 §6.2 headline claim and the §6.4 discretionary-correctness
  disclosure are absent; AP-1 §2.5 (partial result naming links cleared) is marked IMPLEMENTED with
  no report section; the D1 40-item minimum and per-category CIs, and the D2 10×50 minimum, are
  absent; the D2.2 serving-stack disclosure is marked IMPLEMENTED; the seal records no Python,
  library or platform (AP-1 §1.5.1).
- Where: SPEC §1.1, R2.1, R2.2, R3.3, SPEC §10
- Breaks: AP-1 v1.3 D7.4, §6.2, §6.4, §2.5, §3.2.1, D1 Method, D2 Method, D2.2, §1.5.1

**T3-31 · medium · The executable conformance device checks constants and two table rows, not the IMPLEMENTED claims**
- What's wrong: `verify_conformance.py` asserts `MINIMUM_N` constants, its AP-1 §6.8 test is
  vacuous, and its consistency test checks 2 rows and guards only against under-claiming, so a
  clause can be marked IMPLEMENTED with unreachable code (minimum-n, AP-1 §13.1/§13.10, D2.2, §6.8
  composition).
- Where: `verify_conformance.py:129-177`, `:469-499`, `:803-832`
- After the reorg: `tests/legacy/verify_conformance.py:129-177` (`test_d1_accuracy_minimum_n`,
  `test_d5_minimum_20_adversarial`, `test_d6_minimum_10_taxonomy`), `:469-499`
  (`test_6_8_six_outcome_vocabulary`), `:803-832` (`test_conformance_table_consistency`)
- Breaks: SPEC §10 ("normative")

**T3-32 · medium · D1 is not reported per category or with a 95 % CI, yet SPEC lists D1 as IMPLEMENTED**
- What's wrong: the report gives one pooled rate and no interval.
- Where: `report.py:153-174`, `:729-738`; `accuracy.summarise_accuracy`; `SPEC.md:867`
- After the reorg: `src/ap1_run/reporting/report.py:153-174` (`_section_dimension_results`),
  `:729-738` (`_format_dim_result`); `src/ap1_run/scoring/accuracy.py:105` (`summarise_accuracy`)
- Breaks: AP-1 D1 ("per category, with 95 % confidence intervals, and with n stated"), same in v1.2
  and v1.3

**T3-33 · medium · Report §12 names D3–D6 with dimensions AP-1 does not define, calls D7 "Provenance", and cites the wrong clause**
- What's wrong: the section that declares what was not measured misdescribes the standard (AP-1 has
  D3 Provenance, D4 Refusal integrity, D5 Adversarial resistance, D6 Conflicting input, D7
  Computation invocation), and cites "§6.4" where AP-1 D7.7 is meant. The test asserts only `'D3' in
  report`.
- Where: `report.py:747-756`, `:435`, `:177-185`
- After the reorg: `src/ap1_run/reporting/report.py:747-756` (`_unmeasured_reason`), `:435`
  (`_section_scoring_proportions`), `:177-185` (`_section_d7_figures`)
- Breaks: AP-1 v1.3 §4; SPEC R3.3

**T3-34 · medium · D7.2(a) quantisation and near-miss findings are computed and then dropped**
- What's wrong: `_build_summary` never sets the keys, so report §11 always says "No quantisation
  findings": quantised groundings are counted grounded and never disclosed, and the near-miss
  findings that would explain T3-59 are lost. AP-1 v1.2 does not require these findings; SPEC does.
- Where: `provenance_classify.py:69-74`; `report.py:554-578`
- After the reorg: `src/ap1_run/scoring/provenance/classify.py:69-74` (`classify_invocation`);
  `src/ap1_run/reporting/report.py:554-578` (`_section_quantisation`)
- Breaks: AP-1 v1.3 D7.2(a)(iii) ("records a quantisation finding"), AP-1 v1.3 §6.9; SPEC R2.4, R3.3

**T3-35 · medium · Report §10 "Non-Outcome Cells" does not list every non-outcome cell, and the cause of an EV-0 is never recorded**
- What's wrong: rows are de-duplicated on item/condition/status, so 49 rate-limited repeats become
  one row, and figure-level UNMEASURABLE, transcription UNOBSERVABLE, COVERAGE-UNOBSERVABLE and
  OPERATION-UNOBSERVABLE cells are never listed (`run_e_mini` report §10 has one row while report
  §4b reports 182 transcription UNOBSERVABLE). One transport failure appears three times. A mid-loop
  HTTP failure, a timeout and an unknown shape produce identical records with `error_state: None`
  and no round identified.
- Where: `report.py:503-551`; `engine.py:228-234`, `:141-157`
- After the reorg: `src/ap1_run/reporting/report.py:503-551` (`_section_unmeasured_cells`);
  `src/ap1_run/execution/engine.py:228-234` (`_drive_tool_loop`), `:141-157` (`execute_item`)
- Breaks: SPEC R3.3 ("every UNMEASURED, UNOBSERVABLE, UNMEASURABLE and VOID cell with its reason");
  SPEC R1.3; AP-1 v1.3 D7.9 ("with the round identified")

**T3-36 · medium · Adjudication sheets print arm identity in every header**
- What's wrong: headers read `## Item n: Q02 (Condition: base) — Scorer 1`, so scorers see whether a
  response came from the instructed or the instruction-removed arm, which is the D7.1b contrast
  being measured. AP-1 v1.2 asks only for blindness to the system, which is met.
- Where: `adjudication.py:167-168`
- After the reorg: `src/ap1_run/reporting/adjudication.py:167-168` (`_generate_one_sheet`)
- Breaks: AP-1 v1.3 §13.8 ("blind to arm identity where the response text permits")

**T3-37 · medium · A sheet's Release Coverage Finding lists every repeat of that item and condition**
- What's wrong: coverage results are keyed on `(item_id, condition)` and records carry no repeat
  index, so in a 50-repeat run a sheet can show PARTIALLY-GOVERNED with up to 50 bullets even when
  its own execution was GOVERNED-RELEASE, and the sheet does not say which repeat it is. Same root
  cause as T3-9.
- Where: `adjudication.py:79-83`, `:111-124`, `:246-258`; `engine.py:141-157`
- After the reorg: `src/ap1_run/reporting/adjudication.py:79-83`, `:111-124` (`generate_sheets`),
  `:246-258` (`_generate_one_sheet`); `src/ap1_run/execution/engine.py:141-157` (`execute_item`)
- Breaks: SPEC R3.2

**T3-38 · medium · Calling an unoffered or hallucinated tool trips the FATAL consistency check after all requests are spent, and no report is written**
- What's wrong: a call to a non-required tool (`calc`, `python`) gives NOT-INVOKED with
  `tool_calls_count > 0`, which the consistency check treats as fatal; the run aborts after the last
  request with no `report.md`, sheets or summary, and a previous run's `report.md` stays beside the
  new transcript.
- Where: `evidence.py:119-128`; `smoke_test.py:161-192`, called at `:808`
- After the reorg: `src/ap1_run/execution/evidence.py:119-128` (`classify_invocation`);
  `src/ap1_run/runner/summary.py:12-43` (`verify_invocation_consistency`); `src/ap1_run/run.py:283`
  (`main`)
- Breaks: SPEC R2.3 (NOT-INVOKED is a legitimate outcome)

**T3-39 · medium · Model-controlled input can abort the run through unhandled exceptions in provenance and coverage**
- What's wrong: `{"expression": 15.2}` raises `TypeError`; a boolean literal (`"True * 15.2"`,
  `"True + 1"`) raises `InvalidOperation` in `extract_operands`, because a bool is an `int` there;
  and `1e308*10` makes `quantize` fail on `inf`. Nothing catches them, so the run crashes after
  spent requests with no report.
- Where: `provenance.py:62-65`, `:84-85`; `release_coverage.py:127-132`; `transcription.py:83`;
  `engine.py:118`; `smoke_test.py:694`
- After the reorg: `src/ap1_run/scoring/provenance/trace.py:62-65` (`extract_operands`), `:84-85`
  (`_walk_for_operands`); `src/ap1_run/scoring/release_coverage.py:127-132`
  (`check_release_coverage`); `src/ap1_run/scoring/transcription.py:83` (`check_transcription`);
  `src/ap1_run/execution/engine.py:118` (`execute_item`); `src/ap1_run/runner/executions.py:151`
  (`score_execution`)
- Same family (model or endpoint input ends the run with no report): S3-G2-1, S3-G2-2, S3-G2-4,
  S3-G4-4, S3-G4-5.

**T3-40 · medium · The D7.2(b) evaluator accepts far less than the calculator executes**
- What's wrong: `max`, `sqrt`, `log` and similar score OPERATION-UNOBSERVABLE, so correctness is
  never assessed for the more complex formulae, including the calculator's own self-test loan
  expression. Latent: no such outcome occurs in the published runs.
- Where: `operation_correctness.py:41-49` vs `example/calculator_tool.py:38-45`, `:165` (self-test)
- After the reorg: `src/ap1_run/scoring/operation_correctness.py:41-49` (`_ALLOWED_NAMES`,
  `_ALLOWED_FUNCS`); `example/calculator_tool.py:38-45` (`_ALLOWED_FUNCS`, `_ALLOWED_NAMES`), `:165`
  (`selftest`)
- Breaks: AP-1 v1.3 D7.2(b) ("Where the computation … is recoverable … the assessor evaluates it")

**T3-41 · medium · The configured `decimal_separator` and `grouping_separator` are never used**
- What's wrong: every caller of `extract_numeric_tokens` passes only `currency_symbols`, so a
  European-separator config is sealed but parsed with US separators: `1.006,25` splits into two
  tokens, coverage silently becomes UNOBSERVABLE, and the locale-ambiguity route cannot fire.
- Where: `figure_id.py:132`; `smoke_test.py:684-686`, `:748-749`; `ap1_inspect/scorer.py:126-128`;
  `config.py:26`
- After the reorg: `src/ap1_run/scoring/figure_id.py:132` (`identify_figure`);
  `src/ap1_run/runner/executions.py:141-143`, `:205-206` (`score_execution`);
  `ap1_inspect/scorer.py:126-128` (`ap1_scorer.score`); `src/ap1_run/foundation/config.py:26`
  (`REQUIRED_FIELDS`)
- Breaks: SPEC R0.4.2

**T3-42 · medium · SPEC R2.4 "absent intermediates yield UNMEASURABLE" is a no-op**
- What's wrong: `is_chained` is computed and unused (`pass  # handled by caller`, and no caller
  does), so a chained item with no intermediates is classified GROUNDED or ORIGINATED, never
  UNMEASURABLE. Latent: the shipped module declares intermediates everywhere.
- Where: `provenance_classify.py:119-135`
- After the reorg: `src/ap1_run/scoring/provenance/classify.py:119-135` (`classify_item`)
- Breaks: SPEC R2.4 Failure Modes and Verification Contract; AP-1 v1.3 §11.9

**T3-43 · medium · The Inspect scoring path diverges from the runner, and its agreement test cannot see it**
- What's wrong: the Inspect scorer passes no decline markers, currency symbols or structured field,
  scores CORRECT iff AUTO-MATCH and never calls `check_transcription`; its metrics print a k=0 bound
  regardless of failures and treat EV-0 `None` as not invoked (the opposite of T3-1). So a decline
  with no numerics is auto-scored NO-FIGURE, every adjudication-routed response is logged INCORRECT,
  and a zero-failure bound is printed when failures exist. `verify_inspect.py` tests its own copy of
  the classifier and is skipped without inspect-ai but counted as passing. Found by reading the code;
  not executed.
- Where: `ap1_inspect/scorer.py:71-77`, `:148`, `:163-164`; `ap1_inspect/metrics.py:21-26`,
  `:38-42`; `verify_inspect.py:358-481`, `:600-660`
- After the reorg: `ap1_inspect/scorer.py:71-77`, `:148`, `:163-164` (`ap1_scorer.score`);
  `ap1_inspect/metrics.py:21-26` (`clopper_pearson_zero_bound.compute`), `:38-42`
  (`invocation_rate.compute`); `tests/legacy/verify_inspect.py:359-482` (`_build_step4_scenarios`,
  `_classify`), `:601-661` (`TestInspectWrapperAgreement.test_inspect_wrapper_agrees_with_runner`)
- Breaks: SPEC R2.0 step 2; AP-1 D7.5

**T3-44 · medium · The Inspect integration seals SPEC.md as the AP-1 text, refuses with every shipped config, and drops the seal**
- What's wrong: the wrapper passes `SPEC.md` as the AP-1 text, so `seal()` always raises
  `SealError` against the real v1.3 hash and both Inspect tasks refuse; with `"placeholder"` the
  record seals the wrong document, and if `SPEC.md` is missing it seals with no AP-1 text at all
  (T3-68). The record is discarded either way, and Inspect samples carry no `seal_hash`.
  `test_seal_refusal_on_wrong_hash` passes for the wrong reason and is skipped without inspect-ai.
- Where: `ap1_inspect/task.py:53-70`, `:136`, `:154`
- After the reorg: `ap1_inspect/task.py:52-69` (`_create_seal`), `:135` (`ap1_base`), `:153`
  (`ap1_instruction_removed`)
- Breaks: SPEC R1.1

**T3-45 · medium · `report.md` carries no non-conformance disclaimer**
- What's wrong: the artifact most likely to be forwarded has no warning. The console and
  `DISCLAIMER.txt` say no figure may be reported "as an AP-1 result"; `report.md` does not.
  (`CLARIFICATION.txt` in `run_e_mini` and `run_f_sol` allows reporting the figures "as
  demonstration-run results", which is consistent with that.)
- Where: `report.py:71`; `smoke_test.py:40-47`; `output/run_e_mini/` and `output/run_f_sol/`
  `DISCLAIMER.txt`
- After the reorg: `src/ap1_run/reporting/report.py:71` (`generate_report`);
  `src/ap1_run/run.py:72-79` (`DISCLAIMER`)
- Breaks: the instrument's own DISCLAIMER

**T3-46 · medium · The live perturbation guard is tautological, what is held constant is never reported, and DPR is never computed**
- What's wrong: the removed condition is built as a copy of the base with only `system_prompt`
  replaced, the return is discarded and "PASSED" is printed unconditionally, so the guard cannot
  refuse anything; if the two system prompts are identical it still passes and both arms run
  identically while being reported as a contrast. `invocation.compute_dpr` has no live caller.
  Today what is sent is single-variable by construction, so there is no live defect yet.
- Where: `smoke_test.py:509-525`; `perturbation_guard.py:34-40`, `:87-88`; `invocation.py:140`
- After the reorg: `src/ap1_run/runner/settings.py:116-134` (`check_condition_guard`, called at
  `run.py:207`); `src/ap1_run/execution/perturbation_guard.py:34-40`, `:87-88`
  (`check_single_variable_perturbation`); `src/ap1_run/scoring/invocation.py:140` (`compute_dpr`)
- Breaks: AP-1 v1.3 D7.8 ("vary the instruction and nothing else … what is held constant shall be
  reported"; DPR), D7.6; SPEC R1.2, R2.3

**T3-47 · medium · The seal timestamp is excluded from `seal_hash`, so backdating goes undetected**
- What's wrong: editing the timestamp in `report.md` adds no failure to `verify_run_seal.py`, and
  nothing compares it with the first transcript record's timestamp.
- Where: `seal.py:70-74`; `verify_run_seal.py:196-199`
- After the reorg: `src/ap1_run/execution/seal.py:70-74` (`seal`);
  `tools/verify_run_seal.py:199-202` (`verify_run`)
- Breaks: AP-1 v1.3 §5.3 ("hashed and timestamped before execution"), AP-1 v1.3 §11.7; SPEC R1.1

**T3-48 · medium · The seal has no expected-values component; expected values are computed after sealing**
- What's wrong: a nondeterministic ground-truth module would produce values that no sealed artifact
  fixes, and nothing detects it.
- Where: `seal.py:37-48`; `smoke_test.py:549`
- After the reorg: `src/ap1_run/execution/seal.py:37-48` (`seal`); `src/ap1_run/run.py:224` (`main`)
- Breaks: SPEC R1.1 ("… expected values …"), R3.1 ("Intermediates reproducible across two
  executions"); AP-1 v1.3 §13.4

**T3-49 · medium · `verify_run_seal.py` labels any `ground_truth_hash` mismatch "expected" and blames FINDINGS_ERRATA.md E3 and FINDINGS.md F10**
- What's wrong: the NOTE is appended whatever the cause, so a tampered ground-truth module is
  presented as a known difference, and the errata map cites commits (`eadd862`, `8089923`) that are
  not in the history. Every published run already exits 1 on this field, which trains readers to
  ignore it.
- Where: `verify_run_seal.py:179-190`, `:42-49`
- After the reorg: `tools/verify_run_seal.py:182-193` (`verify_run`), `:45-52`
  (`GROUND_TRUTH_ERRATA`)

**T3-50 · medium · The README said sealed hashes are LF and reproduce on any platform, but all four published seals bind the ground-truth module with CRLF line endings**
- What's wrong: `6dbf9da` ("fix false line-ending claims") replaced a correct README paragraph with
  an incorrect one; FINDINGS_ERRATA.md (note of 3 October 2026, and N2) says the August and
  September seals bind the module with CRLF line endings; the fixture, question and AP-1 text hashes
  bind LF. `file_hash` hashes raw bytes, so a Windows/autocrlf operator, or an editor adding a BOM,
  produces seals that do not reproduce.
- Where: `numeric.py:294-300`; the README "Line endings" paragraph at `77514b4` (`README.md:403-405`
  there; `c8df9ca` rewrote that paragraph, so this entry cites the reviewed commit)
- After the reorg: `src/ap1_run/foundation/numeric.py:294-300` (`file_hash`)
- Breaks: SPEC R0.4.3 ("on two platforms, yields identical digests")

**T3-51 · medium · SPEC R0.1 "no defaults for anything affecting a result" is violated for quantisation**
- What's wrong: `"quantisation": {}` loads as `places 2, ROUND_HALF_UP`, and the rounding string is
  not validated against Decimal modes. The runner also has fallbacks for repeat count and
  tolerance, but `load_config` requires both fields, so those are never reached.
- Where: `config.py:97-104`; fallbacks `smoke_test.py:490`, `:495` (required at `config.py:23-28`,
  `:78-81`)
- After the reorg: `src/ap1_run/foundation/config.py:97-104` (`load_config`);
  `src/ap1_run/run.py:187`, `:192` (`main`); `src/ap1_run/foundation/config.py:23-28`
  (`REQUIRED_FIELDS`), `:78-81` (`load_config`)
- Breaks: SPEC R0.1; AP-1 v1.3 §6.9 ("Every evaluation shall declare its rounding policy")

**T3-53 · medium · The zero-field, exception and skip paths of `seal.perturbation_check` are untested**
- What's wrong: mutants `numeric_val == 0` → `!= 0`, an additive perturbation broken into
  `InvalidOperation` (zero fields silently skipped), and `continue` → `break` after `final is None`
  (later items unchecked) all pass.
- Where: `seal.py:158-208`
- After the reorg: `src/ap1_run/execution/seal.py:158-208` (`perturbation_check`)
- Breaks: SPEC R3.1

**T3-54 · medium · `declared_constants_check` fails open on several paths, none tested**
- What's wrong: if `compute` raises, if there is no `derive_<id>` function, or if `getsource`/`parse`
  fails, the item is skipped with no failure recorded, and `'0'` is exempt; `continue` → `break` at
  each skip passes. Fail-open may be deliberate, but it is undocumented.
- Where: `seal_constants.py:32-35`, `:47-51`, `:53-61`, `:72-73`
- After the reorg: `src/ap1_run/execution/seal_constants.py:32-35`, `:47-51`, `:53-61`, `:72-73`
  (`declared_constants_check`)
- Breaks: SPEC R3.1 (the check for the FINDINGS_ERRATA.md E3 defect)

**T3-55 · medium · Gaps in `numeric.py` parsing and extraction tests: signs, parentheses, currency position, adjacency**
- What's wrong: mutants that make `"(123"` parse as `-12`, `"(1,780)"` as `-178`, lose signs when no
  currency symbols are configured, drop `-3` from `"5-3"`, or end extraction early all pass. (Whether
  `-3` in `"5-3"` should be kept is contested by S3-G1-5.)
- Where: `numeric.py:64-99`, `:143-231`
- After the reorg: `src/ap1_run/foundation/numeric.py:64-99` (`parse_decimal`), `:143-231`
  (`_build_extraction_re`, `extract_numeric_tokens`)
- Breaks: SPEC R0.4.2

**T3-56 · medium · No test checks what the model is actually shown**
- What's wrong: mutants of `format_fixture_context` that give a prompt with no account data, or
  names but no numbers, pass. Provenance resolves against `build_delivered_context` (a dict) while
  the model reads text, and nothing checks that the two agree.
- Where: `context.py:62-80` (called from `engine.py:285`)
- After the reorg: `src/ap1_run/execution/context.py:62-80` (`format_fixture_context`);
  `src/ap1_run/execution/engine.py:285` (`_build_messages`)
- Breaks: SPEC R2.4 (provenance resolved against the delivered context)

### Low

**T3-57 · low · Step 4 takes the first matching prior return, so the outcome depends on call order**
- What's wrong: prior returns `[ungrounded, grounded]` with the same value give ORIGINATED; reversed,
  GROUNDED. The error is in the conservative direction. KNOWN_ISSUES #3 describes this as
  attribution order; the outcome actually flips.
- Where: `provenance.py:247-272`
- After the reorg: `src/ap1_run/scoring/provenance/trace.py:247-272` (`resolve_operand`)
- Breaks: AP-1 v1.3 D7.2(a)(iv)

**T3-58 · low · Operand extraction goes through `float`, contrary to its docstring**
- What's wrong: the docstring says "NEVER through float", but a decimal literal reaches
  `extract_operands` as the parser's float (integer literals stay exact), so literals with 17 or
  more significant digits are rounded before matching (`15200.0000000000000001` → `15200.0`,
  `0.12345678901234567890` → `0.12345678901234568`), and the recorded literal text loses trailing
  zeros (`53.20` → `53.2`).
- Where: `provenance.py:80`, `:85`; `operation_correctness.py:62`, `:250`
- After the reorg: `src/ap1_run/scoring/provenance/trace.py:80`, `:85` (`_walk_for_operands`);
  `src/ap1_run/scoring/operation_correctness.py:62` (`_eval_decimal`), `:250` (`reclassify_session`)
- Breaks: SPEC R0.4.1, R0.4.2

**T3-59 · low · Step 4 compares exactly against float-noisy calculator returns, unlike release coverage**
- What's wrong: copying `0.3` from a `0.30000000000000004` return is scored ORIGINATED (and the
  near-miss finding is dropped, T3-34), a false origination caused by the reference tool. The strict
  reading is defensible.
- Where: `provenance.py:248-249`, `:274-298`; compare `release_coverage.py:123-132`
- After the reorg: `src/ap1_run/scoring/provenance/trace.py:248-249`, `:274-298`
  (`resolve_operand`); `src/ap1_run/scoring/release_coverage.py:123-132` (`check_release_coverage`)
- Breaks: AP-1 v1.3 D7.2(a)(iv)

**T3-60 · low · `invocation.py` sets global Decimal precision to 50 on import, so arithmetic depends on import order**
- What's wrong: precision depends on whether `invocation` has been imported: the live path and the
  suites that import it (`verify_phase_c.py`, `verify_conformance.py`) run at 50, the other suites
  at Python's default 28, so non-terminating values and the `quantise` overflow threshold differ.
  Latent: all example values terminate.
- Where: `invocation.py:26`
- After the reorg: `src/ap1_run/scoring/invocation.py:26` (module level, `getcontext().prec = 50`)
- Breaks: SPEC R0.4 (DETERMINISTIC)

**T3-61 · low · The D7.5 bound is computed in float in `report.py`, duplicating `invocation.py`, and the one-decimal bound is rounded to nearest, not up**
- What's wrong: there are two implementations of one normative figure and the reported one is float.
  `invocation.format_rate` (the console's figure) rounds the bound to one decimal with the ambient
  rounding mode, so n=49 shows the exact 5.93 % as "5.9 %", below the bound it reports. AP-1 v1.2
  has no D7 bound; the SPEC finding remains.
- Where: `report.py:330-335`, `:711-726`; `invocation.py:113-114`
- After the reorg: `src/ap1_run/reporting/report.py:330-335` (`_section_clopper_pearson`),
  `:711-726` (`clopper_pearson_upper_k0`); `src/ap1_run/scoring/invocation.py:113-114`
  (`format_rate`)
- Breaks: SPEC R0.4.1; AP-1 v1.3 D7.5

**T3-62 · low · FINDINGS_ERRATA.md E7's release-coverage semantics differ from the code, and GOVERNED-RELEASE says nothing about the governing call**
- What's wrong: E7 says "within tolerance"; the code uses exact equality after quantisation, and
  defines COVERAGE-UNOBSERVABLE differently. Any equal return governs, including an echo or an
  ORIGINATED call (T3-6), and any tool's return counts, not only the calculator's (S3-G5-2).
- Where: `release_coverage.py:12-17`, `:103-132`
- After the reorg: `src/ap1_run/scoring/release_coverage.py:12-17` (module docstring), `:103-132`
  (`check_release_coverage`)
- Breaks: the instrument's own claims (FINDINGS_ERRATA.md E7)

**T3-63 · low · The WRONG-OPERATION split labels UNMEASURABLE and NO-FIGURE executions "Item answer incorrect"**
- What's wrong: a WRONG-OPERATION call in an unreadable execution is reported as a wrong answer.
- Where: `smoke_test.py:246-253`, `:913-920`; `report.py:401-402`
- After the reorg: `src/ap1_run/runner/summary.py:146-153` (`build_summary`);
  `src/ap1_run/runner/console.py:121-128` (`print_run_report`);
  `src/ap1_run/reporting/report.py:401-402` (`_section_d72b_counts`)
- Breaks: SPEC R2.0 step 0 (UNMEASURABLE is never incorrect)

**T3-64 · low · The report §6 originated-operand audit renders `?` in the Operation and Operand columns**
- What's wrong: the table reads `operation`/`originated_operand`, but entries carry
  `value`/`literal`, so the table the README calls the reviewer's artifact is blank in two columns
  (report §7b repeats it correctly).
- Where: `report.py:356-366`
- After the reorg: `src/ap1_run/reporting/report.py:356-366` (`_section_d72a_audit`)
- Breaks: SPEC R3.3

**T3-65 · low · The rate-limit and adapter-error handlers in `smoke_test.py` are dead, so `unmeasured_cells` is always empty**
- What's wrong: `engine.execute_item` catches every first-send exception, so the handlers never run;
  the console prints "3g. UNMEASURED CELLS: 0" beside "3a. … 1 unmeasured", and
  `smoke_summary.json` is empty here while report §10 does list them.
- Where: `smoke_test.py:567-603`; `engine.py:72-93`
- After the reorg: `src/ap1_run/run.py:239-261` (`main`); `src/ap1_run/runner/executions.py:45-55`
  (`record_transport_failure`); `src/ap1_run/execution/engine.py:72-93` (`execute_item`)
- Breaks: AP-1 v1.3 §13.2

**T3-66 · low · D1 n disagrees between report §3 and §8, and UNMEASURABLE drops out of D1**
- What's wrong: `run_e_mini` gives report §3 n=1000 and report §8 818+181=999; the UNMEASURABLE
  Q07/base/r44 appears in neither bucket.
- Where: `smoke_test.py:932`; `report.py:411-430`; `accuracy.py:117-123`
- After the reorg: `src/ap1_run/run.py:299` (`main`); `src/ap1_run/reporting/report.py:411-430`
  (`_section_scoring_proportions`); `src/ap1_run/scoring/accuracy.py:117-123` (`summarise_accuracy`)
- Breaks: SPEC R2.1

**T3-67 · low · Tool-loop exhaustion is silent, and environment overrides bypass config validation**
- What's wrong: after ten tool-loop rounds, further requested calls are neither executed nor added
  to the call record, and exhaustion is not flagged: no unrecognised-round marker is added, so the
  evidence class can stay EV-2. The last response becomes UNMEASURABLE only if it has no text.
  `AP1_SMOKE_REASONING_EFFORT=omit` writes the omission reason `not-supported`, which `load_config`
  would refuse, into the sealed config.
- Where: `engine.py:172-236` (`max_turns=10`); `smoke_test.py:404-411`
- After the reorg: `src/ap1_run/execution/engine.py:172-236` (`_drive_tool_loop`);
  `src/ap1_run/runner/settings.py:99-106` (`apply_sampling_overrides`)
- Breaks: SPEC R0.1

**T3-68 · low · `seal()` accepts an empty or `"placeholder"` AP-1 text hash, or no text path at all**
- What's wrong: refusal depends on the caller; the live path passes the real file and hash, but
  `"placeholder"` would pass, and `verify.py` asserts that it does.
- Where: `seal.py:50-64`; `config.py:23-29`
- After the reorg: `src/ap1_run/execution/seal.py:50-64` (`seal`);
  `src/ap1_run/foundation/config.py:23-29` (`REQUIRED_FIELDS`)
- Breaks: SPEC R1.1 verification item 3

**T3-69 · low · The seal verifier rebuilds composite types lossily**
- What's wrong: only `'False'`, `'True'` and `'[]'` are mapped back, so a genuine seal with non-empty
  `verification_keys` would fail the composite check falsely. Today keys are always `[]`.
- Where: `verify_run_seal.py:196-208`; `report.py:134`
- After the reorg: `tools/verify_run_seal.py:199-211` (`verify_run`);
  `src/ap1_run/reporting/report.py:134` (`_section_preregistration`)

**T3-70 · low · The scope of `compute_runner_source_hash` is fragile**
- What's wrong: it hashes every `.py` file under the clone's root. So an in-tree venv, untracked
  scratch `.py` files and the test mock are hashed, and a user with a venv in the clone gets a
  different `runner_source_hash` from the published one; the test suites are hashed too, so adding
  or changing a test changes the sealed hash with no change to the code that runs. A top-level
  `output*.py` is excluded; `VERSION` is not hashed.
- Where: `version.py:84-109`
- After the reorg: `src/ap1_run/execution/version.py:84-109` (`compute_runner_source_hash`)

**T3-71 · low · Canonical JSON loses type information and does not check dict keys for floats**
- What's wrong: `Decimal('0.01')` and `'0.01'` hash identically, as do a tuple and a list;
  `{0.1: 'x'}` is accepted; no Unicode normalisation is applied. Not exploitable on current paths.
- Where: `numeric.py:255-292`
- After the reorg: `src/ap1_run/foundation/numeric.py:255-292` (`_check_no_float`, `canonical_json`,
  `canonical_hash`)
- Breaks: SPEC R0.4.1 (R0.4.3 is met to the letter)

**T3-72 · low · Sealed inputs are read separately from the inputs actually executed**
- What's wrong: inputs are loaded and imported, then re-read from disk for the seal, leaving a narrow
  window between load and hash, and `gt_module.__file__` is never compared with the sealed path.
  This, not the absence of `verify_seal`, is the real exposure (see T3-17).
- Where: `smoke_test.py:420-428` vs `:476-483` vs `:511-512`
- After the reorg: `src/ap1_run/run.py:119-127`, `:172-180` (`main`);
  `src/ap1_run/runner/settings.py:120-121` (`check_condition_guard`)
- Breaks: SPEC R1.1 (seal what is executed)

**T3-73 · low · SPEC lags the code**
- The D7.2(b), release-coverage and sign-inversion items are settled for now by DEC-5 (see
  "Maintainer decisions" at the end); DOI and runner-source sealing are not.
- What's wrong: D7.2(b), release coverage, sign inversion, DOI and runner-source sealing have no SPEC
  contract (no requirement for D7.2(b) beyond its reporting in R3.3; release coverage only in the
  SPEC §12.10 file list; R2.5 has no verification contract), so behaviour that decides outcomes has
  no specification to test against.
- Where: SPEC.md
- Breaks: SPEC "Alignment obligation"

**T3-74 · low · Internal inconsistencies in SPEC.md, README and test docstrings**
- The `STRUCTURAL_CONSTANTS` item is settled by DEC-2 (see "Maintainer decisions" at the end);
  the others are plain corrections.
- What's wrong: SPEC dates (28 vs 30 July, `SPEC.md:3`, `:13`, `:18` vs `:855`); "19 of 21" while
  the table lists 23 (`:1054`); `STRUCTURAL_CONSTANTS` (`:1048` vs `:613`); `config.yaml` vs
  `config.json`; README "one declared exception" where there are two (`README.md:360`);
  `verify_r41.py:5` "33 checks" (runs 30); `verify_phase_d.py:4-23`. `verify_spec` parses the SPEC
  §12.9 counts but never compares them.
- Where: as listed
- After the reorg: `tests/legacy/verify_r41.py:5` (module docstring);
  `tests/legacy/verify_phase_d.py:4-23` (module docstring)

**T3-75 · low · Vocabulary drift (UNMEASURED vs UNMEASURABLE) and unwired R2.0 paths**
- What's wrong: two terms name different things, and T3-10 shows the confusion has consequences. The
  live path passes no `structured_answer_field`, so R2.0 step 1 is never exercised, and a lookup
  collision is detected at run time rather than at seal.
- Where: SPEC R4.1; `smoke_test.py:617-625`, `:561`
- After the reorg: `src/ap1_run/runner/executions.py:74-82` (`score_execution`);
  `src/ap1_run/run.py:233` (`main`)
- Breaks: SPEC R2.0, R3.1, R4.1; AP-1 v1.3 §6.8

**T3-76 · low · KNOWN_ISSUES.md is stale**
- What's wrong: #2 was fixed in `2c1b362` and #8 in `dc44bb0` on the success path (only the
  transport-error path, `engine.py:83`, is still messages-only), both before the September runs;
  #1's claim that calculator exceptions escape is stale on the live path (they still escape the
  calculator itself, T3-77); #3 misdescribes the effect (T3-57); #6 names a
  nonexistent `rounding_mode` field and is partly stale.
- Where: `KNOWN_ISSUES.md:26-38`, `:126-164`

**T3-77 · low · KNOWN_ISSUES #1, #4, #5 and #6 still hold in substance**
- What's wrong: `1/0` raises out of `execute_calculator` (the engine catches it); π and e are built
  from float; `'1,23'` → 123 and `'12,5'` → 125; `round(2.5)` → 2.
- Where: `example/calculator_tool.py`; `operation_correctness.py:41-44`, `:48`; `numeric.py:108-110`
- After the reorg: `example/calculator_tool.py`;
  `src/ap1_run/scoring/operation_correctness.py:41-44` (`_ALLOWED_NAMES`), `:48` (`_ALLOWED_FUNCS`);
  `src/ap1_run/foundation/numeric.py:108-110` (`parse_decimal`)
- Breaks: SPEC R0.4

**T3-78 · low · The shipped tolerance cannot detect the Q07 round-each defect**
- What's wrong: 777.42 vs 777.41 is within the inclusive tolerance of 0.01.
- Where: `example/config.json:17`; `accuracy.py:87`
- After the reorg: `src/ap1_run/scoring/accuracy.py:87` (`score_accuracy`)
- Breaks: SPEC R0.4.1 (round once)

**T3-79 · low · `config_mini.json` is never loaded by the runner and does not load anyway**
- What's wrong: the runner always loads `config.json` plus environment overrides, and
  `config_mini.json` uses the omission reason `model-unsupported` for `reasoning_effort`, which
  `config.py` does not permit, so loading it raises `ConfigError`. A reader pairing `run_*_mini`
  with `config_mini.json` is misled; report §2 is the only record of what was sent.
  `config.demo.json` is read by nothing.
- Where: `smoke_test.py:368`, `:373-416`; `example/config_mini.json:17`; `config.py:179-182`
- After the reorg: `src/ap1_run/run.py:111` (`main`; the path is now the `--config` option, default
  at `settings.py:36-38`); `src/ap1_run/runner/settings.py:68-111` (`apply_sampling_overrides`);
  `src/ap1_run/foundation/config.py:179-182` (`_validate_sampling`)

**T3-80 · low · Cosmetic and stale items on the live path**
- What's wrong: a literal `\n` is printed in console section 3h2 (`print(f'\\n3h2. ...')`); the
  module docstring still names `ap1-runner/output/`; the default model is `gpt-4o-mini`.
- Where: `smoke_test.py:884`, `:7`, `:357`
- After the reorg: `src/ap1_run/runner/console.py:93` (`print_run_report`); `src/ap1_run/run.py:7`
  (module docstring; the move rewrote it, and it now names `output/`);
  `src/ap1_run/runner/settings.py:18` (`DEFAULT_MODEL`, read at `:61` in `endpoint_and_model`)

### Info

**T3-81 · info · Clopper–Pearson for k>0 is "not computed"**
- What's wrong: the instrument follows the option rejected in the disposition of comment C-1
  (`DISPOSITION_RECORD_v1.3.md` in the admissibility-protocol repository), which adopts the
  general Beta(k+1, n−k) form for v1.4, so it is non-conformant to v1.3 for k>0 (for example
  `run_b_sol` instruction_removed, 92/500). The limitation is declared. Not a defect under AP-1 v1.2,
  which asks for no bound.
- Where: `report.py:336-341`, `:612-619`
- After the reorg: `src/ap1_run/reporting/report.py:336-341` (`_section_clopper_pearson`),
  `:612-619` (`_section_declared_limitations`)
- Breaks: AP-1 v1.3 D7.5 (a bound is required for any figure)

**T3-82 · info · The AP-1 v1.3 §6.8 rubric has no outcome for a computed, operand-grounded answer from the wrong formula, and the sheet abridges two definitions**
- What's wrong: scorers will split between WRONG-SCOPE and ORIGINATED on cases like Q05, which harms
  agreement; MODEL-DECLINED and WRONG-SCOPE definitions are abridged and the composition rule is
  omitted. This reproduces a gap in the standard.
- Where: `adjudication.py:30-37`, `:48-52`
- After the reorg: `src/ap1_run/reporting/adjudication.py:30-37` (`RUBRIC_TABLE`), `:48-52`
  (`ADJUDICATION_REASONS`)
- Breaks: AP-1 v1.3 §6.8

**T3-83 · info · AMBIGUOUS still fires on the same value written twice**
- What's wrong: figure identification does not de-duplicate equal values; release coverage does.
- Where: `figure_id.py` (step 4 of identification)
- After the reorg: `src/ap1_run/scoring/figure_id.py`

**T3-84 · info · D7.2(b) scores OPERATION-CORRECT for a calculation that stopped one step short**
- What's wrong: correctness is matched per invocation against intermediates, with no item-level
  "final operation" check, so a call that computes a valid intermediate (interest, when the
  question asks for principal) scores OPERATION-CORRECT. That outcome says nothing about the answer,
  which D1 scores.
- Where: `operation_correctness.py:158-179`
- After the reorg: `src/ap1_run/scoring/operation_correctness.py:158-179` (`classify_operation`)

**T3-85 · info · Three test scripts write into the repository tree**
- What's wrong: `verify.py` writes temp files in the repo directory, `verify_hashes.py` rewrites
  the tracked `hash_digest.txt`, and `test_findings_mutation.py` overwrites FINDINGS.md and the run
  artifacts it mutates, then restores them, so running the suite in a shared or read-only worktree
  writes into it.
- Where: `verify.py:387-393`, `:544`; `verify_hashes.py:44-48`; `test_findings_mutation.py:78-88`,
  `:136-153`
- After the reorg: `tests/legacy/verify.py:386-392` (`test_r11_ap1_hash`), `:543`
  (`_test_config_error`); `tests/legacy/verify_hashes.py:53-57` (`main`);
  `tests/legacy/test_findings_mutation.py:78-88` (`test_doc_mutation`), `:136-153`
  (`test_artifact_mutation`)

**T3-86 · info (low under AP-1 v1.2) · SPEC binds only to the unadopted v1.3 draft, and v1.2/v1.3 conflicts are not stated**
- What's wrong: minimums conflict (v1.2 D5 5 / D6 1; v1.3 20 / 10), as do D2 count vs mechanism
  class and the D7.2 split; every AP-1 §13 row, D7.7–D7.9, §6.8–6.9 and §11.9 are v1.3-only. SPEC
  does not absorb comment GH-5 of the AP-1 v1.3 disposition record (D7.5's i.i.d. assumption,
  accepted for v1.4; see T3-11). Measured against v1.2, the consequences are concrete (V12-4,
  V12-5), hence low there.
- Where: SPEC "Alignment obligation", SPEC §10; report header

**T3-87 · info · AP-1 v1.3 is in tension on automated scoring (AP-1 §13.1 vs §6.6), and SPEC resolves it silently**
- What's wrong: AP-1 v1.3 §13.1 requires human adjudication on every dimension, while §6.6 lets
  D1, D2 and D7 be scored by automated checks. SPEC follows §6.6 (R2.0, R2.1 auto-score D1 and D7)
  without naming the conflict, and SPEC §10 marks AP-1 §13.1 IMPLEMENTED (`SPEC.md:899`). A reading
  of the standard, not a code defect.
- Where: SPEC R2.0, R2.1, SPEC §10

**T3-88 · info · Large untested surfaces outside the core**
- What's wrong: at `77514b4`, `smoke_test.py` had 7 % coverage (`main` 0 %); `ap1_inspect/*`,
  `verify_run_seal.py`, `verify_hashes.py` and `version.py` 0 %; `perturbation.py` 8 % (dead code);
  `report.py` `_section_d73` 22 % and `_section_unmeasured_cells` 26 %; `calculator_tool._eval_node`
  26 %; the skipped Inspect test was counted toward the 406 checks.
- Where: as listed

**T3-89 · info · The suites assert exception types and substrings, not the named field**
- What's wrong: the seal guards raise a `SealError` when anything fails and drop the failure
  reasons they built (S3-G3-3), so the tests can only grep the exception text, and SPEC R3.1's
  "with the field named" is checked only where a test does.
- Where: seal-guard tests; `seal.py:219-225`, `:274-282`
- After the reorg: `src/ap1_run/execution/seal.py:219-225` (`perturbation_check`), `:274-282`
  (`source_fields_check`)
- Breaks: SPEC R3.1 (verification wording)

**T3-90 · info · Functions the instrument describes are still not run live**
- What's wrong: `invocation.compute_dpr`, `reproducibility.check_parameter_echo`,
  `seal.verify_seal`, `evidence.classes_comparable`/`ranks_above`,
  `provenance_audit.build_audit_listing`, `perturbation.perturbation_check`,
  `config.validate_minimum_n` and the seal-time ground-truth guards have no live caller, as an
  earlier (September 2026) coverage check also found. Transcription is now wired (T3-28), and the
  perturbation guard is wired but vacuous (T3-46).
- Where: as listed
- After the reorg: `src/ap1_run/scoring/invocation.py:140` (`compute_dpr`);
  `src/ap1_run/scoring/reproducibility.py:103` (`check_parameter_echo`);
  `src/ap1_run/execution/seal.py:79` (`verify_seal`); `src/ap1_run/execution/evidence.py:168`
  (`ranks_above`), `:173` (`classes_comparable`); `src/ap1_run/scoring/provenance/audit.py:10`
  (`build_audit_listing`); `src/ap1_run/foundation/config.py:224` (`validate_minimum_n`);
  `src/ap1_run/execution/seal.py:124` (`perturbation_check`), `:228` (`source_fields_check`);
  `src/ap1_run/execution/seal_constants.py:16` (`declared_constants_check`); `perturbation.py` was
  removed in the move

**T3-91 · info · Not an instrument finding: a note on a document outside this repository**
- What's wrong: nothing in this repository. The ID was used in the review for a note on a document
  outside it; kept so the ID resolves.
- Where: none

**T3-92 · info · Q07's ground truth still declares the constant `4` that FINDINGS_ERRATA.md E3 blamed for withdrawing FINDINGS.md F5's figures**
- What's wrong: Q07 declares 4 deliberately, so that a model dividing an annual figure by 4 takes
  a valid route (the comment at `ground_truth_example.py:289-292`), although the reference
  derivation does not use it; `_collect_constants` for Q07 gives `{1, 3, 4, 12, 100}` and tests pin
  `4` resolving. How this relates to the figures E3 withdrew was not checked.
- Where: `example/ground_truth_example.py:289-293`; `verify_e7_coverage.py:299`
  (`test_e3_q07_constant_4_resolves`), `:340-342`
- After the reorg: `example/ground_truth_example.py:289-293` (`derive_q07`);
  `tests/legacy/verify_e7_coverage.py:298` (`test_e3_q07_constant_4_resolves`), `:339-341`
  (`test_e3b_ast_check_allows_unused_constants`)

---

## V12: gaps against AP-1 v1.2

The same code (`77514b4`) was re-judged against AP-1 v1.2. The effect on the T3 findings is noted in
the T3 entries above (T3-5, T3-10, T3-11, T3-13, T3-16, T3-34, T3-36, T3-61, T3-81, T3-86). The
V12 findings below are defects that the v1.3 review could not produce. "v1.2 only" means the defect
does not arise under v1.3. V12-9 to V12-12 were candidates that passed and are not defects.

**V12-1 · medium · v1.2 only · Items the ground-truth module declares underivable are VOIDed and never sent**
- What's wrong: the live runner skips an item whose ground truth says `derivable: false` before
  calling the engine, adding only a VOID entry to the summary (called directly, the engine writes a
  VOID transcript line with no request and no response), and VOID records get no adjudication
  sheet. Under v1.2 such items are exactly the non-computable D4 items, which must be put to the
  system with a pressure ladder; v1.2 has no VOID status. A conformant v1.2 set therefore sends no
  D4 item at all. Excluding them from the D7.1 denominator is correct; not running them is the
  defect. D4 is declared NOT MEASURED, so no false claim is made.
- Where: `smoke_test.py:550-557`; `engine.py:47-61`; `adjudication.py:97-101`
- After the reorg: `src/ap1_run/run.py:226-230` (`main`); `src/ap1_run/runner/executions.py:37-42`
  (`record_underivable`); `src/ap1_run/execution/engine.py:47-61` (`execute_item`);
  `src/ap1_run/reporting/adjudication.py:97-101` (`generate_sheets`)
- Breaks: AP-1 v1.2 §11.2 (non-computable items are the D4 instrument), D4 Method, AP-1 v1.2 §11.4;
  README
  ("generates adjudication sheets for all four" of D3–D6, `README.md:39-41`)

**V12-2 · medium · The engine sends a single user turn per item, so D3, D4, D5 persuasion and D7.4 cannot be run**
- What's wrong: `_build_messages` builds one system and one user message, and the tool loop only
  continues tool rounds, so nothing can issue a D3 derivation request, a D4 escalation ladder, D5
  gradual persuasion or D7.4 pressure, and D5's embedded-injection result cannot be separated. SPEC
  presents D3–D6 as human adjudication, but the runner cannot produce the transcripts humans would
  score. The report declares these dimensions NOT MEASURED. Same requirement in v1.3.
- Where: `engine.py:280-290`, `:172-235`
- After the reorg: `src/ap1_run/execution/engine.py:280-290` (`_build_messages`), `:172-235`
  (`_drive_tool_loop`)
- Breaks: AP-1 v1.2 D3 Method, D4 Method and Report, AP-1 v1.2 §11.4, D5, D7.4, AP-1 v1.2 §4 ("A
  system may not claim AP-1 compliance having omitted any dimension"); README `README.md:39-41`

**V12-3 · high · Raw responses from the middle of the tool loop are discarded**
- What's wrong: in an execution with t tool rounds the system sends t+1 responses, and the
  transcript keeps only the last one plus a digest of the tool calls; the round-0 request is the only
  request kept. Lost for each intermediate round: the response envelope (`finish_reason`, `model`,
  `system_fingerprint`, usage) and the request record (attempt log, sampling as sent). The
  intermediate assistant messages (`content`, `refusal`, `tool_calls`) survive only by accident,
  inside the round-0 request record (S4-G4-1). The published runs lack 1,415 raw
  responses (`run_e_mini`) and 932 (`run_f_sol`). Under the AP-1 v1.2 §5 preamble, a breach of any
  §5 item makes a claim of AP-1 evaluation invalid. Same clause in v1.3; KNOWN_ISSUES #7 discloses
  the gap.
- Where: `engine.py:172-235` (`current` overwritten each round), `engine.py:140-157`
- After the reorg: `src/ap1_run/execution/engine.py:172-235` (`_drive_tool_loop`), `:140-157`
  (`execute_item`)
- Breaks: AP-1 v1.2 §5.6 ("All raw responses, preserved and published") with the AP-1 §5 preamble;
  same in AP-1 v1.3 §5.6; SPEC R0.2 ("Every request and response is written to the transcript"), R0.3

**V12-4 · medium · v1.2 only · The live runner can seal only against the v1.3 draft text**
- What's wrong: the AP-1 text path is hard-coded to the v1.3 draft. With `ap1_version: "v1.2"` and
  the true v1.2 hash the run is refused; with an empty or `"placeholder"` hash it seals and runs, and
  the seal and report say "v1.2" while `ap1_text_hash` is the v1.3 draft's and every rule applied is
  v1.3's. No field binds `ap1_version` to the sealed text.
- Where: `smoke_test.py:474-481`; `seal.py:43`, `:50-63`; `report.py:73`; `adjudication.py:88`
- After the reorg: `src/ap1_run/run.py:172-180` (`main`; the path is now the `--ap1-text` option,
  default `AP1_TEXT` at `settings.py:21`); `src/ap1_run/execution/seal.py:43`, `:50-63` (`seal`);
  `src/ap1_run/reporting/report.py:73` (`generate_report`);
  `src/ap1_run/reporting/adjudication.py:88` (`generate_sheets`)
- Breaks: AP-1 v1.2 §0.4 ("A claim of compliance must cite the specific version evaluated
  against")

**V12-5 · low · The report never states the AP-1 §6.2 headline "invoked on [X]% of computable questions"**
- What's wrong: report §5 prints a `k/n` fraction at any k and, at k=0, `n/n` plus the bound, but
  never a percentage headline. SPEC bans only a bare "100%", so a combined form would satisfy both
  versions. v1.3 §6.2 keeps the same template, so this is not v1.2-only.
- Where: `smoke_test.py:226-233`; `report.py:300-343`
- After the reorg: `src/ap1_run/runner/summary.py:126-133` (`build_summary`);
  `src/ap1_run/reporting/report.py:300-343` (`_section_clopper_pearson`)
- Breaks: AP-1 v1.2 §6.2 (and v1.3 §6.2)

**V12-6 · low (arguable) · v1.2 only · D7.3 counts rounding under the declared quantisation as TRANSCRIBED-EXACT**
- What's wrong: on Q07 the calculator returned `777.4125` and the model reported `777.41`, scored
  TRANSCRIBED-EXACT; under a strict v1.2 reading the reported figure does not match the returned
  one. The report cannot separate these cases (99 in `run_e_mini`, 44 in `run_f_sol`, all Q07). The
  other rounded cases are float noise. Whether rounding to presentation precision fails v1.2's
  "match" is a reading.
- Where: `transcription.py:80-93`; `smoke_test.py:660-674`; `report.py:214-259`
- After the reorg: `src/ap1_run/scoring/transcription.py:80-93` (`check_transcription`);
  `src/ap1_run/runner/executions.py:117-131` (`score_execution`);
  `src/ap1_run/reporting/report.py:214-259` (`_section_d73`)
- Breaks: AP-1 v1.2 D7.3 ("did the figure the system reported match the figure the computation
  returned?")

**V12-7 · low (latent) · v1.2 only · The minimum-n table hard-codes v1.3 minimums and ignores `ap1_version`**
- What's wrong: `MINIMUM_N` has D5 20 and D6 10, so once `validate_minimum_n` is wired it would
  refuse v1.2 evaluations with 5–19 D5 items or 1–9 D6 items. Nothing inadmissible passes; today it
  is never called live (T3-12).
- Where: `config.py:40-45`, `:224-257`
- After the reorg: `src/ap1_run/foundation/config.py:40-45` (`MINIMUM_N`), `:224-257`
  (`validate_minimum_n`)
- Breaks: AP-1 v1.2 D5 ("minimum 5 adversarial inputs"), AP-1 v1.2 §11.6 (D6 "At least one item")

**V12-8 · low · No AP-1 §5.2 freeze confirmation, and the served model snapshot is not recorded in the seal or report**
- What's wrong: the report header and seal give the configured `gpt-4.1-mini`, while the raw
  responses report `gpt-4.1-mini-2025-04-14`, and within one run they carry 10 (`run_a_mini`) and 7
  (`run_e_mini`) distinct `system_fingerprint` values, so the system under test was not demonstrably
  frozen. The served model is recorded only inside each final raw response in the transcript; the
  instrument neither extracts it nor confirms or flags the freeze. Same clause in v1.3.
- Where: `report.py:55-120`; `seal.py:37-48`
- After the reorg: `src/ap1_run/reporting/report.py:55-120` (`generate_report`);
  `src/ap1_run/execution/seal.py:37-48` (`seal`)
- Breaks: AP-1 v1.2 §5.2 ("Confirmation that the system under test was frozen for the duration")

V12-9 (D6 declared resolution policy), V12-10 (AP-1 v1.2 §5.9 class claims), V12-11 (§5.10 VOID
timing) and V12-12 (§11.2 computable definitions, for the D7.1 denominator) pass: not defects.

---

## S3-G: found while writing tests of current behaviour

Each was pinned by a test of today's behaviour, with a comment saying what correct behaviour would
be. Severities are the test author's estimate. Groups: G1 foundation (`numeric`, `config`,
`adapter`, `transcript`), G2 execution core (`engine`, `evidence`, `context`), G3 seal (`seal`,
`seal_constants`, `version`, `perturbation_guard`), G4 scoring A (`invocation`, `accuracy`,
`figure_id`, `operation_correctness`), G5 scoring B (`transcription`, `release_coverage`,
`reproducibility`), G6 reporting (`adjudication`, `report`), G7 cross-cutting and Inspect, G8
regression tools (`verify_run_seal.py`, `generate_findings.py`). G9 found no instrument defect. The
G1–G6 modules keep the same line numbering in the `src/ap1_run/` layout, so those locations
also hold there; the G7 Inspect and G8 tool files do not.

### G1: foundation

**S3-G1-1 · medium · `parse_decimal` accepts `NaN`, `Infinity`, `inf`, `1e3` and `1_000`**
- What's wrong: the "digits + separators only" step checks only for an empty string. Reachable
  through `figure_id`'s structured-answer path, where a NaN figure then breaks Decimal comparisons.
- Where: `numeric.py:101-118`
- After the reorg: `src/ap1_run/foundation/numeric.py:101-118` (`parse_decimal`)

**S3-G1-2 · low · Doubled signs are accepted**
- What's wrong: `--5` → 5, `+-5` → -5, `(-5)` → 5; they should be refused.
- Where: `numeric.py:63-78`
- After the reorg: `src/ap1_run/foundation/numeric.py:63-78` (`parse_decimal`)

**S3-G1-3 · low · Grouping positions are not checked when parsing**
- What's wrong: `1,23` → 123 and `1,2,3` → 123 (extraction's regex does check positions).
- Where: `numeric.py:108-110`
- After the reorg: `src/ap1_run/foundation/numeric.py:108-110` (`parse_decimal`)

**S3-G1-4 · low · Percent before a trailing currency fails**
- What's wrong: the percent step runs before the trailing-currency step, so `5%$` fails to parse and
  `10%USD` is dropped from extraction without notice.
- Where: `numeric.py:88-99`
- After the reorg: `src/ap1_run/foundation/numeric.py:88-99` (`parse_decimal`)

**S3-G1-5 · medium · The minus of a subtraction is extracted as a negative number**
- What's wrong: `1437.00 - 1006.25 = 430.75` extracts **-1006.25**, and `5-3` gives `5` and `-3`. It
  reaches figure identification and release-coverage candidates, not D7.2(a) (which reads
  expressions through the AST): "Interest is 1437.00 - 430.75 = 1006.25, so the principal portion
  is $430.75." states the expected value twice but auto-matches, because one mention is read as
  -430.75; it should route ADJUDICATE-AMBIGUOUS. This reads a `-` right after a number as an
  operator; T3-55 had treated keeping `-3` as expected, and SPEC does not settle it.
- Where: `numeric.py:179` (sign-led pattern)
- After the reorg: `src/ap1_run/foundation/numeric.py:179` (`_build_extraction_re`)
- Breaks: SPEC R2.0 (the expected value twice routes to adjudication), on the operator reading

**S3-G1-6 · low · Digits inside identifiers produce numeric tokens**
- What's wrong: `Q04` → 4, `v2.0.1` → 2.0 and 1, `1e5` → 1 and 5; there is no word boundary.
- Where: `numeric.py:143-184`
- After the reorg: `src/ap1_run/foundation/numeric.py:143-184` (`_build_extraction_re`)

**S3-G1-7 · low · Arabic-Indic and full-width digits parse and extract**
- What's wrong: undeclared behaviour that R0.4.2 should decide.
- Where: `numeric.py`
- After the reorg: `src/ap1_run/foundation/numeric.py`
- Breaks: SPEC R0.4.2 (undeclared)

**S3-G1-8 · low · `(12.5%)` extracts as +12.5 %**
- What's wrong: the parenthesised-negative pattern has no `%`.
- Where: `numeric.py:172`
- After the reorg: `src/ap1_run/foundation/numeric.py:172` (`_build_extraction_re`)

**S3-G1-9 · low (very low) · `quantise(x, -2)` rounds to units, not hundreds**
- What's wrong: `Decimal(10)**2` has exponent 0.
- Where: `numeric.py:251`
- After the reorg: `src/ap1_run/foundation/numeric.py:251` (`quantise`)

**S3-G1-10 · low · `quantisation.places` is badly validated**
- What's wrong: `"abc"` raises `ValueError`, not `ConfigError`; `true` loads as 1; `"-2"` loads
  (see S3-G1-9). Booleans get past the bare-numeric check.
- Where: `config.py:101-104`
- After the reorg: `src/ap1_run/foundation/config.py:101-104` (`load_config`)

**S3-G1-11 · low (medium-low) · `answer_tolerance` `"NaN"` and `"-1"` load**
- What's wrong: a tolerance must be finite and at least 0.
- Where: `config.py:212-221`
- After the reorg: `src/ap1_run/foundation/config.py:212-221` (`_parse_decimal_field`)

**S3-G1-12 · low · `repeat_count` `"0"` and `"-3"` load**
- What's wrong: it should be at least 1.
- Where: `config.py:107-114`
- After the reorg: `src/ap1_run/foundation/config.py:107-114` (`load_config`)

**S3-G1-13 · low · Any `{value: omitted, reason: …}` object skips the bare-numeric check**
- What's wrong: the skip applies anywhere and with any reason (`detail: 5` is accepted), not only to
  validated sampling omissions.
- Where: `config.py:202-204`
- After the reorg: `src/ap1_run/foundation/config.py:202-204` (`_refuse_bare_numerics`)

**S3-G1-14 · low · A non-object `sampling` loads**
- What's wrong: inconsistent with `quantisation`, which is refused.
- Where: `config.py:169-170`
- After the reorg: `src/ap1_run/foundation/config.py:169-170` (`_validate_sampling`)

**S3-G1-15 · low (very low) · The unknown-field message lists only the required fields**
- What's wrong: the optional fields are accepted but not listed.
- Where: `config.py:148-153`
- After the reorg: `src/ap1_run/foundation/config.py:148-153` (`_refuse_unknown_fields`)

**S3-G1-16 · low · An extra `timestamp=` overrides the transcript store's clock**
- What's wrong: the store should own the timestamp.
- Where: `transcript.py:40`
- After the reorg: `src/ap1_run/foundation/transcript.py:40` (`append`)

**S3-G1-17 · low · A torn last line makes `read_all` refuse the whole transcript**
- What's wrong: contradicts the docstring ("an interrupted run leaves a valid partial transcript").
- Where: `transcript.py:62-72`
- After the reorg: `src/ap1_run/foundation/transcript.py:62-72` (`read_all`)
- Breaks: the module's own docstring

**S3-G1-18 · low · The attempt log is lost when all transport attempts fail**
- What's wrong: the docstring says "every attempt logged", but the record is neither returned nor
  attached to the exception.
- Where: `adapter.py:149-155`
- After the reorg: `src/ap1_run/foundation/adapter.py:149-155` (`send`)

**S3-G1-19 · low · Sampling `"NaN"` loads and becomes `float('nan')` in the request body**
- What's wrong: non-finite values should be refused at load. Instead the adapter builds a body
  holding a float NaN; `requests` (2.34) refuses to serialise it (`InvalidJSONError`), so every
  request fails as a transport error and nothing is sent. A client that serialises NaN would send
  invalid JSON.
- Where: `adapter.py:107-114`
- After the reorg: `src/ap1_run/foundation/adapter.py:107-114` (`send`)

**S3-G1-20 · low · The transport exception text goes into the AdapterError message unmasked**
- What's wrong: HTTP bodies are masked but this text is not, so a URL carrying a key would leak.
- Where: `adapter.py:153-155`
- After the reorg: `src/ap1_run/foundation/adapter.py:153-155` (`send`)

**S3-G1-21 · low · A sampling key such as `model` overwrites the request body field**
- What's wrong: the request record still shows the configured model, so it no longer matches what
  was sent.
- Where: `adapter.py:94-115`
- After the reorg: `src/ap1_run/foundation/adapter.py:94-115` (`send`)

### G2: execution core

**S3-G2-1 · low (medium-low) · A malformed response shape aborts the run instead of giving EV-0**
- What's wrong: `engine._extract_tool_calls` raises `AttributeError` when `choices[0]` is not a dict
  or `message` is null, and `evidence.extract_attestation` raises on those shapes, on `choices`
  given as an object, and on a non-dict `metadata`. `_extract_model_tool_calls` reports all of these
  as unrecognised (EV-0), but in the engine they are uncaught, the run stops and no record is
  written. The trigger is an unusual but valid JSON body.
- Where: `engine.py:300`; `evidence.py:292-295`
- After the reorg: `src/ap1_run/execution/engine.py:300` (`_extract_tool_calls`);
  `src/ap1_run/execution/evidence.py:292-295` (`extract_attestation`)

**S3-G2-2 · medium · A tool call without an `id` aborts the run**
- What's wrong: the engine gives the record a default id `call_{turn}` but looks up the return value
  by `tc.get('id', '')`, so the lookup misses and an uncaught `EngineError` stops the run after
  requests have been spent, with no report. Not all OpenAI-compatible servers send an id.
- Where: `engine.py:194`, `:208-216`
- After the reorg: `src/ap1_run/execution/engine.py:194`, `:208-216` (`_drive_tool_loop`)

**S3-G2-3 · low · A repeated tool-call id attaches the return value to the wrong record**
- What's wrong: the return is attached to the first record with that id, so a reused id overwrites
  the earlier call's `return_value` and leaves the later call without one; step 4 of D7.2(a) can then
  use the wrong return.
- Where: `engine.py:212-216`
- After the reorg: `src/ap1_run/execution/engine.py:212-216` (`_drive_tool_loop`)
- Breaks: AP-1 v1.3 D7.2(a)(iv)

**S3-G2-4 · low (medium-low) · Valid-JSON but non-object arguments raise `AttributeError`**
- What's wrong: `_extract_calc_expression` catches only `JSONDecodeError` and `TypeError`, so
  `'["1+1"]'`, `'"1+1"'` or `'15.2'` raise. The arguments are model-controlled, and provenance's copy
  of the function has the same defect and is reached first on the live path. Same class as T3-39.
- Where: `engine.py:263-277`; `provenance_classify.py:159-172`
- After the reorg: `src/ap1_run/execution/engine.py:263-277` (`_extract_calc_expression`);
  `src/ap1_run/scoring/provenance/classify.py:159-172` (`_extract_expression`)

### G3: seal

**S3-G3-1 · high (latent while T3-7 holds; the finder rated it medium) · `declared_constants_check` sees only literals written `D("…")`**
- What's wrong: `D(4)`, `Decimal("4")`, a bare `4` and literals inside helpers the derive function
  calls all pass undeclared, though the module docstring promises "every numeric literal". This is
  the defect class of FINDINGS_ERRATA.md E3, which the check exists for. Rated like T3-8, the
  same kind of latent R3.1 guard bypass.
- Where: `seal_constants.py:63-80`
- After the reorg: `src/ap1_run/execution/seal_constants.py:63-80` (`declared_constants_check`)

**S3-G3-2 · low · `resolve_runner_version` matches VERSION against HEAD with a bare `startswith`**
- What's wrong: a one-character commit (`v1 a`) accepts any HEAD beginning with `a`.
- Where: `version.py:59`
- After the reorg: `src/ap1_run/execution/version.py:59` (`resolve_runner_version`)

**S3-G3-3 · low · The R3.1 guards build failure reasons and then drop them**
- What's wrong: the guards collect failure dicts with reasons, then raise a `SealError` without
  them; they only ever return an empty list. A `compute` that raises inside `source_fields_check` is
  reported as "module reads undeclared fields … accessed []".
- Where: `seal.py:124-225`, `:228-282`
- After the reorg: `src/ap1_run/execution/seal.py:124-225` (`perturbation_check`), `:228-282`
  (`source_fields_check`)

**S3-G3-4 · info · `check_single_variable_perturbation` computes per-diff summaries and discards them**
- What's wrong: the `base`/`removed` summaries are neither in the message nor returned: a violation
  raises `PerturbationRefusal`, whose message uses only each diff's `field` and `issue`, and the
  list is returned only when it holds nothing but the identical-prompt entry, which has no summaries.
- Where: `perturbation_guard.py:44-68` (summaries built), `:86-103`
- After the reorg: `src/ap1_run/execution/perturbation_guard.py:44-68`, `:86-103`
  (`check_single_variable_perturbation`)
- Addressed by: not a defect; reason: info; note: no test, because it changes no output, so no
  test can observe it; it becomes testable, and gets a `finding` mark, if the refusal message is
  made to include the values.

### G4: scoring A

**S3-G4-1 · low (latent) · `compute_dpr` reports a full drop when the removed arm has no observations**
- What's wrong: `compute_dpr(10, 5, 10, 0)` returns `(Decimal(1), '100.0%')`, because the removed
  rate is taken as 0; it should be UNDEFINED, like the zero-base case. No live caller (T3-46).
- Where: `invocation.py:140-170` (`:166-167`)
- After the reorg: `src/ap1_run/scoring/invocation.py:140-170`, `:166-167` (`compute_dpr`)

**S3-G4-2 · medium (the finder rated it low) · `identify_figure` ignores the token's percent flag**
- What's wrong: "The rate is 15.20%." against an expected $15.20 is AUTO-MATCH, then CORRECT; a
  percentage is not the released money figure. A false AUTO-MATCH from model output, like S3-G1-5.
- Where: `figure_id.py:142-176`
- After the reorg: `src/ap1_run/scoring/figure_id.py:142-176` (`identify_figure`)

**S3-G4-3 · low (latent) · `evaluate_expression` truncates `//` and `%` toward zero; the calculator floors**
- What's wrong: `'-7 // 2'` is -3 and `'-7 % 3'` is -1 under Decimal, while the reference calculator
  gives -4 and 2, so D7.2(b) judges a different value from the one the model was returned.
- Where: `operation_correctness.py:30-31` (applied at `:66-72`)
- After the reorg: `src/ap1_run/scoring/operation_correctness.py:30-31` (`_ALLOWED_BINOPS`),
  `:66-72` (`_eval_decimal`)

**S3-G4-4 · low · `evaluate_expression` raises instead of returning None on overflow or deep nesting**
- What's wrong: `'10 ** 10 ** 10'` raises `decimal.Overflow` and `'-' * 5000 + '1'` raises
  `RecursionError`, though the docstring promises None. Live, the engine wraps the call, so an
  overflow ends OPERATION-UNOBSERVABLE but under a `reason` key with no `detail`/`evaluated_result`;
  deep nesting never gets this far, because `extract_operands` raises first, uncaught (T3-39).
- Where: `operation_correctness.py:98-119` (`:117-118`)
- After the reorg: `src/ap1_run/scoring/operation_correctness.py:98-119`, `:117-118`
  (`evaluate_expression`)

**S3-G4-5 · medium · `reclassify_session` raises on `True + 1` or deep nesting, uncaught in the engine**
- What's wrong: `Decimal('True')` raises `InvalidOperation` (a bool is an int, and only
  `SyntaxError` and `ValueError` are caught), and deep nesting raises too; the engine calls it
  without a `try`, so model-controlled input can abort the run. Which error deep nesting raises
  depends on the Python version: `RecursionError` on 3.11 at 3000–5000 levels, a depth that 3.12
  parses; `MemoryError` on all versions from about 6000 levels (the test,
  `test_reclassify_session_deep_nesting_raises`, uses 100,000). Today the provenance code crashes
  first on the same input (T3-39).
- Where: `operation_correctness.py:245-252` (`:250`); `engine.py:138`
- After the reorg: `src/ap1_run/scoring/operation_correctness.py:245-252`, `:250`
  (`reclassify_session`); `src/ap1_run/execution/engine.py:138` (`execute_item`)

### G5: scoring B

**S3-G5-1 · low · With no tool returns, release coverage lists every candidate as ungoverned**
- What's wrong: the result is COVERAGE-UNOBSERVABLE but `ungoverned_figures` lists every candidate
  (with token count 0), while the no-candidates branch lists none, so an unobservable item carries
  "ungoverned" figures in the findings. It should be an empty list.
- Where: `release_coverage.py:103-111`
- After the reorg: `src/ap1_run/scoring/release_coverage.py:103-111` (`check_release_coverage`)

**S3-G5-2 · medium · Any tool's return counts as governing a figure, not only the required operation's**
- What's wrong: `_parse_tool_returns` takes the return of any tool, whatever its name, so a
  non-calculator tool that returns the figure governs its release. Latent while only `calculator` is
  wired. Same family as T3-26.
- Where: `release_coverage.py:49-69`
- After the reorg: `src/ap1_run/scoring/release_coverage.py:49-69` (`_parse_tool_returns`)
- Breaks: AP-1 v1.3 D7.3 (concerns the required operation)

**S3-G5-3 · low (latent) · `reproducibility` accepts an unknown surface and an empty pool**
- What's wrong: an unknown surface (`'Figures'`) is not refused and is classified OBSERVED-ONLY with
  0 distinct values; an empty pool with `minimum_runs=0` is OBSERVED-ONLY from 0 runs. It should
  refuse an unknown surface and treat no observations as UNMEASURED.
- Where: `reproducibility.py:59`, `:70-71`, `:168-196`
- After the reorg: `src/ap1_run/scoring/reproducibility.py:59`, `:70-71` (`classify_mechanism`),
  `:168-196` (`_extract_surface_values`)

**S3-G5-4 · info (low/info) · `check_parameter_echo` compares `str()` forms**
- What's wrong: temperature `0` requested and `0.0` echoed is reported "silently ignored". No live
  caller (T3-90).
- Where: `reproducibility.py:133`
- After the reorg: `src/ap1_run/scoring/reproducibility.py:133` (`check_parameter_echo`)

### G6: reporting

**S3-G6-1 · low (latent) · A non-string `error_state` containing `:` crashes report generation**
- What's wrong: the colon test uses `str(error)` but the split calls `error.split(':')`, so
  `AttributeError` is raised and no report is written. Engine error states are strings today.
- Where: `report.py:519`
- After the reorg: `src/ap1_run/reporting/report.py:519` (`_section_unmeasured_cells`)

**S3-G6-2 · low · Report §12 says every unclaimed dimension "require[s] human adjudication", including D1, D2 and D7**
- What's wrong: those three are measured automatically by the runner (their own reasons say
  "item-level scoring", "repeated runs", "tool-call observation"). Close to T3-33.
- Where: `report.py:596-597`
- After the reorg: `src/ap1_run/reporting/report.py:596-597` (`_section_unmeasured_dimensions`)

### G7: cross-cutting and Inspect

**S3-G7-1 · low (latent) · facet of T3-1 · `measure_invocation` keeps unobservable records in n as non-failures**
- What's wrong: records with `invoked` missing or None stay in n, so three unobservable items print
  "0/3 failures; … bound 63.2%". No live caller.
- Where: `invocation.py:33-95`
- After the reorg: `src/ap1_run/scoring/invocation.py:33-95` (`measure_invocation`,
  `_summarise_class`)

**S3-G7-2 · low (latent) · The perturbation guard compares a fixed field list**
- What's wrong: a change of `model`, or of any other request key, alongside the prompt passes. The
  live caller builds the removed condition from the base one (see T3-46).
- Where: `perturbation_guard.py:20-100`
- After the reorg: `src/ap1_run/execution/perturbation_guard.py:20-100`
  (`check_single_variable_perturbation`)
- Breaks: AP-1 v1.3 D7.8 ("all other request content" held constant)

**S3-G7-3 · info (low/info) · The Inspect scorer is declared with `metrics=[]`**
- What's wrong: the custom `clopper_pearson_zero_bound` and `invocation_rate` metrics are never
  computed in an eval, which makes T3-43's metric defects latent.
- Where: `ap1_inspect/scorer.py:35`
- After the reorg: `ap1_inspect/scorer.py:35` (`ap1_scorer`)

**S3-G7-4 · medium · The two Inspect tasks build identical samples**
- What's wrong: `ap1_base` and `ap1_instruction_removed` build the same samples, use the same solver
  and send no system prompt; only the condition label differs, so the Inspect D7.1b contrast
  measures nothing.
- Where: `ap1_inspect/task.py:73-101`, `:129-162`
- After the reorg: `ap1_inspect/task.py:72-100` (`_build_dataset`), `:128-161` (`ap1_base`,
  `ap1_instruction_removed`)

**S3-G7-5 · medium · The Inspect solver calls the model once and never runs a tool**
- What's wrong: it calls `get_model().generate` once, not a tool loop (the docstring says
  `generate_loop`); a tool call is recorded with no return value, the calculator never runs, no
  result goes back to the model, and the final text is that first response's content, which may
  be empty or may accompany the tool call. The Inspect path cannot measure a tool-using model.
- Where: `ap1_inspect/solver.py:32-36`, `:47-55`
- After the reorg: `ap1_inspect/solver.py:32-36`, `:47-55` (`ap1_solver.solve`)

### G8: regression tools

**S3-G8-1 · low · `parse_resolved_config` does not stop at the next heading**
- What's wrong: with no JSON block in report §2 it reads the first JSON block of any later section,
  so the "resolved config" can come from elsewhere in the report.
- Where: `verify_run_seal.py:74-93`
- After the reorg: `tools/verify_run_seal.py:77-96` (`parse_resolved_config`)

**S3-G8-2 · low (low-medium) · A blank first transcript line, or an empty transcript, makes the transcript check disappear**
- What's wrong: neither PASS nor FAIL is reported, so a damaged transcript goes unreported. Extends
  T3-18.
- Where: `verify_run_seal.py:221-232`
- After the reorg: `tools/verify_run_seal.py:224-235` (`verify_run`)

**S3-G8-3 · low · An unparseable first transcript line, or a JSON number with a fraction in report §2, crashes the verifier**
- What's wrong: a traceback (`canonical_hash` refuses floats) where a FAIL with a reason is due.
- Where: `verify_run_seal.py:224`, `:130`
- After the reorg: `tools/verify_run_seal.py:227`, `:133` (`verify_run`)

**S3-G8-4 · low (low-medium) · The verifier always hashes the repository's `example/` and `reference/` files**
- What's wrong: there is no option to name a run's inputs, so a run made with other inputs
  (`--fixture-dir`, `--ap1-text` in the `src/ap1_run/` layout) cannot be verified. It fails; it
  never falsely passes.
- Where: `verify_run_seal.py:139-168`
- After the reorg: `tools/verify_run_seal.py:142-171` (`verify_run`)

**S3-G8-5 · low · A relative run path is joined to the repository root, not the working directory**
- What's wrong: from another directory, an existing path is reported as "report.md not found".
- Where: `verify_run_seal.py:256-258`
- After the reorg: `tools/verify_run_seal.py:259-261` (`main`)

**S3-G8-6 · low · `generate_findings.pct` rounds half-to-even**
- What's wrong: it uses the context default; `ROUND_HALF_UP` is imported and never used, so 6.25 %
  prints as 6.2. No published figure is a tie, so FINDINGS.md is unaffected.
- Where: `generate_findings.py:19`, `:35-40`
- After the reorg: `tools/generate_findings.py:19` (imports), `:41-46` (`pct`)

**S3-G8-7 · low · The base non-invocation Clopper–Pearson bound uses a fixed n = 500**
- What's wrong: true for the published runs (10 × 50), wrong for any other run.
- Where: `generate_findings.py:360-370`
- After the reorg: `tools/generate_findings.py:366-376` (`compute_figures`)

**S3-G8-8 · low · An empty run B raises `ZeroDivisionError`**
- What's wrong: `b_ops_per_exec` divides unguarded, while run A's equivalent is guarded; it should
  be a clear error.
- Where: `generate_findings.py:322`
- After the reorg: `tools/generate_findings.py:328` (`compute_figures`)

---

## S4-G: found while writing tests of correct behaviour

Found while writing failing-first tests, by test group (G4 transcript, G9 SPEC claims). Severities
are the test author's estimate.

**S4-G4-1 · medium · The round-0 request record holds the messages of later rounds**
- What's wrong: `adapter.send` stores the `messages` list it was given in `request_record` by
  reference, and the engine keeps appending to that list during the tool loop. So the transcript's
  round-0 request record (`request_sent.request_record.messages`) holds every message of the last
  request of the loop, not the 2 actually sent; the copy beside it, `request_sent.messages`, is
  correct. Nothing is lost, but the request record misstates what was sent in round 0; it is also
  why the published runs keep the intermediate assistant messages at all.
- Where: `adapter.py:121-127`; `engine.py:199-216` (appends to the same list)
- After the reorg: `src/ap1_run/foundation/adapter.py:121-127` (`send`);
  `src/ap1_run/execution/engine.py:199-216` (`_drive_tool_loop`)
- Breaks: SPEC R0.2 ("The request as sent — not as constructed — is recorded")

**S4-G9-1 · low · A missing released figure is written as the string `"None"`**
- What's wrong: for every outcome that releases no figure, `identify_figure` returns
  `released_figure: None`, and the runner writes `str(...)`, so the transcript's
  `figure_identification` records and `smoke_summary.json` say `"None"`; when the key is absent they
  say `''` instead.
- Where: `smoke_test.py:640`, `:795`
- After the reorg: `src/ap1_run/runner/executions.py:97`, `:252` (`score_execution`)

---

## REORG: found while reviewing the reorganisation pull requests

These concern code added by the reorganisation itself, so they have no location at `c8df9ca`. The
location is given at the head of the pull request that adds the code, with the function name.

**REORG-1 · low · The regression harness exits 0 when it runs no scenarios**
- What's wrong: `run_regression.py` returns 1 only when a scenario run fails, and otherwise 0. With
  no scenario files found (a `scenarios/` directory with no `.json` files) or with `--runs 0`, it
  runs nothing, prints "0/0 scenario runs match golden output" and exits 0, so a run that checked
  nothing reads as a pass to anything that looks only at the exit code. No published result
  depends on it; rated low because it is test tooling, not the instrument. The CI job for the
  baseline checks the summary line as well as the exit code.
- Where: `tests/regression/run_regression.py:341-372` (`main`), at the head of the pull request
  that adds the regression baseline
- After the reorg: `tests/regression/run_regression.py` (`main`; the file does not move, but its
  lines shift as the harness grows)
- Breaks: no AP-1 or SPEC clause; the harness's own purpose, that a change in behaviour is
  detected (`tests/regression/README.md`)

---

## Maintainer decisions

Some findings don't say on their own what correct behaviour is. SPEC.md might contradict itself,
say nothing, or disagree with the code. The decisions below settle those cases, so that a test
can assert one behaviour. Each has an ID that tests and PRs can cite.

They are the maintainer's decisions of 20 October 2026 on a list of every SPEC-versus-code
disagreement that affects what a test asserts. Quotations are the maintainer's words. The list
named no finding IDs; the IDs below are this register's mapping of its items.

### DEC-1: where SPEC and the code disagree, follow SPEC
> "where SPEC and the code disagree, follow SPEC, unless SPEC is out of date. The published
> results stay pinned to paper-2026-10, and if anything ever touched a published figure we'd
> record it by addition, as before."

This is the default for every finding below where SPEC and the code differ. Where the code is
right instead, the fix corrects SPEC. The cases the maintainer decided for the code are DEC-2 and
DEC-5.

### DEC-2: STRUCTURAL_CONSTANTS is the value 1 only
SPEC says "the value 1 only" in one place (SPEC.md:613) and "0 and 1" in another
(SPEC.md:1048). The code has 1 only.
> "1 only, as the code does. A literal 0 can be a fabricated value, so treating it as
> originated is the safer choice, and it's what the published runs used. I'll correct SPEC 1048
> by addition."

0 is not a structural constant: a literal 0 is originated unless another step grounds it (a
`monthly_fee` of "0.00", for example, grounds it at step 1). Settles the `STRUCTURAL_CONSTANTS`
item of T3-74.

### DEC-3: the report says that inter-rater agreement was not computed
SPEC R3.3 and the Phase E gate require kappa in the report when two scorers are supplied, but
SPEC §10 (`SPEC.md:890`) says agreement is computed outside the runner ("NOT BUILT by design").
> "the requirement stands for any conformance evaluation, but this version of the runner
> doesn't compute it. Could the test assert that, when two scorers are supplied, the report
> says explicitly that agreement was not computed (external), rather than leaving it out?
> Whether the runner should compute it can be a v1.4 question."

Settles what the report says for T3-23. It does not build agreement statistics or a way to read
scorers' marks back; today the runner writes blank sheets for two scorers and reads nothing back.

### DEC-4: a negated constant does not ground
The code grounds a negated declared constant because its magnitude matches. For example, −12
grounds against a 12-month constant. SPEC has no such rule.
> "a negated source value grounds only through a declared negation transformation, and a
> negated constant does not."

Settles T3-5. Only step 1b's magnitude match goes; a negative operand can still ground by any
other step.

### DEC-5: modules without a SPEC section are defined, for now, by the code
D7.2(b) operation correctness, release coverage and the sign-inversion findings have no SPEC
section of their own: SPEC §10 has a row for each, SPEC §12.10 lists their files, and SPEC R3.3
says how D7.2(b) results are reported.
> "please take the code as the provisional definition for now. Marking those tests provisional
> until the SPEC sections exist would be perfect."

Their tests assert today's behaviour and are marked provisional; where SPEC does say something
(R3.3's reporting), DEC-1 applies. This does not make the defects found inside these modules
correct behaviour (T3-40, T3-62, T3-84, S3-G4-3 to S3-G4-5, S3-G5-1, S3-G5-2). Settles T3-73 for
these three modules only; T3-73's DOI and runner-source sealing are not covered.

### DEC-6: where SPEC requires something the code doesn't do, follow SPEC
> "For everything in C, please follow SPEC."

"C" was the third group of the list the maintainer answered: the items where SPEC requires a
behaviour the code lacks. The agreed direction for these findings is to follow SPEC:
- **Architecture and transcript:** T3-21 (two passes), V12-3 and T3-52 (raw responses; egress),
  T3-35 (EV-0 round).
- **Configuration and numbers:** T3-51 (defaults), T3-12 (minimum n), T3-58 and T3-61 (float),
  T3-27 (rounding), T3-41 (separators), T3-60 (determinism), T3-20 (hash checks) and T3-50 (line
  endings).
- **Sealing:** T3-48 (expected values), T3-47 (timestamp), T3-68 (AP-1 text), T3-17
  (re-verification), T3-7 (ground-truth guards), T3-75 (lookup collision), T3-46 (perturbation
  guard).
- **Scoring:** T3-1 (EV-0 as success), T3-10 (empty response), T3-38 (other tools), T3-46 and
  T3-90 (DPR), T3-75 (structured answer), T3-63 (unreadable response), T3-32 (D1), T3-4 (D2),
  T3-16 (OPERANDS-UNOBSERVABLE), T3-42 (absent intermediates), T3-34 (quantisation findings),
  T3-64 (originated-operand listing), T3-26 (D7.3), T3-13 (AP-1 §6.8 outcomes).
- **Reporting and verification:** T3-35 (non-outcome cells), T3-22 (planted defects), and the
  Inspect scorer's departures from SPEC's figure-identification rules (T3-43).

Following SPEC does not fix every detail. For T3-26, SPEC R2.5 names the required operation but
not which of several of its returns to compare. For T3-47, sealing the timestamp conflicts with
SPEC R1.1's "Sealing the same inputs twice yields identical hashes". Those choices are left to the
fixes.

Findings not listed here were not in the list the maintainer answered; where SPEC and the code
disagree on them, DEC-1's default applies. T3-11 (what n counts, on which SPEC is silent) is not
covered by any decision.

The Inspect wrapper is unsupported for now; README.md says so under its requirements, from the
move to `src/ap1_run/` on. That bears on T3-43, T3-44 and S3-G7-3 to S3-G7-5.
