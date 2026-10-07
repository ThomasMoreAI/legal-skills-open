#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
错误处理和用户反馈工具
Error Handling and User Feedback Utilities

提供统一的错误处理、日志记录和用户反馈功能。
"""

import sys
import traceback
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path


# ==================== 自定义异常类 ====================

class ReviewError(Exception):
    """合同审核基础异常类"""
    pass


class CommentNotFoundError(ReviewError):
    """批注目标未找到错误"""
    pass


class DocumentValidationError(ReviewError):
    """文档验证失败错误"""
    pass


class PythonVersionError(ReviewError):
    """Python 版本不兼容错误"""
    pass


class UnpackError(ReviewError):
    """文档解包失败错误"""
    pass


class PackError(ReviewError):
    """文档打包失败错误"""
    pass


# ==================== 版本检查 ====================

def check_python_version(min_version: tuple = (3, 9),
                        recommended_version: tuple = (3, 10)) -> None:
    """
    检查 Python 版本是否满足要求

    Args:
        min_version: 最低版本要求 (默认 3.9)
        recommended_version: 推荐版本 (默认 3.10)

    Raises:
        PythonVersionError: 如果版本低于最低要求

    Example:
        >>> check_python_version()  # 默认要求 3.9+
        >>> check_python_version((3, 10))  # 要求 3.10+
    """
    current = (sys.version_info.major, sys.version_info.minor)

    if current < min_version:
        raise PythonVersionError(
            f"Python {'.'.join(map(str, min_version))}+ required, "
            f"current: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        )

    if current < recommended_version:
        import warnings
        warnings.warn(
            f"Python {'.'.join(map(str, recommended_version))}+ recommended for best compatibility. "
            f"Current: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            UserWarning
        )


# ==================== 错误格式化 ====================

def format_error_summary(errors: List[Dict]) -> str:
    """
    格式化错误摘要为可读文本

    Args:
        errors: 错误列表,每个错误包含 type, location, message, suggestion 等字段

    Returns:
        str: 格式化的错误摘要文本

    Example:
        >>> errors = [
        ...     {"type": "文本一致性", "location": "第10行", "message": "金额不一致"},
        ...     {"type": "合同标的", "location": "第20行", "message": "数量不明确"}
        ... ]
        >>> print(format_error_summary(errors))
    """
    if not errors:
        return "✓ 无错误"

    lines = []
    lines.append(f"✗ 发现 {len(errors)} 个错误:\n")

    for i, error in enumerate(errors, 1):
        lines.append(f"\n{i}. {error.get('type', 'Unknown Error')}")
        lines.append(f"   位置: {error.get('location', 'N/A')}")
        lines.append(f"   原因: {error.get('message', 'N/A')}")

        if 'suggestion' in error:
            lines.append(f"   建议: {error['suggestion']}")

        if 'risk_level' in error:
            lines.append(f"   风险等级: {error['risk_level']}")

    return '\n'.join(lines)


# ==================== 批注批处理日志记录器 ====================

class CommentBatchLogger:
    """
    批注批处理日志记录器

    记录批注添加过程中的成功、失败和警告,
    并生成详细的执行报告。

    Attributes:
        successful: 成功添加的批注列表
        failed: 失败的批注列表
        warnings: 警告列表
        start_time: 开始时间

    Example:
        >>> logger = CommentBatchLogger()
        >>> try:
        ...     logger.log_success(1, "合同总价")
        ... except Exception as e:
        ...     logger.log_failure("合同总价", e)
        >>> print(logger.generate_summary())
    """

    def __init__(self):
        """初始化日志记录器"""
        self.successful = []
        self.failed = []
        self.warnings = []
        self.start_time = datetime.now()

    def log_success(self, comment_id: int, search_text: str, preview: str = ""):
        """
        记录成功添加的批注

        Args:
            comment_id: 批注ID
            search_text: 搜索文本
            preview: 批注内容预览(可选)
        """
        self.successful.append({
            'id': comment_id,
            'search': search_text,
            'preview': preview,
            'timestamp': datetime.now()
        })

    def log_failure(self, search_text: str, error: Exception):
        """
        记录失败的批注

        Args:
            search_text: 搜索文本
            error: 异常对象
        """
        self.failed.append({
            'search': search_text,
            'error': str(error),
            'error_type': type(error).__name__,
            'traceback': traceback.format_exc(),
            'timestamp': datetime.now()
        })

    def log_warning(self, message: str, details: str = ""):
        """
        记录警告

        Args:
            message: 警告消息
            details: 详细信息(可选)
        """
        self.warnings.append({
            'message': message,
            'details': details,
            'timestamp': datetime.now()
        })

    def generate_summary(self) -> str:
        """
        生成执行摘要

        Returns:
            str: 格式化的摘要文本
        """
        duration = (datetime.now() - self.start_time).total_seconds()

        lines = []
        lines.append("=" * 60)
        lines.append("批注添加摘要")
        lines.append("=" * 60)
        lines.append(f"\n执行时间: {duration:.2f} 秒")
        lines.append(f"成功: {len(self.successful)} 个")
        lines.append(f"失败: {len(self.failed)} 个")
        lines.append(f"警告: {len(self.warnings)} 个")

        if self.failed:
            lines.append("\n失败详情:")
            lines.append("-" * 60)
            for i, fail in enumerate(self.failed, 1):
                lines.append(f"\n{i}. 搜索文本: {fail['search'][:50]}")
                lines.append(f"   错误类型: {fail['error_type']}")
                lines.append(f"   错误: {fail['error'][:100]}")

        if self.warnings:
            lines.append("\n警告:")
            lines.append("-" * 60)
            for i, warning in enumerate(self.warnings, 1):
                lines.append(f"{i}. {warning['message']}")
                if warning['details']:
                    lines.append(f"   详情: {warning['details'][:80]}")

        lines.append("\n" + "=" * 60)
        return '\n'.join(lines)

    def save_to_file(self, filepath: str):
        """
        保存详细日志到文件

        Args:
            filepath: 日志文件路径
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            # 写入摘要
            f.write(self.generate_summary())
            f.write("\n\n详细错误追踪:\n")
            f.write("=" * 60 + "\n\n")

            # 写入每个失败的详细信息
            for i, fail in enumerate(self.failed, 1):
                f.write(f"错误 #{i}:\n")
                f.write(f"搜索文本: {fail['search']}\n")
                f.write(f"时间: {fail['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"错误类型: {fail['error_type']}\n")
                f.write(f"错误信息:\n{fail['traceback']}\n")
                f.write("\n" + "-" * 60 + "\n\n")

            # 写入警告详情
            if self.warnings:
                f.write("\n警告详情:\n")
                f.write("=" * 60 + "\n\n")
                for i, warning in enumerate(self.warnings, 1):
                    f.write(f"警告 #{i}:\n")
                    f.write(f"时间: {warning['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"消息: {warning['message']}\n")
                    if warning['details']:
                        f.write(f"详情: {warning['details']}\n")
                    f.write("\n")

    def get_statistics(self) -> Dict:
        """
        获取统计信息

        Returns:
            dict: 包含 total, successful, failed, warnings 等统计
        """
        total = len(self.successful) + len(self.failed)
        success_rate = (len(self.successful) / total * 100) if total > 0 else 0

        return {
            'total': total,
            'successful': len(self.successful),
            'failed': len(self.failed),
            'warnings': len(self.warnings),
            'success_rate': success_rate,
            'duration_seconds': (datetime.now() - self.start_time).total_seconds()
        }


# ==================== 审核报告生成器 ====================

class ReviewReportGenerator:
    """
    审核报告生成器

    生成结构化的审核报告,包括:
    - 基本信息
    - 统计数据
    - 详细问题列表
    - 验证结果
    - 总体评价

    Example:
        >>> generator = ReviewReportGenerator()
        >>> generator.add_basic_info(contract="合同.docx", reviewer="张三")
        >>> generator.add_issue(type="文本一致性", level="高风险", ...)
        >>> generator.save("report.txt")
    """

    def __init__(self):
        """初始化报告生成器"""
        self.basic_info = {}
        self.issues = {
            'high': [],
            'medium': [],
            'low': []
        }
        self.statistics = {}
        self.verification = {}

    def add_basic_info(self, contract: str, reviewer: str, date: str = None):
        """
        添加基本信息

        Args:
            contract: 合同文档路径
            reviewer: 审核人
            date: 审核日期(默认为当前时间)
        """
        self.basic_info = {
            'contract': contract,
            'reviewer': reviewer,
            'date': date or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

    def add_issue(self, issue_type: str, level: str, location: str,
                  reason: str, suggestion: str, original_text: str = ""):
        """
        添加审核问题

        Args:
            issue_type: 问题类型
            level: 风险等级 (高风险/中风险/低风险)
            location: 所在位置
            reason: 风险原因
            suggestion: 修订建议
            original_text: 原文内容(可选)
        """
        issue = {
            'type': issue_type,
            'location': location,
            'reason': reason,
            'suggestion': suggestion,
            'original_text': original_text
        }

        # 根据风险等级分类
        level_key = level.replace('风险', '').replace(' ', '').lower()
        if '高' in level or level_key == 'high':
            self.issues['high'].append(issue)
        elif '中' in level or level_key == 'medium':
            self.issues['medium'].append(issue)
        else:
            self.issues['low'].append(issue)

    def add_statistics(self, total_comments: int, successful: int, failed: int):
        """
        添加统计数据

        Args:
            total_comments: 总批注数
            successful: 成功添加数
            failed: 失败数
        """
        self.statistics = {
            'total': total_comments,
            'successful': successful,
            'failed': failed,
            'success_rate': (successful / total_comments * 100) if total_comments > 0 else 0
        }

    def add_verification(self, total: int, found: int, missing: int):
        """
        添加验证结果

        Args:
            total: 批注总数
            found: 找到的引用数
            missing: 缺失的引用数
        """
        self.verification = {
            'total': total,
            'found': found,
            'missing': missing
        }

    def generate(self) -> str:
        """
        生成报告文本

        Returns:
            str: 完整的报告文本
        """
        lines = []

        # 标题
        lines.append("=" * 60)
        lines.append("合同审核报告")
        lines.append("=" * 60)
        lines.append("")

        # 基本信息
        lines.append("一、基本信息")
        lines.append("-" * 60)
        lines.append(f"合同文档: {self.basic_info.get('contract', 'N/A')}")
        lines.append(f"审核人: {self.basic_info.get('reviewer', 'N/A')}")
        lines.append(f"审核日期: {self.basic_info.get('date', 'N/A')}")
        lines.append("")

        # 统计数据
        if self.statistics:
            lines.append("二、统计数据")
            lines.append("-" * 60)
            lines.append(f"总批注数: {self.statistics['total']}")
            lines.append(f"成功添加: {self.statistics['successful']}")
            lines.append(f"添加失败: {self.statistics['failed']}")
            lines.append(f"成功率: {self.statistics['success_rate']:.1f}%")
            lines.append("")

        # 验证结果
        if self.verification:
            lines.append("三、验证结果")
            lines.append("-" * 60)
            lines.append(f"批注总数: {self.verification['total']}")
            lines.append(f"文档引用: {self.verification['found']}")
            lines.append(f"缺失引用: {self.verification['missing']}")
            lines.append("")

        # 问题列表(按风险等级分组)
        all_issues = []
        if self.issues['high']:
            all_issues.extend([(i, '🔴 高风险') for i in self.issues['high']])
        if self.issues['medium']:
            all_issues.extend([(i, '🟡 中风险') for i in self.issues['medium']])
        if self.issues['low']:
            all_issues.extend([(i, '🔵 低风险') for i in self.issues['low']])

        if all_issues:
            lines.append("四、审核问题列表")
            lines.append("-" * 60)
            lines.append("")

            for idx, (issue, risk_label) in enumerate(all_issues, 1):
                lines.append(f"{idx}. 【问题类型】{issue['type']}")
                lines.append(f"   【风险等级】{risk_label}")
                lines.append(f"   【所在位置】{issue['location']}")
                lines.append(f"   【风险原因】{issue['reason']}")
                lines.append(f"   【修订建议】{issue['suggestion']}")
                if issue.get('original_text'):
                    lines.append(f"   【原文内容】{issue['original_text'][:80]}...")
                lines.append("")

        # 总体评价
        lines.append("=" * 60)
        lines.append("总体评价")
        lines.append("=" * 60)
        high_count = len(self.issues['high'])
        medium_count = len(self.issues['medium'])
        low_count = len(self.issues['low'])

        if high_count > 0:
            lines.append(f"\n发现 {high_count} 个高风险问题,建议优先修改。")
        if medium_count > 0:
            lines.append(f"发现 {medium_count} 个中风险问题,建议仔细评估。")
        if low_count > 0:
            lines.append(f"发现 {low_count} 个低风险问题,可在有时间时优化。")

        if high_count == 0 and medium_count == 0:
            lines.append("\n✓ 合同质量良好,仅发现少量低风险问题。")

        lines.append("")
        lines.append("=" * 60)

        return '\n'.join(lines)

    def save(self, filepath: str):
        """
        保存报告到文件

        Args:
            filepath: 报告文件路径
        """
        report_text = self.generate()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report_text)


# ==================== 使用示例 ====================

if __name__ == "__main__":
    print("错误处理和用户反馈工具")
    print("=" * 60)
    print()
    print("功能模块:")
    print("1. 自定义异常类: ReviewError, CommentNotFoundError 等")
    print("2. 版本检查: check_python_version()")
    print("3. 错误格式化: format_error_summary()")
    print("4. 批注日志: CommentBatchLogger")
    print("5. 报告生成: ReviewReportGenerator")
    print()
    print("使用示例:")
    print()
    print("from scripts.error_handling import CommentBatchLogger")
    print()
    print("logger = CommentBatchLogger()")
    print("logger.log_success(1, '合同总价', '金额不一致')")
    print("logger.log_failure('培训时间', Exception('未找到'))")
    print("print(logger.generate_summary())")
    print("logger.save_to_file('review_log.txt')")
