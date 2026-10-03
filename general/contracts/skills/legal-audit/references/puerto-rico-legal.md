# Puerto Rico Legal Reference — Audit Detail

Puerto Rico operates under a hybrid civil/common law system. For customer-facing legal text targeting PR consumers (or where the operator is PR-domiciled and serves PR), apply the following layered analysis.

## Core consumer protection statutes

### Ley Núm. 5 de 23 de abril de 1973 — Ley Orgánica del Departamento de Asuntos del Consumidor (DACO)
- Establishes DACO as primary consumer-protection regulator.
- Empowers DACO to issue regulations covering refunds, warranties, advertising, debt collection, condominium law, telecom, etc.
- Audit hook: refund/cancellation policy MUST reference the consumer's right to file a DACO complaint as an alternative to (not a substitute for) any arbitration clause.

### Ley Núm. 5 de 27 de septiembre de 1985 — Ley para Reglamentar el Negocio de Garantías
- Governs warranty disclosures.
- Combined with DACO's **Reglamento de Garantías de Servicios Núm. 8540** (2015) requires:
  - Written warranty terms in Spanish
  - Specific disclosure of duration, scope, exclusions
  - Right to repair, replace, or refund within 30 days for "major defects"

### Reglamento de Competencia Justa Núm. 7757 (DACO)
- Prohibits unfair/deceptive practices broadly. Functional analog to FTC Act Section 5 at state level.

### Ley Núm. 247 de 18 de septiembre de 2012 — Ley para Regular las Empresas de Información sobre el Crédito de Consumidores
- Credit-reporting analogue to FCRA. Notice requirements for any service touching credit data.

### Ley Núm. 75 de 24 de junio de 1964 — Dealer's Contracts Act
- Not customer-facing per se but worth flagging in B2B terms targeting PR distributors. Heavily favors PR dealers; cannot be waived. Often relevant for SaaS reseller agreements.

## Privacy and data protection

PR does NOT have a single comprehensive consumer privacy statute analogous to CCPA. Instead, several sectoral laws apply:

- **Ley Núm. 111 de 7 de septiembre de 2005** ("Ley de Información al Ciudadano sobre la Seguridad de Bancos de Información"): security breach notification. Notification "as soon as possible" to affected residents and to DACO.
- **Constitución de Puerto Rico, Art. II §8:** right to privacy and "intimacy" — frequently cited in privacy litigation, broader than US 4th Amendment.
- **Ley Núm. 39 de 2012** for student data + various sectoral health (Carta de Derechos del Paciente — Ley 194 de 2000).
- **HIPAA applies in PR** as a US territory; PR Department of Health adds its own regs for PHI handling.

**Audit shortcut:** A privacy policy that doesn't reference Ley 111 breach notification when collecting PR resident data is a Major finding.

## Spanish-language requirements

- **Ley Núm. 5 + DACO Reglamento 8540** require warranty terms in Spanish for consumer products sold in PR.
- **Ley Núm. 1 de 1993** (Ley para Establecer el Idioma Español como Idioma Oficial): Spanish is co-official; government-facing documents in Spanish; no general statutory requirement for purely commercial websites.
- **Practical audit standard:** for PR-targeted consumer offerings, provide a Spanish-language version of (a) refund/warranty policy, (b) privacy notice, (c) terms acceptance UI. Critical if absent and the offering is consumer-facing in PR.

## DACO complaint mechanism — required disclosure pattern

Recommended clause for PR-targeted consumer terms:

> "Los consumidores en Puerto Rico tienen derecho a presentar una querella ante el Departamento de Asuntos del Consumidor (DACO), Apartado 41059, San Juan, PR 00940-1059, teléfono (787) 722-7555. La presentación de una querella ante DACO no renuncia a ningún otro derecho disponible bajo esta política o la ley aplicable."

Audit finding template if missing: "Refund/cancellation policy lacks DACO complaint mechanism disclosure required by Ley Núm. 5 enforcement practice. Major finding."

## Tax incentive disclosures (Acts 60/20/22 contexts)

If the operator is a PR-domiciled entity availing of Act 60 incentives and serves both PR and non-PR consumers:

- Disclose entity's PR domicile in terms (governing law clause).
- Be careful with class-action waivers — PR Civil Code Art. 1208 limits enforceability of waivers contrary to public order.
- Arbitration clauses: enforceable under FAA but DACO retains primary jurisdiction over consumer complaints; arbitration cannot strip DACO jurisdiction.

## Governing law / venue

For PR-domiciled operators:
- Default governing law: laws of the Commonwealth of Puerto Rico.
- Default venue: Court of First Instance, San Juan Part (Tribunal de Primera Instancia, Sala Superior de San Juan), unless DACO has primary jurisdiction.
- Federal claims: US District Court for the District of Puerto Rico.

For non-PR operators serving PR consumers:
- Cannot waive PR consumer protections via choice-of-law clause for PR-resident consumers (Restatement § 187(2)(b) public-policy override; PR courts have been consistent).
- Audit finding template: "Choice-of-law clause selects [state] without preserving PR consumer's rights under Ley 5; Major finding for the segment of PR consumers."

## PR-specific audit checklist (plug-and-play)

1. [ ] Refund/cancellation policy references Ley Núm. 5 / DACO mechanism
2. [ ] Warranty disclosures comply with Reglamento 8540 (Spanish, scope, duration)
3. [ ] Spanish-language version available for consumer-facing terms
4. [ ] Breach notification commitment matches Ley 111 timing
5. [ ] Choice-of-law preserves PR consumer rights for PR residents
6. [ ] Arbitration clause does not purport to strip DACO jurisdiction
7. [ ] If healthcare: Carta de Derechos del Paciente referenced
8. [ ] If credit/financial: Ley 247 disclosures present
9. [ ] If B2B with PR dealers: Ley 75 considerations addressed in dealer terms
10. [ ] Constitutional privacy right (Art. II §8) acknowledged where personal data is collected
