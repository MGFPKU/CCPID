#!/usr/bin/env python3
"""Insert three new Information instruments:
   - CHNCELELPI01S000 (China Energy Label — products and appliances)
   - CHNCELELBI01S000 (Civil Building Energy Efficiency Evaluation Label)
   - CHNCELELVI01S000 (Light-duty Vehicle Energy Consumption Label)
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_information_instruments.csv"

# 57-column CN template header for Information instruments (matches xlsx)
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
    # ============================================================
    # ELP01 — China Energy Label (products and appliances)
    # ============================================================
    make_row(
        pid="CHNCELELPI01S000",
        group_cn="比较性能效标签",
        approach_cn="产品和电器能效标签",
        sector="工业；建筑；能源",
        subsector="家用电器制造；工业设备制造；办公设备制造；照明设备制造",
        name_cn="能源效率标识",
        name_en="China Energy Label",
        description=(
            "中国能源效率标识制度（China Energy Label, CEL）依据《节约能源法》"
            "建立，对节能潜力大、使用面广的用能产品实行统一的能效标识制度。国家"
            "制定并公布《中华人民共和国实行能源效率标识的产品目录》，列入目录的"
            "产品生产者、进口商须在产品或最小包装的明显部位标注统一格式的能效标识，"
            "标明能效等级、能效指标及依据的强制性国家标准编号。标识采用1-5级等级"
            "制，1级为最高能效。2005年3月1日起实施。2016年6月1日修订版施行，新增"
            "能效信息码（二维码）、网络销售标识展示要求和信用惩戒机制。截至2016年"
            "已发布12批目录，覆盖家用电器、办公及电子设备、工业设备、照明设备和"
            "商用设备5大领域33类产品，备案企业超过9000家，备案型号超过61万个，"
            "累计节电超过4000亿度。"
        ),
        objective="节能降耗；信息透明；绿色消费引导",
        mitigation="间接",
        channel="需求侧",
        adoption="13/08/2004",
        effective="01/03/2005",
        revision="29/02/2016",
        revision_detail=(
            "首次制定于2004年8月13日（国家发展改革委、国家质检总局第17号令），"
            "2005年3月1日实施。2016年2月29日修订发布新版《能源效率标识管理办法》"
            "（第35号令），2016年6月1日施行，新增能效信息码（二维码）、网络销售"
            "标识展示要求、信用惩戒机制，并将监管对象扩展至网络商品经营者和第三方"
            "交易平台。"
        ),
        status="生效",
        admin_authorities=(
            "国家发展和改革委员会；国家市场监督管理总局；"
            "中国标准化研究院（授权备案机构）"
        ),
        asset="列入目录的用能产品",
        asset_status="既有",
        asset_detail=(
            "由国家发展改革委、市场监管总局制定并公布《中华人民共和国实行能源"
            "效率标识的产品目录》，分批发布。截至2016年共12批33类产品，覆盖家用"
            "电器（电冰箱、房间空调器、洗衣机、电热水器、电磁炉、电饭锅、微波炉"
            "等）、办公及电子设备（计算机显示器、复印机、打印机、投影机等）、工业"
            "设备（电动机、变压器、通风机、空压机、冷水机组等）、照明设备（荧光灯、"
            "LED灯、高压钠灯等）和商用设备（商用制冷设备、多联式空调热泵机组等）。"
        ),
        agent="企业",
        agent_detail=(
            "列入目录的用能产品的生产者、进口商和销售者（含网络交易经营者）。"
            "生产者/进口商须在上市前向中国标准化研究院备案能效标识及检测报告；"
            "销售者（含网络平台内经营者）须保证所售产品标识合规并在产品信息展示"
            "主页面醒目位置展示能效标识；第三方交易平台须督促平台内经营者履行标识义务。"
        ),
        activity="生产；进口；销售",
        activity_detail=(
            "用能产品的生产、进口和销售活动。生产者负责检测产品能效、备案标识、"
            "在产品或最小包装的明显部位标注能效标识；网络销售者须在产品信息展示"
            "主页面醒目位置展示能效标识；第三方交易平台须对平台内经营者履行标识"
            "义务进行督促。列入国家能效\"领跑者\"目录的产品须在标识中体现领跑者信息。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）列入目录的用能产品须标注统一格式的\"中国能效标识\"（China Energy "
            "Label），标识须包含生产者名称/规格型号、能效等级（1-5级，1级最高）、"
            "能效指标、依据的强制性国家标准编号和能效信息码（二维码）；2）生产者/"
            "进口商须在产品上市前向中国标准化研究院备案能效标识及能效检测报告，产品"
            "能效须经国家认可的第三方检测机构或符合资质的企业自有实验室检测确定；"
            "3）在网络交易产品信息展示主页面醒目位置展示能效标识；4）列入国家能效"
            "\"领跑者\"目录的产品须在标识中体现领跑者信息。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与能效强制性国家标准（MEPS）联动：产品能效等级划分以对应产品的强制性"
            "能效标准（如GB 12021系列、GB 18613、GB 21455等）为依据，标识中的能效"
            "指标直接引用标准限值。与能效\"领跑者\"制度联动：列入领跑者目录的产品须"
            "在标识中体现相关信息。与绿色产品认证和政府绿色采购联动：高能效等级产品"
            "优先纳入政府采购节能产品清单。"
        ),
        resp_info_capture=(
            "生产者/进口商自行或委托第三方检测机构检测确定产品能效等级，向中国标准化"
            "研究院备案并提供检测报告。中国标准化研究院负责能效标识备案信息系统的管理"
            "和维护。"
        ),
        info_transmission=(
            "产品实物或最小包装上粘贴/印刷能效标识（物理载体）；网络销售须在产品"
            "信息展示主页面醒目位置展示标识图像或包含能效信息码（电子载体）；备案"
            "信息在中国能效标识网公开（网络公示）。"
        ),
        info_frequency="一次性（产品上市前备案）；产品型号或能效信息变更时须重新备案；标识在产品上持续展示至最终销售。",
        info_public=(
            "是。中国能效标识网（www.energylabel.com.cn）公开备案产品的能效标识"
            "信息，消费者可在线查询和验证。市场监管部门定期公布能效标识监督抽查结果。"
        ),
        label_type="比较性标签（1-5级能效等级，等级制，含能效信息码/二维码）",
        monitoring="政府机构开展的监督检查",
        enforcement="行政处罚；罚款；责令整改；信用惩戒",
        promotion="税收优惠；财政补贴",
        capacity_building=(
            "结合全国节能宣传周等开展能效标识宣传和消费者教育，提高公众高效用能意识；"
            "对企业和检测机构开展能效标识技术培训。"
        ),
        ghg_abs="N/A",
        ghg_pct="N/A",
        isic="C27; C28; G47",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="能效提升；能源消耗减少；绿色消费引导；技术创新",
        legal_name="能源效率标识管理办法（国家发展改革委、国家质检总局第35号令，2016年修订）",
        legal_url="https://www.gov.cn/gongbao/content/2016/content_5074057.htm",
        other_links="https://www.energylabel.com.cn",
    ),

    # ============================================================
    # ELB01 — Civil Building Energy Efficiency Evaluation Label
    # ============================================================
    make_row(
        pid="CHNCELELBI01S000",
        group_cn="比较性能效标签",
        approach_cn="建筑能效标签",
        sector="建筑",
        subsector="房屋建筑工程建筑",
        name_cn="民用建筑能效测评标识",
        name_en="Civil Building Energy Efficiency Evaluation and Labeling",
        description=(
            "民用建筑能效测评标识制度由住房和城乡建设部于2008年以建科[2008]80号"
            "通知试行，依据《民用建筑能效测评标识管理暂行办法》和《民用建筑能效"
            "测评标识技术导则》实施。该制度要求四类民用建筑须进行能效测评并标识："
            "（1）新建（改扩建）国家机关办公建筑和大型公共建筑（单体建筑面积≥2万"
            "平方米）；（2）实施节能综合改造并申请财政支持的国家机关办公建筑和大型"
            "公共建筑；（3）国家级或省级节能示范工程建筑；（4）申请绿色建筑评价标识"
            "的建筑。测评内容包括建筑能源消耗量及用能系统效率等性能指标的计算和"
            "检测。能效等级按基础项节能率划分为五个星级（★至★★★★★），标识分两阶段"
            "实施：竣工验收后依据理论值核发标识（有效期1年），投入运行满一年后依据"
            "实测值更新标识（有效期5年）。测评机构按国家和省两级设置，须经住房城乡"
            "建设主管部门认定。"
        ),
        objective="建筑节能；信息透明；绿色建筑推广",
        mitigation="间接",
        channel="需求侧",
        adoption="28/04/2008",
        effective="28/04/2008",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "住房和城乡建设部；省级住房城乡建设主管部门；"
            "国家和省级建筑能效测评机构"
        ),
        asset="民用建筑",
        asset_status="既有",
        asset_detail=(
            "强制测评范围：（1）新建（改扩建）国家机关办公建筑和大型公共建筑"
            "（单体建筑面积≥2万平方米）；（2）实施节能综合改造并申请财政支持的国家"
            "机关办公建筑和大型公共建筑；（3）国家级或省级节能示范工程建筑；（4）申请"
            "绿色建筑评价标识的建筑。测评对象为建筑整体，涵盖围护结构、供暖通风空调、"
            "照明、热水供应等用能系统。"
        ),
        agent="企业",
        agent_detail=(
            "建设单位（开发商）负责委托测评机构进行能效测评并申请标识；建筑产权"
            "所有人负责运行阶段实测值标识的申请和维护；建筑设计、施工和物业管理单位"
            "分别在设计、施工建造和运行阶段配合测评工作。"
        ),
        activity="设计；建造；运行",
        activity_detail=(
            "建筑的设计、施工建造和运行阶段均涉及能效测评标识活动。设计阶段进行能效"
            "预评估；竣工验收后进行理论值测评并核发标识；建筑投入运行满一年后进行实测"
            "值测评并更新标识。测评机构按照《民用建筑能效测评标识技术导则》进行计算和"
            "必要的现场检测。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）上述四类民用建筑须委托经住房城乡建设主管部门认定的国家或省级建筑能效"
            "测评机构进行测评；2）测评机构依据《民用建筑能效测评标识技术导则》（建科"
            "[2008]118号）进行计算和检测，确定能效等级（★至★★★★★，五星为最高）；"
            "3）竣工验收后核发理论值标识（有效期1年），运行满一年后更新为实测值标识"
            "（有效期5年）；4）测评结果和标识须在建筑入口或显著位置公示；5）建筑未按"
            "规定进行能效测评标识的，不予通过竣工验收备案。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与建筑节能强制性标准（GB 55015-2021《建筑节能与可再生能源利用通用规范》"
            "等）联动：建筑节能率计算以强制性通用规范和设计标准为基准，标识等级"
            "（星级）反映建筑实际能效高于强制性标准基准的幅度。与绿色建筑评价标识联动"
            "：申请绿色建筑标识须以能效测评标识为前提。与建筑能耗统计、能源审计、能效"
            "公示制度联动：运行阶段的能耗数据为实测值标识更新提供依据。"
        ),
        resp_info_capture=(
            "建设单位/产权所有人委托经住房城乡建设主管部门认定的建筑能效测评机构"
            "进行测评；测评机构依据技术导则进行计算和必要的现场检测，向主管部门提交"
            "测评报告；主管部门审核后核发标识。"
        ),
        info_transmission=(
            "能效标识以星级证书和标识牌形式在建筑入口或显著位置明示（物理载体）；"
            "测评结果纳入建筑节能监管信息平台和建筑能耗公示系统（网络公示）。"
        ),
        info_frequency="理论值标识：竣工验收后一次性核发（有效期1年）；实测值标识：运行满一年后一次性更新（有效期5年）；到期后须重新测评换发。",
        info_public=(
            "是。测评结果和标识信息通过建筑节能监管信息平台和建筑能耗公示系统"
            "向公众公开。标识牌在建筑入口或显著位置公示，供社会公众查看。"
        ),
        label_type="比较性标签（1-5星级，★至★★★★★，基于建筑节能率高于强制性标准基准的幅度）",
        monitoring="政府机构开展的监督检查",
        enforcement="行政处罚；责令整改；取消测评机构资格",
        promotion="N/A",
        capacity_building=(
            "组织开展建筑能效测评技术培训，支持国家和省级建筑能效测评机构的认定和能力"
            "建设；结合绿色建筑推广开展建筑能效标识宣传。"
        ),
        ghg_abs="N/A",
        ghg_pct="N/A",
        isic="F41",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="建筑领域节能；能源消耗减少；绿色建筑产业发展",
        legal_name="关于试行民用建筑能效测评标识制度的通知（建科[2008]80号）",
        legal_url="https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2008/art_17339_167570.html",
        other_links="民用建筑节能条例（国务院令第530号）：https://www.gov.cn/zhengce/content/2008-08/08/content_4927.htm",
    ),

    # ============================================================
    # ELV01 — Light-duty Vehicle Energy Consumption Label
    # ============================================================
    make_row(
        pid="CHNCELELVI01S000",
        group_cn="比较性能效标签",
        approach_cn="车辆能效标签",
        sector="交通",
        subsector="道路运输",
        name_cn="轻型汽车能源消耗量标识",
        name_en="Light-duty Vehicle Energy Consumption Label",
        description=(
            "轻型汽车能源消耗量标识制度由中国强制性国家标准和工信部管理规定"
            "共同建立。GB 22757-2008《轻型汽车燃料消耗量标识》（强制性国家标准）"
            "于2008年12月31日发布，2009年7月1日实施。工业和信息化部于2009年7月"
            "31日发布《轻型汽车燃料消耗量标示管理规定》（工装[2009]第50号），自"
            "2010年1月1日起施行。适用于最大设计总质量不超过3500kg的M1类（乘用车）、"
            "M2类（小型客车）和N1类（轻型货车）车辆。新车出厂销售时必须在车辆内部"
            "侧车窗或风挡玻璃上粘贴统一格式的《汽车燃料消耗量标识》（现行标准更名"
            "为《汽车能源消耗量标识》），标明生产企业、车辆型号、发动机排量和功率、"
            "燃料类型、变速器类型、驱动型式、整备质量和最大设计总质量、市区/市郊/"
            "综合燃料消耗量（L/100km）、适用的燃料消耗量限值标准及限值、以及标识"
            "燃料消耗量与实际燃料消耗量差别的说明。油耗数据须由工信部指定检测机构"
            "按GB/T 19233标准检测确认，标识样本须在车型上市前报工信部备案。"
            "GB 22757-2008于2018年1月1日废止，由GB 22757.1-2017《轻型汽车能源"
            "消耗量标识 第1部分：汽油和柴油汽车》替代，将\"燃料消耗量\"更新为\"能源"
            "消耗量\"，标准体系扩展至新能源车型。"
        ),
        objective="引导高效节能汽车消费；信息透明",
        mitigation="间接",
        channel="需求侧",
        adoption="31/12/2008",
        effective="01/01/2010",
        revision="2017",
        revision_detail=(
            "首次制定于2008年12月31日（GB 22757-2008），2009年7月1日实施。2009年"
            "7月31日工信部发布《轻型汽车燃料消耗量标示管理规定》（工装[2009]第50号），"
            "自2010年1月1日起施行。2017年发布GB 22757.1-2017《轻型汽车能源消耗量标识 "
            "第1部分：汽油和柴油汽车》，替代GB 22757-2008（2018年1月1日起实施），将标"
            "准名称中的\"燃料消耗量\"更新为\"能源消耗量\"，扩充标识内容要求，并扩展标准"
            "体系至可外接充电式混合动力电动汽车等新能源车型（GB 22757.2）。"
        ),
        status="生效",
        admin_authorities=(
            "工业和信息化部；国家市场监督管理总局；"
            "中国汽车技术研究中心（技术支撑单位）"
        ),
        asset="轻型汽车（M1、M2、N1类，总质量≤3500kg）",
        asset_status="既有",
        asset_detail=(
            "适用于最大设计总质量不超过3500kg的M1类（乘用车，座位数≤9座）、M2类"
            "（小型客车，座位数>9座且总质量≤5吨）和N1类（轻型货车，总质量≤3.5吨）"
            "车辆。早期GB 22757-2008适用于燃用汽油或柴油燃料的车辆，不适用于混合动力"
            "电动汽车；GB 22757.1-2017（现有标准）已将适用范围扩展至可外接充电式混合"
            "动力电动汽车（PHEV）等新能源车型。"
        ),
        agent="企业",
        agent_detail=(
            "汽车生产企业（进口商）负责委托检测机构进行油耗/能耗检测、在车型上市前"
            "将标识样本报工信部备案，并在每辆出厂新车上粘贴标识；汽车经销商（销售者）"
            "须确保所售车辆标识完整、粘贴规范且在消费者可见位置。"
        ),
        activity="生产；进口；销售",
        activity_detail=(
            "汽车生产、进口和销售环节的能源消耗量标识活动。生产企业在车型上市前委托"
            "工信部指定检测机构按GB/T 19233标准检测确定油耗/能耗数据→将标识样本及"
            "检测报告报工信部备案→按备案格式印制标识并粘贴于每辆出厂新车→工信部通过"
            "官方网站公布车型油耗/能耗数据。销售环节须保持标识完整清晰。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）新车出厂销售时必须在车辆内部侧车窗或风挡玻璃上粘贴《汽车能源消耗量"
            "标识》，粘贴位置内容朝外便于车外阅读，不对驾驶员视野构成影响；2）标识"
            "须包含以下信息：生产企业名称、车辆型号、发动机型号/排量/额定功率、燃料"
            "类型、变速器类型、驱动型式、整备质量与最大设计总质量、市区/市郊/综合燃料"
            "消耗量（L/100km）、适用的燃料消耗量限值标准及各阶段限值实施日期和对应"
            "限值、标识燃料消耗量与实际燃料消耗量差别的说明、标识启用日期及政府主管"
            "部门规定的其他信息；3）油耗/能耗数据须由工信部指定检测机构按GB/T 19233"
            "标准检测确认；4）标识样本须在车型上市销售前报工信部备案。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        instrument_linkage=(
            "与乘用车燃料消耗量限值标准（GB 19578等FEC标准）联动：标识中须标明适用"
            "的限值标准及各阶段限值，消费者可直接对比标识值与限值。与乘用车双积分"
            "管理（CAFC/NEV）联动：标识中的燃料消耗量数据为CAFC核算提供车型基础数据。"
            "与工信部\"汽车燃料消耗量通告\"公示制度联动：标识制度提供车型数据，公示"
            "制度向社会公开发布，共同构成汽车能耗信息透明体系。"
        ),
        resp_info_capture=(
            "汽车生产企业（进口商）委托工信部指定检测机构（如中国汽车技术研究中心）"
            "按GB/T 19233《轻型汽车燃料消耗量试验方法》检测确定油耗/能耗数据→车型"
            "上市前将标识样本和检测报告报工业和信息化部备案→工信部审核备案→生产企业"
            "按备案格式印制并粘贴标识。"
        ),
        info_transmission=(
            "标识以物理标签形式粘贴于每辆出厂新车的侧车窗或风挡玻璃上（面向车外，"
            "便于消费者在车外阅读）；工信部在官方网站（www.miit.gov.cn）定期发布"
            "\"汽车燃料消耗量通告\"，公布各车型油耗数据（网络公示）。"
        ),
        info_frequency="一次性（车型上市前备案）。车型能源消耗量数据变更时须重新备案。每辆新车出厂时均须粘贴标识，直至销售给最终消费者。工信部定期（通常每年数次）发布车型油耗通告。",
        info_public=(
            "是。工信部定期在官方网站公布所有备案车型的燃料消耗量/能源消耗量数据，"
            "供社会公众查询和比较；消费者购车时可直接在车辆侧车窗或风挡玻璃上查看"
            "粘贴的标识。"
        ),
        label_type="比较性标签（含综合、市区、市郊燃料消耗量数值及适用的强制性限值标准，便于消费者横向比较）",
        monitoring="政府机构开展的监督检查",
        enforcement="行政处罚；责令整改",
        promotion="N/A",
        capacity_building=(
            "通过工信部\"汽车燃料消耗量通告\"定期公开发布车型油耗数据，引导消费者选购"
            "节能汽车，促进汽车生产企业开发高效节能车型。结合节能宣传周等活动开展"
            "汽车节能消费宣传。"
        ),
        ghg_abs="N/A",
        ghg_pct="N/A",
        isic="C29; G45",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="绿色消费引导；交通运输领域节能；能源消耗减少",
        legal_name="轻型汽车燃料消耗量标示管理规定（工装[2009]第50号）；GB 22757.1-2017《轻型汽车能源消耗量标识 第1部分：汽油和柴油汽车》",
        legal_url="https://www.miit.gov.cn/jgsj/zbys/qcgy/art/2020/art_3fa9c86d1d6d4339a3dca85de7cdacfa.html",
        other_links="https://yhgscx.miit.gov.cn/fuel-consumption-web/",
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

        # Sort by approach code, insert in order
        new_code = pid[6:9]  # ELP, ELB, ELV

        insert_pos = None
        for i, r in enumerate(data):
            if r[2] != "比较性能效标签":
                continue
            existing_code = r[0][6:9]
            if existing_code > new_code:
                insert_pos = i
                break

        if insert_pos is None:
            for i in range(len(data) - 1, -1, -1):
                if data[i][2] == "比较性能效标签":
                    insert_pos = i + 1
                    break

        if insert_pos is None:
            insert_pos = len(data)

        data.insert(insert_pos, list(row))
        inserted += 1
        print(f"  Inserted {pid} ({new_code}) at data index {insert_pos}")

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted, {updated} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
