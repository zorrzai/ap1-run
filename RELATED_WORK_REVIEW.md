# Related Work Review

**Prior art and adjacent literature bearing on AP-1 and the reference runner**

ZORRZ Financial Inc. · Reviewed 5 August 2026 · For the AP-1 v1.3 disposition record

---

## Purpose and method

AP-1 v1.3 Appendix B cites related work as of July 2026. This review re-examines the field against publicly accessible sources as of 5 August 2026, with one question governing every entry:

> **Does this work measure whether a numeric operand supplied to a computation traces to an authoritative source?**

Not whether the answer was correct. Not whether the tool call was permitted. Not whether the value came from an untrusted source. Whether it came from **anywhere at all**.

Where the answer is no, the entry records what the work does measure and why the distinction matters. Where a work is closer to AP-1 than Appendix B acknowledges, it is recorded as a **citation gap** for the adopted version.

**This review is not exhaustive and does not claim to be.** It records what was examined, what was found, and what remains unread.

---

## 1. The findings that matter

**Parameter-level operand provenance is an active research area, and AP-1 v1.3 cites none of it.**

**Agent-Sentry** (Sequeira, Damianakis, Iqbal, Psounis; arXiv:2603.22868, v1 24 March 2026, v2 8 May 2026). A runtime defence that **records a provenance graph for every agent execution capturing where every tool argument value came from**, and learns the structural and provenance patterns of legitimate behaviour from prior executions. Three layers: a classifier over provenance-graph features returning allow / ambiguous / block; a provenance-aware allowlist verifying that sensitive argument values come from trusted sources; and an LLM judge for intent alignment. Blocks 94.3% of injections while allowing 95.1% of benign executions on AgentDojo and AgentDyn, without modifying the agent, its tools, or the model.

**AuthGraph** (Wang et al.; arXiv:2605.26497, 26 May 2026) — *Aligning Provenance with Authorization: A Dual-Graph Defense for LLM Agents*. Constructs an authorization graph and an execution-provenance graph and aligns them. States: *“To our knowledge, AuthGraph is the first agent security defense to structurally compare authorization specifications against execution provenance at the parameter-source level.”* Reduces attack success from 40% to 1% on AgentDojo, outperforming CaMeL, DRIFT and Progent.

**Auditing Provenance Sensitivity in LLM Agent Action Selection** (Liao; arXiv:2607.20827, 23 July 2026). Its opening premise is a sibling of AP-1’s: *“evidence can be relevant without being authorized to determine a decision, so a correct action need not be grounded only in permitted evidence.”* Holds task, proposition, position and policy fixed while varying only source authority, across 450 controlled next-action tasks. Trusted and untrusted variants produce different actions in 5.4% of competing cases against 1.7% of supporting cases.

**From Agent Traces to Trust** (Wang et al.; arXiv:2606.04990, 3 June 2026) surveys the area and formalises **parameter-level as a distinct tracing granularity** alongside run-level, step-level, tool-call-level, claim-level and token-level.

All four predate or closely follow AP-1 v1.3. None appears in Appendix B.

**This is a citation gap.** The contribution AP-1 claims survives it, for the reason set out in §2 — but a reader familiar with this literature would expect it cited, and its absence reads as unfamiliarity rather than as a considered distinction.

---

## 2. The distinction, stated once and applied throughout

The adjacent literature is overwhelmingly **enforcement against untrusted sources**. AP-1 D7.2(a) is **measurement of admissibility**. These are different threat models and they fail in opposite directions.

| | Enforcement literature | AP-1 D7.2(a) |
|---|---|---|
| **Question** | Did this value come from somewhere *untrusted*? | Did this value come from *anywhere*? |
| **Threat** | External content reaching a privileged argument | A figure with no basis in source data |
| **Timing** | Runtime, pre-execution | Post-hoc, evaluative |
| **Failure it prevents** | Injected instruction becomes an email recipient | Fabricated operand becomes a reported figure |
| **Output** | Allow / deny / sandbox | An admissibility profile with declared evidence classes |

**The consequence, and it is the load-bearing point:** a value the model fabricated from nothing has no origin to taint, so taint-propagation systems pass it by construction — there is no untrusted source to detect, because there is no source. Allowlist and graph-alignment systems fail closed on it instead: a value with no provenance edge fails a trusted-source check. But blocking is not measuring. Neither produces a rate, a denominator, or an evidence class for the no-source case; they decide, per action, whether to proceed. AP-1 D7.2(a) reports it as a measured outcome with its population and its bound.

This is the same relationship AP-1 already draws with ToolGate in Appendix B. Enforcement mechanisms answer *should this call proceed*. AP-1 answers *can this figure be entered into a record*.

---

## 3. Information-flow control and runtime enforcement

**FIDES** — *Securing AI Agents with Information-Flow Control* (Costa, Köpf, Kolluri, Paverd, Russinovich, Salem, Tople, Wutschitz, Zanella-Béguelin; Microsoft; arXiv:2505.23643). A formal model characterising the class of properties enforceable by dynamic taint-tracking, and a planner that propagates confidentiality and integrity labels through messages, actions, tool calls and results, executing consequential actions only where a policy over those labels permits. Evaluated on AgentDojo. Implementation published.

*Measures operand provenance:* No. Labels are trust classifications attached to data that has an origin. An operand with no origin carries no label.

**CaMeL** — *Defeating Prompt Injections by Design* (Debenedetti et al., arXiv:2503.18813). Separates control flow from data flow so external data cannot influence agent control decisions.

**NeuroTaint** — *Ghost in the Agent: redefining information flow tracking for LLM agents* (Cai et al., 2026). Taint propagation across semantic transformations, addressing the case where a value is transformed by the model rather than copied.

*Closest of the enforcement family to AP-1’s problem*, because semantic transformation is precisely where naive membership checks fail. But the object tracked is still a tainted origin, not the absence of one.

**AgentSpec** (Wang et al., 2025), **AgentBound** (Bühler et al., 2025), **Progent** (arXiv:2504.11703). Specification-based, boundary-oriented and privilege-based runtime enforcement.

**Assessment.** This family is mature, well-resourced — Microsoft Research, Google DeepMind — and orthogonal to AP-1. None produces an admissibility measurement. Some would block a fabricated operand at runtime; none reports one as a measured outcome. AP-1 should cite FIDES, CaMeL and NeuroTaint as the enforcement counterpart to its measurement, and state the asymmetry explicitly.

---

## 4. Provenance representation and observability

**PROV-AGENT** (Souza et al., 2025) adapts W3C PROV-DM to agentic workflows, modelling prompts, responses, decisions and tool interactions. **AgentOps** (Dong et al., 2024) and **AgentTrace** (AlSayyad et al., 2026) provide structured operational, cognitive and contextual logging. **TRAIL** (Deshpande et al., 2025) and **LADYBUG** (Rorseth et al., 2025) localise failures within recorded traces. **OpenTelemetry** (2026) standardises distributed traces and is the de-facto substrate.

*Measures operand provenance:* No. These record what happened. Whether a recorded operand had a basis in source data is not a question they pose.

**The relationship is worth stating plainly:** observability produces the structural record; AP-1 D7.7 requires exactly such a record as its evidence base, and grades it by independence — `EV-2 PLATFORM-STRUCTURAL` is a serving-layer tool-call record of the kind these systems emit. AP-1 consumes this literature rather than competing with it.

---

## 5. Attribution and claim-level grounding

**ALCE** (Gao et al., 2023), **FActScore** (Min et al., 2023), **SourceCheckup** (Wu et al., 2024), **RAGAS** (Es et al., 2024), **ARES** (Saad-Falcon et al., 2024), **RAGChecker** (Ru et al., 2024), **RAGTruth** (Niu et al., 2024), **PaperTrail** (Martin-Boyle et al., 2026).

*Measures operand provenance:* No, and the reason is structural. Faithfulness asks whether a generated claim is **supported by retrieved context**. A computed figure is not in the retrieved context — it is *derived from* it. Faithfulness as defined in this literature does not address arithmetic derivation.

SourceCheckup’s finding is directly relevant and worth citing: a cited source may be topically relevant without supporting the specific claim. The operand analogue — a value that resembles a source field without being derived from it — is what D7.2(a)’s exact-match rule exists to catch.

---

## 6. Tool-use benchmarks

**BFCL v4** scores function-calling accuracy across single-turn, multi-turn, parallel and agentic scenarios. **τ-bench** and **TAU2** evaluate tool-agent-user workflows under domain policies. **ToolLLM / ToolBench**, **AgentBench**, **WebArena**, **MCP-Atlas**, **Toolathlon**.

**When2Call** (Ross, Mahabaleshwarkar & Suhara, NAACL 2025) — already cited in AP-1 D7 — measures whether a model correctly judges *when* a tool is required.

*Measures operand provenance:* No. These measure capability — did the model call the right function with arguments matching a reference. AP-1’s question is orthogonal: **is the decision the model’s to make at all**, and did the values it passed come from source.

**A benchmark scoring parameter accuracy against a reference is not measuring provenance.** It compares arguments to an expected set. An operand that matches the expectation by coincidence scores identically to one derived from source.

---

## 7. Aerospace and safety-critical evaluation

**ALUE** — *Aerospace Language Understanding Evaluation* (FAA and MITRE, September 2025; AIAA 2025-3247; github.com/mitre/alue). Aviation-specific benchmark covering multiple-choice QA, summarisation, RAG, extractive QA, hazard classification, and token classification of air-traffic-control communications. Metrics combine traditional measures — recall@k, token-level F1 — with **LLM-based evaluation**: context relevancy, composite correctness, claim decomposition.

*Measures operand provenance:* No. ALUE is a language-understanding benchmark. There is no computation to invoke and no operand to trace.

**Two points AP-1 must state rather than leave implicit.** ALUE is the closest existing benchmark to an aerospace LLM assurance conversation among the works surveyed here — domain-specific, safety-critical, institutionally backed — and AP-1 does not cite it. And ALUE uses **LLMs as judges** in its correctness metrics, which AP-1 explicitly forbids in the answer-key path. That difference is defensible and must be framed as *appropriate to different problems*, never as AP-1 being stricter: claim decomposition over long-form aviation prose is not addressed by any deterministic method among the works surveyed here, while numeric ground truth does.

**VALOR** (NASA/TM–20260000076, Ames Research Center, January 2026). Already cited. Retrieval faithfulness, retrieval quality, uncertainty, robustness via Drop-in-Performance Ratio. No invocation dimension.

**PilotBench** (Wu et al., 2026). Evaluates LLMs as agents on flight trajectory and attitude prediction from real general-aviation telemetry, scored on a composite of regression accuracy and instruction/safety adherence.

*Closest aerospace work to a numerical measurement.* But it scores predictive accuracy against ground truth, not the provenance of values entering a computation.

**Pre-Flight** (arXiv:2607.01829, July 2026). Aviation operational knowledge, multiple-choice.

**Trusted AI Framework** (The Aerospace Corporation, with JPL adaptation — *Space Applications of a Trusted AI Framework: Experiences and Lessons Learned*, NTRS 20230005782; *Adapting a trusted AI framework to space mission autonomy*, IEEE AERO 2022). Framework for the implementation, assessment and control of AI-based applications, tailored into mission assurance guidance for the space domain.

**Not cited in AP-1 v1.3, and it should be.** It is the institutional framework for AI assurance in the space domain, and D7’s contribution is best expressed as a metric family that framework does not currently contain.

**NASA Software Engineering Handbook §7.25**. Already cited. States there is no provable means to evaluate an AI/ML system against safety requirements for safety-critical applications.

---

## 8. Deterministic inference

**Thinking Machines Lab** (September 2025), *Defeating Nondeterminism in LLM Inference*. Batch-size-dependent reduction strategies rather than floating-point non-associativity as the principal source of inference non-determinism; batch-invariant kernels published; adopted in mainstream serving frameworks at a reported throughput cost.

Already cited and load-bearing: it is the reason D2 was reframed in v1.3 from counting distinct answers to classifying the mechanism. **And it sharpens AP-1’s central claim** — batch-invariant inference makes a model’s fabrications reproducible along with everything else. Determinism is evidence about process control, not about provenance.

---

## 9. Position

Against this body of work, three things appear specific to AP-1:

**The measurement/enforcement inversion.** Most provenance systems found operate at runtime to prevent unsafe execution. The exceptions in this survey — Liao’s controlled audit, and the trace-recording work in §4 — record provenance without measuring admissibility. AP-1 operates post-hoc to establish whether a figure is admissible. The threat models are complementary and neither substitutes for the other.

**The no-source case.** The literature tracks values from origins. AP-1’s primary detection target is a value with no origin — which every taint system passes by construction, because there is nothing to taint.

**Invocation as a control rather than a capability.** When2Call and the tool-use benchmarks measure whether a model *decides well*. AP-1 measures whether the decision is the model’s to make, and reports the answer with its evidence class.

**None of these is a claim of priority over the ideas above.** They are claims about what AP-1 packages and measures that the examined work does not.

---

## 10. Citation gaps to close in the adopted version

| Work | Why |
|---|---|
| Agent-Sentry (arXiv:2603.22868) | Provenance graph of tool-argument sources; closest operational prior art to D7.2(a) |
| AuthGraph (arXiv:2605.26497) | Claims first structural comparison of authorization against provenance at parameter-source level |
| Auditing Provenance Sensitivity (arXiv:2607.20827) | "A correct action need not be grounded only in permitted evidence" — sibling premise |
| From Agent Traces to Trust (arXiv:2606.04990) | Survey formalising parameter-level granularity |
| FIDES (arXiv:2505.23643) | Information-flow control; the enforcement counterpart |
| CaMeL (arXiv:2503.18813) | Control/data flow separation |
| NeuroTaint (Cai et al., 2026) | Taint across semantic transformation |
| PROV-AGENT (Souza et al., 2025) | W3C PROV applied to agentic workflows |
| ALUE (FAA/MITRE, 2025) | Most relevant aerospace LLM benchmark; not cited |
| Trusted AI Framework (Aerospace Corp / JPL) | Institutional AI assurance framework for the space domain |
| PilotBench (Wu et al., 2026) | Numerical aerospace evaluation |
| SourceCheckup (Wu et al., 2024) | Relevance-without-support; the operand analogue |

**AP-1 v1.3 is not edited.** It is published with a DOI and its comment window is open until 30 September 2026. These entries are recorded here for the disposition record and for Appendix B of the adopted version, per §10.5.

---

## 11. Standing obligation

This review records a point-in-time position. The field is active: four of the works above were published within five months of this review, and two within six weeks of AP-1 v1.3.

The review is repeated before any technical engagement in which AP-1’s contribution is asserted, and before any subsequent version is adopted. A position on prior art that is not re-established is not a position.

---

*Reviewed 5 August 2026. Sources examined are publicly accessible. This document will go stale and does not claim exhaustive coverage of an active field.*
