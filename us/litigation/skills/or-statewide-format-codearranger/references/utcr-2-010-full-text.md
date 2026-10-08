# UTCR 2.010 — Form of Documents (Oregon Uniform Trial Court Rules)

Authoritative source for current text:
https://www.courts.oregon.gov/rules/UTCR/Pages/default.aspx

The OJD publishes a consolidated UTCR PDF annually (effective
August 1). The latest version supersedes all earlier text — pull
the current PDF before citing in a brief.

## UTCR 2.010 — Form of Documents

> *Summary, not verbatim. The verbatim text lives in the
> court-rules corpus at
> `or-law-references/references/court-rules/UTCR.md` once pulled
> from courts.oregon.gov.*

### (1) Paper

- Documents must be on 8½ × 11 inch white paper
- Black or blue-black ink only
- Single-sided printing
- The paper must be of good quality and durability

### (2) Margins

- Top margin on page 1: at least 3 inches (leaves room for the
  clerk's filing stamp and the court's eFile header)
- Top margin on subsequent pages: at least 1 inch
- Left, right, bottom margins: at least 1 inch on every page

### (3) Type

- Documents must be typed or printed
- Minimum font size: 12 point (10 point acceptable for footnotes
  and tables)
- Line spacing: at least 1½-spaced for body text (single-spacing
  allowed for footnotes, block quotations, signature blocks,
  certificates of service)

### (4) Headers and footers

- Each page after page 1 must display the case caption short form
  in a header OR the case number in a footer
- Page numbers must appear on every page after page 1
- The OJD recommended convention is "Document Title — Case No.
  [number]" on the left of the footer and "Page X of Y" on the
  right

### (5) Captions and titles

- See UTCR 2.100 (caption format) and UTCR 2.110 (title
  requirements)

### (6) Signature

- Every document must be signed by the party or the party's
  attorney
- Electronic signatures using the `/s/ [Name]` convention are
  accepted in eFiled documents (UTCR 21.090)

### (7) Confidential information

- See UTCR 2.120 (redaction) and UTCR 2.130 (Confidential
  Information Form)

## UTCR 2.100 — Caption format

The caption must include:

- Court name: "IN THE CIRCUIT COURT OF THE STATE OF OREGON"
- County: "FOR THE COUNTY OF [NAME]"
- Names of all parties on the first paper filed; subsequent papers
  may use the short form ("[Lead Plaintiff] et al., Plaintiffs, v.
  [Lead Defendant] et al., Defendants")
- Case number on the right
- Document title on the right, in all caps, bold

## UTCR 2.110 — Title of document

- The title must describe the document with enough specificity for
  indexing
- The title must identify the party submitting it
- If the matter is on mandatory arbitration or small claims, the
  title must so indicate

## UTCR 2.120 — Personal information

Documents filed with the court must omit or redact:

- Social Security numbers (only the last four digits may appear)
- Account numbers (last four only)
- Dates of birth (year only for adults; full date allowed for
  minor parties in domestic relations cases)
- Names of minor children (use initials, e.g., "J.D.")

## UTCR 2.130 — Confidential Information Form

Personal information that must be in the record (because it is an
element of the claim) but cannot be in the publicly viewable
document is filed on a **Confidential Information Form** (Form
2.130). The CIF is sealed by the clerk and accessible only to the
parties and the court.

## UTCR 1.090 — Certificate of Service

Every filing served on another party must be accompanied by a
**Certificate of Service** stating:

- Date of service
- Method of service (mail, hand delivery, eService, fax, email)
- Name and address of each party served
- Signature of the server

UTCR 1.090 form:

```
                  CERTIFICATE OF SERVICE

I hereby certify that on the ____ day of __________, 20__, I
served a true and correct copy of the foregoing [document title]
on the following parties in the manner indicated:

[Name]              [Method]            [Address/Email]
[Name]              [Method]            [Address/Email]

                            _______________________________
                            [Filer Name]
                            [Role]
                            [Address]
                            [Phone]
                            [Email]
```

## How to re-pull

When the OJD publishes a new UTCR effective August 1, re-pull with:

```bash
python3 scripts/pull_oregon_rules.py --target utcr
```

The script writes verbatim text under
`or-law-references/references/court-rules/UTCR.md`.

## Cross-references

- ORCP 1 E — declaration in lieu of affidavit
- ORCP 9 — service of papers and pleadings
- ORCP 17 — signing of pleadings and motions
- ORCP 9 G — Certificate of Service
- UTCR 21 — eFiling specific rules
