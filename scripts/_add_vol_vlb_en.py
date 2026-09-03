#!/usr/bin/env python3
"""Insert VLB instruments into the Voluntary EN CSV."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_en_voluntary_approaches.csv"
DATA_PATH = Path(__file__).resolve().parent / "_vlb_data.json"

EN_HEADER = [
    "Policy Instrument ID", "Instrument / subscheme", "Group", "Approach",
    "Emission sector", "Sub-sector", "Domestic name", "English name",
    "Policy Package", "Description", "Objective",
    "Mitigation relevance", "Functioning channel",
    "Country", "Jurisdiction level", "Jurisdiction name",
    "Adoption date", "Start date", "End date",
    "Last revisions", "Last revisions (Details)", "Status",
    "Administrating authorities", "Asset", "Asset (Status)",
    "Asset (Details)", "Asset (Other)",
    "Asset (Cut-off range)", "Agent",
    "Agent (Detail)", "Activity",
    "Activity (Details)", "Intensity (Value)",
    "Intensity (Unit)", "Intensity (Details)", "Requirement specification",
    "Compliance calculation methodology I", "Compliance calculation methodology II",
    "Incentives for Participation", "Monitoring",
    "Sanctions for non-compliance",
    "GHG emission coverage (absolute)",
    "GHG emission coverage (% domestic emissions)",
    "Economic sector", "GHGs affected", "Mitigation effect",
    "Mitigation co-benefits", "Legal statute",
    "Legal document", "Other weblinks",
]

MITIGATION_MAP = {"直接": "Direct", "间接": "Indirect"}
CHANNEL_MAP = {"环境": "Environment", "供给侧": "Supply-side"}
STATUS_MAP = {"生效": "In force"}
SECTOR_MAP = {"跨部门": "Cross-sectoral", "建筑": "Buildings"}
AGENT_MAP = {"企业": "Firms"}
ACTIVITY_MAP = {"注册、许可及行政管理": "Registration, licensing or other administrative tasks"}
COBENEFITS_MAP = {
    "能效提升": "Energy efficiency improvement",
    "能源消耗减少": "Energy consumption reduction",
    "空气污染物减排": "Air pollutant emission reduction",
    "技术创新": "Technological innovation",
    "绿色产业发展": "Green industry development",
    "污染防治": "Pollution control",
    "资源节约": "Resource conservation",
    "循环经济": "Circular economy",
    "生态保护": "Ecological protection",
    "水资源节约": "Water resource conservation",
    "公众健康": "Public health",
}

# Per-instrument English translations (text fields only)
TR = {
    "CHNVIIVLBI01S000": {
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
        "Last revisions (Details)": (
            "The system traces back to 11 February 1999 when the China "
            "Energy-Saving Product Certification Administrative Measures "
            "(State Economic and Trade Commission) established the "
            "energy-saving product certification system. On 19 February 2013, "
            "the Interim Administrative Measures for Low-Carbon Product "
            "Certification (NDRC Climate [2013] No. 279, jointly issued by "
            "NDRC and CNCA) established the low-carbon product certification "
            "system. In 2016, the General Office of the State Council issued "
            "the Opinions on Establishing a Unified Green Product Standard, "
            "Certification and Labelling System (Guobanfa [2016] No. 86), "
            "incorporating energy-saving and low-carbon product certification "
            "into the unified green product labelling system framework. On "
            "23 September 2022, the General Office of the State Council "
            "issued the Opinions on Deepening the Reform of the Management "
            "System for the Electronic and Electrical Appliances Industry "
            "(Guobanfa [2022] No. 31), formally integrating the Energy-Saving "
            "Product Certification system and the Low-Carbon Product "
            "Certification system into a unified Energy-Saving and Low-Carbon "
            "Product Certification system, with SAMR leading the development "
            "of certification rules and relevant departments jointly "
            "developing standards."
        ),
        "Other weblinks": (
            "https://www.ndrc.gov.cn/fggz/hjyzy/stwmjs/200507/"
            "t20050711_1159582_ext.html; "
            "https://www.ndrc.gov.cn/xxgk/zcfb/tz/201303/"
            "t20130319_964565.html"
        ),
    },
    "CHNVIIVLBI02S000": {
        "Description": (
            "The Green Building Evaluation Label is a voluntary building "
            "evaluation and labelling system established and administered by the "
            "housing and urban-rural development authorities. Buildings are "
            "comprehensively assessed against the national Green Building "
            "Evaluation Standard across five performance categories — safety and "
            "durability, health and comfort, convenience of living, resource "
            "conservation, and environmental livability — over their full life "
            "cycle, and star-rated green building labels are awarded. Labels are "
            "divided into four grades: Basic, One-Star, Two-Star and Three-Star, "
            "with Three-Star being the highest. The evaluation covers land saving "
            "and outdoor environment, energy saving and energy utilisation, water "
            "saving and water resource utilisation, material saving and material "
            "resource utilisation, indoor environmental quality, and operations "
            "management, among which the energy saving and energy utilisation "
            "indicators directly produce a positive climate change mitigation "
            "effect. The Green Building Label system began in 2007, promulgated "
            "and implemented by the Ministry of Housing and Urban-Rural "
            "Development under the Administrative Measures for Green Building "
            "Labels (MOHURD Jianbiao Gui [2021] No. 1), with evaluation "
            "and certification based on the national standard GB/T 50378 Green "
            "Building Evaluation Standard. Project owners voluntarily apply; "
            "there are no mandatory compliance obligations or penalties."
        ),
        "Objective": "Promote green building development and reduce building-sector carbon emissions",
        "Admin authorities": (
            "Ministry of Housing and Urban-Rural Development (Department of "
            "Standard Quota); housing and urban-rural development authorities "
            "of each province, autonomous region and municipality directly "
            "under the central government"
        ),
        "Regulated asset": "Buildings (green building evaluation objects)",
        "Regulated asset (details)": (
            "The object defined and covered by this instrument is various types "
            "of civil buildings, including residential buildings and public "
            "buildings. The evaluation applies to building clusters, individual "
            "buildings or areas within buildings. The evaluation phases are "
            "divided into design evaluation and operation evaluation; design "
            "evaluation is conducted after the construction drawing design "
            "documents have been reviewed and approved, and operation evaluation "
            "is conducted after the building has been completed and put into "
            "use for one year or more. Evaluation is based on GB/T 50378 Green "
            "Building Evaluation Standard, and Basic, One-Star, Two-Star or "
            "Three-Star green building labels are awarded according to the "
            "comprehensive score."
        ),
        "Regulated agent (details)": (
            "Development and construction entities, design entities and "
            "operation and management entities of various types of civil "
            "building projects. Project construction entities or operation "
            "entities may voluntarily apply to the housing and urban-rural "
            "development authorities or accredited evaluation bodies for the "
            "green building evaluation label. Participation is voluntary, with "
            "no mandatory compliance obligations."
        ),
        "Regulated activity (details)": (
            "The activity regulated and guided by this instrument is the voluntary green building evaluation and label recognition process for building projects. Project construction or operation entities voluntarily apply to the housing and urban-rural development authorities or accredited evaluation bodies for the green building evaluation label, submitting an application form and supporting documentation; after expert review or formal examination, the corresponding star-rated label is awarded based on the comprehensive score under GB/T 50378 Green Building Evaluation Standard. The evaluation covers both the design phase and the operation phase. Participation is voluntary."
        ),
        "Requirement specification": (
            "1) The project applying must satisfy the basic requirements of the "
            "control items specified in GB/T 50378 Green Building Evaluation "
            "Standard; 2) The green building grade is determined according to "
            "the sum of scores of the scoring items: Basic, One-Star, Two-Star "
            "or Three-Star; 3) The evaluation content covers five performance "
            "categories: safety and durability, health and comfort, convenience "
            "of living, resource conservation and environmental livability; "
            "4) A green building label application form and relevant supporting "
            "documents must be submitted, and the label is awarded after expert "
            "review or formal examination; 5) Project owners voluntarily apply; "
            "there are no mandatory compliance obligations or penalties."
        ),
        "Incentives for Participation": (
            "Projects that obtain the green building label gain social "
            "recognition and enhanced market value; the national and local "
            "governments provide financial incentives for high-star-rated green "
            "buildings (e.g. operation label subsidies for Two-Star and "
            "Three-Star green buildings), tax incentives, floor area ratio "
            "bonuses and other incentive policies; green buildings are included "
            "in the scope of green finance support and may receive preferential "
            "loans and green bond support."
        ),
        "Monitoring": (
            "Buildings that have obtained the operation label must continuously "
            "meet the green building operation requirements; competent "
            "authorities conduct random inspections and supervision of labelled "
            "projects, and may require rectification or revoke the label if "
            "non-compliance is found; the validity period of a Three-Star green "
            "building label is three years, after which an application for "
            "renewal may be made."
        ),
        "Sanctions for non-compliance": (
            "N/A (voluntary building evaluation label; no non-compliance "
            "sanctions. Where falsification of application materials is "
            "discovered or operations no longer meet the requirements, the "
            "competent authority shall revoke the label.)"
        ),
        "GHG emissions coverage (absolute)": (
            "N/A (this instrument is a voluntary building evaluation and "
            "labelling tool; the amount of GHG emissions covered depends on the "
            "total amount of green building space voluntarily submitted for "
            "evaluation and awarded labels, and there is no directly "
            "quantifiable fixed coverage amount)"
        ),
        "GHG emissions coverage (% of domestic emissions)": (
            "N/A (this instrument is a voluntary tool; the share of GHG "
            "emissions covered depends on voluntary uptake)"
        ),
        "Mitigation co-benefits": (
            "Energy efficiency improvement; Energy consumption reduction; "
            "Water resource conservation; Pollution control; "
            "Ecological protection"
        ),
        "Legal statute": (
            "Notice of the Ministry of Housing and Urban-Rural Development on "
            "Issuing the Administrative Measures for Green Building Labels "
            "(MOHURD Jianbiao Gui [2021] No. 1)"
        ),
        "Last revisions (Details)": (
            "In 2019, GB/T 50378-2019 Green Building Evaluation Standard "
            "was revised (the original standard was first issued in 2006 "
            "and revised in 2014 and 2019 respectively), restructuring the "
            "evaluation indicator system with five core performance "
            "categories — safety and durability, health and comfort, "
            "convenience of living, resource conservation and environmental "
            "livability — and further strengthening building carbon emission "
            "calculation and renewable energy utilisation content. In 2021, "
            "the Ministry of Housing and Urban-Rural Development issued the "
            "Administrative Measures for Green Building Labels (MOHURD "
            "Jianbiao Gui [2021] No. 1), further standardising the "
            "management of label recognition and award."
        ),
        "Other weblinks": "N/A",
    },
    "CHNVIIVLBI04S000": {
        "Description": (
            "The Energy Efficiency Top-Runner Programme is a voluntary system "
            "established and implemented under the leadership of the National "
            "Development and Reform Commission. It periodically selects and "
            "publishes the top runners with the highest energy efficiency "
            "levels among end-use energy-consuming products, enterprises in "
            "high-energy-consuming industries and public institutions, and uses "
            "their energy efficiency levels as industry benchmarks and "
            "catch-up targets to guide the whole industry in energy efficiency "
            "benchmarking, target attainment and competition, thereby driving "
            "the continuous improvement of the overall energy efficiency of "
            "end-use energy-consuming products and high-energy-consuming "
            "industries. The programme was established under the Implementation "
            "Plan for the Energy Efficiency Top-Runner Programme (NDRC "
            "Environment and Resources [2014] No. 3001) and covers three "
            "categories: (1) Energy-consuming product top runners — products "
            "whose energy efficiency indicators reach or exceed the Grade 1 "
            "energy efficiency level of the national energy efficiency "
            "standards or the top-runner indicators, within a comparable "
            "category; (2) High-energy-consuming industry top runners — "
            "enterprises whose unit product energy consumption reaches the "
            "industry advanced level; (3) Public institution top runners — "
            "state organs, schools, hospitals and other public institutions "
            "whose energy and resource utilisation efficiency reaches an "
            "advanced level. The various top-runner lists are published by "
            "the competent government authorities following voluntary "
            "enterprise application, local recommendation, expert review and "
            "public notification, with a typical validity period of two years. "
            "Participation is voluntary, with no mandatory compliance "
            "obligations or penalties."
        ),
        "Objective": "Promote energy efficiency improvement",
        "Admin authorities": (
            "National Development and Reform Commission (Department of "
            "Resource Conservation and Environmental Protection); Ministry of "
            "Industry and Information Technology (Department of Energy "
            "Conservation and Comprehensive Utilisation); State Administration "
            "for Market Regulation (Department of Product Quality and Safety "
            "Supervision)"
        ),
        "Regulated asset": (
            "End-use energy-consuming products / high-energy-consuming "
            "enterprises / public institutions (energy efficiency top-runner "
            "designation objects)"
        ),
        "Regulated asset (details)": (
            "The object defined and covered by this instrument covers three "
            "categories: (1) End-use energy-consuming products, including "
            "household appliances, office equipment, lighting products and "
            "industrial equipment, with product energy efficiency indicators "
            "as the selection basis; (2) High-energy-consuming industry "
            "enterprises, including those in steel, cement, electrolytic "
            "aluminium, flat glass, oil refining, ethylene and synthetic "
            "ammonia, with unit product comprehensive energy consumption as "
            "the selection basis; (3) Public institutions (state organs, "
            "schools, hospitals, etc.), with per-unit-floor-area energy "
            "consumption and per-capita energy consumption as the selection "
            "basis. Top runners in each category are selected and published "
            "every two years."
        ),
        "Regulated agent (details)": (
            "Manufacturers of end-use energy-consuming products and "
            "enterprises in high-energy-consuming industries. Enterprises "
            "may voluntarily apply for top-runner status, submitting product "
            "energy efficiency test reports or unit product energy "
            "consumption data, and be selected following preliminary review, "
            "expert review and public notification. Public institutions may "
            "voluntarily apply for public institution top-runner status. "
            "Participation is voluntary, with no mandatory compliance "
            "obligations."
        ),
        "Regulated activity (details)": (
            "The activity regulated and guided by this instrument is the voluntary application, selection and publication process for energy efficiency top runners among end-use energy-consuming products, high-energy-consuming industry enterprises and public institutions. Enterprises or public institutions voluntarily submit application materials (product energy efficiency test reports or unit product energy consumption data); following local recommendation, expert review and public notification, the competent government authorities publish the top-runner list. The list is valid for approximately two years, after which re-selection takes place. Participation is voluntary."
        ),
        "Requirement specification": (
            "1) Energy-consuming products must reach or exceed the Grade 1 "
            "energy efficiency level of the national energy efficiency "
            "standards or the top-runner indicators; 2) The unit product "
            "energy consumption of high-energy-consuming industry enterprises "
            "must reach the industry advanced level; 3) Public institutions "
            "must reach the advanced level of energy and resource consumption "
            "for the corresponding category of public institutions; 4) "
            "Selection is through voluntary enterprise/public institution "
            "application, local recommendation, expert review and public "
            "notification; 5) The top-runner list is valid for approximately "
            "two years, after which re-selection takes place; 6) Participation "
            "is voluntary."
        ),
        "Incentives for Participation": (
            "Products selected as energy efficiency top runners may carry the "
            "energy efficiency top-runner mark on the product body and "
            "packaging; selected enterprises and public institutions receive "
            "national and local media publicity and promotion, enhancing brand "
            "image and industry influence; they receive priority "
            "recommendation for inclusion in the energy-saving product "
            "government procurement list; some localities provide "
            "commendation and financial awards to top-runner enterprises."
        ),
        "Monitoring": (
            "Selected top-runner products and enterprises are subject to "
            "dynamic management during the validity period; if the product "
            "energy efficiency or enterprise unit product energy consumption "
            "no longer meets the top-runner requirements, the top-runner "
            "qualification is revoked. The competent authorities organise "
            "third-party bodies to conduct supervisory inspections."
        ),
        "Sanctions for non-compliance": (
            "N/A (voluntary programme; no non-compliance sanctions. Those "
            "that no longer meet the top-runner conditions or are found to "
            "have engaged in falsification shall have their top-runner "
            "qualification revoked and be publicly announced.)"
        ),
        "GHG emissions coverage (absolute)": (
            "N/A (this instrument is a voluntary benchmarking programme; the "
            "amount of GHG emissions covered depends on the scale and extent "
            "of voluntary enterprise participation and energy efficiency "
            "improvement, and there is no directly quantifiable fixed coverage "
            "amount)"
        ),
        "GHG emissions coverage (% of domestic emissions)": (
            "N/A (this instrument is a voluntary tool; the share of GHG "
            "emissions covered depends on voluntary uptake)"
        ),
        "Mitigation co-benefits": (
            "Energy efficiency improvement; Energy consumption reduction; "
            "Technological innovation; Green industry development; "
            "Air pollutant emission reduction"
        ),
        "Legal statute": (
            "Notice on Issuing the Implementation Plan for the Energy "
            "Efficiency Top-Runner Programme (NDRC Environment and Resources "
            "[2014] No. 3001)"
        ),
        "Last revisions (Details)": (
            "On 31 December 2014, the NDRC and other departments issued the "
            "Implementation Plan for the Energy Efficiency Top-Runner Programme "
            "(NDRC Environment and Resources [2014] No. 3001), establishing "
            "the top-runner system covering three categories: end-use "
            "energy-consuming products, enterprises in high-energy-consuming "
            "industries and public institutions. Since implementation, "
            "multiple batches of top-runner enterprises in key industries and "
            "top-runner public institutions have been published. On 23 September "
            "2022, the General Office of the State Council issued the Opinions "
            "on Deepening the Reform of the Management System for the Electronic "
            "and Electrical Appliances Industry (Guobanfa [2022] No. 31), "
            "abolishing the energy efficiency top-runner product selection "
            "system (end-use energy-consuming products track); the enterprise "
            "and public institution top-runner selection continues. In the "
            "2023-2024 cycle, top-runner enterprise selection in key industries "
            "(MIIT Joint Energy Conservation [2023] No. 278, covering 37 "
            "sub-sectors) and public institution top-runner selection (National "
            "Government Offices Administration Energy Conservation [2023] "
            "No. 282) continued."
        ),
    },
    "CHNVIIVLBI05S000": {
        "Description": (
            "Green Product Certification is a unified green product "
            "certification and labelling system established and implemented "
            "under the unified deployment of the State Council, led by the "
            "State Administration for Market Regulation together with relevant "
            "departments. Based on the full-life-cycle assessment concept, "
            "products are comprehensively evaluated and certified across four "
            "dimensions — resource attributes, energy attributes, environmental "
            "attributes and quality attributes — and awarded the unified "
            "national green product label. The system originated from the 2016 "
            "Opinions of the General Office of the State Council on "
            "Establishing a Unified Green Product Standard, Certification and "
            "Labelling System (Guobanfa [2016] No. 86), which integrated the "
            "various environmental protection, energy-saving, water-saving, "
            "circular, low-carbon, recycled and organic product certifications "
            "previously dispersed among different authorities into a unified "
            "national green product certification and labelling system. The "
            "first batch of the green product certification catalogue covers "
            "categories such as wood-based panels and wooden flooring, "
            "coatings, sanitary ceramics, building glass, solar water heating "
            "systems, furniture, waterproof and sealing materials, ceramic "
            "tiles (slabs), textile products, paper and paper products, "
            "wood-plastic products, plastic products and washing products. "
            "Green building material product certification is included as a "
            "sub-category within the unified framework. Enterprises voluntarily "
            "apply for certification; there are no mandatory compliance "
            "obligations or penalties."
        ),
        "Objective": "Promote green production and consumption, and mitigate and adapt to climate change",
        "Admin authorities": (
            "State Administration for Market Regulation (Department of "
            "Certification Supervision); Certification and Accreditation "
            "Administration of the People's Republic of China; National "
            "Development and Reform Commission; Ministry of Industry and "
            "Information Technology; Ministry of Housing and Urban-Rural "
            "Development and other relevant departments"
        ),
        "Regulated asset": "Products (green product certification objects)",
        "Regulated asset (details)": (
            "The object defined and covered by this instrument is the various "
            "categories of products included in the green product certification "
            "catalogue, including but not limited to building materials "
            "(wood-based panels, coatings, sanitary ceramics, building glass, "
            "ceramic tiles, waterproof and sealing materials, etc.), furniture, "
            "textiles, paper products, plastic products, washing products and "
            "other categories. Certification is based on the green product "
            "evaluation standards for the corresponding product category, "
            "comprehensively evaluating products across four dimensions — "
            "resource attributes, energy attributes, environmental attributes "
            "and quality attributes — over their full life cycle."
        ),
        "Regulated agent (details)": (
            "Manufacturers and distributors of the various product categories "
            "covered by the green product certification catalogue. Enterprises "
            "may voluntarily apply to nationally accredited certification "
            "bodies for green product certification; upon product testing and "
            "factory inspection demonstrating compliance with the green "
            "product evaluation standards, they obtain the certification "
            "certificate and the right to use the label. Participation is "
            "voluntary."
        ),
        "Regulated activity (details)": (
            "The activity regulated and guided by this instrument is the voluntary green product certification and labelling process for products. Enterprises voluntarily submit green product certification applications to nationally accredited certification bodies; products must pass full-life-cycle assessment and meet green product evaluation standards across the four dimensions of resource attributes, energy attributes, environmental attributes and quality attributes; upon passing product testing and factory inspection, the green product certification certificate is issued and the right to use the unified national green product label is granted. After certification, enterprises must undergo annual supervisory inspections by the certification body. Participation is voluntary."
        ),
        "Requirement specification": (
            "1) Products must fall within the scope of the green product "
            "certification catalogue; 2) Products must pass full-life-cycle "
            "assessment and meet the requirements of the corresponding green "
            "product evaluation standards across the four dimensions of "
            "resource attributes, energy attributes, environmental attributes "
            "and quality attributes; 3) Enterprises must pass product testing "
            "and factory quality assurance capability inspection; 4) After "
            "certification, enterprises must undergo annual supervisory "
            "inspections by the certification body; 5) Certified products may "
            "carry the unified national green product label on the product and "
            "packaging; 6) Enterprises voluntarily apply for certification; "
            "there are no mandatory compliance obligations or penalties."
        ),
        "Incentives for Participation": (
            "Enterprises that obtain green product certification may use the "
            "unified national green product label on their products, enhancing "
            "product market competitiveness and consumer recognition; green "
            "products receive priority for inclusion in government green "
            "procurement catalogues and green building material government "
            "procurement projects; green product certification is linked with "
            "green finance policies, and certified enterprises and products may "
            "receive green credit and green bond support; green product "
            "designation is coordinated and linked with policies such as "
            "high-tech enterprise recognition and green factory evaluation."
        ),
        "Monitoring": (
            "Certified enterprises must undergo annual supervisory inspections "
            "and product sampling and testing by certification bodies to ensure "
            "continued compliance with green product evaluation standards; "
            "certification bodies may suspend or revoke the certification "
            "certificate for non-compliant products; market regulatory "
            "authorities and relevant industry authorities supervise "
            "certification activities."
        ),
        "Sanctions for non-compliance": (
            "N/A (voluntary certification label; no non-compliance sanctions. "
            "For products and enterprises that fail to pass supervisory "
            "inspections or do not continuously meet green product "
            "certification requirements, the certification body may suspend or "
            "revoke their certification certificate and the right to use the "
            "label; those engaging in falsification shall be pursued for legal "
            "liability in accordance with the law.)"
        ),
        "GHG emissions coverage (absolute)": (
            "N/A (this instrument is a voluntary certification and labelling "
            "tool; the amount of GHG emissions covered depends on the "
            "categories and quantity of products voluntarily certified by "
            "enterprises, and there is no directly quantifiable fixed coverage "
            "amount)"
        ),
        "GHG emissions coverage (% of domestic emissions)": (
            "N/A (this instrument is a voluntary tool; the share of GHG "
            "emissions covered depends on voluntary uptake)"
        ),
        "Mitigation co-benefits": (
            "Green industry development; Pollution control; "
            "Resource conservation; Circular economy; Public health"
        ),
        "Legal statute": (
            "Opinions of the General Office of the State Council on "
            "Establishing a Unified Green Product Standard, Certification and "
            "Labelling System (Guobanfa [2016] No. 86)"
        ),
        "Last revisions (Details)": (
            "In 2020, the State Administration for Market Regulation issued "
            "the Green Product Certification Catalogue, which was formally "
            "implemented after integration, further clarifying the scope of "
            "certified products and implementation rules."
        ),
    },
    "CHNVIIVLBI06S000": {
        "Description": (
            "The Nearly Zero Energy Building Label is a voluntary evaluation "
            "system for assessing and labelling building projects that meet "
            "the nearly zero energy building technical standards. Based on the "
            "national standard GB/T 51350-2019 Technical Standard for Nearly "
            "Zero Energy Buildings, it comprehensively assesses the indoor "
            "environmental parameters and energy efficiency indicators of "
            "buildings, awarding corresponding labels to ultra-low energy "
            "buildings, nearly zero energy buildings and zero energy buildings "
            "that meet the standards. Labels are divided into three grades: "
            "ultra-low energy building (energy saving rate of 82%-85% or "
            "above), nearly zero energy building (energy saving rate of "
            "86%-90% or above) and zero energy building (annual renewable "
            "energy generation greater than or equal to the building's own "
            "annual final energy consumption). Assessment indicators include "
            "building energy efficiency indicators (building envelope energy "
            "saving rate, comprehensive building energy saving rate, renewable "
            "energy utilisation rate) and indoor environmental parameters "
            "(temperature, humidity, fresh air volume, noise, etc.), verified "
            "through building energy simulation calculations and on-site "
            "testing. The system was promoted and established by the housing "
            "and urban-rural development authorities and the building energy "
            "conservation associations, and formally came into operation after "
            "the implementation of the national standard GB/T 51350-2019 in "
            "2019. Project owners voluntarily apply; there are no mandatory "
            "compliance obligations or penalties."
        ),
        "Objective": "Promote deep energy conservation and near-zero carbon emissions in the building sector",
        "Admin authorities": (
            "Ministry of Housing and Urban-Rural Development (Department of "
            "Standard Quota); China Association of Building Energy Efficiency "
            "and other authorised assessment bodies"
        ),
        "Regulated asset": "Buildings (nearly zero energy building evaluation objects)",
        "Regulated asset (details)": (
            "The object defined and covered by this instrument is the various "
            "types of new, renovated and expanded civil buildings, including "
            "residential buildings and public buildings. Evaluation is based "
            "on GB/T 51350-2019 Technical Standard for Nearly Zero Energy "
            "Buildings, and buildings are classified as ultra-low energy, "
            "nearly zero energy or zero energy according to indicators such "
            "as building envelope energy saving rate, comprehensive building "
            "energy saving rate and renewable energy utilisation rate. "
            "Evaluation applies to both the design phase and the operation "
            "phase."
        ),
        "Regulated agent (details)": (
            "Development and construction entities, design entities and "
            "operation and management entities of various types of civil "
            "building projects. Project entities may voluntarily apply to "
            "authorised assessment bodies for nearly zero energy building "
            "assessment and labelling, and obtain the corresponding grade of "
            "label after building energy simulation analysis, on-site testing "
            "and expert review. Participation is voluntary."
        ),
        "Regulated activity (details)": (
            "The activity regulated and guided by this instrument is the voluntary nearly zero energy building assessment and label recognition process for building projects. Project entities voluntarily apply to authorised assessment bodies for nearly zero energy building assessment, submitting building energy simulation calculation reports and on-site testing data; after expert review, the building is classified as ultra-low energy, nearly zero energy or zero energy according to the energy efficiency indicators of GB/T 51350-2019 Technical Standard for Nearly Zero Energy Buildings, and the corresponding label is awarded. The evaluation applies to both the design phase and the operation phase. Participation is voluntary."
        ),
        "Requirement specification": (
            "1) The building must meet the indoor environmental parameter and "
            "energy efficiency indicator requirements of GB/T 51350-2019 "
            "Technical Standard for Nearly Zero Energy Buildings; 2) Ultra-low "
            "energy building: comprehensive building energy saving rate of "
            "82%-85% or above; 3) Nearly zero energy building: comprehensive "
            "building energy saving rate of 86%-90% or above; 4) Zero energy "
            "building: annual renewable energy generation greater than or "
            "equal to the building's own annual final energy consumption; "
            "5) Verification through building energy simulation calculations "
            "and on-site testing is required; 6) Project owners voluntarily "
            "apply; there are no mandatory compliance obligations or penalties."
        ),
        "Incentives for Participation": (
            "Projects that obtain the nearly zero energy building label gain "
            "social recognition and enhanced market value; national and local "
            "governments provide fiscal subsidies for ultra-low energy and "
            "nearly zero energy buildings (e.g. Beijing, Hebei, Shandong and "
            "other localities provide subsidies of several hundred yuan per "
            "square metre for ultra-low energy buildings) and floor area ratio "
            "bonuses; nearly zero energy buildings are included in the scope "
            "of green finance support."
        ),
        "Monitoring": (
            "Buildings that have obtained the label must continuously meet the "
            "nearly zero energy building operation requirements; assessment "
            "bodies conduct periodic follow-up evaluations of labelled "
            "projects, and may revoke the label if they find that the "
            "requirements are no longer met. Project entities are encouraged "
            "to conduct continuous monitoring and public disclosure of the "
            "building's actual operational energy consumption."
        ),
        "Sanctions for non-compliance": (
            "N/A (voluntary building evaluation label; no non-compliance "
            "sanctions. Where falsification of application materials is "
            "discovered or operations no longer meet the requirements, the "
            "assessment body shall revoke the label.)"
        ),
        "GHG emissions coverage (absolute)": (
            "N/A (this instrument is a voluntary building evaluation and "
            "labelling tool; the amount of GHG emissions covered depends on "
            "the total amount of nearly zero energy building space voluntarily "
            "submitted for evaluation and awarded labels, and there is no "
            "directly quantifiable fixed coverage amount)"
        ),
        "GHG emissions coverage (% of domestic emissions)": (
            "N/A (this instrument is a voluntary tool; the share of GHG "
            "emissions covered depends on voluntary uptake)"
        ),
        "Mitigation co-benefits": (
            "Energy efficiency improvement; Energy consumption reduction; "
            "Air pollutant emission reduction; Technological innovation"
        ),
        "Legal statute": (
            "Announcement of the Ministry of Housing and Urban-Rural "
            "Development on Issuing the National Standard Technical Standard "
            "for Nearly Zero Energy Buildings (MOHURD Announcement [2019] "
            "No. 22, GB/T 51350-2019)"
        ),
    },
    "CHNVIIVLBI07S000": {
        "Description": (
            "The Product Carbon Footprint Label Certification is a voluntary "
            "product carbon footprint labelling and certification system "
            "jointly established and implemented by the State Administration "
            "for Market Regulation and other departments. Based on product "
            "carbon footprint accounting standards and certification "
            "specifications, the full-life-cycle GHG emissions of products — "
            "from raw material acquisition, manufacturing, distribution and "
            "transport, use and consumption to disposal and recycling — are "
            "quantified, verified and labelled, conveying product carbon "
            "emission information to consumers and purchasers through a "
            "unified carbon footprint label and guiding low-carbon consumption "
            "and low-carbon production. The system was established under the "
            "Notice on Launching the Pilot Programme for Product Carbon "
            "Footprint Label Certification (Guoshijian Ren Zhengfa [2024] "
            "No. 85) jointly issued by the State Administration for Market "
            "Regulation, the Ministry of Ecology and Environment, the National "
            "Development and Reform Commission and the Ministry of Industry "
            "and Information Technology in August 2024. The pilot covers 11 "
            "priority product categories — lithium batteries, photovoltaic "
            "products, steel, textiles, electronic and electrical appliances, "
            "tyres, cement, electrolytic aluminium, urea, ammonium phosphate "
            "and wood products — with a pilot period of three years. The "
            "certification and labelling system covers two labelling forms: "
            "carbon footprint quantification labels and carbon footprint grade "
            "labels. Enterprises voluntarily apply for certification; there are "
            "no mandatory compliance obligations or penalties."
        ),
        "Objective": "Mitigate climate change (promote carbon footprint transparency and low-carbon consumption)",
        "Admin authorities": (
            "State Administration for Market Regulation (Department of "
            "Certification Supervision); Ministry of Ecology and Environment; "
            "National Development and Reform Commission; Ministry of Industry "
            "and Information Technology"
        ),
        "Regulated asset": "Products (carbon footprint label certification objects)",
        "Regulated asset (details)": (
            "The object defined and covered by this instrument is the various "
            "categories of products included in the carbon footprint label "
            "certification catalogue. The near-term focus is on key-industry "
            "products with urgent carbon footprint data needs, such as "
            "batteries, photovoltaic products, electronic and electrical "
            "appliances, textiles, steel, non-ferrous metals and building "
            "materials. Certification is based on the product carbon footprint "
            "accounting general rules and product-category-specific carbon "
            "footprint accounting rules, quantifying and labelling the "
            "full-life-cycle GHG emissions of products (raw material "
            "acquisition, manufacturing, distribution and transport, use and "
            "consumption, disposal and recycling)."
        ),
        "Regulated agent (details)": (
            "Manufacturers and brand owners of the various product categories "
            "covered by the product carbon footprint label certification "
            "catalogue. Enterprises may voluntarily apply to nationally "
            "accredited certification bodies for product carbon footprint "
            "label certification; upon full-life-cycle carbon footprint "
            "quantification and third-party verification, they obtain the "
            "certification certificate and the right to use the label. "
            "Participation is voluntary."
        ),
        "Regulated activity (details)": (
            "The activity regulated and guided by this instrument is the voluntary product carbon footprint label certification and labelling process for products. Enterprises voluntarily submit product carbon footprint label certification applications to nationally accredited certification bodies; the full-life-cycle GHG emissions of the product are quantified in accordance with the carbon footprint accounting general rules and product-category accounting rules; after verification by a third-party verification body, the carbon footprint label certification certificate is issued and the right to use the carbon footprint label is granted. After certification, enterprises must undergo supervisory inspections and data update verification by the certification body. Participation is voluntary."
        ),
        "Requirement specification": (
            "1) Products must fall within the scope of the carbon footprint "
            "label certification catalogue; 2) Products must complete "
            "full-life-cycle GHG emission accounting in accordance with the "
            "carbon footprint accounting general rules and product-category "
            "accounting rules; 3) The carbon footprint accounting must be "
            "verified by a nationally accredited third-party verification "
            "body; 4) After certification, enterprises must undergo "
            "supervisory inspections and data update requirements by the "
            "certification body; 5) Certified products may carry the carbon "
            "footprint label on the product body, packaging or electronic "
            "platforms; 6) Enterprises voluntarily apply for certification; "
            "there are no mandatory compliance obligations or penalties."
        ),
        "Incentives for Participation": (
            "Enterprises that obtain carbon footprint label certification may "
            "use the carbon footprint label on their products, meeting "
            "downstream customer and end-consumer demand for product carbon "
            "emission information and enhancing the international "
            "competitiveness of products; products with excellent carbon "
            "emission performance may obtain a carbon footprint grade label "
            "(e.g. low-carbon grade), gaining market differentiation "
            "advantages; the system is linked with green finance, green "
            "procurement, carbon inclusion and other policies; it helps "
            "enterprises respond to international carbon border adjustment "
            "mechanisms and green trade rule requirements."
        ),
        "Monitoring": (
            "Certified enterprises must undergo periodic supervisory "
            "inspections and carbon footprint data update verification by "
            "certification bodies; when the product carbon footprint changes "
            "significantly (e.g. due to process improvements or supply chain "
            "changes), the accounting data and label information must be "
            "updated; certification bodies and market regulatory authorities "
            "supervise carbon footprint label certification activities."
        ),
        "Sanctions for non-compliance": (
            "N/A (voluntary certification label; no non-compliance sanctions. "
            "For products and enterprises that fail to pass supervisory "
            "inspections, have false carbon footprint data or do not "
            "continuously meet certification requirements, the certification "
            "body may suspend or revoke their certification certificate and "
            "the right to use the label.)"
        ),
        "GHG emissions coverage (absolute)": (
            "N/A (this instrument is a voluntary certification and labelling "
            "tool; the amount of GHG emissions covered depends on the "
            "categories and quantity of products voluntarily certified by "
            "enterprises as well as the magnitude of product carbon "
            "footprints and emission reductions, and there is no directly "
            "quantifiable fixed coverage amount)"
        ),
        "GHG emissions coverage (% of domestic emissions)": (
            "N/A (this instrument is a voluntary tool; the share of GHG "
            "emissions covered depends on voluntary uptake)"
        ),
        "Mitigation co-benefits": (
            "Technological innovation; Green industry development; "
            "Energy consumption reduction"
        ),
        "Legal statute": (
            "Notice of the State Administration for Market Regulation and "
            "Other Departments on Launching the Pilot Programme for Product "
            "Carbon Footprint Label Certification (Guoshijian Ren Zhengfa "
            "[2024] No. 85)"
        ),
    },
}


def _load_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def _write_rows(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def make_en_row(inst, tr):
    """Build an EN row from CN JSON data + English translations."""
    def _(cn_key, fallback="N/A"):
        return tr.get(cn_key, fallback)

    co_cn = inst["co_benefits"]
    co_parts = [c.strip() for c in co_cn.split("；")]
    co_en_parts = [COBENEFITS_MAP.get(c, c) for c in co_parts]
    co_en = "; ".join(co_en_parts)

    asset_status = inst.get("asset_status", "N/A")
    asset_status_en = {"新建": "New", "既有": "Existing", "新建；既有": "New; existing", "N/A": "N/A"}.get(asset_status, asset_status)

    return [
        inst["pid"],                                           # Policy Instrument ID
        "Instrument",                                          # Instrument / subscheme
        "Voluntary information instrument",                   # Group
        "Voluntary certification and labelling scheme",        # Approach
        SECTOR_MAP.get(inst["sector"], inst["sector"]),        # Emission sector
        inst["subsector"],                                     # Sub-sector
        inst["name_cn"],                                       # Domestic name
        inst["name_en"],                                       # English name
        inst["policy_package"],                                # Policy Package
        _("Description"),                                      # Description
        _("Objective"),                                        # Objective
        MITIGATION_MAP.get(inst["mitigation"], inst["mitigation"]),  # Mitigation relevance
        CHANNEL_MAP.get(inst["channel"], inst["channel"]),     # Functioning channel
        "CHN",                                                  # Country
        "National",                                            # Jurisdiction level
        "N/A",                                                 # Jurisdiction name
        inst["adoption"],                                      # Adoption date
        inst["effective"],                                     # Start date
        "N/A",                                                 # End date
        inst["revision"],                                      # Last revisions
        _("Last revisions (Details)", inst["revision_detail"]),  # Last revisions (Details)
        STATUS_MAP.get(inst["status"], inst["status"]),        # Status
        _("Admin authorities"),                                # Administrating authorities
        _("Regulated asset"),                                  # Asset
        asset_status_en,                                       # Asset (Status)
        _("Regulated asset (details)"),                        # Asset (Details)
        "N/A",                                                 # Asset (Other)
        "N/A",                                                 # Asset (Cut-off range)
        AGENT_MAP.get(inst["agent"], inst["agent"]),           # Agent
        _("Regulated agent (details)"),                        # Agent (Detail)
        ACTIVITY_MAP.get(inst["activity"], inst["activity"]),  # Activity
        _("Regulated activity (details)"),                     # Activity (Details)
        inst["intensity_val"],                                 # Intensity (Value)
        inst["intensity_unit"],                                # Intensity (Unit)
        inst["intensity_detail"],                              # Intensity (Details)
        _("Requirement specification"),                        # Requirement specification
        inst["calc_i"],                                        # Compliance calculation methodology I
        inst["calc_ii"],                                       # Compliance calculation methodology II
        _("Incentives for Participation"),                     # Incentives for Participation
        _("Monitoring"),                                       # Monitoring
        _("Sanctions for non-compliance"),                     # Sanctions for non-compliance
        _("GHG emissions coverage (absolute)"),                # GHG emission coverage (absolute)
        _("GHG emissions coverage (% of domestic emissions)"), # GHG emission coverage (% domestic emissions)
        inst["isic"],                                          # Economic sector
        inst["ghg"],                                           # GHGs affected
        "Positive",                                            # Mitigation effect
        co_en,                                                 # Mitigation co-benefits
        _("Legal statute"),                                    # Legal statute
        inst["legal_url"],                                     # Legal document
        _("Other weblinks"),                                   # Other weblinks
    ]


def main():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        instruments = json.load(f)

    rows = []
    for inst in instruments:
        pid = inst["pid"]
        tr = TR.get(pid, {})
        row = make_en_row(inst, tr)
        if len(row) != 50:
            print(f"ERROR: {pid} has {len(row)} columns, expected 50")
            return 1
        rows.append(row)

    if CSV_PATH.exists():
        existing = _load_rows(CSV_PATH)
        header, data = existing[0], existing[1:]
    else:
        header = EN_HEADER
        data = []

    inserted = 0
    updated = 0
    for row in rows:
        pid = row[0]
        # Find by domestic name match (PID is CN-only in EN CSV... no, EN CSV has PID)
        # Match by PID (first column)
        existing_idx = next((i for i, r in enumerate(data) if r and r[0] == pid), None)
        if existing_idx is not None:
            if data[existing_idx] != row:
                data[existing_idx] = row
                updated += 1
                print(f"  Updated {pid} in place at data index {existing_idx}")
            else:
                print(f"  {pid} already up to date -- skipping")
            continue

        # Insert after last VLB row (Voluntary certification and labelling scheme)
        insert_pos = len(data)
        for i in range(len(data)):
            if data[i] and data[i][2] == "Voluntary certification and labelling scheme":
                insert_pos = i + 1

        data.insert(insert_pos, row)
        inserted += 1
        print(f"  Inserted {pid} at data index {insert_pos}")

    data = [r for r in data if any(r)]
    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted, {updated} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
