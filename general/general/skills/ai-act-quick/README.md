# EU AI Act Quick Assessment

A fast (15–25 minute) **triage** for the EU AI Act (Regulation (EU) 2024/1689): preliminary risk
classification, role determination, headline obligations, timeline, and penalty exposure — a quick
"where do we stand?" before committing to a full assessment.

## When to use

Use this skill for a rapid first read: "does the AI Act apply to us, and at what risk tier?", a quick
provider-vs-deployer check, an Annex III screen, or a German **Schnellprüfung / Ersteinschätzung**.
It is deliberately a triage, not a compliance decision.

## How it works

1. **Quick context** — an adaptive 1–2 batch intake that captures eight fields (what the system does,
   deployment, role, sector, affected persons, modifications, size, jurisdiction) with generous
   extraction so the user rarely answers more than once.
2. **Six-gate classification** (internal) — Art. 2 scope → Art. 3(1) AI-system test → Art. 5
   prohibited screen → Annex I/III high-risk (with the Art. 6(3) exception) → GPAI → Art. 50
   transparency.
3. **Preliminary output** — a single consolidated card: classification, role, top obligations,
   timeline (with the AI Omnibus 2026 postponement applied), jurisdiction flags, Art. 99 penalty
   exposure, and warnings — every determination marked **"Likely"**.
4. **Optional templates** — preliminary classification record, compliance register entry, or
   management briefing, all marked preliminary.

It is **self-contained**: where it recommends a "full assessment," that means depth classification,
role, and obligation analysis plus legal review — not a dependency on any other installed skill.

## Worked example

See [`examples/ai-act-quick-worked-example.md`](examples/ai-act-quick-worked-example.md) for a full
triage of a third-party CV-screening tool used by a German mid-size deployer (intake → six gates →
preliminary output → next steps).

## Reference material

In [`references/`](references/), loaded on demand: `quick-decision-tree.md` (condensed gate logic),
`compliance-deadlines.md` (the four regulatory phases + Omnibus dates), and `jurisdiction-flags.md`
(Member-State-specific flags such as works-council and sectoral-regulator triggers).

## Installation

Copy the `ai-act-quick/` folder into your skills directory (e.g. `~/.claude/skills/ai-act-quick/`). It
auto-triggers on "quick AI Act assessment", "does the AI Act apply", "AI Act triage", "Schnellprüfung",
"Ersteinschätzung", and similar.

## Limitations

This is a **triage tool, not legal advice and not a compliance decision** — every "Likely"
determination requires a full, documented assessment and qualified legal counsel before reliance. It
does not confirm a risk tier, does not invent citations (thin inputs are marked `[UNCLEAR]`), does not
certify compliance, and reports Art. 99 statutory **maxima** for context rather than predicting actual
fines. It prompts a web search on activation because guidelines and enforcement are still developing.
See the **"What this skill does not do"** section in `SKILL.md`.

## License

Apache-2.0 — see [LICENSE](LICENSE). Authored by Oliver Schmidt-Prietz.

---

*More EU regulatory skills (GDPR, EU AI Act, Data Act, NIS2, and more) →
[github.com/oliverschmidtprietz](https://github.com/oliverschmidtprietz)*

## Liability

This skill is provided **"as is" under the Apache License 2.0** — without warranties of any kind, and subject to the limitation of liability in §§ 7–8 of that license. It is not legal advice and creates no attorney–client relationship. To the fullest extent permitted by law, the author (Oliver Schmidt-Prietz, Rechtsanwalt, Germany) accepts no liability for any use of, or reliance on, this skill or its output; users use it at their own responsibility and are solely responsible for validating results and for their own compliance decisions.
