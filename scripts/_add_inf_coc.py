#!/usr/bin/env python3
"""Insert Citizen code of conduct (COC) instrument into the Information CN CSV.

   Instrument:
   - CHNCBACOCI01S000  公民生态环境行为规范十条
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

LQ = "“"
RQ = "”"


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
        pid="CHNCBACOCI01S000",
        group_cn="能力建设与公众意识",
        approach_cn="公民行为规范",
        sector="跨部门",
        subsector="N/A",
        name_cn="公民生态环境行为规范十条",
        name_en="Ten Norms of Ecological and Environmental Behavior for Citizens",
        policy_package="N/A",
        description=(
            "公民生态环境行为规范十条由生态环境部、中央精神文明建设办公室、教育部、"
            "共青团中央、全国妇联五部门联合发布，是中国首份国家层面面向全体公民的"
            "综合性生态环境保护行为规范，旨在引导公民在日常生产生活中履行生态环境"
            "保护义务、践行绿色低碳生活方式。规范围绕十个维度提出具体行为指引："
            + LQ + "一、关爱生态环境" + RQ + "（学习生态环境政策法规，了解生物多样性"
            "和气候变化知识）；" + LQ + "二、节约能源资源" + RQ + "（反浪费，实施"
            + LQ + "光盘行动" + RQ + "，使用高能效电器，合理设定空调温度）；"
            + LQ + "三、践行绿色消费" + RQ + "（购买绿色产品，减少一次性用品使用）；"
            + LQ + "四、选择低碳出行" + RQ + "（优先步行、骑行、公共交通，"
            "推广使用新能源汽车）；" + LQ + "五、分类投放垃圾" + RQ + "（学习生活"
            "垃圾分类知识，规范分类投放）；" + LQ + "六、减少污染产生" + RQ + "（不"
            "露天焚烧，减少化学洗涤剂使用，避免噪声扰民）；" + LQ + "七、呵护自然"
            "生态" + RQ + "（参与义务植树，保护野生动植物，拒绝非法野生动植物"
            "制品）；" + LQ + "八、参加环保实践" + RQ + "（参与生态环境志愿服务"
            "和环保宣传）；" + LQ + "九、参与环境监督" + RQ + "（通过举报热线等"
            "渠道举报破坏生态环境行为，包括食品浪费行为监督）；" + LQ + "十、共建"
            "美丽中国" + RQ + "（践行简约适度、绿色低碳、文明健康的生活方式，"
            "从身边小事做起）。规范最早可追溯至2018年6月4日《公民生态环境行为规范"
            "（试行）》（生态环境部公告2018年第12号，2018年6月5日公开发布），系"
            "首部全国性公民生态环境行为规范；2023年5月31日修订发布《公民生态环境"
            "行为规范十条》（生态环境部等五部门公告2023年第17号，2023年6月5日公开"
            "发布），删除" + LQ + "试行" + RQ + "正式命名，纳入气候变化和碳达峰碳"
            "中和等内容，加强对食品浪费、生物多样性保护等行为引导。规范为倡导和指导"
            "性质，对公民不设强制性合规义务和处罚。"
        ),
        objective=(
            "引导公民履行生态环境保护义务；增强全社会生态环保意识；践行简约适度、"
            "绿色低碳、文明健康的生活方式；形成人人、事事、时时、处处崇尚生态文明的"
            "社会氛围；支持美丽中国建设和碳达峰碳中和目标实现"
        ),
        mitigation="直接",
        channel="需求侧",
        adoption="04/06/2018",
        effective="05/06/2018",
        revision="31/05/2023",
        revision_detail=(
            "规范可追溯至2018年6月4日《公民生态环境行为规范（试行）》（生态环境部"
            "公告2018年第12号，2018年6月5日公开发布），系我国首部全国性公民生态"
            "环境行为规范，共十条行为指引。2023年5月31日由生态环境部、中央精神"
            "文明建设办公室、教育部、共青团中央、全国妇联五部门修订发布《公民生态"
            "环境行为规范十条》（公告2023年第17号，2023年6月5日公开发布），主要"
            "修订包括：删除" + LQ + "试行" + RQ + "正式命名为" + LQ + "十条" + RQ +
            "；纳入气候变化和碳达峰碳中和相关内容；强化食品浪费、生物多样性保护等"
            "行为引导；将具体量化建议（如空调温度）调整为" + LQ + "合理设定" + RQ +
            "等原则性表述；将举报热线更新为更广泛的举报渠道表达。"
        ),
        status="生效",
        admin_authorities=(
            "生态环境部；中央精神文明建设办公室；教育部；"
            "共青团中央；全国妇联"
        ),
        asset="公众环境意识与行为规范（行为倡导）",
        asset_status="N/A",
        asset_detail=(
            "本工具界定和覆盖的对象为公民日常生产生活中的生态环境行为规范和意识，"
            "不直接监管实体排放资产。规范通过十个维度的行为指引，倡导节约能源资源、"
            "绿色消费、低碳出行、垃圾分类、减污降碳、生态保护、环保参与和环境监督"
            "等行为，引导公民从身边小事做起践行绿色低碳生活方式。规范为倡导和指导"
            "性质，不设强制性合规义务和处罚。"
        ),
        agent="社会公众",
        agent_detail=(
            "全体公民个人和家庭。规范面向全社会成员，倡导每一位公民在日常生产生活"
            "中自觉遵守生态环境保护行为规范。参与为自愿性质，通过倡导和指导引导"
            "行为改变，不设强制性合规义务和处罚。"
        ),
        activity="消费与使用",
        activity_detail=(
            "本规范引导和规范的受规制活动为公民日常生产生活中的消费与使用行为，"
            "涵盖能源资源消费（节约用电用水、合理使用空调）、商品和服务消费（购买"
            "绿色产品、减少一次性用品）、出行方式选择（低碳出行、优先公共交通）、"
            "废弃物处置（生活垃圾分类投放）以及生态环境参与（义务植树、志愿服务、"
            "环境监督）等。规范通过倡导简约适度、绿色低碳、文明健康的生活方式，"
            "引导公民在消费与使用环节减少温室气体排放和生态环境影响。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）规范围绕关爱生态环境、节约能源资源、践行绿色消费、选择低碳出行、"
            "分类投放垃圾、减少污染产生、呵护自然生态、参加环保实践、参与环境监督、"
            "共建美丽中国十个维度提出行为指引；2）规范为倡导和指导性质，引导公民"
            "自觉遵守，不设强制性合规义务和处罚；3）各相关部门和地方政府结合职责和"
            "地方实际，组织开展规范的宣传推广、教育普及和实践活动；4）鼓励将规范"
            "融入学校教育、社区治理、企业社会责任等场景。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与全国低碳日（CHNCBAPACI04S000）、全国节能宣传周（CHNCBAPACI03S000）、"
            "全国生态日（CHNCBAPACI02S000）等公众宣传教育活动协同推进，公民十条"
            "为各类主题宣传活动提供长期稳定的行为框架和内容基础。与绿色消费、垃圾"
            "分类等专项政策衔接，为相关制度和实践的公众参与提供行为指引。与《中华"
            "人民共和国环境保护法》关于" + LQ + "一切单位和个人都有保护环境的义务"
            "" + RQ + "的规定相呼应。"
        ),
        resp_info_capture=(
            "生态环境部（宣传教育司）会同中央精神文明建设办公室、教育部、共青团"
            "中央、全国妇联负责规范的研究编制、修订更新和宣传推广。"
        ),
        info_transmission=(
            "五部门通过正式公告和门户网站公开发布规范（政府公开发布）；通过新闻"
            "发布会、媒体报道、公益广告、新媒体等多渠道向社会广泛传播；联合各地"
            "相关部门和机构组织开展宣传教育推广活动。"
        ),
        info_frequency=(
            "不定期修订更新。首次发布于2018年（试行），2023年正式修订发布。"
        ),
        info_public="是（公开）。规范通过生态环境部和联合发布部门的门户网站向社会全文公开。",
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "生态环境部联合相关部门组织开展规范的全国宣传推广和教育普及；各地生态"
            "环境部门会同相关部门结合地方实际制定具体实施方案；持续开展" + LQ +
            "美丽中国我是行动者" + RQ + "等主题实践活动；将公民十条内容融入学校教育"
            "体系和公众生态环境教育基地建设；鼓励社会组织、志愿者开展相关宣传和实践"
            "活动。"
        ),
        ghg_abs=(
            "N/A（本工具为公民行为规范类工具，通过倡导绿色低碳生活方式间接促进"
            "减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接行为倡导工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="M72",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；污染防治；资源节约；循环经济；生态保护；公众健康",
        legal_name=(
            "生态环境部 中央精神文明建设办公室 教育部 共青团中央 全国妇联关于发布"
            "《公民生态环境行为规范十条》的公告（公告2023年第17号）"
        ),
        legal_url=(
            "https://www.mee.gov.cn/xxgk2018/xxgk/xxgk01/202306/"
            "t20230605_1032476.html"
        ),
        other_links=(
            "https://www.mee.gov.cn/xxgk2018/xxgk/xxgk01/201806/"
            "t20180605_629588.html"
        ),
    ),
]


def _load_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def _write_rows(path, rows):
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
                print(f"  {pid} already up to date -- skipping")
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
