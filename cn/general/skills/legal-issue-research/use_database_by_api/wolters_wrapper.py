# -*- coding: utf-8 -*-
"""
威科先行自动调用包装器
=======================
供 legal-issue-research skill 自动调用
无需用户手动操作，skill 流程自动触发

使用方式（skill 内部自动调用）：
    from wolters_wrapper import wolters_auto_search
    result = wolters_auto_search(legal_issue="...", region="...", date_range={...})
"""

from wolters_auto import WoltersAuto, auto_search

# 导出给 skill 用的便捷函数
wolters_auto_search = auto_search


def is_available() -> bool:
    """检查威科 API 是否已配置"""
    return WoltersAuto.is_configured()


def quick_search(keyword: str) -> dict:
    """
    快速检索（最简接口）

    Args:
        keyword: 检索关键词

    Returns:
        dict: 检索结果
    """
    return WoltersAuto.search(keyword)
