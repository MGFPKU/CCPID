#!/usr/bin/env python3
"""Add CHNPPCGPPI06S000: Government procurement supporting green & low-carbon highway pilot."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_government_i_c.csv"

ROW = [
    "CHNPPCGPPI06S000",
    "Instrument",
    "Public procurement",
    "Green public procurement",
    "Transport",
    "Road transport and infrastructure",
    "政府采购支持公路绿色低碳发展试点",
    "Government Procurement Supporting Green and Low-Carbon Highway Development Pilot",
    "N/A",
    # Description
    (
        "财政部、交通运输部联合印发关于组织开展"政府采购支持公路绿色低碳发展""
        "试点工作的通知（财库〔2025〕32号，2025年12月18日），试点期3年，原则上2028年"
        "12月31日前申请验收。试点范围为国道、省道、县道、乡道等各级公路（含高速公路），"
        "覆盖规划、可行性研究、设计、招标（采购）、施工、运营、养护等各阶段。试点核心"
        "内容：（1）制定发布政府采购支持公路绿色低碳发展基本要求（试行），形成客观、量化、"
        "可验证、可推广的政府采购需求标准；（2）将需求标准嵌入招标文件作为实质性要求或加分项，"
        "在公路建设全流程落实绿色低碳政策；（3）对绿色材料探索批量集中采购，鼓励通过电子化"
        "政府采购平台采购；（4）推动新材料、新技术、新工艺、新方法（"四新"技术）在公路"
        "建设中的应用。符合条件的试点任务可按程序纳入交通强国专项试点，纳入试点且符合信贷"
        "要求的项目可申请绿色金融支持。"
    ),
    "Promote green and low-carbon highway development; Reduce carbon emissions from road construction and operation; Scale up green procurement in transport infrastructure",
    "Direct",
    "Demand-side",
    "CHN",
    "National",
    "N/A",
    "18/12/2025",
    "18/12/2025",
    "N/A",
    "N/A",
    "N/A",
    "In force",
    (
        "财政部（主管政府采购政策制定、绿色采购需求标准发布）；"
        "交通运输部（主管公路建设、运营和养护绿色技术标准制定和项目推进）；"
        "试点实施单位所在地省级财政部门和交通运输主管部门（统筹试点申报和实施管理）；"
        "试点实施单位（设区的市级以上交通运输主管部门，负责试点项目的具体组织实施）"
    ),
    "Road transport infrastructure",
    "New; existing",
    # Asset details
    (
        "国道、省道、县道、乡道等各级公路（含高速公路），涵盖新建、在建及运营养护"
        "项目。试点项目须具备应用"四新"技术（新材料、新技术、新工艺、新方法）的"
        "条件，包括但不限于：温拌沥青、再生沥青混合料、工业固废路基填料、高性能混凝土、"
        "光伏路面、低碳养护技术、智能建造装备等绿色低碳公路技术和材料。试点地区须具备"
        "较好的绿色低碳技术应用基础（交通资源循环利用较好、政府绿色采购政策实施情况"
        "较好等）。单个地市可将多个不同类型项目打包一并申报。"
    ),
    "N/A",
    "N/A",
    "Government",
    (
        "试点实施单位为设区的市级以上交通运输主管部门。事业单位、央企或地方国企"
        "原则上不单独作为申报主体，但可承担具体实施工作。省级财政部门和交通运输"
        "主管部门为试点组织单位，负责择优推荐。"
    ),
    "Purchase or use; Investment",
    (
        "试点实施单位在编制招标（采购）文件时须将政府采购支持公路绿色低碳发展基本"
        "要求（试行）作为实质性要求或加分项嵌入。设计单位按需求标准编制设计文件。"
        "施工单位按设计文件和合同要求采用绿色低碳技术和材料。对绿色材料可实施批量集中"
        "采购，鼓励通过电子化政府采购平台采购。试点项目完成竣（交）工验收后30日内"
        "编制验收评估申请报告。鼓励运用大数据、区块链等技术手段跟踪试点情况。"
    ),
    "N/A",
    "N/A",
    (
        "本工具为政府采购需求标准机制，非财政补贴类工具，无直接金额型政策强度指标。"
        "通过政府采购市场力量拉动公路绿色低碳技术和材料需求。纳入试点且符合信贷要求"
        "的项目可申请绿色金融支持。"
    ),
    # Requirement specification
    (
        "1. 制定发布政府采购支持公路绿色低碳发展基本要求（试行），形成客观、量化、"
        "可验证、可推广的需求标准，并动态调整；"
        "2. 在招标（采购）文件中将需求标准作为实质性要求或加分项，在公路建设规划、"
        "可行性研究、设计、招标（采购）、施工、运营、养护、验收全流程中落实绿色低碳政策；"
        "3. 对绿色材料可实施批量集中采购，鼓励通过电子化政府采购平台采购；"
        "4. 试点项目须应用"四新"技术（新材料、新技术、新工艺、新方法），形成良好示范效应；"
        "5. 试点地区管辖范围内公路项目近3年未发生较大及以上等级生产安全事故；"
        "6. 试点项目完成竣（交）工验收后30日内，编制验收评估申请报告逐级上报；"
        "7. 每年1月31日前报送上年度试点总结报告。"
    ),
    "N/A",
    "N/A",
    "公开招标",
    (
        "满足政府采购支持公路绿色低碳发展基本要求（试行）为采购实质性要求或加分项"
    ),
    "财政部门监管；交通运输部门项目监管",
    "合同执行",
    "N/A",
    (
        "未公开。试点尚在申报批复阶段（首批申报2026年1月31日截止，2026年3月6日前批复），"
        "尚无年度支出数据。通过政府采购市场力量拉动绿色公路技术和材料需求。"
    ),
    "N/A",
    "N/A",
    "F42",
    "CO2",
    "Positive",
    (
        "节能；污染防治；循环经济；技术创新；绿色产业发展"
    ),
    "关于组织开展"政府采购支持公路绿色低碳发展"试点工作的通知（财库〔2025〕32号）",
    "https://www.gov.cn/zhengce/zhengceku/202601/content_7055549.htm",
    "https://m.mof.gov.cn/zcfb/202601/t20260104_3981293.htm",
]


def _load_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def _write_rows(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        csv.writer(handle).writerows(rows)


def main():
    # Verify column count
    existing = _load_rows(CSV_PATH)
    expected_cols = len(existing[0])
    if len(ROW) != expected_cols:
        print(f"ERROR: {ROW[0]} has {len(ROW)} columns, expected {expected_cols}")
        return 1

    header, data = existing[0], existing[1:]

    pid = ROW[0]
    existing_idx = next((i for i, r in enumerate(data) if r and r[0] == pid), None)
    if existing_idx is not None:
        data[existing_idx] = list(ROW)
        print(f"  Updated {pid} in place at data index {existing_idx}")
    else:
        # Insert after last GPP row
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][0].startswith("CHNPPCGPP"):
                insert_pos = i + 1
        data.insert(insert_pos, list(ROW))
        print(f"  Inserted {pid} at data index {insert_pos}")

    # Remove empty rows
    data = [r for r in data if any(r)]
    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
