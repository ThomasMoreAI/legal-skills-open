# 自定义简历样式指南

> 完全可配置的简历样式系统
> 用户可以自定义配色、字体、布局等所有视觉元素

---

## 配置结构

简历样式配置采用 YAML 格式，包含以下部分：

```yaml
# 基本信息
style_name: custom-style
display_name: 自定义样式
description: 样式描述

# 配色方案
colors:
  primary: { ... }
  secondary: { ... }
  neutral: { ... }
  accent: { ... }

# 字体配置
fonts:
  family: [ ... ]
  sizes: { ... }
  weights: { ... }

# 布局配置
layout:
  page: { ... }
  header: { ... }
  sidebar: { ... }
  main: { ... }
  spacing: { ... }

# 渐变与特效
gradients: { ... }
effects: { ... }
```

---

## 配色方案

### 色彩体系

```yaml
colors:
  # 主色系 - 用于强调、重要元素
  primary:
    main: "#HEX"         # 主色
    dark: "#HEX"         # 深色变体
    light: "#HEX"        # 浅色变体

  # 辅色系 - 用于次要元素、装饰
  secondary:
    main: "#HEX"
    light: "#HEX"

  # 中性色 - 用于文字、背景
  neutral:
    dark: "#HEX"         # 正文文字
    medium: "#HEX"       # 次要文字
    light: "#HEX"        # 辅助文字
    white: "#HEX"        # 白色
    bg_light: "#HEX"     # 浅色背景
    bg_dark: "#HEX"      # 深色背景（可选）
    bg_border: "#HEX"    # 边框颜色

  # 强调色 - 用于特殊突出（可选）
  accent:
    color1: "#HEX"
    color2: "#HEX"
    color3: "#HEX"
```

### 色彩搭配建议

| 风格 | 主色 | 辅色 | 适用场景 |
|------|------|------|----------|
| 商务专业 | 深蓝/金色 | 灰色系 | 法务、金融、传统行业 |
| 科技现代 | 科技蓝/紫色 | 浅灰 | 互联网、科技公司 |
| 清新简约 | 绿色/青色 | 米白 | 初创企业、文化行业 |
| 温暖亲和 | 橙色/暖黄 | 浅棕 | 教育、服务行业 |
| 创意活力 | 红色/粉色 | 白色 | 设计、创意行业 |

---

## 字体配置

### 字体方案

```yaml
fonts:
  # 字体族（优先级从高到低）
  family:
    - "字体1"           # 首选字体
    - "字体2"           # 备选字体
    - "字体3"           # 备选字体
    - "generic-family"  # 通用字体族

  # 常见中文字体
  # 衬线字体：
  #   - 仿宋 / FangSong / STFangsong
  #   - 宋体 / SimSun / STSong
  #   - serif (通用)
  #
  # 无衬线字体：
  #   - 微软雅黑 / Microsoft YaHei
  #   - 苹方 / PingFang SC
  #   - 思源黑体 / Source Han Sans
  #   - system-ui (系统字体)
  #   - sans-serif (通用)
```

### 字号规范

```yaml
fonts:
  sizes:
    name: 24pt          # 姓名字号（建议 20-28pt）
    title: 13pt         # 职位字号（建议 12-15pt）
    contact: 9pt        # 联系方式字号（建议 8-10pt）
    section: 12pt       # 章节标题字号（建议 11-14pt）
    body: 10pt          # 正文字号（建议 9-11pt）
    body_large: 11pt    # 正文大字号
    small: 8pt          # 小字号（建议 7-9pt）
    small_medium: 9pt   # 中小字号
```

### 字重

```yaml
fonts:
  weights:
    light: 300          # 细体（可选）
    normal: 400         # 常规
    medium: 500         # 中等（可选）
    bold: 700           # 粗体
```

---

## 布局配置

### 页面设置

```yaml
layout:
  page:
    width: 210mm        # A4 宽度（固定）
    height: 297mm       # A4 高度（固定）
    margin_top: 4mm     # 顶部装饰条高度（可选）
    margin_bottom: 2mm  # 底部装饰条高度（可选）
```

### 头部设置

```yaml
layout:
  header:
    padding_vertical: 5mm    # 头部上下内边距
    padding_horizontal: 8mm  # 头部左右内边距
    gap: 6mm                 # 元素间距
    photo_width: 34mm        # 照片宽度
    photo_height: 44mm       # 照片高度
```

### 侧边栏设置

```yaml
layout:
  sidebar:
    width: 42mm        # 侧边栏宽度（建议 35-50mm）
    gap: 6mm           # 侧边栏内元素间距
```

### 主内容区

```yaml
layout:
  main:
    padding: 8mm       # 主内容区内边距
```

### 间距规范

```yaml
layout:
  spacing:
    section: 2.5mm     # 章节间距（建议 2-4mm）
    item: 2.5mm        # 列表项间距（建议 2-3mm）
    paragraph: 1.5     # 段落行高（建议 1.4-1.8）
```

---

## 渐变与特效

### 渐变配置

```yaml
gradients:
  primary: "linear-gradient(135deg, #PRIMARY_MAIN 0%, #PRIMARY_DARK 100%)"
  secondary: "linear-gradient(135deg, #SECONDARY_MAIN 0%, #SECONDARY_LIGHT 100%)"
  light: "linear-gradient(135deg, #LIGHT_COLOR 0%, #FFFFFF 100%)"

# 其他渐变方向（可选）
# radial-gradient: 径向渐变
# linear-gradient(90deg, ...): 水平渐变
# linear-gradient(180deg, ...): 垂直渐变
```

### 特效配置

```yaml
effects:
  shadow: "0 2px 8px rgba(0,0,0,0.1)"           # 卡片阴影
  card_shadow: "0 2px 4px rgba(0,0,0,0.08)"     # 小卡片阴影
  hover_shadow: "..."                           # 悬停阴影（网页版）
  border: "1px solid #BORDER_COLOR"            # 边框样式
```

---

## 完整配置示例

### 示例1：深色专业风

```yaml
style_name: dark-professional
display_name: 深色专业风
description: 深色背景的专业简历样式

colors:
  primary:
    main: "#E0E0E0"
    dark: "#BDBDBD"
    light: "#F5F5F5"
  secondary:
    main: "#424242"
    light: "#616161"
  neutral:
    dark: "#FFFFFF"      # 深色背景用白色文字
    medium: "#E0E0E0"
    light: "#BDBDBD"
    white: "#FFFFFF"
    bg_light: "#212121"
    bg_dark: "#121212"
    bg_border: "#424242"

fonts:
  family:
    - "Microsoft YaHei"
    - "sans-serif"
  sizes:
    name: 24pt
    title: 13pt
    contact: 9pt
    section: 12pt
    body: 10pt
    body_large: 11pt
    small: 8pt
    small_medium: 9pt
  weights:
    normal: 400
    bold: 700

layout:
  page:
    width: 210mm
    height: 297mm
  header:
    padding_vertical: 6mm
    padding_horizontal: 8mm
    gap: 4mm
  sidebar:
    width: 45mm
  main:
    padding: 6mm 8mm
  spacing:
    section: 3mm
    item: 2mm
    paragraph: 1.6

gradients:
  primary: "linear-gradient(135deg, #E0E0E0 0%, #BDBDBD 100%)"
  secondary: "linear-gradient(135deg, #424242 0%, #616161 100%)"

effects:
  shadow: "0 2px 8px rgba(0,0,0,0.3)"
  card_shadow: "0 2px 4px rgba(0,0,0,0.2)"
  border: "1px solid #424242"
```

### 示例2：创意活力风

```yaml
style_name: creative-vibrant
display_name: 创意活力风
description: 充满活力的创意简历样式

colors:
  primary:
    main: "#FF5722"      # 活力橙
    dark: "#E64A19"
    light: "#FFCCBC"
  secondary:
    main: "#9C27B0"      # 紫色
    light: "#BA68C8"
  neutral:
    dark: "#212121"
    medium: "#616161"
    light: "#9E9E9E"
    white: "#FFFFFF"
    bg_light: "#FAFAFA"
    bg_border: "#E0E0E0"
  accent:
    teal: "#009688"
    yellow: "#FFEB3B"

fonts:
  family:
    - "PingFang SC"
    - "system-ui"
  sizes:
    name: 26pt
    title: 14pt
    contact: 10pt
    section: 13pt
    body: 10pt
    body_large: 11pt
    small: 9pt
    small_medium: 10pt
  weights:
    normal: 400
    bold: 700

layout:
  page:
    width: 210mm
    height: 297mm
  header:
    padding_vertical: 5mm
    padding_horizontal: 8mm
    gap: 6mm
  sidebar:
    width: 40mm
  main:
    padding: 6mm 8mm
  spacing:
    section: 3mm
    item: 2.5mm
    paragraph: 1.7

gradients:
  primary: "linear-gradient(135deg, #FF5722 0%, #E64A19 100%)"
  secondary: "linear-gradient(135deg, #9C27B0 0%, #BA68C8 100%)"

effects:
  shadow: "0 3px 10px rgba(255,87,34,0.2)"
  card_shadow: "0 2px 6px rgba(156,39,176,0.15)"
```

---

## 使用方法

1. **复制模板**：选择最接近需求的预设样式作为起点
2. **修改配置**：根据需要调整配色、字体、布局
3. **保存配置**：将配置保存为 YAML 文件
4. **应用样式**：在生成简历时指定配置文件

### 提示词示例

```
请使用以下自定义样式配置生成我的简历：

[粘贴 YAML 配置]

我的简历信息如下：
[粘贴简历信息]
```
