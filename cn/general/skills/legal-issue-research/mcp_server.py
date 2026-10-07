# -*- coding: utf-8 -*-
"""legal_research_mcp — 法律检索 MCP server（W7 ⭐ PAEG 生态）。

MCP 标准件：独立可运行 + tools/list 动态发现 + 严格 schema + 标准化错误对象。
console_scripts: legal-research-mcp
"""

from __future__ import annotations

import json
import os
import sys

_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

try:
    from fastmcp import FastMCP
except ImportError:
    FastMCP = None

from legal_validator import (
    validate_report, validate_citation, check_timeliness,
    normalize_law_name, validate_source_level,
)
# 数据库接入层（W5——用户可配置北大法宝等）
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "use_database_by_api"))

SERVER_NAME = "legal-research"


def build_server() -> "FastMCP":
    """构建 MCP server（幂等）。"""
    if FastMCP is None:
        raise RuntimeError("fastmcp 未安装：pip install fastmcp")

    mcp = FastMCP(name=SERVER_NAME, strict_input_validation=True)

    @mcp.tool()
    def validate_citation_tool(citation: str) -> str:
        """引用准确性校验：法条引用格式检查与法名规范化。"""
        r = validate_citation(citation)
        return json.dumps(r, ensure_ascii=False)

    @mcp.tool()
    def check_timeliness_tool(sources_json: str) -> str:
        """新旧法时效校验：识别已废止法源，提示以新法为准。"""
        try:
            sources = json.loads(sources_json) if sources_json else []
        except Exception:
            sources = []
        r = check_timeliness(sources)
        return json.dumps(r, ensure_ascii=False)

    @mcp.tool()
    def validate_report_tool(report_json: str) -> str:
        """法律检索报告综合校验（效力+时效+引用）。"""
        try:
            report = json.loads(report_json) if report_json else {}
        except Exception:
            report = {}
        r = validate_report(report)
        return json.dumps(r, ensure_ascii=False)

    @mcp.tool()
    def normalize_law_name_tool(name: str) -> str:
        """法名规范化（简称→全称）。"""
        return json.dumps({"ok": True, "normalized": normalize_law_name(name)},
                          ensure_ascii=False)

    @mcp.tool()
    def compare_source_level_tool(type_a: str, type_b: str) -> str:
        """法源效力比较（法律/行政法规/司法解释等层级）。"""
        r = validate_source_level(type_a, type_b)
        return json.dumps(r, ensure_ascii=False)

    @mcp.tool()
    def list_databases() -> str:
        """已配置的法律数据库清单（用户可配置北大法宝等）。"""
        try:
            from db_adapter import available_adapters, load_config
            adapters = available_adapters()
            config = load_config()
            return json.dumps({"ok": True, "adapters": adapters,
                               "config_file": str(config and "db_config.json（配置方法见 README）")},
                              ensure_ascii=False)
        except Exception as e:
            return json.dumps({"ok": False, "error": str(e)[:200]},
                              ensure_ascii=False)

    # W3-W4 ⭐ 差距补齐：案例检索 + 法律推理
    @mcp.tool()
    def extract_case_keywords_tool(case_text: str) -> str:
        """案例关键词提取（案由/争点/事实→检索关键词）。"""
        from case_retriever import extract_case_keywords, build_case_query
        kw = extract_case_keywords(case_text)
        return json.dumps({"ok": True, "keywords": kw,
                           "query": build_case_query(kw)}, ensure_ascii=False)

    @mcp.tool()
    def reasoning_analysis_tool(method: str, params_json: str = "{}") -> str:
        """法律推理分析（演绎/归纳/类比/溯因四类方法）。"""
        import json as _json
        from legal_reasoning import (
            deductive_analysis, inductive_analysis,
            analogical_analysis, abductive_analysis)
        try:
            p = _json.loads(params_json) if params_json else {}
        except Exception:
            p = {}
        if method == "deductive":
            r = deductive_analysis(p.get("major", ""), p.get("minor", ""),
                                   p.get("conclusion", ""))
        elif method == "inductive":
            r = inductive_analysis(p.get("cases", []), p.get("rule", ""))
        elif method == "analogical":
            r = analogical_analysis(p.get("base_case", ""), p.get("target_case", ""),
                                    p.get("similarity", ""))
        elif method == "abductive":
            r = abductive_analysis(p.get("fact", ""), p.get("hypotheses", []))
        else:
            r = {"ok": False, "error": f"未知推理方法: {method}（deductive/inductive/analogical/abductive）"}
        return json.dumps(r, ensure_ascii=False)

    @mcp.tool()
    def recommend_reasoning_tool(question_type: str) -> str:
        """按问题类型推荐法律推理方法。"""
        from legal_reasoning import recommend_method
        return json.dumps({"ok": True, "method": recommend_method(question_type)},
                          ensure_ascii=False)

    return mcp


def main():
    """CLI 入口：启动 MCP server（stdio）。"""
    if FastMCP is None:
        print("错误：fastmcp 未安装", file=sys.stderr)
        sys.exit(1)
    server = build_server()
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
