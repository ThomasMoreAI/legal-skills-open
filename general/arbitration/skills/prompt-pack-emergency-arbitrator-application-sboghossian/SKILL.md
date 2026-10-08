---
name: prompt-pack-emergency-arbitrator-application-sboghossian
title: Emergency Arbitrator Application
description: Use when drafting an application for emergency arbitrator relief under institutional arbitration rules — seeking urgent interim measures before a full tribunal is constituted. Covers the urgency threshold, irreparable harm standard, prima facie case requirement, proportionality, and security for costs. Available under ICC, LCIA, SIAC, DIAC, ADCCAC, and other institutional rules. Trigger when a party to an arbitration agreement needs urgent pre-tribunal relief in hours or days, not weeks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-emergency-arbitrator-application
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Emergency Arbitrator Application

## When to use this

Use this skill when a party to an arbitration agreement needs to apply for urgent interim measures before the main arbitral tribunal has been constituted. Emergency arbitrator (EA) procedures were introduced by major institutions from 2010 onward (ICC in 2012, LCIA from 2010, SIAC from 2010) to fill the gap between the arising of a dispute and the formation of the tribunal.

The EA procedure is appropriate when:
- Assets are being dissipated and the arbitral tribunal cannot be constituted fast enough
- Imminent breach of a key contract clause would cause irreversible damage
- Evidence or documents are at risk of destruction
- A specific action must be taken or restrained within days

**Key threshold distinction**: The EA procedure is not for matters that can wait 3–6 weeks for tribunal constitution. It is for genuine emergencies where the passage of time itself causes the harm.

**Critical limitation**: EA orders are not automatically enforceable in national courts. Before filing, counsel must assess whether the courts of the relevant jurisdiction will enforce EA orders as interim measures.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Arbitration agreement and applicable institutional rules | Determines whether the EA procedure is available and what the rules are | Ask |
| Description of the urgent situation | The factual emergency that justifies EA relief | Ask in detail |
| Relief sought | Exactly what the EA should order (asset freeze, specific performance, status quo preservation, evidence preservation) | Ask with specificity |
| Evidence of urgency | Why this cannot wait for the tribunal to be constituted | Ask |
| Seat of arbitration | Determines enforceability of EA orders in national courts | Ask |
| Prima facie case on the merits | Brief summary of the main claim | Ask |

## Optional inputs

- Willingness to provide security (banks or other assets) if the EA requires it
- Evidence of respondent's financial position (for dissipation risk applications)
- Prior notice given (or why ex parte relief is sought without notice)

## Document structure

### Cover Sheet / Application Header

- Names of parties (Claimant / Respondent)
- Reference to arbitration agreement: document title, date, governing clause number
- Applicable institutional rules (e.g., "Article 29 and Schedule 5 of the 2021 ICC Arbitration Rules")
- Brief description of relief sought
- Request for ex parte consideration (if applicable)

### Section 1 — Introduction and Urgency Summary

Open with a concise statement of the emergency:
> "This application seeks emergency interim relief under [institutional rules] to prevent [Respondent] from [specific action] which, if not immediately restrained, will cause [Claimant] irreparable harm in the form of [specific harm] within [timeframe]."

### Section 2 — Background Facts

Present the background concisely and in chronological order:
- The commercial relationship between the parties
- The relevant contractual obligations
- What has happened to give rise to the emergency
- Timeline of key events (dates matter for urgency assessment)

### Section 3 — The Legal Standards for EA Relief

Most institutional rules require the applicant to demonstrate all of the following:

**a) Urgency**: The matter is so urgent that it cannot wait for the main tribunal to be constituted. Explain specifically: when was the emergency identified? What will happen if relief is not granted in the next [X] days?

**b) Irreparable harm**: Money damages would be an inadequate remedy. Explain why:
- The harm is of a kind that cannot be quantified or compensated after the fact
- The respondent is unlikely to be able to satisfy a damages award (insolvency risk, asset dissipation)
- The harm affects a unique asset, business relationship, or opportunity that cannot be recreated

**c) Prima facie case on the merits**: A reasonable prospect of success on the main claim. This does not require full argument on the merits — a summary showing the contractual or legal basis for the claim is sufficient. Do not over-brief the merits; save that for the main proceedings.

**d) Proportionality**: The relief sought is proportionate to the harm to be prevented. The order will not cause disproportionate harm to the Respondent relative to the benefit to the Claimant.

**e) Balance of convenience** (in some institutional frameworks): Harm to Claimant from denial of relief outweighs harm to Respondent from grant.

### Section 4 — Relief Requested

State with precision what the EA is asked to order:

**Asset preservation order**:
> "An order restraining [Respondent] from transferring, disposing of, encumbering, or otherwise dealing with the following assets: [describe assets] pending final award."

**Status quo preservation**:
> "An order requiring [Respondent] to maintain [specific arrangements/services/supplies] in the ordinary course of business pending constitution of the Tribunal."

**Evidence preservation**:
> "An order requiring [Respondent] to preserve and not destroy, alter, or transfer the following documents or systems: [describe]."

**Specific interim performance**:
> "An order requiring [Respondent] to [take specific action] within [X] days of this order."

### Section 5 — Security

Address whether the Claimant is willing to provide security (a cross-undertaking in damages or financial guarantee) if the EA orders relief. Most institutions give the EA discretion to require security.

### Section 6 — Notice and Ex Parte Relief

- Confirm whether the Respondent has been given notice of this application
- If no notice: explain why ex parte relief is sought (risk that notice would defeat the purpose of the relief, e.g., the Respondent would immediately dissipate assets on learning of the application)
- If notice given: confirm what the Respondent's position is (if known)

### Section 7 — Summary of Relief

One-paragraph summary of the application, the basis for it, and the specific orders sought.

## Jurisdictional notes — EA Procedure Availability

| Institution | EA Provision | Timeline | Key features |
|---|---|---|---|
| **ICC** | Schedule 5 to the ICC Rules 2021 | EA appointed within 2 business days of application fee payment; order within 15 days of file transmission | EA order is not enforceable as ICC award; must be enforced through national courts |
| **LCIA** | Article 9B, LCIA Rules 2020 | EA appointed within 3 days; operates for 14 days or until tribunal constituted | LCIA EA orders are binding on parties; enforcement in courts as interim award |
| **SIAC** | Schedule 1, SIAC Rules 2016 | EA appointed within 1 business day; 14-day window | EA order enforceable in Singapore courts and some others |
| **DIAC** | Article 14, DIAC Arbitration Rules 2022 | EA available; timeline per rules; recent rules reform improved EA process | Enforceability in UAE courts depends on UAE Federal Arbitration Law (Law No. 6 of 2018) |
| **ADCCAC** | Available under updated rules; check current version | Consult current rules | Enforcement through ADGM or Abu Dhabi courts |
| **HKIAC** | Article 23.2 and Schedule 4, HKIAC Rules | EA appointed within 2 days; 15-day window | EA order can be enforced in Hong Kong courts |

### Enforcement considerations

EA orders are **not** automatically binding in the same way as awards. In many jurisdictions, they must be confirmed or domesticated by a national court before enforcement:
- **UAE**: Federal Arbitration Law provides that interim measures ordered by arbitral tribunals can be enforced in UAE courts; EA orders may qualify depending on the applicable rules; seek court confirmation promptly
- **DIFC / ADGM**: DIFC Courts and ADGM Courts are arbitration-friendly; enforcement of EA orders is generally available via a court application
- **KSA**: Saudi courts are less established in enforcing international EA orders; consider parallel national court application (Saudi courts can grant conservative attachments — "hajz tahatiyyati")
- **Lebanon**: Enforcement environment is challenging; consider whether seeking relief in Lebanese courts alongside the EA application is necessary
- **UK / EU / US**: Well-developed frameworks for enforcement of arbitral interim orders

## Common mistakes

- **Failing to meet the urgency threshold**: Applying for EA relief for matters that could wait for a tribunal is a sign of poor judgment and will be rejected; assess urgency objectively.
- **Over-loading the merits section**: EA proceedings are not an opportunity to argue the full case; the prima facie case section should be brief. Overlong submissions delay the EA's decision.
- **Not addressing security**: Failing to offer or address security looks like the applicant has not thought through the application; even if not offering security, explain why it is not appropriate.
- **Inadequate description of the asset or conduct to be restrained**: Vague orders ("restrain the Respondent from dealing with its assets") are too broad; courts and EA arbitrators require specificity.
- **Confusing EA procedure with court injunction**: EA procedures are designed as alternatives to court interim relief; in some jurisdictions, the right to seek court interim relief survives alongside the EA procedure (ICC Rules Art. 29(7)).

## Related skills

- [[prompt-pack-injunction-application]]
- [[prompt-pack-document-production-request]]
- [[prompt-pack-expert-report-arbitration]]
- [[prompt-pack-enforcement-of-judgment]]
