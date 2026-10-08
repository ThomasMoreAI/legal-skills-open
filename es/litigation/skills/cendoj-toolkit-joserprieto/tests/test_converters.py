"""
Unit tests for the converters package — Strategy pattern + ACL ConversionResult.

Tests verify the contract every converter strategy must honour without
running the underlying providers (those would require docling/pdfminer
and large PDFs). Provider-specific integration tests live in
test_converters_integration.py.
"""
from __future__ import annotations

import dataclasses

import pytest

from converters import (
    ConversionResult,
    ConverterUnavailableError,
    DoclingConverter,
    PdfMinerConverter,
    PdfToMarkdownConverter,
    available_converters,
    get_converter,
    list_converters,
)


# ---------------------------------------------------------------------------
# ConversionResult — ACL contract
# ---------------------------------------------------------------------------

class TestConversionResultACL:
    def test_is_frozen_dataclass(self) -> None:
        assert dataclasses.is_dataclass(ConversionResult)
        # Frozen dataclass: cannot mutate after construction
        result = ConversionResult(
            markdown="x", plain_text="x", engine_name="t",
            engine_version="0", page_count=None,
            has_tables=False, has_images=False,
        )
        with pytest.raises(dataclasses.FrozenInstanceError):
            result.markdown = "mutated"  # type: ignore[misc]

    def test_required_fields_present(self) -> None:
        result = ConversionResult(
            markdown="# Title", plain_text="Title",
            engine_name="docling", engine_version="0.5.0",
            page_count=10, has_tables=True, has_images=False,
        )
        assert result.markdown == "# Title"
        assert result.plain_text == "Title"
        assert result.engine_name == "docling"
        assert result.engine_version == "0.5.0"
        assert result.page_count == 10
        assert result.has_tables is True
        assert result.has_images is False

    def test_metadata_defaults_to_empty(self) -> None:
        result = ConversionResult(
            markdown="", plain_text="", engine_name="t",
            engine_version="0", page_count=None,
            has_tables=False, has_images=False,
        )
        assert result.metadata == {}

    def test_warnings_defaults_to_empty_tuple(self) -> None:
        result = ConversionResult(
            markdown="", plain_text="", engine_name="t",
            engine_version="0", page_count=None,
            has_tables=False, has_images=False,
        )
        assert result.warnings == ()

    def test_page_count_can_be_none(self) -> None:
        # Some engines cannot report page count
        result = ConversionResult(
            markdown="", plain_text="", engine_name="t",
            engine_version="0", page_count=None,
            has_tables=False, has_images=False,
        )
        assert result.page_count is None

    def test_metadata_can_carry_provider_specific_extras(self) -> None:
        result = ConversionResult(
            markdown="", plain_text="", engine_name="t",
            engine_version="0", page_count=None,
            has_tables=False, has_images=False,
            metadata={"strategy": "ocr-fallback", "rotation_detected": True},
        )
        assert result.metadata["strategy"] == "ocr-fallback"
        assert result.metadata["rotation_detected"] is True


# ---------------------------------------------------------------------------
# Factory — get_converter / list_converters / available_converters
# ---------------------------------------------------------------------------

class TestFactory:
    def test_list_converters_returns_known_strategies(self) -> None:
        registry = list_converters()
        assert "pdfminer" in registry
        assert "docling" in registry
        assert registry["pdfminer"] is PdfMinerConverter
        assert registry["docling"] is DoclingConverter

    def test_list_converters_returns_a_view_not_the_internal_dict(self) -> None:
        # Mutating the returned view must not affect the registry
        registry = list_converters()
        registry["bogus"] = PdfMinerConverter  # type: ignore[index]
        fresh = list_converters()
        assert "bogus" not in fresh

    def test_get_converter_raises_on_unknown_name(self) -> None:
        with pytest.raises(ValueError) as excinfo:
            get_converter("does-not-exist")
        assert "does-not-exist" in str(excinfo.value)
        assert "pdfminer" in str(excinfo.value)
        assert "docling" in str(excinfo.value)

    def test_available_converters_is_subset_of_list_converters(self) -> None:
        all_names = set(list_converters().keys())
        available_names = set(available_converters())
        assert available_names.issubset(all_names)

    def test_get_converter_returns_instance_of_correct_class(self) -> None:
        # We can only test the converters that have their deps installed
        available = available_converters()
        for name in available:
            instance = get_converter(name)
            assert isinstance(instance, PdfToMarkdownConverter)
            assert instance.name == name

    def test_get_converter_raises_unavailable_when_deps_missing(
        self, monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        # Force pdfminer.is_available() to return False
        monkeypatch.setattr(PdfMinerConverter, "is_available", classmethod(lambda cls: False))
        with pytest.raises(ConverterUnavailableError):
            get_converter("pdfminer")


# ---------------------------------------------------------------------------
# Strategy contract — every registered strategy must comply
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "converter_cls",
    [PdfMinerConverter, DoclingConverter],
)
class TestStrategyContract:
    def test_has_name_class_attribute(self, converter_cls: type[PdfToMarkdownConverter]) -> None:
        assert isinstance(converter_cls.name, str)
        assert len(converter_cls.name) > 0

    def test_has_description_class_attribute(self, converter_cls: type[PdfToMarkdownConverter]) -> None:
        assert isinstance(converter_cls.description, str)
        assert len(converter_cls.description) > 0

    def test_is_available_returns_bool(self, converter_cls: type[PdfToMarkdownConverter]) -> None:
        # The method must not raise — even when deps are missing
        result = converter_cls.is_available()
        assert isinstance(result, bool)

    def test_inherits_from_abstract_base(self, converter_cls: type[PdfToMarkdownConverter]) -> None:
        assert issubclass(converter_cls, PdfToMarkdownConverter)

    def test_cannot_instantiate_when_unavailable(
        self,
        converter_cls: type[PdfToMarkdownConverter],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        # Force is_available() to False, then convert() must refuse with ConverterUnavailableError
        monkeypatch.setattr(converter_cls, "is_available", classmethod(lambda cls: False))
        instance = converter_cls()
        from pathlib import Path
        with pytest.raises(ConverterUnavailableError):
            instance.convert(Path("/tmp/nonexistent.pdf"))


# ---------------------------------------------------------------------------
# Distinct strategy properties
# ---------------------------------------------------------------------------

class TestPdfMinerProperties:
    def test_name_is_pdfminer(self) -> None:
        assert PdfMinerConverter.name == "pdfminer"

    def test_description_mentions_text_only(self) -> None:
        assert "text" in PdfMinerConverter.description.lower()


class TestDoclingProperties:
    def test_name_is_docling(self) -> None:
        assert DoclingConverter.name == "docling"

    def test_description_mentions_structure(self) -> None:
        assert "structure" in DoclingConverter.description.lower()
