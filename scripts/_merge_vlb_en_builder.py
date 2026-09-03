#!/usr/bin/env python3
"""Replace TR entry for CHNVIIVLBI01S000 with merged version,
   remove TR entry for CHNVIIVLBI03S000 in _add_vol_vlb_en.py."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "_add_vol_vlb_en.py"

with open(TARGET, "r", encoding="utf-8") as f:
    lines = f.readlines()

# --- Merged TR entry for CHNVIIVLBI01S000 (replaces old 01, absorbs 03) ---
merged_01 = '''    "CHNVIIVLBI01S000": {
        "Description": (
            "The Energy-Saving and Low-Carbon Product Certification is a voluntary "
            "product certification system established and implemented under the "
            "leadership of the State Administration for Market Regulation together "
            "with multiple departments, formed through the integration of the "
            "former Energy-Saving Product Certification system and Low-Carbon "
            "Product Certification system. Through third-party testing and "
            "certification, it conducts comprehensive evaluation and labelling of "
            "end-use energy-consuming products on both energy efficiency and "
            "full-life-cycle greenhouse gas emissions, guiding consumers toward "
            "energy-saving and low-carbon products and encouraging enterprises to "
            "improve product energy efficiency and reduce carbon emissions. The "
            "system traces back to 1999 when the China Energy-Saving Product "
            "Certification Administrative Measures (State Economic and Trade "
            "Commission) established the earliest national-level voluntary "
            "energy-saving product certification system, and to 2013 when the "
            "Interim Administrative Measures for Low-Carbon Product Certification "
            "(NDRC Climate [2013] No. 279, jointly issued by NDRC and CNCA) added "
            "the low-carbon product certification dimension. In 2016, the General "
            "Office of the State Council issued the Opinions on Establishing a "
            "Unified Green Product Standard, Certification and Labelling System "
            "(Guobanfa [2016] No. 86), incorporating energy-saving and low-carbon "
            "product certification into the unified green product labelling system "
            "framework. In September 2022, the General Office of the State Council "
            "issued the Opinions on Deepening the Reform of the Management System "
            "for the Electronic and Electrical Appliances Industry (Guobanfa "
            "[2022] No. 31), formally integrating the Energy-Saving Product "
            "Certification system and the Low-Carbon Product Certification system "
            "into a unified Energy-Saving and Low-Carbon Product Certification "
            "system, with SAMR leading the development of certification rules and "
            "relevant departments jointly developing standards, and incorporating "
            "it into the green product certification and labelling system. Products "
            "passing the certification enjoy priority procurement or mandatory "
            "procurement policies in government procurement. Enterprises "
            "voluntarily apply for certification; there are no mandatory compliance "
            "obligations or penalties."
        ),
        "Objective": "Promote energy efficiency improvement and low-carbon production and consumption",
        "Admin authorities": (
            "State Administration for Market Regulation (lead, Department of "
            "Certification Supervision); National Development and Reform "
            "Commission; Ministry of Industry and Information Technology; Ministry "
            "of Ecology and Environment. Historically: State Economic and Trade "
            "Commission (1999 energy-saving product certification); NDRC and CNCA "
            "(2013 low-carbon product certification)"
        ),
        "Regulated asset": "End-use energy-consuming products (energy-saving and low-carbon certification objects)",
        "Regulated asset (details)": (
            "The object defined and covered by this instrument is the various "
            "categories of end-use energy-consuming products that have passed "
            "energy-saving and low-carbon product certification, including "
            "household appliances (air conditioners, refrigerators, washing "
            "machines, televisions, etc.), office equipment (computers, printers, "
            "etc.), lighting products (LED luminaires, etc.), industrial equipment "
            "(electric motors, transformers, etc.), building materials "
            "(energy-saving windows and doors, insulation materials, etc.) and "
            "renewable energy products (solar water heaters, etc.). Certification "
            "evaluates products on both energy efficiency and full-life-cycle "
            "carbon emission dimensions; products must pass testing by designated "
            "testing bodies and meet the relevant energy-saving and low-carbon "
            "certification standard requirements."
        ),
        "Regulated agent (details)": (
            "Manufacturers and distributors of end-use energy-consuming products. "
            "Enterprises may voluntarily apply to nationally accredited "
            "certification bodies for energy-saving and low-carbon product "
            "certification; upon product testing and factory inspection "
            "demonstrating compliance with energy-saving and low-carbon "
            "certification standards, they obtain the certification certificate "
            "and the right to use the label. Participation is voluntary, with no "
            "mandatory compliance obligations."
        ),
        "Regulated activity (details)": (
            "The activity regulated and guided by this instrument is the voluntary "
            "energy-saving and low-carbon product certification and labelling "
            "process for end-use energy-consuming products. Enterprises voluntarily "
            "submit certification applications to nationally accredited "
            "certification bodies; products must pass dual-dimension testing and "
            "evaluation on energy efficiency and carbon emissions; upon passing "
            "type testing and factory quality assurance capability inspection and "
            "meeting energy-saving and low-carbon certification standards, the "
            "certification certificate is issued and the right to use the label "
            "is granted. After certification, enterprises must undergo annual "
            "supervisory inspections by the certification body. Participation is "
            "voluntary."
        ),
        "Requirement specification": (
            "1) Products must meet the energy-saving evaluation values and carbon "
            "emission limit requirements specified in the relevant energy "
            "efficiency standards and low-carbon product certification technical "
            "specifications; 2) Enterprises must pass type testing (energy "
            "efficiency and carbon emission testing of product samples by "
            "designated testing bodies) and factory quality assurance capability "
            "inspection; 3) After certification, enterprises must undergo annual "
            "supervisory inspections by the certification body to ensure continued "
            "compliance with certification requirements; 4) Certified products "
            "may carry the energy-saving and low-carbon product certification mark "
            "on the product and packaging; 5) Products passing the certification "
            "enjoy priority procurement or mandatory procurement policies in "
            "government procurement; 6) Enterprises voluntarily apply for "
            "certification; there are no mandatory compliance obligations or "
            "penalties."
        ),
        "Incentives for Participation": (
            "Enterprises that obtain energy-saving and low-carbon product "
            "certification may use the certification mark on their products, "
            "enhancing product market competitiveness and consumer trust; "
            "certified products are included in government procurement priority "
            "procurement or mandatory procurement lists; some localities provide "
            "promotional support and financial incentives for certified products "
            "and enterprises; certification is linked to green finance policies, "
            "with certified enterprises and products eligible for green credit "
            "and green bond support."
        ),
        "Monitoring": (
            "Certified enterprises must undergo annual supervisory inspections "
            "and product sampling and testing by certification bodies to ensure "
            "continued compliance with energy-saving and low-carbon certification "
            "standards; certification bodies may suspend or revoke the "
            "certification certificate for non-compliant products; market "
            "regulatory authorities and relevant sectoral authorities supervise "
            "certification activities."
        ),
        "Sanctions for non-compliance": (
            "N/A (voluntary certification label; no non-compliance sanctions. "
            "For products and enterprises that fail to pass supervisory "
            "inspections or do not continuously meet certification requirements, "
            "the certification body may suspend or revoke their certification "
            "certificate and the right to use the label; those found to have "
            "engaged in falsification shall be held legally liable.)"
        ),
        "GHG emissions coverage (absolute)": (
            "N/A (this instrument is a voluntary certification and labelling "
            "tool; the amount of GHG emissions covered depends on the number of "
            "products voluntarily certified and the energy-saving and carbon "
            "reduction effect, and there is no directly quantifiable fixed "
            "coverage amount)"
        ),
        "GHG emissions coverage (% of domestic emissions)": (
            "N/A (this instrument is a voluntary tool; the share of GHG emissions "
            "covered depends on voluntary uptake)"
        ),
        "Mitigation co-benefits": (
            "Energy efficiency improvement; Energy consumption reduction; "
            "Air pollutant emission reduction; Technological innovation; "
            "Green industry development"
        ),
        "Legal statute": (
            "Opinions of the General Office of the State Council on Deepening "
            "the Reform of the Management System for the Electronic and "
            "Electrical Appliances Industry (Guobanfa [2022] No. 31)"
        ),
    },
'''

# --- Find line ranges ---
# Entry 01: starts at line with '"CHNVIIVLBI01S000": {'
# Entry 03: starts at line with '"CHNVIIVLBI03S000": {'

start_01 = None
end_01 = None
start_03 = None
end_03 = None
brace_depth = 0
in_entry = False

for i, line in enumerate(lines):
    if '"CHNVIIVLBI01S000":' in line and not in_entry:
        start_01 = i
        in_entry = True
        brace_depth = 0
    elif '"CHNVIIVLBI03S000":' in line and not in_entry:
        start_03 = i
        in_entry = True
        brace_depth = 0

    if in_entry:
        brace_depth += line.count("{") - line.count("}")
        if brace_depth == 0 and "{" in lines[max(0, i-5):i+1][-1] or brace_depth == 0 and i > start_01:
            # Actually let's be more precise: the entry ends when brace_depth returns to 0
            # But brace_depth starts counting from the opening brace of the TR entry
            pass

# Simpler approach: find the line with "}, followed by next TR key or empty line
# For entry 01: find '    "CHNVIIVLBI01S000": {' then find the matching closing '    },'
# Let me use a different approach - find by tracking indent level

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

print(f"Entry 01: lines {start_01+1}-{end_01+1}")
print(f"Entry 03: lines {start_03+1}-{end_03+1}")

# --- Build new file ---
new_lines = (
    lines[:start_01] +
    [merged_01] +
    lines[end_01+1:start_03] +
    lines[end_03+1:]
)

with open(TARGET, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Wrote {TARGET}")
print(f"Removed {end_03 - start_03 + 1} lines (entry 03), replaced {end_01 - start_01 + 1} lines (entry 01 -> merged)")
print("Done.")
