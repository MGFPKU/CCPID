# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

China Climate Policy Instrument Database (CCPID) — a bilingual (Chinese/English) national-level climate mitigation policy instrument database aligned with the OECD IFCMA Climate Policy Database. The unit of observation is the policy instrument (or subscheme), not the broader policy package.

- `inputs/` — Source templates, classification definitions, approach definitions, methodology docs, attribute definitions, and the IFCMA paper
- `rules/schema.yaml` — Authoritative schema: templates, columns, allowed values, validation rules, controlled lists, and ID code maps
- `scripts/` — Python CLI tools (standard library only, except `openpyxl` for Excel export)
- `outputs/` — CSV working files, Excel deliverables, and evidence log
- `review/` — Inclusion/exclusion decisions, issues for human review, and governance decisions
- `logs/` — Validation reports

## Classification Hierarchy

Category → Group → Approach → Instrument → Sub-scheme (optional)

Five templates/categories: `Economic instruments`, `Regulatory instruments`, `Government I&C`, `Information instruments`, `Voluntary approaches`. Each has distinct columns defined in `rules/schema.yaml`.

## Instrument ID Format

`{ISO3 country}{group code}{approach code}I{2-digit instrument seq}S{3-digit subscheme seq}` — e.g., `CHNTRAETSI01S000`

Group and approach codes are defined in `rules/schema.yaml` under `known_codes`. Instrument rows use `S000`; subschemes use `S001`, `S002`, etc.

## Core Workflow (per instrument)

1. Make inclusion decision → record in `review/inclusion_exclusion_decisions.md`
2. Fill Chinese draft first using `scripts/fill_instrument.py add`
3. Chinese draft goes through human review and validation
4. After Chinese is confirmed, generate English version with `scripts/generate_english_from_chinese.py`
5. Run `scripts/validate_dataset.py` and review `logs/validation_report.md`
6. Export Excel deliverables with `scripts/export_workbooks.py`

**Ended instruments**: when an included instrument expires or is terminated, move its full row from the category CSV into `outputs/CCPID_{lang}_{category}_ended.csv`. The export pipeline appends these rows to the workbook's `Ended` / `已终止` sheet automatically, below the curated historical rows kept in the template.

## Key Commands

All scripts are run from the repo root with `python scripts/<name>.py`.

**List available templates:**
```powershell
python scripts\fill_instrument.py templates
```

**Initialize an empty dataset:**
```powershell
python scripts\fill_instrument.py init --template "Economic instruments" --lang cn
```

**Generate a new instrument ID from the schema code map:**
```powershell
python scripts\fill_instrument.py id --country CHN --group "Trading scheme" --approach "Emissions trading system" --instrument-sequence 1
```

**Add or update one instrument row:**
```powershell
python scripts\fill_instrument.py add `
  --template "Economic instruments" `
  --id CHNTRAETSI01S000 `
  --set "Instrument / subscheme=Instrument" `
  --set "Group=Trading scheme" `
  --set "Approach=Emissions trading system" `
  --set "Domestic name=..." `
  --set "Country=CHN" `
  --source-url "https://..." --source-title "..." --evidence-quote "..." --confidence-score 0.8
```

**Run the full export + validate pipeline (preferred after any CSV edit):**
```powershell
python scripts\run_pipeline.py
```

**Run pipeline with URL health check:**
```powershell
python scripts\run_pipeline.py --check-urls
```

**Validate outputs (standalone):**
```powershell
python scripts\validate_dataset.py --outputs-dir outputs --report logs\validation_report.md
```

**Validate with URL reachability check:**
```powershell
python scripts\validate_dataset.py --outputs-dir outputs --report logs\validation_report.md --check-urls
```

**Export Excel workbooks (standalone):**
```powershell
python scripts\export_workbooks.py --lang all
```

**Normalize ISIC codes before export/validation:**
```powershell
python scripts\normalize_isic_economic_sector.py
```

**Generate official source search queries (when a source is from a non-canonical URL):**
```powershell
python scripts\suggest_official_source_queries.py "<document title>" --url "<candidate URL>" --document-number "<document number if known>"
```

## Script Dependency Chain

DO NOT run multiple filling scripts that write `outputs/evidence_log.csv` in parallel — they must run sequentially. After filling, always run `run_pipeline.py` (or CN normalizer → ISIC normalizer → export workbooks → validate). Always regenerate both xlsx files after any CSV edit.

## English Translation Safety Mechanisms

`scripts/generate_english_from_chinese.py` has three safeguards against incomplete/missing translations:

1. **Structural field CN→EN auto-translation** — `_STRUCTURAL_TRANSLATIONS` maps known Chinese structural values (Group, Status, Country, Jurisdiction level, Instrument/subscheme, Mitigation relevance, Functioning channel) to their English equivalents. These are applied automatically and never need to be in ROW_TRANSLATIONS entries.

2. **Domestic instrument name passthrough** — `Domestic instrument name` is passed through from the CN CSV automatically (it is CJK-exempt). No ROW_TRANSLATIONS entry needs to include it.

3. **Completeness check** — After generating the EN CSV, `_check_completeness()` verifies every row has non-empty values for critical fields (Instrument/subscheme, Group, Approach, Emission sector, Domestic instrument name, English instrument name, Country, Jurisdiction level, Status). Missing fields are printed as warnings and the script exits non-zero.

4. **Merge-based ROW_TRANSLATIONS** — `existing_english` is always applied as a base; `ROW_TRANSLATIONS` only overrides specific fields. A ROW_TRANSLATIONS entry never needs to duplicate every field — only fields that differ from the existing English row need to be specified.

## Key Coding Rules

- **Evidence for every field**: source_url, source_title, evidence_quote, confidence_score, and review_flag in `outputs/evidence_log.csv`
- **No invention**: use `not found` (CN: `未找到`) when evidence is insufficient; set `needs_human_review=true`
- **N/A vs blank**: Use `N/A` both for structurally non-applicable fields and for true unknowns (where data is not found or not published). Chinese CSVs also use `N/A` (the pipeline auto-normalizes legacy `未指明` → `N/A`). Blank only during draft entry.
- **Chinese first**: always fill the Chinese version first, generate English after human review confirms
- **Instrument row unit**: treat the policy instrument (not the policy package) as the row unit
- **Official sources**: prefer primary legislation or official Chinese government sources
- **Subscheme splitting**: split when rates, thresholds, covered assets, agents, exemptions, or phases differ (especially `New` vs `existing` assets)
- **Group/Approach are dependent**: approach must be valid for the selected group (mapping in `rules/schema.yaml`)
- **Economic sector**: use ISIC Rev.4 division codes (e.g., `D35` for electricity, `C24` for basic metals). Run the ISIC normalizer after edits.
- **Market operation data**: search operational disclosures before marking trading fields as `not found` — use the source ladder: official regulator stats → platform operator data → credible non-official sources
- **Data source attribution for quantitative fields**: when instrument-specific fields (annual revenue, annual revenue forgone, annual budget/expenditure, limit, cap, free allowance, revenue, volume) or GHG baseline fields (emission coverage absolute/% of domestic) contain concrete numeric data, include the data source inline after the value (CN: `来源：{source}`; EN: `Source: {source}`)
- **Instrument-specific fields**: leave tax-specific fields blank for trading-scheme rows, subsidy fields blank for tax rows, etc. The fill script handles this automatically via `INSTRUMENT_SPECIFIC_FIELD_PREFIXES`.
- **Parent/subcheme alignment**: parent rows must have aggregate values covering all current subschemes
- **Date format**: `dd/mm/yyyy` throughout
- **Date convention — 通过日期/生效日期**: use the earliest predecessor's date, not the current version. The earliest standard/regulation that first established the instrument. Example: if GB 16780-2021 replaced GB 16780-2012 which replaced GB 16780-2007, use the GB 16780-2007 dates (03/12/2007, 01/06/2008).
- **Date convention — 最近修订**: the CURRENT version's date for instruments that have been revised/replaced. For first-time instruments with no predecessor, 最近修订 and 最近修订（详情） must both be `N/A` — there is no prior version to have been revised from.
- **Mitigation co-benefits**: use only generalized phrases, never specific industry names or equipment/product types. CN vocabulary: 能效提升, 能源消耗减少, 空气污染物减排, 技术创新, 绿色产业发展, 能源安全, 污染防治, 生态保护, 资源节约, 循环经济, 可再生能源发展, 水资源节约, 公众健康. EN: Energy efficiency improvement, Energy consumption reduction, Air pollutant emission reduction, Technological innovation, Green industry development, Energy security, Pollution control, Ecological protection, Resource conservation, Circular economy, Renewable energy development, Water resource conservation, Public health.
- **Activity (受规制活动)**: select from schema `allowed_values` in `rules/schema.yaml`. The "or" in options like "Disposal, collection or sorting after use" means pick the applicable term(s) — do NOT write all terms. E.g. write `收集或分类（消费后）` not `回收、收集或分类（消费后）` when "回收" belongs to Schema #9 "Recycling, repurposing or other treatment after use".
- **Excel formatting**: parent instrument rows bold, subscheme rows not bold
