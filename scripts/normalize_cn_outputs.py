#!/usr/bin/env python3
"""Normalize Chinese CSV outputs before export and validation.

Replaces legacy ``未指明`` with ``N/A``, validates emission sector values,
flags non-canonical URLs, and detects English text in Chinese-only fields.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"

CN_CSV_PATTERNS = ["CCPID_cn_*.csv"]

# Chinese equivalents of valid IPCC emission sectors (from schema.yaml)
VALID_EMISSION_SECTORS_CN = {
    "能源", "交通", "建筑", "工业", "农业、林业和其他土地利用", "废弃物", "跨部门",
    "N/A",
}

# Fields that should contain only Chinese (not English prose)
CN_ONLY_FIELDS = [
    "强度（单位）", "目标", "排放部门", "描述",
    "本国工具名称", "工具/子方案", "组别", "路径",
    "国家", "管辖层级", "状态", "减缓相关性", "作用渠道",
    "减缓效果", "受规制资产（状态）",
]

LATIN_RE = re.compile(r"[a-z]{3,}")  # 3+ consecutive lowercase = English prose

# Known English enum values that should not appear in Chinese CSVs
# Maps CN header name → set of English values to flag
CN_ENGLISH_ENUM_VALUES: dict[str, dict[str, str]] = {
    "国家": {"CHN": "中国"},
    "管辖层级": {
        "national": "国家", "subnational": "省级",
        "supranational": "超国家", "special economic zone (SEZ)": "经济特区",
    },
    "状态": {
        "in force": "生效", "scheduled": "计划实施",
        "ended": "已终止", "non-existent": "不存在",
    },
    "减缓相关性": {"Direct": "直接", "Indirect": "间接"},
    "作用渠道": {"Supply-side": "供给侧", "demand-side": "需求侧", "environment": "环境"},
    "工具/子方案": {"Instrument": "工具", "Subscheme": "子方案"},
    "减缓效果": {"positive": "正向", "negative": "负向", "neutral": "中性", "unknown": "未知"},
    "受规制资产（状态）": {"New": "新建", "existing": "既有"},
}

# Canonical Chinese values for Asset Status (combinations of 新建/既有 are valid)
_VALID_ASSET_STATUS_CN_PART = {"新建", "既有", "N/A"}

# Province/city tax bureau subdomains that are local, not central
LOCAL_TAX_BUREAU_RE = re.compile(
    r"https?://(?!fgk\.|www\.|12366\.)[a-z]+\.chinatax\.gov\.cn/"
)

# Known non-canonical URL patterns
NON_CANONICAL_URL_PATTERNS = [
    (re.compile(r"https?://12366\.chinatax\.gov\.cn/fwtz/print"),
     "tax bureau print service — use canonical fgk.chinatax.gov.cn or gov.cn URL"),
    (re.compile(r"https?://www\d*\.deloitte\.com/"),
     "consulting firm — replace with official government source"),
    (re.compile(r"https?://.*\.(pdf|doc|docx)$"),
     "direct document download — replace with the page linking to this document"),
]


def split_multi(value: str) -> list[str]:
    """Split a multi-value field using ASCII or full-width semicolons."""
    value = value.replace("；", ";")
    return [v.strip() for v in value.split(";") if v.strip()]


def iter_urls(value: str) -> list[str]:
    """Extract individual URLs from a semicolon-delimited field."""
    value = value.replace("；", ";")
    return [u.strip() for u in value.split(";") if u.strip() and "://" in u]


def normalize_cn_csv(path: Path) -> int:
    """Replace 未指明 with N/A. Returns replacement count."""
    content = path.read_text(encoding="utf-8-sig")
    count = content.count("未指明")
    if count:
        content = content.replace("未指明", "N/A")
        path.write_text(content, encoding="utf-8-sig", newline="")
    return count



def check_emission_sector(path: Path) -> list[str]:
    """Flag invalid emission sector values."""
    warnings = []
    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        try:
            es_idx = header.index("排放部门")
        except ValueError:
            return warnings
        for row in reader:
            rid = row[0]
            val = row[es_idx].strip() if es_idx < len(row) else ""
            if not val or val == "N/A":
                continue
            for part in split_multi(val):
                if part not in VALID_EMISSION_SECTORS_CN:
                    allowed = ", ".join(sorted(VALID_EMISSION_SECTORS_CN - {"N/A"}))
                    warnings.append(
                        f"{path.name} | {rid} | 排放部门: "
                        f"invalid sector \"{part}\" — allowed: {allowed}"
                    )
    return warnings


def check_urls(path: Path) -> list[str]:
    """Flag non-canonical URLs using specific known-bad patterns."""
    warnings = []
    url_col_names = ("法律文件链接", "其他网页链接")
    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        url_cols = [(i, h.strip()) for i, h in enumerate(header)
                     if h.strip() in url_col_names]
        if not url_cols:
            return warnings
        for row in reader:
            rid = row[0]
            for col_idx, col_name in url_cols:
                val = row[col_idx].strip() if col_idx < len(row) else ""
                if not val or val == "N/A":
                    continue
                for url in iter_urls(val):
                    if LOCAL_TAX_BUREAU_RE.search(url):
                        warnings.append(
                            f"{path.name} | {rid} | {col_name}: "
                            f"provincial/city tax bureau — prefer fgk.chinatax.gov.cn — {url}"
                        )
                        continue
                    for pattern, reason in NON_CANONICAL_URL_PATTERNS:
                        if pattern.search(url):
                            warnings.append(
                                f"{path.name} | {rid} | {col_name}: "
                                f"{reason} — {url}"
                            )
                            break
    return warnings


def check_cn_only_fields(path: Path) -> list[str]:
    """Warn if Chinese-only fields contain English prose."""
    warnings = []
    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        idx_map = {field: header.index(field)
                   for field in CN_ONLY_FIELDS if field in header}
        for row in reader:
            rid = row[0]
            for field, idx in idx_map.items():
                val = row[idx] if idx < len(row) else ""
                m = LATIN_RE.search(val)
                if m and "N/A" not in m.group():
                    warnings.append(
                        f"{path.name} | {rid} | {field}: "
                        f"English text detected — \"{m.group()}\""
                    )
    return warnings


def check_cn_enum_values(path: Path) -> list[str]:
    """Flag English enum values and non-standard Asset Status in Chinese CSVs."""
    warnings = []
    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        # Build index for fields we care about
        idx_map: dict[str, int] = {}
        for field in CN_ENGLISH_ENUM_VALUES:
            try:
                idx_map[field] = header.index(field)
            except ValueError:
                pass
        # Also index Asset Status for valid-value check
        try:
            as_idx = header.index("受规制资产（状态）")
        except ValueError:
            as_idx = None

        for row in reader:
            rid = row[0]
            for field, idx in idx_map.items():
                val = row[idx].strip() if idx < len(row) else ""
                if not val or val == "N/A":
                    continue
                en_map = CN_ENGLISH_ENUM_VALUES[field]
                for part in split_multi(val):
                    if part in en_map:
                        cn_val = en_map[part]
                        warnings.append(
                            f"{path.name} | {rid} | {field}: "
                            f"English value \"{part}\" found — use \"{cn_val}\" instead"
                        )
            # Asset Status valid-value check
            if as_idx is not None:
                as_val = row[as_idx].strip() if as_idx < len(row) else ""
                if not as_val or as_val == "N/A":
                    continue
                for part in split_multi(as_val):
                    if part not in _VALID_ASSET_STATUS_CN_PART:
                        warnings.append(
                            f"{path.name} | {rid} | 受规制资产（状态）: "
                            f"non-standard value \"{part}\" — allowed: 新建, 既有, N/A"
                        )
    return warnings


def check_revision_weblinks(path: Path) -> list[str]:
    """Flag instruments that have a revision but no revision weblinks."""
    warnings = []
    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        try:
            rev_idx = header.index("最近修订")
        except ValueError:
            return warnings
        try:
            other_idx = header.index("其他网页链接")
        except ValueError:
            return warnings

        for row in reader:
            rid = row[0]
            rev_date = row[rev_idx].strip() if rev_idx < len(row) else ""
            rev_detail = row[rev_idx + 1].strip() if rev_idx + 1 < len(row) else ""
            other_urls = row[other_idx].strip() if other_idx < len(row) else ""

            if rev_date and rev_date != "N/A" and (not other_urls or other_urls == "N/A"):
                detail_preview = rev_detail[:80] if rev_detail and rev_detail != "N/A" else ""
                warnings.append(
                    f"{path.name} | {rid} | 其他网页链接: "
                    f"instrument has a revision ({rev_date}) but no revision weblinks"
                    + (f" — {detail_preview}" if detail_preview else "")
                )
    return warnings


def check_book_title_marks(path: Path) -> list[str]:
    """Flag 《》 book-title marks in Legal statute field."""
    warnings = []
    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        try:
            ls_idx = header.index("法律文件名称")
        except ValueError:
            return warnings
        for row in reader:
            rid = row[0]
            val = row[ls_idx].strip() if ls_idx < len(row) else ""
            if "《" in val or "》" in val:
                warnings.append(
                    f"{path.name} | {rid} | 法律文件名称: "
                    f"contains book-title marks 《》 — remove them"
                )
    return warnings


def check_cobenefits_format(path: Path) -> list[str]:
    """Flag parenthetical explanations in co-benefits field."""
    warnings = []
    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        try:
            cb_idx = header.index("减缓协同效益")
        except ValueError:
            return warnings
        for row in reader:
            rid = row[0]
            val = row[cb_idx].strip() if cb_idx < len(row) else ""
            if not val or val == "N/A":
                continue
            # Check for Chinese parenthetical explanations: xxx（说明说明）
            if re.search(r"（[^）]{5,}）", val):
                chinese_match = re.findall(r"（([^）]{5,})）", val)
                preview = chinese_match[0][:40] + "..." if len(chinese_match[0]) > 40 else chinese_match[0]
                warnings.append(
                    f"{path.name} | {rid} | 减缓协同效益: "
                    f"contains parenthetical explanation \"（{preview}）\" — use short keyword phrases"
                )
            # Check for English parenthetical explanations
            if re.search(r"\([^)]{5,}\)", val):
                eng_match = re.findall(r"\(([^)]{5,})\)", val)
                if eng_match:
                    preview = eng_match[0][:40] + "..." if len(eng_match[0]) > 40 else eng_match[0]
                    warnings.append(
                        f"{path.name} | {rid} | 减缓协同效益: "
                        f"contains parenthetical explanation \"({preview})\" — use short keyword phrases"
                    )
    return warnings


def check_instrument_name_is_not_document_title(path: Path) -> list[str]:
    """Flag instrument names that are legal-document titles rather than descriptive names."""
    warnings = []
    # CN patterns: 关于...的公告/通知/办法/通告 etc.
    cn_doc_title_re = re.compile(r"^关于.+[的].*(公告|通知|办法|通告|决定|命令|意见|函|批复|报告)$")
    # EN patterns: Announcement on..., Notice on..., Circular on... etc.
    en_doc_title_re = re.compile(r"^(Announcement|Notice|Circular|Decree|Order|Decision|Opinion)\s+(on|of)\s+", re.IGNORECASE)

    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        try:
            cn_idx = header.index("本国工具名称")
        except ValueError:
            cn_idx = None
        try:
            en_idx = header.index("英文工具名称")
        except ValueError:
            en_idx = None
        if cn_idx is None and en_idx is None:
            return warnings

        for row in reader:
            rid = row[0]
            if cn_idx is not None:
                val = row[cn_idx].strip() if cn_idx < len(row) else ""
                if cn_doc_title_re.match(val):
                    warnings.append(
                        f"{path.name} | {rid} | 本国工具名称: "
                        f"\"{val}\" looks like a document title — use a descriptive instrument name"
                    )
            if en_idx is not None:
                val = row[en_idx].strip() if en_idx < len(row) else ""
                if en_doc_title_re.match(val):
                    warnings.append(
                        f"{path.name} | {rid} | 英文工具名称: "
                        f"\"{val}\" is a document title — use a descriptive instrument name"
                    )
    return warnings


def check_compliance_enforcement_consistency(path: Path) -> list[str]:
    """Flag when compliance details mention 罚款 but enforcement doesn't include it."""
    warnings = []
    with path.open(encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        try:
            ce_idx = header.index("合规执行")
        except ValueError:
            return warnings
        try:
            cd_idx = header.index("合规执行详情")
        except ValueError:
            return warnings
        for row in reader:
            rid = row[0]
            enf = row[ce_idx].strip() if ce_idx < len(row) else ""
            detail = row[cd_idx].strip() if cd_idx < len(row) else ""
            if not enf or enf == "N/A" or not detail or detail == "N/A":
                continue
            if "罚款" in detail and "罚款" not in enf:
                warnings.append(
                    f"{path.name} | {rid} | 合规执行: "
                    f"details mention 罚款 but enforcement is \"{enf}\" — should include 罚款"
                )
    return warnings


def main() -> int:
    total_replacements = 0
    all_warnings = []

    for pattern in CN_CSV_PATTERNS:
        for csv_path in sorted(OUTPUTS.glob(pattern)):
            count = normalize_cn_csv(csv_path)
            total_replacements += count
            if count:
                print(f"  {csv_path.name}: {count} 未指明 → N/A")

            all_warnings.extend(check_emission_sector(csv_path))
            all_warnings.extend(check_urls(csv_path))
            all_warnings.extend(check_cn_only_fields(csv_path))
            all_warnings.extend(check_cn_enum_values(csv_path))
            all_warnings.extend(check_revision_weblinks(csv_path))
            all_warnings.extend(check_book_title_marks(csv_path))
            all_warnings.extend(check_cobenefits_format(csv_path))
            all_warnings.extend(check_compliance_enforcement_consistency(csv_path))
            all_warnings.extend(check_instrument_name_is_not_document_title(csv_path))

    if total_replacements:
        print(f"  Total: {total_replacements} replacements")
    else:
        print("  No 未指明 found (already normalized)")

    if all_warnings:
        print(f"\n  Warnings ({len(all_warnings)}):")
        for w in all_warnings:
            print(f"    {w}")
    else:
        print("  No warnings.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
