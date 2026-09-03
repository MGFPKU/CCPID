#!/usr/bin/env python3
"""Insert Voluntary certification and labelling scheme (VLB) instruments
   into the Voluntary CN CSV.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_voluntary_approaches.csv"

CN_HEADER = [
    "政策工具ID", "工具/子方案", "组别", "路径", "排放部门", "子行业",
    "本国名称", "英文名称", "政策包", "描述", "目标", "减缓相关性",
    "作用渠道", "国家", "管辖层级", "管辖地名称", "通过日期", "生效日期",
    "终止日期", "最近修订", "最近修订（详情）", "状态", "管理机构",
    "受规制资产", "受规制资产（状态）", "受规制资产（详情）",
    "受规制资产（其他）", "受规制资产（阈值范围）", "受规制主体",
    "受规制主体（详情）", "受规制活动", "受规制活动（详情）",
    "强度（数值）", "强度（单位）", "强度（详情）", "要求说明",
    "合规计算方法I", "合规计算方法II", "参与激励", "监测", "违规制裁",
    "温室气体排放覆盖（绝对量）", "温室气体排放覆盖（占国内排放百分比）",
    "经济行业", "受影响的温室气体", "减缓效果", "减缓协同效益",
    "法律文件名称", "法律文件链接", "其他网页链接",
]


def make_row(
    pid, group_cn, approach_cn, sector, subsector,
    name_cn, name_en, policy_package, description, objective,
    mitigation, channel, adoption, effective,
    revision, revision_detail, status,
    admin_authorities, asset, asset_status, asset_detail,
    agent, agent_detail, activity, activity_detail,
    intensity_val, intensity_unit, intensity_detail, req_spec,
    calc_i, calc_ii, incentives, monitoring, sanctions,
    ghg_abs, ghg_pct, isic, ghg,
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
        calc_i, calc_ii, incentives, monitoring, sanctions,
        ghg_abs, ghg_pct, isic, ghg,
        mitigation_effects, co_benefits, legal_name, legal_url, other_links,
    )


DATA_PATH = Path(__file__).resolve().parent / "_vlb_data.json"


with open(DATA_PATH, "r", encoding="utf-8") as f:
    _instruments = json.load(f)

GROUP = "自愿性信息工具"
APPROACH = "自愿性认证标识"

ROWS = []
for inst in _instruments:
    ROWS.append(make_row(
        pid=inst["pid"],
        group_cn=GROUP,
        approach_cn=APPROACH,
        sector=inst["sector"],
        subsector=inst["subsector"],
        name_cn=inst["name_cn"],
        name_en=inst["name_en"],
        policy_package=inst["policy_package"],
        description=inst["description"],
        objective=inst["objective"],
        mitigation=inst["mitigation"],
        channel=inst["channel"],
        adoption=inst["adoption"],
        effective=inst["effective"],
        revision=inst["revision"],
        revision_detail=inst["revision_detail"],
        status=inst["status"],
        admin_authorities=inst["admin_authorities"],
        asset=inst["asset"],
        asset_status=inst["asset_status"],
        asset_detail=inst["asset_detail"],
        agent=inst["agent"],
        agent_detail=inst["agent_detail"],
        activity=inst["activity"],
        activity_detail=inst["activity_detail"],
        intensity_val=inst["intensity_val"],
        intensity_unit=inst["intensity_unit"],
        intensity_detail=inst["intensity_detail"],
        req_spec=inst["req_spec"],
        calc_i=inst["calc_i"],
        calc_ii=inst["calc_ii"],
        incentives=inst["incentives"],
        monitoring=inst["monitoring"],
        sanctions=inst["sanctions"],
        ghg_abs=inst["ghg_abs"],
        ghg_pct=inst["ghg_pct"],
        isic=inst["isic"],
        ghg=inst["ghg"],
        mitigation_effects=inst["mitigation_effects"],
        co_benefits=inst["co_benefits"],
        legal_name=inst["legal_name"],
        legal_url=inst["legal_url"],
        other_links=inst["other_links"],
    ))


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

        # Insert after last Voluntary information instrument / VLB row
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][3] == APPROACH:
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
