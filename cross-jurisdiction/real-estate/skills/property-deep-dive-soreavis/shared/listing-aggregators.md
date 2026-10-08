# Listing Aggregator API Catalog

Per-country listing portal status: API availability, scraping rules, partner-only access, fallback approaches. Supports `--listing=<url>` extraction and `--price` comp lookup.

**Snapshot**: April 2026.

## Universal contract

For each country, return:
1. **Top portal(s)** by listing volume
2. **Public API**: yes / partner-only / no
3. **Scraping rules**: ToS allows? rate limit? user-agent rules?
4. **Headed vs headless**: many CDN-protected portals (Cloudflare, Imperva, DataDome) require headed browser
5. **Fallback**: official cadastre + classifieds aggregator
6. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Listings Profile

**Country**: <ISO2>
**Top portal**: <URL>
**API**: <yes (public) | partner-only | no>
**Scraping**: <ToS-allowed? rate-limit? UA rules?>
**CDN protection**: <Cloudflare / Imperva / DataDome / none>
**Fallback**: <secondary portals + cadastre>
```

---

## Portals with public APIs / open data

| Country | Portal | API | Notes |
|---|---|---|---|
| **ES** | Idealista | **public-ish API** (commercial via Idealista Data) | Commercial subscription via https://www.idealista.com/data; some endpoints free for researchers |
| **DE** | ImmoScout24 | partner API only | https://api.immobilienscout24.de/ |
| **PT** | Idealista PT | same Idealista group | as ES |
| **IT** | Immobiliare.it | partner-only | scraping ToS-restricted |
| **NL** | Funda | partner-only via Funda XL | https://developers.funda.nl/ ❌ DEPRECATED — link dead (verified 2026-06-13); no public Funda developer portal, partner API is private — verify with Funda directly |
| **UK** | Rightmove + Zoopla | partner-only | Rightmove RDS data feed; Zoopla RealtyOS — both commercial |
| **AU** | realestate.com.au + Domain | partner-only | Domain Group has API; REA is commercial |
| **NZ** | Trade Me Property | public API | https://developer.trademe.co.nz/ |
| **NO** | Finn.no | partner-only | Schibsted-owned; commercial integrations |

## Portals scrape-only (CDN-protected, browser-OK)

| Country | Portal | CDN | Notes |
|---|---|---|---|
| **FR** | SeLoger / LeBonCoin | Cloudflare/DataDome | scraping aggressive blocking; use rotating IPs + headless-detection bypass |
| **CZ** | Sreality | Cloudflare | RSS feed older endpoint occasionally works |
| **PL** | Otodom | DataDome | Adevinta-owned |
| **HU** | Ingatlan.com | Cloudflare | scrape-only |
| **HR** | Njuškalo | Imperva | scrape-only |
| **GR** | Spitogatos | Cloudflare | scrape-only |
| **CY** | Bazaraki | Cloudflare | 403 to bare curl; browser-OK |
| **MT** | Frank Salt / RE/MAX / Dhalia / djar.ai | mixed | most respond 200 to bare curl; djar.ai aggregator most useful |
| **LU** | athome.lu | none | bare curl 200; immotop.lu 403 to HEAD but loads in browser |
| **BG** | Imot.bg | none | bare curl 200 |
| **RO** | Imobiliare.ro / Storia.ro | mild | mostly accessible |
| **LT** | Aruodas / Domoplius | none | bare curl 200 |
| **LV** | SS.lv / City24 | none | bare curl 200 |
| **AT** | Willhaben | DataDome | scrape-aggressive |
| **CH** | Comparis / Homegate | mixed | scrape-restricted |
| **SE** | Hemnet | Cloudflare | scrape-restricted |
| **FI** | Etuovi / Oikotie | mild | mostly accessible |
| **DK** | Boliga | none | open |
| **IS** | Mbl.is fasteignir | none | open |
| **SI** | Nepremicnine.net | mild | mostly accessible |
| **IE** | Daft.ie | partner-only API + scrape | commercial API exists |
| **EE** | KV.ee + City24 | none | open |
| **CA** | Realtor.ca | partner-only API | CREA owns |
| **MX** | Inmuebles24 | partner-only | OLX-owned |
| **BR** | ZAP / VivaReal | partner-only | OLX-owned |
| **AR** | Zonaprop / Argenprop / MercadoLibre | partner-only | OLX-owned |
| **CR** | Encuentra24 | partner-only | OLX-owned |
| **PA** | Encuentra24 / CompreoAlquile | mixed | partial scrape OK |

## Portals with strong RSS / data download

| Country | Portal | Mode | Notes |
|---|---|---|---|
| **UK** | UK HPI Land Registry | data download | https://www.gov.uk/government/collections/uk-house-price-index-reports |
| **NL** | Kadaster + Funda | data download | Kadaster open data; Funda XL via API |
| **NO** | Eiendom Norge | data download | https://eiendomnorge.no/ |

---

## Universal cadastre fallback

When listing portals are blocked or rate-limited, the **cadastre** is the always-available fallback:
- It has the property's legal description, ownership, encumbrances
- It does NOT have current listing price or comps
- See per-country playbook §mains for the cadastre URL

For comp values, the **price index source** in `shared/price-index-feeds.md` is the authoritative substitute when listings are unreachable.

---

## Operationalization

### How to fetch a listing for `--listing=<url>`

```python
# pseudocode
1. Detect portal from URL → look up CDN/scrape rules in this catalog
2. If partner API: emit "API key required" error + fallback to cadastre
3. If scrape-allowed: use Playwright headless with stealth settings (avoid DataDome/Imperva detection)
4. If scrape-restricted: emit warning + extract what's possible from URL slug + cadastre
5. Always verify against per-country listings template in playbook
```

### Rate limits to respect

- **Cloudflare-fronted**: max 1 req / 3-5 seconds per IP
- **DataDome / Imperva**: rotate IPs; expect captchas
- **Partner APIs**: respect per-key quotas in the API documentation

### Prohibited

- Bulk scraping in violation of ToS (Idealista, Funda, Immoscout24, Rightmove all explicitly forbid)
- Republishing listing photos beyond fair-use snippet for due-diligence preview
- Storing listing data beyond the immediate session output

---

## Status

Last refreshed: 2026-04-26.

## Extension TODOs

- Per-portal stealth-config presets for Playwright (Cloudflare bypass, DataDome detection avoidance)
- Idealista Data commercial subscription evaluation for `--price` deep-comp queries
- Funda XL evaluation for NL premium tier
- LinkedIn-style "company directory" of property-tech APIs (Property Pal, ATTOM Data, etc.)
