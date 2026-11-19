# CCPID 修订建议（桌面版）裁决记录

审查依据：`c:\Users\admin\OneDrive - pku.edu.cn\桌面\revision suggestions.docx`（编号 2–7 共 7 条；**文档中第 1 条缺失**，已向用户提示确认）
裁决日期：2026-11-19
总体原则：沿用「不要再增加字段」约束；本批建议均不涉及新增字段，全部在现有结构内处理。

## 一、裁决总览

| # | 建议 | 裁决 | 实施方式 |
|---|---|---|---|
| 2 | End date 定义 + Status 公式 + 补充 7 条终止日期 | 采纳（三项全采纳） | 定义改为 CCPID 口径；公式 `TODAY()<=End date`；7 条日期按描述所载有效期填入，另补 2 条同类遗漏 |
| 3A | 碳减排支持工具 Indirect→Direct | 采纳 | CN/EN 同步 + pins + 证据日志 |
| 3B | 企业绿色采购指南 Direct→Indirect | 采纳 | 同上（路径定义已为 indirect，改工具行后 Approaches 表自动一致） |
| 3C | 25 条「目标含减缓气候变化 + 相关性间接」人工检查 | 部分采纳 | 抽查结论：除 3A 外均维持（多目标政策属正常）；建立清单留档 |
| 4 | 6 处 IFCMA crosswalk 修正 + 3 个 MEPS 检查 + 总体原则 | 采纳（6 处修正，3 个 MEPS 维持） | TIS/MPS→Extended→Subsidies（沿用先例）；EIL/EPR/VPG→CCPID-specific；VLB→Extended（保留引用）；总体原则写入分类结构规则 6 |
| 5 | 差别电价 Adoption date 补充 + 精度规则说明 | 采纳 | EN N/A→01/06/2004（与 CN 对齐，pin）；数据字典增加月份精度惯例 |
| 6 | Summary 文案补 Cross-sectoral | 采纳 | EN/CN 模板概览第 6 行文案 |
| 7 | Jurisdiction level 统一 | 采纳 | EN 统一 National / Sub-national（与属性定义页一致）；schema + 结构性翻译 + pins；CN 维持现状并补注定义 |

## 二、逐条裁决与理由

### 2. End date 定义与 Status 计算逻辑（采纳）

**事实核验**：三项全部属实。

1. 定义不一致：EN 模板 Attributes definitions、CN 属性定义、field_dictionary.md、schema.yaml 的 End date 均沿用 IFCMA 定义「Date when the final requirement of the legal mandate takes effect, if relevant」，但数据集实际使用（24 条已有终止日期、自动状态脚本）均将其作为政策最后有效日。确认。
2. 公式边界误差：`scripts/export_workbooks.py` 的 `_apply_status_formulas()` 末级判断为 `TODAY()<DATE(...End...)`，结束日当天即显示 Ended/已终止；而 `scripts/update_status_from_dates.py` 用 `end_date < today`（结束日当天仍为 in force）。公式比脚本提前一天翻转，两机制不一致。确认。开始日期侧两处一致（`TODAY()<Start`→Scheduled，开始日当天即转入生效，与脚本 `start <= today` 一致），无需修改。已终止表写入静态值不经公式，不受影响。
3. 7 条记录终止日期为 N/A，且描述/法律文件均载明期限，建议日期全部核对无误：
   - 绿色电力交易（CHNTRAGETI01S000）：电力中长期市场基本规则（发改能源规〔2025〕1656号）2026-03-01 生效、有效期 5 年 → **28/02/2031** ✓
   - 需求响应市场参与/补偿（CHNTRADRMI01S000、CHNSUBDRCI01S000）：电力需求侧管理办法（2023年版）2023-10-01 生效、有效期 5 年 → **30/09/2028** ✓
   - 分布式光伏开发建设管理（CHNFRMDPVI01S000）：国能发新能规〔2025〕7号 2025-01-23 生效、有效期 5 年 → **22/01/2030** ✓
   - 船舶碳强度管理 / 船舶能耗数据报告（CHNPRFSCMI01S000、CHNREPSECI01S000）：海危防〔2022〕164号 2022-12-22 生效、有效期 5 年 → **21/12/2027** ✓
   - 政府采购支持公路绿色低碳发展试点（CHNPPCGPPI06S000）：财库〔2025〕32号，试点 3 年、2028-12-31 前完成验收 → **31/12/2028** ✓（描述原文即载明）

**补充扫描**（回应「至少七条」）：全文检索「有效期 5 年」且终止日期为 N/A 的行，另发现 2 条同类遗漏，一并采纳填入：
- 节能降碳中央预算内投资专项管理办法（CHNPIVCBII02S000）：发改环资规〔2025〕1228号 2025-09-19 印发施行、有效期 5 年 → **18/09/2030**
- 生态保护修复领域中央预算内投资专项管理办法（CHNPIVCBII05S000）：发改农经〔2026〕713号 2026-05-21 印发施行、有效期 5 年 → **20/05/2031**
- 民用建筑能效测评标识（CHNCELELBI01S000）描述中「有效期 5 年」指测评标识证书有效期而非制度有效期，**不填**。

**实施方式**：
1. `export_workbooks.py` 中英两套公式模板末级 `TODAY()<DATE(...)` → `TODAY()<=DATE(...)`，同步更新函数 docstring。
2. End date 定义改为「The last date on which the policy instrument remains in force, where applicable.」（CN：政策工具保持生效的最后一天（如适用）。），同步四处：EN 模板 Attributes definitions、CN 模板属性定义、field_dictionary.md、schema.yaml dates.rules（inputs/attribute definitions.xlsx 若含旧文本一并更新）。
3. 数据：CN 9 行终止日期填入；EN 经 pins 同步；证据日志逐行追加。填入后无任何状态立即翻转（日期均为未来）。

### 3. Mitigation relevance 两处修正（A、B 采纳；C 部分采纳）

**3A 碳减排支持工具（CHNSUBCLGI02S000）**。事实核验：当前 Indirect（CN 间接），目标含「减缓气候变化」，证据引文为人民银行创设工具引导金融机构向碳减排重点领域提供碳减排贷款。按 CCPID 定义（直接＝明确旨在减少或清除温室气体排放），人民银行创设碳减排支持工具以碳减排为明确政策目的（人民银行公告及货币政策执行报告均有记载）。**采纳**：间接→直接（CN 间接→直接，EN Indirect→Direct，pins + 证据日志）。

**3B 企业绿色采购指南（CHNVIIVPGI01S000）**。事实核验：当前 Direct（CN 直接），目标仅「绿色消费」；路径定义（approaches_cn.md / approaches_en.md）已写明「Mitigation relevance is generally indirect」。工具行与路径定义不一致，且工具本身目标确为绿色消费与资源节约。**采纳**：直接→间接（同上实施）；Approaches 表「减缓相关性」列由工具行数据汇总生成，改工具行后自动一致。

**3C 25 条一致性检查**。事实核验：「25 条」数字确认无误（清单见附录）。**部分采纳**：按建议分组抽查结论——价格机制（分时电价、两部制热价）间接合理；产业政策（产能置换、错峰生产、生态保护类）间接合理；公共投资（RDD05 储能与智能电网、RDD06 循环经济关键技术）技术方向并非直接减排目的，维持间接。本轮除 3A 外不改动其余 24 条；「目标含减缓气候变化且相关性为间接」属多目标政策的正常情形，不建立机械规则。另记录观察项（本轮不做）：能力建设组内 Direct×15 与路径定义「通常为间接」、RDD/CBI 组内 Direct/Indirect 混用，留待后续专项核查。

### 4. IFCMA crosswalk 映射修正（采纳）

**事实核验**：6 行现状与文档所述完全一致（approaches_en.md 为唯一数据源，中英文 Approaches 表的 IFCMA 两列由其生成；CN 表无此两列）。表中已有以通用「Subsidies」作 Extended 引用的先例（CCD、LFF、CHS、RTS、DRC 共 5 条）；IFCMA 引用词表中无通用「Performance standards」项。

| CCPID 路径 | 现状 | 裁决 |
|---|---|---|
| 15 Trade-in subsidy | Extended → Electric vehicle purchase subsidies | **Extended → Subsidies**（机制共同基础：以淘汰旧资产并购置低碳替代品为条件的财政支付，与资产类别无关；沿用通用 Subsidies 引用先例） |
| 18 Low-emission machinery purchase subsidy | Extended → Electric vehicle purchase subsidies | **Extended → Subsidies**（同上；非道路机械不属于电动汽车） |
| 52 Energy intensity limit for industrial production | Extended → MEPS for electric equipment | **CCPID-specific**（单位产品能耗限额是工业生产过程强度限额，与设备出售/分销环节的 MEPS 不同源；IFCMA 词表无可对应的通用绩效标准项） |
| 62 Extended producer responsibility | Extended → Environmental permitting process | **CCPID-specific**（生产者全生命周期责任制度，非环境许可制度） |
| 105 Voluntary procurement guidance | Extended → Voluntary reporting standards | **CCPID-specific**（自愿性企业采购指南非披露/报告标准；IFCMA 的 Green public procurement rules 针对强制性公共采购，不适用） |
| 106 Voluntary certification and labelling scheme | Direct match → Voluntary energy efficiency labels | **Extended → Voluntary energy efficiency labels**（保留引用、降级状态：覆盖绿色债券标签、SLB、碳足迹、零碳工厂等，超出能效标签范围，不宜全部标 Direct match） |

**三个 MEPS 路径核查结论**（烹饪系统 MEC、热水系统 MWH、工业热工设备 MIT，现均为 Extended → MEPS for electric equipment）：**维持不变**。三者与电气设备 MEPS 机制同源（设备出售或分销前的最低能效标准），仅资产类别细分（燃气灶具、太阳能/燃气/电热水器、燃气或燃油工业加热设备）；Extended 状态已表达「非完全等同」限定，不构成勉强匹配。与 EIL 的区别在于 EIL 根本不是设备能效标准。

**总体原则采纳**：写入 classification structure.md 混合机制条款第 6 条——「不得为每个 CCPID 路径勉强寻找 IFCMA 对应；无充分准确对应时使用 CCPID-specific approach」。实施范围仅 approaches_en.md（数据）+ classification structure.md（规则）。

### 5. 差别电价 Adoption date（采纳）

**事实核验**：CHNADPIDPI01S000 中文通过日期已为 01/06/2004（与生效日期相同），英文 Adoption date 为 N/A——问题实为生成链丢失（该行无 pin 覆盖，沿用旧 EN 值 N/A），非数据整体缺失。描述记载 2004 年由国家发改委发起，发改价格〔2004〕703号为 2004 年 6 月文件；官方资料仅精确到月份。

**实施方式**：
1. EN Adoption date 经 pin 补为 01/06/2004，与 CN 对齐（格式仍为 dd/mm/yyyy，不引入「06/2004」非规范格式）。
2. 精度惯例写入 field_dictionary.md 与 schema.yaml 日期规则：「当官方来源仅精确到月份时，以该月首日作为代表值（精度处理规则，非已核实生效日），并在证据日志注明」；CN 属性定义通过日期说明同步补注。

### 6. Summary 文案补 Cross-sectoral（采纳）

**事实核验**：EN Summary 第 6 行「Sectors covered: Energy, transport, buildings, industry, AFOLU, waste」缺 Cross-sectoral；CN 概览第 6 行「覆盖部门：能源；交通；建筑；工业；农业、林业和其他土地利用；废弃物」缺跨部门。统计表本身已含该行（20261119 轮已核查）；网页文案亦已于 20261119 轮补齐。

**实施方式**：EN 改为「Energy, Industry, Buildings, Transport, AFOLU, Waste and Cross-sectoral.」（采纳建议文本，统一首字母大写）；CN 改为「能源；工业；建筑；交通；农业、林业和其他土地利用；废弃物；跨部门」。修改 EN/CN 模板后重跑管线同步 outputs 与 docs。

### 7. Jurisdiction level 统一（采纳）

**事实核验**：EN 侧 285 条 national / 38 条 National / 4 条 Subnational（无连字符），确认混用。来源：生成器结构性翻译 `国家→national、省级/县级/城市级→subnational`，部分行 pin 为大写 National/Subnational。而 EN 属性定义页已写「National; Sub-national; Supra-national; Special economic zone」——数据与定义不一致。schema 规范值为小写。

**实施方式**：
1. EN 数据统一为 National / Sub-national：结构性翻译表改为 `国家→National、省级/县级/城市级→Sub-national`；pins 中显式出现的 national/National/Subnational 键值同步为规范值（含已终止 CSV 1 行）。
2. schema.yaml Jurisdiction level 规范值同步为 National / Sub-national / Supra-national / Special economic zone (SEZ)（后两者当前无数据使用，一并统一大小写保持词表一致）。
3. CN 侧维持现状（国家/省级/县级/城市级，信息粒度高于定义的「次国家级」）；CN 属性定义允许值补注「次国家级（省级、县级、城市级）」以消除定义与数据的表述差距。

## 三、执行顺序

1. export_workbooks.py 公式修正 + End date 定义四处同步（条目 2 第一、二项）
2. 数据：9 条终止日期（CN + EN pins）+ Adoption date pin + 精度惯例文档 + 证据日志（条目 2 第三项、条目 5）
3. 减缓相关性 2 行（CN/EN + pins）+ 证据日志（条目 3A、3B）
4. approaches_en.md 6 处 crosswalk + 分类结构规则第 6 条补充（条目 4）
5. Summary 文案 EN/CN 模板（条目 6）；管辖层级结构性翻译 + pins + schema + CN 定义补注（条目 7）
6. 全量管线 run_pipeline.py 6/6，同步 docs 工作簿与网页

## 附录：25 条「Objective 含 Climate change mitigation 且 Mitigation relevance = Indirect」清单

CHNSUBCLGI02S000（本轮改 Direct）、CHNSUBESPI02S000、CHNTAXVATI02S000、CHNTAXVATI03S000、CHNTAXCTII01S000、CHNTRADRMI01S000、CHNSUBDRCI01S000、CHNADPTOUI01S000、CHNADPTPTI01S000、CHNSUBESPI06S000、CHNPIVRDDI05S000、CHNPIVRDDI06S000、CHNREPSECI01S000、CHNFRMCAPI01S000、CHNFRMGFGI01S000、CHNFRMPSMI01S000、CHNFRMECMI01S000、CHNFRMECMI02S000、CHNFRMECMI03S000、CHNFRMSPPI01S000、CHNVIIVLBI02S000、CHNVIIVBRI02S000、CHNVIIVLBI05S000、CHNVIIVLBI08S000、CHNVIIVLBI09S000
