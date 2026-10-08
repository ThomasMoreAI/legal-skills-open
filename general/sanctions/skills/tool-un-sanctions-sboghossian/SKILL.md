---
name: tool-un-sanctions-sboghossian
title: UN Consolidated Sanctions List
description: Use as the baseline layer in any sanctions screening workflow. The UN Security Council Consolidated List is the authoritative multilateral sanctions database mirrored by GCC central banks (CBUAE, SAMA, BDL, CBK, CBI, CBO, CBB, QCB) — making it mandatory for all MENA-region transactions. Screens individuals, entities, and vessels against all active UN Security Council sanctions programs. Always pair with OFAC and EU sanctions lists for a complete three-list screen.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-un-sanctions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: sanctions
language: en
---

# UN Consolidated Sanctions List

## What it does

This tool screens counterparties, individuals, vessels, and aircraft against the United Nations Security Council Consolidated List — the authoritative multilateral sanctions database maintained by the UN Security Council Committee pursuant to its resolutions.

The UN list is the **baseline** for any sanctions screening regime. Every GCC central bank directly mirrors the UN Consolidated List:
- CBUAE (UAE Central Bank)
- SAMA (Saudi Central Bank)
- BDL (Banque du Liban — Lebanon)
- CBI (Central Bank of Iraq)
- CBK (Central Bank of Kuwait)
- CBO (Central Bank of Oman)
- CBB (Central Bank of Bahrain)
- QCB (Qatar Central Bank)

Accordingly, entities on the UN list are automatically blocked in all GCC jurisdictions. MENA-region compliance programs that screen only OFAC and EU lists but miss UN designations are non-compliant.

## UN Sanctions Programs

The UN Security Council operates multiple sanctions programs:

| Resolution(s) | Program | Targets | MENA relevance |
|---|---|---|---|
| 1267/1989/2253 | ISIL (Da'esh) and Al-Qaida | Terrorism / ISIS / AQ affiliates | High — active designations across MENA |
| 2140 | Yemen | Houthi leaders, spoilers of peace process | High — active Yemen conflict |
| 1737/1747/1803/2231 | Iran | Nuclear / ballistic missile program | Very high — Iran-adjacent transactions |
| 1718/2270/2321 | DPRK | North Korea | Relevant for shipping / logistics |
| 1970/1973 | Libya | Libya arms embargo, listed individuals | Moderate |
| 1591 | Darfur/Sudan | Sudan-specific individuals | Lower |
| 2374 | Mali | Mali peace process spoilers | Relevant for OHADA / Francophone Africa |
| 2048 | Guinea-Bissau | Coup leaders | Limited MENA relevance |
| Various | Central African Republic | Arms embargo | Limited MENA relevance |
| 1572 | Côte d'Ivoire | (Delisted 2016; watch for residual) | Historical |

For MENA-region transactions, the **ISIL/Al-Qaida list** and **Yemen list** are the highest-priority programs. The Iran program must be cross-referenced with OFAC, which has more comprehensive Iran sanctions.

## Setup / auth

No API key required. The UN publishes its Consolidated List publicly:
- **XML feed**: https://scsanctions.un.org/resources/xml/en/consolidated.xml (updated as designations are added/removed)
- **CSV/spreadsheet**: available on the UN Security Council website
- **RESTful API**: via https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list

The tool maintains a local cached copy refreshed at least daily. For real-time payment screening, the cache should refresh hourly.

| Parameter | Description | Required |
|-----------|-------------|----------|
| `name` | Full name of individual or entity | Conditional |
| `nameAr` | Arabic name (if available) | Conditional |
| `dob` | Date of birth (individual) | Optional — improves accuracy |
| `nationality` | Country code | Optional |
| `imoNumber` | Vessel IMO number (for vessel screening) | Conditional |
| `entityType` | `individual` / `entity` / `vessel` / `aircraft` | Recommended |
| `minScore` | Minimum match score to flag (0–100), default 75 | No |

## Capabilities

### Name screening
```
Input:  {
  name: "Mohammad Hassan Al-Zawahiri",
  nameAr: "محمد حسن الزواهري",
  dob: "1970-01-15",
  nationality: "EG",
  entityType: "individual"
}
Output: {
  hits: [
    {
      unId: "QDi.001",
      name: "ZAWAHIRI, Ayman Mohammed Rabie",
      programs: ["QDi"],
      aliases: [...],
      dob: "1951-06-19",
      nationality: "EG",
      score: 71
    }
  ],
  cleared: true,
  note: "Possible name-only partial match; DOB mismatch reduces confidence"
}
```

### Entity screening
```
Input:  {
  name: "Al-Nusra Finance Ltd",
  entityType: "entity",
  country: "SY"
}
Output: { hits: [...], cleared: false }
```

### Vessel screening
```
Input:  { imoNumber: "9320187", entityType: "vessel" }
Output: { hits: [...], flagState, operator }
```
IMO numbers are matched exactly for vessels. Vessel name matches are fuzzy.

### Bulk screening
For KYC onboarding batches — screen a list of counterparties in a single call:
```
Input:  { batch: [{ name, dob, nationality }, ...] }
Output: { results: [{ input, hits, cleared }] }
```

## Match rules

Arabic names present specific matching challenges:

| Challenge | Solution |
|---|---|
| Transliteration variants | Muhammad / Mohammed / Mohamad / Muhamad all match to "محمد" |
| Definiteness (al-/el-) | "Al-Hassan" and "Hassan" are normalized |
| Kunya / nisba | "Abu Musab" (father of) and "Al-Zarqawi" (from Zarqa) require fuzzy matching |
| Female names with father's name | "Fatima bint Khalid" — split and match each component |
| DOB tolerance | ±2 years (per standard practice for Arabic names where exact DOB is often uncertain) |

## Three-list screening standard

For any commercial transaction, the minimum standard is a three-list screen:

| List | Tool | Covers |
|---|---|---|
| UN Consolidated List | This tool | Mandatory for all GCC transactions; baseline |
| US OFAC SDN List | [[tool-ofac-sanctions]] | Required for any USD payment or US-person nexus |
| EU Sanctions List | tool-eu-sanctions (separate skill) | Required for any EUR payment or EU-person nexus |

Additional lists for specific sectors:
- UK sanctions (OFSI list) — for UK-person nexus post-Brexit
- FATF grey/black list — country-level risk, not individual designation
- Local AML watchlists — SAMA / CBUAE / BDL internal lists (not public)

## GCC central bank mirror requirement

GCC central banks issue circulars requiring all supervised financial institutions to:
1. Maintain current copies of the UN, OFAC, and EU lists
2. Screen all customers and transactions in real-time or near-real-time
3. Freeze assets of any designated person immediately upon designation
4. Report matches to the relevant FIU (Financial Intelligence Unit)

**SAMA (KSA)**: AML/CTF Law and implementing regulations require list screening at onboarding and on an ongoing basis.

**CBUAE (UAE)**: Cabinet Decision No. 74 of 2020 (on Countering Money Laundering) and CBUAE AML/CFT Standards require financial institutions to screen against the UN list and implement automated transaction monitoring.

**BDL (Lebanon)**: BDL Circular 126 requires banks to maintain and screen against UN, OFAC, and EU lists. Lebanon's FATF-flagged status means enhanced scrutiny from international correspondent banks.

## Output schema

```json
{
  "screeningId": "un-2026-05-14-001",
  "subject": {
    "name": "Mohammad Hassan",
    "dob": "1970-01-15",
    "nationality": "EG"
  },
  "hits": [],
  "cleared": true,
  "programs_checked": ["QDi", "ISTAQi", "Yemen", "Iran", "DPRK", "Libya"],
  "checkDate": "2026-05-14",
  "listVersion": "UN Consolidated List — 2026-05-10",
  "recommendation": "CLEAR — no UN consolidated list match found"
}
```

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Stale list cache | Last refresh > 24 hours | Force refresh before screening |
| XML parse error | Malformed UN list XML | Fall back to CSV; report to admin |
| Common name ambiguity | Multiple high-score hits | Require additional identifiers |
| Arabic name not found | Zero results on Arabic query | Try transliteration variants |
| Vessel flag state unknown | Vessel match without flag data | Cross-reference with IMO ship register |

## Related skills

- [[tool-ofac-sanctions]] — US Treasury OFAC SDN list; always run alongside UN list
- [[tool-ksa-moc]] — Saudi commercial registry for UBO chain verification
- [[tool-lb-commercial-register]] — Lebanon registry for UBO verification
- [[tool-uae-ded]] — UAE DED registry for UAE entity verification
- [[research-beneficial-ownership-lookup]] — UBO tracing to ensure full sanctions coverage
