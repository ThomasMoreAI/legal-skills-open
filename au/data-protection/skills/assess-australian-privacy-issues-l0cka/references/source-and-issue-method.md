# Source and issue method

## Source hierarchy

1. Use the applicable point-in-time text from an official Commonwealth, State
   or Territory legislation publisher for legislation and delegated
   legislation.
2. Use official explanatory materials only to explain legislative context;
   do not let them override enacted text.
3. Use regulator guidance, including OAIC, ACSC, APRA and sector-regulator
   material, as guidance and label it as non-legislative unless it is itself an
   enforceable instrument verified from the official source.
4. Use contracts, policies and standards as separate comparison baselines.
5. Use commentary and discovery results only to locate authoritative material.
   Do not cite them as authority when the primary source is available.

Case law, tribunal decisions and case-derived propositions are outside scope.
Do not use them to resolve ambiguity.

## Legislation routing

- Commonwealth: invoke `$check-commonwealth-legislation` for every material
  title or provision and requested date.
- NSW: invoke `$check-nsw-legislation` for every material title or provision
  and requested date.
- APP framework: invoke `$check-australian-privacy-principles` whenever an APP
  may apply. Use its live inventory and change status; do not rely on the
  candidate-law table as an APP inventory.
- Other States and Territories: route through
  `$route-australian-privacy-jurisdiction`, then use the official publisher and
  preserve title, version, currency and commencement evidence.
- Conflicts, overrides and constitutional questions: identify the issue for
  lawyer review. Do not resolve it without verified authority, and do not use
  case law.

## Candidate-law trigger table

Use this table to generate questions, not conclusions.

| Trigger | Candidate material to verify |
| --- | --- |
| Handling personal information by a private or Commonwealth entity | *Privacy Act 1988* (Cth), including the Australian Privacy Principles and any applicable exemption or special rule |
| Suspected loss, unauthorised access or unauthorised disclosure | *Privacy Act 1988* (Cth) Notifiable Data Breaches provisions; applicable State or Territory privacy and health-records laws; sector-specific reporting regimes |
| NSW public sector or NSW health information | *Privacy and Personal Information Protection Act 1998* (NSW) and/or *Health Records and Information Privacy Act 2002* (NSW) |
| Electronic marketing, calls or messages | *Spam Act 2003* (Cth), *Do Not Call Register Act 2006* (Cth), Privacy Act direct-marketing rules, and telecommunications requirements |
| Consumer Data Right data | Part IVD of the *Competition and Consumer Act 2010* (Cth), CDR rules and data standards |
| My Health Record or healthcare identifiers | *My Health Records Act 2012* (Cth), *Healthcare Identifiers Act 2010* (Cth), Privacy Act and applicable health-records law |
| Critical infrastructure or cyber incident reporting | *Security of Critical Infrastructure Act 2018* (Cth), rules and applicable sector instruments |
| Ransomware or cyber extortion payment/reporting | *Cyber Security Act 2024* (Cth) and applicable rules; verify entity and threshold coverage |
| APRA-regulated entity or regulated service provider | Applicable APRA standards and reporting requirements; distinguish prudential standards from Acts and regulations |
| Surveillance, monitoring, biometrics or employee information | Privacy Act coverage and exemptions; applicable State or Territory surveillance, workplace-surveillance, health-records and public-sector privacy legislation |
| Overseas disclosure, offshore storage or foreign recipient | Privacy Act cross-border rules, contractual allocation and any applicable sector or data-specific restriction |
| Intentional or reckless intrusion, surveillance, scraping, profiling, deepfake, disclosure or publication | Privacy Act Schedule 2 statutory privacy tort, screened independently of APP coverage |
| Automated or AI-assisted consequential decision | Current transparency duties, APP 1.7–1.9 from 10 December 2026, and WA PRIS IPP 10 where applicable |

Also test whether an exemption, small-business rule, employee-records rule,
journalism rule, political exemption, secrecy provision or sector-specific
regime changes the analysis. Verify the current text and threshold; do not
assume an exemption applies from an entity label alone.

## APP issue prompts

After live framework verification, map every verified principle to the facts.
Use these non-authoritative domains to test completeness: governance and
transparency; anonymity or pseudonymity; solicited and unsolicited collection;
collection notice; use and disclosure; direct marketing; overseas disclosure;
government identifiers; data quality; security and lifecycle; access; and
correction. These domains are prompts, not a fixed APP inventory. Add, remove
or revise them when the verified Schedule 1 framework differs.

## Issue-matrix method

For each issue:

1. Quote or pinpoint the material fact without adding facts.
2. State the candidate law and applicability threshold.
3. Record the legislation-skill result or official primary-text check.
4. Distinguish what the verified text says from the provisional application.
5. Identify the missing fact, practical consequence and specific next step.

The matrix structure is informed by the MIT-licensed Harvey AI `harvey-labs`
data-privacy-cybersecurity tasks. Reused concepts are limited to generic
workflow patterns: extract facts, map applicability, compare requirements,
rank urgency, recommend remediation and test against explicit criteria. Do not
copy task scenarios, client artefacts, rubric answers or foreign-law
conclusions into the work product.
