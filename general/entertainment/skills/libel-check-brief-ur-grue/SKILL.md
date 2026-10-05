---
name: libel-check-brief-ur-grue
title: Libel Check Brief
description: Reviews a draft article and flags statements that could pose defamation risk, identifying the specific legal concern and specifying what verification, qualification, or right-of-reply is needed before publication.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/magazine-journalism/legal/libel-check-brief
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: entertainment
language: en
tags: [journalism, legal, libel, defamation, editing, pre-publication]
---

# Libel Check Brief

## What This Skill Does
Reviews a draft article and flags statements that could pose defamation risk, identifying the specific legal concern and specifying what verification, qualification, or right-of-reply is needed before publication.

## When To Use This Skill
- A draft contains allegations, characterizations, or accusations about named or identifiable individuals or organizations
- You are writing about ongoing legal proceedings and want to ensure protected reporting language is being used correctly
- An editor needs to know which passages require legal review before a story can publish
- You want to understand the difference between protected opinion and potentially actionable factual claims in your draft

## What You Need To Provide
**Required:** The full text of the draft article, or a detailed excerpt focusing on the passages you are concerned about; the publication jurisdiction (U.S., UK, Australia, or other — libel law varies significantly)
**Optional:** Whether the named individuals are public figures or private individuals (different legal standards apply); whether the publication has already given subjects right-of-reply; any supporting documentation for the most sensitive claims

## How the Assistant Approaches This
1. Identifies every statement in the draft that makes or implies a factual claim about a named or identifiable person or organization — distinguishing statements of fact from protected opinion
2. Assesses each identified statement for defamation risk factors: specificity of the allegation, public vs. private figure status of the subject, verifiability of the claim, and potential for harm to reputation
3. Flags passages where the current language creates unnecessary risk that could be reduced with simple editing — conditional language, attribution, or right-of-reply framing
4. Produces a risk-tiered brief: passages requiring immediate legal review, passages requiring qualification or right-of-reply before publication, and passages that are currently protected
5. Closes with a "Next Step" note: whether to send to a media lawyer immediately (if any Red items are present), which Amber item to address first, and whether claim-verification-checklist should be run in parallel to resolve factual issues alongside legal risk

## Output Format
Tiered brief. Three sections: Red (do not publish without legal review), Amber (requires qualification, right-of-reply, or additional verification), Green (currently protected). Each flagged passage: Quoted text | Risk Category | Legal Concern Explained in Plain Language | Recommended Action | Suggested Rewrite. Every Red and Amber passage MUST include at least one Suggested Rewrite — a concrete, drop-in replacement sentence (or two) that the editor can paste into the draft. The rewrite must preserve the editorial intent of the original passage while reducing legal risk through attribution, qualification, or specificity. Closes with a publication readiness assessment. Language is plain English — journalists should be able to act on this without legal training, but sensitive cases must still go to a media lawyer. Output ends with a "Next Step" note: whether legal review is needed immediately, which Amber item to clear first, and whether to run claim-verification-checklist in parallel.

## Rewrite Patterns
Suggested Rewrites for Red and Amber passages must follow one of these patterns, chosen to match the legal concern:

- **Attribution-based rewrite:** Replace an unsupported assertion with an attributed claim — name the source on the record where possible, or describe the documentary basis. Example: "Hartwell falsified records" → "Court filings in [case], reviewed by [Magazine], allege Hartwell directed staff to falsify records — claims Hartwell denies."
- **Qualification rewrite:** Insert "alleged," "allegedly," "according to," or "reportedly" only where there is a specific source on record. Avoid free-floating "alleged" without naming who is making the allegation.
- **Specificity rewrite:** Replace a broad characterization ("trail of," "pattern of," "history of") with the specific documented examples that support it. If only one example exists, the characterization must be narrowed to that example.
- **Outcome rewrite:** For investigation/charge references, add the resolution (closed without charges, ongoing, charges filed and pending) so the reader does not infer guilt.
- **Right-of-reply rewrite:** Add the subject's response on the record in the same sentence or paragraph; if the subject declined, include the declination language and date of the request.
- **Removal-and-replacement rewrite:** For clearly defamatory characterizations ("con man," "criminal," "fraudster") with no conviction record, remove the term and replace with a sourced description of the conduct.

## Quality Criteria
- [ ] Every potentially actionable statement is captured — no omissions
- [ ] Risk categories are correctly assigned — not everything is Red
- [ ] Legal concerns are explained in plain language without using technical legal jargon incorrectly
- [ ] Recommended actions are specific — "qualify with 'allegedly'" or "get written right-of-reply on record" rather than "needs more work"
- [ ] The brief makes clear this is a first-pass editorial assessment, not a substitute for legal counsel
- [ ] Output includes at least one concrete next action the user can take immediately (send to a media lawyer, resolve the first Amber item, or run claim-verification-checklist)

## Example

### Input
Draft excerpt: A profile of a regional real estate developer, including the following passages:

A) "Over the past decade, Hartwell Development has left a trail of unfinished projects and unpaid contractors."
B) "According to two former employees, CEO Daniel Hartwell personally instructed staff to falsify safety inspection records."
C) "Hartwell was investigated by the state attorney general's office in 2019."
D) "Industry insiders describe Hartwell as a con man who preys on small investors."
E) "The company's most recent development, Riverside Commons, was three years late and over budget — a pattern consistent with Hartwell's other projects."
F) "Hartwell declined to respond to detailed questions submitted in writing."

Publication: U.S. national magazine
Subject status: Hartwell is a private individual who operates primarily in local markets (not a public figure)

### Output

**Libel Check Brief — Hartwell Development Profile**
*Jurisdiction: United States. Subject: Private individual.*

Note: Because Daniel Hartwell appears to be a private individual rather than a public figure, the applicable standard is ordinary negligence in most U.S. states — a lower burden for a plaintiff than the "actual malice" standard that applies to public figures. Handle with corresponding care.

---

**RED — Do Not Publish Without Legal Review**

**Passage B:** "According to two former employees, CEO Daniel Hartwell personally instructed staff to falsify safety inspection records."

*Legal concern:* This is a serious allegation of criminal conduct (falsifying official records) attributed directly to a named private individual by name. "Two former employees" are anonymous in this passage. If Hartwell denies this and sues, anonymous sourcing will not protect the publication. This passage requires: (1) documented on-record right-of-reply from Hartwell specifically to this allegation before publication; (2) corroborating documentary evidence or a third source willing to be identified; (3) legal review before publication regardless of verification status.

*Recommended action:* Do not publish without media lawyer sign-off. Obtain Hartwell's written response to this specific allegation.

*Suggested rewrites (post legal review and right-of-reply):*

- *Attribution + right-of-reply pattern:* "Two former safety inspectors at Hartwell Development, who spoke on condition of anonymity citing concerns about retaliation, said in separate interviews that CEO Daniel Hartwell personally directed them to alter inspection findings on at least three projects between 2017 and 2020. Hartwell, through his attorney, denied the allegation and said the company has 'never instructed any employee to falsify any record.'"
- *Documentary-corroboration pattern (if internal records or filings can be cited):* "According to a 2021 wrongful-termination complaint filed by [named former employee] in [court, case number], reviewed by [Magazine], Hartwell directed staff to falsify safety inspection records. Hartwell denies the allegation, which has not been adjudicated."
- *Removal pattern (if neither attribution nor documentary corroboration can be secured):* Remove the allegation entirely from the article. Do not retain a vaguer version such as "questions have been raised about Hartwell's safety practices" — this carries similar implication with no defensible foundation.

---

**AMBER — Requires Qualification or Right-of-Reply Before Publication**

**Passage A:** "Over the past decade, Hartwell Development has left a trail of unfinished projects and unpaid contractors."

*Legal concern:* "Trail of" is characterization language that implies a pattern of wrongdoing. If this is supportable by specific documented examples — named projects, court records, contractor liens — it may be defensible as fair comment on documented facts. As currently written, it is an unqualified summary characterization that could be challenged as implying broader fraud than the evidence supports.

*Recommended action:* Either (a) replace with a specific enumeration of documented cases ("In three projects over the past decade, Hartwell Development left contractors unpaid, according to court records"), or (b) ensure the body of the article contains enough documented examples to support the lead characterization, and confirm right-of-reply from Hartwell on this characterization.

*Suggested rewrite (specificity pattern):* "Court filings reviewed by [Magazine] show three Hartwell Development projects since 2015 ended with unpaid contractor claims totaling at least $[amount]; in each case, contractors filed mechanic's liens or breach-of-contract suits, [N] of which resulted in judgments against Hartwell."

**Passage D:** "'Industry insiders describe Hartwell as a con man who preys on small investors.'"

*Legal concern:* "Con man" is defamatory on its face if presented as a factual description. The passive attribution "industry insiders describe" does not protect the publication — the magazine is publishing the statement. "Con man" implies criminal fraud; if Hartwell has not been convicted of fraud, this language is a significant liability.

*Recommended action:* Remove "con man" or replace with a direct quote from a named source willing to be identified. If multiple specific fraud allegations are documented in the article, the article's own evidence may be a partial defense — but "con man" language still requires legal review.

*Suggested rewrites (removal-and-replacement pattern):*

- *If documented investor losses exist:* "Several investors who put money into Hartwell projects told [Magazine] they were unable to recover their funds after projects stalled. [Named investor], who invested $[amount] in [project] in [year], said she was given financial projections that 'bore no relation' to what was actually built."
- *If a regulatory or civil judgment exists:* "Hartwell has been the subject of [N] state regulatory complaints from investors since [year]; [outcome of those complaints]."
- *If neither documented losses nor a judgment can be cited:* Remove the passage. Do not retain a softened version such as "described by some as predatory" — the implication remains, the foundation does not.

**Passage C:** "Hartwell was investigated by the state attorney general's office in 2019."

*Legal concern:* This is a factual claim that requires documentary corroboration. Investigations that did not result in charges are sensitive — naming someone as the subject of a government investigation can damage reputation regardless of outcome. Confirm whether this is verifiable from public records (AG press release, court docket, public filing) and whether the investigation is still active or was closed without action.

*Recommended action:* Verify from public record. Add outcome: "The investigation was closed without charges" or "the matter is ongoing," whichever is accurate. Do not leave the reader to assume guilt.

*Suggested rewrites (outcome pattern, choose the one that matches the verified record):*

- *Closed without charges:* "In 2019, the state attorney general's office opened an inquiry into Hartwell Development's handling of investor funds. The inquiry was closed in [month/year] without any charges or enforcement action, according to [public record]."
- *Resolved with a settlement:* "In 2019, the state attorney general opened an inquiry into Hartwell Development; the matter was resolved in [year] when the company agreed to [terms] without admitting wrongdoing."
- *Still ongoing:* "The state attorney general's office opened an inquiry into Hartwell Development in 2019, which the office confirmed remains active as of [recent date]. No charges have been filed."
- *If no public record can be located:* Remove the sentence. Do not publish based on private knowledge that an inquiry occurred without a public-record citation.

---

**GREEN — Currently Protected**

**Passage E:** "The company's most recent development, Riverside Commons, was three years late and over budget."

*Assessment:* If verifiable from public records (building permits, planning documents, contract dates), this is a statement of fact about a company's project, not a personal character attack. It is defensible if accurate. Confirm factual basis and document it.

**Passage F:** "Hartwell declined to respond to detailed questions submitted in writing."

*Assessment:* Standard right-of-reply notation. Legally protected as a factual statement about the reporting process, provided the questions were actually submitted in writing. Keep the original communication on file.

---

**Publication Readiness Assessment**
This draft is not ready for publication in its current form. Passage B (criminal conduct allegation) requires legal review and documented right-of-reply before any publication decision. Passage D ("con man") requires editing or removal. All other passages are addressable through standard editorial steps.

**Next Step:** Send Passage B's suggested rewrites to media counsel today, alongside Hartwell's written request for response. While that proceeds, paste the Passage A and C rewrites into the working draft to clear those Amber items. Run claim-verification-checklist on the full draft in parallel to lock down the underlying factual record.

*This brief is an editorial pre-screening tool. It is not a substitute for review by a qualified media attorney.*

## Known Limitations
- This skill provides editorial guidance on defamation risk — it is not legal advice and does not substitute for review by a qualified media attorney, particularly for Red-category passages.
- Defamation law varies significantly by jurisdiction. This skill applies a general U.S. framework by default; UK, Australian, and other common-law jurisdictions have different standards (UK libel law is substantially more plaintiff-friendly). Always specify jurisdiction.
- The public figure/private individual distinction significantly affects legal exposure. The skill relies on the characterization provided by the user — misidentifying a private individual as a public figure would change the analysis.
- This skill cannot assess whether evidence available to the reporter (but not shared with the skill) would provide a sufficient defense. The legal concept of "truth as a complete defense" depends on the evidence actually held, not just claimed.

## Related Skills
- [claim-verification-checklist](../../fact-checking/claim-verification-checklist/SKILL.md)
- [source-credibility-brief](../../fact-checking/source-credibility-brief/SKILL.md)
- [fact-check-prompt](../../editing/fact-check-prompt/SKILL.md)
