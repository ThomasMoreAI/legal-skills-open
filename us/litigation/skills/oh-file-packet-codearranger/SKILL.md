---
name: oh-file-packet-codearranger
title: Assemble an Ohio Court Filing Packet
description: Use to assemble an Ohio court filing packet. Triggers include 'assemble Ohio filing packet', 'Ohio filing checklist', 'Ohio Common Pleas eFiling', 'Ohio Municipal Court eFiling', 'Ohio certificate of service', 'Ohio working copy'. Covers e-filing (most Common Pleas courts use county-specific systems), pre-flight checks, exhibit organization, and per-court working-copy conventions.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble an Ohio Court Filing Packet

> **NOT LEGAL ADVICE.** Filing protocols vary by Common
> Pleas court. Verify per-court Loc. R. before filing.

## E-filing landscape in Ohio

Most Ohio Common Pleas courts use **county-specific**
e-filing systems rather than a statewide platform:

- **Cuyahoga County** — eFiling portal at
  `cpdocket.cp.cuyahogacounty.us`
- **Franklin County** — `efile.fccourts.org`
- **Hamilton County** — Court Connect at
  `courtclerk.org`
- **Summit County** — eFiling via Tyler Technologies
- **Montgomery County** — eFiling portal
- **Most other Common Pleas courts** — Tyler Tech / Odyssey
  variants

Each portal requires registration. Pro-se filers can
register without an attorney bar number.

## Municipal Court e-filing

Ohio Municipal Courts run their own e-filing systems
(R.C. Chapter 1901 leaves the choice to each court). Some
larger Municipal Courts (Cleveland, Columbus) have
e-filing; smaller Municipal Courts may still require paper.

## Pre-flight checklist

Before submitting:

- [ ] Caption matches case-management order (court, case
      number, parties)
- [ ] Document title in ALL CAPS in the caption
- [ ] Filer's signature with Atty. Reg. # (or "Pro Se")
- [ ] Certificate of Service signed + dated
- [ ] All exhibits attached + labeled (Exhibit A, B, ...)
- [ ] Page limits per Loc. R. (verify)
- [ ] Proposed order tendered if motion (Civ. R. 12(A);
      most Loc. R. expect this)
- [ ] Format-check.py passes
- [ ] Quality-check passes (oh-quality-check)

## Per-court working copies

Some Common Pleas courts require courtesy paper copies for
the assigned judge:

- **Cuyahoga Civil Division** — some chambers require a
  bench copy for briefs over 15 pages
- **Franklin Civil Division** — varies by judge
- **Smaller Common Pleas courts** — typically no working
  copy required; e-file is sufficient

When working copies are required:

- Print double-sided unless court specifies single-sided
- Hole-punch (3-hole) for chambers binder if requested
- Deliver to bailiff or chambers within 1 business day of
  e-filing

## Certificate of Service (Civ. R. 5)

Required format:

```
                CERTIFICATE OF SERVICE

I certify that on [Date], a copy of the foregoing was
served upon all counsel of record / parties via [eFiling
system / U.S. mail / hand delivery / email] at their
addresses of record.

                            __________________________
                            [Filer's name]
```

## Composition with other oh- skills

- `oh-quality-check` — pre-filing format + content QC
- `oh-statewide-format` — caption + signature block
- `oh-cuya` / `oh-frank` / etc. — per-court e-filing
  portal specifics
- `oh-municipal-courts` — Municipal Court e-filing
