# NIS2 Compliance Navigator

Scope classification, Art. 21 gap analysis, and a prioritized compliance roadmap under **EU Directive
2022/2555 (NIS2)** — with deep German **BSIG-neu** coverage and high-level profiles for Italy, France,
the Netherlands, Austria, and Spain.

## When to use

Reach for this skill when someone asks whether NIS2 applies to an organisation, whether they are an
**essential** or **important** entity, what their **Art. 21** risk-management obligations are, how to
run a NIS2 gap analysis or readiness assessment, or about German **BSI registration** / **§ 30 BSIG**
obligations. It also handles the common "a customer sent us a NIS2 contract clause — are we actually
in scope?" question.

## How it works

A three-phase assessment:

1. **Scope & classification** — Annex I / II sector mapping + size test → essential / important /
   out-of-scope, with DORA and CIR 2024/2690 checks and (for Germany) BSI registration status.
2. **Art. 21 gap analysis** — 0–4 maturity scoring across the 10 risk-management measures, with
   ISO 27001:2022 cross-references so existing controls are credited rather than re-done.
3. **Compliance roadmap** — priority-sequenced remediation (P1/P2/P3) plus an Art. 20 / § 38 BSIG
   management-body briefing (including German personal-liability exposure).

The output is a consolidated, audit-ready assessment report.

## Worked example

See [`examples/nis2-navigator-worked-example.md`](examples/nis2-navigator-worked-example.md) for a
full end-to-end run on a German managed-service provider (scope → gap analysis → roadmap → report).

## Reference material

Substantive depth lives in [`references/`](references/) and is loaded on demand:

| File | Contents |
|---|---|
| `sector-classification.md` | Annex I / II sector taxonomy + entity-size thresholds |
| `art21-measures.md` | The 10 risk-management measures (Art. 21(2)(a)–(j)) + scoring criteria |
| `germany-nis2umsucg.md` | § 28 / § 30 / § 38 BSIG-neu, NIS2UmsuCG, BSI registration |
| `eu-jurisdiction-profiles.md` | IT / FR / NL / AT / ES — entity taxonomy + supervisory authorities |
| `regulatory-sources.md` | Official EU + Member-State source catalog |
| `templates.md` | Output templates (gap analysis, roadmap, management briefing) |

## Installation

Copy the `nis2-navigator/` folder into your skills directory (e.g. `~/.claude/skills/nis2-navigator/`
for Claude Code, or upload the folder under Custom Skills on claude.ai). The skill auto-triggers on
"NIS2", "BSIG", "BSIG-neu", "NIS2UmsuCG", "essential/important entity", "Annex I/II", or
"Art. 21 gap analysis".

## Limitations

This skill provides **structured compliance guidance, not legal advice**, and does not certify
compliance or replace a security audit. NIS2 is a self-assessment regime — the entity remains
responsible for its own classification. Germany is covered in depth; other Member-State profiles are
high-level and several transpositions are still evolving, so verify current status and involve
qualified local counsel. See the **"What this skill does not do"** section in `SKILL.md` for the full
scope boundary.

## License

Apache-2.0 — see [LICENSE](LICENSE). Authored by Oliver Schmidt-Prietz.

---

*More EU regulatory skills (GDPR, EU AI Act, Data Act, NIS2, and more) →
[github.com/oliverschmidtprietz](https://github.com/oliverschmidtprietz)*

## Liability

This skill is provided **"as is" under the Apache License 2.0** — without warranties of any kind, and subject to the limitation of liability in §§ 7–8 of that license. It is not legal advice and creates no attorney–client relationship. To the fullest extent permitted by law, the author (Oliver Schmidt-Prietz, Rechtsanwalt, Germany) accepts no liability for any use of, or reliance on, this skill or its output; users use it at their own responsibility and are solely responsible for validating results and for their own compliance decisions.
