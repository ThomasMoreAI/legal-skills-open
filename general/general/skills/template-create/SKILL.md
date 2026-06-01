---
name: template-create
title: テンプレート作成（template-create）
description: This skill should be used when the user asks to "create a template", "テンプレート作成", "書式を登録", "XLSXをテンプレート化", "テンプレート登録", "この書式を登録して", "テンプレートを追加", or wants to register a new court document template from an XLSX file.
author: llamadrive
author_url: https://github.com/llamadrive/bengo-toolkit/tree/main/skills/template-create
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: ja
---

# テンプレート作成（template-create）

ユーザーが持ち込んだXLSXファイルを分析し、入力フィールドを定義してテンプレートとして登録する。

## ワークフロー

### Step 0: 保存場所の決定と案件フォルダ解決

初回使用時のみ案内メッセージを表示する（2 回目以降は silent、処理は決してブロックしない）:

```bash
python3 skills/_lib/first_run.py notice
```

出力があれば、そのままユーザーに提示してから保存場所の決定へ進む。

テンプレートは **保存場所** を 3 通りから選べる:

- **「この案件のみ」**（`case`、**既定**、安全側）— 現在の案件フォルダの中にだけ保存
  （`<案件フォルダ>/.claude-bengo/templates/`）。他の案件には影響しないため、試しに
  登録する・案件固有の派生版を作る、といった用途に安全。後から
  `/template-promote --to user|firm` で他の案件からも使えるようにできる。
- **「事務所共有」**（`firm`）— 事務所全員で共有するクラウド同期フォルダに保存。
  `/template-firm-setup` で事前に設定した Google Drive / Dropbox / OneDrive 等の
  パスに保存される。事務所全員から見えるため、**クライアントの個人情報が含まれて
  いると保存できない**（以下のガード参照）。未設定や同期フォルダに到達できない
  場合は使えない（その旨を案内する）。
- **「この PC の全案件で共通」**（`user`）— この PC 限定で、すべての案件から使える
  ように `~/.claude-bengo/templates/` に保存。この PC 上の全案件から見えるため、
  **クライアントの個人情報が含まれていると保存できない**（以下のガード参照）。

**優先順**: 実行時は $ARGUMENTS の `--scope` フラグがあればそれを採用。なければ
以下を 1 度だけ尋ねる:

```
このテンプレートをどこに保存する？
  1. この案件のみ（推奨・既定） — {案件フォルダ名} の中にだけ保存される
  2. 事務所全員で共有          — クラウド同期フォルダに保存（要 /template-firm-setup、個人情報の混入注意）
  3. この PC の全案件で共通    — この PC 上の全案件から使える形で保存（個人情報の混入注意）

番号で回答（未回答は 1）:
```

選択肢 2 を選んだ場合、事務所共有フォルダに到達できないと保存できない。事前に
`python3 skills/_lib/workspace.py firm-status` を呼んで確認するか、エラーが返ったら
`/template-firm-setup <パス>` を案内する。

保存場所が決まったら保存先ディレクトリを解決する:

```bash
# user スコープ
python3 skills/_lib/workspace.py templates   # user_templates_dir を読む
# case スコープ
python3 skills/_lib/workspace.py resolve     # workspace_root を読む
```

- `user` → 保存先 = `~/.claude-bengo/templates/`（workspace 初期化不要）
- `case` → 保存先 = `{workspace_root}/.claude-bengo/templates/`。walk-up で
  見つからなければ CWD を silently 初期化する。

**重要（case スコープの制限）:** CWD が `~/.claude-bengo/` 配下の場合、
`ensure_workspace()` は `WorkspaceUnderGlobalError` を投げて拒否する。
`~/.claude-bengo/` は予約領域であり、その下を案件フォルダ扱いすると監査ログや
user テンプレートが混線する。エラーが発生したらユーザーに「別のフォルダ
に `cd` してから再実行してほしい」と案内する。

**セキュリティ（user スコープ時の必須チェック）:** user 保存前に、対象 XLSX に
クライアントの実データが残っていないかを決定論的に走査する:

```bash
python3 skills/_lib/pii_scan.py scan --xlsx "<source.xlsx>" --json
```

戻り値 JSON:
```json
{
  "verdict": "clean" | "suspicious",
  "count": 0,
  "findings": [
    {"category": "personal_name", "cell": "B3", "excerpt": "[シート:Sheet1] …甲野太郎様…", ...},
    ...
  ],
  "by_category": {"personal_name": 2, "postal_code": 1}
}
```

`verdict == "clean"` ならそのまま Step 1 へ進む。`"suspicious"` の場合は、
**user 保存は自動的に拒否** される（ユーザー override 不可）。
発見箇所を全件列挙したうえで、以下のいずれかを案内する:

```
⛔ 「この PC の全案件で共通」での保存は中止した。
   このファイルにクライアントの個人情報のような記述が {N} 件検出されたため:
  - B3 [氏名]: 「…甲野太郎様…」
  - D7 [住所]: 「…東京都千代田区丸の内1丁目…」
  - E9 [生年月日]: 「…生年月日: 昭和50年1月1日…」

次のいずれかを選んでほしい:
  1. 「この案件のみ」に保存する — 現在の案件フォルダの中にだけ保存される
  2. 中止する — 元の XLSX から上記の記述を削除して再実行
```

注意: `pii_scan.py` は conservative（偽陽性寄り）で、検出がプレースホルダや
記入例であることもある。しかし user はこの端末の全案件に波及するため、
**偽陽性側に倒して拒否を既定とする**。

**開発者バックドア（ユーザーには案内しないこと）:** 環境変数
`CLAUDE_BENGO_ALLOW_PII_ON_GLOBAL=1` で findings を無視して保存できる（テスト・
CI 用 escape hatch）。通常運用では設定しない。

### Step 1: XLSXファイルの確認

ユーザーにベースとなるXLSXファイルのパスを確認する。$ARGUMENTS で指定されている場合はそれを使用する。

ファイルが存在することを Glob または Read で確認する。

### Step 2: シート構造の分析

以下のMCPツールでXLSXの構造を把握する:

1. `mcp__xlsx-editor__get_workbook_info` — シート一覧、行数・列数、結合セル情報を取得
2. `mcp__xlsx-editor__read_sheet` — セルデータを取得。**大きなシート（50行超 or 結合セル多数）は `range` パラメータで30行ずつ分割して読み取る**（例: `range: "A1:N30"` → `range: "A31:N60"` → ...）。全体を一括読取するとトークン制限を超えてエラーになる場合がある

複数シートがある場合はユーザーにどのシートをテンプレート対象とするか確認する。

### Step 3: フィールド候補の特定

検出方法は **2 つ** ある。$ARGUMENTS に `--sample <path>` が含まれているか、
あるいはユーザーが「記入済みの例がある」と申告した場合は **A（サンプル差分モード、推奨）**、
それ以外は **B（LLM 近傍推論モード、従来）** を使う。

#### A. サンプル差分モード（推奨）— `--sample` 指定または申告あり

空テンプレ (`blank.xlsx`) と 1 件完全記入済みのサンプル (`sample.xlsx`) を
決定論的に突き合わせ、field を抽出する。section 見出し・小計行・2 列ラベルに強い。

```bash
python3 skills/_lib/template_detect.py diff \
    --blank "<blank.xlsx>" \
    --sample "<sample.xlsx>" \
    [--sheet "<シート名>"]
```

戻り値 JSON の `fields` 配列にそのまま提案候補が入っている:

```json
{
  "fields": [
    {"id": "field_1", "label": "事件番号:", "type": "text", "required": true,
     "position": {"row": 3, "column": 2}, "example_value": "令和5年(ワ)第100号"},
    {"id": "table_1", "label": "債権者一覧表", "type": "table", "required": true,
     "range": {"headerRow": 5, "dataStartRow": 6, "startColumn": 1, "endRow": 8, "endColumn": 3},
     "columns": [{"id": "col_1", "label": "№", "type": "number"}, ...]}
  ],
  "warnings": []
}
```

これをそのまま Step 4 のテーブルに流し込み、ユーザーには「検出を確認して
ほしい」と 1 発で提示する。LLM の勘よりも精度が高いため、フィールド個別の
type 推論や position の手直しは最小限で済む。

ユーザーが sample を持っていない場合は「過去に同じ書式で作成した XLSX があれば
それを使えばよい。なければ B モードに切り替える」と案内する。

#### B. LLM 近傍推論モード（従来）

セルデータを分析し、入力フィールド候補を特定する。以下のパターンを探す:

**単一セルフィールド候補:**
- 空セルの左または上にラベルテキストがある箇所（例: 「氏名」の右隣が空 → テキストフィールド）
- 「年月日」「日付」等のラベル隣接空セル → 日付フィールド
- 「金額」「円」等のラベル隣接空セル → 数値フィールド
- プレースホルダ的テキスト（「○○」「記入」等）が入ったセル

**テーブルフィールド候補:**
- ヘッダ行 + 空行が繰り返される領域
- 「No.」「番号」「№」等のヘッダを持つ表形式の領域

**重要: テーブルの headerRow と dataStartRow の区別**
- ヘッダ行（headerRow）: 列ラベルが記載された行（例: №, 金融機関の名称, 残高 等）
- データ開始行（dataStartRow）: ヘッダの直下にある最初のデータ行（通常 headerRow + 1）
- `range.dataStartRow` には必ずデータ開始行を指定する。ヘッダ行を指定してはならない
- 判別方法: セルの値が列ラベル（名称、種類、金額、所在 等）であればヘッダ行。数字や具体的なデータ（○○銀行、100万円 等）であればデータ行

**選択フィールド候補:**
- データ検証（ドロップダウン）が設定されたセル

ユーザーにフィールド候補の一覧をテーブルで提示する:

```
| # | ラベル | セル位置 | 推定タイプ | 根拠 |
|---|--------|----------|-----------|------|
| 1 | 原告氏名 | C3 | text | 「原告氏名」(B3)の右隣が空 |
| 2 | 事故日 | C5 | date | 「事故年月日」(B5)の右隣が空 |
| 3 | 損害一覧 | A10:E20 | table | ヘッダ行+空行の繰り返し |
```

### Step 4: ユーザーとの対話でフィールド確定

ユーザーと対話しながら以下を確定する:

1. **フィールドの採否**: 候補を承認/却下/追加
2. **フィールドID**: 英数字のスネークケースID（例: `plaintiff_name`, `accident_date`）。
   判断に困ったら label をローマ字化した `field_N` 形式で自動生成してよい（ID は
   内部キー、label が表示・マッピングの主軸のため）。
3. **フィールドラベル**: 日本語表示名
4. **フィールドタイプ**: `text` | `number` | `date` | `textarea` | `select` | `table`
5. **必須/任意**: `required: true/false`
6. **セル位置**:
   - 単一セル: `position: { row: N, column: N }` (1-indexed)
   - テーブル: `range: { headerRow, dataStartRow, startColumn, endRow, endColumn }` (1-indexed)
     - `headerRow`: 列ラベルの行番号
     - `dataStartRow`: 最初のデータ行番号（**ヘッダ行ではなく、その下の行**）
7. **テーブルの場合**: 各列の定義 `columns: [{ id, label, type }]`
8. **選択の場合**: 選択肢 `options: [...]`
9. **マッピング補助（任意、推奨）**: `/template-fill` が PDF からこのフィールドに
   入れる値を正しく拾うためのヒント。label だけで曖昧な場合は必ず聞く:
   - `description`: 1-2 文で「何を入れるフィールドか」を書く（例:「債務者の戸籍上の
     氏名。相手方弁護士の氏名ではない」）
   - `synonyms`: ソース文書で使われそうな別名（例: `["借主", "お名前", "契約者名"]`）
   - `example_value`: 記入例（例: `"甲野太郎"` / `"1,000,000"` / `"令和5年3月1日"`）

   label が明確（例: 「事件番号」）ならスキップしてよい。曖昧（例: 「氏名」「金額」
   「日付」）の場合はユーザーに「これはどの場面の氏名か」などを 1 回だけ確認し、
   その回答を description に転写する。

### Step 4.5: センチネル書込による位置検証（推奨）

Step 4 で確定したフィールドのセル位置が本当に正しいかを視覚的に確認するため、
blank XLSX のコピーに **センチネル値**（`<<氏名>>` `<<金額>>` 等）を書き込んで
ユーザーに見てもらう:

1. blank XLSX を一時パス `<blank>.preview.xlsx` にコピー
2. 各単一セルフィールドの `position` に `mcp__xlsx-editor__write_cell` で
   `<<{label}>>` を書き込む（label が空なら `<<{id}>>`）
3. テーブルフィールドは `dataStartRow` の 1 行目にだけ各列のセンチネルを書き込む
4. ユーザーに「`<blank>.preview.xlsx` を開いて、各 `<<...>>` が想定どおりの
   セルに入っているか確認してほしい」と案内
5. ズレがあればユーザーに該当フィールドの番号を指示してもらい、position を
   修正してから再書込 → 再確認

**スキップ条件:** Step 3 で A（サンプル差分モード）を使った場合は検出が
決定論的なので、ユーザーが「差分モードの結果を信用してスキップ」と明示すれば
省略してよい。B モード（LLM 近傍推論）の場合は必ず通す。

一時プレビューファイルは Step 7 完了後に削除する。

### Step 5: メタデータの確認

テンプレートの基本情報をユーザーに確認する:

- `id`: 一意識別子（ファイル名に使用。英数字・ハイフン）
- `title`: テンプレート名（日本語）
- `description`: 説明（1-2文）
- `category`: カテゴリ（自由記述。例: 民事訴訟, 家事事件, 交通事故, 相続, 労働）

### Step 6: YAML保存

確定したフィールド定義を YAML 形式の文字列として組み立てる（まだ書き込まない）。
Step 7 で XLSX と一緒に保存する。

### Step 6.5: 統合保存（code-level PII guard 経由、v3.3.0-iter1〜）

**Write + copy_file.py で直接保存してはならない。** `template_lib.py save-user`
を呼ぶことで、user スコープ時に PII 混入を **code レベルで** ブロックする:

```bash
# YAML を一時ファイルに書いてから
# /tmp/template-{id}.yaml に組み立て結果を Write

python3 skills/_lib/template_lib.py save-user \
  --source "<original xlsx>" \
  --id "<template_id>" \
  --scope "<case|user>" \
  --yaml-file /tmp/template-{id}.yaml \
  [--replace]
```

戻り値 JSON の `code: "pii_found"` が返った場合（exit 4）は以下を行う:

- `findings` 配列をユーザーに全件表示
- 「この PC の全案件で共通」での保存をあきらめるか、XLSX から個人情報のような
  記述を削除して再実行するかを選んでもらう
- 「このまま保存したい」と言われても **進めてはならない**（コードが弾く）
- 保存場所を「この案件のみ」に切り替えれば保存される（`--scope case`）

他の exit コード:
- exit 1 = ID 不正 / source 不在
- exit 3 = 既存衝突（`--replace` を検討）
- exit 4 = PII 検出（上記）

Step 7 は本コマンドで置換されるため不要。

**ID 検証（必須）:** テンプレート `{id}` は以下の正規表現を必ず満たすこと:

```
^[a-z0-9][-a-z0-9_]{0,63}$
```

- 先頭は小文字英数字
- 以降は小文字英数字・ハイフン・アンダースコアのみ
- 合計 64 文字以内

`.`、`/`、`\`、空白、大文字、非 ASCII は**禁止**。これは `{dest_dir}/{id}.yaml` を生成するときに `..` や絶対パスで保存先ディレクトリの外に書き出す path-traversal を防ぐためである。ユーザーが提案する ID が規則に合わない場合は、該当箇所を示して「英小文字・数字・ハイフン・アンダースコアのみで再提案してほしい」と返す。

YAML形式はプラグインの `templates/_schema.yaml` に準拠する。

### Step 7: （廃止: Step 6.5 に統合済み）

v3.3.0-iter1 以降は `template_lib.py save-user` が YAML 書込と XLSX コピーを
一括で行う。個別の Write / copy_file.py は呼び出さない（PII code-gate を迂回
させないため）。

### Step 8: 完了サマリー

以下を表示する:
- 保存場所（「この PC の全案件で共通」 / 「この案件のみ」 / 「事務所共有」）
- テンプレート名と ID
- 登録フィールド数（タイプ別内訳）
- 保存先パス（YAML + XLSX）
- `/template-fill` での使用方法

## セル位置の変換

XLSXのセルアドレス（A1, B3 等）をYAMLの行列番号に変換する:
- A1 → row: 1, column: 1
- C5 → row: 5, column: 3
- 列: A=1, B=2, C=3, ... Z=26, AA=27, ...

## エラーハンドリング

- XLSX以外のファイル: 対応フォーマットを案内する。
- 空のシート: 「テンプレートとして使用するセルがありません」と報告する。
- 既存 ID との重複（同じ保存場所に同 ID のテンプレートが既にある）: 上書きするか別 ID にするかをユーザーに確認する。保存場所をまたいで同 ID を作ることは禁じないが、`/template-fill` では「この案件のみ」が「この PC の全案件で共通」を上書きして見えるため、意図しているか確認を促す。
- 保存先ディレクトリが存在しない場合: 作成する。

## 次の一手（ユーザーに提案する）

テンプレート登録完了時、以下を提案する:

```
💡 次の一手:
  - 登録した書式にデータを入れる: /template-fill <ソース PDF>
  - 登録済み書式を一覧: /template-list
  - 別の書式も登録: /template-create <別の XLSX>
```
