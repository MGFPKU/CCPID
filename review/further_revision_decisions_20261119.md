# CCPID 数据集进一步修改建议（2026-11-19）裁决记录

审查依据：`d:\下载\CCPID_数据集进一步修改建议_20261119.docx`（共 12 条建议 + 技术/编辑检查）
裁决日期：2026-11-19
总体原则：用户指令「不要再增加字段」——所有建议新增字段的方案一律不采纳，以现有结构内的说明、描述或定义完善替代。

## 一、裁决总览

| # | 建议 | 裁决 | 实施方式 |
|---|---|---|---|
| P0-1 | 修正 Approaches 表工具数量统计 | 部分采纳 | 数量修正采纳；「Number of sub-schemes」新字段不采纳 |
| P0-2 | 统一 Attributes definitions 与字段名 | 采纳 | 表头统一为 schema 规范名；定义更新；拼写全面校对（含 CN） |
| P0-3 | 清理 Mitigation effect 取值 | 采纳 | 以中文为准对齐英文：小写→规范大写；N/A→按中文判定；环保税→Unknown |
| P0-4 | 明确 GHG emission coverage 口径 | 部分采纳 | 方案 B（拆字段）不采纳；方案 A 改名不采纳；采纳口径精神——定义中注明参考性、非严格可比 |
| P0-5 | 补充 Evidence rationale、关闭待核验 | 部分采纳 | 新字段不采纳（理由在描述+证据日志中）；关闭黑土地补助、生活垃圾分类两项待核验（已核实来源） |
| P1-6 | 放宽 Instrument 定义、调整 Approach 定义 | 采纳 | 采纳建议文本（中英文），同步分类结构文档与工作簿分类框架表 |
| P1-7 | IFCMA crosswalk 方法学说明 | 采纳 | Approaches 表数据行下追加三种状态定义 + Extended 说明（中英文） |
| P1-8 | 规范 Policy Package 字段 | 采纳 | 数据侧清理：仅保留真实上位政策包；单部法律法规/税制名/工具自身名/工具交叉引用 → N/A 或移入描述 |
| P1-9 | 复核 Demand response 两项分类 | 部分采纳 | 保留现有分类，补充说明：DRM 为 CCPID 对电力市场机制的扩展；DRC 资金来源核实为财政资金 |
| P1-10 | 复核双控制度主体边界 | 部分采纳 | 保留 FRM/目标责任体系，明确主要受规制主体与核心机制，补与 CHNPARCPAI01S000 的交叉引用 |
| P1-11 | Capacity pricing 母工具 Mitigation effect | 采纳 | 母工具 正向→未知；通用规则写入分类结构文档 |
| P2-12 | 增加 Implementation coverage 字段 | 不采纳 | 不新增字段；实施范围信息已记录在描述/受规制主体（详情）中 |
| 技术 | Status TODAY() 公式静态化 | 部分采纳 | 保留动态公式；封面注明计算基准日与动态计算说明；静态数值版暂缓（发布时另存生成） |
| 编辑 | 网页 Sectors covered 遗漏 Cross-sectoral | 采纳 | 工作簿 Summary/概览已含该行（核查无误）；实际遗漏在网页 scope 文案，已补 |
| 编辑 | Emission sector 大小写、Objective 词表漂移、CF4/C2F6 层级、拼写 | 采纳 | 数据与定义双侧修正（Objective 不扩充词表，以中文受控词表为准修正英文漂移值） |

## 二、逐条裁决与理由

### P0-1 修正 Approaches 表中的工具数量统计

**事实核验**：确认。`scripts/export_workbooks.py` 的 `write_approaches_sheet()` 未过滤子方案行，将 Sub-scheme 计入 Number of instruments（Instruments overview 表已有正确过滤）。109 条 Approach 合计 336 = 297 工具 + 39 子方案，与建议表格完全一致（ETS 5→1、TPS 3→1、Offset credits 19→1、VPS 6→4、ESP 8→6、VOTI 3→1、CPM 5→1、MWS 2→1、VLB 11→9、VBR 5→3）。

- **采纳**：过滤子方案行，Number of instruments 仅计 Instrument。
- **不采纳**：另增 Number of sub-schemes 字段（用户指令不新增字段）。子方案数量已可在数据表中直接统计。

### P0-2 统一 Attributes definitions 与实际数据结构

**事实核验**：确认。EN 模板表头混用 `Mitigation effects`（经济、规制）/`Mitigation effect`（政府、信息、自愿）、`Last revisions`/`Last revision`；Attributes definitions 存在过期定义（Instrument name 仍称 "Preliminary IFCMA harmonised instrument name"；Emission sector 仍列 Agriculture/LULUCF）；拼写问题 Categorial（约 40 处）、Aministrating、Catgorial、Numerial、detao;s、treshhold、housholds、subsidyor、enginge、build。CN 属性定义的目标词表缺 生物多样性保护、自然资源保护 两项。

- **采纳**，实施：
  1. EN 模板表头统一为 schema 规范名：`Mitigation effect`、`Last revision`、`Last revision (Details)`；`Administrating authorities` 保持一致（定义页 Aministrating authority → Administrating authorities）。同步 generator 的字段映射与约 650 处 ROW_TRANSLATIONS 键名。
  2. 定义更新：Instrument name 按现行四级结构重定义；Emission sector 定义与实际取值一致（Energy; Industry; Buildings; Transport; AFOLU; Waste; Cross-sectoral）；Mitigation effect 定义补齐 neutral、取值大小写统一；GHGs affected 注明 PFCs 含 CF4、C2F6。
  3. 拼写全面校对（模板 Cover、Attributes definitions；field_dictionary.md、schema.yaml 的 Categorial→Categorical）。
  4. CN 属性定义同步：目标词表补齐 19 项；排放部门、工具名称、温室气体排放覆盖定义同步更新。

### P0-3 清理 Mitigation effect 中不符合数据字典的记录

**事实核验**：确认，实际比建议所述更多。EN 侧存在 37 条小写 positive、2 条小写 unknown、23 条 N/A（CCER 母工具+18 子方案、环境影响评价、节能降碳审查、县域充换电试点、公共机构节能）。中文侧（数据基准）全部为 正向/未知，仅环保税（CHNTAXEPTI01S000）为 N/A。

- **采纳**，以中文为准逐项判定：
  - EN 小写 positive（37）→ Positive；小写 unknown（2）→ Unknown。
  - EN N/A（23）→ Positive：中文均为 正向（CCER 自愿减排市场、环评、节能降碳审查、县域充换电试点、公共机构节能的减排方向可合理判断）。
  - CHNTAXEPTI01S000（环境保护税）：应税污染物为大气/水污染物、固废、噪声，不含温室气体，减排方向无法合理判断——中文 N/A→未知，EN→Unknown。
  - 同步 generator pins（37 positive + 2 unknown + 21 N/A 值修正、结构性翻译表补 未知→Unknown、键名统一），证据日志逐行追加。

### P0-4 明确 GHG emission coverage 的统计口径

**事实核验**：确认字段内混合了年度覆盖量、累计核证减排量/交易量、碳储量等不同概念，横向不可比。

- **不采纳**：方案 B（拆分为数值/单位/基准年份/方法/来源等字段）——不新增字段。
- **不采纳**：方案 A 的字段改名（Indicative GHG Coverage）——字段名保持与 IFCMA 一致，避免跨模板/CSV/脚本的全链路改名风险。
- **采纳**（口径精神）：中英文属性定义改为「参考性、非严格可比」表述，明确数值须内联附单位与数据来源、不同概念不可横向比较；数据维持既有「数值 + 来源：」内联标注惯例。

### P0-5 补充 Evidence rationale 并关闭待核验事项

- **不采纳**：新增 Mitigation relevance rationale 字段（不新增字段）。纳入理由与作用机制说明已存在于各行描述及证据日志 evidence_quote 中。
- **采纳**：关闭两项待核验。
  1. 黑土地保护性耕作补助（CHNSUBESPI06S000，补贴：限额）——已核实《东北黑土地保护性耕作行动计划（2026-2030年）》（农办机〔2026〕4号）及吉林省实施方案（吉农机发〔2026〕1号，部分覆盖≤50元/亩、大量覆盖≤80元/亩、叠加作业15-25元/亩）、黑龙江省财政下达文件（黑财指（农）〔2026〕243号），与记录费率一致。关闭标志并将 2026 行动计划补入法律文件名称。
  2. 生活垃圾分类（CHNFRMMWSI01S000 描述、S001 强度（详情））——已核实生态环境法典（主席令第70号，2026-08-15施行）第499-515条：第499条确立分类制度与原则、第506条规定分类投放义务、第514条厨余垃圾无害化处理、第1174条罚则。描述微调（投放义务引第506条；个人罚款金额按法典规定表述），关闭标志。
  - 其余 needs_human_review 行不在本建议范围内，维持原状。

### P1-6 适当放宽 Instrument 的定义

**采纳**。Level 4 Instrument 定义改为建议文本（"A specific policy measure, programme, scheme or rule implemented by public authorities in a jurisdiction at a given time, through which governments influence behaviour by imposing obligations, providing incentives or services, allocating resources, or providing information."）；Level 3 Approach 定义改为 "A standardised policy approach that groups instruments with similar operating mechanisms and policy design features, providing a basis for international comparison."。同步：classification structure.md、工作簿 Classification framework 表（中英文模板）。

### P1-7 为 IFCMA crosswalk 增加方法学说明

**采纳**。在 Approaches 表数据行下方追加三种状态定义（Direct match / Extended approach / CCPID-specific approach）及「Extended 不代表两类完全等同，而是具有可识别的共同机制基础」说明（中英文，export_workbooks.py 生成时写入）。

### P1-8 规范 Policy Package 字段

**事实核验**：确认三类混用——单部法律（环评法）、其他工具（公共机构能源统计、绿色采购）、工具自身名称（草原奖补、农机补贴、领跑者制度等）与税制名称（企业所得税优惠政策体系、消费税制度、环境保护税法体系、车船税制度）。属性定义本身已规定「仅记录上位政策包、排除横向联系」，数据未遵守。

- **采纳**（数据侧，规则与定义一致）：
  - 仅保留真实上位政策包：碳达峰碳中和 1+N 政策体系、加快构建碳排放双控制度体系工作方案、新能源汽车产业发展规划、氢能产业发展中长期规划、十四五系列规划、大规模设备更新和消费品以旧换新（统一命名变体）、北方地区冬季清洁取暖规划等。
  - 单部法律法规 → N/A（已在法律文件名称中记录）。
  - 其他工具交叉引用 → 移入描述（不新增字段；需求响应、船舶能耗两对工具的交叉引用已在描述中）。
  - 工具自身名称、税制名称 → N/A。
  - 同步 EN Policy Package、generator pins、证据日志（约 35 行）。

### P1-9 复核 Demand response 两项工具的分类

**核验结论**（依据《电力需求侧管理办法（2023年版）》发改运行规〔2023〕1283号第16、19、20、47条）：

1. DRM（CHNTRADRMI01S000，交易机制/需求响应市场参与）——**保留**。核心机制为需求侧资源以容量/电量形式参与电能量、辅助服务、容量市场交易并按市场规则结算，涉及实际的需求响应交易，属 CCPID 对中国电力市场机制的扩展。按建议要求补充说明：在 approaches 定义与工具描述中注明「CCPID-specific 扩展，不直接对应 IFCMA 许可证或证书交易」。
2. DRC（CHNSUBDRCI01S000，补贴/需求响应补偿）——**保留**。补偿资金来源核实：办法第19、47条明确地方可安排财政资金对参与用户给予支持，属财政资金向非政府主体的支付，符合 IFCMA Subsidies 定义；描述中补注资金来源依据。如需细化不同省份资金渠道差异，可在后续版本以子方案区分（本轮不做）。

### P1-10 复核 Target responsibility system 中政府与企业的分类边界

**核验结论**：CHNFRMTRSI01S000（能耗双控）、CHNFRMTRSI02S000（碳排放双控）为框架性规制/目标责任体系，受规制主体 企业；政府。核心机制为目标分解+考核：国务院向省级政府分解总量/强度目标并考核问责（政府侧义务），同时通过重点用能单位等向企业传导用能/排放约束（企业侧义务）。政府侧考核已有独立工具收录（CHNPARCPAI01S000 碳达峰碳中和综合评价考核办法，公共评估规则/气候绩效评估考核，主体=政府）。

- **部分采纳**：保留 FRM/目标责任体系分类；按建议「明确主要受规制主体和核心运行机制」——更新两行受规制主体（详情）与描述，说明省级政府目标考核为主体义务、企业目标责任为传导义务，并补与 CHNPARCPAI01S000 的交叉引用。证据日志追加记录。

### P1-11 复核 Capacity pricing mechanism 的母工具 Mitigation effect

**采纳**。CHNADPCPMI01S000（发电侧容量电价机制）减缓效果 正向→未知（煤电/气电子方案为未知、储能/抽蓄子方案为正向，母工具不沿用单一子方案判断）；子方案维持。通用规则写入 classification structure.md 混合机制条款：「当母工具包含减排影响方向不同或不确定的子方案时，母工具的减缓效果不应简单沿用其中某一类子方案的判断」。

### P2-12 增加 Implementation coverage 字段

**不采纳**（不新增字段）。实施范围信息已记录于描述与受规制主体（详情）（如县域充换电试点行已载明试点县范围与遴选条件）。未来如需空间分析可另行建设衍生表。

### 技术检查：Status 动态公式

- **采纳**：保留 TODAY() 动态公式；封面注明「Status 由开始/结束日期经 TODAY() 动态计算，以打开工作簿当日为基准」；封面数据日期更新为 2026-11。
- **暂缓**：静态数值版工作簿（openpyxl 不计算公式缓存值，发布时用 Excel 打开另存即可生成；记录为发布日事项）。

### 编辑检查

1. **Summary 遗漏 Cross-sectoral**：核查工作簿 Summary/概览 第24行已含 Cross-sectoral/跨部门（公式完整）——建议基于旧版印象；实际遗漏在网页 overview 的 "Sectors covered" 静态文案（generate_webpage.py `scope_sectors`），已补 跨部门/Cross-sectoral。**采纳**（网页侧）。
2. **Emission sector 大小写**：确认 3 个 EN 单元格小写（CHNTAXCITI01S000 buildings、CHNTAXCITI02/05 waste）→ Buildings/Waste。**采纳**。
3. **Objective 受控词表**：定义页词表已含全部 19 项（建议所称「定义不完整」不成立）；实际问题是 EN 侧 13 处漂移值（Energy conservation、Renewable energy development、Resource conservation、Employment and poverty reduction、Desertification control、Biodiversity conservation 等协同效益词混入目标字段）。**不扩充词表**（中文侧已合规），按中文对应规范词修正 EN 值及 pins。**部分采纳**（数据侧修正）。
4. **CF4/C2F6 与 PFCs 层级**：GHGs affected 定义注明「PFCs（如 CF4、C2F6）」层级关系（中英文）。**采纳**。
5. **Policy Package 名称不统一**：并入 P1-8。
6. **拼写错误**：incorportating、faciliate（封面简介）、Categorial、Aministrating 等（定义页与文档）全面校对。**采纳**。

## 三、执行顺序

1. P0-1 数量修正、P1-7 图例（export_workbooks.py）
2. P0-2 表头统一 + 定义更新 + 拼写校对（模板 ×2、generator、文档）
3. P0-3 + P1-11 减缓效果清理（CN/EN CSV、pins、证据日志）
4. P1-8 政策包清理、P1-9/P1-10 描述补充、P0-5 关闭待核验（CSV、pins、证据日志）
5. P1-6 定义文本、P0-4 口径定义、编辑项（文档、模板、网页脚本）
6. 全量管线 run_pipeline.py 6/6，同步 docs 工作簿
