#!/usr/bin/env python3
"""元典法律法规检索（开放平台版）

子命令:
  search          法律法规语义检索       POST /open/law_vector_search
  search_keyword  法条关键词检索         POST /open/rh_ft_search
  ft_detail       法条详情               POST /open/rh_ft_detail
  search_fg       法规关键词/筛选检索    POST /open/rh_fg_search
  fg_detail       法规详情               POST /open/rh_fg_detail

  search_ft_info  ↔ ft_detail 的旧名别名（向后兼容）
                  旧入参 query/ft_name 自动映射为 fgmc/ftnum
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

API_BASE = "https://open.chineselaw.com"
ENDPOINTS = {
    "search":         "/open/law_vector_search",
    "search_keyword": "/open/rh_ft_search",
    "ft_detail":      "/open/rh_ft_detail",
    "search_fg":      "/open/rh_fg_search",
    "fg_detail":      "/open/rh_fg_detail",
}
ALIASES = {
    "search_ft_info": "ft_detail",
}

API_KEY_HELP = """
未检测到 元典开放平台 API Key。
请按以下顺序之一配置：
  1) export YD_OPEN_API_KEY="你的密钥"
  2) printf "%s" "你的密钥" > ~/.yd_open_api_key
  3) export YD_API_KEY="你的密钥"
  4) printf "%s" "你的密钥" > ~/.yd_api_key
  5) 在脚本目录写入 .api_key
申请入口: https://open.chineselaw.com/
""".strip()


def get_api_key() -> str:
    for env_name in ("YD_OPEN_API_KEY", "YD_API_KEY"):
        key = os.environ.get(env_name, "").strip()
        if key:
            return key
    for path in (
        os.path.expanduser("~/.yd_open_api_key"),
        os.path.expanduser("~/.yd_api_key"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), ".api_key"),
    ):
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                key = f.read().strip()
                if key:
                    return key
    return ""


def normalize_params(endpoint: str, params: dict) -> dict:
    """处理参数差异，向后兼容旧调用形态。"""
    p = dict(params)

    # search_ft_info 旧字段映射
    if "query" in p and endpoint == "ft_detail":
        p.setdefault("fgmc", p.pop("query"))
    if "ft_name" in p and endpoint == "ft_detail":
        p.setdefault("ftnum", p.pop("ft_name"))

    # sxx 类型差异：语义接口要 list，关键词接口要 string
    if endpoint == "search":
        # 语义接口的 sxx 在 fatiao_filter 内，且为 string[]
        ff = p.get("fatiao_filter")
        if ff is None and "sxx" in p:
            ff = {"sxx": p.pop("sxx")}
            p["fatiao_filter"] = ff
        if isinstance(ff, dict) and isinstance(ff.get("sxx"), str):
            ff["sxx"] = [s for s in ff["sxx"].split() if s]
    elif endpoint in ("search_keyword", "search_fg"):
        # 关键词接口 sxx 是 string，多值空格分隔
        if isinstance(p.get("sxx"), list):
            p["sxx"] = " ".join(p["sxx"])

    # 关键词搜索参数兼容 query → keyword
    if endpoint in ("search_keyword", "search_fg") and "query" in p and "keyword" not in p:
        p["keyword"] = p.pop("query")

    # search_mode 大小写：法条/法规关键词接口是 AND/OR
    if endpoint in ("search_keyword", "search_fg") and isinstance(p.get("search_mode"), str):
        p["search_mode"] = p["search_mode"].upper()

    # 默认 top_k
    if endpoint in ("search_keyword", "search_fg"):
        p.setdefault("top_k", 8)

    # 语义接口默认 sxx=现行有效（仅当用户未传 fatiao_filter 时）
    if endpoint == "search":
        ff = p.setdefault("fatiao_filter", {})
        ff.setdefault("sxx", ["现行有效"])
        p.setdefault("return_num", 8)

    return p


def call_api(endpoint: str, params: dict, api_key: str) -> dict:
    url = API_BASE + ENDPOINTS[endpoint]
    data = json.dumps(params, ensure_ascii=False).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-API-Key": api_key,
    }
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"code": e.code, "status": "failed",
                "message": f"HTTP 错误 {e.code}: {body}"}
    except urllib.error.URLError as e:
        return {"code": 500, "status": "failed", "message": f"网络错误: {e.reason}"}
    except Exception as e:
        return {"code": 500, "status": "failed", "message": f"请求失败: {e}"}


# ---------------- 字段归一化 ----------------

def _norm_ft_from_vector(item: dict) -> dict:
    """语义接口 extra.fatiao[] 的字段归一化"""
    return {
        "id": item.get("ftid") or item.get("id", ""),
        "fgid": item.get("fgid", ""),
        "fgmc": item.get("fgtitle") or item.get("fgmc", ""),
        "ft_num": item.get("num") or item.get("ft_num", ""),
        "content": item.get("content", ""),
        "sxx": item.get("sxx", ""),
        "xljb_1": item.get("effect1") or item.get("xljb_1", ""),
        "xljb_2": item.get("effect2") or item.get("xljb_2", ""),
        "fbrq": str(item.get("start") or item.get("fbrq") or ""),
        "ssrq": str(item.get("ssrq") or ""),
        "score": item.get("score"),
    }


def _norm_passthrough(item: dict) -> dict:
    return item


def extract_items(endpoint: str, result: dict):
    """从不同形状的响应里掏出条目列表 + 总数提示。"""
    if endpoint == "search":
        items = (((result.get("extra") or {}).get("fatiao")) or [])
        return [_norm_ft_from_vector(x) for x in items], len(items)
    data = result.get("data")
    if endpoint == "ft_detail" or endpoint == "fg_detail":
        if isinstance(data, dict):
            return [_norm_passthrough(data)], 1
        return [], 0
    # search_keyword / search_fg → data 是 list
    if isinstance(data, list):
        return [_norm_passthrough(x) for x in data], len(data)
    return [], 0


# ---------------- 输出 ----------------

CONTENT_PREVIEW = 120


def is_success(result: dict) -> bool:
    code = result.get("code")
    if code in (200, 201):
        return True
    status = (result.get("status") or "").lower()
    return status == "success"


def fmt_one(idx: int, it: dict, full: bool) -> list[str]:
    title = it.get("title") or f"{it.get('fgmc','')}{it.get('ft_num','')}"
    lines = ["=" * 60, f"【{idx}】{title or '未命名'}"]
    if it.get("sxx"):    lines.append(f"时效性: {it['sxx']}")
    if it.get("xljb_1"): lines.append(f"效力级别: {it['xljb_1']}"
                                     + (f" / {it['xljb_2']}" if it.get('xljb_2') else ""))
    if it.get("fbbm"):   lines.append(f"发布部门: {it['fbbm']}")
    if it.get("fwzh"):   lines.append(f"发文字号: {it['fwzh']}")
    if it.get("fbrq"):   lines.append(f"发布日期: {it['fbrq']}")
    if it.get("ssrq"):   lines.append(f"实施日期: {it['ssrq']}")
    if it.get("id"):     lines.append(f"id: {it['id']}")
    content = (it.get("content") or "").strip()
    if content:
        if full:
            lines.append("内容:")
            for row in content.splitlines() or [""]:
                lines.append(f"  {row.strip()}")
        else:
            preview = content.replace("\n", " ")
            if len(preview) > CONTENT_PREVIEW:
                preview = preview[:CONTENT_PREVIEW] + "…"
            lines.append(f"摘要: {preview}")
    if it.get("url"):
        url = it["url"]
        if url.startswith("/"):
            url = "https://open.chineselaw.com" + url
        lines.append(f"链接: {url}")
    lines.append("")
    return lines


def format_result(endpoint: str, result: dict, full: bool) -> str:
    if not is_success(result):
        return f"调用失败: code={result.get('code')} {result.get('message') or result.get('msg') or ''}"
    items, total = extract_items(endpoint, result)
    if not items:
        return "未查询到相关内容。"
    header = f"共找到 {total} 条结果：" if endpoint not in ("ft_detail", "fg_detail") else "详情:"
    out = [header, ""]
    for i, it in enumerate(items, 1):
        out.extend(fmt_one(i, it, full))
    if not full:
        out.append("提示: 默认仅展示摘要。要获取全文请用 ft_detail / fg_detail 配合 id，或加 --full 重打印。")
    return "\n".join(out)


# ---------------- CLI ----------------

def parse_args(argv: list[str]):
    flags = {"--stdin", "--raw", "--full"}
    flag_set = {a for a in argv if a in flags}
    positional = [a for a in argv if a not in flags]
    if not positional:
        raise ValueError("用法: yd_law_search.py <subcmd> '<json>' [--stdin] [--raw] [--full]")
    sub = positional[0]
    sub = ALIASES.get(sub, sub)
    if sub not in ENDPOINTS:
        raise ValueError(f"未知子命令: {positional[0]}（可用: {', '.join(list(ENDPOINTS) + list(ALIASES))}）")
    if "--stdin" in flag_set:
        payload = sys.stdin.read().strip()
        if not payload:
            raise ValueError("--stdin 模式下未读到 JSON")
        params = json.loads(payload)
    else:
        if len(positional) < 2:
            raise ValueError("缺少 JSON 入参；或使用 --stdin")
        params = json.loads(positional[1])
    return sub, params, ("--raw" in flag_set), ("--full" in flag_set)


def main():
    try:
        sub, params, raw, full = parse_args(sys.argv[1:])
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    api_key = get_api_key()
    if not api_key:
        print(API_KEY_HELP, file=sys.stderr)
        sys.exit(1)
    params = normalize_params(sub, params)
    result = call_api(sub, params, api_key)
    if raw:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_result(sub, result, full))
        print(json.dumps(result, ensure_ascii=False), file=sys.stderr)


if __name__ == "__main__":
    main()
