# ecm-dd-data-verify

ECM 尽职调查工具类 skill：调用 Tushare Pro / 企查查开放平台等公开数据源，与客户材料做
交叉比对，输出"数据差异清单"供业务 DD skill 作为输入使用。

本 skill **不输出** DD Memo（五段式）。合规结论由业务 DD skill 完成。

## 快速开始

```bash
# 1. 安装依赖
pip install -r scripts/requirements.txt

# 2. 配置凭证（至少一个组合；缺失时自动进 fallback）
export TUSHARE_TOKEN=xxxxxx
export QCC_APPKEY=yyy
export QCC_SECRET=zzz

# 3. 预检
python scripts/tushare_connector.py --smoke
python scripts/qcc_connector.py --smoke
```

详见 [SKILL.md](./SKILL.md) 和 [../../docs/data-connectors.md](../../docs/data-connectors.md)。
