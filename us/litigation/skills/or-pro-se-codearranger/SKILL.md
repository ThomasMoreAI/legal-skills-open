---
name: or-pro-se-codearranger
title: Pro Se Drafting for Oregon Courts
description: This skill should be used when drafting Oregon court documents for a self-represented (pro se) litigant. Triggers include "pro se", "self-represented", "I'm representing myself", "Parker framework", "draft without an attorney", or when the user describes themselves as the defendant or plaintiff directly. Covers the pro-se drafting framework, service protocols for pro se filers, common pitfalls specific to Oregon practice (including the no-interrogatories quirk and the OSB# signature-block convention), and Oregon-specific pro se resources. Layer on top of `or-statewide-format` and (if applicable) `or-multcc` or `or-wccc`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Pro Se Drafting Framework
  path: references/pro-se-drafting-framework.md
- title: Pro Se Toolkit
  path: references/pro-se-toolkit.md
- title: Service Protocol
  path: references/service-protocol.md
---

# Pro Se Drafting for Oregon Courts

Use this skill when drafting court documents for a pro se
litigant in an Oregon circuit court. It encodes the 
 drafting framework adapted to Oregon procedural
conventions and the practical service and filing protocols pro
se filers need.

> **NOT LEGAL ADVICE.** This skill is a drafting aid for
> self-represented litigants, not legal advice and not a
> substitute for counsel. For complex matters, or matters with
> substantial sums at stake, consider consulting a licensed
> attorney in your jurisdiction. Verify every rule, deadline,
> and citation against current law before filing.

## The pro-se drafting framework

Every motion and declaration follows four principles:

1. **Front-load the strongest facts.** The judge should know the
   best fact in the case within the first paragraph. Do not bury
   it under procedural history.
2. **Keep motions concise.** Target 4–6 pages for a motion +
   memorandum. Use bold lead-ins to let the judge skim. Every
   sentence earns its place.
3. **Write to the judge, not to opposing counsel.** Avoid ad
   hominem. Let the record speak. State facts; let the judge
   draw the characterizations.
4. **Let the record speak.** Attach the documents that prove the
   point and cite to them by exhibit number and page. A well-
   indexed record is worth more than rhetoric.

## Signature block for pro se (Oregon)

```
____________________________________
[Full Name]
Defendant, pro se
[Street Address]
[City, OR ZIP]
[Phone]
[Email]
```

- Use **"pro se"** (Oregon convention, same as Washington)
- **Omit OSB number** — that's for licensed Oregon attorneys.
  Including a fake OSB# is grounds for sanctions and could
  qualify as unauthorized practice of law (ORS 9.160).
- Include phone (required for chambers contact)
- Include email (most courts and opposing counsel serve
  electronically by default)
- For declarations, also include the perjury clause (ORCP 1 E)
  above the signature

## Service protocol — Oregon

### Initial summons and complaint (ORCP 7)

If you (as plaintiff) are filing a new case, the summons and
complaint must be served per ORCP 7 — File and Serve cannot
serve initial process. Hire a process server or sheriff for
personal service unless the defendant has agreed in writing to
accept service by mail.

### Subsequent filings (ORCP 9, UTCR 21.100)

After the initial complaint, all subsequent filings are served
under ORCP 9. Acceptable methods:

- **eService through File and Serve** — for parties registered
  for eService (most attorneys, some pro se litigants)
- **Email** — if the parties agreed in writing or the receiving
  party has eService registered
- **Mail (USPS first-class)** — universally acceptable
- **Hand delivery** — universally acceptable

Pro se filers without eService access should serve by **both**
email and certified mail (USPS Certified with Return Receipt, or
Priority Mail with tracking) — belt and suspenders.

### Service best practices for pro se

1. **Photograph postmarked envelopes before opening** any
   incoming mail from the court or opposing counsel — date of
   postmark is sometimes important
2. **Memorialize every oral or phone interaction** with opposing
   counsel in writing immediately after it happens (a short
   email "to confirm our call today" is a contemporaneous
   record)
3. **Keep a complete filing log** — date, filing, service
   method, recipient
4. **Use certified mail** whenever opposing counsel has a
   documented history of false Certificates of Service
5. **Include a Certificate of Service (UTCR 1.090)** with every
   filing, signed and dated

## Common pro se pitfalls — Oregon-specific

| Pitfall | Fix |
|---------|-----|
| Overlong motions | Cap at 6 pages; move narrative to declarations |
| Emotional tone | Rewrite as neutral fact statements; let the judge characterize |
| Missing relief clause | Every motion ends with a clear "RELIEF REQUESTED" section |
| Citing exhibits without attaching | Always attach, index, and label with exhibit numbers (NOT letters — Oregon convention) |
| Forgetting the ORCP 1 E perjury clause | Every declaration needs the "I declare under penalty of perjury under the laws of the State of Oregon..." clause |
| Colored or highlighted text | Violates UTCR 2.010 — use bold/italic for emphasis |
| Missing Notice of Hearing | Most counties require a Notice of Hearing to set the motion on calendar |
| Ambiguous signature block | Always include name, "pro se" designation, address, phone, email — NO OSB# |
| Trying to serve interrogatories | **Oregon does not permit interrogatories under ORCP without a court order.** Use RFPs (ORCP 43) and depositions instead. See `or-discovery`. |
| Citing "CR 12(b)(6)" | Use **ORCP 21 A(8)** — Oregon's analog to FRCP 12(b)(6) |
| Citing "RCW" or Washington rules | Oregon uses **ORS** (Oregon Revised Statutes), not RCW |
| Using "vs." | Oregon uses **"v."** (with period) — not "vs." |
| Lettered exhibits (A, B, C) | Oregon convention is **numbered** (1, 2, 3) |
| Filing federal-style citations | Oregon Style Manual uses no periods in "Or", "Or App", "P3d", "USC", "CFR" |

## Drafting checklist (run before filing)

- [ ] Caption is complete and matches the case number exactly
- [ ] Court header uses "IN THE CIRCUIT COURT OF THE STATE OF
      OREGON" + "FOR THE COUNTY OF [COUNTY]"
- [ ] Parties separator is "v." (with period), not "vs."
- [ ] First paragraph states the single most important fact
- [ ] Every factual assertion is supported by an exhibit or
      sworn statement
- [ ] Motion ≤ 6 pages; longer content moved to declaration
- [ ] Relief requested is spelled out at the end
- [ ] Perjury clause (ORCP 1 E form) present on all declarations
- [ ] Signature block includes name, pro se designation,
      address, phone, email — NO OSB#
- [ ] Footer shows document title and "Page X of Y" on every
      page
- [ ] UTCR 2.010 compliant (3″ top margin page 1, 1″ elsewhere,
      no color)
- [ ] Certificate of Service attached with date and method
- [ ] All exhibits listed, cover-paged, and referenced in the
      body by **number** (not letter)
- [ ] Confidential personal info redacted per UTCR 2.120 (SSN
      last 4 only, etc.)

## Oregon-specific pro se resources

### Statewide

- **OJD Self-Help page**: https://www.courts.oregon.gov/help
- **Statewide forms**: courts.oregon.gov/forms
- **Statewide eFiling help**: (855) 642-9748 (Tyler Tech
  support)

### Legal aid

- **Legal Aid Services of Oregon** (LASO): income-eligible
  representation; offices in Portland, Salem, Eugene, Medford,
  Klamath Falls, Pendleton, etc.
  https://lasoregon.org/
- **Oregon Law Center** (OLC): farm-worker and rural-civil
  representation
  https://oregonlawcenter.org/
- **CLEAR Legal Hotline**: (800) 520-5292 (Mon–Fri)
- **Oregon State Bar Lawyer Referral Service**: (503) 684-3763
  or (800) 452-7636
- **OSB Modest Means Program**: reduced-fee referrals
  https://www.osbar.org/public/ris/modestmeans.html

### County-specific

- **Multnomah Civil Self-Help**: Floor 3, Central Courthouse
- **Washington Co Civil Self-Help**: limited; Civil Division
  counter answers procedural questions
- **Lane**: Eugene Justice Center has a Civil Self-Help
  counter
- **Marion**: Salem courthouse has a self-help kiosk

## Companion skills

- Use `or-statewide-format` for the actual document templates,
  caption structure, and UTCR 2.010 formatting
- If the case is in Multnomah Circuit Court, use `or-multcc`
  for chambers / JA / SLR specifics
- If the case is in Washington County, use `or-wccc` for Civil
  Division / SLR specifics
- For any other Oregon county, use `or-county-courts`

## References

- `references/pro-se-drafting-framework.md` — full drafting guide with
  Oregon-flavored examples
- `references/service-protocol.md` — service, postmark
  preservation, Certificate of Service templates per UTCR 1.090
- `references/pro-se-toolkit.md` — common motion types and how
  to draft them without counsel
