#!/usr/bin/env python3
"""Insert English ROW_TRANSLATIONS entry for CHNPRFMEAI30S000."""

from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "generate_english_from_chinese.py"

with open(SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

ENTRY = """

    "CHNPRFMEAI30S000": {
        "Approach": "Minimum Energy Performance Standards (MEPS) for electric appliances",
        "Emission sector": "Industry; Buildings",
        "Sub-sector": "Lighting; Commercial buildings; Residential buildings; Public buildings",
        "English instrument name": (
            "Minimum Allowable Values of Energy Efficiency and Energy Efficiency "
            "Grades for Indoor Lighting LED Products"
        ),
        "Description": (
            "GB 30255-2026 Minimum Allowable Values of Energy Efficiency and Energy "
            "Efficiency Grades for Indoor Lighting LED Products is a mandatory national "
            "standard, published on 27 February 2026 and effective 1 September 2027, "
            "replacing GB 30255-2019. It applies to indoor lighting LED products including "
            "non-directional self-ballasted LED lamps, LED downlights (including narrow-beam "
            "spotlights), integrated LED lamps, LED high-bay luminaires, retrofit double-capped "
            "LED lamps, and LED indoor lighting products with additional functions such as "
            "dimming and colour tuning. Energy efficiency grades are classified into three "
            "levels (Grade 1 highest), with Grade 3 as the minimum allowable value i.e. the "
            "mandatory market access threshold. Compared with the previous edition, the "
            "new standard expands product coverage (adding narrow-beam LED downlights, LED "
            "high-bay luminaires and retrofit double-capped LED lamps), raises energy "
            "efficiency thresholds at each grade, and introduces a standby power requirement "
            "(<= 1.5 W), extending the evaluation from operational efficiency to full-time "
            "energy efficiency."
        ),
        "Objective": (
            "Improve LED lighting product energy efficiency; "
            "Reduce electricity consumption for building lighting"
        ),
        "Administrating authorities": (
            "State Administration for Market Regulation; "
            "Standardization Administration of China"
        ),
        "Asset": "Indoor lighting LED products",
        "Asset (Status)": "new",
        "Asset (Details)": (
            "Indoor lighting LED products, including non-directional self-ballasted LED "
            "lamps (AC- or DC-driven, replacing incandescent and self-ballasted fluorescent "
            "lamps for general lighting), LED downlights and spotlights (including "
            "narrow-beam spotlights with beam angle <= 30 degrees), integrated LED lamps "
            "(including LED retrofit light sources with standard bases and integrated "
            "luminaires), LED high-bay luminaires (for industrial and commercial spaces with "
            "mounting height >= 5 m), retrofit double-capped LED lamps (LED tubes replacing "
            "double-capped fluorescent lamps), and LED indoor lighting products with "
            "additional functions such as dimming, colour tuning and sensor integration. "
            "Colour rendering requirements: LED downlights and integrated LED lamps Ra >= 80; "
            "LED high-bay luminaires and retrofit double-capped LED lamps Ra >= 70; R9 "
            "measured value > 0."
        ),
        "Agent": "Firms",
        "Agent (Detail)": (
            "Manufacturers and importers producing, importing or selling indoor "
            "lighting LED products within China."
        ),
        "Activity": "Production; Sale; Import",
        "Activity (Details)": (
            "Production, import and sale of indoor lighting LED products. Products "
            "must meet the standard's minimum allowable energy efficiency values "
            "before they can enter the market."
        ),
        "Intensity (Value)": "Grade 3",
        "Intensity (Unit)": "Energy efficiency grade",
        "Intensity (Details)": (
            "Energy efficiency grades are classified into three levels (Grade 1 "
            "highest), with Grade 3 as the minimum allowable value i.e. the mandatory "
            "market access threshold. The evaluation indicator is initial luminous "
            "efficacy (lm/W), with limits set by product type (non-directional "
            "self-ballasted LED lamps, LED downlights, integrated LED lamps, LED "
            "high-bay luminaires, retrofit double-capped LED lamps) and by colour "
            "temperature / colour rendering index. The new standard moderately raises "
            "the Grade 3 access threshold, further improves Grade 2 energy-saving "
            "product requirements, and provides energy efficiency correction "
            "coefficients for high-CRI, anti-glare and intelligent control products. "
            "Products with standby mode must have standby power not exceeding 1.5 W."
        ),
        "Requirement specification": (
            "1) Indoor lighting LED products must meet the standard's minimum allowable "
            "energy efficiency values (Grade 3) before they may be produced, imported "
            "or sold; 2) Products must display an energy efficiency grade label; "
            "3) Energy efficiency grades are classified into Grade 1 (highest), Grade 2 "
            "and Grade 3, with Grade 3 as the mandatory market access threshold; "
            "4) Products with standby mode must have standby power not exceeding 1.5 W; "
            "5) LED downlights and integrated LED lamps must have Ra >= 80, LED high-bay "
            "luminaires and retrofit double-capped LED lamps must have Ra >= 70, with "
            "R9 measured value > 0."
        ),
        "Compliance monitoring": "Government inspections",
        "Compliance monitoring details": (
            "Market regulation authorities conduct energy efficiency label supervision "
            "inspections and product quality spot checks for indoor lighting LED "
            "products. Inspections cover accuracy of energy efficiency grade labelling, "
            "whether actual product energy efficiency matches labelled grades, whether "
            "standby power complies with limit values, and whether colour rendering "
            "indices meet standard requirements."
        ),
        "Compliance enforcement": "Compliance orders; Fines",
        "Compliance enforcement details": (
            "For production, import or sale of indoor lighting LED products that do not "
            "meet mandatory energy efficiency standards, market regulation authorities "
            "order cessation of production, import or sale, confiscate illegal gains "
            "and impose fines. In serious cases, business licences may be revoked."
        ),
        "Compliance promotion": "Other incentives or support",
        "Compliance promotion detail": (
            "The state encourages the production and use of Grade 1 and Grade 2 "
            "high-efficiency indoor lighting LED products, and promotes the "
            "high-efficiency LED lighting product market through energy-saving product "
            "certification and government green procurement. Firms are encouraged to "
            "benchmark against Grade 1 energy efficiency and undertake technology "
            "upgrades."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": (
            "Building lighting energy efficiency improvement; "
            "Building energy consumption reduction; "
            "Green building development"
        ),
        "Legal statute": (
            "GB 30255-2026 Minimum Allowable Values of Energy Efficiency and "
            "Energy Efficiency Grades for Indoor Lighting LED Products"
        ),
        "Other relevant websites": "N/A",
        "Last revision (Details)": (
            "First issued on 18 December 2013 as GB 30255-2013 Minimum Allowable "
            "Values of Energy Efficiency and Energy Efficiency Grades for Non-Directional "
            "Self-Ballasted LED Lamps for General Lighting, effective 1 September 2014. "
            "First revised in 2019 (GB 30255-2019), renamed Indoor Lighting LED Products "
            "with expanded product coverage. Second revision on 27 February 2026 "
            "(GB 30255-2026), adding narrow-beam LED downlights, LED high-bay luminaires, "
            "retrofit double-capped LED lamps and intelligent control products, raising "
            "energy efficiency thresholds at each grade, introducing a standby power "
            "requirement of <= 1.5 W, and promoting full-time energy efficiency "
            "evaluation. A 25-month transition period applies with full enforcement "
            "from the 25th month after 1 September 2027."
        ),
    },
"""

# Insert after PRFMEAI29 closing, before PRFMELI01
old = '\n\n\n\n    "CHNPRFMELI01S000": {'
assert old in content, "Insertion point not found!"
content = content.replace(old, ENTRY + '\n\n\n\n    "CHNPRFMELI01S000": {', 1)

with open(SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)
print("PRFMEAI30 English entry inserted into generate_english_from_chinese.py")
