# 极简清新风 - 简历样式配置

> 适用场景：注重简洁的岗位/通用求职
> 风格特点：清爽、简洁、易读

---

## 配置参数

```yaml
style_name: minimal-clean
display_name: 极简清新风
description: 绿色与米白的清新搭配，展现简洁自然的职业形象

colors:
  # 主色系 - 绿色
  primary:
    main: "#66BB6A"       # 清新绿
    dark: "#43A047"       # 深绿色
    light: "#C8E6C9"      # 浅绿色

  # 辅色系 - 棕色
  secondary:
    main: "#795548"       # 深棕
    light: "#A1887F"      # 浅棕

  # 中性色
  neutral:
    dark: "#263238"       # 深灰/正文色
    medium: "#546E7A"     # 中灰/次要文字
    light: "#90A4AE"      # 浅灰/辅助文字
    white: "#FFFFFF"      # 白色
    bg_light: "#FAFAFA"   # 浅灰背景
    bg_cream: "#FFF8E1"   # 米色背景
    bg_border: "#E0E0E0"  # 边框灰色

  # 点缀色
  accent:
    green: "#66BB6A"      # 绿色点缀
    teal: "#26A69A"       # 青色点缀
    lime: "#AED581"       # 黄绿色点缀

fonts:
  # 字体方案（优先级从高到低）
  family:
    - "PingFang SC"       # 苹方
    - "Microsoft YaHei"   # 微软雅黑
    - "system-ui"         # 系统字体
    - "sans-serif"        # 回退到无衬线字体

  # 字号规范
  sizes:
    name: 22pt           # 姓名字号
    title: 13pt          # 职位字号
    contact: 9pt         # 联系方式字号
    section: 12pt        # 章节标题字号
    body: 10pt           # 正文字号
    body_large: 11pt     # 正文大字号
    small: 8pt           # 小字号（技能标签）
    small_medium: 9pt    # 中小字号

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
    margin_top: 5mm
    margin_bottom: 5mm
    margin_left: 5mm
    margin_right: 5mm

  # 头部设置
  header:
    padding_vertical: 4mm
    padding_horizontal: 6mm
    gap: 4mm
    photo_width: 32mm
    photo_height: 42mm

  # 侧边栏设置
  sidebar:
    width: 40mm          # 侧边栏宽度
    gap: 3mm

  # 主内容区
  main:
    padding: 5mm 6mm

  # 间距规范
  spacing:
    section: 3mm         # 章节间距
    item: 2mm            # 列表项间距
    paragraph: 1.7       # 段落行高

# 渐变效果
gradients:
  primary: "linear-gradient(135deg, #66BB6A 0%, #43A047 100%)"
  secondary: "linear-gradient(135deg, #795548 0%, #A1887F 100%)"
  light: "linear-gradient(135deg, #FFF8E1 0%, #FFFFFF 100%)"

# 特效
effects:
  shadow: "0 1px 6px rgba(0,0,0,0.06)"
  card_shadow: "none"     # 极简风格不使用阴影
  border: "1px solid #E0E0E0"
```

---

## CSS 实现

```css
/* 极简清新风 - 核心样式 */

/* 重置 - 极简风格 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* 页面背景 */
body {
    background: #FAFAFA;
}

/* 头部 */
.header {
    background: #FFFFFF;
    padding: 4mm 6mm;
    border-bottom: 1px solid #E0E0E0;
    display: flex;
    gap: 4mm;
    align-items: center;
}

.header-name {
    font-size: 22pt;
    font-weight: 700;
    color: #263238;
}

.header-title {
    font-size: 13pt;
    color: #66BB6A;
    font-weight: 500;
}

.header-contact {
    font-size: 9pt;
    color: #546E7A;
}

.header-contact-item {
    display: inline-block;
    margin-right: 4mm;
}

/* 章节标题 */
.section-title {
    font-size: 12pt;
    font-weight: 700;
    color: #263238;
    margin-bottom: 3mm;
    padding-bottom: 1mm;
    border-bottom: 1px solid #E0E0E0;
}

.section-title::before {
    content: "";
    display: inline-block;
    width: 3mm;
    height: 3mm;
    background: #66BB6A;
    margin-right: 2mm;
    border-radius: 50%;
}

/* 正文 */
.body-text {
    font-size: 10pt;
    color: #263238;
    line-height: 1.7;
}

/* 时间线 */
.timeline-item {
    margin-bottom: 2mm;
}

.timeline-date {
    font-size: 9pt;
    color: #90A4AE;
    font-weight: 500;
}

.timeline-title {
    font-weight: 600;
    color: #263238;
}

/* 技能标签 */
.skill-tag {
    display: inline-block;
    padding: 1mm 2.5mm;
    margin: 1mm;
    background: #C8E6C9;
    color: #43A047;
    font-size: 8pt;
    border-radius: 2mm;
    font-weight: 500;
}

/* 核心竞争力卡片 */
.competency-card {
    background: #FFFFFF;
    padding: 2.5mm;
    margin: 2mm 0;
    border: 1px solid #E0E0E0;
    border-radius: 1mm;
    border-left: 3px solid #66BB6A;
}

.competency-title {
    font-weight: 600;
    color: #43A047;
    margin-bottom: 1mm;
}

/* 侧边栏 */
.sidebar {
    background: #FFFFFF;
    padding: 4mm;
    border-right: 1px solid #E0E0E0;
}

.sidebar-section {
    margin-bottom: 4mm;
}

.sidebar-title {
    font-size: 10pt;
    font-weight: 700;
    color: #263238;
    margin-bottom: 2mm;
}

/* 列表 */
.bullet-list li {
    margin-bottom: 1mm;
    padding-left: 3mm;
    position: relative;
}

.bullet-list li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #66BB6A;
}
```

---

## 视觉效果预览

```
┌─────────────────────────────────────────────────────────────┐
│ ┌────┐  张三                    法务经理                     │
│ │    │  zhangsan@example.com | 138****1234 | 北京市朝阳区  │
│ │照片│  28岁 | 硕士研究生                                │
│ │    │                                                  │
│ └────┘                                                  │
├─────────────────────────────────────────────────────────────┤
│ ┌──────────┬─────────────────────────────────────────────┐ │
│ │ 教育背景  │  职业目标                                  │ │
│ │          │  • 5年法务工作经验，希望在...              │ │
│ │ • 2018-  │                                             │ │
│ │   XX大学 │  工作经历                                  │ │
│ │   硕士   │  • 2021-至今  XX科技有限公司  法务主管      │ │
│ │   民商法 │    – 负责公司合同管理...                   │ │
│ │          │    – 建立知识产权保护体系...               │ │
│ │ • 2014-  │  • 2019-2021  XX律师事务所  律师助理        │ │
│ │   XX大学 │    – 协助处理民商事案件...                 │ │
│ │   本科   │    – 参与重大项目尽职调查...              │ │
│ │   法学   │                                             │ │
│ │          │  核心竞争力                                │ │
│ │ 核心技能  │  ┌──────────┐ ┌──────────┐               │ │
│ │ • 合同审查│  │合同管理  │ │知识产权   │               │ │
│ │ • 诉讼实务│  └──────────┘ └──────────┘               │ │
│ │ • 知识产权│  ┌──────────┐ ┌──────────┐               │ │
│ │ • 合规体系│  │风险控制  │ │合规体系   │               │ │
│ │          │  └──────────┘ └──────────┘               │ │
│ │ 资格证书  │                                             │ │
│ │ • 法律职业│  自我评价                                  │ │
│ │   证书   │  工作细致认真，责任心强，具备良好的...      │ │
│ │ • 英语六级│                                             │ │
│ └──────────┴─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 适用场景

- 通用法务岗位求职
- 注重可读性的场景
- 传统行业向现代化转型的企业
- 需要展现稳重与亲和力的场景

---

## 色彩心理学

- **清新绿**：象征成长、希望、活力
- **米白色**：象征自然、温和、舒适
- **浅灰色**：象征平衡、专业

这套配色方案传递的核心信息：**专业、亲和、可靠**
