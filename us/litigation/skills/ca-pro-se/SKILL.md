---
name: ca-pro-se
title: Pro Se Drafting for California Courts
description: Use when drafting California court documents for a self-represented (pro se / "In Pro Per") litigant. Triggers include "pro se", "in pro per", "self-represented", "representing myself", "pro-se drafting framework", "draft without an attorney", "pro se California", "Judicial Council forms", "fee waiver", "FW-001", "how do I serve", "CCP 415", "CCP 1013", "Self-Help Center", "In Pro Per", or when the user describes themselves as the plaintiff or defendant directly. Covers the Parker drafting framework adapted for California, "In Pro Per" vs. "self-represented litigant" terminology, service protocols under CCP §§ 412.10-417.40 and 1010-1020, Judicial Council form use, In Forma Pauperis fee waivers (FW-001 / FW-003), and California- specific pro se resources. Layer on top of ca-statewide-format and the applicable county skill (ca-lasc, ca-sfsc, or ca-county-courts).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for California Courts

Use this skill when drafting court documents for a self-represented
litigant in a California Superior Court. It encodes the Parker
drafting framework adapted to California procedural conventions and
the practical service and filing protocols pro se filers need.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
> against current rules and case law before filing. For complex
> matters, or matters with substantial sums at stake, consider
> consulting a licensed California attorney.

## "In Pro Per" vs. "Self-Represented Litigant"

California uses both terms, but each has a distinct context:

- **"In Pro Per"** (Latin: *in propria persona*) is the traditional
  California legal term. Use it on signature blocks, caption lines,
  and in court filings. California courts universally accept it and
  judicial officers recognize it immediately.
- **"Self-Represented Litigant" (SRL)** is the preferred term in
  court staff communications, Self-Help Centers, and California Rules
  of Court (CRC 10.960). Judicial Council materials, courthouse
  signage, and the courts.ca.gov website use SRL.

**Rule of thumb:**
- On documents you file: use **"In Pro Per"**
- When talking to court staff or reading courthouse resources: use
  **"self-represented litigant"**

Both terms mean the same thing; neither is wrong in either context.

## The Pro-Se Drafting Framework — adapted for California

Every motion and declaration follows four principles:

1. **Front-load the strongest facts.** The judge should know the
   best fact in the case within the first paragraph. Do not bury
   it under procedural history.
2. **Keep motions concise.** Target 4–6 pages for a motion plus
   memorandum. Use bold lead-ins to let the judge skim. Every
   sentence earns its place.
3. **Write to the judge, not to opposing counsel.** Avoid ad
   hominem. Let the record speak. State facts; let the judge draw
   the characterizations.
4. **Let the record speak.** Attach the documents that prove the
   point. Cite them by exhibit number and page. A well-indexed
   record is worth more than rhetoric.

### California-specific Parker adaptations

**Cite the CCP section on the first line.** California judges
expect the procedural authority up front. "Pursuant to Code of
Civil Procedure section 2031.310, Defendant moves..." not "This
Court has inherent power to compel..."

**California Style Manual citation format.** Use "Code Civ. Proc.,
§ 2030.300" (abbreviated code name, section symbol, section
number) — not "CCP 2030.300" or "§ 2030.300(b)(1)" without the
code prefix. Full citations in argument sections; abbreviated in
parenthetical references.

**Exhibits are lettered in California.** Unlike Oregon (which uses
numbered exhibits), California practice typically uses alphabetical
exhibit labels (Exhibit A, Exhibit B). Follow the convention of
the court and local rules — LASC does not mandate a particular
convention, but lettered exhibits are the dominant practice.

**Verified complaints and declarations.** California Code of Civil
Procedure section 2015.5 governs unsworn declarations. Use the
statutory form: "I declare under penalty of perjury under the laws
of the State of California that the foregoing is true and correct."
Add date and place of execution.

**Tentative-ruling awareness.** California's tentative-ruling
system (CRC 3.1308) means the judge posts a preliminary ruling the
day before the hearing. Read it. If the tentative is adverse,
request oral argument by 4:30 p.m. the day before — silence means
the tentative becomes the order. (See ca-hearings for full detail.)

**CCP 437c summary judgment timing.** California's SJ deadline
differs from FRCP Rule 56: notice must be given 75 days before the
hearing date (Code Civ. Proc., § 437c(a)(2)). Add an additional
5 days if served by mail or 2 days if served by overnight delivery
(Code Civ. Proc., § 1005(b)). **This is longer than federal — do
not port FRCP timelines.**

## Signature block for pro se (California)

```
____________________________________
[Full Name]
In Pro Per
[Street Address]
[City, CA ZIP]
Telephone: [Phone]
Email: [Email]
```

- Use **"In Pro Per"** on all filings
- **Omit California State Bar number** — that is for licensed
  California attorneys. Including a fake bar number could constitute
  unauthorized practice of law under Business and Professions Code
  section 6125 and exposes you to contempt sanctions.
- Include phone number (required for court correspondence)
- Include email (for electronic service under Code Civ. Proc., § 1010.6)
- For declarations, add the Code of Civil Procedure section 2015.5
  perjury clause above the signature

## Common pro se pitfalls — California-specific

| Pitfall | Fix |
|---------|-----|
| Missing tentative ruling deadline | Check the court's website by 5:00 p.m. the day before; if adverse, contest by 4:30 p.m. |
| Missing points-and-authorities | Most California motions require a memorandum of points and authorities (CRC 3.1113(a)); no P&A may mean denial |
| Page limits exceeded | CRC 3.1113(d): 15 pages for most motions; 20 for SJ; get leave for more |
| Separate statement omitted | Summary judgment and motions to compel further discovery responses require a separate statement (CRC 3.1350, 3.1345) |
| Citing "FRCP 12(b)(6)" | California analog is **Code Civ. Proc., § 430.10(e)** — demurrer for failure to state a claim |
| Citing "Fed. R. Civ. P. 56" | California SJ is **Code Civ. Proc., § 437c** with different timing |
| Citing "interrogatory limit 25" | California allows **35** specially prepared interrogatories without a declaration (Code Civ. Proc., § 2030.030) |
| Lettering exhibits "1, 2, 3" | Use letters (A, B, C) or follow the convention used in your court |
| No proof of service | Every filing requires a Proof of Service (POS-030 or POS-040); clerk may reject without it |
| Missing caption format | California captions include case number, assigned department, and hearing date/time if applicable |
| Emotional tone | Rewrite as neutral fact statements with record citations |
| Missing relief clause | Every motion ends with a clear statement of what order is requested |

## Judicial Council forms

California Superior Courts use **Judicial Council of California**
standardized forms. Many filings must use or may use these forms.

Key form prefixes:
- **MC-** (Miscellaneous Civil): general civil motions (MC-025
  Attachment, MC-031 Declaration)
- **CIV-** (Civil): civil case-specific forms (CIV-110 Request for
  Dismissal; CIV-050 Substitution of Attorney)
- **POS-** (Proof of Service): POS-030 (proof of service by mail);
  POS-040 (proof of personal service)
- **SC-** (Small Claims)
- **UD-** (Unlawful Detainer / eviction)
- **FL-** (Family Law)
- **JV-** (Juvenile)

All current forms available at: https://www.courts.ca.gov/forms.htm

**When must you use a Judicial Council form?** CRC 1.35 requires
use of mandatory Judicial Council forms where they exist. If the
form is marked "Mandatory", use it exactly as formatted — do not
reformulate in your own template. If marked "Optional", you may
substitute a pleading in your own format as long as it contains
all required information.

See `references/pro-se-toolkit.md` for detail on form use,
including fee waiver forms.

## Drafting checklist (run before filing)

- [ ] Caption is complete and matches the case number, court, and
      department exactly
- [ ] Court header: "SUPERIOR COURT OF THE STATE OF CALIFORNIA" +
      "COUNTY OF [COUNTY]"
- [ ] Party separator is "vs." (California Superior Court style —
      note: California civil captions traditionally use "vs." not
      "v."; check local rules; LASC uses "vs.")
- [ ] First paragraph states the single most important fact or
      legal point
- [ ] Every factual assertion is supported by an exhibit or sworn
      declaration
- [ ] Memorandum of points and authorities is attached (CRC 3.1113)
- [ ] Page limits checked (15 pages / 20 for SJ — CRC 3.1113(d))
- [ ] Separate statement filed if required (SJ, discovery motions)
- [ ] Proof of service attached (POS-030 or POS-040)
- [ ] Code Civ. Proc., § 2015.5 declaration clause on all
      declarations
- [ ] Signature block: full name, "In Pro Per", address, phone,
      email; NO State Bar number
- [ ] Tentative-ruling checked (if hearing date is tomorrow)
- [ ] Confidential information redacted per CRC 1.20 (SSN last 4
      only; financial account numbers partially masked)

## California-specific pro se resources

### Statewide

- **California Courts Self-Help Guide**:
  https://www.courts.ca.gov/selfhelp.htm
- **Judicial Council forms** (all forms, searchable):
  https://www.courts.ca.gov/forms.htm
- **LawHelpCA.org** (income-qualified legal help):
  https://www.lawhelpca.org/
- **California Courts Self-Help Centers**: every Superior Court
  in California is required to operate a Self-Help Center under
  Government Code section 68651. These provide assistance with
  forms and procedures (not legal advice).

### Legal aid and reduced-fee resources

- **Legal Aid Foundation of Los Angeles (LAFLA)**:
  https://lafla.org/ | (800) 399-4529
- **Bay Area Legal Aid**:
  https://baylegal.org/
- **Bet Tzedek Legal Services** (Los Angeles):
  https://www.bettzedek.org/
- **California State Bar Lawyer Referral Services**: certified
  lawyer referral services by county:
  https://www.calbar.ca.gov/Public/Need-Legal-Help/Lawyer-Referral-Service
- **California Lawyers Association Pro Bono Project**:
  https://calawyers.org/probonosection/

### County-specific self-help

- **LASC Self-Help Center**: Stanley Mosk Courthouse, 111 N. Hill
  St., Los Angeles; also Chatsworth, Inglewood, Compton, Pomona,
  Van Nuys — see courts.ca.gov/selfhelp for all locations
- **SFSC Self-Help Center**: Civic Center Courthouse, 400 McAllister
  St., San Francisco, Rm. 101
- **San Diego**: Hall of Justice, 330 W. Broadway, Rm. 225
- **Sacramento**: Gordon D. Schaber Courthouse, 720 9th St., Rm. 102

## Companion skills

- Use `ca-statewide-format` for document templates, caption
  structure, and CRC formatting requirements
- If the case is in Los Angeles Superior Court, use `ca-lasc` for
  LACourtConnect, department assignments, and LASC-specific rules
- If the case is in San Francisco Superior Court, use `ca-sfsc` for
  CRS reservations and department-specific practice
- For any other California county, use `ca-county-courts`
- For discovery disputes, use `ca-discovery`
- For hearing preparation, use `ca-hearings`

## References

- `references/pro-se-drafting-framework.md` — full drafting guide with
  California-flavored examples and style citations
- `references/service-protocol.md` — CCP §§ 412.10-417.40 service
  of summons; CCP §§ 1010-1020 service of motions; POS-030/POS-040
  templates; the 5-day mail extension under CCP § 1013
- `references/pro-se-toolkit.md` — Judicial Council form use guide;
  fee waivers (FW-001 / FW-003); Self-Help Center resources;
  In Forma Pauperis under Govt. Code §§ 68630-68641

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
