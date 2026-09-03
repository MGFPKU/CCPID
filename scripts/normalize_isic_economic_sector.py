#!/usr/bin/env python3
"""Normalize filled Economic sector values to ISIC Rev.4 division codes."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"

FIELD_NAMES = {
    "Economic sector",
    "经济行业",
}

LEGACY_TO_ISIC = {
    "D44": "D35",  # electricity supply/generation
    "C31": "C24",  # steel/basic metals
    "C30": "C23",  # cement/non-metallic mineral products
    "C32": "C24",  # aluminium/basic metals
    "C36": "C29",  # motor vehicles
    "G56": "G45",  # motor vehicle trade
}

# Legacy GB/T 4754 codes are remapped only when a token is NOT already a valid
# ISIC Rev.4 division (C30, C31, C32 are valid ISIC divisions).
ISIC_DIVISION_RANGES = {
    "A": range(1, 4),
    "B": range(5, 10),
    "C": range(10, 34),
    "D": range(35, 36),
    "E": range(36, 40),
    "F": range(41, 44),
    "G": range(45, 48),
    "H": range(49, 54),
    "I": range(55, 57),
    "J": range(58, 64),
    "K": range(64, 67),
    "L": range(68, 69),
    "M": range(69, 76),
    "N": range(77, 83),
    "O": range(84, 85),
    "P": range(85, 86),
    "Q": range(86, 89),
    "R": range(90, 94),
    "S": range(94, 97),
    "T": range(97, 99),
    "U": range(99, 100),
}


def is_valid_isic_division(value: str) -> bool:
    match = re.fullmatch(r"([A-U])(\d{2})", value.strip().upper())
    if not match:
        return False
    section, division = match.group(1), int(match.group(2))
    return division in ISIC_DIVISION_RANGES.get(section, range(0))


def split_codes(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[;；|]", value) if part.strip()]


def join_codes(codes: list[str], separator: str) -> str:
    result: list[str] = []
    for code in codes:
        original = code.strip()
        if not is_valid_isic_division(original):
            mapped = LEGACY_TO_ISIC.get(original.upper(), original)
        else:
            mapped = original
        if mapped and mapped not in result:
            result.append(mapped)
    return separator.join(result)


def normalize_value(value: str) -> str:
    if not value:
        return value
    separator = "；" if "；" in value and ";" not in value else "; "
    return join_codes(split_codes(value), separator)


def update_csv(path: Path) -> bool:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    changed = False
    for row in rows:
        for field in fieldnames:
            should_check = field in FIELD_NAMES or (
                path.name == "evidence_log.csv" and field == "field_value" and row.get("field_name") in FIELD_NAMES
            )
            if not should_check:
                continue
            old = row.get(field, "")
            new = normalize_value(old)
            if new != old:
                row[field] = new
                changed = True

    if changed:
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    return changed


def main() -> int:
    changed = []
    for path in OUTPUTS.glob("*.csv"):
        if update_csv(path):
            changed.append(path)
    for path in changed:
        print(f"Normalized {path}")
    if not changed:
        print("No Economic sector values needed normalization.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
