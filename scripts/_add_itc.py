"""Fill two Target Responsibility System instruments into the CN regulatory CSV.

Single-run helper — appends two new instrument rows after the last
Framework regulation row.

Run from repo root:
    python scripts/_add_itc.py
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "outputs" / "CCPID_cn_regulatory_instruments.csv"


def make_row(pid, sector, subsector, name_cn, name_en, description,
             objective, adoption, effective, revision, revision_detail,
             agent, agent_detail, activity_detail,
             intensity_val, intensity_unit, intensity_detail,
             req_spec, monitoring_detail, enforcement_detail,
             promotion_detail, co_benefits, legal_name, legal_url, other_links, isic,
             status="生效", asset="N/A", asset_detail="N/A", asset_status="N/A",
             mitigation_effects="正向", channel="需求侧", jurisdiction_name="N/A",
             ghg="CO2", mitigation="直接", enforcement="目标责任考核；问责约谈；项目限批",
             monitoring="目标责任评价考核；监测预警",
             promotion="其他激励或支持", activity="消费（使用）"):
    return (
        pid, "工具", "框架性规制", "目标责任制度", sector, subsector,
        name_cn, name_en, "N/A", description, objective,
        mitigation, channel, "中国", "国家", jurisdiction_name,
        adoption, effective, "N/A", revision, revision_detail,
        status,
        "国家发展和改革委员会；国务院；省级人民政府",
        asset, asset_status, asset_detail, "N/A", "N/A",
        agent, agent_detail,
        activity,
        activity_detail,
        intensity_val, intensity_unit, intensity_detail,
        req_spec,
        "N/A", "N/A",
        monitoring, monitoring_detail,
        enforcement, enforcement_detail,
        promotion, promotion_detail,
        "N/A", "N/A",
        isic, ghg, mitigation_effects, co_benefits,
        legal_name, legal_url, other_links,
    )


ROWS = [
    make_row(
        pid="CHNFRMTRSI01S000",
        sector="跨部门",
        subsector="N/A",
        name_cn="能源消费强度和总量双控制度",
        name_en="Energy Consumption Intensity and Total Control System",
        description=(
            "能源消费强度和总量双控制度是中国“十三五”规划（2016—2020年）确立的约束性目标管理制度，"
            "对省级行政区域设定单位GDP能源消耗降低和能源消费总量控制目标，将国家目标逐级分解至省级"
            "政府和重点用能单位，并对目标完成情况进行年度监测、评价和考核问责。该制度通过控制化石"
            "能源消费总量和强度，推动能源结构优化和温室气体减排。"
        ),
        objective="提高能效；控制能源消费总量；优化能源结构",
        adoption="20/12/2016",
        effective="20/12/2016",
        revision="11/09/2021",
        revision_detail=(
            "2021年9月11日，国家发展改革委印发《完善能源消费强度和总量双控制度方案》"
            "（发改环资〔2021〕1310号），对目标设置、分解落实、监测预警和考核评价机制"
            "作出进一步完善，增加了可再生能源消费不纳入能源消费总量考核等弹性规定。"
        ),
        agent="企业；政府",
        agent_detail=(
            "各省、自治区、直辖市人民政府对本行政区能源消费总量和强度控制负总责；"
            "年综合能源消费量达到限定标准的重点用能单位须履行节能目标责任。"
        ),
        activity_detail=(
            "化石能源和非化石能源的消费活动。省级政府须将能源消费总量和强度控制在国家下达的"
            "目标范围内，重点用能单位须将能源消费控制在核定的总量和强度指标内。"
            "新建高耗能项目须通过节能审查，确保符合区域能源消费总量和强度控制要求。"
        ),
        intensity_val="约束性指标，按五年规划期设定",
        intensity_unit="吨标准煤（总量）；吨标准煤/万元GDP（强度）",
        intensity_detail=(
            "“十三五”期间全国单位GDP能耗降低15%，能源消费总量控制在50亿吨标准煤以内；"
            "“十四五”期间全国单位GDP能耗降低13.5%。各省目标由国家发展改革委分解下达。"
        ),
        req_spec=(
            "1）国家将能源消费强度和总量双控目标作为约束性指标纳入国民经济和社会发展规划；"
            "2）省级政府将国家下达的双控目标分解至地市级政府和重点用能单位；"
            "3）重点用能单位须制定节能规划，建立能源管理体系，报告能源利用状况；"
            "4）新建、改建和扩建高耗能项目须通过节能审查，确保符合能源消费总量和强度控制要求。"
        ),
        monitoring_detail=(
            "国家发展改革委会同有关部门建立能源消费总量和强度监测预警机制，按季度发布各地区"
            "能耗双控目标完成情况晴雨表，对进度严重滞后的地区进行预警。省级政府每年向国务院"
            "报告能源消费总量和强度控制目标完成情况。重点用能单位每年向节能主管部门报告能源"
            "利用状况，并接受节能监察。"
        ),
        enforcement_detail=(
            "省级政府能耗双控目标完成情况纳入生态文明建设评价考核体系，作为领导班子和领导"
            "干部综合考核评价的重要依据。未完成目标的地区由国务院节能主管部门约谈，并暂停"
            "审批该地区新建高耗能项目。重点用能单位未完成节能目标的，予以通报批评并限期整改；"
            "逾期未整改的，依法予以处罚。"
        ),
        promotion_detail=(
            "国家通过节能减排财政补助资金、节能技术改造奖励、合同能源管理税收优惠、绿色金融"
            "等政策措施，鼓励和支持各地区、各用能单位开展节能降耗工作。对超额完成能耗双控"
            "目标的地区，在能源消费总量指标分配中给予适当倾斜。"
        ),
        co_benefits="能效提升；能源消耗减少；空气污染物减排；能源安全",
        legal_name="国务院关于印发“十三五”节能减排综合工作方案的通知",
        legal_url="https://www.gov.cn/zhengce/content/2017-01/05/content_5156789.htm",
        other_links=(
            "《中华人民共和国节约能源法》（2018年修正）："
            "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE2ZjEzNWY0NjAxNmYyMTY5MjAxNTExMjk%3D "
            "| 《完善能源消费强度和总量双控制度方案》（发改环资〔2021〕1310号）："
            "https://www.ndrc.gov.cn/xxgk/zcfb/tz/202109/t20210916_1296856.html"
        ),
        isic="B; C; D35; F; H49",
    ),
    make_row(
        pid="CHNFRMTRSI02S000",
        sector="跨部门",
        subsector="N/A",
        name_cn="碳排放强度和总量双控制度",
        name_en="Carbon Emission Intensity and Total Control System",
        description=(
            "碳排放强度和总量双控制度是中国推动能耗双控向碳排放双控全面转型的新制度框架。"
            "该制度建立国家层面的碳排放强度降低和碳排放总量控制目标，逐级分解至省级政府和"
            "重点排放单位，实行碳排放预算管理，并对目标完成情况进行监测、评估和考核问责。"
            "该制度旨在从源头控制温室气体排放，是实现碳达峰碳中和目标的核心治理制度。"
        ),
        objective="减缓气候变化",
        adoption="30/07/2024",
        effective="30/07/2024",
        revision="N/A",
        revision_detail="N/A",
        agent="企业；政府",
        agent_detail=(
            "各省、自治区、直辖市人民政府对本行政区碳排放总量和强度控制负总责；"
            "年温室气体排放量达到限定标准的重点排放单位须履行碳排放控制目标责任。"
        ),
        activity_detail=(
            "化石能源燃烧、工业生产过程等温室气体排放活动。省级政府须将碳排放总量和强度"
            "控制在国家下达的目标范围内。碳排放双控制度实行碳排放预算管理，将碳排放指标"
            "纳入国民经济和社会发展规划，并通过碳减排项目和碳汇交易实现弹性管控。"
        ),
        intensity_val="约束性指标，按五年规划期设定",
        intensity_unit="吨CO₂（总量）；吨CO₂/万元GDP（强度）",
        intensity_detail=(
            "“十五五”规划（2026—2030年）期间将以碳排放强度和总量双控替代能耗双控，"
            "具体指标数值由国家在“十五五”规划纲要中确定。过渡期内实行碳排放双控与能耗"
            "双控并行的弹性管理制度。"
        ),
        req_spec=(
            "1）国家将碳排放强度和总量双控目标作为约束性指标纳入国民经济和社会发展规划；"
            "2）省级政府将国家下达的碳排放双控目标分解至地市级政府和重点排放单位；"
            "3）建立碳排放预算管理制度，将碳排放指标纳入固定资产投资项目节能审查和环评审批；"
            "4）重点排放单位须建立碳排放管理体系，编制碳排放报告，接受碳排放核查。"
        ),
        monitoring_detail=(
            "国家发展改革委会同生态环境部建立碳排放总量和强度监测预警机制，对各省碳排放"
            "双控目标完成情况进行年度评价和中期评估。省级政府每年报告碳排放双控目标完成"
            "情况。重点排放单位须建立碳排放监测计划，按年度编制温室气体排放报告并接受"
            "第三方核查。"
        ),
        enforcement_detail=(
            "省级政府碳排放双控目标完成情况纳入碳达峰碳中和工作评价考核体系，作为领导"
            "班子和领导干部综合考核评价的重要依据。未完成目标的地区由国务院有关部门约谈，"
            "并采取项目限批等措施。重点排放单位未完成碳排放控制目标的，责令限期整改；"
            "逾期未整改的，依法予以处罚。"
        ),
        promotion_detail=(
            "国家通过碳减排项目支持、碳普惠机制、碳排放权交易、绿色金融等政策措施，"
            "鼓励和支持各地区、各排放单位开展碳减排工作。对碳排放双控成效显著的地区，"
            "在碳排放指标分配和财政转移支付中给予倾斜支持。"
        ),
        co_benefits="能效提升；能源消耗减少；空气污染物减排；技术创新；绿色产业发展",
        legal_name="国务院办公厅关于印发《加快构建碳排放双控制度体系工作方案》的通知",
        legal_url="https://www.gov.cn/zhengce/content/202408/content_6966079.htm",
        other_links=(
            "《中共中央 国务院关于加快经济社会发展全面绿色转型的意见》（2024年7月）："
            "https://www.gov.cn/zhengce/202408/content_6967663.htm"
        ),
        isic="B; C; D35; F; H49",
        status="生效",
        mitigation="直接",
        channel="供给侧",
        activity="生产",
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
    existing = _load_rows(CSV_PATH)
    header, data = existing[0], existing[1:]

    # Insert after last Framework regulation row
    insert_pos = None
    for i in range(len(data) - 1, -1, -1):
        if data[i][2] == "框架性规制":
            insert_pos = i + 1  # +1 to insert after this row (data is 0-indexed)
            break

    if insert_pos is None:
        print("ERROR: No Framework regulation row found")
        return 1

    for row in ROWS:
        pid = row[0]
        if any(r[0] == pid for r in data):
            print(f"  {pid} already in CSV — skipping")
            continue
        data.insert(insert_pos, list(row))
        insert_pos += 1
        print(f"  Inserted {pid} at data index {insert_pos - 1}")

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows)")


if __name__ == "__main__":
    raise SystemExit(main())
