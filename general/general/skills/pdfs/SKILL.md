---
name: pdfs
title: PDF reading, creation, and review guidance
description: Guides reading, creating, and reviewing PDFs using pdftoppm, pdfplumber, and reportlab, including font setup for non-ASCII characters and quality checks for layout fidelity.
author: AFK-surf
author_url: https://github.com/AFK-surf/OpenBridge/tree/main/macos/OpenBridge/Resources/SystemSkills.bundle/pdfs
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# PDF reading, creation, and review guidance

## Reading PDFs
- Use `pdftoppm -png $OUTDIR/$BASENAME.pdf $OUTDIR/$BASENAME` to convert PDFs to PNGs.
- Then open the PNGs and read the images.
- `pdfplumber` is also installed and can be used to read PDFs. It can be used as a complementary tool to `pdftoppm` but not replacing it.
- Only do python printing as a last resort because you will miss important details with text extraction (e.g. figures, tables, diagrams).

## Primary tooling for creating PDFs
- Generate PDFs programmatically with `reportlab` as the primary tool. In most cases, you should use `reportlab` to create PDFs.
- If there are other packages you think are necessary for the task (eg. `pypdf`, `pyMuPDF`), you can use them but you may need to pip install them first.

## Font support for non-ASCII characters
- Before creating PDFs with Chinese, Japanese, Korean (CJK) or other non-ASCII characters, install the required fonts:
  ```bash
  apt-get update && apt-get install -y fonts-noto-cjk fonts-noto-core fonts-noto-ui-core
  ```
- After installing fonts, rebuild the font cache: `fc-cache -fv`
- Verify fonts are available: `fc-list :lang=zh` (for Chinese)
- After **each meaningful update**—content additions, layout adjustments, or style changes—render the PDF to images to check layout fidelity:
  - `pdftoppm -png $INPUT_PDF $OUTPUT_PREFIX`
- Inspect every exported PNG before continuing work. If anything looks off, fix the source and re-run the render → inspect loop until the pages are clean.

## Quality expectations
- Maintain a polished, intentional visual design: consistent typography, spacing, margins, color palette, and clear section breaks across all pages.
- Avoid major rendering issues—no clipped text, overlapping elements, black squares, broken tables, or unreadable glyphs. The rendered pages should look like a curated document, not raw template output.
- Charts, tables, diagrams, and images must be sharp, well-aligned, and properly labeled in the PNGs. Legends and axes should be readable without excessive zoom.
- Text must be readable at normal viewing size; avoid walls of filler text or dense, unstructured bullet lists. Use whitespace to separate ideas.
- Never use the U+2011 non-breaking hyphen or other unicode dashes as they will not be rendered correctly. Use ASCII hyphens instead.
- Citations, references, and footnotes must be human-readable and professional. No tool-internal tokens (e.g., `[145036110387964†L158-L160]`), malformed URLs, or placeholder text should be present in the document.
- You must convert all citations into a human-readable format in the document with standard scholarly citation format. No `【【turn1541736113682297662view0†L11-L19】` notations are allowed in the document as the reader cannot interpret them (such citations will be severely penalized).
- Correct every formatting defect you see in the PNGs, including but not limited to: overlapping text or shapes, clipped text or shapes that are cut off, black squares, broken tables, unreadable characters, etc.

## Final checks
- Do not ship the PDF until the latest PNG inspection shows zero visual or formatting defects. Confirm page numbering, headers/footers, and section transitions look polished.
- You must resolve any issues you spot (typos, spacing, alignment, color contrast) and re-render for a final verification pass before submitting.
- Keep intermediate PNGs/PDFs clearly labeled or cleaned up so reviewers can navigate the outputs easily.
