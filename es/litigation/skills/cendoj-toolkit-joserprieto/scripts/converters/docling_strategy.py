"""
docling strategy — structure-preserving PDF → markdown.

Uses IBM's docling library to extract text + tables + (optionally)
headings into clean markdown. Heavier than pdfminer but produces
output closer to the source layout, which matters for court decisions
where the section structure (Antecedentes / Fundamentos de Derecho /
Fallo) is semantically meaningful.
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


class DoclingConverter(PdfToMarkdownConverter):
    name: ClassVar[str] = "docling"
    description: ClassVar[str] = (
        "docling — structure-preserving extraction (text + tables + headings)."
    )

    @classmethod
    def is_available(cls) -> bool:
        try:
            import_module("docling.document_converter")
        except ImportError:
            return False
        return True

    def convert(self, pdf_path: Path) -> ConversionResult:
        if not self.is_available():
            raise ConverterUnavailableError(
                "docling not installed. Run: pip install docling"
            )

        doc_converter_mod = import_module("docling.document_converter")
        DocumentConverter = doc_converter_mod.DocumentConverter

        converter = DocumentConverter()
        result = converter.convert(str(pdf_path))
        document = result.document

        markdown = document.export_to_markdown()

        # Try to extract a plain-text fallback
        try:
            plain_text = document.export_to_text()
        except AttributeError:
            # Older versions of docling may not have export_to_text
            # Strip markdown formatting as a poor man's fallback
            plain_text = _strip_markdown_to_text(markdown)

        # Probe page count + structure hints
        page_count: int | None = None
        has_tables = False
        has_images = False
        warnings: list[str] = []

        try:
            # docling Document has `pages` attribute in recent versions
            if hasattr(document, "pages") and document.pages is not None:
                page_count = len(document.pages)
        except Exception:
            pass

        # Detect tables in the exported markdown (rough heuristic)
        # A markdown table has the separator line `|---|---|...`
        for line in markdown.splitlines():
            stripped = line.strip()
            if stripped.startswith("|") and "---" in stripped:
                has_tables = True
                break

        # Detect images
        try:
            if any(getattr(item, "image", None) is not None for item in getattr(document, "pictures", [])):
                has_images = True
        except Exception:
            pass

        # Also detect markdown image syntax
        if not has_images and "![" in markdown:
            has_images = True

        return ConversionResult(
            markdown=markdown,
            plain_text=plain_text,
            engine_name=self.name,
            engine_version=_safe_version("docling"),
            page_count=page_count,
            has_tables=has_tables,
            has_images=has_images,
            metadata={
                "strategy": "structure-preserving",
                "preserves_structure": True,
                "ocr_used": False,  # docling does layout-based, not OCR by default
            },
            warnings=tuple(warnings),
        )


def _strip_markdown_to_text(md: str) -> str:
    """Very small fallback to derive plain text from markdown if the
    converter cannot provide it directly."""
    import re

    text = md
    # Remove fenced code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove inline code
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Remove markdown table separators
    text = re.sub(r"^\|[-:\s|]+\|$", "", text, flags=re.MULTILINE)
    # Remove pipe separators from tables
    text = re.sub(r"^\|", "", text, flags=re.MULTILINE)
    text = re.sub(r"\|$", "", text, flags=re.MULTILINE)
    text = text.replace("|", " ")
    # Remove markdown headings hashes
    text = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)
    # Remove emphasis markers
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    # Collapse blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
