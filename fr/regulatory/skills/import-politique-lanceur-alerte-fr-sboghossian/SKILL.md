---
name: import-politique-lanceur-alerte-fr-sboghossian
title: 'Import: Politique Lanceur d''Alerte (France)'
description: Use when migrating a French whistleblower policy (politique lanceur d'alerte) drafting or review skill into the mini-claude-for-legal format. The adapter maps French Sapin II and Waserman Law compliance logic — mandatory alert channels, protected-person scope, investigation procedures, and anti-retaliation obligations — into the standard skill model. Primary jurisdiction France; also relevant for EU Whistleblower Directive transposition in other member states and Lebanese corporate-governance best practice.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/import/import-politique-lanceur-alerte-fr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: regulatory
language: fr
---

# Import: Politique Lanceur d'Alerte (France)

## What it does

This import adapter migrates a **French whistleblower policy (politique lanceur d'alerte) skill** into the `mini-claude-for-legal` standard format. French whistleblower law is among the most developed in Europe: the Sapin II Law (Loi n° 2016-1691 du 9 décembre 2016) and the subsequent Waserman Law (Loi n° 2022-401 du 21 mars 2022, transposing the EU Whistleblower Directive) impose mandatory obligations on companies with 50 or more employees to establish a secure, confidential internal alert channel.

Non-compliance can result in criminal liability for the responsible officer and reputational damage. Critically, any whistleblower who faces retaliation has specific protected-person status and can obtain reinstatement, damages, and criminal sanctions against the retaliating employer.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `policy_type` | Legacy `type` | `politique_lanceur_alerte` |
| `entity_size` | Legacy `employees` | `50+` (triggers mandatory obligation) |
| `channel_type` | Legacy `channel` | `internal_and_external` |
| `referent_alerte` | Legacy `referent` | Required — prompt user if absent |
| `investigation_procedure` | Legacy `procedure` boolean | `true` |
| `anti_retaliation_clause` | Legacy `anti_retaliation` boolean | `true` |
| `confidentiality_guarantee` | Legacy `confidentiality` boolean | `true` |
| `language` | Legacy `lang` | `fr` |
| `output_format` | Legacy `format` | `full_policy_fr` |

## Dry-run preview

```
IMPORT PREVIEW — politique-lanceur-alerte-FR
Source shape         : French whistleblower policy template
Entity size          : 50+ employees (mandatory channel required)
Channel              : internal + external (Waserman Law)
Référent alerte      : [requires user input]
Investigation        : mandatory procedure enabled
Anti-retaliation     : enabled
Confidentiality      : enabled
Language             : French
Output               : full_policy_fr
```

## Legal framework (post-import context)

### Sapin II Law (2016)
- Applies to entities with 50+ employees (public and private)
- Required: internal alert channel, confidential procedure, referent désigné
- Whistleblower definition: person who discloses, in good faith, a crime, misdemeanour, threat to general interest, violation of law or regulation, or international commitment

### Waserman Law (2022) — EU Directive transposition
Key expansions over Sapin II:
- **Extended protection**: protects not only the whistleblower but also facilitators, colleagues, and relatives who may suffer retaliation
- **External channel mandatory**: must inform employees of both internal and external channels (Défenseur des Droits, sectoral authorities)
- **Confidentiality reinforced**: identity of the whistleblower must be kept strictly confidential throughout; violation is a criminal offence
- **Broader scope**: now includes violations of EU law in addition to French law
- **Dedicated referent**: companies must designate a referent with specific training and independence guarantees

## Mandatory policy content

### 1. Scope and purpose
- Who can use the alert channel (employees, suppliers, subcontractors, shareholders)
- What can be reported (violations of law, ethical breaches, threats to general interest)

### 2. Alert channels
- **Internal**: dedicated secure email, secure web form, or physical address; must be separate from normal HR channels
- **External**: reference to external channels (Défenseur des Droits, AFA for anti-corruption, financial regulator, etc.)
- **Protection of anonymity**: option for anonymous reporting must be offered; policy must explain how anonymity is preserved

### 3. Investigation procedure
- [ ] Acknowledgement of receipt within 7 days
- [ ] Investigation timeline: outcome communicated to alertant within 3 months (or extended with justification)
- [ ] Who conducts the investigation: referent alerte (first instance); escalation path to audit committee or external body
- [ ] Separation of investigation from persons implicated

### 4. Confidentiality guarantees
- [ ] Identity of the alertant is confidential — cannot be disclosed without consent except when legally required
- [ ] Identity of the implicated person is confidential pending investigation
- [ ] Information gathered during investigation is confidential

### 5. Anti-retaliation protections
- [ ] Prohibition on all forms of retaliation: dismissal, demotion, harassment, exclusion
- [ ] Reinstatement right: courts can order reinstatement with back pay
- [ ] Shift of burden: employer must demonstrate any adverse action was unrelated to the alert
- [ ] Criminal penalties: 1 year imprisonment + €15,000 fine for obstruction of alert procedure (Sapin II Art 13)

### 6. Data protection compliance
- Alert system processes personal data → GDPR Article 13/14 notice required → reference to GDPR rights
- Retention: limited; CNIL recommends deletion of alert data that does not lead to investigation within 2 months
- Impact assessment (DPIA) recommended for alert processing systems

## Common import issues

| Issue | Resolution |
|---|---|
| No référent designated | Flag HIGH risk; mandatory under Waserman Law |
| Anonymous reporting not offered | Flag MEDIUM risk; Waserman Law strongly encourages |
| Investigation timeline missing | Flag HIGH risk; 3-month response timeline is mandatory |
| Anti-retaliation clause too generic | Flag; must enumerate specific prohibited acts |
| GDPR compliance of alert system not addressed | Flag; add DPIA reference and data-retention limits |

## Related skills

- [[import-politique-confidentialite-fr]]
- [[import-politique-cookies-fr]]
- [[import-gdpr-privacy-notice-eu]]
- [[kb-employment-law-fr]]
- [[import-notification-licenciement]]
