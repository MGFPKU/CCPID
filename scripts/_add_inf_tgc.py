#!/usr/bin/env python3
"""Insert the Technical guidance Information instruments
   (Capacity building and public awareness group):
   - CHNCBATGCI01S000 (Digital Energy-Carbon Management Center Construction Guide)
   - CHNCBATGCI02S000 (Energy-Saving and Carbon-Reduction Upgrade Guide)
   - CHNCBATGCI03S000 (Industrial Green Microgrid Construction and Application Guide)
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
        pid="CHNCBATGCI01S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术指南",
        sector="工业",
        subsector="N/A",
        name_cn="工业企业和园区数字化能碳管理中心建设指南",
        name_en=(
            "Digital Energy-Carbon Management Center Construction Guide "
            "for Industrial Enterprises and Parks"
        ),
        policy_package="N/A",
        description=(
            "工业企业和园区数字化能碳管理中心建设指南由工业和信息化部印发，是面向"
            "工业企业和园区提供数字化能碳管理能力建设方法的信息类工具，旨在通过"
            "推广工业互联网、人工智能、物联网等数字技术在能碳管理领域的应用，引导"
            "企业和园区建设集成碳排放监测、能源消耗分析、节能优化调度等功能的"
            "数字化管理系统。指南明确了能碳管理中心的功能定位、技术体系架构（"
            "基础设施层、数据采集层、数据管理层、模型算法层、应用服务层、展示交互层"
            "六层架构），涵盖能耗在线监测、碳排放核算与溯源、能效对标分析、"
            "节能诊断与优化、碳资产管理、绿色用能分析等12项核心业务功能，并对"
            "两类实施主体（工业企业、工业园区）分别提出差异化建设要求。指南旨在"
            "支撑能耗双控向碳排放双控转变，推动工业领域碳达峰碳中和目标实现。"
        ),
        objective=(
            "引导工业企业和园区构建数字化能碳管理能力；推动数字技术在能碳管理"
            "领域深度应用；支撑能耗双控向碳排放双控全面转型；服务工业领域碳达峰"
            "碳中和目标"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="07/03/2025",
        effective="07/03/2025",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities="工业和信息化部（节能与综合利用司）",
        asset="数字化能碳管理中心（企业级和园区级）",
        asset_status="N/A",
        asset_detail=(
            "本工具界定和覆盖的对象为工业企业和园区建设的数字化能碳管理中心系统，"
            "包括碳排放监测、能源消耗分析、节能优化调度、碳资产管理等数字化功能模块。"
            "系统通过采集生产设施和能源系统的运行数据，运用工业互联网、人工智能、"
            "物联网等技术实现能碳数据的实时监测、智能分析和优化决策。"
        ),
        agent="企业",
        agent_detail=(
            "工业企业（特别是重点用能单位和碳排放单位）和工业园区运营管理机构。"
            "企业和园区可参照指南自愿建设或升级数字化能碳管理中心，指南为推荐性"
            "和指导性质，不设强制性合规义务。"
        ),
        activity="生产",
        activity_detail=(
            "本指南引导和规范的受规制活动为工业企业生产经营过程中的能源消耗和温室"
            "气体排放的数字化监测、核算与管理活动。指南通过提供技术架构和功能规范，"
            "帮助企业和园区建立系统化的能碳数据采集、统计、分析、预警和优化能力，"
            "提高能碳管理精细化水平，支撑企业节能降碳决策和碳双控目标实现。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）数字化能碳管理中心建设应覆盖企业或园区主要能源消耗和碳排放环节；"
            "2）系统架构按六层架构设计，实现12项核心业务功能，满足能碳数据在线采集、"
            "实时监测、智能分析和优化决策需求；3）企业和园区可根据自身规模和需求选择"
            "适宜的建设和应用模式，指南为推荐性指导，不设强制性合规义务；4）做好与"
            "国家重点用能单位能耗在线监测系统、碳排放权交易市场信息平台等的衔接。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与碳排放权交易市场数据报送系统衔接：能碳管理中心可为碳排放报告和核查"
            "提供数据支撑。与重点用能单位能耗在线监测系统衔接：系统数据可作为能耗"
            "监测的组成部分。与工业节能诊断服务衔接：能碳管理中心可提供在线诊断"
            "数据支撑。"
        ),
        resp_info_capture=(
            "工业和信息化部（节能与综合利用司）负责指南的研究编制、发布和宣贯推广。"
        ),
        info_transmission=(
            "工业和信息化部通过通知和门户网站公开发布指南（政府公开发布）。"
        ),
        info_frequency=(
            "一次性发布（2025年版）。后续视需要修订更新。"
        ),
        info_public=(
            "是（公开）。指南通过工业和信息化部门户网站向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "工业和信息化部组织指南的宣传解读和培训推广；指导地方工业和信息化主管"
            "部门结合本地实际组织开展指南应用和能力建设活动；鼓励行业协会和技术服务"
            "机构提供技术支持和解决方案。"
        ),
        ghg_abs=(
            "N/A（本工具为技术指导性工具，通过引导企业和园区建设数字化能碳管理能力"
            "间接促进减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术指导工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="C",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="能效提升；技术创新；污染防治；绿色产业发展",
        legal_name=(
            "工业和信息化部办公厅关于印发《工业企业和园区数字化能碳管理中心建设"
            "指南》的通知（工信厅节〔2025〕13号）"
        ),
        legal_url=(
            "https://www.miit.gov.cn/jgsj/jns/nyjy/art/2025/"
            "art_bd4ed4ce13314ce58ee3896579b27ba0.html"
        ),
        other_links="N/A",
    ),
    make_row(
        pid="CHNCBATGCI02S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术指南",
        sector="工业",
        subsector=(
            "炼油；乙烯；对二甲苯；现代煤化工；合成氨；电石；烧碱；纯碱；"
            "磷铵；黄磷；水泥；平板玻璃；建筑卫生陶瓷；钢铁；焦化；铁合金；"
            "有色金属冶炼"
        ),
        name_cn="高耗能行业重点领域节能降碳改造升级实施指南（2022年版）",
        name_en=(
            "Implementation Guide for Energy-Saving and Carbon-Reduction "
            "Retrofit and Upgrade in Key Areas of Energy-Intensive Industries "
            "(2022 Edition)"
        ),
        policy_package="N/A",
        description=(
            "高耗能行业重点领域节能降碳改造升级实施指南（2022年版）由国家发展"
            "改革委、工业和信息化部、生态环境部、国家能源局等四部门联合发布，"
            "是针对高耗能行业重点领域提供节能降碳技术路径和改造方向的信息类工具，"
            "旨在引导高耗能企业对标能效基准水平和标杆水平，推进节能降碳改造升级"
            "和落后产能退出。指南覆盖炼油、乙烯、对二甲苯、现代煤化工、合成氨、"
            "电石、烧碱、纯碱、磷铵、黄磷、水泥、平板玻璃、建筑卫生陶瓷、钢铁、"
            "焦化、铁合金、有色金属冶炼等17个重点用能行业领域，对各行业分别提出"
            "四个方向：（1）引导改造升级——对能效在基准水平以下的企业提出明确"
            "的改造升级技术路径和预期效果；（2）加强技术攻关——梳理行业前沿"
            "节能降碳技术并推动研发示范；（3）促进集聚发展——推动行业向规模化、"
            "集约化方向发展；（4）加快淘汰落后——对不能按期改造达标的落后产能"
            "依法依规淘汰退出。"
        ),
        objective=(
            "引导高耗能行业企业对标能效基准水平和标杆水平；提供节能降碳改造升级"
            "技术路径；推动高耗能行业绿色低碳转型和高质量发展；支撑工业领域碳达峰"
            "碳中和目标实现"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="03/02/2022",
        effective="03/02/2022",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "国家发展和改革委员会、工业和信息化部、生态环境部、国家能源局"
        ),
        asset="高耗能行业生产设施和能源系统",
        asset_status="既有",
        asset_detail=(
            "本工具界定和覆盖的对象为17个高耗能行业重点领域现有的生产设施和能源"
            "系统，包括但不限于加热炉、反应器、窑炉、锅炉、电机系统、余热回收装置"
            "等主要用能和排放设备。指南为各类设施的节能降碳改造提供技术路径和"
            "方向参照。"
        ),
        agent="企业",
        agent_detail=(
            "17个重点高耗能行业领域内的生产企业，特别是能效未达到行业基准水平的"
            "企业。企业可参照指南自愿制定节能降碳改造升级方案，指南为指导性质，"
            "不设强制性合规义务。"
        ),
        activity="生产",
        activity_detail=(
            "本指南引导和规范的受规制活动为17个高耗能行业重点领域的生产经营活动"
            "中的用能和温室气体排放环节。指南通过提供各行业的具体技术路径和改造方向，"
            "帮助企业对标能效基准水平和标杆水平，指导和推动其开展节能降碳改造升级。"
            "四个方向中的引导改造升级和加快淘汰落后间接推动了生产活动的能效提升"
            "和低碳转型。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）各行业领域的节能降碳改造升级技术路径作为推荐性参考，企业结合实际"
            "选择适用技术和方案；2）指南对各行业提出引导改造升级、加强技术攻关、"
            "促进集聚发展、加快淘汰落后四个方向；3）指南为指导性质，不设强制性合规"
            "义务和处罚；4）推动能效在基准水平以下的企业加快改造升级，推动能效在"
            "标杆水平以上的企业示范引领。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与能效基准水平和标杆水平制度（发改产业〔2021〕1464号）联动：指南以"
            "该制度设定的能效指标为基准，提供改造技术路径。与产业结构调整指导目录"
            "联动：加快淘汰落后方向与淘汰类产业目录衔接。与差别电价等经济工具联动："
            "能效水平与企业电价挂钩。"
        ),
        resp_info_capture=(
            "国家发展改革委（产业发展司）会同工业和信息化部、生态环境部、国家能源局"
            "负责指南的研究编制和发布。"
        ),
        info_transmission=(
            "四部门通过通知和门户网站公开发布指南（政府公开发布）。"
        ),
        info_frequency=(
            "一次性发布（2022年版）。后续视需要修订更新。"
        ),
        info_public=(
            "是（公开）。指南通过国家发展改革委、工业和信息化部门户网站向社会"
            "全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "四部门组织指南的宣传解读和宣贯推广；指导行业协会和专业机构提供技术"
            "咨询和节能诊断服务；鼓励地方结合本地实际出台配套支持政策推动指南"
            "技术路径落地应用。"
        ),
        ghg_abs=(
            "N/A（本工具为技术指导性工具，通过引导高耗能企业对标能效基准水平并"
            "实施节能降碳改造间接促进减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术指导工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="C",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="能效提升；能源消耗减少；污染防治；绿色产业发展",
        legal_name=(
            "四部门关于发布《高耗能行业重点领域节能降碳改造升级实施指南"
            "（2022年版）》的通知（发改产业〔2022〕200号）"
        ),
        legal_url=(
            "https://www.ndrc.gov.cn/xwdt/tzgg/202202/"
            "t20220211_1315447_ext.html"
        ),
        other_links=(
            "https://www.miit.gov.cn/jgsj/jns/nyjy/art/2022/"
            "art_17b6f40586b84957b3503c78ce8584ac.html"
        ),
    ),
    make_row(
        pid="CHNCBATGCI03S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术指南",
        sector="工业",
        subsector="N/A",
        name_cn="工业绿色微电网建设与应用指南",
        name_en="Industrial Green Microgrid Construction and Application Guide",
        policy_package="N/A",
        description=(
            "工业绿色微电网建设与应用指南由工业和信息化部、国家"
            "发展改革委、国务院国资委、市场监管总局、国家能源局等五部门联合发布，"
            "是面向工业领域提供绿色微电网建设和应用技术方法的信息类工具，旨在引导"
            "工业园区和企业建设以可再生能源利用、工业余热余压余能回收、绿氢耦合、"
            "新型储能、柔性互联、数字化能碳管理为核心技术特征的绿色微电网系统。"
            "指南面向工业企业、工业园区、产业集聚区等四类应用场景，提出微电网系统"
            "规划设计、设备选型、建设实施、运行管理、并网互动等全流程技术要求，"
            "涵盖分布式可再生能源发电、余热余压回收发电、工业低温余热利用、新型储能"
            "配置、智能微电网控制、多能互补协调优化等方面。规划期为2026—2030年，"
            "目标到2028年分类建成具有代表性的工业绿色微电网示范标杆，到2030年实现"
            "工业绿色微电网规模化推广。"
        ),
        objective=(
            "引导工业企业和园区建设绿色微电网系统；提升工业领域可再生能源利用比例"
            "和能源利用效率；推动工业用能结构绿色低碳转型；支撑工业领域碳达峰碳中和"
            "目标实现"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="31/12/2025",
        effective="09/01/2026",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "工业和信息化部（节能与综合利用司）、国家发展和改革委员会、国务院国资委、"
            "国家市场监督管理总局、国家能源局"
        ),
        asset="工业绿色微电网系统（含可再生能源发电、储能、余能回收等）",
        asset_status="N/A",
        asset_detail=(
            "本工具界定和覆盖的对象为工业企业和园区建设的绿色微电网系统，包括分布式"
            "可再生能源发电设施（光伏、风电等）、工业余热余压余能回收利用装置、绿氢"
            "制备和利用耦合设施、新型储能装置（电化学储能、压缩空气储能等）、柔性"
            "互联和智能微电网控制系统、多能互补协调优化系统等组成部分。"
        ),
        agent="企业",
        agent_detail=(
            "工业企业、工业园区运营管理机构、产业集聚区管理机构和能源服务公司。"
            "相关主体可参照指南自愿规划建设和运营绿色微电网，指南为推荐性和指导"
            "性质，不设强制性合规义务。"
        ),
        activity="生产",
        activity_detail=(
            "本指南引导和规范的受规制活动为工业企业生产经营过程中的能源供给、转换、"
            "储存和消费活动。指南通过提供绿色微电网全流程技术要求和方法，引导企业"
            "和园区建设集可再生能源利用、余能回收、储能和智能控制于一体的新型能源"
            "供应体系，以分布式可再生能源替代部分化石能源电力，提高清洁能源消费比例"
            "并降低单位产品碳排放强度。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）工业绿色微电网建设应因地制宜利用可再生能源、工业余能、绿氢等清洁"
            "能源资源；2）系统设计应统筹考虑可再生能源发电、储能配置、余能回收、"
            "柔性互联和多能互补协调优化；3）微电网应具备并网运行和离网/孤岛运行"
            "能力，满足供电安全可靠性要求；4）指南为推荐性指导，企业和园区结合自身"
            "条件和需求选择适宜的建设和应用模式，不设强制性合规义务；5）鼓励开展"
            "微电网数字化能碳管理和碳排放核算。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与可再生能源电力消纳责任权重制度联动：工业绿色微电网可帮助用电企业"
            "提升可再生能源消纳比例。与绿证和绿电交易市场联动：微电网自发自用"
            "可再生能源部分可申请绿证。与碳排放权交易市场联动：微电网减少企业外购"
            "电力间接排放，影响企业碳排放核算和配额需求。"
        ),
        resp_info_capture=(
            "工业和信息化部（节能与综合利用司）会同国家发展改革委、国务院国资委、"
            "市场监管总局、国家能源局负责指南的研究编制和发布。"
        ),
        info_transmission=(
            "五部门通过通知和门户网站公开发布指南（政府公开发布）。"
        ),
        info_frequency=(
            "一次性发布（2026—2030年规划期）。后续视需要修订更新。"
        ),
        info_public=(
            "是（公开）。指南通过工业和信息化部门户网站等渠道向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "五部门组织指南的宣传解读和宣贯推广；指导地方相关部门结合本地实际"
            "组织开展工业绿色微电网试点示范和推广应用；鼓励行业协会、科研机构和"
            "技术服务企业提供技术支持和系统解决方案。"
        ),
        ghg_abs=(
            "N/A（本工具为技术指导性工具，通过引导工业企业和园区建设绿色微电网系统"
            "间接促进减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术指导工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="C",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="可再生能源发展；能效提升；能源安全；污染防治",
        legal_name=(
            "工业和信息化部办公厅 国家发展改革委办公厅 国务院国资委办公厅 市场监管"
            "总局办公厅 国家能源局综合司关于印发《工业绿色微电网建设与应用指南"
            "（2026—2030年）》的通知（工信厅联节〔2025〕77号）"
        ),
        legal_url=(
            "https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2026/"
            "art_44c5364d80b748e4b797bc115388c6aa.html"
        ),
        other_links=(
            "https://www.miit.gov.cn/jgsj/jns/nyjy/art/2026/"
            "art_3ef4f0f5b8d54fab92e87517355fb0e1.html"
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
