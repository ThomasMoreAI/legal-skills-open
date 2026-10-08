"""
Anti-Corruption Layer (ACL) + Strategy base for PDF → markdown converters.

Defines the abstract interface every converter must implement and the
normalized `ConversionResult` dataclass that callers consume regardless
of which provider (pdfminer, docling, marker, mistral-ocr, ...) ran the
extraction.

Adding a new provider:
  1. Create `myprovider_strategy.py` implementing `PdfToMarkdownConverter`
  2. Register the class in `converters/__init__.py` factory
  3. Document the converter in the SKILL.md prerequisites section

Callers must NOT import provider-specific modules directly — they
receive a `ConversionResult` from the factory and consume only its
documented fields.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, ClassVar, Mapping


@dataclass(frozen=True)
class ConversionResult:
    """ACL-normalized output for any PDF→markdown converter.

    All fields are provider-agnostic. Provider-specific extras must be
    placed in `metadata` (opaque dict — consumers may inspect but must
    not assume schema across providers).
    """

    markdown: str
    """Final markdown body produced by the converter.

    Does NOT include skill-level frontmatter (the orchestrator wraps
    this in its own document headers). Must be UTF-8 safe.
    """

    plain_text: str
    """Best-effort plain text extraction.

    Always populated as fallback. For text-only converters this equals
    `markdown` (or close to it); for structured converters this is a
    stripped version useful for full-text search/grep.
    """

    engine_name: str
    """Canonical converter name, e.g. ``"pdfminer"``, ``"docling"``."""

    engine_version: str
    """Version string of the underlying library at conversion time."""

    page_count: int | None
    """Total pages in source PDF (None if the engine cannot report it)."""

    has_tables: bool
    """True if the engine extracted any table structure into markdown."""

    has_images: bool
    """True if the engine detected images in the source PDF."""

    metadata: Mapping[str, Any] = field(default_factory=dict)
    """Provider-specific extras. Opaque to consumers."""

    warnings: tuple[str, ...] = field(default_factory=tuple)
    """Non-fatal issues observed during conversion (e.g. fonts not embedded,
    encrypted regions skipped, OCR fallback used). Empty if all clean."""


class ConverterUnavailableError(RuntimeError):
    """Raised when a converter strategy cannot run (missing deps, etc.)."""


class PdfToMarkdownConverter(ABC):
    """Strategy interface for PDF → markdown conversion.

    Each subclass encapsulates one provider (pdfminer.six, docling, marker,
    mistral-ocr, etc.) and exposes a uniform `convert()` method returning
    a `ConversionResult`.
    """

    name: ClassVar[str]
    """Canonical identifier used by the factory and CLI flag."""

    description: ClassVar[str]
    """Human-readable summary used in `--help`."""

    @classmethod
    @abstractmethod
    def is_available(cls) -> bool:
        """Return True if the converter's runtime dependencies are installed.

        Implementations should attempt a lightweight import (no heavy
        side effects). Returning False prevents the factory from
        instantiating this strategy.
        """
        ...

    @abstractmethod
    def convert(self, pdf_path: Path) -> ConversionResult:
        """Run the conversion and return a normalized result.

        Implementations MUST raise an exception on hard failure. Soft
        issues (e.g. unrecognized fonts, partial OCR) belong in
        `result.warnings`.
        """
        ...

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.__class__.__name__} name={self.name!r}>"
