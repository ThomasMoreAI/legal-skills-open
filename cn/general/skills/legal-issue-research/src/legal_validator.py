# -*- coding: utf-8 -*-
"""legal_validator — 法律检索校验机制（W3-W4 ⭐）。

三机制（升级方案 v1.0）：
1. 法源效力校验：法源层级排序（宪法→法律→行政法规→司法解释→部门规章→地方性法规→指导性案例→典型案例）
2. 新旧法时效校验：识别已废止/已修订法源，提示以新法为准
3. 引用准确性校验：法条引用格式规范化（《法名》第X条）

用法（SKILL 调用）：检索报告中引用的每个法源先过本模块校验。
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

# ═══════════════════════════════════════════════════════════
# 法源层级（效力从高到低）
# ═══════════════════════════════════════════════════════════
SOURCE_LEVELS: Dict[str, int] = {
    "宪法": 0,
    "法律": 1,
    "行政法规": 2,
    "司法解释": 3,
    "部门规章": 4,
    "地方性法规": 5,
    "地方政府规章": 6,
    "指导性案例": 7,
    "典型案例": 8,
    "规范性文件": 9,
}

# 法名简称 → 全称（规范化表）
_LAW_NAMES: Dict[str, str] = {
    "民法典": "中华人民共和国民法典",
    "刑法": "中华人民共和国刑法",
    "刑事诉讼法": "中华人民共和国刑事诉讼法",
    "民事诉讼法": "中华人民共和国民事诉讼法",
    "行政诉讼法": "中华人民共和国行政诉讼法",
    "宪法": "中华人民共和国宪法",
    "劳动法": "中华人民共和国劳动法",
    "劳动合同法": "中华人民共和国劳动合同法",
    "公司法": "中华人民共和国公司法",
    "合同法": "中华人民共和国合同法",
    "婚姻法": "中华人民共和国婚姻法",
    "继承法": "中华人民共和国继承法",
    "著作权法": "中华人民共和国著作权法",
    "商标法": "中华人民共和国商标法",
    "专利法": "中华人民共和国专利法",
    "保险法": "中华人民共和国保险法",
    "证券法": "中华人民共和国证券法",
    "消费者权益保护法": "中华人民共和国消费者权益保护法",
    "食品安全法": "中华人民共和国食品安全法",
    "环境保护法": "中华人民共和国环境保护法",
}


def validate_source_level(a: str, b: str) -> Dict[str, Any]:
    """法源效力校验：比较两个法源类型的效力高低。

    Returns: {"higher": 效力更高者, "a_level": int, "b_level": int}
    """
    la = SOURCE_LEVELS.get(a, 99)
    lb = SOURCE_LEVELS.get(b, 99)
    return {
        "higher": a if la < lb else b if lb < la else "同层级",
        "a_level": la if a in SOURCE_LEVELS else None,
        "b_level": lb if b in SOURCE_LEVELS else None,
        "note": f"{a}（效力{la}）vs {b}（效力{lb}）——{'前者优先' if la < lb else '后者优先' if lb < la else '同层级，适用一般/特别规定规则'}",
    }


def check_timeliness(sources: List[Dict[str, Any]]) -> Dict[str, Any]:
    """新旧法时效校验：识别已废止/已修订法源。

    sources: [{"name": "法名", "year": 2020, "status": "现行有效/已废止/已修订"}, ...]

    Returns: {"has_outdated": bool, "outdated": [...], "notes": [...]}
    """
    outdated = []
    for s in sources:
        status = s.get("status", "")
        if status in ("已废止", "已失效", "废止"):
            outdated.append({
                "name": s.get("name", ""),
                "year": s.get("year", ""),
                "status": status,
                "note": f"《{s.get('name', '')}》已废止——若同领域有新法，应以新法为准并注明时效节点",
            })
    return {
        "has_outdated": bool(outdated),
        "outdated": outdated,
        "notes": [o["note"] for o in outdated],
    }


def normalize_law_name(name: str) -> str:
    """法名规范化（简称→全称）。"""
    n = (name or "").strip()
    # 已有书名号 → 去书名号查表
    bare = n.strip("《》")
    if bare in _LAW_NAMES:
        return _LAW_NAMES[bare]
    # 无书名号简称
    if n in _LAW_NAMES:
        return _LAW_NAMES[n]
    return n


def validate_citation(citation: str) -> Dict[str, Any]:
    """引用准确性校验：法条引用格式检查。

    标准格式：《中华人民共和国民法典》第一千零六十五条 或 《民法典》第1065条。
    """
    c = (citation or "").strip()
    if not c:
        return {"ok": False, "issue": "空引用"}
    # 基本格式：《法名》第X条
    if "《" in c and "》" in c and "第" in c and "条" in c:
        # 提取法名规范化
        m = re.search(r"《([^》]+)》", c)
        law = m.group(1) if m else ""
        normalized = normalize_law_name(law)
        if normalized != law:
            return {"ok": True, "normalized": c.replace(law, normalized),
                    "note": f"法名已规范化：{law} → {normalized}"}
        return {"ok": True, "normalized": c}
    if "《" in c and "》" in c:
        return {"ok": True, "normalized": c, "note": "引用含法名但未含条号——建议补充具体条文"}
    return {"ok": False, "issue": "引用格式不标准（缺少书名号或条号）", "input": c}


def validate_report(report: Dict[str, Any]) -> Dict[str, Any]:
    """法律检索报告综合校验（效力 + 时效 + 引用）。

    report: {"sources": [...], "citations": [...]}
    """
    issues: List[str] = []
    # 1. 时效校验
    sources = report.get("sources", [])
    timeliness = check_timeliness(sources)
    if timeliness["has_outdated"]:
        issues.extend(timeliness["notes"])
    # 2. 引用校验
    for cit in report.get("citations", []):
        r = validate_citation(cit)
        if not r["ok"]:
            issues.append(f"引用问题：{cit}——{r.get('issue', '')}")
    # 3. 效力冲突提示（同领域多法源）
    if len(sources) >= 2:
        for i in range(len(sources)):
            for j in range(i + 1, len(sources)):
                a, b = sources[i], sources[j]
                cmp_r = validate_source_level(a.get("type", ""), b.get("type", ""))
                if cmp_r["higher"] == "同层级":
                    issues.append(f"同层级法源：《{a.get('name', '')}》与《{b.get('name', '')}》——需按一般/特别规定规则判断适用")
    return {"ok": not issues, "issues": issues}
