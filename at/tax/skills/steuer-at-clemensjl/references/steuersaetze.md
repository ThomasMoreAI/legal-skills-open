# VAT rates — § 10 UStG

Basis: § 10 UStG 1994 with Anlagen 1, 2 and 3, consolidated version as at 2026-08-05 (RIS). Status as at 2026-08-05.

## The rates in force

| Rate | Provision | Applies to |
|---|---|---|
| **20 %** | § 10 Abs 1 | standard rate, every taxable supply not caught by a reduced rate |
| **13 %** | § 10 Abs 3 | Anlage 2 goods, artists, cinema, theatre, museums, zoos, circus, domestic air passenger transport, swimming pools and thermal treatment, farm-produced wine, admission to sporting events |
| **10 %** | § 10 Abs 2 | Anlage 1 goods (foodstuffs, books and printed matter, medicines), restaurant supplies of Anlage 1 items, residential letting, accommodation, camping, charitable bodies, broadcasting, passenger transport other than air, waste disposal, hospitals, **electronic publications**, repairs to bicycles, shoes, leather goods, clothing and household linen |
| **4,9 %** | § 10 Abs 1a | Anlage 3 basic foodstuffs. **New: BGBl. I Nr. 37/2026, in force for supplies made after 2026-06-30** (§ 28 Abs 69 UStG) |
| **19 %** | § 10 Abs 4 | the territories of Jungholz and Mittelberg only |
| 0 % / exempt | § 6 UStG | exemptions, incl. § 6 Abs 1 Z 27 Kleinunternehmer. Not a "rate" — see `kleinunternehmer.md` |

Precedence is written into the statute: Abs 1a is tested first, then Abs 2, then Abs 3. A product listed in Anlage 3 takes 4,9 % even though the same product also sits in Anlage 1.

## The 4,9 % rate — what is in Anlage 3

Anlage 3 (zu § 10 Abs 1a UStG), "Verzeichnis der dem Steuersatz von 4,9 % unterliegenden Gegenstände", closed list of 12 items by Combined Nomenclature position:

1. Milk including lactose-free milk (CN 0401 10, 0401 20)
2. Yoghurt (CN 0403 20)
3. Butter (CN 0405 10)
4. Fresh hen eggs (CN 0407 21 00)
5. Vegetables, fresh or chilled (CN 0701 9050, 0701 9090, 0702 00, positions 0703–0709, with exclusions)
6. Vegetables, frozen (CN 0710)
7. Edible fruit (CN 0808, 0809)
8. Rice (CN 1006)
9. Wheat flour and semolina (CN 1101 00, 1103 11)
10. Pasta, not cooked, stuffed or otherwise prepared (CN 1902 11 00, 1902 19)
11. Bread (CN 1905 90 30)
12. Table salt (CN 2501 00 91)

§ 10 Abs 1a adds a restriction that matters for product-catalogue logic: the reduced rate applies **only where the supply or import concerns exclusively goods listed in that very CN position or subposition**. A mixed article that falls partly outside the listed subposition does not get 4,9 %.

## Digital products

| Product | Rate | Basis |
|---|---|---|
| Software licence, SaaS subscription, API access, cloud storage | 20 % | no reduced-rate category applies |
| App, game, in-app purchase | 20 % | as above |
| **Electronic publication** (e-book, e-paper, digital magazine) | **10 %** | § 10 Abs 2 Z 9 — "elektronische Publikationen im Sinne der Anlage 1 Z 33 sowie Teile davon" |
| Electronic publication that is wholly or mainly **video or music content**, or serves **advertising** purposes | 20 % | express carve-out in § 10 Abs 2 Z 9 |
| Audiobook | [[UNVERIFIED: whether a given audiobook falls within Anlage 1 Z 33 as an electronic publication or is caught by the "im Wesentlichen aus … Musikinhalten" carve-out — this is a classification question for the Steuerberater, not a coding decision]] |
| Streaming video, streaming music | 20 % | carve-out in § 10 Abs 2 Z 9 |
| Online course, webinar | [[UNVERIFIED: depends on whether it is an electronically supplied service or an exempt educational supply under § 6 Abs 1 Z 11 — classification question]] |

Anlage 1 Z 33 covers goods of CN Chapter 49: books, brochures and similar printed matter (4901); newspapers and periodicals (4902); children's picture, drawing and colouring books (4903 00 00); sheet music (4904 00 00); printed maps, plans and globes (4905). § 10 Abs 2 Z 9 extends the 10 % rate to the electronic equivalents of exactly that list.

## Implementation notes

- **Rates belong in dated, versioned data, not in code constants.** The 4,9 % rate entered force on 2026-07-01 for supplies made after 2026-06-30. A rate lookup must take the *supply date*, not the invoice date, as the key.
- **Store the rate on the line item at the moment of supply.** Later rate changes must not retroactively alter historic documents.
- **Keep the tax base separated per rate on the invoice.** § 11 Abs 1 Z 3 lit e and f require the Entgelt and the tax amount per rate, so an invoice mixing rates needs one subtotal block per rate.
- **The RKSV receipt payload has five amount buckets, not four.** `Betrag-Satz-Normal` (20 %), `Betrag-Satz-Ermaessigt-1`, `Betrag-Satz-Ermaessigt-2`, `Betrag-Satz-Null`, and `Betrag-Satz-Besonders` — the last of which the RKSV Anlage in the version of BGBl. II Nr. 134/2026 (in force 2026-07-01) labels "(19 %, 4,9 %)". See `registrierkasse.md`.

## Rate table skeleton

```json
{
  "jurisdiction": "AT",
  "valid_from": "2026-07-01",
  "source": "§ 10 UStG 1994, Fassung BGBl. I Nr. 37/2026",
  "rates": [
    { "code": "standard",  "rate": 0.20,  "basis": "§ 10 Abs 1"  },
    { "code": "reduced13", "rate": 0.13,  "basis": "§ 10 Abs 3"  },
    { "code": "reduced10", "rate": 0.10,  "basis": "§ 10 Abs 2"  },
    { "code": "reduced49", "rate": 0.049, "basis": "§ 10 Abs 1a, Anlage 3" },
    { "code": "special19", "rate": 0.19,  "basis": "§ 10 Abs 4, Jungholz/Mittelberg" }
  ],
  "product_mapping": "[[FEHLT: Zuordnung je Produktgruppe, freigegeben durch Steuerberater]]"
}
```

## Checkpoints

- [ ] Rate table contains 20, 13, 10 and 4,9 — and 19 if Jungholz or Mittelberg is in scope
- [ ] Rates are keyed by supply date, with `valid_from` / `valid_to`, not hard-coded constants
- [ ] The applied rate is persisted on the line item and never recomputed for historic documents
- [ ] Precedence Abs 1a → Abs 2 → Abs 3 implemented where a product could match more than one Anlage
- [ ] Electronic publications mapped to 10 % with the video/music/advertising carve-out handled
- [ ] Per-rate subtotal blocks rendered on multi-rate invoices
- [ ] Receipt payload exposes all five RKSV amount buckets including `Betrag-Satz-Besonders`
- [ ] Product-to-rate mapping signed off by a Steuerberater and recorded with the date of sign-off
