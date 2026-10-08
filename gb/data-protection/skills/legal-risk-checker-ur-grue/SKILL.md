---
name: legal-risk-checker-ur-grue
title: Legal Risk Checker
description: Reviews a story brief, draft article, or broadcast script and flags potential legal risks — including defamation, privacy, contempt of court, and data protection — so you know what to check before publication.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/archive-legal/legal-risk-checker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
tags: [legal, defamation, privacy, contempt, risk, editorial, pre-publication]
---

# Legal Risk Checker

## What This Skill Does
Reviews a story brief, draft article, or broadcast script and flags potential legal risks — including defamation, privacy, contempt of court, and data protection — so you know what to check before publication.

## When To Use This Skill
- Before publishing any story that makes allegations about named individuals, organisations, or institutions
- When a story involves ongoing legal proceedings, criminal investigations, or civil litigation
- When a source is anonymous and the story relies on unverified claims
- When reporting on private individuals (as opposed to public figures acting in a public role)
- When your editor or legal team asks for a pre-publication risk summary
- Before broadcasting or publishing content that may conflict with court injunctions, super-injunctions, or reporting restrictions

## What You Need To Provide
**Required:**
- A summary or draft of the story: the core allegation or claim, who is named, what evidence you hold, and how the story was sourced
- The publication format (web article, print, broadcast, social media post) and intended territory of publication
- Whether any named party has been given the opportunity to respond, and what their response was (or whether they declined to comment)

**Optional:**
- Whether any related legal proceedings are underway (criminal trial, civil case, inquest, tribunal)
- The publication outlet type (national newspaper, local broadcaster, independent digital outlet) — affects the practical exposure level
- Any legal correspondence or threats already received from parties in the story

## How the Assistant Approaches This
1. Reads the story summary and identifies the legal categories that are potentially engaged: defamation, privacy (including data protection), contempt of court, harassment, malicious falsehood, or copyright/confidence. Notes which are relevant and which are not, with brief reasons.
2. For each relevant legal category, flags the specific elements of the story that create risk — naming a claim, naming a source, naming a subject, the nature of the allegation, the strength of the evidence described, and whether a right of reply was offered.
3. Assigns each flag a risk level (Low / Medium / High) with a plain-English explanation: what the risk is, why this part of the story triggers it, and what a court or regulator would likely focus on.
4. Produces a set of concrete pre-publication steps: specific questions to answer, documents to obtain, changes to consider, and the threshold at which legal counsel must be involved before publication.

## Output Format
A structured report in three sections, approximately 400–600 words.

**Legal Categories Engaged** — a short list noting which areas of law are relevant to this story and which are not, with one-sentence rationale for each.

**Risk Flags** — a bulleted list. Each flag identifies: the specific passage or claim that creates the risk, the legal category, the risk level (Low / Medium / High), and a plain-English explanation of what the exposure means in practice.

**Pre-Publication Checklist** — a numbered list of actions to take before publication. Items are specific and ordered by urgency. The final item always states whether the overall risk profile warrants mandatory legal review before publishing.

Tone: direct, professional, non-alarmist. Written for a journalist or editor, not a lawyer. Legal concepts are explained in plain language the first time they appear.

## Quality Criteria
- [ ] Every risk flag identifies the specific claim or passage that triggers it — no vague or general warnings
- [ ] Risk levels (Low / Medium / High) are applied consistently and justified with a reason
- [ ] Output clearly frames findings as flags and questions, not legal verdicts
- [ ] Pre-publication checklist items are specific enough to act on without further interpretation
- [ ] Contempt of court risks are flagged whenever any legal proceedings are mentioned, even peripherally
- [ ] The right-of-reply status is explicitly addressed in the output
- [ ] Output concludes with a clear recommendation on whether mandatory legal review is required

## Example

### Input
Story summary: A regional news outlet is preparing to publish a story about a local property developer. The story alleges that the developer submitted planning applications containing false information about site ownership and that a council planning officer approved applications despite a personal financial connection to the developer. Named individuals: the developer (a private businessman) and the named planning officer (a public employee acting in an official capacity). Evidence held: two planning application documents obtained via freedom of information, an anonymous source within the council, and a company register entry showing a shared business interest. The developer was contacted and declined to comment. The planning officer has not been contacted yet. The story is for a regional news website, UK publication. No known legal proceedings underway.

### Output

**Legal Categories Engaged**

- **Defamation — relevant.** The story makes factual allegations of dishonesty and misconduct against two named individuals. Both the developer and the planning officer could bring defamation claims if the allegations are published and found to be false or insufficiently substantiated.
- **Privacy — low relevance.** The developer is acting in a commercial capacity; the planning officer is acting in a public official capacity. Neither is in a clearly private context. Routine privacy concerns do not apply here, though the anonymous source's identity must be protected.
- **Contempt of court — not currently relevant.** No legal proceedings are reported to be underway. If that changes before publication, this assessment must be revisited immediately.
- **Data protection — low relevance.** The story relies on publicly filed documents and company register entries. Standard editorial exemptions from UK GDPR apply to journalism in the public interest, provided the outlet has a data protection policy in place.
- **Confidence / whistleblower protection — relevant.** The anonymous source within the council may be disclosing information in breach of their employment terms. The outlet has obligations not to expose the source and should consider whether publication could make the source identifiable.

**Risk Flags**

- **Allegation of false statements in planning applications — developer — High risk.** Alleging that a named private individual submitted false documents is a serious factual claim. The evidence base (FOI documents and company register) supports the financial connection but may not directly prove the developer knew the information was false or submitted it with intent. If the allegation goes beyond what the documents demonstrate, there is a significant defamation exposure. *Right of reply was offered and declined — this is a mitigating factor, but does not eliminate risk.*

- **Allegation against the planning officer — Medium risk.** Public officials have a reduced expectation of protection when acting in their official capacity, and public interest in planning corruption is well-established. However, the planning officer has not yet been given the opportunity to respond. Publishing without offering a right of reply substantially increases legal and regulatory risk.

- **Sole anonymous source — Medium risk.** The financial connection (shared business interest) is corroborated by documentary evidence. The allegation that the officer "approved applications despite knowing the connection" rests in part on the anonymous source. If the source's account cannot be independently verified, publishing it as established fact rather than as an allegation carries defamation risk.

- **Source identification risk — Low to Medium risk.** If the anonymous source is one of a small number of people with access to the information they disclosed, publication of the story's details may inadvertently identify them. This is an ethical and legal obligation — consider whether any detail in the story narrows down who the source could be.

**Pre-Publication Checklist**

1. Contact the planning officer immediately and provide a fair opportunity to respond to the specific allegations before publication. Document the contact and any response.
2. Have a media lawyer review the two FOI documents and company register entry to confirm whether they substantiate the allegation of false statements as currently drafted, or whether the allegation needs to be reframed as "apparent" or "alleged."
3. Review every sentence that attributes information to the anonymous source and ask: does this sentence hold up if the source is wrong or lying? If not, obtain independent corroboration or remove the claim.
4. Check whether any planning appeal, judicial review, or police investigation has been initiated since the FOI request was filed — if proceedings are now underway, contempt of court rules apply and legal advice is mandatory before publication.
5. Review the story text to ensure that passages about the anonymous source do not contain details that could identify them within the council.
6. **Overall risk assessment: mandatory legal review is required before publication.** The combination of serious factual allegations against a private individual, an as-yet uncontacted second subject, and partial reliance on a single anonymous source places this story in a category where publication without legal sign-off creates unacceptable exposure for the outlet.

## Known Limitations
- This skill identifies potential legal risk areas and generates questions for editorial and legal review — it does not provide legal advice and is not a substitute for qualified legal counsel. Any story flagged at High risk must be reviewed by a media lawyer before publication.
- Legal frameworks differ significantly by jurisdiction. This skill applies broad principles drawn from UK, EU, and US media law contexts, but the specific rules — particularly on defamation defences, privacy law, and contempt — vary materially by country. Always verify against the law of the territory where you publish.
- This skill reasons only from the information you provide. It cannot verify documents, confirm evidence, assess source credibility, or search court records. If your summary omits key facts, the risk assessment may be incomplete.
- Contempt of court risk changes rapidly when proceedings are active. This skill cannot monitor live legal proceedings — you must actively check whether any story subject becomes involved in legal proceedings between drafting and publication.

## Related Skills
- [image-rights-checker](../image-rights-checker/SKILL.md)
- [defamation-risk-checker](../../magazine-journalism/legal/libel-check-brief/SKILL.md)
- [rights-clearance-checklist](../../media-business/legal/rights-clearance-checklist/SKILL.md)
