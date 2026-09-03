#!/usr/bin/env python3
"""Insert three new Information instruments (Reporting requirements group,
   green finance data collection):
   - CHNREPGFSI01S000 (Green Loan Special Statistics System)
   - CHNREPGFSI02S000 (Green Insurance Business Statistics System)
   - CHNREPGFEI01S000 (Green Finance Evaluation Scheme for Banking
     Financial Institutions)
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
        pid="CHNREPGFSI01S000",
        group_cn="报告与披露要求",
        approach_cn="绿色金融统计",
        sector="跨部门",
        subsector="N/A",
        name_cn="绿色贷款专项统计制度",
        name_en="Green Loan Special Statistics System",
        policy_package="关于构建绿色金融体系的指导意见（银发〔2016〕228号）",
        description=(
            "绿色贷款专项统计制度是中国人民银行建立的绿色金融统计制度，要求"
            "银行业金融机构按照统一的统计口径和分类标准，定期报送绿色贷款的"
            "余额、投向、质量等数据。制度覆盖境内各类提供贷款业务的银行业金融"
            "机构，统计范围包括节能环保、清洁生产、清洁能源、生态环境、基础设施"
            "绿色升级、绿色服务等绿色产业领域的贷款，以及支持有减排效应项目和"
            "服务的贷款。制度依据绿色产业指导目录和绿色贷款统计口径，将绿色贷款"
            "按用途（项目/服务）、投向行业、贷款质量（正常/关注/不良）等维度"
            "分类统计。制度建设可追溯至2013年原中国银监会《关于报送绿色信贷"
            "统计表的通知》（银监办发〔2013〕185号），首次建立绿色信贷季度统计；"
            "2018年以来中国人民银行统筹推进绿色贷款专项统计；2019年12月27日"
            "《中国人民银行关于修订绿色贷款专项统计制度的通知》（银发〔2019〕"
            "326号）对统计制度进行修订完善，统一绿色贷款统计口径、扩展统计维度"
            "并细化报送要求。通过绿色贷款专项统计掌握金融机构支持绿色发展的信贷"
            "投放情况，为绿色金融政策制定、结构性货币政策工具（如碳减排支持工具）"
            "运用、宏观审慎评估（MPA）和银行业金融机构绿色金融评价提供数据基础。"
        ),
        objective=(
            "全面掌握银行业金融机构绿色贷款投放规模、投向和质量；为绿色金融"
            "政策制定和评估提供数据支撑；支持结构性货币政策工具和宏观审慎管理；"
            "引导金融资源向绿色低碳领域配置"
        ),
        mitigation="间接",
        channel="环境",
        adoption="04/07/2013",
        effective="04/07/2013",
        revision="27/12/2019",
        revision_detail=(
            "制度建设可追溯至2013年7月4日原中国银监会办公厅《关于报送绿色信贷"
            "统计表的通知》（银监办发〔2013〕185号），首次建立绿色信贷季度统计"
            "报送。2018年以来中国人民银行统筹推进绿色贷款专项统计工作。2019年"
            "12月27日《中国人民银行关于修订绿色贷款专项统计制度的通知》（银发"
            "〔2019〕326号）对统计制度进行修订，统一绿色贷款统计口径、按绿色产业"
            "分类扩展统计维度、细化数据报送要求。2025年配合《绿色金融支持项目"
            "目录（2025年版）》的发布，绿色贷款统计口径进一步与统一绿色金融标准"
            "衔接。"
        ),
        status="生效",
        admin_authorities="中国人民银行；中国人民银行分支机构",
        asset="绿色贷款业务",
        asset_status="N/A",
        asset_detail=(
            "本工具为绿色金融统计制度，统计对象为银行业金融机构的绿色贷款业务"
            "（包括节能环保、清洁生产、清洁能源、生态环境、基础设施绿色升级、"
            "绿色服务等绿色产业领域的贷款及有减排效应的项目和服务贷款），不直接"
            "监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "境内银行业金融机构，包括开发性银行、政策性银行、国有商业银行、"
            "股份制商业银行、城市商业银行、农村商业银行、外资银行等各类提供贷款"
            "业务的银行业金融机构法人及其分支机构。银行业金融机构须按照绿色贷款"
            "专项统计制度的统计口径和分类标准，准确统计和报送绿色贷款相关数据，"
            "对数据的真实性、准确性和完整性负责。"
        ),
        activity="注册、许可及行政管理",
        activity_detail=(
            "银行业金融机构的绿色贷款统计报送活动。金融机构按照绿色贷款专项统计"
            "口径和分类标准核算本机构绿色贷款数据→通过金融统计监测管理信息系统"
            "等渠道按季度报送→中国人民银行及其分支机构审核、汇总并开展数据质量"
            "核查。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）银行业金融机构须按照绿色贷款专项统计制度规定的统计口径、分类"
            "标准和报表格式，统计本机构绿色贷款的余额、发放额、投向行业、贷款"
            "用途（项目/服务）和贷款质量等数据；2）绿色贷款按绿色产业分类（节能"
            "环保、清洁生产、清洁能源、生态环境、基础设施绿色升级、绿色服务等）"
            "进行分类统计；3）统计数据按季度报送至中国人民银行（通过金融统计"
            "监测管理信息系统等报送渠道）；4）银行业金融机构对报送数据的真实性、"
            "准确性、完整性和及时性负责；5）中国人民银行及其分支机构对绿色贷款"
            "统计数据进行审核、汇总、分析并开展数据质量核查。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与银行业金融机构绿色金融评价方案（GFE）深度联动：绿色贷款专项统计"
            "数据是绿色金融业绩评价定量指标的核心数据来源。与碳减排支持工具等"
            "结构性货币政策工具联动：绿色贷款统计为货币政策工具的额度测算和效果"
            "评估提供依据。与宏观审慎评估（MPA）联动：绿色信贷情况纳入宏观审慎"
            "管理。与绿色金融标准体系联动：统计口径依据绿色产业指导目录和绿色"
            "金融支持项目目录。"
        ),
        resp_info_capture=(
            "银行业金融机构自行按照绿色贷款专项统计制度的统计口径和分类标准，"
            "采集、核算和填报本机构绿色贷款统计数据；中国人民银行及其分支机构"
            "负责数据审核、汇总和质量核查。"
        ),
        info_transmission=(
            "银行业金融机构通过中国人民银行金融统计监测管理信息系统等报送渠道"
            "在线报送绿色贷款专项统计报表（网络报送）。"
        ),
        info_frequency=(
            "按季度报送（每季度末后规定期限内报送上一季度绿色贷款统计数据）。"
        ),
        info_public=(
            "是（部分公开）。中国人民银行定期通过《金融机构贷款投向统计报告》等"
            "发布绿色贷款总量、增速和结构等汇总统计数据；单个金融机构的明细数据"
            "主要服务于监管和政策制定，不对外公开。"
        ),
        label_type="N/A",
        monitoring="政府机构开展的监督检查",
        enforcement="责令改正；通报",
        promotion="其他激励或支持",
        capacity_building=(
            "中国人民银行发布绿色贷款专项统计制度及统计口径说明、填报指南等配套"
            "文件；组织银行业金融机构开展绿色贷款统计业务培训；建设和维护金融"
            "统计监测管理信息系统绿色贷款统计模块，提供在线报送和数据校验支持。"
        ),
        ghg_abs=(
            "N/A（本工具为绿色金融统计制度，通过引导信贷资源配置间接支持绿色"
            "低碳发展，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接金融工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="K64",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新；污染防治",
        legal_name="中国人民银行关于修订绿色贷款专项统计制度的通知",
        legal_url="http://www.gzgfa.org.cn/Guojiazhengce-35/171.html",
        other_links="N/A",
    ),
    make_row(
        pid="CHNREPGFSI02S000",
        group_cn="报告与披露要求",
        approach_cn="绿色金融统计",
        sector="跨部门",
        subsector="N/A",
        name_cn="绿色保险业务统计制度",
        name_en="Green Insurance Business Statistics System",
        policy_package="关于构建绿色金融体系的指导意见（银发〔2016〕228号）",
        description=(
            "绿色保险业务统计制度是原中国银保监会建立的绿色金融统计制度，要求"
            "保险公司按照统一的统计口径和分类标准，定期报送绿色保险业务相关数据，"
            "系统掌握保险业服务绿色低碳发展、防范环境和气候风险的业务开展情况。"
            "制度明确了绿色保险的定义和统计范围，涵盖为环境保护、应对气候变化、"
            "节能减排、生态保护和绿色产业发展等提供风险保障和资金支持的保险业务，"
            "包括环境污染责任保险、绿色能源保险、绿色建筑保险、绿色交通保险、"
            "巨灾保险等险种。制度设置绿色保险业务统计表，包含承保件数、保险金额、"
            "保费收入、赔款支出等多项统计指标，保险公司总公司通过创新业务统计"
            "信息系统按月报送。制度由2022年11月10日《中国银保监会办公厅关于印发"
            "绿色保险业务统计制度的通知》（银保监办发〔2022〕103号）建立，是首次"
            "在全国范围内统一规范绿色保险业务统计的制度安排。通过绿色保险业务"
            "统计掌握保险业服务绿色发展的规模和结构，为绿色金融政策制定、保险"
            "监管和绿色保险产品创新提供数据基础。"
        ),
        objective=(
            "系统掌握保险业绿色保险业务开展规模、结构和赔付情况；为绿色金融和"
            "绿色保险政策制定提供数据支撑；引导保险资金和保险保障服务绿色低碳"
            "发展；提升保险业环境和气候风险管理能力"
        ),
        mitigation="间接",
        channel="环境",
        adoption="10/11/2022",
        effective="10/11/2022",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "国家金融监督管理总局（原中国银保监会）；国家金融监督管理总局派出机构"
        ),
        asset="绿色保险业务",
        asset_status="N/A",
        asset_detail=(
            "本工具为绿色金融统计制度，统计对象为保险公司的绿色保险业务（涵盖"
            "环境污染责任保险、绿色能源保险、绿色建筑保险、绿色交通保险、巨灾"
            "保险等为绿色低碳发展提供风险保障和资金支持的保险业务），不直接监管"
            "实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "境内保险公司（财产保险公司、人身保险公司等）总公司。保险公司总公司"
            "须按照绿色保险业务统计制度的统计口径和分类标准，汇总本公司系统绿色"
            "保险业务数据并统一报送，对报送数据的真实性、准确性和完整性负责。"
        ),
        activity="注册、许可及行政管理",
        activity_detail=(
            "保险公司的绿色保险业务统计报送活动。保险公司总公司按照绿色保险业务"
            "统计口径和分类标准汇总本公司系统绿色保险业务数据→通过创新业务统计"
            "信息系统按月报送→监管部门审核、汇总和分析。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）保险公司总公司须按照绿色保险业务统计制度规定的统计口径、分类"
            "标准和报表格式，统计绿色保险业务的保单件数、保险金额、保费收入、"
            "赔款支出等数据；2）绿色保险按险种和服务领域进行分类统计；3）统计"
            "数据由保险公司总公司通过创新业务统计信息系统按月报送；4）保险公司"
            "对报送数据的真实性、准确性和完整性负责；5）监管部门对绿色保险业务"
            "统计数据进行审核、汇总和分析。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与绿色金融体系建设联动：绿色保险统计是绿色金融统计监测的重要组成"
            "部分。与绿色金融标准体系联动：绿色保险统计范围依据绿色产业和绿色"
            "金融相关标准界定。与保险监管制度联动：统计数据用于保险业环境和气候"
            "风险监管及绿色保险产品创新引导。"
        ),
        resp_info_capture=(
            "保险公司总公司自行按照绿色保险业务统计制度的统计口径和分类标准，"
            "汇总本公司绿色保险业务数据并填报；国家金融监督管理总局（原中国"
            "银保监会）负责数据审核和汇总。"
        ),
        info_transmission=(
            "保险公司总公司通过创新业务统计信息系统在线报送绿色保险业务统计"
            "报表（网络报送）。"
        ),
        info_frequency=(
            "按月报送（每月规定期限内报送上月绿色保险业务统计数据）。"
        ),
        info_public=(
            "是（部分公开）。监管部门通过行业统计和相关报告发布绿色保险业务总量"
            "等汇总数据；单个保险公司的明细数据主要服务于监管，不对外公开。"
        ),
        label_type="N/A",
        monitoring="政府机构开展的监督检查",
        enforcement="责令改正；通报",
        promotion="其他激励或支持",
        capacity_building=(
            "发布绿色保险业务统计制度及统计口径、指标说明和填报指南；组织保险"
            "公司开展绿色保险业务统计培训；建设和维护创新业务统计信息系统绿色"
            "保险统计模块。"
        ),
        ghg_abs=(
            "N/A（本工具为绿色金融统计制度，通过保险保障和资金支持间接服务绿色"
            "低碳发展，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接金融工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="K65",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；污染防治；生态保护",
        legal_name="中国银保监会办公厅关于印发绿色保险业务统计制度的通知",
        legal_url=(
            "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?"
            "docId=1081137&itemId=915&generaltype=0"
        ),
        other_links="N/A",
    ),
    make_row(
        pid="CHNREPGFEI01S000",
        group_cn="报告与披露要求",
        approach_cn="绿色金融业绩评价",
        sector="跨部门",
        subsector="N/A",
        name_cn="银行业金融机构绿色金融评价方案",
        name_en="Green Finance Evaluation Scheme for Banking Financial Institutions",
        policy_package="关于构建绿色金融体系的指导意见（银发〔2016〕228号）",
        description=(
            "银行业金融机构绿色金融评价方案是中国人民银行建立的绿色金融业绩评价"
            "制度，对银行业金融机构开展绿色金融业务的情况进行定期定量和定性评价。"
            "评价对象为中国人民银行确定的银行业金融机构（法人），评价范围涵盖"
            "绿色贷款、绿色债券等绿色金融业务。评价指标体系由定量指标和定性指标"
            "两部分构成，其中定量指标权重80%（包括绿色金融业务总额占比、余额占比、"
            "余额同比增速、风险总额占比等），定性指标权重20%（包括绿色金融相关"
            "制度制定及实施、机制建设及创新等）。评价按季度开展，评价结果纳入"
            "中国人民银行金融机构评级，并作为宏观审慎评估（MPA）、结构性货币"
            "政策工具运用等的重要参考。制度可追溯至2018年7月27日《中国人民银行"
            "关于开展银行业存款类金融机构绿色信贷业绩评价的通知》（银发〔2018〕"
            "180号），建立绿色信贷业绩评价制度。2021年6月9日《中国人民银行关于"
            "印发〈银行业金融机构绿色金融评价方案〉的通知》（银发〔2021〕142号，"
            "2021年7月1日施行）对制度进行修订升级，将评价业务范围由绿色信贷"
            "扩展至绿色贷款和绿色债券，完善评价指标体系和评价流程，同时废止银发"
            "〔2018〕180号。通过绿色金融业绩评价激励约束银行业金融机构加大绿色"
            "金融供给，引导金融资源支持绿色低碳发展。"
        ),
        objective=(
            "评价银行业金融机构绿色金融业务开展情况；通过评价结果的激励约束作用"
            "引导金融机构加大绿色金融供给；推动金融资源向绿色低碳领域配置；支持"
            "宏观审慎管理和货币政策工具运用"
        ),
        mitigation="直接",
        channel="环境",
        adoption="27/07/2018",
        effective="27/07/2018",
        revision="09/06/2021",
        revision_detail=(
            "制度可追溯至2018年7月27日《中国人民银行关于开展银行业存款类金融"
            "机构绿色信贷业绩评价的通知》（银发〔2018〕180号），建立绿色信贷"
            "业绩评价制度，按季度开展评价。2021年6月9日《中国人民银行关于印发"
            "〈银行业金融机构绿色金融评价方案〉的通知》（银发〔2021〕142号，"
            "2021年7月1日施行）对制度进行修订升级：将评价业务范围由绿色信贷"
            "扩展至绿色贷款和绿色债券，重构定量（权重80%）和定性（权重20%）"
            "评价指标体系，完善评价流程和结果运用，评价结果纳入央行金融机构评级"
            "并作为宏观审慎评估（MPA）的重要参考；同时废止银发〔2018〕180号。"
        ),
        status="生效",
        admin_authorities="中国人民银行；中国人民银行分支机构",
        asset="绿色金融业务",
        asset_status="N/A",
        asset_detail=(
            "本工具为绿色金融业绩评价制度，评价对象为银行业金融机构的绿色金融"
            "业务（绿色贷款、绿色债券等），不直接监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "中国人民银行确定纳入评价范围的银行业金融机构（法人），包括开发性"
            "银行、政策性银行、国有商业银行、股份制商业银行、城市商业银行、"
            "农村商业银行等。被评价机构须按照评价方案要求配合提供绿色金融业务"
            "数据和相关材料，对所提供数据和材料的真实性、准确性负责。"
        ),
        activity="注册、许可及行政管理",
        activity_detail=(
            "中国人民银行对银行业金融机构绿色金融业务开展的业绩评价活动。中国"
            "人民银行按季度对纳入评价范围的机构开展评价→被评价机构提供绿色贷款、"
            "绿色债券等绿色金融业务数据及相关材料（数据主要来源于绿色贷款专项"
            "统计等既有统计）→中国人民银行按定量（80%）和定性（20%）指标汇总"
            "计算评价得分→形成评价结果并纳入央行金融机构评级和宏观审慎评估。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）中国人民银行按季度对纳入评价范围的银行业金融机构开展绿色金融"
            "评价；2）评价指标体系由定量指标（权重80%，包括绿色金融业务总额"
            "占比、余额占比、余额同比增速、风险总额占比等）和定性指标（权重20%，"
            "包括绿色金融相关制度制定及实施情况、机制建设及创新等）构成；3）被"
            "评价机构须按要求提供绿色贷款、绿色债券等绿色金融业务数据及相关"
            "材料；4）绿色金融业务数据主要来源于绿色贷款专项统计等既有统计制度；"
            "5）中国人民银行汇总计算评价得分并形成评价结果；6）评价结果纳入中国"
            "人民银行金融机构评级，并作为宏观审慎评估（MPA）、央行货币政策操作"
            "和相关政策的重要参考。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与绿色贷款专项统计制度（GFS）深度联动：绿色贷款专项统计数据是绿色"
            "金融评价定量指标的核心数据来源。与中国人民银行金融机构评级联动："
            "评价结果纳入央行评级。与宏观审慎评估（MPA）联动：评价结果作为MPA"
            "的重要参考。与碳减排支持工具等结构性货币政策工具联动：评价激励约束"
            "金融机构绿色金融供给。"
        ),
        resp_info_capture=(
            "被评价银行业金融机构按要求提供绿色金融业务数据和相关材料（数据"
            "主要来源于绿色贷款专项统计等既有统计）；中国人民银行及其分支机构"
            "负责数据核实、评价计算和结果形成。"
        ),
        info_transmission=(
            "被评价机构通过中国人民银行相关报送渠道提交绿色金融业务数据和评价"
            "材料（网络报送）；评价结果由中国人民银行反馈至被评价机构。"
        ),
        info_frequency=(
            "按季度开展评价（每季度评价一次）。"
        ),
        info_public=(
            "否（不公开）。绿色金融评价结果纳入中国人民银行金融机构评级，主要"
            "用于监管和政策，单个机构评价结果一般不对外公开。"
        ),
        label_type="N/A",
        monitoring="政府机构开展的监督检查",
        enforcement="责令改正；通报",
        promotion="其他激励或支持",
        capacity_building=(
            "发布《银行业金融机构绿色金融评价方案》及评价指标、评分标准和操作"
            "细则；组织被评价机构开展绿色金融评价业务培训和政策解读；通过评价"
            "结果反馈和沟通指导金融机构改进绿色金融业务。"
        ),
        ghg_abs=(
            "N/A（本工具为绿色金融业绩评价制度，通过激励约束金融机构绿色金融"
            "供给间接支持减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接金融工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="K64",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新",
        legal_name="中国人民银行关于印发《银行业金融机构绿色金融评价方案》的通知",
        legal_url="https://www.gov.cn/zhengce/zhengceku/2021-06/11/content_5616962.htm",
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
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted, {updated} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
