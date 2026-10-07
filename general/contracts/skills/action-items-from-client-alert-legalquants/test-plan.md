# Acceptance Test Plan — Action Items from Client Alert v1.0.0

## Skill summary

Extracts time-sensitive action items, deadlines, and obligations from a regulatory bulletin, law firm memo, or client alert into a deadline-organized checklist. Supports `applicable_jurisdictions` and `industry_filter` inputs to narrow the extraction to items affecting the user's organization.

## Test corpus requirements

Source 5–8 anonymized client alerts / regulatory bulletins covering:

- **At least 1 single-jurisdiction alert with explicit deadlines** (e.g., a state-AG enforcement-deadline notice with a specific compliance date).
- **At least 1 multi-jurisdiction alert** (e.g., a bulletin covering simultaneous federal and state regulatory changes with overlapping but distinct deadlines).
- **At least 1 alert with implicit deadlines** (e.g., "registrants must file before the next annual renewal" — requires inference of when the next annual renewal is).
- **At least 1 alert with no deadlines** (informational / advisory in nature) to test the no-deadlines handling.
- **At least 1 alert with notably narrow industry applicability** (e.g., specific to financial services, healthcare, or another regulated industry).
- **At least 1 alert from a law-firm-memo source** (vs. a regulator-issued bulletin) — different framing, often more analytical.

Sources can include public client alerts (most law firm websites publish them) and regulatory-agency bulletins (Federal Register, SEC press releases, state AG announcements).

## Test scenarios

### Scenario 1: Single-jurisdiction alert with explicit deadlines

**Inputs:** Client alert covering a specific regulatory development with explicit compliance deadlines. Inputs: applicable jurisdiction matching the alert.

**Expected output structure:**
- Markdown report with sections: "Bottom line" (summary of relevance and urgency), "Action items" (organized by deadline timeframe — Immediate / Short-term / Medium-term / Long-term), "Open questions / context" (items needing clarification before action), "What this skill does not do".
- Each action item includes: action description, deadline (date or relative timeframe), source citation in the alert, severity / urgency tag.
- Citations point at the specific section of the alert.

**Expected calibration:**
- Action items extracted are real (a reviewing attorney would identify the same items from the alert).
- Deadlines are accurately captured (specific dates preserved; relative deadlines preserved as relative).
- Actions are appropriately atomic (each action item is one thing the user can do, not a vague "comply with the new rule").
- "Bottom line" addresses applicability to the user's stated jurisdiction.

**Edge cases to verify:**
- If the alert has multiple dates (effective date vs. compliance date vs. enforcement-discretion date), the skill differentiates them.
- If the alert has phased deadlines (initial requirement at date X, full requirement at date Y), each phase becomes a separate action item.

**Pass criteria:**
- Structural pass: All required sections present; deadline tags consistent.
- Calibration pass: Reviewing attorney confirms action items extracted are correct and complete.

### Scenario 2: Multi-jurisdiction alert

**Inputs:** Alert covering federal and state-level changes with overlapping but distinct deadlines. Inputs: `applicable_jurisdictions: [federal, california, new-york]` (or similar).

**Expected output structure:** Same structure with explicit jurisdiction tagging on each action item.

**Expected calibration:**
- Action items are tagged by jurisdiction.
- If the user's jurisdictions filter excludes a jurisdiction in the alert, items applicable only to the excluded jurisdiction are either omitted or surfaced separately under a "filtered out" notation.
- Deadlines that differ across jurisdictions (the federal effective date vs. the California compliance date) are clearly differentiated.

**Edge cases to verify:**
- Items applicable to multiple jurisdictions are flagged once with multi-jurisdiction tagging, not duplicated.
- If a jurisdiction filter is applied but the alert covers a related-but-different jurisdiction (e.g., user filter is California; alert covers federal preemption of California requirements), the skill notes the relationship.

**Pass criteria:** As above with jurisdiction-aware verification.

### Scenario 3: Alert with implicit deadlines

**Inputs:** Alert where deadlines are implicit ("at the time of next annual renewal", "before the start of the next reporting period", "promptly after the effective date").

**Expected output structure:** Same structure with implicit deadlines surfaced as such.

**Expected calibration:**
- Implicit deadlines are flagged as such (not inferred to specific dates the alert does not provide).
- The skill suggests how the user can resolve the implicit deadline (e.g., "the next annual renewal date for our company is required to convert this to an actionable date").
- "Open questions / context" includes the implicit-deadline resolution as a follow-up item.

**Edge cases to verify:**
- The skill does not invent specific dates from implicit references.
- The skill calibrates urgency based on the implicit timeframe (e.g., "next reporting period" suggests near-term; "by next annual renewal" suggests up to 12 months).

**Pass criteria:** As above with implicit-deadline verification.

### Scenario 4: Alert with no deadlines (informational)

**Inputs:** Advisory alert (e.g., a regulatory commentary, FAQ release, or interpretive guidance) without explicit compliance dates.

**Expected output structure:** Modified structure — the "Action items" section is sparse or replaced with an "Awareness items" section; the "Bottom line" addresses why the alert is relevant despite the absence of immediate action items.

**Expected calibration:**
- Skill does not invent deadlines that aren't in the alert.
- Skill identifies forward-looking implications (e.g., "this guidance suggests a future enforcement direction; monitor for follow-on regulatory action").
- Skill does not produce action items where none are warranted.

**Edge cases to verify:**
- Skill clearly distinguishes "no deadlines because none stated" from "deadlines that I missed in extraction."

**Pass criteria:** As above with no-deadline verification.

### Scenario 5: Industry-filtered alert

**Inputs:** Alert with notable industry applicability (e.g., financial services, healthcare). Input: `industry_filter: <industry>` matching the alert's scope.

**Expected output structure:** Same structure with industry-specific scoping called out.

**Expected calibration:**
- Action items are filtered to those applicable to the specified industry.
- Items not applicable to the industry are either omitted or surfaced with a clear "not applicable to your industry" flag.
- "Bottom line" addresses industry-specific impact.

**Edge cases to verify:**
- If the alert is industry-specific but the user's filter doesn't match, the skill notes the mismatch and recommends whether to proceed.
- If the alert has cross-industry implications, the skill differentiates the industry-specific from the cross-cutting.

**Pass criteria:** As above with industry-filter verification.

### Scenario 6: Law-firm-memo source

**Inputs:** Alert sourced from a law firm memo (often more analytical than a regulator-issued bulletin; may include strategic recommendations).

**Expected output structure:** Same structure but with awareness that the source is interpretive / strategic.

**Expected calibration:**
- The skill differentiates the alert's *factual* content (what the regulation requires) from *strategic* content (the firm's recommendation on how to respond).
- The skill does not import the firm's strategic framing as fact.
- Action items are operationally usable for the user's organization, not just summaries of the firm's recommendations.

**Edge cases to verify:**
- The skill calibrates against the firm-memo style (often longer, more analytical, with embedded commentary).

**Pass criteria:** As above with source-aware verification.

## Refusal scenarios

### Refusal 1: Document is not a client alert / regulatory bulletin

**Input:** A research paper, news article, or other document misidentified as a client alert.

**Expected behavior:**
- Skill identifies the document type mismatch.
- Skill suggests whether the document is amenable to action-item extraction or whether a different skill or approach is appropriate.

**Pass criteria:** Explicit identification.

### Refusal 2: Alert is for a jurisdiction outside the user's filter

**Input:** Alert covers a jurisdiction (or industry) that the user has explicitly filtered out.

**Expected behavior:**
- Skill identifies the mismatch.
- Skill recommends either expanding the filter or noting that the alert may not be relevant.
- Skill does not produce filtered-out action items as if they applied.

**Pass criteria:** Explicit mismatch handling.

## Cross-cutting verification

- **No invented action items.** Every action item is grounded in the alert.
- **No invented deadlines.** Implicit deadlines are flagged as implicit, not inferred to specific dates the alert does not provide.
- **No regulatory-compliance opinions.** The skill summarizes what the alert says is required; it does not assert that the user's compliance approach satisfies the requirement.
- **Citations resolve.** Every action item points at the section of the alert where it is supported.
- **"What this skill does not do" enumeration present.** Typical: substantive regulatory analysis, jurisdiction-specific compliance certifications, strategic legal advice on enforcement risk.

## Pass / fail decision

Action Items from Client Alert v1.0.0 passes acceptance testing when:

1. All 6 test scenarios pass structural checks.
2. All 6 test scenarios pass calibration evaluation by a reviewing attorney with regulatory-update experience.
3. Both refusal scenarios trigger documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

## Reviewer notes

The reviewing attorney for Action Items from Client Alert acceptance testing should have practical experience with regulatory update intake and compliance-program management. Specific competencies:

- Recognizing when an extracted action item is too vague to be operational ("comply with new rules") vs. appropriately atomic ("file the new disclosure form by March 31").
- Calibrating implicit deadlines (when "promptly" warrants treatment as immediate vs. when it warrants ~30 days).
- Differentiating an alert's factual content from interpretive framing in firm memos.

Calibration assessment is documented in `test-results/action-items-from-client-alert-v1.0.0/calibration-assessment.md`.
