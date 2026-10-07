# Pan-EU GDPR Privacy Notice Generator

Draft jurisdiction-aware, GDPR-compliant **privacy notices** (Datenschutzerklärung / politique de
confidentialité) as professional **.docx** documents, for any EU/EEA market and audience.

## When to use

Use this skill to create a privacy policy or notice — Art. 13/14 disclosures, cookie/AI-transparency
sections, and audience-specific notices for website/app visitors, **job applicants**, **employees**,
**B2B partners**, or **B2C customers**. It covers DE (DSGVO + BDSG + TDDDG), FR (RGPD + LIL + LCEN),
and AT / IT / ES / NL / BE / IE / UK, including multi-jurisdiction and bilingual notices.

## How it works

A five-step workflow:

1. **Scope** — notice type + jurisdiction(s) + template choice (use the user's base, or generate one).
2. **Intake** — type-driven collection of controller identity, data inventory, purposes/legal bases,
   recipients/transfers, cookies, and AI/automated processing, with DPIA-indicator screening.
3. **Draft** — assemble the notice from the type's **section map** (only relevant sections), with a
   prominent Art. 21 objection box and precise legal-basis citations.
4. **Verify** — Art. 13/14 mandatory-disclosure check + jurisdiction cross-check + type-specific and
   AI Act checks.
5. **Deliver** — formatted **.docx** (A4, numbered headings, purposes/retention + cookie tables, TOC),
   with a Markdown fallback, plus a legal-review and publication checklist.

## Worked example

See [`examples/privacy-notice-eu-worked-example.md`](examples/privacy-notice-eu-worked-example.md) for
a full run on a German e-commerce shop (scope → intake → draft structure → verification → delivery).

## Reference material

Depth lives in [`references/`](references/), loaded on demand: `NOTICE_TYPES.md` (section maps + data
profiles per type), `EU_COMMON.md` (mandatory-disclosures checklist, Art. 9 protocol), `DE.md`, `FR.md`,
`OTHER_EU.md` (jurisdiction specifics + supervisory authorities), and `templates.md` (13-section
structure with DE/FR/EN translations).

## Installation

Copy the `privacy-notice-eu/` folder into your skills directory (e.g.
`~/.claude/skills/privacy-notice-eu/`). It auto-triggers on "privacy notice", "Datenschutzerklärung",
"politique de confidentialité", "Art. 13/14", "Bewerber-/Beschäftigten-Datenschutz", and similar.

## Limitations

This skill provides **drafting assistance, not legal advice**, and does not certify compliance — every
notice must be reviewed by qualified data-protection counsel or a DPO before publication. It does not
draft the Art. 28 DPA, the DPIA, or breach procedures (it flags and hands off), does not fabricate
citations, and does not audit the live site — cookie tables and data flows reflect what the user
reports. Translations are drafting support, not certified legal translation. See the **"What this skill
does not do"** section in `SKILL.md`.

## License

Apache-2.0 — see [LICENSE](LICENSE). Authored by Oliver Schmidt-Prietz.

---

*More EU regulatory skills (GDPR, EU AI Act, Data Act, NIS2, and more) →
[github.com/oliverschmidtprietz](https://github.com/oliverschmidtprietz)*

## Liability

This skill is provided **"as is" under the Apache License 2.0** — without warranties of any kind, and subject to the limitation of liability in §§ 7–8 of that license. It is not legal advice and creates no attorney–client relationship. To the fullest extent permitted by law, the author (Oliver Schmidt-Prietz, Rechtsanwalt, Germany) accepts no liability for any use of, or reliance on, this skill or its output; users use it at their own responsibility and are solely responsible for validating results and for their own compliance decisions.
