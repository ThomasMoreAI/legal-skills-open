---
name: draft-board-resolution-sboghossian
title: Draft — Board Resolution
description: Use when asked to draft a board resolution (written consent or meeting minutes format) for a corporate decision. Covers both the written unanimous resolution form and the meeting-based resolution form, with templates for the most common resolutions (share issuance, director appointments, M&A approvals, bank authorizations, dividends), and jurisdiction-specific notes for UAE, KSA, Lebanon, DIFC/ADGM, and EU civil-law systems.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-board-resolution
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Draft — Board Resolution

## When to use this

Use this skill when the board of directors of a company needs to formally authorize or record a corporate decision. Board resolutions serve as the company's documentary evidence of authority — they are required by banks, counterparties, registrars, and courts as proof that the named individuals are authorized to act.

## Two forms of board resolution

### Form 1 — Written unanimous resolution (signed consent)
Used when:
- The decision is uncontroversial and all directors will sign.
- Speed is needed (no meeting logistics).
- The jurisdiction permits written resolutions in lieu of a meeting (see jurisdictional notes).

**Structure**:
```
WRITTEN RESOLUTION OF THE BOARD OF DIRECTORS
OF [COMPANY NAME]
([REGISTRATION NUMBER / JURISDICTION])

Dated: [DATE]

The undersigned, being all the directors of [Company Name] 
(the "Company"), hereby unanimously resolve as follows:

RESOLVED THAT: [precise resolution text]

RESOLVED FURTHER THAT: [any further resolution]

IN WITNESS WHEREOF, the undersigned have executed this Written 
Resolution as of the date first written above.

_______________________
[Director Name]
Director

_______________________
[Director Name]
Director
```

### Form 2 — Minutes of a board meeting
Used when:
- A formal meeting was held.
- Not all directors agree (record dissent).
- The jurisdiction requires physical board meetings for certain resolutions.
- A voting record is needed.

**Structure**:
```
MINUTES OF A MEETING OF THE BOARD OF DIRECTORS
OF [COMPANY NAME]

Held on [DATE] at [TIME] at [LOCATION / video conference platform]

DIRECTORS PRESENT:
  [Name 1] — [Title]
  [Name 2] — [Title]

DIRECTORS ABSENT (with/without apology):
  [Name 3]

ALSO IN ATTENDANCE:
  [Secretary] — Secretary of the meeting
  [Counsel name] — Legal counsel (if applicable)

CHAIRPERSON: [Name]

1. OPENING AND QUORUM
   The Chairperson confirmed that a quorum was present 
   in accordance with [Article X of the Company's Articles / 
   Section X of the Companies Law / the Bye-Laws].

2. NOTICE
   It was noted that due notice of the meeting had been given 
   to all directors in accordance with [Articles/Bye-Laws].

3. [AGENDA ITEM — SPECIFIC RESOLUTION]
   The Chairperson presented [a brief description of the matter].
   After due discussion, it was unanimously / by a majority of 
   [X] votes to [Y] RESOLVED THAT: [resolution text]

4. FURTHER BUSINESS
   There being no further business, the Chairperson declared 
   the meeting closed at [TIME].

CERTIFIED AS A TRUE AND ACCURATE RECORD:

_______________________
Chairperson / Secretary
Date: ___________
```

## Common resolutions — standard language

### Share issuance
```
RESOLVED THAT the Company issue [number] [class] shares of 
[par value / no par value] each at a subscription price of 
[CURRENCY AMOUNT] per share to [subscriber name] on the terms 
of the Subscription Agreement dated [DATE], and that the 
Company's share register be updated accordingly.

RESOLVED FURTHER THAT the Directors are authorized to execute 
all documents and take all steps necessary to effect the 
issuance and registration of the said shares.
```

### Director appointment
```
RESOLVED THAT [Full Name], of [address / nationality], be and 
is hereby appointed as [Executive / Non-Executive] Director of 
the Company with effect from [DATE], to serve in accordance 
with the Company's [Articles of Association / Bye-Laws].
```

### Director removal / resignation
```
RESOLVED THAT the resignation of [Name] as a Director of the 
Company with effect from [DATE] be and is hereby accepted, 
and the Company records be updated accordingly.
```

### Bank account and signatories
```
RESOLVED THAT the Company open a [current / savings / foreign 
currency] account with [Bank Name], [Branch], in the name of 
the Company.

RESOLVED FURTHER THAT the following individuals are authorized 
to operate the said account as signatories on behalf of the 
Company:
  [Name 1] — [Title] — [signing authority: sole / joint with any one / joint with Name 2]
  [Name 2] — [Title] — [signing authority]

RESOLVED FURTHER THAT [Name] is authorized to sign the bank's 
account mandate and related documentation on behalf of the Company.
```

### Approval of material contract
```
RESOLVED THAT the Company enter into the [Agreement Name] dated 
approximately [DATE] with [Counterparty] substantially on the 
terms discussed by the Board, and that [Name / Title] be and 
is hereby authorized to negotiate the final terms and execute 
the Agreement on behalf of the Company.
```

### Dividend declaration
```
RESOLVED THAT a [interim / final] dividend of [CURRENCY AMOUNT] 
per [class] share be and is hereby declared for the financial 
year ended [DATE], payable on [PAYMENT DATE] to shareholders 
of record as at [RECORD DATE].
```

### M&A transaction approval
```
RESOLVED THAT the Board approves the [acquisition of / sale of] 
[target / assets / business] on the terms set out in the 
[Term Sheet / SPA / APA] presented to the Board, and that [Name] 
be authorized to negotiate and execute the final transaction 
documents on behalf of the Company, subject to the final 
transaction documents being substantially consistent with the 
terms presented.
```

### Granting of power of attorney
```
RESOLVED THAT a Power of Attorney be granted to [Name], 
[nationality], bearing [ID / passport number], to [specific 
authority — list precisely] on behalf of the Company, and that 
the [Chairman / Director] is authorized to execute such Power 
of Attorney under the Company's seal / signature.
```

## Jurisdictional notes

### DIFC / ADGM
- Written resolutions valid if signed by all directors (or the majority required by articles); no meeting required.
- Companies must maintain a minute book with copies of all board resolutions.
- Circular resolutions (passed by email/circulation) expressly permitted.
- Minutes to be signed by the Chair and retained for at least 7 years.

### UAE onshore (Federal Decree-Law 32/2021)
- Physical board meetings preferred; some companies require physical meetings per their articles.
- Virtual meetings: permitted post-UAE Company Law amendment; must be provided for in articles or by resolution.
- Minutes must be signed by all attending directors and the company secretary/manager.
- For LLCs: decisions may sometimes be made by the General Manager (Mudir) without board meeting if that authority is granted in the AoA.

### KSA (Companies Law — Royal Decree M/132 2022)
- Board decisions recorded in minutes and authenticated (Mawthq notarization platform strongly recommended for filings with MOC).
- Quorum: generally more than half of total directors unless AoA states otherwise.
- Written resolutions: permitted if signed by all directors.
- Arabic language required for official documents filed with government authorities.

### Lebanon (SAL / SARL under Commercial Code)
- Board minutes (PV de séance du Conseil d'Administration): signed by attending directors.
- Quorum per company statuts; typically majority of directors.
- Filed copies of certain resolutions (e.g., director changes, capital changes) must be notarized and registered with the Commercial Register.
- Written resolutions: not expressly provided for in the Commercial Code; physical meetings safer for significant decisions.

## Audit trail requirements

- Maintain a resolution register / minute book.
- Number resolutions sequentially within each year (e.g., BR-2025-001).
- Keep supporting materials (term sheets, valuations, board papers) alongside each resolution.
- Many jurisdictions require retention for at least 5–7 years; some require keeping for the life of the company.
- Bank-certified copies and notarized copies are often required by banks and registrars; plan for this in the signing process.

## Common mistakes

- **Vague resolution language**: "the Board approves entering into negotiations" is not sufficient authority to sign a contract; authorization must be specific.
- **Wrong signing authority**: resolution must authorize a named individual or office (not just "a director"); counterparties and banks will verify the authorizing name matches the signatory.
- **Quorum not met**: if the quorum requirement is not met, the resolution is void; always confirm quorum before passing resolutions.
- **Conflict of interest not handled**: an interested director should be recorded as declaring the interest and abstaining from the vote; failure to do so can void the resolution.
- **Missing corporate seal reference** (for jurisdictions requiring a seal): UAE and KSA companies may need to apply the company seal or stamp to certified copies.

## Related skills

- [[draft-agm-minutes]]
- [[draft-articles-of-association]]
- [[draft-cap-table-resolution]]
- [[draft-bylaws]]
