# -*- coding: utf-8 -*-
"""法律检索补齐测试：案例关键词检索 + 法律推理方法（W3-W4 差距补齐 ⭐）。"""
import os
import sys

_SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

import pytest

from case_retriever import (
    extract_case_keywords, build_case_query, CASE_CAUSES,
)
from legal_reasoning import (
    REASONING_METHODS, deductive_analysis, inductive_analysis,
    analogical_analysis, abductive_analysis, recommend_method,
)


# ── R1: 案例关键词提取（案由/争点/事实）──
def test_extract_case_keywords():
    """从案情描述提取检索关键词。"""
    text = "张三与李四签订房屋买卖合同，后李四拒不交付房屋，张三起诉要求继续履行合同。"
    kw = extract_case_keywords(text)
    assert kw, "应提取关键词"
    assert any("合同" in k for k in kw) or any("房屋" in k for k in kw), "应含核心事实词"


def test_extract_case_keywords_empty():
    """空案情 → 空关键词（不抛异常）。"""
    assert extract_case_keywords("") == []


# ── R2: 案例检索查询构建 ──
def test_build_case_query():
    """关键词 → 检索查询（含案由提示）。"""
    q = build_case_query(["房屋买卖", "拒不交付"])
    assert q, "应构建查询"
    assert "房屋" in q, "应含关键词"


# ── R3: 案由词表 ──
def test_case_causes_defined():
    """常见案由词表（合同/侵权/婚姻/劳动等）。"""
    assert len(CASE_CAUSES) >= 8
    assert any("合同" in c for c in CASE_CAUSES)


# ── R4: 法律推理方法模块化 ──
def test_reasoning_methods_defined():
    """四类推理方法定义。"""
    assert "deductive" in REASONING_METHODS
    assert "inductive" in REASONING_METHODS
    assert "analogical" in REASONING_METHODS
    assert "abductive" in REASONING_METHODS


def test_deductive_analysis():
    """演绎推理（大前提→小前提→结论）。"""
    r = deductive_analysis(
        major="合同依法成立后受法律保护",
        minor="本案合同已依法成立",
        conclusion="本案合同受法律保护")
    assert r["valid"] is True
    assert r["structure"] == "大前提→小前提→结论"


def test_inductive_analysis():
    """归纳推理（个案→规则）。"""
    r = inductive_analysis(
        cases=["案例A：格式条款无效", "案例B：格式条款无效", "案例C：格式条款无效"],
        rule="格式条款未尽提示义务无效")
    assert r["confidence"] is not None


def test_analogical_analysis():
    """类比推理（相似案例→适用）。"""
    r = analogical_analysis(
        base_case="类案：借名买房被认定有效",
        target_case="本案：借名买车",
        similarity="均为借名登记财产")
    assert r["applicable"] is True


def test_abductive_analysis():
    """溯因推理（结果→最可能原因）。"""
    r = abductive_analysis(
        fact="合同无法履行",
        hypotheses=["不可抗力", "一方违约", "标的灭失"])
    assert r["hypotheses"]
    assert r["best"]


def test_recommend_method():
    """推理方法推荐（按问题类型）。"""
    assert recommend_method("法条适用") == "deductive"
    assert recommend_method("类案检索") == "analogical"
