# RIS Verification Protocol

> **Every skill that cites Austrian statutes or case law MUST follow this protocol.**
> This is not optional. Unverified citations erode trust and may be wrong.

---

## When This Protocol Applies

This protocol applies whenever you:
- Cite a specific § (e.g., §922 ABGB)
- Quote statute text
- Reference an OGH/VfGH/VwGH decision
- State a GGG fee or RATG rate
- Claim a limitation period (Verjährungsfrist)
- Reference a BGBl amendment
- State current procedural rules or deadlines

---

## Verification Workflow

### Step 1: Classify the Source Type

Before looking anything up, determine what you need:

| Type | RIS Tool | Example |
|------|----------|---------|
| **Statute text** (Bundesnorm) | `search_bundesnormen` | §922 ABGB current wording |
| **State law** (Landesnorm) | `search_landesnormen` | Wiener BauO §60 |
| **OGH case law** | `search_justiz` | OGH 4 Ob 123/21k |
| **VfGH decision** | `search_justiz` | VfGH G 212/2021 |
| **VwGH decision** | `search_justiz` | VwGH Ra 2021/09/0123 |
| **BGBl amendment** | `search_bgbl` | BGBl I 2023/xxx |
| **Fee/tariff table** | `search_bundesnormen` | GGG Tarifpost, RATG §1 |

### Step 2: Query RIS

**If RIS MCP Server is connected:**

1. Use the appropriate RIS tool from the table above
2. Search with specific terms: statute abbreviation + section number, or Geschäftszahl
3. Read the returned text carefully — verify it matches what you intend to cite
4. Note the Fassung (version) date — is this the current consolidated version?
5. If the result is ambiguous or incomplete, refine the search

**Query patterns:**
- For statutes: search the Kurztitel (e.g., "ABGB") and navigate to the specific §
- For case law: search by Geschäftszahl if known, or by legal concept + statute
- For amendments: search BGBl by year and number

### Step 3: Assign Verification Status

After each lookup attempt, assign ONE of these statuses:

| Status | Meaning | When to Use |
|--------|---------|-------------|
| `RIS_VERIFIED` | Text confirmed via RIS MCP | RIS returned the exact provision/decision |
| `OFFICIAL_WEB_VERIFIED` | Confirmed via ris.bka.gv.at web | RIS MCP unavailable, but verified via web search on official RIS site |
| `SECONDARY_SOURCE_ONLY` | Found in non-official source | Only found via general web search, legal commentary, or textbook |
| `UNVERIFIED` | Not verified at all | Could not verify — relying on training data |

### Step 4: Apply Verification Rules

| Verification Level | What You May Do |
|--------------------|-----------------| 
| `RIS_VERIFIED` | Cite freely, quote text, state as current law |
| `OFFICIAL_WEB_VERIFIED` | Cite freely, note "verified via ris.bka.gv.at" |
| `SECONDARY_SOURCE_ONLY` | Cite with caveat: "Laut Sekundärquelle; RIS-Überprüfung empfohlen" |
| `UNVERIFIED` | Cite with explicit warning: "⚠️ Nicht RIS-verifiziert — Aktualität bitte prüfen" |

**Hard rules:**
- Never silently mix verified and unverified citations
- Never quote statute text as current if status is `UNVERIFIED`
- Never state a GGG fee amount without verification — tables change
- Never present an OGH decision without its Geschäftszahl

---

## Fallback Ladder

When RIS MCP is NOT connected, follow this order. Stop at the first successful level:

```
Level 1: RIS MCP Server (philrox/ris-mcp-ts)
    ↓ unavailable
Level 2: Web search on ris.bka.gv.at directly
    ↓ no result
Level 3: Official court/government pages (ogh.gv.at, vfgh.gv.at, bmj.gv.at)
    ↓ no result
Level 4: Established legal databases (LexisNexis AT, RDB.at)
    ↓ no result
Level 5: General web search (flag as SECONDARY_SOURCE_ONLY)
    ↓ no result
Level 6: Training data only (flag as UNVERIFIED)
```

**At every level:** record which source you used and attach the verification status.

---

## RIS MCP Connection Check

At the start of every `/recht` command, check RIS availability:

1. Attempt a simple RIS query (e.g., search for "ABGB" in Bundesnormen)
2. If it succeeds → RIS is available, use it throughout
3. If it fails or times out → RIS is unavailable, use fallback ladder
4. Log the status for the Quellenstatus output block

---

## Quellenstatus Output Block

**Every skill output MUST end with this block** (before the disclaimer):

```markdown
## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

⚠️ Bei Status UNVERIFIED: Aktualität der zitierten Normen bitte selbst auf ris.bka.gv.at prüfen.
```

---

## OGH Case Law Lookup

When a skill requires case law (especially `/recht claim` and `/recht strategy`):

1. **Identify the legal issue** — what doctrine/statute is in dispute?
2. **Search RIS Justiz** — use the legal concept as search term, filter by OGH
3. **Select 3-5 high-signal decisions** — prefer:
   - Leitentscheidungen (leading cases) over isolated rulings
   - Recent decisions over old ones (but classic leading cases are fine)
   - Verstärkter Senat or Großer Senat decisions (highest authority)
4. **Present using the OGH case presentation format** — see `references/ogh-case-presentation.md`

---

## Amendment Detection

When verifying a statute:

1. Check the Fassung (version) — when was this consolidated version published?
2. If the Fassung is older than 12 months, search BGBl for recent amendments
3. If an amendment is found:
   - Note it explicitly: "§922 ABGB idF BGBl I 2025/xxx"
   - If the amendment changes the cited provision, use the NEW text
   - Flag for the user: "Hinweis: Diese Bestimmung wurde zuletzt mit BGBl I [year]/[nr] geändert"
4. For transitional provisions (Übergangsbestimmungen), check if the old or new version applies to the user's situation

---

## Integration into Skills

Every skill file should include this mandatory step early in its procedure:

```markdown
## Step [X]: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations
```

And every skill output template should include the Quellenstatus block before the disclaimer.
