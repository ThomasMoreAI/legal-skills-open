---
name: draft-articles-of-association-sboghossian
title: Draft — Articles of Association
description: Use when asked to draft or review Articles of Association (also called a Memorandum of Association, Company Charter, or Statuts in civil-law systems) for a company being incorporated or restructured. Covers the essential provisions — company name, objects, share capital, share classes, transfer restrictions, board structure, and shareholder meeting procedures — with jurisdiction-specific notes for UAE, KSA, Lebanon, Egypt, DIFC, and ADGM.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-articles-of-association
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Draft — Articles of Association

## When to use this

Use this skill to produce the constitutional document for a new company or to amend the constitutional document of an existing company. The Articles of Association (AoA) — variously called Memorandum and Articles (UK), Statuts (French/Lebanese), Nizam Asasi (Arabic) — is the primary governance document that:
- Creates the company.
- Defines the rights of shareholders.
- Governs the board and its powers.
- Controls how shares are issued and transferred.

In civil-law jurisdictions (Lebanon, KSA, UAE onshore), the AoA is a public document filed with the commercial registrar, typically notarized, and accessible to third parties. In common-law jurisdictions (DIFC, ADGM, UK), the memorandum and articles are filed with the registry.

## Required inputs

| Input | Notes |
|---|---|
| Company name | Full legal name; must be cleared for availability with the registrar |
| Jurisdiction and entity type | UAE LLC / KSA Limited Liability Company / LB SAL / DIFC Company Ltd / ADGM Company Ltd |
| Registered office address | Physical address in jurisdiction; registered agent for some free zones |
| Objects clause | Business purpose — broad vs narrow; see note below |
| Share capital | Total authorized capital; par value per share (if applicable) |
| Share classes | Ordinary, preference, redeemable; rights per class |
| Initial shareholders | Names, nationalities, number/class of shares |
| Director structure | Number, appointment mechanism, term |
| Governing law | Usually the law of the jurisdiction of incorporation |

## Optional inputs

- Pre-emption rights mechanism (right of first refusal on transfer)
- Drag-along and tag-along provisions (especially for VC-backed companies)
- Reserved matters requiring supermajority
- Dividend policy
- Quorum and voting thresholds for shareholder meetings
- Deadlock resolution mechanism (for 50/50 JVs)

## Document structure

### Part 1 — Preliminary
1. **Company name** — including legal form suffix (LLC, PLC, SAL, Ltd).
2. **Registered office** — jurisdiction and address (or registered agent reference for free zones).
3. **Objects** — see note on objects clauses.
4. **Liability** — members' liability limited to their share capital contribution.
5. **Authorized capital** — total share capital; currency; par value.

### Part 2 — Shares
6. **Share classes** — rights attaching to each class: voting, dividend, liquidation preference.
7. **Issuance of shares** — board authority to issue new shares within authorized capital; shareholder approval for issuance beyond authorized capital.
8. **Pre-emption rights** — existing shareholders' right of first offer on new issuances and on transfers.
9. **Transfer restrictions** — approval mechanism for transfers; prohibited transferees (competitors, etc.).
10. **Drag-along** — majority shareholders' right to require minority to sell in an approved exit.
11. **Tag-along** — minority shareholders' right to join a majority sale on same terms.
12. **Share certificates** (if applicable).

### Part 3 — Directors and officers
13. **Board composition** — minimum and maximum number; any class-based nomination rights.
14. **Appointment and removal** — by shareholders in general meeting; by specific shareholder classes.
15. **Term** — fixed term or until removed.
16. **Powers of the board** — general management authority; reserved matters requiring shareholder approval.
17. **Board meetings** — notice, quorum, voting, minutes.
18. **Officers** — CEO, CFO, Secretary; appointment by board; powers.
19. **Conflicts of interest** — disclosure obligation; exclusion from vote.
20. **Indemnification** — scope and limitations.

### Part 4 — Shareholder meetings
21. **Annual General Meeting** — timing, notice period, quorum.
22. **Extraordinary General Meeting** — triggers; who may convene.
23. **Notice** — period (minimum varies by jurisdiction); content requirements.
24. **Quorum** — first call vs second call (civil-law jurisdictions typically have two-call mechanics).
25. **Voting** — show of hands vs poll; proxy rights; written resolutions.
26. **Supermajority matters** — items requiring 75% or higher approval (capital reduction, material asset sale, amendment of articles, liquidation).

### Part 5 — Financial provisions
27. **Financial year** — calendar year or specified.
28. **Auditors** — appointment; mandatory audit threshold.
29. **Dividends** — board recommendation; shareholder approval; payment mechanics.
30. **Reserves** — statutory reserve (mandatory in most MENA jurisdictions).

### Part 6 — Winding up
31. **Voluntary dissolution** — shareholder vote threshold.
32. **Liquidator appointment**.
33. **Distribution of assets** — after liabilities settled; per class rights.

## Jurisdictional notes

### UAE (Federal Decree-Law 32/2021 on Commercial Companies)
- **LLC**: minimum 1 shareholder; maximum 50; no minimum capital (previously AED 150,000); no requirement for UAE national partner in most sectors (significant liberalization post-2020).
- **Mandatory statutory reserve**: 10% of annual net profit until reserve equals 50% of paid-up capital.
- **Objects clause**: can be broad; must not violate licensed activities.
- **Language**: Arabic AoA required for onshore LLCs; dual language (Arabic + English) common; Arabic controls.
- **Filing**: notarized and filed with the relevant DED (economic department) or free-zone authority.
- **PJSC** (public joint stock company): minimum 5 founders; minimum AED 30 million capital; more rigorous governance requirements.

### UAE Free Zones (DIFC / ADGM)
- English-language AoA.
- DIFC: DIFC Companies Law (DIFC Law 5/2018); DIFC Registrar of Companies.
- ADGM: ADGM Companies Regulations 2020; ADGM Registration Authority.
- Common-law principles govern interpretation; English-style articles acceptable.

### KSA (Companies Law — Royal Decree M/132 2022)
- **LLC**: minimum 1 shareholder; minimum capital SAR 500 for single-member, no minimum for multi-member (recent reform).
- **Arabic** is the required language; English translation for international parties.
- **Notarization**: AoA must be notarized and registered with Ministry of Commerce (Mawthq platform).
- **Sharia compliance**: objects clause must not include prohibited activities; certain financial structures require Islamic finance structuring.
- **Foreign ownership**: generally 100% foreign ownership now permitted in most sectors under Vision 2030 reforms; sector-specific restrictions remain.

### Lebanon (SAL — Société Anonyme Libanaise / SARL)
- **SAL**: minimum 3 founders for formation; minimum capital LBP (amount periodically updated; effectively modest in USD terms).
- **Statuts**: in Arabic and French (or Arabic alone); filed with the Commercial Register.
- **Notarization**: required for SAL formation; notary fees significant.
- **SARL** (limited liability): fewer formalities; single-member possible; maximum 20 members.
- **Mandatory legal reserve**: 10% of annual profits until reserve = 50% of capital.

### Egypt (Companies Law — Law 159/1981 and Investment Law 72/2017)
- SAE (Société Anonyme) and LLC (LLC under Law 159/1981).
- Minimum capital requirements vary by sector.
- Notarization and filing with GAFI (General Authority for Investment and Free Zones) or commercial register.
- Arabic required; English translation acceptable alongside.

## Objects clause — drafting note

**Broad objects clause** (preferred for most commercial companies): covers all lawful commercial activities; maximum flexibility. Common in common-law jurisdictions: "The Company may carry on any lawful business or activity."

**Narrow objects clause** (required in some regulated contexts or by local law): lists specific activities. Common in UAE/KSA where the license specifies the permitted activity and the AoA must mirror it.

**Risk of narrow objects**: any activity outside the stated objects is *ultra vires* — legally beyond the company's capacity. Err on the side of breadth.

## Common mistakes

- **Objects too narrow**: company outgrows its objects and cannot contract for new activities without an AoA amendment.
- **Missing pre-emption rights**: without them, a shareholder can transfer to any third party; important for closely-held companies.
- **No supermajority for material decisions**: if articles are silent, ordinary majority controls everything — including diluting minority shareholders.
- **Statutory reserve omitted**: mandatory in UAE, KSA, LB, EG; failure to include does not invalidate AoA but creates regulatory non-compliance.
- **Conflict between AoA and shareholders' agreement**: these must be read together; inconsistencies create legal uncertainty. Always review the SHA when drafting AoA.

## Related skills

- [[draft-bylaws]]
- [[draft-board-resolution]]
- [[draft-agm-minutes]]
- [[draft-cap-table-resolution]]
- [[draft-bilingual-ar-en-side-by-side]]
