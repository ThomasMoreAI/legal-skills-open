---
name: canadian-court-downloader-dmang69
title: Canadian Court Document Downloader v2
description: 'Canadian court document retrieval, BOA builder, batch downloader, duplicate detector, and OCR extractor. ALWAYS trigger when user says: ''download this case'', ''get me the PDF'', ''pull the judgment'', ''build my BOA from these cases'', ''attach the cases'', ''batch download'', ''find duplicate cases'', ''extract text from this PDF'', or provides a list of citations and wants the actual documents. Also trigger for: ''check if I already have this case'', ''organize my cases'', ''export my authorities to CSV'', ''missing authority report'', or any request to retrieve, organize, or analyze Canadian court documents. Aliases: court-downloader, boa-downloader, case-retriever, batch-downloader.'
author: dmang69
author_url: https://github.com/dmang69/bc-legal-ai/tree/master/skills/canadian-court-downloader
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: litigation
language: en
sources:
- title: Scc Item Ids
  path: references/scc-item-ids.md
---

# Canadian Court Document Downloader v2

Full-featured Canadian court document retrieval, organization, and BOA assembly.
**Lawful access only. Not legal advice.**

## Scripts

```text
skills/canadian-court-downloader/
  SKILL.md
  references/scc-item-ids.md
  scripts/court_engine.py
  scripts/cli.py
  outputs/   # manifests, cases/, audit.log
```

```powershell
cd C:\Users\Dizzle\projects\bc-legal-ai\skills\canadian-court-downloader\scripts

python cli.py download --citation "2019 SCC 65" --out ..\outputs
python cli.py download --citation "2008 SCC 9" --citation "2011 SCC 61" --matter "test-boa" --out ..\outputs
python cli.py batch --file cases.json --out ..\outputs --matter "DEMO-JR-0001"
python cli.py ocr --pdf ..\outputs\cases\Tab_01_Vavilov_2019_SCC_65.pdf
```

`cases.json` example:

```json
{
  "matter": "DEMO-JR-0001",
  "cases": [
    {"tab": 1, "citation": "2019 SCC 65", "name": "Vavilov", "proposition": "Reasonableness is the presumptive standard of review."},
    {"tab": 2, "citation": "2008 SCC 9", "name": "Dunsmuir"}
  ]
}
```

## Compliance (non-negotiable)

| Rule | Action |
|------|--------|
| Public documents only | No auth bypass |
| No CAPTCHA / bot-wall defeat | Never |
| No sealed records | Stop if sealed |
| CanLII Cloudflare | **Do not retry** → REFERENCE_PDF + URL |
| Rate limit | **≥ 0.5s** between requests |

## Source ladder

1. **SCC** — `decisions.scc-csc.ca` …/`{ITEM_ID}`/`{1|2|3}`/`document.do`  
2. **BCCA/BCSC** — try courts.gov.bc.ca; usually → reference PDF  
3. **FCA** — try if item id known  
4. **CanLII** — blocked → reference PDF only  

Verified IDs: `references/scc-item-ids.md` (Knight/Kane/Lapointe IDs are **provisional**).

## Status codes

`ALREADY_EXISTS` · `SUCCESS` · `REFERENCE_PDF` · `BLOCKED_CLOUDFLARE` · `HTTP_400/403/404` · `SMALL_FILE` · `NOT_PDF` · `DUPLICATE` · `VERSION_UPDATE` · `OCR_SUCCESS` · `OCR_UNAVAILABLE` · `UNKNOWN_COURT`

## Agent workflow

1. Parse single / list / BOA tabs / folder organize request.  
2. Run `cli.py` or `court_engine.download_batch` — do not invent PDFs.  
3. Default out: `skills/canadian-court-downloader/outputs/`.  
4. After batch, open and summarize: `manifest.json`, `table_of_authorities.csv`, `download_summary.txt`, `missing_authorities.txt`, `access_denied.txt`, `duplicates.txt`.  
5. Never call a REFERENCE_PDF the official judgment.  
6. BOA assembly: use `legal-file-assistant` `boa_assembler.py` if merging SUCCESS PDFs; label **working draft**.  
7. Statutes still via **bc-legislation-admin** / BC Laws — this skill is **cases**.  
8. Local “do I already have it?” → also use **legal-file-assistant** file search.  

## Config (DownloaderConfig)

- `batch_delay_seconds` (default 0.5)  
- `include_ocr` (pytesseract + pdf2image optional)  
- `include_reference_pdfs` (default true)  
- `tag_anchor_cases` (Vavilov/Dunsmuir/Baker/Cardinal tagged ANCHOR)  
- `matter` (written into manifest)  

## File naming

`Tab_{NN}_{ShortName}_{CitationSlug}.pdf` · versions: `_v2`, `_v3`

## See also

- Skill **legal-file-assistant** — Windows local search + combined download/find  
- Monorepo knowledgebase / Form 66 petition (not Form 67) for filings  
