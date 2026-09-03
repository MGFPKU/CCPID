#!/usr/bin/env python3
"""Insert English ROW_TRANSLATIONS entries for 3 new PV GB standards."""

from __future__ import annotations

from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "generate_english_from_chinese.py"

with open(SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# ── PRFMEAI29 ─────────────────────────────────────────────────────────

PRFMEAI29 = """

    "CHNPRFMEAI29S000": {
        "Approach": "Minimum Energy Performance Standards (MEPS) for electric appliances",
        "Emission sector": "Industry",
        "Sub-sector": "Solar photovoltaic",
        "English instrument name": (
            "Minimum Allowable Values of Energy Efficiency and Energy Efficiency "
            "Grades for Crystalline Silicon Photovoltaic Modules and Inverters"
        ),
        "Description": (
            "GB 47834-2026 Minimum Allowable Values of Energy Efficiency and Energy "
            "Efficiency Grades for Crystalline Silicon Photovoltaic Modules and "
            "Inverters is a mandatory national standard, published on 27 June 2026 "
            "and effective 1 January 2027. This is the first mandatory national "
            "standard to include PV modules in energy efficiency assessment. It "
            "applies to ground-mounted n-type crystalline silicon PV modules "
            "(including TOPCon, HJT and BC technology routes) and PV grid-connected "
            "inverters (centralised, string and integrated pre-assembled PV inverter "
            "unit types). It does not apply to BIPV modules, consumer PV modules, "
            "perovskite/crystalline silicon tandem modules, silver-free electrode "
            "modules, grid-forming PV grid-connected inverters, inverters of 20 kW "
            "and below, or string inverters above 500 kW. Energy efficiency grades "
            "are classified into three levels (Grade 1 highest), with Grade 3 as "
            "the minimum allowable value i.e. the mandatory market access "
            "threshold. Together with GB 47835-2026 and GB 29447-2026, this "
            "standard forms the mandatory energy consumption and energy efficiency "
            "standards framework for the PV industry."
        ),
        "Objective": (
            "Improve PV module and inverter energy efficiency; "
            "Eliminate low-efficiency production capacity"
        ),
        "Administrating authorities": (
            "State Administration for Market Regulation; "
            "Standardization Administration of China"
        ),
        "Asset": "Crystalline silicon photovoltaic modules and PV grid-connected inverters",
        "Asset (Status)": "new",
        "Asset (Details)": (
            "Ground-mounted n-type crystalline silicon PV modules (TOPCon, HJT "
            "and BC technology routes), based on a standard module dimension of "
            "1 134 mm x 2 382 mm; PV grid-connected inverters (centralised, "
            "string, and integrated pre-assembled PV inverter unit types). Does "
            "not apply to BIPV modules, consumer PV modules, perovskite/crystalline "
            "silicon tandem modules, modules using silver-free metal paste or "
            "silver-free processes for cell electrodes, grid-forming PV "
            "grid-connected inverters, inverters of 20 kW and below, or string "
            "inverters above 500 kW."
        ),
        "Agent": "Firms",
        "Agent (Detail)": (
            "Manufacturers and importers producing, importing or selling "
            "crystalline silicon PV modules and PV grid-connected inverters "
            "within China."
        ),
        "Activity": "Production; Sale; Import",
        "Activity (Details)": (
            "Production, import and sale of crystalline silicon PV modules and "
            "PV grid-connected inverters. Products must meet the standard's "
            "minimum allowable energy efficiency values before they can enter "
            "the market. PV projects using non-compliant modules cannot be "
            "registered and will not pass grid connection acceptance."
        ),
        "Intensity (Value)": "Grade 3",
        "Intensity (Unit)": "Energy efficiency grade",
        "Intensity (Details)": (
            "Energy efficiency grades are classified into three levels (Grade 1 "
            "highest), with Grade 3 as the minimum allowable value i.e. the "
            "mandatory market access threshold. Module efficiency is evaluated "
            "by photoelectric conversion efficiency (percentage): TOPCon Grade 3 "
            ">= 23.2% (630 W), Grade 2 >= 23.7% (645 W), Grade 1 >= 24.0% (650 W); "
            "HJT Grade 3 >= 23.2% (630 W), Grade 2 >= 23.5% (635 W), Grade 1 >= "
            "23.8% (645 W); BC Grade 3 >= 23.5% (635 W), Grade 2 >= 23.9% (650 W), "
            "Grade 1 >= 24.2% (655 W). Module power ratings are based on a standard "
            "dimension of 1 134 mm x 2 382 mm. Inverters are evaluated by weighted "
            "average efficiency, with limits set by equipment type and rated power."
        ),
        "Requirement specification": (
            "1) Crystalline silicon PV modules and PV grid-connected inverters "
            "must meet the standard's minimum allowable energy efficiency values "
            "(Grade 3) before they may be produced, imported or sold; 2) Products "
            "must display an energy efficiency grade label; 3) Energy efficiency "
            "grades are classified into Grade 1 (highest), Grade 2 and Grade 3, "
            "with Grade 3 as the mandatory market access threshold; 4) PV projects "
            "using non-compliant modules cannot be registered and will not pass "
            "grid connection acceptance."
        ),
        "Compliance monitoring": "Government inspections",
        "Compliance monitoring details": (
            "Market regulation authorities conduct energy efficiency label "
            "supervision inspections and product quality spot checks for "
            "crystalline silicon PV module and PV grid-connected inverter "
            "products. Inspections cover accuracy of energy efficiency grade "
            "labelling, whether actual product energy efficiency matches "
            "labelled grades, and compliance with mandatory minimum energy "
            "efficiency values."
        ),
        "Compliance enforcement": "Compliance orders; Fines",
        "Compliance enforcement details": (
            "For production, import or sale of crystalline silicon PV modules "
            "and inverters that do not meet mandatory energy efficiency standards, "
            "market regulation authorities order cessation of production, import "
            "or sale, confiscate illegal gains and impose fines. In serious cases, "
            "business licences may be revoked. PV projects using non-compliant "
            "modules cannot be registered and will not pass grid connection "
            "acceptance."
        ),
        "Compliance promotion": "Other incentives or support",
        "Compliance promotion detail": (
            "The state encourages the production and use of Grade 1 and Grade 2 "
            "high-efficiency PV modules and inverters, and promotes the "
            "high-efficiency PV product market through energy-saving product "
            "certification and government green procurement. Firms are encouraged "
            "to benchmark against Grade 1 energy efficiency and undertake "
            "technology upgrades."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": (
            "PV product energy efficiency improvement; "
            "PV generation cost reduction; "
            "Green industry development"
        ),
        "Legal statute": (
            "GB 47834-2026 Minimum Allowable Values of Energy Efficiency and "
            "Energy Efficiency Grades for Crystalline Silicon Photovoltaic "
            "Modules and Inverters"
        ),
        "Other relevant websites": "N/A",
        "Last revision (Details)": "N/A",
    },
"""

# ── PRFEILI68 ─────────────────────────────────────────────────────────

PRFEILI68 = """
    "CHNPRFEILI68S000": {
        "Approach": "Energy intensity limit for industrial production",
        "Emission sector": "Industry",
        "Sub-sector": "Solar photovoltaic",
        "English instrument name": "Norm of Energy Consumption per Unit Products of Polysilicon and Germanium",
        "Description": (
            "GB 29447-2026 Norm of Energy Consumption per Unit Products of Polysilicon "
            "and Germanium is a mandatory national standard, published on 27 June 2026 "
            "and effective 1 January 2027, replacing GB 29447-2022 Norm of Energy "
            "Consumption per Unit Products of Polysilicon and Germanium. This standard "
            "sets differentiated energy intensity limits by production process for the "
            "first time, with three energy consumption grades for the trichlorosilane "
            "method (rod silicon) and the silane fluidised bed method (granular silicon) "
            "respectively. Compared with the previous edition, the Grade 3 energy "
            "consumption value for rod silicon has been reduced by nearly 40%. "
            "The standard applies to enterprises producing solar-grade polysilicon "
            "via the trichlorosilane method or silane fluidised bed method, and to "
            "enterprises producing high-purity germanium tetrachloride, high-purity "
            "germanium dioxide, zone-refined germanium ingots and germanium single "
            "crystals from germanium concentrates or recycled germanium materials. "
            "It does not apply to electronic-grade or float-zone grade polysilicon. "
            "Together with GB 47834-2026 and GB 47835-2026, this standard forms the "
            "mandatory energy consumption and energy efficiency standards framework "
            "for the PV industry."
        ),
        "Objective": (
            "Improve energy efficiency; Reduce energy consumption; "
            "Eliminate backward production capacity"
        ),
        "Mitigation relevance": "Direct",
        "Administrating authorities": (
            "State Administration for Market Regulation; "
            "Standardization Administration of China"
        ),
        "Asset": "Polysilicon and germanium production facilities",
        "Asset (Status)": "new; existing",
        "Asset (Details)": (
            "Facilities producing solar-grade polysilicon via the trichlorosilane "
            "method (rod silicon) or silane fluidised bed method (granular silicon), "
            "and facilities producing high-purity germanium tetrachloride, high-purity "
            "germanium dioxide, zone-refined germanium ingots and germanium single "
            "crystals from germanium concentrates or recycled germanium materials. "
            "Does not apply to facilities producing electronic-grade or float-zone "
            "grade polysilicon."
        ),
        "Agent": "Firms",
        "Agent (Detail)": (
            "Enterprises operating polysilicon (solar-grade) or germanium product "
            "production facilities within China."
        ),
        "Activity": "Production",
        "Activity (Details)": (
            "Operation of polysilicon and germanium product production facilities. "
            "Existing firms must meet Grade 3 limit values to continue operating; "
            "non-compliant firms are subject to remediation within a prescribed "
            "period or mandatory retirement. New, expansion and renovation projects "
            "must meet Grade 2 access values before commencing production."
        ),
        "Intensity (Value)": "Grade 3",
        "Intensity (Unit)": "Energy intensity limit grade",
        "Intensity (Details)": (
            "Energy intensity limit grades are classified into three levels "
            "(Grade 1 highest). Grade 3 is the limit value (minimum requirement "
            "for existing firms), Grade 2 is the access value (minimum requirement "
            "for new, expansion and renovation projects), and Grade 1 is the "
            "advanced value. The evaluation indicator is comprehensive energy "
            "consumption per unit product (kgce/kg): trichlorosilane method "
            "(rod silicon) Grade 1 <= 5.0, Grade 2 <= 5.5, Grade 3 <= 6.3; "
            "silane fluidised bed method (granular silicon) Grade 1 <= 3.6, "
            "Grade 2 <= 4.0, Grade 3 <= 4.6."
        ),
        "Requirement specification": (
            "1) Existing polysilicon and germanium producers must meet Grade 3 "
            "limit values to continue operating; non-compliant firms shall "
            "remediate within a prescribed period or face mandatory retirement; "
            "2) New, expansion and renovation projects must meet Grade 2 access "
            "values before commencing production; 3) Grade 1 advanced values "
            "serve as benchmarks for firm self-comparison and industry energy "
            "efficiency leader selection."
        ),
        "Compliance monitoring": "Government inspections; Firm energy consumption data reporting",
        "Compliance monitoring details": (
            "Market regulation authorities conduct supervision inspections of "
            "energy intensity limit compliance by polysilicon and germanium "
            "producers. Firms must report energy consumption data as required "
            "and are subject to energy conservation supervision and energy audits."
        ),
        "Compliance enforcement": (
            "Compliance orders; Fines; Differential electricity pricing; "
            "Mandatory retirement"
        ),
        "Compliance enforcement details": (
            "For polysilicon and germanium producers that do not meet mandatory "
            "energy intensity limit standards, relevant authorities order "
            "remediation within a prescribed period. Firms that fail to comply "
            "after the remediation period may be subject to differential "
            "electricity pricing or mandatory retirement in accordance with the law."
        ),
        "Compliance promotion": "Other incentives or support",
        "Compliance promotion detail": (
            "The state encourages polysilicon and germanium producers to benchmark "
            "against Grade 1 advanced values and undertake energy conservation "
            "and carbon reduction retrofits, supporting uptake of advanced "
            "energy-saving technologies through energy conservation retrofit "
            "rewards and green factory designation."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": (
            "Industrial energy efficiency improvement; "
            "Industrial energy consumption reduction; "
            "PV supply chain emission reduction"
        ),
        "Legal statute": (
            "GB 29447-2026 Norm of Energy Consumption per Unit Products "
            "of Polysilicon and Germanium"
        ),
        "Other relevant websites": "N/A",
        "Last revision (Details)": (
            "First issued on 31 December 2012 as GB 29447-2012 Norm of Energy "
            "Consumption per Unit Products of Polysilicon Enterprise, effective "
            "1 October 2013. First revised in 2022 (GB 29447-2022), renamed "
            "Polysilicon and Germanium with scope extended to germanium products. "
            "Second revision on 27 June 2026 (GB 29447-2026), renamed Silicon "
            "Polysilicon and Germanium, introducing differentiated energy intensity "
            "limits for the trichlorosilane and silane fluidised bed methods for "
            "the first time, reducing the rod silicon Grade 3 energy intensity "
            "indicator by nearly 40% from the previous edition, and adding "
            "granular silicon from the silane fluidised bed process plus detailed "
            "definitions of energy consumption statistical scope for major "
            "process steps."
        ),
    },
"""

# ── PRFEILI69 ─────────────────────────────────────────────────────────

PRFEILI69 = """
    "CHNPRFEILI69S000": {
        "Approach": "Energy intensity limit for industrial production",
        "Emission sector": "Industry",
        "Sub-sector": "Solar photovoltaic",
        "English instrument name": "Norm of Energy Consumption per Unit Products of Monocrystalline Silicon",
        "Description": (
            "GB 47835-2026 Norm of Energy Consumption per Unit Products of "
            "Monocrystalline Silicon is a mandatory national standard, published "
            "on 27 June 2026 and effective 1 January 2027, issued for the first "
            "time. It applies to enterprises producing monocrystalline silicon "
            "square ingots and wafers for solar cells using the Czochralski method, "
            "and is used for the calculation and assessment of energy consumption "
            "as well as energy consumption control for new, expansion and renovation "
            "projects. Energy intensity limit grades are classified into three levels "
            "(Grade 1 highest). Grade 3 is the limit value (minimum requirement for "
            "existing firms), Grade 2 is the access value (minimum requirement for "
            "new, expansion and renovation projects), and Grade 1 is the advanced "
            "value. Together with GB 47834-2026 and GB 29447-2026, this standard "
            "forms the mandatory energy consumption and energy efficiency standards "
            "framework for the PV industry, setting a mandatory energy intensity "
            "limit for the monocrystalline silicon segment for the first time."
        ),
        "Objective": "Improve energy efficiency; Reduce energy consumption",
        "Administrating authorities": (
            "State Administration for Market Regulation; "
            "Standardization Administration of China"
        ),
        "Asset": "Monocrystalline silicon production facilities",
        "Asset (Status)": "new; existing",
        "Asset (Details)": (
            "Czochralski crystal pullers and ancillary equipment for producing "
            "monocrystalline silicon square ingots for solar cells, and wafering "
            "equipment (sawing, grinding, polishing) for processing square ingots "
            "into monocrystalline silicon wafers. Does not apply to semiconductor-grade "
            "monocrystalline silicon production facilities."
        ),
        "Agent": "Firms",
        "Agent (Detail)": (
            "Enterprises operating monocrystalline silicon (solar-grade) ingot "
            "pulling and wafer slicing production facilities within China."
        ),
        "Activity": "Production",
        "Activity (Details)": (
            "Production operations for monocrystalline silicon square ingot "
            "pulling and wafer processing. Existing firms must meet Grade 3 "
            "limit values to continue operating; non-compliant firms are subject "
            "to remediation within a prescribed period or mandatory retirement. "
            "New, expansion and renovation projects must meet Grade 2 access "
            "values before commencing production."
        ),
        "Intensity (Value)": "Grade 3",
        "Intensity (Unit)": "Energy intensity limit grade",
        "Intensity (Details)": (
            "Energy intensity limit grades are classified into three levels "
            "(Grade 1 highest). Grade 3 is the limit value (minimum requirement "
            "for existing firms), Grade 2 is the access value (minimum requirement "
            "for new, expansion and renovation projects), and Grade 1 is the "
            "advanced value. The evaluation indicator is comprehensive energy "
            "consumption per unit product: monocrystalline silicon square ingot "
            "(crystal pulling) Grade 1 <= 2.10 kgce/kg, Grade 2 <= 2.30 kgce/kg, "
            "Grade 3 <= 2.58 kgce/kg; monocrystalline silicon wafer (wafer slicing) "
            "Grade 1 <= 7,800 kgce/million pieces, Grade 2 <= 8,600 kgce/million "
            "pieces, Grade 3 <= 9,525 kgce/million pieces."
        ),
        "Requirement specification": (
            "1) Existing monocrystalline silicon producers must meet Grade 3 "
            "limit values to continue operating; non-compliant firms shall "
            "remediate within a prescribed period or face mandatory retirement; "
            "2) New, expansion and renovation projects must meet Grade 2 access "
            "values before commencing production; 3) Grade 1 advanced values "
            "serve as benchmarks for firm self-comparison and industry energy "
            "efficiency leader selection."
        ),
        "Compliance monitoring": "Government inspections; Firm energy consumption data reporting",
        "Compliance monitoring details": (
            "Market regulation authorities conduct supervision inspections of "
            "energy intensity limit compliance by monocrystalline silicon producers. "
            "Firms must report energy consumption data as required and are subject "
            "to energy conservation supervision and energy audits."
        ),
        "Compliance enforcement": (
            "Compliance orders; Fines; Differential electricity pricing; "
            "Mandatory retirement"
        ),
        "Compliance enforcement details": (
            "For monocrystalline silicon producers that do not meet mandatory "
            "energy intensity limit standards, relevant authorities order "
            "remediation within a prescribed period. Firms that fail to comply "
            "after the remediation period may be subject to differential "
            "electricity pricing or mandatory retirement in accordance with the law."
        ),
        "Compliance promotion": "Other incentives or support",
        "Compliance promotion detail": (
            "The state encourages monocrystalline silicon producers to benchmark "
            "against Grade 1 advanced values and undertake energy conservation "
            "and carbon reduction retrofits, supporting uptake of advanced "
            "energy-saving technologies through energy conservation retrofit "
            "rewards and green factory designation."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": (
            "Industrial energy efficiency improvement; "
            "Industrial energy consumption reduction; "
            "PV supply chain emission reduction"
        ),
        "Legal statute": (
            "GB 47835-2026 Norm of Energy Consumption per Unit Products "
            "of Monocrystalline Silicon"
        ),
        "Other relevant websites": "N/A",
        "Last revision (Details)": "N/A",
    },
"""

# ── Apply insertions ──────────────────────────────────────────────────

# 1. PRFMEAI29: after PRFMEAI28 closing, before PRFMELI01
# 1. PRFMEAI29: after PRFMEAI28 closing, before PRFMELI01
# Variable has 2 leading \n, so prefix needs 3 more for 5 total blank lines
old1 = '    },\n\n\n\n\n\n    "CHNPRFMELI01S000": {'
assert old1 in content, "PRFMEAI29 insertion point not found!"
content = content.replace(old1, '    },\n\n\n' + PRFMEAI29 + '\n\n\n\n\n    "CHNPRFMELI01S000": {', 1)

# 2. PRFEILI68 + PRFEILI69: after PRFEILI67 closing, before PRFEILI01
old2 = '    },\n\n\n\n\n\n    "CHNPRFEILI01S000": {'
assert old2 in content, "PRFEILI68/69 insertion point not found!"
content = content.replace(old2, '    },\n\n\n' + PRFEILI68 + PRFEILI69 + '\n\n\n\n\n    "CHNPRFEILI01S000": {', 1)

with open(SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print("Inserted PRFMEAI29, PRFEILI68, PRFEILI69 into generate_english_from_chinese.py")
