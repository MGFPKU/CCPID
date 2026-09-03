"""Add 5 fuel economy standard (FEC) instruments to the regulatory instruments CSV.

FEC01: 电动汽车能量消耗量限值 (EV energy consumption limit)
FEC02: 插电式混合动力汽车能量消耗限值 (PHEV energy consumption limit)
FEC03: 乘用车燃料消耗量限值 (Passenger car fuel consumption limit)
FEC04: 轻型商用车辆燃料消耗量限值 (Light commercial vehicle fuel consumption limit)
FEC05: 重型商用车辆燃料消耗量限值 (Heavy commercial vehicle fuel consumption limit)

Usage: python scripts/_add_fec1.py
"""

import csv
import sys
from pathlib import Path

CN_REGULATORY = Path("outputs/CCPID_cn_regulatory_instruments.csv")


def make_row(pid, sector, subsector, name_cn, name_en, description,
             objective, adoption, effective, revision, revision_detail,
             asset, asset_detail, agent_detail, activity_detail,
             intensity_val, intensity_unit, intensity_detail,
             req_spec, monitoring_detail, enforcement_detail,
             promotion_detail, co_benefits, legal_name, legal_url, other_links, isic,
             asset_status="新建；既有", terminated="N/A"):
    return {
        "政策工具ID": pid,
        "工具/子方案": "工具",
        "组别": "绩效标准",
        "路径": "燃油经济性标准",
        "排放部门": sector,
        "子行业": subsector,
        "本国工具名称": name_cn,
        "英文工具名称": name_en,
        "政策包": "N/A",
        "描述": description,
        "目标": objective,
        "减缓相关性": "直接",
        "作用渠道": "供给侧",
        "国家": "中国",
        "管辖层级": "国家",
        "管辖地名称": "N/A",
        "通过日期": adoption,
        "生效日期": effective,
        "终止日期": terminated,
        "最近修订": revision,
        "最近修订（详情）": revision_detail,
        "状态": "生效",
        "管理机构": "工业和信息化部；国家市场监督管理总局；国家标准化管理委员会",
        "受规制资产": asset,
        "受规制资产（状态）": asset_status,
        "受规制资产（详情）": asset_detail,
        "受规制资产（其他）": "N/A",
        "受规制资产（阈值范围）": "N/A",
        "受规制主体": "企业",
        "受规制主体（详情）": agent_detail,
        "受规制活动": "销售",
        "受规制活动（详情）": activity_detail,
        "强度（数值）": intensity_val,
        "强度（单位）": intensity_unit,
        "强度（详情）": intensity_detail,
        "要求说明": req_spec,
        "合规计算方法I": "N/A",
        "合规计算方法II": "N/A",
        "合规监测": "政府机构开展的型式批准和一致性监督检查；企业能耗数据报告",
        "合规监测详情": monitoring_detail,
        "合规执行": "合规命令；罚款；禁止生产和销售",
        "合规执行详情": enforcement_detail,
        "合规促进": "其他激励或支持",
        "合规促进详情": promotion_detail,
        "温室气体排放覆盖（绝对量）": "N/A",
        "温室气体排放覆盖（占国内排放百分比）": "N/A",
        "经济行业": isic,
        "受影响的温室气体": "CO2",
        "减缓效果": "正向",
        "减缓协同效益": co_benefits,
        "法律文件名称": legal_name,
        "法律文件链接": legal_url,
        "其他网页链接": other_links,
    }


# -- FEC01: 电动汽车能量消耗量限值 (EV energy consumption limit) --
# GB/T 36980-2018 (recommended) → GB 36980.1-2025 (mandatory)
FEC01 = make_row(
    "CHNPRFFECI01S000",
    "交通", "轻型乘用车",
    "电动汽车能量消耗量限值",
    "Electric Vehicle Energy Consumption Limit",
    (
        "GB 36980.1-2025《电动汽车能量消耗量限值 第1部分：乘用车》是强制性国家标准，"
        "于2025年5月30日发布，2026年1月1日实施，替代GB/T 36980-2018。"
        "适用于最大设计总质量不超过3500kg的M1类纯电动乘用车，"
        "规定车辆在电量消耗模式下的电能消耗量限值。"
        "该标准是全球首个电动汽车电耗限值强制性标准，"
        "将原推荐性标准升级为强制性标准，限值较上一版加严约11%。"
    ),
    "提高能效；减少能耗",
    "28/12/2018", "01/07/2019",
    "30/05/2025",
    "2025年5月30日发布GB 36980.1-2025替代GB/T 36980-2018，将推荐性标准升级为强制性标准，限值加严约11%，于2026年1月1日实施。",
    "纯电动乘用车",
    "以车载电源为唯一动力或主要动力来源、最大设计总质量不超过3500kg的M1类纯电动乘用车。按整备质量分组采用阶梯式限值。",
    "在中国境内生产和销售纯电动乘用车的汽车制造企业。",
    "纯电动乘用车型式批准和销售活动。新申请型式批准的车型自2026年1月1日起执行新限值，已获型式批准的车型自2028年1月1日起执行。",
    "按车重阶梯式", "kWh/100km",
    (
        "按整备质量分组设定电能消耗量限值，采用阶梯式限值评价体系。"
        "限值基于WLTC或中国工况测试循环测定。"
        "约2吨整备质量的车型百公里电耗限值约15.1kWh/100km。"
    ),
    (
        "1）新申请型式批准的车型须满足GB 36980.1-2025规定的电能消耗量限值方可上市销售；"
        "2）已获得型式批准的车型须在过渡期内（至2028年1月1日）达到新限值要求；"
        "3）不满足限值要求的车型不得生产和销售。"
    ),
    "工业和信息化部对车辆进行型式批准，对电动汽车电能消耗量进行一致性监督检查；汽车制造企业须按规定报送车辆能量消耗量数据，接受节能监察。",
    "对不符合电能消耗量限值标准的电动汽车车型，由工业和信息化部责令限期整改；未按要求整改的车型撤销型式批准，禁止生产和销售。",
    "国家鼓励汽车制造企业研发和应用先进节能技术，降低电动汽车电能消耗量，通过新能源汽车推广政策和绿色消费引导支持高效节能车型。",
    "交通能效提升；交通能源消耗减少",
    "GB 36980.1-2025 电动汽车能量消耗量限值 第1部分：乘用车",
    "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=957BCBA7091D453922DE63158D8419AB",
    "GB/T 36980-2018（旧版）：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C572EE48E680FB763D856F07EC26C09D",
    "C29",
)

# -- FEC02: 插电式混合动力汽车能量消耗限值 (PHEV energy consumption limit) --
# PHEV electricity consumption limits are set under GB 36980.1-2025;
# fuel consumption in charge-sustaining mode under GB 19578-2024
FEC02 = make_row(
    "CHNPRFFECI02S000",
    "交通", "轻型乘用车",
    "插电式混合动力汽车能量消耗限值",
    "Plug-in Hybrid Electric Vehicle Energy Consumption Limit",
    (
        "GB 36980.1-2025《电动汽车能量消耗量限值 第1部分：乘用车》适用于"
        "插电式（含增程式）混合动力乘用车在电量消耗模式下的电能消耗量限值；"
        "GB 19578-2024《乘用车燃料消耗量限值》适用于其在电量保持模式下的"
        "燃料消耗量限值。两项标准均为强制性国家标准，于2026年1月1日实施。"
        "适用于最大设计总质量不超过3500kg的M1类插电式混合动力乘用车。"
        "根据工信部2025年第24号公告，插电式混合动力乘用车电能消耗量须小于"
        "GB 36980.1-2025对应车型限值的140%（整备质量<2510kg）或145%（≥2510kg），"
        "燃料消耗量须小于GB 19578-2024对应车型限值的70%（<2510kg）或75%（≥2510kg）。"
    ),
    "提高能效；减少能耗",
    "28/12/2018", "01/07/2019",
    "30/05/2025",
    "2025年5月30日发布GB 36980.1-2025将插电式混合动力乘用车纳入适用范围，2026年1月1日实施。工信部2025年第24号公告同步明确了2026-2027年减免车辆购置税的具体技术指标要求。",
    "插电式混合动力乘用车",
    "具有外部充电接口、可外接充电、具备纯电动行驶模式的M1类混合动力乘用车（含增程式），纯电续驶里程不低于43km（等效全电里程不低于100km），最大设计总质量不超过3500kg。",
    "在中国境内生产和销售插电式混合动力乘用车的汽车制造企业。",
    "插电式混合动力乘用车型式批准和销售活动。车型须同时满足电量消耗模式下的电能消耗量限值和电量保持模式下的燃料消耗量限值。",
    "按车重阶梯式", "kWh/100km；L/100km",
    (
        "电能消耗量（电量消耗模式）：须小于GB 36980.1-2025对应车型限值的140%（整备质量<2510kg）或145%（整备质量≥2510kg）。"
        "燃料消耗量（电量保持模式）：须小于GB 19578-2024对应车型限值的70%（整备质量<2510kg）或75%（整备质量≥2510kg）。"
    ),
    (
        "1）新申请型式批准的插电式混合动力乘用车须同时满足电能消耗量和燃料消耗量限值要求方可上市销售；"
        "2）已获得型式批准的车型须在过渡期内达到新限值要求；"
        "3）不满足限值要求的车型不得生产和销售。"
    ),
    "工业和信息化部对车辆进行型式批准和一致性监督检查；汽车制造企业须按规定报送车辆能量消耗量数据。",
    "对不符合能量消耗限值标准的插电式混合动力车型，由工业和信息化部责令限期整改；未按要求整改的车型撤销型式批准，禁止生产和销售。",
    "国家鼓励汽车制造企业研发和应用先进混合动力技术，通过购置税减免等财税政策支持高效节能的插电式混合动力车型推广应用。",
    "交通能效提升；交通能源消耗减少",
    "GB 36980.1-2025 电动汽车能量消耗量限值 第1部分：乘用车",
    "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=957BCBA7091D453922DE63158D8419AB",
    "GB/T 36980-2018（旧版）：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C572EE48E680FB763D856F07EC26C09D",
    "C29",
)

# -- FEC03: 乘用车燃料消耗量限值 (Passenger car fuel consumption limit) --
# GB 19578-2004 → GB 19578-2014 → GB 19578-2021 → GB 19578-2024
FEC03 = make_row(
    "CHNPRFFECI03S000",
    "交通", "轻型乘用车",
    "乘用车燃料消耗量限值",
    "Passenger Car Fuel Consumption Limit",
    (
        "GB 19578-2024《乘用车燃料消耗量限值》是强制性国家标准，"
        "于2024年11月28日发布，2026年1月1日实施，替代GB 19578-2021。"
        "适用于能够燃用汽油或柴油燃料、最大设计总质量不超过3500kg的M1类车辆，"
        "不适用于仅燃用气体燃料或醇醚类燃料的车辆。"
        "是中国首个控制汽车燃料消耗量的强制性国家标准（GB 19578-2004于2004年发布），"
        "历经2014版、2021版、2024版三次修订，2024版限值较2021版加严约18%。"
    ),
    "提高能效；减少能耗",
    "02/09/2004", "01/07/2005",
    "28/11/2024",
    "2024年11月28日发布GB 19578-2024替代GB 19578-2021，限值加严约18%，于2026年1月1日实施。",
    "传统能源乘用车",
    "能够燃用汽油或柴油燃料、最大设计总质量不超过3500kg的M1类乘用车。不包括仅燃用气体燃料或醇醚类燃料的车辆。按整备质量分组采用阶梯式限值，测试工况采用WLTC或中国工况。",
    "在中国境内生产和销售乘用车的汽车制造企业。",
    "乘用车型式批准和销售活动。新申请型式批准的车型自2026年1月1日起执行GB 19578-2024限值；已获型式批准的车型须在过渡期内达标。",
    "按车重阶梯式", "L/100km",
    (
        "按整备质量分组设定燃料消耗量限值，采用阶梯式限值评价体系。"
        "测试工况为WLTC或中国工况循环。"
        "以约1.5吨整备质量的自动挡车型为例，百公里油耗限值约7.74L/100km。"
    ),
    (
        "1）新申请型式批准的乘用车须满足GB 19578-2024规定的燃料消耗量限值方可上市销售；"
        "2）已获得型式批准的车型须在过渡期内达到新限值要求；"
        "3）不满足限值要求的车型不得生产和销售。"
    ),
    "工业和信息化部对车辆进行型式批准和一致性监督检查；汽车制造企业须按规定报送车辆燃料消耗量数据，接受节能监察。",
    "对不符合燃料消耗量限值标准的车型，由工业和信息化部责令限期整改；未按要求整改的车型撤销型式批准，禁止生产和销售。",
    "国家鼓励汽车制造企业研发和应用先进节能技术，降低车辆燃料消耗量，通过企业平均燃料消耗量（CAFC）核算体系引导行业持续提升能效。",
    "交通能效提升；交通能源消耗减少；温室气体减排；空气污染物减排",
    "GB 19578-2024 乘用车燃料消耗量限值",
    "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=B9F662A5B1E5FA3AAC7914AECA3152DA",
    "GB 19578-2021（旧版）：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=2C4E76A2B4D0D6D9E05397BE0A0A5A8F",
    "C29",
)

# -- FEC04: 轻型商用车辆燃料消耗量限值 (Light commercial vehicle fuel consumption limit) --
# GB 20997-2007 → GB 20997-2015 → GB 20997-2024
FEC04 = make_row(
    "CHNPRFFECI04S000",
    "交通", "轻型商用车",
    "轻型商用车辆燃料消耗量限值",
    "Light-Duty Commercial Vehicle Fuel Consumption Limit",
    (
        "GB 20997-2024《轻型商用车辆燃料消耗量限值及评价指标》是强制性国家标准，"
        "于2024年8月23日发布，2026年1月1日实施，替代GB 20997-2015。"
        "适用于能够燃用汽油或柴油燃料、最大设计总质量不超过3500kg的"
        "N1类和M2类商用车辆，2024版新增纯电动、混合动力、燃料电池和甲醇等"
        "新能源车型的燃料消耗量折算要求。"
        "该标准于2007年首次发布，历经2015版、2024版两次修订，"
        "2024版单车限值较2015版加严约10%，并引入企业平均管理模式（CAFC）。"
    ),
    "提高能效；减少能耗",
    "30/07/2007", "01/01/2009",
    "23/08/2024",
    "2024年8月23日发布GB 20997-2024替代GB 20997-2015，单车限值加严约10%，新增新能源车型纳入管理，引入企业平均管理模式，于2026年1月1日实施。",
    "轻型商用车辆",
    "能够燃用汽油或柴油燃料、最大设计总质量不超过3500kg的N1类（货车）和M2类（客车）商用车辆。2024版将适用范围扩大至纯电动、混合动力、燃料电池和甲醇等新能源商用车型。",
    "在中国境内生产和销售轻型商用车辆的汽车制造企业。",
    "轻型商用车辆的型式批准和销售活动。新申请型式批准的车型自2026年1月1日起执行GB 20997-2024限值；已获型式批准的车型须在过渡期内达标。",
    "按车重阶梯式", "L/100km",
    (
        "按车辆总质量和车型类别分组设定燃料消耗量限值，采用线性阶梯式限值体系。"
        "测试工况从NEDC循环切换为WLTC或中国工况。"
        "单车限值较三阶段（GB 20997-2015）加严10%。"
    ),
    (
        "1）新申请型式批准的轻型商用车辆须满足GB 20997-2024规定的燃料消耗量限值方可上市销售；"
        "2）已获得型式批准的车型须在过渡期内达到新限值要求；"
        "3）企业平均燃料消耗量（CAFC）须满足阶段目标要求；"
        "4）不满足限值要求的车型不得生产和销售。"
    ),
    "工业和信息化部对车辆进行型式批准和一致性监督检查；汽车制造企业须按规定报送车辆燃料消耗量数据和企业平均燃料消耗量核算报告。",
    "对不符合燃料消耗量限值标准的车型，由工业和信息化部责令限期整改；未按要求整改的车型撤销型式批准，禁止生产和销售。",
    "国家鼓励汽车制造企业研发和应用先进节能技术，通过企业平均燃料消耗量管理赋予企业合规灵活性，推动行业持续节能减排。",
    "交通能效提升；交通能源消耗减少；温室气体减排；空气污染物减排",
    "GB 20997-2024 轻型商用车辆燃料消耗量限值及评价指标",
    "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=47E98BA6D15D541E9F00FDD0A738C291",
    "GB 20997-2015（旧版）：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=71F772D80F8CD3A7E05397BE0A0AB82A",
    "C29",
)

# -- FEC05: 重型商用车辆燃料消耗量限值 (Heavy commercial vehicle fuel consumption limit) --
# GB 30510-2014 → GB 30510-2018 → GB 30510-2024
FEC05 = make_row(
    "CHNPRFFECI05S000",
    "交通", "重型商用车",
    "重型商用车辆燃料消耗量限值",
    "Heavy-Duty Commercial Vehicle Fuel Consumption Limit",
    (
        "GB 30510-2024《重型商用车辆燃料消耗量限值》是强制性国家标准，"
        "于2024年9月29日发布，2025年7月1日实施，替代GB 30510-2018。"
        "适用于能够燃用汽油或柴油燃料、最大设计总质量大于3500kg的商用车辆，"
        "包括货车、半挂牵引车、普通客车、自卸汽车和城市客车，"
        "不适用于专项作业车。"
        "该标准于2014年首次发布，历经2018版、2024版两次修订，"
        "2024版限值较2018版降低约10%（降幅6%~13%）。"
    ),
    "提高能效；减少能耗",
    "01/02/2014", "01/07/2014",
    "29/09/2024",
    "2024年9月29日发布GB 30510-2024替代GB 30510-2018，限值降低约10%，于2025年7月1日实施（新车型）/2027年7月1日（已获证车型）。",
    "重型商用车辆",
    "能够燃用汽油或柴油燃料、最大设计总质量大于3500kg的商用车辆，包括货车、半挂牵引车、普通客车、自卸汽车和城市客车。不适用于专项作业车。",
    "在中国境内生产和销售重型商用车辆的汽车制造企业。",
    "重型商用车辆的型式批准和销售活动。新委托型式批准的车型自2025年7月1日起执行GB 30510-2024限值；已获型式批准的车型自2027年7月1日起执行。",
    "按车重和车型", "L/100km",
    (
        "按车辆总质量、车型类别和用途分组设定燃料消耗量限值，采用阶梯式限值体系。"
        "根据不同车型和总质量，2024版限值较2018版降低6%~13%。"
    ),
    (
        "1）新申请型式批准的重型商用车辆须满足GB 30510-2024规定的燃料消耗量限值方可上市销售；"
        "2）已获得型式批准的车型须在过渡期内（至2027年7月1日）达到新限值要求；"
        "3）不满足限值要求的车型不得生产和销售。"
    ),
    "工业和信息化部对车辆进行型式批准和一致性监督检查；汽车制造企业须按规定报送车辆燃料消耗量数据，接受节能监察。",
    "对不符合燃料消耗量限值标准的重型商用车型，由工业和信息化部责令限期整改；未按要求整改的车型撤销型式批准，禁止生产和销售。",
    "国家鼓励汽车制造企业研发和应用先进节能技术，降低重型商用车辆燃料消耗量，推动商用车节能技术升级。",
    "交通能效提升；交通能源消耗减少；温室气体减排；空气污染物减排",
    "GB 30510-2024 重型商用车辆燃料消耗量限值",
    "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=35651BC9CFA4506EB75F140E59A4F73D",
    "GB 30510-2018（旧版）：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=0FECA2934941502E161716E7F2502E76",
    "C29",
)


def main():
    # Read existing CSV
    with open(CN_REGULATORY, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Find insertion point: after the last performance standard row
    # (Performance standard instruments currently end with EIL66)
    instruments = [FEC01, FEC02, FEC03, FEC04, FEC05]

    # Find last performance standard row
    insert_after = None
    for i, row in enumerate(rows):
        if row["组别"] == "绩效标准":
            insert_after = i

    if insert_after is None:
        print("ERROR: No performance standard rows found.")
        sys.exit(1)

    print(f"Inserting after row {insert_after + 2} (Excel): {rows[insert_after]['政策工具ID']}")

    # Insert new rows
    result = rows[:insert_after + 1] + instruments + rows[insert_after + 1:]
    print(f"Inserted {len(instruments)} instruments. Total rows: {len(rows)} → {len(result)}")

    # Write back
    with open(CN_REGULATORY, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)

    print(f"Wrote {len(result)} rows to {CN_REGULATORY}")
    for inst in instruments:
        print(f"  {inst['政策工具ID']}: {inst['本国工具名称']}")


if __name__ == "__main__":
    main()
