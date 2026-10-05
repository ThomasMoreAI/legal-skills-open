# Getting authorities for `/cite-check`

The cite-check is only as reliable as the sources it can actually read. Give `/cite-check` the target filing or brief and the authority documents that support it. Tell the reviewer the tribunal, jurisdiction, and relevant as-of date when those facts affect the result.

## What to supply

Keep the target document separate from the authority set.

- **Target:** the exact filing, brief, or excerpt to review, including the version that will be filed or circulated.
- **Authorities:** separate files for the cases, statutes, regulations, rules, record materials, exhibits, and transcripts the target relies on.
- **Source identity:** the citation, case name, court, date, docket or document number, and any pinpoint information you know. A filename is not source identity.
- **Scope:** the jurisdiction, tribunal, posture, and as-of date for the check.

Supply the target and the authority files you want checked. Keep client and authority material in the review workspace.

Use the authority files, not an account password or token. Never ask the lawyer to provide service credentials in chat.

## Build the source set by authority type

The right source set depends on what the target says and the procedural posture. Look for four main categories:

- **Case law:** the precedential or nonprecedential prior court decisions the target cites or characterizes. Preserve the full opinion, including any separate concurrence or dissent that matters, rather than a search-result entry, headnote, or summary.
- **Statutes and regulations:** the text for the version and effective date that govern the issue, together with amendments, commencement material, or prior versions when timing matters.
- **Legislative and administrative materials:** legislative history, administrative history, administrative enforcement actions, agency orders or decisions, rulemaking notices and comments, and other primary materials on which the target relies.
- **Case-specific materials:** the parts of the matter record needed to test factual or procedural assertions, such as the certified administrative record in an administrative case, the pleadings on a motion to dismiss, or the discovery record in a civil case where discovery has occurred.

Most lawyers will want at least the cited case law checked even when the rest of the source set is narrower. For a United States matter, a Westlaw subscriber can use the workflow below if the subscription and license permit it. For United States case law, CourtListener and other free case-law services can help locate a public copy. In every route, obtain the complete readable decision before treating the case's substance as checked.

## Jurisdiction-specific authority sources

Jurisdiction-specific acquisition rules, publication practices, source coverage, and reuse terms may apply. Start with the relevant page below, then confirm any court-specific restriction or local source the page does not cover:

- [United States](authority-sources/united-states.md)
- [United Kingdom](authority-sources/united-kingdom.md)
- [New Zealand](authority-sources/new-zealand.md)
- [Canada](authority-sources/canada.md)
- [Australia](authority-sources/australia.md)

These pages identify practical acquisition routes. They do not decide whether a source is binding, citable, current, complete, or sufficient for the matter.

## Recommended Westlaw workflow

If you subscribe to Westlaw and your license permits using the downloaded material with external AI products, Westlaw can be a straightforward way to gather separate, complete, readable authority files. Treat it as an acquisition route. A Westlaw copy does not by itself establish that the document is an issuing court's official publication, remains good law, has no later history, or has received complete and current KeyCite treatment.

This skill is not affiliated with Thomson Reuters, Westlaw, or any registered trademark thereof. Users are responsible for ensuring that their use of external platforms complies with any applicable terms and conditions.

Westlaw products, subscriptions, and interfaces vary, and the public product documentation does not establish a universal click path. This is outcome-based acquisition guidance rather than unverified interface instructions. Use the search, citation-analysis, or document-download path actually available to the subscriber, without asking for credentials in chat. The goal is the underlying authority text, not only a result list, citation report, headnote, synopsis, or link.

For each cited case or other authority:

1. Locate it by citation, case name, court, date, docket, or another public identifier.
2. Open the underlying document and confirm its visible identity before downloading it.
3. Obtain the complete readable text rather than a title-only entry, excerpt, or search result. Keep separate files when the interface permits so each source can receive a stable `sourceId`.
4. Preserve the citation, court or issuing body, decision or issuance date, version, and any relevant pinpoint. Keep editorial material distinguishable from the authority itself.
5. If the available output is only a list or research report, use it as a locator and obtain the underlying documents separately.

Keep the target brief separate from the downloaded authorities. If the host cannot unpack an archive, extract it outside the review and upload the readable files; do not install a tool or treat the authorities as absent. If the subscription cannot provide the complete readable authority, ask the lawyer to supply another authorized copy.

## Use files you already have

You may supply authority files you already have. Cases, statutes, regulations, court rules, record materials, exhibits, and transcripts are all useful when they are the sources the target actually relies on.

For each file, preserve the original file and provide the best available source identity. A short manifest is helpful:

| File | What it is | Citation or identifier | Court or issuing body | Date | Pinpoint or relevant pages | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `authority-01.docx` | Case | Reporter or neutral citation | Court | Decision date | Page or paragraph | Official, subscription, or user-supplied |

The reviewer will compare the proposition or quotation in the target with the supplied source. It will not infer missing text from a filename, a citation it recognizes, or a different case that looks similar.

## Public case search with CourtListener

CourtListener, a Free Law Project service, is a public source for United States case law; for other jurisdictions, start with the [jurisdiction-specific authority sources](#jurisdiction-specific-authority-sources). When a case does not match a supplied authority, search CourtListener or another available public source using the citation, case name, court, date, docket, or other public identifier.

CourtListener or a similar public case source may already be available through web search. CourtListener also publishes a [Model Context Protocol server](https://wiki.free.law/c/courtlistener/help/api/mcp/using-the-courtlistener-mcp-in-claude-chatgpt-and-other-ai-assistants) for supported hosts. Its current operator guidance says a CourtListener account is required, standard API access is granted automatically to users, and elevated access is available through Free Law Project membership or a commercial agreement. Use that route only when the host exposes it and the user has authorized the connection.

Send only that citation metadata to the public service. Never upload the client brief, a confidential excerpt, or matter facts merely to find a case.

Report one of three outcomes: the environment could not search; the search did not find the case and it may be hallucinated; or the case was found but was not supplied for substantive checking.

A public search result can show that a case was found, but it does not verify what the case says. For substantive checking, add the complete authority to the workspace with a manifest `sourceId`, or ask the lawyer to supply it. The reviewer then matches it by readable content rather than filename.

If the case is missing, blocked, incomplete, poorly reproduced, or unavailable, supply the authority file yourself. Do not treat a public search result, metadata record, or partial reproduction as the complete authority.

CourtListener does not promise complete coverage; see Free Law Project's [case-law coverage guide](https://wiki.free.law/c/courtlistener/help/data-coverage/case-law) for details. It is not a substitute for checking later treatment in a citator such as KeyCite or Shepard's.

## Authority status and treatment evidence

For a supplied opinion, authority status is limited to what the source itself visibly identifies: the opinion component (such as majority, concurrence, or dissent), publication or precedential designation, the source-visible disposition, the issuing court, the decision date, and the procedural posture. Do not infer an opinion component, publication status, precedential effect, or posture from a filename, citation recognition, or model memory.

Current validity, vacatur, overruling, subsequent limitation, amendment, or other later treatment requires supplied treatment evidence that directly addresses that question. A source-visible statement about the decision's disposition is not proof that the authority remains good law or has not later been vacated or overruled. Without treatment evidence, report currentness as outside the supplied source universe and do not present the authority as current law.

## When a source is not usable

Report the problem plainly. Do not silently substitute a different authority or fill in missing text.

| Problem | What to do |
| --- | --- |
| Missing authority | Search for an identifiable case, report the search outcome, and ask for the exact authority file if its substance must be checked. Do not verify the proposition from memory. |
| Ambiguous citation or match | Ask for the court, date, docket, case name, reporter or neutral citation, and any pinpoint. Keep the result unresolved until the identity is confirmed. |
| Duplicate files | Preserve the supplied files, identify the duplicate content, and avoid counting one authority twice. Ask before treating two similar-looking files as the same edition or decision. |
| Paywalled source | Do not bypass the paywall. Ask for the full authority file from someone who can obtain it. |
| Scanned or image-only file | Ask for a searchable or native-text version when possible. The skill does not install, orchestrate, or require an OCR pipeline; if the host already exposes a local extraction capability, label the result as extracted text. If the text cannot be read reliably, mark the source inaccessible. |
| Misleading filename | Inspect the document's visible title, citation, court, date, and contents. Record the mismatch and ask for clarification; never identify an authority from the filename alone. |
| Wrong authority supplied | Mark the citation-to-source mismatch and ask for the cited authority. Do not silently replace it with a similar case, later decision, or unofficial summary. |

A source that cannot be read is not a source that has been verified. The report should distinguish **source inaccessible**, **not found**, **mismatch**, and **coverage insufficient** rather than collapsing them into one uncertain result.

Obtaining authorities does not expand the review into citator research. The review's scope is in [SKILL.md](../SKILL.md).

## Handling source text

Keep subscription-service text in the workspace rather than bundling it into the plugin or public fixtures. No client or subscription-service source text is included here. Search public case sources using citation metadata only. If a complete public authority is later added for substantive checking, save it in the workspace, assign it a manifest `sourceId`, and record its source. Keep working copies and reports in the workspace, and minimize reproduced source text to what the review requires.
