#!/usr/bin/env python3
"""Fill China's equipment renewal loan interest subsidy as a CCPID row."""

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
INSTRUMENT_ID = generate_policy_id("CHN", GROUP, APPROACH, 3)
OLD_IDS: set[str] = set()

SOURCE_URL = "https://www.gov.cn/zhengce/zhengceku/202406/content_6959323.htm"
REVISION_URL = "https://www.gov.cn/zhengce/zhengceku/202601/content_7055549.htm"
EVIDENCE_URLS = f"{SOURCE_URL}; {REVISION_URL}"
SOURCE_TITLE = "关于实施设备更新贷款财政贴息政策的通知"
REVISION_TITLE = "关于继续实施设备更新贷款财政贴息政策的通知"
SOURCE_QUOTE = (
    "2024年通知规定，中央财政对经营主体的银行贷款本金贴息1个百分点，贴息期限不超过2年。"
    "2026年优化实施通知规定，中央财政对经营主体的设备更新项目相关固定资产贷款本金贴息1.5个百分点，"
    "政策实施至2026年12月31日。"
)
REVIEW_NOTE = (
    "Classified as subsidy / concessional loans, loan guarantees and credit support because the measure "
    "uses central fiscal interest subsidies to reduce borrowing costs for eligible equipment renewal loans. "
    "Concrete terms were filled from the user-provided gov.cn PDFs: the 2026 optimization increased the interest "
    "subsidy to 1.5 percentage points, expanded support fields, and removed relending support as a prerequisite."
)


COMMON_EN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "Instrument",
    "Group": GROUP,
    "Approach": APPROACH,
    "Emission sector": "Cross-sector",
    "Sub-sector": "Equipment renewal; green finance; technological transformation",
    "Domestic instrument name": "设备更新贷款财政贴息",
    "English instrument name": "Fiscal interest subsidy for equipment renewal loans",
    "Policy Package": "Large-scale equipment renewal and consumer goods trade-in policy",
    "Description": (
        "China provides central fiscal interest subsidies for eligible bank loans used for equipment renewal "
        "and technological transformation. The 2024 policy subsidized 1 percentage point of eligible equipment "
        "renewal loan principal interest for up to two years. The 2026 optimization expands eligible fields, "
        "covers equipment-renewal fixed-asset loans and technology-innovation loans supported by the technology "
        "innovation and technological transformation relending policy, raises the subsidy to 1.5 percentage points, "
        "and states that fiscal interest subsidy no longer depends on the loan receiving relending support."
    ),
    "Objective": "Green economy; Economic growth; Energy efficiency",
    "Mitigation relevance": "Indirect",
    "Functioning channel": "environment",
    "Country": "CHN",
    "Jurisdiction level": "national",
    "Jurisdiction name": "N/A",
    "Adoption date": "21/06/2024",
    "Start date": "07/03/2024",
    "End date": "31/12/2026",
    "Last revisions": "19/01/2026",
    "Last revisions (Details)": (
        "The 2026 optimization notice took effect on 1 January 2026, expanded the policy scope, increased the "
        "interest subsidy to 1.5 percentage points, added handling banks, simplified the subsidy process, and "
        "states that provisions inconsistent with the 2024 notice follow the 2026 notice."
    ),
    "Status": "in force",
    "Administrating authorities": "Ministry of Finance; National Development and Reform Commission; People's Bank of China; National Financial Regulatory Administration; relevant sectoral authorities",
    "Asset": "Equipment renewal fixed-asset loans; Technology innovation loans",
    "Asset (Status)": "New; existing",
    "Asset (Details)": (
        "Eligible bank loans used by operating entities for equipment renewal and technological transformation projects. "
        "The 2026 notice covers equipment-renewal fixed-asset loans and technology-innovation loans newly issued "
        "from 2026 under the technology innovation and technological transformation relending policy."
    ),
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": "Eligible loans must support covered equipment renewal fields; the 2026 policy applies through 31/12/2026, with possible extension.",
    "Agent": "Firms",
    "Agent (Detail)": "Operating entities that take bank loans for eligible equipment renewal or technological transformation projects.",
    "Activity": "Equipment renewal loan financing and fiscal interest subsidy",
    "Activity (Details)": (
        "Banks issue eligible equipment renewal loans and central fiscal funds subsidize part of the loan interest cost. "
        "The 2026 notice uses a pre-allocation plus settlement process and no longer requires fiscal interest subsidy "
        "to be conditional on the loan receiving relending support."
    ),
    "Intensity (Value)": "1.5",
    "Intensity (Unit)": "percentage points interest subsidy",
    "Intensity (Details)": (
        "The 2024 notice set a 1 percentage point central fiscal interest subsidy on eligible equipment-renewal loan "
        "principal for a period not exceeding two years. The 2026 optimization notice raises the subsidy to 1.5 "
        "percentage points for eligible equipment-renewal fixed-asset loan principal, with interest subsidy from the "
        "date of relevant fixed-asset loan disbursement."
    ),
    "Requirement specification": (
        "Loan funds must be used for eligible equipment renewal and technological transformation projects and cannot "
        "be used for debt repayment, investment, wealth management or other arbitrage activities. Borrowers, lending "
        "banks and fiscal authorities follow the application, verification, subsidy-disbursement and reporting procedures "
        "set out in the notices."
    ),
    "Compliance calculation methodology I": "Interest subsidy = eligible loan principal and interest basis multiplied by the policy interest-subsidy rate and eligible period.",
    "Compliance calculation methodology II": "Eligibility is assessed against the official equipment renewal loan fiscal interest subsidy policy scope and bank loan documentation.",
    "Subsidy: annual budget/ expenditure": "not found",
    "Subsidy: Limit": "1.5 percentage points interest subsidy under the 2026 optimization; the 2024 notice set 1 percentage point. Interest subsidy period not exceeding 2 years.",
    "Subsidy: Floor or ceiling": "Interest subsidy rate ceiling is 1.5 percentage points under the 2026 policy; support period not exceeding 2 years.",
    "Subsidy: distribution mechanism": "Central fiscal interest subsidy applied through handling banks to eligible equipment-renewal loans; the 2026 process uses pre-allocation plus settlement.",
    "Subsidy: Support duration": "Interest subsidy period not exceeding 2 years; optimized policy implemented through 31/12/2026, with possible extension.",
    "Subsidy: Enforcement Mechanism": "Fiscal authority, development and reform/sector authorities, PBOC, financial regulators and handling banks conduct eligibility review, loan-use verification, reporting, spot checks, recovery of subsidy funds for serious violations, and accountability for collusive or non-compliant banks.",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "K64",
    "GHGs affected": "CO2",
    "Mitigation effects": "positive",
    "Mitigation co-benefits": "Energy supply security; Technological innovation; Industrial development",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": REVISION_URL,
}

COMMON_CN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "工具",
    "Group": "补贴",
    "Approach": "优惠贷款、贷款担保和信贷支持",
    "Emission sector": "跨部门",
    "Sub-sector": "设备更新；绿色金融；技术改造",
    "Domestic instrument name": "设备更新贷款财政贴息",
    "English instrument name": "Fiscal interest subsidy for equipment renewal loans",
    "Policy Package": "大规模设备更新和消费品以旧换新政策",
    "Description": (
        "中国对符合条件的设备更新贷款给予中央财政贴息支持，降低经营主体开展设备更新和技术改造的融资成本。"
        "2024年政策对合格设备更新贷款本金贴息1个百分点、期限不超过2年；2026年优化政策拓展支持领域，"
        "将设备更新项目相关固定资产贷款和科技创新、技术改造再贷款政策支持的2026年起新发放科技创新类贷款纳入支持，"
        "贴息提高至1.5个百分点，并明确财政贴息不再以贷款获得再贷款支持为前提。"
    ),
    "Objective": "绿色经济；经济增长；能源效率",
    "Mitigation relevance": "间接",
    "Functioning channel": "环境",
    "Country": "中国",
    "Jurisdiction level": "国家",
    "Jurisdiction name": "N/A",
    "Adoption date": "21/06/2024",
    "Start date": "07/03/2024",
    "End date": "31/12/2026",
    "Last revisions": "19/01/2026",
    "Last revisions (Details)": "2026年优化实施通知自2026年1月1日起施行，扩大支持范围和支持领域，将贴息提高至1.5个百分点，增加经办银行，优化贴息流程，并规定与2024年通知不一致的以2026年通知为准。",
    "Status": "生效",
    "Administrating authorities": "财政部；国家发展改革委；中国人民银行；金融监管总局；相关行业主管部门",
    "Asset": "设备更新固定资产贷款；科技创新类贷款",
    "Asset (Status)": "新建；既有",
    "Asset (Details)": "经营主体用于设备更新和技术改造项目的合格银行贷款。2026年通知覆盖设备更新项目相关固定资产贷款，以及科技创新和技术改造再贷款政策支持的、银行2026年起新发放的科技创新类贷款。",
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": "合格贷款须支持政策覆盖的设备更新领域；2026年政策实施至31/12/2026，后续可视情延长。",
    "Agent": "企业",
    "Agent (Detail)": "为合格设备更新或技术改造项目取得银行贷款的经营主体。",
    "Activity": "设备更新贷款融资和财政贴息",
    "Activity (Details)": "银行发放合格设备更新贷款，中央财政资金对部分贷款利息成本给予贴息。2026年通知采用“预拨+结算”方式，并明确财政贴息不再以贷款获得再贷款支持为前提。",
    "Intensity (Value)": "1.5",
    "Intensity (Unit)": "百分点贷款贴息",
    "Intensity (Details)": "来源：2024年通知规定中央财政对合格设备更新贷款本金贴息1个百分点、期限不超过2年；2026年优化通知将设备更新项目相关固定资产贷款本金贴息提高至1.5个百分点，并从相关固定资产贷款发放之日起予以贴息。",
    "Requirement specification": "贷款资金须用于政策范围内的设备更新和技术改造项目，不得用于偿还其他债务、投资理财等套利活动；借款主体、贷款银行和财政部门按通知规定履行申请、审核、核验、贴息拨付和报送程序。",
    "Compliance calculation methodology I": "贴息金额 = 合格贷款本金和利息计算基础 × 政策贴息率 × 合格期限。",
    "Compliance calculation methodology II": "贷款合格性依据设备更新贷款财政贴息政策范围和银行贷款材料审核。",
    "Subsidy: annual budget/ expenditure": "未找到",
    "Subsidy: Limit": "2026年优化政策贴息1.5个百分点；2024年通知贴息1个百分点。贴息期限不超过2年。",
    "Subsidy: Floor or ceiling": "2026年政策贴息率上限为1.5个百分点；支持期限不超过2年。",
    "Subsidy: distribution mechanism": "中央财政通过经办银行对合格设备更新贷款给予财政贴息；2026年流程采用“预拨+结算”。",
    "Subsidy: Support duration": "贴息期限不超过2年；优化政策实施至31/12/2026，后续可视情延长。",
    "Subsidy: Enforcement Mechanism": "财政、发展改革、行业主管、人民银行、金融监管部门和经办银行开展合格性审核、贷款用途核验、信息报送、抽查、违规贴息资金追回及对违规银行追责。",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "K64",
    "GHGs affected": "CO2",
    "Mitigation effects": "正向",
    "Mitigation co-benefits": "能源供应安全；技术创新；工业发展",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": REVISION_URL,
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
            "source_title": f"{SOURCE_TITLE}; {REVISION_TITLE}",
            "evidence_quote": SOURCE_QUOTE,
            "confidence_score": "0.70",
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
