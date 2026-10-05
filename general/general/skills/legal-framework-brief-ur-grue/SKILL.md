---
name: legal-framework-brief-ur-grue
title: Legal Framework Brief
description: Produces a plain-language summary of the legal framework applicable to a story — identifying the relevant statutes, regulations, regulatory bodies, and legal principles — so a journalist can report accurately on legal issues without misrepresenting the law or missing key distinctions.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/research/fact-checking/legal-framework-brief
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [research, legal, law, regulation, framework, fact-checking]
---

# Legal Framework Brief

## What This Skill Does
Produces a plain-language summary of the legal framework applicable to a story — identifying the relevant statutes, regulations, regulatory bodies, and legal principles — so a journalist can report accurately on legal issues without misrepresenting the law or missing key distinctions.

## When To Use This Skill
- You are covering a story with legal dimensions and need to understand the applicable laws before writing
- You need to explain a legal issue to a general audience and want to make sure your summary is accurate and accessible
- You are fact-checking a claim about what the law says or requires and need a clear reference framework
- You are interviewing a lawyer, regulator, or official and need enough legal background to ask informed questions

## What You Need To Provide
**Required:** The legal issue or question (be specific — "Is it legal for employers to monitor employees' personal devices?" is better than "employment law"); the jurisdiction (country, state/province, or specify if multiple jurisdictions are relevant).

**Optional:** The specific story context (helps the assistant prioritise which aspects of the law matter most); your current understanding (helps identify what needs correcting or confirming); the audience for your output (general reader, specialist publication, editorial team); whether you need the current law or also the historical evolution.

## How the Assistant Approaches This
1. **Identifies the relevant legal areas.** Determines which branches of law apply to the question — statutory law, regulation, case law, constitutional provisions, or international law. For most journalistic questions, multiple legal areas interact (e.g., a data privacy question involves statute, regulation, and potentially case law).

2. **Summarises the key legal provisions in plain language.** For each relevant statute, regulation, or legal principle, provides a non-technical summary of what it says, who it applies to, and what it requires or prohibits. Uses the actual legal terminology but immediately defines it in plain English.

3. **Identifies the grey areas and contested interpretations.** For any part of the legal framework where the law is ambiguous, contested, or under active litigation, explains the competing interpretations and who holds each position. This is often the most journalistically important part.

4. **Lists the authoritative sources.** Names the specific statutes (with section numbers), regulations, regulatory guidance documents, and landmark court decisions the journalist should reference. For each, provides enough detail to locate the source.

5. **Flags the common mistakes journalists make.** Identifies the specific misstatements or oversimplifications that are common in media coverage of this legal area — and provides the correct framing.

## Output Format
600–900 words. Four sections: **Legal Framework Overview** (plain-language summary of the applicable law, organised by legal area), **Grey Areas and Contested Interpretations** (where the law is unclear or disputed), **Key Sources** (specific statutes, regulations, and cases to reference), and **Common Reporting Mistakes** (2–3 errors to avoid). Tone: clear, authoritative, accessible to a non-lawyer. Legal terms are used but always defined on first use. The output is explicitly not legal advice — it is a journalistic research framework.

## Quality Criteria
- [ ] Legal framework is accurate for the specified jurisdiction — not a generic summary of "how law works"
- [ ] Plain-language explanations are genuinely accessible to a non-lawyer without sacrificing accuracy
- [ ] Grey areas and contested interpretations are identified — the brief does not oversimplify settled-vs-unsettled law
- [ ] Key sources include specific statute names, section numbers, and case names where relevant
- [ ] Common reporting mistakes are real errors seen in media coverage, not hypothetical concerns
- [ ] The brief explicitly states it is not legal advice and that specific cases require qualified legal analysis
- [ ] Output is balanced — does not advocate for any interpretation of contested law

## Example

### Input
**Legal issue:** Can employers legally require employees to use facial recognition technology to clock in and out of work?
**Jurisdiction:** United States (noting that state laws vary significantly)
**Story context:** A warehouse company has implemented mandatory facial recognition timekeeping. Several employees are objecting, and one has contacted a lawyer. I'm writing a news story about the dispute.
**Audience:** General news readership

### Output

**Legal Framework Overview**

*Federal law*
There is no federal statute in the United States that specifically addresses employer use of facial recognition or biometric data. The relevant federal frameworks are indirect:

- **Fair Labor Standards Act (FLSA)** governs timekeeping requirements — employers must keep accurate records of hours worked, but the FLSA does not specify the technology used. Facial recognition timekeeping is not prohibited or required under federal labour law.
- **Americans with Disabilities Act (ADA)** — if facial recognition systems fail to recognise employees with certain physical conditions or disabilities, the employer may have an obligation to provide reasonable accommodations. This is a potential but untested legal argument.
- **National Labor Relations Act (NLRA)** — if employees collectively object to a biometric timekeeping system, their coordinated activity may be protected as concerted activity under the NLRA. This is more likely to apply if the employees are unionised, but Section 7 protections extend to non-union workers engaged in collective action about working conditions.

*State biometric privacy laws*
This is where the law is most directly relevant. A small number of US states have enacted biometric privacy statutes that impose specific obligations on entities collecting biometric data, including facial geometry:

- **Illinois Biometric Information Privacy Act (BIPA), 740 ILCS 14.** The strongest state biometric law. Requires: informed written consent before collecting biometric data; a publicly available written policy on data retention and destruction; prohibits the sale or profiting from biometric data. Critically, BIPA includes a private right of action — individuals can sue employers directly for violations. Statutory damages of $1,000 per negligent violation and $5,000 per intentional or reckless violation. This is the law most likely to be relevant to a dispute over mandatory facial recognition.
- **Texas Capture or Use of Biometric Identifier Act (CUBI), Tex. Bus. & Com. Code Ch. 503.** Requires consent before capturing biometric data and imposes data security and retention obligations. No private right of action — enforcement is through the state attorney general.
- **Washington Biometric Identifier statute, RCW 19.375.** Requires notice and consent. No private right of action.

Several other states have enacted or are considering biometric privacy laws — check the National Conference of State Legislatures database for the most current list.

*Common law*
In states without biometric privacy statutes, employees may have arguments under: common-law invasion of privacy torts; state constitutional privacy protections (where applicable); or contract law (if the biometric requirement was not part of the original employment agreement).

**Grey Areas and Contested Interpretations**

- **Does "consent" mean employees can refuse?** Under BIPA, consent must be given before collection. Courts are still resolving whether employer-mandated biometric systems — where refusal could result in discipline or termination — constitute genuine consent. This is an active area of litigation.
- **Does a timekeeping system constitute "collection" of biometric data?** Some employers argue that systems which convert facial geometry into a mathematical template (rather than storing a photograph) do not collect biometric "information" within the meaning of the statutes. Courts have generally rejected this argument under BIPA, but it remains contested in other jurisdictions.
- **Pre-emption by federal labour law.** If biometric timekeeping is implemented through a collective bargaining agreement, there is an argument that state biometric privacy claims are pre-empted by federal labour law. This has not been definitively resolved.

**Key Sources**

- Illinois BIPA: 740 ILCS 14/1 et seq. — full text available on the Illinois General Assembly website
- Texas CUBI: Tex. Bus. & Com. Code Ch. 503 — full text on Texas Legislature Online
- Washington: RCW 19.375 — full text on Washington State Legislature website
- NCSL biometric law tracker: National Conference of State Legislatures maintains a current table of state biometric privacy legislation
- Key BIPA cases: search legal databases for recent Illinois appellate and federal court decisions interpreting BIPA's consent and private-right-of-action provisions

**Common Reporting Mistakes**

- **Saying "biometric data collection is illegal" without specifying the jurisdiction.** Only a few states have biometric privacy statutes, and their provisions vary significantly. In most US states, there is no specific prohibition on employer use of facial recognition for timekeeping.
- **Conflating biometric privacy laws with general data privacy laws.** State consumer data privacy laws (like those in California, Virginia, or Colorado) have different scopes, exemptions, and enforcement mechanisms than biometric-specific statutes. The employee context further limits applicability, as many consumer privacy laws exempt employment data.
- **Describing BIPA as "the national standard."** Illinois BIPA is uniquely strong because of its private right of action and statutory damages. Reporting on a dispute in another state as if BIPA applies there will mislead readers.

*Note: This brief provides a research framework for journalistic reporting. It is not legal advice. Specific employment disputes require analysis by a qualified attorney in the relevant jurisdiction.*

## Known Limitations
- The assistant's legal knowledge is based on training data and may not reflect the most recent legislative changes, court decisions, or regulatory guidance. The journalist should verify the current state of the law through official legal sources or consultation with a qualified lawyer.
- This skill provides a general framework, not case-specific analysis. The applicability of any law to a specific set of facts requires legal judgment that the assistant cannot provide.
- For jurisdictions outside the common-law tradition (civil law countries, mixed systems), the structure of the legal framework analysis may need to be adapted — the sources, hierarchy of legal authority, and role of case law differ significantly.

## Related Skills
- [claim-origin-tracer](../claim-origin-tracer/SKILL.md) — trace the origin of specific legal claims being made in the dispute
- [debate-state-summary](../../background/debate-state-summary/SKILL.md) — summarise the broader policy debate around biometric privacy regulation
- [legislative-history-brief](../../background/legislative-history-brief/SKILL.md) — trace the legislative history of the applicable statute
- [jargon-translator](../../academic/jargon-translator/SKILL.md) — translate legal terminology into plain language for your audience
