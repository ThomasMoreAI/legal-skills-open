# Practice profile: Technology, Media & Telecom — Cross-jurisdiction

Orchestrator cold-start for plugin `cross-jurisdiction-tmt`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Digital media and online-content law compared across the US and the EU/UK: copyright and its online enforcement, intermediary/platform liability and safe harbours, user-generated content, and the privacy overlay on media services. The US and EU approaches diverge sharply (notice-and-takedown vs. notice-and-action; broad publisher immunity vs. conditional hosting defence) — never state a single combined rule.

## Forums & authorities

US federal courts and the Copyright Office; in the EU/UK, national courts, the CJEU on Union instruments, and national data-protection and media regulators.

## Key sources of law

- **US copyright safe harbour:** DMCA, 17 U.S.C. § 512 (notice-and-takedown).
- **US intermediary immunity:** Section 230 of the Communications Decency Act, 47 U.S.C. § 230.
- **EU intermediary liability:** the hosting defence (formerly Art. 14 of the e-Commerce Directive 2000/31/EC, now Art. 6 of the Digital Services Act, Regulation (EU) 2022/2065) — verify which instrument governs the period in question.
- **Privacy overlay:** Regulation (EU) 2016/679 (GDPR); in the US, the California Consumer Privacy Act (CCPA, Cal. Civ. Code § 1798.100 ff.).

Attribute each rule to its jurisdiction. See `cross-jurisdiction/CLAUDE.md` for the jurisdiction guardrail.

## Citation discipline

Follow the rules in `cross-jurisdiction/CLAUDE.md`. Cite US law as "17 U.S.C. § 512" / "47 U.S.C. § 230", EU instruments in EU form. The e-Commerce Directive's hosting safe harbour has been superseded by the DSA — do not cite the repealed article as current. **Never invent** section numbers or case names.

## When this plugin does NOT apply

- A single jurisdiction's media/telecom or copyright law → that jurisdiction's `tmt` or `ip`
- Pure data-protection compliance → `data-protection`
- Registered-IP prosecution (trademarks, designs) → `ip`

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
