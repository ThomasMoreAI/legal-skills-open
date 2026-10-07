#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render Mermaid code (.mmd) to PNG via mermaid-cli (mmdc).

Simplified wrapper reusing core logic from contract-review's mermaid_renderer.

Usage:
    python3 render_mermaid.py --input chart.mmd --output chart.png [--scale 2]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional


def normalize_mermaid_code(code: str) -> str:
    """Strip markdown code fences and ensure trailing newline."""
    cleaned = code.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if len(lines) >= 2 and lines[-1].strip().startswith("```"):
            cleaned = "\n".join(lines[1:-1]).strip()
    if not cleaned.endswith("\n"):
        cleaned += "\n"
    return cleaned


def render_mermaid_file(
    mmd_path: Path,
    image_path: Path,
    scale: float = 2,
    theme: str = "default",
    background_color: str = "white",
    width: Optional[int] = None,
    height: Optional[int] = None,
) -> None:
    """Render a .mmd file to PNG using mmdc with Chrome fallback."""
    mmdc_path = shutil.which("mmdc") or _find_mmdc()
    if not mmdc_path:
        raise FileNotFoundError("mmdc not found in PATH. Install @mermaid-js/mermaid-cli.")

    def build_cmd(input_path: Path, config_path: Optional[Path] = None) -> list[str]:
        cmd = [mmdc_path, "-i", str(input_path), "-o", str(image_path)]
        if theme:
            cmd += ["-t", theme]
        if background_color:
            cmd += ["-b", background_color]
        if scale and scale != 1:
            cmd += ["-s", str(scale)]
        if width:
            cmd += ["-w", str(width)]
        if height:
            cmd += ["-H", str(height)]
        if config_path:
            cmd += ["-p", str(config_path)]
        return cmd

    config_path: Optional[Path] = None
    created_config = False
    temp_user_data_dir: Optional[Path] = None

    try:
        # Attempt 1: direct mmdc
        try:
            subprocess.run(build_cmd(mmd_path), check=True, capture_output=True)
            return
        except subprocess.CalledProcessError:
            pass

        # Attempt 2: with Chrome/Puppeteer config
        chrome_path = os.environ.get("PUPPETEER_EXECUTABLE_PATH") or _find_chrome_executable()
        if chrome_path:
            config_path, temp_user_data_dir = _write_puppeteer_config(chrome_path)
            created_config = True
            try:
                subprocess.run(build_cmd(mmd_path, config_path), check=True, capture_output=True)
                return
            except subprocess.CalledProcessError:
                pass

        # Attempt 3: sanitize CJK/special chars then retry
        original = mmd_path.read_text(encoding="utf-8")
        sanitized = _sanitize_mermaid_code(original)
        if sanitized != original:
            sanitized_path = _write_temp_mmd(sanitized, mmd_path)
            try:
                cmd_config = config_path if created_config else None
                subprocess.run(build_cmd(sanitized_path, cmd_config), check=True, capture_output=True)
                return
            except subprocess.CalledProcessError:
                pass
            finally:
                sanitized_path.unlink(missing_ok=True)

        raise RuntimeError(f"Failed to render {mmd_path} after all attempts")
    finally:
        if created_config and config_path:
            config_path.unlink(missing_ok=True)
            if temp_user_data_dir:
                shutil.rmtree(temp_user_data_dir, ignore_errors=True)


def _find_mmdc() -> Optional[str]:
    """Search common npm global/local paths for mmdc."""
    home = Path.home()
    candidates = [
        home / ".npm-global" / "bin" / "mmdc",
        home / ".nvm" / "versions",  # handled below
        Path("/usr/local/bin/mmdc"),
        Path("/opt/homebrew/bin/mmdc"),
    ]
    for c in candidates:
        if c.is_file():
            return str(c)
    # Search nvm versions
    nvm_dir = home / ".nvm" / "versions" / "node"
    if nvm_dir.is_dir():
        for version_dir in sorted(nvm_dir.iterdir(), reverse=True):
            mmdc = version_dir / "bin" / "mmdc"
            if mmdc.is_file():
                return str(mmdc)
    return None


def _find_chrome_executable() -> Optional[str]:
    """Detect Chrome/Chromium on macOS."""
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    return None


def _write_puppeteer_config(executable_path: str) -> tuple[Path, Path]:
    """Create a temporary Puppeteer config for mmdc."""
    user_data_dir = Path(tempfile.mkdtemp(prefix="puppeteer-user-data-"))
    payload = {
        "executablePath": executable_path,
        "args": [
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-crashpad",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={user_data_dir}",
        ],
    }
    handle, path = tempfile.mkstemp(prefix="puppeteer-", suffix=".json")
    os.close(handle)
    config_path = Path(path)
    config_path.write_text(json.dumps(payload), encoding="utf-8")
    return config_path, user_data_dir


def _sanitize_mermaid_code(code: str) -> str:
    """Remove chars that can break mmdc rendering (%, CJK percent, etc.)."""
    if "%" not in code and "\uff05" not in code:
        return code
    has_cjk = any("\u4e00" <= ch <= "\u9fff" for ch in code)
    replacement = "\u767e\u5206\u6bd4" if has_cjk else "percent"  # 百分比
    sanitized = code.replace("\uff05", replacement).replace("%", replacement)
    sanitized = sanitized.replace("(", " ").replace(")", " ")
    sanitized = re.sub(r"\s{2,}", " ", sanitized)
    return sanitized


def _write_temp_mmd(code: str, source_path: Path) -> Path:
    """Write sanitized Mermaid code to a temp file."""
    handle, path = tempfile.mkstemp(prefix=f"{source_path.stem}-sanitized-", suffix=".mmd")
    os.close(handle)
    temp_path = Path(path)
    temp_path.write_text(code, encoding="utf-8")
    return temp_path


def main():
    parser = argparse.ArgumentParser(description="Render Mermaid .mmd to PNG")
    parser.add_argument("--input", required=True, help="Input .mmd file path")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--scale", type=float, default=2, help="Scale factor (default: 2)")
    parser.add_argument("--theme", default="default", help="Mermaid theme")
    parser.add_argument("--width", type=int, help="Image width")
    parser.add_argument("--height", type=int, help="Image height")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output)
    render_mermaid_file(
        input_path, output_path,
        scale=args.scale, theme=args.theme,
        width=args.width, height=args.height,
    )
    print(f"Rendered {input_path} -> {output_path}")


if __name__ == "__main__":
    main()
