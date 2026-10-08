# Pleading drafting rules

Apply these rules when generating or substantively reviewing a complaint, arbitration application, civil answer or arbitration answer.

The public external-expression boundary in `legal-os-unified-intake/references/external-expression-boundary.md` supplies the audience rule. R13–R16 apply it to pleadings without replacing procedural disclosure duties or restricting complete internal/client analysis.

## R1 — Resolve the procedure variant first

Classify `procedure_type`, `pleading_role` and `document_variant` before template resolution. Civil litigation, commercial arbitration, labour/personnel arbitration and other procedures do not share identical requests, cost rules or mandatory fields. Stop with `PROCEDURE_VARIANT_REQUIRED` when the variant cannot be established from current material.

## R2 — Analyse broadly, plead through a controlled route

The internal work product may identify all reasonable claims, defences, alternatives and risks. Confirm the current procedural or substantive objective and requested relief or defence scope from current material before selecting the external route. If either remains unresolved, mark it pending in internal analysis and do not complete it by inference in the external pleading. The external pleading should use the strongest compatible route that covers the requested outcome without unnecessary admissions or exposure. Add an alternative position only when the primary route is incomplete and the alternative is factually and legally compatible.

## R3 — Applications must establish each requested remedy

For every material claim or defence, connect internally:

`confirmed objective → executable relief or defence and calculation → legal/procedural elements → material facts → evidence → jurisdiction, limitation, required procedure and verified current authority → legal conclusion`

Adapt the chain to the document's function; do not mechanically expose the entire internal chain in an external pleading. Do not replace facts with abstract legal conclusions or omit an element merely to keep the document short. High information density does not justify omitting necessary logical links, procedural information, amount basis or issue explanation.

## R4 — Answers use an issue-scope gate

Respond to the opposing party's actual claims, alleged facts and legal grounds. Do not volunteer a new claim basis, admit an unproved fact, open an unnecessary adverse exception, or disclose internal fallback strategy. Screen possible defences in this order only as applicable: dispositive procedure; prior agreement, satisfaction or extinguishment; missing elements; amount/calculation; compatible alternative defence.

## R5 — Use conclusion-led headings

Each substantive heading should state a conclusion a decision-maker could adopt. Use the unit:

`conclusion → material facts → evidence anchor → necessary legal evaluation → effect on the claim or defence`

Avoid empty headings such as “relevant circumstances” and repeated conclusory adjectives.

## R6 — Cite authority by function

Before placing authority in the external pleading, ask whether it decides the issue, is needed to complete the claim or defence, responds to an argument actually raised, and whether its proviso or exception would unnecessarily enlarge an adverse issue. Verify current status and an official or otherwise authoritative source. Keep nonessential or contingency authority in the internal authority package.

## R7 — Do not exceed the evidence

Prefer complete originals and signed records to screenshots, OCR or recollection. Keep ambiguous handwriting, amounts, dates or identities unverified. A payment record proves only the parties, time, amount and displayed purpose shown on it; do not infer an unsupported allocation or full settlement. Record the source of each material fact. In internal work, distinguish evidence-supported facts, party statements, opponent assertions, facts still to be proved, disputed/unconfirmed facts, legal evaluations and inferences. An external pleading may state a fact to be proved when necessary, but must not describe it as established beyond source support.

## R8 — Generate the pleading and evidence catalogue as a pair

Every complaint, application or answer has `paired_evidence_catalog_required=true`. Only a request limited to strategy, outline or isolated wording falls outside this rule. If evidence is incomplete, create a `待补证 / 内部草稿` catalogue rather than omitting the paired artifact.

## R9 — No independent evidence-source chapter

Do not create an independent “证据和证据来源” or equivalent chapter inside a complaint, application or answer. Use concise evidence anchors in the relevant factual paragraph when useful. Put evidence number, name, page range and proof purpose in the independent evidence catalogue.

## R10 — Keep the external catalogue lean and the internal map complete

The external catalogue normally uses `编号 | 证据名称 | 页码 | 证明事项`. A proof purpose must identify the claim, element, material fact or defence it supports. The private fact–evidence map additionally records source, formation date, original status, authenticity/completeness risk, corresponding proposition, gaps and review state.

## R11 — Test alternative defences for compatibility

Place an alternative defence in the external answer only if the primary defence does not fully cover the claim, it does not negate a key primary fact or reasonably read as an admission, it has evidence and verified law, and disclosure does not materially expand the opposing party's attack path. Otherwise keep it in the internal hearing plan.

## R12 — The template controls the shell, not the adjudication path

The template controls visual identity, minimum functional sections and signature placement. It does not control paragraph count, create an unraised issue, supply a missing fact/evidence/authority, preserve a procedure-inapplicable cost request, or restore an evidence-source chapter. If the selected variant conflicts with the matter, stop with `TEMPLATE_VARIANT_REQUIRED` rather than silently converting it into a final document.

## R13 — Initial claimant pleadings use a single-party stance gate

For a complaint, arbitration application, payment-order application or equivalent first request filed for a claimant, applicant or creditor, build the external document around four questions only:

1. What legal relationship connects the parties?
2. What supported obligations has the represented party performed?
3. What obligation is due from the opposing party, and how has it been breached?
4. How do verified facts, evidence and authority establish each requested remedy?

Do not volunteer a hypothetical opponent defence, opponent evidence roadmap, opponent proof deficiency, proposed allocation of the opponent's burden, adjudicator investigation plan, nonessential adverse authority or the represented party's complete contingency response. Do not state an unverified favourable fact as established. Keep these items in the internal analysis, hearing plan, authority package or a separate procedural application as applicable.

Keep stage boundaries explicit: an initial or start-up pleading establishes the requested relief and necessary foundation; a responsive or argumentative pleading develops issues actually raised or formed in the proceeding. Do not import hypothetical response analysis into an initial pleading merely because an adverse fact could matter.

## R14 — Exceptions require a recorded function

An initial claimant pleading may address an adverse proposition or use a compatible alternative position only when at least one of the following is true:

- the opposing party has actually raised it in supplied correspondence, a prior pleading, an objection or another identified source;
- it is necessary to establish an element, jurisdiction, limitation, admissibility, a condition precedent or another required procedure;
- the primary route cannot fully support the requested outcome and the alternative is factually, evidentially and legally compatible;
- the selected court, tribunal, institution or document variant expressly requires the information.

Record the source, purpose and compatibility review in the internal workspace. Do not use an exception to introduce an unsupported concession, broaden an adverse issue or reveal internal fallback strategy.

## R15 — Separate content by procedural function

- **Initial complaint or application:** requested relief, supported performance, opposing breach, necessary facts, evidence anchors and verified authority serving the claim.
- **Internal matter analysis:** possible defences, risk, burden analysis, evidence gaps, contrary authority and response options.
- **Hearing plan:** questions, contradictions and follow-up paths.
- **Evidence comments:** responses to evidence actually submitted, including authenticity, legality, relevance and weight as applicable.
- **Closing or agency submission:** developed issues and arguments actually raised in the proceeding.
- **Investigation or evidence-production request:** the specific procedural request and its verified basis, kept separate from the initial pleading unless the selected procedure requires otherwise.

When external text crosses these boundaries, remove it from the external artifact and preserve it in the correct internal artifact; do not destroy the underlying analysis.

## R16 — Conditional language triggers contextual review

Terms such as “如果”, “即使”, “可能”, “如经查明” and “若对方不能证明” trigger `REVIEW_REQUIRED` in an initial claimant pleading. They do not automatically fail the document. Retain them only when R14 is satisfied and the sentence remains supported, compatible and necessary; otherwise replace the sentence with a positive, evidence-supported statement or move it to the internal workspace.

### Case-use control for initial claimant pleadings

- Use a case only when its verified adjudicative proposition materially supports a requested remedy or resolves an issue that must be addressed.
- Do not introduce a nonessential adverse case, summarize the opponent's case theory or provide a roadmap for distinguishing authorities not yet in issue.
- Keep directly relevant contrary material and contingency research in the internal authority package so that external selectivity does not become internal confirmation bias.
- State the adjudicative proposition concisely. Avoid long factual narratives.
- Do not use a case externally unless its source, identifier, adjudicative level and verification status satisfy the authority-package controls.

### Third-party-payment clause scenario

When the represented claimant relies on a direct payment obligation and the contract also refers to payment by a third party, structure the initial pleading in this order, but only to the extent supported by the actual contract, performance record and verified authority:

1. contract formation and effectiveness;
2. the represented party's delivery, service or work;
3. acceptance, settlement or other supported payment basis;
4. the amount and due date of the direct payment obligation;
5. the legally supported character and effect of the third-party-payment wording;
6. why an identified third-party commercial arrangement does or does not affect the direct obligation;
7. the established default and resulting liability;
8. executable relief, calculations and procedural costs where permitted.

Do not speculate about whether the third party paid, whether the opposing party pursued collection, what upstream records should be produced or whether a condition should be deemed fulfilled. Address those matters later only if evidence or an actual defence makes them material. Do not hard-code the substantive effect of third-party-payment wording across matters.

## Pair consistency gate

- Every pleading evidence reference must resolve to one catalogue item.
- Every catalogue item must support at least one claim, element, material fact or defence.
- Renumbering, renaming or changing a proof purpose requires synchronized updates across both artifacts.
- Unknown page ranges remain `待编页`; never invent pagination.
- Distinguish evidence submitted by the represented party from material filed by another party.
- Keep related pleadings, evidence catalogues, written submissions and hearing statements substantively consistent in party identity, dates, amounts, legal relationship, performance and core facts. If new evidence, verification, relief or procedure requires a change, record the difference and legal effect internally rather than leaving an unexplained material conflict.
