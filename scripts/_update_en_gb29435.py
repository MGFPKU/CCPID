#!/usr/bin/env python3
"""Update EN ROW_TRANSLATIONS for CHNPRFEILI63S000 to reflect GB 29435-2025 revision."""

from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "generate_english_from_chinese.py"

with open(SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# Find the exact boundaries of the CHNPRFEILI63S000 entry
start = content.index('\n    "CHNPRFEILI63S000": {')
end = content.index('\n\n\n\n\n\n    "CHNPRFEILI64S000": {', start)

old_entry = content[start:end]

# Build the updated entry
new_entry = """
    "CHNPRFEILI63S000": {


        "Policy Instrument ID": "CHNPRFEILI63S000",


        "Instrument / subscheme": "Instrument",


        "Group": "Performance standard",


        "Approach": "Energy intensity limit for industrial production",


        "Emission sector": "Industry",


        "Sub-sector": "Rare earth smelting",


        "English instrument name": (
            "Norm of Energy Consumption per Unit Production of Rare Earth "
            "Metallurgical Enterprise"
        ),


        "Policy Package": "N/A",


        "Description": (


            "GB 29435-2025 Norm of Energy Consumption per Unit Production of Rare Earth "
            "Metallurgical Enterprise is a mandatory national standard, published on 31 December "
            "2025 and effective 1 January 2027, replacing GB 29435-2012 Norm of Energy Consumption "
            "per Unit Production of Rare Earth Smelting and Processing Enterprises. It applies to "
            "enterprises producing single rare earth compounds (lanthanum oxide, cerium oxide, "
            "praseodymium oxide, neodymium oxide, praseodymium-neodymium oxide, etc.) through "
            "hydrometallurgical processes (leaching, decomposition, solvent extraction separation, "
            "precipitation, calcination, etc.) and rare earth metals and alloys (lanthanum metal, "
            "cerium metal, praseodymium metal, neodymium metal, Pr-Nd alloy, etc.) through "
            "pyrometallurgical processes (molten salt electrolysis, metallothermic reduction, etc.) "
            "using rare earth concentrates and mixed rare earth compounds as raw materials, as "
            "well as enterprises producing rare earth compounds via NdFeB waste integrated "
            "recovery processes. Compared with the 2012 edition, key changes include: deletion of "
            "rare earth tri-band phosphors and polishing powders from scope; addition of rare earth "
            "compound products from NdFeB waste integrated recovery processes; reclassification of "
            "rare earth compounds into 4 categories and rare earth metals and alloys into 2 "
            "categories; revision of energy intensity limit values at each grade; and revision of "
            "statistical scope and calculation methods. Energy intensity limits are classified into "
            "three grades (Grade 1 highest, i.e. most advanced), with Grade 3 as the minimum "
            "limit (mandatory for existing firms), Grade 2 as the access limit (mandatory for new, "
            "expansion and renovation projects), and Grade 1 as the advanced value."


        ),


        "Objective": "Improve energy efficiency; Reduce energy consumption",


        "Mitigation relevance": "Direct",


        "Functioning channel": "Supply-side",


        "Country": "CHN",


        "Jurisdiction level": "National",


        "Jurisdiction name": "N/A",


        "Adoption date": "31/12/2012",


        "Start date": "01/10/2013",


        "End date": "N/A",


        "Last revisions": "31/12/2025",


        "Status": "In force",


        "Administrating authorities": (


            "State Administration for Market Regulation; "
            "Standardization Administration of China"
        ),


        "Asset": "Rare earth metallurgical production installation",


        "Asset (Status)": "New; existing",


        "Asset (Details)": (


            "Installations producing single rare earth compounds (lanthanum oxide, cerium oxide, "
            "praseodymium oxide, neodymium oxide, praseodymium-neodymium oxide, samarium oxide, "
            "etc.) from rare earth concentrates (bastnaesite, monazite, ion-adsorption rare earth "
            "ore, etc.) and mixed rare earth compounds through hydrometallurgical processes "
            "(including acid decomposition, alkali decomposition, solvent extraction separation, "
            "precipitation and calcination); producing rare earth metals and alloys (lanthanum "
            "metal, cerium metal, praseodymium metal, neodymium metal, Pr-Nd alloy, etc.) "
            "through pyrometallurgical processes (including molten salt electrolysis and "
            "metallothermic reduction); and installations producing rare earth compounds via "
            "NdFeB waste integrated recovery processes. The 2025 edition deletes rare earth "
            "tri-band phosphors and polishing powders, classifies rare earth compounds into 4 "
            "categories and rare earth metals and alloys into 2 categories with separate "
            "limit values for each."


        ),


        "Asset (Other)": "N/A",


        "Asset (Cut-off range)": "N/A",


        "Agent": "Firms",


        "Agent (Detail)": (
            "Enterprises operating rare earth metallurgical production installations within China."
        ),


        "Activity": "Production",


        "Activity (Details)": (


            "Operational activities of rare earth metallurgical production installations. "
            "Existing firms must meet Grade 3 (minimum) intensity limits to continue "
            "operating; non-compliant firms must undergo retrofits or be phased out within "
            "a prescribed period. New, expansion and renovation projects must meet Grade 2 "
            "(access) intensity limits before commencing production."


        ),


        "Intensity (Value)": "3 grades",


        "Intensity (Unit)": "Energy intensity limit grade",


        "Intensity (Details)": (


            "Energy intensity limits are classified into three grades (Grade 1 highest, "
            "i.e. most advanced), with Grade 3 as the minimum limit (mandatory for existing "
            "firms), Grade 2 as the access limit (mandatory for new, expansion and renovation "
            "projects), and Grade 1 as the advanced value. Limits are set by product type and "
            "process route, measured in kgce of comprehensive energy per tonne (kgce/t). The "
            "2025 edition classifies rare earth compounds into 4 categories and rare earth "
            "metals and alloys into 2 categories, each with differentiated intensity limit "
            "values. Limits are managed at three levels: Grade 1 (advanced value), Grade 2 "
            "(access value) and Grade 3 (minimum value)."


        ),


        "Requirement specification": (


            "1) Existing rare earth metallurgical firms must meet Grade 3 (minimum) "
            "intensity limits to continue operating; non-compliant firms must undergo "
            "retrofits or be phased out within a prescribed period. 2) New, expansion "
            "and renovation projects must meet Grade 2 (access) intensity limits before "
            "commencing production. 3) Grade 1 advanced values serve as energy efficiency "
            "benchmarks for firms and industry energy efficiency leader selection."


        ),


        "Compliance calculation methodology I": "N/A",


        "Compliance calculation methodology II": "N/A",


        "Compliance monitoring": (


            "Inspections or audits conducted by government authorities or third parties; Energy consumption "
            "data reporting by firms"
        ),


        "Compliance monitoring details": (


            "Market regulatory authorities conduct supervision inspections on rare earth "
            "metallurgical firms' compliance with energy intensity limit standards; firms "
            "must submit energy consumption data as required and undergo energy "
            "conservation supervision and energy auditing."


        ),


        "Compliance enforcement": "Compliance order; Fines; Differentiated electricity pricing; Phase-out and closure",


        "Compliance enforcement details": (


            "For rare earth metallurgical firms that do not meet the mandatory energy "
            "intensity limit standard, relevant authorities shall order rectification "
            "within a prescribed period; those failing to complete rectification or "
            "still not meeting the standard after rectification shall be subject to "
            "differentiated electricity pricing and lawfully ordered to phase out and close."


        ),


        "Compliance promotion": (


            "The state encourages rare earth metallurgical firms to benchmark against "
            "Grade 1 advanced values and undertake energy conservation and carbon reduction "
            "retrofits, and supports uptake of advanced energy-saving technologies through "
            "energy conservation technology retrofit incentives, green factory designation "
            "and other policy measures."


        ),


        "Mitigation co-benefits": "Industrial energy efficiency improvement; Industrial energy consumption reduction",


        "Legal statute": (
            "GB 29435-2025 Norm of Energy Consumption per Unit Production of "
            "Rare Earth Metallurgical Enterprise"
        ),


        "Other relevant websites": "N/A",


        "Last revision (Details)": (


            "First issued on 31 December 2012 as GB 29435-2012 Norm of Energy Consumption "
            "per Unit Production of Rare Earth Smelting and Processing Enterprises, effective "
            "1 October 2013. Second revision on 31 December 2025 (GB 29435-2025), renamed "
            "Norm of Energy Consumption per Unit Production of Rare Earth Metallurgical "
            "Enterprise (removing 'and Processing' from the title). Key revisions include: "
            "deletion of rare earth tri-band phosphors and polishing powders from scope; "
            "addition of rare earth compound product categories from NdFeB waste integrated "
            "recovery processes; reclassification of rare earth compounds into 4 categories "
            "and rare earth metals and alloys into 2 categories; revision of energy intensity "
            "limit values at each grade for each product category; and revision of statistical "
            "scope and calculation methods."


        ),


        "Mitigation effects": "Positive"


    },"""

assert old_entry in content, "Old entry not found!"
content = content.replace(old_entry, new_entry, 1)

with open(SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print("CHNPRFEILI63S000 EN entry updated in generate_english_from_chinese.py")
