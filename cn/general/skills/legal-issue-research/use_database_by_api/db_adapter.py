# -*- coding: utf-8 -*-
"""legal_research.db_adapter — 法律数据库接入抽象层（W5 ⭐ 可扩展）。

用户需求："支持用户配置api，访问北大法宝等国内外权威法律数据库。
可扩展性必须好，配置方法暴露给用户。"

设计：
- DBAdapter 基类（统一接口：search_law / search_case / verify）
- 各数据库实现（威科先行已有 wolters_wrapper；新增北大法宝/裁判文书网占位）
- 用户通过 data/db_config.json 配置 API key/端点
- 新增数据库 = 新增 adapter 实现（不侵入核心）
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

_CONFIG_PATH = Path(__file__).resolve().parent.parent / "data" / "db_config.json"


class DBAdapter:
    """数据库适配器基类。"""

    name = "base"
    label = "基础"

    def search_law(self, query: str, **kw) -> Dict[str, Any]:
        """法规检索。返回 {"ok", "results": [...]}。"""
        return {"ok": False, "error": f"{self.name} 未实现 search_law"}

    def search_case(self, query: str, **kw) -> Dict[str, Any]:
        """案例检索。"""
        return {"ok": False, "error": f"{self.name} 未实现 search_case"}

    def verify_citation(self, text: str, **kw) -> Dict[str, Any]:
        """引注核验。"""
        return {"ok": False, "error": f"{self.name} 未实现 verify_citation"}


class WoltersAdapter(DBAdapter):
    """威科先行适配器（复用现有 wolters_wrapper）。"""

    name = "wolterskluwer"
    label = "威科先行"

    def __init__(self, config: Dict[str, Any]):
        self.config = config or {}

    def search_law(self, query: str, **kw) -> Dict[str, Any]:
        try:
            # 复用现有 wolterskluwer_searcher
            sys_path = os.path.dirname(os.path.abspath(__file__))
            searcher_path = os.path.join(sys_path, "..", "use_database_by_api")
            import sys
            if searcher_path not in sys.path:
                sys.path.insert(0, searcher_path)
            from wolterskluwer_searcher import search  # noqa
            results = search(query, config=self.config)
            return {"ok": True, "source": self.name, "results": results or []}
        except Exception as e:
            return {"ok": False, "error": f"{self.name}: {str(e)[:200]}"}

    def search_case(self, query: str, **kw) -> Dict[str, Any]:
        return self.search_law(query, **kw)


class PkulawAdapter(DBAdapter):
    """北大法宝适配器（可配置 API——用户提供 key/endpoint）。"""

    name = "pkulaw"
    label = "北大法宝"

    def __init__(self, config: Dict[str, Any]):
        self.config = config or {}
        self.api_key = config.get("api_key", "")
        self.endpoint = config.get("endpoint", "")

    def _available(self) -> bool:
        return bool(self.api_key and self.endpoint)

    def search_law(self, query: str, **kw) -> Dict[str, Any]:
        if not self._available():
            return {"ok": False, "error": "北大法宝未配置（需在 db_config.json 填 api_key/endpoint）",
                    "config_hint": "配置方法见 README"}
        # TODO: 接入北大法宝 API（用户配置后）
        return {"ok": False, "error": "北大法宝 API 待接入（已识别配置）"}

    def search_case(self, query: str, **kw) -> Dict[str, Any]:
        return self.search_law(query, **kw)


class CourtsAdapter(DBAdapter):
    """裁判文书网适配器（可配置）。"""

    name = "courts"
    label = "裁判文书网"

    def __init__(self, config: Dict[str, Any]):
        self.config = config or {}

    def search_case(self, query: str, **kw) -> Dict[str, Any]:
        return {"ok": False, "error": "裁判文书网 API 待接入（需配置）"}


# 适配器注册表（可扩展——新增数据库即注册）
ADAPTER_REGISTRY: Dict[str, type] = {
    "wolterskluwer": WoltersAdapter,
    "pkulaw": PkulawAdapter,
    "courts": CourtsAdapter,
}


def load_config() -> Dict[str, Any]:
    """加载用户数据库配置（data/db_config.json）。"""
    if _CONFIG_PATH.exists():
        try:
            return json.loads(_CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def get_adapters() -> Dict[str, DBAdapter]:
    """按配置实例化已启用适配器。"""
    config = load_config()
    adapters: Dict[str, DBAdapter] = {}
    for name, adapter_cls in ADAPTER_REGISTRY.items():
        if name in config and config[name].get("enabled", True):
            try:
                adapters[name] = adapter_cls(config[name])
            except Exception:
                continue
    return adapters


def available_adapters() -> List[str]:
    """已启用适配器清单。"""
    config = load_config()
    return [n for n in ADAPTER_REGISTRY if n in config and config[n].get("enabled", True)]


def multi_search(query: str, kind: str = "law") -> Dict[str, Any]:
    """多数据库检索（按配置自动调用已启用库）。

    kind: "law" 法规 / "case" 案例。
    """
    adapters = get_adapters()
    results = []
    errors = []
    for name, adapter in adapters.items():
        try:
            if kind == "case":
                r = adapter.search_case(query)
            else:
                r = adapter.search_law(query)
            if r.get("ok"):
                results.append({"source": name, "results": r.get("results", [])})
            else:
                errors.append(f"{name}: {r.get('error', '失败')}")
        except Exception as e:
            errors.append(f"{name}: {str(e)[:100]}")
    return {"ok": bool(results), "results": results, "errors": errors}
