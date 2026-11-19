# Classification Revision Recommendations — Decision Record

Date: 2026-11-17
Source document: `CCPID_Approach_Instrument_Classification_Revision_Recommendations_20261117.docx` (external reviewer, 26 recommendations)
Basis for each verdict: IFCMA paper (`inputs/methodology/IFCMA paper.pdf`), `rules/schema.yaml`, `inputs/classification/approaches_en.md` / `approaches_cn.md`, current CN/EN data, and (for items marked "verified") primary legal sources.

Summary of verdicts: **adopt 17** (#1, 2, 3, 6, 7, 9, 10, 13, 15, 16, 17, 19, 20, 22, 24, 25, 26), **partially adopt 9** (#4, 5, 8, 11, 12, 14, 18, 21, 23), **reject 0**.

---

## P1 — Classification reassignment and instrument-unit fixes (implemented first)

### #1 CCER → Trading scheme / Offset credits — ADOPT

- Current: CHNVTSVCMI01S000 + 18 subschemes (S001–S018), Voluntary approaches / Voluntary trading system / Voluntary carbon market.
- Verdict: IFCMA's Offset credits definition ("government-issued tradable credits usable for compliance with legal obligations"; explicitly excludes "voluntary emission trading systems") matches the CCER exactly. Move all 19 rows to Economic instruments / Trading scheme / new approach **Offset credits (OFC)**. IDs become CHNTRAOFCI01S000–S018.
- Note: VTS group becomes empty; the Voluntary carbon market approach definition stays in the classification tables for comparability.

### #2 Construction-project EIA → Regulatory / Framework regulation — ADOPT

- Current: CHNPAREIAI01S000, Government I&C / Public appraisal rules / Environmental impact assessment.
- Verdict: EIA obligations bind project developers, not the government's own decision processes; IFCMA Framework standards explicitly include "environmental permitting process". Move to Regulatory / Framework regulation, approach name unchanged. ID → CHNFRMEIAI01S000.

### #3 Energy-and-carbon review for investment projects → Regulatory / Framework regulation — ADOPT

- Current: CHNPARECRI01S000, Government I&C / Public appraisal rules / Energy and carbon review for investment projects.
- Verdict: same logic as #2; the review obligation binds the project investor. Move to Regulatory / Framework regulation, approach name unchanged. ID → CHNFRMECRI01S000.

### #4 Cleaner production audit → Reporting requirements — PARTIAL ADOPT (verified)

- Current: CHNPARECAI01S000, Government I&C / Public appraisal rules / Environmental compliance audit.
- Verification (Cleaner Production Promotion Law, 2012 revision): the penalty-bearing obligations are audit + report to government + public disclosure (art. 27(2)(4), art. 39 penalties attach only to the audit–report–publish chain). Remediation of over-standard firms runs through environmental law (art. 27(3) cross-reference), which CCPID already records separately.
- Verdict: move to Information / Reporting requirements under a renamed approach **Environmental auditing requirements (EAR)** — no split. The approach row in the classification tables is renamed from Environmental compliance audit (ECA) to Environmental auditing requirements (EAR) with an updated definition; the description notes the cross-reference to environmental-law remediation. ID → CHNREPEARI01S000.

### #5 Public-institution energy performance framework → Government I&C / Public appraisal rules — PARTIAL ADOPT

- Current: CHNFRMEPMI01S000, Regulatory / Framework regulation / Energy performance management framework for public institutions.
- Verdict: the regulated entities are government units; IFCMA Public appraisal rules cover "decision-making processes and operations of the government". Re-classify to Public appraisal rules (approach name unchanged), do **not** split into new rows — set the Policy Package field to link the existing public-institution energy statistics/audit (CHNREPESAI01S000) and green public procurement (CHNPPCGPPI*) rows. ID → CHNPAREPMI01S000.

### #6 Duplicate carbon-peak assessment rows — ADOPT (merge)

- Verified: CHNFRMTRSI03S000 (碳达峰碳中和综合评价考核制度, FRM/TRS) and CHNPARCPAI01S000 (碳达峰碳中和综合评价考核办法, PAR/CPA) are the same document (12/04/2026, "5+9" indicator system; gov.cn notice page vs gazette text).
- Verdict: merge into one row under Government I&C / Public appraisal rules / Climate performance assessment and evaluation (keep CHNPARCPAI01S000; delete CHNFRMTRSI03S000), carrying over any richer field values from the deleted row.

### #7 Electric-motor MEPS → Performance standard — ADOPT

- Current: CHNTECMEMI01–03S000, Regulatory / Technology standard / MEPS for electric motors.
- Verdict: IFCMA Performance standards mandate outcomes ("minimum energy performance standards for electric equipment"); Technology standards require/prohibit inputs or technologies. Efficiency limits mandate outcomes. Move 3 rows to Performance standard (approach name unchanged). IDs → CHNPRFMEMI01–03S000.

### #8 County EV charging pilot → Public investment — ADOPT (verified)

- Current: CHNSUBTDRI02S000, Economic instruments / Subsidy / Technology deployment reward.
- Verification (财建〔2024〕57号 + provincial transfer notices + county tender records): funds flow central → provincial → county fiscal transfers (recorded as 1100250 节能环保共同财政事权转移支付收入); spending forms public fixed capital (charging infrastructure, grid upgrades, monitoring platforms) built by county SOEs through public tender; funds explicitly may not be used for vehicle purchase/operation subsidies.
- Verdict: government spending forming public fixed capital = Public investment, not a subsidy to non-government units. Move to Government I&C / Public investment / Central budget investment (same mechanism family as the four existing CBI rows). ID → CHNPIVCBII06S000.

### #9 Green factory programme → Voluntary approaches — ADOPT

- Current: CHNCBACBPI01S000, Information / Capacity building and public awareness / Capacity building programme.
- Verdict: voluntary application, graded evaluation, list recognition, reputational incentives — not a government training/capacity programme. Move to Voluntary approaches / Voluntary information instrument / new approach **Voluntary benchmarking and recognition schemes (VBR)** (shared with #16). ID → CHNVIIVBRI01S000.

### #10 Multi-user green power direct connection → new FRM approach — ADOPT

- Current: CHNFRMRPDI02S000, Regulatory / Framework regulation / Renewable priority dispatch.
- Verdict: direct-connection and market-participation rules match IFCMA Framework standards ("market structure rules, grid operation"); distinct from priority-dispatch. New approach **Green power direct connection rules (GPC)** under Framework regulation; narrow the RPD definition accordingly. ID → CHNFRMGPCI01S000.

### #11 Minimum renewable consumption share → split power / non-power — PARTIAL ADOPT

- Current: CHNTRARECI03S000 (重点用能行业可再生能源消费最低比重目标), Trading scheme / REC.
- Verified: the power part (self-consumption, GEC trading, surplus-consumption transfers) and the non-power part (renewable heating/cooling, green hydrogen/ammonia, biomass fuels) have different compliance mechanisms.
- Verdict: split into **two instruments** (not subschemes). Power part stays Trading scheme / REC with a new ID CHNTRARECI04S000. Non-power part moves to Regulatory / Performance standard / new approach **Non-electric renewable energy consumption obligations (RCP)**. ID → CHNPRFRCPI01S000.

### #12 GB 55015 comprehensive building energy code — PARTIAL ADOPT

- Current: CHNPRFMEBI01S000 (建筑节能与可再生能源利用通用规范), Performance standard / MEPS for buildings.
- Verdict: the code is a comprehensive mandatory code (envelope, equipment, renewable application), mis-fitting a single MEPS category. Near-term: re-classify to Framework regulation / new approach **Comprehensive building energy code (CBC)** and state the comprehensive nature in the description. Full clause-level splitting deferred as long-term improvement. ID → CHNFRMCBCI01S000.

---

## P2 — Approach boundaries and definitions

### #13 VPS vs trade-in definition overlap — ADOPT

- VPS definition currently includes "as well as scrappage schemes", overlapping TIS. Remove that phrase from VPS. Add new CCPID-specific approach **Vehicle scrappage subsidy** for scrappage-only programmes. Split CHNSUBVPSI01S000 (old operating truck subsidy: scrap-only / scrap-and-replace / cold-chain-only purchase arms) into subschemes accordingly.

### #14 Split the four CLG mechanisms — PARTIAL ADOPT (verified)

- Verified against primary sources:
  - a) CHNSUBCLGI03S000 设备更新贷款财政贴息 → new approach **Interest subsidy (ITS)** under Subsidy. ADOPT.
  - b) CHNSUBCLGI01S000 MLF green collateral expansion → new CCPID-specific approach **Central bank lending support (CBL)** under Subsidy (marked non-IFCMA-typical; crosswalk annotation in #25). ADOPT.
  - c) CHNSUBCLGI02S000 碳减排支持工具 stays under CLG. ADOPT.
  - d) CHNSUBCLGI04S000 CDM Fund: grants go to provincial-or-above government agencies and the remunerated-use arm is capital-preserving investment (Order 111, arts. 13–20) — neither arm is an "unrequited payment to non-government units". REJECT the split-into-four-instruments proposal (one 办法 authorises all modes; splitting violates the instrument-unit principle). Instead move the whole fund to Government I&C / Public investment / Government investment fund as CHNPIVGIFI02S000, sibling of the National Green Development Fund (CHNPIVGIFI01S000); record the four fund-use modes in the description (optionally as subschemes).

### #15 Narrow Eco-compensation — ADOPT (definition level)

- Horizontal/vertical fiscal transfers are not IFCMA subsidies ("unrequited payments from government to non-government units"). Narrow the Eco-compensation approach definition to the framework/governance instrument; specific payment mechanisms are filed separately as ESP/Trading instruments linked via Policy Package. No row moves.

### #16 Top-Runner vs certification labels — ADOPT

- 水效领跑者 (CHNVIIVLBI03S000) and 能效、碳效领跑者 (CHNVIIVLBI04S000) are benchmarking + public recognition, not certification-and-label granting. Move both to the new VBR approach (IDs → CHNVIIVBRI02S000, CHNVIIVBRI03S000). 节能低碳产品认证 (VLB01) and 绿色建筑标识 (VLB02) stay in VLB.

### #17 Rename Professional certification — ADOPT

- The definition describes occupational standards (occupational definition, skill grades, training hours, assessment criteria), not certification. Rename approach to **Occupational standards and skills development** (code OSS). 1 data row + definition + code entries. ID → CHNCBAOSSI01S000.

### #18 Green standard system as single information tool — PARTIAL ADOPT (low priority)

- The Information / CBA / GSS classification is defensible (the guideline is an information document; definition already states guiding/non-mandatory nature). Adopt the filing principle (specific standards inside the system are filed separately by their own legal force) as a note; no row moves.

### #19 Peak-shaving capacity commitment → new Voluntary approach — ADOPT (verified)

- Verified (发改能源〔2021〕1093号): voluntary participation beyond guaranteed grid-connection scale, commitment-to-grid-access mechanism (企业承诺、政府备案、过程核查、假一罚二), 15%/20% linkage ratios. The "commitment" is a condition for extra grid access, not an IFCMA self-set performance target.
- Verdict: new CCPID-specific approach **Voluntary capacity provision and grid-connection commitments (VCP)** under Voluntary approaches (kept in the Voluntary target group for now, with the difference from self-set targets noted in the definition). ID: CHNVTGVCPI01S000. CHNVTGVTGI01S000 (appliance-recycling target responsibility) stays as the VTG archetype.

### #20 Narrow EIL to binding limit values — ADOPT

- EIL definition currently includes "may set benchmark levels for best practice". Narrow to legally binding limit/access values; advanced/leading values are reference information recorded in Details. No row moves (68 rows are limit-based).

### #21 MEA name too narrow — PARTIAL ADOPT

- 30 rows include transformers, servers, industrial pumps, compressors, electrolysers, chargers, PV modules. Adopt the rename to **MEPS for electric equipment** (matching IFCMA's "electric equipment" wording), code MEE. IDs CHNPRFMEAI01–30S000 → CHNPRFMEEI01–30S000. Splitting into per-equipment-type approaches deferred as optional long-term improvement.

### #22 MHS rename — ADOPT

- 1 row (CHNPRFMHSI01S000); the standard covers heat pumps and water chillers. Rename approach to **MEPS for heat pumps and water chillers** (code HPC). ID → CHNPRFHPCI01S000.

### #23 Administered prices + narrow CPM — PARTIAL ADOPT

- Narrow the CPM definition to administratively-set capacity compensation prices (remove auctioned capacity markets and reliability options — market mechanisms that do not belong under administered pricing). Group-name pluralisation is implemented with #24. Also fix the schema internal inconsistency "Residential increasing-block pricing" → "Residential increasing-block tariff".

---

## P3 — Name unification and maintenance rules

### #24 Unify Category/Group names and pluralisation — ADOPT

- Confirmed: Approaches table uses short category names; Categories and groups table has the "Public procuremet" typo; singular/plural inconsistent across workbook/schema/CSV (Public appraisal rule(s), Reporting requirement(s), Trading scheme(s), Administered price(s)).
- Verdict: apply the document's unified naming table in one synchronised pass across schema allowed_values + known_codes + fill scripts + 5 CN/5 EN CSVs + Excel + webpage labels. Group codes are unchanged, so instrument IDs are unaffected.

### #25 IFCMA crosswalk column in the Approaches table — ADOPT

- Add per-approach metadata: crosswalk status (Direct match / Extended / CCPID-specific) + IFCMA reference approach. Pure additive metadata serving the international-comparability goal; required for the new CCPID-specific approaches (#8-related, #14b, #19, #13, #1).

### #26 Codify mixed-mechanism handling rules — ADOPT

- Rules 1–3 already match schema (subscheme_splitting, instrument_specific_row_splitting) and CLAUDE.md principles — write them into the methodology docs. Rules 4–5 are genuinely new and directly support the #1/#2/#3/#5 verdicts:
  - Rule 4: whether the regulated entity is the government decides the Government I&C vs Regulatory category, not the policy's formal addressee.
  - Rule 5: voluntary participation ≠ Voluntary approaches; the binding test is the operating mechanism and legal obligation, not the name or the participation modality.

---

## Implementation order

1. P1 (#1–#12): schema.yaml known_codes + allowed_values + Group_Approach_dependencies; approaches_en.md/cn.md new approaches (OFC, EAR, VBR, GPC, RCP, CBC); CN+EN CSV row moves with ID changes; evidence_log updates; generate_english_from_chinese.py ROW_TRANSLATIONS key renames + _STRUCTURAL_TRANSLATIONS additions; validate_dataset.py VALUE_ALIASES additions; export_workbooks.py OVERVIEW_ROW_HEIGHTS key updates. Run pipeline after the batch.
2. P2 (#13–#23): definition edits and further splits/renames (ITS, CBL, VCP, OSS, MEE, HPC); CLG04 → CHNPIVGIFI02S000; VLB03/04 → VBR; VPS01 subschemes. Run pipeline after the batch.
3. P3 (#24–#26): unified naming pass; crosswalk columns; methodology rule codification. Run pipeline after the batch.

Each batch ends with `python scripts/run_pipeline.py` and a review of `logs/validation_report.md`.
