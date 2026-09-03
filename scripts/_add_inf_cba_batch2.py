#!/usr/bin/env python3
"""Insert four additional Information instruments (CBA group):
   TGC:
   - CHNCBATGCI04S000 (Agricultural Green Development Technical Guidance)
   - CHNCBATGCI06S000 (Industrial Product Green Design Guide)
   CBP:
   - CHNCBACBPI01S000 (Green Factory Gradient Cultivation and Management)
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

# Unicode escapes for Chinese quotation marks to avoid Python string conflicts
LQ = "“"  # left curly double quote
RQ = "”"  # right curly double quote


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
    # ── TGC 04: Agricultural Green Development Technical Guidance ──
    make_row(
        pid="CHNCBATGCI04S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术指南",
        sector="农业、林业和其他土地利用",
        subsector="N/A",
        name_cn="农业绿色发展技术导则（2018—2030年）",
        name_en=(
            "Agricultural Green Development Technical Guidance (2018-2030)"
        ),
        policy_package="N/A",
        description=(
            "农业绿色发展技术导则（2018—2030年）由农业农村部印发，是面向农业"
            "领域提供绿色生产技术发展方向和实施路径的信息类工具，旨在全面构建"
            "高效、安全、低碳、循环、智能、集成的农业绿色发展技术体系。导则以"
            "绿色投入品、节本增效技术、生态循环模式、绿色标准规范为主攻方向，"
            "提出七大任务：研制绿色投入品（高效优质多抗新品种、环保高效肥料与"
            "生物制剂、节能低耗智能化农业装备）；研发绿色生产技术（耕地质量提升、"
            "控水旱作、化肥农药减施增效、废弃物循环利用、面源污染及重金属治理、"
            "畜禽水产安全养殖等）；发展绿色产后增值技术（低碳减污加工贮运、"
            "智能化精深加工）；创新绿色低碳种养结构与技术模式；绿色乡村综合发展"
            "技术与模式；加强农业绿色发展基础研究；以及完善绿色标准体系。导则按"
            + LQ + "重点研发一批、集成示范一批、推广应用一批" + RQ +
            "三个层次分类推进，覆盖从基础研究到田间推广应用的全链条。"
            "规划期限为2018—2030年。"
        ),
        objective=(
            "以绿色投入品、节本增效技术、生态循环模式、绿色标准规范为主攻方向，"
            "全面构建高效、安全、低碳、循环、智能、集成的农业绿色发展技术体系，"
            "引领农业走上产出高效、产品安全、资源节约、环境友好的农业现代化道路"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="02/07/2018",
        effective="02/07/2018",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities="农业农村部（科技教育司）",
        asset="农业技术（信息/知识）",
        asset_status="新建",
        asset_detail=(
            "本工具为技术导则，界定和覆盖的对象为农业绿色发展相关的技术体系，"
            "包括绿色投入品、绿色生产技术、绿色产后增值技术、绿色低碳种养结构与"
            "技术模式等领域的农业技术、工艺和装备。导则本身为指导性质，不直接"
            "监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "农业企业、农业生产经营主体（包括种植业、畜牧业、水产养殖业等），"
            "以及农业科研机构和农业技术推广机构。各类主体可参照导则自愿开展"
            "绿色农业技术研发、集成示范和推广应用，导则为推荐性和指导性质，"
            "不设强制性合规义务。"
        ),
        activity="生产",
        activity_detail=(
            "导则覆盖农业绿色生产全链条活动，包括绿色投入品研制、绿色生产技术"
            "研发与应用、绿色产后增值技术应用、绿色低碳种养结构与技术模式创新、"
            "绿色乡村综合发展技术与模式应用，以及农业绿色发展基础研究。涵盖从"
            "基础研究、技术研发到田间示范推广的全过程。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）围绕绿色投入品、节本增效技术、生态循环模式、绿色标准规范四大"
            "主攻方向推进农业绿色发展技术体系建设；2）按" + LQ + "重点研发一批、"
            "集成示范一批、推广应用一批" + RQ + "三个层次分类推进；3）到2030年"
            "主要目标：农田灌溉用水有效利用系数提高到0.6以上；农业源氮、磷污染物"
            "排放分别削减30%和40%以上；养殖节水源头减排20%以上；农产品加工单位"
            "产值能耗降低20%以上；单位农业增加值温室气体排放强度降低30%以上；"
            "4）导则为推荐性和指导性质，不设强制性合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与农业面源污染治理、耕地质量保护、化肥农药减量增效、畜禽粪污资源化"
            "利用等相关政策形成协同；为农业绿色发展相关标准化工作提供技术基础。"
        ),
        resp_info_capture=(
            "农业农村部科技教育司负责组织导则的研究编制和发布。"
        ),
        info_transmission=(
            "农业农村部通过通知和门户网站公开发布导则（政府公开发布）。"
        ),
        info_frequency="中长期规划（2018—2030年），不定期修订更新。",
        info_public="是（公开）。导则通过政府门户网站向社会全文公开。",
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "农业农村部组织导则的解读宣贯；依托农业技术推广体系和农业科研院所"
            "开展技术培训、示范推广和经验交流；引导地方农业部门和经营主体落实"
            "导则提出的技术方向。"
        ),
        ghg_abs=(
            "N/A（本工具为技术导则，通过引导农业绿色生产技术的研发和推广应用"
            "间接支持农业领域温室气体减排，无直接可量化的排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术指导工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="A01",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="污染防治；资源节约；循环经济；生态保护；食品安全",
        legal_name=(
            "农业农村部关于印发《农业绿色发展技术导则（2018—2030年）》的通知"
            "（农科教发〔2018〕3号）"
        ),
        legal_url=(
            "https://www.gov.cn/zhengce/zhengceku/2018-12/31/content_5445929.htm"
        ),
        other_links=(
            "https://www.moa.gov.cn/gk/zcjd/201904/t20190418_6184810.htm"
        ),
    ),
,

    # ── TGC 06: Industrial Product Green Design Guide ──
    make_row(
        pid="CHNCBATGCI06S000",
        group_cn="能力建设与公众意识",
        approach_cn="技术指南",
        sector="工业",
        subsector="汽车；工程机械；机床；轴承；风电装备；氢能装备；光伏；锂电池；家用电器；包装；洗涤用品；纺织；生物制造；甲醇；轮胎",
        name_cn="工业产品绿色设计指南",
        name_en="Industrial Product Green Design Guide",
        policy_package="N/A",
        description=(
            "工业产品绿色设计指南由工业和信息化部、国家发展改革委、"
            "教育部、生态环境部、市场监管总局五部门联合印发，是面向工业企业提供"
            "产品绿色设计方法和技术路径的信息类工具，旨在系统总结前期试点示范经验"
            "（累计培育451家工业产品绿色设计示范企业），推动工业产品绿色设计工作"
            "从" + LQ + "示范引领" + RQ + "向" + LQ + "全面推广" + RQ + "转变。"
            "指南提出11个绿色设计重点方向：长寿命设计、无害化设计、轻量化设计、"
            "节能设计、节水设计、节材设计、降噪设计、节空间设计、易回收再生设计、"
            "可重复使用设计、零碳设计。指南覆盖汽车、工程机械、机床、轴承、风电"
            "装备、氢能装备、光伏、锂电池、家用电器、包装、洗涤用品、纺织、生物"
            "制造、甲醇、轮胎等15个重点行业，逐一细化了126个可操作的绿色设计解决"
            "方案。同时提出六大实施路径：开发绿色设计解决方案、推进" + LQ +
            "人工智能+绿色设计" + RQ + "、制定绿色设计标准、推广绿色设计标志性"
            "产品、加大绿色设计人才培养、深化国际交流与合作。"
        ),
        objective=(
            "按照产品全生命周期理论，在产品设计开发阶段系统考虑各环节"
            "对资源消耗、生态环境、气候变化的影响；最大限度降低或控制"
            "资源能源消耗；尽可能不用或少用含有毒有害物质的原料；"
            "减少污染物、温室气体的产生和排放；实现绿色低碳发展"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="01/04/2026",
        effective="01/04/2026",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "工业和信息化部（节能与综合利用司）；国家发展改革委；教育部；"
            "生态环境部；市场监管总局"
        ),
        asset="工业产品（设计阶段）",
        asset_status="新建",
        asset_detail=(
            "本工具为技术指南，界定和覆盖的对象为工业产品的绿色设计方法和技术路径，"
            "涵盖汽车、工程机械、机床、轴承、风电装备、氢能装备、光伏、锂电池等"
            "15个重点行业的产品设计活动。指南本身为推荐性和指导性质，不直接监管"
            "实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "工业企业（特别是制造业产品设计和生产企业）；绿色设计解决方案供应商；"
            "相关行业协会和标准化机构。企业可参照指南自愿开展绿色设计，指南为"
            "推荐性和指导性质，不设强制性合规义务。"
        ),
        activity="研究与开发",
        activity_detail=(
            "指南覆盖工业产品设计阶段的绿色化活动，包括长寿命设计、无害化设计、"
            "轻量化设计、节能设计、节水设计、节材设计、降噪设计、节空间设计、"
            "易回收再生设计、可重复使用设计、零碳设计等11个产品绿色设计方向。"
            "产品生命周期约80%的资源消耗和环境影响取决于设计阶段，指南从设计源头"
            "推动工业产品全生命周期绿色化。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）围绕11个绿色设计方向（长寿命、无害化、轻量化、节能、节水、节材、"
            "降噪、节空间、易回收再生、可重复使用、零碳设计）系统推进工业产品"
            "绿色设计；2）覆盖汽车、工程机械、机床、光伏、锂电池等15个重点行业，"
            "提供126个可操作的绿色设计解决方案；3）通过开发绿色设计解决方案、推进"
            + LQ + "人工智能+绿色设计" + RQ + "、制定绿色设计标准、推广标志性产品、"
            "加大人才培养、深化国际合作六大路径推进实施；4）指南为推荐性和指导"
            "性质，不设强制性合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与绿色工厂梯度培育、绿色供应链管理、绿色产品认证、绿色公共采购等"
            "政策形成协同；为《工业产品绿色设计通则》等标准制定提供基础；与中欧、"
            "中德、中法等国际绿色设计合作机制衔接。"
        ),
        resp_info_capture=(
            "工业和信息化部（节能与综合利用司）会同国家发展改革委、教育部、"
            "生态环境部、市场监管总局共同组织指南的研究编制和发布。"
        ),
        info_transmission=(
            "工业和信息化部等五部门通过通知和门户网站公开发布指南（政府公开"
            "发布）。"
        ),
        info_frequency="按需不定期修订（如2026年版）。",
        info_public=(
            "是（公开）。指南通过工业和信息化部等主管部门门户网站向社会全文公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "工业和信息化部等五部门组织指南的解读宣贯；通过行业协会和标准化机构"
            "开展绿色设计培训、技术交流和标杆案例推广；引导绿色设计解决方案供应商"
            "培育和标志性产品推广。"
        ),
        ghg_abs=(
            "N/A（本工具为技术指南，通过引导企业从设计源头实施绿色设计间接减少"
            "产品全生命周期温室气体排放，无直接可量化的排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接技术指导工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="C",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新；资源节约；循环经济；污染防治",
        legal_name=(
            "工业和信息化部等五部门关于印发《工业产品绿色设计指南（2026年版）》"
            "的通知（工信厅联节〔2026〕15号）"
        ),
        legal_url=(
            "https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2026/"
            "art_0e02aa4c9dfe40c0ae322af3c185eed6.html"
        ),
        other_links=(
            "https://www.miit.gov.cn/jgsj/jns/lszz/art/2026/"
            "art_a240711299e045b284c4bff34f13450e.html"
        ),
    ),
    make_row(
        pid="CHNCBACBPI01S000",
        group_cn="能力建设与公众意识",
        approach_cn="能力建设计划",
        sector="工业",
        subsector="N/A",
        name_cn="绿色工厂梯度培育及管理",
        name_en=(
            "Green Factory Gradient Cultivation and Management"
        ),
        policy_package="N/A",
        description=(
            "绿色工厂梯度培育及管理由工业和信息化部印发，是面向制造业"
            "企业组织实施分级评价、动态管理和梯度培育的能力建设类信息工具，旨在"
            "通过建立国家—省—市三级联动的绿色工厂培育机制，引导企业持续提升绿色"
            "低碳水平。绿色工厂是指实现用地集约化、原料无害化、生产洁净化、废物"
            "资源化、能源低碳化的企业。办法从两个维度建立梯度培育机制：纵向形成"
            "国家、省、市三级联动的绿色工厂培育机制；横向通过绿色工业园区和绿色"
            "供应链管理企业带动园区内及供应链上下游企业创建绿色工厂。办法共六章"
            "27条，涵盖培育要求、创建程序（自评价或委托第三方评价，通过" + LQ +
            "工业节能与绿色发展管理平台" + RQ + "提交）、动态管理（" + LQ +
            "有进有出" + RQ + "机制，对得分连续三年处于后5%的移出名单）和配套"
            "机制（推广" + LQ + "企业绿码" + RQ + "，在规划布局、技术改造、金融"
            "服务等方面提供支持）。截至目前累计培育国家级绿色工厂8,336家（产值占"
            "规上制造业总产值22%）、绿色工业园区616家，带动省市级绿色工厂1.6万"
            "余家。"
        ),
        objective=(
            "加快构建绿色制造和服务体系；发挥绿色工厂在制造业"
            "绿色低碳转型中的基础性和导向性作用；加快形成规范化、"
            "长效化培育机制；打造绿色制造领军力量"
        ),
        mitigation="直接",
        channel="供给侧",
        adoption="19/01/2024",
        effective="19/01/2024",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities="工业和信息化部（节能与综合利用司）",
        asset="绿色工厂（制造业生产设施）",
        asset_status="新建；既有",
        asset_detail=(
            "本工具为能力建设计划，界定和覆盖的对象为经评价认定的绿色工厂，即实现"
            "用地集约化、原料无害化、生产洁净化、废物资源化、能源低碳化的制造业"
            "企业生产设施。涵盖国家级、省级、市级三个层次。工具本身为培育和管理"
            "性质，不直接监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "制造业企业（自愿申报绿色工厂评价认定）；第三方评价机构（受委托开展"
            "绿色工厂评价）；各级工业和信息化主管部门（组织推荐和动态管理）；"
            "绿色工业园区和绿色供应链管理企业（横向带动）。企业参与为自愿性质，"
            "通过管理平台自主申报，不设强制性义务。"
        ),
        activity="生产",
        activity_detail=(
            "办法覆盖绿色工厂的梯度培育和动态管理活动，包括企业自评价或委托第三方"
            "评价、通过管理平台申报、地方推荐、国家认定、以及持续的动态管理和绩效"
            "改进。绿色工厂评价涵盖用地、原料、生产、废物、能源五个维度的绿色化"
            "水平，引导企业在生产全过程中持续提升绿色低碳绩效。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）建立国家—省—市三级联动的绿色工厂梯度培育机制；2）绿色工厂须"
            "满足用地集约化、原料无害化、生产洁净化、废物资源化、能源低碳化要求；"
            "3）企业通过" + LQ + "工业节能与绿色发展管理平台" + RQ + "自主申报，"
            "采取自评价或委托第三方评价方式；4）建立" + LQ + "有进有出" + RQ +
            "的动态管理机制，对得分连续三年处于后5%的移出名单；5）推广" + LQ +
            "企业绿码" + RQ + "，在规划布局、技术改造、金融服务等方面提供配套支持；"
            "6）近三年发生安全/环保事故、失信、偷漏税等不得申报（一票否决）；"
            "7）办法为培育和管理性质，企业参与为自愿，不设强制性合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与绿色工厂评价通则（GB/T 36132-2025）、绿色工业园区评价通则等标准"
            "衔接；与绿色供应链管理、绿色设计产品认定、绿色公共采购、绿色金融等"
            "政策协同，将绿色工厂纳入相关支持政策优先对象。"
        ),
        resp_info_capture=(
            "工业和信息化部（节能与综合利用司）负责制定管理办法、组织国家级绿色"
            "工厂的遴选认定和动态管理；省级和市级工业和信息化主管部门负责本辖区"
            "绿色工厂的培育、推荐和日常管理。"
        ),
        info_transmission=(
            "工业和信息化部通过通知和门户网站公开发布办法、年度推荐通知和绿色"
            "工厂名单（政府公开发布）；企业通过" + LQ + "工业节能与绿色发展管理"
            "平台" + RQ + "（https://green.miit.gov.cn）在线申报和填报动态管理表。"
        ),
        info_frequency=(
            "每年7月31日前省级推荐至国家；每年4月15日前已认定企业填报动态管理表；"
            "年度发布绿色工厂推荐通知和名单。"
        ),
        info_public=(
            "是（公开）。绿色工厂名单和管理办法通过工业和信息化部门户网站向社会"
            "公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "工业和信息化部组织绿色工厂评价标准的制修订和宣贯培训；各级工信部门"
            "组织绿色工厂经验交流和标杆推广；推广" + LQ + "企业绿码" + RQ +
            "制度，对绿色工厂实施分级展示和分类管理；将绿色工厂纳入技术改造、"
            "绿色金融、政府采购等支持政策的优先对象。"
        ),
        ghg_abs=(
            "N/A（本工具为能力建设计划，通过引导企业创建绿色工厂提升能效和减少"
            "排放间接支持工业领域温室气体减排，无直接可量化的排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接能力建设工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="C",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；资源节约；污染防治；循环经济",
        legal_name=(
            "工业和信息化部关于印发《绿色工厂梯度培育及管理暂行办法》的通知"
            "（工信部节〔2024〕13号）"
        ),
        legal_url="https://www.gov.cn/zhengce/zhengceku/202401/content_6929104.htm",
        other_links=(
            "https://www.miit.gov.cn/jgsj/jns/gzdt/art/2026/"
            "art_ff0367abfedd4a4d86d56599878d2ff3.html"
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
                print(f"  {pid} already up to date -- skipping")
            continue

        # Insert after the last CBA row to keep CBA group contiguous
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
