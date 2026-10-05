# Lawyer workflow

Keep the first interaction short. Ask for the target document, the authorities the lawyer wants checked, and the intended use. Ask about tribunal, governing jurisdiction, posture, or an as-of date only when that context could change the review; ask no more than three focused questions in one turn.

A useful opening is: “Please cite-check this filing against the authorities I provide and show the source evidence for every material problem.”

## 1. Prep, environment, and plan

Ask for the full text of the cases, statutes, regulations, rules, record materials, or other sources used by the drafter. A citation, filename, URL, or model memory is not source evidence. If no authorities were supplied, explain that the run can search for cited cases but cannot verify what they say.

For a Westlaw subscriber whose license permits the intended use, recommend obtaining the separate, complete, readable underlying documents through the download route their subscription actually offers rather than supplying only a result list or research report. Follow [getting-authorities.md](getting-authorities.md#recommended-westlaw-workflow), which deliberately avoids an unverified product-specific click path. If the lawyer already has the authorities, accept the files directly.

When a case is not in the supplied authorities, search a public case source using only the citation and case metadata. Report whether search was unavailable, the case was not found and may be hallucinated, or the case was found but not supplied for substantive checking. A public search result does not verify what the case says.

After reading the brief and source files, give one broad source-set overview: readable-file count, rough categories that appear present, and categories that are not apparent or appear missing. This is not a per-citation check and not a parent citation census. Do not match citations to authorities until the assigned-unit review.

Run the packaged `scripts/cite_check.py`. It starts one fresh Codex session for each prepared unit. If the host cannot run it, keep the same one-unit assignments with native workers or process them one at a time. The environment probe only checks local capability; it makes no model call and reads no matter content.

## 2. Per-unit fan-out

The parent converts the target to Markdown or plain text, makes one unit per extractable text container, assigns stable `P####`/`F####` IDs, records file paths and line ranges, and does the broad source-set overview above. Run the packaged script; it uses one fresh Codex session per prepared unit. If it cannot run, use native workers or one-at-a-time processing with the same prompt and evidence universe.

## 3. Advisory retry

Give one targeted retry for mechanically incomplete evidence: a missing excerpt, missing locator, invalid or out-of-authority source ID, or inconsistent source-match fields. Do not retry substantive legal disagreement. If the repair still fails, retain the citation as amber (claimed but unverified). Completed receipts and raw attempts remain in the same run directory.

## 4. HTML report and sense check

When the packaged scripts are available, use `scripts/aggregate_report.py` to validate the receipts and render `assets/report-template.html`. If local scripts are unavailable, render the same validated report data with the supplied template using host-native capabilities. Do not hand-author replacement HTML unless the user requests a custom report. The report's main body contains citation rows, while its appendix accounts for every prepared unit, including `no_citations_found`, complete, failed, and still-missing states. One bounded sense check confirms that the appendix accounts for every unit, no visibly citation-dense passage has zero citation rows, and no finding contradicts itself on its face. Anything unresolved goes in `Caveats / Issues`. Include the report's one-sentence scope reminder in the final message so the lawyer understands the scope of the review performed.

If the packaged script cannot run, continue with one-unit native or sequential review. Tell the lawyer only that the fallback may take longer. Do not burden a nontechnical lawyer with runtime setup when the review can continue.

## What the check means

The check compares the target's propositions, quotations, source characterizations, pinpoints, and procedural assertions with the supplied readable sources. It can identify a statement the source does not support or affirmatively conflicts with, an overbroad characterization, a wrong pinpoint, a misleading quotation or omission, an unresolved short-form chain, or a source that cannot be matched or read.

It does not by itself establish that an authority remains good law. Shepard's, KeyCite, later history, amendments, negative treatment, and comprehensive currentness require separately supplied treatment evidence. Authority status is limited to what the source visibly identifies: opinion component, publication or precedential designation, source-visible disposition, issuing court, decision date, and posture.

Civil advocacy may emphasize favorable facts, distinguish adverse authority, preserve an issue, choose the order of its principal arguments, and decide whether a peripheral or unraised point needs rebuttal when no rule or order requires one. It does not permit an objectively false statement, material misstatement, overstatement of what a source says, or quotation that changes meaning. Evidence preservation is a separate obligation: follow any applicable hold, discovery or preservation order, subpoena, privilege rule, and local procedure, and do not alter, destroy, or conceal material evidence when those duties apply. Do not assume that every omission is unethical or that every adverse fact must be volunteered to an adversary. Read [ethics-and-jurisdictions.md](ethics-and-jurisdictions.md) when tribunal, jurisdiction, posture, audience, ex parte status, controlling adverse authority, preservation, discovery, or omission questions could affect the result. The skill does not adjudicate professional responsibility. Do not infer knowledge, intent, materiality, or misconduct from a source flag alone.

The lawyer remains responsible for confidentiality, applicable law, professional duties, and the filing decision. Inspect source excerpts, locators, warnings, limitations, and unresolved questions before changing the filing. Do not call a report verified when source, coverage, jurisdiction, or currentness questions remain unresolved.
