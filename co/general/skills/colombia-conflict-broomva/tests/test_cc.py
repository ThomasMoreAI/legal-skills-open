"""Unit tests for the colombia-conflict knowledge engine (cc.py).

Pure-stdlib, zero network. Covers the deterministic core: tokenization,
overlap scoring, the data queries, the `align` non-repetition scorer, the
catalog generator, two-tier load, AND data-integrity invariants over the
JSON datasets (so a malformed dataset fails the gate, not just bad code).
"""
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import cc  # noqa: E402

DATA = ROOT / "data"


def _j(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


# --- tokenize / scoring ------------------------------------------------------

def test_tokenize_folds_accents_and_drops_stopwords():
    toks = cc.tokenize("La reparación de las víctimas")
    assert "reparacion" in toks      # accent-folded
    assert "victimas" in toks
    assert "las" not in toks         # stopword dropped
    assert "de" not in toks


def test_tokenize_drops_short_tokens():
    assert "is" not in cc.tokenize("is a paz")
    assert "paz" in cc.tokenize("is a paz")


def test_score_overlap_bounds():
    assert cc.score_overlap(set(), {"a"}) == 0.0
    assert cc.score_overlap({"a", "b"}, {"a", "b"}) == 1.0
    assert cc.score_overlap({"a", "b"}, {"a"}) == 0.5


# --- recommendation search ---------------------------------------------------

def test_search_recommendations_by_theme():
    blocks = _j("recommendations.json")["blocks"]
    drug = cc.search_recommendations(blocks, theme="drug")
    assert len(drug) == 1
    assert drug[0]["block"] == 4


def test_search_recommendations_by_block_and_query():
    blocks = _j("recommendations.json")["blocks"]
    assert cc.search_recommendations(blocks, block=6)[0]["theme"] == "security"
    hits = cc.search_recommendations(blocks, query="ELN negotiation")
    assert any(b["block"] == 1 for b in hits)


# --- lookups -----------------------------------------------------------------

def test_lookup_all_vs_key():
    stats = _j("statistics.json")["statistics"]
    assert cc.lookup(stats, None, fields=("key", "label")) == stats
    one = cc.lookup(stats, "disappearance", fields=("key", "label"))
    assert one and any("disappearance" in r["label"].lower() for r in one)


def test_lookup_actor():
    actors = _j("actors.json")["actors"]
    para = cc.lookup(actors, "paramilitar", fields=("key", "name", "type"))
    assert para and para[0]["key"] == "paramilitaries"


# --- align (the non-repetition scorer) --------------------------------------

def test_align_routes_drug_policy_to_block4():
    blocks = _j("recommendations.json")["blocks"]
    ranked = cc.align_text(
        "legalize cannabis and regulate coca cultivation as a public-health drug policy",
        blocks)
    assert ranked, "expected at least one matching block"
    assert ranked[0]["block"] == 4
    assert 0.0 < ranked[0]["score"] <= 1.0


def test_align_routes_land_to_territorial_block():
    blocks = _j("recommendations.json")["blocks"]
    ranked = cc.align_text("an agrarian reform and land restitution program for rural campesinos", blocks)
    assert any(b["theme"] == "territorial-peace" for b in ranked)


def test_align_unrelated_returns_empty():
    blocks = _j("recommendations.json")["blocks"]
    assert cc.align_text("quarterly javascript frontend refactor", blocks) == []


def test_contrary_flags_catches_fumigation_as_opposed_to_block4():
    # A proposal the report recommends ENDING must be flagged CONTRARY, not aligned.
    flags = cc.contrary_flags("increase aerial glyphosate fumigation and forced coca eradication")
    blocks = {f["block"] for f in flags}
    assert 4 in blocks
    assert any("glyphosate" in f["contrary_tokens"] or "fumigation" in f["contrary_tokens"]
               for f in flags)


def test_contrary_flags_empty_for_aligned_proposal():
    assert cc.contrary_flags("support campesinos cocaleros with voluntary crop substitution") == []


# --- catalog + two-tier load -------------------------------------------------

def test_build_catalog_mentions_each_dataset():
    cat = cc.build_catalog(
        _j("statistics.json")["statistics"], _j("actors.json")["actors"],
        _j("recommendations.json")["blocks"], _j("concepts.json")["concepts"],
        [("digests/x.md", "X Volume")])
    for needle in ("stat:`homicides`", "actor:`paramilitaries`", "rec-block:4", "concept:`paz grande`", "page:digests/x.md"):
        assert needle in cat, needle


def test_two_tier_load_finds_topic():
    res = cc.two_tier_load("desaparición forzada víctimas", limit=6)
    assert res["topic"]
    assert res["tier1"] or res["tier2"], "expected some retrieval hit"


def test_two_tier_load_respects_total_limit():
    # limit is a TOTAL budget across both tiers (CodeRabbit #67): tier1+tier2 <= limit.
    for lim in (1, 3, 6):
        res = cc.two_tier_load("guerra conflicto víctimas tierra", limit=lim)
        assert len(res["tier1"]) + len(res["tier2"]) <= lim


def test_two_tier_load_clamps_nonpositive_limit():
    res = cc.two_tier_load("exilio", limit=0)
    assert len(res["tier1"]) + len(res["tier2"]) <= 1


def test_load_cli_rejects_nonpositive_n():
    # `-n 0` / `-n -1` must be rejected by argparse, not silently negative-sliced.
    parser = cc.build_parser()
    for bad in ("0", "-1"):
        with pytest.raises(SystemExit):
            parser.parse_args(["load", "x", "-n", bad])


# --- data integrity invariants ----------------------------------------------

def test_recommendations_have_eight_blocks_and_unique_numbers():
    blocks = _j("recommendations.json")["blocks"]
    assert len(blocks) == 8
    nums = [b["block"] for b in blocks]
    assert nums == sorted(nums) and len(set(nums)) == 8
    for b in blocks:
        assert b["recommendations"] and b["theme"] and b["title"] and b["keywords"]


def test_statistics_have_required_fields():
    for s in _j("statistics.json")["statistics"]:
        assert s.get("key") and s.get("label")
        assert "documented" in s and "period" in s


def test_actors_have_principal_responsibility():
    for a in _j("actors.json")["actors"]:
        assert a.get("key") and a.get("name")
        assert a.get("principal_responsibility")


def test_concepts_have_term_and_gloss():
    for c in _j("concepts.json")["concepts"]:
        assert c.get("term") and c.get("gloss")


def test_all_datasets_are_valid_json():
    for name in ("statistics.json", "actors.json", "recommendations.json", "concepts.json"):
        assert isinstance(_j(name), dict)


def test_fulltext_corpus_present():
    gz = list((ROOT / "references" / "fulltext").glob("*.txt.gz"))
    assert len(gz) == 24, "expected 24 gzipped volume texts"


def test_search_fulltext_finds_known_term():
    # 'Marquetalia' (FARC founding myth) is verbatim in the historical narrative.
    hits = cc.search_fulltext("Marquetalia", limit=5)
    assert hits, "expected a verbatim full-text hit"
    assert any("marquetalia" in h["snippet"].lower() for h in hits)
    assert all(0.0 < h["score"] <= 1.0 for h in hits)


def test_search_fulltext_respects_limit():
    hits = cc.search_fulltext("guerra víctimas tierra conflicto", limit=3)
    assert len(hits) <= 3


def test_search_fulltext_empty_query_returns_empty():
    assert cc.search_fulltext("", limit=5) == []


def test_source_manifest_valid():
    m = json.loads((ROOT / "sources" / "MANIFEST.json").read_text(encoding="utf-8"))
    dl = m["downloads"]
    assert len(dl) == 11 and m["_meta"]["units"] == 11
    for d in dl:
        assert d["url"].startswith("https://") and d["filename"]
        assert d["sha256"] and len(d["sha256"]) == 64  # all hashed
    assert sum(1 for d in dl if d["filename"].endswith(".zip")) == 1


def test_committed_catalog_is_not_stale():
    """The committed references/knowledge-index.md must equal a fresh build —
    so `cc.py index --check` is green on a fresh clone (CI gate honesty)."""
    fresh = cc.build_catalog(
        _j("statistics.json")["statistics"], _j("actors.json")["actors"],
        _j("recommendations.json")["blocks"], _j("concepts.json")["concepts"],
        cc._digest_headers())
    committed = (ROOT / "references" / "knowledge-index.md").read_text(encoding="utf-8")
    assert committed == fresh, "knowledge-index.md is stale — run `python3 scripts/cc.py index`"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
