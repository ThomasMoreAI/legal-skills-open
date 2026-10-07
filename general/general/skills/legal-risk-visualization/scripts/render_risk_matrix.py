#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render a risk matrix (probability × impact) scatter plot to PNG using matplotlib.

Professional legal style with improved color scheme:
- Muted professional color palette
- Clear data visualization with good contrast
- Color-blind friendly palette

Usage:
    python3 render_risk_matrix.py \
        --data '[{"name":"企业用工成本上升","p":0.9,"i":0.6,"score":0.34}]' \
        --output risk_matrix.png
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np


# Professional legal color scheme
COLOR_BG = "#FAFAFA"             # 浅灰背景
COLOR_GRID = "#DDDDDD"           # 网格线

# Risk level colors (professional palette)
COLOR_SAFE = "#6B9B37"           # 1-2级 安全 - 橄榄绿
COLOR_ATTENTION = "#F0A830"     # 3级 关注 - 琥珀色
COLOR_ALERT = "#C0392B"          # 4-5级 警戒 - 深红

# Node type colors (professional blue-greys)
COLOR_SOURCE = "#2C5282"        # 风险源头 - 深蓝
COLOR_INTERM = "#5D7D9A"         # 中间环节 - 蓝灰
COLOR_CONSEQ = "#D9775A"         # 风险后果 - 棕色
COLOR_IMPACT = "#8874A3"         # 业务影响 - 青色

# Color for unconfirmed edges
COLOR_UNCONFIRMED = "#9E9EAF"


def _quadrant_background_color(p: float, i: float) -> str:
    """Background color for each quadrant (subtle)."""
    if p >= 0.5 and i >= 0.5:
        return "#FDF2F5"  # 右上 - 极浅红
    elif p < 0.5 and i >= 0.5:
        return "#FEF7E2"  # 左上 - 极浅橙
    elif p >= 0.5 and i < 0.5:
        return "#E8F5E9"  # 右下 - 极浅绿
    else:
        return "#F0F4F4"  # 左下 - 浅灰


def _find_cjk_font() -> str | None:
    """Find a CJK-capable font on system (macOS priority)."""
    preferred = [
        "PingFang SC",
        "Hiragino Sans GB",
        "STHeiti",
        "Microsoft YaHei",
        "SimHei",
        "Noto Sans CJK SC",
        "WenQuanYi Micro Hei",
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for name in preferred:
        if name in available:
            return name
    return None


def render_risk_matrix(
    data: list[dict],
    output_path: str | Path,
    title: str = "风险矩阵",
    dpi: int = 150,
) -> Path:
    """
    Generate a professional risk matrix scatter plot PNG.

    Args:
        data: list of dicts, each with keys:
              "name" (str), "p" (float 0-1), "i" (float 0-1), "score" (float, risk index)
        output_path: where to write the PNG
        title: chart title
        dpi: output resolution
    """
    output_path = Path(output_path)

    # Font setup
    font_name = _find_cjk_font()
    if font_name:
        plt.rcParams["font.family"] = font_name
    plt.rcParams["axes.unicode_minus"] = False

    if not data:
        raise ValueError("Risk matrix requires at least 1 data point")

    # Create figure with professional styling
    fig, ax = plt.subplots(figsize=(9, 8))
    fig.patch.set_facecolor(COLOR_BG)

    # Draw quadrant backgrounds (subtle)
    for p_corner in [0.25, 0.75]:
        for i_corner in [0.25, 0.75]:
            x_center = (p_corner + 0.25) / 2
            y_center = (i_corner + 0.25) / 2
            width = 0.5
            height = 0.5
            color = _quadrant_background_color(p_corner, i_corner)
            rect = mpatches.Rectangle((x_center - width/2, y_center - height/2),
                                     width, height,
                                     facecolor=color, edgecolor="none", alpha=0.6, zorder=0)
            ax.add_patch(rect)

    # Quadrant divider lines
    ax.axhline(y=0.5, color=COLOR_GRID, linewidth=1.2, linestyle="--", zorder=1, alpha=0.7)
    ax.axvline(x=0.5, color=COLOR_GRID, linewidth=1.2, linestyle="--", zorder=1, alpha=0.7)

    # Quadrant labels (professional styling)
    label_style = dict(fontsize=13, fontweight="bold", ha="center", va="center", alpha=0.85)
    ax.text(0.75, 0.75, "高优先级", color=COLOR_ALERT, **label_style)
    ax.text(0.25, 0.75, "重点关注", color=COLOR_ATTENTION, **label_style)
    ax.text(0.75, 0.25, "常规监控", color="#7F8C8D", **label_style)
    ax.text(0.25, 0.25, "持续观察", color=COLOR_SAFE, **label_style)

    # Plot bubbles with professional styling
    for item in data:
        p = item["p"]
        i_val = item["i"]
        score = item.get("score", 0.1)
        name = item["name"]

        # Color by risk level
        if p >= 0.5 and i_val >= 0.5:
            color = COLOR_ALERT
        elif p >= 0.5 or i_val >= 0.5:
            color = COLOR_ATTENTION
        else:
            color = COLOR_SAFE

        # Bubble size proportional to score, with minimum visibility
        size = max(score, 0.08) * 2000

        ax.scatter(p, i_val, s=size, c=color, alpha=0.75, edgecolors="white",
                   linewidth=1.5, zorder=3)

        # Label: offset upward to avoid overlap with bubble
        ax.annotate(
            name,
            (p, i_val),
            textcoords="offset points",
            xytext=(0, int(math.sqrt(size) / 2) + 8),
            ha="center", va="bottom",
            fontsize=9.5, fontweight="500",
            color="#333333",
            zorder=4,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#CCCCCC",
                      linewidth=0.8, alpha=0.9),
        )

    # Axes with professional styling
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.set_xlabel("发生可能性 →", fontsize=13, fontweight="bold", labelpad=12, color="#333333")
    ax.set_ylabel("影响严重性 →", fontsize=13, fontweight="bold", labelpad=12, color="#333333")
    ax.set_title(title, fontsize=16, fontweight="bold", pad=18, color="#222222")

    # Tick labels
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0", "0.25", "0.5", "0.75", "1.0"], fontsize=10, color="#666666")
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0", "0.25", "0.5", "0.75", "1.0"], fontsize=10, color="#666666")

    # Grid
    ax.grid(True, color=COLOR_GRID, alpha=0.4, linestyle=":", linewidth=0.8)
    ax.set_aspect("equal")

    # Legend (professional style)
    legend_elements = [
        mpatches.Patch(facecolor=COLOR_ALERT, alpha=0.6, label="高优先级 (4-5级)", edgecolor="#CCCCCC"),
        mpatches.Patch(facecolor=COLOR_ATTENTION, alpha=0.6, label="重点关注 (3级)", edgecolor="#CCCCCC"),
        mpatches.Patch(facecolor=COLOR_SAFE, alpha=0.6, label="持续观察 (1-2级)", edgecolor="#CCCCCC"),
    ]
    ax.legend(
        handles=legend_elements,
        loc="upper left",
        fontsize=10,
        framealpha=0.9,
        facecolor="#FAFAFA",
        edgecolor="#DDDDDD",
    )

    fig.tight_layout()
    fig.savefig(str(output_path), dpi=dpi, bbox_inches="tight", facecolor=COLOR_BG)
    plt.close(fig)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Render risk matrix scatter plot to PNG")
    parser.add_argument(
        "--data",
        required=True,
        help='JSON array: [{"name":"...", "p":0.9, "i":0.6, "score":0.34}, ...]',
    )
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--title", default="风险矩阵", help="Chart title")
    parser.add_argument("--dpi", type=int, default=150, help="Output DPI")
    args = parser.parse_args()

    try:
        data = json.loads(args.data)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in --data: {e}", file=sys.stderr)
        sys.exit(1)

    out = render_risk_matrix(data, args.output, title=args.title, dpi=args.dpi)
    print(f"Risk matrix saved to {out}")


if __name__ == "__main__":
    main()
