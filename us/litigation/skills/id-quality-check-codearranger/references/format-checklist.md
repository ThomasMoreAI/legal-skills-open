# I.R.C.P. 2 Format Checklist

> **NOT LEGAL ADVICE.** A format-compliance checklist mirroring
> `scripts/format-check.py`. WARN items are local-rule matters — confirm
> them against the venue's local rules. Resolve every FAIL before
> filing.

I.R.C.P. 2 (not Rule 10) carries Idaho's statewide form-of-documents
spec; Rule 10 cross-references Rule 2 and adds the numbered-paragraph
requirement. Pull the controlling text from
`../../id-law-references/references/court-rules/IRCP-civil-procedure.md`.

## Run the script first (for .docx)

```
python3 plugins/id-court-docs/scripts/format-check.py path/to/filing.docx
```

The script checks the following — this checklist mirrors it item for
item:

| # | Check | Script rule | Pass / Fail |
|---|-------|-------------|-------------|
| 1 | **Letter paper** — 8½" × 11" (12240 × 15840 DXA) | exact match required | FAIL if not Letter (WARN if landscape) |
| 2 | **Margins** — top & sides **≥ 1.2"** (1728 DXA); bottom **≥ 1"** (1440 DXA) | floor per side | WARN if below (permitted only to fit one page) |
| 3 | **Line spacing** — **double or 1½** (body mode ≥ 1.5×; 360/480 in 240ths) | body-mode spacing | FAIL if body mode < 1.5× |
| 4 | **Font size** — **≥ 11 pt** (22 half-points) | body mode ≥ 11pt | FAIL if body mode < 11pt; WARN if only some runs small |
| 5 | **Font family** — a legible serif (Times New Roman customary) | not mandated by Rule 2 | WARN only; Rule 2 names no font |
| 6 | **Black ink only** — no color text / highlight / shading | black-ink requirement | WARN/FAIL on color markings (reserve color for exhibits that require it) |
| 7 | **Footer pagination** — footer carries the **document title + "Page X of Y"** (PAGE and NUMPAGES fields) | both fields + title literal | FAIL if PAGE, NUMPAGES, or the title literal is missing |

## Checks the script cannot make (verify manually)

The script validates paper, margins, spacing, font, ink, and the footer.
These I.R.C.P. 2 / 10 form requirements need a human eye:

- **Title of the court ≥ 3" from the top** of page 1.
- **Document title at the bottom of each page** (the footer literal that
  the script confirms is present is this title).
- **Caption (I.R.C.P. 2 / 10(a))** — names of the parties, title of the
  court (e.g., "IN THE DISTRICT COURT OF THE [Nth] JUDICIAL DISTRICT OF
  THE STATE OF IDAHO, IN AND FOR THE COUNTY OF ___"), party designations
  (Plaintiff/Defendant; Petitioner/Respondent in family/special
  matters), the **case number**, and the document title.
- **Line-numbered pleading paper** down the left margin (marketplace
  common-practice default).
- **Numbered paragraphs (I.R.C.P. 10(b))** — sequential, each averment a
  single set of circumstances.
- **Signature block (I.R.C.P. 11)** — name, address, telephone, email,
  and the **Idaho State Bar number** (attorney) or the **self-represented**
  designation; the Rule 11 signature certifies the filing.
- **Certificate of Service (I.R.C.P. 5)** — date, manner, recipients
  (plus the I.R.E.F.S. e-service confirmation where e-filed).

## Markdown / text drafts (non-.docx)

The script only reads `.docx`. For a markdown or plain-text draft, verify
the caption, the ≥ 3" court-title drop, the document title at the foot of
each page, numbered paragraphs, the signature block, and the certificate
of service by hand against the list above.

## Composition

- Content / cross-document pass: `references/content-checklist.md`
- Deep evidentiary citation pass: `id-fact-check`
- Canonical rule text: `id-law-references`
