# 威科先行 API 整合指南

## 概述

本文档说明 `legal-issue-research` skill 如何集成威科先行数据库，实现**自动化配置与调用**。

**核心设计**：
- 用户只需回答"有/没有威科 API"，AI 自动完成剩余所有步骤
- 配置写入、关键词提取、API 调用全程自动化
- 用户无需修改任何代码，无需理解 Python

---

## 一、工作流程

```
用户提问
    ↓
第0步：身份识别
    ↓
第一阶段：信息确认（争议类型、事实、地域等）
    ↓
第二阶段：事实总结与确认
    ↓
【新】威科先行 API 确认（AI 主动询问）
    ↓
第三阶段：法律检索（公开渠道 + 威科自动合并）
    ↓
输出完整报告
```

### 威科 API 确认流程（放大）

```
事实确认完成
    ↓
AI 询问："您是否拥有威科先行 API？"
    ↓
用户回答："有" 或 "没有"
    ↓
┌─────────────────┬─────────────────┐
│  用户回答"有"   │ 用户回答"没有"  │
└────────┬────────┴────────┬────────┘
         ↓                  ↓
┌────────────────┐    ┌────────────────┐
│ AI 询问 API    │    │ 仅用公开渠道   │
│ 四项信息       │    │ 检索，继续     │
└────────┬───────┘    └────────────────┘
         ↓
┌────────────────┐
│ AI 自动写入   │
│ config.json   │
└────────┬───────┘
         ↓
┌────────────────┐
│ AI 自动调用   │
│ 威科检索      │
└────────┬───────┘
         ↓
┌────────────────┐
│ 结果合并到    │
│ 公开检索报告  │
└────────────────┘
```

---

## 二、文件清单

上传到 GitHub 的文件：

| 文件 | 用途 |
|---|---|
| `SKILL.md` | 主 skill 文件（已整合完整威科流程） |
| `wolters_auto.py` | 懒人检索接口（自动读取 config.json） |
| `wolters_wrapper.py` | 自动调用包装器（skill 内部调用） |
| `config.json.example` | 配置文件模板 |
| `wolters_API_GUIDE.md` | 本文档（合并后的完整指南） |

---

## 三、模块架构

```
用户 config.json 配置文件
        ↓
┌─────────────────────────────┐
│      wolters_auto.py        │  ← 懒人接口（主接口）
│  自动读取 config.json       │
│  无需修改代码               │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│     wolters_wrapper.py      │  ← skill 自动调用
│  skill 流程自动触发         │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│  wolterskluwer_searcher.py  │  ← 完整功能（需手动配置）
│  完整但复杂的接口            │
│  供高级用户参考             │
└─────────────────────────────┘
```

### 核心文件说明

| 文件 | 用途 | 用户操作 |
|---|---|---|
| `config.json.example` | 配置模板 | 复制为 `config.json` 填入凭证 |
| `wolters_auto.py` | **懒人接口** | 无需修改，skill 自动调用 |
| `wolters_wrapper.py` | 包装器 | 无需修改，skill 自动调用 |
| `wolterskluwer_searcher.py` | 完整模块 | 可选上传，供高级用户参考 |

---

## 四、自动化流程详解

### 4.1 AI 主动询问

在事实确认完成后，AI 会主动询问：

```
现在进入法律检索阶段。在开始之前，请问您是否拥有威科先行数据库的 API 权限？

- 有（我帮您配置并自动调用威科补充检索）
- 没有（仅使用公开渠道检索）
```

### 4.2 用户回答"有"

AI 依次询问：

```css
请提供威科先行 API 的以下信息（我帮您自动配置）：

1. API 端点地址（API_BASE_URL）
   - 威科提供的 API 接入地址，如 https://api.wkinfo.com.cn/v1

2. API Key（API_KEY）
   - 您的 API 密钥

3. API Secret（API_SECRET）
   - 您的 API 密钥（可选）

4. 认证方式（AUTH_TYPE）
   - Bearer / API-Key（默认 Bearer）
```

### 4.3 AI 自动配置

收到信息后，AI 自动：

1. **生成 config.json**
2. **写入 skill 根目录**
3. **验证写入成功**
4. **用已确认的检索关键词调用威科 API**

### 4.4 关键词自动提取

AI 从已确认的事实总结中提取关键词：

| 事实总结 | 提取的关键词 |
|---|---|
| 违法解除劳动合同，索赔2N赔偿金 | 违法解除劳动合同赔偿金 |
| 公司拖欠三个月工资，员工维权 | 拖欠工资 劳动报酬 |
| 工伤后公司拒绝赔偿 | 工伤保险待遇 赔偿责任 |
| 购房合同违约，定金不退 | 商品房买卖合同 定金 违约 |

---

## 五、关键保证

### 5.1 配置失败不影响主流程

- config.json 写入失败 → 告知用户，但继续公开检索
- API 调用失败 → 返回 `available=False`，继续公开检索
- 用户可随时说"重新配置威科 API"重新来过

### 5.2 静默失败，不中断用户

如果威科调用失败，AI 会继续用公开渠道，不告诉用户威科失败了（除非用户主动问）。

### 5.3 用户可随时重新配置

用户说"重新配置威科 API"，AI 会重新走配置流程更新 config.json。

---

## 六、接口说明

### WoltersAuto（wolters_auto.py）

```python
from wolters_auto import WoltersAuto

# 检查是否配置
print(WoltersAuto.is_configured())  # True 表示已配置

# 执行检索
result = WoltersAuto.search(
    keyword="违法解除劳动合同赔偿金",
    search_type="all",       # law/case/judgment/interpretation/guidance/all
    region="全国",
    date_from="2020-01-01",
    date_to="2024-12-31",
    page=1,
    page_size=20
)
```

**返回字段**：

| 字段 | 说明 |
|---|---|
| `success` | 是否成功 |
| `source` | "威科先行" |
| `keyword` | 检索关键词 |
| `total` | 总结果数 |
| `laws` | 法规列表 |
| `cases` | 案例列表 |
| `judgments` | 裁判文书列表 |
| `interpretations` | 司法解释列表 |
| `guidance_cases` | 指导性案例列表 |
| `error` | 错误信息（如有） |

**便捷方法**：

```python
# 只检索法规
result = WoltersAuto.search_laws("劳动合同法")

# 只检索案例
result = WoltersAuto.search_cases("违法解除劳动合同")

# 只检索指导性案例
result = WoltersAuto.search_guidance("劳动争议")
```

### wolters_wrapper（wolters_wrapper.py）

供 skill 流程自动调用的包装器：

```python
from wolters_wrapper import wolters_auto_search, is_available

# 检查是否可用
if is_available():
    print("威科 API 已配置")

# 检索（skill 流程自动调用）
result = wolters_auto_search(
    legal_issue="违法解除劳动合同赔偿金",
    legal_type="labor",
    region="全国",
    date_range={"from": "2020-01-01", "to": "2024-12-31"}
)
```

---

## 七、配置步骤（用户操作）

### 第一步：获取威科先行 API 权限

1. 联系威科先行销售申请机构用户 API 权限
2. 获取以下信息：
   - API 端点地址（Base URL）
   - API Key
   - API Secret（如需要）
   - 认证方式（Bearer / API-Key）

### 第二步：创建配置文件

在 skill 根目录创建 `config.json` 文件：

```json
{
    "API_BASE_URL": "https://api.wkinfo.com.cn/v1",
    "API_KEY": "你的API_KEY",
    "API_SECRET": "你的API_SECRET（可选）",
    "AUTH_TYPE": "Bearer"
}
```

### 第三步：验证配置

配置完成后，skill 自动检测到 `config.json` 并在检索时自动调用威科 API。

---

## 八、故障排查

| 现象 | 原因 | 解决方法 |
|---|---|---|
| `is_configured()` 返回 `False` | `config.json` 不存在或格式错误 | 检查文件是否在 skill 根目录，JSON 是否有效 |
| `success` 返回 `False` | API Key 错误或权限不足 | 检查 API_KEY 是否正确，联系威科确认权限 |
| `401 Unauthorized` | 认证失败 | 检查 AUTH_TYPE 是否与威科要求一致 |
| `429 Rate Limited` | 请求过于频繁 | 降低请求频率 |
| `Timeout` | 网络超时 | 检查网络连接 |

---

## 九、用户操作总结

| 步骤 | 用户操作 | AI 自动完成 |
|---|---|---|
| 1 | 描述法律问题 | 记录并提问确认 |
| 2 | 回答事实确认 | 总结并提取关键词 |
| 3 | 回答"有威科 API" | 询问四项信息 |
| 4 | 提供 API 信息 | 写入 config.json |
| 5 | 无需任何操作 | 自动调用并合并结果 |

**用户需要做的：回答问题 + 提供 API 凭证**，其余全部自动完成。

---

## 十、完整文件列表

```
legal-issue-research/
├── SKILL.md                       ← 主 skill 文件（已整合威科）
├── wolters_auto.py                ← 懒人接口（自动读取 config.json）✅
├── wolters_wrapper.py             ← 自动调用包装器（skill 自动调用）✅
├── wolterskluwer_searcher.py      ← 完整功能模块（需手动配置）
├── config.json.example            ← 配置文件模板 ✅
└── wolters_API_GUIDE.md           ← 本文档（合并后的完整指南）
```

标注 ✅ 的文件为让用户能够"配置即用"的核心文件。
