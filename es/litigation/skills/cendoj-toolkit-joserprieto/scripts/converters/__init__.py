"""
Converters package — Strategy pattern + ACL for PDF → markdown providers.

Exports:

- `ConversionResult` — provider-agnostic result dataclass (the ACL).
- `PdfToMarkdownConverter` — strategy abstract base class.
- `ConverterUnavailableError` — raised when a strategy is missing deps.
- `get_converter(name)` — factory: returns an instantiated strategy by name.
- `list_converters()` — registry introspection: name → class.
- `available_converters()` — names of converters whose dependencies are present.

Adding a new provider:

1. Create `<name>_strategy.py` implementing `PdfToMarkdownConverter`
2. Add the class to `_REGISTRY` below
3. Document install steps in the SKILL.md prerequisites
"""
from __future__ import annotations

from typing import Mapping, Type

from .base import ConversionResult, ConverterUnavailableError, PdfToMarkdownConverter
from .docling_strategy import DoclingConverter
from .pdfminer_strategy import PdfMinerConverter

_REGISTRY: Mapping[str, Type[PdfToMarkdownConverter]] = {
    PdfMinerConverter.name: PdfMinerConverter,
    DoclingConverter.name: DoclingConverter,
}


def list_converters() -> Mapping[str, Type[PdfToMarkdownConverter]]:
    """Return the converter registry (name → class) as an immutable view."""
    return dict(_REGISTRY)


def available_converters() -> list[str]:
    """Return the names of converters whose dependencies are installed."""
    return [name for name, cls in _REGISTRY.items() if cls.is_available()]


def get_converter(name: str) -> PdfToMarkdownConverter:
    """Factory: instantiate a converter by canonical name.

    Raises:
        ValueError: if `name` is not registered.
        ConverterUnavailableError: if the converter's runtime deps are missing.
    """
    cls = _REGISTRY.get(name)
    if cls is None:
        known = ", ".join(sorted(_REGISTRY.keys()))
        raise ValueError(
            f"Unknown converter {name!r}. Known: {known}"
        )
    if not cls.is_available():
        raise ConverterUnavailableError(
            f"Converter {name!r} is registered but its runtime dependencies "
            f"are not installed. See SKILL.md prerequisites."
        )
    return cls()


__all__ = [
    "ConversionResult",
    "ConverterUnavailableError",
    "DoclingConverter",
    "PdfMinerConverter",
    "PdfToMarkdownConverter",
    "available_converters",
    "get_converter",
    "list_converters",
]
