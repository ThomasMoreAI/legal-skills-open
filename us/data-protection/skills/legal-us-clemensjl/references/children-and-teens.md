# Children and teenagers

Status as at 2026-08-05.

The US age threshold that carries federal law is **13**, not 16. There is no US equivalent to Art 8 GDPR. Below 13 the regime is COPPA and it is strict, prescriptive and penalised per violation. Between 13 and 18 there is no federal statute — the duties come from state comprehensive privacy laws, state minors' codes, and FTC Act § 5. Assuming a single "children's data" rule across the age range produces both over- and under-compliance.

## COPPA — 15 U.S.C. §§ 6501–6506; COPPA Rule, 16 CFR Part 312

**Who is covered.** An operator of a website or online service **directed to children under 13**, or an operator of a general-audience service that has **actual knowledge** it is collecting personal information from a child under 13. "Directed to children" is assessed on subject matter, visual and audio content, animated characters, child-oriented activities and incentives, music, age of models, celebrity appeal, advertising placement, and competent and reliable empirical evidence about audience composition (16 CFR § 312.2).

There is no revenue or volume threshold. A one-person operation running a game site is fully covered.

**Core obligations:**

- Post a clear and complete privacy policy describing what is collected from children, how it is used and disclosed (§ 312.4).
- Give direct notice to parents and obtain **verifiable parental consent** before collecting, using or disclosing personal information from a child (§ 312.5).
- Give parents access to the child's information, the ability to refuse further use, and the ability to delete (§ 312.6).
- Do not condition a child's participation on disclosing more information than is reasonably necessary (§ 312.7).
- Establish and maintain reasonable procedures to protect confidentiality, security and integrity (§ 312.8).
- Retain personal information only as long as reasonably necessary for the purpose collected, and delete it securely (§ 312.10).

**The 2025 amendments.** Published 22 April 2025 (Federal Register document 2025-05904). **Effective 23 June 2025.** Compliance date: "Except with respect to Sec. 312.11(d)(1), (d)(4), and (g), regulated entities have until **April 22, 2026** to comply." That date has passed — the amended Rule is fully operative.

What the amendments changed:

- **Separate verifiable parental consent** is required for disclosing a child's personal information to third parties, including for **targeted advertising**. Consent to operate the service no longer carries consent to share for advertising. This is the change with the largest practical impact: a children's site cannot run third-party ad tech on a single consent.
- **Personal information** now expressly includes **biometric identifiers** that can be used for automated or semi-automated recognition.
- A standalone definition of a **mixed audience** website or online service, with age-determination procedures required before collecting personal information.
- **Online contact information** extended to mobile telephone numbers where used solely to text a parent to initiate parental consent.
- A **written children's personal information security programme** and strengthened deletion and retention duties; retention policies must be documented and published rather than left implicit.
- Expanded assessment, disclosure and reporting duties for FTC-approved **Safe Harbor** programmes, including publication of membership lists.

Education technology provisions were **deferred** pending Department of Education FERPA rulemaking.

**Penalties.** COPPA Rule violations are civil-penalty-bearing per violation under 15 U.S.C. § 45(m)(1)(A). The last verified figure is **$53,088 per violation**, effective 17 January 2025 (16 CFR § 1.98, 90 Fed. Reg. 5581); **there was no 2026 adjustment**: OMB Memorandum M-26-11 of 17.04.2026 cancelled the inflation adjustment for 2026, so the January 2025 figure carries through. `[[UNVERIFIED: read against 16 CFR § 1.98 itself — ecfr.gov and federalregister.gov both block automated retrieval (federalregister.gov redirects to an unblock interstitial). The $53,088 figure and the M-26-11 cancellation are corroborated across independent secondary sources but the rule text was not read on 05.08.2026. Confirm before putting a number in a client letter]]` Per violation in COPPA practice has meant per child.

**Do not solve COPPA with an age gate that fails.** A neutral age screen that does not encourage falsification is the mechanism; a checkbox saying "I am over 13" placed after the data has already been collected is not, and a service that receives a birth date indicating under-13 and proceeds has actual knowledge.

## 13 to 18 — no federal statute

There is no federal law protecting teenagers' data as such. The duties come from three other places:

1. **State comprehensive privacy laws.** Several treat data of a known minor as sensitive data requiring opt-in consent, and several prohibit targeted advertising to, or sale of the personal data of, consumers the controller knows or should know are under a stated age (commonly 16, in some states 18). See `state-privacy-scope.md` for which states and which ages.
2. **State minors' codes and social media statutes**, many of which are in litigation.
3. **FTC Act § 5** — an unfair practice claim over design features aimed at minors does not need a specific statute.

## California Age-Appropriate Design Code — partially enjoined

Cal. Civ. Code §§ 1798.99.28–1798.99.40. Its litigation status is regularly misstated in both directions. As at 2026-08-05, following *NetChoice, LLC v. Bonta*, No. 25-2366 (9th Cir., **12 March 2026**), the position is:

**Still enjoined:**

- § 1798.99.31(b)(1)–(4) — the data-use restrictions (materially detrimental use, profiling by default, collection/sale/sharing/retention beyond necessity, secondary use), held unconstitutionally vague on Due Process grounds
- § 1798.99.31(b)(7) — the dark patterns restriction, same ground
- § 1798.99.31(a)(1)(B) — the data protection impact assessment report requirement, enjoined earlier in *NetChoice I*, 113 F.4th 1101 (9th Cir. 2024)
- § 1798.99.35(c)(2) — the 90-day notice-and-cure provision, enjoined in *NetChoice I*

**No longer enjoined** — the Ninth Circuit vacated the remainder of the preliminary injunction:

- the Act's coverage definition and its application as a whole (the facial challenge failed the *Moody v. NetChoice* burden)
- § 1798.99.31(a)(5), the **age estimation** requirement
- the balance of the Act, remanded for severability analysis

Enforcement is by the Attorney General only, § 1798.99.35(a): up to **$2,500 per affected child** for a negligent violation and **$7,500** for an intentional one.

So: "the CAADCA is enjoined" is now wrong, and "the CAADCA is in force" is also wrong. State which provisions. `[[UNVERIFIED: proceedings on remand, and any en banc or certiorari activity after 12 March 2026]]`

## Template — children's privacy notice block

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Children's Privacy</h2>
<p>
  [[OPTION A — GENERAL AUDIENCE, NOT DIRECTED TO CHILDREN:]]
  This service is not directed to children under 13 and we do not knowingly
  collect personal information from children under 13. If we learn that we
  have collected personal information from a child under 13, we will delete
  it. If you believe a child has provided us with personal information,
  contact us at [[EMAIL]].
</p>
<p>
  [[OPTION B — DIRECTED TO CHILDREN: this notice must instead comply in full
  with 16 CFR § 312.4 and state, at minimum: the operator's name, address,
  telephone number and email; what information is collected from children and
  whether it is collected directly or passively; how it is used; that it is
  disclosed to third parties and to whom, and that the parent may consent to
  collection and use without consenting to disclosure; that the operator will
  not condition participation on disclosing more information than reasonably
  necessary; and the parent's rights of review and deletion.]]
</p>
```

Option A is a representation, not a formality. If the service in fact has under-13 users and the operator knows it, the statement is itself a § 5 deception on top of the COPPA violation.

## Checkpoints

- [ ] Determined whether the service is directed to children under 13 against the § 312.2 factors, and the determination written down
- [ ] If mixed audience: age determination performed before any personal information is collected
- [ ] If covered: verifiable parental consent obtained before collection, with the method documented
- [ ] **Separate** parental consent obtained for any disclosure to third parties, including advertising SDKs and analytics
- [ ] No third-party advertising or analytics tags firing on child-directed pages without that separate consent
- [ ] Written children's data security programme in place
- [ ] Retention policy documented and published; deletion actually executed
- [ ] Privacy notice contains every element of 16 CFR § 312.4
- [ ] Parental access, refusal and deletion mechanism built and tested
- [ ] For 13–17 users: checked whether any applicable state law bars targeted advertising or sale without consent, and at what age
- [ ] No claim that the service "complies with the CAADCA" or that the CAADCA is void — state the provision-level position
- [ ] "We do not knowingly collect information from children" verified against actual audience data before it is published
