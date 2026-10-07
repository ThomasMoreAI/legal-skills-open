# DPA Art. 28 GDPR — Review, Drafting & Redlining

Review, draft, and redline **Data Processing Agreements (DPA / Auftragsverarbeitungsvertrag / AVV)**
under **Art. 28 GDPR**, and prepare **Joint Controller Arrangements** under **Art. 26 GDPR** — bilingual
(DE / EN), from either the controller's or processor's perspective.

## When to use

Use this skill to check whether a DPA is compliant and signable, to draft a new AVV from modular
templates, to redline a counterparty's draft with tracked changes, or to determine whether two parties
are in a controller-processor or a joint-controller relationship. Triggers include "DPA", "AVV",
"Auftragsverarbeitung", "Art. 28 contract", "processor agreement", "JCA", and "Art. 26 arrangement".

## How it works

A **mode router** runs first and classifies the request into one of five modes, each with its own
output structure:

| Mode | Produces |
|---|---|
| `REVIEW_QUICK` | Art. 28(3)(a)–(h) coverage table + sign / no-sign recommendation |
| `REVIEW_NEG` | Clause-by-clause risk scoring + negotiation strategy + walk-away conditions |
| `DRAFT` | A complete DPA / AVV from a chosen tier (Commercial / Strict / Hybrid), with Annexes |
| `REDLINE` | Marked-up counter-proposal + cover memo with fallback positions |
| `JOINT_CONTROLLER` | An Art. 26 JCA with an allocation matrix + public summary |

A structured intake (roles, perspective, language, tier, processing scenario, transfers,
sub-processors, special-category data) precedes any output, and hard rules prevent the common
invalidating defects (missing TOMs, empty sub-processor annex, non-operative SCC references,
mis-papering a joint-controller relationship as a DPA).

## Worked example

See [`examples/dpa-art28-worked-example.md`](examples/dpa-art28-worked-example.md) for a full
`REVIEW_QUICK` of a processor-favourable SaaS DPA (coverage table → blockers → recommendation).

## What's in the folder

| Folder | Contents |
|---|---|
| `references/` | Art. 28(3) checklist, common defects, negotiation fallbacks, tier selection, SCC module guide, Art. 26 joint-controller screen, and the EU SCC 2021/915 text (DE/EN) |
| `templates/` | DPA templates — Commercial / Strict / Hybrid and a JCA, each in DE and EN |
| `workflows/` | The five mode workflows (quick review, negotiation review, draft, redline, joint-controller) |

## Installation

Copy the `dpa-art28/` folder into your skills directory (e.g. `~/.claude/skills/dpa-art28/`). It
auto-triggers on DPA / AVV / Art. 28 / Art. 26 / joint-controller language.

## Limitations

This skill provides **drafting and analysis, not legal advice**, and does not certify compliance or
guarantee a "safe to sign" outcome — its default posture after a quick review is "sign with documented
residual risk" or "request changes." It defers enforceability opinions and does not fabricate
citations. Bilingual output is drafting support, not certified legal translation. See the **"What this
skill does not do"** section in `SKILL.md`.

## License

Apache-2.0 — see [LICENSE](LICENSE). Authored by Oliver Schmidt-Prietz.

---

*More EU regulatory skills (GDPR, EU AI Act, Data Act, NIS2, and more) →
[github.com/oliverschmidtprietz](https://github.com/oliverschmidtprietz)*

## Liability

This skill is provided **"as is" under the Apache License 2.0** — without warranties of any kind, and subject to the limitation of liability in §§ 7–8 of that license. It is not legal advice and creates no attorney–client relationship. To the fullest extent permitted by law, the author (Oliver Schmidt-Prietz, Rechtsanwalt, Germany) accepts no liability for any use of, or reliance on, this skill or its output; users use it at their own responsibility and are solely responsible for validating results and for their own compliance decisions.
