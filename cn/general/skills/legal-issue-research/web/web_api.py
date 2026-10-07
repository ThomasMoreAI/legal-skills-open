# -*- coding: utf-8 -*-
"""legal_web — 法律检索独立网页后端（Flask API）。

三项目总控："法律检索有独立的前端网页"。提供校验工具网页：
引用校验/时效校验/报告校验/法名规范/效力比较/推理分析。
"""

from __future__ import annotations

import json
import sys
import os
from pathlib import Path

from flask import Flask, jsonify, request

_SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)
_DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "use_database_by_api")
if _DB not in sys.path:
    sys.path.insert(0, _DB)

from legal_validator import (  # noqa: E402
    validate_citation, check_timeliness, validate_report,
    normalize_law_name, validate_source_level,
)
from legal_reasoning import (  # noqa: E402
    deductive_analysis, inductive_analysis,
    analogical_analysis, abductive_analysis, recommend_method,
)
from case_retriever import extract_case_keywords, build_case_query  # noqa: E402

_WEB_DIR = Path(__file__).resolve().parent  # web 目录


def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)

    @app.route("/api/health")
    def health():
        return jsonify({"ok": True, "service": "legal-research-web"})

    @app.route("/api/citation", methods=["POST"])
    def citation():
        data = request.get_json(force=True) or {}
        r = validate_citation(data.get("citation", ""))
        return jsonify(r)

    @app.route("/api/timeliness", methods=["POST"])
    def timeliness():
        data = request.get_json(force=True) or {}
        r = check_timeliness(data.get("sources", []))
        return jsonify(r)

    @app.route("/api/report", methods=["POST"])
    def report():
        data = request.get_json(force=True) or {}
        r = validate_report(data)
        return jsonify(r)

    @app.route("/api/normalize", methods=["POST"])
    def normalize():
        data = request.get_json(force=True) or {}
        return jsonify({"ok": True, "normalized": normalize_law_name(data.get("name", ""))})

    @app.route("/api/compare", methods=["POST"])
    def compare():
        data = request.get_json(force=True) or {}
        r = validate_source_level(data.get("type_a", ""), data.get("type_b", ""))
        return jsonify(r)

    @app.route("/api/reasoning", methods=["POST"])
    def reasoning():
        data = request.get_json(force=True) or {}
        method = data.get("method", "deductive")
        p = data.get("params", {})
        if method == "deductive":
            r = deductive_analysis(p.get("major", ""), p.get("minor", ""), p.get("conclusion", ""))
        elif method == "inductive":
            r = inductive_analysis(p.get("cases", []), p.get("rule", ""))
        elif method == "analogical":
            r = analogical_analysis(p.get("base_case", ""), p.get("target_case", ""), p.get("similarity", ""))
        elif method == "abductive":
            r = abductive_analysis(p.get("fact", ""), p.get("hypotheses", []))
        else:
            r = {"ok": False, "error": f"未知方法: {method}"}
        return jsonify(r)

    @app.route("/api/case-keywords", methods=["POST"])
    def case_keywords():
        data = request.get_json(force=True) or {}
        kw = extract_case_keywords(data.get("case_text", ""))
        return jsonify({"ok": True, "keywords": kw, "query": build_case_query(kw)})

    @app.route("/")
    def index():
        idx = _WEB_DIR / "index.html"
        if idx.exists():
            return idx.read_text(encoding="utf-8")
        return "法律检索网页运行中"

    return app
