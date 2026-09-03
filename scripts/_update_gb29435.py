#!/usr/bin/env python3
"""Surgical update of CHNPRFEILI63S000 for GB 29435-2025 revision."""

import csv
from pathlib import Path

CSV = Path(__file__).resolve().parents[1] / "outputs" / "CCPID_cn_regulatory_instruments.csv"

with CSV.open("r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.reader(f))
header, data = rows[0], rows[1:]
idx = next(i for i, r in enumerate(data) if r and r[0] == "CHNPRFEILI63S000")
r = data[idx]

# Track changes
changed = []

# [6] Name: remove "加工" — "稀土冶炼加工企业" → "稀土冶炼企业"
old_name = r[6]
r[6] = r[6].replace("加工企业", "企业")
if r[6] != old_name:
    changed.append(f"name: {old_name} → {r[6]}")

# [7] English name
old_en = r[7]
r[7] = "Norm of Energy Consumption per Unit Production of Rare Earth Metallurgical Enterprise"
if r[7] != old_en:
    changed.append(f"en_name: {old_en} → {r[7]}")

# [9] Description: update GB reference and add revision info
# Replace "GB 29435-2012" → "GB 29435-2025", add mention of key changes
old_desc = r[9]
r[9] = r[9].replace("GB 29435-2012", "GB 29435-2025")
r[9] = r[9].replace("2012年12月31日发布", "2025年12月31日第二次修订发布")
# Also update the old effective date sentence
r[9] = r[9].replace("2013年10月1日实施", "2027年1月1日实施（首次发布于2012年12月31日，2013年10月1日首次实施）")
if r[9] != old_desc:
    changed.append("description: updated GB reference and dates")

# [19] Last revision
old_lr = r[19]
r[19] = "31/12/2025"
if r[19] != old_lr:
    changed.append(f"last_revision: {old_lr} → {r[19]}")

# [20] Last revision details
old_lrd = r[20]
r[20] = (
    "首次制定于2012年12月31日（GB 29435-2012《稀土冶炼加工企业单位产品"
    "能源消耗限额》，2013年10月1日实施）。2025年12月31日第二次修订"
    "（GB 29435-2025），名称变更为《稀土冶炼企业单位产品能源消耗限额》，"
    "主要修订包括：删除灯用稀土三基色荧光粉和抛光粉产品；增加钕铁硼废料"
    "综合回收工艺生产的稀土化合物产品类别；将稀土化合物分为4类、稀土金属"
    "及合金分为2类；更改各产品类别能耗限额等级指标值；更改统计范围和计算方法。"
)
if r[20] != old_lrd:
    changed.append("revision_detail: updated")

# [23] Asset: remove "加工"
old_asset = r[23]
r[23] = r[23].replace("加工", "")
if r[23] != old_asset:
    changed.append(f"asset: {old_asset} → {r[23]}")

# [25] Asset details: update scope
old_ad = r[25]
r[25] = r[25].replace(
    "以及稀土荧光粉（红粉荧光粉、蓝粉荧光粉、绿粉荧光粉等）和稀土抛光粉的生产装置",
    "以及钕铁硼废料综合回收工艺生产稀土化合物的装置"
)
r[25] = r[25] + "2025年版删除灯用稀土三基色荧光粉和抛光粉产品，将稀土化合物分为4类、稀土金属及合金分为2类分别设定限额指标。"
if r[25] != old_ad:
    changed.append("asset_details: updated scope")

# [34] Intensity details: mention new categories
old_idet = r[34]
r[34] = r[34] + "2025年版将稀土化合物分为4类、稀土金属及合金分为2类，分别设定差异化限额指标。"
if r[34] != old_idet:
    changed.append("intensity_details: appended category info")

# [50] Legal statute
old_ls = r[50]
r[50] = "GB 29435-2025 稀土冶炼企业单位产品能源消耗限额"
if r[50] != old_ls:
    changed.append(f"legal_statute: {old_ls} → {r[50]}")

# [51] Legal URL
old_lu = r[51]
r[51] = "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=A5998295FAC676B7C86391356A185816"
if r[51] != old_lu:
    changed.append(f"legal_url: updated")

# Print changes
for c in changed:
    print(f"  {c}")

# Write back
with CSV.open("w", encoding="utf-8-sig", newline="") as f:
    csv.writer(f).writerows([header] + data)
print(f"\nUpdated {len(changed)} fields in CHNPRFEILI63S000 — {len(data)} total data rows")
