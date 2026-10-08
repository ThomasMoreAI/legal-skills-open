"""Tests for scripts/merge_chunk_analysis.py — Phase A.4.1."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from merge_chunk_analysis import (  # noqa: E402
    check_helper_scripts,
    discover_analysis_files,
    main,
    merge,
)


def _skeleton() -> dict:
    return {
        "analysis_version": "2.0",
        "schema_version": "2.0",
        "processo_number": "1234567-89.2024.8.26.0100",
        "total_chunks": 2,
        "chunks": [
            {
                "index": 0,
                "label": "PETIÇÃO INICIAL",
                "char_count": 8000,
                "chunk_file": "chunks/00-peticao-inicial.txt",
                "_pending_analysis": True,
            },
            {
                "index": 1,
                "label": "SENTENÇA",
                "char_count": 5000,
                "chunk_file": "chunks/01-sentenca.txt",
                "_pending_analysis": True,
            },
        ],
    }


def _write_analysis(chunks_dir: Path, idx: str, data: dict) -> Path:
    p = chunks_dir / f"{idx}.analysis.json"
    p.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return p


def _sample_peticao(index: int = 0) -> dict:
    return {
        "index": index,
        "tipo_peca": "PETIÇÃO INICIAL",
        "partes": {"autor": ["João"], "reu": ["Empresa X Ltda"]},
        "pedidos": ["Condenação em R$ 50.000"],
        "valores": {"causa": "R$ 50.000,00"},
        "fatos_relevantes": ["Contrato descumprido"],
        "artigos_lei": ["CC art. 389"],
    }


def _sample_sentenca(index: int = 1) -> dict:
    return {
        "index": index,
        "tipo_peca": "SENTENÇA",
        "decisao": "JULGO PROCEDENTE em parte",
        "valores": {"condenacao": "R$ 30.000,00"},
        "fatos_relevantes": ["Perícia confirmou inadimplemento"],
        "artigos_lei": ["CC art. 475"],
    }


def _load_schema() -> dict:
    return json.loads(
        (REPO_ROOT / "references" / "chunk_analysis_schema.json").read_text(encoding="utf-8")
    )


# ---------- discover_analysis_files ----------

def test_discover_numeric_only(tmp_path):
    (tmp_path / "00.analysis.json").write_text("{}")
    (tmp_path / "01.analysis.json").write_text("{}")
    (tmp_path / "02.analysis.json").write_text("{}")
    (tmp_path / "other.txt").write_text("ignored")
    found = discover_analysis_files(tmp_path)
    assert set(found.keys()) == {"00", "01", "02"}


def test_discover_with_suffixes(tmp_path):
    (tmp_path / "02a.analysis.json").write_text("{}")
    (tmp_path / "02b.analysis.json").write_text("{}")
    found = discover_analysis_files(tmp_path)
    assert "02a" in found
    assert "02b" in found


def test_discover_empty(tmp_path):
    found = discover_analysis_files(tmp_path)
    assert found == {}


def test_discover_missing_dir(tmp_path):
    found = discover_analysis_files(tmp_path / "nope")
    assert found == {}


# ---------- merge() core ----------

def test_merge_complete_set(tmp_path):
    skel = _skeleton()
    _write_analysis(tmp_path, "00", _sample_peticao(0))
    _write_analysis(tmp_path, "01", _sample_sentenca(1))

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert errors == []
    assert len(merged["chunks"]) == 2

    c0 = merged["chunks"][0]
    assert c0["tipo_peca"] == "PETIÇÃO INICIAL"
    assert c0["pedidos"] == ["Condenação em R$ 50.000"]
    assert c0["chunk_file"] == "chunks/00-peticao-inicial.txt"
    assert "_pending_analysis" not in c0

    c1 = merged["chunks"][1]
    assert c1["tipo_peca"] == "SENTENÇA"
    assert c1["decisao"] == "JULGO PROCEDENTE em parte"


def test_merge_missing_file_is_error(tmp_path):
    skel = _skeleton()
    _write_analysis(tmp_path, "00", _sample_peticao(0))
    # Missing "01"

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert len(errors) == 1
    assert "chunk[1]" in errors[0]
    assert "01.analysis.json" in errors[0]


def test_merge_schema_invalid_rejected(tmp_path):
    skel = _skeleton()
    bad = {"index": 0, "tipo_peca": "INVALID_TYPE"}
    _write_analysis(tmp_path, "00", bad)
    _write_analysis(tmp_path, "01", _sample_sentenca(1))

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert any("INVALID_TYPE" in e or "enum" in e.lower() for e in errors)


def test_merge_missing_required_field_rejected(tmp_path):
    skel = _skeleton()
    bad = {"tipo_peca": "PETIÇÃO INICIAL"}  # missing "index"
    _write_analysis(tmp_path, "00", bad)
    _write_analysis(tmp_path, "01", _sample_sentenca(1))

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert any("index" in e.lower() for e in errors)


def test_merge_split_semantic_creates_additional_entries(tmp_path):
    """Chunk 01 physically contains both SENTENÇA and a pending APELAÇÃO.
    User creates 01.analysis.json (SENTENÇA) and 01a.analysis.json (APELAÇÃO).
    After v3.1.1 fix, the APELAÇÃO is inserted right after SENTENÇA and
    all indices are renumbered sequentially.
    """
    skel = _skeleton()
    _write_analysis(tmp_path, "00", _sample_peticao(0))
    _write_analysis(tmp_path, "01", _sample_sentenca(1))

    apelacao_split = {
        "index": "1a",
        "tipo_peca": "APELAÇÃO",
        "pedidos": ["Reforma integral da sentença"],
        "chunk_file_override": "chunks/01-sentenca.txt",
    }
    _write_analysis(tmp_path, "01a", apelacao_split)

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert errors == []
    assert len(merged["chunks"]) == 3
    # Order: PETIÇÃO (0), SENTENÇA (1), APELAÇÃO (2 — inserted after parent 1)
    assert merged["chunks"][0]["tipo_peca"] == "PETIÇÃO INICIAL"
    assert merged["chunks"][1]["tipo_peca"] == "SENTENÇA"
    apelacao = merged["chunks"][2]
    assert apelacao["tipo_peca"] == "APELAÇÃO"
    assert apelacao["index"] == 2  # Renumbered to integer
    # Split-semantic preserves the parent's physical file
    assert apelacao["chunk_file"] == "chunks/01-sentenca.txt"


def test_merge_drops_pending_markers(tmp_path):
    skel = _skeleton()
    _write_analysis(tmp_path, "00", _sample_peticao(0))
    _write_analysis(tmp_path, "01", _sample_sentenca(1))

    found = discover_analysis_files(tmp_path)
    merged, _errors = merge(skel, found, _load_schema())

    for ch in merged["chunks"]:
        assert "_pending_analysis" not in ch


def test_merge_updates_total_chunks(tmp_path):
    skel = _skeleton()
    _write_analysis(tmp_path, "00", _sample_peticao(0))
    _write_analysis(tmp_path, "01", _sample_sentenca(1))
    split = {"index": "1a", "tipo_peca": "APELAÇÃO"}
    _write_analysis(tmp_path, "01a", split)

    found = discover_analysis_files(tmp_path)
    merged, _errors = merge(skel, found, _load_schema())

    assert merged["total_chunks"] == 3


# ---------- check_helper_scripts ----------

def test_helper_script_warning(tmp_path):
    (tmp_path / "build_analyzed.py").write_text("# hardcode enrichments")
    warnings = check_helper_scripts(tmp_path, tmp_path)
    assert any("build_analyzed.py" in w for w in warnings)


def test_no_helper_script_no_warning(tmp_path):
    warnings = check_helper_scripts(tmp_path, tmp_path)
    assert warnings == []


# ---------- CLI ----------

def test_cli_success(tmp_path):
    chunks_dir = tmp_path / "chunks"
    chunks_dir.mkdir()
    skel_path = tmp_path / "analyzed.json"
    skel_path.write_text(json.dumps(_skeleton()), encoding="utf-8")

    _write_analysis(chunks_dir, "00", _sample_peticao(0))
    _write_analysis(chunks_dir, "01", _sample_sentenca(1))

    out = tmp_path / "merged.json"
    rc = main([
        "--analyzed", str(skel_path),
        "--chunks-dir", str(chunks_dir),
        "--output", str(out),
    ])
    assert rc == 0
    data = json.loads(out.read_text(encoding="utf-8"))
    assert len(data["chunks"]) == 2
    assert data["chunks"][0]["tipo_peca"] == "PETIÇÃO INICIAL"


def test_cli_no_analysis_files(tmp_path):
    chunks_dir = tmp_path / "chunks"
    chunks_dir.mkdir()
    skel_path = tmp_path / "analyzed.json"
    skel_path.write_text(json.dumps(_skeleton()), encoding="utf-8")

    rc = main([
        "--analyzed", str(skel_path),
        "--chunks-dir", str(chunks_dir),
        "--output", str(tmp_path / "out.json"),
    ])
    assert rc == 1


def test_merge_renumbers_to_sequential_integers(tmp_path):
    """v3.1.1 fix: after merge, all chunks[].index MUST be sequential
    integers starting at 0, even when split-semantic created entries
    with string indices like '1a'."""
    skel = _skeleton()  # 2 chunks: 0, 1
    _write_analysis(tmp_path, "00", _sample_peticao(0))
    _write_analysis(tmp_path, "01", _sample_sentenca(1))
    split = {"index": "1a", "tipo_peca": "APELAÇÃO", "pedidos": ["reforma"]}
    _write_analysis(tmp_path, "01a", split)
    split_b = {"index": "1b", "tipo_peca": "CONTRARRAZÕES"}
    _write_analysis(tmp_path, "01b", split_b)

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert errors == []
    assert len(merged["chunks"]) == 4
    # ALL indices must be integers, sequential starting at 0
    for i, ch in enumerate(merged["chunks"]):
        assert ch["index"] == i, f"chunk[{i}] has index={ch['index']!r}"
        assert isinstance(ch["index"], int)


def test_merge_split_semantic_inserts_after_parent(tmp_path):
    """v3.1.1 fix: suffixed children should appear IMMEDIATELY after their
    parent in the merged list, not appended at the end. This produces a
    natural chronological flow when split-semantic is used."""
    # Skeleton with 3 chunks: 0, 1, 2
    skel = {
        "analysis_version": "2.0",
        "chunks": [
            {"index": 0, "label": "A", "char_count": 100, "chunk_file": "chunks/00.txt"},
            {"index": 1, "label": "B", "char_count": 100, "chunk_file": "chunks/01.txt"},
            {"index": 2, "label": "C", "char_count": 100, "chunk_file": "chunks/02.txt"},
        ],
    }
    _write_analysis(tmp_path, "00", {"index": 0, "tipo_peca": "PETIÇÃO INICIAL"})
    _write_analysis(tmp_path, "01", {"index": 1, "tipo_peca": "CONTESTAÇÃO"})
    # Chunk 1 split-semantic: also contains a RÉPLICA
    _write_analysis(tmp_path, "01a", {"index": "1a", "tipo_peca": "RÉPLICA"})
    _write_analysis(tmp_path, "02", {"index": 2, "tipo_peca": "SENTENÇA"})

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert errors == []
    # Expected order: PETIÇÃO (0), CONTESTAÇÃO (1), RÉPLICA (2 — child of parent 1), SENTENÇA (3)
    tipos = [ch["tipo_peca"] for ch in merged["chunks"]]
    assert tipos == ["PETIÇÃO INICIAL", "CONTESTAÇÃO", "RÉPLICA", "SENTENÇA"]
    # And indices are all sequential integers
    assert [ch["index"] for ch in merged["chunks"]] == [0, 1, 2, 3]


def test_merge_preserves_original_index_for_debugging(tmp_path):
    skel = _skeleton()
    _write_analysis(tmp_path, "00", _sample_peticao(0))
    _write_analysis(tmp_path, "01", _sample_sentenca(1))
    _write_analysis(tmp_path, "01a", {"index": "1a", "tipo_peca": "APELAÇÃO"})

    found = discover_analysis_files(tmp_path)
    merged, _errors = merge(skel, found, _load_schema())

    # Numeric parent keeps its old int as original_index
    assert merged["chunks"][0]["original_index"] == 0
    assert merged["chunks"][1]["original_index"] == 1
    # Suffixed child keeps its string as original_index
    assert merged["chunks"][2]["original_index"] == "1a"


def test_merge_multiple_split_children_alphabetical_order(tmp_path):
    """When a parent has multiple split children (02a, 02b, 02c), they
    should be inserted in alphabetical order."""
    skel = {
        "analysis_version": "2.0",
        "chunks": [
            {"index": 2, "label": "MEGA", "char_count": 500, "chunk_file": "chunks/02.txt"},
        ],
    }
    _write_analysis(tmp_path, "02", {"index": 2, "tipo_peca": "LAUDO PERICIAL"})
    _write_analysis(tmp_path, "02c", {"index": "2c", "tipo_peca": "CONTRARRAZÕES"})
    _write_analysis(tmp_path, "02a", {"index": "2a", "tipo_peca": "SENTENÇA"})
    _write_analysis(tmp_path, "02b", {"index": "2b", "tipo_peca": "APELAÇÃO"})

    found = discover_analysis_files(tmp_path)
    merged, _errors = merge(skel, found, _load_schema())

    tipos = [ch["tipo_peca"] for ch in merged["chunks"]]
    assert tipos == ["LAUDO PERICIAL", "SENTENÇA", "APELAÇÃO", "CONTRARRAZÕES"]


def test_merge_split_semantic_inherits_primary_date_from_parent(tmp_path):
    """v3.1.2 fix: split-semantic children inherit primary_date from parent
    when not specified in their own analysis file."""
    skel = {
        "analysis_version": "2.0",
        "chunks": [
            {
                "index": 2,
                "label": "LAUDO",
                "char_count": 500,
                "chunk_file": "chunks/02.txt",
                "primary_date": "30/09/2024",
                "dates_found": ["30/09/2024", "15/09/2024"],
            },
        ],
    }
    _write_analysis(tmp_path, "02", {"index": 2, "tipo_peca": "LAUDO PERICIAL"})
    # Child has no primary_date of its own
    _write_analysis(tmp_path, "02a", {"index": "2a", "tipo_peca": "SENTENÇA"})

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert errors == []
    assert len(merged["chunks"]) == 2
    # Parent keeps its own date
    assert merged["chunks"][0]["primary_date"] == "30/09/2024"
    # Child inherits parent's date
    assert merged["chunks"][1]["primary_date"] == "30/09/2024"
    assert merged["chunks"][1]["dates_found"] == ["30/09/2024", "15/09/2024"]


def test_merge_split_semantic_override_primary_date(tmp_path):
    """v3.1.2 fix: when split-semantic child specifies its own primary_date,
    it overrides the parent's inherited date. This is the CORRECT usage
    since each piece typically has its own date."""
    skel = {
        "analysis_version": "2.0",
        "chunks": [
            {
                "index": 2,
                "label": "LAUDO",
                "char_count": 500,
                "chunk_file": "chunks/02.txt",
                "primary_date": "30/09/2024",
            },
        ],
    }
    _write_analysis(tmp_path, "02", {"index": 2, "tipo_peca": "LAUDO PERICIAL"})
    _write_analysis(tmp_path, "02a", {
        "index": "2a",
        "tipo_peca": "SENTENÇA",
        "primary_date": "12/12/2024",  # override!
    })
    _write_analysis(tmp_path, "02b", {
        "index": "2b",
        "tipo_peca": "APELAÇÃO",
        "primary_date": "15/01/2025",
    })

    found = discover_analysis_files(tmp_path)
    merged, errors = merge(skel, found, _load_schema())

    assert errors == []
    assert merged["chunks"][0]["primary_date"] == "30/09/2024"  # laudo keeps
    assert merged["chunks"][1]["primary_date"] == "12/12/2024"  # sentença overrides
    assert merged["chunks"][2]["primary_date"] == "15/01/2025"  # apelação overrides


def test_merge_numeric_chunk_can_override_primary_date(tmp_path):
    """Even non-split chunks can override primary_date if the analysis file
    is more specific than what extract_and_chunk inferred."""
    skel = {
        "analysis_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "label": "DESPACHO",
                "char_count": 500,
                "chunk_file": "chunks/00.txt",
                "primary_date": "01/01/2024",  # wrong inference
            },
        ],
    }
    _write_analysis(tmp_path, "00", {
        "index": 0,
        "tipo_peca": "DESPACHO",
        "primary_date": "20/07/2024",  # correct
    })

    found = discover_analysis_files(tmp_path)
    merged, _errors = merge(skel, found, _load_schema())

    assert merged["chunks"][0]["primary_date"] == "20/07/2024"


def test_merge_output_passes_integer_index_contract(tmp_path):
    """Regression test for the v3.1.0-legacy bug: schema_validator.py
    (output_schema_v2.json) requires integer indices. The output of
    merge() must satisfy this even when split-semantic was used."""
    skel = _skeleton()
    _write_analysis(tmp_path, "00", _sample_peticao(0))
    _write_analysis(tmp_path, "01", _sample_sentenca(1))
    _write_analysis(tmp_path, "01a", {"index": "1a", "tipo_peca": "APELAÇÃO"})
    _write_analysis(tmp_path, "01b", {"index": "1b", "tipo_peca": "CONTRARRAZÕES"})

    found = discover_analysis_files(tmp_path)
    merged, _errors = merge(skel, found, _load_schema())

    # Every index must be exactly an int (not bool, not str, not None)
    for ch in merged["chunks"]:
        assert type(ch["index"]) is int  # noqa: E721


def test_merge_is_idempotent_when_index_present(tmp_path):
    """v3.1.4: re-running merge on an already-merged analyzed.json should
    rebuild the skeleton from index.json rather than failing because of
    post-merge renumbering."""
    chunks_dir = tmp_path / "chunks"
    chunks_dir.mkdir()
    # Write physical chunk text files so integrity gate is happy if invoked
    (chunks_dir / "00-peticao-inicial.txt").write_text("x" * 8000)
    (chunks_dir / "01-sentenca.txt").write_text("x" * 5000)

    # index.json mirrors the skeleton shape
    index = {
        "analysis_version": "2.0",
        "processo_number": "1234567-89.2024.8.26.0100",
        "total_chunks": 2,
        "chunks": [
            {
                "index": 0,
                "label": "PETIÇÃO INICIAL",
                "char_count": 8000,
                "chunk_file": "chunks/00-peticao-inicial.txt",
            },
            {
                "index": 1,
                "label": "SENTENÇA",
                "char_count": 5000,
                "chunk_file": "chunks/01-sentenca.txt",
            },
        ],
    }
    (tmp_path / "index.json").write_text(json.dumps(index), encoding="utf-8")

    skel_path = tmp_path / "analyzed.json"
    skel_path.write_text(json.dumps(_skeleton()), encoding="utf-8")

    _write_analysis(chunks_dir, "00", _sample_peticao(0))
    _write_analysis(chunks_dir, "01", {"index": 1, "tipo_peca": "SENTENÇA"})

    out = tmp_path / "analyzed.json"
    # First merge
    rc = main(["--analyzed", str(skel_path), "--chunks-dir", str(chunks_dir), "--output", str(out)])
    assert rc == 0

    # Second merge — should detect post-merge state and rebuild from index.json
    rc2 = main(["--analyzed", str(out), "--chunks-dir", str(chunks_dir), "--output", str(out)])
    assert rc2 == 0
    data = json.loads(out.read_text(encoding="utf-8"))
    assert len(data["chunks"]) == 2
    assert data["chunks"][0]["tipo_peca"] == "PETIÇÃO INICIAL"


def test_merge_idempotent_with_split_semantic(tmp_path):
    """v3.1.4: idempotency works even when split-semantic creates extra rows."""
    chunks_dir = tmp_path / "chunks"
    chunks_dir.mkdir()
    (chunks_dir / "00-peticao-inicial.txt").write_text("x" * 8000)
    (chunks_dir / "01-sentenca.txt").write_text("x" * 5000)

    index = {
        "analysis_version": "2.0",
        "processo_number": "1234567-89.2024.8.26.0100",
        "total_chunks": 2,
        "chunks": [
            {"index": 0, "label": "PETIÇÃO INICIAL", "char_count": 8000, "chunk_file": "chunks/00-peticao-inicial.txt"},
            {"index": 1, "label": "SENTENÇA", "char_count": 5000, "chunk_file": "chunks/01-sentenca.txt"},
        ],
    }
    (tmp_path / "index.json").write_text(json.dumps(index), encoding="utf-8")

    skel_path = tmp_path / "analyzed.json"
    skel_path.write_text(json.dumps(_skeleton()), encoding="utf-8")

    _write_analysis(chunks_dir, "00", _sample_peticao(0))
    _write_analysis(chunks_dir, "01", {"index": 1, "tipo_peca": "SENTENÇA"})
    _write_analysis(chunks_dir, "01a", {
        "index": "1a",
        "tipo_peca": "ACÓRDÃO",
        "chunk_file_override": "chunks/01-sentenca.txt",
    })

    out = tmp_path / "analyzed.json"
    assert main(["--analyzed", str(skel_path), "--chunks-dir", str(chunks_dir), "--output", str(out)]) == 0
    data1 = json.loads(out.read_text(encoding="utf-8"))
    assert len(data1["chunks"]) == 3  # 2 physical + 1 split

    # Re-run merge on post-merged file — must still produce 3 chunks, not fail
    assert main(["--analyzed", str(out), "--chunks-dir", str(chunks_dir), "--output", str(out)]) == 0
    data2 = json.loads(out.read_text(encoding="utf-8"))
    assert len(data2["chunks"]) == 3
    types = [c.get("tipo_peca") for c in data2["chunks"]]
    assert "PETIÇÃO INICIAL" in types
    assert "SENTENÇA" in types
    assert "ACÓRDÃO" in types


def test_cli_allow_missing(tmp_path):
    chunks_dir = tmp_path / "chunks"
    chunks_dir.mkdir()
    skel_path = tmp_path / "analyzed.json"
    skel_path.write_text(json.dumps(_skeleton()), encoding="utf-8")

    _write_analysis(chunks_dir, "00", _sample_peticao(0))
    # Skip 01

    out = tmp_path / "merged.json"
    rc = main([
        "--analyzed", str(skel_path),
        "--chunks-dir", str(chunks_dir),
        "--output", str(out),
        "--allow-missing",
    ])
    assert rc == 0
