#!/usr/bin/env python3
"""Insert five new Information instruments (Capacity building and public
   awareness group, Technology promotion catalogue approach):
   - CHNCBATPCI01S000 (Energy-saving & carbon-reduction tech/equipment catalogue, MIIT)
   - CHNCBATPCI02S000 (National key low-carbon technology catalogue, NDRC/MEE)
   - CHNCBATPCI03S000 (Green technology promotion catalogue, NDRC et al.)
   - CHNCBATPCI04S000 (Industrial resource comprehensive utilisation catalogue, MIIT)
   - CHNCBATPCI05S000 (Industrial power demand-side management catalogue, MIIT)
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
        pid="CHNCBATPCI01S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术推广目录",
        sector="工业",
        subsector="N/A",
        name_cn="国家工业和信息化领域节能降碳技术装备推荐目录",
        name_en=(
            "National Catalogue of Recommended Energy-Saving and Carbon-Reduction "
            "Technologies and Equipment for the Industry and Information Technology Sector"
        ),
        policy_package="N/A",
        description=(
            "国家工业和信息化领域节能降碳技术装备推荐目录是工业和信息化部发布的"
            "技术推广类信息工具，通过遴选和向社会公开推荐先进适用的节能降碳技术"
            "和装备，传播先进技术信息、引导工业企业采用高能效低碳技术装备。目录"
            "面向钢铁、有色、建材、石化化工、机械、电子等重点工业行业，涵盖流程"
            "工业节能、重点用能设备（工业锅炉、电机、变压器等）能效提升、余热余压"
            "利用、数据中心节能等技术装备。工业和信息化部通过公开征集、专家评审、"
            "公示等程序确定入选技术装备清单并印发目录。目录建设可追溯至2017年"
            "《国家工业节能技术装备推荐目录》（工业和信息化部公告2017年第50号，"
            "此前为节能机电设备（产品）推荐目录），2022年更名为《国家工业节能"
            "技术装备推荐目录》（公告2022年第29号），2024年首次以《国家工业和"
            "信息化领域节能降碳技术装备推荐目录（2024年版）》（工业和信息化部"
            "公告2024年第8号）发布，将推广范围由节能扩展至节能降碳；现行版本为"
            "《国家工业和信息化领域节能降碳技术装备推荐目录（2025年版）》（工业"
            "和信息化部公告2025年第37号），为落实《制造业绿色低碳发展行动方案"
            "（2025—2027年）》（国办发〔2025〕21号）修订发布。入选目录的技术"
            "装备可作为工业企业节能降碳改造、政策支持和推广应用的重要参考。"
        ),
        objective=(
            "推广先进适用的工业节能降碳技术和装备；引导工业企业采用高能效低碳"
            "技术改造；促进工业领域能效提升和碳排放强度下降；支撑工业绿色低碳"
            "转型"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="10/11/2017",
        effective="10/11/2017",
        revision="08/12/2025",
        revision_detail=(
            "目录建设可追溯至2017年11月10日《国家工业节能技术装备推荐目录》"
            "（工业和信息化部公告2017年第50号，其前身为节能机电设备（产品）"
            "推荐目录）。此后按年度或隔年更新（2017、2018、2020、2022年版）。"
            "2022年发布《国家工业节能技术装备推荐目录》（公告2022年第29号）。"
            "2024年5月16日首次以《国家工业和信息化领域节能降碳技术装备推荐目录"
            "（2024年版）》（工业和信息化部公告2024年第8号）印发，将推广范围由"
            "工业节能扩展至工业和信息化领域节能降碳。2025年12月8日修订发布"
            "《国家工业和信息化领域节能降碳技术装备推荐目录（2025年版）》（工业"
            "和信息化部公告2025年第37号，成文日期2025年12月8日，发布日期2025年"
            "12月15日），为落实《制造业绿色低碳发展行动方案（2025—2027年）》"
            "（国办发〔2025〕21号）加快推广节能降碳先进技术、加强重点行业领域"
            "技术改造升级和大规模设备更新而修订，并调整完善技术装备遴选范围和标准。"
        ),
        status="生效",
        admin_authorities="工业和信息化部（节能与综合利用司）",
        asset="节能降碳技术与装备（研发与推广成果）",
        asset_status="N/A",
        asset_detail=(
            "本工具为技术推广目录，推广对象为工业和信息化领域先进适用的节能降碳"
            "技术和装备（涵盖流程工业节能、重点用能设备能效提升、余热余压利用、"
            "数据中心节能等），不直接监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "技术装备的研发生产企业（申报入选目录的技术装备供给方）以及采用推荐"
            "技术装备的工业企业（技术需求方）。企业自愿申报技术装备参与目录遴选，"
            "申报单位对所提交材料的真实性负责；工业企业可自主参考目录选用节能降碳"
            "技术装备，入选与选用均不设强制性义务。"
        ),
        activity="研究与开发",
        activity_detail=(
            "工业和信息化部组织的节能降碳技术装备遴选和推广活动。技术装备研发"
            "生产企业自愿申报→工业和信息化部组织专家评审、公示→印发推荐目录并"
            "向社会公开→引导工业企业选用和推广应用入选技术装备。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）技术装备研发生产企业按照目录申报通知要求，自愿提交技术装备的"
            "节能降碳指标、技术成熟度、应用案例等申报材料；2）工业和信息化部按"
            "先进性、适用性、节能降碳效果等标准组织专家评审和公示；3）通过评审"
            "的技术装备纳入推荐目录并向社会公开发布；4）目录定期或分版更新；"
            "5）入选目录不设强制性合规义务，工业企业可自主参考选用，入选技术"
            "装备可作为相关支持政策和推广应用的重要参考。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与工业节能监察、节能诊断等工业节能管理制度联动：推荐目录为企业节能"
            "改造提供技术选择。与节能降碳改造相关财政、金融支持政策衔接：入选"
            "技术装备可作为支持对象参考。与重点用能设备能效标准（MEPS）联动："
            "共同推动高能效设备推广应用。"
        ),
        resp_info_capture=(
            "技术装备研发生产企业自愿申报并提供技术装备信息；工业和信息化部"
            "（节能与综合利用司）负责组织评审、汇总和目录发布。"
        ),
        info_transmission=(
            "工业和信息化部通过公告和门户网站公开发布推荐目录（政府公开发布）；"
            "企业通过目录申报渠道提交申报材料。"
        ),
        info_frequency=(
            "不定期/约每一至两年更新一版（2017、2018、2020、2022、2024、2025年版）。"
        ),
        info_public=(
            "是（公开）。推荐目录通过工业和信息化部公告和门户网站向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "工业和信息化部发布推荐目录及技术装备说明；组织节能降碳技术装备"
            "推广对接、案例宣传和经验交流；引导地方和行业开展入选技术装备的"
            "推广应用。"
        ),
        ghg_abs=(
            "N/A（本工具为技术推广目录，通过引导先进节能降碳技术装备推广应用"
            "间接支持减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术推广工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="C25; C27; C28",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="能效提升；能源消耗减少；技术创新；绿色产业发展",
        legal_name=(
            "工业和信息化部公告2025年第37号《国家工业和信息化领域节能降碳技术"
            "装备推荐目录（2025年版）》"
        ),
        legal_url=(
            "https://www.miit.gov.cn/jgsj/jns/gzdt/art/2025/"
            "art_6047ab0f0b1846cf8918ed2e3d01395c.html"
        ),
        other_links=(
            "https://www.miit.gov.cn/jgsj/jns/gzdt/art/2024/"
            "art_60736b016395460890aeda756751526d.html；"
            "https://www.miit.gov.cn/jgsj/jns/gzdt/art/2022/"
            "art_9d1d61dbfd264efd970e76ea81074d4c.html"
        ),
    ),
    make_row(
        pid="CHNCBATPCI02S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术推广目录",
        sector="能源；工业；建筑；交通；农业、林业和其他土地利用",
        subsector="N/A",
        name_cn="国家重点推广的低碳技术目录",
        name_en="National Catalogue of Key Low-Carbon Technologies for Promotion",
        policy_package="N/A",
        description=(
            "国家重点推广的低碳技术目录是由国家发展改革委（后为生态环境部）发布的"
            "技术推广类信息工具，通过遴选和公开发布重点推广的低碳技术，传播成熟"
            "适用的低碳技术信息、引导各行业加快低碳技术应用推广。目录采取分批"
            "发布方式，覆盖能源、工业（钢铁、化工、建材等）、建筑、交通、农业等"
            "重点领域的减碳、零碳和负碳技术，并包含储碳固碳、数智赋能、非二氧化碳"
            "减排等方向，对每项技术的适用范围、技术原理、减排效果和应用前景等"
            "作出说明。第一批由国家发展改革委2014年第13号公告发布（33项技术），"
            "第二批2015年第31号公告发布，第三批2017年发布；随着应对气候变化职能"
            "由国家发展改革委划转生态环境部，第四批由生态环境部以《国家重点推广的"
            "低碳技术目录（第四批）》（环办气候函〔2022〕484号，2022年12月19日）"
            "发布（35项技术）；第五批（最新）由生态环境部、工业和信息化部、住房"
            "城乡建设部、交通运输部、农业农村部五部门联合以《国家重点推广的低碳"
            "技术目录（第五批）》（环办气候函〔2025〕44号，2025年1月20日印发、"
            "2月12日公布）发布，共103项技术，涵盖能源绿色低碳转型、工业、建筑、"
            "交通、农业领域降碳及储碳固碳、数智赋能、非二氧化碳减排等类别。目录"
            "旨在为地方、行业和企业选用低碳技术提供权威参考，推动重点领域低碳"
            "技术产业化和规模化应用。"
        ),
        objective=(
            "推广成熟适用的低碳技术；引导重点领域加快低碳技术应用；促进低碳技术"
            "产业化和规模化推广；支撑国家碳达峰碳中和目标实现"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="25/08/2014",
        effective="25/08/2014",
        revision="20/01/2025",
        revision_detail=(
            "目录采取分批发布。第一批由国家发展改革委2014年8月25日第13号公告"
            "发布（33项技术）；第二批2015年12月18日第31号公告发布；第三批2017年"
            "发布。随着应对气候变化职能由国家发展改革委划转生态环境部，第四批"
            "由生态环境部以《国家重点推广的低碳技术目录（第四批）》（环办气候函"
            "〔2022〕484号）于2022年12月19日发布，共35项技术。第五批（最新）由"
            "生态环境部、工业和信息化部、住房城乡建设部、交通运输部、农业农村部"
            "五部门联合以《国家重点推广的低碳技术目录（第五批）》（环办气候函"
            "〔2025〕44号）于2025年1月20日印发、2月12日公布，共103项技术，涵盖"
            "能源绿色低碳转型（20项）、工业（28项）、建筑（11项）、交通（15项）、"
            "农业（5项）领域降碳，以及储碳固碳（3项）、数智赋能（14项）、"
            "非二氧化碳减排（7项）等类别。"
        ),
        status="生效",
        admin_authorities=(
            "生态环境部、工业和信息化部、住房城乡建设部、交通运输部、农业农村部"
            "（第五批）；生态环境部（第四批）；国家发展改革委（第一至三批）"
        ),
        asset="低碳技术（研发与推广成果）",
        asset_status="N/A",
        asset_detail=(
            "本工具为技术推广目录，推广对象为能源、工业、建筑、交通、农业等重点"
            "领域先进适用的低碳（减碳、零碳、负碳）技术，以及储碳固碳、数智赋能、"
            "非二氧化碳减排等方向的技术，不直接监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "低碳技术的研发和应用单位（企业、科研机构等）。技术研发或应用单位"
            "可自愿申报低碳技术参与目录遴选，申报单位对所提交材料的真实性负责；"
            "地方、行业和企业可自主参考目录选用推广低碳技术，入选与选用均不设"
            "强制性义务。"
        ),
        activity="研究与开发",
        activity_detail=(
            "国家发展改革委/生态环境部组织的低碳技术遴选和推广活动。技术研发或"
            "应用单位自愿申报→主管部门组织专家评审、筛选→分批印发目录并向社会"
            "公开→引导地方、行业和企业选用推广入选低碳技术。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）低碳技术研发或应用单位按目录征集要求，自愿提交技术的减排效果、"
            "技术成熟度、适用范围、推广应用情况等材料；2）主管部门按先进性、"
            "适用性、减排效果和推广潜力等标准组织专家评审筛选；3）入选技术分批"
            "纳入目录并向社会公开发布；4）目录不设强制性合规义务，地方、行业和"
            "企业可自主参考选用，入选技术可作为相关支持政策和推广应用的参考。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与碳达峰碳中和政策体系联动：低碳技术目录为重点领域低碳转型提供技术"
            "支撑。与低碳技术示范推广、气候投融资等政策衔接：入选技术可作为支持"
            "和推广对象参考。与绿色技术推广目录等其他技术推广工具形成协同。"
        ),
        resp_info_capture=(
            "技术研发或应用单位自愿申报并提供低碳技术信息；生态环境部等五部门"
            "（第五批）/生态环境部（第四批）/国家发展改革委（第一至三批）负责"
            "组织评审、筛选和目录发布。"
        ),
        info_transmission=(
            "国家发展改革委/生态环境部通过公告、通知和门户网站公开发布目录"
            "（政府公开发布）；单位通过征集渠道提交申报材料。"
        ),
        info_frequency=(
            "不定期分批发布（第一至五批分别于2014、2015、2017、2022、2025年发布）。"
        ),
        info_public=(
            "是（公开）。目录通过主管部门公告/通知和门户网站向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "主管部门发布低碳技术目录及技术说明；组织低碳技术推广对接、宣传"
            "和经验交流；引导地方和行业开展入选低碳技术的示范和推广应用。"
        ),
        ghg_abs=(
            "N/A（本工具为技术推广目录，通过引导低碳技术推广应用间接支持减排，"
            "无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术推广工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="M72",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="技术创新；能效提升；绿色产业发展；污染防治",
        legal_name=(
            "关于印发《国家重点推广的低碳技术目录（第五批）》的通知"
            "（环办气候函〔2025〕44号）"
        ),
        legal_url=(
            "https://www.mee.gov.cn/xxgk2018/xxgk/xxgk06/202502/"
            "t20250212_1102102.html"
        ),
        other_links=(
            "https://www.mee.gov.cn/xxgk2018/xxgk/xxgk06/202212/"
            "t20221221_1008424.html；"
            "https://www.ndrc.gov.cn/xxgk/zcfb/gg/201409/t20140905_961102.html；"
            "https://www.ndrc.gov.cn/xxgk/zcfb/gg/201512/t20151218_961138.html"
        ),
    ),
    make_row(
        pid="CHNCBATPCI03S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术推广目录",
        sector="跨部门",
        subsector="N/A",
        name_cn="绿色技术推广目录",
        name_en="Green Technology Promotion Catalogue",
        policy_package="N/A",
        description=(
            "绿色技术推广目录是由国家发展改革委等部门联合发布的技术推广类信息"
            "工具，通过遴选和公开发布先进适用的绿色技术，传播绿色技术信息、引导"
            "绿色技术推广应用。目录涵盖节能降碳、环境保护、资源循环利用、绿色"
            "能源转型、生态保护修复、绿色基础设施、绿色服务等领域的先进适用绿色"
            "技术，对每项技术的适用范围、主要技术指标和应用情况等作出说明。目录"
            "由2020年版首次发布（《绿色技术推广目录（2020年）》，发改办环资"
            "〔2020〕990号，共116项技术，由国家发展改革委、科技部、工业和信息化部、"
            "自然资源部联合印发）；2024年版（《绿色技术推广目录（2024年版）》，"
            "发改环资〔2024〕1812号，共112项技术）由国家发展改革委、科技部、工业和"
            "信息化部、自然资源部、生态环境部、住房城乡建设部、国务院国资委、"
            "国家能源局等部门联合印发。目录旨在为企业、地方和相关方选用绿色技术"
            "提供权威参考，推动绿色技术创新成果转化和推广应用。"
        ),
        objective=(
            "推广先进适用的绿色技术；引导企业和地方加快绿色技术应用；促进绿色"
            "技术创新成果转化和产业化；支撑经济社会绿色低碳发展"
        ),
        mitigation="间接",
        channel="供给侧",
        adoption="31/12/2020",
        effective="31/12/2020",
        revision="24/12/2024",
        revision_detail=(
            "目录2020年版首次发布：《绿色技术推广目录（2020年）》（发改办环资"
            "〔2020〕990号，2020年12月31日，共116项技术），由国家发展改革委、"
            "科技部、工业和信息化部、自然资源部联合印发。2024年版《绿色技术推广"
            "目录（2024年版）》（发改环资〔2024〕1812号，2024年12月24日印发，"
            "2025年1月20日公布，共112项技术）由国家发展改革委等8部门联合印发，"
            "扩充联合发文部门、更新技术条目并完善技术领域分类。"
        ),
        status="生效",
        admin_authorities=(
            "国家发展改革委；科技部；工业和信息化部；自然资源部；生态环境部；"
            "住房城乡建设部；国务院国资委；国家能源局"
        ),
        asset="绿色技术（研发与推广成果）",
        asset_status="N/A",
        asset_detail=(
            "本工具为技术推广目录，推广对象为节能降碳、环境保护、资源循环利用、"
            "绿色能源、生态保护修复、绿色基础设施和绿色服务等领域先进适用的绿色"
            "技术，不直接监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "绿色技术的研发和应用单位（企业、科研机构等）。技术研发或应用单位"
            "可自愿申报绿色技术参与目录遴选，申报单位对所提交材料的真实性负责；"
            "企业和地方可自主参考目录选用推广绿色技术，入选与选用均不设强制性"
            "义务。"
        ),
        activity="研究与开发",
        activity_detail=(
            "国家发展改革委等部门组织的绿色技术遴选和推广活动。技术研发或应用"
            "单位自愿申报→主管部门组织专家评审、筛选、公示→印发目录并向社会"
            "公开→引导企业和地方选用推广入选绿色技术。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）绿色技术研发或应用单位按目录征集要求，自愿提交技术的主要技术"
            "指标、适用范围、绿色环境效益和推广应用情况等材料；2）主管部门按"
            "先进性、适用性、绿色效益和推广潜力等标准组织专家评审、筛选和公示；"
            "3）入选技术纳入目录并向社会公开发布；4）目录定期修订更新；5）目录"
            "不设强制性合规义务，企业和地方可自主参考选用，入选技术可作为相关"
            "支持政策和推广应用的参考。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与绿色技术创新体系建设联动：目录是绿色技术推广应用的重要抓手。与"
            "绿色金融、政府绿色采购等政策衔接：入选绿色技术可作为支持和采购参考。"
            "与国家重点推广的低碳技术目录等其他技术推广工具形成协同。"
        ),
        resp_info_capture=(
            "绿色技术研发或应用单位自愿申报并提供绿色技术信息；国家发展改革委"
            "等部门负责组织评审、筛选和目录发布。"
        ),
        info_transmission=(
            "国家发展改革委等部门通过通知和门户网站公开发布目录（政府公开发布）；"
            "单位通过征集渠道提交申报材料。"
        ),
        info_frequency=(
            "不定期更新（2020年版、2024年版）。"
        ),
        info_public=(
            "是（公开）。目录通过主管部门通知和门户网站向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "主管部门发布绿色技术推广目录及技术说明；组织绿色技术推广对接、"
            "宣传和经验交流；引导企业和地方开展入选绿色技术的推广应用。"
        ),
        ghg_abs=(
            "N/A（本工具为技术推广目录，通过引导绿色技术推广应用间接支持减排，"
            "无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术推广工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="M72",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="技术创新；绿色产业发展；污染防治；资源节约；生态保护",
        legal_name=(
            "关于印发《绿色技术推广目录（2024年版）》的通知"
            "（发改环资〔2024〕1812号）"
        ),
        legal_url=(
            "https://www.ndrc.gov.cn/xxgk/zcfb/tz/202501/t20250120_1395788.html"
        ),
        other_links=(
            "https://www.ndrc.gov.cn/xxgk/zcfb/tz/202101/t20210108_1264625.html"
        ),
    ),
    make_row(
        pid="CHNCBATPCI04S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术推广目录",
        sector="工业；废弃物",
        subsector="N/A",
        name_cn="国家工业资源综合利用先进适用工艺技术设备目录",
        name_en=(
            "National Catalogue of Advanced and Applicable Processes, Technologies "
            "and Equipment for the Comprehensive Utilisation of Industrial Resources"
        ),
        policy_package="N/A",
        description=(
            "国家工业资源综合利用先进适用工艺技术设备目录是工业和信息化部（近年"
            "会同国家发展改革委、生态环境部）发布的技术推广类信息工具，通过遴选"
            "和公开推荐先进适用的工业资源综合利用工艺、技术和设备，传播先进技术"
            "信息、引导工业固体废物和再生资源综合利用。目录覆盖大宗工业固体废物"
            "（尾矿、粉煤灰、煤矸石、冶炼渣、工业副产石膏等）综合利用、再生资源"
            "（废钢铁、废有色金属、废塑料、废旧动力电池等）回收利用、以及资源"
            "综合利用公共服务等领域的工艺技术设备。工业和信息化部通过公开征集、"
            "专家评审、公示等程序确定入选清单并印发目录。目录建设可追溯至2017年"
            "《国家工业资源综合利用先进适用技术装备目录》（工业和信息化部公告"
            "2017年第40号），此后按年度或隔年更新（2019、2021、2023年版）；"
            "2025年版《国家工业资源综合利用先进适用工艺技术设备目录（2025年版）》"
            "（工业和信息化部等公告2025年第21号）由工业和信息化部会同国家发展"
            "改革委、生态环境部发布。目录旨在为工业企业选用资源综合利用技术设备"
            "提供参考，推动工业固废和再生资源规模化高值化利用。"
        ),
        objective=(
            "推广先进适用的工业资源综合利用工艺技术设备；引导工业固体废物和再生"
            "资源综合利用；促进资源循环利用产业发展；支撑工业绿色低碳循环发展"
        ),
        mitigation="间接",
        channel="供给侧",
        adoption="13/10/2017",
        effective="13/10/2017",
        revision="10/09/2025",
        revision_detail=(
            "目录建设可追溯至2017年10月13日《国家工业资源综合利用先进适用技术"
            "装备目录》（工业和信息化部公告2017年第40号）。此后按年度或隔年更新"
            "（2019、2021、2023年版，如公告2023年第15号）。2025年版《国家工业"
            "资源综合利用先进适用工艺技术设备目录（2025年版）》（工业和信息化部、"
            "国家发展改革委、生态环境部公告2025年第21号，2025年9月10日）发布，"
            "分4个领域、共96项，扩充联合发文部门并更新工艺技术设备条目。"
        ),
        status="生效",
        admin_authorities=(
            "工业和信息化部（节能与综合利用司）；国家发展改革委；生态环境部"
        ),
        asset="工业资源综合利用工艺技术设备（研发与推广成果）",
        asset_status="N/A",
        asset_detail=(
            "本工具为技术推广目录，推广对象为工业固体废物综合利用、再生资源回收"
            "利用等领域先进适用的工艺、技术和设备，不直接监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "工艺技术设备的研发生产企业（申报入选目录的供给方）以及采用推荐工艺"
            "技术设备的工业资源综合利用企业（需求方）。企业自愿申报工艺技术设备"
            "参与目录遴选，申报单位对所提交材料的真实性负责；工业企业可自主参考"
            "目录选用，入选与选用均不设强制性义务。"
        ),
        activity="研究与开发",
        activity_detail=(
            "工业和信息化部等组织的工业资源综合利用工艺技术设备遴选和推广活动。"
            "研发生产企业自愿申报→主管部门组织专家评审、公示→印发目录并向社会"
            "公开→引导工业企业选用推广入选工艺技术设备。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）工艺技术设备研发生产企业按目录申报要求，自愿提交工艺技术设备的"
            "资源利用指标、技术成熟度、应用案例等材料；2）主管部门按先进性、"
            "适用性、资源环境效益等标准组织专家评审和公示；3）入选工艺技术设备"
            "纳入目录并向社会公开发布；4）目录定期或分版更新；5）目录不设强制性"
            "合规义务，工业企业可自主参考选用，入选技术设备可作为相关支持政策"
            "和推广应用的参考。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与工业资源综合利用相关税收优惠（资源综合利用增值税、企业所得税优惠）"
            "政策衔接：入选技术设备可为资源综合利用认定提供技术参考。与循环经济"
            "和工业固废综合利用政策联动：目录推动固废和再生资源规模化利用。"
        ),
        resp_info_capture=(
            "工艺技术设备研发生产企业自愿申报并提供技术设备信息；工业和信息化部"
            "（节能与综合利用司）等负责组织评审、汇总和目录发布。"
        ),
        info_transmission=(
            "工业和信息化部等通过公告和门户网站公开发布目录（政府公开发布）；"
            "企业通过目录申报渠道提交申报材料。"
        ),
        info_frequency=(
            "不定期/约每一至两年更新一版（2017、2019、2021、2023、2025年版）。"
        ),
        info_public=(
            "是（公开）。目录通过工业和信息化部等公告和门户网站向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "工业和信息化部等发布目录及工艺技术设备说明；组织工业资源综合利用"
            "技术推广对接、案例宣传和经验交流；引导地方和企业开展入选技术设备的"
            "推广应用。"
        ),
        ghg_abs=(
            "N/A（本工具为技术推广目录，通过引导工业资源综合利用技术推广应用"
            "间接支持减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术推广工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="E38",
        ghg="CO2; CH4",
        mitigation_effects="正向",
        co_benefits="资源节约；循环经济；污染防治；绿色产业发展",
        legal_name=(
            "工业和信息化部等公告2025年第21号《国家工业资源综合利用先进适用"
            "工艺技术设备目录（2025年版）》"
        ),
        legal_url=(
            "https://www.miit.gov.cn/zwgk/zcwj/wjfb/gg/art/2025/"
            "art_dd99789c9aba4900942418f37c505387.html"
        ),
        other_links=(
            "https://www.miit.gov.cn/jgsj/jns/zhlyh/art/2023/"
            "art_169733afb2f647e8adf670927bae6c07.html"
        ),
    ),
    make_row(
        pid="CHNCBATPCI05S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术推广目录",
        sector="工业；能源",
        subsector="N/A",
        name_cn="工业领域电力需求侧管理产品（技术）参考目录",
        name_en=(
            "Reference Catalogue of Industrial Power Demand-Side Management "
            "Products (Technologies)"
        ),
        policy_package="N/A",
        description=(
            "工业领域电力需求侧管理产品（技术）参考目录是工业和信息化部办公厅"
            "（运行监测协调局）发布的技术推广类信息工具，通过遴选和公开发布先进"
            "适用的电力需求侧管理产品和技术，传播先进技术信息、引导工业领域"
            "开展电力需求侧管理、提高电能利用效率和电力系统灵活性。目录覆盖有序"
            "用电与负荷管理、电能替代与电气化、储能、电力需求响应、电能质量治理、"
            "智慧能源与虚拟电厂等方向的产品和技术。目录采取分批发布方式，工业和"
            "信息化部办公厅通过公开征集、评审、公示等程序确定入选产品（技术）"
            "清单并印发目录。目录第一批由《工业和信息化部办公厅关于印发工业领域"
            "电力需求侧管理参考产品（技术）目录（第一批）的通知》（工信厅运行函"
            "〔2017〕409号，2017年7月7日）发布，此后按批次陆续发布；最新为第六批"
            "（工信厅运行函〔2024〕204号，2024年6月3日，共24项）。目录旨在为工业"
            "企业和电力用户选用电力需求侧管理产品技术提供参考，推动工业电力系统"
            "高效灵活运行和绿色低碳转型。"
        ),
        objective=(
            "推广先进适用的电力需求侧管理产品和技术；引导工业领域开展电力需求侧"
            "管理；提高电能利用效率和电力系统灵活性；支撑新型电力系统建设和工业"
            "绿色低碳转型"
        ),
        mitigation="间接",
        channel="供给侧",
        adoption="07/07/2017",
        effective="07/07/2017",
        revision="03/06/2024",
        revision_detail=(
            "目录采取分批发布。第一批由《工业和信息化部办公厅关于印发工业领域"
            "电力需求侧管理参考产品（技术）目录（第一批）的通知》（工信厅运行函"
            "〔2017〕409号）于2017年7月7日发布。此后按批次陆续发布，第一至五批"
            "于2024年2月整合（工信厅运行函〔2024〕37号）。最新为第六批（工信厅"
            "运行函〔2024〕204号，2024年6月3日印发、6月5日公布，共24项）。"
        ),
        status="生效",
        admin_authorities="工业和信息化部办公厅（运行监测协调局）",
        asset="电力需求侧管理产品与技术（研发与推广成果）",
        asset_status="N/A",
        asset_detail=(
            "本工具为技术推广目录，推广对象为负荷管理、电能替代、储能、需求响应、"
            "电能质量治理、智慧能源等电力需求侧管理产品和技术，不直接监管实体"
            "排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "电力需求侧管理产品（技术）的研发生产企业（申报入选目录的供给方）"
            "以及采用推荐产品技术的工业企业和电力用户（需求方）。企业自愿申报"
            "产品（技术）参与目录遴选，申报单位对所提交材料的真实性负责；工业"
            "企业可自主参考目录选用，入选与选用均不设强制性义务。"
        ),
        activity="研究与开发",
        activity_detail=(
            "工业和信息化部办公厅组织的电力需求侧管理产品（技术）遴选和推广活动。"
            "研发生产企业自愿申报→主管部门组织评审、公示→分批印发目录并向社会"
            "公开→引导工业企业和电力用户选用推广入选产品技术。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）产品（技术）研发生产企业按目录申报要求，自愿提交产品技术的功能"
            "指标、节电节能效果、技术成熟度、应用案例等材料；2）主管部门按先进性、"
            "适用性、节电和调节效果等标准组织评审和公示；3）入选产品（技术）"
            "纳入目录并向社会公开发布；4）目录按批次发布更新；5）目录不设强制性"
            "合规义务，工业企业和电力用户可自主参考选用，入选产品技术可作为相关"
            "支持政策和推广应用的参考。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与电力需求侧管理办法和新型电力系统建设政策联动：目录为工业电力需求"
            "侧管理提供产品技术支撑。与电能替代、工业节能等政策衔接：入选产品"
            "技术可作为推广和支持参考。与需求响应、虚拟电厂等市场机制形成协同。"
        ),
        resp_info_capture=(
            "产品（技术）研发生产企业自愿申报并提供产品技术信息；工业和信息化部"
            "办公厅（运行监测协调局）负责组织评审、汇总和目录发布。"
        ),
        info_transmission=(
            "工业和信息化部办公厅通过通知和门户网站公开发布目录（政府公开发布）；"
            "企业通过目录申报渠道提交申报材料。"
        ),
        info_frequency=(
            "按批次发布，约每年组织一次征集（第一批2017年，最新第六批2024年）。"
        ),
        info_public=(
            "是（公开）。目录通过工业和信息化部办公厅通知和门户网站向社会全文"
            "公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "工业和信息化部办公厅发布目录及产品技术说明；组织电力需求侧管理"
            "技术推广对接、案例宣传和经验交流；引导地方和企业开展入选产品技术的"
            "推广应用。"
        ),
        ghg_abs=(
            "N/A（本工具为技术推广目录，通过引导电力需求侧管理产品技术推广应用"
            "间接支持减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术推广工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="D35",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="能效提升；能源消耗减少；技术创新；能源安全",
        legal_name=(
            "工业和信息化部办公厅关于印发《工业领域电力需求侧管理产品（技术）"
            "参考目录（第六批）》的通知（工信厅运行函〔2024〕204号）"
        ),
        legal_url=(
            "https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2024/"
            "art_23836d619c814d8587ecfda9cfc6b68e.html"
        ),
        other_links=(
            "https://www.miit.gov.cn/jgsj/yxj/wjfb/art/2020/"
            "art_09a11724de154215ae9d5ef81a79ff48.html"
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

        # New group (CBA): keep CBA rows contiguous. Insert after the last CBA
        # row if any exist, else append at the end of the file (after REP block).
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][2] == "能力建设与公众意识":
                insert_pos = i + 1

        data.insert(insert_pos, list(row))
        inserted += 1
        print(f"  Inserted {pid} at data index {insert_pos}")

    # Drop any stray empty trailing rows before rewriting
    data = [r for r in data if any(r)]

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted, {updated} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
