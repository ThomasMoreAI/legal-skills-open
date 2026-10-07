#!/usr/bin/env python3
"""
软件著作权 - 项目分析 + 源程序 .tex 生成脚本

功能：
  1. 分析项目结构，检测项目类型（微信小程序/Web/Node.js 等）
  2. 识别遗留代码候选项（mockData / util.js 模板 / logs 等），列出供裁决
  3. 统计源代码有效行数
  4. 生成源程序 LaTeX 文件（前30页 + 后30页 = 60页）

用法：
  python3 analyze_and_generate_source.py <项目路径> \\
    --name "软件全称" \\
    --version "V1.0" \\
    --owner "著作权人名称" \\
    --date "2025年4月30日" \\
    --output <输出目录> \\
    [--exclude-pattern "utils/mockData.js" --exclude-pattern "pages/logs/**"] \\
    [--front-lines 1490 --back-lines 1498]

输出：
  - 控制台打印项目分析报告（项目类型、技术栈、文件统计、总行数）
  - 生成 <软件全称>源程序.tex 文件
  - project_analysis.json，含 legacy_candidates 字段
"""

import os
import sys
import json
import fnmatch
import argparse
from pathlib import Path
from collections import defaultdict


# ── 排版经验值（基于实际项目实测数据）──────────────────
# 10pt + \small Verbatim + 上下2cm左右1.5cm 边距
# 实测：2988行代码（含空行）精确填满60页

LINES_PER_FULL_PAGE = 50        # 标准页每页行数
FIRST_PAGE_HEADER_LINES = 10    # 首页标题区域占用的行数空间
BACK_HEADER_LINES = 2           # 后30页分隔标题占用的行数空间
TOTAL_PAGES = 60
HALF_PAGES = 30

# 前30页容量：首页减少 + 其余满页
FRONT_TARGET = (LINES_PER_FULL_PAGE - FIRST_PAGE_HEADER_LINES) + (HALF_PAGES - 1) * LINES_PER_FULL_PAGE  # 1490
# 后30页容量：首页减少 + 其余满页
BACK_TARGET = (LINES_PER_FULL_PAGE - BACK_HEADER_LINES) + (HALF_PAGES - 1) * LINES_PER_FULL_PAGE  # 1498


# ── 配置 ──────────────────────────────────────────────

# 识别为源代码的文件扩展名
CODE_EXTENSIONS = {
    '.js', '.ts', '.jsx', '.tsx',       # JavaScript/TypeScript
    '.wxml', '.wxss', '.wxs',           # 微信小程序
    '.vue', '.svelte',                   # 前端框架
    '.py',                               # Python
    '.java', '.kt',                      # Java/Kotlin
    '.go',                               # Go
    '.rs',                               # Rust
    '.swift',                            # Swift
    '.dart',                             # Dart/Flutter
    '.c', '.cpp', '.h', '.hpp',         # C/C++
    '.cs',                               # C#
    '.rb',                               # Ruby
    '.php',                              # PHP
    '.css', '.scss', '.less',           # 样式
    '.html', '.htm',                     # HTML
    '.sql',                              # SQL
    '.sh', '.bash',                      # Shell
}

# 排除的目录
EXCLUDE_DIRS = {
    '.git', 'node_modules', '__pycache__', 'dist', 'build',
    '.trae', '.vscode', '.idea', 'vendor', 'venv', '.env',
    'miniprogram_npm', 'typings', '.cache', 'coverage',
}

# 排除的文件名
EXCLUDE_FILES = {
    'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml',
    '.DS_Store', 'Thumbs.db',
}

# 遗留代码候选模式（识别但不自动排除，由 Claude+用户裁决）
LEGACY_PATTERNS = [
    # (模式, 描述, 触发条件 lambda(rel_path, abs_path) -> bool 或 None=仅按文件名匹配)
    ('mockData*.js', 'Mock 假数据', None),
    ('mockData*.ts', 'Mock 假数据', None),
    ('mock*.js', 'Mock 数据/工具', None),
    ('fakeData*.js', '假数据', None),
    ('pages/logs/**', '微信小程序默认模板日志页', None),
    ('miniprogram/pages/logs/**', '微信小程序默认模板日志页', None),
    # util.js 仅当 < 1KB 或仅含模板函数时视为遗留
    ('util.js', '微信小程序默认模板（仅 formatTime 等样板）',
     lambda rel, abs: abs.stat().st_size < 1024
     or _is_template_util(abs)),
    ('utils/util.js', '微信小程序默认模板（仅 formatTime 等样板）',
     lambda rel, abs: abs.stat().st_size < 1024
     or _is_template_util(abs)),
]


def _is_template_util(abs_path: Path) -> bool:
    """判断 util.js 是否为微信小程序默认模板。
    默认模板特征：仅含 formatTime / formatNumber 等样板函数，无业务代码。
    """
    try:
        text = abs_path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return False
    # 默认模板的典型 API 是 formatTime + formatNumber，且 module.exports 只导出这两个
    has_format_time = 'formatTime' in text
    has_format_number = 'formatNumber' in text
    # 没有典型业务关键字（API 调用、wx. 调用、import 业务模块）
    no_business = (
        'wx.request' not in text
        and 'wx.login' not in text
        and 'require(' not in text.replace('require(\'./formatNumber\')', '')
    )
    return has_format_time and has_format_number and no_business


def detect_legacy_candidates(code_files: list, project_path: Path) -> list:
    """扫描遗留代码候选项，返回 [{path, reason, size}]"""
    candidates = []
    seen = set()
    for rel, abspath in code_files:
        rel_str = str(rel)
        if rel_str in seen:
            continue
        for pattern, desc, cond in LEGACY_PATTERNS:
            if fnmatch.fnmatch(rel_str, pattern) or fnmatch.fnmatch(rel.name, pattern):
                if cond is None or cond(rel, abspath):
                    try:
                        size = abspath.stat().st_size
                    except Exception:
                        size = 0
                    candidates.append({
                        'path': rel_str,
                        'reason': desc,
                        'matched_pattern': pattern,
                        'size_bytes': size,
                    })
                    seen.add(rel_str)
                    break
    return candidates


def filter_by_exclude_patterns(code_files: list, exclude_patterns: list) -> list:
    """按用户指定的 glob 模式剔除文件"""
    if not exclude_patterns:
        return code_files
    filtered = []
    for rel, abspath in code_files:
        rel_str = str(rel)
        excluded = False
        for pat in exclude_patterns:
            if fnmatch.fnmatch(rel_str, pat) or fnmatch.fnmatch(rel.name, pat):
                excluded = True
                break
        if not excluded:
            filtered.append((rel, abspath))
    return filtered

# 文件优先级（数字越小越优先）
PRIORITY_RULES = [
    (lambda p: p.name == 'app.js', 0),
    (lambda p: p.name == 'app.ts', 1),
    (lambda p: p.name == 'main.js', 2),
    (lambda p: p.name == 'main.ts', 3),
    (lambda p: p.name == 'index.js', 4),
    (lambda p: p.name == 'index.ts', 5),
    (lambda p: 'utils' in p.parts, 10),
    (lambda p: 'helpers' in p.parts, 11),
    (lambda p: 'services' in p.parts, 12),
    (lambda p: 'api' in p.parts, 13),
    (lambda p: 'pages' in p.parts, 20),
    (lambda p: 'views' in p.parts, 21),
    (lambda p: 'components' in p.parts, 30),
    (lambda p: 'config' in p.parts, 40),
    (lambda p: p.suffix in {'.css', '.scss', '.less', '.wxss'}, 50),
]


# ── 项目分析 ──────────────────────────────────────────

def detect_project_type(project_path: Path) -> dict:
    """检测项目类型和基本信息"""
    info = {
        'type': '未知',
        'platform': '',
        'tech_stack': [],
        'name': '',
        'description': '',
    }

    # 微信小程序
    if (project_path / 'app.json').exists():
        info['type'] = '微信小程序'
        info['platform'] = 'iOS、Android、Windows、macOS、HarmonyOS（微信客户端）'
        info['tech_stack'].append('微信小程序原生框架（WXML + WXSS + JavaScript）')
        try:
            with open(project_path / 'app.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                info['name'] = data.get('window', {}).get('navigationBarTitleText', '')
        except Exception:
            pass

    # project.config.json（小程序）
    if (project_path / 'project.config.json').exists():
        try:
            with open(project_path / 'project.config.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                info['appid'] = data.get('appid', '')
                info['lib_version'] = data.get('libVersion', '')
                compiler = data.get('compileType', '')
                if compiler:
                    info['tech_stack'].append(f'编译类型: {compiler}')
        except Exception:
            pass

    # package.json
    if (project_path / 'package.json').exists():
        try:
            with open(project_path / 'package.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not info['name']:
                    info['name'] = data.get('name', '')
                info['description'] = data.get('description', '')
                deps = list(data.get('dependencies', {}).keys())
                if 'vue' in deps:
                    info['tech_stack'].append('Vue.js')
                if 'react' in deps:
                    info['tech_stack'].append('React')
                if 'express' in deps:
                    info['tech_stack'].append('Express.js')
                if info['type'] == '未知':
                    info['type'] = 'Web/Node.js'
                    info['platform'] = 'Windows、macOS、Linux（浏览器）'
        except Exception:
            pass

    return info


def collect_code_files(project_path: Path) -> list:
    """收集所有源代码文件，返回 (相对路径, 绝对路径) 列表"""
    files = []
    for root, dirs, filenames in os.walk(project_path):
        # 排除目录
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fname in filenames:
            if fname in EXCLUDE_FILES:
                continue
            fpath = Path(root) / fname
            if fpath.suffix.lower() in CODE_EXTENSIONS:
                rel = fpath.relative_to(project_path)
                files.append((rel, fpath))
    return files


def get_file_priority(rel_path: Path) -> int:
    """返回文件优先级分数"""
    for rule_fn, priority in PRIORITY_RULES:
        if rule_fn(rel_path):
            return priority
    return 99


def count_effective_lines(filepath: Path) -> int:
    """统计有效代码行数（排除空行和纯注释行）"""
    count = 0
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            in_block_comment = False
            for line in f:
                stripped = line.strip()
                # 跳过空行
                if not stripped:
                    continue
                # 块注释处理
                if in_block_comment:
                    if '*/' in stripped:
                        in_block_comment = False
                    continue
                if stripped.startswith('/*'):
                    if '*/' not in stripped[2:]:
                        in_block_comment = True
                    continue
                # 单行注释
                if stripped.startswith('//') or stripped.startswith('#'):
                    continue
                # 纯 XML 注释
                if stripped.startswith('<!--') and stripped.endswith('-->'):
                    continue
                count += 1
    except Exception:
        pass
    return count


def count_total_lines(filepath: Path) -> int:
    """统计文件总行数"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0


def read_file_content(filepath: Path, strip_empty: bool = True) -> list:
    """读取文件所有行，返回行列表。strip_empty=True 时去除空行"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            if strip_empty:
                lines = [l for l in lines if l.strip()]
            return lines
    except Exception:
        return []


# ── LaTeX 源程序生成 ──────────────────────────────────

def escape_latex_verbatim(text: str) -> str:
    """Verbatim 环境内无需转义，但需要确保没有 \\end{Verbatim}"""
    return text.replace('\\end{Verbatim}', '\\end {Verbatim}')


def generate_source_tex(
    project_path: Path,
    code_files: list,
    total_lines: int,
    software_name: str,
    version: str,
    owner: str,
    date: str,
    output_path: Path,
    front_target: int = FRONT_TARGET,
    back_target: int = BACK_TARGET,
):
    """
    生成源程序 .tex 文件（前30页 + 后30页 = 60页）

    排版经验值（10pt + \\small Verbatim + 上下2cm左右1.5cm）：
      - 标准页容量：50行/页
      - 首页因标题区域减少约10行 → 40行
      - 后30页首页因分隔标题减少约2行 → 48行
      - 前30页目标：1490行，后30页目标：1498行，合计2988行
      - 代码不足时直接使用全部代码，不强凑60页
      - 编译后若 PDF 不是 60 页，调整 front_target / back_target 微调（每次 ±2~5 行试探）
    """

    # 按优先级排序
    sorted_files = sorted(code_files, key=lambda x: get_file_priority(x[0]))

    # ── 收集所有代码行（去除空行）──
    all_code_lines = []
    file_boundaries = []  # (start_index, rel_path)
    for rel, abspath in sorted_files:
        content = read_file_content(abspath, strip_empty=True)
        if not content:
            continue
        separator = f'// ========== {rel} ==========\n'
        start_idx = len(all_code_lines)
        all_code_lines.append(separator)
        all_code_lines.extend(content)
        file_boundaries.append((start_idx, str(rel)))

    total_code = len(all_code_lines)

    # ── 判断代码量是否足够60页 ──
    total_target = front_target + back_target  # 2988

    if total_code <= total_target:
        # 代码不足，全部使用，不分前后
        # 按实际行数计算能填多少页
        front_lines = all_code_lines
        back_lines = []
        front_end_line = total_code
        back_start_line = 0
        use_full = True
        print(f'  代码总量 {total_code} 行，不足 {total_target} 行，将使用全部代码')
    else:
        # 代码充足，取前 front_target 行 + 后 back_target 行
        front_lines = all_code_lines[:front_target]
        back_lines = all_code_lines[-back_target:]
        front_end_line = front_target
        back_start_line = total_lines - back_target + 1
        use_full = False

    # ── 生成 .tex ──
    front_text = escape_latex_verbatim(''.join(front_lines))

    if use_full:
        # 代码不足60页，只生成一个 Verbatim 块
        tex = rf"""\documentclass[a4paper,10pt]{{article}}
\usepackage[UTF8]{{ctex}}
\usepackage[top=2cm,bottom=2cm,left=1.5cm,right=1.5cm]{{geometry}}
\usepackage{{fancyhdr}}
\usepackage{{lastpage}}
\usepackage{{hyperref}}
\usepackage{{fancyvrb}}

\hypersetup{{hidelinks}}

\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[C]{{{software_name}{version}\quad 源程序}}
\fancyfoot[C]{{第 \thepage\ 页\quad 共 \pageref{{LastPage}} 页}}
\renewcommand{{\headrulewidth}}{{0.5pt}}
\renewcommand{{\footrulewidth}}{{0.5pt}}
\fancypagestyle{{plain}}{{\pagestyle{{fancy}}}}

\setlength{{\parindent}}{{0em}}

\begin{{document}}

\begin{{center}}
  {{\LARGE\bfseries {software_name}\quad 源程序}}

  \vspace{{0.5em}}
  {{\large 著作权人：{owner}}}

  \vspace{{0.3em}}
  软件名称：{software_name}\qquad 版本号：{version}\qquad 生成日期：{date}

  \vspace{{0.3em}}
  源程序量：{total_lines}行\qquad 本文档含全部源程序
\end{{center}}

\vspace{{0.3em}}

\begin{{Verbatim}}[fontsize=\small]
{front_text}\end{{Verbatim}}

\end{{document}}
"""
    else:
        back_text = escape_latex_verbatim(''.join(back_lines))
        tex = rf"""\documentclass[a4paper,10pt]{{article}}
\usepackage[UTF8]{{ctex}}
\usepackage[top=2cm,bottom=2cm,left=1.5cm,right=1.5cm]{{geometry}}
\usepackage{{fancyhdr}}
\usepackage{{lastpage}}
\usepackage{{hyperref}}
\usepackage{{fancyvrb}}

\hypersetup{{hidelinks}}

\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[C]{{{software_name}{version}\quad 源程序}}
\fancyfoot[C]{{第 \thepage\ 页\quad 共 \pageref{{LastPage}} 页}}
\renewcommand{{\headrulewidth}}{{0.5pt}}
\renewcommand{{\footrulewidth}}{{0.5pt}}
\fancypagestyle{{plain}}{{\pagestyle{{fancy}}}}

\setlength{{\parindent}}{{0em}}

\begin{{document}}

\begin{{center}}
  {{\LARGE\bfseries {software_name}\quad 源程序}}

  \vspace{{0.5em}}
  {{\large 著作权人：{owner}}}

  \vspace{{0.3em}}
  软件名称：{software_name}\qquad 版本号：{version}\qquad 生成日期：{date}

  \vspace{{0.3em}}
  源程序量：{total_lines}行\qquad 本文档含前30页 + 后30页
\end{{center}}

\vspace{{0.3em}}

\begin{{center}}\large\bfseries —— 前30页（第1--{front_end_line}行）——\end{{center}}

\begin{{Verbatim}}[fontsize=\small]
{front_text}\end{{Verbatim}}

\newpage
\begin{{center}}\large\bfseries —— 后30页（第{back_start_line}--{total_lines}行）——\end{{center}}

\begin{{Verbatim}}[fontsize=\small]
{back_text}\end{{Verbatim}}

\end{{document}}
"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(tex)

    return front_end_line, back_start_line


# ── 主程序 ────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='软著项目分析 + 源程序 .tex 生成')
    parser.add_argument('project_path', help='项目根目录路径')
    parser.add_argument('--name', required=True, help='软件全称')
    parser.add_argument('--version', default='V1.0', help='版本号（默认 V1.0）')
    parser.add_argument('--owner', required=True, help='著作权人名称')
    parser.add_argument('--date', required=True, help='生成日期（如：2025年4月30日）')
    parser.add_argument('--output', default='.', help='输出目录（默认当前目录）')
    parser.add_argument('--exclude-pattern', action='append', default=[],
                        help='额外排除的文件 glob 模式，可重复传入。例：--exclude-pattern "utils/mockData.js" --exclude-pattern "pages/logs/**"')
    parser.add_argument('--front-lines', type=int, default=FRONT_TARGET,
                        help=f'前30页目标代码行数（默认 {FRONT_TARGET}）。编译后若 PDF 不是 60 页，调整此值微调')
    parser.add_argument('--back-lines', type=int, default=BACK_TARGET,
                        help=f'后30页目标代码行数（默认 {BACK_TARGET}）。编译后若 PDF 不是 60 页，调整此值微调')

    args = parser.parse_args()
    project_path = Path(args.project_path).resolve()
    output_dir = Path(args.output).resolve()

    if not project_path.is_dir():
        print(f'错误：项目路径不存在 {project_path}')
        sys.exit(1)

    # ── 1. 项目分析 ──
    print('=' * 60)
    print('项目分析报告')
    print('=' * 60)

    info = detect_project_type(project_path)
    print(f'项目类型：{info["type"]}')
    print(f'运行平台：{info["platform"]}')
    print(f'技术栈：{", ".join(info["tech_stack"]) or "待确认"}')
    if info.get('appid'):
        print(f'AppID：{info["appid"]}')

    # ── 2. 代码统计 ──
    code_files = collect_code_files(project_path)

    # 识别遗留代码候选项（在过滤前扫描，让用户看到完整清单）
    legacy_candidates = detect_legacy_candidates(code_files, project_path)
    if legacy_candidates:
        print('\n⚠️  发现以下遗留代码候选项（mockData / 默认模板 / 日志页等）：')
        for c in legacy_candidates:
            print(f'  - {c["path"]}  ({c["reason"]}, {c["size_bytes"]}B)')
        print('  → 已通过 legacy_candidates 字段输出到 project_analysis.json')
        print('  → 如需排除，请用 --exclude-pattern "<glob>" 重新运行本脚本')

    # 应用用户指定的排除模式
    if args.exclude_pattern:
        before = len(code_files)
        code_files = filter_by_exclude_patterns(code_files, args.exclude_pattern)
        print(f'\n按用户指定的排除模式 {args.exclude_pattern} 剔除了 {before - len(code_files)} 个文件')

    print(f'\n代码文件数：{len(code_files)}')

    ext_stats = defaultdict(lambda: {'files': 0, 'lines': 0})
    total_effective = 0
    total_raw = 0

    for rel, abspath in code_files:
        ext = rel.suffix.lower()
        raw = count_total_lines(abspath)
        effective = count_effective_lines(abspath)
        ext_stats[ext]['files'] += 1
        ext_stats[ext]['lines'] += effective
        total_effective += effective
        total_raw += raw

    print(f'总行数（含空行和注释）：{total_raw}')
    print(f'有效代码行数：{total_effective}')

    print(f'\n按文件类型统计：')
    for ext, stat in sorted(ext_stats.items(), key=lambda x: -x[1]['lines']):
        print(f'  {ext:8s}  {stat["files"]:4d} 文件  {stat["lines"]:6d} 行')

    # ── 3. 生成源程序 .tex ──
    tex_filename = f'{args.name}源程序.tex'
    output_path = output_dir / tex_filename

    front_end, back_start = generate_source_tex(
        project_path=project_path,
        code_files=code_files,
        total_lines=total_effective,
        software_name=args.name,
        version=args.version,
        owner=args.owner,
        date=args.date,
        output_path=output_path,
        front_target=args.front_lines,
        back_target=args.back_lines,
    )

    print(f'\n源程序文档已生成：{output_path}')
    print(f'  前30页：第 1 - {front_end} 行  （目标 {args.front_lines} 行）')
    print(f'  后30页：第 {back_start} - {total_effective} 行  （目标 {args.back_lines} 行）')
    estimated_pages = round((args.front_lines + args.back_lines) / LINES_PER_FULL_PAGE)
    print(f'  估算页数（按 {LINES_PER_FULL_PAGE} 行/页）：约 {estimated_pages} 页')
    print('  → 编译后请用 `pdfinfo <软件全称>源程序.pdf | grep Pages` 核对是否正好 60 页')
    print('  → 如不是 60 页，调整 --front-lines / --back-lines 重新生成')

    # ── 4. 输出 JSON 供 Claude 使用 ──
    report = {
        'project_type': info['type'],
        'platform': info['platform'],
        'tech_stack': info['tech_stack'],
        'total_files': len(code_files),
        'total_lines_raw': total_raw,
        'total_lines_effective': total_effective,
        'source_tex': str(output_path),
        'ext_stats': {k: v for k, v in ext_stats.items()},
        'legacy_candidates': legacy_candidates,
        'exclude_patterns_applied': args.exclude_pattern,
        'front_target_lines': args.front_lines,
        'back_target_lines': args.back_lines,
    }
    report_path = output_dir / 'project_analysis.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f'分析报告已保存：{report_path}')


if __name__ == '__main__':
    main()
