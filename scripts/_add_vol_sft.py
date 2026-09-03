#!/usr/bin/env python3
"""Insert the first Voluntary-approaches instrument (Sustainable finance
   taxonomy group/approach):
   - CHNVIISFTI01S000 (Green Finance Endorsed Project Catalogue, PBoC/NFRA/CSRC)

   Bootstraps outputs/CCPID_cn_voluntary_approaches.csv (50-column Voluntary
   template). No prior Voluntary CSV or builder exists.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_cn_voluntary_approaches.csv"

# 50-column CN template header for Voluntary approaches (自愿措施 sheet)
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


ROWS = [
    make_row(
        pid="CHNVIISFTI01S000",
        group_cn="自愿性信息工具",
        approach_cn="可持续金融分类目录",
        sector="跨部门",
        subsector="N/A",
        name_cn="绿色金融支持项目目录",
        name_en="Green Finance Endorsed Project Catalogue",
        policy_package="N/A",
        description=(
            "绿色金融支持项目目录是由中国人民银行会同金融监管部门发布的绿色"
            "金融标准类自愿性工具，通过统一界定各类绿色金融产品所支持项目的"
            "范围和认定标准，为绿色贷款、绿色债券等绿色金融产品的识别、认定"
            "和信息披露提供依据，引导金融资源投向绿色低碳领域。目录以项目"
            "活动为基础分级分类，涵盖节能降碳、环境保护、资源循环利用、绿色"
            "能源低碳转型、生态保护修复和利用、绿色基础设施升级、绿色服务、"
            "绿色贸易、绿色消费等领域，对纳入项目明确界定条件、国民经济行业"
            "分类代码和温室气体减排贡献属性标识。目录建设可追溯至2015年"
            "《绿色债券支持项目目录（2015年版）》（中国人民银行公告〔2015〕"
            "第39号），2021年修订为《绿色债券支持项目目录（2021年版）》"
            "（银发〔2021〕96号，由中国人民银行、发展改革委、证监会联合印发，"
            "自2021年7月1日起施行）；2025年在《绿色低碳转型产业指导目录"
            "（2024年版）》和《绿色债券支持项目目录（2021年版）》基础上修订"
            "形成《绿色金融支持项目目录（2025年版）》（银发〔2025〕132号，由"
            "中国人民银行、金融监管总局、中国证监会联合印发，自2025年10月1日"
            "起施行），统一适用于各类绿色金融产品。发行主体和金融机构参照"
            "目录开展绿色项目认定和信息披露，参与为自愿性质。"
        ),
        objective="引导绿色投资",
        mitigation="间接",
        channel="环境",
        adoption="22/12/2015",
        effective="22/12/2015",
        revision="01/10/2025",
        revision_detail=(
            "目录建设可追溯至2015年12月22日《绿色债券支持项目目录（2015年版）》"
            "（中国人民银行公告〔2015〕第39号，我国首份绿色债券界定与分类"
            "文件）。2021年修订为《绿色债券支持项目目录（2021年版）》（银发"
            "〔2021〕96号，由中国人民银行、发展改革委、证监会联合印发，自"
            "2021年7月1日起施行），以《绿色产业指导目录（2019年版）》为基础"
            "统一绿色债券标准。2025年在《绿色低碳转型产业指导目录（2024年版）》"
            "和《绿色债券支持项目目录（2021年版）》基础上修订形成《绿色金融"
            "支持项目目录（2025年版）》（银发〔2025〕132号，成文2025年6月27日，"
            "自2025年10月1日起施行），由中国人民银行、金融监管总局、中国证监会"
            "联合印发，统一绿色贷款、绿色债券等各类绿色金融产品适用标准，设"
            "9大领域，新增国民经济行业分类代码和温室气体减排贡献属性标识。"
        ),
        status="生效",
        admin_authorities=(
            "中国人民银行、金融监管总局、中国证监会（2025年版）；中国人民"
            "银行、国家发展改革委、中国证监会（绿色债券目录2021年版）；中国"
            "人民银行（绿色债券目录2015年版）"
        ),
        asset="绿色金融产品（绿色贷款、绿色债券等）",
        asset_status="N/A",
        asset_detail=(
            "本工具为绿色金融标准目录，界定对象为绿色贷款、绿色债券等各类绿色"
            "金融产品，通过统一其所支持项目的范围和认定标准，为绿色金融产品的"
            "识别、认定和信息披露提供依据。目录所支持的绿色低碳项目涵盖节能"
            "降碳、环境保护、资源循环利用、绿色能源、生态保护修复、绿色基础"
            "设施、绿色服务、绿色贸易、绿色消费等领域符合条件的项目，不直接"
            "监管实体排放资产。"
        ),
        agent="企业",
        agent_detail=(
            "绿色债券发行主体、绿色贷款融资主体等市场主体，以及提供绿色金融"
            "产品和服务的金融机构。发行主体和金融机构参照目录开展绿色项目"
            "认定和信息披露，参与为自愿性质，无强制性义务。"
        ),
        activity="融资与投资",
        activity_detail=(
            "本工具规范的受规制活动为面向绿色低碳领域的各类绿色金融融资与"
            "投资活动，涵盖绿色贷款、绿色债券、绿色投资、绿色保险等绿色金融"
            "产品的提供与配置。目录通过统一界定各类绿色金融产品所支持项目的"
            "范围和认定标准，引导融资与投资资源流向符合条件的绿色低碳项目。"
            "发行主体和金融机构参照目录开展绿色项目认定和信息披露，参与为"
            "自愿性质。"
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1）目录按领域分级分类列出绿色金融支持项目，对纳入项目明确界定"
            "条件、国民经济行业分类代码和温室气体减排贡献属性标识；2）目录"
            "统一适用于各类绿色金融产品（沪深北交易所上市及股票发行、新三板"
            "挂牌及股票发行业务暂不适用）；3）发行主体和金融机构参照目录开展"
            "绿色项目认定和信息披露，参与为自愿性质，无强制处罚；4）做好与"
            "绿色贷款、绿色债券等产品历史标准的衔接；5）目录适时调整修订。"
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "纳入目录的项目可获得绿色贷款、绿色债券等绿色金融产品的资金支持"
            "和市场认可；统一标准有助于降低识别成本、提升绿色金融资产管理"
            "效率，增强绿色项目的融资便利。"
        ),
        monitoring=(
            "发行主体和金融机构参照目录自行开展绿色项目认定并进行信息披露；"
            "由相关业务主管部门在绿色金融产品管理中结合目录进行业务规范和"
            "指导，无强制性合规监测处罚。"
        ),
        sanctions=(
            "N/A（本工具为自愿性绿色金融标准目录，不设违规制裁）"
        ),
        ghg_abs=(
            "N/A（本工具为绿色金融标准目录，通过统一绿色项目认定标准并引导"
            "资金投向绿色低碳项目间接支持减排，无直接可量化的温室气体排放"
            "覆盖量）"
        ),
        ghg_pct=(
            "N/A（本工具为间接绿色金融标准工具，无直接的温室气体排放覆盖占比）"
        ),
        isic="K64",
        ghg="CO2; CH4; N2O",
        mitigation_effects="正向",
        co_benefits="绿色产业发展；污染防治；资源节约；循环经济；生态保护",
        legal_name=(
            "中国人民银行 金融监管总局 中国证监会关于印发《绿色金融支持项目"
            "目录（2025年版）》的通知（银发〔2025〕132号）"
        ),
        legal_url=(
            "https://www.gov.cn/zhengce/zhengceku/202507/content_7032004.htm"
        ),
        other_links=(
            "https://www.gov.cn/zhengce/zhengceku/2021-04/22/content_5601284.htm；"
            "https://www.pbc.gov.cn/tiaofasi/144941/3581332/3588085/index.html"
        ),
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
