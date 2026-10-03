# 商务精英风 - 简历样式配置

> 适用场景：法务/商务岗位求职
> 风格特点：稳重、专业、高端

---

## 配置参数

```yaml
style_name: business-elite
display_name: 商务精英风
description: 金色与深蓝色的经典搭配，展现稳重专业的商务形象

colors:
  # 主色系 - 金色
  primary:
    main: "#D4AF37"      # 主金色
    dark: "#C9A227"      # 深金色
    light: "#F7E7CE"     # 浅金色/米色

  # 辅色系 - 深蓝
  secondary:
    main: "#1C3F5E"      # 深蓝色
    light: "#2C5282"     # 中蓝色

  # 中性色
  neutral:
    dark: "#2C3E50"      # 深灰/正文色
    medium: "#5A6C7D"    # 中灰/次要文字
    light: "#7F8C8D"     # 浅灰/辅助文字
    white: "#FFFFFF"     # 白色
    bg_light: "#F8F9FA"  # 浅灰背景
    bg_border: "#E9ECEF" # 边框灰色

fonts:
  # 字体方案（优先级从高到低）
  family:
    - "仿宋"
    - "FangSong"
    - "STFangsong"
    - "serif"  # 回退到衬线字体

  # 字号规范
  sizes:
    name: 26pt           # 姓名字号
    title: 13pt          # 职位字号
    contact: 9pt         # 联系方式字号
    section: 12pt        # 章节标题字号
    body: 10pt           # 正文字号
    body_large: 11pt     # 正文大字号
    small: 8pt           # 小字号（技能标签）
    small_medium: 9pt    # 中小字号

  # 字重
  weights:
    normal: 400
    bold: 700

layout:
  # 页面设置
  page:
    width: 210mm         # A4 宽度
    height: 297mm        # A4 高度
    margin_top: 4mm      # 顶部装饰条高度
    margin_bottom: 2mm   # 底部装饰条高度

  # 头部设置
  header:
    padding_vertical: 5mm
    padding_horizontal: 8mm
    gap: 6mm
    photo_width: 34mm
    photo_height: 44mm

  # 侧边栏设置
  sidebar:
    width: 42mm          # 侧边栏宽度
    gap: 6mm

  # 主内容区
  main:
    padding: 8mm

  # 间距规范
  spacing:
    section: 2.5mm       # 章节间距
    item: 2.5mm          # 列表项间距
    paragraph: 1.5       # 段落行高

# 渐变效果
gradients:
  primary: "linear-gradient(135deg, #D4AF37 0%, #C9A227 100%)"
  secondary: "linear-gradient(135deg, #1C3F5E 0%, #2C5282 100%)"
  light: "linear-gradient(135deg, #F7E7CE 0%, #FFFFFF 100%)"

# 特效
effects:
  shadow: "0 2px 8px rgba(0,0,0,0.1)"
  card_shadow: "0 2px 4px rgba(0,0,0,0.08)"
```

---

## CSS 实现

```css
/* 商务精英风 - 核心样式 */

/* 顶部装饰条 */
.top-bar {
    height: 4mm;
    background: linear-gradient(135deg, #D4AF37 0%, #C9A227 100%);
}

/* 头部 */
.header {
    background: linear-gradient(135deg, #1C3F5E 0%, #2C5282 100%);
    color: #FFFFFF;
    padding: 5mm 8mm;
    display: flex;
    gap: 6mm;
    align-items: center;
}

.header-name {
    font-size: 26pt;
    font-weight: bold;
    color: #FFFFFF;
}

.header-title {
    font-size: 13pt;
    color: #D4AF37;
}

.header-contact {
    font-size: 9pt;
    color: rgba(255,255,255,0.85);
}

/* 章节标题 */
.section-title {
    font-size: 12pt;
    font-weight: bold;
    color: #1C3F5E;
    margin-bottom: 2mm;
    border-left: 3mm solid #D4AF37;
    padding-left: 2mm;
}

/* 正文 */
.body-text {
    font-size: 10pt;
    color: #2C3E50;
    line-height: 1.5;
}

/* 时间线 */
.timeline-item {
    margin-bottom: 2.5mm;
}

.timeline-date {
    font-size: 9pt;
    color: #5A6C7D;
}

/* 技能标签 */
.skill-tag {
    display: inline-block;
    padding: 1mm 2mm;
    margin: 1mm;
    background: linear-gradient(135deg, #1C3F5E 0%, #2C5282 100%);
    color: #FFFFFF;
    font-size: 8pt;
    border-radius: 2mm;
}

/* 核心竞争力卡片 */
.competency-card {
    background: linear-gradient(135deg, #F7E7CE 0%, #FFFFFF 100%);
    padding: 3mm;
    margin: 2mm 0;
    border-radius: 1mm;
    border-left: 2mm solid #D4AF37;
}

/* 底部装饰条 */
.bottom-bar {
    height: 2mm;
    background: #1C3F5E;
}
```

---

## 视觉效果预览

```
┌─────────────────────────────────────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ ← 金色渐变
├─────────────────────────────────────────────────────────────┤
│ ┌────┐  张三                    法务经理                     │
│ │    │  138****1234  |  zhangsan@example.com              │
│ │照片│  北京市朝阳区 |  28岁 | 硕士研究生                   │
│ │    │                                                  │
│ └────┘                                                  │
├─────────────────────────────────────────────────────────────┤
│ ┌──────────┬─────────────────────────────────────────────┐ │
│ │ 教育背景  │  职业目标                                  │ │
│ │          │  • 5年法务工作经验...                      │ │
│ │ XX大学   │                                             │ │
│ │ 硕士     │  工作经历                                  │ │
│ │ 2018-2021│  ┌─────────────────────────────────────┐  │ │
│ │          │  │ XX科技有限公司 | 法务主管 | 2021-至今│  │ │
│ │ XX大学   │  │ • 负责公司合同管理...              │  │ │
│ │ 本科     │  │ • 建立知识产权保护体系...          │  │ │
│ │ 2014-2018│  └─────────────────────────────────────┘  │ │
│ │          │                                             │ │
│ │ 核心技能  │  核心竞争力                                │ │
│ │ ┌────┐   │  ┌──────┐ ┌──────┐                       │ │
│ │ │合同│   │  │风险  │ │合规  │                       │ │
│ │ └────┘   │  │控制  │ │体系建设│                       │ │
│ │ ┌────┐   │  └──────┘ └──────┘                       │ │
│ │ │诉讼│   │                                             │ │
│ │ └────┘   │  自我评价                                  │ │
│ │          │  5年法务工作经验，精通...                  │ │
│ │ 资格证书  │                                             │ │
│ │ • 法律职业│                                             │ │
│ │   证书   │                                             │ │
│ └──────────┴─────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │ ← 深蓝色
└─────────────────────────────────────────────────────────────┘
```

---

## 适用场景

- 法务岗位求职
- 商务岗位求职
- 需要展现专业性和稳重的场景
- 传统行业、金融行业、大型企业

---

## 色彩心理学

- **金色**：象征品质、高端、成功
- **深蓝色**：象征信任、专业、稳重
- **米白色**：象征简洁、清爽

这套配色方案传递的核心信息：**专业、可靠、高端**
