#!/usr/bin/env python3
"""One-off fix for EN outputs (2026-09-01):
1. Case-normalise controlled multi/single-value fields (part-wise majority casing).
2. Fix 'Industry; Business' emission sector to 'Buildings; Industry' (aligned with CN 建筑；工业).
3. Align adoption/start dates of CHNTAXULTI01S000 and CHNTAXULTI02S000 with CN (01/11/1988).

Backs up each file to *.bak_casefix before rewriting.
"""

from __future__ import annotations

import collections
import csv
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"

FILES = [
    "economic_instruments",
    "regulatory_instruments",
    "government_i_c",
    "information_instruments",
    "voluntary_approaches",
]

COLUMNS_TO_NORMALIZE = [
    "Emission sector",
    "Sub-sector",
    "Objective",
    "Functioning channel",
    "Jurisdiction level",
    "Status",
    "Asset (Status)",
    "Agent",
    "Activity",
    "Mitigation effects",
    "Mitigation co-benefits",
]

SECTOR_FIX = {
    "CHNPRFMELI02S000": "Buildings; Industry",
    "CHNPRFMELI06S000": "Buildings; Industry",
}

DATE_FIX = {
    "CHNTAXULTI01S000": {"Adoption date": "01/11/1988", "Start date": "01/11/1988"},
    "CHNTAXULTI02S000": {"Adoption date": "01/11/1988", "Start date": "01/11/1988"},
}


def load_rows() -> dict[str, tuple[list[str], list[dict]]]:
    data = {}
    for f in FILES:
        p = OUT / f"CCPID_en_{f}.csv"
        with open(p, encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            data[f] = (list(reader.fieldnames), list(reader))
    return data


def part_casing_map(data: dict, col: str) -> dict[str, str]:
    """casefold -> most frequent original spelling, counted per ';'-separated part."""
    variants: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for _, rows in data.values():
        for r in rows:
            v = (r.get(col) or "").strip()
            if not v or v == "N/A":
                continue
            for part in v.split(";"):
                part = part.strip()
                if part and part != "N/A":
                    variants[part.casefold()][part] += 1
    return {cf: counter.most_common(1)[0][0] for cf, counter in variants.items()}


def normalize_cell(value: str, cmap: dict[str, str]) -> str:
    v = value.strip()
    if not v or v == "N/A":
        return v
    parts = []
    for part in v.split(";"):
        part = part.strip()
        if not part:
            continue
        if part == "N/A":
            parts.append("N/A")
            continue
        parts.append(cmap.get(part.casefold(), part))
    return "; ".join(parts)


def detect_newline(p: Path) -> str:
    with open(p, "rb") as fh:
        head = fh.read(4096)
    return "\r\n" if b"\r\n" in head else "\n"


def main() -> int:
    data = load_rows()
    maps = {col: part_casing_map(data, col) for col in COLUMNS_TO_NORMALIZE}

    total_changes = 0
    for f in FILES:
        p = OUT / f"CCPID_en_{f}.csv"
        fieldnames, rows = data[f]
        changes = 0
        for r in rows:
            row_id = r["Policy Instrument ID"]
            for col in COLUMNS_TO_NORMALIZE:
                if col not in r:
                    continue
                new = normalize_cell(r[col] or "", maps[col])
                if new != r[col]:
                    r[col] = new
                    changes += 1
            if row_id in SECTOR_FIX:
                new = SECTOR_FIX[row_id]
                if r["Emission sector"] != new:
                    print(f"  {row_id}: Emission sector {r['Emission sector']!r} -> {new!r}")
                    r["Emission sector"] = new
                    changes += 1
            if row_id in DATE_FIX:
                for col, new in DATE_FIX[row_id].items():
                    if r.get(col) != new:
                        print(f"  {row_id}: {col} {r.get(col)!r} -> {new!r}")
                        r[col] = new
                        changes += 1
        if not changes:
            print(f"{f}: no changes")
            continue
        shutil.copy2(p, str(p) + ".bak_casefix")
        newline = detect_newline(p)
        with open(p, "w", encoding="utf-8-sig", newline="") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=fieldnames, extrasaction="raise", lineterminator=newline
            )
            writer.writeheader()
            writer.writerows(rows)
        print(f"{f}: {changes} cell(s) changed (backup: {p.name}.bak_casefix)")
        total_changes += changes

    print(f"\nTotal cells changed: {total_changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
