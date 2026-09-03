"""Fill carbon peak and neutrality evaluation & assessment instrument into the CN regulatory CSV.

Single-run helper — appends one new instrument row after the last
Framework regulation row.

Run from repo root:
    python scripts/_add_trs3.py
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


ROWS = [
    make_row(
        pid="CHNFRMTRSI03S000",
        sector="跨部门",
        subsector="N/A",
        name_cn="碳达峰碳中和综合评价考核制度",
        name_en="Comprehensive Carbon Peak and Carbon Neutrality Evaluation and Assessment System",
        description=(
            "碳达峰碳中和综合评价考核制度是对省级党委和政府落实碳达峰碳中和目标任务情况"
            "进行年度评价考核的党政同责治理制度。该制度建立“5+9”评价考核指标体系，"
            "涵盖碳排放总量、碳排放强度降低、煤炭消费总量、石油消费总量和非化石能源消费占比"
            "5项控制指标，以及节能、工业、城乡建设、交通运输、公共机构、碳排放权交易和森林"
            "碳汇等领域9项支撑指标。考核结果分为优秀、合格和不合格三个等次，作为领导班子和"
            "领导干部综合考核评价、选拔任用和监督管理的重要参考。"
        ),
        objective="减缓气候变化",
        adoption="12/04/2026",
        effective="12/04/2026",
        revision="N/A",
        revision_detail="N/A",
        agent="政府",
        agent_detail=(
            "各省、自治区、直辖市党委和政府对本行政区碳达峰碳中和目标任务完成情况负总责，"
            "实行党政同责、一岗双责。中央组织部统筹指导，国家发展改革委会同有关部门组织实施"
            "评价考核。"
        ),
        activity_detail=(
            "化石能源燃烧、工业生产过程等温室气体排放活动，以及能源消费、城乡建设、交通"
            "运输、公共机构运营和森林碳汇等涉及碳排放和碳吸收的各类活动。省级党委和政府须"
            "确保完成国家设定的碳排放总量和强度等5项控制指标和9项支撑指标，推动经济社会"
            "发展全面绿色转型。"
        ),
        intensity_val="约束性指标，按年度设定",
        intensity_unit="5项控制指标+9项支撑指标；等次：优秀、合格、不合格",
        intensity_detail=(
            "“十五五”时期目标为2030年碳排放强度比2005年降低65%以上，"
            "非化石能源消费占比达到25%左右，实现煤炭消费总量和石油消费总量达峰。"
            "控制指标全部达标且支撑指标全部达标为优秀；1项及以上控制指标不达标或"
            "3项及以上支撑指标不达标为不合格；其余为合格。"
        ),
        req_spec=(
            "1）省级党委和政府对本行政区碳达峰碳中和目标任务负总责，实行党政同责、一岗双责；"
            "2）国家设定碳排放总量、碳排放强度降低、煤炭消费总量、石油消费总量和非化石能源"
            "消费占比5项控制指标，以及单位地区生产总值能源消耗降低、清洁能源电量占比、工业"
            "能耗和碳排放降低、“两高”项目碳排放置换和节能降碳审查、城乡建设绿色低碳"
            "转型、交通运输绿色低碳转型、公共机构碳排放强度降低、碳排放权交易市场覆盖行业"
            "碳排放控制和森林蓄积量增长等支撑指标；"
            "3）按年度开展评价考核，于考核年度次年实施，程序包括地方自评、部门评价、实地核验"
            "和综合评定四个步骤；"
            "4）考核结果报党中央、国务院审定后反馈各省党委和政府，抄送中央纪委国家监委，作为"
            "领导班子和领导干部综合考核评价、选拔任用和监督管理的重要参考。"
        ),
        monitoring_detail=(
            "国家发展改革委会同有关部门建立碳达峰碳中和监测预警机制，对各地区碳排放总量和"
            "强度等关键指标进行动态监测。省级党委和政府每年开展碳达峰碳中和自评，按时将自评"
            "报告报党中央、国务院。各有关部门对所负责指标的全国年度进展情况进行评估，对各省"
            "单一指标评价结果分为“达标”和“不达标”，对不达标指标剖析问题"
            "原因并提出改进建议。国家发展改革委会同有关部门采取实地抽查和委托第三方核查等"
            "方式，对工作进展、任务落实、目标完成及数据真实性进行核验。"
        ),
        enforcement_detail=(
            "考核结果经党中央、国务院审定后，由中央组织部、国家发展改革委向各省党委和政府"
            "反馈，并抄送中央纪委国家监委。考核不合格的，督促在30个工作日内向党中央、国务院"
            "作出书面报告，提出整改措施和完成时限；逾期整改不到位的，约谈该省党委和政府。"
            "考核合格但部分指标不达标的，在一定范围内通报提醒。存在徇私舞弊、谎报瞒报、"
            "篡改数据、伪造资料等行为造成结果严重失真失实的，该省评价考核结果直接确定为"
            "不合格，并严肃追究相关单位和人员责任。"
        ),
        promotion_detail=(
            "对考核优秀或单项工作表现突出的省份予以通报表扬，总结宣传推广好经验好做法。"
            "对碳达峰碳中和工作成效显著的地区，在碳排放指标分配、财政转移支付和重大项目"
            "布局等方面给予倾斜支持。对表现突出的单位和个人，按规定给予表彰奖励。"
        ),
        co_benefits="能效提升；能源消耗减少；空气污染物减排；技术创新；绿色产业发展；能源安全；可再生能源发展；生态保护",
        legal_name="中共中央办公厅 国务院办公厅关于印发《碳达峰碳中和综合评价考核办法》的通知",
        legal_url="https://www.gov.cn/zhengce/202604/content_7066695.htm",
        other_links=(
            "国家发展改革委有关负责同志就《碳达峰碳中和综合评价考核办法》答记者问："
            "https://www.ndrc.gov.cn/xxgk/jd/jd/202604/t20260423_1404856_ext.html"
        ),
        isic="B; C; D35; F; H49",
        status="生效",
        mitigation="直接",
        channel="供给侧",
        activity="生产",
        enforcement="目标责任考核；问责约谈",
        admin_authorities="中共中央组织部；国家发展和改革委员会；国务院；省级人民政府",
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
