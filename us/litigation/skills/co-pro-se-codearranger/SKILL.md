---
name: co-pro-se-codearranger
title: Pro Se Drafting for Colorado
description: This skill should be used when drafting Colorado court documents for a self-represented (pro se) litigant. Triggers include "pro se", "self-represented", "in pro per", "drafting a pro se motion in Colorado", "drafting an answer without a lawyer", "filing without a lawyer in Colorado". Covers the pro-se drafting framework adapted for Colorado civil practice, the C.R.C.P. 5 service rules and CCEFS Pro Se workflow, the JDF (Judicial Department Forms) catalog, the Self-Help Center resources at major courthouses, and Colorado's particular pro se conventions (no attorney-registration number, "Self-Represented" or "Pro Se" designation, sworn-financial- statement requirement under C.R.C.P. 16.2 for domestic cases).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for Colorado

> **NOT LEGAL ADVICE.** This skill helps unrepresented parties
> prepare paper and procedure. It does not substitute for advice from
> a licensed Colorado attorney.

Use this skill in addition to `co-statewide-format` whenever the
filer is unrepresented. Colorado uses the terms "pro se" and
"self-represented" interchangeably; "in pro per" is also accepted but
less common.

## The pro-se drafting framework — adapted for Colorado

The pro-se drafting framework (from *Parker v. Dist. Court for City & County
of Denver*, 173 Colo. 537 (1971), and its successors) sets out the
two-track standard Colorado courts use when reviewing pro se filings:

1. **Substantial compliance with form.** Courts construe pro se
   filings liberally and look past minor formatting errors so long
   as the substantive components are present (caption, claim or
   defense, signature, verification when required).
2. **No substantive advocacy from the bench.** The court will not
   reframe a pro se filer's argument, supply missing elements of a
   claim, or fill gaps in the record.

The practical takeaway: a pro se filing must clearly **name the
relief sought**, **cite the rule or statute** under which that relief
is available, **state facts** that support each element, and
**conclude with a signature** and (where required) a verification.

## Signature block — no attorney-registration number

Colorado-licensed attorneys must include their **Reg. No.** under
C.R.C.P. 11(a). Pro se filers **omit** the registration number and
replace it with a clear self-represented designation:

```
Respectfully submitted this ___ day of __________, 20__.

                                        ____________________________
                                        Jane Q. Doe
                                        [Street address]
                                        [City, CO ZIP]
                                        Phone: (###) ###-####
                                        Email: jane@example.com
                                        Self-Represented Defendant
```

Use **"Self-Represented"** or **"Pro Se"** on the last line. The
designation tracks the filer's role in the case ("Self-Represented
Petitioner", "Pro Se Defendant", "Self-Represented Third-Party
Plaintiff", etc.).

## Service of process and service of pleadings

Pro se filers serve under the same rules as represented parties:

- **C.R.C.P. 4** governs service of the initial complaint /
  petition. A pro se plaintiff cannot personally serve their own
  defendant — use the sheriff (for in-county service), a private
  process server, or another disinterested adult.
- **C.R.C.P. 5** governs service of subsequent papers. If you have a
  CCEFS Pro Se account, e-service is automatic for represented
  opposing parties; otherwise serve by **U.S. Mail**, **hand
  delivery**, or **email under C.R.C.P. 5(b)(2)(E)** (email service
  requires opposing party's prior agreement or court order).

A **Certificate of Service** is required on every filed paper. See
`co-statewide-format` for the certificate template.

## CCEFS Pro Se — the e-filing portal for unrepresented parties

The Colorado Courts E-Filing System (CCEFS) operates a **Pro Se**
track at:

**https://www.jbits.courts.state.co.us/efiling/**

To use it:

1. Create a free account (requires valid email + photo ID
   verification)
2. Search for the existing case by number or party name
3. File the paper as a PDF; pay any associated filing fee by credit
   card or apply for a fee waiver (JDF 205/206)

CCEFS Pro Se is **not yet universal across all 22 JDs** — some
county courts only accept paper filings from pro se parties. Confirm
the filing county's e-filing acceptance before relying on the portal.

## JDF (Judicial Department Forms) catalog

The Colorado Judicial Branch publishes hundreds of standardized
**JDF forms** for pro se use. Use the JDF if one exists for your
filing — courts process JDF-format filings faster and clerks
recognize them on sight.

**Master index**: https://www.coloradojudicial.gov/self-help/forms

Common JDF forms by category:

### Civil (district court)
- **JDF 80** — Civil Cover Sheet (filed with every new complaint)
- **JDF 205** — Motion to File without Payment of Filing Fee
- **JDF 206** — Affidavit Supporting Motion to File without Payment
- **JDF 1402** — Notice of Appeal (limited jurisdiction)

### County Court — Civil
- **JDF 76** — Answer to Complaint (county court)
- **JDF 250** — Notice, Claim, and Summons to Appear (small claims)
- **JDF 251** — Defendant's Response (small claims)

### Domestic Relations (filed in district court)
- **JDF 1099** — Petition for Dissolution of Marriage or Legal
  Separation
- **JDF 1102** — Petition for Declaration of Invalidity of Marriage
  (annulment)
- **JDF 1111** — Sworn Financial Statement (required under C.R.C.P.
  16.2(e))
- **JDF 1820 E** — Child Support Worksheet (electronic)
- **JDF 1116** — Decree of Dissolution / Legal Separation
- **JDF 1129** — Parenting Plan

### Post-judgment
- **JDF 82** — Writ of Continuing Garnishment
- **JDF 84** — Claim of Exemption
- **JDF 90** — Citation to Appear (debtor exam)

## Self-Help Centers

Most populous-county courthouses operate a **Self-Help Center** with
non-lawyer staff who can:

- Help select the right JDF form
- Explain procedure (not advice)
- Witness signatures and notarize documents (some centers)
- Refer to limited-scope-representation lawyers and legal aid

**Self-Help Center locations** (verify hours at the JD page):

- Lindsey-Flanigan Courthouse (Denver)
- Arapahoe County District Court (Centennial)
- Jefferson County (Golden)
- El Paso County (Colorado Springs)
- Adams County (Brighton)
- Boulder County (Boulder)
- Larimer County (Fort Collins)
- Weld County (Greeley)
- Pueblo (Pueblo)
- Mesa County (Grand Junction)

The **Colorado Judicial Branch** also operates a statewide self-help
page:

**https://www.coloradojudicial.gov/self-help**

## Fee waiver — JDF 205 + JDF 206

Pro se filers with limited income should file **JDF 205** (Motion)
together with **JDF 206** (Sworn Financial Affidavit) at the time of
the first filing. The court reviews the affidavit and grants or
denies under C.R.S. § 13-16-103. Approval covers filing fees,
service-of-process fees by sheriff, jury fees, and certain other
charges.

## Common pro se pitfalls in Colorado

1. **Omitting the Division and Courtroom from the caption** — newer
   pro se filings often leave the right-side box blank. Always
   include the assigned Division (chambers number) and Courtroom
   (physical room) once known.
2. **Forgetting the Certificate of Conferral for non-dispositive
   motions** — C.R.C.P. 121 § 1-15(8) requires it. Many pro se
   filers learn this only after summary denial. Include the
   certificate on every motion that is not a 12(b) or 56 motion.
3. **Missing the C.R.C.P. 5 service mechanic** — pro se filers
   without CCEFS access must mail or email-with-permission and
   document service in a Certificate of Service. "Sent by FedEx" or
   "left at their office" without certified evidence does not satisfy
   Rule 5.
4. **C.R.C.P. 16.2 disclosures in domestic cases** — in any
   dissolution / legal separation / allocation of parental
   responsibilities case, both parties must file a **Sworn Financial
   Statement (JDF 1111)** within 42 days of the case being at issue.
   Failure carries serious consequences including default and
   sanctions.
5. **Counting deadlines wrong** — C.R.C.P. 6(a) excludes the
   triggering day but includes the last day, with the C.R.C.P.
   6(a)(1)(C) roll-forward when the last day is a Saturday, Sunday,
   or legal holiday. Use `co-deadlines` to compute correctly.

## Composition

- For statewide format: `co-statewide-format`
- For the specific court: `co-denver`, `co-arapahoe`,
  `co-county-courts`
- For motion drafting: `co-draft-motion`
- For declarations: `co-draft-declaration`
- For consumer-debt defense as pro se: `co-consumer-debt`
- For family-law cases as pro se: `co-family-law`

## References

- `references/pro-se-drafting-framework.md` — case law on pro se construction
- `references/jdf-forms-index.md` — annotated JDF catalog
- `references/self-help-centers.md` — directory and hours
- `references/limited-scope-representation.md` — "unbundled" legal
  services under Colo. R. Prof. Conduct 1.2(c)
