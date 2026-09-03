#!/usr/bin/env python3
"""Fill China's new energy sustainable price settlement mechanism."""

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
APPROACH = "Renewable electricity contract for difference"
INSTRUMENT_ID = generate_policy_id("CHN", GROUP, APPROACH, 1)
OLD_IDS: set[str] = set()

SOURCE_URL = "https://www.ndrc.gov.cn/xxgk/zcfb/tz/202502/t20250209_1396066.html"
SOURCE_TITLE = "国家发展改革委 国家能源局关于深化新能源上网电价市场化改革 促进新能源高质量发展的通知"
SOURCE_QUOTE = (
    "建立支持新能源可持续发展的价格结算机制。纳入机制的电量，市场交易均价低于机制电价时，"
    "向新能源发电企业支付差价；高于机制电价时，由新能源发电企业支付差价。"
)
REVIEW_NOTE = (
    "Classified as renewable electricity contract for difference because the mechanism settles the difference "
    "between market transaction prices and a mechanism electricity price for eligible new energy generation. "
    "The official NDRC notice URL is used. Direct shell fetching is blocked in this environment; "
    "verify any clause-level transcription against the web page before publication."
)


COMMON_EN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "Instrument",
    "Group": GROUP,
    "Approach": APPROACH,
    "Emission sector": "Energy",
    "Sub-sector": "Renewable electricity; wind power; solar power; new energy power generation",
    "Domestic instrument name": "新能源可持续发展价格结算机制",
    "English instrument name": "New energy sustainable price settlement mechanism",
    "Policy Package": "New energy feed-in tariff market-oriented reform",
    "Description": (
        "China deepens market-based reform of new energy feed-in tariffs and establishes a sustainable price "
        "settlement mechanism for eligible new energy generation. New energy electricity enters power markets "
        "and feed-in prices are formed through market transactions. For electricity included in the mechanism, "
        "a difference settlement is made between the market transaction average price and the mechanism electricity "
        "price: when the market average is lower than the mechanism price, the difference is paid to the generator; "
        "when it is higher, the generator pays back the difference."
    ),
    "Objective": "Renewable energy development and consumption; Green economy",
    "Mitigation relevance": "Direct",
    "Functioning channel": "Supply-side",
    "Country": "CHN",
    "Jurisdiction level": "national",
    "Jurisdiction name": "N/A",
    "Adoption date": "27/01/2025",
    "Start date": "01/06/2025",
    "End date": "N/A",
    "Last revisions": "27/01/2025",
    "Last revisions (Details)": (
        "The 2025 NDRC/NEA notice establishes the sustainable price settlement mechanism alongside the reform "
        "that new energy feed-in electricity should fully enter electricity markets. Stock projects are connected "
        "to existing price policies, while incremental projects use market-based competitive determination of the "
        "mechanism electricity price."
    ),
    "Status": "in force",
    "Administrating authorities": "National Development and Reform Commission; National Energy Administration; provincial pricing and energy authorities; power market operators",
    "Asset": "Electricity; Solar energy; Wind energy; Other renewable energies",
    "Asset (Status)": "New; existing",
    "Asset (Details)": (
        "Eligible on-grid electricity from new energy projects, including stock projects and incremental projects "
        "such as wind and solar power generation."
    ),
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": (
        "Electricity quantity included in the settlement mechanism; stock and incremental projects are treated "
        "under differentiated rules, with incremental project mechanism prices determined through competitive mechanisms."
    ),
    "Agent": "Firms",
    "Agent (Detail)": "New energy power generation enterprises and electricity market participants subject to settlement or cost sharing.",
    "Activity": "Renewable electricity generation and price settlement",
    "Activity (Details)": (
        "Generation and market sale of eligible new energy electricity, plus difference settlement against the "
        "mechanism electricity price."
    ),
    "Intensity (Value)": "formula",
    "Intensity (Unit)": "CNY/MWh price difference",
    "Intensity (Details)": (
        "Difference settlement amount is based on mechanism electricity quantity multiplied by the difference "
        "between the mechanism electricity price and the market transaction average price; positive or negative "
        "payments depend on whether the market average is below or above the mechanism price, according to the "
        "2025 NDRC/NEA notice."
    ),
    "Requirement specification": (
        "New energy feed-in electricity enters electricity markets and prices are formed through market transactions. "
        "Eligible mechanism electricity is settled against a mechanism price under stock-project and incremental-project rules."
    ),
    "Compliance calculation methodology I": "Settlement difference = mechanism electricity quantity x (mechanism electricity price - market transaction average price).",
    "Compliance calculation methodology II": (
        "If the market transaction average price is below the mechanism electricity price, the difference is paid "
        "to the new energy generator; if it is above, the generator pays the difference back."
    ),
    "Subsidy: annual budget/ expenditure": "not found",
    "Subsidy: Limit": "Mechanism electricity quantity and mechanism electricity price are determined under stock-project and incremental-project rules; fixed national budget not specified.",
    "Subsidy: Floor or ceiling": "Incremental project mechanism electricity prices are determined through competitive mechanisms; specific provincial prices not found in this national notice.",
    "Subsidy: distribution mechanism": "Two-way difference settlement between market transaction average price and mechanism electricity price for included new energy electricity.",
    "Subsidy: Support duration": "Not specified in the national notice.",
    "Subsidy: Enforcement Mechanism": "Implemented through electricity market settlement and provincial mechanisms for mechanism quantity, mechanism price and cost sharing.",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "D35",
    "GHGs affected": "CO2",
    "Mitigation effects": "positive",
    "Mitigation co-benefits": "Energy supply security; Technological innovation; Industrial development",
    "Legal statute": SOURCE_TITLE,
    "Legal document": SOURCE_URL,
    "Other weblinks": "",
}

COMMON_CN = {
    "Policy Instrument ID": INSTRUMENT_ID,
    "Instrument / subscheme": "工具",
    "Group": "补贴",
    "Approach": "可再生电力差价合约",
    "Emission sector": "能源",
    "Sub-sector": "可再生电力；风电；太阳能发电；新能源发电",
    "Domestic instrument name": "新能源可持续发展价格结算机制",
    "English instrument name": "New energy sustainable price settlement mechanism",
    "Policy Package": "新能源上网电价市场化改革",
    "Description": (
        "中国深化新能源上网电价市场化改革，建立支持新能源可持续发展的价格结算机制。新能源上网电量进入电力市场，"
        "上网电价通过市场交易形成。纳入机制的电量按市场交易均价与机制电价进行差价结算：市场均价低于机制电价时，"
        "向新能源发电企业支付差价；市场均价高于机制电价时，由新能源发电企业返还差价。"
    ),
    "Objective": "可再生能源发展和消纳；绿色经济",
    "Mitigation relevance": "直接",
    "Functioning channel": "供给侧",
    "Country": "中国",
    "Jurisdiction level": "国家",
    "Jurisdiction name": "N/A",
    "Adoption date": "27/01/2025",
    "Start date": "01/06/2025",
    "End date": "N/A",
    "Last revisions": "27/01/2025",
    "Last revisions (Details)": "2025年国家发展改革委、国家能源局通知建立新能源可持续发展价格结算机制，并推动新能源上网电量全面进入电力市场；存量项目与现行价格政策衔接，增量项目机制电价通过市场化竞争确定。",
    "Status": "生效",
    "Administrating authorities": "国家发展改革委；国家能源局；省级价格和能源主管部门；电力市场运营机构",
    "Asset": "电力；太阳能；风能；其他可再生能源",
    "Asset (Status)": "新建；既有",
    "Asset (Details)": "符合机制条件的新能源项目上网电量，包括存量项目和增量项目，主要包括风电、太阳能发电等新能源发电。",
    "Asset (Other)": "N/A",
    "Asset (Cut-off range)": "纳入价格结算机制的电量；存量项目和增量项目分别适用不同规则，增量项目机制电价通过竞争机制确定。",
    "Agent": "企业",
    "Agent (Detail)": "参与机制结算或费用分摊的新能源发电企业和电力市场主体。",
    "Activity": "可再生电力发电和价格结算",
    "Activity (Details)": "符合条件的新能源电量发电、进入市场交易，并按机制电价进行差价结算。",
    "Intensity (Value)": "公式",
    "Intensity (Unit)": "元/兆瓦时价差",
    "Intensity (Details)": "差价结算金额依据机制电量乘以机制电价与市场交易均价的差额计算；市场均价低于机制电价时形成对发电企业的支付，高于机制电价时由发电企业返还差价；来源为2025年国家发展改革委、国家能源局通知。",
    "Requirement specification": "新能源上网电量进入电力市场、上网电价通过市场交易形成；纳入机制的电量按存量项目和增量项目规则与机制电价结算。",
    "Compliance calculation methodology I": "差价结算金额 = 机制电量 ×（机制电价 - 市场交易均价）。",
    "Compliance calculation methodology II": "市场交易均价低于机制电价时，向新能源发电企业支付差价；高于机制电价时，由新能源发电企业返还差价。",
    "Subsidy: annual budget/ expenditure": "未找到",
    "Subsidy: Limit": "机制电量规模和机制电价按存量项目、增量项目规则确定；国家通知未规定固定全国预算。",
    "Subsidy: Floor or ceiling": "增量项目机制电价通过竞争机制确定；本国家通知未找到具体省级价格。",
    "Subsidy: distribution mechanism": "纳入机制的新能源电量按市场交易均价与机制电价进行双向差价结算。",
    "Subsidy: Support duration": "国家通知未明确规定。",
    "Subsidy: Enforcement Mechanism": "通过电力市场结算，以及省级机制电量、机制电价和费用分摊安排执行。",
    "GHG emission coverage (absolute)": "N/A",
    "GHG emission coverage (% domestic emissions)": "N/A",
    "Economic sector": "D35",
    "GHGs affected": "CO2",
    "Mitigation effects": "正向",
    "Mitigation co-benefits": "能源供应安全；技术创新；工业发展",
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
            "confidence_score": "0.72",
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
