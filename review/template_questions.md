# Template Governance Decisions

These decisions resolve the initial template questions and should be applied before policy data entry. The schema implementation is in `rules/schema.yaml`.

## Required Fields

1. Enforce a small draft-entry core: `Policy Instrument ID`, `Instrument / subscheme`, `Group`, `Approach`, `Country`, `Jurisdiction level`, and `Status`.
2. For final publication, also require source coverage: `Legal statute` when known and at least one source URL from `Legal document` or `Other relevant websites`.
3. If the legal statute name is unavailable, enter `Not specified` in `Legal statute` and provide an official `Legal document` URL.
4. Require at least one policy name. For China records, prefer `Domestic name`; `English name` may be translated later.

## Header Normalization

1. Treat `Domestic instrument name` as an alias of canonical `Domestic name`.
2. Treat `English instrument name` as an alias of canonical `English name`.
3. Use `Last revision` as canonical; treat `Last revisions` as an alias.
4. Use `Mitigation effect` as canonical; treat `Mitigation effects` as an alias.
5. Use `Other relevant websites` as canonical; treat `Other weblinks` as an alias.

## Controlled Values

1. Validation is case-insensitive for controlled values, but export should use canonical display values from the schema.
2. `Objective` options are non-exhaustive. Prefer a concise objective explicitly stated in the policy text over `Other`; use `Other` only when no clearer source-stated objective can be coded.
3. Treat `No compliance monitoring Random` as a source error. Use separate values: `No compliance monitoring` or `Random`.
4. Regulated `Asset` and `Activity` lists are non-exhaustive. Allow custom values only when the paired details/other field explains the value.
5. Validate `Group` and `Approach` as dependent pairs.

## Field Semantics

1. `End date` means the date when the final legal requirement of the mandate takes effect. It is not necessarily policy expiry.
2. Add `Intensity (Year)` to the schema because it appears in the attribute definitions, even though it is not visible in every template sheet.
3. For formulas, ranges, thresholds, and tiered rates: put the simplest comparable scalar in `Intensity (Value)` when possible, the measurement unit in `Intensity (Unit)`, and the full formula/table/range in `Intensity (Details)`.
4. Split rows into subschemes when `New` and `existing` assets have different legal requirements. A single row may cover both only when the same requirement applies.
5. For national policies with subnational implementation variation, keep `Jurisdiction level = national` and capture variation in details or subschemes.

## Instrument-Specific Sections

1. Keep all template columns during export. Use `N/A` for structurally non-applicable instrument-specific fields, `Not specified` for true unknowns, and blank only during draft entry.
2. `Tax and Tax Incentive: annual revenue forgone` applies to tax incentives and tax exemptions that reduce liability.
3. `Trading System: Linkages` should prefer IFCMA policy instrument IDs. External market names are acceptable while IDs are not assigned.
4. Regulatory `Compliance promotion` should use the same controlled list as information instruments: `No compliance promotion`, `Information and direct assistance`, `Financial support`, and `Other incentives or support`.
5. Split public investment and public procurement into separate rows when they are legally or operationally distinct. One Government I&C row may contain both when the same instrument genuinely includes both.

## Source and Evidence Rules

1. Final-publication records should rely on primary legislation or official government sources.
2. Secondary sources are acceptable only as temporary support when primary sources are inaccessible during drafting.
3. Multiple URLs in one source cell must be separated with semicolons.
4. Every non-empty factual field should be traceable to `Legal statute`, `Legal document`, `Other relevant websites`, or another source note before final publication.

## Monitor During Data Entry

1. Check whether the strict `Group` and `Approach` dependency map needs additional voluntary-approach entries.
2. Check whether `End date` needs a separate future companion field for legal expiry or repeal date.
3. Check whether recurring complex tier tables need a separate structured table instead of repeated use of `Intensity (Details)`.
