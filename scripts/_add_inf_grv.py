#!/usr/bin/env python3
"""Insert a new Information instrument (Reporting requirements group):
   - CHNREPGRVI01S000 (Greenhouse Gas Emissions Reporting and Verification
     System for Key Industries)
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_information_instruments.csv"

# 57-column CN template header for Information instruments
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
    asset_threshold="N/A",
):
    return (
        pid, "工具", group_cn, approach_cn, sector, subsector,
        name_cn, name_en, "ETS", description, objective,
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
        pid="CHNREPGRVI01S000",
        group_cn="报告与披露要求",
        approach_cn="温室气体排放报告",
        sector="工业；交通",
        subsector="发电；钢铁；水泥；电解铝；石化；化工；造纸；民航",
        name_cn="重点行业企业温室气体排放报告与核查制度",
        name_en="Greenhouse Gas Emissions Reporting and Verification System for Key Industries",
        description=(
            "中国重点行业企业温室气体排放报告与核查制度依据碳排放权交易管理"
            "相关法规建立，由生态环境部（原国家发展和改革委员会）组织实施。制度"
            "要求温室气体年排放量达到2.6万吨二氧化碳当量及以上的重点排放单位，"
            "按照统一的技术指南核算和报告其温室气体排放数据，并接受第三方机构的"
            "核查。制度覆盖发电、钢铁、水泥、电解铝、石化、化工、造纸、民航等"
            "重点排放行业。制度内容包括两个相互衔接的部分：（1）排放报告——企业"
            "须按照行业温室气体排放核算与报告指南，编制年度温室气体排放报告，"
            "涵盖化石燃料燃烧排放、工业过程排放、净购入电力/热力排放等，通过"
            "全国碳排放权交易市场管理平台报送；（2）第三方核查——由省级生态环境"
            "主管部门委托具备资质的第三方技术服务机构对企业排放报告进行核查，"
            "核查内容涵盖核算方法合规性、活动数据准确性、排放因子取值合理性和"
            "排放量计算正确性等，出具核查结论并提交核查报告。制度建设可追溯至"
            "2014年《碳排放权交易管理暂行办法》（国家发展改革委令第17号），首次"
            "确立重点排放单位温室气体排放报告与核查义务；2020年《碳排放权交易"
            "管理办法（试行）》（生态环境部令第19号）进一步完善报告核查程序和"
            "技术要求；2024年《碳排放权交易管理暂行条例》（国务院令第775号）将"
            "排放报告与核查制度上升为国务院行政法规层次，明确了企业的报告义务、"
            "第三方核查机构的法律地位、数据质量法律责任和违法处罚。通过排放报告"
            "摸清重点行业温室气体排放底数、通过第三方核查确保数据质量，为碳排放"
            "配额分配与清缴履约、国家温室气体清单编制和低碳发展政策制定提供数据"
            "基础。"
        ),
        objective=(
            "摸清重点行业温室气体排放底数；保障碳排放数据质量；为全国碳排放权"
            "交易市场配额分配和清缴履约提供数据基础；支撑国家温室气体清单编制和"
            "碳达峰碳中和政策制定"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="10/12/2014",
        effective="09/01/2015",
        revision="25/01/2024",
        revision_detail=(
            "制度建设可追溯至2014年12月10日《碳排放权交易管理暂行办法》（国家"
            "发展改革委令第17号，2015年1月9日施行），首次确立重点排放单位温室气体"
            "排放报告与核查义务。2020年12月31日《碳排放权交易管理办法（试行）》"
            "（生态环境部令第19号，2021年2月1日施行）进一步完善报告核查程序、"
            "扩展覆盖行业并细化技术要求，配套发布分行业的温室气体排放核算方法与"
            "报告指南。2024年1月25日《碳排放权交易管理暂行条例》（国务院令第775号，"
            "2024年5月1日施行）将排放报告与核查制度上升为国务院行政法规层次，"
            "明确企业报告义务、第三方核查机构法律地位、数据质量主体责任，并大幅"
            "提高违法处罚力度。"
        ),
        status="生效",
        admin_authorities=(
            "生态环境部（应对气候变化司）；省级生态环境主管部门；设区的市级"
            "生态环境主管部门"
        ),
        asset="重点排放单位的生产设施和排放源",
        asset_status="既有",
        asset_detail=(
            "温室气体年排放量达到2.6万吨二氧化碳当量及以上的重点排放单位所拥有"
            "或控制的生产设施和排放源。涵盖化石燃料燃烧排放（锅炉、窑炉、燃气"
            "轮机等固定燃烧装置）、工业过程排放（水泥熟料煅烧、石灰石分解、钢铁"
            "冶炼、电解铝阳极效应等）、净购入电力及热力产生的间接排放。覆盖行业"
            "包括发电、钢铁、水泥、电解铝、石化、化工、造纸、民航等。"
        ),
        agent="企业",
        agent_detail=(
            "年度温室气体排放量达到2.6万吨二氧化碳当量及以上的企业或者其他经济"
            "组织。重点排放单位须对其温室气体排放数据进行核算，编制年度排放报告，"
            "对所报告数据的真实性、完整性和准确性负责，并配合第三方核查机构开展"
            "核查工作。"
        ),
        activity="生产",
        activity_detail=(
            "重点排放单位在生产经营过程中的温室气体排放活动。企业须按照行业温室"
            "气体排放核算方法与报告指南，对年度排放数据进行核算→通过全国碳排放权"
            "交易市场管理平台提交年度排放报告→配合省级生态环境主管部门委托的第三"
            "方技术服务机构进行核查→对核查发现的问题进行整改或说明→省级生态环境"
            "主管部门审核并出具核查结论。排放报告和核查结果作为碳排放配额清缴的"
            "依据。"
        ),
        intensity_val="2.6万",
        intensity_unit="吨二氧化碳当量/年",
        intensity_detail="纳入温室气体排放报告与核查管理的温室气体年排放量阈值门槛，即年排放量达2.6万吨二氧化碳当量及以上的企业须纳入报告与核查范围。来源：《碳排放权交易管理暂行条例》及生态环境部相关通知。",
        req_spec=(
            "1）重点排放单位须于每年规定期限内（一般为次年3月31日前）编制上一年度"
            "温室气体排放报告，报告内容涵盖企业基本信息、核算边界、排放源和气体"
            "种类、活动数据及来源、排放因子数据及来源、排放量计算结果等，按照行业"
            "温室气体排放核算方法与报告指南编制；2）排放报告通过全国碳排放权交易"
            "市场管理平台在线报送；3）省级生态环境主管部门委托具备资质的第三方"
            "技术服务机构对排放报告进行核查，核查机构须独立、客观、公正，对核查"
            "结论负责；4）核查内容包括核算方法合规性、活动数据准确性、排放因子"
            "取值合理性、排放量计算正确性、数据质量控制计划执行情况等，核查机构"
            "出具核查报告和核查结论；5）企业对核查发现的问题须在规定时限内整改"
            "或说明，逾期未改的由生态环境主管部门依法处理；6）重点排放单位须妥善"
            "保存排放报告、核查报告和相关原始数据记录，保存期限不少于五年；"
            "7）重点排放单位对排放报告的真实性、完整性和准确性负责，不得弄虚作假。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与碳排放权交易市场（ETS）深度联动：排放报告和核查结果是碳排放配额"
            "分配、清缴履约和碳排放权交易的基础数据来源，重点排放单位名录与碳市场"
            "覆盖主体高度重合。与国家温室气体清单编制联动：分行业、分区域的排放"
            "报告数据为国家温室气体清单提供重要基础信息。与企业环境信息依法披露"
            "制度（EID）联动：碳排放信息是环境信息披露的重要组成部分，两套制度在"
            "碳排放信息披露方面相互补充。与碳排放标准（核算指南）联动：排放报告"
            "编制须依据行业温室气体排放核算方法与报告指南。"
        ),
        resp_info_capture=(
            "重点排放单位自行或委托技术服务机构按照行业温室气体排放核算方法与"
            "报告指南进行排放数据核算，编制年度排放报告；省级生态环境主管部门委托"
            "具备资质的第三方技术服务机构对排放报告进行核查并出具核查结论。"
        ),
        info_transmission=(
            "重点排放单位通过全国碳排放权交易市场管理平台（全国碳排放权交易市场"
            "信息网）在线填报和提交年度排放报告（网络报送）；第三方核查机构通过"
            "平台提交核查报告；省级生态环境主管部门通过平台审核确认。"
        ),
        info_frequency=(
            "年度排放报告每年报送一次（一般于次年3月31日前）；第三方核查由省级"
            "生态环境主管部门在排放报告提交后统一组织开展（每年一次）。"
        ),
        info_public=(
            "是（部分公开）。省级生态环境主管部门将重点排放单位名录和排放报告"
            "核查结果向社会公开；单个企业的详细排放数据主要服务于碳市场履约和政府"
            "统计，部分汇总数据可通过全国碳排放权交易市场信息网查询。"
        ),
        label_type="N/A",
        monitoring="政府机构开展的监督检查",
        enforcement="行政处罚；罚款；责令改正；纳入信用记录",
        promotion="其他激励或支持",
        capacity_building=(
            "组织开展重点行业企业温室气体排放核算与报告能力建设培训；发布分行业"
            "温室气体排放核算方法与报告指南及配套技术文件；建设全国碳排放权交易"
            "市场管理平台并提供在线填报和核查系统培训；组织开展第三方核查机构资质"
            "认定和核查人员业务培训。"
        ),
        ghg_abs=(
            "八行业合计覆盖排放量约为70-80亿吨CO2（来源：发电行业约2200家重点"
            "排放单位年排放量约50亿吨CO2；钢铁行业约2.3亿吨、水泥行业约1.5亿吨、"
            "电解铝行业约1.2亿吨、石化行业约2亿吨、化工行业约1.2亿吨、造纸行业"
            "约0.5亿吨、民航约0.2亿吨，合计八行业年排放量约70-80亿吨CO2。"
            "上述数据基于分行业典型企业年排放量及行业总产量估算。碳市场当前交易"
            "覆盖量约50亿吨CO2，报告核查覆盖范围大于交易覆盖范围。）"
        ),
        ghg_pct=(
            "覆盖约60%以上全国温室气体排放（来源：基于八行业合计排放量约占全国"
            "温室气体排放总量的60-65%。全国温室气体排放总量约120-130亿吨CO2e；"
            "发电行业约占总排放40%，钢铁、水泥、电解铝、石化、化工、造纸、民航"
            "合计约占总排放20-25%。报告核查覆盖范围大于碳市场交易覆盖范围"
            "（约40%）。）"
        ),
        isic="D35; C24; C23; C20; C21; C17; H51",
        ghg="CO2; CH4; N2O; HFCs; PFCs; SF6",
        mitigation_effects="正向",
        co_benefits="污染防治；空气污染物减排；能效提升",
        legal_name=(
            "关于做好2023—2025年部分重点行业企业温室气体排放报告"
            "与核查工作的通知"
        ),
        legal_url="https://www.mee.gov.cn/xxgk2018/xxgk/xxgk06/202310/t20231018_1043427.html",
        asset_threshold="≥2.6万吨CO2e/年",
        other_links=(
            "碳排放权交易管理暂行条例（国务院令第775号）："
            "https://www.gov.cn/zhengce/content/202402/content_6929567.htm；"
            "碳排放权交易管理办法（试行）（生态环境部令第19号）："
            "https://www.mee.gov.cn/xxgk2018/xxgk/xxgk02/202101/"
            "t20210105_816131.html"
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
    for row in ROWS:
        pid = row[0]
        if any(r and r[0] == pid for r in data):
            print(f"  {pid} already in CSV — skipping")
            continue

        # Insert after the last Reporting requirements (REP) group row
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][2] == "报告与披露要求":
                insert_pos = i + 1

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
