#!/usr/bin/env python3
"""Insert Information instrument (CBA group):
   - CHNCBAGSSI01S000 (Green Manufacturing Standard System)
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
    make_row(
        pid="CHNCBAGSSI01S000",
        group_cn="能力建设与公众意识",
        approach_cn="绿色标准体系",
        sector="工业",
        subsector="N/A",
        name_cn="绿色制造标准体系",
        name_en="Green Manufacturing Standard System",
        description=(
            "绿色制造标准体系是由工业和信息化部与国家标准化管理委员会联合建立"
            "的标准制定计划，以《绿色制造标准体系建设指南》（工信部联节〔2016〕"
            "304号，2016年9月7日发布）为核心文件，构建覆盖制造业绿色转型全维度"
            "的标准体系框架。标准体系分为七个子体系：综合基础、绿色产品、"
            "绿色工厂、绿色企业、绿色园区、绿色供应链及绿色评价与服务，覆盖19个"
            "制造业行业。建设目标分阶段推进：到2020年制定一批基础通用和关键核心"
            "标准，形成基本健全的标准体系；到2025年绿色制造标准在各行业普遍应用，"
            "形成较为完善的标准体系。截至2025年，已累计制定发布绿色工厂评价相关"
            "标准450余项（覆盖工业领域29个大类、100个中类、334个小类），绿色产品"
            "（产品绿色设计）标准近200项，绿色供应链管理国家标准9项及行业/团体标准"
            "20余项，绿色园区评价国家标准在制定中。标准体系中除基础通用的推荐性"
            "国家标准（GB/T）外，也包括部分强制性国家标准（GB，如能耗限额标准），"
            "各标准具有各自独立的效力和适用场景。全国绿色制造技术标准化技术委员会"
            "（SAC/TC 337）为绿色制造标准化的主要技术归口机构。"
        ),
        objective=(
            "建立统一协调的绿色制造标准体系框架；为绿色工厂、绿色产品、绿色园区"
            "和绿色供应链的评价、认证和推广提供技术标准基础；规范和引领制造业绿色"
            "低碳转型；减少标准重复和碎片化；支撑《中国制造2025》绿色制造战略的"
            "实施"
        ),
        mitigation="间接",
        channel="供给侧",
        adoption="07/09/2016",
        effective="07/09/2016",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "工业和信息化部（节能与综合利用司）；国家标准化管理委员会；全国绿色"
            "制造技术标准化技术委员会（SAC/TC 337，技术归口）"
        ),
        asset="绿色制造标准体系（标准/信息基础设施）",
        asset_status="新建",
        asset_detail=(
            "本工具为政府主导的标准体系规划和标准制定协调计划，界定和覆盖的对象为"
            "绿色制造领域的技术标准体系框架，涵盖综合基础、绿色产品、绿色工厂、"
            "绿色企业、绿色园区、绿色供应链及绿色评价与服务七个子体系。至2025年"
            "已累计制定发布各级标准约700项，包括推荐性国家标准（GB/T）、强制性"
            "国家标准（GB）、行业标准（JC/QB/HG等）和团体标准。各具体标准具有"
            "独立的效力和适用场景。"
        ),
        agent="企业（标准的使用者）；标准化技术机构（标准的制定者）",
        agent_detail=(
            "绿色制造领域标准的制定由全国绿色制造技术标准化技术委员会（SAC/TC "
            "337）及相关行业标准化技术委员会承担。标准的使用者为制造业企业，涵盖"
            "各行业规模以上工业企业，企业可自愿采用推荐性标准（GB/T）或遵循强制性"
            "标准（GB）。"
        ),
        activity="研究与开发",
        activity_detail=(
            "政府部门联合标准化管理机构制定标准体系框架和路线图；标准化技术委员会"
            "组织标准的调研、起草、征求意见、审查和报批；标准经批准后通过全国标准"
            "信息公共服务平台发布；制造业企业根据标准的性质和自身需要选择采用或将"
            "标准要求转化为企业生产和管理活动。标准体系规划为指导性和协调性文件，"
            "不设强制性合规义务和处罚；但体系内包括的强制性国家标准（GB，如能耗"
            "限额）具有法律约束力。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）工业和信息化部与国家标准委联合发布标准体系建设指南，确立7个子体系"
            "的架构；2）根据标准体系建设指南确定各领域标准制定的优先序和任务分工；"
            "3）各标准化技术委员会按照标准化工作程序组织具体标准的研究和制定工作；"
            "4）标准的制修订遵循《标准化法》规定的程序（立项、起草、征求意见、审查、"
            "批准、发布）；5）对标准体系实施效果进行跟踪评估并适时修订完善。标准体系"
            "规划本身为指导性文件，不设强制性合规义务。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "为绿色工厂梯度培育管理（CHNCBACBPI01S000）、绿色设计产品评价、"
            "绿色园区评价以及绿色供应链管理评价等绿色制造体系应用层仪器提供标准"
            "基础。与国家能耗限额标准（GB系列）、排污许可相关技术规范、碳排放"
            "核算与报告标准（GB/T 32150/32151系列）、绿色产品认证标准等互补衔接。"
            "为绿色金融目录（如绿色金融支持项目目录）中的绿色产业识别提供技术标准"
            "依据。"
        ),
        resp_info_capture=(
            "工业和信息化部与国家标准委联合发布标准体系建设指南；各标准化技术"
            "委员会（以SAC/TC 337为主）负责标准的起草和技术归口；全国标准信息"
            "公共服务平台（std.samr.gov.cn）和全国标准全文公开系统为标准的发布和"
            "查询平台。"
        ),
        info_transmission=(
            "标准体系建设指南通过工业和信息化部网站和政府公报发布；已制定发布的"
            "标准通过全国标准信息公共服务平台和全国标准全文公开系统向社会公开。"
        ),
        info_frequency="标准体系按建设目标分阶段推进（2020年、2025年目标）；具体标准按标准化工作程序持续制修订。",
        info_public=(
            "是（公开）。标准体系建设指南全文通过工业和信息化部网站公开发布。"
            "已发布的国家标准和行业标准文本通过全国标准信息公共服务平台和全国标准"
            "全文公开系统向社会公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "工业和信息化部组织标准体系建设指南的释义和宣贯培训；全国绿色制造技术"
            "标准化技术委员会和各行业标准化技术委员会组织开展标准起草人员培训和"
            "标准宣贯解读；通过绿色制造公共服务平台（gmpsp.org.cn）发布和推广标准"
            "信息；组织绿色制造标准化试点示范和经验交流。"
        ),
        ghg_abs=(
            "N/A（本工具为标准体系规划，通过构建绿色制造技术标准基础、引导和规范"
            "制造业绿色低碳转型间接促进温室气体减排，无直接可量化的排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接能力建设工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="C",
        ghg="CO2; CH4; N2O; HFCs; PFCs; SF6; NF3",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新；能效提升；污染防治；资源节约；循环经济",
        legal_name=(
            "工业和信息化部 国家标准化管理委员会关于印发《绿色制造标准体系建设"
            "指南》的通知（工信部联节〔2016〕304号）"
        ),
        legal_url=(
            "https://www.miit.gov.cn/jgsj/jns/wjfb/art/2020/"
            "art_d364c0664fc04535addaeb550cd45f76.html"
        ),
        other_links=(
            "https://www.gov.cn/xinwen/2016-09/29/content_5113568.htm；"
            "https://std.samr.gov.cn/（全国标准信息公共服务平台）"
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

        # Insert after the last CBA row to keep approach grouping
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
