# Immigration — France

Immigration skills under the law of France.

Practice-area definition (`practices.json`, jurisdiction-agnostic): immigration law: visas and petitions (USCIS), status and residency, asylum, deportation/removal, work and residence permits (pobyt/Aufenthalt), consular procedures for foreign nationals.

Jurisdiction: `fr` · Practice: `immigration` · Skill language: en, zh

## Skills (22)

| Skill | What it does |
|---|---|
| [`/accommodation-verify`](skills/accommodation-verify-torlyai/) | Audits accommodation bookings (hotel, AirBnB, hostel, host-stay) for France Schengen visa requirements —… |
| [`/appointment-prep`](skills/appointment-prep-torlyai/) | TLScontact 法国申根签证赴约前 24 小时清单。核实所有文件已打印（不能 仅屏幕看）、照片是实物打印（不是手机图）、付款卡在钱包、交通已规划 早 15 分钟到、用户已收拾合理的文件夹。在 TLS… |
| [`/audit-application`](skills/audit-application-torlyai/) | Pre-submission audit gate. Reads all the user's collected documents, the scope from /start-here, the cover… |
| [`/bank-statement-check`](skills/bank-statement-check-torlyai/) | 审查银行流水的申根签证申请充足性和格式。核实流水：(1) 覆盖最近 3 个月，(2) 显示申请人全名+地址，(3) 显示足够出行的余额， (4) 无红旗（申请前单笔大额存款、涂抹、刚开户的账户）。当用户说… |
| [`/cover-letter`](skills/cover-letter-torlyai/) | 起草个性化求情信，说明出行目的、日期、资金来源和回国承诺。 按目的分变体（旅游/探亲/商务/其他）。输出可打印、A4、单页、 不超过 300 字。当用户说"写求情信"、"求情信该写什么"、"如何向… |
| [`/decide-visa-type`](skills/decide-visa-type-torlyai/) | 为法国之旅选择正确申根签证类型的向导 — A 类（机场过境）、C 类 （短期，最多 90 天）、D 类（长期，90+ 天）、单次 vs 多次入境、 旅游/商务/探亲/留学、以及是否在法国领事或别处申请（多国行程的… |
| [`/document-checklist`](skills/document-checklist-torlyai/) | 根据申请人的目的、家庭组成、担保情况和过往签证记录，生成法国申根签证申请的 个性化文件清单。按章节（身份/目的/财务/保险/住宿/特殊情况）组织成可打印、… |
| [`/france-visas-form`](skills/france-visas-form-torlyai/) | france-visas.gouv.fr 官方在线申请表的分步指南。引导用户走完 10 个章节（签证向导 → 个人信息 → 旅行证件 → 联系 → 职业 → 出行 细节 → 住宿 → 过往签证 → 家庭 →… |
| [`/itinerary-builder`](skills/itinerary-builder-torlyai/) | 将 /plan-trip 的骨架扩展为可附在 France-Visas 申请上的逐日行程 — 抵达、每日活动、住宿过渡、返程。交叉检查住宿订单覆盖每一晚、 城际交通切实可行、活动组合匹配申报的出行目的。当用户说"帮我… |
| [`/learn`](skills/learn-torlyai/) | vstack 工具集的选择性跨会话记忆。把用户的基本申请上下文（姓名、行程 日期、同行组成、担保、雇主、TLS 中心、当前申请阶段）存到本地笔记文件， 以便未来 Claude Code 会话能从上次结束的地方继续 —… |
| [`/minor-application`](skills/minor-application-torlyai/) | 未成年人（18 岁以下）儿童申请法国申根短期签证的入口。引导用户处理 未成年人特定文件要求：出生证明、父母一方/双方不随行时的同意书、 学校请假信、父母护照复印件 + 英国签证/BRP/分享码（如适用）。 路由到… |
| [`/minor-birth-certificate`](skills/minor-birth-certificate-torlyai/) | Verifies birth certificate requirements for minor (under-18) France Schengen visa applicants. UK-issued birth… |
| [`/minor-parent-consent`](skills/minor-parent-consent-torlyai/) | Drafts a notarised parental consent letter for minor (under-18) Schengen visa applicants travelling without… |
| [`/minor-school-letter`](skills/minor-school-letter-torlyai/) | Drafts a UK school absence letter for a minor's France Schengen visa application. Letter must come from the… |
| [`/photo-check`](skills/photo-check-torlyai/) | 启用视觉识别的护照照片合规性检查（法国申根签证）。当用户附上图片时， 对照每一项申根照片要求（35×45mm、白色背景、不戴眼镜、中性表情、 6 个月内）分析。输出每项 ✅/❌/⚠️ 表格，含具体失败原因。… |
| [`/plan-trip`](skills/plan-trip-torlyai/) | Iteratively plans a France Schengen trip with the user — destinations, dates, duration, group composition,… |
| [`/refusal-appeal`](skills/refusal-appeal-torlyai/) | Handles France Schengen visa refusals. Reads the refusal letter, decodes the refusal code (A-Z categories),… |
| [`/sponsored-application`](skills/sponsored-application-torlyai/) | Handles France Schengen visa applications where a third party sponsors the applicant's trip. Branches by… |
| [`/start-here`](skills/start-here-torlyai/) | 申根签证申请的入口技能。通过 6 个关键问题锁定范围（目的、日期、申请人、 担保情况、过往签证、紧迫性），然后路由到下一步合适的技能。当用户说 "我要申请申根签证"、"从哪里开始"、"第一次申请"等表明刚开始时使用。… |
| [`/timeline-planner`](skills/timeline-planner-torlyai/) | 从用户最早出行日倒推签证申请时间表。计算关键路径截止：出行日 减去领取窗口、减去领事处理窗口、减去 TLS 预约缓冲、减去文件准备 时间 = 今日的"做/不做"。标记危险紧张的时间表、建议修复（提前申请、 换 TLS… |
| [`/track-application`](skills/track-application-torlyai/) | 引导用户跟踪已提交的法国申根签证申请 — 在哪查、每个状态什么 含义、何时担心、各阶段做什么。涵盖 TLScontact 追踪器、 France-Visas 门户状态和典型处理时间。当用户说"跟踪我的申请"、… |
| [`/translate-doc`](skills/translate-doc-torlyai/) | 关于法国申根签证申请何时需要"认证翻译"的指引 — 接受哪些语言（英文+ 法文可直接；其他需认证翻译）、谁能认证（宣誓翻译、ATA 认证、使馆 推荐）、典型费用（每页 £25-60）、如何核实证书。当用户有中文结婚证、… |

## Cold-start context

See [`CLAUDE.md`](CLAUDE.md) — scope, sources of law, citation discipline, and when this plugin does NOT apply.

## Provenance & license

Skills found on GitHub by the ThomasMore search pipeline and imported with their original text; see each `SKILL.md` `author` / `author_url` for provenance and `license` for terms. The author's license text is kept next to each skill in `LICENSE`.

## Disclaimer

These skills produce informational drafts and analyses, not legal advice. Verify against current law before use.
