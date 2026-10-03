# Immigration — France

Immigration skills under the law of France.

Practice-area definition (`practices.json`, jurisdiction-agnostic): immigration law: visas and petitions (USCIS), status and residency, asylum, deportation/removal, work and residence permits (pobyt/Aufenthalt), consular procedures for foreign nationals.

Jurisdiction: `fr` · Practice: `immigration` · Skill language: en, zh

## Skills (42)

| Skill | What it does |
|---|---|
| [`Accommodation verify`](skills/accommodation-verify/) | 按法国申根签证要求审核住宿订单（酒店、AirBnB、青旅、住朋友家） — 覆盖每一晚、列出每位申请人、退订政策清楚、东道详情可核实。识别何时 需要 Attestation d'Accueil… |
| [`Accommodation verify`](skills/accommodation-verify-torlyai/) | Audits accommodation bookings (hotel, AirBnB, hostel, host-stay) for France Schengen visa requirements… |
| [`Appointment day`](skills/appointment-day/) | TLScontact 法国申根签证赴约日早晨的指引。简短的"出门前"理智核查 （5 项）、赴约期间做什么、回家后立刻做什么。比 /appointment-prep 刻意 更短… |
| [`Appointment prep`](skills/appointment-prep-torlyai/) | TLScontact 法国申根签证赴约前 24 小时清单。核实所有文件已打印（不能 仅屏幕看）、照片是实物打印（不是手机图）、付款卡在钱包、交通已规划 早 15 分钟到、用户已收拾合理的文件夹。在 TLS… |
| [`Audit application`](skills/audit-application/) | 提交前审核关卡。读取用户收集的所有文件、/start-here 的范围、 求情信，进行整体合规性+一致性检查。标注不一致（姓名、日期、 金额在不同文件间不匹配）、缺漏（必备文件缺失）、薄弱点… |
| [`Audit application`](skills/audit-application-torlyai/) | Pre-submission audit gate. Reads all the user's collected documents, the scope from /start-here, the… |
| [`Audit log`](skills/audit-log/) | vstack 工具集的会话内行动历史。显示当前 Claude Code 会话中跑过哪些 技能、做了哪些决定、还有什么未完成。用户休息回来问"我们到哪了"或 需要为家人小结时有用。严格内存中；无跨会话持久化（用… |
| [`Bank statement check`](skills/bank-statement-check-torlyai/) | 审查银行流水的申根签证申请充足性和格式。核实流水：(1) 覆盖最近 3 个月，(2) 显示申请人全名+地址，(3) 显示足够出行的余额， (4) 无红旗（申请前单笔大额存款、涂抹、刚开户的账户）。当用户说… |
| [`Book appointment`](skills/book-appointment/) | 在用户拿到 France-Visas 参考号后，引导他们走完整个 TLScontact 预约 流程 — 选 TLS 中心、选日期、支付 TLS 服务费、确认赴约当天带什么。 与… |
| [`Cost estimate`](skills/cost-estimate/) | 计算法国申根签证申请的总成本，包括领事馆、TLScontact、照片、保险、 快递和其他费用。按申请人或家庭团体。帮助用户提前预算，避免赴约… |
| [`Cover letter`](skills/cover-letter-torlyai/) | 起草个性化求情信，说明出行目的、日期、资金来源和回国承诺。 按目的分变体（旅游/探亲/商务/其他）。输出可打印、A4、单页、 不超过 300 字。当用户说"写求情信"、"求情信该写什么"、"如何向… |
| [`Decide visa type`](skills/decide-visa-type-torlyai/) | 为法国之旅选择正确申根签证类型的向导 — A 类（机场过境）、C 类 （短期，最多 90 天）、D 类（长期，90+ 天）、单次 vs 多次入境、… |
| [`Document checklist`](skills/document-checklist-torlyai/) | 根据申请人的目的、家庭组成、担保情况和过往签证记录，生成法国申根签证申请的 个性化文件清单。按章节（身份/目的/财务/保险/住宿/特殊情况）组织成可打印、… |
| [`Employment letter`](skills/employment-letter/) | 起草公司抬头纸上的工作证明信模板，确认申请人的职位、薪资、批准的 出行假期，以及归来后继续雇佣。同时说明工资单要求（最近 3 个月 与信件配套）。自雇申请人有替代路径，需税务报表+营业注册。当用户… |
| [`Financial checklist`](skills/financial-checklist/) | 将所有财务证据文件整合为单一提交前财务就绪检查。汇总 /employment-letter、/bank-statement-check、/cost-estimate… |
| [`Find slot`](skills/find-slot/) | 无可用时段时寻找 TLScontact 预约的策略。推荐 Visa Master Chrome 扩展为主要工具。说明 TLS 时段释放时间规律。提供中心切换策略… |
| [`France visas form`](skills/france-visas-form-torlyai/) | france-visas.gouv.fr 官方在线申请表的分步指南。引导用户走完 10 个章节（签证向导 → 个人信息 → 旅行证件 → 联系 → 职业 → 出行 细节 → 住宿 → 过往签证 → 家庭 →… |
| [`Group application`](skills/group-application/) | 处理家庭/团体申根签证申请：多人申请的结构性问题。每位申请人需要 自己的 France-Visas 参考号，但可共享一个 TLScontact 团队 ID+… |
| [`Insurance check`](skills/insurance-check/) | 核实旅行保险证明是否符合申根签证要求。检查保额（≥€30,000 医疗， 欧元面值）、地理范围（整个申根区）、医疗遣返覆盖、保单日期 （覆盖全程+缓冲）、姓名与护照一致、证明页清晰度。如有附件则… |
| [`Itinerary builder`](skills/itinerary-builder-torlyai/) | 将 /plan-trip 的骨架扩展为可附在 France-Visas 申请上的逐日行程 — 抵达、每日活动、住宿过渡、返程。交叉检查住宿订单覆盖每一晚、… |
| [`/learn`](skills/learn-torlyai/) | vstack 工具集的选择性跨会话记忆。把用户的基本申请上下文（姓名、行程 日期、同行组成、担保、雇主、TLS 中心、当前申请阶段）存到本地笔记文件， 以便未来 Claude Code… |
| [`Minor application`](skills/minor-application-torlyai/) | 未成年人（18 岁以下）儿童申请法国申根短期签证的入口。引导用户处理 未成年人特定文件要求：出生证明、父母一方/双方不随行时的同意书、 学校请假信、父母护照复印件 + 英国签证/BRP/分享码（如适用）。… |
| [`Minor birth certificate`](skills/minor-birth-certificate/) | 核实未成年（18 岁以下）法国申根签证申请人的出生证明要求。英国签发 的出生证原样接受；外国签发的可能需 apostille+翻译。需原件或公证副本；… |
| [`Minor birth certificate`](skills/minor-birth-certificate-torlyai/) | Verifies birth certificate requirements for minor (under-18) France Schengen visa applicants. UK-issued… |
| [`Minor parent consent`](skills/minor-parent-consent/) | 为父母一方/双方不随行的未成年人（18 岁以下）申根签证申请人起草 公证父母同意书。输出可打印单页信件，父母去公证处签字。当用户说 "为孩子写同意书"、"未成年人出行许可信"，或从… |
| [`Minor parent consent`](skills/minor-parent-consent-torlyai/) | Drafts a notarised parental consent letter for minor (under-18) Schengen visa applicants travelling… |
| [`Minor parent docs`](skills/minor-parent-docs/) | 核实未成年人随行父母为法国申根签证申请准备的文件 — 父母自己的护照、 父母签证/BRP/share code（如非英国国民）、覆盖孩子的父母财务证据。… |
| [`Minor school letter`](skills/minor-school-letter/) | 为未成年人法国申根签证申请起草英国学校请假信。信必须来自学校、用 学校公函抬头、由校长或授权员工签名、确认在读、列出与行程相符的批准 请假日期、并体现孩子预计回校上学。当用户带学龄孩子在学期间出行，… |
| [`Minor school letter`](skills/minor-school-letter-torlyai/) | Drafts a UK school absence letter for a minor's France Schengen visa application. Letter must come from… |
| [`Mock interview`](skills/mock-interview/) | 为法国申根签证申请做的模拟领事面试。法国旅游签证从英国申请很少有 面试（多数仅凭文件决定），但领事可能要求 — 尤其拒签-重申、不规则 财务状况或异常行程。提供按主题组织的题库（目的、与英国的关系、… |
| [`Photo check`](skills/photo-check-torlyai/) | 启用视觉识别的护照照片合规性检查（法国申根签证）。当用户附上图片时， 对照每一项申根照片要求（35×45mm、白色背景、不戴眼镜、中性表情、 6 个月内）分析。输出每项 ✅/❌/⚠️ 表格，含具体失败原因。… |
| [`Plan trip`](skills/plan-trip-torlyai/) | Iteratively plans a France Schengen trip with the user — destinations, dates, duration, group… |
| [`Refusal appeal`](skills/refusal-appeal/) | 处理法国申根签证拒签。读取拒签信、解码拒签代码（A-Z 类别）、 决定是否上诉（罕见；约 60 天窗口）或重申（常见；成功率更好）、 并组织回应特定拒签原因。为重申起草补充求情信。当用户说"我的… |
| [`Refusal appeal`](skills/refusal-appeal-torlyai/) | Handles France Schengen visa refusals. Reads the refusal letter, decodes the refusal code (A-Z… |
| [`Sponsored application`](skills/sponsored-application/) | 处理由第三方为申请人出资的法国申根签证申请。按担保人类型分支： 配偶（最常见）、父母、朋友或雇主（商务出行）。对每种识别具体 文件要求：结婚证/出生证明/关系证明、担保人护照复印件、担保人… |
| [`Sponsored application`](skills/sponsored-application-torlyai/) | Handles France Schengen visa applications where a third party sponsors the applicant's trip. Branches by… |
| [`Start here`](skills/start-here-torlyai/) | 申根签证申请的入口技能。通过 6 个关键问题锁定范围（目的、日期、申请人、 担保情况、过往签证、紧迫性），然后路由到下一步合适的技能。当用户说… |
| [`Timeline planner`](skills/timeline-planner-torlyai/) | 从用户最早出行日倒推签证申请时间表。计算关键路径截止：出行日 减去领取窗口、减去领事处理窗口、减去 TLS 预约缓冲、减去文件准备 时间 = 今日的"做/不做"。标记危险紧张的时间表、建议修复（提前申请、 换… |
| [`Tlscontact form`](skills/tlscontact-form/) | TLScontact 账户创建+预约表的分步指南（https://visas-fr.tlscontact.com/en-us）。 引导用户走完账户设置、France-Visas 参考号关联、团队申请设置、… |
| [`Track application`](skills/track-application-torlyai/) | 引导用户跟踪已提交的法国申根签证申请 — 在哪查、每个状态什么 含义、何时担心、各阶段做什么。涵盖 TLScontact 追踪器、 France-Visas 门户状态和典型处理时间。当用户说"跟踪我的申请"、… |
| [`Translate doc`](skills/translate-doc-torlyai/) | 关于法国申根签证申请何时需要"认证翻译"的指引 — 接受哪些语言（英文+ 法文可直接；其他需认证翻译）、谁能认证（宣誓翻译、ATA 认证、使馆 推荐）、典型费用（每页… |
| [`Vstack upgrade`](skills/vstack-upgrade/) | 自更新 Schengen-master 技能工具集到最新版。检查当前安装版本 vs GitHub 最新可用版、显示变更内容、跑 `git pull` 更新。幂等 — 重复跑… |

## Cold-start context

See [`CLAUDE.md`](CLAUDE.md) — scope, sources of law, citation discipline, and when this plugin does NOT apply.

## Provenance & license

Skills found on GitHub by the ThomasMore search pipeline and imported with their original text; see each `SKILL.md` `author` / `author_url` for provenance and `license` for terms. The author's license text is kept next to each skill in `LICENSE`.

## Disclaimer

These skills produce informational drafts and analyses, not legal advice. Verify against current law before use.
