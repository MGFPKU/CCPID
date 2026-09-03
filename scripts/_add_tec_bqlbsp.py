#!/usr/bin/env python3
"""Insert two new Technology standard instruments:
   - CHNTECBQLI01S000 (E10 Ethanol Gasoline Mandate)
   - CHNTECBPPI01S000 (Plastic Products Ban and Restriction)
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_regulatory_instruments.csv"


def make_row(pid, approach_cn, sector, subsector, name_cn, name_en, description,
             objective, adoption, effective, revision, revision_detail,
             agent, agent_detail, activity, activity_detail,
             intensity_val, intensity_unit, intensity_detail,
             req_spec, monitoring_detail, enforcement_detail,
             promotion_detail, co_benefits, legal_name, legal_url, other_links, isic,
             asset, asset_detail, mitigation,
             admin_authorities, monitoring,
             enforcement="行政处罚",
             promotion="税收优惠；财政补贴",
             asset_status="既有",
             mitigation_effects="正向",
             channel="供给侧",
             jurisdiction_name="N/A",
             ghg="CO2",
             ghg_abs="N/A",
             ghg_pct="N/A",
             status="生效",
             group_cn="技术标准",
             instrument_type="工具"):
    row = (
        pid,
        instrument_type,
        group_cn,
        approach_cn,
        sector,
        subsector,
        name_cn,
        name_en,
        "N/A",  # Policy Package
        description,
        objective,
        mitigation,
        channel,
        "中国",  # Country
        "国家",  # Jurisdiction level
        jurisdiction_name,
        adoption,
        effective,
        "N/A",  # End date
        revision,
        revision_detail,
        status,
        admin_authorities,
        asset,
        asset_status,
        asset_detail,
        "N/A",  # Asset (Other)
        "N/A",  # Asset (Cut-off range)
        agent,
        agent_detail,
        activity,
        activity_detail,
        intensity_val,
        intensity_unit,
        intensity_detail,
        req_spec,
        "N/A",  # Compliance calculation methodology I
        "N/A",  # Compliance calculation methodology II
        monitoring,
        monitoring_detail,
        enforcement,
        enforcement_detail,
        promotion,
        promotion_detail,
        ghg_abs,
        ghg_pct,
        isic,
        ghg,
        mitigation_effects,
        co_benefits,
        legal_name,
        legal_url,
        other_links,
    )
    return row


ROWS = [
    # ============================================================
    # BQL01 — E10 Ethanol Gasoline Mandate
    # ============================================================
    make_row(
        pid="CHNTECBQLI01S000",
        approach_cn="陆路交通燃料生物燃料配额",
        sector="交通",
        subsector="道路运输",
        name_cn="推广使用车用乙醇汽油",
        name_en="Promotion of Ethanol Gasoline for Motor Vehicles",
        description=(
            "中国自2000年代初期开始推广车用乙醇汽油（E10，含10%燃料乙醇的混合汽油）。"
            "2002年启动试点，2004年扩大至六省一市（黑龙江、吉林、辽宁、河南、安徽、"
            "湖北和河北部分地区）。2017年9月13日，国家发展改革委、国家能源局等十五部门"
            "联合印发《关于扩大生物燃料乙醇生产和推广使用车用乙醇汽油的实施方案》（发"
            "改能源[2017]1508号），要求到2020年在全国范围内推广使用车用乙醇汽油，基本"
            "实现全覆盖。以玉米等陈化粮为主要原料生产燃料乙醇，同时发展纤维素燃料乙醇"
            "等非粮生物燃料。标准方面，GB 18351-2017《车用乙醇汽油（E10）》于2017年9月"
            "7日发布，2018年6月1日实施；GB 18351-2025于2025年6月30日发布，2026年7月1日"
            "实施。覆盖率最高时约15个省份推广，全国乙醇汽油掺混率约2.1%，高峰期覆盖约"
            "五分之一全国汽油消费量。该制度通过强制掺混生物燃料乙醇替代化石汽油，直接"
            "减少汽油全生命周期温室气体排放。"
        ),
        objective="能源安全；生态环境保护；空气污染防治；农业农村发展",
        adoption="13/09/2017",
        effective="13/09/2017",
        revision="30/06/2025",
        revision_detail=(
            "首次制定于2017年9月13日（发改能源[2017]1508号）。2025年6月30日，GB "
            "18351-2025《车用乙醇汽油（E10）》发布，自2026年7月1日起替代GB 18351-2017"
            "，更新了乙醇汽油的技术要求和试验方法标准。"
        ),
        agent="企业",
        agent_detail=(
            "汽油生产企业（中国石化、中国石油、中国海油等）；成品油销售企业。"
        ),
        activity="生产；销售",
        activity_detail="生物燃料乙醇生产、汽油调配和车用乙醇汽油销售。车辆所有者被动使用所供应油品。",
        intensity_val="10%",
        intensity_unit="%（体积分数）",
        intensity_detail=(
            "车用乙醇汽油（E10）要求乙醇体积掺混比例为10%（±2%），"
            "即变性燃料乙醇占成品汽油体积的10%。该比例为GB 18351-2017和"
            "GB 18351-2025标准的强制性技术要求。"
            "来源：GB 18351-2017《车用乙醇汽油（E10）》；GB 18351-2025。"
        ),
        req_spec=(
            "1）在黑龙江、吉林、辽宁、河南、安徽、湖北、河北等粮食主产区及周边省份，"
            "推广使用车用乙醇汽油（E10）；2）成品油销售企业须在指定区域内全面供应车用"
            "乙醇汽油，不得销售普通汽油；3）燃料乙醇生产企业须以陈化粮为主，积极发展非"
            "粮生物燃料乙醇（纤维素乙醇等）；4）车用乙醇汽油须符合GB 18351标准的品质"
            "要求；5）到2020年基本实现全国覆盖（除西藏、青海、新疆等不具备条件的地区外）。"
        ),
        monitoring_detail=(
            "产品质量监督抽查；市场检查。各级市场监管部门组织车用乙醇汽油产品质量监督"
            "抽查，对不符合GB 18351标准的产品依法处理。"
        ),
        enforcement_detail=(
            "行政处罚；责令整改。销售不符合GB 18351标准的车用乙醇汽油，由市场监管部门"
            "依据《产品质量法》相关规定予以处罚。"
        ),
        promotion_detail=(
            "税收优惠；财政补贴（对生物燃料乙醇生产企业）。国家对燃料乙醇生产企业给予"
            "增值税先征后退、原料补贴等政策支持。"
        ),
        co_benefits="能源安全；空气污染物减排；生态保护",
        legal_name=(
            "关于扩大生物燃料乙醇生产和推广使用车用乙醇汽油的实施方案"
            "（发改能源[2017]1508号）"
        ),
        legal_url="https://www.nea.gov.cn/2017-09/13/c_136606035.htm",
        other_links=(
            "GB 18351-2017《车用乙醇汽油（E10）》（旧版标准）"
            "：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?"
            "hcno=9F9E8E6A5E5A1D7B8C2F3A4D5E6F7A8B；"
            "GB 18351-2025《车用乙醇汽油（E10）》（新版标准，"
            "2026年7月1日实施）：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?"
            "hcno="
        ),
        isic="C19; C20; G47",
        asset="车用乙醇汽油（E10）",
        asset_detail=(
            "车用乙醇汽油（E10）是由不添加含氧化合物的车用乙醇汽油调合组分油加入10%"
            "（±2%）体积分数的变性燃料乙醇调合而成的混合汽油。标准涵盖GB 18351-2017"
            "（已替代）和GB 18351-2025（2026年7月1日实施），涵盖89号、92号、95号和"
            "98号四个辛烷值等级，规定了辛烷值、蒸气压、水分含量、乙醇含量等技术要求。"
        ),
        mitigation="间接",
        admin_authorities=(
            "国家能源局；国家发展和改革委员会；国家市场监督管理总局；工业和信息化部；"
            "财政部"
        ),
        monitoring="政府机构开展的监督检查",
    ),

    # ============================================================
    # BPP01 — Plastic Products Ban and Restriction
    # ============================================================
    make_row(
        pid="CHNTECBPPI01S000",
        approach_cn="塑料制品禁止和淘汰",
        sector="工业",
        subsector="塑料制品制造；零售；餐饮；住宿；快递",
        name_cn="塑料制品禁限制",
        name_en="Ban and Restrictions on Plastic Products",
        description=(
            "中国塑料制品禁限制制度由《关于进一步加强塑料污染治理的意见》（发"
            "改环资〔2020〕80号，2020年1月16日）建立，按照“禁限一批、替代循环一批、规"
            "范一批”的思路，分2020年、2022年、2025年三个时间段，有序禁止、限制部分塑料"
            "制品的生产、销售和使用。禁限品类包括：到2020年底，全国范围禁止生产和销售"
            "厚度小于0.025毫米的超薄塑料购物袋、厚度小于0.01毫米的聚乙烯农用地膜，禁"
            "止以医疗废物为原料制造塑料制品，禁止废塑料进口；到2020年底，全国范围餐饮"
            "行业禁止使用不可降解一次性塑料吸管，地级以上城市建成区餐饮堂食服务禁止使"
            "用不可降解一次性塑料餐具；到2020年底，禁止生产和销售一次性发泡塑料餐具、"
            "一次性塑料棉签；到2022年底，禁止销售含塑料微珠的日化产品；到2025年底，全"
            "国范围邮政快递网点禁止使用不可降解的塑料包装袋、塑料胶带、一次性塑料编织"
            "袋。2021年9月8日，国家发展改革委、生态环境部印发《十四五塑料污染治理行动"
            "方案》（发改环资〔2021〕1298号），进一步强化了塑料污染全链条治理要求。"
            "2020年4月29日修订的《固体废物污染环境防治法》（2020年9月1日实施）首次将"
            "塑料制品禁限纳入法律，为禁限制制度提供了法律基础。该制度的减缓相关"
            "性为间接：通过减少石油基塑料的生产和消费，避免了上游化石原料开采和加工过"
            "程中的温室气体排放。"
        ),
        objective="污染防治；资源节约；循环经济",
        adoption="16/01/2020",
        effective="16/01/2020",
        revision="08/09/2021",
        revision_detail=(
            "首次制定于2020年1月16日（发改环资〔2020〕80号）。2020年4月29日，《固体"
            "废物污染环境防治法》修订通过（2020年9月1日实施），将塑料制品禁限纳"
            "入法律。2021年9月8日，国家发展改革委、生态环境部联合印发《十四五塑料污染"
            "治理行动方案》（发改环资〔2021〕1298号），在2020年版基础上进一步强化塑料"
            "生产和使用源头减量、替代产品推广、塑料废弃物回收处置和重点区域塑料垃圾清"
            "理整治等全链条治理要求。"
        ),
        agent="企业",
        agent_detail=(
            "塑料制品生产企业；零售企业；餐饮企业；酒店；快递企业；电商平台。"
        ),
        activity="生产；销售；使用",
        activity_detail=(
            "各类受禁限塑料制品的生产、销售和使用活动。包括：塑料购物袋的生产和零售环"
            "节销售使用；一次性塑料吸管和餐具的餐饮行业使用；一次性塑料用品的宾馆酒店"
            "提供使用；不可降解塑料包装的快递行业使用；含塑料微珠日化产品的生产销售。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）到2020年底，全国范围禁止生产和销售厚度小于0.025mm的超薄塑料购物袋、"
            "厚度小于0.01mm的聚乙烯农用地膜、一次性发泡塑料餐具、一次性塑料棉签；"
            "2）到2020年底，全国范围餐饮行业禁止使用不可降解一次性塑料吸管，地级以上"
            "城市建成区餐饮堂食禁止使用不可降解一次性塑料餐具；3）到2020年底，禁止以"
            "医疗废物为原料制造塑料制品，禁止废塑料进口；4）到2022年底，禁止销售含塑料"
            "微珠的日化产品；5）到2025年底，全国范围邮政快递网点禁止使用不可降解的塑料"
            "包装袋、塑料胶带、一次性塑料编织袋；6）到2025年底，地级以上城市餐饮外卖"
            "领域不可降解一次性塑料餐具消耗强度下降30%；7）到2025年，全国所有宾馆、酒"
            "店、民宿不再主动提供一次性塑料用品。"
        ),
        monitoring_detail=(
            "政府机构开展的监督检查；企业报告。县级以上地方人民政府商务、邮政管理等"
            "部门按职责对零售场所、餐饮企业、快递企业等进行监督检查。零售场所、电商平台、"
            "快递企业和外卖平台须向商务、邮政等部门报告一次性塑料制品的使用和回收情况。"
        ),
        enforcement_detail=(
            "行政处罚（1万至10万元）；没收违法所得；责令整改；信用惩戒。违反禁限制规定"
            "的，由县级以上地方人民政府市场监督管理等有关部门依法查处。未遵守国家有关"
            "禁止、限制使用不可降解塑料袋等一次性塑料制品规定的，依照《固体废物污染环境"
            "防治法》第一百零六条处一万元以上十万元以下的罚款。2025年《生态环境法典》二"
            "审稿引入生产和销售环节的处罚（货值金额1-3倍罚款+没收+吊销许可）。"
        ),
        promotion_detail=(
            "替代产品推广；可降解塑料研发支持；回收体系建设。鼓励使用纸袋、布袋、竹木"
            "制品、可降解塑料等替代产品；支持可降解塑料、再生塑料等绿色包装材料研发和"
            "产业化；推进快递包装回收利用和塑料废弃物回收体系建设。"
        ),
        co_benefits="污染防治；资源节约；循环经济",
        legal_name=(
            "关于进一步加强塑料污染治理的意见（发改环资〔2020〕80号）"
        ),
        legal_url="https://www.ndrc.gov.cn/xxgk/zcfb/tz/202001/t20200119_1219275_ext.html",
        other_links=(
            "十四五塑料污染治理行动方案（发改环资〔2021〕1298号，2021年9月8日）"
            "：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202109/t20210915_1296557_ext.html；"
            "固体废物污染环境防治法（2020年修订，主席令第43号）"
            "：https://www.gov.cn/xinwen/2020-04/30/content_5507561.htm"
        ),
        isic="C20; C22; G47; I55; I56; H53",
        asset="受禁限塑料制品",
        asset_detail=(
            "涵盖多类受禁限塑料制品：（1）超薄塑料购物袋（厚度<0.025mm）—2020年底全"
            "国禁止生产和销售；（2）聚乙烯农用地膜（厚度<0.01mm）—2020年底全国禁止生产"
            "和销售；（3）一次性塑料吸管—2020年底全国餐饮行业禁止使用；（4）一次性发泡"
            "塑料餐具—2020年底全国禁止生产和销售；（5）一次性塑料棉签—2020年底全国禁止"
            "生产；（6）含塑料微珠的日化产品—2022年底全国禁止销售；（7）不可降解一次性"
            "塑料餐具—2020年底地级以上城市建成区餐饮堂食禁止使用，2025年县城建成区餐饮"
            "堂食禁止使用；（8）不可降解塑料包装袋、塑料胶带、一次性塑料编织袋—2025年"
            "底全国邮政快递网点禁止使用；（9）一次性塑料用品（宾馆酒店）—2025年全国星"
            "级宾馆酒店不再主动提供。"
        ),
        enforcement="行政处罚；罚款；没收违法所得",
        mitigation="间接",
        admin_authorities=(
            "国家发展和改革委员会；生态环境部；商务部；国家市场监督管理总局；"
            "国家邮政局；农业农村部"
        ),
        monitoring="政府机构开展的监督检查",
    ),
]


def _load_rows(path: Path) -> list[list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def _write_rows(path: Path, rows: list[list[str]]):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def _approach_code(pid: str) -> str:
    return pid[6:9]


def main():
    for row in ROWS:
        if len(row) != 53:
            print(f"ERROR: {row[0]} has {len(row)} columns, expected 53")
            return 1

    existing = _load_rows(CSV_PATH)
    header, data = existing[0], existing[1:]

    ROWS.sort(key=lambda r: _approach_code(r[0]))

    inserted = 0
    for row in ROWS:
        pid = row[0]
        if any(r[0] == pid for r in data):
            print(f"  {pid} already in CSV — skipping")
            continue

        new_code = _approach_code(pid)

        insert_pos = None
        for i, r in enumerate(data):
            if r[2] != "技术标准":
                continue
            existing_code = _approach_code(r[0])
            if existing_code > new_code:
                insert_pos = i
                break

        if insert_pos is None:
            for i in range(len(data) - 1, -1, -1):
                if data[i][2] == "技术标准":
                    insert_pos = i + 1
                    break

        if insert_pos is None:
            print("ERROR: No Technology standard section found")
            return 1

        data.insert(insert_pos, list(row))
        inserted += 1
        print(f"  Inserted {pid} ({new_code}) at data index {insert_pos}")

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
