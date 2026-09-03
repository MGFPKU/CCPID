# Data Filling Workflow

This workflow is for filling CCPID instruments one by one from user-provided instrument names and official source evidence.

## Operating Rules

1. Fill the Chinese draft first.
2. Before filling any requested instrument, make an inclusion decision. If the item should not be included as a CCPID instrument, stop data filling and tell the user the exclusion reason. If it should be included, record the rationale and proceed directly with data filling.
3. Treat the policy instrument, not the policy package, as the row unit.
4. Use official Chinese government sources wherever possible.
5. Do not invent values. Use `not found` for unsupported fields and set `needs_human_review=true`.
6. Record evidence for every filled field in `outputs/evidence_log.csv`.
7. Fill every generally applicable template cell before validation. Use `N/A` for structurally non-applicable fields and `not found` for relevant fields where evidence was searched but not found.
8. Leave instrument-specific attribute blocks for other instrument groups blank. For example, an ETS/trading-scheme row should leave tax- and subsidy-specific fields blank.
9. Keep draft rows in CSV until the instrument has passed human review and validation.
10. Chinese outputs must use headers from `inputs/template_cn.xlsx`; English canonical headers are allowed only as script input aliases, not as `CCPID_cn_*` output columns.
11. Keep source, confidence, and review metadata in `outputs/evidence_log.csv`, not as extra columns in the template dataset.
12. Output dataset cells should contain data values, not filling instructions, search notes, or unresolved caveats.
12. When a specific quantitative data value is filled, include a compact source label in the output cell, e.g. `189百万吨（2024；来源：生态环境部2025报告）`. Keep full URL, source title, quote, confidence score, and review note in `outputs/evidence_log.csv`.
13. In Chinese outputs, use `未找到` instead of English `not found`.
14. When a specific data value is filled, record the exact data source in `outputs/evidence_log.csv` with source URL/title, evidence quote, confidence score, and review flag/note.
15. After every substantive correction, update this workflow, validation, or scripts when the correction reveals a reusable rule. Do not leave recurring fixes as one-off row edits.
16. `Last revisions` should refer to the latest formal policy, statute, notice, implementation plan, or allocation plan that amends or operationalises the instrument. Do not use progress reports, analytical reports, or market updates as the latest revision date.
17. `Legal document` should contain exactly one primary legal or formal instrument URL. Put supporting sources, official reports, data disclosures, and secondary references in `Other weblinks`.
17a. Before accepting an official-looking but non-canonical page, especially consultation/public-comment portals such as `yyglxxbsgw.ndrc.gov.cn`, run `python scripts\suggest_official_source_queries.py "<exact document title>" --url "<candidate URL>" --document-number "<document number if known>"` and search the generated official-domain queries. Prefer final formal ministry notice pages such as `ndrc.gov.cn/xwdt/tzgg/...`, `ndrc.gov.cn/xxgk/zcfb/...`, `nea.gov.cn`, or `gov.cn` over consultation systems, reposts, or broad policy pages.
18. For subscheme rows, use the subscheme-specific formal legal document or implementation document when available. Use the parent legal framework only when no subscheme-specific formal source exists.
19. For ETS intensity fields, do not code the one-for-one allowance surrender obligation as an `Intensity (Value)`. If a market carbon price is available, fill the price as the intensity value and state the exact date or period, price definition, and source in `Intensity (Details)`. If no price source is available, set value/unit to `N/A` and explain that the carbon price is market-determined.
20. Check industry-specific GHG scope instead of assuming CO2 only. For China's national ETS expansion, aluminum smelting can include PFCs such as CF4 and C2F6.
21. Excel deliverables should visually distinguish parent instruments from subschemes: instrument rows are bold; subscheme rows are not bold.
22. For subscheme GHG coverage fields, do not stop at `not found` after checking only legal texts. Search official disclosures first, then credible non-official datasets, news, academic estimates, or transparent calculations. If only an estimate can be produced, fill it as an estimate and include the year, data sources, and calculation basis in the cell and evidence log.
23. Chinese and English outputs are mirrored language versions of the same records. Validation checks for duplicate instrument IDs and parent/subscheme aggregation should run within each output file/language, not across CN and EN files combined.
24. Instrument IDs must encode the selected classification, not a generic market acronym. Use `{ISO3}{group code}{approach code}I{instrument sequence}S{subscheme sequence}`. For current China trading-scheme rows, `TRA` is the group code, `ETS` is `Emissions trading system`, `REC` is `Tradable renewable electricity credits, quota or tradable performance standards`, and `TPS` is `Tradable performance standards`. For example, China's green certificate market is `CHNTRARECI01S000`, parsed as `CHN` + `TRA` + `REC` + `I01` + `S000`, while the passenger-vehicle dual-credit policy is coded under `TPS`.
24a. Generate new instrument IDs from the shared code map in `rules/schema.yaml` instead of inventing abbreviations inline. Use `python scripts\fill_instrument.py id --country CHN --group "<Group>" --approach "<Approach>" --instrument-sequence <n>` before filling the row. The validator and fill scripts read the same `known_codes` map, so any new approach code must be added there first and should be transparent (e.g. `CLG` = concessional loans / loan guarantees / credit support).
25. For trading schemes and other market instruments, do not mark market-operation fields as `not found` after checking only legal texts. Search operational data sources first: official statistics, ministry/newsletter/press-release pages, official platform announcements, market operator releases, and then credible non-official reports or news.
26. Chinese approach definitions in `inputs/classification/approaches_cn.md` must be content-equivalent translations of `inputs/classification/approaches_en.md`, not shortened summaries. Keep the Chinese path name aligned with values used in `CCPID_cn_*` data so the `路径汇总` sheet can resolve category, group, path, and definition.

27. `Objective` should capture the policy objective(s) explicitly stated in the legal or formal policy text. The controlled list is non-exhaustive: use a concise source-stated objective such as `Renewable energy development and consumption` when it is more accurate than `Other`. Do not default to `Climate change mitigation` based only on inferred mitigation relevance; keep that inference in `Mitigation relevance` and mitigation-effect fields.
28. For credit-support instruments such as concessional loans, loan guarantees, relending facilities, collateral eligibility, and fiscal interest subsidies, code `Asset` as the direct financial asset or instrument affected by the policy (e.g. eligible loans, guarantees, collateral, bonds). Do not list underlying projects, equipment, technologies, or sectors as `Asset`; capture those in `Asset (Details)`, `Asset (Cut-off range)`, `Sub-sector`, or `Activity (Details)`.
29. For renewable electricity mechanisms that settle the difference between a market transaction average price and an administratively or competitively determined mechanism/strike price, classify the approach as `Renewable electricity contract for difference` (`ECD`). Code `Asset` as the electricity/renewable energy being settled, such as electricity, solar energy, wind energy, or other renewable energies; describe project cohorts, mechanism electricity volumes, and market-entry rules in `Asset (Details)` and `Asset (Cut-off range)`.
30. When adding a new approach, update the schema ID code map, allowed approach dependencies, English and Chinese classification definition tables, abbreviation tables, validator aliases, and workbook export aliases together. Keep the approach sequence consistent across these files; for subsidy approaches, `Renewable electricity contract for difference` (`ECD`) follows `Concessional loans, loan guarantees and credit support` (`CLG`).
31. For a national framework policy with provincial implementation documents, official provincial policy links may be added to `Other weblinks` as implementation examples. If the provincial policy changes substantive parameters such as mechanism volumes, prices, eligibility, auction rules, or settlement responsibilities, create a provincial subscheme/row or add a human-review issue rather than treating the link as merely background.
32. `Economic sector` must use ISIC Rev.4 division codes in the format section letter plus two digits, such as `D35`, `C29`, `G45`, or `K64`. Do not use Chinese GB/T industry codes, free-text sector names, or section-only letters. For multiple regulated sectors, separate ISIC division codes with semicolons. Common mappings used in China rows: electricity supply/generation `D35`; basic metals including steel and aluminium `C24`; cement/non-metallic mineral products `C23`; motor vehicle manufacturing `C29`; motor vehicle trade `G45`; financial service activities `K64`.
33. Before exporting workbooks or validating after historical edits, run `python scripts\normalize_isic_economic_sector.py` to normalize legacy economic-sector values in working CSVs and `outputs/evidence_log.csv` (e.g. `D44 -> D35`, `C31/C32 -> C24`, `C30 -> C23`, `C36 -> C29`, `G56 -> G45`).
34. Do not run multiple filling scripts that write `outputs/evidence_log.csv` in parallel. Run them sequentially, then run the ISIC normalizer, export workbooks, and validate. Parallel writes can corrupt the evidence CSV.

## Coding Notes

- Functioning channel: use `供给侧` / `Supply-side` when the instrument directly changes producer or regulated-firm behaviour. Use `需求侧` / `demand-side` when it directly changes consumer behaviour. Use `环境` / `environment` only for enabling conditions that let supply- or demand-side measures operate.
- For mandatory ETS instruments covering emitting firms, code functioning channel as `供给侧` unless the specific instrument is only an enabling market infrastructure rule.
- Market operation fields such as `交易系统：交易量` and `交易系统：年收入` usually do not come from legal texts. They are annual-data fields: use annual volume/revenue or annual transaction value only. Do not substitute first-day figures or cumulative figures unless the field is explicitly redefined for that scope. Fill them from data disclosure sources: first official disclosures from MEE, the national carbon trading institution / Shanghai Environment and Energy Exchange, State Council briefings, or official annual reports; then credible secondary sources if official data is unavailable. Clearly distinguish secondary-market transaction value from paid-allocation or auction revenue.
- Mitigation co-benefits must be checked against the attribute definition and controlled values. First use co-benefits explicitly stated in the policy/legal text or official explanation. If the text does not state a co-benefit but the policy mechanism strongly implies one, infer cautiously, record the reasoning in evidence/review notes, and use a lower confidence score. Do not default to `未找到` if the source text or a well-supported mechanism indicates a non-mitigation positive outcome such as air-pollution co-control, energy security, technological innovation, employment, or industrial development.
- ETS sector coverage should be treated as included once an official MEE/government source says the sector's key emitters have been brought into the national ETS. Do not leave those sectors as pending/preparatory in output or review notes. When multiple currently covered sectors have distinct scope, allocation, or compliance details, model them as subscheme rows under the parent ETS instrument.
- Parent instrument rows must align with their subscheme rows. Fields such as emission sector, sub-sector, regulated asset/activity, economic sector, GHG coverage, and source links should use an aggregate or parent-level value that covers all current subschemes, not only the first or most familiar subscheme.
- Market operation source ladder: for `Trading System: Volume`, `Trading System: revenue (annual)`, and market-price-based `Intensity`, search annual/period operational data in this order before using `not found`: official regulator statistics, newsletters, press releases, policy briefings, and Q&A pages; official market operator/platform announcements, dashboards, annual reports, and trading bulletins; official industry association or system-operator reports when they publish delegated market data; credible non-official sources such as ICAP, IEA, OECD, exchange-recognized reports, specialist market data providers, or reputable financial/energy news.
- Market operation coding: distinguish annual trading volume from cumulative trading volume; total transaction value from average price; standalone certificate trades from green-power-bundled certificate trades; and secondary-market transaction value from paid-allocation or auction revenue. If only volume plus price by vintage/category is available, do not calculate total annual transaction value unless the matching volume split is also disclosed. When a value is still unavailable, write a precise `not found` statement naming the searched data and closest available official disclosure.
- Compliance calculation fields should use the latest formal operative document when it changes or clarifies assessment mechanics, not only the original framework notice. For renewable electricity credit/quota/RPS instruments, distinguish: provincial or aggregate responsibility-weight accounting, market-entity allocation/reporting, and any green-electricity consumption-share accounting. Do not collapse physical renewable electricity consumption, purchased out-of-province GECs, and GEC-based green-consumption-share assessment into one undifferentiated formula.

## Per-Instrument Steps

1. Identify the requested item and collect enough source context to decide whether it is a CCPID policy instrument.
2. Make and record an inclusion decision in `review/inclusion_exclusion_decisions.md`:
   - Include when the item is a specific legal, regulatory, fiscal, information, voluntary, or public-investment measure that can be represented as an instrument or subscheme row.
   - Exclude when the item is only a policy goal, strategy, target, analytical report, market update, institution, broad package without a row-level instrument, duplicate of an existing row, or outside CCPID scope.
3. If excluded, stop and report the reason to the user. If included, continue without asking for another confirmation.
4. Identify the instrument boundary: instrument vs. package vs. subscheme.
5. Choose the template/category: `Economic instruments`, `Regulatory instruments`, `Government I&C`, `Information instruments`, or `Voluntary approaches`.
6. Fill the draft core fields:
   `Policy Instrument ID`, `Instrument / subscheme`, `Group`, `Approach`, one policy name, `Country`, `Jurisdiction level`, and `Status`.
7. Before committing the ID, check that its country, group, approach, and `S000`/subscheme suffix match the row classification and boundary.
8. Verify the legal/source links before filling attributes. Search by exact document title, document number, issuing agency, and key phrases; test official ministry/agency URL variants and any user-provided official URLs. Use `scripts\suggest_official_source_queries.py` to generate official-domain searches when a source is found through a consultation portal, repost, search result snippet, or user-provided non-canonical URL. Use the most instrument-specific official legal or formal implementation page in `Legal document`; use broad reposts only when no direct official page can be verified.
9. For market instruments, run the market-operation source ladder before filling `Trading System` fields or market-price `Intensity`: search official regulator pages with the instrument name plus terms such as `交易量`, `成交额`, `交易规模`, `价格`, `均价`, `运行情况`, `新闻稿`, `发布会`, `newsletter`, `press release`, and the latest year.
10. Fill source-backed attributes from the official text and operational disclosures.
11. If a trading field remains unavailable, write a precise `not found` statement naming the data searched and the closest available official data, and set the evidence-log review note accordingly.
12. Run the data-filling script to append or update the draft row and evidence log.
13. Run `scripts/validate_dataset.py` and review `logs/validation_report.md`.
14. Add unresolved questions to `review/issues_for_human_review.md`.

## Commands

List templates:

```powershell
python scripts\fill_instrument.py templates
```

Initialize a Chinese draft dataset:

```powershell
python scripts\fill_instrument.py init --template "Regulatory instruments" --lang cn
```

Add or update one instrument:

```powershell
python scripts\fill_instrument.py add `
  --template "Regulatory instruments" `
  --id CHNREGFUEL01S000 `
  --set "Instrument / subscheme=Instrument" `
  --set "Group=Performance standard" `
  --set "Approach=Fuel economy standard" `
  --set "Domestic instrument name=..." `
  --set "Country=CHN" `
  --set "Jurisdiction level=national" `
  --set "Status=in force" `
  --source-url "https://..." `
  --source-title "..." `
  --evidence-quote "..." `
  --confidence-score 0.8
```

Generate an instrument ID from the canonical group/approach code map:

```powershell
python scripts\fill_instrument.py id `
  --country CHN `
  --group "Subsidy" `
  --approach "Concessional loans, loan guarantees and credit support" `
  --instrument-sequence 1
```

Validate current outputs:

```powershell
python scripts\validate_dataset.py --outputs-dir outputs --report logs\validation_report.md
```

When a row uses an approved recurring secondary source for data fields, add it as an extra accepted suffix rather than replacing the default official-domain checks:

```powershell
python scripts\validate_dataset.py --outputs-dir outputs --report logs\validation_report.md --official-domain-suffix icapcarbonaction.com
```

Export reviewable Excel outputs:

```powershell
python scripts\export_workbooks.py --lang all
```

## Output Files

- `outputs/CCPID_cn_<template>.csv`: Chinese draft rows.
- `outputs/CCPID_en_<template>.csv`: English rows after Chinese review.
- `outputs/CCPID_cn.xlsx`: Chinese template workbook exported from CSV working files.
- `outputs/CCPID_en.xlsx`: English template workbook exported after English rows exist.
- `outputs/evidence_log.csv`: field-level evidence metadata.
- `outputs/evidence_log.xlsx`: Excel evidence log for review.
- `logs/validation_report.md`: automated validation result.
- `review/issues_for_human_review.md`: unresolved manual review items.
