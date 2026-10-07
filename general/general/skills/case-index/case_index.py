#!/usr/bin/env python3
"""
JuriSupport CSV 사건 인덱스 헬퍼.

JuriSupport MCP를 쓰지 않는 사용자를 위한 가벼운 사건관리 도구.
CSV 한 파일(_index.csv)을 source of truth로 사용한다.

컬럼: 사건번호,법원,사건명,의뢰인,상대방,진행단계,다음기일,비고
키: 사건번호 (중복 불가)

Usage:
  case_index.py --csv <path> list [--stage <단계>] [--upcoming-days N]
  case_index.py --csv <path> get <사건번호>
  case_index.py --csv <path> add --사건번호 X --법원 Y ...
  case_index.py --csv <path> update <사건번호> --진행단계 X ...
  case_index.py --csv <path> close <사건번호>            (진행단계=종결로 표시)
  case_index.py --csv <path> init                          (헤더만 있는 빈 CSV 생성)
"""
from __future__ import annotations
import argparse
import csv
import datetime as dt
import io
import os
import sys
import tempfile
from pathlib import Path

COLUMNS = ["사건번호", "법원", "사건명", "의뢰인", "상대방", "진행단계", "다음기일", "비고"]


def die(msg: str, code: int = 1) -> None:
    print(f"오류: {msg}", file=sys.stderr)
    sys.exit(code)


def ensure_csv(path: Path, create_if_missing: bool = False) -> None:
    if path.exists():
        return
    if not create_if_missing:
        die(f"CSV 파일이 없습니다: {path}\n  먼저 `init` 명령으로 생성하거나 경로를 확인하세요.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerow(COLUMNS)


def read_all(path: Path) -> list[dict]:
    ensure_csv(path)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for c in COLUMNS:
            r.setdefault(c, "")
    return rows


def write_all(path: Path, rows: list[dict]) -> None:
    # write atomically via temp file in same dir (OneDrive-safe)
    fd, tmp = tempfile.mkstemp(prefix="._index_", suffix=".csv", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow({c: r.get(c, "") for c in COLUMNS})
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def parse_date(s: str) -> dt.date | None:
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def cmd_init(path: Path, args) -> None:
    if path.exists() and not args.force:
        die(f"이미 존재합니다: {path} (덮어쓰려면 --force)")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerow(COLUMNS)
    print(f"생성: {path}")


def cmd_list(path: Path, args) -> None:
    rows = read_all(path)
    if args.stage:
        rows = [r for r in rows if r.get("진행단계") == args.stage]
    if args.upcoming_days is not None:
        today = dt.date.today()
        cutoff = today + dt.timedelta(days=args.upcoming_days)
        rows = [
            r for r in rows
            if (d := parse_date(r.get("다음기일", ""))) is not None
            and today <= d <= cutoff
        ]
    if not rows:
        print("(해당 사건 없음)")
        return
    rows.sort(key=lambda r: (parse_date(r.get("다음기일", "")) or dt.date.max, r.get("사건번호", "")))
    w = csv.DictWriter(sys.stdout, fieldnames=COLUMNS, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c, "") for c in COLUMNS})


def cmd_get(path: Path, args) -> None:
    rows = read_all(path)
    for r in rows:
        if r["사건번호"] == args.사건번호:
            for c in COLUMNS:
                print(f"{c}: {r.get(c, '')}")
            return
    die(f"사건번호를 찾을 수 없습니다: {args.사건번호}", code=2)


def cmd_add(path: Path, args) -> None:
    ensure_csv(path, create_if_missing=True)
    rows = read_all(path)
    if any(r["사건번호"] == args.사건번호 for r in rows):
        die(f"이미 존재하는 사건번호: {args.사건번호} (update 사용)", code=3)
    rows.append({c: getattr(args, c, "") or "" for c in COLUMNS})
    write_all(path, rows)
    print(f"추가: {args.사건번호}")


def cmd_update(path: Path, args) -> None:
    rows = read_all(path)
    target = None
    for r in rows:
        if r["사건번호"] == args.사건번호:
            target = r
            break
    if target is None:
        die(f"사건번호를 찾을 수 없습니다: {args.사건번호}", code=2)
    changed = []
    for c in COLUMNS:
        if c == "사건번호":
            continue
        v = getattr(args, c, None)
        if v is not None:
            target[c] = v
            changed.append(c)
    if not changed:
        die("변경할 필드가 없습니다.", code=4)
    write_all(path, rows)
    print(f"갱신: {args.사건번호} ({', '.join(changed)})")


def cmd_close(path: Path, args) -> None:
    rows = read_all(path)
    target = None
    for r in rows:
        if r["사건번호"] == args.사건번호:
            target = r
            break
    if target is None:
        die(f"사건번호를 찾을 수 없습니다: {args.사건번호}", code=2)
    target["진행단계"] = "종결"
    target["다음기일"] = ""
    write_all(path, rows)
    print(f"종결 처리: {args.사건번호}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="JuriSupport CSV 사건 인덱스")
    p.add_argument("--csv", required=True, help="_index.csv 경로 (예: ~/사건/_index.csv)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="빈 CSV 생성").add_argument("--force", action="store_true")

    sp = sub.add_parser("list", help="사건 목록")
    sp.add_argument("--stage", help="진행단계 필터 (예: 1심, 항소, 상고, 종결)")
    sp.add_argument("--upcoming-days", type=int, help="앞으로 N일 이내 기일만")

    sp = sub.add_parser("get", help="단일 사건 조회")
    sp.add_argument("사건번호")

    sp = sub.add_parser("add", help="사건 추가")
    sp.add_argument("--사건번호", required=True)
    for c in COLUMNS:
        if c == "사건번호":
            continue
        sp.add_argument(f"--{c}", default="")

    sp = sub.add_parser("update", help="사건 갱신")
    sp.add_argument("사건번호")
    for c in COLUMNS:
        if c == "사건번호":
            continue
        sp.add_argument(f"--{c}", default=None)

    sp = sub.add_parser("close", help="사건 종결")
    sp.add_argument("사건번호")

    return p


def main() -> None:
    args = build_parser().parse_args()
    path = Path(os.path.expanduser(args.csv)).resolve()
    {
        "init": cmd_init,
        "list": cmd_list,
        "get": cmd_get,
        "add": cmd_add,
        "update": cmd_update,
        "close": cmd_close,
    }[args.cmd](path, args)


if __name__ == "__main__":
    main()
