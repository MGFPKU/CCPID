#!/usr/bin/env python3
"""Fill MLF green collateral expansion as a CCPID economic instrument."""

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
OLD_IDS = {"CHNSUBCSUI01S000", "CHNSUBCRSI01S000"}
GROUP = "Subsidy"
APPROACH = "Concessional loans, loan guarantees and credit support"
INSTRUMENT_ID = generate_policy_id("CHN", GROUP, APPROACH, 1)
SOURCE_URL = (
    "https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125437/"
    "125446/125873/3d10b70283e3479bb6b4b55a38a48399/index.html"
)
SOURCE_TITLE = "中国人民银行决定适当扩大中期借贷便利（MLF）担保品范围"
SOURCE_QUOTE = (
    "人民银行近日决定适当扩大中期借贷便利（MLF）担保品范围，新纳入不低于AA级的小微企业、"
    "绿色和“三农”金融债券，AA+、AA级公司信用类债券，优质的小微企业贷款和绿色贷款。"
)
REVIEW_NOTE = (
    "Classification uses a newly added subsidy approach for concessional loans, loan guarantees and "
    "credit support because IFCMA subsidy typology includes concessional loans, guarantees and other "
    "financial risk-mitigation mechanisms. Confirm approach coding and whether a broader green-finance "
    "collateral instrument should be split if later PBOC collateral rules are added."
)


COMMON_EN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "Instrument",
    "Group": GROUP,
    "Approach": APPROACH,
    "Emission sector": "Cross-sector",
    "Sub-sector": "Green finance; green credit; green bonds",
    "Domestic instrument name": "中期借贷便利（MLF）绿色担保品范围扩容",
    "English instrument name": "MLF green collateral eligibility expansion",
    "Policy Package": "N/A",
    "Description": (
        "The People's Bank of China expanded the collateral accepted for medium-term lending facility "
        "(MLF) operations to include AA-or-above green financial bonds and high-quality green loans, "
        "alongside small/micro, agriculture-related and selected corporate credit bonds. The green "
        "collateral treatment improves the liquidity and central-bank refinancing value of eligible "
        "green finance assets."
    ),
    "Objective": "Green economy",
    "Mitigation relevance": "Indirect",
    "Functioning channel": "environment",
    "Country": "CHN",
    "Jurisdiction level": "national",
    "Jurisdiction name": "N/A",
    "Adoption date": "01/06/2018",
    "Start date": "01/06/2018",
    "End date": "N/A",
    "Last revisions": "01/06/2018",
    "Last revisions (Details)": (
        "The PBOC notice announced the expansion of MLF collateral eligibility; no later source-specific "
        "revision for this green-collateral expansion was identified in this fill."
    ),
    "Status": "in force",
    "Administrating authorities": "People's Bank of China",
    "Asset": "Green financial bonds; Green loans",
    "Asset (Status)": "existing",
    "Asset (Details)": "Eligible collateral in PBOC MLF operations: green financial bonds rated AA or above and high-quality green loans.",
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": "Green financial bonds must be rated no lower than AA; green loans must be high-quality.",
    "Agent": "Firms",
    "Agent (Detail)": "Financial institutions participating in MLF operations, especially commercial banks holding or originating eligible green finance assets.",
    "Activity": "Collateral acceptance and credit support",
    "Activity (Details)": "Acceptance of green financial bonds and green loans as eligible collateral for central-bank medium-term lending facility operations.",
    "Intensity (Value)": "N/A",
    "Intensity (Unit)": "N/A",
    "Intensity (Details)": "The notice changes collateral eligibility rather than setting a per-unit payment rate or emissions intensity.",
    "Requirement specification": "Eligible green collateral newly includes AA-or-above green financial bonds and high-quality green loans.",
    "Compliance calculation methodology I": "N/A",
    "Compliance calculation methodology II": "N/A",
    "Subsidy: annual budget/ expenditure": "not found",
    "Subsidy: Limit": "N/A",
    "Subsidy: Floor or ceiling": "N/A",
    "Subsidy: distribution mechanism": "Collateral eligibility in PBOC MLF operations; support is accessed through eligible financial institutions' MLF borrowing and pledged collateral.",
    "Subsidy: Support duration": "Not specified in the notice.",
    "Subsidy: Enforcement Mechanism": "PBOC operational eligibility and collateral acceptance controls.",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "K64",
    "GHGs affected": "CO2",
    "Mitigation effects": "positive",
    "Mitigation co-benefits": "Energy supply security; Industrial development",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": "",
}

COMMON_CN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "工具",
    "Group": "补贴",
    "Approach": "优惠贷款、贷款担保和信贷支持",
    "Emission sector": "跨部门",
    "Sub-sector": "绿色金融；绿色信贷；绿色债券",
    "Domestic instrument name": "中期借贷便利（MLF）绿色担保品范围扩容",
    "English instrument name": "MLF green collateral eligibility expansion",
    "Policy Package": "N/A",
    "Description": (
        "中国人民银行扩大中期借贷便利（MLF）担保品范围，将不低于AA级的绿色金融债券和优质绿色贷款"
        "纳入合格担保品范围。该安排提高符合条件绿色金融资产在央行中期流动性操作中的可用性和融资支持价值。"
    ),
    "Objective": "绿色经济",
    "Mitigation relevance": "间接",
    "Functioning channel": "环境",
    "Country": "中国",
    "Jurisdiction level": "国家",
    "Jurisdiction name": "N/A",
    "Adoption date": "01/06/2018",
    "Start date": "01/06/2018",
    "End date": "N/A",
    "Last revisions": "01/06/2018",
    "Last revisions (Details)": "人民银行该通知公布扩大MLF担保品范围；本次填报未找到针对绿色担保品扩容的后续专门修订文件。",
    "Status": "生效",
    "Administrating authorities": "中国人民银行",
    "Asset": "绿色金融债券；绿色贷款",
    "Asset (Status)": "既有",
    "Asset (Details)": "MLF操作合格担保品：不低于AA级的绿色金融债券和优质绿色贷款。",
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": "绿色金融债券评级不低于AA级；绿色贷款须为优质贷款。",
    "Agent": "企业",
    "Agent (Detail)": "参与MLF操作的金融机构，特别是持有或发放合格绿色金融资产的商业银行。",
    "Activity": "担保品接受和信贷支持",
    "Activity (Details)": "将绿色金融债券和绿色贷款接受为央行中期借贷便利操作的合格担保品。",
    "Intensity (Value)": "N/A",
    "Intensity (Unit)": "N/A",
    "Intensity (Details)": "该通知调整担保品资格，不设置单位补贴率或排放强度。",
    "Requirement specification": "新纳入不低于AA级的绿色金融债券和优质绿色贷款作为MLF合格担保品。",
    "Compliance calculation methodology I": "N/A",
    "Compliance calculation methodology II": "N/A",
    "Subsidy: annual budget/ expenditure": "未找到",
    "Subsidy: Limit": "N/A",
    "Subsidy: Floor or ceiling": "N/A",
    "Subsidy: distribution mechanism": "通过人民银行MLF操作中的担保品资格实施；符合条件金融机构以合格担保品参与MLF借款。",
    "Subsidy: Support duration": "通知未明确规定。",
    "Subsidy: Enforcement Mechanism": "人民银行通过MLF操作规则和担保品审核接受机制执行。",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "K64",
    "GHGs affected": "CO2",
    "Mitigation effects": "正向",
    "Mitigation co-benefits": "能源供应安全；工业发展",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": "",
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
            "source_url": SOURCE_URL,
            "source_title": SOURCE_TITLE,
            "evidence_quote": SOURCE_QUOTE,
            "confidence_score": "0.82",
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
