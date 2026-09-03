"""Insert ROW_TRANSLATIONS entries for 6 new FRM instruments into generate_english_from_chinese.py.

Run from repo root:
    python scripts/_add_frm_en.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "generate_english_from_chinese.py"

NEW_ENTRIES = """

    "CHNFRMAPPI01S000": {
        "Policy Instrument ID": "CHNFRMAPPI01S000",
        "Approach": "Agricultural pollution prevention",
        "Asset": "Scale livestock farms and breeding communities",
        "Asset (Status)": "Existing",
        "Asset (Details)": (
            "Applies to livestock farms and breeding communities that meet the "
            "scale thresholds prescribed by provincial-level governments. "
            "Scale thresholds vary by species and region, typically: pig annual "
            "slaughter >= 500 head, dairy cow inventory >= 100 head, beef cattle "
            "slaughter >= 100 head, layer inventory >= 10,000 birds, broiler "
            "slaughter >= 50,000 birds. Farms in prohibited breeding zones are "
            "not covered and must relocate or close within prescribed time limits."
        ),
        "GHG emission coverage (absolute)": (
            "Livestock farming is one of the largest agricultural greenhouse gas "
            "emission sources in China. Methane and nitrous oxide emissions from "
            "manure management and feed production associated with scale farms "
            "(pig annual slaughter >= 500 head, dairy cow inventory >= 100 head, "
            "etc.) together account for approximately 5%-8% of national GHG "
            "emissions. The scale farms and breeding communities covered by the "
            "regulation account for approximately 60%-70% of national livestock "
            "production. Through biogas recovery and manure-to-fertiliser "
            "substitution, scale treatment can significantly reduce methane "
            "emissions and fertiliser-related production emissions."
        ),
        "GHG emission coverage (% domestic emissions)": (
            "Approximately 5%-8% (Source: China GHG Inventory; livestock "
            "farming sector emission share; covering scale farms and breeding "
            "communities accounting for approximately 60%-70% of national "
            "livestock production)"
        ),
        "Emission sector": "AFOLU",
        "Sub-sector": "Livestock farming",
        "English instrument name": "Livestock Scale Farming Pollution Prevention and Control System",
        "Policy Package": "N/A",
        "Description": (
            "The livestock scale farming pollution prevention and control system "
            "is a regulatory governance framework that implements systematic "
            "prevention and treatment of environmental pollution from livestock "
            "farms and breeding communities that meet prescribed scale thresholds. "
            "Established by the Regulation on the Prevention and Control of "
            "Pollution from Scale Livestock Farming (State Council Order No. 643), "
            "the system requires county-level and above local governments to "
            "designate prohibited breeding zones; scale farms must conduct "
            "environmental impact assessments, construct pollution prevention "
            "supporting facilities commensurate with their farming scale, "
            "implement comprehensive utilisation and harmless treatment of waste, "
            "and file records with environmental protection authorities. New "
            "farms are prohibited in prohibited zones, and existing farms must "
            "relocate or close within prescribed time limits. Scale thresholds "
            "are set by provincial governments, and fines range from 30,000 to "
            "500,000 yuan. The system covers approximately 2 million scale farms "
            "and breeding communities nationwide."
        ),
        "Objective": (
            "Livestock pollution prevention and control; waste resource "
            "utilisation promotion; rural ecological environment protection"
        ),
        "Administrating authorities": (
            "Ministry of Ecology and Environment; Ministry of Agriculture and "
            "Rural Affairs"
        ),
        "Agent": "Firms",
        "Agent (Detail)": (
            "Operators of scale livestock farms and breeding communities. Scale "
            "thresholds are determined and publicly notified by provincial "
            "people's governments, typically using indicators such as annual "
            "pig slaughter volume, dairy cow inventory, beef cattle slaughter "
            "volume, layer inventory and broiler slaughter volume. Prohibited "
            "breeding zones include drinking water source protection areas, "
            "core and buffer zones of nature reserves, urban residential areas, "
            "and population concentration areas such as cultural, educational "
            "and scientific research zones. Existing farms in prohibited zones "
            "must relocate or close within prescribed time limits."
        ),
        "Activity": "Production, generation or conversion",
        "Activity (Details)": (
            "Scale livestock farming activities, including scale farming of "
            "pigs, cattle and chickens as the main livestock species. Farms "
            "must construct pollution prevention supporting facilities "
            "commensurate with farming scale (rainwater-sewage separation, dry "
            "manure collection, biogas digesters, composting facilities, etc.) "
            "and ensure their normal operation. Waste must be comprehensively "
            "utilised (manure application to cropland, biogas production, "
            "organic fertiliser processing, etc.) or treated to meet discharge "
            "standards. Farms must file records with county-level ecology and "
            "environment authorities."
        ),
        "Intensity (Value)": "Determined by provincial governments",
        "Intensity (Unit)": (
            "Scale thresholds (e.g., annual pig slaughter >= 500 head)"
        ),
        "Intensity (Details)": (
            "Scale thresholds for livestock farming are determined by provincial "
            "people's governments based on local livestock development conditions "
            "and environmental carrying capacity, and reported to the State "
            "Council environmental protection and agriculture authorities for "
            "filing. The 12th Five-Year Plan on National Livestock Farming "
            "Pollution Prevention and Control, issued jointly by the then "
            "Ministry of Environmental Protection and Ministry of Agriculture, "
            "proposed reference standards: annual pig slaughter >= 500 head, "
            "dairy cow inventory >= 100 head, beef cattle slaughter >= 100 head, "
            "layer inventory >= 10,000 birds, broiler slaughter >= 50,000 birds."
        ),
        "Requirement specification": (
            "1) County-level and above local governments shall lawfully designate "
            "prohibited breeding zones; new farms are prohibited in such zones "
            "and existing farms must relocate or close within prescribed time "
            "limits; 2) new construction, reconstruction and expansion of farms "
            "must undergo environmental impact assessment; 3) farms must construct "
            "pollution prevention supporting facilities commensurate with farming "
            "scale and ensure their normal operation; 4) waste must be "
            "comprehensively utilised or treated harmlessly to achieve compliant "
            "discharge; 5) farms must file records with county-level ecology and "
            "environment authorities; 6) entities engaged in livestock farming "
            "and waste treatment activities must establish ledger recording systems."
        ),
        "Compliance calculation methodology I": "N/A",
        "Compliance calculation methodology II": "N/A",
        "Compliance monitoring": (
            "Filing; Information reporting; On-site inspection"
        ),
        "Compliance monitoring details": (
            "County-level and above ecology and environment authorities are "
            "responsible for supervision and inspection of pollution prevention "
            "by farms, and may conduct on-site inspections and sampling "
            "monitoring in accordance with law. Farms must establish pollution "
            "prevention ledgers, truthfully recording waste generation, "
            "comprehensive utilisation and treatment and disposal conditions. "
            "Township people's governments are responsible for routine patrol "
            "inspections of farms. Ecology and environment authorities report "
            "periodically to the people's government at the same level on "
            "pollution prevention conditions."
        ),
        "Compliance enforcement": (
            "Order to cease construction; Fines; "
            "Order to relocate or close within a time limit"
        ),
        "Compliance enforcement details": (
            "Illegal construction of farms in prohibited breeding zones is "
            "subject to an order by county-level and above ecology and "
            "environment authorities to cease construction and a fine of "
            "30,000-100,000 yuan; existing farms must relocate or close within "
            "a time limit. Failure to conduct EIA is subject to a fine of "
            "50,000-200,000 yuan. Failure to construct or ensure normal "
            "operation of pollution prevention supporting facilities is subject "
            "to a fine of up to 100,000 yuan. Discharge of pollutants exceeding "
            "standards is subject to a fine of up to 50,000 yuan. Compensation "
            "liability applies in accordance with law for environmental "
            "pollution caused."
        ),
        "Compliance promotion": (
            "Tax preferences; Agricultural electricity tariff; "
            "Biogas power generation feed-in tariff; VAT preferences"
        ),
        "Compliance promotion detail": (
            "The state provides policy support for livestock farming pollution "
            "prevention and control: tax preferences for comprehensive waste "
            "utilisation (biogas production, organic fertiliser processing, "
            "manure application to cropland, etc.); farm electricity consumption "
            "is charged at agricultural tariff rates; biogas power generation "
            "enjoys renewable energy feed-in tariffs; VAT preferences apply to "
            "organic fertiliser production from livestock waste. Integration of "
            "planting and breeding and agriculture-livestock circular systems "
            "are encouraged to achieve on-site waste absorption."
        ),
        "Mitigation co-benefits": (
            "Pollution control; Ecological protection; "
            "Resource conservation; Circular economy"
        ),
        "Mitigation effects": "Positive",
        "Legal statute": (
            "Regulation on the Prevention and Control of Pollution from Scale "
            "Livestock Farming (State Council Order No. 643)"
        ),
        "Last revisions (Details)": (
            "On 2 March 2019, the Decision of the State Council on Amending "
            "Certain Administrative Regulations (State Council Order No. 709) "
            "made package amendments to the regulation, changing "
            "“environmental protection authority” to “ecology and "
            "environment authority” and “industry and commerce "
            "administration authority” to “market regulatory "
            "authority” to align with the 2018 State Council institutional "
            "reform. The core regulatory framework underwent no substantive "
            "amendment and has remained stable since coming into effect in 2014."
        ),
        "Other weblinks": (
            "Decision of the State Council on Amending Certain Administrative "
            "Regulations (State Council Order No. 709, 2019 revision): "
            "https://www.gov.cn/gongbao/content/2019/content_5468893.htm"
        ),
    },

    "CHNFRMCEPI01S000": {
        "Policy Instrument ID": "CHNFRMCEPI01S000",
        "Approach": "Clean energy priority",
        "Asset": "Renewable energy generating units",
        "Asset (Status)": "Existing",
        "Asset (Details)": (
            "Applies to wind power, solar photovoltaic, hydropower, biomass "
            "power and other renewable energy generating units. The guaranteed "
            "full purchase system applies to the guaranteed purchase portion "
            "of electricity at state-approved feed-in tariffs. Renewable "
            "energy electricity participating in market-based trading is "
            "subject to contractually agreed prices and conditions."
        ),
        "GHG emission coverage (absolute)": (
            "In 2024, national renewable energy generation was approximately "
            "3.2 trillion kWh, accounting for 34% of total electricity "
            "consumption. The guaranteed full purchase system covers the entire "
            "guaranteed purchase portion of wind and solar power generation. "
            "In 2024, renewable energy generation displaced approximately "
            "2.5 Gt CO₂ from fossil fuel generation."
        ),
        "GHG emission coverage (% domestic emissions)": (
            "Approximately 20% (Source: NEA 2024 data; renewable energy "
            "generation displacing fossil fuel emissions as share of "
            "national emissions)"
        ),
        "Emission sector": "Energy",
        "Sub-sector": "Electricity",
        "English instrument name": "Clean Energy Priority Dispatch and Priority Purchase System",
        "Policy Package": "N/A",
        "Description": (
            "The clean energy priority dispatch and priority purchase system "
            "is an electricity market governance framework that establishes "
            "priority dispatch and guaranteed full purchase of renewable "
            "energy generation. The system is constituted jointly by the "
            "Energy Law of the People's Republic of China (2024) and the "
            "Regulatory Measures for the Guaranteed Full Purchase of Renewable "
            "Energy Electricity (NDRC Order No. 15, effective April 2024). It "
            "requires power dispatch institutions to dispatch renewable energy "
            "generation on a priority basis, grid enterprises to purchase the "
            "guaranteed purchase portion of renewable energy electricity in "
            "full, and promotes green energy consumption through the renewable "
            "energy green electricity certificate (GEC) system. Renewable "
            "energy on-grid electricity is divided into guaranteed purchase "
            "electricity and market-traded electricity: the guaranteed "
            "purchase portion is borne by electricity market participants "
            "in accordance with state requirements; market-traded electricity "
            "is priced through market-based mechanisms. Failure to dispatch "
            "renewable energy on a priority basis attracts regulatory penalties."
        ),
        "Objective": (
            "Guarantee renewable energy consumption; Promote clean energy "
            "development; Drive green energy structure transition"
        ),
        "Administrating authorities": (
            "National Development and Reform Commission; National Energy "
            "Administration; provincial energy authorities"
        ),
        "Agent": (
            "Grid enterprises; Power dispatch institutions; "
            "Electricity trading institutions"
        ),
        "Agent (Detail)": (
            "Grid enterprises bear the responsibility for absorbing guaranteed "
            "purchase electricity and must ensure the purchase and absorption "
            "of guaranteed purchase electricity in accordance with state "
            "requirements. Power dispatch institutions are responsible for "
            "compiling priority dispatch operating procedures for renewable "
            "energy and ensuring priority dispatch of renewable energy "
            "generation. Electricity trading institutions are responsible for "
            "promoting the participation of renewable energy in electricity "
            "market trading. Renewable energy generating enterprises must "
            "submit generation forecast data as required and cooperate with "
            "grid dispatch."
        ),
        "Activity": "Production, generation or conversion",
        "Activity (Details)": (
            "Grid connection dispatch and electricity purchase activities for "
            "renewable energy generation (wind, solar, hydropower, biomass "
            "power, etc.). Guaranteed purchase electricity is purchased in "
            "full by grid enterprises at state-approved feed-in tariffs; "
            "market-traded electricity is priced through electricity "
            "market-based mechanisms (bilateral negotiation, centralised "
            "bidding, listing transactions, etc.). Power dispatch institutions "
            "must dispatch renewable energy generation on a priority basis "
            "and compile and publish priority dispatch operating procedures."
        ),
        "Intensity (Value)": (
            "Implemented in accordance with renewable energy electricity "
            "consumption responsibility weights"
        ),
        "Intensity (Unit)": (
            "Renewable energy electricity consumption responsibility weight (%)"
        ),
        "Intensity (Details)": (
            "The state issues renewable energy electricity consumption "
            "responsibility weights (including total consumption responsibility "
            "weight and non-hydro consumption responsibility weight) to each "
            "province (autonomous region / municipality) on an annual basis; "
            "provincial energy authorities decompose them to city/county level "
            "and market entities. In 2024, provincial renewable energy "
            "electricity consumption responsibility weights ranged between 15% "
            "and 80% (differentiated by resource endowment and absorption "
            "capacity). Grid enterprises, electricity retailers and electricity "
            "users must fulfil consumption responsibilities according to weights; "
            "shortfalls must be made up through green certificate purchases."
        ),
        "Requirement specification": (
            "1) Power dispatch institutions must ensure priority dispatch of "
            "renewable energy generation and compile and publish priority "
            "dispatch operating procedures; 2) grid enterprises must purchase "
            "guaranteed purchase renewable energy electricity in full; "
            "3) each province (autonomous region / municipality) must meet "
            "state-issued renewable energy electricity consumption "
            "responsibility weights; 4) public institutions must give priority "
            "to procuring and using clean and low-carbon energy such as "
            "renewable energy (Energy Law, Article 34); 5) the state promotes "
            "a green energy consumption mechanism through the green electricity "
            "certificate (GEC) system; 6) failure to dispatch renewable energy "
            "generation on a priority basis will attract regulatory penalties."
        ),
        "Compliance calculation methodology I": "N/A",
        "Compliance calculation methodology II": "N/A",
        "Compliance monitoring": (
            "Information reporting; Annual assessment; "
            "Energy regulatory agency supervision and inspection"
        ),
        "Compliance monitoring details": (
            "The National Energy Administration and its regional offices are "
            "responsible for regulating priority dispatch and guaranteed full "
            "purchase of renewable energy generation. Grid enterprises must "
            "periodically report renewable energy consumption conditions to "
            "energy authorities. The state assesses the performance of each "
            "province's consumption responsibility weight on an annual basis; "
            "those failing to meet targets must rectify within a prescribed "
            "time limit. Priority dispatch performance by power dispatch "
            "institutions is subject to supervision and inspection by energy "
            "regulatory agencies."
        ),
        "Compliance enforcement": (
            "Order to rectify; Fines; Administrative sanctions"
        ),
        "Compliance enforcement details": (
            "Where a grid enterprise fails to purchase renewable energy "
            "electricity in accordance with state requirements, the energy "
            "regulatory agency orders it to rectify and imposes a fine. "
            "Where a power dispatch institution fails to dispatch renewable "
            "energy generation on a priority basis, directly responsible "
            "supervisors and other directly responsible personnel are subject "
            "to sanctions in accordance with law. Provinces and market entities "
            "failing to meet consumption responsibility weights must make up "
            "the shortfall through green certificate purchases and face "
            "deduction in the following year's assessment."
        ),
        "Compliance promotion": (
            "GEC trading revenue; Renewable energy fund subsidies; "
            "Priority procurement by public institutions"
        ),
        "Compliance promotion detail": (
            "Renewable energy generating enterprises may earn additional "
            "revenue through GEC trading. The state encourages enterprises "
            "to voluntarily purchase GECs to fulfil green electricity "
            "consumption commitments. Public institutions give priority in "
            "government procurement to products and services that use clean "
            "energy. Eligible renewable energy projects may receive subsidies "
            "from the National Renewable Energy Development Fund."
        ),
        "Mitigation co-benefits": (
            "Air pollutant emission reduction; Energy security; "
            "Green industry development; Renewable energy development"
        ),
        "Mitigation effects": "Positive",
        "Legal statute": (
            "Energy Law of the People's Republic of China "
            "(Presidential Order No. 37, 2024)"
        ),
        "Last revisions (Details)": (
            "The Energy Law of the People's Republic of China was adopted at "
            "the 12th session of the Standing Committee of the 14th National "
            "People's Congress on 8 November 2024 (Presidential Order No. 37), "
            "effective 1 January 2025, establishing for the first time at the "
            "statutory level the priority development and utilisation of "
            "renewable energy, the renewable energy electricity consumption "
            "guarantee and the green electricity certificate system. The "
            "Regulatory Measures for the Guaranteed Full Purchase of Renewable "
            "Energy Electricity (NDRC Order No. 15) was adopted on 5 February "
            "2024, effective 1 April 2024, replacing the 2007 version "
            "(Electricity Regulatory Commission Order No. 25)."
        ),
        "Other weblinks": (
            "Regulatory Measures for the Guaranteed Full Purchase of Renewable "
            "Energy Electricity (NDRC Order No. 15, 2024): "
            "https://www.gov.cn/gongbao/2024/issue_11326/202405/content_6949616.html"
        ),
    },

    "CHNFRMEPRI01S000": {
        "Policy Instrument ID": "CHNFRMEPRI01S000",
        "Approach": "Extended producer responsibility",
        "Asset": (
            "Product life-cycle take-back and treatment systems for products "
            "covered by the EPR system"
        ),
        "Asset (Status)": "new; existing",
        "Asset (Details)": (
            "Covers electrical and electronic products, automobile products, "
            "lead-acid batteries, beverage paper-based composite packaging, "
            "photovoltaic modules, power batteries and other products. "
            "Sector-specific implementation plans determine the detailed "
            "product catalogue, recovery rate targets and recycled content "
            "standards. Both new and existing manufacturing enterprises must "
            "be included under EPR system management."
        ),
        "GHG emission coverage (absolute)": "N/A",
        "GHG emission coverage (% domestic emissions)": "N/A",
        "Emission sector": "Cross-sectoral",
        "Sub-sector": "N/A",
        "English instrument name": "Extended Producer Responsibility System",
        "Policy Package": "N/A",
        "Description": (
            "The Extended Producer Responsibility (EPR) system is a governance "
            "framework that requires product producers to assume extended "
            "responsibility for the entire life cycle of their products, in "
            "particular post-consumer take-back and treatment. Established as "
            "a national-level institutional framework by the State Council "
            "General Office's Implementation Plan for the Extended Producer "
            "Responsibility System (SCGO [2016] No. 99), the system defines "
            "four responsibility areas (eco-design, use of recycled raw "
            "materials, standardised recycling and treatment, and strengthened "
            "information disclosure) and four priority sectors (electrical and "
            "electronic products, automobile products, lead-acid batteries "
            "and beverage paper-based composite packaging). Subsequently, "
            "Article 66 of the amended Law on the Prevention and Control of "
            "Environmental Pollution by Solid Waste (2020 revision) wrote EPR "
            "into law for the first time, and Article 959 of the Ecology and "
            "Environment Code (effective 2026) further entrenched the EPR "
            "principle and added penalty provisions. Emerging sectors such as "
            "photovoltaic modules and power batteries have been progressively "
            "included. The 2025 targets are: recycled raw material use ratio "
            "of 20% for key products, and average standardised take-back and "
            "recycling rate of 50% for end-of-life products."
        ),
        "Objective": (
            "Promote product life-cycle greening; Improve resource recovery "
            "and recycling levels; Reduce life-cycle environmental impacts "
            "of products"
        ),
        "Administrating authorities": (
            "National Development and Reform Commission; Ministry of Industry "
            "and Information Technology; Ministry of Ecology and Environment; "
            "State Administration for Market Regulation"
        ),
        "Agent": "Firms",
        "Agent (Detail)": (
            "Manufacturing enterprises of products covered by the EPR system, "
            "including electrical and electronic products, automobile products, "
            "lead-acid batteries, beverage paper-based composite packaging, "
            "photovoltaic modules, power batteries, etc. Producers must "
            "consider ease of recycling, disassembly and regeneration at the "
            "product design stage; prioritise the use of recycled raw materials "
            "at the procurement stage; establish take-back systems and recovery "
            "service outlets commensurate with product sales volumes; and "
            "publicly disclose information on product eco-design, recycled "
            "content ratios and take-back system development."
        ),
        "Activity": "Production, generation or conversion",
        "Activity (Details)": (
            "Design, production, sale, take-back and recycling of products "
            "covered by the EPR system across the full chain. Producers must "
            "implement eco-design and label recovery information at the "
            "production stage; establish recovery service outlets at the sales "
            "stage; accept or commission the take-back of end-of-life products "
            "at the recovery stage; and deliver end-of-life products to "
            "qualified treatment enterprises for resource recovery at the "
            "recycling stage."
        ),
        "Intensity (Value)": (
            "20% (recycled raw material use target); "
            "50% (recovery and recycling rate target)"
        ),
        "Intensity (Unit)": "Recovery and recycling rate target (%)",
        "Intensity (Details)": (
            "The State Council implementation plan sets 2025 targets: recycled "
            "raw material (recycled plastics, recycled metals, etc.) use ratio "
            "of 20% for key products; standardised take-back and recycling "
            "rate averaging 50% for end-of-life products. Sector-specific "
            "implementation plans set further detailed targets, e.g. beverage "
            "paper-based composite packaging recovery rate of 40% or above and "
            "resource recovery rate of 30% or above."
        ),
        "Requirement specification": (
            "1) Producers must implement eco-design at the product design "
            "stage, considering ease of recycling, disassembly and regeneration; "
            "2) producers must use a prescribed proportion of recycled raw "
            "materials in procurement; 3) producers must establish take-back "
            "systems commensurate with product sales volumes; 4) producers "
            "must publicly disclose information on product eco-design, recycled "
            "content ratios and take-back system plans; 5) each sector "
            "authority formulates an EPR implementation plan for its sector, "
            "specifying recovery and recycling targets and regulatory measures; "
            "6) the Ecology and Environment Code provides that producers "
            "failing to fulfil take-back obligations shall be ordered to "
            "rectify and fined."
        ),
        "Compliance calculation methodology I": "N/A",
        "Compliance calculation methodology II": "N/A",
        "Compliance monitoring": (
            "Information reporting; Sector EPR information platform; "
            "Environmental credit assessment; Whole-process monitoring"
        ),
        "Compliance monitoring details": (
            "Each sector authority is responsible for supervising the "
            "implementation of the EPR system in its sector. NDRC leads "
            "the coordination of EPR system promotion. Producers must "
            "periodically report product sales volumes, recycled raw material "
            "usage, end-of-life product take-back and treatment volumes, and "
            "other information to sector authorities and ecology and "
            "environment authorities. Industry associations such as the China "
            "Association of Electronic Equipment Technology Development and "
            "Utilisation have established EPR information management platforms "
            "to conduct sector data statistics and assessment. The system is "
            "integrated into the National Solid Waste Management Information "
            "System for whole-process supervision."
        ),
        "Compliance enforcement": (
            "Order to rectify; Fines; "
            "Order to suspend production for remediation; "
            "Recovery of subsidy funds"
        ),
        "Compliance enforcement details": (
            "Where a producer fails to fulfil end-of-life product take-back "
            "obligations, the ecology and environment authority orders "
            "rectification and imposes a fine in accordance with the Law on "
            "the Prevention and Control of Environmental Pollution by Solid "
            "Waste and the Ecology and Environment Code; where the circumstances "
            "are serious, suspension of production for remediation may be "
            "ordered. Failure to disclose EPR information as required is "
            "subject to rectification orders and penalties by market regulatory "
            "authorities. Fraudulent claims for EPR-related subsidies or "
            "incentives result in recovery of funds and penalties in accordance "
            "with law."
        ),
        "Compliance promotion": (
            "Environmental credit assessment; Central budgetary investment; "
            "Green finance support; Priority in government procurement"
        ),
        "Compliance promotion detail": (
            "The state provides policy incentives for enterprises implementing "
            "EPR: EPR performance is incorporated into the enterprise "
            "environmental credit assessment system. Eligible EPR projects may "
            "apply for central budgetary investment and green finance support. "
            "Products manufactured using recycled raw materials receive "
            "priority or bonus points in government procurement. Recycled raw "
            "material manufacturing enterprises enjoy VAT refund-upon-collection "
            "preferential policies for comprehensive resource utilisation."
        ),
        "Mitigation co-benefits": (
            "Resource conservation; Circular economy; "
            "Pollution control; Green industry development"
        ),
        "Mitigation effects": "Positive",
        "Legal statute": (
            "Implementation Plan for the Extended Producer Responsibility "
            "System (SCGO [2016] No. 99)"
        ),
        "Last revisions (Details)": (
            "On 1 September 2020, the amended Law on the Prevention and "
            "Control of Environmental Pollution by Solid Waste (2020 revision) "
            "came into force; Article 66 wrote EPR into law for the first "
            "time, specifying that the state establishes EPR systems for "
            "electrical and electronic products, lead-acid batteries, "
            "automotive power batteries and other products. On 15 August 2026, "
            "the Ecology and Environment Code came into force; Article 959 "
            "further entrenched the EPR system's legal status, Article 978 "
            "imposed obligations on producers to establish and publicly "
            "disclose take-back systems for end-of-life products, and Article "
            "1223 specified administrative penalty amounts. The 2016 version "
            "(SCGO [2016] No. 99) is the framework document for the system."
        ),
        "Other weblinks": (
            "Law on the Prevention and Control of Environmental Pollution by "
            "Solid Waste (2020 revision), Article 66 (EPR enshrined in law): "
            "https://www.gov.cn/xinwen/2020-04/30/content_5507646.htm "
            "| Ecology and Environment Code (effective 2026), Articles 959, "
            "978 and 1223"
        ),
    },

    "CHNFRMEPRI02S000": {
        "Policy Instrument ID": "CHNFRMEPRI02S000",
        "Approach": "Extended producer responsibility",
        "Asset": "Waste electrical and electronic equipment",
        "Asset (Status)": "new; existing",
        "Asset (Details)": (
            "Applies to waste electrical and electronic products listed in the "
            "WEEE Treatment Catalogue, including televisions, refrigerators, "
            "washing machines, air conditioners, microcomputers and extended "
            "catalogue products totalling 14 categories. Post-consumer products "
            "must enter the multi-channel take-back system and be centrally "
            "treated by permitted treatment enterprises meeting national standards."
        ),
        "GHG emission coverage (absolute)": "N/A",
        "GHG emission coverage (% domestic emissions)": "N/A",
        "Emission sector": "Waste",
        "Sub-sector": "E-waste",
        "English instrument name": (
            "Management of Waste Electrical and Electronic "
            "Equipment Recycling and Treatment"
        ),
        "Policy Package": "N/A",
        "Description": (
            "The Management of Waste Electrical and "
            "Electronic Equipment Recycling and Treatment is based on the "
            "Regulation on the Management of Waste Electrical and "
            "Electronic Equipment (WEEE) Recycling and Treatment (State Council "
            "Order No. 551), which is an administrative regulation establishing a "
            "multi-channel take-back and centralised treatment system for "
            "waste electrical and electronic products. The regulation requires "
            "electrical and electronic product manufacturers and importers to "
            "fulfil post-consumer take-back and treatment responsibilities, "
            "establishes a treatment catalogue system, implements a treatment "
            "qualification permit system, and established a WEEE treatment fund "
            "(replaced by direct central fiscal appropriations after the 2024 "
            "reform). The regulation covers five product categories: "
            "televisions, refrigerators, washing machines, air conditioners "
            "and microcomputers. Treatment enterprises must obtain a treatment "
            "qualification permit issued by the districted-city-level ecology "
            "and environment authority. Penalties for violations range from "
            "50,000 to 500,000 yuan. The regulation was enacted in 2009 and "
            "underwent institutional name-adaptation amendments in 2019. This "
            "instrument is the statutory implementation system for EPR in the "
            "e-waste sector and is an independent institutional-layer "
            "instrument from the economic instrument WEEE Recycling and "
            "Treatment Reward and Subsidy (CHNSUBRTSI01S000) which operates "
            "under the regulation's framework."
        ),
        "Objective": (
            "Standardise WEEE take-back and treatment; "
            "Promote resource recycling; "
            "Prevent and control e-waste pollution"
        ),
        "Administrating authorities": (
            "Ministry of Ecology and Environment; NDRC; "
            "Ministry of Industry and Information Technology; "
            "Ministry of Finance"
        ),
        "Agent": (
            "Electrical and electronic product manufacturers and importers; "
            "WEEE treatment enterprises"
        ),
        "Agent (Detail)": (
            "Electrical and electronic product manufacturers and importers "
            "must fulfil end-of-life product take-back and treatment "
            "responsibilities, and pay into the treatment fund (prior to the "
            "2024 reform) or incorporate the corresponding costs into product "
            "pricing. Treatment enterprises must obtain a treatment "
            "qualification permit issued by the districted-city-level ecology "
            "and environment authority, and possess the requisite treatment "
            "facilities, technology and environmental management capacity. "
            "Producers and importers may undertake self-take-back and treatment "
            "or commission qualified treatment enterprises."
        ),
        "Activity": "Production, generation or conversion",
        "Activity (Details)": (
            "Collection, transport, storage, dismantling, recovery and "
            "disposal of waste electrical and electronic products (televisions, "
            "refrigerators, washing machines, air conditioners, microcomputers "
            "and other products designated by NDRC jointly with relevant "
            "State Council departments). Treatment enterprises must operate "
            "in accordance with nationally prescribed treatment standards and "
            "environmental protection requirements. Take-back operators must "
            "deliver collected WEEE to qualified treatment enterprises and may "
            "not dismantle or resell it without authorisation."
        ),
        "Intensity (Value)": (
            "5 product categories (TVs, refrigerators, washing machines, "
            "air conditioners, microcomputers)"
        ),
        "Intensity (Unit)": (
            "Number of product categories in the treatment catalogue"
        ),
        "Intensity (Details)": (
            "The first batch of the WEEE Treatment Catalogue (2011) covered "
            "5 product categories. The catalogue was expanded to 14 categories "
            "in 2015 (additions: range hoods, electric water heaters, gas water "
            "heaters, printers, photocopiers, fax machines, telephones, "
            "monitors, mobile communication handsets). Treatment fund subsidy "
            "rates were set by product type and specification (e.g. TV 14-inch "
            "and above 25 yuan/unit, refrigerator 45 yuan/unit, washing "
            "machine 25 yuan/unit, etc.; replaced by direct central fiscal "
            "appropriations in 2024)."
        ),
        "Requirement specification": (
            "1) The state implements multi-channel take-back and centralised "
            "treatment for WEEE; 2) electrical and electronic product "
            "manufacturers and importers must fulfil post-consumer take-back "
            "and treatment responsibilities; 3) treatment of WEEE requires a "
            "treatment qualification permit; 4) treatment enterprises must "
            "carry out harmless treatment in accordance with national standards "
            "and technical specifications; 5) take-back operators must deliver "
            "collected WEEE to qualified treatment enterprises and may not "
            "dismantle it without authorisation; 6) treatment enterprises must "
            "establish a WEEE treatment information management system and "
            "retain treatment records for no fewer than 3 years."
        ),
        "Compliance calculation methodology I": "N/A",
        "Compliance calculation methodology II": "N/A",
        "Compliance monitoring": (
            "Treatment qualification permit approval; "
            "Treatment information system reporting; "
            "On-site inspection; Surveillance monitoring"
        ),
        "Compliance monitoring details": (
            "Districted-city-level ecology and environment authorities are "
            "responsible for the approval and routine supervision and "
            "inspection of treatment qualification permits. Treatment "
            "enterprises must establish treatment information management "
            "systems, truthfully recording the receipt, treatment, product "
            "sales and final disposal of end-of-life products. Provincial-level "
            "and above ecology and environment authorities conduct periodic "
            "on-site inspections and surveillance monitoring of treatment "
            "enterprises. The state has established a National WEEE Treatment "
            "Management Information System for whole-process supervision."
        ),
        "Compliance enforcement": (
            "Order to cease treatment activities; "
            "Confiscation of illegal gains; Fines; "
            "Public notification and disclosure"
        ),
        "Compliance enforcement details": (
            "Engaging in WEEE treatment activities without a treatment "
            "qualification permit is subject to an order by the ecology and "
            "environment authority to cease treatment activities, confiscation "
            "of illegal gains, and a fine of 50,000-500,000 yuan. Treatment "
            "enterprises failing to treat in accordance with specifications "
            "and causing environmental pollution are ordered to rectify "
            "within a time limit and fined 50,000-200,000 yuan. Producers "
            "failing to fulfil post-consumer take-back and treatment "
            "responsibilities are ordered to rectify within a time limit; "
            "failure to do so results in public notification and disclosure "
            "in relevant media."
        ),
        "Compliance promotion": (
            "Central fiscal treatment subsidy; "
            "VAT refund-upon-collection; "
            "Industrial land policy preferences"
        ),
        "Compliance promotion detail": (
            "The state provides treatment subsidies to qualified treatment "
            "enterprises (after the 2024 reform, central fiscal funds are "
            "transferred to provincial-level finance via atmospheric pollution "
            "prevention and control fund transfers, then allocated to "
            "treatment enterprises). Treatment enterprises enjoy VAT "
            "refund-upon-collection preferential policies for comprehensive "
            "resource utilisation. Treatment enterprise land use enjoys "
            "industrial land policy preferences. Producers and treatment "
            "enterprises are encouraged to cooperate in building take-back "
            "and treatment systems."
        ),
        "Mitigation co-benefits": (
            "Resource conservation; Circular economy; "
            "Pollution control; Green industry development"
        ),
        "Mitigation effects": "Positive",
        "Legal statute": (
            "Regulation on the Management of Waste Electrical and Electronic "
            "Equipment Recycling and Treatment (State Council Order No. 551)"
        ),
        "Last revisions (Details)": (
            "On 2 March 2019, package amendments were made in accordance with "
            "the Decision of the State Council on Amending Certain "
            "Administrative Regulations (State Council Order No. 709), "
            "changing “environmental protection authority” to "
            "“ecology and environment authority” and “industry "
            "and commerce administration authority” to “market "
            "regulatory authority” to align with the 2018 State Council "
            "institutional reform. The WEEE treatment fund established in 2012 "
            "was reformed in 2024 to direct central fiscal appropriations "
            "(MC-ER [2024] No. 119), discontinuing the fund system."
        ),
        "Other weblinks": (
            "WEEE Treatment Catalogue (2014 edition, covering 14 product "
            "categories): "
            "https://www.gov.cn/zhengce/content/2015-02/11/content_9468.htm "
            "| WEEE Recycling and Treatment Reward and Subsidy economic "
            "instrument: CHNSUBRTSI01S000"
        ),
    },

    "CHNFRMEPRI03S000": {
        "Policy Instrument ID": "CHNFRMEPRI03S000",
        "Approach": "Extended producer responsibility",
        "Asset": "Waste power batteries from new energy vehicles",
        "Asset (Status)": "Existing",
        "Asset (Details)": (
            "Applies to waste power batteries (lithium-ion batteries, etc.) "
            "retired from new energy vehicles. Power battery enterprises must "
            "code and label batteries, establish digital IDs, and upload "
            "production information to the national traceability management "
            "platform. A vehicle-battery integrated scrapping system is "
            "implemented: end-of-life NEVs must carry their power batteries "
            "when scrapped (battery-swap models excepted). It is prohibited "
            "to use waste power batteries directly or after processing for "
            "electric bicycles, electric motorcycles, low-speed electric "
            "vehicles, power tools and other non-design-purpose applications."
        ),
        "GHG emission coverage (absolute)": (
            "As of end-2025, China's NEV fleet exceeded 30 million vehicles "
            "with total installed power battery capacity exceeding 1.5 TWh. "
            "Annual waste power battery generation is projected to exceed "
            "1 million tonnes by 2030. Formal channel recovery and recycling "
            "can effectively recover key metals including lithium, cobalt and "
            "nickel, reducing carbon emissions from virgin mineral extraction "
            "(lithium recovery reduces emissions by approximately 50% compared "
            "to virgin extraction; cobalt and nickel recovery reduces "
            "emissions by approximately 70%). The formal channel recovery "
            "rate was approximately 30% in 2024."
        ),
        "GHG emission coverage (% domestic emissions)": (
            "N/A (Source: MIIT data; no unified national total share "
            "accounting for power battery recycling emission reductions "
            "is currently available)"
        ),
        "Emission sector": "Industry",
        "Sub-sector": "New energy vehicles; Power batteries",
        "English instrument name": (
            "Management of Recycling and "
            "Comprehensive Utilisation of Waste Power Batteries "
            "from New Energy Vehicles"
        ),
        "Policy Package": "N/A",
        "Description": (
            "The Interim Measures for the Management of Recycling and "
            "Comprehensive Utilisation of Waste Power Batteries from New "
            "Energy Vehicles is a joint departmental regulation establishing "
            "a whole-life-cycle traceability management and recycling system "
            "for power batteries. The measures were jointly issued by six "
            "departments — the Ministry of Industry and Information "
            "Technology, NDRC, Ministry of Ecology and Environment, Ministry "
            "of Transport, Ministry of Commerce and State Administration for "
            "Market Regulation — as Joint Departmental Regulation No. 73, "
            "adopted at the MIIT ministerial affairs meeting on 30 October "
            "2025 and effective 1 April 2026. Core institutions include: "
            "establishment of a national NEV power battery traceability "
            "information platform; implementation of a battery coding and "
            "digital ID card system; power battery enterprises and NEV "
            "manufacturers bear primary take-back responsibility and must "
            "establish take-back service outlets; a vehicle-battery integrated "
            "scrapping system (battery-swap models excepted); prohibition on "
            "using waste power batteries directly or after processing for "
            "electric bicycles and other applications; and administrative "
            "penalties for violations such as failure to code and failure to "
            "fulfil take-back responsibilities. Annual waste power battery "
            "generation is projected to exceed 1 million tonnes in 2030. This "
            "instrument is the EPR system's sector-specific implementation "
            "instrument for the power battery sector."
        ),
        "Objective": (
            "Establish a power battery whole-life-cycle traceability "
            "management system; Implement producer take-back primary "
            "responsibility; Standardise comprehensive utilisation of "
            "waste power batteries"
        ),
        "Administrating authorities": (
            "Ministry of Industry and Information Technology; NDRC; "
            "Ministry of Ecology and Environment; Ministry of Transport; "
            "Ministry of Commerce; State Administration for Market Regulation"
        ),
        "Agent": (
            "Power battery enterprises; "
            "New energy vehicle manufacturers"
        ),
        "Agent (Detail)": (
            "Power battery enterprises and NEV manufacturers bear primary "
            "responsibility for waste power battery take-back. Power battery "
            "enterprises must code and label batteries at the production "
            "stage, upload information to the national traceability management "
            "platform, and establish battery digital ID cards. NEV "
            "manufacturers must establish take-back service outlets, accept "
            "waste power batteries returned by consumers, and transfer them "
            "as required to qualified comprehensive utilisation enterprises. "
            "End-of-life vehicle recycling and dismantling enterprises must "
            "transfer waste power batteries obtained from dismantling to "
            "comprehensive utilisation enterprises. Consumers must return "
            "waste power batteries to designated take-back service outlets."
        ),
        "Activity": "Production, generation or conversion",
        "Activity (Details)": (
            "Collection, transport, testing, dismantling and regenerative "
            "recovery of waste power batteries across the full chain. Power "
            "batteries retired from NEVs must enter formal take-back channels "
            "through take-back service outlets, and after testing be directed "
            "to comprehensive utilisation (regenerative recovery) by category. "
            "The measures no longer use the concept of “ascade "
            "utilisation” and prohibit using waste power batteries "
            "directly or after processing for electric bicycles, electric "
            "motorcycles, low-speed electric vehicles, power tools and "
            "similar applications. Comprehensive utilisation enterprises "
            "must be located in development zones or industrial parks, with "
            "capacity no less than 5,000 tonnes/year (regenerative recovery) "
            "and paid-in capital no less than 5 million yuan."
        ),
        "Intensity (Value)": (
            "Regenerative recovery enterprise capacity "
            ">= 5,000 tonnes/year"
        ),
        "Intensity (Unit)": (
            "Annual comprehensive utilisation capacity (tonnes/year)"
        ),
        "Intensity (Details)": (
            "The NEV Waste Power Battery Comprehensive Utilisation Industry "
            "Standard Conditions (2024 edition) (MIIT Announcement No. 42 of "
            "2024) provides: cascade utilisation enterprise capacity in "
            "principle no less than 1,000 tonnes/year and regenerative "
            "recovery enterprise capacity in principle no less than 5,000 "
            "tonnes/year. Enterprise registered capital no less than 10 "
            "million yuan with paid-in capital no less than 5 million yuan. "
            "New comprehensive utilisation enterprises must be located in "
            "development zones or industrial parks. Only approximately 30% "
            "of retired power batteries entered formal take-back channels "
            "in 2024; the management measures aim to increase the formal "
            "channel recovery rate."
        ),
        "Requirement specification": (
            "1) Power battery enterprises must code and label batteries and "
            "upload to the national traceability management platform, "
            "establishing battery digital ID cards; 2) power battery "
            "enterprises and NEV manufacturers must establish take-back "
            "service outlets; 3) a vehicle-battery integrated scrapping "
            "system is implemented: end-of-life NEVs must carry their power "
            "batteries when scrapped (battery-swap models excepted); 4) waste "
            "power batteries must be transferred to qualified comprehensive "
            "utilisation enterprises and may not be dismantled or resold "
            "without authorisation; 5) it is prohibited to use waste power "
            "batteries directly or after processing for electric bicycles, "
            "electric motorcycles, low-speed electric vehicles, power tools "
            "and similar applications; 6) comprehensive utilisation "
            "enterprises must be located in industrial parks as required and "
            "meet capacity, registered capital and environmental protection "
            "entry conditions; 7) enterprises must establish traceability "
            "systems and upload information to the national traceability "
            "management platform."
        ),
        "Compliance calculation methodology I": "N/A",
        "Compliance calculation methodology II": "N/A",
        "Compliance monitoring": (
            "Traceability information platform whole-process traceability; "
            "Battery coding and digital ID cards; "
            "Information reporting; Supervision and inspection"
        ),
        "Compliance monitoring details": (
            "MIIT has established a national NEV power battery traceability "
            "information platform for retrospective management of the entire "
            "process of power battery production, sale, use, scrapping, "
            "take-back and comprehensive utilisation. Battery coding and "
            "labelling information must be uploaded within 30 working days "
            "of battery production. Industry and IT, ecology and environment, "
            "transport and market regulatory authorities at all levels conduct "
            "supervision and inspection of recycling activities according to "
            "their respective responsibilities. Comprehensive utilisation "
            "enterprises must periodically report production and operation "
            "information."
        ),
        "Compliance enforcement": (
            "Order to rectify; Fines; "
            "Order to suspend production for rectification"
        ),
        "Compliance enforcement details": (
            "Where a power battery enterprise or NEV manufacturer fails to "
            "code and label batteries as required, it is ordered to rectify "
            "within a time limit and fined 10,000-50,000 yuan. Failure to "
            "establish take-back service outlets or failure to fulfil "
            "take-back responsibilities is subject to an order to rectify "
            "and a fine of 50,000-200,000 yuan. Failure to transfer waste "
            "power batteries as required is subject to an order to rectify "
            "and a fine of 100,000-500,000 yuan. Where a comprehensive "
            "utilisation enterprise disposes of waste power batteries in "
            "violation of regulations, it is ordered to suspend production "
            "for rectification and fined 200,000-500,000 yuan. Failure to "
            "report information as required is subject to a fine of "
            "10,000-30,000 yuan."
        ),
        "Compliance promotion": (
            "VAT refund-upon-collection; "
            "Central budgetary investment; "
            "Industrial park preferences; "
            "Green finance support"
        ),
        "Compliance promotion detail": (
            "Qualified comprehensive utilisation enterprises may enjoy VAT "
            "refund-upon-collection preferential policies for comprehensive "
            "resource utilisation. Waste power battery recycling projects "
            "may apply for central budgetary investment support. Power "
            "battery enterprises and NEV manufacturers are encouraged to "
            "cooperate with comprehensive utilisation enterprises to "
            "establish waste power battery recycling systems. Comprehensive "
            "utilisation enterprises locating in industrial parks as required "
            "may enjoy land and infrastructure support preferences. Waste "
            "power battery recycling is included within the scope of green "
            "bond and green credit support."
        ),
        "Mitigation co-benefits": (
            "Resource conservation; Circular economy; "
            "Pollution control; Green industry development"
        ),
        "Mitigation effects": "Positive",
        "Legal statute": (
            "Interim Measures for the Management of Recycling and "
            "Comprehensive Utilisation of Waste Power Batteries from "
            "New Energy Vehicles (Six-Department Joint "
            "Departmental Regulation No. 73)"
        ),
        "Last revisions (Details)": (
            "These measures are the first-time enactment, adopted at the MIIT "
            "ministerial affairs meeting on 30 October 2025, published 16 "
            "January 2026, and effective 1 April 2026. They simultaneously "
            "repeal four previous documents including the 2018 version "
            "Interim Measures for the Management of New Energy Vehicle Power "
            "Battery Recycling and Utilisation (MIIT-LJ [2018] No. 43). The "
            "measures implement the requirements of the State Council General "
            "Office Action Plan for Perfecting the NEV Power Battery "
            "Recycling System issued in February 2025, enhancing legal "
            "binding force through the form of a joint departmental "
            "regulation. Compared with the 2018 version, the measures remove "
            "the concept of “cascade utilisation” and add the "
            "digital ID card system and vehicle-battery integrated scrapping "
            "requirement."
        ),
        "Other weblinks": (
            "NEV Waste Power Battery Comprehensive Utilisation Industry "
            "Standard Conditions (2024 edition) (MIIT Announcement No. 42 "
            "of 2024) | Action Plan of the General Office of the State Council "
            "for Perfecting the NEV Power Battery Recycling System "
            "(SCGO [2025] No. 10)"
        ),
    },

    "CHNFRMISAI01S000": {
        "Policy Instrument ID": "CHNFRMISAI01S000",
        "Approach": "Industrial structural adjustment",
        "Asset": (
            "Production facilities across all industrial sectors"
        ),
        "Asset (Status)": "Existing",
        "Asset (Details)": (
            "Applies to fixed-asset investment activities across all "
            "industrial sectors, covering new construction, reconstruction "
            "and expansion projects of production facilities in agriculture, "
            "forestry and fisheries, mining, manufacturing, electricity, "
            "heat, gas and water production and supply, and all other "
            "industry categories. Categories other than Encouraged, "
            "Restricted and Eliminated are categorised as Permitted, which "
            "are not listed in the catalogue but must comply with laws, "
            "regulations and policy requirements."
        ),
        "GHG emission coverage (absolute)": "N/A",
        "GHG emission coverage (% domestic emissions)": "N/A",
        "Emission sector": "Cross-sectoral",
        "Sub-sector": "N/A",
        "English instrument name": "Industrial Structure Adjustment Guidance Catalogue",
        "Policy Package": "N/A",
        "Description": (
            "The Industrial Structure Adjustment Guidance Catalogue is a "
            "comprehensive industrial governance institution that classifies "
            "all industry sectors into three categories: Encouraged, "
            "Restricted and Eliminated. The catalogue serves as an important "
            "basis for guiding social investment direction, for government "
            "management of investment projects, and for formulating and "
            "implementing fiscal, tax, credit, land, import and export and "
            "other policies. All enterprises within Chinese territory "
            "undertaking new construction, reconstruction or expansion "
            "projects must comply with the sector entry conditions set out "
            "in the catalogue. New projects in Restricted categories are "
            "prohibited; existing production capacity is allowed to undergo "
            "upgrading within a prescribed period. Projects in Eliminated "
            "categories are prohibited from investment and must be "
            "eliminated by the prescribed deadline; those failing to meet "
            "the deadline are ordered to cease production or close. The "
            "catalogue is formulated by the National Development and Reform "
            "Commission jointly with relevant State Council departments "
            "and published after State Council approval. The current 2024 "
            "edition contains 1,005 entries (352 Encouraged, 231 Restricted, "
            "422 Eliminated), covering more than 50 broad industry "
            "categories. The system was established on the basis of the "
            "Decision of the State Council on Issuing and Implementing the "
            "Interim Provisions on Promoting Industrial Structural "
            "Adjustment (SC [2005] No. 40)."
        ),
        "Objective": (
            "Guide industrial investment direction; "
            "Eliminate backward production capacity; "
            "Promote industrial structure optimisation and upgrading; "
            "Drive green and low-carbon transition"
        ),
        "Administrating authorities": (
            "National Development and Reform Commission; "
            "Relevant State Council departments; "
            "Provincial people's governments"
        ),
        "Agent": "Firms",
        "Agent (Detail)": (
            "All types of enterprises within Chinese territory, covering "
            "investment entities undertaking new construction, reconstruction "
            "or expansion of industrial projects. Foreign-invested enterprises "
            "must also comply with the provisions of the Encouraged Foreign "
            "Investment Industry Catalogue. The catalogue classification "
            "applies to enterprise investment projects in all sectors; any "
            "enterprise undertaking a new construction, reconstruction or "
            "expansion project must check the catalogue to determine the "
            "category to which the project belongs and obtain the "
            "corresponding project approval, verification or filing "
            "qualification accordingly."
        ),
        "Activity": "Production, generation or conversion",
        "Activity (Details)": (
            "Fixed-asset investment activities (new construction, "
            "reconstruction, expansion projects) covering more than 50 "
            "broad industry categories including agriculture, forestry "
            "and fisheries, coal, electricity, new energy, nuclear energy, "
            "steel, non-ferrous metals, petrochemicals and chemicals, "
            "building materials, pharmaceuticals, machinery, automobiles, "
            "aerospace, light industry, textiles, construction, transport, "
            "information industry, finance, modern logistics, science and "
            "technology services, artificial intelligence and intelligent "
            "manufacturing. Encouraged projects are approved, verified or "
            "filed in accordance with relevant provisions; Restricted "
            "projects are prohibited from new construction, with existing "
            "capacity required to upgrade within a prescribed period; "
            "Eliminated projects are prohibited from investment and must "
            "be eliminated by the prescribed deadline."
        ),
        "Intensity (Value)": (
            "352 Encouraged entries; 231 Restricted entries; "
            "422 Eliminated entries"
        ),
        "Intensity (Unit)": "Number of industry classification entries",
        "Intensity (Details)": (
            "The 2024 edition contains 1,005 entries: 352 Encouraged entries, "
            "covering technologies, equipment and products that have a "
            "significant promotional role in economic and social development; "
            "financial institutions provide credit support on market-based "
            "principles. 231 Restricted entries, covering processes, "
            "technologies and products with backward technology, that fail "
            "to meet sector entry conditions, or that are detrimental to "
            "workplace safety and carbon peaking / carbon neutrality; new "
            "construction is prohibited, and existing capacity is allowed "
            "to undergo upgrading within a prescribed period. 422 Eliminated "
            "entries, covering technical equipment and products that fail to "
            "comply with laws and regulations, seriously waste resources, "
            "cause environmental pollution or pose serious workplace safety "
            "hazards; investment is prohibited and elimination must occur by "
            "the prescribed deadline; those failing to do so are ordered by "
            "local governments to cease production or close in accordance "
            "with law."
        ),
        "Requirement specification": (
            "1) All new construction, reconstruction and expansion projects "
            "must check the catalogue to determine their category and obtain "
            "project approval, verification or filing qualification "
            "accordingly; 2) Encouraged projects are approved, verified or "
            "filed in accordance with relevant provisions; financial "
            "institutions provide credit support on market-based principles; "
            "3) new construction of Restricted projects is prohibited; "
            "existing production capacity is allowed to undergo upgrading "
            "within a prescribed period; 4) Eliminated projects are "
            "prohibited from investment and must be eliminated by the "
            "prescribed deadline; failing to do so, local governments shall "
            "order them to cease production or close in accordance with "
            "law; 5) for projects in violation of catalogue provisions, "
            "investment authorities shall not approve, verify or file; "
            "financial institutions shall not extend loans; land, "
            "environmental protection, quality inspection, fire protection, "
            "customs, industry and commerce and other departments shall not "
            "process relevant procedures; 6) the catalogue is formulated by "
            "NDRC jointly with relevant State Council departments and "
            "published after State Council approval."
        ),
        "Compliance calculation methodology I": "N/A",
        "Compliance calculation methodology II": "N/A",
        "Compliance monitoring": (
            "Project approval compliance review; "
            "Periodic catalogue revision; On-site verification"
        ),
        "Compliance monitoring details": (
            "NDRC leads and is responsible for supervising the implementation "
            "of the catalogue, and periodically revises it jointly with "
            "relevant State Council departments based on economic and social "
            "development needs. Each sector authority implements classified "
            "management of projects in its sector based on the catalogue. "
            "Local governments are responsible for the implementation of the "
            "catalogue within their administrative areas, ensuring the "
            "elimination of Eliminated-category capacity on schedule. "
            "Investment authorities must conduct compliance reviews based on "
            "the catalogue when approving, verifying or filing projects."
        ),
        "Compliance enforcement": (
            "Denial of approval, verification or filing; "
            "Denial of loans; "
            "Order to cease production or close; "
            "Revocation of permits"
        ),
        "Compliance enforcement details": (
            "For new construction of Restricted-category projects, investment "
            "authorities shall not process approval, verification or filing "
            "procedures; financial institutions shall not extend loans; and "
            "land, environmental protection and other departments shall not "
            "process relevant procedures. For Eliminated-category projects "
            "that fail to eliminate backward capacity on schedule, local "
            "governments shall order cessation of production or closure in "
            "accordance with law and revoke relevant permits. Departments "
            "and institutions granting approvals or providing credit support "
            "in violation of regulations are held accountable in accordance "
            "with law."
        ),
        "Compliance promotion": (
            "Credit support; Tax preferences; "
            "Land policy preferences"
        ),
        "Compliance promotion detail": (
            "Encouraged-category projects enjoy preferential policies in "
            "credit, tax and land. Enterprises are encouraged to upgrade "
            "Restricted-category capacity to Encouraged category through "
            "technological transformation. Financial institutions provide "
            "priority credit support to Encouraged-category projects on "
            "market-based principles. Enterprises are encouraged to "
            "eliminate backward capacity and receive elimination "
            "compensation or capacity indicator trading revenue in "
            "accordance with laws and regulations."
        ),
        "Mitigation co-benefits": (
            "Energy efficiency improvement; Energy consumption reduction; "
            "Air pollutant emission reduction; Technological innovation; "
            "Green industry development"
        ),
        "Mitigation effects": "Positive",
        "Legal statute": (
            "Industrial Structure Adjustment Guidance Catalogue (2024 "
            "edition) (National Development and Reform Commission "
            "Order No. 7)"
        ),
        "Last revisions (Details)": (
            "On 27 December 2023, NDRC issued the Industrial Structure "
            "Adjustment Guidance Catalogue (2024 edition) (NDRC Order No. 7), "
            "effective 1 February 2024, simultaneously repealing the 2019 "
            "edition. The 2024 edition contains 1,005 entries: 352 Encouraged, "
            "231 Restricted and 422 Eliminated. Compared with the 2019 "
            "edition, Encouraged entries newly added categories such as "
            "intelligent manufacturing, CNC machine tools and cybersecurity; "
            "Eliminated entries newly added high-energy-consuming backward "
            "electromechanical equipment and backward steel plants. Previous "
            "editions: 2005 edition (SC [2005] No. 40, first issuance), "
            "2011 edition, 2013 edition (amended), 2019 edition (amended "
            "2021)."
        ),
        "Other weblinks": (
            "Decision of the State Council on Issuing and Implementing the "
            "Interim Provisions on Promoting Industrial Structural "
            "Adjustment (SC [2005] No. 40): "
            "https://www.gov.cn/gongbao/content/2005/content_130166.htm"
        ),
    },
"""


def main():
    text = TARGET.read_text(encoding="utf-8")
    # Find the ROW_TRANSLATIONS closing brace
    marker = "\n}\n\ndef load_cn_to_en_headers"
    pos = text.find(marker)
    if pos == -1:
        print("ERROR: Could not find insertion point")
        return 1
    new_text = text[:pos] + NEW_ENTRIES + "\n" + text[pos:]
    TARGET.write_text(new_text, encoding="utf-8")
    print(f"Inserted 6 entries into {TARGET}")
    # Verify syntax
    import ast
    ast.parse(new_text)
    print("Syntax check passed")


if __name__ == "__main__":
    raise SystemExit(main())
