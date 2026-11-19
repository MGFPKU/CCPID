# Final Comprehensive Review Recommendations — Decision Record

Date: 2026-11-18
Source document: `CCPID_Final_Recommendations_Comprehensive_Review_20261117.docx` (external reviewer: completeness, inclusion scope, and classification methodology)
Review basis: 2026-11-17 pre-revision workbook (`CCPID_en(1).xlsx`), IFCMA paper, `rules/schema.yaml`, current CN/EN data (post 26-item revision).

Verdict legend: 已实施 (already implemented in the 26-item revision) / 采纳 (adopt, action needed) / 部分采纳 (partial) / 不采纳 (reject) / 待裁定 (user decision needed) / 维持原裁决 (maintain prior partial-adopt verdict).

---

## 一、最终方法学口径

| # | Rule | Verdict | Notes |
|---|---|---|---|
| 1 | Inclusion based on GHG-affecting potential, not name/authority/objective | 已实施 | CLAUDE.md mixed-mechanism rules; schema has mitigation relevance |
| 2 | Direct/Indirect describes linkage path; keep separate from Mitigation effects | 已实施 | 减缓相关性 (Direct/Indirect) and 减缓效果/Mitigation effect are separate fields in all templates |
| 3 | Mark effects Positive/Negative/Neutral/Unknown | 已实施 | Schema allowed_values: positive/negative/neutral/unknown (正向/负向/中性/未知). Correction 2026-11-18: earlier adjudication wrongly treated this as a missing field |
| 4 | Pollution/transport/circularity/ecology/product standards/public investment → Indirect inclusion | 已实施 | All Section 四 instruments retained with Indirect |
| 5 | No automatic inclusion of all green policies; distant paths → mark for verification | 已实施 | Line added as item 7 in inputs/classification/classification structure.md; consistent with needs_human_review |
| 6 | National pilot ≠ local policy; separate issuing level from implementation coverage | 部分采纳 | Issuing level exists (Jurisdiction level = National); coverage via description first |
| 7 | Distinguish Policy package / Instrument / Subscheme | 已实施 | #26 codified in methodology; CLAUDE.md has splitting rules |

## 二、对现有分类的最终修改建议（21 项）

All items already adjudicated and implemented in the 26-item revision (20261117 decision record), except where noted:

| Item | Verdict |
|---|---|
| CCER → Trading/Offset credits | 已实施 (#1; CHNVTSVCMI→CHNTRAOFCI01S000–S018, 19 rows) |
| Construction EIA → Regulatory/Framework | 已实施 (#2; →CHNFRMEIAI01S000; approach name kept as EIA rather than "Environmental permitting and project assessment" — same substance) |
| Planning EIA stays Government I&C | 已实施 (kept in PAR, distinct from construction EIA) |
| Energy-and-carbon review → Regulatory | 已实施 (#3; →CHNFRMECRI01S000) |
| Environmental compliance audit → Information/Reporting | 已实施 (#4; →CHNREPEARI01S000, approach renamed Environmental auditing requirements — matches doc exactly) |
| Public-institution energy framework → Government I&C | 已实施 (#5; →CHNPAREPMI01S000, Policy Package field links statistics/audit and green procurement) |
| TRS03/CPA01 suspected duplicate | 已实施 (#6 verified same document "5+9" indicators, 12/04/2026; merged into CHNPARCPAI01S000, deleted FRMTRSI03) |
| Electric-motor MEPS → Performance standards | 已实施 (#7; →CHNPRFMEMI01–03) |
| County EV charging pilot | 已实施, stronger than suggested (#8 verified 财建〔2024〕57号: funds form public fixed capital, explicitly barred from vehicle subsidies → wholly Public investment, CHNPIVCBII06S000; supersedes doc's "verify boundary" suggestion) |
| Green factory programme → Voluntary benchmarking | 已实施 (#9; →CHNVIIVBRI01S000, new VBR approach) |
| Green power direct connection split from RPD | 已实施 (#10; new GPC approach → CHNFRMGPCI01S000, RPD definition narrowed) |
| RECI03 split power/non-power | 已实施 (#11; power → CHNTRARECI04S000 Trading/REC; non-power → CHNPRFRCPI01S000 Performance/RCP — matches doc) |
| GB 55015 full clause split | 维持原裁决 (#12 partial: reclassified to FRM/CBC → CHNFRMCBCI01S000 with comprehensive nature stated; full clause-level split deferred as long-term improvement, not executed) |
| Vehicle purchase subsidy / Trade-in overlap | 已实施 (#13; VPS definition de-scoped, new Vehicle scrappage subsidy approach, VPS01 subschemes) |
| CLG four-mechanism mix | 已实施 (#14 partial: CLGI03→Interest subsidy, CLGI01→Central bank lending support, CLGI02 stays; CDM Fund NOT split four ways — one 办法 authorises all modes, instrument-unit principle → whole fund to Public investment CHNPIVGIFI02S000 with modes in description. Differs from doc's four-way split) |
| Eco-compensation mix | 已实施 (#15; approach narrowed to framework/governance instrument; payment/trading mechanisms filed separately via Policy Package) |
| Certification labels vs Top-Runner | 已实施 (#16; new VBR; top-runners → CHNVIIVBRI02/03; certification labels stay VLB) |
| Carbon administrator occupational standard | 已实施 (#17; approach renamed Occupational standards and skills development → CHNCBAOSSI01S000 — matches doc) |
| Green standard system → policy package | 维持原裁决 (#18 partial: kept as Information/CBA tool with guiding/non-mandatory definition; filing principle written — specific standards filed by own legal force, preventing double counting) |
| Peak-shaving capacity by renewables enterprises | 已实施, stronger than suggested (#19 verified 发改能源〔2021〕1093号: voluntary participation + commitment-to-grid-access (假一罚二), not self-set target → new VCP approach → CHNVTGVCPI01S000) |
| Energy intensity limits vs benchmark levels | 已实施 (#20; EIL narrowed to binding limit/access values) |
| MEA/MHS names too narrow | 已实施 (#21→MEE "MEPS for electric equipment", #22→HPC "MEPS for heat pumps and water chillers"; per-equipment-type split deferred as long-term optional) |
| Administered prices plural + CPM narrowed | 已实施 (#23 CPM limited to administratively-set capacity prices, auctioned markets/reliability options removed; #24 unified pluralisation) |

## 三、应新增的 Instrument

**3.1 建议新增（11 项）** — all verified absent from the dataset; all 采纳:

| Item | Decision |
|---|---|
| 绿电交易机制 | 已实施: CHNTRAGETI01S000 — Trading systems / Green electricity trading; linked to GEC market (TRARECI01) and consumption responsibility (TRARECI02/04). Basis: 发改能源规〔2025〕1656号 |
| 分时电价 | 已实施: CHNADPTOUI01S000 — Administered prices / Time-of-use pricing. Basis: 发改价格〔2021〕1093号 (national framework; local rates not filed) |
| 分布式光伏开发建设管理 | 已实施: CHNFRMDPVI01S000 — Regulatory/Framework standards. Basis: 国能发新能规〔2025〕7号 |
| 需求响应 | 已实施 (split by mechanism, no whole-package row): compensation → CHNSUBDRCI01S000 Subsidies; market participation → CHNTRADRMI01S000 Trading systems; Policy Package links the two. Basis: 发改运行规〔2023〕1283号 |
| 煤层气排放标准 GB 21522-2024 | 已实施: CHNPRFMTLI01S000 — Performance standards / Methane emission limits; dates per earliest-predecessor convention (02/04/2008, 01/07/2008, 最近修订 01/12/2024) |
| 船舶能耗数据报告 | 已实施: CHNREPSECI01S000 — Information/Reporting requirements. Basis: 海危防〔2022〕164号 |
| 船舶碳强度管理 | 已实施: CHNPRFSCMI01S000 — Regulatory/Performance standards; Policy Package links the reporting row |
| 港口船舶岸电 | 已实施: CHNFRMSPPI01S000 — Regulatory/Framework standards; Indirect. Basis: 2019年第45号, 最近修订 2025年第2号 (13/05/2025) |
| 生活垃圾强制分类 | 已实施: CHNFRMMWSI01S000 (tool) + CHNFRMMWSI01S001 (厨余垃圾 Subscheme) — Regulatory/Framework standards / Mandatory waste sorting; Indirect, effects Unknown. Basis: 生态环境法典 (2026) arts. 499–515, 1169, 1174 |
| 能源计量 GB 17167-2025 | 已实施核实路径→采纳: independence verified → CHNFRMEMRI01S000 Regulatory/Framework standards / Energy metering requirements. Dates per earliest-predecessor convention (02/06/2006, 01/01/2007, 最近修订 24/01/2025) |
| 黑土地保护性耕作补助 | 已实施核实路径→采纳: verified as independent programme → CHNSUBESPI06S000 Subsidies / Ecosystem service payments (农机发〔2020〕2号 + 农办机〔2020〕3号; 2026 update noted in 最近修订（详情）, needs_human_review=true) |

**3.2 条件性候选（4 项）**:
- 居民阶梯气价 → 已实施核实路径→采纳: CHNADPRITI02S000 — Administered prices / Residential increasing-block tariff (发改价格〔2014〕467号, 20/03/2014); approach 路径 shared with electricity block tariff (ADPRITI01 路径 updated to 居民阶梯电价/气价)
- 供热计量两部制热价 → 已实施核实路径→采纳: CHNADPTPTI01S000 — Administered prices / Two-part heat tariff (发改价格〔2007〕1195号, 03/06/2007)
- 节能监察 → 不单独计数 (enforcement attribute of existing instruments unless independent obligations found)
- 秸秆综合利用 → 不建档 (policy list alone insufficient; avoid duplication with black-soil subsidy and existing CBI)

### 3.4 实施记录（2026-11-19）

15 rows added (7 econ, 7 reg, 1 info; CN+EN): TRAGETI01, TRADRMI01, SUBDRCI01, ADPTOUI01, ADPTPTI01, ADPRITI02, SUBESPI06, FRMDPVI01, PRFMTLI01, PRFSCMI01, FRMSPPI01, FRMMWSI01S000+S001, FRMEMRI01, REPSECI01. 12 new approach codes in schema known_codes (DRC, GET, DRM, TOU, TPT, DPV, SPP, MWS, EMR, MTL, SCM, SEC); approaches_cn.md / approaches_en.md updated; ADPRITI01 路径 → 居民阶梯电价/气价; ROW_TRANSLATIONS pins + OVERVIEW_ROW_HEIGHTS entries added; evidence log +15 entries (3 rows needs_human_review=true). EN CSVs regenerated via generate_english_from_chinese.py (also applied pending 26-item-revision pin updates: Group pluralisation + VPS01 2025 policy content). CN normalizer warnings for the new rows fixed (《》 removed from 法律文件名称, MTL "min"→分钟, MWS 合规执行→合规命令；罚款). Pipeline 6/6; 297 instruments / 109 approaches; no new validation issues.

**3.3 已收录不重复（9 项）**: all verified present — no action.

## 四、保留 Indirect 工具（15 项）

采纳 — all already retained with Indirect; no removals. Refinements:
- Railway/water transport CBI: focus descriptions on credible low-carbon transport substitution → 已实施 (CHNPIVCBII03/04 描述 refined toward low-carbon transport substitution)
- Cement peak-shifting, plastic ban, etc.: effects not assumed Positive; Unknown where evidence lacking → 采纳 (tied to 八.2)
- **SLB label (CHNVIIVLBI09S000, industry self-regulatory) → 采纳选项① (2026-11-18)**: included under a "national market self-regulation rules" scope, limited to SLBs with GHG/energy-efficiency-related KPIs/SPTs. Scope note added to CN+EN descriptions + evidence log; row stays Indirect/Positive.

## 五、政策状态与重复记录（6 项）

采纳核实要求. Common principle: **no auto-move to Ended**; keep 生效 with verification annotation until evidence confirms otherwise.

| Item | Action |
|---|---|
| 退耕还林 SUBESPI01 | 2022 halt of new enrolment ≠ ended; verify stock subsidies and stewardship funding; annotate "closed to new entry, stock implementation ongoing / under verification" |
| 天然林 SUBESPI05 | Verify 2021–2035 protection/restoration subsidy mechanism; FRMECMI01 stays as current framework; update SUBESPI05 or convert to package to avoid duplication |
| 退牧还草 SUBESPI04 | Feed-grain subsidy transferred out in 2011 must not appear as current subsidy; adjust current construction-investment part to Public investment or split historical/current mechanisms; distinguish from SUBESPI03 |
| 家电回收目标责任制 VTGVTGI01 | Verify whether 2024–2026 enterprise lists/targets continue to be published; keep 生效 pending verification |
| 生产者责任延伸 FRMEPRI01 | Independent obligations → keep as framework linked to sector tools; umbrella framework only → convert to Policy package to avoid double counting |
| 绿色制造标准体系 CBAGSSI01 | 维持原裁决 (see 二) |

## 六、国家标准状态维护

| Item | Verdict |
|---|---|
| GB 29445-2025 / PRFEILI04 | Issue confirmed, handling adjusted: doc's "Start date = 2026-08-01 + move old rows to Ended" conflicts with CLAUDE.md — (1) date convention: 通过/生效 = earliest predecessor dates (PRFEILI04 already correct: 31/12/2012, 01/10/2013, 最近修订 01/08/2025); (2) superseded standards: DELETE old-version rows, not Ended. TODO: delete PRFEILI65/66 (GB 29444-2012, GB 29445-2012, still 生效); note replacement in PRFEILI04 description |
| GB 30185-2025 / PRFEILI09 | Same: TODO delete PRFEILI62 (GB 30185-2013, still 生效); note replacement in description |
| GB 46519-2025 / PRFMEEI28 | Already satisfied — 生效, auto-flipped 01/11/2026 by date-driven pipeline |
| GB 47834-2026 / PRFMEEI29 | Already satisfied — 计划实施 until 01/01/2027 |
| GB 47835-2026 / PRFEILI69 | Already satisfied — 计划实施 until 01/01/2027 |
| GB 17167-2025 / GB 21522-2024 | See Section 三 (new-instrument decisions) |

## 七、Policy package 关联库（5 项）

采纳方向 (none counted as single instruments): 农业农村减排固碳实施方案 (AFOLU package), 甲烷排放控制行动方案 (cross-sectoral; GB 21522 filed separately), 生态环境法典 (legal framework — update legal-basis fields of specific tools), 电力需求侧管理办法 (package → split mechanisms per 三), 绿色制造标准体系建设指南 (standards framework). Implement via existing Policy package field; priority below Section 三.

## 八、数据结构（9 项）

| Item | Verdict |
|---|---|
| Mitigation relevance Direct/Indirect | 已实施 |
| Mitigation effects | 已实施 — the field already exists in all templates (减缓效果 / Mitigation effect), allowed values positive/negative/neutral/unknown. Earlier 待裁定 verdict was an error (corrected by user 2026-11-18). Data-quality pass done 2026-11-18: 错峰生产/限塑/排污许可/三线一单 marked 未知 (CN+EN + generator + evidence log) |
| Policy status edge cases | 部分采纳 — date-driven status in place; "closed to new entry / under verification" expressed via description + review_flag, no new status values (avoids breaking auto-flip) |
| Issuing level / implementation coverage | 部分采纳 — issuing level exists; coverage via description first |
| Policy package linkage | 部分采纳 — existing Policy package field already used (#5, #15); formal registry low priority |
| IFCMA crosswalk | 已实施 (#25, EN Approaches sheet two columns) |
| Approach/Group naming | 已实施 (#24) |
| Evidence/rationale 1–2 sentences per record | 采纳 (low cost, batch description updates possible pre-release) |
| Data validation workflow | 已实施 (multi-model cross-check + human adjudication) |

## 九、执行优先级

- P1 分类去重 → 已实施 (26-item revision)
- P1 标准状态 → partially done (28/29/69 correct; PRFEILI65/66/62 deletion pending)
- P2 新增 → 已实施 (Section 三 15 rows, 2026-11-19)
- P3 数据结构 → crosswalk done; rest 待裁定

## 十、结论

Agree with overall direction: no mass deletion of Indirect tools; clean up superseded standards still marked In force, ended subsidies without stock obligations, duplicates, packages miscounted as instruments, and items with no credible mitigation pathway; add the Section 三 list. Use Indirect and Unknown for uncertain policies rather than deletion.

---

## Section 五 verification results (2026-11-18)

All six instruments stay 生效; no moves to Ended. Verification outcomes:

| Item | Outcome |
|---|---|
| 退耕还林 SUBESPI01 | 生效 confirmed. Stock subsidies continue: 延长补助 tied to stewardship, disbursed via "一卡通" (local publicised validity to 31/12/2029). New enrolment suspended since 2022-10 (自然资发〔2022〕191号); 2023 提质增效 notice (林工发〔2023〕109号): urgent tasks by 2025, two full rounds by 2030. **Updated CN+EN**: 最近修订 2022→2023, 详情/描述/法律文件/链接; evidence log +2. |
| 退牧还草 SUBESPI04 | 生效 confirmed. Construction tasks continue under provincial plans (Qinghai 2016–2025 plan) with central budget investment. **Classification kept as Subsidy/ESP** — rationale: enclosure/shed assets are built on herders' contracted grassland and become herder assets (in-kind support to non-government units), unlike #8's public fixed capital. 2011 feed-grain transfer already recorded. **Updated CN+EN**: 描述; evidence log +1. |
| 天然林 SUBESPI05 | 生效 confirmed. Row already current: 2025-02 six-agency 《天然林保护修复中长期规划》(to 2035), funding integrated into unified 森林保护修复补助. No data change needed. |
| 家电回收目标责任制 VTGVTGI01 | 生效 kept with annotation. As of end-2025 only two batches organised (6 enterprises 2022, 8 in 2023); no new batch lists since 2024; annual target mechanism continues to apply to enrolled enterprises — 待核实 (needs_human_review=true). **Updated CN+EN**: 描述; evidence log +1. |
| 生产者责任延伸 FRMEPRI01 | 生效 confirmed. Independent obligations exist (2025 targets, compliance monitoring, penalties via 固废法/生态环境法典) → keep as Regulatory framework row, linked to sector tools. No change. |
| 绿色制造标准体系 CBAGSSI01 | 维持原裁决 — row already states guiding/non-mandatory nature and the filing principle. No change. |

Pipeline after edits: 6/6 passed; no new validation warnings for the edited rows; 0 status flips; 286 instruments / 97 approaches unchanged.

## Old-standard row deletion (2026-11-18)

Per CLAUDE.md superseded-standards rule and user confirmation of the earliest-version date convention: deleted PRFEILI65 (GB 29444-2012 井工), PRFEILI66 (GB 29445-2012 露天), PRFEILI62 (GB 30185-2013) from CN+EN regulatory CSVs (164→161 rows). The current rows PRFEILI04 (通过 31/12/2012, 生效 01/10/2013, 最近修订 01/08/2025) and PRFEILI09 (通过 31/12/2013, 生效 01/12/2014, 最近修订 28/02/2025) already carried the earliest-predecessor dates and replacement mentions — no description edits needed. Removed the three dead ROW_TRANSLATIONS entries from generate_english_from_chinese.py and the three OVERVIEW_ROW_HEIGHTS keys from export_workbooks.py (matching the FRMTRSI03 deletion practice). Evidence log had no rows for the deleted IDs. Pipeline 6/6; 283 instruments / 97 approaches; validation clean for these changes.

## Pending work (as of 2026-11-18)

1. ~~Delete PRFEILI65/66/62 + note replacements (六)~~ — done 2026-11-18 (see above)
2. ~~Section 五 verification of 6 instruments~~ — done 2026-11-18 (see above)
3. ~~Railway/water transport CBI description refinement (四)~~ — done (CHNPIVCBII03/04)
4. ~~Methodology line: no automatic inclusion of green policies (一.5)~~ — done (classification structure.md item 7)
5. ~~Section 三 ~11 new instruments~~ — done 2026-11-19 (15 rows, see 三.4)
6. ~~Mitigation effects field (八.2)~~ — field already exists in all templates; adjudication corrected 2026-11-18. ~~SLB label scope (四)~~ — resolved 选项① (national market self-regulation rules), implemented in CN+EN descriptions + evidence log. ~~Optional: mark 未知 for 错峰生产/限塑/排污许可/三线一单~~ — done 2026-11-18: FRMPSMI01/TECBPPI01/FRMPDPI01/FRMEEZI01 减缓效果 正向→未知 (CN+EN CSVs + generator pins + 4 evidence entries), pipeline 6/6
