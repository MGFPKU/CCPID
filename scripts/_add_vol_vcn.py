#!/usr/bin/env python3
"""Insert a Voluntary-approaches instrument under Voluntary information
   instruments group:
   - CHNVIIVCNI01S000 (Implementation Guide for Carbon Neutrality
     of Large-Scale Events, MEE, trial)

   Appends to outputs/CCPID_cn_voluntary_approaches.csv (50-column
   Voluntary template, already bootstrapped by _add_vol_sft.py).
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


ROWS = []

ROWS = [
    make_row(
        pid="CHNVIIVCNI01S000",
        group_cn="自愿性信息工具",
        approach_cn="自愿碳中和方法",
        sector="跨部门",
        subsector="N/A",
        name_cn="大型活动碳中和实施指南",
        name_en="Implementation Guide for Carbon Neutrality of Large-Scale Events",
        policy_package="N/A",
        description=('大型活动碳中和实施指南（试行）由生态环境部发布，是为大型活动组织者自愿实施碳中和提供标准化方法论的自愿性信息类工具，旨在鼓励各类大型活动通过核算、减排和抵消三个步骤实现温室气体净零排放。指南适用对象包括演出、赛事、会议、展览、庆典等各类大型活动，覆盖活动筹备、举办和收尾阶段的全生命周期温室气体排放。指南建立了「核算排放、实施减排、购买抵消」的三步框架：（1）核算——界定核算边界和排放源（化石燃料燃烧、净购入电力/热力、交通、住宿、餐饮、活动用品隐含排放、废弃物处理等），编制温室气体排放清单；（2）减排——通过绿色场馆、绿色交通、绿色住宿、绿色餐饮、无纸化办公、垃圾分类等措施减少活动自身排放；（3）抵消——优先采用经国家或地方认可的碳信用进行抵消，包括全国碳排放权交易配额、CCER、省级碳普惠减排量、清洁发展机制中国项目减排量等。活动组织者完成上述步骤后可依据指南声明大型活动碳中和。指南为自愿性质，不设强制性合规义务和处罚。'        ),
        objective="减缓气候变化",
        mitigation="直接",
        channel="环境",
        adoption="29/05/2019",
        effective="29/05/2019",
        revision="N/A",
        revision_detail="N/A",
        status="生效",
        admin_authorities="生态环境部（应对气候变化司）",
        asset="大型活动（演出、赛事、会议、展览、庆典等）",
        asset_status="N/A",
        asset_detail=('本工具界定和覆盖的对象为在中国境内举办的各类大型活动，包括但不限于体育赛事、文艺演出、大型会议、展览展销、节庆庆典等。指南涵盖活动筹备、举办和收尾阶段全生命周期的温室气体排放源，包括化石燃料燃烧排放、净购入电力/热力排放、交通排放、住宿餐饮排放、活动用品隐含排放和废弃物处理排放等。'        ),
        agent="企业",
        agent_detail=('各类大型活动的主办单位、承办单位和组织者。活动组织者可依据指南自愿开展大型活动碳排放核算、减排和抵消并声明碳中和，参与为自愿性质，无强制性合规义务。'        ),
        activity="消费与使用",
        activity_detail=('本工具引导和规范的受规制活动为大型活动的组织、举办和消费过程。指南通过「核算、减排、抵消」的三步框架，引导活动组织者在活动筹备、举办和收尾阶段核算温室气体排放，采取绿色场馆、绿色交通、绿色餐饮等措施减少活动自身排放，并通过购买经认可的碳信用抵消剩余排放，实现大型活动碳中和。参与为自愿性质。'        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=('1）大型活动碳中和实施应遵循「核算、减排、抵消」三步框架；2）核算边界应涵盖活动筹备、举办和收尾阶段的直接和间接温室气体排放；3）活动组织者应优先通过减排措施降低活动自身排放，再对无法减排的剩余排放进行碳抵消；4）碳抵消信用应符合指南规定的合格类型和准则（全国碳排放权交易配额、CCER、省级碳普惠减排量等）；5）鼓励活动组织者委托第三方机构对碳中和实施过程和结果进行独立评价或核查，并向社会公开相关信息；6）指南为自愿性质，不设强制性合规义务和处罚。'        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=('活动组织者完成碳中和后可依据指南声明大型活动碳中和，提升活动绿色品牌形象和社会影响力；部分地方对实施碳中和的大型活动给予宣传推广和表彰。'        ),
        monitoring=('活动组织者自行开展碳排放核算和实施减排抵消措施；鼓励委托第三方机构对碳中和实施过程和结果进行独立评价和核查，但非强制要求。'        ),
        sanctions="N/A（本工具为自愿性碳中和方法指南，不设违规制裁）",
        ghg_abs=('N/A（本工具为自愿性碳中和方法工具，碳排放覆盖量取决于活动组织者自愿采纳的规模和程度，无直接可量化的固定覆盖量）'        ),
        ghg_pct="N/A（本工具为自愿性工具，碳排放覆盖占比取决于自愿采纳情况）",
        isic="R93; S94",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="公众健康；绿色产业发展；空气污染物减排",
        legal_name="关于发布《大型活动碳中和实施指南（试行）》的公告（生态环境部公告2019年第19号）",
        legal_url="https://www.mee.gov.cn/xxgk2018/xxgk/xxgk01/201906/t20190617_706706.html",
        other_links="https://www.gov.cn/gongbao/content/2019/content_5430516.htm",
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
                print(f"  {pid} already up to date — skipping")
            continue
        data.append(list(row))
        inserted += 1
        print(f"  Inserted {pid} at data index {len(data) - 1}")

    data = [r for r in data if any(r)]

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted, {updated} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
