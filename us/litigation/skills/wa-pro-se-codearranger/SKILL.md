---
name: wa-pro-se-codearranger
title: Pro Se Drafting for Washington Courts
description: This skill should be used when drafting Washington court documents for a self-represented (pro se) litigant. Triggers include "pro se", "self-represented", "I'm representing myself", "pro-se drafting framework", "draft without an attorney", or when the user describes themselves as the defendant or plaintiff directly. Covers the  /  drafting framework, service protocols for pro se filers, common pitfalls, and signature block conventions. Layer on top of wa-statewide-format and (if applicable) wa-kcdc.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-pro-se
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

# Pro Se Drafting for Washington Courts

Use this skill when drafting court documents for a pro se litigant. It
encodes the pro-se drafting framework and practical
service and filing protocols that pro se filers need.

> **NOT LEGAL ADVICE.** This skill is a drafting aid for
> self-represented litigants, not legal advice and not a
> substitute for counsel. For complex matters, or matters with
> substantial sums at stake, consider consulting a licensed
> attorney in your jurisdiction. Verify every rule, deadline,
> and citation against current law before filing.

## The pro-se drafting framework

Every motion and declaration follows four principles:

1. **Front-load the strongest facts.** The judge should know the best
   fact in the case within the first paragraph. Do not bury it under
   procedural history.
2. **Keep motions concise.** Target 4–6 pages for a motion + memorandum.
   Use bold lead-ins to let the judge skim. Every sentence earns its
   place.
3. **Write to the judge, not to opposing counsel.** Avoid ad hominem.
   Let the record speak. State facts; let the judge draw the
   characterizations.
4. **Let the record speak.** Attach the documents that prove the point
   and cite to them by exhibit letter and page. A well-indexed record is
   worth more than rhetoric.

## Signature block for pro se

```
____________________________________
[Full Name]
Defendant/Counter-Claimant, pro se
[Street Address]
[City, State ZIP]
[Email]
```

- Use **"pro se"** (not "in pro per" — that's California)
- Include address and email — courts and opposing counsel may serve to
  either
- For declarations, also include a perjury clause above the signature
  (see wa-statewide-format)

## Service protocol

Pro se filers without e-service access should serve by **both** email and
certified mail (USPS Certified with Return Receipt, or Priority Mail
Express with tracking). Always:

1. **Photograph postmarked envelopes before opening** any incoming mail
2. **Memorialize every oral or phone interaction** with opposing counsel
   in writing immediately after it happens
3. **Keep a complete filing log** with date, filing, and service method
4. **Use certified mail** whenever opposing counsel has a documented
   history of false Certificates of Service
5. **Include a Certificate (or Declaration) of Service** with every
   filing, signed and dated

## Common pro se pitfalls and how to avoid them

| Pitfall | Fix |
|---------|-----|
| Overlong motions | Cap at 6 pages; move narrative to declarations |
| Emotional tone | Rewrite as neutral fact statements; let the judge characterize |
| Missing relief clause | Every motion ends with a clear "RELIEF REQUESTED" section |
| Citing to exhibits without attaching them | Always attach, index, and label with exhibit letters |
| Forgetting the perjury clause | Every declaration needs the WA RCW 9A.72.085-style clause |
| Colored or highlighted text | Violates GR 14 — use bold/italic for emphasis instead |
| No Note for Motion Docket | In courts that require scheduling (KCDC, Superior), motions without a note never get heard |
| Ambiguous signature block | Always include name, role (pro se), address, email |

## Drafting checklist (run before filing)

- [ ] Caption is complete and matches the case number exactly
- [ ] First paragraph states the single most important fact
- [ ] Every factual assertion is supported by an exhibit or sworn statement
- [ ] Motion ≤ 6 pages; longer content moved to declaration
- [ ] Relief requested is spelled out at the end
- [ ] Perjury clause present on all declarations
- [ ] Signature block includes name, pro se designation, address, email
- [ ] Footer shows document title and "Page X of Y" on every page
- [ ] GR 14 compliant (3″ top margin page 1, 1″ elsewhere, no color)
- [ ] Certificate of Service attached with date and method
- [ ] All exhibits listed, cover-paged, and referenced in the body

## Companion skills

- Use `wa-statewide-format` for the actual document templates, caption
  structure, and GR 14 formatting
- If the case is in KCDC, use `wa-kcdc` for South Division / Burien
  specifics and CivilMGT docket procedure

## References

- `references/pro-se-drafting-framework.md` — full drafting guide with examples
- `references/service-protocol.md` — service, postmark preservation,
  Certificate of Service templates
- `references/pro-se-toolkit.md` — common motion types and how to draft
  them without counsel
