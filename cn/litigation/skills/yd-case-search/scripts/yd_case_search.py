#!/usr/bin/env python3
"""元典案例检索（开放平台版）

子命令:
  search_al         案例关键词检索        POST /open/rh_ptal_search 或 /open/rh_qwal_search
                    路由: authority_only=true → qwal；否则 → ptal
  search_al_vector  案例语义检索          POST /open/case_vector_search
  case_detail       案例详情              GET  /open/rh_case_details (需 type=ptal|qwal)
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API_BASE = "https://open.chineselaw.com"

POST_ENDPOINTS = {
    "search_al_vector": "/open/case_vector_search",
}
# search_al 需要根据 authority_only 路由：
SEARCH_AL_PTAL = "/open/rh_ptal_search"
SEARCH_AL_QWAL = "/open/rh_qwal_search"
# case_detail 是 GET
CASE_DETAIL = "/open/rh_case_details"

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
    for env in ("YD_OPEN_API_KEY", "YD_API_KEY"):
        v = os.environ.get(env, "").strip()
        if v:
            return v
    for p in (
        os.path.expanduser("~/.yd_open_api_key"),
        os.path.expanduser("~/.yd_api_key"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), ".api_key"),
    ):
        if os.path.isfile(p):
            with open(p, "r", encoding="utf-8") as f:
                v = f.read().strip()
                if v:
                    return v
    return ""


# ---------------- 参数归一化 ----------------

def normalize_search_al(params: dict) -> tuple[str, dict]:
    """根据 authority_only 决定走哪个 endpoint，并把参数清洗成对应接口形态。"""
    p = dict(params)
    authority_only = bool(p.pop("authority_only", False))
    target = SEARCH_AL_QWAL if authority_only else SEARCH_AL_PTAL
    # 兼容旧 query → qw（全文关键词）
    if "query" in p and "qw" not in p:
        p["qw"] = p.pop("query")
    # search_mode 关键词接口期望小写 and/or
    if isinstance(p.get("search_mode"), str):
        p["search_mode"] = p["search_mode"].lower()
    if isinstance(p.get("ft_search_mode"), str):
        p["ft_search_mode"] = p["ft_search_mode"].lower()
    # qwal 接口不支持 fxgc/yyft，剔除避免 500
    if authority_only:
        for k in ("fxgc", "yyft", "ft_search_mode"):
            p.pop(k, None)
    p.setdefault("top_k", 8)
    return target, p


def normalize_search_al_vector(params: dict) -> dict:
    p = dict(params)
    # 兼容旧 jarq_start/jarq_end → wenshu_filter.ja_start/ja_end
    wf = p.get("wenshu_filter")
    if wf is None:
        wf = {}
        for old, new in (("jarq_start", "ja_start"), ("jarq_end", "ja_end")):
            if old in p:
                wf[new] = p.pop(old)
        if "authority_only" in p:
            wf["dianxing"] = bool(p.pop("authority_only"))
        if wf:
            p["wenshu_filter"] = wf
    p.setdefault("return_num", 8)
    return p


# ---------------- HTTP ----------------

def call_post(endpoint_path: str, body: dict, api_key: str) -> dict:
    url = API_BASE + endpoint_path
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    headers = {"Content-Type": "application/json", "Accept": "application/json",
               "X-API-Key": api_key}
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    return _do(req)


def call_get(endpoint_path: str, query: dict, api_key: str) -> dict:
    qs = urllib.parse.urlencode({k: v for k, v in query.items() if v not in (None, "")})
    url = f"{API_BASE}{endpoint_path}?{qs}"
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "X-API-Key": api_key}, method="GET")
    return _do(req)


def _do(req) -> dict:
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


# ---------------- 归一化抽取 ----------------

def _norm_case_from_vector(it: dict) -> dict:
    return {
        "id": it.get("scid") or it.get("id", ""),
        "title": it.get("title", ""),
        "ah": it.get("ah", ""),
        "ay": it.get("ay", ""),
        "ajlb": it.get("ajlb", ""),
        "wszl": it.get("wszl", ""),
        "jbdw": it.get("jbdw", ""),
        "xzqh_p": it.get("xzqh_p", ""),
        "xzqh_c": it.get("xzqh_c", ""),
        "cprq": str(it.get("jaDate") or it.get("cprq") or ""),
        "content": it.get("content", ""),
        "score": it.get("score"),
        "type_hint": "qwal" if (it.get("authority") or it.get("db") == "权威案例库") else "ptal",
    }


def _norm_case_passthrough(it: dict) -> dict:
    out = dict(it)
    out.setdefault("type_hint", "ptal" if it.get("type") == "普通案例" else "qwal")
    return out


def extract(endpoint_kind: str, result: dict):
    """endpoint_kind: 'al_ptal' | 'al_qwal' | 'al_vector' | 'detail'"""
    if endpoint_kind == "al_vector":
        items = ((result.get("extra") or {}).get("wenshu")) or []
        return [_norm_case_from_vector(x) for x in items], len(items)
    if endpoint_kind in ("al_ptal", "al_qwal"):
        data = result.get("data") or {}
        lst = data.get("lst") or []
        total = data.get("total")
        if isinstance(total, dict):
            total = total.get("value") or len(lst)
        return [_norm_case_passthrough(x) for x in lst], (total or len(lst))
    if endpoint_kind == "detail":
        data = result.get("data")
        if isinstance(data, list):
            return [_norm_case_passthrough(x) for x in data], len(data)
        if isinstance(data, dict):
            return [_norm_case_passthrough(data)], 1
        return [], 0
    return [], 0


# ---------------- 输出 ----------------

CONTENT_PREVIEW = 160


def is_success(result: dict) -> bool:
    if result.get("code") in (200, 201):
        return True
    return (result.get("status") or "").lower() == "success"


def fmt_one(idx: int, it: dict, full: bool) -> list[str]:
    lines = ["=" * 60, f"【{idx}】{it.get('title') or '未命名案例'}"]
    if it.get("ah"):     lines.append(f"案号: {it['ah']}")
    if it.get("type"):   lines.append(f"类型: {it['type']}")
    if it.get("ajlb"):   lines.append(f"案件类别: {it['ajlb']}")
    if it.get("ay"):
        ay = it["ay"]
        ay_str = "；".join(ay) if isinstance(ay, list) else str(ay)
        lines.append(f"案由: {ay_str}")
    if it.get("wszl"):   lines.append(f"文书种类: {it['wszl']}")
    if it.get("jbdw"):   lines.append(f"经办法院: {it['jbdw']}")
    province = it.get("xzqh_p") or ""
    city = it.get("xzqh_c") or ""
    if province or city: lines.append(f"地区: {province}{city}")
    if it.get("cprq"):   lines.append(f"裁判日期: {it['cprq']}")
    if it.get("id"):     lines.append(f"id: {it['id']}  (type={it.get('type_hint','ptal')})")
    content = (it.get("content") or "").strip()
    if content:
        if full:
            lines.append("正文:")
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


def format_result(endpoint_kind: str, result: dict, full: bool) -> str:
    if not is_success(result):
        return f"调用失败: code={result.get('code')} {result.get('message') or result.get('msg') or ''}"
    items, total = extract(endpoint_kind, result)
    if not items:
        return "未查询到相关案例。"
    header = ("详情:" if endpoint_kind == "detail"
              else f"共找到 {total} 条结果（展示前 {len(items)}）：")
    out = [header, ""]
    for i, it in enumerate(items, 1):
        out.extend(fmt_one(i, it, full))
    if not full:
        out.append("提示: 默认仅展示摘要。要获取全文请用 case_detail 配合 id 与 type，或加 --full 重打印。")
    return "\n".join(out)


# ---------------- CLI ----------------

VALID_SUBS = {"search_al", "search_al_vector", "case_detail"}


def parse_args(argv: list[str]):
    flags = {"--stdin", "--raw", "--full"}
    flag_set = {a for a in argv if a in flags}
    positional = [a for a in argv if a not in flags]
    if not positional:
        raise ValueError(f"用法: yd_case_search.py <{'|'.join(VALID_SUBS)}> '<json>' [--stdin] [--raw] [--full]")
    sub = positional[0]
    if sub not in VALID_SUBS:
        raise ValueError(f"未知子命令: {sub}（可用: {', '.join(VALID_SUBS)}）")
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

    if sub == "search_al":
        endpoint_path, body = normalize_search_al(params)
        result = call_post(endpoint_path, body, api_key)
        kind = "al_qwal" if endpoint_path == SEARCH_AL_QWAL else "al_ptal"
    elif sub == "search_al_vector":
        body = normalize_search_al_vector(params)
        result = call_post(POST_ENDPOINTS["search_al_vector"], body, api_key)
        kind = "al_vector"
    elif sub == "case_detail":
        if "type" not in params:
            print("case_detail 必须传 type=ptal 或 type=qwal", file=sys.stderr)
            sys.exit(1)
        result = call_get(CASE_DETAIL, params, api_key)
        kind = "detail"
    else:
        print(f"未知子命令: {sub}", file=sys.stderr)
        sys.exit(1)

    if raw:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_result(kind, result, full))
        print(json.dumps(result, ensure_ascii=False), file=sys.stderr)


if __name__ == "__main__":
    main()
