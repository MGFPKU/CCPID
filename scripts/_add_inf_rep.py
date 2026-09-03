#!/usr/bin/env python3
"""Insert two new Information instruments (Reporting requirements group):
   - CHNREPESAI01S000 (Public institution energy consumption statistics survey and audit)
   - CHNREPSIDI01S000 (Enterprise environmental information disclosure system)
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_information_instruments.csv"

# 57-column CN template header for Information instruments (matches xlsx)
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
    name_cn, name_en, description, objective,
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
):
    return (
        pid, "工具", group_cn, approach_cn, sector, subsector,
        name_cn, name_en, "N/A", description, objective,
        mitigation, channel, "中国", "国家", "N/A",
        adoption, effective, "N/A", revision, revision_detail, status,
        admin_authorities, asset, asset_status, asset_detail,
        "N/A", "N/A", agent, agent_detail, activity, activity_detail,
        intensity_val, intensity_unit, intensity_detail, req_spec,
        calc_i, calc_ii, instrument_linkage, resp_info_capture,
        info_transmission, info_frequency, info_public,
        label_type, monitoring, enforcement, promotion,
        capacity_building, ghg_abs, ghg_pct, isic, ghg,
        mitigation_effects, co_benefits, legal_name, legal_url, other_links,
    )


ROWS = [
    # ============================================================
    # ESA01 — Public institution energy consumption statistics survey and audit
    # ============================================================
    make_row(
        pid="CHNREPESAI01S000",
        group_cn="报告与披露要求",
        approach_cn="能源统计与审计",
        sector="建筑；交通",
        subsector="公共机构（党政机关、事业单位、团体组织）",
        name_cn="公共机构能源消费统计调查与审计",
        name_en="Public Institution Energy Consumption Statistics Survey and Audit",
        description=(
            "公共机构能源消费统计调查与审计制度依据《公共机构节能条例》"
            "（国务院令第531号，2008年公布）建立，由国家机关事务管理局会同国家"
            "统计局等部门组织实施。制度包括两个相互衔接的部分：（1）能源资源消费"
            "统计调查——公共机构须按照《公共机构能源资源消费统计制度》定期报送"
            "用电、用水、用气、用油、用热以及建筑面积、用能人数、公务用车等能源"
            "资源消费数据，实行分级分类、逐级审核汇总的统计报表制度，覆盖全国党政"
            "机关、事业单位和团体组织；（2）能源审计——依据《公共机构能源审计管理"
            "暂行办法》，对重点用能公共机构定期开展能源审计，核查其能源消费、用能"
            "系统效率和节能管理状况，提出节能改进措施并跟踪整改。通过统计调查掌握"
            "公共机构能源消费底数、通过能源审计诊断用能问题，为公共机构能耗定额"
            "管理、节能目标考核和节约型机关建设提供信息基础。"
        ),
        objective="推动公共机构节能；提高能源利用效率；发挥公共机构节能表率作用",
        mitigation="间接",
        channel="需求侧",
        adoption="01/08/2008",
        effective="01/10/2008",
        revision="01/03/2017",
        revision_detail=(
            "《公共机构节能条例》于2008年8月1日公布、2008年10月1日施行，"
            "2017年3月1日根据《国务院关于修改和废止部分行政法规的决定》"
            "（国务院令第686号）修订。配套的《公共机构能源资源消费统计制度》由"
            "国家机关事务管理局会同国家统计局制定，并根据工作需要定期修订更新"
            "统计指标和报表；《公共机构能源审计管理暂行办法》对公共机构能源审计"
            "的组织实施作出具体规定。"
        ),
        status="生效",
        admin_authorities=(
            "国家机关事务管理局；国家统计局；国家发展和改革委员会；"
            "县级以上人民政府管理机关事务工作的机构"
        ),
        asset="公共机构建筑、用能系统及公务用车",
        asset_status="既有",
        asset_detail=(
            "统计和审计对象为公共机构（全部或者部分使用财政性资金的国家机关、"
            "事业单位和团体组织）的能源资源消费，涵盖办公建筑及其供暖、通风、"
            "空调、照明、热水等用能系统，以及公务用车、数据中心等用能设施。"
        ),
        agent="公共机构（国家机关、事业单位、团体组织）",
        agent_detail=(
            "全部或者部分使用财政性资金的国家机关、事业单位和团体组织。中央"
            "国家机关及所属公共机构、地方各级公共机构分级组织统计和审计。重点"
            "用能公共机构（能源消费量较大或具有示范意义的公共机构）为能源审计"
            "的重点对象。"
        ),
        activity="使用",
        activity_detail=(
            "公共机构在日常运行中消费能源资源的活动。公共机构须建立能源资源"
            "消费统计台账，按季度/年度报送能源资源消费数据；重点用能单位须配合"
            "开展能源审计，接受用能状况核查和节能诊断。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）公共机构须指定专门机构或人员负责能源资源消费统计，建立统计台账，"
            "按照《公共机构能源资源消费统计制度》规定的指标、口径和报表格式，"
            "通过统计信息系统逐级报送能源资源消费数据（含用电、水、气、油、集中"
            "供热及建筑面积、用能人数、公务用车数量和行驶里程等）；2）统计数据"
            "实行分级审核、逐级汇总，管理机关事务工作的机构负责本级公共机构统计"
            "数据的审核汇总；3）重点用能公共机构须按规定周期接受能源审计，审计"
            "内容包括能源消费核算、用能系统效率检测、节能管理制度评价等，并根据"
            "审计结论制定和落实节能整改措施；4）能源资源消费统计数据和能源审计"
            "结果作为公共机构能耗定额、节能目标责任考核和节约型机关创建的依据。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与公共机构能耗定额管理和节能目标责任考核联动：统计数据是能耗定额"
            "核定和目标考核的基础。与公共机构节能规划和节约型机关创建联动：审计"
            "结论为节能改造和管理提升提供依据。与国家能源资源消费统计和政府能耗"
            "监管平台联动：数据纳入公共机构能源资源消费统计信息系统。"
        ),
        resp_info_capture=(
            "公共机构指定的能源资源消费统计人员负责数据采集、台账记录和报表填报；"
            "管理机关事务工作的机构负责逐级审核汇总；能源审计由公共机构委托具备"
            "资质的能源审计机构或由管理机关事务工作的机构组织实施。"
        ),
        info_transmission=(
            "通过公共机构能源资源消费统计信息系统在线填报和逐级上报（网络报送）；"
            "能源审计报告以书面形式提交管理机关事务工作的机构。"
        ),
        info_frequency="能源资源消费统计按季度和年度定期报送；能源审计按规定周期（一般每若干年一次）对重点用能公共机构开展。",
        info_public=(
            "是（部分公开）。国家机关事务管理局定期汇总并通报全国公共机构能源"
            "资源消费统计情况，部分汇总数据向社会公开；单个公共机构的详细能耗"
            "数据主要用于节能管理和目标考核。"
        ),
        label_type="N/A",
        monitoring="政府机构开展的监督检查",
        enforcement="行政处罚；通报批评；责令整改",
        promotion="表彰奖励",
        capacity_building=(
            "组织开展公共机构能源资源消费统计和能源审计业务培训；推广能耗监测"
            "和统计信息化系统；结合节约型机关创建开展节能宣传。"
        ),
        ghg_abs="N/A",
        ghg_pct="N/A",
        isic="O84; P85; Q86",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="能效提升；能源消耗减少；资源节约",
        legal_name="公共机构节能条例（国务院令第531号）",
        legal_url="https://www.gov.cn/zhengce/2008-08/11/content_2602516.htm",
        other_links="公共机构能源审计管理暂行办法：https://gbc.ggj.gov.cn/zcfg/bmgz/202201/t20220126_34491.htm",
    ),

    # ============================================================
    # EID01 — Enterprise environmental information disclosure system
    # ============================================================
    make_row(
        pid="CHNREPSIDI01S000",
        group_cn="报告与披露要求",
        approach_cn="可持续信息披露",
        sector="工业",
        subsector="重点排污行业（电力、钢铁、建材、化工、石化等）",
        name_cn="企业环境信息依法披露制度",
        name_en="Enterprise Environmental Information Disclosure System",
        description=(
            "企业环境信息依法披露制度是要求企业依法披露环境信息的强制性信息公开"
            "制度。现行制度以生态环境部2021年印发的《环境信息依法披露制度改革"
            "方案》和2021年12月发布的《企业环境信息依法披露管理办法》（生态环境"
            "部令第24号，2022年2月8日施行）为核心，并配套《企业环境信息依法披露"
            "格式准则》。制度沿革可追溯至2007年《环境信息公开办法（试行）》"
            "（国家环境保护总局令第35号）和2014年《企业事业单位环境信息公开办法》"
            "（环境保护部令第31号）。制度明确五类企业为强制披露主体：重点排污"
            "单位、实施强制性清洁生产审核的企业、因生态环境违法行为被追究刑事责任"
            "或受到重大行政处罚的企业，以及符合规定情形的上市公司和发债企业。"
            "披露内容涵盖企业基本信息、污染物产生排放及防治设施情况、碳排放信息、"
            "生态环境行政许可和处罚信息、清洁生产及强制性清洁生产审核信息等。"
            "企业须通过统一的企业环境信息依法披露系统编制并公开年度环境信息依法"
            "披露报告和临时环境信息依法披露报告。"
        ),
        objective="规范企业环境信息依法披露；加强社会监督；保障公众环境知情权、参与权和监督权",
        mitigation="间接",
        channel="供给侧",
        adoption="11/04/2007",
        effective="01/05/2008",
        revision="11/12/2021",
        revision_detail=(
            "制度沿革：2007年4月11日《环境信息公开办法（试行）》（国家环境保护"
            "总局令第35号）公布、2008年5月1日施行，首次确立环境信息公开（含企业"
            "环境信息公开）制度；2014年12月19日《企业事业单位环境信息公开办法》"
            "（环境保护部令第31号）公布、2015年1月1日施行，强化重点排污单位强制"
            "公开；2021年生态环境部印发《环境信息依法披露制度改革方案》，2021年"
            "12月《企业环境信息依法披露管理办法》（生态环境部令第24号）发布、"
            "2022年2月8日施行，并配套《企业环境信息依法披露格式准则》，将企业"
            "环境信息公开升级为依法强制披露制度，新增碳排放信息披露要求，建立"
            "统一的企业环境信息依法披露系统。"
        ),
        status="生效",
        admin_authorities="生态环境部；地方各级生态环境主管部门",
        asset="工业企业及其生产经营设施",
        asset_status="既有",
        asset_detail=(
            "披露主体为五类企业：（1）重点排污单位；（2）实施强制性清洁生产审核"
            "的企业；（3）因生态环境违法行为被追究刑事责任或受到较大数额罚款等"
            "重大行政处罚的企业；（4）符合规定情形的上市公司；（5）符合规定情形"
            "的发债企业。涉及的生产设施涵盖排放大气污染物、水污染物、固体废物"
            "以及产生碳排放的工业生产装置和污染防治设施。"
        ),
        agent="企业",
        agent_detail=(
            "依法负有环境信息强制披露义务的企业，包括重点排污单位、实施强制性"
            "清洁生产审核的企业、受到重大生态环境行政处罚或被追究刑事责任的企业，"
            "以及符合规定情形的上市公司和发债企业。企业对所披露环境信息的真实性、"
            "准确性、完整性和及时性负责。"
        ),
        activity="生产",
        activity_detail=(
            "企业在生产经营过程中产生污染物排放、碳排放和环境影响的活动。企业须"
            "依法编制并公开年度环境信息依法披露报告，在发生受到重大行政处罚、被"
            "追究刑事责任、发行股票或债券等特定情形时编制并公开临时环境信息依法"
            "披露报告，通过企业环境信息依法披露系统向社会披露。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）强制披露主体须于每年规定期限内（一般为次年3月15日前）通过企业"
            "环境信息依法披露系统编制并公开上一年度《企业环境信息依法披露报告》；"
            "2）发生规定情形（如受到重大行政处罚、被追究刑事责任、上市公司再融资、"
            "发债等）的，须在规定时限内编制并公开临时环境信息依法披露报告；"
            "3）披露内容须符合《企业环境信息依法披露格式准则》，涵盖企业基本信息、"
            "企业环境管理信息、污染物产生治理与排放信息、碳排放信息、生态环境"
            "应急信息、生态环境违法信息、本年度临时环境信息依法披露情况等；"
            "4）企业对披露信息的真实性、准确性、完整性负责，披露信息长期公开、"
            "可查询；5）生态环境主管部门对披露情况进行监督检查，对未按规定披露"
            "或披露不实的依法查处并纳入信用记录。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与排污许可制度联动：重点排污单位范围和污染物排放信息与排污许可证"
            "载明事项衔接。与强制性清洁生产审核制度联动：实施强制性清洁生产审核"
            "的企业须披露审核信息。与企业环境信用评价和绿色金融联动：披露信息"
            "作为环境信用评价、绿色信贷和绿色债券评估的重要依据。与碳排放报告"
            "制度联动：纳入碳排放信息披露要求。"
        ),
        resp_info_capture=(
            "企业自行编制环境信息依法披露报告并对其真实性负责，通过生态环境部"
            "建立的企业环境信息依法披露系统在线填报和公开；生态环境主管部门负责"
            "系统的建设、维护和监督管理，并可对披露信息进行抽查核实。"
        ),
        info_transmission=(
            "通过全国统一的企业环境信息依法披露系统在线编制、上传和公开（网络"
            "披露）；披露报告向社会公开，公众可通过系统查询。"
        ),
        info_frequency="年度报告每年披露一次（一般于次年3月15日前）；临时报告在发生规定情形后的规定时限内披露。",
        info_public=(
            "是。企业环境信息依法披露报告通过全国统一的企业环境信息依法披露"
            "系统向社会公开，公众、投资者、金融机构和监管部门可在线查询，披露"
            "信息长期留存可追溯。"
        ),
        label_type="N/A",
        monitoring="政府机构开展的监督检查",
        enforcement="行政处罚；罚款；责令改正；纳入信用记录",
        promotion="环境信用评价激励",
        capacity_building=(
            "组织开展企业环境信息依法披露培训和政策宣贯；建设和推广企业环境信息"
            "依法披露系统；发布格式准则和填报指南，指导企业规范披露。"
        ),
        ghg_abs="N/A",
        ghg_pct="N/A",
        isic="C19; C20; C23; C24; D35",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="污染防治；空气污染物减排；技术创新",
        legal_name="企业环境信息依法披露管理办法（生态环境部令第24号）",
        legal_url="https://www.mee.gov.cn/xxgk2018/xxgk/xxgk02/202112/t20211221_964837.html",
        other_links="环境信息公开办法（试行）（国家环境保护总局令第35号）：https://www.gov.cn/gongbao/content/2008/content_892212.htm",
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
    for row in ROWS:
        pid = row[0]
        if any(r and r[0] == pid for r in data):
            print(f"  {pid} already in CSV — skipping")
            continue

        # New group (报告与披露要求) sorts after the existing 比较性能效标签
        # group; append after the last non-empty data row, preserving ROWS order.
        insert_pos = len(data)
        while insert_pos > 0 and not any(data[insert_pos - 1]):
            insert_pos -= 1

        data.insert(insert_pos, list(row))
        inserted += 1
        print(f"  Inserted {pid} at data index {insert_pos}")

    # Drop any stray empty trailing rows before rewriting
    data = [r for r in data if any(r)]

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
