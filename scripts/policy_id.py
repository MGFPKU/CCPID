#!/usr/bin/env python3
"""Shared helpers for CCPID policy instrument IDs.

IDs follow:
{ISO3 country}{group code}{approach code}I{2-digit instrument sequence}S{3-digit subscheme sequence}
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA_PATH = ROOT / "rules" / "schema.yaml"
POLICY_ID_RE = re.compile(
    r"^(?P<country>[A-Z]{3})(?P<group>[A-Z]{3})(?P<approach>[A-Z]{3})I(?P<instrument>\d{2})S(?P<subscheme>\d{3})$"
)

COUNTRY_ID_CODES = {
    "CHN": "CHN",
    "CHINA": "CHN",
    "中国": "CHN",
}


def normalise_key(value: str) -> str:
    return value.strip().strip('"').strip("'").casefold()


def parse_mapping_entry(line: str) -> tuple[str, str] | None:
    stripped = line.strip()
    if ":" not in stripped:
        return None
    key, value = stripped.rsplit(":", 1)
    key = key.strip().strip('"').strip("'")
    value = value.strip().strip('"').strip("'")
    if not key or not value:
        return None
    return key, value


def load_id_codes(schema_path: Path = DEFAULT_SCHEMA_PATH) -> tuple[dict[str, str], dict[str, str]]:
    """Load group and approach ID codes from rules/schema.yaml."""
    group_codes: dict[str, str] = {}
    approach_codes: dict[str, str] = {}
    if not schema_path.exists():
        return group_codes, approach_codes

    section: str | None = None
    in_known_codes = False
    for raw_line in schema_path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.rstrip()
        if not in_known_codes:
            if re.match(r"^\s{4}known_codes:\s*$", line):
                in_known_codes = True
            continue

        if re.match(r"^\s{2}\S", line):
            break
        if re.match(r"^\s{6}group:\s*$", line):
            section = "group"
            continue
        if re.match(r"^\s{6}approach:\s*$", line):
            section = "approach"
            continue
        if not section or not re.match(r"^\s{8}\S", line):
            continue

        entry = parse_mapping_entry(line)
        if not entry:
            continue
        key, value = entry
        target = group_codes if section == "group" else approach_codes
        target[normalise_key(key)] = value.upper()

    return group_codes, approach_codes


def country_id_code(country: str) -> str:
    return COUNTRY_ID_CODES.get(country.strip().upper()) or COUNTRY_ID_CODES.get(country.strip(), "")


def id_code_lookup(value: str, mapping: dict[str, str]) -> str:
    return mapping.get(normalise_key(value), "")


def generate_policy_id(
    country: str,
    group: str,
    approach: str,
    instrument_sequence: int,
    subscheme_sequence: int = 0,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
) -> str:
    group_codes, approach_codes = load_id_codes(schema_path)
    country_code = country_id_code(country)
    group_code = id_code_lookup(group, group_codes)
    approach_code = id_code_lookup(approach, approach_codes)
    missing = []
    if not country_code:
        missing.append(f"country={country}")
    if not group_code:
        missing.append(f"group={group}")
    if not approach_code:
        missing.append(f"approach={approach}")
    if missing:
        raise ValueError("Cannot generate policy ID; missing code for " + ", ".join(missing))
    return f"{country_code}{group_code}{approach_code}I{instrument_sequence:02d}S{subscheme_sequence:03d}"


def parse_policy_id(instrument_id: str) -> re.Match[str] | None:
    return POLICY_ID_RE.fullmatch(instrument_id.strip().upper())


def expected_id_codes(
    country: str,
    group: str,
    approach: str,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
) -> tuple[str, str, str]:
    group_codes, approach_codes = load_id_codes(schema_path)
    return (
        country_id_code(country),
        id_code_lookup(group, group_codes),
        id_code_lookup(approach, approach_codes),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate CCPID policy instrument IDs.")
    parser.add_argument("--country", required=True)
    parser.add_argument("--group", required=True)
    parser.add_argument("--approach", required=True)
    parser.add_argument("--instrument-sequence", type=int, required=True)
    parser.add_argument("--subscheme-sequence", type=int, default=0)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA_PATH)
    args = parser.parse_args(argv)
    print(
        generate_policy_id(
            args.country,
            args.group,
            args.approach,
            args.instrument_sequence,
            args.subscheme_sequence,
            args.schema,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
