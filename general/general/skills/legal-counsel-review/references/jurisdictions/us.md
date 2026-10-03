# United States — Legal Review Reference Map

> **Disclaimer.** This file is a review map — a structured checklist of where to look, not a statement of current law. Content may be out of date. Every point must be verified against current official sources. Jurisdiction-specific conclusions require qualified US counsel.

Last verified: 2026-05-18

---

## Regime overview

The US has no single federal omnibus privacy or data-protection statute. The legal landscape is a patchwork of federal sectoral laws, state comprehensive privacy acts, and state consumer-protection regimes. Contract law is primarily state common law (Restatement of Contracts; UCC Article 2 for goods). Federal and state regulatory bodies each have independent enforcement authority.

---

## Primary regulators and authorities

| Regulator | Jurisdiction / Focus | Official source |
|-----------|---------------------|-----------------|
| Federal Trade Commission (FTC) | Unfair or deceptive trade practices; privacy and security enforcement for most commercial entities | https://www.ftc.gov |
| Department of Justice (DOJ) | Criminal enforcement; FCPA; antitrust (with FTC); export controls | https://www.justice.gov |
| Securities and Exchange Commission (SEC) | Public-company disclosure; cybersecurity incident disclosure; insider trading | https://www.sec.gov |
| Department of Labor (DOL) | Wage-and-hour (FLSA); ERISA; OSHA | https://www.dol.gov |
| Equal Employment Opportunity Commission (EEOC) | Employment discrimination; harassment | https://www.eeoc.gov |
| Office for Civil Rights (OCR), HHS | HIPAA health-data enforcement | https://www.hhs.gov/hipaa |
| Office of Foreign Assets Control (OFAC) | Sanctions compliance | https://ofac.treas.gov |
| Bureau of Industry and Security (BIS) | Export Administration Regulations (EAR) | https://www.bis.gov |
| State Attorneys General | State privacy acts (CCPA/CPRA, etc.); consumer protection; data-breach notification | Varies by state |
| California Privacy Protection Agency (CPPA) | CCPA/CPRA enforcement | https://cppa.ca.gov |

---

## Primary statutes and regulations (verify current text and amendments)

### Federal — sectoral

| Statute / Regulation | Scope | Official source |
|---------------------|-------|-----------------|
| Federal Trade Commission Act, § 5 | Unfair or deceptive acts; primary privacy enforcement lever for non-covered entities | https://www.ftc.gov/legal-library/browse/statutes/federal-trade-commission-act |
| Health Insurance Portability and Accountability Act (HIPAA) + HITECH | Health information — covered entities and business associates | https://www.hhs.gov/hipaa/for-professionals/index.html |
| Gramm-Leach-Bliley Act (GLBA) | Financial institutions — consumer financial data | https://www.ftc.gov/legal-library/browse/statutes/gramm-leach-bliley-act |
| Family Educational Rights and Privacy Act (FERPA) | Student education records | https://studentprivacy.ed.gov |
| Children's Online Privacy Protection Act (COPPA) | Online data collection from children under 13 | https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa |
| Fair Credit Reporting Act (FCRA) | Consumer reporting agencies; background checks | https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act |
| Electronic Communications Privacy Act (ECPA) | Interception; stored communications; pen registers | https://www.law.cornell.edu/uscode/text/18/part-I/chapter-119 |
| Computer Fraud and Abuse Act (CFAA) | Unauthorized computer access; cybercrime | https://www.law.cornell.edu/uscode/text/18/1030 |
| Foreign Corrupt Practices Act (FCPA) | Anti-bribery; books-and-records | https://www.justice.gov/criminal/criminal-fraud/fcpa |
| Fair Labor Standards Act (FLSA) | Minimum wage; overtime; child labor | https://www.dol.gov/agencies/whd/flsa |
| SEC Cybersecurity Disclosure Rules (2023) | Material cybersecurity incident disclosure; risk-management governance | https://www.sec.gov/corpfin/cybersecurity |

### State — privacy (representative; verify full list against current enactments)

| Statute | State | Official source |
|---------|-------|-----------------|
| California Consumer Privacy Act / CPRA (Cal. Civ. Code § 1798.100 et seq.) | California | https://oag.ca.gov/privacy/ccpa |
| Virginia Consumer Data Protection Act (VCDPA) | Virginia | Verify at https://law.lis.virginia.gov |
| Colorado Privacy Act (CPA) | Colorado | Verify at https://coag.gov/resources/data-privacy-laws/ |
| Connecticut Data Privacy Act (CTDPA) | Connecticut | Verify at https://portal.ct.gov |
| Texas Data Privacy and Security Act (TDPSA) | Texas | Verify at https://capitol.texas.gov |

> Many additional state acts have been enacted or amended since mid-2024. The reviewer must verify the current list of enacted state privacy laws against official state sources or a current legal-counsel summary before any compliance conclusion.

### Data-breach notification

All 50 US states have data-breach notification laws. Timelines, covered data types, and thresholds vary. Verify the applicable state law(s) for each breach scenario at the state attorney general's official website.

---

## Structural review checkpoints

1. **Governing law and forum selection** — identify the stated choice of law and venue. Flag if the clause conflicts with mandatory local law in either party's jurisdiction.
2. **Entity and regulator mapping** — determine which federal and state regulators have jurisdiction over the entity, the data types processed, and the sector.
3. **Privacy and data protection** — identify data types (health, financial, children's, biometric, precise geolocation, credentials). Map to applicable sectoral or state law. Flag if cross-border transfers are involved.
4. **Employment matters** — classify the worker (employee, independent contractor, gig). Check state classification rules (California AB 5 criteria differ from federal FLSA). Flag wage-and-hour, non-compete enforceability (FTC rule status — verify current status with counsel), and restrictive covenants.
5. **Sanctions and export controls** — flag any counterparty, transaction, technology, or geography that could touch OFAC SDN lists or BIS EAR/ITAR controls. Verify against official lists at https://ofac.treas.gov and https://www.bis.gov.
6. **Anti-bribery** — flag any payment to a foreign government official or intermediary. Apply FCPA analysis; confirm whether UK Bribery Act or local law also applies.
7. **Public-company disclosure** — flag material cybersecurity incidents (SEC 8-K 4-business-day rule), material contract changes, and related-party transactions.
8. **Dispute resolution** — note arbitration clauses, class-action waivers, and jury-trial waivers. Check enforceability under applicable state law (some states limit these in employment and consumer contexts).
9. **Limitation of liability and indemnification** — verify whether caps apply to IP indemnity, data-breach indemnity, or gross-negligence/willful-misconduct carve-outs.
10. **Records and retention** — identify applicable retention obligations under the matter's sector, litigation hold status, and state destruction requirements.

---

## Escalation triggers (US-specific)

- Any matter touching OFAC-designated parties, countries, or transactions — escalate immediately; penalties are strict liability.
- FCPA suspicion — escalate to counsel before any internal investigation step that could impair privilege or obstruct.
- HIPAA breach with more than 500 individuals affected — 60-day HHS OCR notification clock; confirm current rule with counsel.
- SEC material cybersecurity incident — 4-business-day 8-K disclosure clock; confirm current rule and materiality threshold with counsel.
- Class-action demand, PAGA notice (California), EEOC charge, or DOL investigation — escalate immediately.
- Non-compete or trade-secret matter in California — California's near-total ban on non-competes is well-established; confirm current FTC rule status with counsel.
- Immigration / work-authorization issue for any employee — escalate to immigration counsel.
- Proposed acquisition or investment touching US critical infrastructure or technology — flag for CFIUS review; verify thresholds with M&A counsel.

---

## Sources (verified in this session)

- California AG CCPA page: https://oag.ca.gov/privacy/ccpa — loaded successfully; confirmed CCPA/CPRA scope, business thresholds, and enforcement structure.
- Cornell LII Wex legal dictionary: https://www.law.cornell.edu/wex — loaded successfully; confirmed as free US legal reference.
- FTC, DOJ, SEC, DOL, EEOC, HHS official domain URLs confirmed accessible in prior sessions; verify individual pages before citing in advice.
