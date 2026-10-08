"""
Unit tests for cendoj_lib — pure functions (URL building, parsing, file helpers).
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from cendoj_lib import (
    CENDOJ_BASE,
    DEFAULT_MAX_DOWNLOADS,
    HARD_CAP_MAX_DOWNLOADS,
    MIN_DELAY_SECONDS,
    build_pdf_url,
    is_pdf,
    parse_open_document_url,
    parse_result_text,
    parse_title,
    safe_filename,
    sha256_file,
)


# ---------------------------------------------------------------------------
# Constants (compliance guarantees)
# ---------------------------------------------------------------------------

class TestConstants:
    def test_min_delay_is_five_seconds_per_cendoj_robots_txt(self) -> None:
        assert MIN_DELAY_SECONDS == 5.0

    def test_default_max_downloads_is_conservative(self) -> None:
        assert 0 < DEFAULT_MAX_DOWNLOADS <= 100

    def test_hard_cap_is_not_excessive(self) -> None:
        assert DEFAULT_MAX_DOWNLOADS <= HARD_CAP_MAX_DOWNLOADS <= 500

    def test_base_url_is_official_cendoj_domain(self) -> None:
        assert CENDOJ_BASE == "https://www.poderjudicial.es"


# ---------------------------------------------------------------------------
# URL construction
# ---------------------------------------------------------------------------

class TestBuildPdfUrl:
    def test_format_includes_all_required_params(self) -> None:
        url = build_pdf_url("a73e3b3c0538644fa0a8778d75e36f0d", "20260316")
        assert "action=accessToPDF" in url
        assert "publicinterface=true" in url
        assert "tab=AN" in url
        assert "reference=a73e3b3c0538644fa0a8778d75e36f0d" in url
        assert "encode=true" in url
        assert "optimize=20260316" in url
        assert "databasematch=AN" in url

    def test_uses_official_base(self) -> None:
        url = build_pdf_url("abcd1234", "20240101")
        assert url.startswith(CENDOJ_BASE)
        assert "/search/contenidos.action" in url

    def test_accepts_short_reference_pre_2018(self) -> None:
        # Pre-2018 references are 16 chars
        url = build_pdf_url("1b0ad28855e44799", "20180425")
        assert "reference=1b0ad28855e44799" in url

    def test_accepts_long_reference_post_2018(self) -> None:
        url = build_pdf_url("a73e3b3c0538644fa0a8778d75e36f0d", "20260316")
        assert "reference=a73e3b3c0538644fa0a8778d75e36f0d" in url

    def test_empty_reference_raises(self) -> None:
        with pytest.raises(ValueError):
            build_pdf_url("", "20260316")

    def test_empty_optimize_raises(self) -> None:
        with pytest.raises(ValueError):
            build_pdf_url("abcd1234", "")


class TestParseOpenDocumentUrl:
    def test_parses_post_2018_long_reference(self) -> None:
        url = (
            "https://www.poderjudicial.es/search/AN/openDocument/"
            "a73e3b3c0538644fa0a8778d75e36f0d/20260316"
        )
        ref, opt = parse_open_document_url(url)
        assert ref == "a73e3b3c0538644fa0a8778d75e36f0d"
        assert opt == "20260316"

    def test_parses_pre_2018_short_reference(self) -> None:
        url = (
            "https://www.poderjudicial.es/search/AN/openDocument/"
            "1b0ad28855e44799/20180425"
        )
        ref, opt = parse_open_document_url(url)
        assert ref == "1b0ad28855e44799"
        assert opt == "20180425"

    def test_returns_none_for_non_matching_url(self) -> None:
        assert parse_open_document_url("https://example.com/foo/bar") is None

    def test_returns_none_for_truncated_url(self) -> None:
        assert parse_open_document_url("openDocument/abc") is None


# ---------------------------------------------------------------------------
# Title parsing
# ---------------------------------------------------------------------------

class TestParseTitle:
    def test_extracts_roj(self) -> None:
        title = "STSJ Galicia, a 06 de febrero de 2026 - ROJ: STSJ GAL 1040/2026"
        result = parse_title(title)
        assert result["roj"] == "STSJ GAL 1040/2026"

    def test_extracts_tribunal_prefix(self) -> None:
        title = "STSJ Galicia, a 06 de febrero de 2026 - ROJ: STSJ GAL 1040/2026"
        result = parse_title(title)
        assert result["tribunal"] == "STSJ Galicia"

    def test_extracts_spanish_date_to_iso(self) -> None:
        title = "STSJ Galicia, a 06 de febrero de 2026 - ROJ: STSJ GAL 1040/2026"
        result = parse_title(title)
        assert result["date_iso"] == "2026-02-06"

    @pytest.mark.parametrize(
        "spanish_month,expected_iso_month",
        [
            ("enero", "01"), ("febrero", "02"), ("marzo", "03"),
            ("abril", "04"), ("mayo", "05"), ("junio", "06"),
            ("julio", "07"), ("agosto", "08"), ("septiembre", "09"),
            ("octubre", "10"), ("noviembre", "11"), ("diciembre", "12"),
        ],
    )
    def test_parses_every_spanish_month(self, spanish_month: str, expected_iso_month: str) -> None:
        title = f"STS, a 15 de {spanish_month} de 2024 - ROJ: STS 1/2024"
        result = parse_title(title)
        assert result["date_iso"] == f"2024-{expected_iso_month}-15"

    def test_returns_none_for_missing_date(self) -> None:
        title = "Sentence without date - ROJ: STS 1/2024"
        result = parse_title(title)
        assert result["date_iso"] is None

    def test_returns_none_for_missing_roj(self) -> None:
        title = "STSJ Galicia, a 06 de febrero de 2026 (no roj here)"
        result = parse_title(title)
        assert result["roj"] is None

    def test_preserves_raw_title(self) -> None:
        title = "STS, a 23 de junio de 2025 - ROJ: STS 3291/2025"
        result = parse_title(title)
        assert result["raw_title"] == title

    def test_pads_single_digit_day(self) -> None:
        title = "STS, a 5 de febrero de 2025 - ROJ: STS 1/2025"
        result = parse_title(title)
        assert result["date_iso"] == "2025-02-05"


# ---------------------------------------------------------------------------
# Result text parsing
# ---------------------------------------------------------------------------

class TestParseResultText:
    def test_extracts_ecli_standard_format(self) -> None:
        text = "ECLI:ES:TSJGAL:2026:1040 - Nº de Resolución: 572/2026"
        result = parse_result_text(text)
        assert result["ecli"] == "ECLI:ES:TSJGAL:2026:1040"

    def test_extracts_ecli_with_auto_suffix(self) -> None:
        # Autos have an 'A' suffix
        text = "ECLI:ES:APM:2024:6968A - Nº Recurso: 817/2023"
        result = parse_result_text(text)
        assert result["ecli"] == "ECLI:ES:APM:2024:6968A"

    def test_extracts_resolution_number(self) -> None:
        text = "Nº de Resolución: 910/2026 - Municipio: Valencia"
        result = parse_result_text(text)
        assert result["resolution_number"] == "910/2026"

    def test_extracts_appeal_number(self) -> None:
        text = "Nº Recurso: 3281/2024 - Ponente: ALGUIEN"
        result = parse_result_text(text)
        assert result["appeal_number"] == "3281/2024"

    def test_extracts_city(self) -> None:
        text = "Municipio: Coruña (A) - Ponente: EVA MARIA"
        result = parse_result_text(text)
        assert result["city"] == "Coruña (A)"

    def test_extracts_ponente(self) -> None:
        text = "Ponente: EVA MARIA DOVAL LORENTE - Nº Recurso: 3429/2025"
        result = parse_result_text(text)
        assert result["ponente"] == "EVA MARIA DOVAL LORENTE"

    def test_prefers_RESUMEN_over_Resumen_Automatico(self) -> None:
        text = (
            "RESUMEN: DESPIDO DISCIPLINARIO\n"
            "Resumen Automático: this should be ignored"
        )
        result = parse_result_text(text)
        assert result["summary"] == "DESPIDO DISCIPLINARIO"

    def test_falls_back_to_Resumen_Automatico(self) -> None:
        text = "Resumen Automático: fallback content for cases without RESUMEN"
        result = parse_result_text(text)
        assert result["summary"] == "fallback content for cases without RESUMEN"

    def test_returns_none_for_all_missing_fields(self) -> None:
        result = parse_result_text("totally unrelated text")
        assert result["ecli"] is None
        assert result["resolution_number"] is None
        assert result["appeal_number"] is None
        assert result["city"] is None
        assert result["ponente"] is None
        assert result["summary"] is None


# ---------------------------------------------------------------------------
# Filename sanitization
# ---------------------------------------------------------------------------

class TestSafeFilename:
    def test_prefers_roj_when_present(self) -> None:
        entry = {"roj": "STSJ GAL 1040/2026", "ecli": "ECLI:ES:TSJGAL:2026:1040"}
        assert safe_filename(entry, 4) == "04-STSJ-GAL-1040-2026.pdf"

    def test_falls_back_to_ecli_when_no_roj(self) -> None:
        entry = {"roj": None, "ecli": "ECLI:ES:TSJGAL:2026:1040"}
        assert safe_filename(entry, 5) == "05-ECLI-ES-TSJGAL-2026-1040.pdf"

    def test_falls_back_to_index_when_no_identifiers(self) -> None:
        entry = {"roj": "", "ecli": None}
        assert safe_filename(entry, 7) == "07-sentencia-007.pdf"

    def test_uses_two_digit_index_padding(self) -> None:
        entry = {"roj": "STS 1/2024"}
        assert safe_filename(entry, 1).startswith("01-")
        assert safe_filename(entry, 99).startswith("99-")

    def test_strips_special_characters(self) -> None:
        entry = {"roj": "STS!@# 1/2024"}
        result = safe_filename(entry, 1)
        # No special chars beyond hyphens, dots and alphanumerics in result
        import re as _re
        assert _re.fullmatch(r"\d{2}-[A-Za-z0-9\-]+\.pdf", result)

    def test_handles_missing_keys(self) -> None:
        # Empty dict should still produce a fallback filename
        assert safe_filename({}, 3) == "03-sentencia-003.pdf"


# ---------------------------------------------------------------------------
# PDF magic byte validation
# ---------------------------------------------------------------------------

class TestIsPdf:
    def test_true_for_valid_pdf_magic_bytes(self, fake_pdf_path: Path) -> None:
        assert is_pdf(fake_pdf_path) is True

    def test_false_for_html_file(self, non_pdf_path: Path) -> None:
        assert is_pdf(non_pdf_path) is False

    def test_false_for_empty_file(self, tmp_path: Path) -> None:
        empty = tmp_path / "empty.pdf"
        empty.write_bytes(b"")
        assert is_pdf(empty) is False

    def test_false_for_nonexistent_file(self, tmp_path: Path) -> None:
        nonexistent = tmp_path / "does-not-exist.pdf"
        assert is_pdf(nonexistent) is False

    def test_false_for_truncated_magic_bytes(self, tmp_path: Path) -> None:
        truncated = tmp_path / "truncated.pdf"
        truncated.write_bytes(b"%PD")  # Less than 5 bytes
        assert is_pdf(truncated) is False


# ---------------------------------------------------------------------------
# SHA-256 hashing
# ---------------------------------------------------------------------------

class TestSha256File:
    def test_matches_hashlib_on_same_content(self, tmp_path: Path) -> None:
        content = b"hello cendoj-toolkit testing"
        p = tmp_path / "data.bin"
        p.write_bytes(content)
        expected = hashlib.sha256(content).hexdigest()
        assert sha256_file(p) == expected

    def test_consistent_across_calls(self, fake_pdf_path: Path) -> None:
        first = sha256_file(fake_pdf_path)
        second = sha256_file(fake_pdf_path)
        assert first == second
        assert len(first) == 64  # SHA-256 hex digest length

    def test_different_content_different_hash(self, tmp_path: Path) -> None:
        a = tmp_path / "a.bin"
        b = tmp_path / "b.bin"
        a.write_bytes(b"alpha")
        b.write_bytes(b"beta")
        assert sha256_file(a) != sha256_file(b)

    def test_handles_large_chunks(self, tmp_path: Path) -> None:
        # Write a file > 64 KiB to exercise the chunk loop
        big = tmp_path / "big.bin"
        big.write_bytes(b"x" * (128 * 1024))  # 128 KiB
        expected = hashlib.sha256(b"x" * (128 * 1024)).hexdigest()
        assert sha256_file(big) == expected
