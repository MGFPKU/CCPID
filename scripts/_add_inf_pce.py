#!/usr/bin/env python3
"""Insert Professional certification Information instrument
   (Capacity building and public awareness group):
   - CHNCBAPCEI01S000 (National Occupational Standard for Carbon Emission Administrators)
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
        pid="CHNCBAPCEI01S000",
        group_cn="能力建设与公众意识",
        approach_cn="职业资格认证",
        sector="跨部门",
        subsector="N/A",
        name_cn="碳排放管理员国家职业标准",
        name_en="National Occupational Standard for Carbon Emission Administrators",
        policy_package="N/A",
        description=(
            "碳排放管理员国家职业标准（2023年版）是由人力资源和社会保障部"
            "会同生态环境部联合颁布的国家职业标准，是中国首个碳管理领域的"
            "国家职业资格标准，旨在规范碳排放管理从业者的职业行为、引导职业"
            "教育培训方向并为职业技能等级认定提供依据。标准将碳排放管理员"
            "界定为从事二氧化碳等温室气体排放监测、统计核算、核查、交易和"
            "咨询等工作的人员，职业编码4-09-07-04，标注绿色职业标识（L）。"
            "标准下设六个工种：碳排放监测员、碳排放核算员、碳排放核查员、"
            "碳排放交易员、碳排放咨询员和民航碳排放管理员。职业技能等级分设"
            "五个等级（五级/初级工、四级/中级工、三级/高级工、二级/技师、"
            "一级/高级技师），其中五级/初级工不分工种，碳排放咨询员仅设三级"
            "至一级。标准对各等级的职业功能、工作内容、技能要求和相关知识要求"
            "作出系统规定，并设定培训参考学时（五级不少于40标准学时，二级/一级"
            "不少于100标准学时）和考核标准。标准于2023年9月19日由人力资源和"
            "社会保障部办公厅、生态环境部办公厅联合颁布（人社厅发〔2023〕40号），"
            "2023年9月22日公开发布，自公布之日起施行。牵头起草单位为中国石油"
            "和化学工业联合会，审定单位包括生态环境部环境发展中心、国家应对"
            "气候变化战略研究和国际合作中心、清华大学等。"
        ),
        objective=(
            "规范碳排放管理从业者的职业行为和从业要求；统一碳排放管理职业的"
            "技能标准和等级认定；引导职业教育和技能培训方向，培养碳达峰碳中和"
            "领域急需的专业技能人才；为服务国家碳达峰碳中和战略提供人力资源"
            "支撑"
        ),
        mitigation="直接",
        channel="环境",
        adoption="19/09/2023",
        effective="19/09/2023",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "人力资源和社会保障部；生态环境部"
        ),
        asset="碳排放管理员职业标准与技能等级（人力资源建设）",
        asset_status="N/A",
        asset_detail=(
            "本工具为职业资格标准，界定对象为碳排放管理相关职业的技能要求和"
            "等级认定标准，包括碳排放监测员、核算员、核查员、交易员、咨询员"
            "及民航碳排放管理员六个工种，不直接监管实体排放资产。标准通过"
            "规范从业者技能水平间接支持温室气体排放的准确监测、核算、核查和"
            "管理。"
        ),
        agent="社会公众",
        agent_detail=(
            "拟从事碳排放管理相关工作的人员（含碳排放监测、核算、核查、交易、"
            "咨询等工种）；开展碳排放管理相关培训的职业院校和培训机构；以及"
            "组织实施职业技能等级认定的评价机构。参与为自愿性质，从业者和培训"
            "机构可自主参照标准开展培训和认定。"
        ),
        activity="注册、许可及行政管理",
        activity_detail=(
            "碳排放管理从业人员的职业技能培训、等级认定和从业活动。标准为职业"
            "教育和培训提供统一的内容框架和考核基准，培训机构和职业院校依据"
            "标准设计课程和开展培训，评价机构依据标准实施职业技能等级认定，"
            "从业者通过培训和认定获取相应等级的职业技能证书。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）标准将碳排放管理员职业设五个技能等级（五级/初级工至一级/高级"
            "技师），各等级对应不同的职业功能、工作内容、技能要求和知识要求；"
            "2）各工种（监测员、核算员、核查员、交易员、咨询员、民航碳排放管理"
            "员）有各自的技能要求和考核标准；3）培训参考学时从五级不少于40标准"
            "学时到一级不少于100标准学时不等；4）标准为从业者和培训机构自愿"
            "参照，不设强制性合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与国家职业技能等级认定体系联动：碳排放管理员纳入国家职业技能等级"
            "认定目录（绿色职业标识L）。与温室气体排放报告与核查制度（GRV）"
            "联动：标准为温室气体排放核算和核查岗位人员提供职业能力基准。与"
            "碳排放权交易市场联动：碳排放交易员标准为碳市场参与机构的人员配置"
            "和能力建设提供参考。"
        ),
        resp_info_capture=(
            "人力资源和社会保障部会同生态环境部负责标准的研究编制、颁布和"
            "修订；职业技能等级认定评价机构依据标准对从业人员实施考核和认定。"
        ),
        info_transmission=(
            "人力资源和社会保障部通过官网公开发布标准全文（政府公开发布）；"
            "职业技能等级认定评价机构依据标准发布培训和考核相关信息。"
        ),
        info_frequency=(
            "不定期修订更新（首次颁布为2023年版）。"
        ),
        info_public=(
            "是（公开）。标准通过人力资源和社会保障部官网向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "标准本身就是能力建设的基础性文件。人力资源和社会保障部会同生态"
            "环境部组织推动标准的宣贯和实施；职业院校和培训机构依据标准开发"
            "培训课程和教材；评价机构依据标准建设题库并开展技能等级认定；"
            "相关行业组织、企业和机构参与标准的推广和应用（如中国石油和化学"
            "工业联合会等）。2026年出版配套教材《碳排放核算专业知识与实务》。"
        ),
        ghg_abs=(
            "N/A（本工具为职业资格标准，通过规范碳排放管理从业人员技能水平"
            "间接支持温室气体排放的监测、核算、核查和管理，无直接可量化的"
            "温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接能力建设工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="P85",
        ghg="CO2; CH4; N2O; HFCs; PFCs; SF6; NF3",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新",
        legal_name=(
            "人力资源社会保障部办公厅 生态环境部办公厅关于颁布碳排放管理员"
            "国家职业标准的通知（人社厅发〔2023〕40号）"
        ),
        legal_url=(
            "https://www.mohrss.gov.cn/xxgk2020/fdzdgknr/rcrs_4225/"
            "jnrc/202312/t20231205_510006.html"
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
