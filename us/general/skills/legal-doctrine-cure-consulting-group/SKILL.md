---
name: legal-doctrine-cure-consulting-group
title: Legal Doctrine — Rules, NY Distinctions, Traps
description: Black-letter law and NY practice references with bar-exam traps. Use when analyzing a legal issue (contracts, CPLR, estates, privacy, NIL, IP, cannabis, ethics) or answering a bar-style question.
author: Cure-Consulting-Group
author_url: https://github.com/Cure-Consulting-Group/ProductEngineeringSkills/tree/main/skills/legal/legal-doctrine
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Legal Doctrine — Rules, NY Distinctions, Traps

Answer a legal issue with the correct rule for the stated jurisdiction, applied element by
element. Done means: the governing law (majority/federal/UCC/MPC vs New York) is named, every
element is applied to the facts, the NY distinction is flagged where it changes the result, and
the answer carries the not-legal-advice line when it is about a real matter.

The bar-subject files hold what a frontier model gets wrong unprompted: exact elements, the
majority/minority splits exams test, New York statutes and Court of Appeals rules that depart
from the multistate rule, limitation periods, and traps. They're a `CATALOG` source (see
`legal-research`): good for analysis and exam answers; any rule relied on for a real matter
gets its primary source read and cited through `legal-research`.

## Step 1: Classify the question

| Signal | Law to apply |
|---|---|
| Bar-style multistate question (MBE/MEE) | Majority rule, federal law, Restatement, UCC, or MPC as stated. Not NY |
| NYLE-style, NY forum, or NY facts | New York law. Read the **NY:** lines first |
| Ethics (MPRE) | ABA Model Rules; flag where the NY Rules of Professional Conduct differ |
| Real client matter | New York unless a choice-of-law analysis says otherwise; hand citations to `legal-research` |

## Step 2: Route to the subject file

Read the one file that covers the issue (two if the issue crosses subjects, e.g. a conflicts
question about a tort). Each file opens with a "Load when" line.

| Issue | Reference file |
|---|---|
| Jurisdiction, venue, pleading, joinder, discovery, judgments, preclusion; CPLR practice and limitation periods | `reference/civil-procedure.md` |
| Relevance, character, hearsay, confrontation, privileges, experts; NY evidence (Frye, Molineux, Sandoval) | `reference/evidence.md` |
| Federalism, individual rights, First Amendment, due process, equal protection | `reference/constitutional-law.md` |
| Formation, consideration, statute of frauds, parol evidence, performance, remedies; UCC Art. 2; GOL | `reference/contracts.md` |
| Negligence, intentional torts, strict and products liability, defamation; NY tort damages and CPLR Art. 14/16 | `reference/torts.md` |
| Homicide, inchoate crimes, defenses; 4th/5th/6th Amendment; NY Penal Law and CPL | `reference/criminal-law-procedure.md` |
| Estates, future interests, RAP, landlord-tenant, easements, recording acts, mortgages; RPL/RPAPL | `reference/real-property.md` |
| Agency, partnerships, LLCs, corporations; NY BCL/LLCL | `reference/business-associations.md` |
| UCC Art. 9: attachment, perfection, priority, default | `reference/secured-transactions.md` |
| Wills, intestacy, trusts, fiduciaries; EPTL/SCPA | `reference/trusts-estates.md` |
| Marriage, divorce, equitable distribution, maintenance, child support, custody; DRL/FCA | `reference/family-law.md` |
| Choice of law, interest analysis, borrowing statute, judgments recognition | `reference/conflict-of-laws.md` |
| Agency rulemaking and adjudication, Article 78, FOIL | `reference/administrative-law.md` |
| Lawyer ethics, NY RPC vs ABA Model Rules, UPL, AI use in practice | `reference/professional-responsibility.md` |

**Practice references** (regulatory areas the bar doesn't test; read these for product and client work):

| Issue | Reference file |
|---|---|
| Minors' names, photos, clips; minors' contracts; NY child-data laws; COPPA interplay; athlete agents and NIL | `reference/minors-likeness-nil.md` |
| Breach and safeguards (SHIELD), consumer-health data, recording consent, biometrics, student data (Ed. Law §2-d) | `reference/privacy-health-data.md` |
| Deceptive practices, auto-renewal and free trials, endorsements and reviews, SMS/telemarketing consent | `reference/consumer-protection.md` |
| Copyright and work-for-hire, fair use, trademark clearance, trade dress, open-source licenses, AI-generated works | `reference/ip-licensing.md` |
| NY adult-use cannabis: OCM, 9 NYCRR Parts 113–130, vendor arrangements, federal overlay | `reference/cannabis-ny.md` |
| Software vs the practice of law, lawyer referral and fee-sharing rules, AI legal tools | `reference/legal-tech-upl.md` |

## Step 3: Answer in IRAC

- **Issue**: one sentence per issue; a fact pattern usually hides three or four.
- **Rule**: the governing rule with its elements; name the jurisdiction's version.
- **Application**: each element against the facts, including the facts that cut the other way.
  An exam answer that states the rule and skips the application scores poorly, and a memo
  that does it is useless.
- **Conclusion**: the most likely result and why; note the strongest counter-argument.

For multiple choice: identify the issue the call of the question tests, eliminate choices that
state the right rule for the wrong jurisdiction (the most common distractor), then choose.

Match length to the need; no restated summaries.

## Currency

Law changes. Each reference file is dated; figures marked "confirm before use" were not
source-checked. NY moves to the NextGen bar exam in July 2028 (nine doctrine areas plus
lawyering skills), and the NYLC/NYLE continues alongside it.

## Related

`legal-research` (authority and citation checks), `bar-benchmark` (measure answers against a
scored bank), the `legal-analyst` agent (full memo workflow).
