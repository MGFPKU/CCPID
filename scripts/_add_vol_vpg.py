#!/usr/bin/env python3
"""Insert Voluntary procurement guidance (VPG) instrument into the Voluntary CN CSV.

   Instrument:
   - CHNVIIVPGI01S000  企业绿色采购指南（试行）
"""

from __future__ import annotations

import csv
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

LQ = "“"
RQ = "”"


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


ROWS = [
    make_row(
        pid="CHNVIIVPGI01S000",
        group_cn="自愿性信息工具",
        approach_cn="自愿性采购指南",
        sector="跨部门",
        subsector="N/A",
        name_cn="企业绿色采购指南",
        name_en="Enterprise Green Procurement Guide",
        policy_package="N/A",
        description=(
            "企业绿色采购指南（试行）由商务部、环境保护部（现生态环境部）、工业和"
            "信息化部三部门联合印发，是中国首份国家层面引导企业开展绿色采购和绿色"
            "供应链管理的自愿性信息工具，旨在引导企业将环境保护和资源节约理念融入"
            "采购决策全流程，推动绿色供应链建设。指南共六章三十条，涵盖采购原则、"
            "绿色产品和供应商识别、采购流程管理和政府引导等内容。第一章总则明确绿色"
            "采购应遵循" + LQ + "经济效益与环境效益兼顾" + RQ + "、" + LQ + "打造绿色"
            "供应链" + RQ + "、" + LQ + "企业主体与政府引导相结合" + RQ + "三项原则，"
            "要求企业制定绿色采购方案。第二章界定四类绿色产品标准：产品设计采用绿色"
            "理念、生产过程推行清洁生产、使用过程低消耗低排放、废弃后可回收利用。"
            "第三章建立供应商绿色筛选机制：提出供应商环境信用评级、清洁生产审核、"
            "ISO 14001/ISO 50001认证等9条优先采购标准，以及环境刑事处罚记录、重大"
            "环境污染事件、排放不达标等9条采购排除标准。第四章明确绿色采购与供应商"
            "管理要求，包括招标文件中设定绿色权重、引入价格优惠或份额激励等正激励"
            "机制。第五章规定政府部门引导职责，包括发布绿色产品清单、建立供应商环境"
            "信用信息平台和绿色采购信息服务平台。企业参与为自愿性质，不设强制性合规"
            "义务和处罚。"
        ),
        objective="促进绿色采购",
        mitigation="直接",
        channel="环境",
        adoption="22/12/2014",
        effective="01/01/2015",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities=(
            "商务部（流通发展司）；环境保护部（现生态环境部）；工业和信息化部"
        ),
        asset="企业采购的货物与服务（绿色采购）",
        asset_status="N/A",
        asset_detail=(
            "本工具界定和覆盖的对象为企业采购的各类原材料、产品和服务。指南通过"
            "设定绿色产品和绿色供应商标准，引导企业在采购环节将环境绩效作为采购"
            "决策依据。重点关注产品全生命周期的环境影响，包括设计阶段的绿色理念、"
            "生产阶段的清洁生产水平、使用阶段的能源消耗和污染物排放、以及废弃后的"
            "回收利用和处理。指南为推荐性和指导性质，不直接监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "所有开展原材料、产品和服务采购活动的企业，包括但不限于制造业企业、"
            "流通企业和大型采购企业。企业可参照指南自愿建立绿色采购制度、设定绿色"
            "采购目标和供应商筛选标准，并将环境绩效纳入采购评价体系。参与为自愿"
            "性质，不设强制性合规义务和处罚。"
        ),
        activity="消费与使用",
        activity_detail=(
            "本指南引导和规范的受规制活动为企业的采购和消费行为，涵盖原材料采购、"
            "产品采购和服务采购等各类采购活动，以及相应的供应商筛选和管理。指南通过"
            "设定绿色供应商标准和绿色产品识别准则，引导企业在采购决策中系统纳入环境"
            "保护和温室气体减排因素，优先采购符合绿色标准的产品和服务，优先选择环境"
            "信用良好的供应商。企业自愿采纳，无强制性合规义务。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）企业绿色采购应遵循经济效益与环境效益兼顾、打造绿色供应链、企业主体"
            "与政府引导相结合三项原则；2）企业应制定绿色采购方案，明确绿色采购目标、"
            "供应商筛选标准和绩效评估机制；3）优先采购符合绿色产品标准的产品（产品"
            "设计采用绿色理念、生产过程推行清洁生产、使用过程低消耗低排放、废弃后可"
            "回收利用）；4）依据9条优先标准和9条排除标准对供应商进行绿色筛选，禁止"
            "采购列入淘汰或禁止目录的产品；5）可在招标文件中设定绿色权重，对达到绿色"
            "标准的供应商给予价格优惠或份额激励；6）参与为自愿性质，不设强制性合规"
            "义务和处罚。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "企业采纳绿色采购可获得市场认可和竞争优势，优先列入政府部门发布的绿色"
            "采购典型案例和最佳实践推广；与绿色金融、政府采购优惠政策衔接，绿色采购"
            "企业可能获得融资便利和政府采购倾斜；利用政府部门建立的绿色产品清单和"
            "供应商环境信用信息平台降低绿色采购信息搜寻成本。"
        ),
        monitoring=(
            "企业参照指南自行开展绿色采购管理和供应商环境绩效评估，自愿披露绿色采购"
            "信息；政府部门通过行业调查和信息平台了解企业绿色采购实践情况，无强制性"
            "合规监测要求。"
        ),
        sanctions=(
            "N/A（自愿性指南，无违规制裁。指南为推荐性和指导性质，企业自愿采纳，"
            "不设强制性合规义务和处罚。）"
        ),
        ghg_abs=(
            "N/A（本工具为自愿性信息工具，通过引导企业自愿采纳绿色采购实践间接"
            "促进减排，无直接可量化的温室气体排放覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接自愿性工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="C",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；污染防治；资源节约；循环经济",
        legal_name=(
            "商务部 环境保护部 工业和信息化部关于印发《企业绿色采购指南（试行）》"
            "的通知（商流通函[2014]973号）"
        ),
        legal_url=(
            "https://www.mee.gov.cn/gkml/hbb/gwy/201412/t20141226_293493.htm"
        ),
        other_links=(
            "https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=6413"
        ),
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

        # Insert after last Voluntary information instrument row
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][2] == "自愿性信息工具":
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
