# -*- coding: utf-8 -*-
"""case_retriever — 案例关键词检索（W3-W4 差距补齐 ⭐）。

对标北大法宝 MCP case-retrieval：案由/争点/事实 → 类案检索。
把长案情收敛成可检索的案由词、争点词、事实词，构建检索查询。
"""

from __future__ import annotations

import re
from typing import List

# 常见案由词表（中国民事/刑事/行政案由）
CASE_CAUSES: List[str] = [
    "合同纠纷", "买卖合同纠纷", "房屋买卖合同纠纷", "借款合同纠纷",
    "劳动争议", "劳动合同纠纷", "追索劳动报酬纠纷",
    "侵权责任纠纷", "机动车交通事故责任纠纷", "医疗损害责任纠纷",
    "婚姻家庭纠纷", "离婚纠纷", "抚养纠纷", "继承纠纷",
    "物权纠纷", "相邻关系纠纷", "所有权确认纠纷",
    "公司纠纷", "股权转让纠纷", "损害公司利益责任纠纷",
    "著作权侵权纠纷", "商标权侵权纠纷", "专利权侵权纠纷",
    "民间借贷纠纷", "租赁合同纠纷", "承揽合同纠纷", "建设工程合同纠纷",
    "保险合同纠纷", "运输合同纠纷", "服务合同纠纷",
    "不当得利纠纷", "无因管理纠纷", "名誉权纠纷", "隐私权纠纷",
    "行政处罚", "行政复议", "行政许可",
    "故意伤害罪", "盗窃罪", "诈骗罪", "贪污贿赂",
]

# 争点/事实关键词模式
_KEYWORD_PATTERNS = [
    r"(不履行|拒绝履行|迟延履行|违约|解除合同|继续履行|赔偿损失)",
    r"(拖欠|拒付|逾期|未支付|给付)",
    r"(侵[害犯]|致[伤死亡]|造成损失|损害)",
    r"(抚养|赡养|扶养|监护|探望)",
    r"(继承|遗嘱|遗产|析产)",
    r"(股权|出资|分红|股东会|董事会)",
    r"(解除|撤销|变更|确认|无效)",
    r"(工伤|劳动报酬|经济补偿|社会保险|竞业限制)",
    r"(借名|抵押|质押|担保|保证)",
    r"(不可抗力|情势变更|重大误解|显失公平)",
]


def extract_case_keywords(text: str) -> List[str]:
    """从案情描述提取检索关键词（案由词/争点词/事实词）。"""
    t = (text or "").strip()
    if not t:
        return []
    keywords = []
    # 1. 案由词命中（支持无"纠纷"后缀的子串——"房屋买卖合同"命中"房屋买卖合同纠纷"）
    for cause in CASE_CAUSES:
        bare = cause.rstrip("纠纷").rstrip("罪")
        if cause in t or (len(bare) >= 4 and bare in t):
            keywords.append(cause)
    # 2. 争点模式命中
    for pattern in _KEYWORD_PATTERNS:
        for m in re.findall(pattern, t):
            if m not in keywords:
                keywords.append(m)
    # 3. 去重保序，限 8 个
    return keywords[:8]


def build_case_query(keywords: List[str]) -> str:
    """关键词 → 案例检索查询（含案由提示，供数据库/网页检索）。"""
    if not keywords:
        return ""
    parts = " ".join(keywords[:5])
    return f"类案检索：{parts}"


def summarize_case_results(results: List[dict]) -> List[dict]:
    """案例结果整理（案号/法院/日期/摘要/链接/样本观察）。

    results: [{"case_no", "court", "date", "summary", "url"}, ...]
    """
    out = []
    for r in results[:10]:
        out.append({
            "case_no": r.get("case_no", ""),
            "court": r.get("court", ""),
            "date": r.get("date", ""),
            "summary": r.get("summary", "")[:200],
            "url": r.get("url", ""),
        })
    return out
