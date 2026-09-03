#!/usr/bin/env python3
"""Insert Sustainability/ESG disclosure Information instrument
   (Reporting requirements group):
   - CHNREPSIDI02S000 (Sustainability Reporting Guidelines for Listed Companies)
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_information_instruments.csv"

CN_HEADER = [
    "政策工具ID", "工具/子方案", "组别", "路径", "排放部门", "子行业",
    "本国名称", "英文名称", "政策包", "描述", "目标", "减缓相关性",
    "作用渠道", "国家", "管辖层级", "管辖地名称", "通过日期", "生效日期",
    "终止日期", "最近修订", "最近修订（详情）", "状态", "管理机构",
    "受规制资产", "受规制资产（状态）", "受规制资产（详情）",
    "受规制资产（其他）", "受规制资产（阈值范围）", "受规制主体",
    "受规制主体（详情）", "受规制活动", "受规制活动（详情）",
    "强度（数值）", "强度（单位）", "强度（详情）", "要求说明",
    "合规计算方法I", "合规计算方法II", "工具联动", "信息采集责任方",
    "信息传输方式", "信息提供频率", "信息公开可用性", "标签类型",
    "合规监测", "合规执行", "合规促进",
    "能力建设、培训/教育、宣传和奖励计划详情",
    "温室气体排放覆盖（绝对量）", "温室气体排放覆盖（占国内排放百分比）",
    "经济行业", "受影响的温室气体", "减缓效果", "减缓协同效益",
    "法律文件名称", "法律文件链接", "其他相关网站",
]


def make_row(
    pid, group_cn, approach_cn, sector, subsector,
    name_cn, name_en, policy_package, description, objective,
    mitigation, channel, adoption, effective,
    revision, revision_detail, status,
    admin_authorities, asset, asset_status, asset_detail,
    agent, agent_detail, activity, activity_detail,
    intensity_val, intensity_unit, intensity_detail, req_spec,
    calc_i, calc_ii, instrument_linkage, resp_info_capture,
    info_transmission, info_frequency, info_public,
    label_type, monitoring, enforcement, promotion,
    capacity_building, ghg_abs, ghg_pct, isic, ghg,
    mitigation_effects, co_benefits, legal_name, legal_url, other_links,
    asset_threshold="N/A",
):
    return (
        pid, "工具", group_cn, approach_cn, sector, subsector,
        name_cn, name_en, policy_package, description, objective,
        mitigation, channel, "中国", "国家", "N/A",
        adoption, effective, "N/A", revision, revision_detail, status,
        admin_authorities, asset, asset_status, asset_detail,
        "N/A", asset_threshold, agent, agent_detail, activity, activity_detail,
        intensity_val, intensity_unit, intensity_detail, req_spec,
        calc_i, calc_ii, instrument_linkage, resp_info_capture,
        info_transmission, info_frequency, info_public,
        label_type, monitoring, enforcement, promotion,
        capacity_building, ghg_abs, ghg_pct, isic, ghg,
        mitigation_effects, co_benefits, legal_name, legal_url, other_links,
    )


ROWS = [
    make_row(
        pid="CHNREPSIDI02S000",
        group_cn="报告与披露要求",
        approach_cn="可持续信息披露",
        sector="跨部门",
        subsector="N/A",
        name_cn="上市公司可持续发展报告指引",
        name_en="Sustainability Reporting Guidelines for Listed Companies",
        policy_package="N/A",
        description=(
            "上市公司可持续发展报告指引是由上海证券交易所、深圳证券交易所和"
            "北京证券交易所在中国证监会指导下联合发布的上市公司信息披露规则，"
            "要求符合条件的上市公司按照统一的可持续发展/ESG报告框架进行年度"
            "信息披露。指引覆盖环境、社会和治理（ESG）全维度共21个议题，以"
            "应对气候变化为首要议题，要求披露范围一、范围二温室气体排放（强制）"
            "和范围三温室气体排放（鼓励），以及气候转型风险和机遇的识别与应对"
            "策略。指引采用双重重要性原则（财务重要性和影响重要性），对特定"
            "上市公司群体实施强制披露，对其他上市公司实施自愿披露。强制披露"
            "主体范围包括上证180指数、科创50指数、深证100指数、创业板指数"
            "成分股及境内外同时上市的公司等（约450余家，覆盖A股总市值的50%"
            "以上）。指引于2024年2月8日公开征求意见，2024年4月12日正式发布，"
            "2024年5月1日起施行，首批强制披露的年度报告须于2026年4月30日前"
            "完成（覆盖2025财政年度）。配套发布了《上市公司可持续发展报告编制"
            "指南》（2025年1月发布，2026年1月更新第二版），为上市公司落实"
            "指引要求提供具体操作指导。上交所称为《上海证券交易所上市公司自律"
            "监管指引第14号——可持续发展报告（试行）》，深交所称为《深圳证券"
            "交易所上市公司自律监管指引第17号——可持续发展报告（试行）》，"
            "北交所称为《北京证券交易所上市公司持续监管指引第11号——可持续"
            "发展报告（试行）》。"
        ),
        objective=(
            "规范上市公司可持续发展信息披露行为；提升上市公司ESG信息披露"
            "质量和可比性；引导资本向绿色低碳和可持续发展领域配置；支持国家"
            "碳达峰碳中和目标和可持续发展战略实施"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="12/04/2024",
        effective="01/05/2024",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "中国证券监督管理委员会（指导）；上海证券交易所；深圳证券交易所；"
            "北京证券交易所"
        ),
        asset="上市公司可持续发展报告（企业信息披露）",
        asset_status="N/A",
        asset_detail=(
            "本工具为上市公司可持续/ESG信息披露规则，规范对象为上市公司的"
            "可持续发展报告编制和披露行为，不直接监管实体排放资产。指引要求"
            "上市公司披露气候变化相关议题，包括温室气体排放、气候风险与机遇、"
            "转型计划等信息。"
        ),
        agent="企业",
        agent_detail=(
            "在上交所、深交所和北交所上市的公司。其中上证180指数、科创50指数、"
            "深证100指数、创业板指数成分股及境内外同时上市的公司须按照指引"
            "强制披露可持续发展报告（约450余家，覆盖A股总市值的50%以上）；"
            "其他上市公司自愿披露。披露主体须按照指引框架编制和发布可持续"
            "发展报告或ESG报告，对所披露信息的真实性、准确性和完整性负责。"
        ),
        activity="注册、许可及行政管理",
        activity_detail=(
            "上市公司的可持续发展/ESG信息披露活动。上市公司按照交易所发布的"
            "可持续发展报告指引编制年度可持续发展报告或ESG报告→经董事会审议"
            "通过→在指定信息披露平台（如巨潮资讯网、上交所/深交所/北交所官网）"
            "公开披露→交易所对披露合规性进行监管。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）指引要求符合条件的上市公司在每个会计年度结束后规定期限内编制"
            "并披露可持续发展报告（或ESG报告）；2）披露框架涵盖环境、社会和"
            "治理（ESG）三个维度共21个议题，以应对气候变化为首要议题；3）采用"
            "双重重要性原则（财务重要性和影响重要性）确定披露内容；4）强制"
            "披露范围一、范围二温室气体排放数据（鼓励披露范围三排放）；"
            "5）披露气候相关风险与机遇的识别、评估和管理，包括情景分析（范围一、"
            "二强制，范围三鼓励）和转型计划；6）上市公司须确保披露信息的"
            "真实性、准确性和完整性，不得有虚假记载、误导性陈述或重大遗漏；"
            "7）交易所对上市公司信息披露合规性进行监管。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与《企业可持续披露准则——基本准则（试行）》（财会〔2024〕17号）"
            "和《企业可持续披露准则第1号——气候》（财会〔2025〕34号）等财政"
            "部可持续披露准则体系衔接，指引的披露框架与财政部准则体系协调"
            "互补。与企业环境信息依法披露制度（CHNREPSIDI01S000）同属"
            "可持续信息披露路径，前者覆盖ESG全维度且以资本市场信息披露为场景，"
            "后者聚焦环境维度。与温室气体排放报告"
            "与核查制度（GRV）互补：GRV面向碳市场管控企业，指引面向资本市场"
            "上市公司。"
        ),
        resp_info_capture=(
            "上市公司按照指引框架自行编制可持续发展报告，采集和核算温室气体"
            "排放等ESG数据；鼓励上市公司聘请第三方机构对可持续发展报告进行"
            "鉴证。"
        ),
        info_transmission=(
            "上市公司通过交易所指定的信息披露平台（如上交所官网、深交所官网、"
            "北交所官网、巨潮资讯网等）公开披露可持续发展报告（网络公示）。"
        ),
        info_frequency=(
            "按年度披露（每个会计年度结束后四个月内，与年度报告同时或独立"
            "发布）。"
        ),
        info_public=(
            "是（公开）。上市公司通过交易所指定的信息披露平台向社会公众全文"
            "公开披露可持续发展报告。"
        ),
        label_type="N/A",
        monitoring="政府机构开展的监督检查",
        enforcement="责令改正；通报",
        promotion="其他激励或支持",
        capacity_building=(
            "上交所、深交所、北交所联合发布《上市公司可持续发展报告编制指南》"
            "（2025年1月发布第一版，2026年1月更新第二版），为上市公司落实指引"
            "要求提供操作层面的具体指导；交易所组织开展可持续发展信息披露培训"
            "和交流活动；支持上市公司建立和完善ESG数据采集和管理体系。"
        ),
        ghg_abs=(
            "N/A（本工具为上市公司ESG信息披露规则，通过资本市场信息披露机制"
            "提升企业气候透明度并引导资本导向绿色低碳领域，无直接可量化的"
            "温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接信息披露工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="K64",
        ghg="CO2; CH4; N2O; HFCs; PFCs; SF6; NF3",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新；污染防治",
        legal_name=(
            "上海证券交易所上市公司自律监管指引第14号——可持续发展报告（试行）"
            "；深圳证券交易所上市公司自律监管指引第17号——可持续发展报告（试行）"
            "；北京证券交易所上市公司持续监管指引第11号——可持续发展报告（试行）"
        ),
        legal_url=(
            "https://www.sse.com.cn/lawandrules/sselawsrules2025/"
            "stocks/mainipo/c/c_20250516_10779150.shtml"
        ),
        other_links=(
            "http://www.szse.cn/www/sustainablefinance/document/"
            "guide/t20240412_606839.html；"
            "https://www.bse.cn/cxjg_list/200021393.html；"
            "https://www.sse.com.cn/lawandrules/guide/stock/"
            "zbxxpljg/ssgszljg/c/c_20250117_10770284.shtml"
            "（编制指南）"
        ),
    ),
]


def _load_rows(path: Path) -> list[list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def _write_rows(path: Path, rows: list[list[str]]):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main():
    for row in ROWS:
        if len(row) != 57:
            print(f"ERROR: {row[0]} has {len(row)} columns, expected 57")
            return 1

    if CSV_PATH.exists():
        existing = _load_rows(CSV_PATH)
        header, data = existing[0], existing[1:]
    else:
        header = CN_HEADER
        data = []

    inserted = 0
    updated = 0
    for row in ROWS:
        pid = row[0]
        existing_idx = next((i for i, r in enumerate(data) if r and r[0] == pid), None)
        if existing_idx is not None:
            if data[existing_idx] != list(row):
                data[existing_idx] = list(row)
                updated += 1
                print(f"  Updated {pid} in place at data index {existing_idx}")
            else:
                print(f"  {pid} already up to date — skipping")
            continue

        # Reporting requirements group: insert after last REP row
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][2] == "报告与披露要求":
                insert_pos = i + 1

        data.insert(insert_pos, list(row))
        inserted += 1
        print(f"  Inserted {pid} at data index {insert_pos}")

    data = [r for r in data if any(r)]

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted, {updated} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
