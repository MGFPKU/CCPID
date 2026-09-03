"""Insert Voluntary information disclosure (VID) instruments into Voluntary CN CSV.

Run from repo root:
    python scripts/_add_vol_vid.py
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_voluntary_approaches.csv"

GROUP = "自愿性信息工具"
APPROACH = "自愿性信息披露"


def make_row(pid, name_cn, name_en, sector, subsector, policy_package,
             description, objective, mitigation, channel,
             adoption, effective, revision, revision_detail, status,
             admin_authorities, asset, asset_status, asset_detail,
             agent, agent_detail, activity, activity_detail,
             intensity_val, intensity_unit, intensity_detail, req_spec,
             calc_i, calc_ii, incentives, monitoring, sanctions,
             ghg_abs, ghg_pct, isic, ghg,
             mitigation_effects, co_benefits, legal_name, legal_url, other_links):
    return [
        pid, "工具", GROUP, APPROACH, sector, subsector,
        name_cn, name_en, policy_package, description, objective,
        mitigation, channel, "中国", "国家", "N/A",
        adoption, effective, "N/A", revision, revision_detail, status,
        admin_authorities, asset, asset_status, asset_detail,
        "N/A", "N/A", agent, agent_detail, activity, activity_detail,
        intensity_val, intensity_unit, intensity_detail, req_spec,
        calc_i, calc_ii, incentives, monitoring, sanctions,
        ghg_abs, ghg_pct, isic, ghg,
        mitigation_effects, co_benefits, legal_name, legal_url, other_links,
    ]


ROWS = [
    make_row(
        pid="CHNVIIVIDI01S000",
        name_cn="企业可持续披露准则",
        name_en="Corporate Sustainability Disclosure Standards",
        sector="跨部门",
        subsector="N/A",
        policy_package="N/A",
        description=(
            "企业可持续披露准则是由财政部会同外交部、国家发展改革委、工业和信息化部、"
            "生态环境部、商务部、中国人民银行、国务院国资委、金融监管总局、中国证监会"
            "等九部门联合制定并发布的统一可持续信息披露准则体系，旨在建立国家统一的"
            "可持续信息披露基准，为企业提供标准化的可持续信息披露方法论和内容规范，"
            "提升披露信息的可比性和决策有用性。准则体系由基本准则、具体准则和应用指南"
            "三级构成，其中《企业可持续披露准则——基本准则（试行）》（财会〔2024〕17号）"
            "为体系首部文件，共六章31条，规定了可持续信息披露的基本概念、原则、方法和"
            "一般共性要求。准则借鉴国际可持续准则理事会（ISSB）S1准则的有益经验，结合"
            "中国国情，围绕治理、战略、风险和机遇管理、指标和目标四个核心要素构建披露"
            "框架。准则体系建设目标为到2027年出台基本准则和气候相关披露准则及应用指南，"
            "到2030年基本建成国家统一的可持续披露准则体系。实施策略为分步推进：从上市"
            "公司到非上市公司、从大型企业到中小企业、从定性要求到定量要求、从自愿披露"
            "到强制披露。当前阶段由企业自愿实施，不设强制合规义务和处罚。"
        ),
        objective="规范企业可持续信息披露，提高信息透明度和可比性",
        mitigation="间接",
        channel="环境",
        adoption="20/11/2024",
        effective="17/12/2024",
        revision="19/12/2025",
        revision_detail=(
            "2025年12月19日，财政部会同生态环境部、外交部、国家发展改革委、"
            "工业和信息化部、商务部、中国人民银行、国务院国资委、金融监管总局、"
            "中国证监会等9部门联合印发《企业可持续披露准则第1号——气候（试行）》"
            "（财会〔2025〕34号），作为准则体系的首个具体准则，规范企业与气候相关"
            "风险、机遇和影响的信息披露，涵盖气候相关风险和机遇的识别与评估、"
            "转型计划和气候韧性、温室气体排放等核心披露要求。该准则与ISSB的IFRS S2"
            "气候相关披露准则总体衔接，由企业自愿实施。"
        ),
        status="生效",
        admin_authorities=(
            "财政部（会计司，牵头）；外交部；国家发展和改革委员会；"
            "工业和信息化部；生态环境部；商务部；中国人民银行；"
            "国务院国有资产监督管理委员会；国家金融监督管理总局；中国证券监督管理委员会"
        ),
        asset="可持续/ESG信息（披露对象）",
        asset_status="N/A",
        asset_detail=(
            "本工具界定和覆盖的对象为企业可持续信息披露所涉及的可持续风险和机遇相关"
            "信息，涵盖治理、战略、风险和机遇管理、指标和目标四个核心披露要素。企业"
            "披露的可持续信息应涵盖其价值链范围内的可持续风险和机遇，包括气候、污染、"
            "水资源、生物多样性、循环经济等环境议题，员工权益、消费者保护、社区关系、"
            "乡村振兴等社会议题，以及商业行为等治理议题。"
        ),
        agent="企业",
        agent_detail=(
            "在中华人民共和国境内注册的企业。当前阶段由企业自愿参照准则进行可持续信息"
            "披露，未来将分步扩展至上市公司、非上市公司、大型企业和中小企业。准则不"
            "设强制性合规义务和行政处罚，企业可自主决定是否应用、应用的程度和应用的时间表。"
        ),
        activity="注册、许可及行政管理",
        activity_detail=(
            "本工具规范和引导的活动为企业参照统一准则框架进行可持续信息披露的全过程，"
            "包括：识别和评估可持续风险和机遇；确定披露范围和边界；按照治理、战略、"
            "风险和机遇管理、指标和目标四个核心要素编制可持续信息报告；确保信息满足"
            "可靠性、相关性、可比性、可验证性、可理解性和及时性等质量要求；将可持续"
            "信息与财务报表信息进行关联；以及通过年度报告、可持续发展报告或专门环境"
            "信息报告等载体对外公开披露。参与为自愿性质。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）披露信息须覆盖治理（可持续风险和机遇的治理架构）、战略（可持续风险和"
            "机遇对企业的财务影响和战略韧性）、风险和机遇管理（识别、评估、优先排序和"
            "监控流程）、指标和目标（可量化的可持续相关绩效指标和进展）四个核心要素；"
            "2）披露信息须满足可靠性、相关性、可比性、可验证性、可理解性和及时性六个"
            "信息质量要求；3）企业须披露可持续风险和机遇的当期和预期财务影响，以及战略"
            "和业务模式对可持续风险的韧性；4）披露应涵盖价值链范围内的重要可持续风险和"
            "机遇；5）企业应说明可持续信息报告与财务报表报告之间的关系和关联信息；"
            "6）当前阶段由企业自愿实施，不设强制合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "采纳准则进行可持续信息披露的企业可提升信息披露质量和国际可比性，获得投资者、"
            "债权人等利益相关方的信任；高质量可持续信息披露有助于企业获得绿色金融产品"
            "支持和ESG投资；准则与国际ISSB准则总体衔接，有助于企业应对国际可持续信息"
            "披露要求和跨境资本流动需求。"
        ),
        monitoring=(
            "当前自愿实施阶段无强制性合规监测要求。财政部将会同相关部门对准则实施情况"
            "进行跟踪评估，适时调整实施范围和强制要求。企业自愿进行的可持续信息披露可由"
            "第三方机构提供鉴证服务。"
        ),
        sanctions="N/A（自愿性披露标准，不设违规制裁。当前阶段由企业自愿实施，无强制合规义务和处罚。）",
        ghg_abs=(
            "N/A（本工具为自愿性披露准则框架，碳排放覆盖量取决于自愿采纳准则进行气候"
            "相关信息披露的企业数量和披露范围，无直接可量化的固定覆盖量）"
        ),
        ghg_pct="N/A（本工具为自愿性工具，碳排放覆盖占比取决于自愿采纳情况）",
        isic="M72",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="技术创新；绿色产业发展；能源消耗减少",
        legal_name=(
            "财政部等部门关于印发《企业可持续披露准则——基本准则（试行）》的通知"
            "（财会〔2024〕17号）"
        ),
        legal_url="http://kjs.mof.gov.cn/zhengcefabu/202412/t20241216_3949745.htm",
        other_links="https://www.casc.org.cn/2025/1225/278706.shtml",
    ),
    make_row(
        pid="CHNVIIVIDI02S000",
        name_cn="金融机构环境信息披露指南",
        name_en="Environmental Information Disclosure Guidelines for Financial Institutions",
        sector="跨部门",
        subsector="N/A",
        policy_package="N/A",
        description=(
            "金融机构环境信息披露指南是由中国人民银行制定并发布的推荐性金融行业标准"
            "（JR/T 0227—2021），为金融机构提供环境信息披露的框架性指引，引导金融机构"
            "规范开展环境信息披露。指南规定了金融机构在环境信息披露过程中应遵循的原则（真实性、及时性、"
            "一致性、连贯性）、披露形式和频次（鼓励每年至少对外披露一次，可编制专门环境"
            "信息报告、在社会责任报告中披露或在年度报告中披露），以及披露的核心内容要素："
            "年度概况、治理结构、政策制度、产品与服务创新、风险管理流程、投融资活动的"
            "环境影响、经营活动的环境影响、数据梳理校验与保护、绿色金融创新研究成果等。"
            "指南适用于在中国境内依法设立的银行、资产管理、保险、信托、期货、证券等"
            "金融机构。标准为推荐性标准，金融机构自愿采纳，不设强制合规义务和处罚。"
        ),
        objective="规范金融机构环境信息披露，提升金融领域环境信息透明度",
        mitigation="间接",
        channel="环境",
        adoption="22/07/2021",
        effective="22/07/2021",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "中国人民银行（研究局、科技司）；全国金融标准化技术委员会（SAC/TC 180）"
        ),
        asset="环境信息（披露对象）",
        asset_status="N/A",
        asset_detail=(
            "本工具界定和覆盖的对象为金融机构在经营活动和投融资活动中涉及的环境信息，"
            "具体包括：金融机构绿色金融年度概况（绿色金融发展战略、目标及年度成效）；"
            "环境相关治理结构（董事会及高管层对环境议题的监督职责）；环境相关政策制度"
            "（绿色金融相关内部制度和流程）；绿色金融产品与服务创新（绿色信贷、绿色债券、"
            "绿色保险、ESG投资等产品类型和规模）；环境风险管理流程（环境风险识别、评估、"
            "监测和应对机制）；投融资活动的环境影响（投融资组合的环境绩效指标如碳排放"
            "强度或减排量）；经营活动的环境影响（机构自身能源消耗、碳排放和资源使用等"
            "绿色运营指标）；以及数据梳理、校验与保护安排。"
        ),
        agent="企业",
        agent_detail=(
            "在中华人民共和国境内依法设立的金融机构，包括银行机构（商业银行、政策性银行、"
            "农村合作银行、农村信用社等）、资产管理公司、保险公司、信托公司、期货公司、"
            "证券公司等。标准为推荐性行业标准，金融机构自愿采纳并根据自身实际情况确定"
            "披露程度和范围。"
        ),
        activity="注册、许可及行政管理",
        activity_detail=(
            "本工具规范和引导的活动为金融机构参照指南进行环境信息披露的全过程，包括："
            "建立环境信息披露治理架构和责任分工；识别和确定环境信息披露的范围和内容要素；"
            "建立环境信息数据收集、计量、校验和管理系统；选择适当的披露形式和载体"
            "（专门环境信息报告、社会责任报告或年度报告）；按照规定要素编制环境信息"
            "披露内容；以及通过公开发布渠道对外披露并接受社会监督。金融机构可自愿选择"
            "披露形式、频次和范围，鼓励每年至少对外披露一次。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）披露应遵循真实性、及时性、一致性、连贯性四项原则；2）披露内容应涵盖"
            "年度概况、治理结构、政策制度、产品与服务创新、风险管理流程、投融资活动的"
            "环境影响、经营活动的环境影响、数据梳理校验与保护、绿色金融创新研究成果等"
            "核心要素；3）披露形式可采用专门环境信息报告、社会责任报告中披露或年度报告"
            "中披露等形式；4）鼓励每年至少对外披露一次；5）金融机构应建立数据收集、"
            "计量、校验和管理机制，确保披露信息准确可靠；6）标准为推荐性行业标准，"
            "金融机构自愿采纳，不设强制合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "采纳指南进行环境信息披露的金融机构可提升自身环境风险管理和绿色金融发展水平，"
            "增强市场透明度和利益相关方信任；高质量环境信息披露有助于金融机构在绿色金融"
            "业绩评价中获得良好表现，并满足投资者和评级机构对环境信息的需求；绿色金融"
            "改革创新试验区等地区鼓励辖内金融机构率先实现环境信息全披露。"
        ),
        monitoring=(
            "当前自愿采纳阶段无强制性合规监测要求。中国人民银行及相关金融监管部门对金融"
            "机构环境信息披露情况进行跟踪了解，绿色金融改革创新试验区等部分地区对辖内"
            "金融机构环境信息披露比例和披露质量进行监测和评估。金融机构可聘请第三方机构"
            "对环境信息进行独立鉴证。"
        ),
        sanctions="N/A（推荐性行业标准，不设违规制裁。金融机构自愿采纳，无强制合规义务和处罚。）",
        ghg_abs=(
            "N/A（本工具为自愿性披露指南，碳排放覆盖量取决于金融机构自愿采纳指南进行"
            "环境信息（包括投融资组合碳排放）披露的覆盖范围和披露深度，无直接可量化的"
            "固定覆盖量）"
        ),
        ghg_pct="N/A（本工具为自愿性工具，碳排放覆盖占比取决于自愿采纳情况）",
        isic="K64",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；技术创新；能源消耗减少；污染防治",
        legal_name="中国人民银行《金融机构环境信息披露指南》（JR/T 0227—2021）",
        legal_url="https://std.samr.gov.cn/hb/search/stdHBDetailed?id=C8CBBCAE2F3D5981E05397BE0A0AB29C",
        other_links="N/A",
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
        if len(row) != 50:
            print(f"ERROR: {row[0]} has {len(row)} columns, expected 50")
            return 1

    existing = _load_rows(CSV_PATH)
    header, data = existing[0], existing[1:]

    inserted = 0
    for row in ROWS:
        pid = row[0]
        if any(r and r[0] == pid for r in data):
            print(f"  {pid} already in CSV — skipping")
            continue

        # Insert after existing VII rows (SFT, VPG, VCN) and before VLB rows
        insert_pos = 0
        for i in range(len(data)):
            if data[i] and data[i][2] == GROUP and data[i][3] in (
                "可持续金融分类目录",
                "自愿性采购指南",
                "自愿碳中和方法",
                "自愿性信息披露",
            ):
                insert_pos = i + 1

        if insert_pos == 0:
            print(f"ERROR: Cannot find insertion position for {pid}")
            return 1

        data.insert(insert_pos, list(row))
        inserted += 1
        print(f"  Inserted {pid} at data index {insert_pos}")

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
