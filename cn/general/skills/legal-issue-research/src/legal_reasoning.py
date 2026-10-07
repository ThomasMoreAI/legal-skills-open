# -*- coding: utf-8 -*-
"""legal_reasoning — 法律推理方法模块化（W3-W4 差距补齐 ⭐）。

对标 legalaiskill 推理类 skills：归纳/演绎/类比/溯因四类法律推理。
为检索报告的法律分析环节提供结构化推理框架。
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

# 四类推理方法
REASONING_METHODS = {
    "deductive": {
        "zh": "演绎推理",
        "desc": "大前提（法律规范）→ 小前提（案件事实）→ 结论（法律适用）。三段论。",
        "use_when": "法条适用、构成要件判断、法律后果推导",
    },
    "inductive": {
        "zh": "归纳推理",
        "desc": "多个个案 → 一般规则。类案裁判倾向总结。",
        "use_when": "类案裁判规则总结、司法实践倾向分析",
    },
    "analogical": {
        "zh": "类比推理",
        "desc": "相似案例 → 相似处理。关键相似点对比。",
        "use_when": "类案检索、先例参照、相似事实适用",
    },
    "abductive": {
        "zh": "溯因推理",
        "desc": "结果（事实）→ 最可能原因（法律事实假设）。多个假设择优。",
        "use_when": "事实认定、举证责任判断、因果关系推定",
    },
}


def deductive_analysis(major: str, minor: str,
                       conclusion: str) -> Dict[str, Any]:
    """演绎推理分析（三段论）。"""
    return {
        "method": "deductive",
        "structure": "大前提→小前提→结论",
        "major": major,
        "minor": minor,
        "conclusion": conclusion,
        "valid": bool(major and minor and conclusion),
        "note": f"大前提「{major}」+ 小前提「{minor}」⇒ 结论「{conclusion}」",
    }


def inductive_analysis(cases: List[str], rule: str) -> Dict[str, Any]:
    """归纳推理分析（个案→规则）。"""
    n = len(cases)
    confidence = min(0.9, 0.4 + 0.15 * n) if n else None
    return {
        "method": "inductive",
        "cases_count": n,
        "rule": rule,
        "confidence": confidence,
        "note": f"{n} 个类案支持规则「{rule}」——样本越多置信度越高（{confidence:.2f}）",
    }


def analogical_analysis(base_case: str, target_case: str,
                        similarity: str) -> Dict[str, Any]:
    """类比推理分析（相似案例→适用）。"""
    return {
        "method": "analogical",
        "base_case": base_case,
        "target_case": target_case,
        "similarity": similarity,
        "applicable": bool(similarity),
        "note": f"类案「{base_case}」与本案「{target_case}」关键相似点：{similarity}——可参照适用",
    }


def abductive_analysis(fact: str,
                       hypotheses: List[str]) -> Dict[str, Any]:
    """溯因推理分析（结果→最可能原因）。"""
    hypotheses = [h for h in hypotheses if h]
    return {
        "method": "abductive",
        "fact": fact,
        "hypotheses": hypotheses,
        "best": hypotheses[0] if hypotheses else "",
        "note": (f"对事实「{fact}」形成 {len(hypotheses)} 个假设，"
                 f"首选「{hypotheses[0] if hypotheses else '无'}」——需证据支持"),
    }


def recommend_method(question_type: str) -> str:
    """按问题类型推荐推理方法。"""
    q = question_type or ""
    if "法条" in q or "适用" in q or "要件" in q:
        return "deductive"
    if "类案" in q or "相似" in q or "参照" in q:
        return "analogical"
    if "倾向" in q or "总结" in q or "裁判规则" in q:
        return "inductive"
    if "原因" in q or "事实" in q or "举证" in q:
        return "abductive"
    return "deductive"
