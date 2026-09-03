#!/usr/bin/env python3
"""Add GB 30255-2026 to the Regulatory CN CSV (PRFMEAI30)."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_regulatory_instruments.csv"

ROW = [
    "CHNPRFMEAI30S000",
    "工具",
    "绩效标准",
    "用能产品最低能源绩效标准",
    "工业；建筑",
    "照明；商业建筑；住宅建筑；公共建筑",
    "室内照明用LED产品能效限定值及能效等级",
    "Minimum Allowable Values of Energy Efficiency and Energy Efficiency Grades for Indoor Lighting LED Products",
    "N/A",
    # Description
    "GB 30255-2026《室内照明用LED产品能效限定值及能效等级》是强制性国家标准，于2026年2月27日发布，2027年9月1日实施，替代GB 30255-2019。该标准适用于室内照明用LED产品，包括非定向自镇流LED灯、LED筒灯（含小光束角射灯）、集成式LED灯、LED高天棚灯、替换型双端LED灯以及具备调光、调色等附加功能的LED室内照明产品。能效等级分为3级（1级最高），3级为能效限定值即强制市场准入门槛。与旧版相比，新标准扩展了产品覆盖范围（新增小光束角LED筒灯、LED高天棚灯、替换型双端LED灯），提升了各等级能效指标，并新增待机功率要求（≤1.5W），推动从运行能效向全时能效延伸。",
    "提高LED照明产品能效；减少建筑照明用电",
    "直接",
    "供给侧",
    "中国",
    "国家",
    "N/A",
    "18/12/2013",         # 最早版本 GB 30255-2013
    "01/09/2014",         # 最早版本生效日期
    "N/A",
    "27/02/2026",         # 最近修订
    # 最近修订（详情）
    "首次制定于2013年12月18日（GB 30255-2013《普通照明用非定向自镇流LED灯能效限定值及能效等级》，2014年9月1日实施）。2019年第一次修订（GB 30255-2019），名称变更为《室内照明用LED产品能效限定值及能效等级》，扩展产品覆盖范围。2026年2月27日第二次修订（GB 30255-2026），新增小光束角LED筒灯、LED高天棚灯、替换型双端LED灯及智能调控产品覆盖，提升各等级能效指标，新增待机功率≤1.5W要求，推动全时能效评价。过渡期25个月，自2027年9月1日起第25个月开始强制执行。",
    "生效",
    "国家市场监督管理总局；国家标准化管理委员会",
    "室内照明用LED产品",
    "新建",
    # Asset details
    "室内照明用LED产品，包括非定向自镇流LED灯（以交流市电或直流电驱动，可取代白炽灯及自镇流荧光灯的普通照明用LED灯）、LED筒灯和射灯（含小光束角射灯，光束角≤30°）、集成式LED灯（含标准接口的LED替换光源和一体化灯具）、LED高天棚灯（安装高度≥5m的工业及商业场所用LED照明灯具）、替换型双端LED灯（替代双端荧光灯的LED灯管），以及具备调光、调色、传感联动等附加功能的LED室内照明产品。显色指数要求：LED筒灯和集成式LED灯Ra≥80，LED高天棚灯和替换型双端LED灯Ra≥70，R9实测值>0。",
    "N/A",
    "N/A",
    "企业",
    "在中国境内生产、进口或销售室内照明用LED产品的生产企业和进口商。",
    "生产；销售；进口",
    "室内照明用LED产品的生产、进口和销售活动。产品须达到标准规定的能效限定值方可进入市场。",
    "3级",
    "能效等级",
    # Intensity details
    "能效等级分为3级（1级最高），3级为能效限定值即市场准入最低要求。以初始光效（lm/W）为评价指标，按产品类型（非定向自镇流LED灯、LED筒灯、集成式LED灯、LED高天棚灯、替换型双端LED灯）和色温/显色指数分级设定限值。新标准适度提升3级准入门槛，进一步提高2级节能型产品技术要求，对高显色性、防眩光、智能调控等高端产品给出能效修正系数。具有待机模式的产品待机功率不得超过1.5W。",
    # Requirement specification
    "1）室内照明用LED产品须达到标准规定的能效限定值（3级）方可生产、进口或销售；2）产品须标注能效等级标识；3）能效等级分为1级（最高）、2级、3级，3级为市场准入最低要求；4）具有待机模式的产品待机功率不得超过1.5W；5）LED筒灯和集成式LED灯显色指数Ra≥80，LED高天棚灯和替换型双端LED灯Ra≥70，R9实测值>0。",
    "N/A",
    "N/A",
    "政府机构开展的监督检查",
    "市场监督管理部门对室内照明用LED产品进行能效标识监督检查和产品质量监督抽查。检查内容包括能效等级标注的准确性、产品实际能效是否符合标称等级、待机功率是否符合限值要求、显色指数是否符合标准等。",
    "合规命令；罚款",
    "对生产、进口、销售不符合强制性能效标准的室内照明用LED产品的，由市场监督管理部门责令停止生产、进口、销售，没收违法所得，并处罚款；情节严重的，吊销营业执照。",
    "其他激励或支持",
    "国家鼓励生产和使用1级、2级高效室内照明用LED产品；通过节能产品认证、政府绿色采购等措施引导高效LED照明产品市场推广；鼓励企业对标1级能效开展技术升级。",
    "N/A",
    "N/A",
    "C27",                # ISIC - lighting equipment
    "CO2",
    "正向",
    "建筑照明能效提升；建筑能源消耗减少；绿色建筑发展",
    "GB 30255-2026 室内照明用LED产品能效限定值及能效等级",
    "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C037214954746E0BFCE4CBE3CD779A7C",
    "N/A",
]


def _load_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def _write_rows(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main():
    if len(ROW) != 53:
        print(f"ERROR: {ROW[0]} has {len(ROW)} columns, expected 53")
        return 1

    existing = _load_rows(CSV_PATH)
    header, data = existing[0], existing[1:]

    pid = ROW[0]
    existing_idx = next((i for i, r in enumerate(data) if r and r[0] == pid), None)
    if existing_idx is not None:
        if data[existing_idx] != list(ROW):
            data[existing_idx] = list(ROW)
            print(f"  Updated {pid} in place at data index {existing_idx}")
        else:
            print(f"  {pid} already up to date -- skipping")
            return 0

    # Insert after last PRFMEAI row
    insert_pos = len(data)
    for i in range(len(data)):
        if data[i] and data[i][0].startswith("CHNPRFMEA"):
            insert_pos = i + 1

    data.insert(insert_pos, list(ROW))
    print(f"  Inserted {pid} at data index {insert_pos}")

    data = [r for r in data if any(r)]
    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
