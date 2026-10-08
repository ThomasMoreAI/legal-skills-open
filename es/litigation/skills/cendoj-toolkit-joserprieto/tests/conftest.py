"""
Shared pytest fixtures for cendoj-toolkit tests.

Adds the scripts/ directory to sys.path so tests can import the modules
under test without requiring the package to be installed.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))


@pytest.fixture
def minimal_pdf_bytes() -> bytes:
    """A minimal valid PDF (magic header + minimal trailer).

    Just enough bytes to fool ``is_pdf()`` and round-trip through file IO
    without needing pdfminer/docling for unit tests.
    """
    return (
        b"%PDF-1.4\n"
        b"1 0 obj <<>> endobj\n"
        b"trailer <<>>\n"
        b"%%EOF\n"
    )


@pytest.fixture
def fake_pdf_path(tmp_path: Path, minimal_pdf_bytes: bytes) -> Path:
    """Write a minimal valid-looking PDF to tmp_path and return the path."""
    p = tmp_path / "fake.pdf"
    p.write_bytes(minimal_pdf_bytes)
    return p


@pytest.fixture
def non_pdf_path(tmp_path: Path) -> Path:
    """Write a non-PDF file (HTML or plain text) for negative is_pdf tests."""
    p = tmp_path / "not-a-pdf.html"
    p.write_text("<html><body>this is not a pdf</body></html>", encoding="utf-8")
    return p
