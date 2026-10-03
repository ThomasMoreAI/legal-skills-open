# Intake Questionnaire Workflow

**Purpose.** A structured intake to extract the information required to run applicability triage, status determination, and gap analysis. Use this when the user opens with an open-ended request ("help me get compliant"). Skip when the user has already supplied the relevant inputs.

> **Process discipline.** Ask in batches of 5 questions or fewer per turn. Do not interrogate one question at a time — wastes the user's clock. Acknowledge what they've supplied; ask only what's missing.

## Tier 1 — Entity and threshold inputs (always ask if not supplied)

1. **Legal entity and corporate structure.** Name, state of formation, parent/subsidiary structure, brand affiliates. (Used to determine joint-venture and affiliate-coverage analysis under CCPA § 1798.140(d) and similar.)
2. **Annual revenue.** Total gross annual revenue for the most recent calendar year. Specify whether US-only or global. (Triggers CA $25M threshold, UT $25M threshold, TN $25M threshold, FL $1B threshold.)
3. **Consumer count by state.** Number of distinct natural persons whose PD was processed during the preceding (or current) calendar year, by state of residency. If the user has total US count but no state breakdown, request a reasonable estimate or census-share approximation. (Triggers all states' consumer-volume thresholds.)
4. **Sale or sharing of PD.** Does the entity sell PD for monetary or other valuable consideration? Does it share PD for cross-context behavioral advertising? Approximate share of revenue from sale, if any. (Triggers second-tier thresholds in most states; triggers FL ad-revenue prong.)
5. **SBA size status.** For TX and NE applicability, determine whether the entity is a "small business" under SBA size standards. NAICS code; revenue or employee count per applicable size standard.

## Tier 2 — Data and processing inputs

6. **Data categories processed.** A high-level inventory: account/profile data; transaction data; payment data; web/mobile analytics; device identifiers; precise geolocation; biometric data; health data; financial data; communications content; government identifiers; account credentials. (Drives sensitive-data analysis.)
7. **Sensitive data processing.** Specifically address each sensitive-data category: do you process racial/ethnic origin, religion, mental/physical health, sex life/orientation, citizenship/immigration status, genetic data, biometric data for unique ID, precise geolocation, child data? (Drives consent / limit-use analysis.)
8. **Children and teens.** Is the service directed to children under 13? Does the service have actual knowledge of users under 13? Are minors aged 13–17 a known user segment? What age verification or estimation, if any, is in place?
9. **Profiling and automated decision-making.** Is consumer PD used in automated profiling that produces or contributes to legal or similarly significant decisions (e.g., credit, employment, housing, insurance, healthcare access, education access)? (Drives profiling-opt-out and DPA analysis.)
10. **Targeted advertising.** Does the entity engage in targeted / cross-context behavioral advertising? Specify channels (retargeting, lookalike audiences, programmatic display, social platform ads). What pixels/SDKs are deployed (Meta, Google, TikTok, LinkedIn, others)?

## Tier 3 — Channels and infrastructure inputs

11. **Channels.** Where do consumers interact with the service? Web (logged-in vs. logged-out); mobile apps (iOS, Android); offline (POS, call center, kiosks); connected devices/IoT; email/SMS marketing.
12. **CMP / consent infrastructure.** Is there a Consent Management Platform (CMP) deployed? Which one? Does it handle GPC? Is consent recorded with audit trail?
13. **Existing privacy notice and notice-at-collection.** When were they last updated? What jurisdictions do they purport to address?
14. **Existing rights-request workflow.** How does the entity receive consumer rights requests today (web form, email, support tickets)? Average response time? Volume per quarter?
15. **Vendor and processor relationships.** Approximate number of vendors with access to PD. Are written DPAs in place? When were they last updated? Are subprocessor flow-down provisions current?

## Tier 4 — Sectoral and contextual overlay

16. **Sectoral overlay.** Is the entity a HIPAA covered entity or business associate? GLBA-covered financial institution? FCRA consumer reporting agency or user? FERPA-covered or processing student data? COPPA operator?
17. **Employee, applicant, B2B contact data.** Does the entity process this data of California residents? (CCPA covers; most other states do not, but this is a specific CA exposure.)
18. **Existing privacy program governance.** Is there a written privacy program? A privacy officer or DPO equivalent? Privacy training? An incident response plan? When was the last DPA?
19. **Cross-border data flows.** Is data transferred outside the US? (May trigger GDPR/UK GDPR analysis — flag for separate analysis if so.)
20. **Anticipated changes.** Mergers, new product launches, new data uses, new geographies, new vendors? (Privacy programs degrade as the underlying business changes; capture forward-looking events.)

## Asking pattern

When running intake, group the questions thematically and ask 3–5 at a time. Example sequence:

**Turn 1 (entity and threshold)**: "Before I run the applicability analysis, I need a few inputs. (1) What's your annual gross revenue (most recent calendar year)? (2) How many distinct US consumers do you process PD for, broken down by state if you have it? If not, total US count is fine. (3) Do you sell PD or share for cross-context behavioral advertising? (4) Are you a HIPAA covered entity, GLBA-covered financial institution, FCRA reporter, or COPPA-covered? (5) Do you have customers, users, or contacts in CA who are employees, applicants, or B2B contacts of yours?"

**Turn 2 (data and processing)** — after Turn 1 answers — "Got it. Now: (1) What sensitive-data categories do you process? Specifically: health, biometric, precise geolocation, racial/ethnic, religious beliefs, sexual orientation, citizenship status, genetic data, child data, communications content, account credentials, government IDs. (2) Do you have known minor users (under 13 or 13–17)? (3) Do you use automated profiling for decisions that affect consumers (credit, employment, housing, insurance, healthcare)? (4) What advertising pixels/SDKs are deployed and where (login pages, marketing pages, app)?"

**Turn 3 (infrastructure)** — after Turn 2 answers — "Last few: (1) Do you have a CMP? Which one, and is GPC handling enabled? (2) When was your privacy notice last updated, and what jurisdictions does it address? (3) How are consumer rights requests received and routed today, and what's the volume? (4) How many vendors process PD on your behalf, and are DPAs current?"

After three turns, you should have enough to run applicability, status, and a meaningful gap analysis.

## Insufficient-info handling

If the user cannot answer a Tier 1 input, flag in the deliverable as **Insufficient Info** for the affected analysis. List the specific input needed.

If the user provides ranges or estimates ("around 80–120k California consumers"), run the analysis with the conservative reading (in scope) and note the borderline.

## Inputs the user usually does not have ready

Typical gaps even from sophisticated controllers:

- State-by-state consumer breakdown.
- Categorization of every vendor as controller / processor / third party.
- Up-to-date data flow diagram.
- Inventory of pixels and SDKs across all properties.
- Documentation of rights-request volumes and response times.

Where these are missing, the analysis should propose a data-mapping or vendor-inventory project as a precursor remediation step.

## Sample minimal-viable intake

If the user is impatient, here is the minimum required to produce useful Tier 1 analysis:

- Annual revenue (US or global, specify).
- US consumer count (state breakdown if possible).
- Whether the entity sells or shares PD.
- Whether the entity is sectorally exempted (HIPAA / GLBA / FCRA / non-profit).

Everything else can be collected iteratively as the analysis proceeds.
