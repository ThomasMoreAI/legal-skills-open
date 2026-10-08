# AGLC4 Citation — Formatting, Short Forms, Table of Authorities

Hand-formatting rules for the **Australian Guide to Legal Citation (4th ed)**, so the skill can
produce AGLC4-compliant citations, pinpoints, and a Table of Authorities **without** the jurisd
MCP (whose `format_citation` / `bibliography` tools are the Layer-0 equivalent — prefer them when
registered, per `references/retrieval-mechanics.md`). Read by the **case-law agent**, the
**validation gate**, and the **orchestrator** when writing memo authorities tables.

**Golden rule — cite only verified metadata.** Every element of a citation (parties, year, court,
number, report volume/page, judge names) comes from the **fetched judgment header or register
page**, never from memory. A citation whose elements cannot all be confirmed on the source is
marked `unverified` and never formatted as if final.

---

## 1. Cases

### Medium-neutral (unreported) citation
```
Case Name [Year] Court Number
```
> *Nobarani v Mariconte* [2018] HCA 36

- Case name in *italics*; parties as they appear on the judgment (first applicant/respondent only;
  omit second and subsequent parties; abbreviate to surname for individuals, drop "Pty Ltd" never).
- Court abbreviations are the medium-neutral codes (HCA, FCAFC, FCA, NSWCA, NSWSC, VSCA, QCA …).

### Reported citation
```
Case Name (Year) Volume Report Page
```
> *Mabo v Queensland [No 2]* (1992) 175 CLR 1

- **Prefer the authorised report where one exists** (CLR for HCA; FCR for Federal Court; NSWLR for
  NSW Supreme Court/CA). Order of preference: authorised → generalist unauthorised (ALR, ALJR) →
  subject-specific.
- Round brackets when the year identifies the volume by date; square brackets when the year *is*
  the volume identifier ([1975] AC 396).

### Combined (memo/ledger house style)
Give the medium-neutral citation first, then the authorised report, semicolon-separated:
> *Nobarani v Mariconte* [2018] HCA 36; (2018) 265 CLR 236

This is the form the agent report schemas already require (`<medium-neutral>; <authorised report>`).

### Pinpoints
- Paragraph: `[45]`; span: `[45]–[47]`; multiple: `[45], [52]`. Use paragraph numbers for any
  judgment that has them (all medium-neutral era judgments do).
- Page (older reports without paragraph numbers): `(1992) 175 CLR 1, 42`.
- Pinpoint follows the citation, comma-separated: *Nobarani v Mariconte* [2018] HCA 36, [47].
- Judge attribution in round brackets after the pinpoint: `[47] (Kiefel CJ, Gageler and Keane JJ)`.
  Use the judge names **as printed in the fetched judgment** — a wrong bench is a validation FAIL.

## 2. Legislation

```
Act Title Year (Jurisdiction) pinpoint
```
> *Evidence Act 1995* (NSW) s 59 · *Bankruptcy Act 1966* (Cth) ss 40–41 · *Civil Procedure Act 2005* (NSW) sch 2

- Title + year in *italics*; jurisdiction abbreviation in round brackets, not italicised:
  (Cth), (NSW), (Vic), (Qld), (SA), (WA), (Tas), (ACT), (NT), (Imp), (NZ).
- Pinpoint abbreviations: `s` / `ss` (section), `pt` (part), `div` (division), `sub-s`, `para`,
  `sch` (schedule), `cl` (clause), `reg` / `regs` (regulation), `r` / `rr` (rule), `o` (order).
- **Delegated legislation and court rules** take the same form:
  > *Uniform Civil Procedure Rules 2005* (NSW) r 14.28 · *Federal Court Rules 2011* (Cth) r 26.01
- Practice notes/directions: cite by identifier and issuing court, with version date from the
  court's site: `Supreme Court of NSW, Practice Note SC Eq 3 (10 December 2021)`.

## 3. Subsequent references (footnote-style short forms)

- **Short title.** After a first full citation, a case may be given a short form declared in
  brackets: *Mabo v Queensland [No 2]* (1992) 175 CLR 1 ('*Mabo*'); thereafter: *Mabo* (n 4) 42.
- **Ibid** — refers to the immediately preceding footnote/reference; add a pinpoint only if it
  differs: `Ibid 45 [47].`
- **(n N)** — repeated reference to an earlier footnote: `Nobarani (n 12) [38].`
- In **memo body text and tables** (not footnotes), use the combined citation on first mention and
  the short title afterwards; `Ibid`/`(n N)` forms only make sense in footnoted deliverables
  (e.g. a docx built from the memo).

## 4. Secondary sources (minimum forms)

- **Journal article:** Author, 'Title' (Year) Volume(Issue) *Journal* Page.
- **Book:** Author, *Title* (Publisher, edition, Year) pinpoint.
- **Report:** Body, *Title* (Report No, Date) pinpoint — e.g. Australian Law Reform Commission,
  *Uniform Evidence Law* (Report No 102, December 2005).
- **Web page:** Author, 'Title', *Site* (Web Page, Date) <URL>.

## 5. Table of Authorities / bibliography ordering

When a memo (or a docx deliverable) carries an AGLC4 Table of Authorities:

1. **Cases** — alphabetically by first party surname/name; each with its combined citation.
2. **Legislation** — grouped by jurisdiction (Cth first, then states/territories alphabetically);
   alphabetically by title within each group. Delegated legislation/rules listed with statutes.
3. **Secondary sources** (labelled "Other") — alphabetically by author surname.

Every entry in the table must correspond to a **validated** authority (verified — or suspect, in
which case it is listed with its flag, never silently cleaned). The ledger's authorities table is
the source of truth; the AGLC4 table is a formatting pass over it, not a fresh list.

## 6. Where this feeds the workflow

- **Case-law agent** — records the `AGLC4 citation` field per case (combined form + pinpoint),
  built from the verified header metadata it fetched.
- **Validation gate (existence check)** — confirms the citation's *elements* match the source; a
  formatting slip is corrected, an element mismatch (wrong year/court/number/report) is a FAIL.
- **Orchestrator memo** — the authorities/verification table carries an AGLC4 citation column, and
  the final-cycle memo may append a Table of Authorities per §5.
- **jurisd Layer 0** — `format_citation` (modes full/short/ibid/subsequent/pinpoint) and
  `bibliography` (`op=export` → `.bib`) do this natively; use them when registered and hand-format
  per this file when not. Output must be identical either way.
