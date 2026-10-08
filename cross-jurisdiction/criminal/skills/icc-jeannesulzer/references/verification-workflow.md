# Verification workflow

The operational procedure for getting any ICC citation into an output. Read this any time you are about to draft something containing ICC citations.

## The discipline

For any case-specific document — judgment, decision, warrant, filing, OTP statement — verify before citing. Verification means retrieving the document from legal-tools.org (the ICC Legal Tools Database, where the Court's public decisions are systematically registered) or icc-cpi.int (or another Tier 1 source) in the current conversation. Foundational texts in project knowledge are the only exception.

The reason: ICC document numbers are exact, paragraph numbers are exact, and the cost of an invented citation in real work — a filed brief, a published article, an internal memo a colleague relies on — is high. Two to five `web_fetch` calls per citation is the correct cost.

## Verification is gradient

In practice, retrieval is unreliable. icc-cpi.int sometimes returns 403. Some documents are only on legal-tools.org. Some are paywalled in academic databases. Treat verification as having three levels, and apply them per-claim, not per-document:

| Level | What is confirmed | Use it for |
|---|---|---|
| **Existence** | Document number, title, date, chamber against a Tier 1 source | "X case was decided on Y date by Z Chamber" |
| **Content** | The retrieved text confirms the document holds, in substance, what the output claims | "The Chamber held that…" |
| **Paragraph** | The cited paragraph(s) contain the cited proposition | Any quotation, any paragraph-pinpoint |

If the output's claim is "Z Chamber held X in paragraph N", paragraph-level verification is required. If the claim is "the Chamber convicted on Y date", existence-level is enough. Match the verification to the claim.

When verification stops short of what the claim needs, either: (a) soften the claim to match what is verified, or (b) flag in the output that the paragraph-level pinpoint is provisional pending fetch.

## The fallback ladder

When the first attempt fails, work the ladder. Stop at the first level that gives you what the claim needs.

**1. legal-tools.org.** The ICC Legal Tools Database — the first retrieval stop. The Court's public decisions are systematically registered there, each under a Persistent URL, and the Database answers automated retrieval reliably. Search the document number; open the record.

**2. icc-cpi.int direct fetch.** The case page or court-record URL. Authoritative whenever it answers; its 403s are structural, not a sign the document does not exist.

**3. Search-engine snippet from a Tier 1 domain.** `web_search` for the document number plus `icc-cpi.int` or `legal-tools.org`. If a result excerpts the relevant passage from a Tier 1 page, that excerpt is existence-verifying (the document exists and the search engine pulled real text from a Tier 1 URL) but generally not paragraph-verifying (snippets are short and not always paragraph-aligned).

**4. Court press release on icc-cpi.int.** ICC press releases summarise decisions in the Court's own voice. They establish existence and broad holding, not paragraph text.

**5. Authoritative secondary databases.** Oxford ORIL (opil.ouplaw.com) hosts the Court's own structured summaries; some academic databases mirror filings. Existence-verifying when the database cites the document number; not paragraph-verifying unless the source includes the full text.

**6. Ask the user for a URL.** The user may have direct access (e.g. through a Court-records portal) that the skill does not.

**Never** invent a paragraph number to fill a gap. If verification stops at level 4, the output stops at level-4 claims.

## Standard workflow

**Step 0 — Identify the document.** Before listing citations or fetching anything, read what is actually in front of you. If the user provides a file, open it and confirm its case, document number, date, chamber against the document's own header. If the user references a document by name ("the Lubanga reparations order"), confirm which one (there are several; appellate amendments matter). Identity errors propagate; one read at Step 0 prevents them.

**Step 1 — Build the citation list.** Before drafting, list every citation that will appear, with the proposition each will support and the source to verify against.

**Step 2 — Verify each citation.** Work the ladder for each. Capture: document number (with all suffixes), date as printed, chamber, title verbatim, paragraph numbers. Read the cited passage and confirm it supports the proposition. Record the verification level reached.

**Step 3 — Draft using verified material.** Match the verification level to the claim. Where partial, label.

**Step 4 — Self-audit.** Walk through every citation in the output. For each:
- Is it from project knowledge (foundational text) or a successful retrieval in this conversation?
- Does the cited proposition match what was retrieved?
- Is the verification level appropriate to the claim?

If any answer is no, fix it or remove the citation.

## Worked example

**User**: "Draft a paragraph on the Bemba effective control test under Article 28, with citations."

**Step 0 — identify the documents.** Bemba has two decisive judgments: Trial Chamber III conviction (21 March 2016, `ICC-01/05-01/08-3343`) and Appeals Chamber acquittal (8 June 2018, `ICC-01/05-01/08-3636-Red`). A memo on effective control that does not address the acquittal would be misleading. Both documents must be in the citation list.

**Step 1 — citation list.**
- Bemba TJ on the effective-control standard, expected paragraphs in the Article 28 / command-responsibility section.
- Bemba AJ on the set-aside and its reasoning.

**Step 2 — verify.**

```
search legal-tools.org for "ICC-01/05-01/08-3343" → open the record's Persistent URL
```

If this succeeds: read the Article 28 section. Note the paragraphs articulating the standard. Verification: paragraph-level.

If the Database record is not retrievable: try the icc-cpi.int court record directly, then the search snippet, then the press release. Each gives a different verification level. The output must then match. If only the press release is reachable, the output can say "the Trial Chamber's articulation of effective control" but cannot quote or pinpoint to a paragraph.

Repeat for the AJ.

**Step 3 — draft.**

> Under Article 28(a) of the Rome Statute, a military commander incurs criminal responsibility for crimes committed by forces under his effective command and control. The Trial Chamber in *Bemba* articulated effective control as requiring the material ability to prevent or repress crimes [*Prosecutor v. Bemba*, Trial Chamber III, "Judgment pursuant to Article 74 of the Statute", ICC-01/05-01/08-3343, 21 March 2016, paras [verified]]. **This judgment was set aside on appeal.** The Appeals Chamber acquitted Mr Bemba by majority, finding that the Trial Chamber had erred on two grounds: convicting him for criminal acts that fell outside the scope of the confirmed charges, and in its assessment of the measures he took to prevent and repress crimes by the MLC contingent in the CAR [*Prosecutor v. Bemba*, Appeals Chamber, ICC-01/05-01/08-3636-Red, 8 June 2018, paras [verified]].

The `[verified]` placeholders are filled from the actual retrieved content. If retrieval stopped at level 4, the draft instead says: "The Trial Chamber articulated effective control as requiring the material ability to prevent or repress crimes (TJ paragraph references to be confirmed against the full text)."

**Step 4 — self-audit.**
- TJ exists, content matches, paragraphs verified: yes
- AJ exists, content matches, paragraphs verified: yes
- Article 28(a) used (not the non-statutory "28(1)"), matching the Statute's numbering: yes

## What this discipline buys and costs

**Cost:** two to five `web_fetch` calls per substantive citation. For a brief with twenty citations, this can be the bulk of the work.

**Buys:**
- No invented document numbers
- No misremembered holdings
- Honest verification status on each claim
- Secondary material clearly separable from Court findings
- Output that a downstream user can rely on as a starting point for real work

The skill exists because this discipline does not happen automatically. Following it under time pressure is the test.

---

## Reading the source document directly (the top of the ladder)

The most reliable verification is reading the **actual document**, not a
website's search snippet. Put this above everything else:

**Rung 0 — work from the document itself when it is available.** Official
tribunal sites frequently block automated fetching (HTTP 403), so a judgment
can be public yet still unreachable by a direct fetch. Two ways to reach the
text anyway:

- **The user supplies it** — an uploaded PDF or pasted pages can be read
  directly, reaching paragraph-level verification. A practitioner working on a
  matter usually already holds the document; ask for it.
- **A retrieval tool reads it** — where a document-retrieval tool or MCP server
  is available (one that fetches and extracts PDF text, with a fallback
  ladder), prefer it over a raw fetch.

Only when the document cannot be obtained do you fall back to the search ladder
above — and then you state the ceiling honestly.

## Site-search results are leads, not content

A result from a site-search index — or a "synthesis" of search snippets —
establishes at most that something **exists**. It is **never** content- or
paragraph-level verification. Treat it as a lead to confirm against the
document, and label it as such. Two recurring traps:

- **Transliteration / OCR garbling.** Names and acronyms get corrupted (for
  example, an Arabic acronym surfacing as "KARA" where the source has
  "RADA/RADAA"). A name or acronym that appears only once in a snippet is a red
  flag — do not assert it.
- **Relational claims.** Who is whose subordinate, associate, superior, or
  co-perpetrator is the detail a synthesis most often gets inverted. Never
  assert a relationship from a snippet; it requires the document.
