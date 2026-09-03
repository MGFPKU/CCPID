#!/usr/bin/env python3
"""Create and update CCPID draft rows for one policy instrument at a time.

This script keeps first-pass data entry simple and reproducible:

- one CSV dataset per template/category;
- one evidence-log CSV with field-level source metadata;
- draft-entry validation before handing files to ``validate_dataset.py``.

It intentionally uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from policy_id import expected_id_codes, generate_policy_id, parse_policy_id


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "rules" / "schema.yaml"
CN_TEMPLATE_PATH = ROOT / "inputs" / "template_cn.xlsx"
DEFAULT_OUTPUTS_DIR = ROOT / "outputs"
DEFAULT_EVIDENCE_LOG = DEFAULT_OUTPUTS_DIR / "evidence_log.csv"

DRAFT_REQUIRED = [
    "Policy Instrument ID",
    "Instrument / subscheme",
    "Group",
    "Approach",
    "Country",
    "Jurisdiction level",
    "Status",
]

NAME_FIELDS = [
    "Domestic instrument name",
    "English instrument name",
    "Domestic name",
    "English name",
]

ROW_METADATA_FIELDS = [
    "source_url",
    "source_title",
    "evidence_quote",
    "confidence_score",
    "needs_human_review",
    "review_note",
]

INSTRUMENT_SPECIFIC_FIELD_PREFIXES = {
    "Tax": (
        "Subsidy:",
        "Trading System:",
        "补贴：",
        "交易系统：",
    ),
    "Subsidy": (
        "Tax and Tax Incentive:",
        "Trading System:",
        "税收及激励：",
        "交易系统：",
    ),
    "Trading scheme": (
        "Tax and Tax Incentive:",
        "Subsidy:",
        "税收及激励：",
        "补贴：",
    ),
    "税收": (
        "补贴：",
        "交易系统：",
    ),
    "补贴": (
        "税收及激励：",
        "交易系统：",
    ),
    "交易机制": (
        "Tax and Tax Incentive:",
        "Subsidy:",
        "税收及激励：",
        "补贴：",
    ),
    "Administered price": (
        "Tax and Tax Incentive:",
        "Subsidy:",
        "Trading System:",
        "税收及激励：",
        "补贴：",
        "交易系统：",
    ),
    "行政定价": (
        "税收及激励：",
        "补贴：",
        "交易系统：",
    ),
}

EVIDENCE_FIELDS = [
    "instrument_id",
    "field_name",
    "field_value",
    "source_url",
    "source_title",
    "evidence_quote",
    "confidence_score",
    "needs_human_review",
    "review_note",
    "updated_at",
]

TEMPLATE_ALIASES = {
    "economic": "Economic instruments",
    "regulatory": "Regulatory instruments",
    "government": "Government I&C",
    "government i&c": "Government I&C",
    "information": "Information instruments",
    "voluntary": "Voluntary approaches",
}

CN_SHEET_BY_TEMPLATE = {
    "Economic instruments": "经济工具",
    "Regulatory instruments": "规制工具",
    "Government I&C": "政府投资与消费",
    "Information instruments": "信息工具",
    "Voluntary approaches": "自愿措施",
}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.strip().lower())
    return slug.strip("_") or "dataset"


def normalise_header(value: str) -> str:
    return "".join(ch for ch in value.strip().lower() if ch.isalnum())


def parse_key_value(raw: str) -> tuple[str, str]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError(f"Expected FIELD=VALUE, got: {raw}")
    key, value = raw.split("=", 1)
    key = key.strip()
    if not key:
        raise argparse.ArgumentTypeError(f"Empty field name in: {raw}")
    return key, value.strip()


def load_templates(schema_path: Path = SCHEMA_PATH) -> dict[str, list[str]]:
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema not found: {schema_path}")

    templates: dict[str, list[str]] = {}
    current_template: str | None = None
    in_templates = False
    in_columns = False

    for line in schema_path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("templates:"):
            in_templates = True
            continue
        if in_templates and line and not line.startswith(" "):
            break
        if not in_templates:
            continue

        template_match = re.match(r"^  (\S[^:]+):\s*$", line)
        if template_match:
            current_template = template_match.group(1).strip().strip('"')
            templates.setdefault(current_template, [])
            in_columns = False
            continue

        if current_template and re.match(r"^    columns:\s*$", line):
            in_columns = True
            continue

        if in_columns:
            column_match = re.match(r"^      - (.+?)\s*$", line)
            if column_match:
                column = column_match.group(1).strip().strip('"')
                templates[current_template].append(column)
                continue
            if line.startswith("    ") and not line.startswith("      "):
                in_columns = False

    if not templates:
        raise RuntimeError(f"No templates parsed from {schema_path}")
    return templates


_VALID_STATUSES: set[str] | None = None
_VALID_STATUS_ALIASES: dict[str, str] = {
    "生效": "in force",
    "计划实施": "scheduled",
    "已终止": "ended",
    "不存在": "non-existent",
}


def load_valid_statuses(schema_path: Path = SCHEMA_PATH) -> set[str]:
    """Lazily load allowed Status values from schema.yaml allowed_values section."""
    global _VALID_STATUSES
    if _VALID_STATUSES is not None:
        return _VALID_STATUSES
    _VALID_STATUSES = set()
    if not schema_path.exists():
        return _VALID_STATUSES
    in_allowed_values = False
    in_status = False
    for line in schema_path.read_text(encoding="utf-8-sig").splitlines():
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0 and stripped:
            if stripped == "allowed_values:":
                in_allowed_values = True
                continue
            if in_allowed_values:
                break  # next top-level key
        if not in_allowed_values:
            continue
        if indent == 2 and stripped == "Status:":
            in_status = True
            continue
        if in_status:
            if indent == 2 and stripped:
                break  # next allowed_values key at same level
            if indent == 4 and stripped.startswith("- "):
                _VALID_STATUSES.add(stripped[2:].strip().strip('"'))
    return _VALID_STATUSES


def validate_status(value: str, lang: str) -> str | None:
    """Return error message if status is invalid, or None if valid."""
    if not value.strip():
        return None  # blank is checked separately by draft_issues
    canonical = _VALID_STATUS_ALIASES.get(value.strip(), value.strip())
    valid = load_valid_statuses()
    if canonical not in valid:
        allowed = ", ".join(sorted(valid)) + ", " + ", ".join(_VALID_STATUS_ALIASES)
        return f"Invalid status '{value}'. Allowed values: {allowed}"
    return None


def cell_ref_column(ref: str) -> int:
    letters = re.sub(r"[^A-Z]", "", ref.upper())
    value = 0
    for letter in letters:
        value = value * 26 + (ord(letter) - ord("A") + 1)
    return value


def load_xlsx_row_headers(path: Path, row_number: int = 2) -> dict[str, list[str]]:
    """Read one header row from each worksheet without third-party packages."""
    if not path.exists():
        raise FileNotFoundError(f"Template workbook not found: {path}")

    ns = {
        "a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    }
    with zipfile.ZipFile(path) as archive:
        shared_strings: list[str] = []
        try:
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in root.findall("a:si", ns):
                shared_strings.append("".join(t.text or "" for t in item.findall(".//a:t", ns)))
        except KeyError:
            pass

        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        relmap = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels}
        headers_by_sheet: dict[str, list[str]] = {}
        sheets = workbook.find("a:sheets", ns)
        if sheets is None:
            return headers_by_sheet
        for sheet in sheets:
            sheet_name = sheet.attrib["name"]
            rel_id = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
            target = relmap[rel_id]
            if target.startswith("/xl/"):
                worksheet = ET.fromstring(archive.read(target[1:]))
            else:
                worksheet = ET.fromstring(archive.read("xl/" + target))
            rows = worksheet.findall(".//a:sheetData/a:row", ns)
            selected = next((row for row in rows if row.attrib.get("r") == str(row_number)), None)
            if selected is None:
                continue
            values_by_index: dict[int, str] = {}
            for cell in selected.findall("a:c", ns):
                cell_type = cell.attrib.get("t", "")
                if cell_type == "inlineStr":
                    is_el = cell.find("a:is", ns)
                    value = "".join(t.text or "" for t in (is_el.findall(".//a:t", ns) if is_el is not None else []))
                else:
                    raw_value = cell.find("a:v", ns)
                    value = raw_value.text if raw_value is not None else ""
                    if cell_type == "s" and value:
                        value = shared_strings[int(value)]
                values_by_index[cell_ref_column(cell.attrib.get("r", ""))] = value
            max_index = max(values_by_index, default=0)
            headers_by_sheet[sheet_name] = [values_by_index.get(index, "") for index in range(1, max_index + 1)]
    return headers_by_sheet


def get_template_columns(template: str, lang: str, templates: dict[str, list[str]]) -> list[str]:
    if lang == "en":
        return templates[template]
    cn_headers = load_xlsx_row_headers(CN_TEMPLATE_PATH)
    sheet_name = CN_SHEET_BY_TEMPLATE[template]
    headers = cn_headers.get(sheet_name, [])
    if len(headers) != len(templates[template]):
        raise RuntimeError(
            f"Chinese template/header length mismatch for {template}: "
            f"{len(headers)} vs {len(templates[template])}"
        )
    return headers


def build_field_aliases(template: str, lang: str, templates: dict[str, list[str]]) -> dict[str, str]:
    english = templates[template]
    output = get_template_columns(template, lang, templates)
    aliases: dict[str, str] = {}
    for source, target in zip(english, output):
        aliases[normalise_header(source)] = target
        aliases[normalise_header(target)] = target
    return aliases


def resolve_template(name: str, templates: dict[str, list[str]]) -> str:
    if name in templates:
        return name
    alias = TEMPLATE_ALIASES.get(name.strip().lower())
    if alias and alias in templates:
        return alias

    by_norm = {normalise_header(template): template for template in templates}
    resolved = by_norm.get(normalise_header(name))
    if resolved:
        return resolved

    choices = ", ".join(sorted(templates))
    raise ValueError(f"Unknown template '{name}'. Choose one of: {choices}")


def default_dataset_path(template: str, lang: str, outputs_dir: Path) -> Path:
    return outputs_dir / f"CCPID_{lang}_{slugify(template)}.csv"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        return [], []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def canonicalise_fields(values: dict[str, str], fieldnames: list[str], aliases: dict[str, str]) -> dict[str, str]:
    by_norm = {normalise_header(name): name for name in fieldnames}
    by_norm.update(aliases)
    canonical: dict[str, str] = {}
    unknown: list[str] = []
    for key, value in values.items():
        resolved = by_norm.get(normalise_header(key))
        if resolved:
            canonical[resolved] = value
        else:
            unknown.append(key)
    if unknown:
        available = ", ".join(unknown)
        raise ValueError(f"Unknown field(s) for this template: {available}")
    return canonical


def localise_values(values: dict[str, str], lang: str) -> dict[str, str]:
    if lang != "cn":
        return values
    return {key: "未找到" if value.strip().lower() == "not found" else value for key, value in values.items()}


def get_row_value(row: dict[str, str], names: list[str], aliases: dict[str, str]) -> str:
    by_norm = {normalise_header(key): key for key in row}
    for name in names:
        target = aliases.get(normalise_header(name), name)
        key = by_norm.get(normalise_header(target))
        if key and row.get(key, "").strip():
            return row[key].strip()
    return ""


def set_row_value(row: dict[str, str], name: str, value: str, aliases: dict[str, str]) -> None:
    target = aliases.get(normalise_header(name), name)
    row[target] = value


def row_has_name(row: dict[str, str], aliases: dict[str, str]) -> bool:
    return any(get_row_value(row, [field], aliases) for field in NAME_FIELDS)


def draft_issues(row: dict[str, str], aliases: dict[str, str]) -> list[str]:
    issues = [field for field in DRAFT_REQUIRED if not get_row_value(row, [field], aliases)]
    if not row_has_name(row, aliases):
        issues.append("at least one policy name")
    return issues


def apply_defaults(row: dict[str, str], instrument_id: str, values: dict[str, str], aliases: dict[str, str], lang: str = "en") -> None:
    row.update(values)
    set_row_value(row, "Policy Instrument ID", instrument_id, aliases)
    if lang == "cn":
        if not get_row_value(row, ["Instrument / subscheme"], aliases):
            set_row_value(row, "Instrument / subscheme", "工具", aliases)
        if not get_row_value(row, ["Country"], aliases):
            set_row_value(row, "Country", "中国", aliases)
        if not get_row_value(row, ["Jurisdiction level"], aliases):
            set_row_value(row, "Jurisdiction level", "国家", aliases)
    else:
        if not get_row_value(row, ["Instrument / subscheme"], aliases):
            set_row_value(row, "Instrument / subscheme", "Instrument", aliases)
        if not get_row_value(row, ["Country"], aliases):
            set_row_value(row, "Country", "CHN", aliases)
        if not get_row_value(row, ["Jurisdiction level"], aliases):
            set_row_value(row, "Jurisdiction level", "national", aliases)


def coerce_rows_to_fieldnames(
    rows: list[dict[str, str]],
    fieldnames: list[str],
    aliases: dict[str, str],
) -> list[dict[str, str]]:
    coerced: list[dict[str, str]] = []
    for row in rows:
        next_row = {field: "" for field in fieldnames}
        for source, value in row.items():
            target = aliases.get(normalise_header(source))
            if target in next_row:
                next_row[target] = value
        coerced.append(next_row)
    return coerced


def fill_empty_template_cells(
    row: dict[str, str],
    fieldnames: list[str],
    aliases: dict[str, str],
    value: str = "N/A",
) -> None:
    group = get_row_value(row, ["Group"], aliases)
    skip_prefixes = INSTRUMENT_SPECIFIC_FIELD_PREFIXES.get(group, ())
    for field in fieldnames:
        if any(field.startswith(prefix) for prefix in skip_prefixes):
            continue
        if not row.get(field, "").strip():
            row[field] = value


def load_json_values(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("JSON input must be an object.")
    fields = data.get("fields", data)
    if not isinstance(fields, dict):
        raise ValueError("JSON input 'fields' must be an object.")
    return {str(key): "" if value is None else str(value) for key, value in fields.items()}


def append_evidence(
    evidence_path: Path,
    instrument_id: str,
    field_values: dict[str, str],
    metadata: dict[str, str],
) -> int:
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    existing_header, existing_rows = read_csv(evidence_path)
    header = existing_header or EVIDENCE_FIELDS
    now = dt.datetime.now().isoformat(timespec="seconds")

    rows = existing_rows
    existing_keys = {
        (row.get("instrument_id", ""), row.get("field_name", ""))
        for row in rows
    }
    new_count = 0
    for field, value in field_values.items():
        if field in ROW_METADATA_FIELDS or not value.strip():
            continue
        entry = {
            "instrument_id": instrument_id,
            "field_name": field,
            "field_value": value,
            "source_url": metadata.get("source_url", ""),
            "source_title": metadata.get("source_title", ""),
            "evidence_quote": metadata.get("evidence_quote", ""),
            "confidence_score": metadata.get("confidence_score", ""),
            "needs_human_review": metadata.get("needs_human_review", "true"),
            "review_note": metadata.get("review_note", ""),
            "updated_at": now,
        }
        key = (instrument_id, field)
        if key in existing_keys:
            for index, row in enumerate(rows):
                if (row.get("instrument_id", ""), row.get("field_name", "")) == key:
                    rows[index] = {**row, **entry}
                    break
        else:
            rows.append(entry)
            existing_keys.add(key)
        new_count += 1

    write_csv(evidence_path, header, rows)
    return new_count


def command_templates(_: argparse.Namespace) -> int:
    templates = load_templates()
    for template in sorted(templates):
        try:
            cn_columns = get_template_columns(template, "cn", templates)
            cn_count = str(len(cn_columns))
        except Exception as exc:  # noqa: BLE001 - show template health without aborting
            cn_count = f"mismatch ({exc})"
        print(f"{template}: {len(templates[template])} EN columns / {cn_count} CN columns")
    return 0


def command_init(args: argparse.Namespace) -> int:
    templates = load_templates()
    template = resolve_template(args.template, templates)
    output = args.output or default_dataset_path(template, args.lang, args.outputs_dir)
    fieldnames = get_template_columns(template, args.lang, templates)
    if output.exists() and not args.force:
        print(f"Dataset already exists: {output}")
        return 0
    write_csv(output, fieldnames, [])
    print(f"Initialized {template} dataset: {output}")
    return 0


def command_add(args: argparse.Namespace) -> int:
    templates = load_templates()
    template = resolve_template(args.template, templates)
    output = args.output or default_dataset_path(template, args.lang, args.outputs_dir)
    expected_header = get_template_columns(template, args.lang, templates)
    aliases = build_field_aliases(template, args.lang, templates)

    header, rows = read_csv(output)
    fieldnames = expected_header
    if header:
        rows = coerce_rows_to_fieldnames(rows, fieldnames, aliases)

    values = dict(args.set or [])
    if args.from_json:
        values.update(load_json_values(args.from_json))

    metadata = {
        "source_url": args.source_url or values.pop("source_url", ""),
        "source_title": args.source_title or values.pop("source_title", ""),
        "evidence_quote": args.evidence_quote or values.pop("evidence_quote", ""),
        "confidence_score": args.confidence_score or values.pop("confidence_score", ""),
        "needs_human_review": str(args.needs_human_review).lower(),
        "review_note": args.review_note or values.pop("review_note", ""),
    }
    if args.no_human_review:
        metadata["needs_human_review"] = "false"

    canonical_values = localise_values(canonicalise_fields(values, fieldnames, aliases), args.lang)

    status_value = canonical_values.get("Status", "")
    if status_value.strip():
        status_error = validate_status(status_value, args.lang)
        if status_error:
            print(f"Error: {status_error}", file=sys.stderr)
            return 1

    target_index = None
    for index, row in enumerate(rows):
        if get_row_value(row, ["Policy Instrument ID"], aliases) == args.id:
            target_index = index
            break

    if target_index is None:
        row = {field: "" for field in fieldnames}
        rows.append(row)
        target_index = len(rows) - 1
    else:
        if not args.force:
            dom_name = get_row_value(rows[target_index], ["Domestic instrument name", "本国工具名称"], aliases)
            filled = sum(1 for v in rows[target_index].values() if v.strip() and v.strip() != "N/A")
            print(
                f"Error: instrument {args.id} already exists ({dom_name}, {filled} fields filled). "
                f"Use --force to overwrite.",
                file=sys.stderr,
            )
            return 1
        row = {field: rows[target_index].get(field, "") for field in fieldnames}

    apply_defaults(row, args.id, canonical_values, aliases, args.lang)
    if not args.allow_blank_cells:
        fill_empty_template_cells(row, fieldnames, aliases)
    rows[target_index] = row
    write_csv(output, fieldnames, rows)

    evidence_count = append_evidence(args.evidence_log, args.id, canonical_values, metadata)
    issues = draft_issues(row, aliases)

    print(f"Saved instrument row: {args.id}")
    print(f"Dataset: {output}")
    print(f"Evidence entries updated: {evidence_count}")
    parsed_id = parse_policy_id(args.id)
    if parsed_id:
        country_code, group_code, approach_code = expected_id_codes(
            get_row_value(row, ["Country"], aliases),
            get_row_value(row, ["Group"], aliases),
            get_row_value(row, ["Approach"], aliases),
        )
        id_warnings = []
        if country_code and parsed_id["country"] != country_code:
            id_warnings.append(f"country code {parsed_id['country']} != expected {country_code}")
        if group_code and parsed_id["group"] != group_code:
            id_warnings.append(f"group code {parsed_id['group']} != expected {group_code}")
        if approach_code and parsed_id["approach"] != approach_code:
            id_warnings.append(f"approach code {parsed_id['approach']} != expected {approach_code}")
        if id_warnings:
            print("Policy ID warnings:")
            for warning in id_warnings:
                print(f"- {warning}")
    else:
        print("Policy ID warning: ID does not match {ISO3}{group}{approach}I##S### pattern.")
    if issues:
        print("Draft issues still needing data:")
        for issue in issues:
            print(f"- {issue}")
        return 2 if args.strict else 0
    print("Draft-entry required fields are complete.")
    return 0


def command_id(args: argparse.Namespace) -> int:
    print(
        generate_policy_id(
            args.country,
            args.group,
            args.approach,
            args.instrument_sequence,
            args.subscheme_sequence,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    templates = subparsers.add_parser("templates", help="List available dataset templates.")
    templates.set_defaults(func=command_templates)

    init = subparsers.add_parser("init", help="Initialize an empty dataset CSV.")
    init.add_argument("--template", required=True, help="Template/category name or alias.")
    init.add_argument("--lang", choices=["cn", "en"], default="cn")
    init.add_argument("--outputs-dir", type=Path, default=DEFAULT_OUTPUTS_DIR)
    init.add_argument("--output", type=Path)
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=command_init)

    add = subparsers.add_parser("add", help="Append or update one instrument draft row.")
    add.add_argument("--template", required=True, help="Template/category name or alias.")
    add.add_argument("--id", required=True, help="Policy Instrument ID.")
    add.add_argument("--lang", choices=["cn", "en"], default="cn")
    add.add_argument("--outputs-dir", type=Path, default=DEFAULT_OUTPUTS_DIR)
    add.add_argument("--output", type=Path)
    add.add_argument("--evidence-log", type=Path, default=DEFAULT_EVIDENCE_LOG)
    add.add_argument("--set", action="append", type=parse_key_value, default=[], metavar="FIELD=VALUE")
    add.add_argument("--from-json", type=Path, help="JSON object, or object with a 'fields' object.")
    add.add_argument("--source-url")
    add.add_argument("--source-title")
    add.add_argument("--evidence-quote")
    add.add_argument("--confidence-score")
    add.add_argument("--needs-human-review", default="true")
    add.add_argument("--no-human-review", action="store_true")
    add.add_argument("--review-note", default="")
    add.add_argument("--strict", action="store_true", help="Return non-zero when draft fields are incomplete.")
    add.add_argument("--allow-blank-cells", action="store_true", help="Allow blank template cells in the output row.")
    add.add_argument("--force", action="store_true", help="Allow overwriting an existing instrument row.")
    add.set_defaults(func=command_add)

    id_parser = subparsers.add_parser("id", help="Generate a policy instrument ID from schema codes.")
    id_parser.add_argument("--country", required=True, help="Country code or country name, e.g. CHN.")
    id_parser.add_argument("--group", required=True, help="IFCMA group/type.")
    id_parser.add_argument("--approach", required=True, help="IFCMA approach.")
    id_parser.add_argument("--instrument-sequence", type=int, required=True, help="Two-digit instrument sequence as an integer.")
    id_parser.add_argument("--subscheme-sequence", type=int, default=0, help="Three-digit subscheme sequence as an integer.")
    id_parser.set_defaults(func=command_id)

    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:  # noqa: BLE001 - CLI should show clear one-line failures
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
