"""
pdfminer.six strategy — fast text extraction, no structure.

Suitable for plain-text searches and audit trails where layout is not
required. Returns markdown that is essentially the extracted text with
whitespace normalized.
"""
from __future__ import annotations

from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import ClassVar

from .base import ConversionResult, ConverterUnavailableError, PdfToMarkdownConverter


def _safe_version(pkg: str) -> str:
    try:
        return version(pkg)
    except PackageNotFoundError:
        return "unknown"


class PdfMinerConverter(PdfToMarkdownConverter):
    name: ClassVar[str] = "pdfminer"
    description: ClassVar[str] = (
        "pdfminer.six — fast plain-text extraction (no structure preserved)."
    )

    @classmethod
    def is_available(cls) -> bool:
        try:
            import_module("pdfminer.high_level")
        except ImportError:
            return False
        return True

    def convert(self, pdf_path: Path) -> ConversionResult:
        if not self.is_available():
            raise ConverterUnavailableError(
                "pdfminer.six not installed. Run: pip install pdfminer.six"
            )

        high_level = import_module("pdfminer.high_level")
        pdfdocument = import_module("pdfminer.pdfdocument")
        pdfparser = import_module("pdfminer.pdfparser")

        # Extract text
        text = high_level.extract_text(str(pdf_path))

        # Count pages (open PDF separately to query metadata)
        page_count: int | None = None
        try:
            with pdf_path.open("rb") as f:
                parser = pdfparser.PDFParser(f)
                doc = pdfdocument.PDFDocument(parser)
                page_count = sum(1 for _ in pdfdocument.PDFPage.create_pages(doc))  # type: ignore[attr-defined]
        except Exception:
            # `PDFPage.create_pages` lives in `pdfminer.pdfpage` — try alternate
            try:
                pdfpage = import_module("pdfminer.pdfpage")
                with pdf_path.open("rb") as f:
                    page_count = sum(1 for _ in pdfpage.PDFPage.get_pages(f))
            except Exception:
                page_count = None

        # Normalize whitespace
        lines = text.split("\n")
        cleaned: list[str] = []
        blank_streak = 0
        for line in lines:
            if not line.strip():
                blank_streak += 1
                if blank_streak <= 1:
                    cleaned.append("")
            else:
                blank_streak = 0
                cleaned.append(line.rstrip())
        body = "\n".join(cleaned).strip()

        return ConversionResult(
            markdown=body,
            plain_text=body,
            engine_name=self.name,
            engine_version=_safe_version("pdfminer.six"),
            page_count=page_count,
            has_tables=False,
            has_images=False,
            metadata={
                "strategy": "text-only",
                "preserves_structure": False,
            },
            warnings=(
                "pdfminer.six does not preserve tables, headings, or images. "
                "For structured output use the docling strategy.",
            ),
        )
