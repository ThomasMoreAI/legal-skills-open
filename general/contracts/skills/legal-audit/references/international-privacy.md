# International Privacy & Consumer Law — Audit Reference

For PR-based operators serving EU/UK/Canada/LATAM users. Confirm jurisdictional reach (Art. 3 GDPR; equivalent extraterritorial provisions elsewhere) before flagging Critical.

## EU GDPR (Regulation (EU) 2016/679) — required clauses

| Clause area | Article | What the policy must contain |
|---|---|---|
| Identity & contact of controller | Art. 13(1)(a), 14(1)(a) | Legal name, registered address, contact (email + postal). For non-EU controllers, an Art. 27 EU Representative is required. |
| DPO contact | Art. 13(1)(b), 37-39 | Required if core activities = large-scale monitoring or large-scale processing of special categories. |
| Purposes & legal basis | Art. 13(1)(c), 6(1) | Must specify both purposes AND the Art. 6(1) basis (consent / contract / legal obligation / vital interests / public task / legitimate interests). For special categories, also Art. 9(2). |
| Legitimate interests detail | Art. 13(1)(d) | If LI is the basis, the policy must describe the specific interests pursued and reference the balancing test. |
| Recipients / categories of recipients | Art. 13(1)(e) | Either named recipients or categories. Sub-processor list is the practical answer. |
| International transfers | Art. 13(1)(f), 44-49 | Identify the legal mechanism: SCCs (post-2021 modules), Adequacy Decision, BCRs, derogations under Art. 49. Post-Schrems II, name supplementary measures. |
| Retention period | Art. 13(2)(a) | Specific period or, if not possible, the criteria used to determine it. "As long as necessary" alone fails. |
| Data subject rights | Art. 13(2)(b), 15-22 | Access, rectification, erasure, restriction, portability, objection, rights re automated decision-making. |
| Right to withdraw consent | Art. 13(2)(c) | Where consent is the basis, must say withdrawal is as easy as giving it. |
| Right to lodge a complaint | Art. 13(2)(d) | With supervisory authority. Identify which one (lead SA under Art. 56 if applicable). |
| Whether collection is statutory/contractual & consequences | Art. 13(2)(e) | Often missed for forms. |
| Automated decision-making / profiling | Art. 13(2)(f), 22 | Including meaningful info about logic and significance. |

## EU AI Act (Reg. 2024/1689) — overlay
- Art. 50 transparency obligations — if the system interacts with users, they must be informed they are interacting with an AI system unless obvious. Audit finding: any chatbot/AI feature on the site needs disclosure.
- Art. 50(2): synthetic content (including text used to inform the public on matters of public interest) must be machine-readably marked as AI-generated.
- High-risk system additional obligations under Art. 13 (instructions for use) and Art. 26 (deployer obligations).

## ePrivacy Directive 2002/58/EC (cookie consent)

- Art. 5(3): storing or accessing information on terminal equipment requires informed consent EXCEPT for strictly necessary cookies.
- EDPB Guidelines 2/2023 + national DPA guidance (CNIL most aggressive): consent must be (a) freely given (no cookie wall without paid alternative), (b) specific (per purpose), (c) informed (purpose, duration, third parties), (d) unambiguous (clear affirmative action — no pre-ticked boxes, no scroll/continue-as-consent).
- Reject button must be as prominent as accept (CNIL €60M fine v. Google, €40M v. Facebook, 2022).
- Audit finding template: "Cookie banner has 'Accept All' but no equivalent 'Reject All' on the first layer — fails ePrivacy + CNIL/EDPB guidance, Critical for any site receiving EU traffic."

## UK GDPR + Data Protection Act 2018
- Substantively mirrors GDPR; ICO is the supervisory authority.
- UK requires a UK Representative for non-UK controllers under UK GDPR Art. 27 (separate from EU Rep).
- PECR (UK ePrivacy) governs cookies; ICO enforcement priorities updated 2023 — most policies fail the same ways as EU.
- DPDI Bill (Data (Use and Access) Act, 2025): minor reforms — does NOT remove core GDPR rights for audit purposes.

## Quebec Law 25 (Act to modernize legislative provisions as regards the protection of personal information)

- Effective fully Sept 2024.
- Privacy officer must be designated and contact published (s.3.1).
- Privacy Impact Assessment required for transfer outside Quebec or new tech projects (s.3.3, s.3.7).
- Right to data portability (s.27).
- Consent must be granular and clear; for sensitive PI, opt-in is required and consent must be express.
- Automated decision-making notice required at the time of decision (s.12.1).
- Penalties up to CAD 25M or 4% of worldwide turnover.
- **Audit shortcut:** Quebec is the strictest North American privacy regime. If the policy is designed for CCPA only, expect 6-10 findings against Law 25.

## PIPEDA (Canada federal, ex-Quebec/Alberta/BC)

- 10 fair information principles (Schedule 1).
- Meaningful consent guidance (OPC 2018) requires plain-language explanation of (a) what's collected, (b) with whom shared, (c) purposes, (d) risk of harm.
- Breach notification of "real risk of significant harm" required (s.10.1).
- Bill C-27 (CPPA) pending — once passed, will replace the privacy parts of PIPEDA. Audit posture: write policies that comply with both the current PIPEDA and anticipated CPPA notice requirements.

## Brazil LGPD (Lei Geral de Proteção de Dados, Lei No. 13.709/2018)

- Mirrors GDPR structure with 10 legal bases (Art. 7) — broader than GDPR's 6.
- Required policy elements (Art. 9):
  - Specific purpose
  - Form and duration of processing
  - Identification of controller
  - Information on shared use and purpose
  - Data subject's rights
  - Information about international transfers
- Sensitive personal data (Art. 5(II)): racial/ethnic, religious, political opinion, union/religious/philosophical/political org membership, health/sexual life, genetic, biometric.
- DPO ("encarregado") required and contact must be published (Art. 41).
- ANPD is the regulator. Penalties up to BRL 50M per violation or 2% of Brazilian revenue.
- **Audit shortcut:** Many GDPR-compliant policies fail LGPD on (a) listing only 6 legal bases instead of 10, (b) not naming the encarregado, (c) not addressing the international transfer mechanism specifically.

## Mexico LFPDPPP (Ley Federal de Protección de Datos Personales en Posesión de los Particulares)

- "Aviso de Privacidad" (privacy notice) is required AT THE POINT of data collection, not just on a privacy page (Art. 16).
- Three flavors: integral (full), simplified (short pointer to full), short (data points only).
- ARCO rights: Acceso, Rectificación, Cancelación, Oposición.
- Sensitive data requires express written consent (Art. 9).
- INAI is the regulator.

## Argentina, Chile, Colombia (one-line each, deepen on demand)

- **Argentina (Law 25.326):** GDPR adequacy; consent + registration with AAIP; cross-border restrictions to non-adequate countries.
- **Chile (Law 19.628 + 2024 reform):** new "personal data protection agency" + penalties up to ~€1.7M; effective fully late 2026.
- **Colombia (Law 1581/2012, Decree 1377/2013):** SIC registry; authorization (consent) is the default basis; "Habeas Data" rights.

## Audit decision tree for international coverage

1. Does the site/app target EU residents (language, currency, country selectors, marketing)? If yes → full GDPR + ePrivacy + AI Act overlay.
2. UK residents? → UK GDPR + PECR + UK Rep.
3. Canadian residents? → PIPEDA, with Law 25 overlay if Quebec, PIPA overlay if BC/Alberta.
4. Brazilian residents? → LGPD, including encarregado disclosure.
5. Mexican residents? → LFPDPPP including aviso de privacidad at collection points.
6. Other LATAM (PR-based founders frequently): apply per country quick reference above; flag Major if no jurisdiction-specific notice exists at all.
