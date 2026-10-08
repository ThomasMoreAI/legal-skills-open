# id-statutes-debt Corpus — Idaho

> **NOT LEGAL ADVICE.** Confirm every section and **especially every
> dollar amount** against the current Idaho Code on legislature.idaho.gov
> before relying on it. Idaho statutes are updated to the website July 1
> following each legislative session.

This corpus holds **verbatim Idaho Code text** for the sections most
relevant to civil practice, consumer-debt defense, exemptions, family
law, and deadline arithmetic. Each file carries the verbatim section text
(catchline + body + History) under `## Idaho Code §` headings. It is a
**bounded, representative** set — the sections a drafter reaches for — not
a full enumeration of the Idaho Code.

## Mode

- **Mode:** `verbatim` (fetched section text).
- **Source:** Idaho Legislature — https://legislature.idaho.gov/statutesrules/idstat/
- **Puller:** `scripts/pull_idaho_statutes.py`

## Topic files

- `Title5-limitations.md` — statutes of limitation (Title 5)
- `Title11-exemptions-garnishment.md` — exemptions and wage garnishment (Title 11)
- `homestead-Title55.md` — homestead exemption (Title 55)
- `consumer-protection-collection.md` — Idaho Consumer Protection Act, Collection Agency Act, Idaho Credit Code
- `attorney-fees-costs-Title12.md` — attorney fees and costs (Title 12)
- `family-Title32.md` — domestic relations / community property (Title 32)
- `holidays-Title73.md` — legal holidays for deadline arithmetic (Title 73)
- `ucc-article9-Title28.md` — Idaho UCC Article 9 secured transactions (Title 28)

## Refresh

`scripts/pull_idaho_statutes.py` fetches the per-section pages from
`https://legislature.idaho.gov/statutesrules/idstat/title<t>/t<t>ch<c>/sect<s>/`,
slices out the verbatim section body, and writes one file per topic group
(the topic→section map lives in `_manifest.json`). A curated-content guard
keeps an offline run from clobbering committed text; pass
`--overwrite-curated` to force a refresh. Verify dollar figures against the
live source on each refresh.
