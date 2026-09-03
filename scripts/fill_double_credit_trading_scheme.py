#!/usr/bin/env python3
"""Recode China's passenger-vehicle dual-credit measures as a trading scheme."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

from fill_instrument import (
    DEFAULT_EVIDENCE_LOG,
    append_evidence,
    apply_defaults,
    build_field_aliases,
    canonicalise_fields,
    default_dataset_path,
    fill_empty_template_cells,
    get_row_value,
    get_template_columns,
    load_templates,
    read_csv,
    write_csv,
)


ECONOMIC_TEMPLATE = "Economic instruments"
REGULATORY_TEMPLATE = "Regulatory instruments"

OLD_IDS = {
    "CHNREGFUEI01S000",
    "CHNREGFUEI01S001",
    "CHNREGFUEI01S002",
    "CHNREGEVSI01S000",
    "CHNTRARECI03S000",
    "CHNTRARECI03S001",
    "CHNTRARECI03S002",
    "CHNTRATPSI01S000",
    "CHNTRATPSI01S001",
    "CHNTRATPSI01S002",
}

OFFICIAL_MEASURE_URL = "https://www.gov.cn/zhengce/2022-11/27/content_5722693.htm"
ORIGINAL_MEASURE_URL = "https://www.gov.cn/zhengce/content/2017-09/28/content_5228217.htm"
AMENDMENT_2020_URL = "https://www.gov.cn/zhengce/zhengceku/2020-06/22/content_5521144.htm"
AMENDMENT_2023_URL = "https://wap.miit.gov.cn/jgsj/zbys/gzdt/art/2023/art_02e935e2cce74be4a641d7b8ca5621b4.html"
NOTICE_2025_URL = "https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2025/art_c22055da7deb48c397ad16247beaff22.html"
TENCENT_MARKET_URL = "https://news.qq.com/rain/a/20240412A06XQR00"


def meta(url: str, title: str, quote: str, note: str) -> dict[str, str]:
    return {
        "source_url": url,
        "source_title": title,
        "evidence_quote": quote,
        "confidence_score": "0.86",
        "needs_human_review": "true",
        "review_note": note,
    }


SOURCE_MEASURE = meta(
    OFFICIAL_MEASURE_URL,
    "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法",
    "本办法所称乘用车企业平均燃料消耗量与新能源汽车积分并行管理，是指对乘用车企业平均燃料消耗量积分、新能源汽车积分分别核算、合并考核。",
    "Official consolidated measure page supplied by reviewer.",
)

SOURCE_CAFC = meta(
    OFFICIAL_MEASURE_URL,
    "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法",
    "乘用车企业平均燃料消耗量积分为该企业平均燃料消耗量达标值与实际值之间的差额，与其乘用车生产量或者进口量的乘积。",
    "Official consolidated measure page supplied by reviewer.",
)

SOURCE_NEV = meta(
    NOTICE_2025_URL,
    "关于2026—2027年度乘用车企业平均燃料消耗量与新能源汽车积分管理有关事项的通知",
    "2026年度、2027年度的新能源汽车积分比例要求分别为48%和58%。",
    "Latest MIIT operational notice found by reviewer; official consolidated measure remains the Legal document.",
)

SOURCE_2025 = meta(
    NOTICE_2025_URL,
    "关于2026—2027年度乘用车企业平均燃料消耗量与新能源汽车积分管理有关事项的通知",
    "现就2026—2027年度乘用车企业平均燃料消耗量和新能源汽车积分管理有关事项通知如下。",
    "Latest MIIT operational notice for 2026-2027 CAFC and NEV credit management.",
)


COMMON_CN = {
    "Group": "交易机制",
    "Approach": "可交易绩效标准",
    "Emission sector": "交通",
    "Sub-sector": "道路交通",
    "Policy Package": "N/A",
    "Objective": "能源效率；工业发展",
    "Mitigation relevance": "直接",
    "Functioning channel": "供给侧",
    "Country": "中国",
    "Jurisdiction level": "国家",
    "Jurisdiction name": "N/A",
    "Adoption date": "27/09/2017",
    "Start date": "01/04/2018",
    "End date": "N/A",
    "Last revisions": "07/11/2025",
    "Status": "生效",
    "Administrating authorities": "工业和信息化部；财政部；商务部；海关总署；市场监管总局",
    "Asset": "道路运输车辆",
    "Asset (Status)": "新建",
    "Asset (Other)": "N/A",
    "Agent": "企业",
    "Agent (Detail)": "中国境内乘用车生产企业和进口乘用车供应企业。",
    "Activity": "生产、销售或进口",
    "Tax and Tax Incentive: annual revenue": "",
    "Tax and Tax Incentive: earmarked revenue": "",
    "Tax and Tax Incentive: annual revenue forgone": "",
    "Subsidy: annual budget/ expenditure": "",
    "Subsidy: Limit": "",
    "Subsidy: Floor or ceiling": "",
    "Subsidy: distribution mechanism": "",
    "Subsidy: Support duration": "",
    "Subsidy: Enforcement Mechanism": "",
    "GHG emission coverage (absolute)": "未找到",
    "GHG emission coverage (% domestic emissions)": "未找到",
    "Economic sector": "C29; G45",
    "GHGs affected": "CO2",
    "Mitigation effects": "正向",
    "Legal statute": "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法",
    "Legal document": OFFICIAL_MEASURE_URL,
    "Other weblinks": f"{ORIGINAL_MEASURE_URL}; {AMENDMENT_2020_URL}; {AMENDMENT_2023_URL}; {NOTICE_2025_URL}; {TENCENT_MARKET_URL}",
}

COMMON_EN = {
    "Group": "Trading scheme",
    "Approach": "Tradable performance standards",
    "Emission sector": "Transport",
    "Sub-sector": "Road transport",
    "Policy Package": "N/A",
    "Objective": "Energy efficiency; Industrial development",
    "Mitigation relevance": "Direct",
    "Functioning channel": "Supply-side",
    "Country": "CHN",
    "Jurisdiction level": "national",
    "Jurisdiction name": "N/A",
    "Adoption date": "27/09/2017",
    "Start date": "01/04/2018",
    "End date": "N/A",
    "Last revisions": "07/11/2025",
    "Status": "in force",
    "Administrating authorities": (
        "Ministry of Industry and Information Technology; Ministry of Finance; "
        "Ministry of Commerce; General Administration of Customs; State Administration for Market Regulation"
    ),
    "Asset": "Road transport vehicles",
    "Asset (Status)": "New",
    "Asset (Other)": "N/A",
    "Agent": "Firms",
    "Agent (Detail)": "Passenger vehicle manufacturers in China and imported passenger vehicle suppliers.",
    "Activity": "Production, sale or import",
    "Tax and Tax Incentive: annual revenue": "",
    "Tax and Tax Incentive: earmarked revenue": "",
    "Tax and Tax Incentive: annual revenue forgone": "",
    "Subsidy: annual budget/ expenditure": "",
    "Subsidy: Limit": "",
    "Subsidy: Floor or ceiling": "",
    "Subsidy: distribution mechanism": "",
    "Subsidy: Support duration": "",
    "Subsidy: Enforcement Mechanism": "",
    "GHG emission coverage (absolute)": "not found",
    "GHG emission coverage (% domestic emissions)": "not found",
    "Economic sector": "C29; G45",
    "GHGs affected": "CO2",
    "Mitigation effects": "positive",
    "Legal statute": (
        "Parallel Management Measures for Passenger Vehicle Corporate Average Fuel Consumption "
        "and New Energy Vehicle Credits"
    ),
    "Legal document": OFFICIAL_MEASURE_URL,
    "Other weblinks": f"{ORIGINAL_MEASURE_URL}; {AMENDMENT_2020_URL}; {AMENDMENT_2023_URL}; {NOTICE_2025_URL}; {TENCENT_MARKET_URL}",
}


ROWS_CN = [
    (
        "CHNTRATPSI01S000",
        SOURCE_2025,
        {
            **COMMON_CN,
            "Policy Instrument ID": "CHNTRATPSI01S000",
            "Instrument / subscheme": "工具",
            "Domestic instrument name": "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法",
            "English instrument name": "Passenger vehicle CAFC and NEV dual-credit trading scheme",
            "Description": (
                "该办法建立平均燃料消耗量积分和新能源汽车积分并行管理的可交易绩效标准机制。企业"
                "按年度形成 CAFC 正/负积分和 NEV 正/负积分，并通过结转、转让、购买、积分池等"
                "方式完成负积分抵偿和合规。"
            ),
            "Last revisions (Details)": "工业和信息化部2025年11月7日印发2026—2027年度积分管理事项通知，规定2026、2027年度新能源汽车积分比例分别为48%和58%，明确低油耗乘用车核算倍数、新能源车型积分计算方法和循环外节能技术减免衔接安排。",
            "Asset (Details)": "在中国境内销售的乘用车，包括境内生产和进口乘用车；父工具覆盖 CAFC 和 NEV 两类积分。",
            "Asset (Cut-off range)": "年度生产量或者进口量达到2000辆及以上的乘用车企业纳入积分核算。",
            "Activity (Details)": "乘用车生产、进口和销售，以及 CAFC/NEV 积分核算、结转、转让、交易、积分池管理和负积分抵偿。",
            "Intensity (Value)": "N/A",
            "Intensity (Unit)": "N/A",
            "Intensity (Details)": "父工具包含两个积分子方案：CAFC 子方案使用燃料消耗量目标核算，NEV 子方案使用年度新能源汽车积分比例核算；最新通知规定2026、2027年度 NEV 积分比例分别为48%和58%（来源：工信部2025年通知）。",
            "Requirement specification": "乘用车企业应分别满足平均燃料消耗量积分和新能源汽车积分要求；负积分应按办法规定抵偿归零。",
            "Compliance calculation methodology I": "CAFC 积分按企业平均燃料消耗量达标值与实际值之差乘以企业乘用车核算数量计算。",
            "Compliance calculation methodology II": "NEV 积分目标值由传统能源乘用车核算数量乘以年度新能源汽车积分比例确定；实际值与目标值之差形成正/负积分。",
            "Trading System: Type": "可交易绩效标准；乘用车企业平均燃料消耗量积分和新能源汽车积分并行管理机制。",
            "Trading System: cap": "未设置固定绝对总量上限；合规义务由企业燃料消耗量达标值、新能源汽车积分比例和企业生产/进口规模共同决定。",
            "Trading System: allowance mechanism": "积分由企业车型燃料消耗量表现、新能源汽车车型积分和年度生产/进口量核算产生；正积分可按办法结转、转让、交易或进入积分池。",
            "Trading System: Free Allowance": "不适用；该制度不分配免费配额，积分由企业绩效核算产生。",
            "Trading System: Offset use allowed": "允许。CAFC 负积分可按规则使用 CAFC 正积分和 NEV 正积分抵偿；NEV 负积分主要通过购买 NEV 正积分抵偿。",
            "Trading System: Linkages": "N/A",
            "Trading System: market stabilisation mechanism": "2023年修订建立新能源汽车积分池管理制度；CAFC 正积分也有结转和关联企业转让规则。",
            "Trading System: revenue (annual)": "30.5亿元（2022年度新能源汽车积分交易总额；来源：工信部2022年度双积分实施情况报告，转引电车汇/腾讯新闻2024-04-12）。未找到2023年度或更新实际交易总额。",
            "Trading System: Volume": "约270万分（2022年度交易量估算，按交易总额30.5亿元/交易订单均价1128元/分计算；来源：电车汇/腾讯新闻2024-04-12）；2023年度抵偿需求约342万分（需求量，非实际成交量；来源：同上）。未找到2023年度或更新实际成交量。",
            "Trading System: penalties for non-compliance": "负积分未抵偿归零的企业需提交调整计划，并可能受到车型公告、产品申报或进口管理限制；弄虚作假、拒不配合核查等按办法处理。",
            "Mitigation co-benefits": "空气污染；能源供应安全；技术创新；工业发展",
        },
    ),
    (
        "CHNTRATPSI01S001",
        SOURCE_2025,
        {
            **COMMON_CN,
            "Policy Instrument ID": "CHNTRATPSI01S001",
            "Instrument / subscheme": "子方案",
            "Domestic instrument name": "乘用车企业平均燃料消耗量积分子方案",
            "English instrument name": "Passenger vehicle corporate average fuel consumption credit subscheme",
            "Policy Package": "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法",
            "Description": "该子方案对乘用车企业平均燃料消耗量进行年度核算，形成 CAFC 正积分或负积分，并规定结转、转让和负积分抵偿规则。",
            "Objective": "能源效率",
            "Last revisions (Details)": "工业和信息化部2025年11月7日通知规定2026—2027年度 CAFC 相关核算安排：小规模企业 CAFC 达标值放宽条件、低油耗乘用车按0.1倍核算、循环外节能技术减免继续衔接执行。",
            "Asset (Details)": "传统能源乘用车和纳入企业平均燃料消耗量核算的乘用车车型。",
            "Asset (Cut-off range)": "年度生产量或者进口量达到2000辆及以上的乘用车企业纳入标准核算。",
            "Activity (Details)": "企业乘用车生产、进口和销售形成的平均燃料消耗量核算活动。",
            "Intensity (Value)": "N/A",
            "Intensity (Unit)": "L/100 km",
            "Intensity (Details)": "企业层面强度由车型燃料消耗量目标值和实际值按产量或进口量加权核算；办法未给出单一固定强度值。",
            "Requirement specification": "企业平均燃料消耗量实际值低于达标值产生正积分，高于达标值产生负积分；负积分应按办法规定抵偿归零。",
            "Compliance calculation methodology I": "企业平均燃料消耗量实际值为各车型燃料消耗量与对应产量或进口量加权平均。",
            "Compliance calculation methodology II": "CAFC 积分为企业平均燃料消耗量达标值与实际值之差，乘以企业乘用车生产量或进口量。",
            "Trading System: Type": "CAFC 可交易/可转让绩效积分子方案。",
            "Trading System: cap": "未设置固定绝对总量上限；企业义务由平均燃料消耗量达标值和企业生产/进口规模决定。",
            "Trading System: allowance mechanism": "CAFC 正/负积分由企业平均燃料消耗量达标值和实际值核算产生；正积分可结转或在关联企业间转让。",
            "Trading System: Free Allowance": "不适用；积分由企业燃料消耗量绩效核算产生。",
            "Trading System: Offset use allowed": "允许。CAFC 负积分可使用本企业结转或受让的 CAFC 正积分、NEV 正积分等方式抵偿。",
            "Trading System: Linkages": "与 NEV 积分子方案联动，NEV 正积分可用于抵偿 CAFC 负积分。",
            "Trading System: market stabilisation mechanism": "CAFC 正积分设置结转和关联企业转让规则；可由 NEV 正积分抵偿负积分。",
            "Trading System: revenue (annual)": "未找到单独 CAFC 积分交易额；CAFC 正积分主要结转或关联企业间转让，公开资料未披露独立年度交易金额（来源：电车汇/腾讯新闻2024-04-12及官方双积分公开资料检索）。",
            "Trading System: Volume": "未找到单独 CAFC 积分成交量；公开资料未披露 CAFC 正积分结转/转让的年度成交量（来源：电车汇/腾讯新闻2024-04-12及官方双积分公开资料检索）。",
            "Trading System: penalties for non-compliance": "CAFC 负积分未抵偿归零的企业需提交调整计划，并可能受到车型公告、产品申报或进口管理限制。",
            "Mitigation co-benefits": "空气污染；能源供应安全；技术创新",
        },
    ),
    (
        "CHNTRATPSI01S002",
        SOURCE_NEV,
        {
            **COMMON_CN,
            "Policy Instrument ID": "CHNTRATPSI01S002",
            "Instrument / subscheme": "子方案",
            "Domestic instrument name": "乘用车企业新能源汽车积分子方案",
            "English instrument name": "Passenger vehicle new energy vehicle credit subscheme",
            "Policy Package": "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法",
            "Description": "该子方案要求乘用车企业按年度新能源汽车积分比例形成目标值，并按车型积分和产量或进口量核算实际值；正积分可交易，负积分需购买正积分等方式抵偿。",
            "Objective": "工业发展；能源效率",
            "Last revisions (Details)": "工业和信息化部2025年11月7日通知规定2026年度、2027年度新能源汽车积分比例要求分别为48%和58%，并明确2026—2027年度新能源乘用车车型积分按照附件计算方法确定。",
            "Asset (Details)": "符合办法规定的纯电动乘用车、插电式混合动力乘用车和燃料电池乘用车。",
            "Asset (Cut-off range)": "对年度传统能源乘用车生产量或者进口量达到规定规模的企业核算新能源汽车积分比例要求。",
            "Activity (Details)": "新能源乘用车生产、进口和销售，以及 NEV 积分目标值、实际值、交易和积分池管理。",
            "Intensity (Value)": "48; 58",
            "Intensity (Unit)": "占传统能源乘用车核算数量的比例",
            "Intensity (Details)": "2026年度、2027年度新能源汽车积分比例要求分别为48%和58%（来源：工信部2025年通知）。",
            "Requirement specification": "企业新能源汽车积分实际值应不低于目标值；负积分应通过购买 NEV 正积分等方式抵偿归零。",
            "Compliance calculation methodology I": "NEV 积分实际值为各新能源汽车车型积分与对应生产量或进口量乘积之和。",
            "Compliance calculation methodology II": "NEV 积分目标值为传统能源乘用车核算数量与年度新能源汽车积分比例要求的乘积。",
            "Trading System: Type": "NEV 可交易绩效积分子方案。",
            "Trading System: cap": "未设置固定绝对总量上限；年度目标由传统能源乘用车核算数量与 NEV 积分比例要求决定。",
            "Trading System: allowance mechanism": "NEV 正/负积分由企业新能源乘用车车型积分和生产/进口量核算产生；NEV 正积分可交易，并可按规则储存至或提取自积分池。",
            "Trading System: Free Allowance": "不适用；积分由企业新能源汽车生产/进口绩效核算产生。",
            "Trading System: Offset use allowed": "允许。NEV 负积分通过购买 NEV 正积分等方式抵偿；NEV 正积分也可用于抵偿 CAFC 负积分。",
            "Trading System: Linkages": "与 CAFC 积分子方案联动，NEV 正积分可用于抵偿 CAFC 负积分。",
            "Trading System: market stabilisation mechanism": "2023年修订建立新能源汽车积分池管理制度，用于调节积分供需。",
            "Trading System: revenue (annual)": "30.5亿元（2022年度新能源汽车积分交易总额；来源：工信部2022年度双积分实施情况报告，转引电车汇/腾讯新闻2024-04-12）。未找到2023年度或更新实际交易总额。",
            "Trading System: Volume": "约270万分（2022年度交易量估算，按交易总额30.5亿元/交易订单均价1128元/分计算；来源：电车汇/腾讯新闻2024-04-12）；2023年度抵偿需求约342万分（需求量，非实际成交量；来源：同上）。未找到2023年度或更新实际成交量。",
            "Trading System: penalties for non-compliance": "NEV 负积分未抵偿归零的企业需提交调整计划，并可能受到车型公告、产品申报或进口管理限制。",
            "Mitigation co-benefits": "空气污染；能源供应安全；技术创新；工业发展",
        },
    ),
]

ROWS_EN = [
    (
        "CHNTRATPSI01S000",
        SOURCE_2025,
        {
            **COMMON_EN,
            "Policy Instrument ID": "CHNTRATPSI01S000",
            "Instrument / subscheme": "Instrument",
            "Domestic instrument name": "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法",
            "English instrument name": "Passenger vehicle CAFC and NEV dual-credit trading scheme",
            "Description": "The measures establish a tradable-performance-standard mechanism that jointly manages CAFC credits and NEV credits for passenger vehicle firms.",
            "Last revisions (Details)": "MIIT issued the 2026-2027 credit-management notice on 7 November 2025. It sets NEV credit percentage requirements of 48% for 2026 and 58% for 2027, and specifies low-fuel-consumption vehicle accounting, NEV model-credit calculation and off-cycle technology arrangements.",
            "Asset (Details)": "Passenger vehicles sold in China, including domestically produced and imported passenger vehicles; the parent covers both CAFC and NEV credits.",
            "Asset (Cut-off range)": "Passenger vehicle firms with annual production or import volume of 2,000 vehicles or more are included in credit accounting.",
            "Activity (Details)": "Passenger vehicle production, import and sale, plus CAFC/NEV credit accounting, carry-forward, transfer, trading, credit-pool management and negative-credit offsetting.",
            "Intensity (Value)": "N/A",
            "Intensity (Unit)": "N/A",
            "Intensity (Details)": "The parent instrument contains two credit subschemes: CAFC uses fuel-consumption target accounting, while NEV uses annual NEV credit-percentage requirements. The latest MIIT notice sets NEV ratios of 48% for 2026 and 58% for 2027.",
            "Requirement specification": "Passenger vehicle firms must meet both CAFC and NEV credit requirements; negative credits must be offset to zero under the measures.",
            "Compliance calculation methodology I": "CAFC credits are calculated from the target-minus-actual CAFC difference multiplied by the firm's passenger vehicle accounting volume.",
            "Compliance calculation methodology II": "NEV target credits are calculated from conventional passenger vehicle accounting volume multiplied by the annual NEV credit percentage; actual minus target value forms positive or negative credits.",
            "Trading System: Type": "Tradable performance standard; parallel management mechanism for passenger vehicle CAFC credits and NEV credits.",
            "Trading System: cap": "No fixed absolute cap is set; compliance obligations are determined by CAFC targets, NEV credit ratios and firm production/import volume.",
            "Trading System: allowance mechanism": "Credits are generated from firm performance, NEV model credits and annual production/import volume; positive credits may be carried forward, transferred, traded or deposited in the credit pool under the rules.",
            "Trading System: Free Allowance": "Not applicable; credits are generated through firm performance accounting, not allocated as free allowances.",
            "Trading System: Offset use allowed": "Yes. CAFC negative credits may be offset using positive CAFC credits and positive NEV credits; NEV negative credits are mainly offset by purchasing positive NEV credits.",
            "Trading System: Linkages": "N/A",
            "Trading System: market stabilisation mechanism": "The 2023 amendment established an NEV credit-pool management system; CAFC positive credits also have carry-forward and affiliated-company transfer rules.",
            "Trading System: revenue (annual)": "CNY 3.05 billion (2022 annual NEV credit transaction value; source: MIIT 2022 dual-credit implementation report, as cited by Dianchehui/Tencent News, 12 Apr 2024). Actual 2023 or newer transaction value not found.",
            "Trading System: Volume": "Approx. 2.70 million credits (estimated 2022 transaction volume, calculated as CNY 3.05 billion / CNY 1,128 per credit; source: Dianchehui/Tencent News, 12 Apr 2024). 2023 offsetting demand was approx. 3.42 million credits, but this is demand, not actual traded volume. Actual 2023 or newer traded volume not found.",
            "Trading System: penalties for non-compliance": "Firms with unoffset negative credits must submit adjustment plans and may face vehicle-model announcement, product application or import-management restrictions.",
            "Mitigation co-benefits": "Air pollution; Energy supply security; Technological innovation; Industrial development",
        },
    ),
    (
        "CHNTRATPSI01S001",
        SOURCE_2025,
        {
            **COMMON_EN,
            "Policy Instrument ID": "CHNTRATPSI01S001",
            "Instrument / subscheme": "Subscheme",
            "Domestic instrument name": "乘用车企业平均燃料消耗量积分子方案",
            "English instrument name": "Passenger vehicle corporate average fuel consumption credit subscheme",
            "Policy Package": "Passenger vehicle CAFC and NEV dual-credit trading scheme",
            "Description": "This subscheme annually assesses passenger vehicle firms' CAFC performance, generates positive or negative CAFC credits, and sets carry-forward, transfer and negative-credit offsetting rules.",
            "Objective": "Energy efficiency",
            "Last revisions (Details)": "MIIT's 7 November 2025 notice sets 2026-2027 CAFC-related accounting arrangements, including relaxed CAFC target conditions for small-scale firms, 0.1x accounting for low-fuel-consumption passenger vehicles, and continued off-cycle technology credit treatment.",
            "Asset (Details)": "Conventional passenger vehicles and passenger vehicle models included in CAFC accounting.",
            "Asset (Cut-off range)": "Passenger vehicle firms with annual production or import volume of 2,000 vehicles or more are subject to standard accounting.",
            "Activity (Details)": "Passenger vehicle production, import and sale activities entering CAFC accounting.",
            "Intensity (Value)": "N/A",
            "Intensity (Unit)": "L/100 km",
            "Intensity (Details)": "Firm-level intensity is calculated from model fuel-consumption target and actual values weighted by production or import volume; the measures do not set one fixed intensity value.",
            "Requirement specification": "Actual CAFC below the target creates positive credits; actual CAFC above the target creates negative credits, which must be offset to zero.",
            "Compliance calculation methodology I": "The firm's actual CAFC is the volume-weighted average of each model's fuel consumption.",
            "Compliance calculation methodology II": "CAFC credits equal target CAFC minus actual CAFC, multiplied by the firm's passenger vehicle production or import volume.",
            "Trading System: Type": "CAFC tradable/transferable performance-credit subscheme.",
            "Trading System: cap": "No fixed absolute cap is set; firm obligations are determined by CAFC target values and production/import volume.",
            "Trading System: allowance mechanism": "CAFC positive/negative credits are generated from the firm's CAFC target and actual values; positive credits may be carried forward or transferred among affiliated companies.",
            "Trading System: Free Allowance": "Not applicable; credits are generated through fuel-consumption performance accounting.",
            "Trading System: Offset use allowed": "Yes. Negative CAFC credits may be offset using carried-forward or transferred positive CAFC credits, positive NEV credits and other allowed methods.",
            "Trading System: Linkages": "Linked to the NEV credit subscheme; positive NEV credits may be used to offset negative CAFC credits.",
            "Trading System: market stabilisation mechanism": "CAFC positive credits have carry-forward and affiliated-company transfer rules; positive NEV credits may offset negative CAFC credits.",
            "Trading System: revenue (annual)": "Separate CAFC credit transaction value not found; positive CAFC credits are mainly carried forward or transferred among affiliated companies, and public sources do not disclose a standalone annual transaction value.",
            "Trading System: Volume": "Separate CAFC credit traded volume not found; public sources do not disclose annual traded volume for CAFC credit carry-forward/transfers.",
            "Trading System: penalties for non-compliance": "Firms with unoffset negative CAFC credits must submit adjustment plans and may face vehicle-model announcement, product application or import-management restrictions.",
            "Mitigation co-benefits": "Air pollution; Energy supply security; Technological innovation",
        },
    ),
    (
        "CHNTRATPSI01S002",
        SOURCE_NEV,
        {
            **COMMON_EN,
            "Policy Instrument ID": "CHNTRATPSI01S002",
            "Instrument / subscheme": "Subscheme",
            "Domestic instrument name": "乘用车企业新能源汽车积分子方案",
            "English instrument name": "Passenger vehicle new energy vehicle credit subscheme",
            "Policy Package": "Passenger vehicle CAFC and NEV dual-credit trading scheme",
            "Description": "This subscheme requires passenger vehicle firms to meet annual NEV credit-ratio targets and calculates actual credits from NEV model credits and production or import volume; positive credits are tradable and negative credits must be offset.",
            "Objective": "Industrial development; Energy efficiency",
            "Last revisions (Details)": "MIIT's 7 November 2025 notice sets NEV credit percentage requirements of 48% for 2026 and 58% for 2027 and specifies that 2026-2027 NEV model credits are determined by the attached calculation method.",
            "Asset (Details)": "Battery electric, plug-in hybrid and fuel-cell passenger vehicles meeting the measures' requirements.",
            "Asset (Cut-off range)": "Firms reaching the specified conventional passenger vehicle volume are assessed against annual NEV credit-percentage requirements.",
            "Activity (Details)": "NEV production, import and sale, plus NEV credit target-value accounting, actual-value accounting, trading and credit-pool management.",
            "Intensity (Value)": "48; 58",
            "Intensity (Unit)": "% of conventional passenger vehicle accounting volume",
            "Intensity (Details)": "The NEV credit percentage requirements for 2026 and 2027 are 48% and 58% respectively (source: 2025 MIIT notice).",
            "Requirement specification": "A firm's actual NEV credits must be no lower than the target; negative NEV credits must be offset to zero by purchasing positive NEV credits or through other allowed methods.",
            "Compliance calculation methodology I": "Actual NEV credits equal the sum of each NEV model's credit value multiplied by the corresponding production or import volume.",
            "Compliance calculation methodology II": "NEV target credits equal conventional passenger vehicle accounting volume multiplied by the annual NEV credit percentage requirement.",
            "Trading System: Type": "NEV tradable performance-credit subscheme.",
            "Trading System: cap": "No fixed absolute cap is set; annual targets are determined by conventional passenger vehicle accounting volume and the NEV credit percentage requirement.",
            "Trading System: allowance mechanism": "NEV positive/negative credits are generated from NEV model credits and production/import volume; positive NEV credits may be traded and may be deposited in or withdrawn from the credit pool under the rules.",
            "Trading System: Free Allowance": "Not applicable; credits are generated through NEV production/import performance accounting.",
            "Trading System: Offset use allowed": "Yes. Negative NEV credits are offset by purchasing positive NEV credits; positive NEV credits may also offset negative CAFC credits.",
            "Trading System: Linkages": "Linked to the CAFC credit subscheme; positive NEV credits may offset negative CAFC credits.",
            "Trading System: market stabilisation mechanism": "The 2023 amendment established an NEV credit-pool management system to regulate credit supply and demand.",
            "Trading System: revenue (annual)": "CNY 3.05 billion (2022 annual NEV credit transaction value; source: MIIT 2022 dual-credit implementation report, as cited by Dianchehui/Tencent News, 12 Apr 2024). Actual 2023 or newer transaction value not found.",
            "Trading System: Volume": "Approx. 2.70 million credits (estimated 2022 transaction volume, calculated as CNY 3.05 billion / CNY 1,128 per credit; source: Dianchehui/Tencent News, 12 Apr 2024). 2023 offsetting demand was approx. 3.42 million credits, but this is demand, not actual traded volume. Actual 2023 or newer traded volume not found.",
            "Trading System: penalties for non-compliance": "Firms with unoffset negative NEV credits must submit adjustment plans and may face vehicle-model announcement, product application or import-management restrictions.",
            "Mitigation co-benefits": "Air pollution; Energy supply security; Technological innovation; Industrial development",
        },
    ),
]


def purge_old_evidence() -> None:
    header, rows = read_csv(DEFAULT_EVIDENCE_LOG)
    if not header:
        return
    rows = [row for row in rows if row.get("instrument_id") not in OLD_IDS]
    write_csv(DEFAULT_EVIDENCE_LOG, header, rows)


def purge_old_dataset_rows(template: str, lang: str) -> None:
    templates = load_templates()
    fieldnames = get_template_columns(template, lang, templates)
    aliases = build_field_aliases(template, lang, templates)
    output = default_dataset_path(template, lang, Path("outputs"))
    header, rows = read_csv(output)
    if not header:
        write_csv(output, fieldnames, [])
        return
    rows = [row for row in rows if get_row_value(row, ["Policy Instrument ID"], aliases) not in OLD_IDS]
    write_csv(output, fieldnames, rows)


def fix_market_data_evidence() -> None:
    header, rows = read_csv(DEFAULT_EVIDENCE_LOG)
    if not header:
        return
    target_ids = {"CHNTRATPSI01S000", "CHNTRATPSI01S001", "CHNTRATPSI01S002"}
    target_fields = {
        "Trading System: revenue (annual)",
        "Trading System: Volume",
        "交易系统：年收入",
        "交易系统：交易量",
    }
    for row in rows:
        if row.get("instrument_id") in target_ids and row.get("field_name") in target_fields:
            row["source_url"] = TENCENT_MARKET_URL
            row["source_title"] = "双积分交易市场数据（电车汇/腾讯新闻）"
            row["evidence_quote"] = "2022年度新能源汽车积分交易总额为30.5亿元，交易订单均价为1128元/分；预计2023年双积分市场需求为342万分。"
            row["confidence_score"] = "0.62"
            row["needs_human_review"] = "true"
            row["review_note"] = (
                "Non-official secondary source citing the MIIT 2022 dual-credit implementation report; "
                "2023 figure is demand, not actual traded volume. Replace with official transaction disclosure if found."
            )
    write_csv(DEFAULT_EVIDENCE_LOG, header, rows)


def fix_legal_document_evidence() -> None:
    header, rows = read_csv(DEFAULT_EVIDENCE_LOG)
    if not header:
        return
    target_ids = {"CHNTRATPSI01S000", "CHNTRATPSI01S001", "CHNTRATPSI01S002"}
    legal_fields = {"Legal document", "法律文件链接"}
    for row in rows:
        if row.get("instrument_id") in target_ids and row.get("field_name") in legal_fields:
            row["source_url"] = OFFICIAL_MEASURE_URL
            row["source_title"] = "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法"
            row["evidence_quote"] = "乘用车企业平均燃料消耗量与新能源汽车积分并行管理办法"
            row["confidence_score"] = "0.9"
            row["needs_human_review"] = "false"
            row["review_note"] = "Official gov.cn measure text supplied by reviewer."
    write_csv(DEFAULT_EVIDENCE_LOG, header, rows)


def upsert_rows(lang: str, rows: list[tuple[str, dict[str, str], dict[str, str]]]) -> None:
    templates = load_templates()
    fieldnames = get_template_columns(ECONOMIC_TEMPLATE, lang, templates)
    aliases = build_field_aliases(ECONOMIC_TEMPLATE, lang, templates)
    output = default_dataset_path(ECONOMIC_TEMPLATE, lang, Path("outputs"))
    header, existing = read_csv(output)
    if not header:
        existing = []

    existing = [row for row in existing if get_row_value(row, ["Policy Instrument ID"], aliases) not in OLD_IDS]
    for instrument_id, metadata, values in rows:
        canonical = canonicalise_fields(values, fieldnames, aliases)
        output_row = {field: "" for field in fieldnames}
        apply_defaults(output_row, instrument_id, canonical, aliases)
        fill_empty_template_cells(output_row, fieldnames, aliases)
        existing.append(output_row)
        append_evidence(DEFAULT_EVIDENCE_LOG, instrument_id, canonical, metadata)

    write_csv(output, fieldnames, existing)
    print(f"Updated {len(rows)} {lang} economic rows: {output}")


def main() -> None:
    purge_old_evidence()
    for lang in ("cn", "en"):
        purge_old_dataset_rows(REGULATORY_TEMPLATE, lang)
    upsert_rows("cn", ROWS_CN)
    upsert_rows("en", ROWS_EN)
    fix_market_data_evidence()
    fix_legal_document_evidence()
    print(f"Completed at {dt.datetime.now().isoformat(timespec='seconds')}")


if __name__ == "__main__":
    main()
