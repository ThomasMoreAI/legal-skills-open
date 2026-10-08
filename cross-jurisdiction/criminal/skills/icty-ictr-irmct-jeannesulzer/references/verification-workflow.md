# Verification workflow — ICTY / ICTR / IRMCT

The step-by-step procedure for verifying a citation before it appears in an output. Read this whenever an output will contain a case-specific citation.

## The principle

No case-specific citation appears in an output until it has been verified against an authoritative source in the current conversation. Foundational instruments (the three Statutes, the RPEs, the Transitional Arrangements) may be cited from project knowledge when present. Everything else — judgments, decisions, indictments, filings — is verified by retrieval.

## The fallback ladder

For each case-specific citation, work down this ladder until verification succeeds:

1. **irmct.org / the case page.** Search for the case (`irmct.org/en/cases`) and open the case page. Confirm case number, accused, status, and locate the document. Mechanism case documents live under `irmct.org/sites/default/files/casedocuments/mict-[number]/…`.
2. **The Case Law Database (cld.irmct.org).** For a *legal finding* — "where was JCE III articulated", "which paragraph held Srebrenica to be genocide" — the CLD maps findings to decisions and paragraphs. Use it to locate, then open the underlying decision.
3. **The Unified Court Records database (ucr.irmct.org).** For filings and the full documentary record by case and document number.
4. **The legacy sites.** `icty.org` for ICTY documents (e.g. `icty.org/en/case/[name]`), `unictr.irmct.org` for ICTR documents.
5. **legal-tools.org.** The ICC Legal Tools Database often has the same document with stable metadata. Cross-check the case number and date against Tier 1.
6. **Secondary source, clearly labelled.** If only a Tier 2 source (academic, IWPR, UN report) can be reached, the output may rely on it *only* with explicit labelling and only for existence/context — never as authority for a precise holding or quotation.
7. **Ask the user.** If nothing verifies, tell the user what is missing and ask them to supply the document or the reference.

## Capture these fields

For every verified citation:
- Party designation (*Prosecutor v. …*, with correct diacritics and any nickname)
- Case number **with phase suffix** (and note if the trial and appeal carry different IT/ICTR vs MICT numbers)
- Document title and **chamber** (Trial Chamber / Appeals Chamber / Single Judge)
- Date
- Paragraph(s), if the claim is paragraph-specific
- **Version**: public, public redacted, or confidential — prefer and cite the public version

## Match the verification level to the claim

- "X was indicted/convicted of genocide" → **existence verified** suffices (case page confirms).
- "The Chamber held that the Srebrenica killings constituted genocide" → **content verified** (the judgment text confirms the holding in substance).
- "The Appeals Chamber held, at paragraph 220, that …" or any quotation → **paragraph verified** (the specific paragraph contains the proposition).

Never state a higher level than was actually reached. If only existence is verified, do not phrase the output as though the holding's wording has been confirmed.

## Protective measures — a hard rule

The ad hoc tribunals made extensive use of witness protective measures. Many witnesses are identified in the record only by pseudonym (e.g. "Witness KDZ-…"), and many documents exist in redacted public versions precisely to protect identities.

- Never attempt to identify, infer, or reconstruct the identity of a protected witness.
- Never reconstruct redacted content.
- Always prefer the public or public redacted version of a document, and say which version is cited.
- If a user supplies what appears to be a confidential or ex parte document, flag it and do not reproduce protected content in the output.

## Partial verification is acceptable if disclosed

If retrieval confirms the case and the document but not the specific paragraph, the honest output says so: *"The Krstić Trial Judgment (IT-98-33-T, 2 August 2001) held that the Srebrenica massacre constituted genocide; the precise paragraph was not confirmed in this session."* Disclosed partial verification is acceptable. Silent overstatement is not.

## Language note

The working languages of the tribunals and the Mechanism are English and French; the authoritative version of a document is the one marked as such (often English, sometimes both). Where a French version is cited, note it. Bosnian/Croatian/Serbian and Kinyarwanda translations exist for many documents but are not the authoritative legal text unless so marked.

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
