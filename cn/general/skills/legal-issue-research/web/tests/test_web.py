# -*- coding: utf-8 -*-
"""法律检索独立网页测试（web_api + 前端）。"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WEB = os.path.dirname(_HERE)  # legal-research 目录
if _WEB not in sys.path:
    sys.path.insert(0, _WEB)

import pytest

from web_api import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.get_json()["ok"] is True


def test_citation(client):
    r = client.post("/api/citation", json={"citation": "《民法典》第1065条"})
    assert r.status_code == 200
    assert r.get_json()["ok"] is True


def test_timeliness(client):
    r = client.post("/api/timeliness", json={
        "sources": [{"name": "民法通则", "year": 1986, "status": "已废止"}]})
    assert r.get_json()["has_outdated"] is True


def test_reasoning(client):
    r = client.post("/api/reasoning", json={
        "method": "deductive",
        "params": {"major": "M", "minor": "m", "conclusion": "c"}})
    assert r.status_code == 200


def test_case_keywords(client):
    r = client.post("/api/case-keywords", json={"case_text": "房屋买卖合同拒不交付"})
    d = r.get_json()
    assert d["ok"] is True
    assert d["keywords"]


def test_index_page(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "法律检索工具" in r.get_data(as_text=True)
