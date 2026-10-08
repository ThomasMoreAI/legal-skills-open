# Photo OCR Pipeline (Operational)

Listing-photo OCR pipeline for the `--integrity` layer. Replaces the template-only state with a runnable workflow: download listing photos → extract text/labels via OCR or vision-model → cross-check against listing-claimed facts.

**Snapshot**: April 2026.

## What this catches

Common listing-photo signals that OCR/vision can verify:
- **EPC/DPE class label** painted on display board (vs listing's stated class)
- **Address signage** on building (vs listing's stated address)
- **Construction year placard** on facade or interior plaque
- **Surface (m²) marked on floor plan** (vs listing's stated m²)
- **For-sale sign agency contact** (vs listing's seller info)
- **Visible damage / works** (vs listing's "ready to move" claim)
- **Heritage-listing plaque** ("inscrit MH" / "scheduled grade I" / "Denkmalschutz")
- **Cadastre number** on agent's professional sign
- **Energy-label sticker** on appliance/boiler
- **Photo metadata (EXIF)** — capture date, GPS coords (if not stripped)

## Tooling options

### Local (free, batch)

**Tesseract OCR** — battle-tested, multi-language. Works for printed text on signs, labels, floor plans. Limited on handwriting or stylized fonts.

```bash
# install
brew install tesseract tesseract-lang

# run on a single image
tesseract listing-photo-01.jpg output -l fra+ita+eng

# → output.txt with extracted text improve accuracy with image preprocessing
convert listing-photo-01.jpg -threshold 60% -density 300 cleaned.png
tesseract cleaned.png output -l fra+ita+eng
```

**Limits**: poor on stylized signage, agency logos, multi-color backgrounds. Good for clear printed text on plaques and floor plans.

### Cloud (paid, higher quality)

**Anthropic Vision** — direct image-to-claim verification via Claude API. Best for "does this photo confirm the listing's claimed [X]?" questions.

**Google Vision API** — OCR + label detection + landmark recognition. ~$1.50/1k images.

**AWS Textract** — focused on documents, handles tables and key-value pairs. Best for floor-plan tables.

**Microsoft Azure AI Vision** — OCR + image analysis. Similar to Google Vision.

### Recommended hybrid

For property due-diligence:
1. **Tesseract first pass** on all photos (free, local, fast)
2. **Anthropic Vision second pass** on ambiguous photos OR specific fact-check queries ("does this photo show an EPC label, and what class is it?")
3. **EXIF reader** for metadata (GPS, capture date) via `exiftool`

---

## Operational pipeline

```bash
#!/usr/bin/env bash
# photo-ocr-pipeline.sh — one-shot pipeline for a listing
# Usage: ./photo-ocr-pipeline.sh <listing-url> [output-dir]
set -euo pipefail

LISTING_URL="${1:?usage: $0 <listing-url> [output-dir]}"
OUT_DIR="${2:-./photo-ocr-output}"
mkdir -p "$OUT_DIR"

# Step 1: extract photo URLs from listing (use the per-portal extraction prompt from `shared/preflight.md`) pseudo: yields photos.txt with one URL per line Step 2: download photos
mkdir -p "$OUT_DIR/raw"
n=0
while IFS= read -r url; do
    n=$((n+1))
    curl -sSL -o "$OUT_DIR/raw/photo-$n.jpg" "$url"
done < "$OUT_DIR/photos.txt"

# Step 3: extract EXIF (GPS, capture date)
exiftool -j "$OUT_DIR/raw/" > "$OUT_DIR/exif.json"

# Step 4: Tesseract OCR (multi-language)
mkdir -p "$OUT_DIR/ocr"
for img in "$OUT_DIR/raw"/*.jpg; do
    base=$(basename "$img" .jpg)

    # preprocess for better OCR
    convert "$img" -threshold 60% -density 300 "$OUT_DIR/ocr/$base-clean.png"

    # run Tesseract
    tesseract "$OUT_DIR/ocr/$base-clean.png" "$OUT_DIR/ocr/$base" -l fra+ita+eng+spa+deu
done

# Step 5: aggregate findings
cat "$OUT_DIR/ocr"/*.txt > "$OUT_DIR/all-extracted-text.txt"

# Step 6 (optional): Anthropic Vision pass
# (separate Python script — see below)
```

### Anthropic Vision verification (Python)

```python
# verify-listing-claims.py
# Verify specific listing claims against photos via Claude
import anthropic
import base64
import json
from pathlib import Path

client = anthropic.Anthropic()

def verify_claim(photo_path: Path, claim: str) -> dict:
    """Verify whether a photo supports a listing claim."""
    image_data = base64.standard_b64encode(photo_path.read_bytes()).decode()

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": f"""Listing claims: {claim}

Examine this photo. Does it confirm, contradict, or neither support nor contradict the claim?

Respond JSON: {{"verdict": "confirms" | "contradicts" | "neutral", "evidence": "<what the photo shows>", "confidence": "high" | "medium" | "low"}}""",
                },
            ],
        }],
    )

    return json.loads(response.content[0].text)

# example usage
for photo in Path("./photo-ocr-output/raw").glob("*.jpg"):
    result = verify_claim(photo, "EPC class C, 95 m², no visible damage")
    print(f"{photo.name}: {result}")
```

Tip: cache photo→Vision-result by photo hash to avoid re-billing on repeated runs.

---

## Integration with `--integrity` layer

When the user runs `/property-deep-dive <listing-url> --integrity`, the photo-OCR pipeline is invoked as part of the **listing-photo OCR check** (one of the 4 integrity checks in `shared/integrity-checks.md`).

Specifically:
1. Pipeline runs against the listing's photos
2. Aggregates extracted text + Vision verdicts
3. Flags any **contradictions** between photos and listing fields:
   - Stated EPC class ≠ photo'd EPC label class → 🟠
   - Stated address ≠ visible building signage → 🔴
   - Stated "no works needed" ≠ photo of partial demolition → 🔴
   - Stated 100 m² ≠ floor plan total 80 m² → 🟠
   - Listed agency ≠ for-sale sign agency → 🟡 (could be platform aggregator)
   - Heritage plaque visible but not mentioned in listing → 🟠
4. Output integrated into `--integrity` section of the report

---

## Privacy & ToS

- **Listing photos are seller-/platform-owned** — fair-use for buyer due-diligence is generally OK; do NOT republish or store beyond the run
- **EXIF GPS** — many platforms strip; some preserve (esp. older listings)
- **Vision-model billing** — only run on photos that need verification, not the entire gallery
- **Cache by photo hash** to avoid duplicate Vision calls

---

## Limitations

- **Tesseract poor on stylized fonts, handwriting, low-contrast signage** — fallback to Vision
- **Vision can hallucinate** — always require an "evidence:" field grounding the verdict in pixels
- **Photos can be staged** — verifiable contradictions are HIGH signal, but absence of contradiction is NOT proof
- **EXIF can be stripped** — agents commonly post-process photos through their listing platform which strips GPS
- **OCR multilingual** — install all language packs you need (`fra ita spa deu nld por pol ces hun ron bul ell tur ara heb` etc.)

---

## Status

Last refreshed: 2026-04-26. **Operational** (replaces prior template-only state).

## Extension TODOs

- Per-portal photo-extraction prompt presets (SeLoger/Idealista/Immoscout24/Rightmove all expose photos differently)
- Heritage-plaque visual classifier (vs OCR — heritage plaques often have specific iconography rather than text)
- Floor-plan area extractor (computer vision: detect closed polygons, compute area from scale bar)
- EXIF→commune cross-check (does the photo's GPS land in the listed commune?)
- Cache layer (photo hash → Vision result) to avoid duplicate billing across runs of the same listing
