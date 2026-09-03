"""Fill TRS04 (SASAC central enterprise supervision) and EEM01 (key energy-consuming
unit energy management) instruments into the CN regulatory CSV.

Single-run helper — appends two new instrument rows after the last
Framework regulation row.

Run from repo root:
    python scripts/_add_trs4_eem1.py
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "outputs" / "CCPID_cn_regulatory_instruments.csv"


def make_trs_row(pid, sector, subsector, name_cn, name_en, description,
                 objective, adoption, effective, revision, revision_detail,
                 agent, agent_detail, activity_detail,
                 intensity_val, intensity_unit, intensity_detail,
                 req_spec, monitoring_detail, enforcement_detail,
                 promotion_detail, co_benefits, legal_name, legal_url, other_links, isic,
                 status="生效", asset="N/A", asset_detail="N/A", asset_status="N/A",
                 mitigation_effects="正向", channel="需求侧", jurisdiction_name="N/A",
                 ghg="CO2", mitigation="直接",
                 enforcement="目标责任考核；问责约谈",
                 monitoring="目标责任评价考核；监测预警",
                 promotion="其他激励或支持", activity="消费（使用）",
                 admin_authorities="国家发展和改革委员会；国务院；省级人民政府"):
    return (
        pid, "工具", "框架性规制", "目标责任制度", sector, subsector,
        name_cn, name_en, "N/A", description, objective,
        mitigation, channel, "中国", "国家", jurisdiction_name,
        adoption, effective, "N/A", revision, revision_detail,
        status,
        admin_authorities,
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


def make_eem_row(pid, sector, subsector, name_cn, name_en, description,
                 objective, adoption, effective, revision, revision_detail,
                 agent, agent_detail, activity_detail,
                 intensity_val, intensity_unit, intensity_detail,
                 req_spec, monitoring_detail, enforcement_detail,
                 promotion_detail, co_benefits, legal_name, legal_url, other_links, isic,
                 status="生效", asset="N/A", asset_detail="N/A", asset_status="N/A",
                 mitigation_effects="正向", channel="需求侧", jurisdiction_name="N/A",
                 ghg="CO2", mitigation="直接",
                 enforcement="行政处罚；责令整改；罚款",
                 monitoring="能源审计；能源利用状况报告；节能监察",
                 promotion="其他激励或支持", activity="消费（使用）",
                 admin_authorities="国家发展和改革委员会；省级人民政府"):
    return (
        pid, "工具", "框架性规制", "企业能源管理义务", sector, subsector,
        name_cn, name_en, "N/A", description, objective,
        mitigation, channel, "中国", "国家", jurisdiction_name,
        adoption, effective, "N/A", revision, revision_detail,
        status,
        admin_authorities,
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
    make_trs_row(
        pid="CHNFRMTRSI04S000",
        sector="跨部门",
        subsector="N/A",
        name_cn="中央企业节能环保监督管理制度",
        name_en="Central Enterprise Energy Conservation and Environmental Protection Supervision and Management System",
        description=(
            "中央企业节能环保监督管理制度是国务院国资委对其履行出资人职责的中央企业"
            "实施节约能源与生态环境保护分类监督管理的治理制度。该制度根据行业属性、"
            "年能耗量和主要污染物排放水平将中央企业划分为三类，实行动态分类监管，"
            "涵盖绿色低碳发展、碳达峰碳中和、污染防控、统计监测报告、突发环境事件应急"
            "等要求，并将考核结果纳入中央企业负责人经营业绩考核体系。"
        ),
        objective="减缓气候变化；能效提升；环境保护",
        adoption="29/06/2022",
        effective="01/08/2022",
        revision="N/A",
        revision_detail="N/A",
        agent="企业",
        agent_detail=(
            "国务院国资委履行出资人职责的中央企业是本制度的受规制主体。中央企业须建立"
            "节约能源与生态环境保护领导机构，设置监督管理机构，落实党政同责、一岗双责。"
            "国资委根据企业行业属性、能耗和排放水平，将中央企业划分为三类并实行动态分类"
            "监督管理。"
        ),
        activity_detail=(
            "中央企业在石油石化、钢铁、有色金属、电力、化工、煤炭、建材、交通运输、建筑"
            "等行业的能源消费、温室气体排放和主要污染物排放活动。第一类企业（年耗能200万吨"
            "标准煤以上或主要污染物排放居央企前三分之一）和第二类企业（年耗能10万吨标准煤"
            "以上）按季度报送统计报表，第三类企业按年度报送。各类企业均须报送年度总结分析"
            "报告，制定碳达峰碳中和规划，建立碳排放统计核算体系。"
        ),
        intensity_val="三类分类管理，动态调整",
        intensity_unit="企业类别（第一类、第二类、第三类）",
        intensity_detail=(
            "第一类企业：主业处于石油石化、钢铁、有色金属、电力、化工、煤炭、建材、交通"
            "运输、建筑行业，且年耗能200万吨标准煤以上，或主要污染物排放总量居央企前三分"
            "之一，或对生态环境有较大影响。第二类企业：年耗能10万吨标准煤以上，或主要污染"
            "物排放居央企中等水平。第三类企业：上述以外的企业。国资委根据能耗和排放水平"
            "适时调整企业类别。"
        ),
        req_spec=(
            "1）中央企业须建立节约能源与生态环境保护领导机构和监督管理机构，落实党政同责、"
            "一岗双责；2）中央企业须将节能环保纳入企业发展战略，制定碳达峰碳中和规划，"
            "建立碳排放统计核算体系，遏制“两高”项目盲目发展；3）中央企业须建立"
            "统计监测与报告制度，第一类和第二类企业按季度、第三类企业按年度报送统计报表"
            "和年度总结分析报告，发生突发环境事件须逐级上报至国资委；4）国资委将节约能源与"
            "生态环境保护考核结果纳入中央企业负责人经营业绩考核体系，实行年度和任期考核，"
            "发生突发环境事件或数据弄虚作假的予以扣分或降级处理。"
        ),
        monitoring_detail=(
            "国资委建立中央企业节约能源与生态环境保护统计报送信息系统，对中央企业能耗"
            "和排放数据进行动态监测。中央企业须配备能源计量器具，建立能源计量管理制度，"
            "按要求建设能耗在线监测系统。第一类和第二类企业按季度、第三类企业按年度报送"
            "统计报表。各类企业每年报送年度总结分析报告。发生突发环境事件须逐级上报至"
            "国资委，每级上报时间不超过2小时。"
        ),
        enforcement_detail=(
            "国资委将节约能源与生态环境保护考核评价结果纳入中央企业负责人经营业绩考核"
            "体系，实行年度和任期、定量或定性考核。发生突发环境事件、节能环保违法违规"
            "事件、统计数据严重不实和弄虚作假的，年度考核予以扣分或降级处理。中央企业"
            "应建立完善内部考核奖惩体系，逐级分解落实责任。国资委依据本办法制定《中央企业"
            "节约能源与生态环境保护考核细则》。"
        ),
        promotion_detail=(
            "对节约能源与生态环境保护取得突出成绩的中央企业，经国资委评定后予以任期通报"
            "表扬。中央企业应按照同行业国际国内先进水平，提出科学合理的任期考核指标和目标"
            "建议值，在中央企业负责人任期经营考核责任书中明确。对表现突出的单位和个人，"
            "按规定给予表彰奖励。"
        ),
        co_benefits="能效提升；能源消耗减少；空气污染物减排；技术创新；绿色产业发展；能源安全；污染防治；生态保护",
        legal_name="《中央企业节约能源与生态环境保护监督管理办法》（国务院国资委令第41号）",
        legal_url="https://www.gov.cn/zhengce/2022-08/03/content_5718613.htm",
        other_links=(
            "《中央企业节能减排监督管理暂行办法》（国资委令第23号，已废止）："
            "https://www.gov.cn/gongbao/content/2010/content_1705528.htm"
        ),
        isic="B; C; D35; F; H49",
        status="生效",
        mitigation="直接",
        channel="供给侧",
        activity="生产",
        enforcement="目标责任考核",
        admin_authorities="国务院国有资产监督管理委员会",
    ),
    make_eem_row(
        pid="CHNFRMEEMI01S000",
        sector="跨部门",
        subsector="N/A",
        name_cn="重点用能单位节能管理制度",
        name_en="Key Energy-Consuming Unit Energy Conservation Management System",
        description=(
            "重点用能单位节能管理制度是要求年综合能源消费量达到限定标准的用能单位建立"
            "内部节能管理基础设施并履行持续合规义务的监管制度。该制度要求重点用能单位设立"
            "能源管理岗位、建立能源管理体系、配备能源计量器具、开展能源审计、报送能源利用"
            "状况报告和建设能耗在线监测系统，并对违规行为设定行政处罚。"
        ),
        objective="提高能效；控制能源消费总量；优化能源结构",
        adoption="10/03/1999",
        effective="10/03/1999",
        revision="22/02/2018",
        revision_detail=(
            "2018年2月22日，国家发展改革委、科技部、人民银行、国务院国资委、国家质检总局、"
            "国家统计局、证监会联合发布新的《重点用能单位节能管理办法》（令第15号），"
            "自2018年5月1日起施行，废止1999年原国家经贸委令第7号。新办法增加了能耗总量"
            "控制、能源管理体系认证、能耗在线监测系统建设等要求，并补充和细化了法律责任条款。"
        ),
        agent="企业",
        agent_detail=(
            "年综合能源消费量一万吨标准煤及以上的用能单位，以及国务院有关部门或省级人民政府"
            "指定的年综合能源消费量五千吨及以上不满一万吨标准煤的用能单位。重点用能单位须"
            "成立节能工作领导小组，聘任能源管理负责人（中级以上技术职称），设立能源管理岗位，"
            "并报管理节能工作的部门备案。"
        ),
        activity_detail=(
            "化石能源和非化石能源的消费活动。重点用能单位须将能源消费总量和强度控制在"
            "核定的目标范围内，建立节能目标责任制并将目标分解至相应层级或岗位，定期组织"
            "内部考核。重点用能单位须建立能源管理体系，按年度报送能源利用状况报告，"
            "实施能源审计，建设能耗在线监测系统，并接受节能监察。"
        ),
        intensity_val="年综合能源消费量一万吨标准煤（一般门槛）；五千吨标准煤（特殊指定）",
        intensity_unit="吨标准煤/年",
        intensity_detail=(
            "年综合能源消费量一万吨标准煤及以上的用能单位自动纳入管理。国务院有关部门或"
            "省级人民政府可指定年综合能源消费量五千吨及以上不满一万吨标准煤的用能单位参照"
            "执行。地市级以上管理节能工作的部门将能耗总量控制和节能目标分解至重点用能单位，"
            "逐级开展节能目标责任评价考核并公布结果。"
        ),
        req_spec=(
            "1）重点用能单位须建立节能目标责任制，将能耗总量控制和节能目标分解至相应层级"
            "或岗位，定期组织内部考核并建立节能奖惩制度；2）重点用能单位须按照"
            "GB/T 23331《能源管理体系 要求》建立能源管理体系并有效运行，成立节能工作"
            "领导小组，聘任能源管理负责人并设立能源管理岗位；3）重点用能单位须配备能源计量"
            "器具，按年度报送能源利用状况报告，实施能源审计，并建设能耗在线监测系统；"
            "4）重点用能单位须遵守单位产品能耗限额标准，淘汰落后生产工艺、用能设备和产品，"
            "新建、改建和扩建固定资产投资项目须通过节能审查。"
        ),
        monitoring_detail=(
            "地市级以上人民政府管理节能工作的部门对重点用能单位分级开展节能目标责任评价"
            "考核，主要考核能耗总量控制和节能目标完成情况、能源利用效率及节能措施落实情况，"
            "逐级报送考核结果并向社会公布。管理节能工作的部门对能源利用状况报告进行审查，"
            "对节能管理制度不健全、节能措施不落实、能源利用效率低的单位开展现场调查，"
            "组织实施用能设备能源效率检测，责令实施能源审计。"
        ),
        enforcement_detail=(
            "节能管理制度不健全、拒不落实整改要求或整改未达标的，处10万元以上30万元以下"
            "罚款。未设立能源管理岗位、未聘任能源管理负责人或未备案的，处1万元以上3万元"
            "以下罚款。未按规定报送能源利用状况报告或报告内容不实的，处1万元以上5万元以下"
            "罚款。不按要求建设能耗在线监测系统的，处1万元以上3万元以下罚款。超过单位产品"
            "能耗限额标准用能的，提请执行惩罚性电价。不按期淘汰落后生产工艺、用能设备和产品"
            "的，责令停用、没收设备并处罚款，情节严重的停业整顿或关闭。"
        ),
        promotion_detail=(
            "国家鼓励重点用能单位开展能源管理体系认证，积极开展能效对标活动，争当能效"
            "“领跑者”。对节能考核结果优秀的重点用能单位，在节能技术改造资金、"
            "节能产品推广、绿色金融等方面给予优先支持。对超额完成节能目标的单位，在能源"
            "消费总量指标分配中给予适当倾斜。"
        ),
        co_benefits="能效提升；能源消耗减少；空气污染物减排；技术创新",
        legal_name="《重点用能单位节能管理办法》（国家发展改革委等七部门令第15号，2018年）",
        legal_url="https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=18518",
        other_links=(
            "《重点用能单位节能管理办法》（国家经贸委令第7号，1999年，已废止）："
            "http://www.nea.gov.cn/2011-08/18/c_131057691.htm "
            "| 《中华人民共和国节约能源法》（2018年修正）："
            "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE2ZjEzNWY0NjAxNmYyMTY5MjAxNTExMjk%3D"
        ),
        isic="B; C; D35; F; H49",
        status="生效",
        mitigation="直接",
        channel="需求侧",
        activity="消费（使用）",
        admin_authorities="国家发展和改革委员会；省级人民政府",
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
            insert_pos = i + 1
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
