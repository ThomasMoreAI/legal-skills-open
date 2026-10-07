# -*- coding: utf-8 -*-
"""
威科先行（Wolters Kluwer China）懒人接口
==========================================
在 skill 根目录创建 config.json 填入 API 凭证即可使用。
无需修改任何代码。

使用方式（自动调用，无需手动）：
    from wolters_auto import WoltersAuto
    result = WoltersAuto.search("违法解除劳动合同赔偿金")

config.json 路径：skill根目录/config.json
"""

import json
import os
import requests
from typing import Dict, Optional, Any
from datetime import datetime, timedelta

# ============================================================
# 配置读取（用户只需修改 config.json）
# ============================================================

# 向上两级找到 skill 根目录，然后在该目录查找 config.json
# 例如：use_database_by_api/wolters_auto.py → skill根目录/config.json
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(SKILL_ROOT, "config.json")


def load_config() -> Optional[Dict[str, str]]:
    """从 config.json 加载配置"""
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# 威科先行懒人检索接口
# ============================================================

class WoltersAuto:
    """
    懒人接口 - 配置后自动工作

    使用步骤：
    1. 在此文件同目录创建 config.json
    2. 填入 API 凭证
    3. from wolters_auto import WoltersAuto; WoltersAuto.search("问题")
    """

    _config: Optional[Dict] = None
    _token: Optional[str] = None
    _token_expires: Optional[datetime] = None

    @classmethod
    def is_configured(cls) -> bool:
        """检查是否已配置"""
        config = load_config()
        if not config:
            return False
        return bool(config.get("API_KEY") and config.get("API_BASE_URL"))

    @classmethod
    def _get_token(cls) -> str:
        """获取认证 Token"""
        config = load_config()
        if not config:
            raise ValueError("未配置威科先行 API，请创建 config.json")

        # 如果已有有效 token，直接返回
        if cls._token and cls._token_expires and datetime.now() < cls._token_expires:
            return cls._token

        # 获取新 token
        auth_type = config.get("AUTH_TYPE", "Bearer")

        if auth_type == "API-Key":
            cls._token = config["API_KEY"]
            return cls._token

        elif auth_type == "Bearer":
            token_url = config.get("TOKEN_URL") or f"{config['API_BASE_URL']}/oauth/token"
            response = requests.post(
                token_url,
                data={
                    "grant_type": "client_credentials",
                    "client_id": config["API_KEY"],
                    "client_secret": config.get("API_SECRET", ""),
                },
                timeout=30
            )
            result = response.json()
            cls._token = result["access_token"]
            cls._token_expires = datetime.now() + timedelta(seconds=result.get("expires_in", 3600))
            return cls._token

        else:
            raise ValueError(f"不支持的 AUTH_TYPE: {auth_type}")

    @classmethod
    def _get_headers(cls) -> Dict[str, str]:
        """获取请求头"""
        config = load_config()
        auth_type = config.get("AUTH_TYPE", "Bearer")
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if auth_type == "Bearer":
            headers["Authorization"] = f"Bearer {cls._get_token()}"
        elif auth_type == "API-Key":
            headers["X-API-Key"] = config["API_KEY"]
        return headers

    @classmethod
    def search(
        cls,
        keyword: str,
        search_type: str = "all",
        region: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        page: int = 1,
        page_size: int = 20
    ) -> Dict[str, Any]:
        """
        执行检索（自动配置，使用简单）

        Args:
            keyword: 检索关键词
            search_type: 检索类型 (law/case/judgment/interpretation/guidance/all)
            region: 地域限定
            date_from: 开始日期 (YYYY-MM-DD)
            date_to: 结束日期 (YYYY-MM-DD)
            page: 页码
            page_size: 每页条数

        Returns:
            Dict: 检索结果，包含以下字段：
            {
                "success": bool,
                "source": "威科先行",
                "keyword": str,
                "search_time": str,
                "total": int,
                "laws": [...],      # 法规列表
                "cases": [...],     # 案例列表
                "judgments": [...], # 裁判文书列表
                "interpretations": [...],  # 司法解释列表
                "guidance_cases": [...],   # 指导性案例列表
                "error": str        # 如有错误
            }
        """
        config = load_config()
        if not config:
            return {
                "success": False,
                "source": "威科先行",
                "keyword": keyword,
                "search_time": datetime.now().isoformat(),
                "error": "未配置 API，请创建 config.json",
                "laws": [], "cases": [], "judgments": [],
                "interpretations": [], "guidance_cases": []
            }

        try:
            base_url = config["API_BASE_URL"]
            
            # 根据 search_type 确定 endpoint
            endpoint_map = {
                "law": "/laws/search",
                "case": "/cases/search",
                "judgment": "/judgments/search",
                "interpretation": "/interpretations/search",
                "guidance": "/guidance-cases/search",
                "all": "/search"
            }
            endpoint = endpoint_map.get(search_type, "/search")

            # 构建请求
            request_body = {
                "keyword": keyword,
                "page": page,
                "pageSize": page_size,
            }
            if region:
                request_body["region"] = region
            if date_from or date_to:
                request_body["dateRange"] = {
                    "from": date_from,
                    "to": date_to
                }

            # 发送请求
            headers = cls._get_headers()
            response = requests.post(
                f"{base_url}{endpoint}",
                headers=headers,
                json=request_body,
                timeout=30
            )
            response.raise_for_status()
            raw = response.json()

            # 解析响应（通用解析，用户可根据实际返回字段调整）
            return cls._parse_response(keyword, raw, search_type)

        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "source": "威科先行",
                "keyword": keyword,
                "search_time": datetime.now().isoformat(),
                "error": f"请求失败: {str(e)}",
                "laws": [], "cases": [], "judgments": [],
                "interpretations": [], "guidance_cases": []
            }
        except Exception as e:
            return {
                "success": False,
                "source": "威科先行",
                "keyword": keyword,
                "search_time": datetime.now().isoformat(),
                "error": f"未知错误: {str(e)}",
                "laws": [], "cases": [], "judgments": [],
                "interpretations": [], "guidance_cases": []
            }

    @classmethod
    def _parse_response(
        cls,
        keyword: str,
        raw: Dict,
        search_type: str
    ) -> Dict[str, Any]:
        """解析 API 响应 - 适配 skill 格式"""

        # 根据威科实际返回格式调整此处
        # 通用解析逻辑（可能需要根据实际返回字段修改）

        def parse_items(items: list, item_type: str) -> list:
            """通用解析函数"""
            if not items:
                return []
            result = []
            for item in items:
                if item_type == "law":
                    result.append({
                        "title": item.get("title") or item.get("lawTitle") or item.get("name", ""),
                        "document_number": item.get("documentNumber") or item.get("lawNo", ""),
                        "effective_date": item.get("effectiveDate") or item.get("effectiveDate", ""),
                        "category": item.get("category") or item.get("lawType", ""),
                        "issuer": item.get("issuer") or item.get("agency", ""),
                        "content_summary": (item.get("content") or item.get("fullText") or "")[:500],
                        "url": item.get("url") or item.get("detailUrl", "")
                    })
                elif item_type == "case":
                    result.append({
                        "case_name": item.get("caseName") or item.get("title", ""),
                        "case_number": item.get("caseNumber") or item.get("caseNo", ""),
                        "case_type": item.get("caseType") or item.get("type", ""),
                        "court": item.get("court", ""),
                        "judge_date": item.get("judgeDate") or item.get("date", ""),
                        "summary": (item.get("summary") or item.get("judgmentSummary") or "")[:500],
                        "url": item.get("url") or item.get("detailUrl", "")
                    })
                # 其他类型类似处理...
            return result

        # 提取结果
        data = raw.get("data", raw)
        total = raw.get("total", raw.get("totalCount", 0))

        # 处理 all 类型（返回各类型数据）
        if search_type == "all":
            return {
                "success": True,
                "source": "威科先行",
                "keyword": keyword,
                "search_time": datetime.now().isoformat(),
                "total": total,
                "laws": parse_items(data.get("laws", []), "law"),
                "cases": parse_items(data.get("cases", []), "case"),
                "judgments": parse_items(data.get("judgments", []), "case"),
                "interpretations": parse_items(data.get("interpretations", []), "law"),
                "guidance_cases": parse_items(data.get("guidanceCases", []), "case"),
                "error": None
            }

        # 单类型
        item_type = "law" if search_type in ["law", "interpretation"] else "case"
        items = data if isinstance(data, list) else data.get("items", data.get("results", []))

        result = {
            "success": True,
            "source": "威科先行",
            "keyword": keyword,
            "search_time": datetime.now().isoformat(),
            "total": total,
            "error": None
        }
        result[f"{search_type}s"] = parse_items(items, item_type)
        return result

    # 便捷方法
    @classmethod
    def search_laws(cls, keyword: str, **kwargs):
        return cls.search(keyword, search_type="law", **kwargs)

    @classmethod
    def search_cases(cls, keyword: str, **kwargs):
        return cls.search(keyword, search_type="case", **kwargs)

    @classmethod
    def search_guidance(cls, keyword: str, **kwargs):
        return cls.search(keyword, search_type="guidance", **kwargs)


# ============================================================
# Skill 自动调用接口（供 skill 流程调用）
# ============================================================

def auto_search(legal_issue: str, legal_type: str = None, region: str = None, date_range: dict = None) -> dict:
    """
    供 legal-issue-research skill 自动调用的接口

    Args:
        legal_issue: 法律问题描述
        legal_type: 法律类型（labor/civil/criminal/administrative）
        region: 地域
        date_range: {"from": "YYYY-MM-DD", "to": "YYYY-MM-DD"}

    Returns:
        dict: 兼容 skill 格式的检索结果
    """
    # 先检查是否已配置，避免不必要的 API 调用
    if not WoltersAuto.is_configured():
        return {
            "available": False,
            "source": "威科先行",
            "keyword": legal_issue,
            "message": "用户未配置威科先行 API",
            "results": {}
        }

    date_from = date_range.get("from") if date_range else None
    date_to = date_range.get("to") if date_range else None

    result = WoltersAuto.search(
        keyword=legal_issue,
        search_type="all",
        region=region,
        date_from=date_from,
        date_to=date_to
    )

    return {
        "available": True,
        "source": "威科先行",
        "keyword": legal_issue,
        "search_time": result.get("search_time", ""),
        "results": result
    }


# ============================================================
# 使用示例
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("威科先行懒人接口")
    print("=" * 60)

    if not WoltersAuto.is_configured():
        print()
        print("⚠️  尚未配置 API")
        print()
        print("请在同目录创建 config.json，内容如下：")
        print("""
{
    "API_BASE_URL": "https://api.wkinfo.com.cn/v1",
    "API_KEY": "你的API_KEY",
    "API_SECRET": "你的API_SECRET（可选）",
    "AUTH_TYPE": "Bearer"
}
""")
    else:
        print("✅ 已配置，开始检索...")
        result = WoltersAuto.search("劳动合同违法解除")
        print(json.dumps(result, ensure_ascii=False, indent=2))
