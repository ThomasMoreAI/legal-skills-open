---
name: legal-audit
title: Legal Audit
description: 'Audits PUBLIC, CUSTOMER-FACING web app legal pages (terms of service, privacy policy, HIPAA notice, refund/cancellation policy, cookie banner, age-gating, accessibility statement, jurisdiction-specific notices, AI/algorithmic disclosure) for missing required clauses, ambiguous language, loopholes, and regulatory compliance failures across HIPAA, GDPR, CCPA/CPRA, FTC, ADA, FDA SaMD, CAN-SPAM, PCI-DSS, COPPA, Puerto Rico consumer law, and general US contract law. Make sure to use this skill whenever the user says audit our legal pages, review our terms/privacy/disclaimer/refund policy, check our website for legal compliance, find legal loopholes in our policies, harden our customer-facing legal text, or describes wanting to evaluate ALREADY-LIVE OR ALREADY-DRAFTED public-facing legal text on a website or app. Produces a prioritized findings report with exact citations from the source text and ready-to-paste suggested rewrites graded by severity. Do NOT use for: (a) auditing INTERNAL-only
  terms shown to staff/contractors at login (not customer-facing — handle directly), (b) PROPOSED-but-not-yet-shipped feature/initiative regulatory check (use legal:compliance-check), (c) B2B contract documents like MSA/NDA/DPA/SOW between businesses (use legal:review-contract), (d) SOX 404 internal financial control testing (use finance:audit-support), (e) ongoing compliance program operations like SOC 2/ISO 27001 evidence tracking (use operations:compliance-tracking), or (f) drafting a NEW policy from scratch (this skill audits existing text, not drafts new).'
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/legal-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
sources:
- title: International privacy
  path: references/international-privacy.md
- title: Puerto rico legal
  path: references/puerto-rico-legal.md
- title: State privacy laws
  path: references/state-privacy-laws.md
---

# Legal Audit

Comprehensive review of customer-facing web app legal pages for missing clauses, loopholes, and regulatory failures.

## Pre-audit gate (run BEFORE producing any findings)

Answer these three questions internally. If any is "no" or "unclear", either ask the user or defer to the right skill — do NOT produce findings.

1. **Is the artifact ALREADY LIVE or ALREADY DRAFTED?** If the user is describing a proposed-but-not-yet-built feature/initiative, defer to `legal:compliance-check`. (Do not audit something that doesn't exist yet.)
2. **Is the artifact CUSTOMER-FACING?** If the legal text is shown only to authenticated employees or contractors at internal login, it is not in scope. Handle the request directly without invoking the audit framework, or defer to internal-policy review.
3. **Is the artifact a UNILATERAL POLICY (not a negotiated B2B contract)?** Privacy policies, ToS, refund policies, cookie banners are unilateral and in scope. MSAs, NDAs, DPAs, SOWs are negotiated B2B documents — defer to `legal:review-contract`.

If all three answers are yes, proceed to jurisdictional triage below.

## Common false-positive triggers and the right deferral

| User says... | Looks like legal:legal-audit but actually is... | Defer to |
|---|---|---|
| "Review this DPA our vendor sent us" | B2B contract document | `legal:review-contract` |
| "Will it be legal if we add facial recognition next quarter?" | Pre-launch compliance check | `legal:compliance-check` |
| "Help me draft a new privacy policy" | Drafting (this skill audits, doesn't draft) | Decline, or refer to a vetted template service + counsel |
| "Audit our SOC 2 evidence collection process" | Ongoing compliance program ops | `operations:compliance-tracking` |
| "Test SOX 404 controls for Q4" | Internal financial control testing | `finance:audit-support` |
| "Review the NDA before we sign" | Contract triage | `legal:triage-nda` |
| "Sign this contract and send for signature" | Signature workflow | `legal:signature-request` |
| "Respond to a data subject access request" | Templated legal response | `legal:legal-response` |
| "Audit our internal AUP shown to staff at SSO" | Internal policy (not customer-facing) | Handle directly — out of scope here |

## What "customer-facing" means here (the most-confused boundary)

This skill audits legal text that EXTERNAL USERS (customers, prospects, site visitors) see on a public website or app. Examples that QUALIFY:

- Terms of Service displayed at /terms on your marketing site
- Privacy Policy linked from your homepage footer
- Cookie banner shown to first-time site visitors
- Refund/Cancellation policy in your customer help center
- HIPAA Notice of Privacy Practices on a healthcare app
- Accessibility statement on your public site

Examples that do NOT qualify (and should not trigger this skill):

- Internal employee handbook
- Acceptable Use Policy shown only to internal admin users at login
- Confidentiality terms in employment contracts
- Internal data handling procedures
- Terms shown only inside a private B2B portal to authenticated business users

If the legal text is shown to authenticated employees/contractors only and not to customers, this is the wrong skill. For internal documents, the user can describe the situation directly.

## When to use vs. adjacent audit/compliance skills

This is the most confused skill cluster in the library. The disambiguating questions:

| Question | Skill |
|---|---|
| Are you reviewing a public web page that's already live or already drafted? | **legal:legal-audit (this one)** |
| Are you evaluating whether a proposed-but-not-yet-shipped feature or initiative will create regulatory issues? | `legal:compliance-check` |
| Are you reviewing a B2B contract document (MSA, NDA, DPA, SOW)? | `legal:review-contract` |
| Are you running SOX 404 internal financial control testing? | `finance:audit-support` |
| Are you tracking ongoing compliance program operations (SOC 2/ISO/GDPR/HIPAA evidence)? | `operations:compliance-tracking` |

## Jurisdictional triage (run this FIRST)

Before opening any artifact, establish three things and write them at the top of the audit:

1. **Where is the operator domiciled?** (e.g., Delaware C-corp with PR-domiciled subsidiary)
2. **Where do users come from?** (target markets, country selectors, ad spend, language toggles)
3. **Where is data processed/stored?** (cloud regions, sub-processor locations)

Then walk this triage to load the right reference:

| If users / data touch... | Load |
|---|---|
| Any of 19 enacted US comprehensive privacy state laws (CA, VA, CO, CT, UT, IA, IN, TN, TX, MT, OR, DE, NH, NJ, KY, MD, MN, RI, FL FDBR) | `references/state-privacy-laws.md` |
| EU/EEA, UK, Canada, Brazil, Mexico, other LATAM | `references/international-privacy.md` |
| Puerto Rico residents (consumer or B2B-with-PR-dealers) | `references/puerto-rico-legal.md` |
| WA consumer health data, IL biometric, NY SHIELD, NV PI | sector overlay in `references/state-privacy-laws.md` |

If the answer to (1)/(2)/(3) is unclear from what the user shared, ASK before producing findings — a multi-jurisdiction audit done blind is the most common cause of false-positive Critical findings.

## Audit scope

This skill examines every customer-facing legal artifact:

1. **Terms of Service / Terms of Use**
2. **Privacy Policy** (with sub-sections: data collection, use, sharing, retention, rights, children, international)
3. **Cookie Policy & Cookie Banner** (ePrivacy / state cookie rules)
4. **HIPAA Notice of Privacy Practices** (if PHI processed)
5. **Refund / Cancellation / Subscription Terms** (auto-renewal: CA ARL, NY GBL §§527-a/b, FTC Click-to-Cancel rule)
6. **Acceptable Use Policy** (the customer-facing version, not internal)
7. **DMCA Notice / Copyright Policy** (17 U.S.C. §512 designated agent + safe harbor language)
8. **Accessibility Statement** (ADA Title III; WCAG 2.1 AA reference; EU EAA where applicable)
9. **Age-Gating / COPPA Notice** (under 13) + state minors layer (CA/CT/MD up to 18, etc.)
10. **California-specific Notice** (CCPA/CPRA) — see state-privacy-laws.md
11. **EU/UK-specific Notice** (GDPR, ePrivacy, AI Act) — see international-privacy.md
12. **State-specific notices** for the 19 enacted state laws — see state-privacy-laws.md
13. **Puerto Rico consumer law notices** — see puerto-rico-legal.md
14. **SMS/Email consent language** (TCPA, CAN-SPAM, CASL where Canada-targeted)
15. **AI/Algorithmic disclosure** (EU AI Act Art. 50; CO SB 24-205; CA AB 2013/SB 942 watermarking)
16. **Jurisdiction & dispute resolution** (governing law, arbitration clause, class action waiver, mass-arbitration carveouts)

## Findings classification

Every finding gets:

- **Severity:** Critical (regulatory violation, lawsuit-magnet) / Major (significant gap) / Minor (best-practice deviation)
- **Regulation:** Cite the specific law/section (e.g., "CCPA §1798.100(b)" or "GDPR Art. 13(1)(c)")
- **Verification:** Required on every Critical and Major finding. Use `[verified YYYY-MM-DD]` if the statute/section was confirmed against an authoritative source within the last 90 days; otherwise use `[needs-verification]` and add the finding to the "Citations to verify" appendix.
- **Citation:** Quote the EXACT text from the user's page that is the problem (not paraphrased)
- **Suggested fix:** Concrete rewrite or addition, ready to paste
- **Counsel-review flag:** Yes/No — flag any finding requiring local-jurisdiction counsel before adoption

## Citation verification protocol

Statute section numbers, regulatory citations, and rulemaking references DRIFT. CCPA §1798.100 was renumbered after CPRA. State privacy law section numbers have shifted between draft, enacted, and amended versions (e.g., CT, TX, OR have all renumbered between 2023 and 2025). Court-of-appeals case citations get reordered in reporters. Treating any cited section as accurate by memory is the #1 cause of an embarrassing audit deliverable.

The verification protocol is a hard gate on every Critical and Major finding:

1. **Authoritative source list** (these and ONLY these count as "verified"):
   - Official state legislature site or the codified statute compilation (e.g., leginfo.ca.gov, ct.gov for CGS, legis.iowa.gov)
   - Federal Register / eCFR for federal regulations (ecfr.gov)
   - Official EU OJ for EU instruments (eur-lex.europa.eu)
   - Official ICO/CNIL/AEPD/Garante guidance pages for member-state interpretations
   - Official UK legislation.gov.uk for UK statutes
   - For US case law: West reporter or the issuing court's official slip opinion
2. **Verification tag rules:**
   - `[verified YYYY-MM-DD]` — pulled from authoritative source on that date; section text matches what the finding cites
   - `[needs-verification]` — used when there is no live tool access, when the citation comes from skill knowledge older than 90 days, or when the user has indicated time pressure that doesn't permit a fresh check
   - NEVER omit the tag on a Critical or Major finding
3. **Mandatory secondary check for state privacy laws:** The 2024-2025 wave of amendments has shifted enumerations in CO, CT, TX, OR, NJ, MD, MN, RI. Any citation to one of these statutes carries the tag inline next to the section number, not just at the bottom of the finding.
4. **Honesty default:** If the model has no live retrieval tool, every finding is `[needs-verification]`. The skill must NEVER fabricate a `[verified]` date.

## Citation hygiene checklist (run before findings ship)

Before producing the final report, walk this six-item gate. If any answer is "no", do not ship the report — fix or downgrade.

1. Does every Critical and Major finding carry a `[verified YYYY-MM-DD]` or `[needs-verification]` tag?
2. Do all `[verified]` dates fall within the last 90 days from today?
3. For any state privacy law citation (CCPA, VCDPA, CPA, CTDPA, UCPA, IDAPA, INCDPA, TIPA, MTCDPA, OCPA, DPDPA, NHPA, NJDPA, KCDPA, MODPA, MNCDPA, RICDPA, TDPSA, FDBR), is the section number tagged inline (not paraphrased)?
4. Is every quoted "Citation (verbatim from source)" actually verbatim — no ellipses, no paraphrase, no normalization of capitalization?
5. Is every regulation citation paired with the operative subsection (e.g., GDPR Art. 13(1)(c), not bare "GDPR")?
6. Does the executive summary include a "Citations to verify" appendix listing every `[needs-verification]` finding for the user's counsel to confirm?

## Worked examples

### Example 1 — Catch-all purpose language (GDPR + CCPA)

**Input:** User pastes their privacy policy and asks for an audit.

**Output (excerpt — one finding):**

```
## Finding L-PP-007 — Critical
**Regulation:** GDPR Article 13(1)(c) [verified 2026-04-15] and CCPA §1798.100(a)(1) [verified 2026-04-15]
**Verification:** [verified 2026-04-15] — confirmed against eur-lex.europa.eu (GDPR consolidated text) and leginfo.ca.gov (Cal. Civ. Code §1798.100 as amended by CPRA, current through Ch. 887 Stats. 2024)
**Page:** Privacy Policy, "How We Use Your Information" section
**Citation (verbatim from source):**
  "We may use your information for any purpose related to our business operations, 
  including improving our services and other lawful purposes."

**Problem:** "Other lawful purposes" is a catch-all that fails GDPR's specificity 
requirement (purpose must be specified at collection) and CCPA's notice requirement 
(consumer must know specific purposes at or before collection). This phrasing 
invalidates consent for EU users and creates a CCPA private-right-of-action exposure.

**Suggested fix (ready to paste):**
  "We use your information for the following specific purposes:
   (a) To provide and operate the Services you have requested
   (b) To process payment for paid features
   (c) To send you transactional communications related to your account
   (d) To detect and prevent fraud, abuse, or security threats
   (e) To comply with legal obligations applicable to us
   (f) With your separate, explicit consent, for analytics and product improvement
  
  We will not use your information for new purposes without first updating this 
  Privacy Policy and, where required by applicable law, obtaining your consent."

**Counsel-review flag:** YES — adopt language only after local-jurisdiction counsel 
review confirms it covers your actual data processing operations.
```

### Example 2 — Missing Universal Opt-Out + state-by-state Right to Know (multi-state)

**Input:** User runs a SaaS analytics product, registered in Delaware, processing data of CA, CO, CT, TX, OR, NJ, MD residents. Their privacy policy mentions "If you are a California resident, you have the right to..." and stops there.

**Output (excerpt — one finding):**

```
## Finding L-PP-014 — Critical
**Regulation:** Cal. Civ. Code §1798.135(b)(1) (UOOM honor) [verified 2026-04-15]; 
CCPA Reg. §7025 [verified 2026-04-15]; 
4 CCR 904-3 Rule 5.04 (Colorado UOOM) [verified 2026-04-15]; 
Conn. Public Act 22-15 §6(e)(1) (UOOM Jan 2025) [verified 2026-04-15]; 
Tex. Bus. & Com. Code §541.055(e) (UOOM Jan 2025) [verified 2026-04-15]; 
ORS §646A.578(6) (UOOM Jan 2026) [verified 2026-04-15]; 
NJDPA §11(a)(5)(b) (UOOM ~Jul 2025) [verified 2026-04-15]; 
MODPA §14-4607(a)(4) (UOOM Oct 2025) [verified 2026-04-15].
**Verification:** [verified 2026-04-15] — section numbers cross-checked against each state's official 
legislative compilation. Note that CT, TX, and OR statutes were renumbered between draft and 
enacted versions; cited numbers reflect the currently-codified text. If running this audit more 
than 90 days from the verification date, re-confirm — TX §541 series saw a technical-corrections 
bill in early 2026.
**Page:** Privacy Policy, "Your Rights" section
**Citation (verbatim from source):**
  "If you are a California resident, you have the right to know what personal 
  information we collect, the right to request deletion, and the right to opt-out 
  of the sale of your personal information."

**Problem:** Three defects compound here:
1. Policy enumerates CA rights only and is silent on CO/CT/TX/OR/NJ/MD residents 
   whose statutes ALSO grant rights to access, delete, correct, port, opt-out of 
   targeted advertising, and (where applicable) opt-out of profiling — and require 
   ENUMERATION of these rights in the privacy notice.
2. Policy says "sale" but does not address "share" (CCPA §1798.140(ah)) — covers 
   cross-context behavioral advertising even without monetary exchange. Sephora 
   2022 ($1.2M AG settlement) was for this exact gap.
3. Policy does not mention honoring the Global Privacy Control (GPC) browser signal,
   which is REQUIRED by CA, CO, CT, TX, OR, NJ, MD (and others — see 
   references/state-privacy-laws.md). This is the highest-enforced gap of 2024-2025.

**Suggested fix (ready to paste):**
  "Your privacy rights depend on where you reside. The table below summarizes 
   rights available to residents of US states with comprehensive privacy laws. 
   To exercise any right, email privacy@example.com or use the request form at 
   example.com/privacy-rights.

   | Right | CA | VA | CO | CT | UT | TX | OR | NJ | MD | (others — see policy appendix) |
   |---|---|---|---|---|---|---|---|---|---|---|
   | Access / Know   | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | … |
   | Delete          | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | … |
   | Correct         | Yes | Yes | Yes | Yes | No  | Yes | Yes | Yes | Yes | … |
   | Portability     | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | … |
   | Opt-out of Sale/Share | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | … |
   | Opt-out of Targeted Ads | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | … |
   | Opt-out of Profiling (significant effects) | Yes | Yes | Yes | Yes | No | Yes | Yes | Yes | Yes | … |
   | Limit/Opt-out of Sensitive Data | Yes | Opt-in | Opt-in | Opt-in | Opt-out | Opt-in | Opt-in | Opt-in | Opt-in | … |
   | Right to Appeal | No  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | … |

   We respond within 45 days; we may extend by an additional 45 days with notice.

   **Universal Opt-Out:** We honor browser-based opt-out signals, including the 
   Global Privacy Control (GPC). When we detect a GPC signal from your browser, 
   we treat it as a request to opt-out of the sale and sharing of your personal 
   information for that browser, as required by California, Colorado, Connecticut,
   Texas, Oregon, New Jersey, Maryland, and other applicable state laws.

   **Sale and Share:** We do not sell your personal information for monetary 
   consideration. We may 'share' personal information for cross-context behavioral
   advertising as defined by CCPA §1798.140(ah). You can opt-out at 
   example.com/do-not-sell-or-share."

**Counsel-review flag:** YES — confirm the rights matrix matches your actual 
processing and that the GPC honor implementation has been engineered (not just 
written into the policy). A written commitment without an engineered honor path 
is itself a deceptive-practice exposure under FTC Section 5.
```

### Example 3 — Correct deferral (audit skill recognizes it should NOT run)

**Input:** User pastes a 14-page document and says "Audit this for legal issues — it's our terms with our cloud vendor."

**Expected behavior (excerpt):**

```
Before I run the audit framework on this, the pre-audit gate flags a routing 
question. The document you pasted reads as a Data Processing Addendum + MSA 
between your company and a vendor — it has bilateral signature blocks, 
negotiated indemnity language at §11, and references "the parties" throughout. 
That's a B2B contract, not a customer-facing legal page.

The legal:legal-audit skill is scoped to UNILATERAL customer-facing policies (your 
public ToS, privacy policy, cookie banner, etc.). For a vendor MSA/DPA review 
with playbook-based redlines, the right tool is `legal:review-contract`.

Two paths from here:
1. If you'd like me to run legal:review-contract on this document, say so and 
   I'll switch.
2. If you actually wanted me to audit your CUSTOMER-FACING DPA template (the 
   one you offer DOWNSTREAM customers under GDPR Art. 28), paste that template 
   and I'll proceed with this skill.
```

This is the correct outcome. Producing audit findings on a B2B contract using 
the customer-facing-policy framework would generate false positives (e.g., 
flagging the absence of GPC honor language in a contract that has no end-user 
relationship).

## Output structure

1. **Executive summary** — risk dashboard: count by severity, top 3 critical findings, overall risk posture (Red/Yellow/Green)
2. **Findings table** — sortable by severity, regulation, page
3. **Detailed findings** — one section per finding with the structure shown in the worked example above
4. **Missing pages** — what should exist on the site but doesn't, with regulation requiring it
5. **Jurisdiction gap analysis** — table of jurisdictions you operate in vs. which your terms cover
6. **Re-audit cadence recommendation** — typically annually or after material product/regulatory change

## Specific cybersecurity-relevant patterns to check

For SaaS / cybersecurity products especially:

- **Data Processing Agreement** offered for B2B customers (GDPR Art. 28 requires it)
- **Sub-processor list** published and updated, with subscription option for changes
- **Security disclosure** (vulnerability reporting / responsible disclosure policy with security.txt)
- **SOC 2 / ISO references** that don't overpromise (don't claim "compliant" if you mean "supports workflows for")
- **Data residency commitments** matched to actual infrastructure
- **Incident notification SLA** in line with your DPA commitments (often 72 hours for personal data)
- **Encryption in transit / at rest** statements that match reality (specify TLS version, encryption algorithm)
- **Data retention** specifics (specific period, not just "as long as needed")
- **Government request transparency** (warrant canary or transparency report reference)
- **Customer audit rights** language (typical for enterprise contracts)

## Puerto Rico-specific patterns (PR-based operators)

PR is a hybrid civil/common law jurisdiction with active consumer protection. Quick triggers that demand a deeper pass against `references/puerto-rico-legal.md`:

- Refund/cancellation policy without DACO complaint-mechanism disclosure (Ley Núm. 5; Reglamento 7757)
- Warranty terms not in Spanish for consumer products (Reglamento 8540)
- Choice-of-law clause that strips PR consumer rights for PR residents
- Data breach notice missing Ley Núm. 111 timing commitment
- Healthcare app missing Carta de Derechos del Paciente (Ley 194-2000)
- Arbitration clause that purports to remove DACO jurisdiction (unenforceable; flag)
- Act 60 / Act 22 entity terms that don't disclose PR domicile in governing law

For the 10-item PR audit checklist, statute citations, and the recommended DACO disclosure clause in Spanish, load `references/puerto-rico-legal.md`.

## Tools that should be connected for best output

- The site itself (for live page fetch — Chrome MCP if available)
- Existing legal docs in cloud storage (Box, Drive, Egnyte)
- CLM if templates are stored there
- The user's actual data inventory (to verify privacy policy claims match reality)

## Anti-pattern: don't paste a generic policy

If the audit reveals a missing policy, do NOT generate a generic one to paste. Always:
1. Surface the gap as a finding (Critical or Major depending on regulation)
2. Recommend either custom drafting (note this skill is audit, not drafting) or a vetted template service
3. Flag for legal counsel review before publishing

## Anti-pattern: confident regulatory advice

This skill produces audit findings, not legal advice. Every Critical or Major finding includes a counsel-review flag. The output is for the user to take to counsel, not to publish unreviewed.

## Anti-pattern: stale citation by memory

The single most damaging deliverable is one that cites a renumbered, repealed, or superseded statute by section number from training memory. State privacy laws are amended on a yearly cadence (CT, TX, OR, NJ, MD, MN, RI all saw enumeration changes in 2024-2025). CPRA renumbered swathes of CCPA. EU AI Act final article numbers shifted from the trilogue draft. If a citation cannot be confirmed against an authoritative source within the last 90 days, the finding ships with `[needs-verification]` and is listed in the "Citations to verify" appendix — never as `[verified]` with a guessed date. Fabricating a verification date is a more serious failure than missing a finding.
