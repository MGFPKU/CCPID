#!/usr/bin/env python3
"""Insert Education system integration Information instrument
   (Capacity building and public awareness group):
   - CHNCBAESII01S000 (Green Low-Carbon Development National Education System Implementation Plan)
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
        pid="CHNCBAESII01S000",
        group_cn="能力建设与公众意识",
        approach_cn="教育体系建设",
        sector="跨部门",
        subsector="N/A",
        name_cn="绿色低碳发展国民教育体系建设",
        name_en=(
            "Construction of a Green and Low-Carbon"
            " Development National Education System"
        ),
        policy_package="N/A",
        description=(
            "绿色低碳发展国民教育体系建设是由教育部部署的全国性教育"
            "体系建设，旨在将绿色低碳发展理念全面融入国民教育体系各层次和"
            "各领域，从课程教材、学科专业、教师培训、校园建设等多维度系统构建"
            "绿色低碳育人体系，培养践行绿色低碳理念的新一代青少年和碳达峰碳中和"
            "专业人才。方案设定两阶段目标：到2025年，绿色低碳生活理念与规范在"
            "大中小学普及传播，绿色低碳理念进入大中小学教育体系，全国绿色低碳"
            "领域相关专业布点数不少于600个；到2030年，学生绿色低碳生活方式及"
            "行为习惯系统养成，形成较为完善的多层次绿色低碳理念育人体系。方案"
            "围绕四大板块部署：（一）将绿色低碳发展融入教育教学，包括：将绿色"
            "低碳内容融入学前教育绘本和动画；在基础教育阶段的政治、语文、生物、"
            "地理、物理、化学等学科教材中系统纳入绿色低碳知识；高等教育建立跨"
            "学科碳达峰碳中和核心知识体系并融入思政课；职业教育增设碳排放统计"
            "核算、碳汇计量评估等新兴专业；以及在师范生培养和各级教师培训中"
            "加入碳达峰碳中和知识。（二）以绿色低碳发展引领提升教育服务贡献力，"
            "包括支持高校建设储能、氢能、碳捕集利用与封存、碳排放权交易、碳汇、"
            "绿色金融等碳达峰碳中和相关学科专业，建设全国重点实验室和国家技术"
            "创新中心等国家级创新平台。（三）将绿色低碳发展融入校园建设，包括"
            "完善校园能源管理工作体系、建立能耗监测体系、推广超低能耗建筑和"
            "可再生能源应用。（四）建立跨部门协作、经费保障和宣传引导等保障措施。"
            "方案于2022年10月26日由教育部以教发〔2022〕2号印发。"
        ),
        objective=(
            "将绿色低碳发展理念全面融入国民教育体系各层次和领域；培养践行绿色"
            "低碳理念的新一代青少年；建设碳达峰碳中和相关学科专业体系，培养专业"
            "人才队伍；通过教育体系支撑国家碳达峰碳中和战略实施"
        ),
        mitigation="直接",
        channel="环境",
        adoption="26/10/2022",
        effective="26/10/2022",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities="教育部",
        asset="国民教育体系（课程、学科与校园建设）",
        asset_status="N/A",
        asset_detail=(
            "本工具为教育体系建设方案，界定对象为国民教育体系中与绿色低碳发展"
            "相关的课程教材、学科专业设置、教师培训和校园基础设施建设等，不直接"
            "监管实体排放资产。方案通过教育体系系统性地培养绿色低碳理念和碳达峰"
            "碳中和专业人才，间接支持全社会温室气体减排。"
        ),
        agent="社会公众",
        agent_detail=(
            "各级教育行政部门、大中小学及幼儿园、职业院校和高等学校。方案为"
            "教育行政部门和学校的指导性文件，各级教育行政部门负责制定具体实施"
            "方案并组织落实，学校按照方案要求将绿色低碳理念融入教育教学和校园"
            "建设。不设强制性合规义务和处罚。"
        ),
        activity="生产、发电或转化",
        activity_detail=(
            "教育行政部门和学校的绿色低碳发展教育体系建设活动。教育部制定总体"
            "方案和指导意见→各级教育行政部门制定地方实施方案并组织落实→大中小学"
            "和职业院校将绿色低碳内容融入课程教材、专业设置和校园建设→高等学校"
            "建设碳达峰碳中和相关学科专业和国家级创新平台。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）到2025年绿色低碳生活理念与规范在大中小学普及传播，绿色低碳"
            "理念进入大中小学教育体系，全国绿色低碳领域相关专业布点数不少于"
            "600个；2）到2030年实现学生绿色低碳生活方式及行为习惯系统养成，"
            "形成较为完善的多层次绿色低碳理念育人体系；3）将绿色低碳内容融入"
            "基础教育各相关学科教材和高等教育课程体系；4）增设储能、氢能、碳捕集"
            "利用与封存、碳排放权交易、碳汇、绿色金融等碳达峰碳中和相关学科专业；"
            "5）在师范生培养和各级教师培训中加入碳达峰碳中和知识；6）推动绿色"
            "校园建设和可再生能源应用；7）方案为教育行政部门和学校的指导性文件，"
            "不设强制性合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与全国低碳日（CHNCBAPACI04S000）、全国节能宣传周（CHNCBAPACI03S000）"
            "等公众宣传教育活动联动：各学校在主题日/周期间开展主题班会、知识"
            "竞赛等配套活动。与碳排放管理员国家职业标准（PCE）联动：绿色低碳"
            "相关学科专业建设和职业教育为碳排放管理员等职业人才培养提供教育基础。"
            "与中共中央、国务院《关于完整准确全面贯彻新发展理念做好碳达峰碳中和"
            "工作的意见》和《2030年前碳达峰行动方案》衔接，落实国家碳达峰碳中和"
            "战略对教育体系的要求。"
        ),
        resp_info_capture=(
            "教育部负责方案的总体制定和组织协调；各级教育行政部门按照方案要求"
            "制定地方实施方案，组织辖区内学校落实，并定期总结和上报工作进展。"
        ),
        info_transmission=(
            "教育部通过通知和门户网站公开发布方案（政府公开发布）；各级教育"
            "行政部门转发方案并组织学校落实。"
        ),
        info_frequency=(
            "方案设定2025年和2030年两阶段目标，实施过程中按计划推进和总结。"
        ),
        info_public=(
            "是（公开）。方案通过教育部和国务院门户网站向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "方案本身就是能力建设的顶层设计文件。教育部组织开发绿色低碳发展"
            "相关课程教材和教学资源；在师范生培养、各级教师和校长培训中系统纳入"
            "碳达峰碳中和知识；支持和引导高校加快碳达峰碳中和相关学科专业建设，"
            "推动建设全国重点实验室、国家技术创新中心等国家级创新平台；各地教育"
            "行政部门和学校组织落实方案，开展绿色校园建设和相关教育活动。"
        ),
        ghg_abs=(
            "N/A（本工具为教育体系建设方案，通过教育体系系统性地培养绿色低碳"
            "理念和碳达峰碳中和专业人才间接支持全社会减排，无直接可量化的"
            "温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接能力建设工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="P85",
        ghg="CO2; CH4; N2O; HFCs; PFCs; SF6; NF3",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新；资源节约",
        legal_name=(
            "教育部关于印发《绿色低碳发展国民教育体系建设实施方案》的通知"
            "（教发〔2022〕2号）"
        ),
        legal_url=(
            "https://www.gov.cn/zhengce/zhengceku/2022-11/09/"
            "content_5725566.htm"
        ),
        other_links="N/A",
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

        # CBA group: keep CBA rows contiguous. Insert after last CBA row.
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][2] == "能力建设与公众意识":
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
