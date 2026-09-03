#!/usr/bin/env python3
"""Insert the Industry guidance catalogue Information instrument
   (Capacity building and public awareness group):
   - CHNCBAIGCI01S000 (Green Low-Carbon Transition Industry Guidance Catalogue, NDRC et al.)
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
        pid="CHNCBAIGCI01S000",
        group_cn="能力建设与公众意识",
        approach_cn="产业指导目录",
        sector="跨部门",
        subsector="N/A",
        name_cn="绿色低碳转型产业指导目录",
        name_en=(
            "Green Low-Carbon Transition Industry Guidance Catalogue"
        ),
        policy_package="N/A",
        description=(
            "绿色低碳转型产业指导目录是由国家发展改革委会同多部门发布的产业"
            "指导类信息工具，通过界定绿色低碳产业范围、统一绿色产业认定标准，"
            "厘清产业边界并引导投资、价格、金融、税收等政策资源投向绿色低碳"
            "领域。目录以产业活动为基础分级分类，涵盖节能降碳产业、环境保护"
            "产业、资源循环利用产业、能源绿色低碳转型、生态保护修复和利用、"
            "基础设施绿色升级、绿色服务等领域，对各类活动明确内涵、界定条件"
            "和适用的法规政策标准。目录建设可追溯至2019年《绿色产业指导目录"
            "（2019年版）》（发改环资〔2019〕293号，由国家发展改革委等7部门"
            "联合印发，分节能环保、清洁生产、清洁能源、生态环境、基础设施"
            "绿色升级、绿色服务6大类）。2024年修订更名为《绿色低碳转型产业"
            "指导目录（2024年版）》（发改环资〔2024〕165号，由国家发展改革委"
            "等10部门联合印发），全面落实碳达峰碳中和战略，调整为节能降碳"
            "产业、环境保护产业、资源循环利用产业等7大类31类二级246类三级"
            "目录，并新增温室气体控制等内容。目录作为各部门制定细化目录、"
            "子目录及配套支持政策的共同基础，为地方、行业和市场主体识别绿色"
            "低碳产业活动提供权威参考。"
        ),
        objective=(
            "厘清绿色低碳产业边界；统一绿色产业认定标准；引导投资、价格、"
            "金融、税收等政策资源投向绿色低碳领域；支撑经济社会发展全面绿色"
            "转型和碳达峰碳中和目标实现"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="14/02/2019",
        effective="14/02/2019",
        revision="29/02/2024",
        revision_detail=(
            "目录建设可追溯至2019年2月14日《绿色产业指导目录（2019年版）》"
            "（发改环资〔2019〕293号），由国家发展改革委、工业和信息化部、"
            "自然资源部、生态环境部、住房城乡建设部、人民银行、国家能源局"
            "等7部门联合印发，设节能环保、清洁生产、清洁能源、生态环境、"
            "基础设施绿色升级、绿色服务6大类。2024年2月修订更名为《绿色"
            "低碳转型产业指导目录（2024年版）》（发改环资〔2024〕165号，"
            "制发日期2024年2月2日），由国家发展改革委等10部门联合印发，"
            "调整为节能降碳产业、环境保护产业、资源循环利用产业、能源绿色"
            "低碳转型、生态保护修复和利用、基础设施绿色升级、绿色服务7大类"
            "（31类二级、246类三级），纳入低碳转型相关产业并新增温室气体"
            "控制等内容。"
        ),
        status="生效",
        admin_authorities=(
            "国家发展改革委、工业和信息化部、自然资源部、生态环境部、住房"
            "城乡建设部、交通运输部、中国人民银行、金融监管总局、中国证监会、"
            "国家能源局（2024年版）；国家发展改革委等7部门（2019年版）"
        ),
        asset="绿色低碳产业活动（产业分类标准）",
        asset_status="N/A",
        asset_detail=(
            "本工具为产业指导目录，界定对象为节能降碳、环境保护、资源循环"
            "利用、绿色能源、生态保护修复、绿色基础设施、绿色服务等领域的"
            "绿色低碳产业活动分类，不直接监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "各领域从事绿色低碳产业活动的企业及相关市场主体，以及依据目录"
            "制定配套政策的各部门和地方。市场主体可自主参考目录识别绿色低碳"
            "产业活动，目录本身为指导性质，不设强制性义务。"
        ),
        activity="生产",
        activity_detail=(
            "目录界定和覆盖的对象为各领域绿色低碳产业的生产活动，涵盖节能降碳、"
            "环境保护、资源循环利用、能源绿色低碳转型、生态保护修复和利用、"
            "基础设施绿色升级、绿色服务等领域中符合条件的产业生产、制造和"
            "服务提供活动。目录对这些绿色低碳产业活动明确内涵、界定条件和适用"
            "的法规政策标准，引导相关生产活动向绿色低碳方向转型。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）目录按产业类别分级分类列出绿色低碳产业活动，对各类活动明确"
            "内涵、界定条件和适用的法规政策标准；2）各地方、各部门以目录为"
            "基础出台投资、价格、金融、税收等配套支持政策，并逐步制定细化"
            "目录或子目录；3）目录为指导性和自愿性质，不设强制性合规义务和"
            "处罚；4）目录适时修订更新，并做好与既有绿色产业支持政策的衔接。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "作为绿色金融、绿色投资、绿色财税等政策的产业界定基础：绿色金融"
            "支持项目目录等即以本目录为编制基础之一。与绿色技术推广目录、"
            "产业结构调整指导目录等形成协同，共同引导产业绿色低碳转型。"
        ),
        resp_info_capture=(
            "国家发展改革委（环境和资源综合利用司）会同相关部门负责组织目录"
            "的研究编制、修订和发布。"
        ),
        info_transmission=(
            "国家发展改革委等部门通过通知和门户网站公开发布目录（政府公开"
            "发布）。"
        ),
        info_frequency=(
            "不定期修订更新（2019年版、2024年版）。"
        ),
        info_public=(
            "是（公开）。目录通过主管部门通知和门户网站向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "国家发展改革委等部门发布目录及解释说明；组织绿色产业专家委员会"
            "提供专业意见；指导各地方、各部门和市场主体依据目录识别和支持"
            "绿色低碳产业活动。"
        ),
        ghg_abs=(
            "N/A（本工具为产业指导目录，通过统一绿色产业标准并引导资源投向"
            "绿色低碳产业间接支持减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接产业指导工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="M72",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新；污染防治；资源节约；循环经济",
        legal_name=(
            "关于印发《绿色低碳转型产业指导目录（2024年版）》的通知"
            "（发改环资〔2024〕165号）"
        ),
        legal_url=(
            "https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=20340"
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

        # Capacity building group (CBA): keep CBA rows contiguous. Insert after
        # the last CBA row if any exist, else append at the end of the file.
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
