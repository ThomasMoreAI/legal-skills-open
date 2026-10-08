---
name: thai-pdpa-boom-vitt
title: PDPA ไทย (Thailand Personal Data Protection Act drafting)
description: 'Use this skill for tasks involving Thailand''s PDPA (พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562). Trigger whenever the user asks to: draft a Thai privacy notice, write a PDPA consent banner, prepare a data subject rights notice, draft a 72-hour breach notification to the PDPC, decide if a DPO is required, list lawful bases, handle cross-border transfers, or audit a notice against PDPA. Also trigger for "เขียน privacy policy", "PDPA", "ขอความยินยอม", "นโยบายความเป็นส่วนตัว", "consent banner ไทย", "Thai privacy notice", "PDPA compliance", "DPO Thailand", "ประกาศการละเมิดข้อมูล", or any variation. If the task involves Thai personal data law, consent, or notice drafting, use this skill.'
author: Boom-Vitt
author_url: https://github.com/Boom-Vitt/claude-thai-skills/tree/main/skills/thai-pdpa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: th
practice: data-protection
language: th
---

# PDPA ไทย (Thailand Personal Data Protection Act drafting)

## Overview
พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA, effective 1 June 2022) ใกล้เคียงกับ GDPR แต่ไม่เหมือนกัน. Copy-pasting a GDPR notice into Thai is the #1 reason notices fail audits — references to "Article 6 GDPR" make the notice non-compliant on its face. Always re-anchor citations to PDPA sections.

## When to use
- ร่างนโยบายความเป็นส่วนตัว (privacy notice) สำหรับเว็บไซต์ / แอป
- ออกแบบ cookie / consent banner ที่ผ่านเกณฑ์ PDPA
- ร่างหนังสือแจ้งสิทธิ์เจ้าของข้อมูล (data subject rights notice)
- แจ้งเหตุการละเมิดข้อมูล (data breach notification) ภายใน 72 ชั่วโมงต่อ PDPC
- ประเมินว่าต้องแต่งตั้ง DPO หรือไม่
- ตรวจสอบ template ที่แปลมาจาก GDPR ว่าใช้ได้กับ PDPA หรือไม่

## PDPA vs GDPR — what changes when drafting

| Topic | GDPR | PDPA (พ.ร.บ.) |
|---|---|---|
| Consent | Opt-in, freely given | Opt-in, freely given (Sec 19); no pre-checked boxes |
| Reject button | Recommended | **Required equal-weight** under PDPC consent guidance |
| Breach notice to regulator | 72h to DPA | **72h to PDPC** (Sec 37) |
| Subject rights | 8 rights | Same 8 rights (Sec 30–36): access, rectify, erase, restrict, port, object, withdraw, complain |
| DPO trigger | Large-scale systematic monitoring or special-category data | Same trigger + state agencies (Sec 41) |
| Cross-border | Adequacy or safeguards | Adequacy or safeguards; PDPC keeps adequacy list (Sec 28) |
| Sensitive data | Art 9 categories | Sec 26: race, ethnicity, political opinion, religion/philosophy, sexual behavior, criminal record, health, disability, trade union, genetic, biometric, others as prescribed |
| Penalties | Up to 4% global turnover | Admin fines up to ฿5M; criminal up to ฿1M + 1 yr imprisonment; civil punitive up to 2x damages |

## Required elements of a privacy notice (Section 23)
A compliant Thai notice must state, in plain Thai:
1. **วัตถุประสงค์** — Purpose for each item collected (itemized, not lumped)
2. **ฐานทางกฎหมาย** — Lawful basis (consent / contract / legal obligation / vital interest / public task / legitimate interest)
3. **ประเภทข้อมูล** — Categories of personal data processed
4. **ระยะเวลาเก็บรักษา** — Retention period (or criteria to determine it)
5. **ผู้รับข้อมูล** — Recipients / categories (including processors, group companies, third parties)
6. **การส่งข้อมูลข้ามประเทศ** — Cross-border transfer info: destination countries, safeguards (SCC-equivalent, BCR, adequacy)
7. **สิทธิ์ของเจ้าของข้อมูล** — All 8 data subject rights + how to exercise
8. **ผู้ควบคุมข้อมูล / DPO** — Controller identity, address, DPO contact
9. **สิทธิ์ในการร้องเรียน** — Right to complain to PDPC (สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล)
10. **ผลของการไม่ให้ข้อมูล** — Consequences of refusing (where data is required by contract or law)

See `templates/privacy-notice-th.md` for the full bilingual skeleton.

## Consent banner rules (Section 19 + PDPC consent guidance)
- **Pre-checked boxes are invalid** — every non-essential category starts off
- **"ยอมรับทั้งหมด" and "ปฏิเสธทั้งหมด" must be equally prominent** — same colour, same size, same depth in navigation. "Reject all" cannot be hidden behind a "Manage preferences" wall.
- **Granular consent** — at minimum: necessary / analytics / marketing / personalization. Necessary cookies don't need consent but must still be disclosed.
- **Withdrawal as easy as giving** — provide a "Cookie preferences" link in the footer that re-opens the banner.
- **No "implied consent by continuing to use the site"** — explicitly invalid under PDPA.

See `templates/consent-banner.md` for the HTML mockup and Thai copy.

## Breach notification (Section 37)
Notify the PDPC within **72 hours** of becoming aware, unless the breach is unlikely to result in risk to rights and freedoms. Notify affected data subjects **without undue delay** if high risk. Include:
- Nature of the breach (what happened, when, attack vector)
- Categories and approximate number of subjects + records
- Categories of personal data affected
- Likely consequences for subjects
- Measures taken and proposed (containment, remediation, notification plan)
- DPO / contact point

## DPO appointment triggers (Section 41)
Required when:
- Core activity = regular and systematic monitoring of data subjects on a large scale (e.g. ad-tech, ride-hailing, loyalty program at scale)
- Core activity = large-scale processing of sensitive data under Sec 26 (e.g. hospitals, HR for tens of thousands of employees)
- The controller / processor is a state agency
- Other criteria prescribed by PDPC sub-notification (check current PDPC notifications)

The DPO must report directly to top management, cannot have a conflict of interest, and their contact must be published in the notice.

## Penalties cheat sheet
- Administrative fines: up to ฿5,000,000 per violation for serious breaches (no-consent processing, unlawful sensitive-data processing, illegal cross-border transfer)
- Criminal: up to ฿1,000,000 and/or 1 year imprisonment for unauthorized disclosure of sensitive data for personal benefit
- Civil: actual damages + punitive damages up to 2× actual damages

## Cross-border transfers (Section 28 / 29) and standard contractual clauses
PDPC issued two notifications in the Royal Gazette on 25 ธ.ค. 2566 (eff. 24 มี.ค. 2567): one under **Sec 28** (adequacy / "whitelist" route) and one under **Sec 29** (appropriate safeguards incl. BCR and standard contractual clauses / สัญญามาตรฐาน). Check the current PDPC notification text before quoting numbers — these are the controlling sub-regulations.

**Practical state:** PDPC has not yet published an adequacy whitelist. In practice, almost every transfer (Cloudflare, AWS, GCP, Azure, Slack, HubSpot, Zendesk, parent-company HR systems) needs a **Sec 29** safeguard.

Lawful routes under Sec 28/29:

| Route | Source | When to use |
|---|---|---|
| Adequacy | Sec 28 + Whitelist Notification | Only if destination is on the PDPC whitelist (none as of writing) |
| BCR (binding corporate rules) | Sec 29 + Safeguards Notification | Intra-group transfers; **must be pre-approved by the PDPC** |
| SCC (สัญญามาตรฐาน) | Sec 29 + Safeguards Notification | Most third-party processor/controller transfers; clauses must meet PDPC minimum content |
| Certification | Sec 29 + Safeguards Notification | Where a PDPC-recognized certification scheme exists |
| Explicit consent | Sec 28(1) | Data subject informed of inadequate protection and consents — fragile, not for routine use |
| Contractual necessity | Sec 28(3)/(4) | Transfer needed to perform a contract with / in the interest of the data subject |
| Vital interest / legal claim / public interest | Sec 28(2)/(5)/(6) | Narrow exceptions |

What to write in the privacy notice (Sec 23(5)+(6) anchor):
- Destination countries (list them — "global cloud providers" is not enough)
- The Sec 28 or Sec 29 route relied on for each
- For SCC: state that PDPC-compliant standard contractual clauses are in place and available on request
- For BCR: state PDPC approval status
- Do not write "we comply with GDPR SCCs" — EU SCCs are not automatically a PDPA Sec 29 safeguard; either re-paper to PDPC SCC or add a Thai addendum

## DPIA — risk assessment (no codified DPIA section)
Important framing: **PDPA does not have a GDPR-style Article 35 "DPIA is mandatory" provision.** What it does have:
- Sec 37(1) — controller must put in place security measures appropriate to the risk
- Sec 39 — Record of Processing Activities (RoPA), which forces you to enumerate purpose, categories, retention, recipients, safeguards
- Sec 40 — same duties on the processor
- PDPC guidance (and SME-exemption carve-outs) treats certain processing as inherently high-risk and effectively expects a written impact assessment

When to run a DPIA (ประเมินผลกระทบด้านการคุ้มครองข้อมูลส่วนบุคคล) even though not statutorily required:
- Large-scale processing of Sec 26 sensitive data (health, biometric, genetic, religion, sexual behavior, criminal record, trade union, etc.)
- Systematic monitoring of a public area or of users (CCTV at scale, employee monitoring, location tracking)
- AI / automated decision-making / profiling that materially affects the subject (credit scoring, AI hiring screen, fraud risk score)
- New technology with unclear risk profile (biometrics for entry, emotion AI, large-scale scraping)
- Children's data at scale
- Any processing the SME RoPA-exemption carve-out catches (risk-creating, not occasional, or sensitive — see Sec 39 ¶3)

Minimum DPIA content (align with PDPC expectations and EU sub-processor due-diligence):
1. Description of processing — purpose, categories, flows, retention
2. Necessity and proportionality assessment against the lawful basis
3. Risk to data subjects' rights and freedoms (likelihood + severity)
4. Mitigations — technical (encryption, pseudonymization, access control) and organizational (DPA, training, retention limits)
5. Residual risk and sign-off by DPO / management

There is no PDPA equivalent of GDPR's "prior consultation" duty, but where residual risk is high and you cannot mitigate, the prudent path is to consult the PDPC before launch and document the consultation.

## Sectoral overlays
PDPA is the floor. Sector regulators add stricter obligations and sometimes carve out specific data types from PDPA entirely. Always check the sector rule on top of PDPA.

| Sector | Regulator | Overlay (non-exhaustive) |
|---|---|---|
| Banking / financial institutions | Bank of Thailand (ธปท.) | BoT Data Governance Guidelines (2564 / 2021); IT-risk and outsourcing notifications; incident reporting to BoT and TB-CERT in parallel with PDPC |
| Credit bureau data | OFIPC / Credit Information Business Act | CIBA governs credit information; credit-bureau operations are largely **outside** PDPA scope — consent and disclosure rules come from CIBA, not Sec 19 |
| Capital markets / securities / digital assets | สำนักงาน ก.ล.ต. (SEC) | Client-data confidentiality under SEC Act and digital-asset notifications; KYC/AML retention duties may override "delete on request" |
| Insurance | คปภ. (OIC) | Insurance-specific customer-data and claims-data rules layered on PDPA |
| Telecom | กสทช. (NBTC) | NBTC notification on protection of telecom users' personal data, privacy, and freedom of communication (replaced the 2549/2006 notification) — extra duties for CDR, location, traffic data |
| Digital ID / e-transactions | MDES, ETDA | Electronic Transactions Act, digital-ID framework; ETDA notifications on trusted service providers |
| Healthcare | กระทรวงสาธารณสุข (MOPH), NHSO, Medical Council | Patient confidentiality under the National Health Act (พ.ร.บ. สุขภาพแห่งชาติ) Sec 7, Medical Profession Act ethics, and MOPH circulars; health data is also Sec 26 sensitive data under PDPA |
| Cybersecurity for CII | สกมช. (NCSA) | Cybersecurity Act 2562 incident reporting for critical information infrastructure — runs in parallel with PDPC breach notice |

When drafting a privacy notice for a regulated entity, state the sector regulator alongside PDPC in the rights / complaints section, and acknowledge sector-specific retention duties (e.g. "5 years under AML / 10 years under SEC rules") rather than promising deletion on request.

## Controller, processor, and "joint controllers" (Section 6)
PDPA codifies two roles, not three:
- **ผู้ควบคุมข้อมูลส่วนบุคคล (data controller)** — the person who decides the purposes and means of processing (กำหนดวัตถุประสงค์และวิธีการ). Holder of the primary duties under Sec 23, 37, 39 and the primary target of enforcement.
- **ผู้ประมวลผลข้อมูลส่วนบุคคล (data processor)** — the person who processes on behalf of and on the instructions of the controller (ประมวลผลตามคำสั่ง). Duties in Sec 40: act only on documented instructions, security measures, record of processing activities, notify the controller of breaches.

**Joint controllership** is not a codified concept in PDPA the way GDPR Art 26 codifies it. PDPC sub-regulations recognize "affiliated business / group of undertakings" — e.g. allowing a shared DPO — but there is no PDPA "joint controller" article that allocates liability between co-controllers. Practical implication: if two entities jointly determine purposes (กำหนดร่วมกัน), each is a controller in its own right and each carries full controller liability to the data subject. Allocate responsibility in a contract, but assume the data subject can sue either of you.

Data processing agreement (DPA / สัญญาประมวลผลข้อมูล) requirements — Sec 40 sets the duty; PDPC has not published a fixed DPA template, but a defensible DPA should include:
- Scope: subject matter, duration, nature and purpose, categories of data and subjects
- Processor obligation to act only on the controller's documented instructions
- Confidentiality of personnel; security measures referencing Sec 37(1)
- Sub-processor controls: prior written authorization and flow-down of equivalent terms
- Assistance with data-subject rights requests and breach notification within timeframes that let the controller meet its own Sec 37 72-hour clock
- Return / deletion of data at end of services
- Audit / inspection rights
- Cross-border transfer terms (Sec 28/29 route used)

Liability to the data subject (who gets sued):
- Pure processor acting within instructions → controller is primarily liable
- Processor exceeds instructions, becomes a de-facto controller for that processing → processor carries controller liability for that scope
- Joint determination of purposes → both are controllers; both are exposed

What to put in the privacy notice:
- Name the controller (Sec 23(7))
- Disclose categories of processors and what they do (cloud hosting, analytics, payments) — naming each by brand is not required by statute but is best practice and increasingly expected
- If there is a co-controller arrangement, name the other controller and which one handles which data-subject rights requests; do not hide behind "our partners"

## Common mistakes
- **Translated GDPR template** — leaves "Art. 6 / Art. 9 GDPR" references; re-cite to Sec 24 / Sec 26 PDPA
- **"By continuing to browse, you consent..."** — invalid; PDPA needs explicit affirmative action
- **Hiding "Reject all"** — direct Sec 19 violation
- **English-only notice on a Thai-targeted site** — PDPC guidance: Thai must be primary; English may be secondary
- **Missing cross-border disclosure** when using Cloudflare / AWS us-east / GCP — these are transfers outside Thailand and must be listed with safeguards
- **"We keep data forever"** — must specify period or determining criteria
- **Treating IP / cookie ID / device ID as non-personal** — PDPA includes them as personal data (Sec 6)
- **No DPO contact in notice** even when DPO is required — Sec 41(3) requires publication
- **Bundling marketing consent with terms acceptance** — Sec 19(4) bars bundled consent for unrelated purposes
- **Forgetting children's data special treatment** — under 10 needs parental consent (Sec 20); 10–20 depends on capacity
- **Citing "GDPR SCCs" as the Sec 29 safeguard** — EU SCCs are not automatically PDPA-compliant; re-paper with PDPC standard contractual clauses or add a Thai addendum
- **Assuming a destination country is "adequate"** — PDPC has not published an adequacy whitelist; default to a Sec 29 safeguard for every transfer
- **Skipping a DPIA for AI hiring / credit scoring / employee monitoring** — no codified DPIA section, but Sec 37/39 + PDPC guidance treat these as high-risk and EU sub-processors will demand the document
- **Treating a SaaS vendor as a "joint controller"** to dodge a DPA — almost all SaaS relationships are controller-to-processor and need a Sec 40 DPA, not a co-controller clause
- **Promising "delete on request" in a regulated sector** — AML, SEC, BoT, NBTC, and medical-records retention duties override the Sec 33 erasure right
- **Ignoring BoT / NBTC / sector incident-reporting clocks** — sector regulators want notice in parallel with the PDPC 72-hour clock, not after it
- **Treating credit-bureau queries as PDPA-governed** — Credit Information Business Act largely displaces PDPA for credit-bureau operations; use CIBA consent language, not Sec 19
