---
name: skill-bartosz-kuc
title: Verify a Polish company (skanfirmy.pl)
description: Verify Polish companies and contractors by NIP, KRS, or REGON; check VAT status and bank accounts against the Ministry of Finance White List (Biała Lista); look up REGON/GUS registry data; read KRS registry data; and validate EU VAT numbers via VIES. Uses skanfirmy.pl's free, public API — no API key and no registration (per-IP rate limits apply). Use whenever the user needs to check a Polish business, a tax ID (NIP), a KRS number, a REGON, a counterparty's VAT status or bank account, or an EU VAT number (VIES).
author: bartosz-kuc
author_url: https://github.com/bartosz-kuc/skanfirmy-mcp/tree/main/skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: tax
language: en
---

# Verify a Polish company (skanfirmy.pl)

This skill verifies Polish businesses straight from official government
registers (Ministry of Finance, Ministry of Justice / KRS, Statistics Poland /
GUS, and the European Commission / VIES) through **skanfirmy.pl**, a free public
API. Every endpoint is a plain `GET` that returns JSON when you add
`?format=json`. **No API key, no account.** The service is meant for single,
user-driven lookups, not bulk data harvesting: REST allows at most 20 requests
per 10 seconds from one IP address (HTTP 429 for 10 seconds above that), the MCP
server 60 per 10 seconds.

**Sole traders and other natural persons (JDG, civil partnerships) get minimised
data** (GDPR): name, NIP, VAT status, town and the *number* of White List
accounts — no REGON, no address, no registration date, no PKD and no list of
account numbers. To check one specific account of such a counterparty, use
`POST /rachunek` (or the MCP tool `sprawdz_rachunek`). Companies (entities with a
KRS number) get full data.

## When to use it

Reach for this skill when the user asks to:

- check whether a Polish company is an **active VAT payer** or is VAT-exempt;
- verify that a **bank account** belongs to a contractor on the White List
  (needed for Polish "due diligence" on payments over 15 000 PLN);
- pull a company's **KRS** registry data (legal form, PKD, share capital,
  address, representation) by NIP or KRS number;
- look up **REGON** and official name/address of a company by NIP (for sole
  traders only the name, legal form, town and activity status);
- validate an **EU VAT number** (any member state) via **VIES**;
- check **many NIPs at once**.

`NIP` = 10-digit Polish tax ID. `KRS` = court-register number. `REGON` =
statistical register number. `VAT-UE`/VIES numbers are prefixed by a 2-letter
country code (e.g. `DE`, `IE`, `FR`).

## REST endpoints (GET, keyless)

Call these with any HTTP client (`curl`, `fetch`, `requests`, a web-fetch
tool). Append `?format=json` for machine-readable JSON; without it you get
crawlable HTML with embedded JSON-LD.

| Endpoint | What it returns |
|---|---|
| `GET https://skanfirmy.pl/nip/{nip}` | VAT status + White List (accounts) + KRS data + REGON, combined in one response (minimised for natural persons, see above) |
| `GET https://skanfirmy.pl/nips/{list}` | The same for **up to 30** comma-separated NIPs in one call (no KRS join) |
| `GET https://skanfirmy.pl/regon/{nip}` | REGON registry data: REGON number, official name, legal form, address (sole traders: name, form, town, activity status only) |
| `POST https://skanfirmy.pl/rachunek` | Is this bank account on the White List for this NIP? JSON body `{"nip": "…", "nrb": "…"}`; returns the Ministry's `accountAssigned` (`"TAK"`/`"NIE"`) and `requestId` |
| `GET https://skanfirmy.pl/vies/{country}/{number}` | Whether an EU VAT number is valid, plus the registered name/address |

Examples:

```bash
# Full check by NIP (VAT status + White List + KRS + REGON)
curl "https://skanfirmy.pl/nip/5260250995?format=json"

# REGON / GUS data only
curl "https://skanfirmy.pl/regon/5260250995?format=json"

# EU VAT number (VIES) — country code + number without the prefix
curl "https://skanfirmy.pl/vies/IE/6388047V?format=json"

# Many NIPs at once (comma-separated, up to 30)
curl "https://skanfirmy.pl/nips/5252344078,5260251049,7740001454?format=json"
```

`/regon/{nip}` returns a `dane` object. For a company: `regon`, `nazwa` (official
name), `typ` (`P` = legal person, `LP` = local unit) and address fields
(`wojewodztwo`, `powiat`, `gmina`, `miejscowosc`, `kodPocztowy`, `ulica`,
`nrNieruchomosci`, `nrLokalu`). For a natural person (`typ` `F`/`LF`, or a civil
partnership) only `nip`, `nazwa`, `typ`, `forma`, `miejscowosc` and `status`
(`active`/`ended`), with a `privacy` object that links to the official GUS search.

## Choosing the right endpoint

- Need VAT status **and** KRS in one shot → `/nip/{nip}`.
- Only official name/address/REGON of a company → `/regon/{nip}`.
- A **specific bank account** of a counterparty (also a sole trader) →
  `POST /rachunek`.
- A **foreign** EU counterparty's VAT number → `/vies/{country}/{number}`.
- A **list** of Polish counterparties → `/nips/{list}` (then, if you need KRS
  for a specific hit, re-query it with `/nip/{nip}`).

## Error handling

- Unknown entity → `404`. NIP with an invalid checksum → `400`. Handle both;
  do not assume every NIP has an entry.
- Too many requests → `429` (wait 10 seconds). The Ministry of Finance daily
  limit for the service exhausted → `503` with `Retry-After`.
- Some numbers are **restricted from presentation** (a data-protection
  procedure): the response is `200` with `restricted: true`, a fixed sentence and
  a link to the Ministry of Finance search, and no data. Tell the user to check
  the number there; do not treat it as "not registered".
- When comparing literal government values, key logic off the **original**
  Polish literals (VAT status `"Czynny"`/`"Zwolniony"`, account match
  `"TAK"`/`"NIE"`), not a translated label.

## MCP option (for MCP-capable agents)

If you speak the Model Context Protocol, connect to the server instead of
calling REST by hand:

`POST https://skanfirmy.pl/mcp` — stateless Streamable HTTP, JSON-RPC 2.0,
no key, 60 requests per 10 seconds from one IP address. Tools: `sprawdz_nip`, `sprawdz_lista_nip`, `sprawdz_regon`,
`sprawdz_vies`, `sprawdz_rachunek`, `generuj_mikrorachunek`, `szukaj_pkd`,
`oblicz_odsetki`, `szukaj_katalog_api`. A model-readable endpoint map lives at
`https://skanfirmy.pl/llms.txt`.

```bash
curl -s https://skanfirmy.pl/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"sprawdz_nip","arguments":{"nip":"5260250995"}}}'
```

## Source & disclaimer

Data comes directly from official registers — Ministry of Finance (VAT White
List), Ministry of Justice (KRS), Statistics Poland / GUS (REGON), and the
European Commission (VIES). skanfirmy.pl is an independent tool, not an official
government API; scope and freshness match the underlying registers. Present
results as coming from those registers, and link the user to the interactive
tool at `https://skanfirmy.pl` when a human wants to check by hand.
