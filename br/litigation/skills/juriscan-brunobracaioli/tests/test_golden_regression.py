"""Golden regression suite for juriscan.

Runs both the legacy and (eventually) agents pipelines against synthetic
fixtures in tests/golden/ and asserts structural invariants.

Phase 0 scope: only legacy pipeline. Invariants are intentionally conservative
so they pass with the current regex chunker. Agents-only invariants (e.g.
art. 942 detection) live in separate `expected_art_942.json` files and are
gated by the pipeline mode.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
GOLDEN_ROOT = REPO_ROOT / "tests" / "golden"
EXTRACT_SCRIPT = REPO_ROOT / "scripts" / "extract_and_chunk.py"


def _discover_fixtures() -> list[Path]:
    fixtures = []
    for child in sorted(GOLDEN_ROOT.iterdir()):
        if not child.is_dir():
            continue
        if child.name.startswith("_"):
            continue
        if (child / "input.pdf").exists() and (child / "expected_invariants.json").exists():
            fixtures.append(child)
    return fixtures


FIXTURES = _discover_fixtures()


@pytest.fixture(scope="module")
def legacy_outputs(tmp_path_factory) -> dict[str, Path]:
    """Run the legacy extract_and_chunk pipeline against every fixture.

    Returns a map { fixture_name: output_dir }.
    """
    out: dict[str, Path] = {}
    root = tmp_path_factory.mktemp("golden_legacy")
    for fixture in FIXTURES:
        out_dir = root / fixture.name
        out_dir.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            [
                sys.executable,
                str(EXTRACT_SCRIPT),
                "--input",
                str(fixture / "input.pdf"),
                "--output",
                str(out_dir),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"extract_and_chunk failed for {fixture.name}:\n"
            f"stdout={result.stdout}\nstderr={result.stderr}"
        )
        out[fixture.name] = out_dir
    return out


def _load_index(out_dir: Path) -> dict:
    index_path = out_dir / "index.json"
    assert index_path.exists(), f"missing index.json in {out_dir}"
    return json.loads(index_path.read_text(encoding="utf-8"))


def _load_all_chunks_text(out_dir: Path) -> str:
    chunks_dir = out_dir / "chunks"
    assert chunks_dir.exists(), f"missing chunks/ in {out_dir}"
    parts = []
    for chunk_file in sorted(chunks_dir.iterdir()):
        if chunk_file.suffix == ".txt":
            parts.append(chunk_file.read_text(encoding="utf-8"))
    return "\n".join(parts)


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda f: f.name)
def test_golden_legacy_pipeline(fixture: Path, legacy_outputs: dict[str, Path]) -> None:
    """Run legacy pipeline and validate against expected_invariants.json."""
    invariants = json.loads((fixture / "expected_invariants.json").read_text(encoding="utf-8"))
    if "legacy" not in invariants.get("pipeline_compat", ["legacy"]):
        pytest.skip(f"{fixture.name} not marked legacy-compatible")

    out_dir = legacy_outputs[fixture.name]
    index = _load_index(out_dir)
    all_text = _load_all_chunks_text(out_dir)

    # Extraction lower bound
    min_chars = invariants.get("extraction", {}).get("min_chars")
    if min_chars is not None:
        assert len(all_text) >= min_chars, (
            f"extracted text too short: {len(all_text)} < {min_chars}"
        )

    # Chunk count range
    chunk_min = invariants.get("chunks", {}).get("min_count")
    chunk_max = invariants.get("chunks", {}).get("max_count")
    chunks = index.get("chunks") or index.get("pieces") or []
    chunk_count = len(chunks)
    if chunk_min is not None:
        assert chunk_count >= chunk_min, (
            f"too few chunks: {chunk_count} < {chunk_min}"
        )
    if chunk_max is not None:
        assert chunk_count <= chunk_max, (
            f"too many chunks: {chunk_count} > {chunk_max}"
        )

    # Piece types present
    required_types = invariants.get("piece_types_present", [])
    observed_types = {
        (c.get("tipo_peca") or c.get("label") or "").upper()
        for c in chunks
    }
    for required in required_types:
        # Normalize accents for comparison — legacy labels may vary
        required_upper = required.upper()
        matched = any(required_upper in obs for obs in observed_types)
        assert matched, (
            f"required piece type not found: {required} "
            f"(observed: {sorted(observed_types)})"
        )

    # Text must contain
    for needle in invariants.get("text_must_contain", []):
        assert needle in all_text, f"text missing required substring: {needle!r}"

    # Text must NOT contain
    for needle in invariants.get("text_must_not_contain", []):
        assert needle not in all_text, (
            f"text contains forbidden substring: {needle!r}"
        )


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda f: f.name)
def test_golden_art942_gate_is_skipped_in_legacy(fixture: Path) -> None:
    """Ensure agents-only invariants (art_942) are properly gated.

    In Phase 0 we only run the legacy pipeline. Any fixture that has an
    expected_art_942.json file MUST declare skip_when_pipeline=legacy,
    otherwise the gate is misconfigured.
    """
    art942_path = fixture / "expected_art_942.json"
    if not art942_path.exists():
        pytest.skip("no art942 invariant for this fixture")

    invariant = json.loads(art942_path.read_text(encoding="utf-8"))
    assert invariant.get("skip_when_pipeline") == "legacy", (
        f"{fixture.name}: expected_art_942.json must declare "
        f"skip_when_pipeline=legacy during Phase 0 "
        f"(got: {invariant.get('skip_when_pipeline')})"
    )
    assert invariant.get("required_when_pipeline") == "agents", (
        f"{fixture.name}: expected_art_942.json must declare "
        f"required_when_pipeline=agents"
    )


def test_golden_fixtures_exist() -> None:
    """Sanity check: make sure the golden suite is not empty."""
    assert len(FIXTURES) >= 2, (
        f"expected at least 2 golden fixtures, found {len(FIXTURES)}: "
        f"{[f.name for f in FIXTURES]}"
    )
    names = {f.name for f in FIXTURES}
    assert "processo_01_sintetico_simples" in names
    assert "processo_02_sintetico_art942" in names
