# Source notes

## Access and provenance

- Primary owner: New Zealand Customs Service
- Primary source: https://www.customs.govt.nz/business/tariffs/tariff-classifications-and-rates/
- Archive: https://www.customs.govt.nz/media/0nmaamqd/tariff.tar.gz
- Official format guide: https://www.customs.govt.nz/media/y1dmuyec/tariff-and-concession-readme.pdf
- Website terms: https://www.customs.govt.nz/about-us/using-our-website/using-this-website/
- Declared outbound host: www.customs.govt.nz
- Access mode: unauthenticated HTTPS public download
- Authentication: none
- Last verified: 2026-09-02

On 2026-09-02 both the landing page and archive returned HTTP 200 within a 10-second request timeout. The archive was a gzip-compressed tar with `time_stamp.txt`, `Tariff_Details.csv`, `Tariff_Rates.csv`, `Tariff_Levies.csv`, and `Tariff_Levy_Formulas.csv`. Its embedded update marker was `Thu Sep  3 04:00:01 AM NZST 2026`; the HTTP `Last-Modified` value was `Wed, 02 Sep 2026 16:55:31 GMT`.

Customs says these files are updated every 24 hours and are database files for specialised Customs broker software, not general-public files. Customs states that there are no known rights covering this dataset and links its website terms. The checked-in archive fixture is independently authored synthetic data released as CC0-1.0; it contains no copied records, credentials or personal data.

## Parser contract

The archive CSVs use `~` as the delimiter and currently decode as Windows-1252. Details, rates and levies join on five two-digit tariff levels, producing a 10-digit tariff item. The parser requires the exact published headers and all five files, rejects oversized or malformed archives, and never extracts archive paths to disk.

- Details: classification description, check letter, section, statistical/supplementary units, GST-exempt indicator and validity dates.
- Rates: rate group, validity dates, excise factor, duty formula code and factors A–F.
- Levies: levy type, levy-formula code and validity dates.
- Levy formulas: levy-formula code and raw formula-rate coefficient.
- Timestamp: the source-generated archive update time from `time_stamp.txt`.

Blank expiry dates are treated as open-ended. Start and expiry dates are compared inclusively to the requested `--as-of` date. The live archive also uses far-future expiry dates for some current rows. Source/schema mismatches fail with exit code 6 rather than returning an empty successful result.

## Formula and interpretation limits

The official guide documents duty formulas separately from the levy-formula coefficient table. Rate rows expose the published formula code and Factors A–F without calculating duty. The common current duty formulas described by Customs include free duty (01), manual calculation (02), percentage of value for duty (03), quantity-based duty (04), and a combination of value and quantity (05). Consult the official guide for the complete formula definitions and variables such as VFD, QTY and CIF.

The CLI deliberately does not calculate duty, levies, GST or landed cost. The archive alone does not resolve legal classification, valuation, country-of-origin preferences, concessions, prohibited goods, anti-dumping measures, freight, insurance, fees or brokerage. Treat results as research leads and confirm consequential decisions with Customs or a qualified customs broker.

## Health and failure states

- HTTP 403 or 429 returns blocked/rate-limited exit code 4.
- DNS, timeout, connection and other upstream HTTP failures return exit code 5.
- Missing members, unexpected headers, bad encodings, invalid dates and malformed archives return parser/schema exit code 6.
- The smoke test always runs local fixture assertions first; only the bounded live assertion is skipped during a recognised source outage.
