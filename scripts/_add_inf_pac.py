#!/usr/bin/env python3
"""Insert four Public awareness campaign (PAC) instruments into the Information CN CSV.

   Instruments:
   - CHNCBAPACI01S000  全国城市生活垃圾分类宣传周
   - CHNCBAPACI03S000  全国节能宣传周
   - CHNCBAPACI04S000  全国低碳日
   - CHNCBAPACI05S000  绿色出行宣传月和公交出行宣传周
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
    # ── PAC 01: 全国城市生活垃圾分类宣传周 ──
    make_row(
        pid="CHNCBAPACI01S000",
        group_cn="能力建设与公众意识",
        approach_cn="公众宣传教育活动",
        sector="废弃物",
        subsector="N/A",
        name_cn="全国城市生活垃圾分类宣传周",
        name_en="National Urban Waste Sorting Awareness Week",
        policy_package="N/A",
        description=(
            "全国城市生活垃圾分类宣传周由住房和城乡建设部、教育部、国家机关事务"
            "管理局、中华全国总工会、共青团中央五部门联合设立，自2023年起每年5月"
            "第四周举办，是全国性公众宣传教育活动，旨在提升全社会对生活垃圾分类的"
            "认知度和参与度，推动垃圾分类从" + LQ + "新时尚" + RQ + "变为" + LQ +
            "好习惯" + RQ + "。宣传周活动内容包括：传达中央关于垃圾分类的部署要求；"
            "宣贯垃圾分类相关制度政策标准；宣介阶段性工作成果和典型城市经验；推广"
            "各地垃圾分类实践中的可行做法；普及生活垃圾分类知识和方法。宣传周采用"
            "" + LQ + "线上+线下" + RQ + "相结合方式，通过媒体报道、公益广告、主题"
            "活动、志愿服务、知识竞赛等多种形式开展。宣传周设立以来，每年确定一个"
            "主题，如2023年" + LQ + "让垃圾分类成为新时尚" + RQ + "、2024年" +
            LQ + "践行新时尚 分类志愿行" + RQ + "、2025年" + LQ + "分类齐参与 "
            "低碳新时尚" + RQ + "。各地方住房城乡建设（环卫）主管部门会同相关部门"
            "制定本地区实施方案并组织实施。"
        ),
        objective=(
            "提升公众生活垃圾分类意识和知识水平；引导公众积极参与垃圾分类实践；"
            "推动城市生活垃圾减量化、资源化、无害化处理；促进绿色低碳生活方式形成"
        ),
        mitigation="直接",
        channel="需求侧",
        adoption="18/05/2023",
        effective="18/05/2023",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "住房和城乡建设部；教育部；国家机关事务管理局；"
            "中华全国总工会；共青团中央"
        ),
        asset="公众意识/知识（宣传教育）",
        asset_status="N/A",
        asset_detail=(
            "本工具为公众宣传教育活动，界定和覆盖的对象为生活垃圾分类相关的公众"
            "意识和行为，不直接监管实体排放资产。宣传周通过知识普及、行为倡导等"
            "非强制性手段引导公众提高垃圾分类意识、参与垃圾分类实践。"
        ),
        agent="社会公众；企业；公共机构",
        agent_detail=(
            "城市居民和家庭（生活垃圾分类投放主体）；机关、企事业单位、学校、"
            "社会团体等（分类投放和分类管理责任人）；环卫服务企业和从业人员（分类"
            "收集、运输和处理主体，但不设强制性要求）。参与者为自愿性质，通过宣传"
            "教育引导行为改变，不设强制性合规义务和处罚。"
        ),
        activity="收集或分类（消费后）",
        activity_detail=(
            "宣传周覆盖的宣传教育对象为城市生活垃圾从产生、分类投放到收集转运的"
            "全过程行为，重点引导居民在源头进行生活垃圾分类（可回收物、有害垃圾、"
            "厨余垃圾、其他垃圾），帮助公众掌握分类知识和技能，养成分类投放习惯。"
            "宣传周本身为信息传播和公众教育活动，不直接监管排放活动。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）每年5月第四周在全国范围内组织开展城市生活垃圾分类宣传周活动；"
            "2）围绕制度政策宣贯、工作成果展示、典型经验推广、分类知识普及等"
            "内容开展宣传活动；3）采用" + LQ + "线上+线下" + RQ + "相结合方式，"
            "通过多种媒体渠道和活动形式覆盖社会公众；4）各地方制定实施方案并组织"
            "实施，活动结束后报送总结；5）活动为宣传教育性质，不设强制性合规义务"
            "和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与《固体废物污染环境防治法》和城市生活垃圾分类管理相关法规制度衔接，"
            "为分类制度落地执行提供公众认知基础和社会氛围支撑；与生活垃圾分类"
            "示范城市创建、垃圾分类考核评估等工作协同推进。"
        ),
        resp_info_capture=(
            "住房和城乡建设部（城市建设司）会同教育部、国管局、全国总工会、"
            "共青团中央联合制发年度活动通知。"
        ),
        info_transmission=(
            "住房和城乡建设部等五部门通过通知和门户网站公开发布活动方案"
            "（政府公开发布）；宣传内容通过传统媒体、新媒体、社区宣传栏、"
            "志愿服务等渠道向公众传播。"
        ),
        info_frequency="每年一次（每年5月第四周），每年印发活动通知。",
        info_public=(
            "是（公开）。宣传周活动通知和活动内容通过政府网站和各类媒体向社会公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "住房和城乡建设部等部门制作垃圾分类宣传资料并组织分发；通过媒体报道、"
            "公益广告、主题活动、志愿服务和知识竞赛等多种形式向公众传播垃圾分类"
            "知识；组织垃圾分类科普教育基地和示范场所向公众开放；引导各地开展"
            "垃圾分类主题公园、体验馆等宣传教育设施建设。"
        ),
        ghg_abs=(
            "N/A（本工具为公众宣传教育活动，通过提高垃圾分类意识和参与率间接"
            "减少垃圾填埋产生的甲烷排放，无直接可量化的排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接宣传教育工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="E38",
        ghg="CO2; CH4",
        mitigation_effects="正向",
        co_benefits="资源节约；循环经济；污染防治；绿色产业发展",
        legal_name=(
            "住房和城乡建设部办公厅等五部门关于开展"
            "" + LQ + "全国城市生活垃圾分类宣传周" + RQ + "活动的通知"
        ),
        legal_url=(
            "https://gbc.ggj.gov.cn/xwzx/ggjxw/202305/"
            "t20230522_42974.htm"
        ),
        other_links="N/A",
    ),

    # ── PAC 03: 全国节能宣传周 ──
    make_row(
        pid="CHNCBAPACI03S000",
        group_cn="能力建设与公众意识",
        approach_cn="公众宣传教育活动",
        sector="跨部门",
        subsector="N/A",
        name_cn="全国节能宣传周",
        name_en="National Energy Conservation Awareness Week",
        policy_package="N/A",
        description=(
            "全国节能宣传周是在1990年国务院第六次节能办公会议（国阅[1990]129号）"
            "决定设立的基础上，自1991年起每年举办的全国性节能主题宣传教育活动，"
            "是中国设立最早、持续时间最长的全国性节能公益宣传活动。首届宣传周于"
            "1991年10月7日至12日举行，由原国家计委、广播电影电视部、共青团中央、"
            "能源部、全国总工会和中国科学技术协会联合发起。原安排每年10月至11月，"
            "2004年起调整为每年6月（应对夏季用电高峰）。2013年起，每年节能宣传周"
            "第三天定为" + LQ + "全国低碳日" + RQ + "。宣传周由国家发展改革委和"
            "生态环境部牵头，会同教育部、科技部、工业和信息化部等多部门联合印发"
            "年度活动通知（发改环资），各地方和部门按职责分工组织实施。宣传周围绕"
            "年度主题，宣传节能法律法规和标准规范，展示节能降碳技术和产品，"
            "推广先进节能经验和做法，普及节能知识和方法，通过" + LQ + "线上+线下"
            + RQ + "方式开展形式多样的宣传活动，覆盖工业、建筑、交通、公共机构"
            "等重点领域。活动结束后，各地各部门须将活动情况报送国家发展改革委和"
            "生态环境部。"
        ),
        objective=(
            "宣传节能法律法规和标准规范；展示节能降碳技术和产品；推广先进节能"
            "经验；普及节能知识和方法；提高全民节能意识和能力；推动形成绿色低碳的"
            "生产方式和生活方式"
        ),
        mitigation="直接",
        channel="需求侧",
        adoption="07/10/1991",
        effective="07/10/1991",
        revision="17/06/2013",
        revision_detail=(
            "全国节能宣传周自1991年起每年举办，最初安排在每年10月至11月。2004年"
            "调整至每年6月以应对夏季用电高峰。2013年起增设全国低碳日（节能宣传周"
            "第三天）。活动由国务院节能办公会议决定设立，每年由国家发展改革委牵头"
            "联合多部门印发年度活动通知，年度主题和重点内容随节能工作形势调整。"
        ),
        status="生效",
        admin_authorities=(
            "国家发展和改革委员会；生态环境部；会同教育部、科技部、工业和信息化部、"
            "住房和城乡建设部、交通运输部、农业农村部、商务部、国务院国资委、"
            "市场监管总局、广电总局、国家机关事务管理局、全国总工会、共青团中央、"
            "全国妇联等多部门"
        ),
        asset="公众意识/知识（宣传教育）",
        asset_status="N/A",
        asset_detail=(
            "本工具为公众宣传教育活动，界定和覆盖的对象为全社会节能意识和节能"
            "知识，不直接监管实体排放资产。宣传周通过节能知识普及、技术展示和经验"
            "推广等非强制性手段提高全社会节能意识，引导企业和公众采取节能行动。"
        ),
        agent="社会公众；企业；公共机构",
        agent_detail=(
            "全社会各类用能主体，包括工业生产企业、建筑运营单位、交通运输企业、"
            "公共机构（政府机关、学校、医院等）以及居民家庭和个人。宣传周为面向"
            "全社会的宣传教育活动，各主体可自主参与，不设强制性合规义务和处罚。"
        ),
        activity="消费",
        activity_detail=(
            "宣传周宣传教育覆盖全社会各领域的能源消费行为，包括工业生产用能、"
            "建筑运营用能（供暖、制冷、照明）、交通运输用能（车辆运行、出行方式"
            "选择）、公共机构用能和居民生活用能等。活动通过倡导节能行为和高效用能"
            "实践，引导全社会在能源消费活动中节约和提高能效。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）每年6月在全国范围内组织开展全国节能宣传周活动；2）国家发展改革委"
            "和生态环境部牵头制定年度活动方案，会同多部门联合印发通知；3）各地方"
            "和部门围绕年度主题，采取" + LQ + "线上+线下" + RQ + "方式开展形式多样"
            "的宣传活动；4）活动结束后各地各部门将总结报送国家发展改革委（环资司）"
            "和生态环境部（气候司）；5）活动为宣传教育性质，不设强制性合规义务和"
            "处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与全国低碳日（每年节能宣传周第三天）同期联合举办，共享年度活动通知"
            "和组织体系；与节能产品惠民工程、能效标识制度、能效" + LQ + "领跑者"
            + RQ + "制度等节能政策和标准体系衔接，为其提供公众认知基础；与公共"
            "机构节能管理和工业节能监察形成宣传和监管配合。"
        ),
        resp_info_capture=(
            "国家发展改革委（资源节约和环境保护司）和生态环境部（应对气候变化司）"
            "联合牵头制定年度活动方案。"
        ),
        info_transmission=(
            "国家发展改革委等部门通过政府网站和通知公开发布年度活动方案（政府公开"
            "发布）；宣传教育内容通过传统媒体、新媒体、户外广告、社区宣传、"
            "现场活动等渠道向社会传播。"
        ),
        info_frequency="每年一次（每年6月），每年印发活动通知。",
        info_public=(
            "是（公开）。节能宣传周活动通知和内容通过政府网站和各类媒体渠道"
            "向社会公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "国家发展改革委等牵头部门制作节能宣传资料并组织媒体宣传；通过节能技术"
            "展示、产品推介、经验交流、知识竞赛和公益广告等形式向企业和公众传播"
            "节能知识和方法；组织节能服务机构开展节能诊断和咨询服务；开展节能"
            "先进典型和最佳实践的宣传推广；各地方结合实际情况组织地方特色活动。"
        ),
        ghg_abs=(
            "N/A（本工具为公众宣传教育活动，通过提高全社会节能意识和能力间接减少"
            "化石能源消费碳排放，无直接可量化的排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接宣传教育工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="M72",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="能源消耗减少；能源安全；绿色产业发展；技术创新；污染防治",
        legal_name=(
            "国家发展改革委 生态环境部关于开展2026年全国节能宣传周和全国低碳日"
            "活动的通知（发改环资〔2026〕664号）"
        ),
        legal_url=(
            "https://www.ndrc.gov.cn/xwdt/tzgg/202605/t20260520_1405335.html"
        ),
        other_links=(
            "https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=20632"
        ),
    ),

    # ── PAC 04: 全国低碳日 ──
    make_row(
        pid="CHNCBAPACI04S000",
        group_cn="能力建设与公众意识",
        approach_cn="公众宣传教育活动",
        sector="跨部门",
        subsector="N/A",
        name_cn="全国低碳日",
        name_en="National Low-Carbon Day",
        policy_package="N/A",
        description=(
            "全国低碳日由2012年9月19日国务院常务会议决定设立，自2013年起将每年"
            "全国节能宣传周的第三天定为全国低碳日，旨在普及气候变化知识，宣传低碳"
            "发展理念和政策，鼓励公众参与，推动落实控制温室气体排放任务。首个全国"
            "低碳日为2013年6月17日。全国低碳日由国家发展改革委和生态环境部牵头，"
            "会同多部门联合印发年度活动通知（与全国节能宣传周同文印发），各地方"
            "和部门按职责分工组织实施。全国低碳日每年设定一个活动主题，围绕应对"
            "气候变化、推动绿色低碳发展、普及碳排放双控和碳市场知识等内容，通过"
            "" + LQ + "线上+线下" + RQ + "方式开展形式多样的宣传活动，包括主题"
            "宣讲、媒体宣传、公众体验、低碳日现场活动等，倡导绿色低碳生产生活方式，"
            "动员全社会参与碳达峰碳中和行动。活动目的之一是配合全国碳排放权交易"
            "市场的宣传推广，提高企业和公众对碳市场、碳普惠、碳足迹等的认知和参与"
            "意识。"
        ),
        objective=(
            "普及气候变化知识；宣传绿色低碳发展理念和政策；鼓励公众参与应对"
            "气候变化行动；推动落实控制温室气体排放任务；营造绿色低碳社会风尚"
        ),
        mitigation="直接",
        channel="需求侧",
        adoption="19/09/2012",
        effective="17/06/2013",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "国家发展和改革委员会；生态环境部；会同教育部、科技部、工业和信息化部、"
            "住房和城乡建设部、交通运输部等多部门"
        ),
        asset="公众意识/知识（宣传教育）",
        asset_status="N/A",
        asset_detail=(
            "本工具为公众宣传教育活动，界定和覆盖的对象为全社会应对气候变化和低碳"
            "发展意识及知识，不直接监管实体排放资产。全国低碳日通过气候变化知识普及"
            "和低碳理念传播等非强制性手段提高全社会低碳意识，引导企业和公众采取低碳"
            "行动。"
        ),
        agent="社会公众；企业；公共机构",
        agent_detail=(
            "全社会各类主体，包括工业企业、建筑运营单位、交通运输企业、公共机构"
            "以及居民家庭和个人。全国低碳日为面向全社会的宣传教育活动，各主体可自主"
            "参与，不设强制性合规义务和处罚。"
        ),
        activity="消费",
        activity_detail=(
            "全国低碳日宣传教育覆盖全社会各领域的碳排放行为，重点引导公众在能源消费、"
            "交通出行、消费购物和日常生活等方面的低碳选择，包括节约用电用水用气、"
            "优先选择公共交通和绿色出行、减少一次性用品使用、践行光盘行动和低碳"
            "消费等。活动本身为宣传教育性质，不直接监管特定排放活动。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）每年全国节能宣传周的第三天定为全国低碳日，在全国范围内组织开展"
            "低碳主题宣传教育活动；2）国家发展改革委和生态环境部牵头制定年度活动"
            "方案，与全国节能宣传周同文印发通知（发改环资）；3）各地方和部门围绕"
            "年度主题，采取" + LQ + "线上+线下" + RQ + "方式开展形式多样的宣传活动；"
            "4）活动结束后各地各部门将总结报送国家发展改革委和生态环境部；5）活动"
            "为宣传教育性质，不设强制性合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与全国节能宣传周同期联合举办，共享年度活动通知和组织体系；与全国碳市场"
            "（ETS）和碳普惠机制衔接，为碳市场运行提供公众认知基础和社会氛围支撑；"
            "与全国生态日等生态文明宣传教育矩阵协同。"
        ),
        resp_info_capture=(
            "国家发展改革委（资源节约和环境保护司）和生态环境部（应对气候变化司）"
            "联合牵头制定年度活动方案。"
        ),
        info_transmission=(
            "国家发展改革委等部门通过政府网站和通知公开发布年度活动方案（政府公开"
            "发布）；宣传教育内容通过传统媒体、新媒体、社区宣传、现场活动等渠道"
            "向社会传播。"
        ),
        info_frequency="每年一次（每年节能宣传周第三天，约6月中旬），每年印发活动通知。",
        info_public="是（公开）。全国低碳日活动通知和内容通过政府网站和各类媒体渠道向社会公开。",
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "国家发展改革委和生态环境部等牵头部门组织全国低碳日主场活动；制作和"
            "发布气候变化与低碳发展科普宣传资料；通过媒体专题报道、公益广告、知识"
            "竞赛和公众体验活动等形式传播气候变化知识和低碳理念；引导地方开展低碳"
            "社区、低碳校园、低碳出行等主题实践活动；围绕全国碳市场、碳普惠、碳足迹"
            "等开展政策解读和公众宣传。"
        ),
        ghg_abs=(
            "N/A（本工具为公众宣传教育活动，通过提高全社会应对气候变化意识和低碳"
            "行动参与度间接减少温室气体排放，无直接可量化的排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接宣传教育工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="M72",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="能源消耗减少；绿色产业发展；技术创新；污染防治；公众健康",
        legal_name=(
            "国家发展改革委 生态环境部关于开展2026年全国节能宣传周和全国低碳日"
            "活动的通知（发改环资〔2026〕664号）"
        ),
        legal_url=(
            "https://www.ndrc.gov.cn/xwdt/tzgg/202605/t20260520_1405335.html"
        ),
        other_links=(
            "https://www.gov.cn/zwgk/2013-05/07/content_2397275.htm"
        ),
    ),

    # ── PAC 05: 绿色出行宣传月和公交出行宣传周 ──
    make_row(
        pid="CHNCBAPACI05S000",
        group_cn="能力建设与公众意识",
        approach_cn="公众宣传教育活动",
        sector="交通",
        subsector="N/A",
        name_cn="绿色出行宣传月和公交出行宣传周",
        name_en=(
            "Green Travel Awareness Month and "
            "Public Transit Awareness Week"
        ),
        policy_package="N/A",
        description=(
            "绿色出行宣传月和公交出行宣传周是由交通运输部牵头，会同公安部、民政部、"
            "国家机关事务管理局、中华全国总工会、共青团中央、中国残疾人联合会等"
            "多部门联合组织的全国性绿色出行主题宣传教育活动。公交出行宣传周最早"
            "于2013年由交通运输部设立，定于每年9月16日至22日，以贯彻落实《国务院"
            "关于城市优先发展公共交通的指导意见》（国发〔2012〕64号）为政策基础。"
            "2018年起扩展为绿色出行宣传月（覆盖整个9月）和公交出行宣传周。活动围绕"
            "年度主题，以" + LQ + "优选公交 绿色出行" + RQ + "为核心理念，通过"
            "" + LQ + "线上+线下" + RQ + "方式开展多种形式的宣传和公众参与活动，"
            "主要包括：绿色出行公益宣传作品征集与展播（海报、微视频等）；绿色出行"
            "主题宣传（总结公交和慢行交通发展成就）；多样化公众参与和体验活动"
            "（碳积分、碳普惠、知识竞赛、乘车优惠等）；提升适老化无障碍出行服务；"
            "安全文明绿色出行活动；以及关心关爱公交司乘人员活动。活动结束后各地"
            "报送总结。"
        ),
        objective=(
            "深入实施城市公共交通优先发展战略；鼓励引导社会公众优先选择公共交通"
            "和绿色出行方式；推动形成绿色低碳生活方式；改善城市交通环境和空气质量"
        ),
        mitigation="直接",
        channel="需求侧",
        adoption="31/08/2013",
        effective="16/09/2013",
        revision="01/09/2018",
        revision_detail=(
            "公交出行宣传周于2013年由交通运输部设立（交运发〔2013〕XXX号），"
            "最初仅在9月16日至22日举行为期一周的宣传教育活动。2018年起扩展为"
            "绿色出行宣传月和公交出行宣传周，覆盖整个9月，由交通运输部、公安部、"
            "国管局、全国总工会等四部门联合部署。后续参与部门扩展至七部门。"
        ),
        status="生效",
        admin_authorities=(
            "交通运输部；公安部；民政部；国家机关事务管理局；中华全国总工会；"
            "共青团中央；中国残疾人联合会"
        ),
        asset="公众意识/知识（宣传教育）",
        asset_status="N/A",
        asset_detail=(
            "本工具为公众宣传教育活动，界定和覆盖的对象为全社会绿色出行意识和公共"
            "交通使用行为，不直接监管实体排放资产。宣传月和宣传周通过公交优先理念"
            "传播、绿色出行倡导和公众体验活动等非强制性手段引导公众改变出行方式。"
        ),
        agent="社会公众；企业；公共机构",
        agent_detail=(
            "城市居民和出行者（公共交通和绿色出行选择主体）；公共交通运营企业"
            "（公交、地铁等运营和宣传配合主体）；政府机关和公共机构（绿色出行"
            "示范带头主体）；互联网出行平台和共享交通企业。活动为面向全社会的"
            "宣传教育性质，各主体可自主参与，不设强制性合规义务和处罚。"
        ),
        activity="消费",
        activity_detail=(
            "宣传月和宣传周宣传教育覆盖的主要行为领域为城市居民的日常出行交通消费"
            "行为，重点引导公众在通勤、购物、休闲等日常出行中优先选择公共交通"
            "（公交车、轨道交通）、骑行和步行等绿色出行方式，减少私家车依赖，降低"
            "交通出行碳排放。活动通过倡导和信息传播影响出行消费决策。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）每年9月为绿色出行宣传月，9月16日至22日为公交出行宣传周；"
            "2）交通运输部牵头会同多部门联合印发年度活动通知；3）围绕" + LQ +
            "优选公交 绿色出行" + RQ + "理念开展公益宣传、公众参与、适老化无障碍"
            "服务提升和关爱司乘人员等活动；4）活动结束后各地报送总结至交通运输部；"
            "5）活动为宣传教育性质，不设强制性合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "以《国务院关于城市优先发展公共交通的指导意见》（国发〔2012〕64号）"
            "为政策基础；与公交都市创建、城市公共交通发展规划、新能源公交车推广"
            "应用等政策协同；与全国低碳日、全国节能宣传周等主题宣传教育活动共同"
            "构成绿色低碳出行宣传矩阵。"
        ),
        resp_info_capture=(
            "交通运输部（运输服务司）牵头会同公安部、民政部、国管局、全国总工会、"
            "共青团中央、中国残联联合制发年度活动通知。"
        ),
        info_transmission=(
            "交通运输部等部门通过通知和门户网站公开发布年度活动方案（政府公开"
            "发布）；宣传教育内容通过传统媒体、新媒体、公共交通车载媒体和站台"
            "广告、社区宣传等渠道传播。"
        ),
        info_frequency="每年一次（绿色出行宣传月为每年9月，公交出行宣传周为每年9月16日至22日）。",
        info_public=(
            "是（公开）。绿色出行宣传月和公交出行宣传周活动通知和内容通过政府网站"
            "和各类媒体渠道向社会公开。"
        ),
        label_type="N/A",
        monitoring="无合规监测",
        enforcement="无合规执行",
        promotion="其他激励或支持",
        capacity_building=(
            "交通运输部等牵头部门制作绿色出行公益宣传海报和微视频并向社会征集和"
            "展播宣传作品；通过媒体宣传、乘车优惠体验、碳积分/碳普惠活动、知识竞赛"
            "等形式普及公交优先和绿色出行理念；组织提升适老化无障碍出行服务体验"
            "活动；开展安全文明绿色出行和关爱公交司乘人员活动；各地方结合当地实际"
            "组织公众参与活动。"
        ),
        ghg_abs=(
            "N/A（本工具为公众宣传教育活动，通过引导公众选择公共交通和绿色出行方式"
            "间接减少交通碳排放，无直接可量化的排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接宣传教育工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="H49",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="能源消耗减少；空气污染物减排；公众健康；绿色产业发展",
        legal_name=(
            "交通运输部办公厅 公安部办公厅 民政部办公厅 国家机关事务管理局办公室 "
            "中华全国总工会办公厅 共青团中央办公厅 中国残疾人联合会办公厅关于组织"
            "开展2025年绿色出行宣传月和公交出行宣传周活动的通知"
        ),
        legal_url=(
            "https://xxgk.mot.gov.cn/2020/jigou/ysfws/202508/t20250828_4175597.html"
        ),
        other_links=(
            "https://xxgk.mot.gov.cn/jigou/ysfws/202006/"
            "t20200623_3315967.html"
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
