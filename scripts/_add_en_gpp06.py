#!/usr/bin/env python3
"""Insert EN ROW_TRANSLATIONS entry for CHNPPCGPPI06S000."""

from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "generate_english_from_chinese.py"

with open(SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# Insert after PPCGPPI05, before PIVCBII02
old_marker = '\n\n\n\n\n\n    "CHNPIVCBII02S000": {'
assert old_marker in content, "Marker not found!"

new_entry = """

    "CHNPPCGPPI06S000": {


        "Policy Instrument ID": "CHNPPCGPPI06S000",


        "Instrument / subscheme": "Instrument",


        "Group": "Public procurement",


        "Approach": "Green public procurement",


        "Emission sector": "Transport",


        "Sub-sector": "Road transport and infrastructure",


        "English instrument name": (
            "Government Procurement Supporting Green and Low-Carbon Highway Development Pilot"
        ),


        "Policy Package": "N/A",


        "Description": (


            "The Ministry of Finance and the Ministry of Transport jointly issued the Notice on "
            "Organising the Government Procurement Supporting Green and Low-Carbon Highway "
            "Development Pilot (Caiku [2025] No. 32, 18 December 2025). The pilot runs for 3 "
            "years, with completion and acceptance in principle by 31 December 2028. It covers "
            "national, provincial, county and township highways (including expressways) across "
            "all stages: planning, feasibility study, design, tendering (procurement), "
            "construction, operation, and maintenance. Core elements: (1) develop and issue the "
            "Basic Requirements for Government Procurement Supporting Green and Low-Carbon "
            "Highway Development (Trial), forming an objective, quantified, verifiable and "
            "replicable government procurement demand standard; (2) embed the demand standard "
            "into tender documents as a substantive requirement or scoring criterion, "
            "implementing green and low-carbon policies throughout the highway construction "
            "process; (3) explore bulk centralised procurement for green materials, encouraging "
            "procurement through e-government procurement platforms; (4) promote the application "
            "of new materials, new technologies, new processes and new methods in highway "
            "construction. Eligible pilot tasks may be included in the Transport Powerhouse "
            "Special Pilot programme, and pilot projects meeting credit requirements may apply "
            "for green finance support."


        ),


        "Objective": (
            "Promote green and low-carbon highway development; "
            "Reduce carbon emissions from road construction and operation; "
            "Scale up green procurement in transport infrastructure"
        ),


        "Mitigation relevance": "Direct",


        "Functioning channel": "Demand-side",


        "Country": "CHN",


        "Jurisdiction level": "National",


        "Jurisdiction name": "N/A",


        "Adoption date": "18/12/2025",


        "Start date": "18/12/2025",


        "End date": "N/A",


        "Last revisions": "N/A",


        "Status": "In force",


        "Administrating authorities": (


            "Ministry of Finance (responsible for government procurement policy formulation "
            "and green procurement demand standard issuance); "
            "Ministry of Transport (responsible for highway construction, operation and "
            "maintenance green technology standard formulation and project promotion); "
            "Provincial finance departments and transport authorities in pilot areas "
            "(responsible for coordinating pilot application and implementation management); "
            "Pilot implementing units (transport authorities at or above the prefecture-city "
            "level, responsible for specific pilot project implementation)"


        ),


        "Asset": "Road transport infrastructure",


        "Asset (Status)": "New; existing",


        "Asset (Details)": (


            "National, provincial, county and township highways (including expressways), "
            "covering new construction, in-progress, and operation and maintenance projects. "
            "Pilot projects must have conditions suitable for applying new materials, new "
            "technologies, new processes and new methods, including but not limited to: warm "
            "mix asphalt, recycled asphalt mixtures, industrial solid waste subgrade fillers, "
            "high-performance concrete, photovoltaic road surfaces, low-carbon maintenance "
            "technologies, and intelligent construction equipment. Pilot areas must have a "
            "good foundation in green and low-carbon technology application. Individual "
            "prefecture-level cities may bundle multiple projects of different types in a "
            "single application."


        ),


        "Asset (Other)": "N/A",


        "Asset (Cut-off range)": "N/A",


        "Agent": "Government",


        "Agent (Detail)": (


            "Pilot implementing units are transport authorities at or above the prefecture-city "
            "level. Public institutions, central SOEs or local SOEs are in principle not "
            "separate application entities but may undertake specific implementation work. "
            "Provincial finance departments and transport authorities serve as pilot organising "
            "units, responsible for merit-based recommendation."


        ),


        "Activity": "Purchase or use; Investment",


        "Activity (Details)": (


            "Pilot implementing units must embed the Basic Requirements for Government "
            "Procurement Supporting Green and Low-Carbon Highway Development (Trial) into "
            "tender documents as a substantive requirement or scoring criterion. Design "
            "institutions prepare design documents in accordance with the demand standard. "
            "Construction units adopt green and low-carbon technologies and materials as "
            "required by design documents and contracts. Bulk centralised procurement may be "
            "implemented for green materials, with procurement through e-government platforms "
            "encouraged. Pilot projects prepare an acceptance assessment report within 30 days "
            "of completion (handover) acceptance. Use of big data and blockchain technologies "
            "to track pilot progress is encouraged."


        ),


        "Intensity (Value)": "N/A",


        "Intensity (Unit)": "N/A",


        "Intensity (Details)": (


            "This instrument is a government procurement demand standard mechanism, not a "
            "fiscal subsidy-type instrument, and does not have a direct monetary policy "
            "intensity indicator. It leverages the government procurement market to drive "
            "demand for green and low-carbon highway technologies and materials. Pilot "
            "projects meeting credit requirements may apply for green finance support."


        ),


        "Requirement specification": (


            "1. Develop and issue the Basic Requirements for Government Procurement Supporting "
            "Green and Low-Carbon Highway Development (Trial), forming an objective, "
            "quantified, verifiable and replicable demand standard, with dynamic adjustment; "
            "2. Embed the demand standard into tender documents as a substantive requirement "
            "or scoring criterion, implementing green and low-carbon policies throughout "
            "all stages of highway planning, feasibility study, design, tendering, "
            "construction, operation, maintenance and acceptance; "
            "3. Bulk centralised procurement may be implemented for green materials, with "
            "procurement through e-government platforms encouraged; "
            "4. Pilot projects must apply new materials, new technologies, new processes and "
            "new methods to create a strong demonstration effect; "
            "5. Highway projects under the jurisdiction of pilot areas must not have "
            "experienced a major or above production safety incident in the preceding 3 years; "
            "6. Pilot projects prepare an acceptance assessment report and submit it upward "
            "level by level within 30 days of completion acceptance; "
            "7. Submit an annual pilot summary report by 31 January each year."


        ),


        "Compliance calculation methodology I": "N/A",


        "Compliance calculation methodology II": "N/A",


        "Public investment: Contract type": "N/A",


        "Public investment: Selection criteria": "N/A",


        "Public procurement: Tender process": "Open tender",


        "Public procurement: Award criteria tender process": (
            "Compliance with the Basic Requirements for Government Procurement Supporting "
            "Green and Low-Carbon Highway Development (Trial) is a substantive procurement "
            "requirement or scoring criterion"
        ),


        "Public procurement: Compliance monitoring": (
            "Finance department oversight; Transport authority project supervision"
        ),


        "Public procurement: Compliance enforcement": "Contract enforcement",


        "Public procurement: Life-cycle costing": "N/A",


        "Public investment/procurement: Annual expenditure": (
            "Not disclosed. The pilot is still at the application and approval stage "
            "(first batch applications closed 31 January 2026, approval by 6 March 2026), "
            "and no annual expenditure data is available yet. The instrument leverages the "
            "government procurement market to drive demand for green highway technologies and "
            "materials."


        ),


        "Economic sector": "F42",


        "GHG affected": "CO2",


        "Mitigation effects": "Positive",


        "Mitigation co-benefits": (
            "Energy efficiency improvement; "
            "Pollution control; "
            "Circular economy; "
            "Technological innovation; "
            "Green industry development"
        ),


        "Legal statute": (
            "Notice on Organising the Government Procurement Supporting Green and "
            "Low-Carbon Highway Development Pilot (Caiku [2025] No. 32)"
        ),


        "Other relevant websites": (
            "https://m.mof.gov.cn/zcfb/202601/t20260104_3981293.htm"
        ),


    },"""

content = content.replace(old_marker, new_entry + old_marker, 1)

with open(SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print("EN entry inserted for CHNPPCGPPI06S000 in generate_english_from_chinese.py")
