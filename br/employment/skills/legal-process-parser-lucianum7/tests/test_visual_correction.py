from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT))

from scripts.helpers import (
    build_pages,
    classify_visual_asset,
    consolidate_visual_inventory,
)
from scripts.ingest_document import resolve_vision_configuration, run_ingest
from scripts.validate_links import validate_links


class VisualCorrectionTests(unittest.TestCase):
    def test_asset_classification_preserves_relevant_visuals(self) -> None:
        self.assertEqual(classify_visual_asset({"width": 2, "height": 2}), "technical_artifact")
        self.assertEqual(classify_visual_asset({"source_name": "qr-code.png", "width": 80, "height": 80}), "qr_code")
        self.assertEqual(classify_visual_asset({"alt_text": "logotipo da empresa", "width": 100, "height": 50}), "logo")
        self.assertEqual(classify_visual_asset({"source_name": "fotografia-autora.jpg", "width": 400, "height": 300}), "photo")
        self.assertEqual(classify_visual_asset({"kind": "page_scan"}), "document_scan")

    def test_embedded_assets_are_deduplicated_with_occurrences(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "images"
            output.mkdir()
            first = output / "page-0001-a.bin"
            second = output / "page-0002-b.bin"
            first.write_bytes(b"same image bytes")
            second.write_bytes(b"same image bytes")
            pages = {
                1: [{"image_id": "P0001-I001", "source_name": "a.bin", "image_path": str(first), "sha256": ""}],
                2: [{"image_id": "P0002-I001", "source_name": "b.bin", "image_path": str(second), "sha256": ""}],
            }
            result = consolidate_visual_inventory(pages, output)
            records = [record for page in result.values() for record in page]
            self.assertEqual(len({record["unique_image_id"] for record in records}), 1)
            self.assertEqual(sorted(record["occurrence_index"] for record in records), [1, 2])
            self.assertEqual(len([path for path in output.iterdir() if path.is_file()]), 1)

    def test_required_vision_gate_and_agent_review_sidecar(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "processo.pdf"
            source.write_bytes(b"%PDF-placeholder")
            output = root / "out"
            with self.assertRaises(ValueError):
                resolve_vision_configuration(source, output, "required", "none", None, None)
            review = root / "vision_review.json"
            review.write_text(json.dumps({"schema_version": "1.0", "pages": {}, "images": []}), encoding="utf-8")
            provider, selected = resolve_vision_configuration(source, output, "required", "agent_review", None, review)
            self.assertEqual(provider, "agent_review")
            self.assertEqual(selected, review.resolve())

    def test_off_policy_does_not_require_pdf_render_or_vision(self) -> None:
        pages, _ = build_pages(["texto nativo"], source_kind=".pdf", vision_mode="never", vision_policy="off")
        self.assertEqual(pages[0].status, "COMPLETE")
        self.assertFalse(pages[0].render["required"])
        self.assertFalse(pages[0].vision["required"])

    def test_utf8_sig_bundle_remains_valid_and_links_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "processo.txt"
            source.write_text("Petição Inicial\nPrazo de 5 dias", encoding="utf-8")
            output = root / "out"
            result = run_ingest(source, output, output_encoding="utf-8-sig")
            self.assertEqual(result["manifest"]["encoding"]["output"], "utf-8-sig")
            self.assertTrue((output / "processo_completo.zip").is_file())
            self.assertEqual((output / "processo_completo.md").read_bytes()[:3], b"\xef\xbb\xbf")
            self.assertEqual(validate_links(output), [])


if __name__ == "__main__":
    unittest.main()
