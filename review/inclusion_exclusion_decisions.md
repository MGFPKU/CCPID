# Inclusion / Exclusion Decisions

Record instrument boundary decisions here, especially when deciding whether a policy text is a policy package, a database instrument, or a subscheme.

For every user-requested data-filling item, record the inclusion gate before filling data:

- Requested item:
- Decision: include / exclude.
- Reason:
- If included: template, classification, and instrument/subscheme boundary.
- If excluded: concise reason to report to the user and any existing row it duplicates, if relevant.

## CHNTRAETSI01S000 - 全国碳排放权交易市场

- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Trading scheme / Emissions trading system.
- Rationale: The national carbon market creates a tradable allowance compliance system for key emitting entities.
- Subscheme decision: split current covered industries into four subscheme rows: power generation, steel, cement, and aluminum smelting. This preserves the parent national ETS row while allowing industry-specific coverage, allocation rules, and compliance data to be filled when available.
- Review flag: confirm whether future compliance-period allocation plans require additional phase or sector-detail subscheme rows.

## CHNTRARECI01S000 - 可再生能源绿色电力证书市场

- Requested item: 可再生能源绿色电力证书市场.
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Trading scheme / Tradable renewable electricity credits, quota or tradable performance standards.
- Rationale: The green electricity certificate system creates tradable certificates for renewable electricity environmental attributes. It is a specific market-based instrument rather than only a policy target or broad strategy.
- Instrument boundary: one parent instrument covering national GEC issuance and trading; no subscheme split in this first pass.

## CHNTRARECI02S000 - 可再生能源电力消纳责任权重制度

- Requested item: 可再生能源电力消纳责任权重制度.
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Trading scheme / Tradable renewable electricity credits, quota or tradable performance standards.
- Rationale: The system establishes mandatory renewable electricity consumption responsibility weights and allows obligated market entities to meet obligations through actual renewable electricity consumption, purchases of excess consumption amounts, or green certificate purchases. It is therefore a specific RPS/quota-style market instrument rather than only a broad renewable-energy target.
- Instrument boundary: one parent instrument covering the national renewable electricity consumption responsibility weight mechanism; no subscheme split in this first pass.

## CHNTRATPSI01S000 - 乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法

- Requested item: 乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法.
- Decision: include as one national-level trading-scheme instrument with two subscheme rows.
- Template: Economic instruments.
- Classification: Trading scheme / Tradable performance standards.
- Rationale: The measure creates a tradable performance-credit compliance system for passenger vehicle firms. CAFC and NEV credits are separately calculated but jointly assessed, and negative-credit compliance can be met through credit carry-forward, transfer, purchase, and the NEV credit-pool mechanism.
- Subscheme decision: parent row `CHNTRATPSI01S000`; CAFC credit subscheme `CHNTRATPSI01S001`; NEV credit subscheme `CHNTRATPSI01S002`.
- Legal-source decision: use the official gov.cn measure text (`https://www.gov.cn/zhengce/2022-11/27/content_5722693.htm`) as the primary Legal document. Keep the 2017 original page, 2020 amendment, 2023 MIIT revision page, and 2025 MIIT 2026-2027 management notice in Other weblinks.
- Latest-revision decision: use the 2025 MIIT notice (`https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2025/art_c22055da7deb48c397ad16247beaff22.html`) as the latest formal operational revision because it sets 2026-2027 CAFC/NEV credit management rules, including NEV credit ratios of 48% and 58%.
- Review flag: confirm whether official annual disclosures provide transaction volume or transaction value for CAFC/NEV credits; current market-operation value uses a secondary source for 2022 NEV credit transaction value and estimated volume.

## CHNSUBCLGI01S000 - 中期借贷便利（MLF）绿色担保品范围扩容

- Requested item: 中期借贷便利（MLF）绿色担保品范围扩容.
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Concessional loans, loan guarantees and credit support.
- Rationale: The PBOC notice changes central-bank MLF collateral eligibility by accepting AA-or-above green financial bonds and high-quality green loans. This is a specific credit-support / financial-risk-mitigation mechanism, and the IFCMA typology treats concessional loans, loan guarantees, and other financial risk-mitigation mechanisms as subsidies.
- ID decision: use `SUB` for subsidy and `CLG` for concessional loans / loan guarantees / credit support, giving `CHNSUBCLGI01S000`.
- Instrument boundary: one instrument row for the 2018 green-collateral eligibility expansion; no subscheme split in this first pass.
- Review flag: confirm the new credit-support approach label and whether later PBOC collateral rules should be represented as revisions or separate instruments.

## CHNSUBCLGI02S000 - 碳减排支持工具

- Requested item: 碳减排支持工具.
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Concessional loans, loan guarantees and credit support.
- Rationale: The PBOC provides low-cost central-bank funding to eligible financial institutions after they issue qualified carbon-reduction loans. This is a credit-support and concessional-funding mechanism rather than a trading scheme or regulatory performance standard.
- ID decision: use `SUB` for subsidy and `CLG` for concessional loans / loan guarantees / credit support, giving `CHNSUBCLGI02S000`.
- Instrument boundary: one instrument row for the national carbon emission reduction support tool; no subscheme split in this first pass. The eligible project areas are captured as sub-sector/asset details rather than separate subschemes.
- Source/revision decision: use the PBOC carbon emission reduction support tool page as Legal document and record the PBOC 15/01/2026 revision source in Other weblinks. Record the end date as 31/12/2027 and the latest revision date as 15/01/2026.

## CHNSUBCLGI03S000 - 设备更新贷款财政贴息

- Requested item: 设备更新贷款财政贴息.
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Concessional loans, loan guarantees and credit support.
- Rationale: The measure subsidizes interest costs for eligible equipment-renewal loans, reducing financing costs for equipment renewal and technological transformation. This is a concessional-credit/interest-subsidy mechanism rather than a direct regulatory standard or trading scheme.
- ID decision: use `SUB` for subsidy and `CLG` for concessional loans / loan guarantees / credit support, giving `CHNSUBCLGI03S000`.
- Instrument boundary: one instrument row for the national equipment renewal loan fiscal interest subsidy; no subscheme split in this first pass.
- Source/revision decision: use the 2024 gov.cn notice as Legal document and the 2026 gov.cn optimization notice as Other weblinks. User-provided gov.cn PDFs were used to verify the 2024 notice date, the 2026 latest revision date, the 1.5 percentage point optimized interest subsidy rate, the two-year maximum subsidy period, expanded covered fields, and the 31/12/2026 implementation end date.

## CHNSUBESPI01S000 - 退耕还林还草

- Requested item: 退耕还林还草 (Grain for Green / Sloping Land Conversion Program).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Ecosystem service payments.
- Rationale: A concrete, specific program with its own State Council regulation (《退耕还林条例》, Decree 367, 2002; revised 2016). Compensates farmers for converting sloping/degraded cropland to forest or grassland. GGP contributed >60% of Loess Plateau vegetation NPP growth, shifted the region from carbon source to sink, and contributed >4% of global net green growth area. Mitigation relevance: indirect — primary objectives are erosion control and rural development, but substantial carbon sequestration co-benefit.
- New approach: Ecosystem service payments (ESP) added to the Subsidy group.
- Instrument boundary: one parent instrument covering both 退耕还林 and 退耕还草 under the unified legal framework; no subscheme split in this first pass.
- ID: CHNSUBESPI01S000 = CHN + SUB + ESP + I01 + S000.
- Source decision: legal basis is 《退耕还林条例》(State Council Decree 367). Key operational documents: 2007 State Council notice (国发〔2007〕25号) and 2022 five-agency notice (自然资发〔2022〕191号).
- Review flag: confirm whether 退耕还林 and 退耕还草 should be split into separate subscheme rows; confirm whether 1999 first round and 2014 second round should be one continuous instrument or two phases.

## CHNSUBESPI02S000 - 森林生态效益补偿

- Requested item: 森林生态效益补偿 (Forest Ecological Benefit Compensation).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Ecosystem service payments.
- Rationale: The Central Fiscal Forest Ecological Benefit Compensation Fund (中央财政森林生态效益补偿基金), established under the Forest Law (Arts. 7, 29), provides per-unit-area payments for ongoing management and protection of nationally designated ecological welfare forests (~1.7 billion mu, ~113 million ha). Payments compensate for logging restrictions and incentivize forest quality maintenance. China's forest vegetation carbon stock is ~7.8 billion tonnes of carbon, with annual net sequestration of ~359 million tonnes CO2. Public benefit forests account for ~67% of national forest stock. Mitigation relevance: direct — carbon sequestration is an explicit ecosystem service, with forest carbon sinks integrated into CCER and carbon ticket pilots.
- Instrument boundary: one parent instrument covering the unified national compensation fund; no subscheme split in this first pass. Separate from NFPP (天然林保护工程) and GGP (退耕还林) — these are three distinct pillars of China's forest ecological protection fiscal architecture, though the NFPP and FEBC are progressively converging under the 2025 Long-term Plan.
- ID: CHNSUBESPI02S000 = CHN + SUB + ESP + I02 + S000.
- Source decision: legal basis is 《森林法》(2019 revision) Arts. 7, 29. Current operative regulation: 财资环〔2024〕159号. Key historical: 财农〔2007〕7号 (2007 fund management rules). National-level public benefit forest delineation: 林资发〔2017〕34号.
- Review flag: confirm mitigation relevance (direct vs indirect); confirm whether state-owned and collective/individual components should be subschemes given different payment rates (10 vs 16 yuan/mu/year).

## CHNSUBESPI03S000 - 草原生态保护补助奖励

- Requested item: 草原生态保护补助奖励 (Grassland Ecological Protection Subsidy and Reward).
- Decision: include as one national-level policy instrument with two subschemes.
- Template: Economic instruments.
- Classification: Subsidy / Ecosystem service payments.
- Rationale: Established by State Council 128th Executive Meeting (2010-10-12), effective 2011. Provides conditional cash payments to herders for grazing bans and grass-livestock balance compliance across 13 provinces, ~38 billion mu of grassland, benefiting 1,200+ million herder households. Cumulative central budget >2,300 billion yuan (2011-2025). Mitigation relevance: indirect but material — China's grasslands cover ~40 billion mu (27.6% of territory); the policy governs grazing intensity on this land, with significant carbon sink implications. However, carbon is not an explicit policy objective (stated goals are "两保一促进": ecology, livestock supply, herder income).
- Subscheme decision: parent row CHNSUBESPI03S000; Grazing Ban Subsidy subscheme CHNSUBESPI03S001 (禁牧补助); Grass-Livestock Balance Reward subscheme CHNSUBESPI03S002 (草畜平衡奖励). The two components have different payment rates (7.5 vs 2.5 yuan/mu/year), different obligations (total prohibition vs stocking rate limits), and mutually exclusive land designations.
- Instrument boundary: separate from 退牧还草 (CHNSUBESPI04S000) — 退牧还草 is an infrastructure/engineering project (fencing, reseeding, sheds), while 草原补奖 is a cash transfer program. The two form a two-pillar grassland protection system. The 2011 policy explicitly transferred feed grain subsidies from 退牧还草 to the new 草原补奖 mechanism.
- ID: CHNSUBESPI03S000 = CHN + SUB + ESP + I03 + S000.
- Source decision: Round 1: 农财发[2011]85号; Round 2: 农办财[2016]10号; Round 3: 财农[2021]82号. Round 4 announced in 2026 Central Document No. 1 for 2026-2030. Use Round 3 guidance as primary legal document.
- Review flag: confirm Round 4 formal guidance once published; confirm whether mitigation relevance should be indirect or direct given grassland carbon sink pilots.

## CHNSUBESPI04S000 - 退牧还草

- Requested item: 退牧还草 (Returning Grazing Land to Grassland).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Ecosystem service payments.
- Rationale: A major national grassland ecological engineering project (生态建设工程) authorized by State Council 国发〔2002〕19号 and launched March 2003. Constructs fencing, reseeding, artificial forage land, and livestock shed infrastructure across 8 provinces/regions, covering 215 counties and ~1.2 million herder households. Cumulative central investment through 2011: ~209 billion yuan. Mitigation relevance: indirect — primary objectives are combating desertification, watershed protection, and ecological restoration. Carbon sequestration is increasingly recognized (40-60% CO2 sink enhancement in restored alpine grasslands) and grassland carbon trading pilots are active, but carbon was not a founding objective.
- Instrument boundary: one parent instrument covering the unified engineering program; no subscheme split. Distinct from 草原生态保护补助奖励 (CHNSUBESPI03S000) — 退牧还草 funds infrastructure ("hardware"), while 草原补奖 funds cash compensation to herders ("software"). The two were operationally separated in 2011 when feed grain subsidies were transferred from 退牧还草 to the new 草原补奖 mechanism.
- ID: CHNSUBESPI04S000 = CHN + SUB + ESP + I04 + S000.
- Source decision: legal basis is 《草原法》Arts. 35, 42, 46-48. Founding policy: 国发〔2002〕19号. Key operational: 国西办农〔2003〕8号 and 发改西部〔2011〕1856号. Current framework: 国办发〔2021〕7号.
- Review flag: confirm whether the program is still actively funded as a standalone line item or has been fully absorbed into integrated frameworks (三北, 山水林田湖草沙); confirm whether 退牧还草 and 退耕还林还草 (CHNSUBESPI01S000) share the same Grassland Law provisions.

## CHNSUBESPI05S000 - 天然林保护工程

- Requested item: 天然林资源保护工程 / 天然林保护修复 (Natural Forest Protection Program).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Ecosystem service payments.
- Rationale: One of China's largest conservation investments (cumulative >5,000 billion yuan, 1998-2020). Covers 17 provinces, 56.43 million ha of natural forest. Enforces logging bans, funds forest tending and restoration, resettles displaced forestry workers (675,000 in Phase I). Carbon sequestration explicit from Phase II (target: +416 million tonnes forest carbon sink). Post-2019 transitioned from time-limited "project" (工程) to permanent "system" (制度) under the 2019 System Plan (中办/国办). 2025 Long-term Plan (2021-2035) consolidates budget lines. Mitigation relevance: indirect — primary objectives are ecological disaster prevention, soil/water conservation, biodiversity, and forest industry restructuring. Carbon sequestration was NOT a Phase I objective but became explicit and quantified from Phase II (2011) onward.
- Instrument boundary: one continuous instrument covering all phases (Phase I 2000-2010, Phase II 2011-2020, post-2019 permanent system). The two geographic implementation plans (Upper Yangtze/Yellow River vs. Northeast/Inner Mongolia) are operational subdivisions of the same instrument, not separate instruments. Distinct from 森林生态效益补偿 (FEBC, CHNSUBESPI02S000) — NFPP is an ecological construction project (工程建设) funding operational costs + worker resettlement; FEBC is a compensation system (补偿制度) paying for development opportunity loss on designated public-benefit forests. The two are converging under the 2025 Long-term Plan but remain administratively distinct.
- ID: CHNSUBESPI05S000 = CHN + SUB + ESP + I05 + S000.
- Source decision: highest legal basis is 《森林法》(2019 revision) Art. 32. Authoritative programmatic document: 2019 System Plan (https://www.gov.cn/zhengce/2019-07/23/content_5413850.htm). Key operational: 林天发[2001]180号 (Phase I management rules), 发改西部〔2011〕1856号. Latest: 2025 Long-term Plan (六部门, Feb 2025).
- Review flag: confirm whether the pre-2019 "工程" and post-2019 "制度" should be one continuous instrument or two entries; confirm mitigation relevance given explicit Phase II carbon targets; confirm whether "environment" is correct functioning channel.

## CHNSUBTISI01S000 - 老旧营运船舶报废更新补贴

- Requested item: 老旧营运船舶报废更新补贴 (Old operating ship scrapping and renewal subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Trade-in subsidy.
- New approach: Trade-in subsidy (TIS) added to the Subsidy group.
- Rationale: Part of China's 大规模设备更新和消费品以旧换新 (Large-scale equipment renewal and consumer goods trade-in) initiative. Provides subsidies to shipping companies for scrapping old operating vessels and purchasing new, more energy-efficient replacements. Mitigation relevance: direct — the policy explicitly targets replacement of high-emission, low-efficiency vessels with modern fuel-efficient ships, reducing fuel consumption and CO2 emissions per tonne-kilometre.
- Instrument boundary: one parent instrument; no subscheme split. Covers both maritime and inland waterway operating ships.
- ID: CHNSUBTISI01S000 = CHN + SUB + TIS + I01 + S000.
- Source decision: key legal basis 交办水〔2024〕60号 (交通运输部、国家发展改革委老旧营运船舶报废更新补贴实施细则). Supporting policy documents include 国发〔2024〕7号 and 发改环资〔2024〕1104号.
- Review flag: confirm subsidy rate structure across vessel types and fuel options (LNG, electric, etc.).

## CHNSUBTISI02S000 - 农业机械报废更新补贴

- Requested item: 农业机械报废更新补贴 (Agricultural machinery scrapping and renewal subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Trade-in subsidy.
- Rationale: Part of the same 大规模设备更新和消费品以旧换新 initiative. Provides subsidies to farmers and agricultural operators for scrapping old, high-emission agricultural machinery and purchasing new, more efficient replacements. Mitigation relevance: indirect — primary objectives are agricultural modernization, productivity improvement, and safety; fuel efficiency and emission reduction are material co-benefits.
- Instrument boundary: one parent instrument; no subscheme split. Covers tractors, harvesters, planters, and other agricultural machinery categories with differentiated subsidy rates.
- ID: CHNSUBTISI02S000 = CHN + SUB + TIS + I02 + S000.
- Source decision: key legal basis 农办机〔2024〕4号 (农业农村部办公厅、财政部办公厅通知). Also linked to 国发〔2024〕7号 and 发改环资〔2024〕1104号.
- Review flag: confirm whether provincial variation in subsidy rates should be captured as subschemes.

## CHNSUBTISI03S000 - 家电以旧换新补贴

- Requested item: 家电以旧换新补贴 (Home appliances trade-in subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Trade-in subsidy.
- Rationale: Part of the same 大规模设备更新和消费品以旧换新 initiative. Provides subsidies to households for trading in old, energy-inefficient home appliances and purchasing new, higher-energy-efficiency-grade replacements. Mitigation relevance: indirect — primary objectives are consumer spending stimulation and industrial production support; energy efficiency improvement is a secondary co-benefit achieved through efficiency-grade requirements on new appliances.
- Instrument boundary: one parent instrument; no subscheme split. Covers multiple appliance categories (air conditioners, refrigerators, washing machines, televisions, water heaters, etc.) with differentiated subsidy rates based on energy efficiency grade.
- ID: CHNSUBTISI03S000 = CHN + SUB + TIS + I03 + S000.
- Source decision: key legal basis 商消费发〔2024〕18号 (商务部等13部门通知). Also linked to 国发〔2024〕7号 and related MOFCOM/MOF implementation circulars.
- Review flag: confirm whether energy efficiency grade requirements and subsidy rate differences across appliance categories warrant subscheme splitting.

## CHNSUBVPSI01S000 - 老旧营运货车报废更新补贴

- Requested item: 老旧营运货车报废更新补贴 (Old operating truck scrapping and renewal subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Vehicle purchase subsidy.
- Rationale: Part of China's 大规模设备更新和消费品以旧换新 (Large-scale equipment renewal and consumer goods trade-in) initiative. Provides subsidies to freight companies for scrapping old China III and below diesel trucks and purchasing new China VI diesel or new energy trucks. Mitigation relevance: direct — the policy explicitly targets replacement of high-emission, low-efficiency old diesel trucks with modern fuel-efficient or zero-emission vehicles.
- Instrument boundary: one parent instrument covering both maritime and inland waterway operating ships; no subscheme split. The three subsidy scenarios (scrap-only, scrap+renewal, new NEV cold-chain van only) are differentiated within the same instrument row.
- ID: CHNSUBVPSI01S000 = CHN + SUB + VPS + I01 + S000.
- Source decision: Legal basis is 交规划发〔2024〕90号 (交通运输部、财政部, 2024-07-30). Supporting: 国发〔2024〕7号, 发改环资〔2024〕1104号, 交办运〔2024〕44号. URL: https://app.www.gov.cn/govdata/gov/202408/02/517908/article.html.
- Review flag: confirm whether scrap-only and scrap+renewal should be split as subschemes given different subsidy rates.

## CHNSUBVPSI02S000 - 汽车报废更新补贴

- Requested item: 汽车报废更新补贴 (Car scrapping and renewal subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Vehicle purchase subsidy.
- Rationale: Part of the same 大规模设备更新和消费品以旧换新 initiative. Provides subsidies to individual consumers for scrapping old China III and below fuel passenger cars or pre-2018 NEVs and purchasing new NEVs or fuel-efficient ICE vehicles. Mitigation relevance: direct — explicitly targets high-emission old vehicles for replacement with NEVs or fuel-efficient ICEs, reducing transport sector emissions.
- Instrument boundary: one parent instrument; no subscheme split. The updated rates (商消费函〔2024〕392号) doubled from the original (商消费函〔2024〕75号): NEV subsidy raised from 1万 to 2万; ICE subsidy raised from 0.7万 to 1.5万.
- ID: CHNSUBVPSI02S000 = CHN + SUB + VPS + I02 + S000.
- Source decision: Primary legal basis is 商消费函〔2024〕75号 (商务部等7部门, 2024-04-24). Rate updated by 商消费函〔2024〕392号 (2024-08-15). URLs: http://www.mofcom.gov.cn/zfxxgk/fdzdgknr/ztfl/gnmygl/art/2024/art_00ec662a1a234fa6878308334ad0d728.html and https://www.mofcom.gov.cn/zfxxgk/gkml/art/2024/art_d4224d2ebd8b4120875bc99963538fbe.html.
- Review flag: confirm whether NEV and ICE subsidy tiers should be tracked as subschemes.

## CHNSUBVPSI03S000 - 汽车置换更新补贴

- Requested item: 汽车置换更新补贴 (Car replacement/swap subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Vehicle purchase subsidy.
- Rationale: Established within the 商消费函〔2024〕392号 framework as a national-level instrument requiring provincial implementation. Individual consumers trading in old vehicles for new ones receive provincial subsidies. While subsidy amounts vary by province, the instrument is defined and authorized at the national level. Mitigation relevance: direct — targets replacement of older vehicles with newer, more efficient or zero-emission models.
- Instrument boundary: one parent instrument for the national framework; no subscheme split. Provincial variations in subsidy rates are implementation details, not separate instruments. Typically NEV replacements receive higher subsidies (1.5-2万) than ICE replacements (0.8-1.5万 depending on engine size).
- ID: CHNSUBVPSI03S000 = CHN + SUB + VPS + I03 + S000.
- Source decision: Legal basis is 商消费函〔2024〕392号 (商务部等7部门, 2024-08-15), which established the national framework and required provinces to set their own subsidy standards. URL: https://www.mofcom.gov.cn/zfxxgk/gkml/art/2024/art_d4224d2ebd8b4120875bc99963538fbe.html.
- Review flag: confirm that provincial variation does not warrant subscheme splitting; confirm whether a central funding mechanism exists.

## CHNSUBVPSI04S000 - 新能源城市公交车及动力电池更新补贴

- Requested item: 新能源城市公交车及动力电池更新补贴 (New energy city bus and power battery renewal subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Vehicle purchase subsidy.
- Rationale: Part of the same 大规模设备更新和消费品以旧换新 initiative. Provides subsidies to city bus operators for replacing old (8-year+) buses with new energy buses and/or replacing power batteries. Mitigation relevance: direct — explicitly promotes zero-emission public transport and battery renewal to maintain NEV fleet performance.
- Instrument boundary: one parent instrument; no subscheme split. The bus renewal (8万/vehicle) and battery replacement (4.2万/vehicle) are two components of the same instrument.
- ID: CHNSUBVPSI04S000 = CHN + SUB + VPS + I04 + S000.
- Source decision: Primary legal basis is 交运函〔2024〕390号 (交通运输部、财政部, 2024-07-29). Supplemented by 交办运〔2024〕49号 (2024-09-24, 3 departments). URL: https://www.ndrc.gov.cn/xwdt/ztzl/tddgmsbgxhxfpyjhx/gzdt/202410/t20241031_1394144_ext.html. Supplement URL: https://xxgk.mot.gov.cn/2020/jigou/ysfws/202409/t20240925_4156949.html.
- Review flag: confirm whether bus renewal and battery replacement should be separate subschemes given different rates and conditions.

## CHNSUBCHSI01S000 - 北方地区冬季清洁取暖补贴

- Requested item: 北方地区冬季清洁取暖补贴 (Northern winter clean heating subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Clean heating subsidy.
- New approach: Clean heating subsidy (CHS) added to the Subsidy group.
- Rationale: Central fiscal funds (via 大气污染防治资金) subsidise coal-to-clean-heating conversion in northern Chinese cities for both equipment purchase (heat pumps, gas boilers, biomass stoves) and operating costs. Since 2017 the program has covered 88 cities across 4 batches; 204亿元 budgeted for 2025. Mitigation relevance: direct — replacing coal heating with electricity, gas, biomass, or geothermal directly reduces CO2, SO2, NOx, and PM emissions from the buildings sector.
- Instrument boundary: one parent instrument covering the national framework implemented through city-level programs; no subscheme split in this first pass. The program operates as a unified national fiscal transfer mechanism even though individual cities set local subsidy rates and eligible technology menus.
- ID: CHNSUBCHSI01S000 = CHN + SUB + CHS + I01 + S000.
- Source decision: legal basis is 大气污染防治资金管理办法 and annual MOF/MEE joint funding notices. Key policy documents include the central government clean heating planning notices since 2017.
- Review flag: confirm whether different heating technology types (electric, gas, biomass, geothermal) warrant subscheme splitting given different subsidy rates; confirm exact legal statute title for the national framework.

## CHNSUBRTSI01S000 - 废弃电器电子产品回收处理奖补

- Requested item: 废弃电器电子产品回收处理奖补 (Waste electrical and electronic equipment recycling and treatment reward/subsidy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Recycling and treatment subsidy.
- New approach: Recycling and treatment subsidy (RTS) added to the Subsidy group.
- Rationale: 财资环〔2024〕119号 transitioned WEEE recycling funding from a producer-funded scheme to a central budget special fund (专项资金) in 2024, with 75亿元 (2024) and 50亿元 (2025). Supports collection, recycling, and environmentally sound treatment across 5 categories of WEEE. Mitigation relevance: indirect — primary objectives are circular economy and resource efficiency, but the instrument generates material GHG co-benefits through HFC refrigerant recovery (high-GWP substances), avoided landfill methane, and reduced virgin-material energy demand. Per IFCMA scope, mitigation-relevant instruments with indirect climate effects are eligible.
- Instrument boundary: one parent instrument; no subscheme split in this first pass.
- ID: CHNSUBRTSI01S000 = CHN + SUB + RTS + I01 + S000.
- Source decision: primary legal basis is 财资环〔2024〕119号 (财政部、生态环境部). The 2024 reform replaced the earlier producer-funded WEEE disposal fund (废弃电器电子产品处理基金, established 2012) with direct central budget appropriations.
- Review flag: confirm whether the 5 WEEE categories (televisions, refrigerators, washing machines, air conditioners, computers) warrant subscheme splitting; confirm whether the pre-2024 producer-funded fund and the post-2024 central budget special fund should be one continuous instrument or two entries.

## CHNSUBMPSI01S000 - 农机购置与应用补贴（新能源）

- Requested item: 农机购置与应用补贴（新能源）(Agricultural machinery purchase and application subsidy — new energy).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Subsidy / Low-emission machinery purchase subsidy.
- New approach: Low-emission machinery purchase subsidy (MPS) added to the Subsidy group.
- Rationale: 农办机〔2024〕3号/6号, 2024–2026 period. Provides a preferential purchase subsidy rate for new energy agricultural machinery (35% subsidy rate vs. 30% standard rate for conventional machinery, with up to 20% additional uplift for certain categories). Mitigation relevance: direct — explicitly incentivises replacement of diesel agricultural machinery with electric, hybrid, or hydrogen alternatives, directly reducing agricultural sector fuel combustion emissions.
- Instrument boundary: one parent instrument; no subscheme split in this first pass. Distinct from CHNSUBTISI02S000 (农业机械报废更新补贴) which is a trade-in/scrapping subsidy; this instrument is a purchase subsidy specifically incentivising new energy equipment regardless of whether old machinery is scrapped.
- ID: CHNSUBMPSI01S000 = CHN + SUB + MPS + I01 + S000.
- Source decision: primary legal basis is 农办机〔2024〕3号 and 农办机〔2024〕6号 (农业农村部办公厅、财政部办公厅). Part of the broader 农机购置与应用补贴 program (2024–2026) with the new-energy component receiving differentiated preferential rates.
- Review flag: confirm whether the new-energy component is legally a standalone instrument or a preferential rate tier within the general agricultural machinery purchase subsidy; confirm whether conventional and new-energy agricultural machinery subsidies should be tracked as separate instruments or as differentiated rates within one instrument.

## 农田建设补助 — EXCLUDE

- Requested item: 农田建设补助 (Farmland construction subsidy / High-standard farmland construction subsidy).
- Decision: exclude.
- Reason: Primary objectives are food security, agricultural productivity, and farmland infrastructure (irrigation, drainage, field roads, land levelling). Any climate mitigation effect — theoretical soil carbon sequestration or water pumping energy efficiency — is too attenuated and incidental to qualify even as an indirect mitigation-relevant instrument. Including this would open the door to nearly any agricultural infrastructure program. No material, measurable impact on GHG emissions that can be attributed to the instrument's design.

## CHNPIVCBII01S000 - 县域充换电设施补短板试点

- Requested item: 县域充换电设施补短板试点 (County-level charging and battery-swapping facility pilot to fill gaps).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public investment / Central budget investment.
- New approach: Central budget investment (CBI) added under the Public investment group.
- Rationale: 财建〔2024〕57号, 2024–2026 pilot program. Central government provides grants to selected pilot counties (67 in 2024, 75 in 2025) to build EV charging and battery-swapping infrastructure, up to 4500万元 per county. Requires ≥120kW fast chargers and ≥99% availability, targeting township-level coverage (乡乡全覆盖). Mitigation relevance: direct — builds essential enabling infrastructure for EV adoption in underserved rural areas where private investment in charging has been insufficient.
- Instrument boundary: one parent instrument covering the national pilot program; no subscheme split. County-level implementation variation is operational, not structural.
- ID: CHNPIVCBII01S000 = CHN + PIV + CBI + I01 + S000.
- Source decision: primary legal basis is 财建〔2024〕57号 (财政部、工业和信息化部、交通运输部). The pilot was expanded in 2025 with a second cohort of counties.
- Review flag: confirm whether the 2024 and 2025 cohorts should be tracked as phases or as one continuous instrument; confirm whether charging and battery-swapping infrastructure should be separate subschemes.

## CHNPIVRDDI01S000 - 氢能综合应用试点

- Requested item: 氢能综合应用试点 (Hydrogen comprehensive application pilot).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public investment / Government-funded RD&D programmes for low-carbon energy technologies.
- Rationale: 2026年3月 jointly launched by 工信部、财政部、国家发展改革委. Selects 5 city clusters for a 4-year pilot period, with central government funding up to 16亿元 per cluster. Covers 6 application scenarios: fuel cell vehicles (FCVs), green ammonia/methanol production, hydrogen chemicals, hydrogen metallurgy, hydrogen co-firing in power generation, and innovative applications. Mitigation relevance: direct — targets emission reductions across multiple hard-to-abate sectors (heavy transport, chemicals, steel, power) through hydrogen deployment.
- Instrument boundary: one parent instrument; no subscheme split in this first pass. The 6 application scenarios are captured within the Description and Asset fields rather than as separate subschemes.
- ID: CHNPIVRDDI01S000 = CHN + PIV + RDD + I01 + S000.
- Source decision: primary legal basis is the 2026 joint notice from MIIT/MOF/NDRC establishing the pilot program. The program represents China's flagship hydrogen economy deployment initiative.
- Review flag: confirm whether the 6 application scenarios warrant subscheme splitting given different technologies, sectors, and funding mechanisms; confirm whether the pilot nature (4-year fixed term) and the 5 city clusters imply future phase-based subscheme rows.

## CHNTAXFETI01S000 - 成品油消费税 (Fuel excise tax)

- Requested item: 成品油消费税 (Fuel excise tax).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / Fuel excise tax.
- Rationale: China's fuel excise tax (成品油消费税) is a per-unit excise tax on gasoline, diesel, naphtha, kerosene, fuel oil, and solvent oil consumption under the 消费税暂行条例. It raises the price of fossil fuel consumption relative to alternatives and is the most material carbon-price-equivalent economic instrument in China's tax system. For 2024, fuel excise revenue was approximately 1.6 trillion yuan, with the effective carbon price averaging ~89 yuan/tCO2 for gasoline and ~48 yuan/tCO2 for diesel. Mitigation relevance: direct — the tax explicitly raises the cost of fossil fuel combustion, which is the primary source of GHG emissions.
- Instrument boundary: one parent instrument covering consumption tax on all成品油 categories; no subscheme split. Differential rates across fuel types are captured in Intensity/Details fields.
- ID: CHNTAXFETI01S000 = CHN + TAX + FET + I01 + S000.
- Source decision: legal basis is 《中华人民共和国消费税暂行条例》(State Council Decree 539, 2008 revision) and its implementation rules. Rate schedules are set by MOF/SAT notices.

## CHNTAXDVTI01S000 - 汽车消费税 (Differentiated vehicle tax)

- Requested item: 汽车消费税 (Automobile consumption tax).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / Differentiated vehicle tax.
- New approach: Differentiated vehicle tax (DVT) added to the Tax group.
- Rationale: China's automobile consumption tax (汽车消费税) levies different tax rates based on engine displacement, creating a structural price incentive against large-displacement, high-emission vehicles. Rates range from 1% (≤1.0L) to 40% (>4.0L). The tax is levied on manufacturers/importers at the production/import stage and is distinct from the vehicle purchase tax (车辆购置税) and the annual vehicle and vessel tax (车船税). Mitigation relevance: direct — the tax structure explicitly differentiates by engine displacement, which is strongly correlated with CO2 emissions, creating a price mechanism that discourages high-emission vehicle purchases.
- Instrument boundary: one parent instrument; no subscheme split. The rate tiers by engine displacement are captured within Intensity/Details fields rather than as separate subschemes.
- ID: CHNTAXDVTI01S000 = CHN + TAX + DVT + I01 + S000.
- Source decision: legal basis is 《中华人民共和国消费税暂行条例》(State Council Decree 539, 2008 revision), specifically the automobile (小汽车) tax item schedule. Rate schedules are maintained by MOF/SAT.

## CHNTAXVOTI01S000 - 节能与新能源车船税优惠 (Vehicle ownership tax incentive)

- Requested item: 新能源车船免征车船税 (NEV vehicle and vessel tax exemption) and 节能汽车减半征收车船税 (fuel-efficient vehicle 50% reduction).
- Decision: include as one national-level policy instrument with two subschemes.
- Template: Economic instruments.
- Classification: Tax / Vehicle ownership tax incentive.
- New approach: Vehicle ownership tax incentive (VOT) added to the Tax group.
- Rationale: China's Vehicle and Vessel Tax Law (《中华人民共和国车船税法》, 2011) provides for tax exemptions and reductions for new energy and fuel-efficient vehicles. NEVs (pure electric, fuel cell, plug-in hybrid) receive full exemption from the annual vehicle and vessel tax (车船税). Fuel-efficient passenger cars that achieve fuel consumption below a specified threshold receive a 50% reduction. These are recurring annual tax incentives that reduce the total cost of ownership for low-carbon vehicles. Mitigation relevance: direct — explicitly incentivises ownership and continued operation of low-carbon vehicles through the annual tax system.
- Subscheme decision: parent row CHNTAXVOTI01S000; NEV exemption subscheme CHNTAXVOTI01S001 (新能源车船免征车船税); fuel-efficient vehicle 50% reduction subscheme CHNTAXVOTI01S002 (节能汽车减半征收车船税). The two components have different eligibility criteria (vehicle type vs. fuel consumption threshold) and different incentive levels (100% exemption vs. 50% reduction).
- Instrument boundary: one parent instrument covering vehicle ownership tax incentives for low-carbon vehicles; the basic vehicle and vessel tax rate structure without climate differentiation is excluded from the database.
- ID: CHNTAXVOTI01S000 = CHN + TAX + VOT + I01 + S000.
- Source decision: legal basis is 《中华人民共和国车船税法》Art. 4 (NEV exemption) and Art. 5 (energy-saving vehicle reduction). Implementing regulations in 《中华人民共和国车船税法实施条例》and MOF/SAT/MIIT joint notices.

## CHNTAXVATI01S000 - 合同能源管理项目增值税优惠 (VAT incentive for energy performance contracting)

- Requested item: 合同能源管理项目暂免征收增值税（货物）and 合同能源管理项目免征增值税（服务）.
- Decision: include as one national-level policy instrument merging both the goods and services VAT relief components.
- Template: Economic instruments.
- Classification: Tax / VAT incentive.
- New approach: VAT incentive (VAT) added to the Tax group.
- Rationale: Energy Performance Contracting (EPC) projects are a key delivery mechanism for energy efficiency retrofits in industry and buildings. The VAT incentive removes the tax burden on EPC companies' provision of both goods (equipment) and services (energy management), lowering the cost of energy efficiency projects. This is a mechanism-based approach classification: all VAT incentives for climate-relevant goods and services are grouped under one "VAT incentive" approach regardless of sector. Mitigation relevance: direct — explicitly targets energy efficiency improvement through reducing the tax cost of EPC delivery.
- Instrument boundary: one parent instrument combining both the goods component (暂免征收增值税 for equipment transferred under EPC) and the services component (免征增值税 for energy management services). The two components are legally intertwined as part of the EPC VAT relief framework.
- ID: CHNTAXVATI01S000 = CHN + TAX + VAT + I01 + S000.
- Source decision: legal basis is 财税〔2010〕110号 (MOF/SAT notice on VAT policy for energy performance contracting) and subsequent extensions/supplements.

## CHNTAXVATI02S000 - 资源综合利用产品及劳务增值税即征即退 (VAT refund for resource comprehensive utilization)

- Requested item: 资源综合利用产品及劳务增值税即征即退 (Immediate VAT refund for resource comprehensive utilisation products and services).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / VAT incentive.
- Rationale: The VAT immediate refund (即征即退) mechanism provides refunds of 30%, 50%, 70%, or 100% of VAT paid on products manufactured from recycled or waste materials (e.g., recycled building materials, waste plastics, scrap metals, waste paper, waste rubber). Mitigation relevance: indirect — primary objectives are circular economy and resource efficiency, but the instrument generates material GHG co-benefits through avoided virgin-material energy intensity, avoided landfill methane, and reduced industrial process emissions. The IFCMA scope includes mitigation-relevant instruments even when climate is not the primary objective.
- Instrument boundary: one parent instrument covering all product categories under the unified VAT refund catalogue; no subscheme split. Differentiated refund rates by product category are captured in Intensity/Details fields.
- ID: CHNTAXVATI02S000 = CHN + TAX + VAT + I02 + S000.
- Source decision: legal basis is 财税〔2015〕78号 (MOF/SAT notice on VAT policy for resource comprehensive utilisation products and services) and its updated catalogue.

## CHNTAXVATI03S000 - 有机肥产品免征增值税 (VAT exemption for organic fertiliser products)

- Requested item: 有机肥产品免征增值税 (VAT exemption for organic fertiliser products).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / VAT incentive.
- Rationale: The VAT exemption for organic fertiliser products reduces the cost of organic fertiliser relative to synthetic nitrogen fertilisers, whose production is highly energy-intensive (Haber-Bosch process) and generates substantial N2O emissions during use. By incentivising substitution toward organic fertilisers, the instrument has indirect but material GHG mitigation effects through reduced industrial energy use and agricultural N2O emissions. Mitigation relevance: indirect — primary objective is agricultural sustainability and soil health, but fertiliser substitution generates measurable GHG co-benefits.
- Instrument boundary: one parent instrument; no subscheme split.
- ID: CHNTAXVATI03S000 = CHN + TAX + VAT + I03 + S000.
- Source decision: legal basis is 财税〔2008〕56号 (MOF/SAT notice on VAT exemption for organic fertiliser products).

## CHNTAXVATI04S000 - 海上风力发电增值税即征即退50% (50% VAT refund for offshore wind power)

- Requested item: 海上风力发电增值税即征即退50% (50% VAT immediate refund for offshore wind power).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / VAT incentive.
- Rationale: This instrument provides a 50% VAT immediate refund (即征即退) for offshore wind power generation, reducing the effective VAT burden from 13% to 6.5%. Offshore wind is a high-cost, high-potential renewable energy technology that is central to China's carbon neutrality strategy. The VAT refund improves project economics and investment viability. Mitigation relevance: direct — explicitly targets deployment of zero-emission electricity generation technology.
- Instrument boundary: one parent instrument; no subscheme split.
- ID: CHNTAXVATI04S000 = CHN + TAX + VAT + I04 + S000.
- Source decision: legal basis is MOF/SAT joint notice on VAT policy for offshore wind power.

## CHNTAXEPTI01S000 - 环境保护税 (Environmental protection tax)

- Requested item: 环境保护税 (Environmental protection tax).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / Environmental pollution tax.
- New approach: Environmental pollution tax (EPT) added to the Tax group.
- Rationale: China's environmental protection tax (《中华人民共和国环境保护税法》, 2016-12-25, effective 2018-01-01) taxes air pollutants (1.2-12 yuan/pollution equivalent, with provincial rate-setting), water pollutants (1.4-14 yuan), solid waste (5-1,000 yuan/tonne), and industrial noise. It replaced the old pollutant discharge fee system (排污费). Annual revenue is approximately 200+ billion yuan. Mitigation relevance: indirect — the tax raises the cost of fossil fuel combustion by taxing associated conventional pollutants (SO2, NOx, PM), creating an implicit carbon price signal. While the statutory tax base is pollutant emissions (pollution equivalents) not GHG emissions, the IFCMA scope includes mitigation-relevant instruments with indirect climate effects.
- Instrument boundary: one parent instrument covering the unified national environmental protection tax framework; no subscheme split. Differentiated rates across pollutant categories and provincial variations are captured in Intensity/Details and Jurisdiction fields.
- ID: CHNTAXEPTI01S000 = CHN + TAX + EPT + I01 + S000.
- Source decision: legal basis is 《中华人民共和国环境保护税法》(2016-12-25, Presidential Order No. 61) and its implementing regulations (国务院令第693号).
- Review flag: confirm whether provincial rate variations warrant subscheme splitting; confirm indirect mitigation relevance classification.

## 车船税基准税率 — EXCLUDE

- Requested item: 车船税 (Vehicle and vessel tax, basic rate structure).
- Decision: exclude.
- Reason: The baseline vehicle and vessel tax rate schedule, while differentiated by engine displacement, is a general fiscal revenue instrument predating and structurally separate from climate policy. Only the climate-specific tax incentives (NEV exemption and fuel-efficient vehicle reduction) qualify for inclusion. Including the basic tax structure would over-extend the database scope to general-purpose tax instruments.

## 资源税 — EXCLUDE

- Requested item: 资源税 (Resource tax).
- Decision: exclude.
- Reason: China's resource tax is a fiscal instrument for natural resource extraction revenue distribution with no GHG-related rate differentiation or climate objective. The tax applies to crude oil, natural gas, coal, minerals, and salt based on extraction volume or revenue, not on carbon content or emissions. Its primary purposes are resource conservation and fiscal revenue sharing between central and local governments.

## 中国清洁发展机制基金取得的收入免征企业所得税 — EXCLUDE

- Requested item: 中国清洁发展机制基金取得的收入免征企业所得税 (CIT exemption for China CDM Fund income).
- Decision: exclude.
- Reason: This CIT exemption applies to one specific government-affiliated fund's own income, not to firms or individuals undertaking mitigation activities. The affected agent is the CDM Fund itself — an internal fiscal treatment rather than a behavioral incentive. The China CDM Fund's grant/loan disbursement activities could be a separate public-finance instrument, but the CIT exemption for the fund's own balance sheet is an administrative tax treatment, not a policy instrument.

## 实施清洁发展机制项目减免企业所得税 — EXCLUDE

- Requested item: 实施清洁发展机制项目减免企业所得税 (CIT reduction/exemption for implementing CDM projects).
- Decision: exclude.
- Reason: This CIT incentive for CDM project CER revenue was active during the Kyoto Protocol era. China's last new CDM projects were registered before 2013, and the CDM Executive Board has not registered new Chinese projects since. China has transitioned to the domestic CCER voluntary carbon market. The policy is effectively ended. If evidence surfaces that it remains in force, re-evaluate.

## CHNTAXCITI01S000 - 节能服务公司实施合同能源管理项目的所得定期减免企业所得税 (CIT incentive for energy performance contracting)

- Requested item: 节能服务公司实施合同能源管理项目的所得定期减免企业所得税 (Periodic CIT reduction/exemption for income from energy performance contracting projects by ESCOs).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / CIT incentive.
- Rationale: ESCOs implementing EPC projects receive a 3+3 tax holiday (first 3 years CIT-exempt, next 3 years half-rate) on project income. EPC is the primary delivery mechanism for industrial and building energy efficiency retrofits in China. By reducing the tax cost of ESCO operations, the instrument directly incentivises energy efficiency improvement. Mitigation relevance: Direct — explicitly targets energy consumption reduction through the EPC delivery model.
- Instrument boundary: one parent instrument; no subscheme split. This is the CIT counterpart to the existing EPC VAT incentive (CHNTAXVATI01S000) — distinct tax type, different mechanism (income exemption vs. VAT relief).
- ID: CHNTAXCITI01S000 = CHN + TAX + CIT + I01 + S000.
- Legal basis: Enterprise Income Tax Law Art. 27; Implementation Regulations Art. 88; 财税〔2010〕110号; 国家税务总局 国家发展改革委公告2013年第77号.

## CHNTAXCITI02S000 - 环境保护、节能节水项目企业所得税优惠 (CIT incentive for environmental protection, energy-saving and water-saving projects)

- Requested item: 环境保护、节能节水项目企业所得税优惠 (CIT incentives for environmental protection, energy-saving and water-saving projects).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / CIT incentive.
- Rationale: Qualifying environmental protection, energy-saving, and water-saving projects receive a 3+3 tax holiday (first 3 years CIT-exempt, next 3 years half-rate) on project income, starting from the first revenue-generating year. Energy-saving projects directly reduce fossil fuel consumption and associated GHG emissions. Environmental protection projects (e.g., wastewater treatment) have indirect mitigation co-benefits. The instrument operates through a defined project catalogue that determines eligibility.
- Mitigation relevance: Direct — energy-saving projects explicitly reduce energy consumption and GHG emissions.
- Instrument boundary: one parent instrument covering all project categories under the unified catalogue; no subscheme split. Differentiated project categories captured in Asset/Details fields.
- ID: CHNTAXCITI02S000 = CHN + TAX + CIT + I02 + S000.
- Legal basis: Enterprise Income Tax Law Art. 27; Implementation Regulations Art. 88; 财税〔2009〕59号; 国家税务总局公告2012年第30号; 财政部等公告2021年第36号 (updated catalogue).

## CHNTAXCITI03S000 - 环境保护、节能节水专用设备投资额抵免企业所得税 (CIT credit for investment in special equipment for environmental protection, energy-saving and water-saving)

- Requested item: 环境保护、节能节水专用设备投资额抵免企业所得税 (CIT credit for investment in special equipment for environmental protection, energy-saving and water-saving).
- Decision: include as one national-level policy instrument, separate from CHNTAXCITI02S000.
- Template: Economic instruments.
- Classification: Tax / CIT incentive.
- Rationale: Enterprises purchasing qualifying special equipment for environmental protection, energy-saving, or water-saving purposes may credit 10% of the equipment purchase price against their CIT payable in the current year. Any excess credit may be carried forward for up to five years. This is a different mechanism from CHNTAXCITI02S000 — CITI02 exempts project operating income (income-based), while CITI03 credits equipment capital expenditure (investment-based). Different economic channel, different compliance calculation, independent legal basis.
- Instrument boundary: one parent instrument; no subscheme split. Equipment categories across EP, energy-saving, and water-saving covered as one instrument with differentiation in Asset/Details.
- ID: CHNTAXCITI03S000 = CHN + TAX + CIT + I03 + S000.
- Legal basis: Enterprise Income Tax Law Art. 34; Implementation Regulations Art. 100; 财税〔2008〕48号; 财税〔2017〕71号; 财政部等公告2021年第36号 (updated equipment catalogue).

## CHNTAXCITI04S000 - 环境保护、节能节水专用设备数字化智能化改造投资抵免企业所得税 (CIT credit for digital and intelligent transformation of EP/energy/water-saving special equipment)

- Requested item: 环境保护、节能节水专用设备数字化智能化改造投资抵免企业所得税 (CIT credit for digital and intelligent transformation investment in EP/energy/water-saving special equipment).
- Decision: include as one national-level policy instrument, separate from CHNTAXCITI03S000.
- Template: Economic instruments.
- Classification: Tax / CIT incentive.
- Rationale: This instrument provides a 10% CIT credit for investment in digital and intelligent retrofitting of existing special equipment for environmental protection, energy-saving, and water-saving purposes. It is independently issued with a distinct legal basis from CHNTAXCITI03S000, covers a different eligible expenditure type (digital/intelligent retrofit of existing equipment vs. purchase of new equipment), and has a different policy timeline. The separation mirrors the dataset's approach for distinct VAT incentive instruments that share the same approach but have independent legal bases.
- Instrument boundary: one parent instrument; no subscheme split.
- ID: CHNTAXCITI04S000 = CHN + TAX + CIT + I04 + S000.
- Legal basis: Enterprise Income Tax Law Art. 34; Implementation Regulations Art. 100; 财政部 税务总局公告2024年第9号.

## CHNTAXCITI05S000 - 资源综合利用企业所得税优惠 (CIT incentive for comprehensive resource utilization)

- Requested item: 资源综合利用企业所得税优惠 (CIT incentives for comprehensive resource utilization).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Tax / CIT incentive.
- Rationale: Income from products manufactured using qualifying comprehensive-resource-utilization inputs (waste materials, residues, co-associated minerals, etc.) is taxed at a reduced rate — only 90% of the income is included in taxable income. This is the CIT counterpart to the existing VAT immediate-refund instrument (CHNTAXVATI02S000), but uses a different mechanism (taxable income reduction vs. VAT refund). Mitigation relevance: Indirect — primary objective is circular economy and resource efficiency, but the instrument generates material GHG co-benefits through avoided virgin-material production energy intensity and avoided landfill methane.
- Instrument boundary: one parent instrument covering all resource categories under the unified catalogue; no subscheme split.
- ID: CHNTAXCITI05S000 = CHN + TAX + CIT + I05 + S000.
- Legal basis: Enterprise Income Tax Law Art. 33; Implementation Regulations Art. 99; 财税〔2008〕47号; 财税〔2008〕117号; 财政部等公告2021年第36号 (updated catalogue).

## 滴灌产品免征增值税 — EXCLUDE

- Requested item: 滴灌产品免征增值税 (VAT exemption for drip irrigation products).
- Decision: exclude.
- Reason: While drip irrigation improves agricultural water efficiency and may indirectly reduce energy use for water pumping, the primary objective is water conservation, not GHG mitigation. The carbon benefit pathway is too attenuated — agricultural water pumping energy represents a tiny fraction of emissions, and water efficiency does not reliably translate to measurable GHG reductions. Including water-saving agricultural equipment would open the door to nearly any resource-efficiency tax incentive.

## CHNADPIDPI01S000 - 高耗能行业阶梯电价制度 (差别电价)

- Requested item: 高耗能行业阶梯电价制度 (Industrial differentiated electricity pricing / Differential electricity pricing for energy-intensive industries).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Administered price / Industrial differentiated electricity pricing.
- Rationale: NDRC policy (发改价格〔2004〕1383号, improved by 国办发〔2006〕77号 and subsequent notices) imposes per-kWh surcharges on electricity consumed by energy-intensive industries based on enterprise classification (permitted/encouraged, restricted, or eliminated). Initially covering 6 industries (electrolytic aluminum, ferroalloy, calcium carbide, caustic soda, cement, steel), expanded to 8 in 2006 (adding yellow phosphorus, zinc smelting). Restricted-class enterprises pay 0.05 yuan/kWh surcharge; eliminated-class enterprises pay 0.20 yuan/kWh surcharge (further raised in 2010 to 0.10 and 0.30 yuan/kWh respectively). Mitigation relevance: direct — the price incentive explicitly penalises excessive industrial electricity consumption, which is the largest driver of China's indirect energy-related GHG emissions.
- New approach: Industrial differentiated electricity pricing (IDP) added under the new Administered price (ADP) group.
- Instrument boundary: one parent instrument covering all covered energy-intensive industries under the unified national framework; no subscheme split in this first pass. Differentiated rates by enterprise category are captured in Intensity/Details.
- ID: CHNADPIDPI01S000 = CHN + ADP + IDP + I01 + S000.
- Source decision: primary legal basis is 发改价格〔2004〕1383号 (NDRC notice on differential electricity pricing pilot for high energy-consuming industries), with subsequent strengthening under 国办发〔2006〕77号, 发改价格〔2010〕978号, and the 2024-2025 energy conservation and carbon reduction action plan (节能降碳行动方案).
- Review flag: confirm whether the 8 industry categories warrant subscheme splitting given different electricity consumption profiles; confirm exact current surcharge rates per enterprise category.

## CHNADPRITI01S000 - 居民阶梯电价

- Requested item: 居民阶梯电价 (Residential increasing-block electricity pricing).
- Decision: include as one national-level policy instrument.
- Template: Economic instruments.
- Classification: Administered price / Residential increasing-block pricing.
- Rationale: NDRC 发改价格〔2011〕2617号 established a three-tier increasing-block tariff for residential electricity consumption. Tier 1 covers 80% of residential users' monthly consumption at a low base rate; Tier 2 covers 80-95% with a surcharge of at least 0.05 yuan/kWh; Tier 3 covers consumption above the 95th percentile with a surcharge of approximately 0.30 yuan/kWh (roughly 1.5× the Tier 2 rate). The marginal price incentive discourages excessive residential electricity consumption. Mitigation relevance: indirect — primary objectives are social equity (basic energy needs affordability) and demand-side management; household electricity conservation provides a secondary but material emissions reduction co-benefit.
- New approach: Residential increasing-block pricing (RIT) added under the new Administered price (ADP) group.
- Instrument boundary: one parent instrument; no subscheme split. Provincial implementation variation (different tier thresholds and rates) is captured as jurisdictional implementation, not separate instruments.
- ID: CHNADPRITI01S000 = CHN + ADP + RIT + I01 + S000.
- Source decision: primary legal basis is 发改价格〔2011〕2617号 (NDRC Guiding Opinions on Trial Implementation of Increasing-block Electricity Pricing for Residential Electricity Consumption). Framework refined by 发改价格〔2013〕2523号.
- Review flag: confirm whether provincial tier thresholds and rates warrant subscheme splitting; confirm whether 2026 rates remain consistent with 2011 framework.

## CHNADPCPMI01S000 - 发电侧容量电价机制

- Requested item: 发电侧容量电价机制 (Generation-side capacity pricing mechanism).
- Decision: include as one national-level policy instrument with four subschemes.
- Template: Economic instruments.
- Classification: Administered price / Capacity pricing mechanism.
- Rationale: China's generation-side capacity pricing reform establishes a two-part tariff (energy price + capacity price) to remunerate generators for available capacity separate from energy delivered. Four technology types are covered under two distinct legal bases with different effective dates, rate structures, and eligibility criteria.
- Subscheme decision: parent row CHNADPCPMI01S000; Coal-fired capacity pricing subscheme CHNADPCPMI01S001 (煤电容量电价, 发改价格〔2023〕1501号, effective 2024-01-01); Gas-fired capacity pricing subscheme CHNADPCPMI01S002 (天然气发电容量电价, 发改价格〔2026〕114号, effective 2026); New-type energy storage capacity compensation subscheme CHNADPCPMI01S003 (新型储能容量补偿, 发改价格〔2026〕114号); Pumped hydro storage capacity pricing subscheme CHNADPCPMI01S004 (抽水蓄能容量电价, 发改价格〔2026〕114号). The four technologies have different rate-setting methodologies: coal uses a national uniform fixed-cost standard with recovery ratio; gas is set by provincial authorities; storage is anchored to the coal benchmark with a duration-based conversion factor; pumped hydro uses a cost-of-service model differentiated by project vintage.
- Instrument boundary: one parent instrument covering the national generation-side capacity pricing framework; four subschemes split by technology type and legal basis.
- ID: CHNADPCPMI01S000 = CHN + ADP + CPM + I01 + S000.
- Source decision: coal capacity pricing established by 发改价格〔2023〕1501号 (NDRC/NEA, 2023-11-08). Gas, storage, and pumped hydro added by 发改价格〔2026〕114号 (NDRC/NEA, 2026-01-27).
- Review flag: confirm mitigation effect classification per subscheme; confirm whether provincial gas capacity pricing implementation warrants further subscheme splitting; confirm whether the post-spot-market reliable capacity compensation mechanism transition should be captured as a future revision.

## CHNPPCGPPI01S000 - 节能产品政府采购

- Requested item: 节能产品政府采购 (Energy-saving products government procurement).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public procurement / Green public procurement.
- Rationale: 财库〔2004〕185号 (MOF/NDRC, 2004-12-17) established China's first mandatory government procurement list for energy-saving products. Government agencies at all levels must prioritise or exclusively purchase products certified under the energy-saving product certification system when making procurement decisions within the listed categories. The procurement list covers energy-consuming products including air conditioners, lighting, computers, printers, monitors, transformers, electric motors, and water pumps. Mitigation relevance: direct — explicit statutory objective of reducing government energy consumption and associated GHG emissions through procurement market power.
- Instrument boundary: one parent instrument; no subscheme split. The product categories covered by the procurement list are captured in Asset/Details.
- ID: CHNPPCGPPI01S000 = CHN + PPC + GPP + I01 + S000.
- Source decision: primary legal basis is 财库〔2004〕185号 (MOF/NDRC Opinions on Implementing Government Procurement of Energy-Saving Products). The procurement list is updated periodically; current framework under 财库〔2019〕9号 (MOF notice on adjusting the energy-saving product government procurement list mechanism).
- Review flag: confirm whether the 2019 reform (财库〔2019〕9号) changed the legal status from a mandatory list to a category-based procurement preference mechanism; confirm current list revision date.

## CHNPPCGPPI02S000 - 环境标志产品政府采购

- Requested item: 环境标志产品政府采购 (Environmental labeling products government procurement).
- Decision: include as one national-level policy instrument, separate from CHNPPCGPPI01S000.
- Template: Government investment and procurement.
- Classification: Public procurement / Green public procurement.
- Rationale: 财库〔2006〕90号 (MOF/SEPA, 2006-10-24) established a parallel mandatory government procurement list for products certified under China's Environmental Labeling (十环认证) program. While CHNPPCGPPI01S000 targets energy efficiency specifically, this instrument targets broader environmental criteria (hazardous substance limits, recyclability, production process environmental management). The two lists have partially overlapping but distinct product categories and certification requirements. Mitigation relevance: indirect — primary objectives are pollution prevention and resource conservation; climate mitigation is a co-benefit through lifecycle environmental performance standards that include energy efficiency components.
- Instrument boundary: one parent instrument; no subscheme split.
- ID: CHNPPCGPPI02S000 = CHN + PPC + GPP + I02 + S000.
- Source decision: primary legal basis is 财库〔2006〕90号 (MOF/SEPA Opinions on Implementing Government Procurement of Environmental Labeling Products).
- Review flag: confirm whether the environmental labeling procurement list has been consolidated with the energy-saving list under a unified green procurement framework; confirm current list revision date.

## CHNPPCGPPI03S000 - 新能源汽车政府采购

- Requested item: 新能源汽车政府采购 (New energy vehicles government procurement).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public procurement / Green public procurement.
- Rationale: This instrument mandates government fleet procurement quotas for new energy vehicles (BEVs, PHEVs, FCEVs). Central and local government agencies are required to meet specified NEV procurement proportions when replacing or expanding official vehicle fleets. The policy uses government procurement market power to build NEV demand at scale, support domestic manufacturing, and reduce transport sector emissions from public-sector operations. Mitigation relevance: direct — explicitly replaces ICE official vehicles with zero-emission alternatives.
- Instrument boundary: one parent instrument; no subscheme split.
- ID: CHNPPCGPPI03S000 = CHN + PPC + GPP + I03 + S000.
- Source decision: primary legal basis to be confirmed — key documents include MOF/NDRC/MIIT joint notices on government NEV procurement quotas. Framework linked to State Council NEV development plan (新能源汽车产业发展规划 2021-2035).
- Review flag: confirm exact legal statute and procurement quota percentages for central vs. local government fleets; confirm whether public service vehicles (buses, sanitation, logistics) are covered under this instrument or separate mandates.

## CHNPPCGPPI04S000 - 绿色建筑和绿色建材政府采购

- Requested item: 绿色建筑和绿色建材政府采购 (Green building and green building materials government procurement).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public procurement / Green public procurement.
- Rationale: 财库〔2020〕31号 (MOF/MOHURD, 2020-10-13) launched a pilot program requiring government-funded construction projects to use green building materials and meet green building standards. Initially piloted in 6 cities (Nanjing, Hangzhou, Shaoxing, Huzhou, Qingdao, Foshan), subsequently expanded. Government procurement of construction services is conditioned on meeting specified green building standards (e.g., GB/T 50378) and using materials with green certification. Mitigation relevance: direct — buildings sector accounts for ~20% of China's carbon emissions; mandatory green procurement standards for government construction directly reduce operational and embodied carbon.
- Instrument boundary: one parent instrument; no subscheme split in this first pass. The pilot-to-national rollout transition is captured as a single continuous instrument.
- ID: CHNPPCGPPI04S000 = CHN + PPC + GPP + I04 + S000.
- Source decision: primary legal basis is 财库〔2020〕31号 (MOF/MOHURD Notice on Pilot Work for Government Procurement Supporting Green Building Materials to Promote Building Quality Improvement). Subsequent expansion notices to be added as Other weblinks.
- Review flag: confirm whether the pilot has been formally converted to a national-level mandate; confirm exact criteria for green building material certification; confirm whether operational carbon and embodied carbon are both addressed.

## CHNPPCGPPI05S000 - 绿色数据中心政府采购

- Requested item: 绿色数据中心政府采购 (Green data center government procurement).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public procurement / Green public procurement.
- Rationale: This instrument mandates green certification and energy efficiency standards for government-procured data center services and infrastructure. Government agencies are required to prioritise or exclusively select data center service providers meeting specified PUE thresholds and green certification standards. With government digital transformation driving rapid growth in public-sector data center demand, procurement-based energy efficiency requirements directly reduce ICT sector electricity consumption. Mitigation relevance: direct — explicitly imposes energy efficiency requirements on government data center procurement.
- Instrument boundary: one parent instrument; no subscheme split.
- ID: CHNPPCGPPI05S000 = CHN + PPC + GPP + I05 + S000.
- Source decision: primary legal basis to be confirmed — key sources include MIIT/NDRC/MOE joint guidance on green data center development and MOF procurement circulars specifying data center green certification requirements for government cloud service procurement.
- Review flag: confirm exact legal statute and PUE/energy efficiency thresholds; confirm whether this is a standalone procurement instrument or part of a broader green ICT procurement framework.

## CHNPIVCBII02S000 - 节能降碳中央预算内投资专项

- Requested item: 节能降碳中央预算内投资专项 (Energy Conservation and Carbon Reduction Central Budget Investment Special).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public investment / Central budget investment.
- Rationale: 发改环资规〔2025〕1228号 (NDRC, 2025-09-19, 5-year validity) supports six categories of investment projects: (1) key industry energy-saving and carbon-reduction retrofit; (2) coal consumption clean substitution; (3) circular economy for carbon reduction; (4) low/zero/negative-carbon demonstration; (5) carbon peak/neutrality capacity building; (6) other CPC/State Council assignments. The instrument name explicitly includes 降碳 (carbon reduction) and support areas directly target GHG mitigation through CCUS, zero-carbon pilots, coal substitution, and carbon accounting infrastructure. Mitigation relevance: direct — 降碳 is an explicit statutory objective of the instrument.
- New approach: none — fits under existing Central budget investment (CBI).
- Instrument boundary: one parent instrument covering all six support directions under the unified management rules; no subscheme split in this first pass.
- ID: CHNPIVCBII02S000 = CHN + PIV + CBI + I02 + S000.
- Source decision: primary legal basis is 发改环资规〔2025〕1228号 (NDRC Notice on Issuing the Administrative Measures for the Energy Conservation and Carbon Reduction Central Budget Investment Special). Replaces 发改环资规〔2024〕338号.
- Review flag: confirm whether the six support directions warrant subscheme splitting given different funding ratios (20% for four categories, 60-80% for capacity building) and asset types; confirm annual budget/expenditure figures.

## CHNPIVCBII05S000 - 生态保护修复中央预算内投资专项

- Requested item: 生态保护修复中央预算内投资专项 (Ecological Protection and Restoration Central Budget Investment Special).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public investment / Ecosystem restoration investment.
- New approach: Central budget investment (CBI) added under the Public investment group.
- Rationale: 发改农经〔2026〕713号 (NDRC, 2026-05-21, 5-year validity) supports four categories: (1) key regional ecological protection and restoration (afforestation, degraded grassland restoration, desertification control); (2) key ecological resource protection (forest/grassland fire prevention, national reserve forest, pest control); (3) nature reserve and wildlife protection (national parks, wetland restoration); (4) forestry law enforcement capacity building. Mitigation relevance: indirect — primary objectives are ecosystem protection, biodiversity conservation, and land degradation control; carbon sequestration is a substantial co-benefit. Precedent: 退耕还林还草 (CHNSUBESPI01S000), 天然林保护工程 (CHNSUBESPI05S000), and 森林生态效益补偿 (CHNSUBESPI02S000) were all included with carbon sink co-benefits even when not the primary stated objective. This instrument differs from those in being a Public investment program (infrastructure/project funding) rather than a Subsidy transfer.
- Instrument boundary: one parent instrument covering all four support categories; no subscheme split in this first pass.
- ID: CHNPIVCBII05S000 = CHN + PIV + CBI + I01 + S000.
- Source decision: primary legal basis is 发改农经〔2026〕713号 (NDRC Notice on Issuing the Administrative Measures for the Ecological Protection and Restoration Field Central Budget Investment Special). Replaces 发改农经规〔2024〕590号. Note: the predecessor 发改农经规〔2024〕590号 had already abolished and absorbed the former 农业绿色发展中央预算内投资专项管理办法 (2021).
- Review flag: confirm whether carbon sequestration is explicitly mentioned as an objective in the document text; confirm whether the four support categories warrant subscheme splitting given different regional funding ratios; confirm annual budget/expenditure.

## CHNPIVCBII03S000 - 铁路专项中央预算内投资

- Requested item: 铁路项目中央预算内投资专项 (Railway Project Central Budget Investment Special).
- Decision: include as one national-level policy instrument.
- Template: Government investment and procurement.
- Classification: Public investment / Central budget investment.
- Rationale: 发改基础规〔2025〕1516号 (NDRC, 2025-11-27, valid until 2030-12-31) provides central budget capital injections for trunk railways and intercity railways. Railways are a core low-carbon transport mode — modal shift from road and air to rail reduces GHG emissions per passenger-km and tonne-km. The IFCMA paper explicitly includes government spending on public transport and low-carbon mobility under public investment. Mitigation relevance: indirect — primary objectives are transport connectivity, economic development, and national defence; GHG reduction is a co-benefit of modal shift rather than a stated objective of the investment rules. Precedent: 县域充换电设施补短板试点 (CHNPIVCBII01S000) was included under the same approach as low-carbon transport infrastructure.
- Instrument boundary: one parent instrument covering trunk railways and intercity railways under the unified management rules; no subscheme split in this first pass.
- ID: CHNPIVCBII03S000 = CHN + PIV + CBI + I03 + S000.
- Source decision: primary legal basis is 发改基础规〔2025〕1516号 (NDRC Notice on Issuing the Administrative Measures for the Railway Special Central Budget Investment). Replaces 发改基础规〔2023〕1761号.
- Review flag: confirm whether the document mentions climate, green, or low-carbon objectives explicitly; confirm whether trunk railways and intercity railways warrant subscheme splitting given different funding ratios; confirm annual budget/expenditure figures.

## CHNFRMEPMI01S000 - 公共机构节能管理框架

- Requested item: 公共机构节能管理框架 (Energy performance management framework for public institutions).
- Decision: include as one national-level policy instrument.
- Template: Regulatory instruments.
- Classification: Framework regulation / Energy performance management framework for public institutions.
- New approach: Energy performance management framework for public institutions (EPM) added to the Framework regulation group.
- Rationale: 《公共机构节能条例》(State Council Decree 531, 2008; revised 2017) establishes a mandatory governance framework for the ~1.7 million public institutions (国家机关、事业单位、团体组织) funded by public finance. It requires energy consumption quota management, energy metering/statistics/reporting, periodic energy audits (7 audit items), and energy conservation target responsibility with performance evaluation tied to officials' performance appraisal. The regulation is a framework regulation rather than a performance standard because it establishes governance processes and institutional arrangements (planning—quota—audit—evaluation) without prescribing specific energy performance thresholds (e.g., kWh/m² caps), which are set by provincial and sectoral subsidiary rules. Although the regulated entities are public institutions, the mechanism is regulatory (mandatory quotas, audits, targets, sanctions), not government investment or procurement. Mitigation relevance: direct — public institutions account for ~5% of national building energy consumption; the regulation's explicit objective is energy conservation and emission reduction, and the 14th Five-Year Plan for Public Institution Energy and Resource Conservation sets binding targets including 5% reduction in energy consumption per unit building area and 7% reduction in carbon emissions per unit building area during 2021-2025.
- Instrument boundary: one parent instrument covering the unified national regulatory framework; no subscheme split in this first pass. Provincial and sectoral subsidiary quota rules are captured as implementing details, not separate instruments.
- ID: CHNFRMEPMI01S000 = CHN + FRM + EPM + I01 + S000.
- Source decision: primary legal basis is 《公共机构节能条例》(State Council Decree 531, 2008; revised by Decree 676, 2017-03-01). Key supporting: 《"十四五"公共机构节约能源资源工作规划》(国管局/发改委, 2021); 《公共机构能源审计管理暂行办法》(国管局/发改委, 2016).
- Review flag: confirm whether the 2026 15th Five-Year Plan successor document has been issued; confirm exact energy consumption and carbon emission data for public institutions nationally; confirm whether the 2017 revision was purely technical (no substantive changes to key provisions).

## CHNTECODSI01S000 - 消耗臭氧层物质管理条例

- Requested item: 消耗臭氧层物质管理条例 (Regulation on the Administration of Ozone-Depleting Substances).
- Decision: include as one national-level policy instrument.
- Template: Regulatory instruments.
- Classification: Technology standard / Bans and phase-outs of ozone-depleting substances.
- New approach: Bans and phase-outs of ozone-depleting substances (ODS) added to the Technology standard group.
- Rationale: 《消耗臭氧层物质管理条例》(State Council Decree No. 573, 2010; revised 2018; revised 2023 by Decree No. 770) establishes a systematic control framework for ODS and HFCs production, sale, use, import and export. It implements China's obligations under the Montreal Protocol. The 2023 revision expanded coverage to HFCs to implement the Kigali Amendment. It is classified as a Technology standard rather than a Performance standard because it bans or phases out specific substances rather than prescribing performance thresholds. Mitigation relevance: indirect — many ODS are also potent GHGs (e.g., CFC-12 has GWP ~10,200), and their phase-out has generated substantial climate co-benefits, but the regulation's primary objective is ozone layer protection.
- Instrument boundary: one parent instrument covering the unified national ODS/HFC regulatory framework; no subscheme split.
- ID: CHNTECODSI01S000 = CHN + TEC + ODS + I01 + S000.
- Source decision: primary legal basis is 《消耗臭氧层物质管理条例》(State Council Decree No. 573, 2010; revised 2018; second revision by Decree No. 770, effective 2024-03-01). Key supporting: 《中国受控消耗臭氧层物质清单》.
- Review flag: confirm annual ODS/HFC production and consumption quota data; confirm total emission reduction attributable to ODS phase-out in China.

## CHNTECHFCI01S000 - 禁止生产以HFCs为制冷剂的家用电冰箱和冰柜产品

- Requested item: 关于禁止生产以氢氟碳化物（HFCs）为制冷剂的家用电冰箱和冰柜产品的公告.
- Decision: include as one national-level policy instrument.
- Template: Regulatory instruments.
- Classification: Technology standard / Bans and phase-outs of hydrofluorocarbons (HFCs).
- New approach: Bans and phase-outs of hydrofluorocarbons (HFCs) (HFC) added to the Technology standard group.
- Rationale: 《关于禁止生产以氢氟碳化物（HFCs）为制冷剂的家用电冰箱和冰柜产品的公告》(MEE Announcement 2025 No. 27, 2025-11-15) bans the production of household refrigerators and freezers using HFCs as refrigerants from 2026-01-01. It implements the Kigali Amendment obligations under《中国履行〈关于消耗臭氧层物质的蒙特利尔议定书〉国家方案（2025—2030年）》which mandated the household refrigeration sector ban from 2026. It is a Technology standard (ban/phase-out) rather than a Performance standard because it prohibits a specific product type based on its chemical composition rather than setting energy performance thresholds. Mitigation relevance: direct — HFCs are potent GHGs with GWP hundreds to thousands of times that of CO2, and the ban directly reduces HFC emissions from the household refrigeration sector.
- Instrument boundary: one parent instrument covering the specific HFC refrigerator production ban; no subscheme split.
- ID: CHNTECHFCI01S000 = CHN + TEC + HFC + I01 + S000.
- Source decision: primary legal basis is 《关于禁止生产以氢氟碳化物（HFCs）为制冷剂的家用电冰箱和冰柜产品的公告》(MEE 2025 No. 27). Key supporting: 《中国履行〈关于消耗臭氧层物质的蒙特利尔议定书〉国家方案（2025—2030年）》.
- Review flag: confirm whether other HFC-containing product bans (e.g., foams, air conditioning, commercial refrigeration) are planned or issued and whether they should be separate instruments or subschemes; confirm market share of HFC-based refrigerators at ban effective date.

## CHNTECMEMI01S000 - 电动机能效限定值及能效等级

- Requested item: 电动机能效限定值及能效等级 (GB 18613-2020).
- Decision: include as one national-level policy instrument.
- Template: Regulatory instruments.
- Classification: Technology standard / Minimum Energy Performance Standards (MEPS) for electric motors.
- Rationale: GB 18613-2020 is a mandatory national standard setting minimum energy efficiency requirements for general-purpose electric motors (three-phase asynchronous, single-phase asynchronous, air conditioner fan motors). It sets IE3 as the minimum efficiency threshold. It is a Technology standard in the IFCMA taxonomy. Mitigation relevance: direct — motors account for approximately 60% of industrial electricity consumption, and higher efficiency standards directly reduce electricity-related emissions.
- Instrument boundary: one parent instrument covering the unified motor MEPS standard for general-purpose motors; distinct from the two specialised motor standards (GB 30253, GB 30254) which cover specific motor sub-types.
- ID: CHNTECMEMI01S000 = CHN + TEC + MEM + I01 + S000.
- Source decision: primary legal basis is GB 18613-2020《电动机能效限定值及能效等级》(published 2020-05-29, effective 2021-06-01). Replaces GB 18613-2012 and GB 25958-2010.
- Review flag: confirm China's motor efficiency market shares by grade at standard effective date; confirm whether IE4/IE5 upgrade pathway has been announced.

## CHNTECMEMI02S000 - 永磁同步电动机能效限定值及能效等级

- Requested item: 永磁同步电动机能效限定值及能效等级 (GB 30253-2024).
- Decision: include as one national-level policy instrument.
- Template: Regulatory instruments.
- Classification: Technology standard / Minimum Energy Performance Standards (MEPS) for electric motors.
- Rationale: GB 30253-2024 is a mandatory national standard setting minimum energy efficiency requirements for permanent magnet synchronous motors, replacing GB 30253-2013. The 2024 revision extends the power range to 0.55–1,000 kW and adds high-voltage motor requirements. Mitigation relevance: direct — permanent magnet motors are more efficient than induction motors and are increasingly used in energy-saving applications.
- Instrument boundary: one parent instrument; distinct from the general motor MEPS (GB 18613) and high-voltage motor MEPS (GB 30254).
- ID: CHNTECMEMI02S000 = CHN + TEC + MEM + I02 + S000.
- Source decision: primary legal basis is GB 30253-2024《永磁同步电动机能效限定值及能效等级》(effective 2025-10-01). Replaces GB 30253-2013.
- Review flag: confirm market penetration of permanent magnet motors and energy savings attributable to the standard upgrade.

## CHNTECMEMI03S000 - 高压三相笼型异步电动机能效限定值及能效等级

- Requested item: 高压三相笼型异步电动机能效限定值及能效等级 (GB 30254-2024).
- Decision: include as one national-level policy instrument.
- Template: Regulatory instruments.
- Classification: Technology standard / Minimum Energy Performance Standards (MEPS) for electric motors.
- Rationale: GB 30254-2024 is a mandatory national standard setting minimum energy efficiency requirements for high-voltage three-phase cage asynchronous motors, replacing GB 30254-2013. The 2024 revision extends coverage to explosion-proof motors and raises the energy efficiency threshold. Mitigation relevance: direct — high-voltage motors are used in heavy industry with large unit capacities, so efficiency gains generate substantial absolute energy savings.
- Instrument boundary: one parent instrument; distinct from the general motor MEPS (GB 18613) and permanent magnet motor MEPS (GB 30253).
- ID: CHNTECMEMI03S000 = CHN + TEC + MEM + I03 + S000.
- Source decision: primary legal basis is GB 30254-2024《高压三相笼型异步电动机能效限定值及能效等级》(effective 2025-09-01). Replaces GB 30254-2013.
- Review flag: confirm the population and total capacity of high-voltage motors covered and energy savings from the raised threshold.

## CHNTECBFHI01S000 - 禁止新建和逐步淘汰燃煤锅炉

- Requested item: 禁止新建和逐步淘汰燃煤锅炉 (Ban on new coal-fired boilers and phase-out of existing units).
- Decision: include as one national-level policy instrument.
- Template: Regulatory instruments.
- Classification: Technology standard / Bans and phase-outs of fossil fuel heating systems.
- Rationale: China's Air Pollution Prevention and Control Law (2015) and subsidiary action plans establish a comprehensive regulatory regime banning new coal-fired boilers and phasing out existing ones. The policy is classified as a Technology standard (ban/phase-out of fossil fuel heating systems) rather than a Performance standard because it prohibits specific equipment types rather than setting emission performance thresholds. Mitigation relevance: indirect — the primary objective is air quality improvement through SO2, NOx and PM reduction; CO2 reduction is a co-benefit of coal displacement.
- Instrument boundary: one parent instrument covering the national coal boiler ban/phase-out framework; provincial implementation variations are captured as implementing details, not separate instruments or subschemes.
- ID: CHNTECBFHI01S000 = CHN + TEC + BFH + I01 + S000.
- Source decision: primary legal basis is 《中华人民共和国大气污染防治法》(revised 2015-08-29, effective 2016-01-01). Key supporting: 《空气质量持续改善行动计划》(国发〔2023〕24号); 《锅炉绿色低碳高质量发展行动方案》(发改环资〔2023〕1638号).
- Review flag: confirm number of coal-fired boilers eliminated nationally and remaining stock by size category; confirm CO2 emission reduction attributable to coal boiler phase-out programme.

## 企业温室气体排放核算与报告指南 — EXCLUDE (supporting reference)

- Requested item: 企业温室气体排放核算与报告指南 (Enterprise GHG emission accounting and reporting guidelines — the sectoral 核算方法与报告指南 series).
- Decision: exclude as a standalone instrument; retain as the technical basis of an existing instrument.
- Reason: The accounting/reporting guidelines are the calculation methodology operationalised by the existing reporting-and-verification instrument CHNREPGRVI01S000 (重点行业企业温室气体排放报告与核查制度, Group 报告与披露要求 / Approach 温室气体排放报告). They define *how* covered entities compute emissions once obligated to report; their mitigation effect flows through the reporting/verification obligation and the ETS, not independently. CHNREPGRVI01S000 already documents them as its technical basis in four fields (描述, 要求说明 item 1, 工具联动 "与碳排放标准（核算指南）联动", and 信息采集责任方). Coding them separately would double-count the same reporting effect.
- Existing row it relates to: CHNREPGRVI01S000. No edit required — the guidelines remain a supporting reference within that instrument.
- Re-evaluate if: the guidelines come to function as the economy-wide national carbon-accounting standard with reach independent of the mandatory ETS reporting scheme (e.g., product carbon footprint, corporate ESG/voluntary disclosure, or GHG inventory use); in that case code standalone as a Regulatory / Standards instrument (a measurement/methodology standard), not an Information instrument.

## 工业重点行业领域设备更新和技术改造指南 — EXCLUDE (supporting reference)

- Requested item: 工业重点行业领域设备更新和技术改造指南 (MIIT 工信厅规〔2024〕33号, 23/05/2024, advisory).
- Decision: exclude as a standalone instrument; retain as a supporting reference.
- Reason: This guide operationalises the large-scale equipment renewal (大规模设备更新) action plan already captured by the equipment-renewal loan subsidy (CHNSUBCLGI03S000) and trade-in subsidies (CHNSUBTISI01S000, CHNSUBTISI02S000, CHNSUBVPSI01-04S000). The guide tells firms HOW to implement equipment renewal; its behavioural effect flows through those subsidy instruments, not independently. Coding it separately would double-count the same equipment-renewal effect.
- Existing rows it relates to: CHNSUBCLGI03S000, CHNSUBTISI01S000, CHNSUBTISI02S000, CHNSUBVPSI01-04S000.

## 绿色建造技术导则（试行） — EXCLUDE (supporting reference)

- Requested item: 绿色建造技术导则（试行）(MOHURD 建办质〔2021〕9号, 16/03/2021, advisory/trial).
- Decision: exclude as a standalone instrument.
- Reason: Generic construction-phase guidance (planning → design → construction → delivery) with no specific quantitative thresholds. Its effect flows through green building procurement (CHNPPCGPPI04S000) and building energy efficiency standards; the guide provides soft technical detail but does not create independent behavioural incentives. The original MOHURD URL is now 404 (MOHURD site restructured in 2022). No discrete, attributable mitigation effect beyond what the green-building framework already captures.

## 制造企业绿色供应链管理实施指南 — EXCLUDE (wrong instrument type; a national standard)

- Requested item: 制造企业绿色供应链管理实施指南.
- Decision: exclude from Information/CBA consideration.
- Reason: This is a recommended national standard (GB/T 43902-2024) issued by SAMR/SAC (effective 01/08/2024), NOT a ministry-issued technical guidance document. It falls under the IFCMA Regulatory instruments / Framework standard category. If coded at all, it belongs under Regulatory, not Information instruments. The GB/T is recommended (推荐性) not mandatory, so its standalone regulatory effect is weak; it would need its own Regulatory approach.
- Re-evaluate if: the user wishes to code GB/T standards systematically.

## 农业绿色发展技术导则（2018-2030年） — EXCLUDE (too broad, attenuated)

- Requested item: 农业绿色发展技术导则（2018-2030年）(农业农村部 农科教发〔2018〕3号, 02/07/2018, advisory, 2018-2030 horizon).
- Decision: exclude.
- Reason: A strategic sectoral planning document covering 7 task areas across the entire agricultural chain (inputs, production, processing, breeding, villages, R&D, standards). Too diffuse to be a discrete policy instrument with attributable mitigation effect. Precedent: 农田建设补助 EXCLUDE — the same gate applies. Agricultural productivity/development instruments without a discrete, measurable climate pathway are excluded.

## 生态环境导向的开发（EOD）项目实施导则（试行） — EXCLUDE (too attenuated)

- Requested item: 生态环境导向的开发（EOD）项目实施导则（试行）(MEE/NDRC/PBOC/NFRA 环办科财〔2023〕22号, 27/12/2023, advisory/trial).
- Decision: exclude.
- Reason: The primary objectives are ecological restoration and project self-financing (bundling eco-governance with revenue-generating industries), not GHG mitigation. The climate pathway is too indirect — eco-environmental improvement may have some carbon co-benefits, but there is no discrete, attributable mitigation effect from the implementation methodology itself. Precedent: 农田建设补助 EXCLUDE (same gate — too attenuated).
- Re-evaluate if: the EOD model is later shown to generate material, quantifiable GHG reductions through, e.g., ecosystem carbon sequestration outcomes.

## 工业产品绿色设计指南（2026年版） — EXCLUDE (soft advisory, borderline)

- Requested item: 工业产品绿色设计指南（2026年版）(MIIT/NDRC/MOE/MEE/SAMR 工信厅联节〔2026〕15号, 01/04/2026, advisory).
- Decision: exclude as a standalone instrument.
- Reason: This is a soft advisory guide defining 11 green-design directions and 126 solutions across 15 industries. Mitigation link is indirect (lifecycle environmental design philosophy) and the guide has no classification/eligibility function comparable to TPC or IGC. Its effect is too diffuse to credit as a discrete instrument. Comparable in form but weaker than the included TGC documents.
- Re-evaluate if: the guide gains a certification, procurement preference, or financial-incentive linkage that gives it harder behavioural effect.

## 村镇微能网建设试点 — EXCLUDE

- Requested item: 国家能源局综合司关于深入推进农村能源革命 开展村镇微能网建设试点工作的通知（国能综通新能〔2026〕75号，2026年7月14日制发）.
- Decision: exclude.
- Reason: Investment is by grid companies and third-party investors under government directive, not direct central fiscal expenditure. Falls short of IFCMA's "Public investment" definition (spending by a government unit toward fixed capital). The instrument is better characterised as government planning/guidance directing SOE investment rather than a discrete budgetary instrument. Also at very early stage — pilot applications not yet submitted.
- Re-evaluate if: central fiscal funds are later allocated to the pilot, or if the programme evolves into a direct government investment mechanism.

## PAE approach renamed — deviation from IFCMA Approaches Table naming

- Approach: Performance assessment and evaluation → Climate performance assessment and evaluation (CN: 绩效评估考核 → 气候绩效评估考核). Code PAE → CPA; PID CHNPARPAEI01S000 → CHNPARCPAI01S000.
- Decision: rename (14/08/2026). The IFCMA table name was judged too generic to distinguish the approach from Target responsibility system (TRS) and Green finance performance evaluation (GFE). Adding "Climate" retains the open agent scope (sub-national governments, public agencies, other designated entities). "Public institutions" (公共机构) was considered and rejected — the only instrument under CPA, 碳达峰碳中和综合评价考核办法, assesses provincial party committees and governments; public-institution carbon intensity is only one indicator among many.
- Affected instrument: CHNPARCPAI01S000 — Emission sector changed from the five-sector enumeration (Energy; Industry; Buildings; Transport; AFOLU) to Cross-sectoral (跨部门), consistent with other whole-economy instruments.
- Files updated: rules/schema.yaml, inputs/classification/approaches_cn.md, approaches_en.md, outputs CSVs (CN+EN), outputs/evidence_log.csv, generate_english_from_chinese.py.

## PAR instruments: Emission sector → Cross-sectoral

- Decision (14/08/2026): CHNPARSEAI01S000 (战略环境评价), CHNPAREIAI01S000 (环境影响评价), CHNPARECRI01S000 (投资项目节能减排评价) — Emission sector changed from enumerated sector lists to Cross-sectoral (跨部门).
- Rationale: statutory coverage of all three is economy-wide (SEA: "一地、两域、十专项"; EIA: all construction projects under classified management; ECR: all fixed-asset investment projects meeting energy thresholds). The enumerations were incomplete (omitting waste, and AFOLU/waste respectively) and implied sector limits that do not exist in law. Consistent with CHNPARCPAI01S000 (CPA) which was set to Cross-sectoral as a whole-economy instrument. Contrast: CHNPARECAI01S000 (环境合规审计) remains 工业 — its statutory scope is limited to industrial facilities.
- Files updated: outputs CSVs (CN+EN), outputs/evidence_log.csv, generate_english_from_chinese.py.

## Emission sector: whole-economy adjustments (second round)

- Decision (14/08/2026), extending the PAR Cross-sectoral change:
  - CHNREPSIDI01S000 (企业环境信息依法披露制度): 工业 → Cross-sectoral (跨部门) — five mandatory disclosure categories include all listed companies and bond issuers regardless of sector; consistent with CHNREPSIDI02S000.
  - CHNPIVGIFI01S000 (国家绿色发展基金) and CHNSUBCLGI04S000 (中国清洁发展机制基金): five-sector enumeration → Cross-sectoral — investment scope covers pollution control (incl. waste), ecological restoration, green transport and clean energy, i.e. all sectors; CLGI01-03 already Cross-sectoral.
  - CHNREPGRVI01S000 (重点行业企业温室气体排放报告与核查): 工业；交通 → 能源；工业；交通 — statutory coverage of the eight key industries includes power generation (能源).
  - CHNVTSVCMI01S000 (CCER parent): kept enumeration per user decision; fixed errors — normalised ASCII semicolons to full-width and added the missing 建筑 to the EN row (CN/EN previously inconsistent). Sectors: AFOLU；能源；交通；工业；建筑.
  - CHNTAXEPTI01S000 (环境保护税): kept 能源；工业；废弃物 scope, normalised ASCII semicolons only.
  - Checked, no change: 低碳技术目录 (statutory scope = five listed sectors, waste not covered), 公共机构能源统计 (建筑；交通 = buildings + official vehicles), 绿色制造标准体系/绿色工厂 (manufacturing only), 排污许可 (industrial-dominated).
- Files updated: outputs CSVs (CN+EN), outputs/evidence_log.csv, generate_english_from_chinese.py.

## Emission sector: CHNCBATPCI05S000 工业领域电力需求侧管理产品（技术）参考目录

- Decision (14/08/2026): 工业；能源 → 工业 (EN: Industry; Energy → Industry).
- Rationale: statutory scope is explicitly 工业领域 — the catalogue targets industrial enterprises' demand-side management. The energy sector (generation/supply) is not covered; electricity is the medium of industrial indirect emissions, not a covered sector. Consistent with sibling rows (电动机MEPS = 工业; TBPCI01 = 工业).
- Files updated: outputs CSVs (CN+EN), generate_english_from_chinese.py. No evidence-log emission row exists for this instrument.

## CHNPPCGPPI02S000 环境标志产品政府采购 — asset evidence enrichment

- Decision (14/08/2026): emission sector 工业；建筑；交通 verified correct and kept (财库〔2019〕18号品目清单 includes vehicle categories 载货汽车/乘用车/客车/专用车辆 per HJ2532); enriched the 受规制资产 and 受规制资产（详情） fields to include the vehicle categories, with the MOF original URL (gks.mof.gov.cn 20190329) as source.
- Cross-sectoral was considered and rejected: the catalogue is a finite 50-item product list covering three sectors only (no energy, AFOLU or waste products); consistent with the sibling GPP instruments' sector enumerations.
- Files updated: outputs CSVs (CN+EN), outputs/evidence_log.csv, generate_english_from_chinese.py.

## Emission sector: CHNCBATPCI02S000 国家重点推广的低碳技术目录 → Cross-sectoral

- Decision (14/08/2026): 能源；工业；建筑；交通；AFOLU → 跨部门 (EN: Cross-sectoral).
- Rationale: the fourth batch (环办气候函〔2022〕484号) includes municipal solid waste treatment technology (生活垃圾生态化前处理和水泥窑协同后处置技术), so all six emission sectors are covered across the catalogue's batches. The catalogue's stated purpose is to guide all industries (引导各行业). Consistent with CHNCBATPCI03S000 绿色技术推广目录, already Cross-sectoral. Description updated to mention 废弃物处理.
- Files updated: outputs CSVs (CN+EN), generate_english_from_chinese.py. No evidence-log rows exist for this instrument.

## Emission sector: CHNTAXEPTI01S000 环境保护税 → Cross-sectoral

- Decision (14/08/2026): 能源；工业；废弃物 → 跨部门 (EN: Cross-sectoral).
- Rationale: the taxpayer definition is universal — all enterprises, institutions and other producers/operators directly discharging taxable pollutants, regardless of sector. The statutory exemptions are partial carve-outs within sectors, not sector exclusions: large-scale livestock farming remains taxable (AFOLU), fixed transport facilities remain taxable (transport), and directly discharging buildings remain taxable (buildings). All six sectors have statutory tax situations; the emission-sector field cannot express "all sectors with carve-outs", so Cross-sectoral plus a documented exemption clause is the faithful representation. Consistent with the universal-base precedent (EIA, CPA, 重点用能单位). Description updated with the exemption clause (agricultural production excluding large-scale livestock; mobile sources).
- Files updated: outputs CSVs (CN+EN), outputs/evidence_log.csv, generate_english_from_chinese.py.

## Emission sector: CHNFRMEPRI03S000 新能源汽车废旧动力电池回收和综合利用管理 → 工业；废弃物

- Decision (14/08/2026): 工业 → 工业；废弃物 (EN: Industry; Waste).
- Rationale: the 规章 regulates two lifecycle phases, unlike WEEE which regulates only the waste phase: (1) production phase (工业) — battery enterprises must code and label batteries, establish digital IDs and upload production information to the national traceability platform; (2) end-of-life phase (废弃物) — collection, testing, dismantling and regeneration of waste batteries, plus the ban on non-design-purpose use. The old value 工业 captured only the traceability requirements and missed the waste phase, which is the instrument's core. Parent 生产者责任延伸制度 (跨部门) and WEEE (废弃物) reviewed and kept as-is: the parent framework spans six product categories used economy-wide; the WEEE 条例 regulates only the waste phase.
- Files updated: outputs CSVs (CN+EN), outputs/evidence_log.csv, generate_english_from_chinese.py.

## Approach rename: 行为规范 → 公民行为规范 (Code of conduct → Citizen code of conduct)

- Decision (14/08/2026): renamed the approach display name; code COC and instrument ID CHNCBACOCI01S000 unchanged.
- Rationale: the approach definition is already citizen-scoped (guiding citizens' ecological and environmental behaviour); the sole instrument under it is 公民生态环境行为规范十条; the generic 行为规范 was ambiguous with corporate codes of conduct. Consistent with the Public awareness campaign (公众宣传教育活动) precedent of naming the target audience. English name mirrors: Citizen code of conduct.
- Files updated: rules/schema.yaml, inputs/classification/approaches_cn.md, approaches_en.md, outputs CN/EN information instruments CSVs (Approach cell only), generate_english_from_chinese.py structural map, scripts/_add_inf_coc.py.

## Approach rename (CN): 自愿信息披露 → 自愿性信息披露

- Decision (14/08/2026): renamed the Chinese display name of the VID approach; English name "Voluntary information disclosure" and code VID unchanged.
- Rationale: 自愿性信息披露 is the established Chinese term for voluntary disclosure (contrasting 强制性信息披露); the DB's other voluntary approaches already use the 性 form where the fixed term exists (自愿性采购指南 VPG, 自愿性认证标识 VLB, 自愿性目标 VTS).
- Files updated: inputs/classification/approaches_cn.md, outputs/CCPID_cn_voluntary_approaches.csv (2 VID rows, 路径 cell), generate_english_from_chinese.py structural map, scripts/_add_vol_vid.py.

## Category rename: 政府投资与采购 → 政府投资与消费 (Government investment and procurement → Government investment and consumption)

- Decision (14/08/2026): renamed the Government I&C category to align with the IFCMA source typology (inputs/methodology/IFCMA_typology.md uses "Government investment and consumption"). Template key "Government I&C" unchanged; CSV data rows unaffected (Group column stores group names, not the category name).
- Rationale: procurement names only one of the three groups (public investment, public procurement, public appraisal rules); the IFCMA category definition covers shaping government expenditure choices and decision-making processes, which 消费/consumption captures. I&C already abbreviates Investment & Consumption.
- Files updated: rules/schema.yaml, inputs/classification/approaches_cn.md, approaches_en.md, inputs/fields/field_dictionary.md, scripts/fill_instrument.py, validate_dataset.py, export_workbooks.py, generate_english_from_chinese.py. Historical decision entries keep the old name as a record.

## Terminology unification: 管制价格 → 行政定价 (Administered price)

- Decision (14/08/2026): unified the Chinese group name for Administered price on 行政定价; removed the last remaining 管制价格 (a static label cell B14 in the summary sheet of inputs/template_cn.xlsx that leaked into the exported workbook).
- Rationale: all live data (CSVs, classification files, fill/export scripts, other workbook sheets) already use 行政定价, which also renders IFCMA's "Administered price" more precisely (行政定价 vs 市场定价); 管制价格 is associated with general price controls and was a leftover.
- Files updated: inputs/template_cn.xlsx (zip-level cell text edit). No CSV/schema/script changes needed.
