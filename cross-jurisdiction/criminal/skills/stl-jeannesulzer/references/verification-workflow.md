# Verification workflow — STL

The step-by-step procedure for verifying an STL citation before it appears in an output.

## The principle

No case-specific citation appears in an output until it has been verified against an authoritative source in the current conversation. Foundational instruments (UN-Lebanon Agreement, Resolution 1757, Statute, RPE) may be cited from project knowledge when present. Everything else — passages of the Trial Judgment, the 2011 Interlocutory Decision, indictments, sentencing judgments, contempt cases — is verified by retrieval.

## The fallback ladder

1. **stl-tsl.org** — the official legacy website. First point of entry for the Statute, the major decisions and judgments, case information sheets, and procedural records. The site is preserved post-closure but no longer actively maintained.
2. **Wayback Machine** (`https://web.archive.org/web/*/stl-tsl.org/*`) — fallback if a particular stl-tsl.org page returns an error.
3. **legal-tools.org** — ICC Legal Tools Database, mirrors STL principal decisions with permanent IDs.
4. **un.org** — for the founding resolutions (1644, 1664, 1686, 1757) and Secretary-General reports.
5. **UN Audiovisual Library** (`https://legal.un.org/avl/`) — for the introductory note on the Statute.
6. **Tier 2 scholarship** (Cassese, Scharf, Milanović, Vasiliev, Saul, Ambos, Kress) — for context and doctrinal commentary; never as authority for what the Tribunal has held.
7. **Ask the user** if nothing verifies.

## Capture these fields

For every verified citation:

- **Case number** — STL-11-01, STL-13-04, STL-18-10, STL-14-05, STL-14-06, etc.
- **Phase suffix and chamber** — I/AC, PT/TC, T/TC, S/TC, A/AC, R176bis, etc.
- **Document title** — the full title as it appears on the filing
- **Date** — the date of the decision or filing
- **Paragraph number(s)** — required for paragraph-pinpoint citations and quotations
- **For in absentia decisions** — note that the trial was held in absentia (Statute Art. 22) and identify the Rule 106 review status if relevant
- **Public vs confidential** — use public versions; identify version status

## Match the verification level to the claim

- "Ayyash was convicted in absentia in case STL-11-01 on 18 August 2020" → existence verified
- "The Trial Chamber held that Ayyash committed a terrorist act by means of an explosive device" → content verified
- A direct quotation from the Trial Judgment or the 2011 Interlocutory Decision → paragraph verified

Never state a higher level than was actually reached.

## Specific STL traps

### Trap 1 — The 2011 Interlocutory Decision and customary international law

The Appeals Chamber's **Interlocutory Decision on the Applicable Law** of 16 February 2011 held that an emerging customary international law definition of terrorism in peacetime had crystallised. **This finding is heavily contested in scholarship** and has not been adopted by subsequent international tribunals.

When citing the decision:
- Cite it accurately as the holding of the STL Appeals Chamber.
- Note its contested status when relevant to the proposition.
- Do not represent the customary international law finding as universally accepted; do not assume it has been adopted by the ICC, ICTY/IRMCT, ICTR, or other tribunals.
- Distinguish the STL's finding under STL law from any general claim about customary international law.

### Trap 2 — Trial in absentia procedure and the right to retrial

STL Statute Art. 22 authorises trial in absentia. Rule 106 of the RPE governs the procedure on subsequent arrest or surrender. **Note carefully:**
- Article 22 imposes conditions on in absentia trial (notification, representation, etc.).
- Rule 106 provides for retrial *de novo* if the accused subsequently appears, **except** in certain conditions where the accused was effectively notified and waived participation.
- The Defence Office plays an unusual institutional role at the STL — it is an organ on equal footing with the Prosecutor, not a private defence team. Decisions affecting defence rights are often referenced as Defence Office decisions, not Prosecutor decisions.

Misstating the retrial right at the STL is a common error. Verify against the current Statute and the RPE in force at the relevant date.

### Trap 3 — Lebanese law vs international law

The STL applies **Lebanese substantive criminal law** for the offences themselves (Article 314 of the Lebanese Criminal Code on terrorism, etc.). Modes of liability are international (Statute Art. 3). Sentencing draws on Lebanese law (with reference to international standards for in absentia and review).

Common error: characterising the STL as having convicted Ayyash of "the international crime of terrorism" — strictly inaccurate. The STL convicted Ayyash of *terrorism under Article 314 of the Lebanese Criminal Code* (as informed by the STL's reading of the elements via the 2011 Interlocutory Decision). The international dimension is in the Tribunal's structure, not in the substantive criminal law.

### Trap 4 — The connected/related attacks distinction

STL jurisdiction extends to attacks "connected" to the 14 February 2005 Hariri attack (Statute Art. 1). Connected attacks (Hamadeh, Hawi, El-Murr) were the subject of separate cases, primarily **STL-18-10**, not the principal STL-11-01. Confusing the cases means citing the wrong judgment for the wrong attack.

### Trap 5 — Defendant status changes between Trial Chamber and Appeals Chamber

The Trial Chamber on 18 August 2020 acquitted Merhi, Oneissi, and Sabra. The Prosecutor appealed the acquittals of Merhi and Oneissi (not Sabra). The Appeals Chamber subsequently *reversed* certain Merhi and Oneissi acquittals and convicted them in absentia; sentencing followed on 16 June 2022.

If citing a defendant's status, identify which decision is the source (Trial Chamber judgment of 18 August 2020 vs Appeals Chamber judgment of 10 March 2022 vs Sentencing Judgment of 16 June 2022).

## Translation discipline

STL proceedings were conducted in English, French, and Arabic. Many filings exist in all three; the **English version is typically authoritative for international scholarship**. Where the original speaker spoke Arabic or French, the original-language version may matter for interpretation. The Statute exists in three authentic texts (Art. 30 of the Statute).

If citing a particular language version, identify it.

## Partial verification is acceptable if disclosed

If you can confirm the existence and substance of a passage but not the paragraph, the honest output says so. Disclosed partial verification is acceptable; silent overstatement is not.

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
