---
name: us-state-privacy-navigator
title: US State Privacy Navigator
description: Cross-jurisdictional analysis engine for the US state consumer privacy law patchwork (CCPA/CPRA, VCDPA, CPA, CTDPA, UCPA, TDPSA, OCPA, FDBR, MCDPA, ICDPA, INCDPA, TIPA, DPDPA, NJDPA, NHDPA, NDPA, KCDPA, MODPA, MCDPA-MN, RIDTPPA, and emerging laws). Use this skill whenever the user asks anything involving applicability of US state privacy laws, CCPA/CPRA compliance, multi-state privacy compliance, consumer rights requests (DSARs/access/deletion/correction/opt-out/appeal), notice-at-collection, sensitive personal information, sale or sharing of personal information, targeted advertising, profiling, automated decision-making at the state level, universal opt-out mechanisms (Global Privacy Control), risk assessments under state privacy laws, data broker registration, kids' or teens' privacy at the state level, employee/HR data privacy, B2B data privacy, gap analysis or remediation roadmaps for a US business, or drafting state-compliant privacy notices and disclosures. Trigger broadly
  whenever a US business asks 'do I need to comply with [state] privacy law?', 'what do I do about [right]?', 'how do I handle a consumer request from [state]?', or any variation. Also use when a federally-regulated entity (HIPAA covered entity / business associate, GLBA-regulated financial institution, COPPA-subject service, FERPA-regulated educational institution or ed-tech vendor, FCRA-touching consumer reporting agency or furnisher) asks how state privacy law overlays the federal regime — see `references/federal-overlays.md`. Do NOT use this skill for HIPAA / GLBA / COPPA / FERPA / FCRA standalone analysis (use a sectoral resource), GDPR-only questions, or non-US privacy regimes.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/us-state-privacy-navigator
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
sources:
- title: Ag priorities
  path: references/ag-priorities.md
- title: Applicability matrix
  path: references/applicability-matrix.md
- title: Controller duties
  path: references/controller-duties.md
- title: Defense arguments
  path: references/defense-arguments.md
- title: Enforcement
  path: references/enforcement.md
- title: Federal overlays
  path: references/federal-overlays.md
- title: Kids and teens
  path: references/kids-and-teens.md
- title: Rights comparison
  path: references/rights-comparison.md
- title: Sensitive data
  path: references/sensitive-data.md
- title: Ca
  path: references/states/ca.md
- title: Co
  path: references/states/co.md
- title: Ct
  path: references/states/ct.md
- title: De
  path: references/states/de.md
- title: Fl
  path: references/states/fl.md
- title: Ia
  path: references/states/ia.md
- title: In
  path: references/states/in.md
- title: Ky
  path: references/states/ky.md
- title: Md
  path: references/states/md.md
- title: Mn
  path: references/states/mn.md
- title: Mt
  path: references/states/mt.md
- title: Ne
  path: references/states/ne.md
- title: Nh
  path: references/states/nh.md
- title: Nj
  path: references/states/nj.md
- title: Or
  path: references/states/or.md
- title: Ri
  path: references/states/ri.md
- title: Tn
  path: references/states/tn.md
- title: Tx
  path: references/states/tx.md
- title: Ut
  path: references/states/ut.md
- title: Va
  path: references/states/va.md
- title: Universal opt out
  path: references/universal-opt-out.md
- title: Dsar routing
  path: references/workflows/dsar-routing.md
- title: Gap analysis method
  path: references/workflows/gap-analysis-method.md
- title: Intake questionnaire
  path: references/workflows/intake-questionnaire.md
- title: Status determination
  path: references/workflows/status-determination.md
---

# US State Privacy Navigator

Cross-jurisdictional applicability, gap analysis, and deliverable generation for the US state consumer privacy patchwork. Authored for legal practitioners and privacy professionals who need defensible, citation-ready output rather than vendor-style checklists.

## What this skill does

1. **Applicability triage.** Given a business profile, returns a per-state applicability verdict (Applies / Likely Applies / Does Not Apply / Insufficient Info) with the threshold reasoning shown.
2. **Gap analysis.** Compares current practice to each applicable law's controller obligations and consumer rights, produces a severity-scored issue log, and prioritizes remediation.
3. **Deliverables.** Generates a memo (Markdown) and a formal client-ready deliverable (.docx) including the applicability matrix, gap log, and remediation roadmap. Where requested, drafts state-compliant notice clauses keyed to the specific obligations triggered.
4. **DSAR / consumer-rights orchestration.** Routes a single consumer request to the correct response procedure based on the requester's residency, the right invoked, and the controller's status under each law.

## When to consult what

This SKILL.md is the orchestrator. The depth lives in `references/`. Read references on demand — never preload all of them.

| If the user is asking about... | Read |
|---|---|
| Whether a law applies to their business | `references/applicability-matrix.md`, then the relevant `states/<xx>.md` |
| What rights consumers have / how to fulfill | `references/rights-comparison.md` + relevant state file |
| What the controller must *do* (notices, contracts, assessments) | `references/controller-duties.md` + relevant state file |
| Sensitive data, special categories, opt-in vs opt-out | `references/sensitive-data.md` |
| Global Privacy Control / universal opt-out | `references/universal-opt-out.md` |
| Kids/teens, schools, COPPA interaction | `references/kids-and-teens.md` |
| **Entity is HIPAA-covered, GLBA-regulated, COPPA-subject, FERPA-related, or FCRA-touching** — entity-level vs. data-level exemption diagnostic per state | **`references/federal-overlays.md`** |
| Penalties, AG enforcement, private right of action, cure periods | `references/enforcement.md` |
| **What an AG is actually likely to enforce, by state** | **`references/ag-priorities.md`** |
| **Analogous prior enforcement actions for a given gap** | **`scripts/precedent_match.py` against `references/enforcement_actions.json`** |
| **The binding constraint across multi-state operations** | **`scripts/conflict_resolver.py`** (compliance-ceiling synthesis) |
| **Litigation-defense framing — what controllers can argue** | **`references/defense-arguments.md`** |
| **Controller / processor / third-party status (per data flow)** | **`references/workflows/status-determination.md`** |
| Single state deep-dive | `references/states/<xx>.md` |
| Running a structured intake before answering | `references/workflows/intake-questionnaire.md` |
| Scoring gaps and prioritizing remediation | `references/workflows/gap-analysis-method.md` |
| Routing a specific consumer request | `references/workflows/dsar-routing.md` |
| Drafting model clauses for notices | `assets/notice-clauses/*.md` |
| **Pre-publication QA on memo citation discipline** | **`scripts/citation_audit.py`** |

## Core operating principles

These are not suggestions. They preserve the defensibility of any analysis this skill produces.

1. **Statutes over recollection.** State privacy law has changed faster than most training data. When the user names a state or cites a code section, treat the reference files as ground truth and flag any conflict between the user's recollection and the reference. If neither the references nor the user supplies a citation for a contested point, say so explicitly — never fabricate code sections, regulatory citations, or AG enforcement actions.
2. **Applicability first.** Never analyze obligations until you have run applicability through the threshold tests. A business that does not meet a state's threshold has no obligations under that statute; pretending otherwise wastes the user's time and makes the work product unusable.
3. **Status before duties.** US state privacy laws split obligations between *controllers* and *processors* (CA uses *business* / *service provider* / *contractor* / *third party*; the other 19 use *controller* / *processor*). Identify the entity's status under each applicable law before assigning duties.
4. **Personal information ≠ consumer.** Most state laws exclude employee, applicant, B2B contact, and certain HIPAA/GLBA/FCRA-covered data from "consumer" or from coverage entirely. California's CCPA/CPRA covers employees and B2B; the other states generally do not. Apply the entity-and-data-type filter before assuming a duty attaches.
5. **Distinguish "sale" from "sharing" from "targeted advertising" from "profiling."** These are statutorily distinct and each triggers different opt-outs and disclosures. Sloppy collapsing of these terms is the most common error in vendor compliance work; it must not appear in this skill's output.
6. **Cite as you go.** Every non-trivial obligation, threshold, or right asserted in the output must carry an inline citation to the relevant state code section, regulation, or AG/AGO guidance. Format: `(Cal. Civ. Code § 1798.140(d))`, `(Va. Code § 59.1-575)`, etc. If the citation isn't in the references, mark the assertion `[citation needed — verify before reliance]`.
7. **No legal advice posture.** Outputs are analysis and drafts for review by qualified counsel admitted in the relevant jurisdiction. Include this disclaimer in every formal deliverable. This is not a CYA reflex — it sets the user's expectation about how to use the output.
8. **AD/BC dating where dates appear in formal deliverables.** Use AD/BC, not CE/BCE.

## Standard workflow

This is the logical sequence, not a rigid script. Skip steps when the user has already supplied the input. Slow down or speed up to match the user's sophistication.

```
Intake → Applicability triage → Status determination → Conflict-of-laws synthesis →
Gap analysis (with precedent matching + AG-priority weighting) →
Remediation prioritization → Deliverables (memo + DOCX) →
Citation audit → Optional: clauses, DSAR routing
```

### Step 1 — Intake

If the user opens with a specific narrow question ("does Colorado apply if I make $20M and have 80,000 CO customers?"), answer it directly using the relevant references.

If the user opens with an open-ended request ("help me get compliant" / "I'm hiring a privacy counsel and need a baseline"), run a structured intake. Read `references/workflows/intake-questionnaire.md` and ask the questions in batches of no more than 5 at a time. Do not ask one question at a time — that wastes the user's clock.

Critical intake categories: entity & corporate structure; revenue and consumer-volume thresholds; data categories processed (and whether any are sensitive); whether the entity sells data, shares for cross-context behavioral advertising, profiles individuals, or processes minors' data; channels (website, mobile, offline, hardware); B2B vs B2C; existing notices and contracts; sectoral overlay (HIPAA/GLBA/FCRA/COPPA).

### Step 2 — Applicability triage

For each state, run the state's threshold test. The thresholds are not all the same — California uses revenue *or* consumer count *or* data-sale share; Texas has no numerical threshold but excludes SBA-defined small businesses with sensitive-data carve-outs; Florida has a $1B narrow trigger. See `references/applicability-matrix.md` for the master matrix.

Output a table with columns: State | Statute | Applies? | Reasoning | Effective Date / Enforcement Status. Mark "Insufficient info" rather than guessing — and list the specific input you'd need.

### Step 3 — Status determination

For each applicable state, determine whether the entity is a controller, processor, third party, service provider/contractor (CA-specific), or some combination by data flow. **For anything more nuanced than a clearly-controller posture, read `references/workflows/status-determination.md` and run the decision tree per data flow.** A SaaS vendor processing customer data is typically a *processor* for that data and a *controller* for its own business contacts and marketing data. Many entities are dual-status. State this explicitly per data flow, with a per-flow status table per the workflow file.

### Step 3.5 — Conflict-of-laws synthesis (multi-state engagements)

Where two or more states are applicable, do not stop at parallel state analyses. Run `scripts/conflict_resolver.py --states CA,VA,CO,...` to synthesize the binding constraint across applicable states (the "compliance ceiling"). For each of ~13 compliance dimensions (notice content, sensitive-data treatment, sale of sensitive data, minor treatment, response time, appeal right, UOOM recognition, opt-out persistence, processor contract terms, DPA requirements, etc.), the script returns the strictest applicable rule, the controlling state, the citation, and other states' positions for context. Use the output to drive a unified-implementation recommendation rather than a state-by-state checklist that the controller cannot operationalize.

### Step 4 — Gap analysis

For each applicable state, walk through `references/controller-duties.md` and the relevant `states/<xx>.md`, comparing each statutory duty against current practice. Score each gap using the methodology in `references/workflows/gap-analysis-method.md`:

- **Severity** (1–5): regulatory exposure if challenged, considering enforcement priors and cure availability.
- **Likelihood** (1–5): probability a regulator, plaintiff, or consumer surfaces the gap.
- **Score** = Severity × Likelihood. Levels: Low (1–6), Medium (7–12), High (13–19), Critical (20–25).

**Adjust the score by AG posture.** Read `references/ag-priorities.md` and apply the heuristic adjustments from the "Risk weighting in gap analysis" section: a gap implicating a stated Tier 1 AG priority (CA, TX, CO) gets +1 severity; a gap in an industry currently under sweep (connected vehicles, healthcare-pixel, child-directed apps, etc.) gets +1 likelihood; a gap subject to an active cure period gets -1 severity.

**Match each material gap to analogous enforcement actions.** Use `scripts/precedent_match.py` with violation-theory tags from the corpus (e.g., `--tag gpc_not_honored --tag no_donotsell_link --state CA`) to pull the 3-5 most analogous prior actions from `references/enforcement_actions.json`. Cite the most directly analogous matter with the operational lesson and headline figure in the gap-log entry. This shifts the work product from "here's the rule" to "here's what happened to companies in your shoes."

**For the highest-severity gaps, also pull defense-side framing** from `references/defense-arguments.md` so the deliverable shows both the exposure and the recovery posture.

Surface cross-cutting gaps — e.g., a single missing disclosure that creates exposure under 8 statutes is a higher-priority fix than a CA-only edge case.

### Step 5 — Remediation prioritization

Sort gaps by Score, then bucket into **0–30 day**, **31–90 day**, and **>90 day / strategic** lanes. Note dependencies — e.g., updating the privacy notice often depends first on completing a data inventory; flag that.

### Step 6 — Deliverables

Generate two artifacts:

1. **Markdown memo.** Use `assets/memo-template.md` as the skeleton. Substantive content fills in. Save to the working directory.
2. **DOCX deliverable.** This is the formal client-ready version. Always read the `docx` skill (which is generally available alongside this one) before generating. Then run `scripts/generate_docx_memo.js` with a JSON payload built from the analysis. The script is idempotent and produces a US Letter document with covers, TOC, the applicability matrix, gap log table, and remediation roadmap.

Both artifacts must include the no-legal-advice disclaimer and a "Limitations and assumptions" section that lists what the analysis depends on (e.g., revenue figures provided by user, data flows as described, no anomalous facts not yet known).

### Step 6.5 — Citation audit (mandatory pre-delivery QA)

Before finalizing the markdown memo, run `scripts/citation_audit.py --input <memo>.md --strict`. The auditor enforces the citation discipline mandated in the operating principles:

- Every substantive claim (assertion of obligation, right, threshold, or penalty) must carry an inline citation.
- Citations must match canonical formats for the relevant statute (e.g., `Cal. Civ. Code § 1798.140(d)`, `Va. Code § 59.1-575`, `4 CCR § 904-3`).
- Section numbers cited must be plausible (e.g., `Cal. Civ. Code § 1798.X` must fall in the CCPA codified range).
- "CCPA" / "CPRA" should not be reified as separate statutes outside parentheticals.
- No `[citation needed]` markers should remain in the final memo.

Do not deliver a memo with audit errors. Warnings are reviewable; surface them to the user when flagged.

### Step 7 — Optional: notice clauses and DSAR routing

If the user asks for model clauses (notice-at-collection, opt-out disclosures, sensitive data notice, financial incentive notice), pull the matching template from `assets/notice-clauses/` and adapt it to the entity's specific facts. Never paste a template verbatim — it must be tuned to the data categories, purposes, retention periods, and recipients actually in play.

If the user asks how to handle a specific consumer request, follow `references/workflows/dsar-routing.md`.

## Output discipline

- **Tables for comparisons.** When showing multi-state output, always use a table. Prose comparisons of 5+ states are unreadable.
- **Citations inline.** Every obligation, right, threshold, or penalty figure must carry a code section. If you can't cite it, flag it.
- **Quantify uncertainty.** If applicability is borderline (e.g., consumer count near 100k threshold), say so and explain what would tip it.
- **No marketing language.** Do not write "industry-leading," "robust," "best-in-class," or "comprehensive privacy program." This is legal analysis, not a brochure.
- **Active voice and concrete subjects.** "The controller must provide" — not "It must be provided."
- **AD/BC for any dates referenced narratively.** Statute citations and effective dates use the form on the books.

## Common errors to avoid

These are the failure modes that show up repeatedly in privacy work product. The skill exists in part to prevent them.

1. **Conflating CCPA and CPRA.** CCPA was the original 2018 act; CPRA (2020) amended it, created the CPPA agency, and added rights and obligations effective Jan 2023. Always cite the consolidated Cal. Civ. Code §§ 1798.100 et seq., not "CCPA" or "CPRA" as if they were distinct statutes.
2. **Treating "sensitive data" as one concept.** California uses "sensitive personal information" with an opt-out / right-to-limit-use structure. The other 19 states use "sensitive data" with an *opt-in* (consent) requirement before processing. The structural difference matters.
3. **Missing the universal opt-out signal mandate.** CO, CT, OR, MT, NJ, NH, MN, MD, DE, and others require recognition of universal opt-out mechanisms (e.g., GPC). California also recognizes GPC for opt-out of sale/share. Do not omit this.
4. **Forgetting employee and B2B coverage.** California is the outlier — employee/applicant data and B2B contact data ARE within CCPA/CPRA scope. The other states generally exclude these. Outputs that lump them together are wrong.
5. **Stating cure periods as permanent.** Many states had cure periods at enactment that have since sunset (e.g., California's general 30-day cure sunset under CPRA; Colorado's cure period sunset Jan 2025). Verify against `references/enforcement.md` rather than memory.
6. **Stale threshold figures.** Texas excludes SBA small businesses but with carve-outs for sensitive-data sales without consent. Florida's threshold is narrowly tied to $1B revenue plus enumerated activities. Don't paraphrase from memory; cite.
7. **Skipping the kids' overlay.** California's Age-Appropriate Design Code (partial preliminary injunction history; check `references/kids-and-teens.md`), CT/CO teen-specific provisions, and federal COPPA all overlay state laws when minors are present. State-only analysis without this overlay produces incorrect output.

## Limitations of this skill

- The reference files reflect law as of the version date in this skill's frontmatter. Laws change; new states pass laws (NM, IL biometrics, etc.) and existing laws are amended (CPPA rulemaking on automated decision-making, profiling, risk assessments). When a question turns on a development that may post-date the reference, say so and recommend the user verify with a current source.
- The skill produces analysis and drafts. It does not file registrations (e.g., California or Texas data broker registration), submit risk assessments to regulators, or constitute the practice of law. A licensed attorney must review.

### What this skill is *not* for — explicit scope and referrals

This skill is a **state privacy patchwork navigator**. It is deliberately narrow, and that narrowness is what makes it useful. Several adjacent regimes intentionally fall outside the scope. **If the user's question is purely within one of the regimes below — without a state privacy overlay — this skill is the wrong tool, and continuing to answer with it produces low-quality work product.** Recommend a sectoral resource and stop.

**Federal sectoral regimes (out of scope standalone; in scope as overlay).**

- HIPAA (Privacy Rule, Security Rule, Breach Notification Rule) — *use a HIPAA-specific resource for standalone analysis.*
- GLBA (Privacy Rule / Reg P, Safeguards Rule) — *use a GLBA-specific resource for standalone analysis.*
- COPPA Rule compliance (notice, VPC mechanics, internal-use exception, 2025 amendments) — *use a COPPA-specific resource for standalone analysis.*
- FERPA disclosure analysis, school-official exception, directory information — *use a FERPA-specific resource for standalone analysis.*
- FCRA furnisher obligations, dispute mechanics, permissible-purpose, adverse-action notices — *use an FCRA-specific resource for standalone analysis.*
- NYDFS Part 500, FTC Safeguards Rule expansion, HHS Reproductive Health Privacy amendments standalone.

When any of the above intersect with state privacy law (e.g., a HIPAA covered entity asking about CCPA obligations for non-PHI marketing data; a GLBA-regulated bank asking about CPA's coverage of B2B data; a COPPA-subject service asking how MD's flat ban on minor targeted advertising layers on top), `references/federal-overlays.md` is the right place to start. The overlays file is a **bridge**, not a standalone navigator.

**Other adjacent regimes (out of scope entirely; recommend dedicated skills).**

- GDPR / UK GDPR / non-US privacy regimes (Canadian PIPEDA / Quebec Law 25, Brazilian LGPD, etc.) — entirely different paradigm.
- State biometric laws standalone (Illinois BIPA, Texas CUBI, Washington biometric) — though enforcement actions appear in the corpus where they intersect with state privacy work.
- State consumer-health-data laws standalone (Washington MHMDA, Connecticut amendments, Nevada SB 370) — though private-right-of-action filings appear in the corpus.
- State AI-specific laws (Colorado AI Act, NYC Local Law 144, Utah AI Disclosure Act).
- State social-media / minor-platform laws (CA SB 976, NY SAFE for Kids, FL HB 3, TX SCOPE Act) — distinct from state comprehensive privacy law's minor provisions.

## Quickstart prompts

The skill is most useful when the user provides structured inputs. If they don't, drive the intake. Examples of well-formed prompts:

- "I run a Series-B SaaS, $40M ARR, US-only, 200k US consumer-end-user accounts (40k California, 30k Colorado, 8k Connecticut, scattered elsewhere). We don't sell data but we run Meta and Google Ads with their pixels for retargeting on logged-out marketing pages. Which state laws apply, and what's our top-5 priority remediation list?"
- "Consumer in Oregon emailed asking us to delete their data. We're a healthcare-adjacent vendor (not a covered entity). Walk me through the response."
- "Draft a notice-at-collection that satisfies California, Colorado, and Connecticut for an e-commerce company that uses third-party analytics, runs targeted ads via cross-context behavioral advertising, and offers a loyalty program with a discount for email signup."

If a user prompt is vague, run intake. If a user prompt is sharp, answer sharply.
