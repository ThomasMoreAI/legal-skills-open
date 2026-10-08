# Validation Gate — Five Checks, Dispatch, Reconciliation

The citation-integrity gate runs **every cycle**, over every candidate authority that cycle
produced, before any of it reaches the cycle memo. It replicates the `submissions-verification`
skill's checks so this skill stays standalone.

**Dispatch rule (same as Step 3).** The five checks are dispatched as **five named Claude Code Task
subagents in a single turn** — so they run in genuinely parallel, isolated contexts and each is
separately visible. Name them explicitly; do not collapse two checks into one dispatch; if a check
fails or returns malformed output, re-dispatch only that check. The orchestrator then runs a sixth
**reconciliation** pass itself. (Single-threaded fallback — running the checks sequentially — applies
**only** where the Task tool is absent, e.g. claude.ai chat.)

Certainty states: **verified / suspect / overridden** — never "probably fine". An authority that
cannot be fetched cannot be verified; mark it suspect and say so.

## Common dispatch contract

Every check subagent receives: the **candidate-authority list** for this cycle (citations +
pinpoints + the propositions/quotes attributed to them, from the area-agents' reports); the
**temporal anchor**; a pointer to read `references/retrieval-mechanics.md` before any fetch (jurisd
Layer 0 first — `resolve_citation`, `fetch_document_text`; for treatment/citing-cases the citator
recipe (jurisd v0.5.0 has no live citator; Jade's free-tier citation panel is the best seed); else
the fallback stack) and `references/aglc4-citation.md` (the citation-format rules the existence
check tests against); its role prompt (below); and its output path
`agent-reports/cycle<N>-validation-<check>.md`.

Hard constraints in every check's prompt: work only your own check; ground every finding in a fresh
fetch performed during this dispatch (never from training-data memory); confirm on the highest source
tier reachable (see ranking); if an authority cannot be located after reasonable search, return
`not_located` with the attempts listed — do not guess; write strictly to the §3.7 schema.

## The five role prompts

**Check 1 — Existence** *(paste verbatim):*
> You are the **Existence check**. For every candidate authority, confirm it exists on a primary
> source in the form cited: party names (correct order), court, year, medium-neutral citation number,
> and authorised report volume/page all match. Use jurisd `resolve_citation` (or the fallback) to
> locate it by neutral cite, by report cite, and by party name — whichever resolves first. A Jade
> article (tier 2 — resolve via `site:jade.io "<citation>"`, open in Chrome) is acceptable evidence
> of existence, but anything destined for a filed document still needs tier-1 confirmation. Check
> the **AGLC4 citation string** against the fetched metadata per `references/aglc4-citation.md`: a
> formatting slip is corrected in your note; an element mismatch (wrong year, court, number, or
> report volume/page) is a `FAIL`. Record
> `PASS` (exists, form correct), `FAIL` (cannot locate after listed attempts, or the form is wrong —
> state the discrepancy), or `DISPUTED`. Do not check pinpoint, quote, or treatment. Write to
> `references/templates.md` §3.7.

**Check 2 — Pinpoint** *(paste verbatim):*
> You are the **Pinpoint check**. For every candidate authority with a paragraph/page pinpoint,
> retrieve that pinpoint **verbatim** from the source and compare it to the proposition attributed to
> it. Record `PASS` (pinpoint supports the proposition), `FAIL` (it does not — quote the retrieved
> text and say why), or `DISPUTED`. Where there is no pinpoint, note `not_applicable`. Do not check
> existence, quote fidelity, or treatment. Write to §3.7.

**Check 3 — Quote** *(paste verbatim):*
> You are the **Quote check**. For every candidate authority carrying text in quotation marks,
> retrieve the cited paragraph and compare the quoted text to the source **word-for-word**. Treat as
> discrepancies: changed/dropped/added words, ellipses that hide a qualification, capitalisation or
> punctuation that alters sense, and silent emphasis changes. Record `PASS` (verbatim), `FAIL`
> (substantive discrepancy — show source vs submission side by side), or `DISPUTED`. Pay particular
> attention to ellipses that elide a condition in the original. Skip entries with no quote. Write to
> §3.7.

**Check 4 — Treatment** *(paste verbatim):*
> You are the **Treatment check**. For every case, determine whether it remains good law as at the
> temporal anchor. Use the **citator recipe** in `references/retrieval-mechanics.md` (jurisd v0.5.0
> has no live citator; LawCite/SINO are Cloudflare-walled), optionally seeded by jurisd `search_cases`
> on the case name. Apply
> the **treatment taxonomy** below and assign Good Law / Reinforced / Qualified / Overruled. Where
> Qualified or Overruled, record the name, citation, and URL of the later decision and a 1–3 sentence
> note on what it held. Also record the **how-cited** classification (followed / applied /
> cited-in-argument / mentioned-as-history / distinguished). Record `PASS` (Good Law or Reinforced),
> `FAIL` (Overruled, or Qualified in a way that defeats the proposition relied on), or `DISPUTED`.
> Skip statutes — the currency check owns those. Write to §3.7.

**Check 5 — Red-team (currency)** *(paste verbatim):*
> You are the **Red-team currency check**. Adversarially test the cycle's authorities: (a) for every
> statutory citation, confirm via the register that the section exists, bears the content claimed,
> and the **version was in force as at the temporal anchor** (or the relevant past date) — state any
> version mismatch precisely; (b) flag any common-law authority cited as live where statute has since
> codified, modified, or displaced the principle; (c) flag mis-characterised holdings (obiter as
> ratio, plurality as majority, dissent as accepted). Record `PASS` / `FAIL` / `DISPUTED` per item
> with the issue stated. Write to §3.7.

## Treatment taxonomy (decision tree for Check 4)

- **Overruled** — a higher court, or the same court in a later case, has held it wrongly decided / no
  longer good law. → **Do not rely.** Mark suspect; tell the orchestrator to replace it.
- **Qualified / Distinguished / Doubted** — later authority limits it, distinguishes it on the
  facts/law, or expresses doubt. → Rely **with care**; record the limitation and the limiting case.
- **Reinforced** — later higher authority approves or follows it. → Strong; record the approving case.
- **Good Law** — no adverse subsequent treatment found after running the defined paths. → Stands (a
  verified-negative finding, not an absence of work).

A **history-only** citation (mentioned-as-history) does not make a case authority for a proposition —
never report it as endorsement.

## Source-authority ranking (every check)

Confirm on the highest tier reachable; anything to be **relied on in a filed document** must be
confirmed on a **tier-1 primary source** (AustLII / CaseLaw NSW / HCA site / legislation registers,
or a jurisd fetch of same). Tiers below primary — official-party host / authentic aggregator
(including free-tier Jade), chambers/law-society summary, general aggregator — may *surface* an
item (Jade is good enough for existence and text) but are not sufficient for court reliance. Record
the tier consulted for each authority.

## Reconciliation (orchestrator's sixth pass)

A **dispute** is any disagreement between the checks on existence, pinpoint match, quote fidelity, or
treatment, **or** any single `FAIL` on a substantive question, **or** any Red-team flag the other
checks did not address. For each disputed item the orchestrator runs an **independent re-fetch on a
primary source** (it does not vote — the checks are input, not ballots) and records the resolution in
the **Reconciliation Log** in the cycle memo: what each check found, where they diverged, and how it
was settled.

## Outcome feeding the memo

- **Verified** — passes all applicable checks on a tier-1 source; treatment ≠ Overruled. Reported as
  good law with its treatment + how-cited.
- **Suspect** — fails a check, cannot be fetched, or is Overruled. Flagged; **not** presented as good
  law; the orchestrator decides whether to replace it (may spawn a follow-up case-law task).
- **Overridden** — only if the user explicitly overrides (e.g. a decision too recent to be indexed);
  recorded with the user's stated reason.
