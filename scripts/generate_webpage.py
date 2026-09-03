#!/usr/bin/env python3
"""Generate the CCPID webpage modules (self-contained HTML fragments): the data
overview and a data-download button that links to the latest Excel workbook.

The module mirrors the Excel 概览/Summary sheet: it replicates the counting
semantics of export_workbooks.write_summary_sheet (COUNTIF / SEARCH formulas
over the approaches and instruments overview views), so the webpage numbers
always match the Excel workbook. The output is a plain HTML fragment with
scoped CSS and no JavaScript, meant to be embedded into the CCPID website.

Usage:
    python scripts/generate_webpage.py                # Chinese module (default)
    python scripts/generate_webpage.py --lang en      # English module
    python scripts/generate_webpage.py --lang all     # both
"""

from __future__ import annotations

import argparse
import csv
import shutil
import sys
from datetime import date
from pathlib import Path

from export_workbooks import (
    LANG_CONFIG,
    SUMMARY_LAYOUT,
    append_unique,
    get_field,
    load_chinese_approaches,
    load_english_approaches,
    normalise_key,
)

ROOT = Path(__file__).resolve().parents[1]

CATEGORY_FILES = list(LANG_CONFIG["cn"]["sheets"].keys())

FIELDS = {
    "cn": {
        "type": "工具/子方案",
        "group": "组别",
        "approach": "路径",
        "sector": "排放部门",
        "mitigation": "减缓相关性",
    },
    "en": {
        "type": "Instrument / subscheme",
        "group": "Group",
        "approach": "Approach",
        "sector": "Emission sector",
        "mitigation": "Mitigation relevance",
    },
}

INSTRUMENT_LABEL = {"cn": "工具", "en": "Instrument"}

# Cross-table header display labels; the SUMMARY_LAYOUT values stay untouched
# because they double as match keys for counts and Excel COUNTIFS formulas.
CROSS_CAT_LABELS = {
    "en": {"Government investment and consumption": "Government I&C"},
}

TEXT = {
    "cn": {
        "download_btn": "数据下载",
        "scope_labels": {"approaches": "路径数量：", "instruments": "工具数量：", "sectors": "覆盖部门："},
        "scope_sectors": "能源；交通；建筑；工业；农业、林业和其他土地利用；废弃物",
        "cat_col": "类别",
        "group_col": "组别",
        "sector_col": "排放部门",
        "mitigation_col": "减缓相关性",
        "total_col": "总计",
        "note": (
            '注："类别"和"组别"的数字之和等于路径/工具的总数，因为每个路径/工具仅属于一个类别/组别。'
            "其他表中的数字之和大于路径/工具总数，因为部分路径/工具属于多个分类。"
        ),
    },
    "en": {
        "download_btn": "Download Data",
        "scope_labels": {"approaches": "Number of approaches: ", "instruments": "Number of instruments: ", "sectors": "Sectors covered: "},
        "scope_sectors": "Energy, Transport, Buildings, Industry, AFOLU, Waste",
        "cat_col": "Category",
        "group_col": "Group",
        "sector_col": "Emission Sector",
        "mitigation_col": "Mitigation relevance",
        "total_col": "Total",
        "note": (
            'Note: The sum of numbers for "category" and "group" equals the total number of '
            "approaches/instruments, since each approach/instrument only belongs to one "
            "category/group. The sum of numbers in the other tables are larger than the total "
            "number of approaches/instruments since some approaches/instruments belong to more "
            "than one classification."
        ),
    },
}

CSS = """
#ccpid-overview {
  font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei",
    "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  color: #20302c; line-height: 1.6; max-width: 1080px; margin: 0 auto;
}
#ccpid-overview .ccpid-scope {
  background: #f0f7f4; border-left: 4px solid #14936f; border-radius: 6px;
  padding: 12px 18px; margin-bottom: 20px;
}
#ccpid-overview .ccpid-scope h3 { font-size: 16px; margin: 0 0 6px; color: #0e5c46; }
#ccpid-overview .ccpid-scope p { margin: 3px 0; font-size: 15px; }
#ccpid-overview .ccpid-scope strong { color: #0e5c46; }
#ccpid-overview .ccpid-cols {
  display: grid; grid-template-columns: 1.25fr 1fr; gap: 18px; align-items: start;
}
#ccpid-overview .ccpid-col-right { display: grid; gap: 18px; align-content: start; }
#ccpid-overview .ccpid-panel {
  background: #fff; border: 1px solid #e2e8e5; border-radius: 8px; padding: 14px 16px;
  overflow-x: auto;
}
#ccpid-overview .ccpid-cross { margin-top: 18px; }
#ccpid-overview .ccpid-full { margin-top: 18px; }
#ccpid-overview .ccpid-bottom {
  display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr);
  gap: 18px; align-items: start; margin-top: 18px;
}
#ccpid-overview .ccpid-bottom .ccpid-note { margin: 6px 0 0; }
#ccpid-overview table.ccpid-table { width: 100%; border-collapse: collapse; font-size: 14px; table-layout: fixed; }
#ccpid-overview .ccpid-table th {
  background: #0e7a5f; color: #fff; padding: 7px 10px; text-align: center; font-weight: 600;
}
#ccpid-overview .ccpid-table.ccpid-narrow { width: min(440px, 100%); }
#ccpid-overview .ccpid-table td { padding: 6px 10px; border-bottom: 1px solid #eef2f0; }
#ccpid-overview .ccpid-table tbody tr:last-child td { border-bottom: none; }
#ccpid-overview .ccpid-table td.ccpid-rowlabel { font-weight: 600; background: #f6faf8; }
#ccpid-overview .ccpid-table td.ccpid-num { text-align: right; font-variant-numeric: tabular-nums; }
#ccpid-overview .ccpid-note { font-size: 13px; color: #66756f; margin: 12px 0 0; }
@media (max-width: 760px) {
  #ccpid-overview .ccpid-cols { grid-template-columns: 1fr; }
  #ccpid-overview .ccpid-bottom { grid-template-columns: 1fr; }
}
"""


def load_rows(outputs_dir: Path, lang: str) -> dict[str, tuple[list[str], list[dict]]]:
    data = {}
    for file_key in CATEGORY_FILES:
        path = outputs_dir / f"CCPID_{lang}_{file_key}.csv"
        if not path.exists():
            sys.exit(f"ERROR: missing input file: {path}")
        with open(path, encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            missing = [v for v in FIELDS[lang].values() if v not in (reader.fieldnames or [])]
            if missing:
                sys.exit(f"ERROR: {path.name} is missing required columns: {missing}")
            data[file_key] = (list(reader.fieldnames), list(reader))
    return data


def build_approaches(data: dict, lang: str) -> dict[str, dict]:
    """One entry per distinct approach present in the CSVs, mirroring
    write_approaches_sheet: values are unioned across rows, category/group
    come from the classification doc."""
    lookup = load_chinese_approaches() if lang == "cn" else load_english_approaches()
    summaries: dict[str, dict] = {}

    cn_to_en: dict[str, str] = {}
    if lang == "en":
        seen_ids: set[int] = set()
        for cn_entry in load_chinese_approaches().values():
            entry_id = id(cn_entry)
            if entry_id in seen_ids:
                continue
            seen_ids.add(entry_id)
            en_name = cn_entry.get("路径_en", "")
            cn_name = cn_entry.get("路径", "")
            if en_name and cn_name:
                cn_to_en[normalise_key(cn_name)] = en_name

    for _file_key, (headers, rows) in data.items():
        for row in rows:
            approach = get_field(row, headers, "Approach", "路径")
            if not approach:
                continue
            key = normalise_key(approach)
            if lang == "en" and key in cn_to_en:
                approach = cn_to_en[key]
                key = normalise_key(approach)
            summary = summaries.setdefault(
                key, {"approach": approach, "sectors": [], "relevance": []}
            )
            append_unique(summary["sectors"], get_field(row, headers, "Emission sector", "排放部门"))
            append_unique(summary["relevance"], get_field(row, headers, "Mitigation relevance", "减缓相关性"))

    for key, summary in summaries.items():
        cls = lookup.get(key, {})
        summary["category"] = str(cls.get("类别", "") or cls.get("Category", ""))
        summary["group"] = str(cls.get("组别", "") or cls.get("Group", ""))
    return summaries


def compute_stats(data: dict, lang: str) -> dict:
    layout = SUMMARY_LAYOUT[lang]
    file_sheets = LANG_CONFIG[lang]["sheets"]
    instrument_label = INSTRUMENT_LABEL[lang]

    approaches = build_approaches(data, lang)

    instruments = []
    for file_key, (headers, rows) in data.items():
        category = file_sheets[file_key]
        for row in rows:
            if (get_field(row, headers, "Instrument / subscheme", "工具/子方案") or "").strip() != instrument_label:
                continue
            instruments.append(
                {
                    "category": category,
                    "group": (get_field(row, headers, "Group", "组别") or "").strip(),
                    "sector": (get_field(row, headers, "Emission sector", "排放部门") or "").strip(),
                    "mitigation": (get_field(row, headers, "Mitigation relevance", "减缓相关性") or "").strip(),
                }
            )

    def eq(a: str, b: str) -> bool:
        return a.casefold() == b.casefold()

    def contains(cell: str, term: str) -> bool:
        return term.casefold() in cell.casefold()

    # Category/Group breakdown (exact match, like COUNTIF without wildcards)
    groups = []
    for _, group in layout["groups"]:
        ap = sum(1 for s in approaches.values() if eq(s["group"], group))
        ins = sum(1 for r in instruments if eq(r["group"], group))
        groups.append((group, ap, ins))

    # Category totals
    cats = []
    for _, cat_doc in layout["cats"]:
        ap = sum(1 for s in approaches.values() if eq(s["category"], cat_doc))
        cats.append({"label": "", "ap": ap, "ins": 0})
    for i, (_, cat_label) in enumerate(layout["ov_cats"]):
        cats[i]["label"] = cat_label
        cats[i]["ins"] = sum(1 for r in instruments if eq(r["category"], cat_label))

    # Emission sectors (substring, like SEARCH / COUNTIF "*s*")
    sectors = []
    for _, sector in layout["sectors"]:
        ap = sum(1 for s in approaches.values() if contains("；".join(s["sectors"]), sector))
        ins = sum(1 for r in instruments if contains(r["sector"], sector))
        sectors.append((sector, ap, ins))

    # Mitigation relevance: approaches substring; instruments EXACT
    # (the Excel formula uses COUNTIF without wildcards for instruments)
    mitigations = []
    for _, rel in layout["mitigations"]:
        ap = sum(1 for s in approaches.values() if contains("；".join(s["relevance"]), rel))
        ins = sum(1 for r in instruments if eq(r["mitigation"], rel))
        mitigations.append((rel, ap, ins))

    # Cross-tabulation: emission sector x category (approaches only)
    cross = []
    for _, sector in layout["cross_sectors"]:
        row_values = []
        for _, cat_doc in layout["cross_cats"]:
            row_values.append(
                sum(
                    1
                    for s in approaches.values()
                    if contains("；".join(s["sectors"]), sector) and eq(s["category"], cat_doc)
                )
            )
        row_values.append(sum(row_values))
        cross.append((sector, row_values))

    return {
        "n_approaches": len(approaches),
        "n_instruments": len(instruments),
        "groups": groups,
        "cats": cats,
        "sectors": sectors,
        "mitigations": mitigations,
        "cross": cross,
        "group_categories": _group_categories(approaches, layout),
    }


def _group_categories(approaches: dict, layout: dict) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for summary in approaches.values():
        group = summary["group"]
        if group and group not in mapping:
            mapping[group] = summary["category"]
    for _, group in layout["groups"]:
        if group not in mapping:
            mapping[group] = ""
    return mapping


BAR_COLOR = "rgba(20, 147, 111, 0.30)"  # accent #14936f, matched to module theme

PADDING_EM = 1.7  # 10px cell padding each side (1.43em) + safety margin


def text_em(text: str) -> float:
    """Estimated width in em: CJK chars are 1em wide, latin/digits ~0.55em."""
    return sum(1.0 if ord(ch) > 0x2E80 else 0.55 for ch in text)


def _table(
    headers: list[str],
    rows: list[list],
    num_from: int = 1,
    label_cols: int = 1,
    extra_cls: str = "",
    fit_headers: bool = False,
    uniform_cols: bool = False,
) -> str:
    # Data bars scaled per table (min/max), like the Excel conditional-formatting ranges;
    # a 10% floor keeps the smallest bar visible.
    nums = [
        cell
        for row in rows
        for i, cell in enumerate(row)
        if i >= num_from and isinstance(cell, (int, float))
    ]
    lo, hi = (min(nums), max(nums)) if nums else (0, 1)

    def bar_style(value: float) -> str:
        width = 100.0 if hi <= lo else 10.0 + (value - lo) / (hi - lo) * 90.0
        return (
            f"background-image:linear-gradient(to right,{BAR_COLOR} 0,"
            f"{BAR_COLOR} {width:.1f}%,rgba(20,147,111,0) {width:.1f}%);"
        )

    if uniform_cols:
        colgroup = "<colgroup>" + "".join(
            f'<col style="width:calc(100% / {len(headers)})">' for _ in headers
        ) + "</colgroup>"
    else:
        # Label columns sized to their content (no wrap). Numeric columns sized to
        # their header: the full header text when fit_headers (wide full-width
        # tables), otherwise the longest word so headers wrap but stay complete.
        col_ems = []
        for c in range(label_cols):
            texts = [str(headers[c])]
            for row in rows:
                cell = row[c] if c < len(row) else None
                if cell is None:
                    continue
                texts.append(cell[0] if isinstance(cell, tuple) else str(cell))
            col_ems.append(max(text_em(t) for t in texts))
        num_ems = []
        for c in range(label_cols, len(headers)):
            words = headers[c].split() or [headers[c]]
            em = max(text_em(w) for w in words)
            if fit_headers:
                em = max(em, text_em(headers[c]))
            for row in rows:
                cell = row[c] if c < len(row) else None
                if isinstance(cell, (int, float)):
                    em = max(em, text_em(str(cell)))
            num_ems.append(em)
        colgroup = "<colgroup>" + "".join(
            f'<col style="width:{em + PADDING_EM:.2f}em">' for em in col_ems + num_ems
        ) + "</colgroup>"

    thead = "".join(
        f'<th class="{"ccpid-num" if i >= num_from else ""}">{h}</th>'
        for i, h in enumerate(headers)
    )
    tbody = []
    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            if cell is None:
                continue
            if isinstance(cell, tuple):  # (text, rowspan) for merged row labels
                text, rowspan = cell
                cells.append(f'<td class="ccpid-rowlabel" rowspan="{rowspan}">{text}</td>')
            else:
                cls = "ccpid-num" if i >= num_from else ""
                style = (
                    f' style="{bar_style(cell)}"'
                    if i >= num_from and isinstance(cell, (int, float))
                    else ""
                )
                cells.append(f'<td class="{cls}"{style}>{cell}</td>')
        tbody.append("<tr>" + "".join(cells) + "</tr>")
    table_cls = f"ccpid-table {extra_cls}".strip()
    return (
        f'<table class="{table_cls}">{colgroup}<thead><tr>{thead}</tr></thead>'
        f'<tbody>{"".join(tbody)}</tbody></table>'
    )


def build_html(lang: str, stats: dict, generated: str) -> str:
    t = TEXT[lang]
    layout = SUMMARY_LAYOUT[lang]
    ap_label = layout["approaches_label"]
    ins_label = layout["instruments_label"]

    scope = t["scope_labels"]
    scope_html = "\n".join(
        [
            f'    <p class="ccpid-scope-line"><strong>{scope["approaches"]}</strong><span>{stats["n_approaches"]}</span></p>',
            f'    <p class="ccpid-scope-line"><strong>{scope["instruments"]}</strong><span>{stats["n_instruments"]}</span></p>',
            f'    <p class="ccpid-scope-line"><strong>{scope["sectors"]}</strong><span>{t["scope_sectors"]}</span></p>',
        ]
    )
    scope_heading_html = (
        f'    <h3>{t["scope_heading"]}</h3>\n' if t.get("scope_heading") else ""
    )

    # Category/Group breakdown with rowspan category labels
    group_rows = []
    for i, (_, cat_doc) in enumerate(layout["cats"]):
        cat_label = layout["ov_cats"][i][1]
        cat_groups = [
            (g, ap, ins) for g, ap, ins in stats["groups"]
            if stats["group_categories"].get(g, "").casefold() == cat_doc.casefold()
        ]
        if not cat_groups:
            continue
        for j, (g, ap, ins) in enumerate(cat_groups):
            first = (cat_label, len(cat_groups)) if j == 0 else None
            group_rows.append([first, g, ap, ins])
    groups_html = _table(
        [t["cat_col"], t["group_col"], ap_label, ins_label],
        group_rows,
        num_from=2,
        label_cols=2,
        fit_headers=True,
    )

    cats_html = _table(
        [t["cat_col"], ap_label, ins_label],
        [[c["label"], c["ap"], c["ins"]] for c in stats["cats"]],
    )
    sectors_html = _table(
        [t["sector_col"], ap_label, ins_label],
        [list(row) for row in stats["sectors"]],
    )
    mitigations_html = _table(
        [t["mitigation_col"], ap_label, ins_label],
        [list(row) for row in stats["mitigations"]],
        extra_cls="ccpid-narrow",
    )

    cross_cat_labels = CROSS_CAT_LABELS.get(lang, {})
    cross_headers = (
        [t["sector_col"]]
        + [cross_cat_labels.get(label, label) for _, label in layout["cross_cats"]]
        + [t["total_col"]]
    )
    cross_rows = [[sector, *values] for sector, values in stats["cross"]]
    cross_html = _table(cross_headers, cross_rows, uniform_cols=True)

    return f"""<!-- CCPID 数据概览模块 · 自动生成于 {generated} · 由 scripts/generate_webpage.py 生成，请勿手改 -->
<div class="ccpid-overview" id="ccpid-overview">
  <div class="ccpid-scope">
{scope_heading_html}{scope_html}
  </div>
  <div class="ccpid-cols">
    <div class="ccpid-col-left">
      <div class="ccpid-panel">
{cats_html}
      </div>
    </div>
    <div class="ccpid-col-right">
      <div class="ccpid-panel">
{sectors_html}
      </div>
    </div>
  </div>
  <div class="ccpid-panel ccpid-full">
{groups_html}
  </div>
  <div class="ccpid-panel ccpid-cross">
{cross_html}
  </div>
  <div class="ccpid-bottom">
    <div class="ccpid-panel">
{mitigations_html}
    </div>
    <p class="ccpid-note">{t["note"]}</p>
  </div>
</div>
<style>
{CSS}</style>
"""


DOWNLOAD_CSS = """
#ccpid-download {
  font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei",
    "Segoe UI", "Helvetica Neue", Arial, sans-serif;
}
#ccpid-download .ccpid-download-btn {
  display: inline-block;
  background: #14936f;
  color: #fff;
  font-size: 16px;
  font-weight: 600;
  padding: 10px 28px;
  border-radius: 6px;
  text-decoration: none;
}
#ccpid-download .ccpid-download-btn:hover { background: #0e5c46; }
"""


def build_download_html(lang: str, generated: str) -> str:
    t = TEXT[lang]
    return f"""<!-- CCPID 数据下载模块 · 自动生成于 {generated} · 由 scripts/generate_webpage.py 生成，请勿手改 -->
<div class="ccpid-download" id="ccpid-download">
  <a class="ccpid-download-btn" href="CCPID_{lang}.xlsx" download>{t["download_btn"]}</a>
</div>
<style>
{DOWNLOAD_CSS}</style>
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate the CCPID data-overview module (HTML fragment, mirrors the Excel 概览 sheet)."
    )
    parser.add_argument(
        "--outputs-dir", type=Path, default=ROOT / "outputs",
        help="Directory containing the CCPID CSVs (default: outputs/).",
    )
    parser.add_argument(
        "--out", type=Path, default=ROOT / "webpage",
        help="Output directory for the generated module (default: webpage/).",
    )
    parser.add_argument(
        "--lang", choices=["all", "cn", "en"], default="cn",
        help="Languages to generate (default: cn).",
    )
    args = parser.parse_args()

    generated = date.today().isoformat()
    langs = ["cn", "en"] if args.lang == "all" else [args.lang]

    for lang in langs:
        data = load_rows(args.outputs_dir, lang)
        stats = compute_stats(data, lang)
        html = build_html(lang, stats, generated)
        out_dir = args.out
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"overview_{lang}.html"
        out_path.write_text(html, encoding="utf-8")
        print(
            f"Generated {out_path.relative_to(ROOT)} "
            f"({stats['n_approaches']} approaches, {stats['n_instruments']} instruments)"
        )

        dl_path = out_dir / f"download_{lang}.html"
        dl_path.write_text(build_download_html(lang, generated), encoding="utf-8")
        xlsx_src = args.outputs_dir / f"CCPID_{lang}.xlsx"
        xlsx_dst = out_dir / f"CCPID_{lang}.xlsx"
        shutil.copy2(xlsx_src, xlsx_dst)
        print(f"Generated {dl_path.relative_to(ROOT)} (downloads {xlsx_dst.name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
