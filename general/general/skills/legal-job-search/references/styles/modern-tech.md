# 现代科技风 - 简历样式配置

> 适用场景：科技公司/互联网岗位求职
> 风格特点：简洁、现代、科技感

---

## 配置参数

```yaml
style_name: modern-tech
display_name: 现代科技风
description: 蓝色与灰白的现代搭配，展现简洁专业的科技形象

colors:
  # 主色系 - 蓝色
  primary:
    main: "#2196F3"       # 科技蓝
    dark: "#1976D2"       # 深蓝色
    light: "#BBDEFB"      # 浅蓝色

  # 辅色系 - 灰色
  secondary:
    main: "#455A64"       # 深灰
    light: "#78909C"      # 中灰

  # 中性色
  neutral:
    dark: "#212121"       # 深黑/正文色
    medium: "#616161"     # 中灰/次要文字
    light: "#9E9E9E"      # 浅灰/辅助文字
    white: "#FFFFFF"      # 白色
    bg_light: "#FAFAFA"   # 浅灰背景
    bg_medium: "#F5F5F5"  # 中灰背景
    bg_border: "#E0E0E0"  # 边框灰色

  # 强调色
  accent:
    blue: "#2196F3"       # 蓝色强调
    green: "#4CAF50"      # 绿色强调
    orange: "#FF9800"     # 橙色强调

fonts:
  # 字体方案（优先级从高到低）
  family:
    - "Microsoft YaHei"   # 微软雅黑
    - "PingFang SC"       # 苹方
    - "system-ui"         # 系统字体
    - "sans-serif"        # 回退到无衬线字体

  # 字号规范
  sizes:
    name: 24pt           # 姓名字号
    title: 14pt          # 职位字号
    contact: 10pt        # 联系方式字号
    section: 13pt        # 章节标题字号
    body: 10pt           # 正文字号
    body_large: 11pt     # 正文大字号
    small: 9pt           # 小字号（技能标签）
    small_medium: 10pt   # 中小字号

  # 字重
  weights:
    light: 300
    normal: 400
    medium: 500
    bold: 700

layout:
  # 页面设置
  page:
    width: 210mm         # A4 宽度
    height: 297mm        # A4 高度
    margin_top: 0mm
    margin_bottom: 0mm

  # 头部设置
  header:
    padding_vertical: 6mm
    padding_horizontal: 8mm
    gap: 4mm
    photo_width: 36mm
    photo_height: 46mm

  # 侧边栏设置
  sidebar:
    width: 45mm          # 侧边栏宽度
    gap: 4mm

  # 主内容区
  main:
    padding: 6mm 8mm

  # 间距规范
  spacing:
    section: 3mm         # 章节间距
    item: 2mm            # 列表项间距
    paragraph: 1.6       # 段落行高

# 渐变效果
gradients:
  primary: "linear-gradient(135deg, #2196F3 0%, #1976D2 100%)"
  secondary: "linear-gradient(135deg, #455A64 0%, #78909C 100%)"
  light: "linear-gradient(135deg, #F5F5F5 0%, #FFFFFF 100%)"

# 特效
effects:
  shadow: "0 2px 12px rgba(0,0,0,0.08)"
  card_shadow: "0 2px 6px rgba(0,0,0,0.04)"
  hover_shadow: "0 4px 16px rgba(33,150,243,0.15)"
```

---

## CSS 实现

```css
/* 现代科技风 - 核心样式 */

/* 重置 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* 头部 */
.header {
    background: #FAFAFA;
    padding: 6mm 8mm;
    border-bottom: 1px solid #E0E0E0;
    display: flex;
    gap: 4mm;
    align-items: center;
}

.header-name {
    font-size: 24pt;
    font-weight: 700;
    color: #212121;
}

.header-title {
    font-size: 14pt;
    color: #2196F3;
    font-weight: 500;
}

.header-contact {
    font-size: 10pt;
    color: #616161;
}

.header-contact-item {
    display: inline-flex;
    align-items: center;
    gap: 2mm;
    margin-right: 4mm;
}

/* 章节标题 */
.section-title {
    font-size: 13pt;
    font-weight: 700;
    color: #212121;
    margin-bottom: 3mm;
    padding-bottom: 1mm;
    border-bottom: 2px solid #2196F3;
}

/* 正文 */
.body-text {
    font-size: 10pt;
    color: #212121;
    line-height: 1.6;
}

/* 时间线 */
.timeline-item {
    margin-bottom: 2mm;
    padding-left: 4mm;
    border-left: 2px solid #E0E0E0;
}

.timeline-date {
    font-size: 9pt;
    color: #757575;
    font-weight: 500;
}

/* 技能标签 */
.skill-tag {
    display: inline-block;
    padding: 1.5mm 3mm;
    margin: 1mm;
    background: #E3F2FD;
    color: #1976D2;
    font-size: 9pt;
    border-radius: 3mm;
    font-weight: 500;
}

.skill-tag.high-level {
    background: #2196F3;
    color: #FFFFFF;
}

/* 核心竞争力卡片 */
.competency-card {
    background: #FFFFFF;
    padding: 3mm;
    margin: 2mm 0;
    border-radius: 1mm;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    border-left: 3px solid #2196F3;
}

.competency-title {
    font-weight: 600;
    color: #1976D2;
    margin-bottom: 1mm;
}

/* 侧边栏 */
.sidebar {
    background: #F5F5F5;
    padding: 4mm;
}

.sidebar-section {
    margin-bottom: 4mm;
}

.sidebar-title {
    font-size: 11pt;
    font-weight: 700;
    color: #212121;
    margin-bottom: 2mm;
}

/* 联系方式图标 */
.contact-icon {
    width: 3mm;
    height: 3mm;
    fill: #757575;
}
```

---

## 视觉效果预览

```
┌─────────────────────────────────────────────────────────────┐
│ ┌────┐  张三                    法务经理                     │
│ │    │  📧 zhangsan@example.com  │  📱 138****1234         │
│ │照片│  📍 北京市朝阳区           │  🎂 28岁                 │
│ │    │  🎓 硕士研究生                                     │
│ └────┘                                                  │
├─────────────────────────────────────────────────────────────┤
│ ┌──────────┬─────────────────────────────────────────────┐ │
│ │ 教育背景  │  职业目标                                  │ │
│ │          │  寻求在科技企业发挥法务专业能力...           │ │
│ │ ┌────┐   │                                             │ │
│ │ │2018│  │  工作经历                                  │ │
│ │ └────┘   │  ┌─────────────────────────────────────┐  │ │
│ │ XX大学   │  │ XX科技有限公司 | 法务主管 | 2021-至今│  │ │
│ │ 硕士     │  │ • 负责公司合同管理...              │  │ │
│ │ 民商法学 │  │ • 建立知识产权保护体系...          │  │ │
│ │          │  └─────────────────────────────────────┘  │ │
│ │ ┌────┐   │  ┌─────────────────────────────────────┐  │ │
│ │ │2014│  │  │ XX律师事务所 | 律师助理 | 2019-2021 │  │ │
│ │ └────┘   │  │ • 协助处理民商事案件...            │  │ │
│ │ XX大学   │  └─────────────────────────────────────┘  │ │
│ │ 本科     │                                             │ │
│ │ 法学     │  核心竞争力                                │ │
│ │          │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐   │ │
│ │ 核心技能  │  │合同  │ │诉讼  │ │知识产权│ │合规  │   │ │
│ │ [合同审查]│ │管理  │ │实务  │ │保护   │ │体系  │   │ │
│ │ [诉讼实务]│ └──────┘ └──────┘ └──────┘ └──────┘   │ │
│ │ [知识产权]│                                             │ │
│ │ [合规体系]│  自我评价                                  │ │
│ │          │  5年法务工作经验，擅长...                  │ │
│ │ 资格证书  │                                             │ │
│ │ 📜 法律职业│                                             │ │
│ │    证书   │                                             │ │
│ │ 📜 英语六级│                                             │ │
│ └──────────┴─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 适用场景

- 科技公司法务岗位求职
- 互联网企业法务岗位求职
- 需要展现现代感和专业性的场景
- 创新型企业、快速发展的公司

---

## 色彩心理学

- **科技蓝**：象征创新、理性、专业
- **灰色**：象征稳重、平衡、现代
- **白色**：象征简洁、清爽

这套配色方案传递的核心信息：**创新、专业、现代**
