# 批量补来源标注与残留中文转写裁决记录

裁决日期：2026-11-24
背景：验证报告存在三类问题——EN 单元格残留中文文号（untranslated text）、强度明细行缺来源标注（intensity source detail missing）、量化字段缺来源标注（quantitative source missing）。用户批准修复范围 1–4 项（不含 102 处非官方来源 URL 替换）。

## 一、诊断

| 类别 | 数量 | 处理 |
|---|---|---|
| EN 单元格残留中文文号（如 财税〔2010〕110号） | 批量转写 49 处 pin 字段 + 未 pin 字段若干 | 按数据集惯例拼音转写（Cai Shui [2010] No. 110） |
| 强度明细行缺来源标注 | 249 处（EN 182 + CN 67） | 句末追加来源（EN: `(Source: ...)`；CN: `（来源：...）。`） |
| 量化字段缺来源标注（交易量、补贴限额/预算、温室气体覆盖等） | 72 处（EN 35 + CN 37） | 同上追加来源；顺带修正 EN `sources:` → `Source:` 大小写 |
| 批量规则未覆盖的残余中文/全角字符 | 5 单元格（2 Description、3 自愿工具） | 基金名用英文释义、专名拼音转写、全角引号「」改 ASCII 引号 |

## 二、执行

- `temp/fix_source_attributions.py`：批量转写 + 补标，共 321 字段（249 强度 + 72 量化）。来源取自既有字段（法律文件名称、工具名称），量化字段另有 20 条 curated 映射（如 CHNSUBESPI05S000 限额 → 天保二期实施方案；碳市场交易量 → 北京绿色交易所）；无法从文号提取时回退至政策文件名称。
- CN 侧同步补标以保证双语一致（强度 67、量化 37）。
- `temp/fix_cjk_2rows.py` + 全角引号修复：清除剩余 5 单元格中文/全角字符。
- 生成器 `scripts/generate_english_from_chinese.py` 同步 297 处 ROW_TRANSLATIONS pin（批量补标的 EN 字段 + 早前会话 CSV 漂移字段），使再生成输出与当前 CSV 逐字节一致。
- 执行中生成器源文件损坏，经 `.pyc` 字节码执行恢复 + tokenize 定位拼接修复；全部函数字节码与原 pyc 一致，5 个模板再生成 EN CSV 与当前 CSV 逐字节一致（cmp 验证）。
- 证据日志：无需新增记录——来源标注出自既有数据字段，判定由本记录载明（与 `blank_field_backfill_20261124.md` 惯例一致）。

## 三、验证结果

- EN CSV 全量扫描：除豁免字段 `Domestic instrument name` 外中文字符 0 处。
- 验证报告仅剩 102 条 `non-official source_url` 警告（用户明确排除范围）；untranslated / intensity / quantitative 三类清零。

## 四、惯例声明

- 中文文号在 EN 侧一律拼音转写（含文号前缀逐字转写，如 交办水〔2024〕60号 → Jiao Ban Shui [2024] No. 60）。
- 量化字段来源标注用 `Source: {来源}`（EN）/ `来源：{来源}`（CN）置于数值之后；基金名等不可译专名用英文释义；口号式原则句用拼音（谁提供、谁获利，谁受益、谁承担 → Shui Tigong, Shui Huoli; Shui Shouyi, Shui Chengdan）。
- 102 处非官方 source_url 留待后续按官方来源阶梯处理（未在本批范围）。
