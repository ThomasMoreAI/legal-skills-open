---
name: poland-xopoko
title: Poland
description: Poland router. Use when topics cross domains.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: immigration
language: en
---

# Poland

Use this router when a request spans several Poland domains, the correct owner is
unclear, or the user wants an end-to-end newcomer or resident plan. For one clear
domain, use the focused skill directly.

## Route from facts, not assumptions

Collect only facts that can change the route:

1. citizenship group: Polish, EU/EEA/Swiss, third-country, stateless, or
   unknown;
2. current location and legal/status basis, stated in the user's own terms;
3. exact goal and any official deadline or received letter;
4. voivodeship and gmina/city when an office or local procedure matters;
5. work, family, study, or business context only when relevant.

Do not request passport numbers, PESEL, credentials, scans, addresses, or other
identifiers for routing. If a material fact is unknown, keep branches separate.

Resolve `$PLUGIN_ROOT` from the host when provided; otherwise use this skill
folder's `../..`. Use the offline router before broad web searching:

```bash
python3 "$PLUGIN_ROOT/scripts/poland.py" route "<goal>" \
  --citizenship-group <group> --voivodeship <region> --gmina <gmina>
```

## Focused owners

- Stay and temporary residence: `poland-stay-residence`; protection referral:
  `poland-protection-referral`; permanent/long-term status and citizenship:
  `poland-citizenship-long-term`; refusals, delay, and review:
  `poland-appeals-review`.
- EU mobility: `poland-eu-mobility`; PESEL, meldunek, identity, and civil
  records: `poland-identity`.
- Permission to work: `poland-work-authorization`; contracts and workplace
  rights: `poland-employment-rights`; tax: `poland-tax`; ZUS and social
  insurance: `poland-social-insurance`; business/registry: `poland-business`.
- Healthcare: `poland-healthcare`; housing: `poland-housing`; family, schools,
  and universities: `poland-family-education`; benefits and public support:
  `poland-benefits-support`.
- Civil status, birth, marriage, death, funeral, and succession administration:
  `poland-civil-life-events`; disability and accessibility:
  `poland-disability-accessibility`; pensions, senior support, and care:
  `poland-pensions-seniors`.
- Driving and public transport: `poland-transport-driving`; vehicle ownership,
  registration, and road records: `poland-vehicles-road`; consumer, telecom,
  banking, and utility disputes: `poland-consumer-banking`; household utilities,
  waste, and environmental routing: `poland-utilities-environment`.
- Translations and foreign documents: `poland-foreign-documents`; consular and
  cross-border travel administration: `poland-consular-travel`; public
  employment-office and jobseeker services: `poland-employment-services`.
- Courts, free legal aid, ombudsmen, victim support, and procedural ownership:
  `poland-justice-legal-aid`; elections and civic participation:
  `poland-civic-participation`.
- Portals: `poland-digital-government`; office/locality:
  `poland-local-services`; urgent rights: `poland-emergency-rights`.
- Case/deadline ledger: `poland-case-planning`; evidence refresh:
  `poland-source-verification`.

Automation is a shared effect policy, not a substantive owner. For any Browser,
Computer, API, email, calendar, or portal step, apply
`../../references/automation-playbook.md` and the bundled action boundaries
after loading the relevant domain skill. The plugin bundles no authenticated
connector or Browser/Computer adapter; use whichever caller-owned capability is
actually installed and permitted, or guide the user semantically when none is
available. The user handles authentication, secrets, CAPTCHA/2FA, signatures,
attestations, final payment authorization, and irreversible destructive steps.
Minimum personal-record inspection and form filling require explicit task scope;
every consequential external effect requires a fresh visible summary and
action-time confirmation.

For a first-weeks or relocation plan, compose only the applicable focused
owners instead of inventing one universal registration sequence. Start with
urgent safety, stay deadlines, and housing, then branch into identity/local
services, healthcare, work, tax/ZUS, family/education, banking/consumer safety,
driving, and document/language support. Read
`../../references/daily-life-map.md` and
`../../references/life-events-and-services.md` for this composition.

## Output contract

Give the user: known facts; material unknowns; the competent authority and
official source links; a phased checklist; which steps vary locally; which facts
must be rechecked and when; the next smallest action; and the manual fallback if
the host lacks a suitable tool. Label drafts as drafts. Report an external action
as complete only when a visible official receipt or unambiguous final state is
present. Never present navigation as legal, tax, medical, or financial
representation.

Read `../../references/operating-contract.md` for cross-domain work and
`../../references/source-methodology.md` before asserting a changing fact. Read
`../../references/architecture-decisions.md` when changing the plugin's runtime,
data, privacy, Browser, or host-integration boundary.
