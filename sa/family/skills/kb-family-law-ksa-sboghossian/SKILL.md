---
name: kb-family-law-ksa-sboghossian
title: Knowledge Pack — KSA Family Law (Personal Status Law 2022)
description: Use when a matter involves marriage, divorce, custody, maintenance, or inheritance in Saudi Arabia. Covers the KSA Personal Status Law (Royal Decree 73/1443H, 2022) — the first codified personal status law in KSA — which maintains the Hanbali Sharia framework while introducing clearer procedural rules on talaq, khula, custody (hadana), maintenance (nafaqa), and Islamic inheritance (fara'id). Also covers the position of non-Muslims in KSA family matters. Triggers on Saudi divorce, mahr, custody KSA, inheritance Saudi, or talaq questions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-family-law-ksa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: family
language: en
---

# Knowledge Pack — KSA Family Law (Personal Status Law 2022)

## Scope and Sources

Saudi Arabia's family law is historically grounded in **Islamic Sharia** (Sunni Hanbali school as the default for KSA Muslims). The **Personal Status Law (Royal Decree 73/1443H, 2022)** represents the Kingdom's first comprehensive codification of personal status matters — reducing judicial discretion while maintaining the Sharia framework.

| Source | Role |
|---|---|
| Personal Status Law (RD 73/1443H, 2022) | Primary codification — marriage, divorce, custody, maintenance, inheritance |
| Hanbali Fiqh | Default gap-filler where the law is silent |
| Judicial Interpretations | Increasing standardization through specialized family courts |
| Non-Muslim foreign law | Permitted in limited matters for non-Muslim foreigners (see below) |

**Applicable persons**: Saudi nationals + foreign Muslims residing in KSA (by default). Non-Muslims may apply for foreign-law application in certain civil-status matters.

---

## Marriage

### Requirements

| Requirement | Detail |
|---|---|
| Mutual consent (Ijab and Qabul) | Both parties must expressly accept |
| Mahr (dower) | Gift from husband to wife; may be prompt (muajjal) or deferred (mu'ajjal); not waivable |
| Wali (guardian) | Wife requires a male guardian (typically father, then paternal relatives) to conclude the marriage contract |
| Witnesses | At least two adult Muslim male witnesses (or one male and two female in some interpretations; codified rules apply) |
| Court registration | Marriage must be registered with the court — 2022 law strengthens this requirement |
| Age | Minimum age for marriage regulated; court approval required for marriages below prescribed age |

### Polygamy

- A Muslim man may marry up to four wives simultaneously.
- 2022 law requires court permission to contract a second (or further) marriage, with assessment of the first wife's rights and husband's financial capacity.

---

## Divorce

### Types of Divorce

| Type | Initiated by | Mechanism |
|---|---|---|
| **Talaq** | Husband | Verbal or written pronouncement; 2022 law requires court documentation and notification to wife |
| **Khula** | Wife | Wife returns mahr or agrees compensation to husband; court-facilitated; does not require husband's agreement if court approves |
| **Faskh** (judicial dissolution) | Wife | Judicial divorce on specific grounds — non-support (nafaqa), cruelty, harm, impotence, absence, imprisonment, disease |
| **Mutual divorce** | Both parties | By agreement; simplified court process |

### Talaq — Key Procedural Changes (2022 Law)

- Talaq must be **notified to the court** and registered; automatic operation on oral pronouncement alone no longer sufficient for full legal effect.
- **Revocable talaq** (raj'i): husband may revoke within the iddah period without needing a new marriage contract.
- **Irrevocable talaq** (bain): after three pronouncements, or after iddah if not revoked; remarriage requires an intervening marriage (muhalil) — a significant social and legal threshold.

### Iddah (Waiting Period)

| Status | Iddah Duration |
|---|---|
| Divorced, non-pregnant | Three menstrual cycles |
| Divorced, pregnant | Until delivery of child |
| Widowed | 4 months and 10 days |

- During iddah: husband must provide maintenance and housing.
- Revocable talaq: husband may revoke; wife cannot remarry until iddah completes.

---

## Custody (Hadana)

The 2022 Personal Status Law modernizes custody rules, incorporating a **best-interest standard** alongside traditional Sharia rules.

| Principle | Rule |
|---|---|
| Primary custody | **Mother** has priority for young children post-divorce |
| Transfer to father | Traditionally: boys ~9–10 years, girls at marriageable age; 2022 law allows courts to extend mother's custody under best-interest standard |
| Best-interest discretion | Courts now explicitly weigh the child's welfare, including education, stability, and relationships with both parents |
| Visitation | Non-custodial parent (typically father) has enforceable visitation rights |
| Relocation | Custodian may not relocate child outside KSA without court approval |

### Custody Termination Grounds

Mother loses custody rights if:
- She remarries a man not related to the child (in Hanbali rules — courts may now apply discretion)
- She is proven unfit (abuse, neglect, moral unfitness)
- She changes religion (in strict Hanbali interpretation — courts weigh best interest)

---

## Maintenance (Nafaqa)

| Obligation | Rule |
|---|---|
| During marriage | Husband must provide adequate maintenance (food, clothing, housing, medical care) proportionate to his means |
| Iddah maintenance | Continues at full level during iddah after revocable talaq; limited during irrevocable talaq |
| Child support | Father responsible for child support regardless of custody arrangement |
| Duration (children) | Males: until financially independent (adulthood); Females: until marriage |
| Enforcement | Family courts enforce maintenance orders; non-compliance can lead to imprisonment in extreme cases |

---

## Islamic Inheritance (Fara'id)

KSA inheritance is governed by **Quranic fixed shares (fara'id)** — mandatory for Muslims; courts apply these rules automatically.

### Core Principles

1. **Fixed shares**: Quran specifies exact proportions for certain heirs (spouse, parents, children in different configurations).
2. **Male double female rule**: in the same class of heirs, a male typically receives twice the share of a female (e.g., son vs daughter).
3. **Residuaries (asaba)**: heirs not in fixed-share categories inherit the remainder proportionately.
4. **Non-Muslim exclusion**: under classical Hanbali rules, a non-Muslim cannot inherit from a Muslim, nor vice versa.
5. **Bequest limit**: testator may bequeath by will up to **1/3 of the estate** to non-heirs; bequests to legal heirs beyond fara'id share are void.
6. **Debts first**: all debts and funeral expenses are settled before inheritance distribution.

### Common Spouse Shares

| Scenario | Husband's Share | Wife's Share |
|---|---|---|
| No children | 1/2 | 1/4 |
| With children | 1/4 | 1/8 |

### Children's Shares

- Daughter only (no son): 1/2 (if one daughter); 2/3 (if multiple daughters, shared equally).
- Son only: inherits as residuary (remainder after other fixed shares).
- Son + daughter: son gets twice daughter's share from the residue.

---

## Non-Muslims in KSA

- The 2022 Personal Status Law allows **non-Muslim foreigners** to elect foreign-law application for personal status matters in certain circumstances.
- Non-Muslims married under a foreign civil law may seek divorce / inheritance through foreign-law processes, provided both parties consent and the applicable foreign law can be proven.
- DIFC-style civil-personal-status courts **do not exist in KSA** — there is no free-zone equivalent.
- Cross-border marriages and divorces are recognized case-by-case; courts examine conformity with Sharia and public order.

---

## Practical Drafting Notes

| Situation | Advice |
|---|---|
| Pre-marital agreements (Aqd al-Zawaj addendum) | Permissible to include additional conditions favorable to wife (e.g., right to work, right to education, conditions for talaq) — courts will enforce if not contrary to Sharia |
| Mahr specification | Always specify: amount, currency, whether prompt or deferred; deferred mahr is payable on divorce or death |
| Divorce proceedings | Require specialized family court lawyers; court-supervised documentation essential |
| Inheritance planning | Wills limited to 1/3 of estate for non-heirs; coordinate with overseas assets (foreign assets may allow broader testamentary freedom) |
| Foreign nationals | Confirm whether both parties are Muslim and whether foreign-law election is applicable |

---

## Specialized Family Courts

- 2022 reform established dedicated **family courts** across KSA.
- Cases managed through **Najiz** (electronic court system).
- Judge has broader discretion to balance best-interest considerations under the new law.
- Legal representation increasingly the norm for contested matters.

## Caveats & Currency

The 2022 Personal Status Law was a landmark reform; court implementation continues to develop. Judicial practice may vary between regions. Islamic inheritance rules require case-by-case computation as the final estate composition determines each heir's share. Cross-border recognition of KSA family-court orders varies by country — verify in any relevant foreign jurisdiction before advising on international aspects.

## Related Skills

- [[kb-family-law-lb-personal-status]]
- [[kb-family-law-uae-civil-personal-status]]
- [[kb-shariah-finance-aaoifi]]
- [[kb-employment-law-ksa]]
- [[draft-prenup]]
- [[draft-will]]
