# Authoritative ICC sources

Sources that may be cited, and how to access them. Read this whenever verifying a citation or deciding whether a source is authoritative.

## Tier 1 — primary, authoritative

For retrieval, start with the Legal Tools Database (`legal-tools.org`): the
Court's public decisions are comprehensively registered there, each under a
Persistent URL, and the Database answers automated retrieval reliably.
`icc-cpi.int` remains the Court's official website — authoritative for
everything it serves — but its 403s on direct fetch are structural.

### icc-cpi.int — the official Court website

Authoritative for everything the Court itself issues.

Entry points:
- Cases: `https://www.icc-cpi.int/cases`
- Situations: `https://www.icc-cpi.int/situations`
- Court records: `https://www.icc-cpi.int/court-record/icc-[situation]/[case]-[filing]`
- News and statements: `https://www.icc-cpi.int/news`
- OTP statements: filter the news page to OTP-issued items.

**Fetch reliability.** Direct `web_fetch` on icc-cpi.int returns 403 in a non-trivial fraction of requests. This is structural — not a one-off. When it happens, do *not* abandon the icc-cpi.int citation; the document still exists and is authoritative. Instead:

1. Search for the document number plus `icc-cpi.int`. The Court's own press release is usually the first hit and confirms document number, title, date, chamber, and holding-in-substance — that is, verification levels A and B (see `verification-workflow.md`).
2. If a paragraph-specific (level C) citation is needed, try Legal Tools (below) for the full text.
3. Search-result snippets from the `icc-cpi.int` domain are themselves Court content and can be cited at level A/B with the disclosure that the full PDF was not retrievable.

When the fetch *does* succeed, capture from the official page:
- Document number, exactly as printed, including suffix (`-Red`, `-Conf-Exp`, `-Anx1`, `-tENG`).
- Date in the form printed by the Court.
- Chamber.
- Title — verbatim.
- Paragraph(s) you plan to cite.

### legal-tools.org — ICC Legal Tools Database

The first retrieval stop. Comprehensive collection of ICC documents and related international criminal law materials — the Court's public decisions are systematically registered, each with a Persistent URL — and reliable to automated retrieval where icc-cpi.int blocks. Entry: `https://www.legal-tools.org/`; search: `https://www.legal-tools.org/search`.

Documents have unique LTD identifiers (e.g. `LTD-12345`). Prefer the ICC document number for citation; you may include the Legal Tools URL as a retrievability aid.

The same platform hosts the **ICC Case Law Database** (`legal-tools.org/cld`) — curated ICC case law with the Court's own document references, the ICC counterpart of the IRMCT's Case Law Database that the ICTY/ICTR guide already designates. Use it to locate a holding and its exact reference; the citation still carries the ICC document number, verified as usual.

### asp.icc-cpi.int — Assembly of States Parties

Authoritative for:
- ASP resolutions
- Statute amendments (Kampala and subsequent)
- Budget and audit documents
- Independent expert review reports

Entry: `https://asp.icc-cpi.int/`

## Tier 2 — secondary (must be labelled)

Useful for context. Never authoritative on what the Court has said. Always in a clearly separate part of the output (e.g. a "Context" section, or footnotes plainly marked as secondary).

- **Coalition for the ICC** (CICC) — civil-society coalition
- **Human Rights Watch**, **Amnesty International** — NGO reports
- **UN bodies** — Panels of Experts, Commissions of Inquiry, FFMs, OHCHR. Authoritative on facts they investigate; never on ICC findings.
- **Academic journals** — JICJ, LJIL, EJIL, AJIL, ICLR; OUP commentaries (Schabas, Triffterer/Ambos)
- **CLICC / Lexsitus** (`cilrap-lexsitus.org`) — CILRAP's free, provision-by-provision commentary on the Rome Statute and the RPE (chief editor Mark Klamberg), with per-article lectures, preparatory works and digests. The natural first stop for an interpretation question on a specific article; cite as doctrine (e.g. "CLICC, Article 75 commentary"), never as a substitute for what the Court itself held — the holding still gets verified against Tier 1.
- **Mainstream news** — Reuters, AP, AFP, BBC, major broadsheets
- **Specialist journalism** — IJ-Monitor, Justice Info, Opinio Juris
- **OUP ORIL** (`opil.ouplaw.com`) — editorially curated case entries with the Court's own document references; useful for confirming citation details when icc-cpi.int isn't reachable.

When citing secondary material:
- Format that cannot be confused with a Court document.
- Separate part of the output.
- Never used to establish what the Court held. Used only for context, background, or the wider debate.

## Not authoritative — do not cite

- Wikipedia
- Personal blogs that don't quote primary documents (if a blog quotes a Court document, cite the Court document)
- Social media posts
- AI-generated summaries from any tool
- Party press releases (party submission, not Court finding)
- Trial-monitoring summaries as a substitute for the underlying transcript or decision

## Practical notes

- **Redactions.** Cite only the public (`-Red`) version unless the user lawfully has the confidential version. Never cite a confidential filing from memory.
- **Translations.** ICC working languages are English and French. Note `-tENG` / `-tFRA` where translation status matters.
- **Corrigenda.** Documents are sometimes reissued with `-Corr` / `-Corr2` suffixes. Cite the corrected version.
- **Under seal / ex parte.** Treat as unverifiable for any output.

## Fallback ladder when icc-cpi.int returns 403

In order:

1. `web_search` for `[document number] legal-tools.org` → full text (Tier 1; supports level C if the document is retrievable).
2. `web_fetch` against legal-tools.org URLs that appear in search results.
3. `web_search` for `[document number] icc-cpi.int` → ICC press release (Tier 1; supports verification levels A and B).
4. `web_search` for the document on OUP ORIL or in a Court-published "Summary of the Judgment" PDF (Tier 1 / Tier 2 mix; supports levels A and B).
5. If none of the above produces enough, report the level achieved and the gap — do not invent.

When following this ladder, document in the output what was actually checked. The user benefits more from "verified at level B via the Court's press release; full text not retrieved" than from a citation that looks complete but isn't.
