#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render a radar (spider/polar) chart from dimension scores to PNG.

Professional legal/financial style with improved color scheme:
- Muted professional blue tones as base
- Soft risk level bands (pastel backgrounds)
- Clear contrast for data visualization
- Color-blind friendly palette

Usage:
    python3 render_radar.py --data '{"诉讼风险":2,"财务风险":2,"运营风险":2,"执行风险":2}' --output radar.png
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
import numpy as np


# Professional legal color scheme
# 主色调：柔和的蓝色系
COLOR_PRIMARY = "#2C5282"      # 深蓝 - 主色、数据线
COLOR_SECONDARY = "#5D7D9A"    # 灰蓝 - 次要数据
COLOR_TERTIARY = "#88B3C7"     # 浅蓝 - 辅助色

# 风险等级色（柔和但清晰）
COLOR_SAFE = "#6B9B37"          # 1-2级 安全 - 柔和橄榄绿
COLOR_ATTENTION = "#F0A830"      # 3级 关注 - 温暖橙色
COLOR_ALERT = "#C0392B"          # 4-5级 警戒 - 深红

# 功能色（专业蓝色系）
COLOR_CONTROL = "#4472C4"         # 可控节点 - 深蓝紫
COLOR_UNCONFIRMED = "#9E9EAF"     # 待确认 - 灰色

# 等级标签
LEVEL_LABELS = {1: "极低", 2: "低", 3: "中", 4: "高", 5: "极高"}


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


def _get_level_color(score: float) -> str:
    """Get color for a given score value."""
    if score <= 2:
        return COLOR_SAFE
    elif score <= 3:
        return COLOR_ATTENTION
    else:
        return COLOR_ALERT


def render_radar(
    data: dict[str, int | float],
    output_path: str | Path,
    title: str = "风险雷达图",
    max_score: int = 5,
    dpi: int = 150,
) -> Path:
    """
    Generate a professional radar chart PNG.

    Args:
        data: mapping of dimension name -> score (1-max_score)
        output_path: where to write the PNG
        title: chart title
        max_score: max grid value (default 5)
        dpi: output resolution
    """
    output_path = Path(output_path)

    # Font setup
    font_name = _find_cjk_font()
    if font_name:
        plt.rcParams["font.family"] = font_name
    plt.rcParams["axes.unicode_minus"] = False

    labels = list(data.keys())
    values = [min(max(v, 0), max_score) for v in data.values()]
    n = len(labels)
    if n < 3:
        raise ValueError("Radar chart requires at least 3 dimensions")

    # Compute angles
    angles = [i * 2 * math.pi / n for i in range(n)]
    values_closed = values + [values[0]]
    angles_closed = angles + [angles[0]]

    # Create figure with professional style
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("#FAFAFA")  # 浅灰背景

    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)

    # Draw soft concentric risk level bands
    theta_fill = np.linspace(0, 2 * np.pi, 100)

    # Level 1-2: Safe (soft green tint)
    ax.fill_between(theta_fill, 0, 2, alpha=0.15, color="#E8F5E9", zorder=0)
    # Level 3: Attention (soft amber tint)
    ax.fill_between(theta_fill, 2, 3, alpha=0.18, color="#FEF3C7", zorder=0)
    # Level 4-5: Alert (soft red tint)
    ax.fill_between(theta_fill, 3, max_score, alpha=0.15, color="#FADBD8", zorder=0)

    # Draw level boundary circles
    for level in range(1, max_score + 1):
        color = "#CCCCCC"
        linewidth = 0.8 if level in [2, 3, max_score] else 0.5
        alpha = 0.4 if level in [2, 3, max_score] else 0.2
        ax.plot(theta_fill, [level] * len(theta_fill), color=color,
                linewidth=linewidth, alpha=alpha, zorder=1)

    # Grid settings
    ax.set_ylim(0, max_score)
    ax.set_yticks(range(1, max_score + 1))

    # Level labels with both number and text
    ytick_labels = []
    for i in range(1, max_score + 1):
        label = LEVEL_LABELS.get(i, str(i))
        ytick_labels.append(f"{i} {label}")
    ax.set_yticklabels(ytick_labels, fontsize=9, color="#555555", fontweight="medium")

    # Dimension labels
    ax.set_xticks(angles)
    ax.set_xticklabels(labels, fontsize=12, fontweight="bold", color="#333333")

    # Plot data polygon with professional styling
    ax.plot(angles_closed, values_closed, "o-", linewidth=2.5, color=COLOR_PRIMARY,
            markersize=6, zorder=5, markerfacecolor="#FAFAFA", markeredgewidth=1.5)
    ax.fill(angles_closed, values_closed, alpha=0.25, color=COLOR_PRIMARY, zorder=4)

    # Annotate actual scores at each vertex
    for angle, value, label in zip(angles, values, labels):
        score_color = _get_level_color(value)

        # Offset text slightly outward
        offset_r = value + 0.4
        if offset_r > max_score:
            offset_r = value - 0.5

        ax.text(
            angle, offset_r,
            f"{value:.0f}" if value == int(value) else f"{value:.1f}",
            ha="center", va="center",
            fontsize=11, fontweight="bold",
            color="#333333",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                     edgecolor=score_color, linewidth=2, alpha=0.95),
            zorder=6,
        )

    # Title
    ax.set_title(title, fontsize=16, fontweight="bold", pad=25, color="#222222")

    # Style
    ax.grid(True, color="#DDDDDD", linewidth=0.5, alpha=0.6)
    ax.spines["polar"].set_color("#BBBBBB")
    ax.spines["polar"].set_linewidth(1)
    ax.set_facecolor("#FAFAFA")

    fig.tight_layout()
    fig.savefig(str(output_path), dpi=dpi, bbox_inches="tight", facecolor="#FAFAFA")
    plt.close(fig)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Render radar chart to PNG")
    parser.add_argument(
        "--data",
        required=True,
        help='JSON object: {"维度名": 分数, ...}',
    )
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--title", default="风险雷达图", help="Chart title")
    parser.add_argument("--max-score", type=int, default=5, help="Max grid value")
    parser.add_argument("--dpi", type=int, default=150, help="Output DPI")
    args = parser.parse_args()

    try:
        data = json.loads(args.data)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in --data: {e}", file=sys.stderr)
        sys.exit(1)

    out = render_radar(data, args.output, title=args.title, max_score=args.max_score, dpi=args.dpi)
    print(f"Radar chart saved to {out}")


if __name__ == "__main__":
    main()
