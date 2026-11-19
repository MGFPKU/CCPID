#!/usr/bin/env python3
"""Advance Status (状态) automatically from dates so statuses stay current over time.

Rules (date-driven only; other statuses are untouched):
- scheduled/计划实施 with Start date (CN: 生效日期) on or before today -> in force/生效
- in force/生效 with End date (CN: 截止日期) before today               -> ended/已终止

Updates both the CN and EN category CSVs so the two sides stay consistent.
Run before export and validation.
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from validate_dataset import CN_FIELD_ALIASES, normalise_header, normalise_value, parse_date

ROOT = SCRIPT_DIR.parent

CSV_FILES = [
    "CCPID_cn_economic_instruments.csv", "CCPID_en_economic_instruments.csv",
    "CCPID_cn_government_i_c.csv", "CCPID_en_government_i_c.csv",
    "CCPID_cn_regulatory_instruments.csv", "CCPID_en_regulatory_instruments.csv",
    "CCPID_cn_information_instruments.csv", "CCPID_en_information_instruments.csv",
    "CCPID_cn_voluntary_approaches.csv", "CCPID_en_voluntary_approaches.csv",
]

CN_ID_KEY = "政策工具ID"
SCHEDULED = {"scheduled", "计划实施"}
IN_FORCE = {"in force", "生效"}


def find_col(fieldnames, names):
    by_norm = {normalise_header(k): k for k in fieldnames}
    for name in names:
        key = by_norm.get(normalise_header(name))
        if key is None:
            alias = CN_FIELD_ALIASES.get(normalise_header(name))
            key = by_norm.get(normalise_header(alias or ""))
        if key is not None:
            return key
    return None


def update_file(path: Path) -> list[tuple[str, str, str]]:
    with io.open(path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)
    status_col = find_col(fieldnames, ["Status", "status"])
    start_col = find_col(fieldnames, ["Start date", "start_date"])
    end_col = find_col(fieldnames, ["End date", "end_date"])
    id_col = CN_ID_KEY if CN_ID_KEY in fieldnames else "Policy Instrument ID"
    is_cn = CN_ID_KEY in fieldnames
    today = dt.date.today()
    changed = []
    for row in rows:
        status = normalise_value(row.get(status_col)).lower()
        if not status:
            continue
        start_date = parse_date(normalise_value(row.get(start_col)))
        end_date = parse_date(normalise_value(row.get(end_col)))
        if status in SCHEDULED and start_date and start_date <= today:
            row[status_col] = "生效" if is_cn else "in force"
            changed.append((row[id_col], status, row[status_col]))
        elif status in IN_FORCE and end_date and end_date < today:
            row[status_col] = "已终止" if is_cn else "ended"
            changed.append((row[id_col], status, row[status_col]))
    if changed:
        with io.open(path, "w", encoding="utf-8-sig", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\r\n")
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
    return changed


def main() -> int:
    total = 0
    for name in CSV_FILES:
        path = ROOT / "outputs" / name
        changed = update_file(path)
        for pid, old, new in changed:
            print(f"{name}: {pid}: {old} -> {new}")
        total += len(changed)
    print(f"statuses updated: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
