"""Insert Voluntary target (VTG) instruments into Voluntary CN CSV.

Run from repo root:
    python scripts/_add_vol_vtg.py
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_voluntary_approaches.csv"

GROUP = "自愿性目标"
APPROACH = "自愿性目标"


def make_row(pid, name_cn, name_en, sector, subsector, policy_package,
             description, objective, mitigation, channel,
             adoption, effective, revision, revision_detail, status,
             admin_authorities, asset, asset_status, asset_detail,
             agent, agent_detail, activity, activity_detail,
             intensity_val, intensity_unit, intensity_detail, req_spec,
             calc_i, calc_ii, incentives, monitoring, sanctions,
             ghg_abs, ghg_pct, isic, ghg,
             mitigation_effects, co_benefits, legal_name, legal_url, other_links):
    return [
        pid, "工具", GROUP, APPROACH, sector, subsector,
        name_cn, name_en, policy_package, description, objective,
        mitigation, channel, "中国", "国家", "N/A",
        adoption, effective, "N/A", revision, revision_detail, status,
        admin_authorities, asset, asset_status, asset_detail,
        "N/A", "N/A", agent, agent_detail, activity, activity_detail,
        intensity_val, intensity_unit, intensity_detail, req_spec,
        calc_i, calc_ii, incentives, monitoring, sanctions,
        ghg_abs, ghg_pct, isic, ghg,
        mitigation_effects, co_benefits, legal_name, legal_url, other_links,
    ]


ROWS = [
    make_row(
        pid="CHNVTGVTGI01S000",
        name_cn="家电生产企业回收目标责任制",
        name_en="Home Appliance Manufacturer Recycling Target Responsibility System",
        sector="工业",
        subsector="家电",
        policy_package="N/A",
        description=(
            "家电生产企业回收目标责任制是由国家发展改革委、工业和信息化部、生态环境部"
            "联合建立的自愿性目标责任框架，引导家电生产企业自主设定废旧家电回收量化目标"
            "并公开承诺，推动落实生产者责任延伸制度。通知（发改产业〔2021〕1102号）明确"
            "在电视机、电冰箱、洗衣机、空调器四类家电产品中，鼓励生产企业按年度确定回收"
            "量和回收率等量化目标，并围绕六大行动推进实施：明确回收目标（回收量/回收率"
            "占评估权重70%，回收行为目标占30%）；拓展回收渠道（利用销售网络、售后服务"
            "和电商平台开展逆向回收和以旧换新）；优化存储与运输网络；加强流向管理"
            "（统一编码、转运联单，全流程可追溯，废旧家电须交由有资质企业规范拆解）；"
            "推动绿色发展（提升再生原料加工水平和采购比例，优化产品易回收易拆解设计）；"
            "以及政策激励约束。责任企业于每年1月31日前提交申请报告，三部委于每年3月底前"
            "公布责任企业名单及回收目标；企业开展年度自我评价并公开发布，三部委按年度"
            "跟踪评估。总体目标为到2023年发展一批示范标杆。参与为自愿性质，不设强制性"
            "合规义务和处罚。"
        ),
        objective="落实生产者责任延伸制度，提升废旧家电规范回收利用率",
        mitigation="间接",
        channel="供给侧",
        adoption="27/07/2021",
        effective="04/08/2021",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "国家发展和改革委员会（产业发展司，牵头）；工业和信息化部（节能与综合利用司）；"
            "生态环境部（固体废物与化学品司）"
        ),
        asset="废旧家电（电视机、电冰箱、洗衣机、空调器）",
        asset_status="既有",
        asset_detail=(
            "本工具界定和覆盖的对象为电视机、电冰箱、洗衣机、空调器四类家电产品的废旧品。"
            "回收统计不受品类和品牌限制，生产企业可回收非本企业生产的产品。废旧家电须"
            "交由有资质的废弃电器电子产品处理企业进行规范拆解处理。"
        ),
        agent="企业",
        agent_detail=(
            "家电生产企业（按总公司计算）。企业可自愿申报参与回收目标责任制行动，"
            "自主确定年度回收量和回收率目标并向社会公开。参与为自愿性质，不设强制性"
            "合规义务和处罚。"
        ),
        activity="收集或分类（消费后）",
        activity_detail=(
            "本工具规范和引导的活动为家电生产企业自愿建立废旧家电逆向回收体系并实施"
            "回收目标责任制的全过程，包括：按年度确定回收量和回收率等量化目标；利用销售"
            "网络、售后服务和电商平台拓展回收渠道；建设回收存储设施并优化运输网络；建立"
            "覆盖回收、运输和处置利用全流程的信息追溯系统；以及将废旧家电交由有资质企业"
            "规范拆解处理。参与为自愿性质。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）企业按年度自主确定回收量和回收率（年度回收量/前三年平均销售量）等量化"
            "目标，回收量和回收率指标占评估权重70%，回收行为目标占30%；2）回收统计不受"
            "品类和品牌限制；3）废旧家电须交由有资质的废弃电器电子产品处理企业进行规范"
            "拆解处理；4）企业须建立覆盖回收、运输和处置利用全过程的信息追溯系统，实行"
            "统一编码和转运联单管理；5）企业须在每年1月31日前通过省级发展改革委提交申请"
            "报告，三部委于每年3月底前公布责任企业名单及回收目标；6）企业须进行年度自我"
            "评价并公开发布；7）参与为自愿性质，不设强制性合规义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "完成回收目标的企业纳入「绿色责任名单」，在绿色债券、绿色信贷审批、"
            "政府专项基金等方面给予优先支持；示范标杆企业的经验和模式在全国推广。"
        ),
        monitoring=(
            "责任企业须进行年度自我评价并将结果向社会公开发布。国家发展改革委、工业和"
            "信息化部、生态环境部按年度对责任企业的回收目标完成情况进行跟踪评估，评估"
            "结果向社会公布。"
        ),
        sanctions="N/A（自愿性目标责任，不设违规制裁。企业自愿参与，无强制合规义务和处罚。）",
        ghg_abs=(
            "N/A（本工具为自愿性目标责任框架，碳排放覆盖量取决于企业自愿参与和回收"
            "处理的规模和程度，无直接可量化的固定覆盖量）"
        ),
        ghg_pct="N/A（本工具为自愿性工具，碳排放覆盖占比取决于自愿参与情况）",
        isic="C27",
        ghg="CO2; CH4",
        mitigation_effects="正向",
        co_benefits="循环经济；资源节约；污染防治",
        legal_name=(
            "国家发展改革委 工业和信息化部 生态环境部关于鼓励家电生产企业开展回收"
            "目标责任制行动的通知（发改产业〔2021〕1102号）"
        ),
        legal_url="https://www.miit.gov.cn/jgsj/jns/wjfb/art/2021/art_5df08ed7493e4a40af80f0124fc2e7b7.html",
        other_links="N/A",
    ),
    make_row(
        pid="CHNVTGVTGI02S000",
        name_cn="可再生能源发电企业自建或购买调峰能力增加并网规模",
        name_en="Self-Built or Purchased Peak-Shaving Capacity by Renewable Energy Power Generation Enterprises to Increase Grid-Connected Scale",
        sector="能源",
        subsector="风电；太阳能",
        policy_package="N/A",
        description=(
            "可再生能源发电企业自建或购买调峰能力增加并网规模是由国家发展改革委、"
            "国家能源局联合建立的自愿性目标机制，引导可再生能源发电企业通过自建或购买"
            "调峰储能能力的方式，增加可再生能源发电装机并网规模。通知（发改运行〔2021〕"
            "1138号）明确，在电网企业承担保障性并网责任的基础上，鼓励风电、太阳能发电"
            "企业通过自建、合建或市场化购买调峰资源的方式增加并网规模。调峰资源包括"
            "抽水蓄能、电化学储能等新型储能、气电、光热电站和灵活性制造改造的煤电。"
            "挂钩比例要求：超过保障性并网以外的规模，初期按功率15%的挂钩比例配建调峰"
            "能力（时长4小时以上），按20%以上比例配建的优先并网。合建方式可按出资比例"
            "折算。购买调峰能力包括购买调峰储能项目和购买调峰储能服务两种方式，被购买"
            "主体仅限于本年度新建的调峰资源。发电项目须与新增调峰项目同步建成、同步并网。"
            "未用完的调峰资源可市场化交易给其他发电企业，但不允许结转至下年。"
            "电网调度机构不定期对调峰项目开展调度测试，确保能力真实可用。参与为自愿"
            "性质，但虚假承诺按未完成容量2倍扣除调峰能力并取消下年度自行承担消纳责任资格。"
        ),
        objective="促进可再生能源消纳，提升电力系统灵活性和调节能力",
        mitigation="直接",
        channel="供给侧",
        adoption="29/07/2021",
        effective="10/08/2021",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "国家发展和改革委员会（经济运行调节局）；国家能源局（新能源和可再生能源司）"
        ),
        asset="调峰资源（抽水蓄能、电化学储能等新型储能、气电、光热电站、灵活性改造煤电）",
        asset_status="新建",
        asset_detail=(
            "本工具界定和覆盖的对象为用于增加可再生能源并网规模的调峰储能资源，包括"
            "抽水蓄能电站、电化学储能等新型储能设施、天然气发电、光热电站以及经灵活性"
            "制造改造的煤电机组。调峰能力按装机规模（抽水蓄能、电化学储能、光热电站）、"
            "机组设计出力（气电）或改造前后可调出力范围差值（煤电灵活性改造）认定。"
        ),
        agent="企业",
        agent_detail=(
            "风电、太阳能发电等可再生能源发电企业。企业可自愿选择自建、合建或市场化"
            "购买调峰储能能力的方式增加并网规模。参与为自愿性质，但虚假承诺的企业将被"
            "取消下年度自行承担可再生能源消纳责任资格。"
        ),
        activity="电力生产、输送和分配",
        activity_detail=(
            "本工具规范和引导的活动为可再生能源发电企业通过自建或购买调峰储能能力增加"
            "可再生能源发电装机并网规模的全过程，包括：企业根据挂钩比例（初期15%，推荐"
            "20%以上）确定需配建的调峰能力规模；选择自建、合建或市场化购买方式落实调峰"
            "资源；确保发电项目与新增调峰项目同步建成、同步并网；接受电网调度机构的不定期"
            "调度测试；以及未用完调峰资源的省内市场化交易（不允许结转至下年）。参与为自愿"
            "性质，遵循「企业承诺、政府备案、过程核查、假一罚二」的确认原则。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）超过保障性并网以外的规模，初期按功率15%的挂钩比例配建调峰能力（时长4小时"
            "以上），按20%以上比例配建的优先并网；2）合建方式按出资比例折算挂钩比例，"
            "初期可适当高于出资比例；3）购买调峰能力仅限于本年度新建的调峰资源；4）发电"
            "项目须与新增调峰项目同步建成、同步并网；5）调峰能力按装机规模、机组设计"
            "出力或可调出力范围差值认定；6）遵循「企业承诺、政府备案、过程核查、假一罚二"
            "（按未完成容量2倍扣除调峰能力，限期整改）「的确认原则；7）未用完的调峰资源"
            "可在省内市场化交易，不允许结转至下年；8）参与为自愿性质。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "按20%以上挂钩比例配建调峰能力的企业获得优先并网安排；未用完的调峰资源可"
            "在省内市场化交易给其他发电企业，增加额外收益。"
        ),
        monitoring=(
            "电网调度机构不定期对调峰储能项目开展调度测试，确保调峰能力真实可用。"
            "各省（区、市）发展改革委和能源主管部门对本地区落实情况进行监督管理。"
            "国家发展改革委和国家能源局对各地进展情况进行统筹跟踪，适时开展第三方评估。"
        ),
        sanctions=(
            "虚假承诺或未按承诺履行的企业，按未完成容量的2倍扣除调峰能力，责令限期"
            "整改；未按期整改到位的，取消下年度自行承担可再生能源消纳责任资格。"
        ),
        ghg_abs=(
            "N/A（本工具为自愿性目标机制，通过增加可再生能源并网规模间接促进减排，"
            "碳排放覆盖量取决于企业自愿参与和新增调峰能力的实际规模，无直接可量化的"
            "固定覆盖量）"
        ),
        ghg_pct="N/A（本工具为自愿性工具，碳排放覆盖占比取决于自愿参与情况）",
        isic="D35",
        ghg="CO2",
        mitigation_effects="正向",
        co_benefits="可再生能源发展；技术创新",
        legal_name=(
            "国家发展改革委 国家能源局关于鼓励可再生能源发电企业自建或购买调峰能力"
            "增加并网规模的通知（发改运行〔2021〕1138号）"
        ),
        legal_url="https://www.ndrc.gov.cn/xwdt/tzgg/202108/t20210810_1293397_ext.html",
        other_links="N/A",
    ),
]


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

    existing = _load_rows(CSV_PATH)
    header, data = existing[0], existing[1:]

    inserted = 0
    for row in ROWS:
        pid = row[0]
        if any(r and r[0] == pid for r in data):
            print(f"  {pid} already in CSV — skipping")
            continue

        # Insert after existing VTG rows, or at end if none
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][2] == "自愿性目标":
                insert_pos = i + 1

        if insert_pos == 0:
            print(f"ERROR: Cannot find insertion position for {pid}")
            return 1

        data.insert(insert_pos, list(row))
        inserted += 1
        print(f"  Inserted {pid} at data index {insert_pos}")

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
