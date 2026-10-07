# -*- coding: utf-8 -*-
"""北大法宝数据库接入验证测试（第 3 差距——配置路径验证）。"""
import os
import sys

_SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)
# db_adapter 在 use_database_by_api 目录
_DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "use_database_by_api")
if _DB not in sys.path:
    sys.path.insert(0, _DB)

import pytest

from db_adapter import (
    ADAPTER_REGISTRY, load_config, get_adapters, available_adapters,
    PkulawAdapter, WoltersAdapter, multi_search,
)


# ── R1: 适配器注册表可扩展 ──
def test_adapter_registry():
    """三数据库适配器注册（威科先行/北大法宝/裁判文书网）。"""
    assert "wolterskluwer" in ADAPTER_REGISTRY
    assert "pkulaw" in ADAPTER_REGISTRY
    assert "courts" in ADAPTER_REGISTRY


# ── R2: 北大法宝配置检查 ──
def test_pkulaw_not_configured():
    """未配置 key → 明确提示（含配置指引）。"""
    adapter = PkulawAdapter({"api_key": "", "endpoint": ""})
    assert adapter._available() is False
    r = adapter.search_law("劳动合同法")
    assert r["ok"] is False
    assert "未配置" in r.get("error", ""), "应提示未配置"


def test_pkulaw_configured():
    """已配置 key → 进入检索路径（配置识别）。"""
    adapter = PkulawAdapter({"api_key": "test_key", "endpoint": "https://pkulaw/api"})
    assert adapter._available() is True


# ── R3: 配置加载（用户配置暴露）──
def test_load_config_graceful():
    """无配置文件 → 空配置（不抛异常）。"""
    cfg = load_config()
    assert isinstance(cfg, dict)


def test_available_adapters_graceful():
    """适配器清单（无配置时优雅返回）。"""
    adapters = available_adapters()
    assert isinstance(adapters, list)


# ── R4: 多库检索（未配置库优雅跳过）──
def test_multi_search_graceful():
    """多数据库检索——未配置的库优雅报错不崩溃。"""
    r = multi_search("劳动合同", kind="law")
    assert "ok" in r
    assert "errors" in r or "results" in r
