#!/bin/bash
# =====================================================================
# 软件著作权申请材料一键编译脚本
# 使用方法：chmod +x build_all.sh && ./build_all.sh
# 前置条件：已安装 XeLaTeX 环境和中文宏包
# =====================================================================

# 设置 TeX 路径（macOS BasicTeX 默认路径）
export PATH="/Library/TeX/texbin:$PATH"

# 进入脚本所在目录
cd "$(dirname "$0")"

# ===== 修改此处：填入实际的文件名（不含 .tex 后缀）=====
# 注意：申请表是 Markdown（.md），不参与 LaTeX 编译，因此不在此列表中。
DOCS=(
  "{{软件全称}}用户手册"
  "{{软件全称}}设计说明书"
  "{{软件全称}}源程序"
)

echo "开始编译软件著作权申请材料..."
echo ""

FAILED=0

for doc in "${DOCS[@]}"; do
  echo "=== 编译: ${doc}.tex ==="

  # 第一遍编译
  xelatex -interaction=nonstopmode "${doc}.tex" > /dev/null 2>&1
  # 第二遍编译（确保页码引用正确）
  xelatex -interaction=nonstopmode "${doc}.tex" > /dev/null 2>&1

  if [ -f "${doc}.pdf" ]; then
    size=$(ls -lh "${doc}.pdf" | awk '{print $5}')
    echo "  -> ${doc}.pdf (${size})"
  else
    echo "  !! 编译失败: ${doc}.tex"
    FAILED=$((FAILED + 1))
  fi

  # 清理临时文件
  rm -f "${doc}.aux" "${doc}.log" "${doc}.out" "${doc}.toc" "${doc}.fls" "${doc}.fdb_latexmk"
done

echo ""
if [ $FAILED -eq 0 ]; then
  echo "全部编译成功！"
else
  echo "有 ${FAILED} 个文件编译失败，请检查 .tex 文件内容。"
  echo ""
  echo "常见问题排查："
  echo "  1. 是否安装了 XeLaTeX？运行: xelatex --version"
  echo "  2. 是否安装了中文宏包？运行: tlmgr list --only-installed | grep ctex"
  echo "  3. 图片文件是否存在于 images/ 目录？"
  echo "  4. 手动编译查看详细错误: xelatex ${DOCS[0]}.tex"
fi
