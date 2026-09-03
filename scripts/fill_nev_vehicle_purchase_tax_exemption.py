#!/usr/bin/env python3
"""Fill China's NEV vehicle purchase tax exemption and reduction policy."""

from __future__ import annotations

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
from policy_id import generate_policy_id


TEMPLATE = "Economic instruments"
GROUP = "Tax"
APPROACH = "Vehicle purchase tax incentive"
INSTRUMENT_ID = generate_policy_id("CHN", GROUP, APPROACH, 1)
OLD_IDS: set[str] = {"CHNSUBVPSI01S000"}

SOURCE_URL = "https://szs.mof.gov.cn/zhengcefabu/202306/t20230620_3891500.htm"
ORIGINAL_URL = "https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=48973"
EVIDENCE_URLS = f"{SOURCE_URL}; {ORIGINAL_URL}"
SOURCE_TITLE = "财政部 税务总局 工业和信息化部关于延续和优化新能源汽车车辆购置税减免政策的公告"
ORIGINAL_TITLE = "财政部 国家税务总局 工业和信息化部关于免征新能源汽车车辆购置税的公告"
SOURCE_QUOTE = (
    "对购置日期在2024年1月1日至2025年12月31日期间的新能源汽车免征车辆购置税，"
    "其中，每辆新能源乘用车免税额不超过3万元；对购置日期在2026年1月1日至2027年12月31日期间的新能源汽车减半征收车辆购置税，"
    "其中，每辆新能源乘用车减税额不超过1.5万元。"
)
REVIEW_NOTE = (
    "Classified as tax / vehicle purchase tax incentive because the policy exempts or reduces vehicle purchase "
    "tax liability for eligible low-carbon vehicles. This is a tax expenditure rather than a direct cash subsidy."
)


COMMON_EN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "Instrument",
    "Group": GROUP,
    "Approach": APPROACH,
    "Emission sector": "Transport",
    "Sub-sector": "Road transport; passenger cars; new energy vehicles",
    "Domestic instrument name": "新能源汽车车辆购置税减免政策",
    "English instrument name": "New energy vehicle purchase tax exemption and reduction policy",
    "Policy Package": "New energy vehicle promotion policy",
    "Description": (
        "China exempts or reduces vehicle purchase tax for eligible new energy vehicles. The original 2014 policy "
        "exempted eligible NEVs from vehicle purchase tax from 1 September 2014 to 31 December 2017. The 2023 "
        "extension and optimization continues support through 2027: NEVs purchased from 1 January 2024 to "
        "31 December 2025 are exempt from vehicle purchase tax, with a maximum exemption of CNY 30,000 per new "
        "energy passenger vehicle; NEVs purchased from 1 January 2026 to 31 December 2027 receive a 50% vehicle "
        "purchase tax reduction, with a maximum reduction of CNY 15,000 per new energy passenger vehicle."
    ),
    "Objective": "Industrial development; Low-carbon mobility; Green economy",
    "Mitigation relevance": "Direct",
    "Functioning channel": "demand-side",
    "Country": "CHN",
    "Jurisdiction level": "national",
    "Jurisdiction name": "N/A",
    "Adoption date": "01/08/2014",
    "Start date": "01/09/2014",
    "End date": "31/12/2027",
    "Last revisions": "19/06/2023",
    "Last revisions (Details)": (
        "The 2023 announcement extends and optimizes the policy through 31 December 2027. It provides full vehicle "
        "purchase tax exemption for eligible NEVs purchased in 2024-2025, capped at CNY 30,000 per new energy "
        "passenger vehicle, and a 50% reduction for eligible NEVs purchased in 2026-2027, capped at CNY 15,000 "
        "per new energy passenger vehicle."
    ),
    "Status": "in force",
    "Administrating authorities": "Ministry of Finance; State Taxation Administration; Ministry of Industry and Information Technology",
    "Asset": "Road transport vehicles; Cars",
    "Asset (Status)": "New",
    "Asset (Details)": (
        "Eligible new energy vehicles, including battery electric vehicles, plug-in hybrid vehicles including "
        "range-extended vehicles, and fuel-cell vehicles that are listed in the catalogue of NEV models eligible "
        "for vehicle purchase tax exemption or reduction."
    ),
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": (
        "For 2024-2025, exemption applies to eligible NEVs purchased during 01/01/2024-31/12/2025, capped at "
        "CNY 30,000 per new energy passenger vehicle. For 2026-2027, a 50% reduction applies to eligible NEVs "
        "purchased during 01/01/2026-31/12/2027, capped at CNY 15,000 per new energy passenger vehicle."
    ),
    "Agent": "Individuals; Firms",
    "Agent (Detail)": "Purchasers of eligible new energy vehicles; vehicle sellers and manufacturers support catalogue and tax documentation.",
    "Activity": "Purchase, lease or retrofit",
    "Activity (Details)": "Purchase of eligible new energy vehicles and declaration of vehicle purchase tax exemption or reduction.",
    "Intensity (Value)": "100; 50",
    "Intensity (Unit)": "% vehicle purchase tax exemption/reduction",
    "Intensity (Details)": (
        "For eligible NEVs purchased in 2024-2025, vehicle purchase tax is exempted at 100%, capped at CNY 30,000 "
        "per new energy passenger vehicle. For eligible NEVs purchased in 2026-2027, vehicle purchase tax is reduced "
        "by 50%, capped at CNY 15,000 per new energy passenger vehicle. Source: 2023 MOF/STA/MIIT announcement."
    ),
    "Requirement specification": (
        "Vehicles must be eligible new energy vehicles included in the official catalogue for vehicle purchase tax "
        "exemption or reduction. The purchase date is determined according to the valid vehicle sale invoice or "
        "other valid document."
    ),
    "Compliance calculation methodology I": (
        "Tax relief amount equals otherwise payable vehicle purchase tax multiplied by the applicable relief rate, "
        "subject to the per-vehicle cap for new energy passenger vehicles."
    ),
    "Compliance calculation methodology II": (
        "2024-2025: relief amount is capped at CNY 30,000 per new energy passenger vehicle. 2026-2027: relief amount "
        "is capped at CNY 15,000 per new energy passenger vehicle."
    ),
    "Tax and Tax Incentive: annual revenue": "N/A",
    "Tax and Tax Incentive: earmarked revenue": "N/A",
    "Tax and Tax Incentive: annual revenue forgone": "not found",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "C29; G45",
    "GHGs affected": "CO2",
    "Mitigation effects": "positive",
    "Mitigation co-benefits": "Air pollution; Energy supply security; Industrial development",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": ORIGINAL_URL,
}

COMMON_CN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "工具",
    "Group": "税收",
    "Approach": "车辆购置税优惠",
    "Emission sector": "交通",
    "Sub-sector": "道路交通；乘用车；新能源汽车",
    "Domestic instrument name": "新能源汽车车辆购置税减免政策",
    "English instrument name": "New energy vehicle purchase tax exemption and reduction policy",
    "Policy Package": "新能源汽车推广政策",
    "Description": (
        "中国对符合条件的新能源汽车免征或减半征收车辆购置税。2014年原始政策规定，自2014年9月1日至2017年12月31日，"
        "对购置的新能源汽车免征车辆购置税。2023年延续和优化政策将支持延长至2027年底：2024年1月1日至2025年12月31日期间购置的新能源汽车免征车辆购置税，"
        "每辆新能源乘用车免税额不超过3万元；2026年1月1日至2027年12月31日期间购置的新能源汽车减半征收车辆购置税，"
        "每辆新能源乘用车减税额不超过1.5万元。"
    ),
    "Objective": "工业发展；低碳出行；绿色经济",
    "Mitigation relevance": "直接",
    "Functioning channel": "需求侧",
    "Country": "中国",
    "Jurisdiction level": "国家",
    "Jurisdiction name": "N/A",
    "Adoption date": "01/08/2014",
    "Start date": "01/09/2014",
    "End date": "31/12/2027",
    "Last revisions": "19/06/2023",
    "Last revisions (Details)": (
        "2023年公告将政策延续并优化至31/12/2027：2024-2025年购置的符合条件新能源汽车免征车辆购置税，"
        "新能源乘用车每辆免税额不超过3万元；2026-2027年购置的符合条件新能源汽车减半征收车辆购置税，"
        "新能源乘用车每辆减税额不超过1.5万元。"
    ),
    "Status": "生效",
    "Administrating authorities": "财政部；税务总局；工业和信息化部",
    "Asset": "道路运输车辆；汽车",
    "Asset (Status)": "新建",
    "Asset (Details)": "符合条件的新能源汽车，包括列入免征或减免车辆购置税新能源汽车车型目录的纯电动汽车、插电式混合动力汽车（含增程式）和燃料电池汽车。",
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": (
        "2024-2025年购置的符合条件新能源汽车免征车辆购置税，新能源乘用车每辆免税额不超过3万元；"
        "2026-2027年购置的符合条件新能源汽车减半征收车辆购置税，新能源乘用车每辆减税额不超过1.5万元。"
    ),
    "Agent": "个人；企业",
    "Agent (Detail)": "符合条件新能源汽车的购买者；车辆销售方和生产企业配合车型目录和税务资料管理。",
    "Activity": "购置、租赁或改装",
    "Activity (Details)": "购买符合条件的新能源汽车，并申报车辆购置税免征或减半征收。",
    "Intensity (Value)": "100；50",
    "Intensity (Unit)": "%车辆购置税免征/减征",
    "Intensity (Details)": (
        "2024-2025年购置的符合条件新能源汽车免征车辆购置税，新能源乘用车每辆免税额不超过3万元；"
        "2026-2027年购置的符合条件新能源汽车减半征收车辆购置税，新能源乘用车每辆减税额不超过1.5万元。来源：2023年财政部、税务总局、工业和信息化部公告。"
    ),
    "Requirement specification": "车辆须属于列入免征或减免车辆购置税车型目录的新能源汽车；购置日期按机动车销售统一发票或海关关税专用缴款书等有效凭证的开具日期确定。",
    "Compliance calculation methodology I": "减免税额 = 应纳车辆购置税额 × 适用减免比例，并受新能源乘用车单车上限约束。",
    "Compliance calculation methodology II": "2024-2025年新能源乘用车单车免税额上限为3万元；2026-2027年新能源乘用车单车减税额上限为1.5万元。",
    "Tax and Tax Incentive: annual revenue": "N/A",
    "Tax and Tax Incentive: earmarked revenue": "N/A",
    "Tax and Tax Incentive: annual revenue forgone": "未找到",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "C29; G45",
    "GHGs affected": "CO2",
    "Mitigation effects": "正向",
    "Mitigation co-benefits": "空气污染；能源供应安全；工业发展",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": ORIGINAL_URL,
}


def upsert(lang: str, values: dict[str, str]) -> None:
    templates = load_templates()
    fieldnames = get_template_columns(TEMPLATE, lang, templates)
    aliases = build_field_aliases(TEMPLATE, lang, templates)
    output = default_dataset_path(TEMPLATE, lang, Path("outputs"))
    header, rows = read_csv(output)
    if not header:
        rows = []

    purge_ids = OLD_IDS | {INSTRUMENT_ID}
    rows = [row for row in rows if get_row_value(row, ["Policy Instrument ID"], aliases) not in purge_ids]
    canonical = canonicalise_fields(values, fieldnames, aliases)
    row = {field: "" for field in fieldnames}
    apply_defaults(row, INSTRUMENT_ID, canonical, aliases)
    fill_empty_template_cells(row, fieldnames, aliases)
    rows.append(row)
    write_csv(output, fieldnames, rows)

    append_evidence(
        DEFAULT_EVIDENCE_LOG,
        INSTRUMENT_ID,
        canonical,
        {
            "source_url": EVIDENCE_URLS,
            "source_title": f"{SOURCE_TITLE}; {ORIGINAL_TITLE}",
            "evidence_quote": SOURCE_QUOTE,
            "confidence_score": "0.86",
            "needs_human_review": "true",
            "review_note": REVIEW_NOTE,
        },
    )
    print(f"Updated {lang} row: {output}")


def purge_old_evidence() -> None:
    header, rows = read_csv(DEFAULT_EVIDENCE_LOG)
    if not header:
        return
    purge_ids = OLD_IDS | {INSTRUMENT_ID}
    rows = [row for row in rows if row.get("instrument_id") not in purge_ids]
    write_csv(DEFAULT_EVIDENCE_LOG, header, rows)


def main() -> None:
    purge_old_evidence()
    upsert("cn", COMMON_CN)
    upsert("en", COMMON_EN)


if __name__ == "__main__":
    main()
