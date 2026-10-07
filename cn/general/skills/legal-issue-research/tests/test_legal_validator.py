# -*- coding: utf-8 -*-
"""法律检索校验机制测试（效力/时效/引用准确性——W3-W4 ⭐）。"""
import os
import sys

_SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

import pytest

from legal_validator import (
    SOURCE_LEVELS, validate_source_level, check_timeliness,
    validate_citation, normalize_law_name, validate_report,
)


# ── R1: 法源效力层级 ──
def test_source_levels_defined():
    """法源层级定义（宪法→法律→...→典型案例）。"""
    assert "宪法" in SOURCE_LEVELS or "constitution" in SOURCE_LEVELS
    assert len(SOURCE_LEVELS) >= 6


def test_validate_source_level_law():
    """法律 > 行政法规（效力排序正确）。"""
    r = validate_source_level("法律", "行政法规")
    assert r["higher"] == "法律"


def test_validate_source_level_unknown():
    """未知法源类型 → 提示（不抛异常）。"""
    r = validate_source_level("未知类型", "法律")
    assert r is not None


# ── R2: 新旧法时效校验 ──
def test_check_timeliness_same_law():
    """同法律新旧版本 → 提示以新法为准。"""
    r = check_timeliness([
        {"name": "民法典", "year": 2020, "status": "现行有效"},
        {"name": "民法通则", "year": 1986, "status": "已废止"},
    ])
    assert r["has_outdated"] is True


def test_check_timeliness_all_valid():
    """全部现行有效 → 无过期提示。"""
    r = check_timeliness([
        {"name": "民法典", "year": 2020, "status": "现行有效"},
    ])
    assert r["has_outdated"] is False


# ── R3: 引用准确性校验 ──
def test_validate_citation_standard():
    """标准法条引用格式 → 通过。"""
    r = validate_citation("《中华人民共和国民法典》第一千零六十五条")
    assert r["ok"] is True


def test_validate_citation_simplified():
    """简化引用（《民法典》第1065条）→ 通过（通用格式）。"""
    r = validate_citation("《民法典》第1065条")
    assert r["ok"] is True


def test_validate_citation_empty():
    """空引用 → 不通过。"""
    r = validate_citation("")
    assert r["ok"] is False


# ── R4: 法名规范化 ──
def test_normalize_law_name():
    """法名规范化（简称→全称）。"""
    assert normalize_law_name("民法典") == "中华人民共和国民法典"
    assert normalize_law_name("刑法") == "中华人民共和国刑法"


def test_normalize_law_name_unknown():
    """未知法名 → 原样返回。"""
    assert normalize_law_name("某个未知法") == "某个未知法"


# ── R5: 报告级校验 ──
def test_validate_report():
    """法律检索报告校验（综合效力/时效/引用）。"""
    report = {
        "sources": [
            {"name": "民法典", "type": "法律", "year": 2020, "status": "现行有效"},
            {"name": "民法通则", "type": "法律", "year": 1986, "status": "已废止"},
        ],
        "citations": ["《民法典》第1065条", "《民法通则》第1条"],
    }
    r = validate_report(report)
    assert r["ok"] is False, "含已废止法源应提示"
    assert r["issues"], "应列出问题"
