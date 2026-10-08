---
name: prompt-pack-nda-strength-check-sboghossian
title: NDA Strength Check
description: Use when reviewing an existing NDA (mutual or unilateral) to assess whether it adequately protects the disclosing party's confidential information. Evaluates the definition of confidential information, duration of obligations, permitted disclosures, remedies for breach, return/destruction provisions, and residuals clauses. Identifies weaknesses and proposes stronger alternative drafting. Applicable across MENA, EU, UK, and US jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-nda-strength-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# NDA Strength Check

## When to use this

Use this skill when a party needs to evaluate whether an NDA already drafted or received from a counterparty adequately protects the disclosing party's confidential information. The output is a structured review identifying weaknesses and proposing specific redrafted clauses.

Triggers:
- "Evaluate this NDA — does it protect [Company]'s confidential information?"
- "The counterparty sent us their NDA — check how strong it is for us."
- "We're about to share our trade secrets under this NDA — what are the gaps?"

## Required inputs

| Input | Why it matters |
|---|---|
| Full NDA text | The document to be reviewed |
| Party perspective | Are we the disclosing party, receiving party, or both (mutual)? |
| Nature of information to be shared | Trade secrets, financial data, customer lists, technical IP — affects adequacy of the definition |
| Jurisdiction | Determines which law governs and available remedies |

## Optional inputs

- Counterparty identity and context (M&A due diligence vs vendor engagement vs employment)
- Whether the NDA is unilateral (one-way) or mutual
- Whether existing confidential information shared before the NDA is meant to be covered
- Whether a "residuals" clause is acceptable in this context

## Review methodology — five areas

### Area 1: Definition of Confidential Information

**What to check**:
- Is "Confidential Information" defined broadly enough to capture all information you intend to share?
- Does the definition cover: oral disclosures (if confirmed in writing within X days); information in tangible and intangible form; derivative works created from CI?
- Are the exclusions appropriate and appropriately narrow?

**Standard exclusions (acceptable)**:
1. Publicly available information (not through breach of the NDA)
2. Information independently developed by the Recipient without use of CI
3. Information already known to Recipient prior to disclosure (if they can prove it)
4. Information received from a third party without restriction

**Red flags in the definition**:
- Definition limited to "written information marked Confidential": inadequate for oral disclosures or for disclosures made in a data room without consistent marking.
- Exclusion for "information Recipient develops": if not carefully worded, could cover information derived from CI.
- "Necessary" qualifier on oral disclosure confirmation: gives Recipient an argument that no confirmation is needed.

**Stronger drafting example**:
> "Confidential Information means all information disclosed by or on behalf of Disclosing Party to Recipient, in any form or medium, that is identified as confidential at the time of disclosure or that a reasonable person would understand to be confidential given the nature of the information and circumstances of disclosure, including all analyses, compilations, studies, and other materials prepared by Recipient that contain or reflect Confidential Information."

---

### Area 2: Duration of Confidentiality Obligations

**What to check**:
- What is the term of the NDA and the duration of the confidentiality obligation?
- Does the obligation continue after the NDA term?
- Are trade secrets protected indefinitely or only for the contractual period?

**Red flags**:
- 1-year or 2-year confidentiality obligation: inadequate for trade secrets and long-term relationships; technology NDAs often require 3–5 years, trade secrets ideally indefinitely.
- No distinction between general CI (time-limited obligation is acceptable) and trade secrets (should be indefinite under applicable trade secrets law — US DTSA, EU Trade Secrets Directive, UAE unfair competition law).
- NDA expires with no surviving confidentiality clause.

**Stronger drafting**:
> "Recipient's obligations with respect to Confidential Information shall continue for [5] years from the date of disclosure of each item of Confidential Information. Notwithstanding the foregoing, with respect to Confidential Information that constitutes a trade secret under applicable law, Recipient's obligations shall continue for as long as such information retains its status as a trade secret."

---

### Area 3: Permitted Disclosures

**What to check**:
- Who can the Recipient share CI with?
- Is disclosure to employees, contractors, and Affiliates appropriately restricted to those with "need to know"?
- Does each permitted sub-recipient agree to be bound by equivalent obligations?
- Is disclosure required by law / regulatory order covered — and does it require notice to Disclosing Party?

**Red flags**:
- Blanket disclosure to "Recipient's advisors" without restriction: should require NDA terms flowing down.
- Regulatory disclosure carve-out without a notice and assistance obligation: Recipient should be required to promptly notify Disclosing Party and assist in seeking a protective order.
- No limitation to "need to know" employees: CI should not be shared organization-wide.

**Stronger drafting for regulatory carve-out**:
> "If Recipient is compelled by law, regulation, or court order to disclose Confidential Information, Recipient shall (i) provide Disclosing Party with prompt prior written notice (to the extent legally permitted), (ii) cooperate with Disclosing Party in seeking a protective order or other appropriate relief, and (iii) disclose only the minimum amount of Confidential Information required to comply."

---

### Area 4: Remedies for Breach

**What to check**:
- Does the NDA acknowledge that breach would cause irreparable harm?
- Does it provide for injunctive relief (interim / preliminary injunction without bond requirement)?
- Does it include consequential loss as a recoverable head of damages?
- Are there any liquidated damages provisions (note enforceability varies by jurisdiction)?

**Red flags**:
- NDA silent on remedies: parties are left to argue available remedies in court.
- Limitation of liability clause that caps damages: undermines the value of the NDA for trade secrets protection.
- Arbitration clause with no interim measures carve-out: inability to obtain emergency injunctive relief before arbitration is constituted.

**Stronger drafting**:
> "Each Party acknowledges that a breach of this Agreement would cause irreparable harm to Disclosing Party for which monetary damages may be an inadequate remedy, and that Disclosing Party shall be entitled to seek equitable relief, including injunctions and specific performance, without posting a bond or proving actual damages. Nothing in this Agreement shall limit Disclosing Party's right to seek any other remedy at law or in equity."

---

### Area 5: Return and Destruction of Confidential Information

**What to check**:
- On termination or request, must Recipient return or certify destruction of all CI?
- Does the return/destruction obligation cover copies, notes, analyses, and derivative works?
- Is there a carve-out for archival copies retained in backup systems?
- Does Recipient's legal or regulatory retention obligation override the return/destruction obligation?

**Red flags**:
- No return/destruction obligation: CI remains with Recipient indefinitely.
- Carve-out for "backup copies retained in the ordinary course of business" that is not time-limited: gives Recipient indefinite retention of CI on backup servers.

**Stronger drafting**:
> "Upon Disclosing Party's request or upon termination of this Agreement, Recipient shall promptly return or certify destruction of all Confidential Information and all copies, extracts, and derivatives thereof, except for such copies as Recipient is required to retain by applicable law or bona fide automated backup systems (which shall remain subject to this Agreement's confidentiality obligations and shall be destroyed in the normal course of Recipient's backup rotation schedule)."

---

### Bonus Area: Residuals Clause

**What it is**: A residuals clause allows Recipient to use CI retained in the unaided memories of its employees without restriction, even after the NDA terminates. Common in tech industry NDAs (Microsoft, Google standard NDAs include residuals clauses).

**Risk**: A residuals clause can effectively hollow out the NDA's trade secret protection for any information an employee has memorized.

**Recommendation**: Disclosing Party should resist residuals clauses in any NDA covering valuable trade secrets or technical IP. If the counterparty insists, limit the residuals carve-out to general skills and knowledge, not specific technical processes or customer information.

---

## Output format

Produce the review as:

1. **Executive summary** (2–3 sentences): is this NDA adequate for the Disclosing Party's purposes?
2. **Findings table**:

| Area | Finding | Risk level | Recommended fix |
|---|---|---|---|
| Definition of CI | Limited to written, marked materials | High | Expand to cover oral/unmarked CI |
| Duration | 1-year obligation | Medium-High | Extend to 5 years; indefinite for trade secrets |
| Permitted disclosures | No notice on compelled disclosure | Medium | Add notice + assistance clause |
| Remedies | No injunction clause | High | Add irreparable harm / injunction paragraph |
| Return/destruction | No obligation | High | Add return/destroy on request |

3. **Redlined clauses**: for each High and Medium issue, provide a specific revised clause.

## Jurisdictional notes

| Jurisdiction | Key issues |
|---|---|
| **UAE** | Trade secrets protected under the Commercial Transactions Law and Competition Law; courts grant interim injunctions to protect trade secrets; Arabic translation may be required for court enforcement. |
| **DIFC / ADGM** | English law framework; courts enforce NDAs robustly; interim injunctions available on short notice; damages assessed on English law principles. |
| **KSA** | Trade secrets protected under the Protection of Intellectual Property Rights regulations; SAIP enforces trade secret rights; Sharia courts' approach to injunctive relief is evolving. |
| **Lebanon** | Code of Obligations and Contracts; injunctive relief available; enforcement quality is variable given judicial system constraints. |
| **France / EU** | EU Trade Secrets Directive (2016/943) harmonizes trade secret protection across EU member states; France has implemented via Loi Macron. |

## Common mistakes

- **Accepting a counterparty's standard NDA without review**: technology companies routinely send NDAs with residuals clauses and 1-year terms that are heavily Recipient-favorable.
- **Forgetting to check mutual vs unilateral**: a mutual NDA gives both parties identical protections; if the deal is one-directional (Disclosing Party is the party sharing), a unilateral NDA is more appropriate and stronger.
- **Not linking the NDA to downstream agreements**: if the NDA covers due diligence for an M&A transaction, include a clause stating that CI provisions survive the NDA and are incorporated into any subsequent SPA or JV agreement.

## Related skills

- [[prompt-pack-ip-assignment-agreement]]
- [[prompt-pack-ip-due-diligence-checklist]]
- [[prompt-pack-master-services-agreement]]
- [[prompt-pack-joint-venture-agreement]]
- [[prompt-pack-letter-of-intent]]
