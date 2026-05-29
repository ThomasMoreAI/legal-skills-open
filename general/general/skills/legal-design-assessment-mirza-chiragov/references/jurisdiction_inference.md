# Jurisdiction Inference — Reference

Loaded when the audit reaches Step 2 of the SKILL.md workflow.

## Why this matters

The statutory-duplication pillar (Step 7) requires knowing which statute could be duplicated. Other pillars are jurisdiction-light. Treat jurisdiction inference as **probabilistic**, not deterministic — give an explicit confidence level and flag findings accordingly.

## Signals to use, in roughly descending weight

### 1. Governing law clause

The strongest single signal. Look for, in the relevant language:

- **English.** "This Agreement is governed by the laws of [X]"; "shall be construed in accordance with the laws of [X]"; "the laws of England and Wales"; "the laws of the State of New York"; "the laws of the Commonwealth of Australia"; "the federal laws of Canada".
- **French.** "Le présent contrat est régi par le droit français"; "soumis au droit belge"; "régi par le droit suisse"; "régi par les lois du Grand-Duché de Luxembourg"; "régi par le droit du Québec".
- **German.** "Dieser Vertrag unterliegt dem Recht der Bundesrepublik Deutschland"; "unterliegt österreichischem Recht"; "unterliegt schweizerischem Recht unter Ausschluss des UN-Kaufrechts"; "es gilt liechtensteinisches Recht".

If a governing-law clause is present and unambiguous, jurisdiction confidence is **High**.

### 2. Forum / jurisdiction clause

Where the governing law is silent or ambiguous, an exclusive-forum clause is the next strongest signal: "the courts of [X]", "les tribunaux de [X]", "ausschließlicher Gerichtsstand ist [X]". Note that forum and governing law can diverge; if they do, jurisdiction is set by the governing-law clause for substantive law and the forum clause for procedure. Statutory-duplication review keys off the substantive law.

### 3. Statute citations in the body

Concrete references to a named statute or code anchor the jurisdiction even without a governing-law clause. Inventory:

- **France / Belgium / Switzerland (Romandie) / Luxembourg / Québec.** "Code civil" (FR, BE, LU, QC use distinct Codes civils), "Code de la consommation" (FR, BE, LU), "Code du travail", "Code monétaire et financier", "Code de commerce", "LCD" (Loi fédérale contre la concurrence déloyale, CH), "Code des obligations" or "CO" (CH), "Loi du 8 décembre 1992" (BE, data protection precursor).
- **Germany / Austria / Switzerland (Deutschschweiz) / Liechtenstein.** BGB (DE), HGB (DE), AGG (DE), UWG (DE/AT), AGBG (AT), KSchG (AT), OR (CH, Obligationenrecht, parallel French CO), DSG (CH, Datenschutzgesetz), ABGB (AT, Allgemeines bürgerliches Gesetzbuch), PGR (LI, Personen- und Gesellschaftsrecht).
- **England & Wales / Scotland / Northern Ireland.** Consumer Rights Act 2015, Sale of Goods Act 1979, Unfair Contract Terms Act 1977, Companies Act 2006, Data Protection Act 2018, Equality Act 2010.
- **United States (federal and state).** UCC (state, varies), Sherman Act, FTC Act, CCPA / CPRA (California), state consumer-protection statutes. "U.S.C." citations are federal.
- **Canada.** Civil Code of Québec (CCQ) → Québec; Sale of Goods Act → common-law province; PIPEDA → federal.
- **Australia / New Zealand.** Australian Consumer Law, Competition and Consumer Act 2010 (Cth); Consumer Guarantees Act 1993 (NZ).
- **Ireland.** Consumer Rights Act 2022.

Statute citations resolve to a jurisdiction with **High** confidence if at least two distinct citations point to the same jurisdiction and there are no contradicting signals.

### 4. Currency, addresses, and registration identifiers

Weaker signals, useful when combined:

- **Currency.** GBP → UK; CHF → Switzerland / Liechtenstein; USD → US (state still to be determined); CAD → Canada; AUD → Australia; NZD → New Zealand. EUR is multi-jurisdictional — never decisive alone.
- **Postal address formats.** German postal codes are 5 digits; French 5 digits with regional prefix; Belgian 4 digits; Swiss 4 digits; UK alphanumeric (e.g., SW1A 1AA); US 5- or 9-digit ZIP; Canadian alphanumeric (e.g., K1A 0B1).
- **Registration identifiers.** SIREN/SIRET (FR); BCE / KBO (BE); IDE / UID (CH); HRB / HRA / Amtsgericht reference (DE); FN (AT); Companies House number (UK); EIN (US); ABN (AU); NZBN (NZ).
- **Telephone country codes.** +33 FR; +32 BE; +41 CH; +49 DE; +43 AT; +423 LI; +352 LU; +44 UK; +1 US/CA.

Combine multiple weak signals before promoting confidence. Two addresses in Germany + EUR + an HRB number is **High** confidence Germany even without a governing-law clause.

### 5. Spelling conventions

Useful tiebreakers, never primary:

- **English.** -ize / -ization → US bias; -ise / -isation → UK / Commonwealth. "Color" / "colour"; "judgment" (US, UK legal) / "judgement" (UK general). Note that UK legal drafting often uses "judgment" without the e even in non-legal contexts — do not over-read.
- **French.** Belgian French uses "septante" / "nonante" (where French France uses "soixante-dix" / "quatre-vingt-dix") — rare but decisive. Swiss French likewise. Québécois French uses anglicisms more freely.
- **German.** Austrian German has its own legal vocabulary ("Erkenntnis" instead of "Urteil" in administrative law contexts; "Pönale" instead of "Vertragsstrafe"). Swiss German legal drafting in standard German is usually otherwise indistinguishable, but watch for "ß" → "ss" everywhere (Swiss convention).

### 6. Document-type metadata

A document titled "CGU" (Conditions Générales d'Utilisation) is more likely French-French; "CGV" likewise. "AGB" → Germany / Austria / Switzerland. "T&Cs" / "Terms of Use" → UK or US. "EULA" → typically US. These are weak signals at best.

## Confidence levels — when to assign which

- **High.** Governing-law clause present and unambiguous, **or** two or more independent strong signals (statute citation + address + registration ID) all aligned with no contradicting signals.
- **Medium.** One strong signal aligned with weak signals, **or** multiple weak signals aligned. Most cross-border B2B contracts without an explicit governing-law clause sit here.
- **Low.** Conflicting signals (e.g., German party + French statute citations), **or** only weak signals available, **or** the document is plausibly drafted under several jurisdictions and ambiguous.
- **Unknown.** No usable signals.

## What to do with each confidence level in the report

- **High** → Statutory duplication pillar at full weight; pillar findings cite the relevant statute confidently.
- **Medium** → Statutory duplication pillar at full weight but findings are phrased as "Likely restating [jurisdiction] [statute] — verify".
- **Low** → Halve the statutory-duplication weight; redistribute 5 percentage points pro rata across other pillars. Phrase findings as `Unverified — jurisdiction-dependent`.
- **Unknown** → Skip the statutory-duplication pillar entirely; redistribute its 10 points pro rata. Note the skip in Section 11 of the report.

## Multi-jurisdiction documents

Some documents apply different jurisdictions to different parts (e.g., a master agreement under New York law with EU-specific addenda under each member state's local consumer law). In that case:

1. Identify the segments and their respective jurisdictions.
2. Run the statutory-duplication pillar **per segment** under its own jurisdiction.
3. Report a single composite linguistic / readability / structure / hidden-conditions / visual score (these are not jurisdiction-dependent) and a per-segment statutory-duplication score.
4. Confidence level for the composite is set by the weakest segment.

## What you do not do here

- Do not advise on conflict-of-laws choice — that is a substantive legal question outside this skill.
- Do not assert that a governing-law clause is enforceable — only note its existence as a signal.
- Do not infer jurisdiction from the language alone if textual signals conflict. The language sets the default jurisdictional pool (EN → English-speaking jurisdictions; FR → francophone jurisdictions; DE → germanophone jurisdictions), not the answer.
