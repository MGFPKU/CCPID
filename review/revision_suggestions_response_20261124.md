# CCPID 修订建议（2026-11-24 版）裁决记录

审查依据：`c:\Users\admin\OneDrive - pku.edu.cn\桌面\revision suggestions.docx`（2026-11-24 15:26 更新版，共 5 条）
裁决日期：2026-11-24
用户指令：「1. 公交车一并修正；4. 路径名按建议修改。其余都按你的判定执行。」

本记录取代 `further_revision_decisions_20261119.md` P1-9，并取代 `structural_review_decisions_20261124.md` 第 1、3、4 项（取代声明见文末）。

## 一、裁决总览

| # | 建议 | 裁决 | 实施方式 |
|---|---|---|---|
| 1 | 车辆补贴区分三种机制：报废并新购归 Trade-in subsidy；Row 40 父工具拆分 | 采纳（含公交车） | 货车报废并新购 → CHNSUBTISI04S000；冷链仅新购 → CHNSUBVPSI05S000（独立工具）；乘用车报废更新 → CHNSUBTISI05S000；公交车及动力电池更新 → CHNSUBTISI06S000；删除旧 CHNSUBVPSI01S000/S001/S002 行；VSS 交叉引用更新。CN+EN 同步 |
| 2 | 区分绿电交易与绿证单独交易，新增 Renewable energy certificate trading | 无需修正 | 数据现状已满足：CHNTRAGETI01S000（绿电交易，Extended）与 CHNTRARECI01S000（绿证市场，Direct match）两工具均已收录，描述已注明并行关系与区别。不新增路径、不新增工具 |
| 3 | 需求响应两项：DRM 转 Framework standards 并更名；删除国家层面 DRC | 采纳（DRC 路径定义保留，见下） | 删除 CHNSUBDRCI01S000；CHNTRADRMI01S000 → CHNFRMDRMI01S000，路径更名为 需求响应市场参与规则 / Demand response market participation rules，描述吸收第 19 条价格机制与第 47 条背景；**保留** DRC 路径定义（与建议的偏差及理由见条目 3） |
| 4 | DPV 保留并优化名称 | 采纳 | EN 路径名改为 Distributed solar PV project development and grid-integration rules（CN 路径名不变）；描述补 CCPID 特有路径对照说明；英文工具名称维持官方规章译名 |
| 5 | MEPS 细分维持，IFCMA 映射优化 | 维持现状（无需数据修正） | 5A/5B 现状已符合建议；5C 维持 2026-11-19 裁决（IFCMA 引用词表无更宽泛可引用项，Extended → MEPS for electric equipment 已表达限定） |

## 二、逐条裁决与理由

### 1. 车辆补贴三种机制区分（采纳，含公交车）

**事实核验**：建议所述三机制区分（VPS 仅购置 / VSS 仅报废 / TIS 报废并新购）与 IFCMA 路径定义一致，且与 approaches_cn.md 中 VPS 定义「仅报废不置换的计划另行归入车辆报废更新补贴」的既有规则相符。旧结构问题属实：CHNSUBVPSI01S000 父工具同时包含「需报废旧车的报废并新购补贴（S001）」与「不需报废的仅新购补贴（S002）」，补贴条件不同，违反一个工具对应一个运行机制的原则。

**执行**（CN+EN 同步，证据日志 ID 重指 + 裁决行追加，generator pins 同步）：

| 旧结构 | 新结构 | ID |
|---|---|---|
| 老旧营运货车报废并新购补贴（VPS01S000） | 老旧营运货车报废并新购补贴（以旧换新补贴） | CHNSUBTISI04S000 |
| 冷链配送货车仅新购（VPS01S001） | 新能源城市冷链配送货车购置补贴（独立工具） | CHNSUBVPSI05S000 |
| 老旧营运货车提前报废补贴（VSS01S000） | 维持（车辆报废更新补贴），描述交叉引用更新 | CHNSUBVSSI01S000 |
| 汽车报废更新补贴（VPS02S000） | 汽车报废更新补贴（以旧换新补贴） | CHNSUBTISI05S000 |
| 新能源城市公交车及动力电池更新补贴（VPS04S000） | 同左（以旧换新补贴，用户指令「公交车一并修正」） | CHNSUBTISI06S000 |
| 汽车置换更新补贴（VPS03S000） | 维持（仅出售旧车不报废，建议明确仍归 VPS） | CHNSUBVPSI03S000 |

旧 CHNSUBVPSI01S000/S001/S002 三行删除。经济类 CSV 车辆补贴块现序：TIS01（船舶）→ TIS02（农机）→ TIS03（家电）→ TIS04（货车报废并新购）→ VSS01（货车提前报废）→ VPS05（冷链仅新购）→ TIS05（乘用车报废更新）→ VPS03（乘用车置换更新）→ TIS06（公交车）。

### 2. 绿电交易与绿证单独交易（无需修正）

**事实核验**：建议要求「两个独立 Instrument：Green electricity trading（Extended）与 Renewable energy certificate trading（Direct match）」——数据集现状已完全满足：CHNTRAGETI01S000（绿色电力交易机制，交易机制/绿色电力交易，Extended）与 CHNTRARECI01S000（可再生能源绿色电力证书市场，交易机制/可交易可再生能源证书/配额/RPS，Direct match）均为独立工具行，两行描述已注明并行关系与区别（2026-11-18 终审确认）。路径名维持「可交易可再生能源证书/配额/RPS」与「绿色电力交易」，不按建议新增第三路径（现有 REC 路径已覆盖绿证单独交易）。

### 3. 需求响应两项修正（采纳；DRC 路径定义保留）

**事实核验**：建议的实质判断成立。《电力需求侧管理办法（2023年版）》（发改运行规〔2023〕1283号）第 19 条规定的是需求响应价格机制（谁提供、谁获利，谁受益、谁承担，按市场规则获取收益），并非政府向参与者直接支付补贴；第 47 条允许地方安排资金支持，但未设立全国统一的需求响应财政补偿制度。国家层面「需求响应补偿补贴」工具缺乏制度依据，属误建。

**执行**：

1. **删除** CHNSUBDRCI01S000（经济类补贴），证据日志该 ID 7 行删除并补 1 行删除裁决记录。
2. **迁移** CHNTRADRMI01S000 → CHNFRMDRMI01S000（框架性规制），路径更名为 需求响应市场参与规则 / **Demand response market participation rules**（采纳建议的 Rules 后缀），IFCMA 对照为电力市场规制类（electricity market regulations），不再作为交易机制下的 CCPID 特有扩展路径。新描述覆盖第 16/19/20/47 条：市场参与规则为主体；第 19 条价格机制与市场收益安排、第 47 条地方财政支持作为政策背景说明，并明确「国家层面不另设需求响应财政补贴工具」。
3. **路径定义调整**：DRM 路径定义自交易机制移至框架性规制（绿电直连之后）；DRC 路径定义**保留**于 Approaches 表（与建议「删除 Approaches 中的 Demand response compensation」的偏差），定义为地方层面可能存在的需求响应财政补偿机制，并注明「国家层面未设立全国统一的财政补偿制度，故国家层面数据库暂不收录该路径下的工具」——保留理由：Approaches 表为机制类型词表，省级补偿政策（如各省需求响应补贴）真实存在，保留路径定义可为后续地方层面扩展预留分类位置，删除则需未来重新增补词表。

**取代**：本裁决取代 further_revision_decisions_20261119.md P1-9（原裁决保留两项分类）及 structural_review_decisions_20261124.md 第 3 项（原裁决「正确，无需修正」）。

### 4. DPV 名称优化（采纳）

**事实核验**：现行英文路径名 "Distributed solar PV development and construction management" 语法欠自然且未体现电网接入与运行管理；建议名 "Distributed solar PV project development and grid-integration rules" 更准确。

**执行**：

1. EN 路径名改为 **Distributed solar PV project development and grid-integration rules**（approaches_cn.md、schema.yaml、CHNFRMDPVI01S000 行的 Approach 字段、generator pin 四处同步）；CN 路径名维持「分布式光伏开发建设管理」（官方规章标题）。
2. CN+EN 描述追加 CCPID 特有路径对照说明：最接近 IFCMA 框架性标准中的电力市场规制类示例（如可再生能源优先调度），但该制度规制项目开发建设环节，而非可再生能源电力的调度和消纳（取代 structural_review_decisions_20261124.md 第 4 项原注文）。
3. 英文工具名称（English instrument name）维持现行官方规章译名体系（Distributed solar PV development and construction management），不整体改为建议的法律文件译名——与库内其他法律文件名称处理惯例一致，法律文件官方译名已载于 Legal statute 字段。

### 5. MEPS 细分与映射（维持现状）

**事实核验**：5A（保留 electric equipment 而非 appliances）与 5B（不设笼统的 heating systems）与数据集现状一致——11 个 MEPS 路径细分方式即为建议所认可的结构，无需改动。

5C（映射优化）：建议对同时涵盖燃气/太阳能/电气产品的标准优先引用更宽泛的 appliances 类示例、对工业热工设备避免强行映射至 electric equipment。**维持 2026-11-19 裁决**（revision_suggestions_decisions_20261119.md 条目 4）：IFCMA 引用词表中无通用的「MEPS for appliances」独立项，其 Table 1 示例为 "Minimum energy performance standard for appliances, buildings, etc."，无法作为精确引用目标；MEC/MWH/MIT 三个路径维持 Extended → MEPS for electric equipment（Extended 状态本身即表达「非完全等同、具有可识别的共同机制基础」的限定），不强行改为 CCPID-specific。与 structural_review_decisions_20261124.md 第 5 项一致。

## 三、取代声明

1. **取代** `further_revision_decisions_20261119.md` P1-9：需求响应两项分类裁决由「保留两项」改为「删除 DRC、DRM 转框架性规制」。
2. **取代** `structural_review_decisions_20261124.md` 第 1 项：货车补贴由「不合并、维持两工具」改为「报废并新购转 TIS、仅新购独立成 VPS 工具、父工具拆分」。
3. **取代** `structural_review_decisions_20261124.md` 第 3 项：由「正确、无需修正」改为「实质性修正」。
4. **取代** `structural_review_decisions_20261124.md` 第 4 项执行细节：DPV 路径 EN 名变更，IFCMA 对照说明文本更新。
5. `structural_review_decisions_20261124.md` 第 2、5 项维持有效，不取代。

## 四、执行清单

- `outputs/CCPID_cn_economic_instruments.csv` / `CCPID_en_economic_instruments.csv`：车辆补贴块重组（TIS04 新建、VPS05 新建、TIS05/TIS06 迁移、旧 VPS01S000/S001/S002 删除、VSS 交叉引用更新）；CHNSUBDRCI01S000、CHNTRADRMI01S000 删除。
- `outputs/CCPID_cn_regulatory_instruments.csv` / `CCPID_en_regulatory_instruments.csv`：新增 CHNFRMDRMI01S000；CHNFRMDPVI01S000 的 EN Approach 字段更名、CN+EN 描述追加对照说明。
- `rules/schema.yaml`：DRM 自交易机制依赖表移除、加入框架性标准（GPC 之后）；DPV 路径 EN 名更新；DRC 定义更新（保留）。
- `inputs/classification/approaches_cn.md`：DRM 路径行移至框架性规制并更名；DRC 定义修订（保留，注明国家层面不收录）；DPV EN 名更新 + 特有路径说明。
- `scripts/generate_english_from_chinese.py`：删除 5 个废弃 pin（VPS01S000/VPS02S000/VPS04S000/TRADRMI01S000/SUBDRCI01S000），新增 5 个 pin（TIS04/VPS05/TIS05/TIS06/FRMDRM），更新 DPV pin。
- `outputs/evidence_log.csv`：ID 重指（VPS01S000→TIS04 ×50、VPS02S000→TIS05 ×50、VPS04S000→TIS06 ×52、TRADRMI01S000→FRMDRM ×7）；删除 SUBDRCI01S000 ×7；DPV 描述/Description 两行更新为本记录条目 4；追加 6 行裁决记录（条目 1 四行、条目 3 两行）。
- EN TIS05/TIS06 行同步刷新 2025-2026 版内容（2026 年实施细则：商办消费函2025年第467号 12%/10% 比例补贴；交办运〔2026〕28号 公交 8 万元/辆、电池 4.2 万元/辆，车龄阈值放宽至 2018 年底前注册）。
