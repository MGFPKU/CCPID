"""Fill one speed limit instrument into the CN regulatory instruments CSV.

Single-run helper — appends a new instrument row after the last
Performance standard row (within the same Group → Approach block).

Run from repo root:
    python scripts/_add_spd1.py
"""

import csv
import io
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "outputs" / "CCPID_cn_regulatory_instruments.csv"

HEADER_ROW = (
    "政策工具ID", "工具/子方案", "组别", "路径", "排放部门", "子行业",
    "本国工具名称", "英文工具名称", "政策包", "描述", "目标",
    "减缓相关性", "作用渠道", "国家", "管辖层级", "管辖地名称",
    "通过日期", "生效日期", "终止日期", "最近修订", "最近修订（详情）",
    "状态", "管理机构", "受规制资产", "受规制资产（状态）",
    "受规制资产（详情）", "受规制资产（其他）", "受规制资产（阈值范围）",
    "受规制主体", "受规制主体（详情）", "受规制活动",
    "受规制活动（详情）", "强度（数值）", "强度（单位）",
    "强度（详情）", "要求说明", "合规计算方法I", "合规计算方法II",
    "合规监测", "合规监测详情", "合规执行", "合规执行详情",
    "合规促进", "合规促进详情", "温室气体排放覆盖（绝对量）",
    "温室气体排放覆盖（占国内排放百分比）", "经济行业",
    "受影响的温室气体", "减缓效果", "减缓协同效益",
    "法律文件名称", "法律文件链接", "其他网页链接",
)


def make_row(pid, sector, subsector, name_cn, name_en, description,
             objective, adoption, effective, revision, revision_detail,
             asset, asset_detail, activity_detail,
             intensity_val, intensity_unit, intensity_detail,
             req_spec, monitoring_detail, enforcement_detail,
             promotion_detail, co_benefits, legal_name, legal_url, other_links, isic,
             asset_status="新建；既有", terminated="N/A"):
    """Return a regulatory-instrument CSV row tuple."""
    return (
        pid, "工具", "绩效标准", "速度限值", sector, subsector,
        name_cn, name_en, "N/A", description, objective,
        "间接", "需求侧", "中国", "国家", "N/A",
        adoption, effective, terminated, revision, revision_detail,
        "生效",
        "国务院；公安部；交通运输部",
        asset, asset_status, asset_detail, "N/A", "N/A",
        "企业；个人", "在中国境内道路上行驶机动车的企业和个人。",
        "行驶",
        activity_detail,
        intensity_val, intensity_unit, intensity_detail,
        req_spec,
        "N/A", "N/A",
        "公安机关交通管理部门测速执法；道路监控设备",
        monitoring_detail,
        "罚款；扣分",
        enforcement_detail,
        "其他激励或支持",
        promotion_detail,
        "N/A", "N/A",
        isic,
        "CO2",
        "正向",
        co_benefits,
        legal_name, legal_url, other_links,
    )


ROWS = [
    make_row(
        pid="CHNPRFSPDI01S000",
        sector="交通",
        subsector="道路运输",
        name_cn="机动车行驶速度限制",
        name_en="Motor Vehicle Speed Limits",
        description=(
            "《中华人民共和国道路交通安全法实施条例》（国务院令第405号，2004年公布，2017年修订）"
            "对全国机动车行驶速度按道路类型、车辆类型和气象条件设定统一最高限速。"
            "该速度限制体系通过约束车辆行驶速度降低燃料消耗和温室气体排放。"
        ),
        objective="维护道路交通秩序；预防和减少交通事故；保护人身和财产安全；提高通行效率",
        adoption="30/04/2004",
        effective="01/05/2004",
        revision="07/10/2017",
        revision_detail=(
            "2017年10月7日根据《国务院关于修改部分行政法规的决定》（国务院令第687号）修订，"
            "速度限制核心条款（第四十五、四十六、七十八、八十一条）内容未发生实质性变化。"
            "2021年4月29日《道路交通安全法》修正（主席令第八十一号），违法记分管理办法于"
            "2022年4月1日更新。"
        ),
        asset="机动车",
        asset_detail=(
            "在中国境内道路上行驶的各类机动车，包括小型载客汽车、其他载客汽车、载货汽车、"
            "摩托车、拖拉机、轮式专用机械车等。高速公路按车型和车道分别设定速度限值。"
        ),
        activity_detail=(
            "机动车在高速公路、城市道路和公路上的行驶活动。高速公路还设有最低速度限制"
            "（60km/h）和分车道最低速度（90-110km/h），低能见度条件下按气象条件分级限速。"
        ),
        intensity_val="120",
        intensity_unit="km/h",
        intensity_detail=(
            "高速公路小型载客汽车最高限速120km/h，是现行中国道路体系中的最高允许行驶速度。"
            "不同道路类型和车型的最高限速范围为20-120km/h。违反限速的罚款额度为20-200元"
            "（道路交通安全法第九十条），超速记分标准为一次1-12分（2022年4月1日起施行）。"
        ),
        req_spec=(
            "1）机动车行驶不得超过限速标志、标线标明的最高速度，无限速标志时须遵守法定"
            "最高速度（实施条例第四十五条）；2）遇雾、雨、雪、沙尘、冰雹等低能见度天气及"
            "冰雪、泥泞路面等特殊情形时须遵守降低的速度限值（实施条例第四十六、八十一条）；"
            "3）高速公路须同时遵守最高限速和最低限速（实施条例第七十八条）；4）违反限速"
            "规定处警告或罚款并记分（道路交通安全法第九十条及配套记分管理办法）。"
        ),
        monitoring_detail=(
            "公安机关交通管理部门通过固定测速设备、移动测速设备和区间测速系统对机动车"
            "行驶速度进行监测和执法。高速公路和城市快速路普遍安装测速监控设备。交通违法"
            "行为可通过公安交通管理综合应用平台（交管12123）查询和处理。"
        ),
        enforcement_detail=(
            "《道路交通安全法》第九十条规定违反限速处警告或20元以上200元以下罚款。"
            "《道路交通安全违法行为记分管理办法》（2022年4月1日施行）规定：超速10%-20%"
            "记3分，超速20%-50%记6分，超速50%以上记12分。严重超速可吊销驾驶证。"
        ),
        promotion_detail=(
            "公安机关交通管理部门通过交通安全宣传教育、限速标志和警示标志提醒驾驶员遵守"
            "速度限制；部分地区试点推行经济速度建议标志引导节能驾驶。"
        ),
        co_benefits="交通能效提升；交通能源消耗减少；空气污染物减排",
        legal_name="中华人民共和国道路交通安全法实施条例",
        legal_url="https://www.gov.cn/gongbao/content/2019/content_5468932.htm",
        other_links=(
            "《中华人民共和国道路交通安全法》（2021年修正）："
            "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE3OTZhNjM2YTAxNzk4NTY4YzY1NzA3N2Y"
        ),
        isic="H49",
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

    # Insert after last Performance standard row (same Group → Approach convention)
    insert_pos = None
    for i in range(len(data) - 1, -1, -1):
        if data[i][2] == "绩效标准":
            insert_pos = i + 1  # +1 to insert after this row (data is 0-indexed)
            break

    if insert_pos is None:
        print("ERROR: No Performance standard row found")
        return 1

    for row in ROWS:
        pid = row[0]
        # Check if already in CSV
        if any(r[0] == pid for r in data):
            print(f"  {pid} already in CSV — skipping")
            continue
        data.insert(insert_pos, list(row))
        insert_pos += 1
        print(f"  Inserted {pid} at row {insert_pos}")

    # Write back
    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows)")


if __name__ == "__main__":
    raise SystemExit(main())
