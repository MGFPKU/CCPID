#!/usr/bin/env python3
"""Merge ROW_TRANSLATIONS for 01+03, update 04 in generate_english_from_chinese.py."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "generate_english_from_chinese.py"

with open(TARGET, "r", encoding="utf-8") as f:
    lines = f.readlines()

def find_tr_entry_end(lines, start_line):
    """Find the closing line of a TR dict entry starting at start_line."""
    depth = 0
    started = False
    for i in range(start_line, len(lines)):
        line = lines[i]
        if not started:
            if '{' in line:
                started = True
                depth = 1
            continue
        depth += line.count('{') - line.count('}')
        if depth == 0:
            return i
    return None

start_01 = next(i for i, l in enumerate(lines) if '"CHNVIIVLBI01S000":' in l)
end_01 = find_tr_entry_end(lines, start_01)
start_03 = next(i for i, l in enumerate(lines) if '"CHNVIIVLBI03S000":' in l)
end_03 = find_tr_entry_end(lines, start_03)
start_04 = next(i for i, l in enumerate(lines) if '"CHNVIIVLBI04S000":' in l)
end_04 = find_tr_entry_end(lines, start_04)

print(f"Entry 01: lines {start_01+1}-{end_01+1}")
print(f"Entry 03: lines {start_03+1}-{end_03+1}")
print(f"Entry 04: lines {start_04+1}-{end_04+1}")

# --- Merged ROW_TRANSLATIONS entry for CHNVIIVLBI01S000 ---
merged_01 = '''    "CHNVIIVLBI01S000": {
        "Emission sector": "Cross-sectoral",
        "English name": "Energy-Saving and Low-Carbon Product Certification",
        "Description": "The Energy-Saving and Low-Carbon Product Certification is a voluntary product certification system established and implemented under the leadership of the State Administration for Market Regulation together with multiple departments, formed through the integration of the former Energy-Saving Product Certification system and Low-Carbon Product Certification system. Through third-party testing and certification, it conducts comprehensive evaluation and labelling of end-use energy-consuming products on both energy efficiency and full-life-cycle greenhouse gas emissions, guiding consumers toward energy-saving and low-carbon products and encouraging enterprises to improve product energy efficiency and reduce carbon emissions. The system traces back to 1999 when the China Energy-Saving Product Certification Administrative Measures (State Economic and Trade Commission) established the earliest national-level voluntary energy-saving product certification system, and to 2013 when the Interim Administrative Measures for Low-Carbon Product Certification (NDRC Climate [2013] No. 279, jointly issued by NDRC and CNCA) added the low-carbon product certification dimension. In 2016, the General Office of the State Council issued the Opinions on Establishing a Unified Green Product Standard, Certification and Labelling System (Guobanfa [2016] No. 86), incorporating energy-saving and low-carbon product certification into the unified green product labelling system framework. In September 2022, the General Office of the State Council issued the Opinions on Deepening the Reform of the Management System for the Electronic and Electrical Appliances Industry (Guobanfa [2022] No. 31), formally integrating the Energy-Saving Product Certification system and the Low-Carbon Product Certification system into a unified Energy-Saving and Low-Carbon Product Certification system, with SAMR leading the development of certification rules and relevant departments jointly developing standards, and incorporating it into the green product certification and labelling system. Products passing the certification enjoy priority procurement or mandatory procurement policies in government procurement. Enterprises voluntarily apply for certification; there are no mandatory compliance obligations or penalties.",
        "Objective": "Promote energy efficiency improvement and low-carbon production and consumption",
        "Administrating authorities": "State Administration for Market Regulation (lead, Department of Certification Supervision); National Development and Reform Commission; Ministry of Industry and Information Technology; Ministry of Ecology and Environment. Historically: State Economic and Trade Commission (1999 energy-saving product certification); NDRC and CNCA (2013 low-carbon product certification)",
        "Asset": "End-use energy-consuming products (energy-saving and low-carbon certification objects)",
        "Asset (Details)": "The object defined and covered by this instrument is the various categories of end-use energy-consuming products that have passed energy-saving and low-carbon product certification, including household appliances (air conditioners, refrigerators, washing machines, televisions, etc.), office equipment (computers, printers, etc.), lighting products (LED luminaires, etc.), industrial equipment (electric motors, transformers, etc.), building materials (energy-saving windows and doors, insulation materials, etc.) and renewable energy products (solar water heaters, etc.). Certification evaluates products on both energy efficiency and full-life-cycle carbon emission dimensions; products must pass testing by designated testing bodies and meet the relevant energy-saving and low-carbon certification standard requirements.",
        "Agent (Detail)": "Manufacturers and distributors of end-use energy-consuming products. Enterprises may voluntarily apply to nationally accredited certification bodies for energy-saving and low-carbon product certification; upon product testing and factory inspection demonstrating compliance with energy-saving and low-carbon certification standards, they obtain the certification certificate and the right to use the label. Participation is voluntary, with no mandatory compliance obligations.",
        "Activity": "Registration, licensing or other administrative tasks",
        "Activity (Details)": "The activity regulated and guided by this instrument is the voluntary energy-saving and low-carbon product certification and labelling process for end-use energy-consuming products. Enterprises voluntarily submit certification applications to nationally accredited certification bodies; products must pass dual-dimension testing and evaluation on energy efficiency and carbon emissions; upon passing type testing and factory quality assurance capability inspection and meeting energy-saving and low-carbon certification standards, the certification certificate is issued and the right to use the label is granted. After certification, enterprises must undergo annual supervisory inspections by the certification body. Participation is voluntary.",
        "Requirement specification": "1) Products must meet the energy-saving evaluation values and carbon emission limit requirements specified in the relevant energy efficiency standards and low-carbon product certification technical specifications; 2) Enterprises must pass type testing (energy efficiency and carbon emission testing of product samples by designated testing bodies) and factory quality assurance capability inspection; 3) After certification, enterprises must undergo annual supervisory inspections by the certification body to ensure continued compliance with certification requirements; 4) Certified products may carry the energy-saving and low-carbon product certification mark on the product and packaging; 5) Products passing the certification enjoy priority procurement or mandatory procurement policies in government procurement; 6) Enterprises voluntarily apply for certification; there are no mandatory compliance obligations or penalties.",
        "Incentives for Participation": "Enterprises that obtain energy-saving and low-carbon product certification may use the certification mark on their products, enhancing product market competitiveness and consumer trust; certified products are included in government procurement priority procurement or mandatory procurement lists; some localities provide promotional support and financial incentives for certified products and enterprises; certification is linked to green finance policies, with certified enterprises and products eligible for green credit and green bond support.",
        "Monitoring": "Certified enterprises must undergo annual supervisory inspections and product sampling and testing by certification bodies to ensure continued compliance with energy-saving and low-carbon certification standards; certification bodies may suspend or revoke the certification certificate for non-compliant products; market regulatory authorities and relevant sectoral authorities supervise certification activities.",
        "Sanctions for non-compliance": "N/A (voluntary certification label; no non-compliance sanctions. For products and enterprises that fail to pass supervisory inspections or do not continuously meet certification requirements, the certification body may suspend or revoke their certification certificate and the right to use the label; those found to have engaged in falsification shall be held legally liable.)",
        "GHG emission coverage (absolute)": "N/A (this instrument is a voluntary certification and labelling tool; the amount of GHG emissions covered depends on the number of products voluntarily certified and the energy-saving and carbon reduction effect, and there is no directly quantifiable fixed coverage amount)",
        "GHG emission coverage (% domestic emissions)": "N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        "Mitigation co-benefits": "Energy efficiency improvement; Energy consumption reduction; Air pollutant emission reduction; Technological innovation; Green industry development",
        "Legal statute": "Opinions of the General Office of the State Council on Deepening the Reform of the Management System for the Electronic and Electrical Appliances Industry (Guobanfa [2022] No. 31)",
        "Other weblinks": "https://www.ndrc.gov.cn/fggz/hjyzy/stwmjs/200507/t20050711_1159582_ext.html; https://www.ndrc.gov.cn/xxgk/zcfb/tz/201303/t20130319_964565.html",
    },
'''

# --- Updated ROW_TRANSLATIONS for CHNVIIVLBI04S000 ---
updated_04 = '''    "CHNVIIVLBI04S000": {
        "Emission sector": "Cross-sectoral",
        "English name": "Energy Efficiency Top-Runner Programme",
        "Description": "The Energy Efficiency Top-Runner Programme is a voluntary system established and implemented under the leadership of the National Development and Reform Commission. It periodically selects and publishes the top runners with the highest energy efficiency levels among enterprises in high-energy-consuming industries and public institutions, and uses their energy efficiency levels as industry benchmarks and catch-up targets to guide energy users in energy efficiency benchmarking, target attainment and competition, thereby driving the continuous improvement of overall energy efficiency. The programme was established under the Implementation Plan for the Energy Efficiency Top-Runner Programme (NDRC Environment and Resources [2014] No. 3001) and originally covered three categories: end-use energy-consuming products, enterprises in high-energy-consuming industries and public institutions. In September 2022, the General Office of the State Council issued the Opinions on Deepening the Reform of the Management System for the Electronic and Electrical Appliances Industry (Guobanfa [2022] No. 31), abolishing the energy efficiency top-runner product selection system (end-use energy-consuming products track); the enterprise and public institution tracks continue. It now focuses on two categories: (1) High-energy-consuming industry top runners — enterprises whose unit product energy consumption reaches the industry advanced level, covering more than 30 sub-sectors including steel, non-ferrous metals, building materials, petrochemicals, chemicals, textiles and paper-making; (2) Public institution top runners — state organs, schools, hospitals and other public institutions whose energy and resource utilisation efficiency reaches an advanced level. The various top-runner lists are published by the competent government authorities following voluntary enterprise or public institution application, local recommendation, expert review and public notification. Participation is voluntary, with no mandatory compliance obligations or penalties.",
        "Objective": "Promote energy efficiency improvement",
        "Administrating authorities": "National Development and Reform Commission (Department of Resource Conservation and Environmental Protection); Ministry of Industry and Information Technology (Department of Energy Conservation and Comprehensive Utilisation); State Administration for Market Regulation (Department of Product Quality and Safety Supervision)",
        "Asset": "High-energy-consuming enterprises / public institutions (energy efficiency top-runner designation objects)",
        "Asset (Details)": "The object defined and covered by this instrument covers two categories: (1) High-energy-consuming industry enterprises, including those in steel, cement, electrolytic aluminium, flat glass, oil refining, ethylene and synthetic ammonia, with unit product comprehensive energy consumption as the selection basis; (2) Public institutions (state organs, schools, hospitals, etc.), with per-unit-floor-area energy consumption and per-capita energy consumption as the selection basis. Top runners in each category are selected and published every two years. The end-use energy-consuming product top-runner selection was abolished in September 2022 (Guobanfa [2022] No. 31).",
        "Agent (Detail)": "Enterprises in high-energy-consuming industries and public institutions. Enterprises may voluntarily apply for top-runner status, submitting unit product energy consumption data, and be selected following preliminary review, expert review and public notification. Public institutions may voluntarily apply for public institution top-runner status. The end-use energy-consuming product top-runner selection was abolished in September 2022. Participation is voluntary, with no mandatory compliance obligations.",
        "Activity": "Registration, licensing or other administrative tasks",
        "Activity (Details)": "The activity regulated and guided by this instrument is the voluntary application, selection and publication process for energy efficiency top runners among high-energy-consuming industry enterprises and public institutions. Enterprises or public institutions voluntarily submit application materials (unit product energy consumption data or per-unit-floor-area energy consumption indicators); following local recommendation, expert review and public notification, the competent government authorities publish the top-runner list. The list is valid for approximately two years, after which re-selection takes place. The end-use energy-consuming product top-runner selection was abolished in September 2022 (Guobanfa [2022] No. 31). Participation is voluntary.",
        "Requirement specification": "1) The unit product energy consumption of high-energy-consuming industry enterprises must reach the industry advanced level; 2) Public institutions must reach the advanced level of energy and resource consumption for the corresponding category of public institutions; 3) Selection is through voluntary enterprise/public institution application, local recommendation, expert review and public notification; 4) The top-runner list is valid for approximately two years, after which re-selection takes place; 5) The end-use energy-consuming product top-runner selection was abolished in September 2022 (Guobanfa [2022] No. 31); 6) Participation is voluntary.",
        "Incentives for Participation": "Selected top-runner enterprises and public institutions receive national and local media publicity and promotion, enhancing brand image and industry influence; they receive priority recommendation for inclusion in relevant demonstration lists; some localities provide commendation and financial awards to top-runner enterprises and public institutions; public institution top runners are incorporated into evaluation systems such as the establishment of resource-conserving institutions.",
        "Monitoring": "Selected top-runner enterprises and public institutions are subject to dynamic management during the validity period; if the enterprise unit product energy consumption or public institution energy consumption no longer meets the top-runner requirements, the top-runner qualification is revoked. The competent authorities organise third-party bodies to conduct supervisory inspections.",
        "Sanctions for non-compliance": "N/A (voluntary programme; no non-compliance sanctions. Those that no longer meet the top-runner conditions or are found to have engaged in falsification shall have their top-runner qualification revoked and be publicly announced.)",
        "GHG emission coverage (absolute)": "N/A (this instrument is a voluntary benchmarking programme; the amount of GHG emissions covered depends on the scale and extent of voluntary enterprise and public institution participation and energy efficiency improvement, and there is no directly quantifiable fixed coverage amount)",
        "GHG emission coverage (% domestic emissions)": "N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        "Mitigation co-benefits": "Energy efficiency improvement; Energy consumption reduction; Technological innovation; Green industry development; Air pollutant emission reduction",
        "Legal statute": "Notice on Issuing the Implementation Plan for the Energy Efficiency Top-Runner Programme (NDRC Environment and Resources [2014] No. 3001)",
        "Other weblinks": "N/A",
    },
'''

# --- Build new file ---
# Order: keep everything before 01, insert merged_01, skip old 01+03 entries, insert updated 04, keep rest
new_lines = (
    lines[:start_01] +
    [merged_01] +
    lines[end_03+1:start_04] +
    [updated_04] +
    lines[end_04+1:]
)

with open(TARGET, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

old_lines_removed = (end_01 - start_01 + 1) + (end_03 - start_03 + 1) + (end_04 - start_04 + 1)
new_lines_added = len(merged_01.splitlines(True)) + len(updated_04.splitlines(True))
print(f"Removed {old_lines_removed} old lines (entries 01+03+04)")
print(f"Added {new_lines_added} new lines (merged 01 + updated 04)")
print(f"Net change: {new_lines_added - old_lines_removed} lines")
print(f"Wrote {TARGET}")
print("Done.")
