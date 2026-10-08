---
name: oh-pro-se-codearranger
title: Pro Se Drafting Framework — Ohio
description: Use to draft Ohio pro se filings. Triggers include 'Ohio pro se', 'self-represented Ohio', 'Ohio without a lawyer', 'represent myself Ohio Common Pleas', 'Ohio Municipal Court pro se', 'Ohio Self-Help Center'. Covers the Ohio pro-se drafting framework, signature-block conventions (no attorney registration number), affidavit vs. declaration terminology (R.C. 2319.04 affidavit is the Ohio form), Ohio Self-Help Center catalog, and tone conventions for pro-se litigants.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting Framework — Ohio

> **NOT LEGAL ADVICE.** Ohio pro-se litigants face the same
> procedural rules as represented parties (Ohio Civ. R. + per-
> court local rules). The court does not relax standards for
> self-represented filers. For complex matters, or matters with
> substantial sums at stake, consider consulting a licensed
> Ohio attorney.

## Signature block (pro se)

```
Respectfully submitted,

[Your full legal name]
Pro Se
[Address]
[City, State ZIP]
[Phone]
[Email]
```

Important conventions:

- **Designate "Pro Se" or "Self-Represented"** below your
  name. Some Ohio courts use "Pro Per" or
  "Self-Represented Litigant"; "Pro Se" is universally
  accepted.
- **Omit the attorney registration number** (don't make one
  up — Civ. R. 11 sanctions for false attestations).
- **Email is recommended** even for paper filings — Ohio
  courts increasingly serve via email after appearance.
- **No "Esq."** suffix.

## Affidavit form (not "declaration")

Ohio civil practice uses **affidavits** under R.C. 2319.04
and Civ. R. 56(C). The federal-style "declaration under
penalty of perjury" (28 U.S.C. § 1746) is **not** Ohio
practice for state-court filings.

Required elements of an Ohio affidavit:

1. Caption
2. Statement of affiant's competency: "I [name], being
   first duly sworn, state as follows:"
3. Numbered paragraphs of facts within personal knowledge
4. Closing: "FURTHER AFFIANT SAYETH NAUGHT."
5. Affiant's signature
6. **Notarization** — Ohio affidavits require a notary
   public's acknowledgment (or, in limited circumstances,
   another officer authorized to administer oaths under R.C.
   147.07)

If notarization is impractical, Ohio Civ. R. 56(C) allows
unsworn "declarations under penalty of perjury" pursuant to
the federal-style statement in **certain limited Civ. R. 56
contexts**, but the safer practice for any Ohio filing is
the notarized affidavit.

## Tone conventions

- Professional + factual; no ALL CAPS shouting; no emotional
  language
- Number each paragraph in the body of a motion or affidavit
- Use complete sentences in caption, body, and prayer for
  relief
- Refer to yourself as "Plaintiff" / "Defendant" /
  "Petitioner" / "Respondent" depending on role; some pro
  se filers refer to themselves in the first person ("I,
  John Smith, ...") — both are accepted

## Pro-se resources in Ohio

- **Ohio Legal Help** (`ohiolegalhelp.org`) — the
  statewide pro-se forms + procedural guide host
- **Common Pleas court Self-Help Centers** — most Cuyahoga,
  Franklin, Hamilton, and Summit County Common Pleas courts
  operate a Self-Help Center with paid staff to answer
  procedural questions (NOT legal advice)
- **Ohio State Legal Services Association (OSLSA)** —
  income-qualified civil legal aid statewide
- **Volunteer Lawyers Project** — pro bono assistance in
  several Ohio counties
- **Ohio Bar Lawyer Referral Service**: 800-282-6556

## Composition with other oh- skills

- `oh-statewide-format` — caption + signature baseline
- `oh-draft-declaration` — produces Ohio-correct affidavits
  (despite the scaffolder-conventional `declaration` name)
- `oh-fact-check` — citation verification
- `oh-draft-motion` / `-note` / `-order` — pro-se scaffolders
