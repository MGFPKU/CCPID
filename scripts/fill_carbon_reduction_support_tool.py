#!/usr/bin/env python3
"""Fill China's carbon emission reduction support tool as a CCPID row."""

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
GROUP = "Subsidy"
APPROACH = "Concessional loans, loan guarantees and credit support"
INSTRUMENT_ID = generate_policy_id("CHN", GROUP, APPROACH, 2)
OLD_IDS: set[str] = set()

SOURCE_URL = "https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025092212552065420/index.html"
REVISION_URLS = (
    "https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026011515253112924/index.html"
)
SOURCE_TITLE = "碳减排支持工具"
SOURCE_QUOTE = (
    "人民银行通过碳减排支持工具向金融机构提供低成本资金，引导金融机构在自主决策、自担风险的前提下，"
    "向碳减排重点领域内各类企业一视同仁提供碳减排贷款。"
)
REVIEW_NOTE = (
    "Classified as subsidy / concessional loans, loan guarantees and credit support because the PBOC "
    "provides low-cost funding to financial institutions against eligible carbon-reduction loans. Revision "
    "sources record extension to end-2027 and the 2026 source reports an annual operation limit of CNY 800 billion."
)


COMMON_EN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "Instrument",
    "Group": GROUP,
    "Approach": APPROACH,
    "Emission sector": "Cross-sector",
    "Sub-sector": "Green finance; green credit; carbon-reduction projects",
    "Domestic instrument name": "碳减排支持工具",
    "English instrument name": "Carbon emission reduction support tool",
    "Policy Package": "N/A",
    "Description": (
        "The People's Bank of China provides low-cost funds to eligible financial institutions that issue "
        "loans to key carbon-reduction areas. The tool operates on a lend-first-borrow-later basis: after "
        "financial institutions issue qualified carbon-reduction loans, they may apply to the PBOC for "
        "central-bank funding equal to 60% of the loan principal."
    ),
    "Objective": "Green economy; Climate change mitigation",
    "Mitigation relevance": "Indirect",
    "Functioning channel": "environment",
    "Country": "CHN",
    "Jurisdiction level": "national",
    "Jurisdiction name": "N/A",
    "Adoption date": "08/11/2021",
    "Start date": "08/11/2021",
    "End date": "31/12/2027",
    "Last revisions": "15/01/2026",
    "Last revisions (Details)": (
        "Revision sources record that the carbon emission reduction support tool has been extended to the end "
        "of 2027. The PBOC source dated 15 January 2026 also reports that support areas have been expanded "
        "and that annual operations should not exceed CNY 800 billion."
    ),
    "Status": "in force",
    "Administrating authorities": "People's Bank of China",
    "Asset": "Carbon-reduction loans",
    "Asset (Status)": "New",
    "Asset (Details)": (
        "Qualified loans issued by eligible financial institutions to enterprises in key carbon-reduction "
        "areas, including clean energy, energy conservation and environmental protection, and carbon-reduction technologies."
    ),
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": "PBOC funding support equals 60% of the principal of qualified carbon-reduction loans.",
    "Agent": "Firms",
    "Agent (Detail)": (
        "Eligible financial institutions that issue carbon-reduction loans and enterprises receiving loans "
        "for qualified carbon-reduction projects."
    ),
    "Activity": "Carbon-reduction loan provision and relending support",
    "Activity (Details)": (
        "Financial institutions issue qualified carbon-reduction loans, then apply for PBOC low-cost funds "
        "against those loans under a lend-first-borrow-later mechanism."
    ),
    "Intensity (Value)": "1.75",
    "Intensity (Unit)": "% annual interest rate",
    "Intensity (Details)": (
        "PBOC funds are provided to financial institutions at a 1.75% annual interest rate; the support amount "
        "is 60% of the qualified carbon-reduction loan principal."
    ),
    "Requirement specification": (
        "Financial institutions make independent lending decisions and bear their own risks. Qualified loans "
        "must support key carbon-reduction areas and information on the loans and expected carbon reductions "
        "is subject to disclosure and verification requirements."
    ),
    "Compliance calculation methodology I": "PBOC support amount = 60% of the principal of qualified carbon-reduction loans.",
    "Compliance calculation methodology II": (
        "Qualified loan eligibility is assessed against the PBOC's key carbon-reduction areas and project information requirements."
    ),
    "Subsidy: annual budget/ expenditure": "not found",
    "Subsidy: Limit": "60% of qualified loan principal; annual operations not exceeding CNY 800 billion",
    "Subsidy: Floor or ceiling": "PBOC funding interest rate of 1.75%; support equal to 60% of qualified loan principal.",
    "Subsidy: distribution mechanism": (
        "Lend-first-borrow-later: financial institutions issue qualified carbon-reduction loans first and then "
        "apply to the PBOC for low-cost funding support."
    ),
    "Subsidy: Support duration": "One-year central-bank funds, renewable twice; the tool has been extended to 31/12/2027.",
    "Subsidy: Enforcement Mechanism": (
        "PBOC eligibility review, disclosure of loan and carbon-reduction information, and third-party verification of carbon-reduction effects."
    ),
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "K64",
    "GHGs affected": "CO2",
    "Mitigation effects": "positive",
    "Mitigation co-benefits": "Air pollution; Energy supply security; Technological innovation; Industrial development",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": REVISION_URLS,
}

COMMON_CN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "工具",
    "Group": "补贴",
    "Approach": "优惠贷款、贷款担保和信贷支持",
    "Emission sector": "跨部门",
    "Sub-sector": "绿色金融；绿色信贷；碳减排项目",
    "Domestic instrument name": "碳减排支持工具",
    "English instrument name": "Carbon emission reduction support tool",
    "Policy Package": "N/A",
    "Description": (
        "中国人民银行向发放碳减排重点领域贷款的金融机构提供低成本资金。该工具采取“先贷后借”机制："
        "金融机构发放合格碳减排贷款后，可按贷款本金的60%向人民银行申请资金支持。"
    ),
    "Objective": "绿色经济；减缓气候变化",
    "Mitigation relevance": "间接",
    "Functioning channel": "环境",
    "Country": "中国",
    "Jurisdiction level": "国家",
    "Jurisdiction name": "N/A",
    "Adoption date": "08/11/2021",
    "Start date": "08/11/2021",
    "End date": "31/12/2027",
    "Last revisions": "15/01/2026",
    "Last revisions (Details)": (
        "修订来源记录碳减排支持工具延续至2027年末。2026年1月15日人民银行来源还披露，该工具支持领域拓展，全年操作量不超过8000亿元。"
    ),
    "Status": "生效",
    "Administrating authorities": "中国人民银行",
    "Asset": "碳减排贷款",
    "Asset (Status)": "新建",
    "Asset (Details)": "合格金融机构向碳减排重点领域企业发放的贷款，重点领域包括清洁能源、节能环保和碳减排技术。",
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": "人民银行资金支持额度为合格碳减排贷款本金的60%。",
    "Agent": "企业",
    "Agent (Detail)": "发放碳减排贷款的合格金融机构，以及获得合格碳减排项目贷款的企业。",
    "Activity": "碳减排贷款发放和再贷款资金支持",
    "Activity (Details)": "金融机构先发放合格碳减排贷款，再按“先贷后借”机制向人民银行申请低成本资金支持。",
    "Intensity (Value)": "1.75",
    "Intensity (Unit)": "% 年利率",
    "Intensity (Details)": "来源：人民银行2021年11月推出该工具时披露，向金融机构提供资金的利率为1.75%；支持额度为合格碳减排贷款本金的60%。",
    "Requirement specification": "金融机构自主决策、自担风险；合格贷款须投向碳减排重点领域，并按要求披露贷款和碳减排效应信息、接受核验。",
    "Compliance calculation methodology I": "人民银行支持额度 = 合格碳减排贷款本金的60%。",
    "Compliance calculation methodology II": "贷款合格性依据人民银行规定的碳减排重点领域和项目信息要求进行审核。",
    "Subsidy: annual budget/ expenditure": "未找到",
    "Subsidy: Limit": "来源：2026年1月15日人民银行；合格贷款本金的60%；全年操作量不超过8000亿元",
    "Subsidy: Floor or ceiling": "人民银行资金利率1.75%；支持额度为合格贷款本金的60%。",
    "Subsidy: distribution mechanism": "先贷后借：金融机构先发放合格碳减排贷款，再向人民银行申请低成本资金支持。",
    "Subsidy: Support duration": "人民银行资金期限1年，可展期2次；该工具已延续至31/12/2027。",
    "Subsidy: Enforcement Mechanism": "人民银行开展合格性审核，并通过贷款和碳减排信息披露、第三方核验碳减排效果等机制执行。",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "K64",
    "GHGs affected": "CO2",
    "Mitigation effects": "正向",
    "Mitigation co-benefits": "空气污染；能源供应安全；技术创新；工业发展",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": REVISION_URLS,
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
            "confidence_score": "0.76",
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
