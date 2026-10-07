---
name: nis2-compliance-triage-en-matematicsolutions
title: NIS2 Compliance Triage EN - scope and obligations navigator (Directive (EU) 2022/2555)
description: 'NIS2 scope and obligations triage (Directive (EU) 2022/2555) in English - a scope navigator: is the entity in scope at all (Annex I and II sectors, size-cap rule, size-independent exceptions), essential vs important entity, map of the 10 risk-management measures under Art. 21(2), incident reporting clock under Art. 23 (24h -> 72h -> 1 month), management body duties under Art. 20, penalty ceilings. NIS2 is a directive: obligations bite through NATIONAL transposition, and transpositions differ per member state - so the skill puts the transposition question first and marks it for checking against the national source before anything is relied on. It has no connector of its own and does not confirm transposition status. Output: a NIS2 card for human decision. Use when: "does NIS2 apply to us", "essential or important entity", "the 10 measures of Art. 21", "NIS2 incident reporting", "management board cybersecurity duties", "NIS2 fines", "national transposition of NIS2".'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/ai-governance/skills/nis2-compliance-triage-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: en
---

# NIS2 Compliance Triage EN - scope and obligations navigator (Directive (EU) 2022/2555)

## Philosophy

NIS2 is first a scope question, only then a measures question. Most bad advice skips triage: a
company "feels" in scope (or out of scope) and jumps straight to an audit. This skill runs the
navigator in a fixed order: **in scope? -> which category -> which measures -> which reporting ->
what does the national transposition say**. Every claim carries a certainty tag; an article
number that cannot be confirmed in the session gets [TO VERIFY], never a guessed number.

Second principle: **a directive does not bind a company directly**. Obligations come from the
national implementing act, and member states transposed NIS2 differently and at different times.
Until the transposition status of the relevant country is established as of the day of use,
everything below is a map of the directive, not a list of enforceable duties.

## When to use / What it does NOT do

**Use for:** initial "does NIS2 apply to us" triage, the "essential or important" dispute, an
inventory of the 10 measures under Art. 21(2) before an audit, laying out the incident reporting
clock in advance, briefing the management body on Art. 20 liability, turning gaps into an
implementation plan.

**Does NOT:**
- replace a security audit or penetration test - the measures map is built from user
  declarations; the skill verifies nothing technically,
- assess the quality of a measure (whether backups actually restore) - only whether it exists
  and is documented according to the user,
- run a live incident - during an ongoing incident it points to the internal response procedure
  and the responsible human (CISO / board / counsel),
- send any notification to a CSIRT or competent authority - it drafts and sets the clock,
- settle entity classification definitively - that is a legal call on the national implementing
  act, behind the human gate.

**Regime boundary:** if the incident involves personal data, TWO clocks run IN PARALLEL - NIS2
(24h early warning / 72h incident notification to the CSIRT or authority) and GDPR (72h
notification to the data protection authority, Art. 33 GDPR). The GDPR clock is run by
`gdpr-breach-72h-en`. One notification never substitutes for the other.

## Workflow

### Step 0 - national transposition status (MANDATORY, before any advice)

The transposition deadline expired on 17 October 2024 (Art. 41 of the directive). Member states
missed it to varying degrees, and national acts diverge on registration, deadlines, authority
structure and penalties. Therefore:

1. Identify the member state(s) whose law applies to the entity (main establishment rule for
   digital infrastructure and digital providers - verify against Art. 26 [TO VERIFY]).
2. Verify the transposition status of that state as of the day of use. Examples of national
   acts: Germany - NIS2UmsuCG (NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz), status [TO VERIFY]; Poland -
   amendment of the Act on the National Cybersecurity System (KSC), status [TO VERIFY in ISAP
   via the sejm-eli-mcp connector]. For other states, check the national gazette or the
   mcp-eu-compliance connector; do not assume any act is in force without checking.
3. Record the result on the card (field "Transposition status") with the date checked.
4. Pick the analysis regime: (a) national act in force -> analyse on the act; (b) not in
   force -> analyse on the directive as a map of INCOMING obligations, and flag that the old
   NIS1-based national regime may still apply in the meantime.
5. **Never state that a national transposition is in force without verifying it in the
   session.**

### Step 1 - sector triage (Annex I and II)

**Annex I - sectors of high criticality:** energy (electricity, district heating and cooling,
oil, gas, hydrogen), transport (air, rail, water, road), banking, financial market
infrastructures, health, drinking water, waste water, digital infrastructure (incl. IXPs, DNS
service providers, TLD name registries, cloud computing providers, data centre providers, CDNs,
trust service providers, public electronic communications networks and services), ICT service
management B2B (managed service providers and managed security service providers), public
administration, space.

**Annex II - other critical sectors:** postal and courier services, waste management,
manufacture, production and distribution of chemicals, food (production, processing,
distribution), manufacturing (incl. medical devices, computer/electronic/optical products,
electrical equipment, machinery, motor vehicles and other transport equipment), digital
providers (online marketplaces, online search engines, social networking platforms), research
organisations.

Entity outside both annexes -> as a rule out of scope; still check whether the national
transposition extends the catalogue ([TO VERIFY] field on the card).

### Step 2 - size-cap rule and size-independent exceptions (Art. 2)

**Size-cap rule (Art. 2(1)):** the directive covers Annex I or II entities that are at least
**medium-sized enterprises** under Recommendation 2003/361/EC (roughly: 50+ employees, or annual
turnover / balance sheet above EUR 10 million; large: 250+ employees, or turnover above EUR 50
million / balance sheet above EUR 43 million). Micro and small enterprises are, as a rule, out.

**Size-independent exceptions (Art. 2(2)-(4))** - the entity is in scope regardless of size,
among others where it:
- provides public electronic communications networks or publicly available electronic
  communications services,
- is a trust service provider, a TLD name registry or a DNS service provider,
- is the sole provider in a member state of a service essential for critical societal or
  economic activities,
- could, by disruption of its service, significantly impact public safety, public security or
  public health, or induce significant systemic risk,
- is critical at national or regional level,
- is a public administration entity (central government; regional per member state decision),
- has been identified as a critical entity under the CER Directive (2022/2557).

### Step 3 - essential vs important entity (Art. 3)

**Essential** (indicatively): large entities in Annex I sectors; regardless of size - qualified
trust service providers, TLD name registries and DNS service providers; medium-sized providers
of public electronic communications networks or services; critical entities under CER; entities
designated as essential by a member state. **Important**: all remaining in-scope entities
(medium-sized Annex I entities plus medium and large Annex II entities). The final national
split is set by the implementing act - tag the national classification [TO VERIFY] until Step 0
confirms it. Why it matters: different supervision (ex ante vs ex post) and different penalty
ceilings (Step 7).

### Step 4 - map of the 10 risk-management measures (Art. 21(2))

All in-scope entities (essential and important) implement measures proportionate to the risk,
covering AT LEAST:

1. policies on risk analysis and information system security,
2. incident handling,
3. business continuity (backup management, disaster recovery) and crisis management,
4. supply chain security, including relationships with direct suppliers and service providers,
5. security in network and information systems acquisition, development and maintenance,
   including vulnerability handling and disclosure,
6. policies and procedures to assess the effectiveness of cybersecurity risk-management
   measures,
7. basic cyber hygiene practices and cybersecurity training,
8. policies and procedures on the use of cryptography and, where appropriate, encryption,
9. human resources security, access control policies and asset management,
10. multi-factor or continuous authentication, secured voice, video and text communications and
    secured emergency communication systems, where appropriate.

For each measure ask the user for status (implemented / partial / missing / unknown) and record
it. "Unknown" is a gap, not a zero - do not guess on the user's behalf.

### Step 5 - significant incident reporting (Art. 23)

**Significant incident** (Art. 23(3)): it has caused or is capable of causing severe operational
disruption of the services or financial loss for the entity, OR it has affected or is capable of
affecting other natural or legal persons by causing considerable material or non-material
damage.

The clock (runs from becoming aware of the significant incident):
- **24h** - early warning to the CSIRT or competent authority (incl. whether unlawful or
  malicious action is suspected and whether cross-border impact is possible),
- **72h** - incident notification (updating the early warning; initial assessment of severity,
  impact and indicators of compromise),
- on CSIRT/authority request - **intermediate report** on status updates,
- **1 month** after the incident notification - **final report** (detailed description, threat
  type, root cause, mitigation applied, cross-border impact); if the incident is still ongoing -
  a progress report, with the final report one month after the incident is handled.
- Where appropriate - notify the recipients of the services likely to be affected.

The addressee (which CSIRT / authority) and the exact submission channel are national - [TO
VERIFY in the transposition from Step 0]. During a LIVE incident: the skill sets the clock and
drafts, then hands over to the response procedure and the human. Personal data involved ->
`gdpr-breach-72h-en` in parallel.

### Step 6 - management body (Art. 20)

The management body of an essential or important entity: **approves** the Art. 21
risk-management measures, **oversees** their implementation, and **can be held liable** for the
entity's infringements of that article. Members of the management body must **follow training**
in cybersecurity and should offer similar training to employees. The precise shape of personal
liability (fines on managers, other sanctions) is national - [TO VERIFY in the transposition].

### Step 7 - penalties (Art. 34)

Ceilings from the directive (maxima each member state must at least provide for):
- **essential** entities: at least up to **EUR 10 000 000 or 2%** of total worldwide annual
  turnover - whichever is higher,
- **important** entities: at least up to **EUR 7 000 000 or 1.4%** of turnover - whichever is
  higher.

National acts set the concrete brackets, manager-level fines and supervisory measures (including
a possible temporary ban on managerial functions in essential entities - [TO VERIFY article
number and national shape]) - all [TO VERIFY in the transposition from Step 0].

## Output format - NIS2 card (literal template)

```
NIS2 CARD - [entity] - [analysis date]

TRANSPOSITION STATUS (Step 0): [member state + result + date checked / TO VERIFY]
Analysis regime: [national implementing act / directive 2022/2555 as map + legacy NIS1 regime]

IN SCOPE: [YES / NO / TO VERIFY]
Entity category: [essential / important / out of scope / TO VERIFY]
Sector: [Annex I or II - sector - subsector]
Basis for inclusion: [size-cap: medium/large / size-independent exception: which one]

MAP OF 10 MEASURES (Art. 21(2)) - status per user declaration:
| #  | Measure                                      | Status                          | Gap |
| 1  | risk analysis and IS security policies       | [implemented/partial/missing/unknown] | ... |
| 2  | incident handling                            | ...                             | ... |
| ... (all 10)                                                                            |

REPORTING CLOCK (Art. 23) - [mode: simulation / live incident]:
- awareness:                  [date+time or "n/a"]
- early warning (24h):        [deadline]
- incident notification (72h):[deadline]
- final report (1 month):     [deadline]
- addressee: [CSIRT/authority per transposition - TO VERIFY if not established]
- personal data involved: [YES -> gdpr-breach-72h-en in parallel / NO]

MANAGEMENT BODY (Art. 20): [approval: status | oversight: status | training: status]

PENALTY EXPOSURE: [ceiling per category: EUR 10m / 2% or EUR 7m / 1.4%]

GAPS: [numbered list - including every "unknown" from the measures map]
NEXT STEPS: [1-5 items, most urgent first]
CERTAINTY TAGS: [what was verified in session, what remains TO VERIFY]
```

## Human gate

The NIS2 card is a draft for decision, not a ruling. Entity classification, the decision to
notify an incident and any submission to a CSIRT or competent authority are approved and
executed by an authorised human (board / CISO / counsel). During a live incident the skill does
not take over response - it sets the clock and drafts; the procedure and the human run the rest.
Submission is never automatic.

## Companion skills

- `gdpr-breach-72h-en` - the parallel GDPR clock when the incident involves personal data,
- `matematic-konstytucja-ai` - AI governance rules for organisations in NIS2 scope,
- **sejm-eli-mcp** connector - status of the Polish KSC act and its amendment in ISAP,
- **mcp-eu-compliance** connector - text of Directive (EU) 2022/2555 from EUR-Lex for verifying
  provisions.

## Source verification

Article numbers in this skill come from the text of Directive (EU) 2022/2555; before they enter
a deliverable, verify each citation against EUR-Lex (CELEX 32022L2555, via mcp-eu-compliance)
and the national law against the national gazette (for Poland: ISAP via sejm-eli-mcp). The
verification foundation tags apply: verified / [TO VERIFY] / do not use. Any number or threshold
you cannot confirm in the session keeps its [TO VERIFY] tag - never invent an article number or
a penalty bracket.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the ai-governance plugin (AI governance)

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

These skills run regulatory triage for organisations deploying or building AI: EU AI Act classification and role mapping, NIS2 scope and obligations triage, and a privilege pre-flight check before legal content is sent to an external AI surface. Each ends in a draft for decision, not a finished act.

### Rules

- **Output is a draft for decision.** A classification card, a scope assessment or a redacted prompt is a starting point for counsel / the compliance owner. A person approves and acts on it.
- **Governance boundary - the outward act stays human.** Registering an AI system, notifying a CSIRT or supervisory authority, filing a FRIA, sending anything to an external AI service - the skill prepares the draft, it does not perform the act.
- **Regulation from the source, not from memory.** Article references carry confidence tags; anything uncertain is marked for verification against EUR-Lex (eu-sparql-search / mcp-eu-compliance connectors) or the national transposition before it is relied on. National transposition status changes - always check it at time of use.
- **Triage is not a conformity assessment.** These skills classify, map and flag. A high-risk or GPAI finding routes to a human and a full assessment; it is never the end of the analysis.
- **Not legal advice.** The skills organise obligations and map them to provisions; they do not replace legal analysis of a specific matter.
- **Confidentiality.** System descriptions, incident details and prompt content are confidential - do not move them outside the agreed flow. These skills add no outbound channel of their own; what reaches your model is decided by your configuration (see https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/TRUST.md).

### Plugin scope

Regulatory triage for AI and cyber (AI Act, NIS2) plus prompt-level privilege hygiene. It does not verify citations or fetch sources of law - use `verification-foundation` and `eu-law-sources` for that. GDPR operations (DPIA, breach, DSAR) live in `data-protection`; the AI Act triage pairs with `gdpr-dpia-en` when a system processes personal data.
<!-- shared-rules:end -->
