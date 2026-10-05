# Preservation and legal holds

Read this reference only when the user asks about preservation, legal holds, suspected loss, a Rule 26(f) preservation position, or a hold refresh or release. It provides a U.S. federal civil baseline for lawyer work product; it does not decide the duty, issue or release a hold, direct a custodian, change a system, collect data, or declare spoliation.

## Source and authority ledger

Confirm current law and the actual forum at use time. Keep a source receipt for each material proposition.

| ID | Source | Proposition supported | Limit |
| --- | --- | --- | --- |
| FRCP-2025 | [Federal Rules of Civil Procedure, December 1, 2025](https://www.uscourts.gov/sites/default/files/document/federal-rules-of-civil-procedure.pdf) | Rule 16(b)(3)(B)(iii) scheduling orders; Rule 26(f)(2) preservation discussion; Rule 26(f)(3)(C) ESI preservation planning; Rule 37(e) lost-ESI threshold and remedies | Rules do not supply one universal common-law trigger or hold procedure; local rules, orders, and controlling decisions matter |
| ACN-2015 | [2015 Advisory Committee Note to Rule 37(e)](https://www.uscourts.gov/sites/default/files/2014-09-26-supreme_court-rules_package_final_0.pdf) | Rule 37(e) does not create a duty; reasonable steps do not demand perfection; proportionality, hindsight, and restoration or replacement matter; subdivision (e)(2) requires intent to deprive | Authoritative explanatory note, not a case holding; its Rule 37(e) discussion is limited to ESI |
| FJC-37E | [FJC summary of the 2015 Rule 37(e) amendment](https://www.fjc.gov/publications/amendments-federal-rules-practice-and-procedure-civil-rules-2015-failure-preserve) | Rule 37(e) requires ESI that should have been preserved, failure to take reasonable steps, and inability to restore or replace; it leaves the common-law duty in place | Federal Judiciary educational source, not a holding; Rule 37(e) applies only to ESI |
| FJC-ESI | [Managing Discovery of Electronic Information, Third Edition](https://www.fjc.gov/content/323370/managing-discovery-electronic-information-third-edition) | Early, reasonable and proportionate preservation; knowledgeable personnel; recurring communication; monitoring, collection management, and documentation | Federal Judicial Center guidance for judges; persuasive practice guidance, not binding law |
| SEDONA-HOLDS | [The Sedona Conference Commentary on Legal Holds, Second Edition](https://www.thesedonaconference.org/sites/default/files/publications/Commentary%20on%20Legal%20Holds%20Second%20Edition%20extended%20PC%20period_0.pdf) | Contextual trigger assessment; proportionate scope; custodian and data-steward notice; documentation, monitoring, and release | Influential secondary consensus guidance from 2018; not binding and not a substitute for current authority |
| SILVESTRI | [Silvestri v. General Motors Corp., 271 F.3d 583 (4th Cir. 2001)](https://www.ca4.uscourts.gov/Opinions/Published/002523.P.pdf) | Illustrates pre-filing preservation and the need to preserve or afford inspection of material evidence even when another person possesses it | Fourth Circuit, fact-specific physical-evidence decision; do not generalize its sanctions analysis nationwide |
| HOFFER | [Hoffer v. United States (2d Cir. 2025)](https://www.govinfo.gov/content/pkg/USCOURTS-ca2-22-01377/pdf/USCOURTS-ca2-22-01377-0.pdf) | Illustrates Rule 37(e)(2)'s intent-to-deprive requirement for severe measures | Second Circuit and fact-specific; do not generalize its burden-of-proof treatment without checking the governing circuit |
| SKANSKA | [Skanska USA Civil Southeast, Inc. v. Bagelheads, Inc. (11th Cir. 2023)](https://www.govinfo.gov/content/pkg/USCOURTS-ca11-22-10203/pdf/USCOURTS-ca11-22-10203-0.pdf) | Illustrates that notice issuance alone does not resolve whether implementation steps were reasonable | Eleventh Circuit and fact-specific; does not create a universal mobile-device, backup, or monitoring rule |

Rule 37(e) is a remedial framework, not the source of the duty. It concerns ESI; paper, physical evidence, state proceedings, and other forums can follow different law. Statutes, regulations, court orders, contracts, government investigations, and records regimes can create independent obligations but do not automatically establish the scope of the litigation duty. Check the Judiciary's [current-rules page](https://www.uscourts.gov/forms-rules/current-rules-practice-procedure/federal-rules-civil-procedure) and [pending amendments](https://www.uscourts.gov/forms-rules/pending-rules-and-forms-amendments), then governing law, circuit law, local rules, judge procedures, protective orders, and case-specific orders before giving a conclusion.

## Choose the requested mode

Preservation work can produce one or more of these review-ready artifacts:

1. Trigger and authority issue list.
2. Information-source map and immediate-loss risk register.
3. Proposed preservation scope and action plan.
4. Draft legal-hold notice and acknowledgment plan.
5. Refresh, modification, or release decision record and draft communication.
6. Rule 26(f) preservation agenda or preservation-dispute matrix.
7. Suspected-loss fact record for counsel's Rule 37(e) and other-law analysis.

Return only the requested artifact. Preserve unknowns rather than turning the full lifecycle into a mandatory checklist.

## 1. Assess trigger and authority

Build a dated, sourced trigger record. Capture the claim, threat, demand, complaint, subpoena, investigation, internal report, incident, contemplated affirmative claim, or other event; who knew what and when; how concrete and credible the prospect of litigation was; what information appeared likely to matter at that time; and any independent retention regime. Separate facts known at the decision time from hindsight.

The common federal formulation asks when litigation was reasonably foreseeable or reasonably anticipated, but the controlling jurisdiction's articulation and facts govern. A complaint is not the only possible trigger, and every complaint, business dispute, accident, demand, or investigation does not generate an identical scope. The model should frame the decision for counsel rather than announce a trigger from a keyword.

Output `trigger_status: counsel-decision-needed | asserted-triggered | asserted-not-triggered | disputed | unknown`, with the human or source supplying any assertion. Never convert a prediction into a verified legal conclusion.

## 2. Map information and immediate loss risk

Connect the claims, defenses, remedies, and likely disputed facts to people and information sources. Consider only sources plausibly implicated by the known issues, including as appropriate:

- Current and former custodians, data stewards, records personnel, and knowledgeable IT staff.
- Email, messaging and collaboration platforms, texts, mobile devices, BYOD, shared drives, cloud storage, document systems, and local files.
- Structured databases, source systems, audit logs, transaction systems, source code, model or system logs, websites, social media, recordings, and metadata where material.
- Paper, physical evidence, inspection targets, third-party-controlled information, legacy systems, archives, and disaster-recovery media where their value is not merely duplicative.
- Data created after the asserted trigger when the ongoing matter makes it relevant.

For each source record owner/control, subject matter, period, accessibility, uniqueness or duplication, volume, ordinary retention/deletion behavior, preservation method, cost or burden, privacy or localization constraint, status, owner, and next decision. Flag time-sensitive risks such as auto-delete, ephemeral settings, device replacement, employee departure, account closure, expiring video or logs, system migration, backup rotation, physical alteration, or vendor termination.

Do not equate preservation with collection. A reasonable step may preserve information in place, suspend a deletion rule, snapshot a source, retain a device, or use another technically sound method selected by counsel and knowledgeable personnel. Do not direct technical steps unless the user supplies an authorized process and asks for a draft plan.

## 3. Frame reasonable and proportionate steps

Rule 37(e) calls for reasonable steps, not perfection. Proportionality, party sophistication and resources, information uniqueness, accessibility, likely relevance, burden, and whether substitute information exists can matter. That does not authorize silent omission of a difficult source: record the source, the decision, the known benefit and burden, the alternatives considered, the decision maker, and any need to confer or seek court guidance.

A preservation plan should identify:

| Field | Treatment |
| --- | --- |
| Authority and trigger | Governing sources, facts, date, decision owner, and uncertainty |
| Scope | Issues, periods, custodians, systems, data types, physical evidence, and exclusions with reasons |
| Immediate steps | Time-sensitive loss risks and the proposed responsible person; no system change by the skill |
| Hold communication | Audience, sender, scope, acknowledgment, questions route, confidentiality treatment, and lawyer approval |
| Technical implementation | Data owner, preservation method, validation, exceptions, and dependency on IT/vendor action |
| Monitoring | Acknowledgments, follow-up, new custodians/systems/issues, departures, migrations, and exception handling |
| Documentation | Versioned decision record, notices, recipients, dates, responses, steps, tests, gaps, and changes |
| Coordination | Rule 26(f), opposing positions, protective-order or privacy needs, and possible court guidance |
| Exit | Conditions and authority for modification or release; records and retention consequences |

Do not adopt a universal custodian count, date range, collection method, refresh interval, or rule that every backup must be retained. Do not assume a firm's standard notice proves reasonable implementation in the particular matter.

## 4. Draft a hold notice for lawyer review

A draft notice should be understandable to its recipients and specific enough to act on. Adapt it to the client, audience, governing authority, and systems. Include:

- Matter description sufficient to orient the recipient without unnecessary merits detail.
- Effective date and clear instruction to preserve potentially relevant information within the approved scope.
- Topics, date ranges, systems, devices, accounts, locations, paper, and physical evidence actually selected by counsel.
- Specific direction concerning ordinary deletion, editing, replacement, loss, or disposal practices that counsel and IT have decided must change.
- Treatment of new information created while the hold remains active, if applicable.
- Acknowledgment method, questions contact, exception/escalation route, and statement that the notice remains active until modified or released.

Prepare the notice as `DRAFT FOR LAWYER REVIEW — NOT ISSUED`. Do not choose a privilege legend mechanically; governing law, audience, purpose, client practice, and discoverability risk may affect marking and content. Do not send it, populate recipients from unsourced inference, or state that a recipient has acknowledged it.

## 5. Implement, monitor, refresh, and document

Issuing a notice is not the same as preserving information. The plan should assign human owners for notice delivery, acknowledgments, questions, technical measures, verification, exceptions, and documentation. Counsel should consider whether interviews, sampling, testing, or follow-up with custodians and data stewards are appropriate. Report what was actually done separately from what was requested or planned.

Refresh is event-driven and matter-specific, not automatically six months. Reassess when claims, defenses, parties, custodians, systems, data sources, retention settings, business operations, personnel, discovery demands, court orders, or collection findings materially change. Record additions, removals, reasons, recipients, acknowledgments, unresolved exceptions, and superseded versions.

Departing personnel, device replacement, expiring accounts, migrations, and vendor changes call for an explicit preservation decision before ordinary offboarding or deletion proceeds. The skill may flag and draft the decision request; it does not instruct HR, IT, a vendor, or a custodian to act.

## 6. Confer and address disputes

Rule 26(f)(2) requires discussion of issues about preserving discoverable information, and Rule 26(f)(3)(C) requires the discovery plan to state views and proposals about ESI disclosure, discovery, or preservation. Prepare a concrete agenda: sources and systems, periods, custodians or role groups, inaccessible or ephemeral data, preservation methods, disputed burden and benefit, loss risks, agreed exclusions, discovery sequencing, protective measures, and whether court guidance is needed.

Do not send a preservation demand or tell the user that an opponent's unilateral demand defines the duty. Preserve both positions, evidence of burden and likely value, offers and counteroffers, agreements, unresolved items, and the operative local conferral or motion rule. Route the final letter or email to `correspondence` if that is the requested deliverable.

## 7. Suspected loss

If information may have been altered, destroyed, or become unavailable, preserve the known facts without making a spoliation finding:

- What information and source are involved; whether it is ESI, paper, physical evidence, or mixed.
- Asserted duty and trigger; when the source existed, changed, or was lost.
- Control, retention settings, preservation directions, responsible people, and steps actually taken.
- How loss was detected and whether alteration continues.
- Available copies, recipients, backups, exports, logs, third parties, or additional discovery that may restore or replace it.
- Relevance, prejudice positions, intent evidence if any, and contradictory facts.
- Current authority and the human decisions or urgent containment steps requested.

Do not conceal, overwrite, reconstruct, or selectively curate the evidence. Do not tell the user that negligence automatically permits an adverse inference: Rule 37(e)(2)'s severe measures require intent to deprive, while Rule 37(e)(1) has its own prejudice and cure analysis. Non-ESI and nonfederal law require separate research.

## 8. Modify or release

Prepare a decision checklist rather than assuming that settlement, judgment, inactivity, or administrative closure ends every duty. Check appeals, enforcement, related or reasonably anticipated claims, subpoenas or investigations, insurer/indemnity obligations, court orders, regulatory retention, contractual duties, other holds, privacy restrictions, and firm/client records policy.

Identify the person with authority to modify or release, the scope affected, effective date, systems and custodians, outstanding exceptions, superseded notices, and the retention instruction counsel selected. Draft any communication as `DRAFT FOR LAWYER REVIEW — NOT RELEASED`. Release from this hold does not itself direct immediate deletion; ordinary retention and any other applicable obligation still govern.

## Output and handoff boundary

Every work product should distinguish `reported`, `verified-from-source`, `proposed`, `counsel-decision-needed`, `implemented`, `exception`, and `unknown`. Include the as-of date, source boundary, governing jurisdiction, authority receipt, responsible humans, urgent risks, and actions not taken.

The skill may prepare research, maps, registers, plans, draft notices, decision records, and conferral positions. It must not issue or release a hold, communicate with custodians or opponents, alter retention settings, preserve or collect data, image a device, access an account, delete material, make a privilege decision, or declare compliance or spoliation. Those actions require separate human authority and appropriate technical and legal process.
