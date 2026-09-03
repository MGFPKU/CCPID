"""Insert English rows for 2 new VLB + 2 new VID instruments into EN Voluntary CSV.

Run from repo root:
    python scripts/_add_vol_new_en.py
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_en_voluntary_approaches.csv"


def make_en_row(pid, instrument, group, approach, sector, subsector,
                domestic_name, english_name, policy_package, description,
                objective, mitigation, channel, country, jurisdiction,
                jurisdiction_name, adoption, effective, end_date,
                last_revision, last_revision_detail, status,
                admin_authorities, asset, asset_status, asset_detail,
                asset_other, asset_cutoff, agent, agent_detail,
                activity, activity_detail, intensity_val, intensity_unit,
                intensity_detail, req_spec, calc_i, calc_ii,
                incentives, monitoring, sanctions,
                ghg_abs, ghg_pct, isic, ghg,
                mitigation_effect, co_benefits, legal_name, legal_url, other_links):
    return [
        pid, instrument, group, approach, sector, subsector,
        domestic_name, english_name, policy_package, description,
        objective, mitigation, channel, country, jurisdiction,
        jurisdiction_name, adoption, effective, end_date,
        last_revision, last_revision_detail, status,
        admin_authorities, asset, asset_status, asset_detail,
        asset_other, asset_cutoff, agent, agent_detail,
        activity, activity_detail, intensity_val, intensity_unit,
        intensity_detail, req_spec, calc_i, calc_ii,
        incentives, monitoring, sanctions,
        ghg_abs, ghg_pct, isic, ghg,
        mitigation_effect, co_benefits, legal_name, legal_url, other_links,
    ]


ROWS = [
    # ── VLB 08: Green Bond Label ──
    make_en_row(
        pid="CHNVIIVLBI08S000",
        instrument="Instrument",
        group="Voluntary information instrument",
        approach="Voluntary certification and labelling scheme",
        sector="Cross-sectoral",
        subsector="N/A",
        domestic_name="绿色债券标识",
        english_name="Green Bond Label",
        policy_package="N/A",
        description=(
            "The Green Bond Label is a voluntary green bond assessment, certification and labelling system jointly established by the People's Bank of China (PBC) and the China Securities Regulatory Commission (CSRC), established under the Green Bond Assessment and Certification Conduct Guidelines (Interim) (PBC and CSRC Announcement [2017] No. 20). Through third-party assessment and certification bodies that evaluate bond proceeds utilisation, project screening and fund management against green bond criteria, a unified Green Bond Label is awarded to products meeting green bond standards, providing investors with a basis for identifying and assessing green bonds and promoting standardised development of the green bond market. The labelling system covers green financial bonds, green enterprise bonds, green corporate bonds, green debt financing instruments and green asset-backed securities. In 2021, the PBC, NDRC and CSRC jointly issued the Green Bond Endorsed Project Catalogue (2021 Edition) (Yinfa [2021] No. 96), unifying the definitional standards for green bond eligible projects. On 29 July 2022, the Green Bond Standard Committee issued the China Green Bond Principles (Announcement [2022] No. 1), requiring 100% of proceeds to be used for green projects, further aligning with international green bond standards. In 2025, the PBC, NFRA and CSRC jointly issued the Green Finance Endorsed Project Catalogue (2025 Edition) (Yinfa [2025] No. 132, effective 1 October 2025), unifying the project classification standards for green loans, green bonds and other green finance products, expanding the catalogue from six major categories in the 2021 edition to nine domains, and adding NBS economic sector classification codes and GHG emission reduction benefit attribute tags. Issuers voluntarily apply for green bond assessment and certification; there are no mandatory compliance obligations or penalties."
        ),
        objective="Promote standardised development of the green bond market and steer capital towards green and low-carbon fields",
        mitigation="Indirect",
        channel="Environment",
        country="CHN",
        jurisdiction="National",
        jurisdiction_name="N/A",
        adoption="26/10/2017",
        effective="28/12/2017",
        end_date="N/A",
        last_revision="01/10/2025",
        last_revision_detail=(
            "On 28 December 2017, the PBC and CSRC jointly issued the Green Bond Assessment "
            "and Certification Conduct Guidelines (Interim) (Announcement [2017] No. 20), "
            "establishing the institutional framework for green bond assessment, certification "
            "and labelling management. On 2 April 2021, the PBC, NDRC and CSRC jointly issued "
            "the Green Bond Endorsed Project Catalogue (2021 Edition) (Yinfa [2021] No. 96, "
            "effective 1 July 2021), which unified the definitional standards for green bond "
            "eligible projects. On 29 July 2022, the Green Bond Standard Committee issued the "
            "China Green Bond Principles (Announcement [2022] No. 1), establishing the core "
            "requirement that 100% of proceeds be used for green projects. On 27 June 2025, "
            "the PBC, NFRA and CSRC jointly issued the Green Finance Endorsed Project Catalogue "
            "(2025 Edition) (Yinfa [2025] No. 132, effective 1 October 2025), unifying green "
            "loan and green bond standards into a nine-domain catalogue and adding NBS economic "
            "sector classification codes and GHG emission reduction benefit attribute tags."
        ),
        status="In force",
        admin_authorities=(
            "People's Bank of China (Financial Market Department); China Securities Regulatory Commission (Department of Corporate Bond Supervision); National Development and Reform Commission (Department of Fiscal, Financial and Credit Construction)"
        ),
        asset="Green bonds (certification and labelling objects)",
        asset_status="New; Existing",
        asset_detail=(
            "The objects defined and covered by this instrument are various categories of green bonds, including green financial bonds, green enterprise bonds, green corporate bonds, green debt financing instruments and green asset-backed securities. Bonds must meet the green project classification standards set out in the Green Bond Endorsed Project Catalogue, with proceeds used exclusively to support eligible green industries, green projects or green economic activities, and must be assessed and certified by a third-party assessment and certification body before obtaining the Green Bond Label."
        ),
        asset_other="N/A",
        asset_cutoff="N/A",
        agent="Firms",
        agent_detail=(
            "Issuers and lead underwriters of green bonds. Issuers may voluntarily engage an accredited third-party assessment and certification body to conduct green bond assessment and certification; those meeting green bond standards upon assessment and certification may use the Green Bond Label in the bond name and offering documents, and must conduct ongoing information disclosure during the bond's life. Participation is voluntary, with no mandatory compliance obligations."
        ),
        activity="Registration, licensing or other administrative tasks",
        activity_detail=(
            "The activity regulated and guided by this instrument is the voluntary green bond assessment, certification and labelling process. Issuers voluntarily engage third-party assessment and certification bodies to assess and certify the direction and management system for bond proceeds use, project assessment and screening criteria and decision-making processes, and information disclosure and reporting systems, among other matters. Issuers whose bonds meet green bond standards upon assessment and certification may use the green label in the full bond name and register and display the bond on the CFETS green bond section and the SSE/SZSE G-labelling system. Registered green bonds must conduct ongoing annual information disclosure during their life. Participation is voluntary."
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1) Bond proceeds must be used exclusively to support green industries, green projects or green economic activities that meet the Green Bond Endorsed Project Catalogue; 2) Issuers must engage a third-party assessment and certification body to conduct pre-issuance assessment and certification of the bond; 3) Annual green bond information disclosure must be conducted during the bond's life, with ongoing tracking of proceeds use and project progress; 4) Third-party assessment and certification bodies must possess the prescribed qualification requirements, with at least five project experiences in green bond assessment and certification; 5) Bonds that pass assessment and certification may use the Green Bond Label in their full name; 6) Issuers voluntarily apply for assessment and certification; there are no mandatory compliance obligations or penalties."
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "Issuers that obtain the Green Bond Label gain enhanced market recognition and investor trust, attracting ESG investors and green investors; green bonds enjoy green bond sections and label displays in the interbank market and stock exchanges, enhancing trading convenience and market visibility; some localities provide interest subsidies, guarantees and other policy support to green bond issuers and investors; green bonds are included in the green finance performance evaluation of financial institutions."
        ),
        monitoring=(
            "Issuers must conduct ongoing annual information disclosure during the life of the green bond, publicly disclosing proceeds use, green project progress and environmental benefits; third-party assessment and certification bodies must conduct tracking assessments of the bond's continuous compliance with green bond standards; the PBC, CSRC and NDRC supervise the operation of the green bond market and the professional quality of assessment and certification bodies; the Green Bond Standard Committee exercises self-regulatory management."
        ),
        sanctions=(
            "N/A (voluntary certification label; no non-compliance sanctions. For issuers that no longer meet green bond standards during the bond's life or breach information disclosure requirements, the relevant regulatory authority shall take supervisory measures in accordance with its authority. For assessment and certification bodies with non-compliant conduct, the PBC and CSRC shall handle the matter in accordance with regulations.)"
        ),
        ghg_abs=(
            "N/A (this instrument is a voluntary bond labelling tool; the amount of GHG emissions covered depends on the scale of green bonds voluntarily labelled by issuers and the emission reduction effects of the green projects supported, and there is no directly quantifiable fixed coverage amount)"
        ),
        ghg_pct="N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        isic="K64",
        ghg="CO2; CH4; N2O",
        mitigation_effect="Positive",
        co_benefits="Green industry development; Technological innovation; Energy consumption reduction; Pollution control",
        legal_name="Announcement of the People's Bank of China and the China Securities Regulatory Commission ([2017] No. 20) — Green Bond Assessment and Certification Conduct Guidelines (Interim)",
        legal_url="https://www.gov.cn/gongbao/content/2018/content_5271800.htm",
        other_links=(
            "https://www.gov.cn/zhengce/zhengceku/2021-04/22/content_5601284.htm"
            ";https://www.nafmii.org.cn/xhdt/202207/t20220729_255959.html"
            ";https://www.gov.cn/zhengce/zhengceku/202507/content_7032004.htm"
        ),
    ),

    # ── VLB 09: Sustainability-Linked Bond Label ──
    make_en_row(
        pid="CHNVIIVLBI09S000",
        instrument="Instrument",
        group="Voluntary information instrument",
        approach="Voluntary certification and labelling scheme",
        sector="Cross-sectoral",
        subsector="N/A",
        domestic_name="可持续发展挂钩债券标识",
        english_name="Sustainability-Linked Bond Label",
        policy_package="N/A",
        description=(
            "The Sustainability-Linked Bond (SLB) Label is a voluntary bond labelling system established by the National Association of Financial Market Institutional Investors (NAFMII), which links bond terms to the issuer's sustainability development targets. Bonds meeting SLB requirements may add the special designation '(Sustainability-Linked)' to their full name upon registration and issuance. The system was established under the Sustainability-Linked Bond (SLB) Ten Questions and Answers published by NAFMII on 28 April 2021, drawing on the ICMA Sustainability-Linked Bond Principles while incorporating domestic self-regulatory rules. Through the setting of Key Performance Indicators (KPIs) and Sustainability Performance Targets (SPTs), SLBs link bond structure features (such as coupon step-up/step-down, early redemption, one-time additional payments, etc.) to the achievement of the issuer's sustainability targets, locking in the enterprise's overall emission reduction or sustainability commitments through bond structure design and pressing enterprises to achieve sustainability in a planned manner. Proceeds may be used for general purposes without special restrictions. On 10 October 2024, NAFMII issued the Notice on Further Optimising Mechanisms for Green and Transition Bonds, further enriching the design of linked targets, encouraging integration with ESG, and adding a coupon step-down incentive mechanism. Issuers voluntarily apply for the label; there are no mandatory compliance obligations or penalties."
        ),
        objective="Promote corporate sustainability and support carbon peaking and carbon neutrality goals",
        mitigation="Indirect",
        channel="Environment",
        country="CHN",
        jurisdiction="National",
        jurisdiction_name="N/A",
        adoption="28/04/2021",
        effective="28/04/2021",
        end_date="N/A",
        last_revision="10/10/2024",
        last_revision_detail=(
            "On 28 April 2021, NAFMII published the Sustainability-Linked Bond (SLB) Ten Questions and Answers, officially launching SLBs and establishing the SLB labelling and issuance framework. On 10 October 2024, NAFMII issued the Notice on Further Optimising Mechanisms for Green and Transition Bonds, further enriching linked target design, supporting SLB linkage to enterprises' overall sustainability targets and key regional development targets, recommending coupon step-down clauses and floating ranges, encouraging integration of SLBs with ESG scores, and implementing a green channel with immediate review upon filing for green and transition product registration and issuance."
        ),
        status="In force",
        admin_authorities="National Association of Financial Market Institutional Investors (NAFMII)",
        asset="Sustainability-linked bonds (labelling objects)",
        asset_status="New; Existing",
        asset_detail=(
            "The objects defined and covered by this instrument are sustainability-linked bonds (SLBs), including medium-term notes (MTNs), private placement notes (PPNs) and other debt financing instrument types in the interbank bond market. SLBs must set Key Performance Indicators (KPIs) and Sustainability Performance Targets (SPTs) that are strongly linked to the issuer's main business and strategic planning, with bond terms (such as coupon step-up/step-down, early redemption, one-time additional payments, etc.) linked to the achievement of the SPTs. Proceeds may be used for general purposes. The bond's full name carries the special designation '(Sustainability-Linked)' at the end."
        ),
        asset_other="N/A",
        asset_cutoff="N/A",
        agent="Firms",
        agent_detail=(
            "Issuers of sustainability-linked bonds. There are no restrictions on issuer type, issuance method or bond type; issuers that value reputation, wish to expand their ESG investor base, and have the capacity to achieve sustainability targets are encouraged to participate. Existing DFI/TDFI or MTN/PPN registration quotas may be converted to SLBs through the pre-issuance change process. Participation is voluntary, with no mandatory compliance obligations."
        ),
        activity="Registration, licensing or other administrative tasks",
        activity_detail=(
            "The activity regulated and guided by this instrument is the voluntary registration, issuance and labelling process for sustainability-linked bonds. At the time of bond registration and issuance, issuers must clearly disclose in the offering circular the definition, selection basis, measurement methodology and historical data of the linked targets (KPIs and SPTs), engage a third-party institution for pre-issuance assessment and certification, and engage a third-party institution to issue verification reports on SPT performance at least once a year during the bond's life. Bonds meeting the requirements may add the special designation '(Sustainability-Linked)' to their full name. During the bond's life, a dedicated report must be disclosed by 30 April each year until the last trigger event concludes. Participation is voluntary."
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1) KPIs must be strongly linked to the issuer's main business and overall strategic planning, be objectively quantifiable, and the quantified results must be capable of ex-post verification and repeated calculation by an authoritative third-party institution; 2) SPTs must satisfy the principles of materiality, verifiability and time-boundness, and represent a material improvement over a 'business-as-usual' operating scenario; 3) The offering circular must disclose the definition of linked targets, selection basis, measurement methodology, specific numerical values triggering changes in bond structure, and at least three years of historical data; 4) During the bond's life, a dedicated report must be disclosed by 30 April each year at the latest until the last trigger event concludes; 5) A third-party institution must be engaged during the bond's life to issue verification reports on SPT performance at least once a year; 6) In a trigger year, the verification report should be issued at least 15 working days before the interest payment date, redemption date or payment date; 7) Issuers voluntarily apply; there are no mandatory compliance obligations or penalties."
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "Issuers that obtain the SLB label can demonstrate their commitment to sustainability and transition resolve, gaining heightened attention from ESG investors and market reputation; SLBs offer flexible structural design, with the potential benefit of reduced financing costs through mechanisms such as coupon step-downs; after the implementation of the 2024 optimisation notice, enterprises that exceed their sustainability targets may receive additional coupon step-down awards (recommended floating range of [-30BP, 30BP]); green and transition product registration and issuance enjoys a green channel with immediate review upon filing."
        ),
        monitoring=(
            "Issuers must disclose a dedicated sustainability performance report by 30 April each year during the SLB's life; a third-party institution must be engaged to issue verification reports on SPT performance at least once a year; in a trigger year, the verification report shall be issued at least 15 working days before the interest payment date, redemption date or payment date; third-party assessment and certification bodies must possess prescribed qualification requirements (sound internal management systems, professional personnel, at least five project experiences in green bond assessment and certification or at least ten project experiences in related fields)."
        ),
        sanctions=(
            "N/A (voluntary labelling system; no non-compliance sanctions. For issuers that fail to achieve SPTs as agreed, the bond terms shall automatically trigger arrangements such as coupon adjustment or early redemption in accordance with the bond terms. For issuers that breach information disclosure requirements or submit false verification reports, NAFMII shall take self-regulatory disciplinary measures in accordance with self-regulatory rules.)"
        ),
        ghg_abs=(
            "N/A (this instrument is a voluntary bond labelling tool; the amount of GHG emissions covered depends on the scale of SLBs voluntarily labelled by issuers and the coverage of climate-related indicators among the sustainability targets linked to the bonds, and there is no directly quantifiable fixed coverage amount)"
        ),
        ghg_pct="N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        isic="K64",
        ghg="CO2; CH4; N2O",
        mitigation_effect="Positive",
        co_benefits="Green industry development; Technological innovation; Energy consumption reduction; Pollution control",
        legal_name="Sustainability-Linked Bond (SLB) Ten Questions and Answers published by the National Association of Financial Market Institutional Investors (NAFMII) on 28 April 2021",
        legal_url="https://www.nafmii.org.cn/xhdt/202104/t20210428_197371.html",
        other_links="N/A",
    ),

    # ── VLB 03: Water Efficiency Top-Runner System ──
    make_en_row(
        pid="CHNVIIVLBI03S000",
        instrument="Instrument",
        group="Voluntary information instrument",
        approach="Voluntary certification and labelling scheme",
        sector="Cross-sectoral",
        subsector="N/A",
        domestic_name="水效领跑者制度",
        english_name="Water Efficiency Top-Runner System",
        policy_package="N/A",
        description=(
            "The Water Efficiency Top-Runner System is a voluntary water efficiency benchmarking mechanism jointly established by the National Development and Reform Commission, the Ministry of Water Resources, the Ministry of Industry and Information Technology, the Ministry of Housing and Urban-Rural Development, the former General Administration of Quality Supervision, Inspection and Quarantine (now the State Administration for Market Regulation) and the National Energy Administration, founded under the Implementation Plan for the Water Efficiency Top-Runner Leading Action (Fa Gai Huan Zi [2016] No. 876), which selects top runners with leading water resource use efficiency in the domains of water-using products, key water-using enterprises, irrigation districts and public institutions, promoting society-wide water-saving and carbon-reduction synergy through benchmarking and positive incentives. The selection procedure follows a mechanism of voluntary application, local recommendation, expert review and public announcement. The implementation scope covers four domains: water-using products (toilets, smart toilets, dishwashers, showers, water purifiers, etc.; selected biennially); key water-using enterprises (covering 21 industries including thermal power, iron and steel, textile dyeing and finishing, papermaking, petroleum refining and chemicals; selected biennially); irrigation districts (large and medium-sized irrigation districts with an area of 10,000 mu or more; selected triennially); and public institutions (Party and government organs, schools, hospitals, etc.; selected triennially, incorporated under the Implementation Plan for the Water Efficiency Top-Runner Leading Action for Public Institutions jointly issued by the National Government Offices Administration, NDRC and MWR in 2020). The designation is valid for two years. Water savings drive down energy consumption in water abstraction, conveyance, heating and treatment, producing significant water-saving and carbon-reduction synergy benefits. Participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        objective="Improve society-wide water resource use efficiency and promote water-saving and carbon-reduction synergy",
        mitigation="Indirect",
        channel="Supply-side",
        country="CHN",
        jurisdiction="National",
        jurisdiction_name="N/A",
        adoption="21/04/2016",
        effective="21/04/2016",
        end_date="N/A",
        last_revision="N/A",
        last_revision_detail="N/A",
        status="In force",
        admin_authorities=(
            "National Development and Reform Commission (Department of Resource Conservation and Environmental Protection, lead); Ministry of Water Resources (National Water Conservation Office); Ministry of Industry and Information Technology (Department of Energy Conservation and Comprehensive Utilisation); Ministry of Housing and Urban-Rural Development; State Administration for Market Regulation; National Energy Administration; National Government Offices Administration (for the public institutions domain)"
        ),
        asset="Water-using products (toilets, smart toilets, dishwashers, showers, water purifiers, etc.); key water-using enterprises (21 industries including thermal power, iron and steel, textile dyeing and finishing, papermaking, petroleum refining and chemicals); irrigation districts (large and medium-sized irrigation districts with an area of 10,000 mu or more); public institutions (Party and government organs, schools, hospitals, etc.)",
        asset_status="Existing",
        asset_detail=(
            "The objects defined and covered by this instrument are the four domains of Water Efficiency Top-Runner selection: water-using products — end-use water-consuming products whose water efficiency has been tested and conforms to national water efficiency standards and whose water efficiency indicators rank at the leading level among comparable products; key water-using enterprises — industrial enterprises in 21 high-water-consumption industries that, through water-saving technological retrofits and recycling, have achieved a leading level of water withdrawal per unit of product among comparable enterprises; irrigation districts — large and medium-sized irrigation districts with an area of 10,000 mu or more whose effective irrigation water use coefficient ranks at the leading level among comparable districts; public institutions — units in the public institution domain such as Party and government organs, schools and hospitals that have sound water-saving management, high penetration of water-saving technologies and appliances, and leading water resource use efficiency. The designation is valid for two years."
        ),
        asset_other="N/A",
        asset_cutoff="N/A",
        agent="Enterprises; irrigation district management units; public institutions",
        agent_detail=(
            "Four types of entities may voluntarily apply for Water Efficiency Top-Runner: manufacturers of water-using products voluntarily submit product water efficiency test reports and application materials; key water-using enterprises voluntarily submit enterprise water efficiency assessment reports; irrigation district management units voluntarily submit irrigation district water resource use efficiency data; public institutions voluntarily submit water-saving management performance reports. Participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        activity="Registration, licensing or other administrative tasks",
        activity_detail=(
            "The activity regulated and guided by this instrument is the entire process of voluntary application, selection, designation and benchmarking demonstration for Water Efficiency Top-Runners: applying entities independently choose a domain and submit application materials to local competent authorities; local competent authorities conduct preliminary review and recommendation; national competent authorities organise expert review and, following prescribed procedures, announce and publish the list of Water Efficiency Top-Runners after public notice; designated entities fulfil demonstration and promotion obligations during the title validity period and are subject to dynamic tracking management. Participation is voluntary."
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1) Water-using products must pass national water efficiency testing, with water efficiency indicators meeting the top-running level among comparable products, based on relevant mandatory product water efficiency standards; 2) Key water-using enterprises must meet industry-specific Water Efficiency Top-Runner indicator requirements, with indicators such as water withdrawal per unit of product and recycling rate ranking at the leading level in the industry, and must have had no major safety or environmental incidents in the preceding three years; 3) Irrigation districts must have an irrigation area of 10,000 mu or more and an effective irrigation water use coefficient ranking at the leading level among comparable districts; 4) Public institutions must have sound water-saving management systems, high penetration of water-saving appliances and leading water resource use efficiency; 5) The selection process follows the mechanism of voluntary application, local recommendation, expert review and public notice; 6) The designation is valid for two years, during which entities are subject to dynamic tracking management; 7) Participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "Products, enterprises, irrigation districts and public institutions designated as Water Efficiency Top-Runners receive the national Water Efficiency Top-Runner title, enhancing market reputation and social image; the Top-Runner list is announced to the public and promoted through official channels, exerting a benchmarking and demonstration role; some local governments provide financial support for water-saving retrofits and tax incentives for Water Efficiency Top-Runner enterprises; the designation may serve as a reference for green manufacturing system certification such as Green Factory and Green Supply Chain."
        ),
        monitoring=(
            "Designated Water Efficiency Top-Runner entities are subject to dynamic tracking management during the title validity period to ensure continued compliance with Top-Runner requirements; provincial-level development and reform commissions and water resources, industry and information technology, and housing and urban-rural development competent authorities conduct routine supervision and periodic re-verification of Water Efficiency Top-Runners in their respective areas; national competent authorities carry out overall tracking and effectiveness assessment of progress across all regions."
        ),
        sanctions=(
            "N/A (voluntary selection system; no non-compliance sanctions. Entities that no longer meet Water Efficiency Top-Runner conditions shall have their title revoked and publicly announced. Entities that engage in fraudulent applications shall be disqualified and barred from re-applying for a specified period.)"
        ),
        ghg_abs=(
            "N/A (this instrument is a voluntary benchmarking mechanism; the amount of GHG emissions covered depends on the water-saving scale of designated entities and the water-saving and carbon-reduction synergy effects, and there is no directly quantifiable fixed coverage amount)"
        ),
        ghg_pct="N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        isic="C; A; O84; P85; Q86",
        ghg="CO2",
        mitigation_effect="Positive",
        co_benefits="Water resource conservation; Energy consumption reduction; Pollution control",
        legal_name="Notice of the National Development and Reform Commission, Ministry of Water Resources, Ministry of Industry and Information Technology, Ministry of Housing and Urban-Rural Development, General Administration of Quality Supervision, Inspection and Quarantine and National Energy Administration on Issuing the Implementation Plan for the Water Efficiency Top-Runner Leading Action (Fa Gai Huan Zi [2016] No. 876)",
        legal_url="https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=2443",
        other_links="N/A",
    ),

    # ── VLB 10: Zero-Carbon Industrial Park Label ──
    make_en_row(
        pid="CHNVIIVLBI10S000",
        instrument="Instrument",
        group="Voluntary information instrument",
        approach="Voluntary certification and labelling scheme",
        sector="Industry",
        subsector="N/A",
        domestic_name="零碳园区标识",
        english_name="Zero-Carbon Industrial Park Label",
        policy_package="N/A",
        description=(
            "The Zero-Carbon Industrial Park Label is a national-level voluntary park evaluation, designation and labelling system jointly established by the National Development and Reform Commission, the Ministry of Industry and Information Technology, and the National Energy Administration, founded under the Notice on Carrying Out Zero-Carbon Industrial Park Construction (Fa Gai Huan Zi [2025] No. 910). A zero-carbon industrial park refers to a park where the CO2 emissions generated by production and living activities within the park are reduced to near-zero levels through planning, design, technology and management approaches, and which has the conditions to further achieve net-zero. The system follows an implementation pathway of 'voluntary application, local recommendation, national review, construction implementation, and assessment and acceptance': provincial-level and above development zones (including provincial-level emerging industry parks and high-tech parks) apply voluntarily; each province recommends no more than two parks; the NDRC, together with relevant parties, reviews and determines the list of national-level zero-carbon industrial parks for construction; after the construction period expires, the provincial Development and Reform Commission organises a self-assessment, and the NDRC organises assessment and acceptance; parks that pass are formally designated as National-Level Zero-Carbon Industrial Parks. The core evaluation indicator is carbon emissions per unit of energy consumption: parks with an annual comprehensive energy consumption of 200,000–1,000,000 tce must achieve ≤0.2 tCO2/tce, and parks with ≥1,000,000 tce must achieve ≤0.3 tCO2/tce (approximately a 90% reduction from the national park average of about 2.1 tCO2/tce). There are five additional guiding indicators: clean energy consumption share (≥90%), energy consumption per unit of product of enterprises in the park (meeting or exceeding Level-II energy consumption quota standards), comprehensive industrial solid waste utilisation rate (≥80%), comprehensive waste heat/cold/pressure utilisation rate (≥50%), and industrial water reuse rate (≥80%). Applicant parks must have a foundation in energy consumption and carbon emissions statistics, accounting, metering and monitoring, and must have had no major safety or environmental incidents in the preceding three years. The construction tasks cover eight domains: energy consumption structure transition, energy conservation and carbon reduction, industrial structure adjustment, resource conservation and intensification, infrastructure upgrading, advanced technology application, energy and carbon management capacity enhancement, and reform and innovation. Participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        objective="Promote the green and low-carbon transition of industrial parks and advance carbon peaking and carbon neutrality",
        mitigation="Direct",
        channel="Supply-side",
        country="CHN",
        jurisdiction="National",
        jurisdiction_name="N/A",
        adoption="30/06/2025",
        effective="08/07/2025",
        end_date="N/A",
        last_revision="N/A",
        last_revision_detail="N/A",
        status="In force",
        admin_authorities=(
            "National Development and Reform Commission (Department of Resource Conservation and Environmental Protection, lead); Ministry of Industry and Information Technology (Department of Energy Conservation and Comprehensive Utilisation); National Energy Administration (Department of New and Renewable Energy)"
        ),
        asset="Industrial parks (zero-carbon park evaluation and designation objects)",
        asset_status="New; Existing",
        asset_detail=(
            "The objects defined and covered by this instrument are provincial-level and above development zones (including emerging industry parks and high-tech parks approved by provincial-level and above people's governments or competent authorities). The construction scope may be the entire park or a 'park-within-a-park' with clearly defined four-boundary boundaries. A zero-carbon industrial park must reduce the CO2 emissions generated by production and living activities within the park to near-zero levels through planning, design, technology and management approaches, and must have the conditions to further achieve net-zero. The core evaluation indicator is carbon emissions per unit of energy consumption (tCO2/tce). The application threshold is annual comprehensive energy consumption of 200,000 tce or above."
        ),
        asset_other="N/A",
        asset_cutoff="N/A",
        agent="Firms",
        agent_detail=(
            "Operating enterprises or park management enterprises of provincial-level and above development zones. Park operating enterprises may voluntarily apply for national-level zero-carbon industrial park construction, prepare a construction plan and submit it according to procedures. After being reviewed and included in the list of national-level zero-carbon industrial parks for construction, they shall advance zero-carbon construction in accordance with the construction plan and undergo assessment and acceptance after the construction period expires. Participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        activity="Registration, licensing or other administrative tasks",
        activity_detail=(
            "The activities regulated and guided by this instrument are the full process of voluntary application, construction implementation, assessment and acceptance, and labelling and designation for zero-carbon industrial parks. Park management bodies voluntarily submit an application and construction plan to the provincial Development and Reform Commission; each province recommends no more than two parks to the NDRC; the NDRC, together with relevant parties, reviews and determines the list of national-level zero-carbon industrial parks for construction. Parks carry out key tasks in eight domains in accordance with the construction plan: energy consumption structure transition, energy conservation and carbon reduction, industrial structure adjustment, resource conservation and intensification, infrastructure upgrading, advanced technology application, energy and carbon management capacity enhancement, and reform and innovation. After the construction period expires, the provincial Development and Reform Commission organises a self-assessment, and the NDRC organises assessment and acceptance; parks that pass are formally designated as National-Level Zero-Carbon Industrial Parks. Participation is voluntary."
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1) Applicant parks must be provincial-level or above development zones (including provincial-level emerging industry parks or high-tech parks); the construction scope may be the entire park or a 'park-within-a-park'; 2) Applicant parks must have a foundation in energy consumption and carbon emissions statistics, accounting, metering and monitoring; 3) Applicant parks must have had no major safety or environmental incidents or other adverse social impact events in the preceding three years; 4) Core indicator: parks with annual comprehensive energy consumption of 200,000–1,000,000 tce must achieve ≤0.2 tCO2/tce, and parks with ≥1,000,000 tce must achieve ≤0.3 tCO2/tce; 5) Five guiding indicators: clean energy consumption share ≥90%, energy consumption per unit of product of enterprises in the park meeting or exceeding Level-II energy consumption quota standards, comprehensive industrial solid waste utilisation rate ≥80%, comprehensive waste heat/cold/pressure utilisation rate ≥50%, and industrial water reuse rate ≥80%; 6) Each province may recommend no more than two parks; 7) After the construction period expires, a provincial self-assessment and national assessment and acceptance must be passed before formal designation as a National-Level Zero-Carbon Industrial Park; 8) Participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "Parks included in the list of national-level zero-carbon industrial parks for construction receive national and local policy support, including: coordinated use of existing funding channels to support construction, encouragement of local government special bond investment; encouragement of policy banks to provide medium- and long-term credit support; support for park enterprises to issue green bonds; innovation in energy conservation review and carbon emission evaluation models, exploring regional approval or project filing; strengthening land and sea use factor guarantees; and support for bringing in external talent, technology and professional institutions to serve energy-saving and carbon-reduction retrofits and product carbon footprint certification. Formally designated national-level zero-carbon industrial parks receive the National Zero-Carbon Industrial Park title, enhancing park brand value and investment attractiveness, and exerting a benchmarking and demonstration role."
        ),
        monitoring=(
            "Parks included in the construction list must implement the construction plan and carry out periodic tracking and assessment of progress; after the construction period expires, the provincial Development and Reform Commission organises a self-assessment, and the NDRC, together with relevant parties, organises assessment and acceptance. Parks must have a foundation in energy consumption and carbon emissions statistics, accounting, metering and monitoring, build energy and carbon management platforms, and implement dynamic monitoring of the park's energy load and carbon emissions. Each region may carry out provincial-level zero-carbon industrial park construction based on local conditions and implement corresponding supervision and management."
        ),
        sanctions=(
            "N/A (voluntary evaluation, designation and labelling system; no non-compliance sanctions. Parks that fail assessment and acceptance upon expiry of the construction period may re-apply for acceptance after rectification. Parks found to have engaged in fraud or that no longer meet zero-carbon park conditions shall have their National-Level Zero-Carbon Industrial Park designation revoked.)"
        ),
        ghg_abs=(
            "N/A (this instrument is a voluntary park evaluation, designation and labelling tool; the amount of GHG emissions covered depends on the scale and number of parks that voluntarily apply and pass designation, and there is no directly quantifiable fixed coverage amount)"
        ),
        ghg_pct="N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        isic="C",
        ghg="CO2",
        mitigation_effect="Positive",
        co_benefits="Green industry development; Technological innovation; Energy consumption reduction; Pollution control; Renewable energy development",
        legal_name=(
            "Notice of the National Development and Reform Commission, the Ministry of Industry and Information Technology, and the National Energy Administration on Carrying Out Zero-Carbon Industrial Park Construction (Fa Gai Huan Zi [2025] No. 910)"
        ),
        legal_url="https://www.ndrc.gov.cn/xxgk/zcfb/tz/202507/t20250708_1399055_ext.html",
        other_links="https://www.gov.cn/zhengce/zhengceku/202507/content_7031090.htm",
    ),

    # ── VID 01: Corporate Sustainability Disclosure Standards ──
    make_en_row(
        pid="CHNVIIVIDI01S000",
        instrument="Instrument",
        group="Voluntary information instrument",
        approach="Voluntary information disclosure",
        sector="Cross-sectoral",
        subsector="N/A",
        domestic_name="企业可持续披露准则",
        english_name="Corporate Sustainability Disclosure Standards",
        policy_package="N/A",
        description=(
            "The Corporate Sustainability Disclosure Standards are a unified sustainability disclosure standards system jointly formulated and issued by the Ministry of Finance together with nine departments — the Ministry of Foreign Affairs, the National Development and Reform Commission, the Ministry of Industry and Information Technology, the Ministry of Ecology and Environment, the Ministry of Commerce, the People's Bank of China, the State-owned Assets Supervision and Administration Commission of the State Council, the National Financial Regulatory Administration, and the China Securities Regulatory Commission — aimed at establishing national unified sustainability disclosure baselines, providing enterprises with standardised sustainability information disclosure methodology and content specifications, and enhancing the comparability and decision-usefulness of disclosed information. The standards system consists of three tiers: Basic Standards, Specific Standards and Application Guidance. The Corporate Sustainability Disclosure Standards — Basic Standards (Trial) (Cai Kuai [2024] No. 17) is the first document of the system, comprising six chapters and 31 articles, setting out the fundamental concepts, principles, methods and general common requirements for sustainability information disclosure. The Standards draw on the useful experience of the ISSB's IFRS S1 while taking account of China's national circumstances, and construct the disclosure framework around four core elements: governance, strategy, risk and opportunity management, and metrics and targets. The system-building targets are to issue the Basic Standards and climate-related disclosure standards with application guidance by 2027, and to substantially complete the national unified sustainability disclosure standards system by 2030. The implementation strategy is phased: from listed companies to unlisted companies, from large enterprises to small and medium-sized enterprises, from qualitative requirements to quantitative requirements, and from voluntary disclosure to mandatory disclosure. At the current stage, enterprises implement the standards voluntarily; there are no mandatory compliance obligations or penalties."
        ),
        objective="Standardise corporate sustainability information disclosure and improve information transparency and comparability",
        mitigation="Indirect",
        channel="Environment",
        country="CHN",
        jurisdiction="National",
        jurisdiction_name="N/A",
        adoption="20/11/2024",
        effective="17/12/2024",
        end_date="N/A",
        last_revision="19/12/2025",
        last_revision_detail=(
            "On 19 December 2025, the Ministry of Finance, together with nine departments — the Ministry of Ecology and Environment, the Ministry of Foreign Affairs, the National Development and Reform Commission, the Ministry of Industry and Information Technology, the Ministry of Commerce, the People's Bank of China, the State-owned Assets Supervision and Administration Commission of the State Council, the National Financial Regulatory Administration, and the China Securities Regulatory Commission — jointly issued the Corporate Sustainability Disclosure Standards No. 1 — Climate (Trial) (Cai Kuai [2025] No. 34), the first specific standard of the standards system, regulating enterprise disclosure of climate-related risks, opportunities and impacts. It covers core disclosure requirements including identification and assessment of climate-related risks and opportunities, transition planning and climate resilience, and greenhouse gas emissions. The Standard is broadly aligned with the ISSB's IFRS S2 Climate-related Disclosures and is implemented voluntarily by enterprises."
        ),
        status="In force",
        admin_authorities=(
            "Ministry of Finance (Accounting Regulatory Department, lead); Ministry of Foreign Affairs; National Development and Reform Commission; Ministry of Industry and Information Technology; Ministry of Ecology and Environment; Ministry of Commerce; People's Bank of China; State-owned Assets Supervision and Administration Commission of the State Council; National Financial Regulatory Administration; China Securities Regulatory Commission"
        ),
        asset="Sustainability/ESG information (disclosure object)",
        asset_status="N/A",
        asset_detail=(
            "The objects defined and covered by this instrument are the sustainability risk and opportunity-related information involved in corporate sustainability disclosure, covering the four core disclosure elements of governance, strategy, risk and opportunity management, and metrics and targets. The sustainability information disclosed by enterprises should cover sustainability risks and opportunities within their value chain, including environmental topics (climate, pollution, water resources, biodiversity, circular economy), social topics (employee rights, consumer protection, community relations, rural revitalisation), and governance topics (business conduct)."
        ),
        asset_other="N/A",
        asset_cutoff="N/A",
        agent="Firms",
        agent_detail=(
            "Enterprises registered within the territory of the People's Republic of China. At the current stage, enterprises voluntarily refer to the Standards for sustainability information disclosure; the scope will be phased to listed companies, unlisted companies, large enterprises, and small and medium-sized enterprises. The Standards impose no mandatory compliance obligations or administrative penalties; enterprises may independently decide whether to apply them, the extent of application and the timeline for application."
        ),
        activity="Registration, licensing or other administrative tasks",
        activity_detail=(
            "The activity regulated and guided by this instrument is the full process by which enterprises conduct sustainability information disclosure with reference to the unified standards framework, including: identifying and assessing sustainability risks and opportunities; determining the disclosure scope and boundary; preparing sustainability information reports in accordance with the four core elements of governance, strategy, risk and opportunity management, and metrics and targets; ensuring information meets the quality requirements of reliability, relevance, comparability, verifiability, understandability and timeliness; connecting sustainability information with financial statement information; and publicly disclosing the information through annual reports, sustainability reports or dedicated environmental information reports. Participation is voluntary."
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1) Disclosed information must cover the four core elements: governance (the governance structure for sustainability risks and opportunities), strategy (the financial impact of sustainability risks and opportunities on the enterprise and the resilience of its strategy), risk and opportunity management (the processes for identifying, assessing, prioritising and monitoring), and metrics and targets (quantifiable sustainability-related performance indicators and progress); 2) Disclosed information must meet the six information quality requirements of reliability, relevance, comparability, verifiability, understandability and timeliness; 3) Enterprises must disclose the current and anticipated financial effects of sustainability risks and opportunities, and the resilience of their strategy and business model to sustainability risks; 4) Disclosure should cover material sustainability risks and opportunities within the value chain; 5) Enterprises should describe the relationship and connected information between the sustainability information report and the financial statement report; 6) At the current stage, enterprises implement the standards voluntarily; there are no mandatory compliance obligations or penalties."
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "Enterprises that adopt the Standards for sustainability information disclosure can improve the quality and international comparability of their disclosed information, gaining the trust of investors, creditors and other stakeholders; high-quality sustainability information disclosure helps enterprises obtain green finance product support and ESG investment; the Standards are broadly aligned with the ISSB's IFRS S1, helping enterprises respond to international sustainability information disclosure requirements and cross-border capital flow needs."
        ),
        monitoring=(
            "At the current voluntary implementation stage, there are no mandatory compliance monitoring requirements. The Ministry of Finance, together with relevant departments, will track and assess the implementation of the Standards and adjust the implementation scope and mandatory requirements in due course. Sustainability information voluntarily disclosed by enterprises may be subject to assurance services by third-party institutions."
        ),
        sanctions=(
            "N/A (voluntary disclosure standards; no non-compliance sanctions. At the current stage, enterprises implement the standards voluntarily; there are no mandatory compliance obligations or penalties.)"
        ),
        ghg_abs=(
            "N/A (this instrument is a voluntary disclosure standards framework; the amount of GHG emissions covered depends on the number of enterprises voluntarily adopting the standards for climate-related information disclosure and the scope of disclosure, and there is no directly quantifiable fixed coverage amount)"
        ),
        ghg_pct="N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        isic="M72",
        ghg="CO2; CH4; N2O",
        mitigation_effect="Positive",
        co_benefits="Technological innovation; Green industry development; Energy consumption reduction",
        legal_name="Notice of the Ministry of Finance and Other Departments on Issuing the Corporate Sustainability Disclosure Standards — Basic Standards (Trial) (Cai Kuai [2024] No. 17)",
        legal_url="http://kjs.mof.gov.cn/zhengcefabu/202412/t20241216_3949745.htm",
        other_links="https://www.casc.org.cn/2025/1225/278706.shtml",
    ),

    # ── VID 02: Environmental Information Disclosure Guidelines for Financial Institutions ──
    make_en_row(
        pid="CHNVIIVIDI02S000",
        instrument="Instrument",
        group="Voluntary information instrument",
        approach="Voluntary information disclosure",
        sector="Cross-sectoral",
        subsector="N/A",
        domestic_name="金融机构环境信息披露指南",
        english_name="Environmental Information Disclosure Guidelines for Financial Institutions",
        policy_package="N/A",
        description=(
            "The Environmental Information Disclosure Guidelines for Financial Institutions is a recommended financial industry standard (JR/T 0227—2021) formulated and issued by the People's Bank of China, providing a framework for financial institutions to standardise their environmental information disclosure. The Guidelines specify the principles to be followed in the environmental information disclosure process (truthfulness, timeliness, consistency, continuity), disclosure forms and frequency (at least once a year is encouraged; disclosure may take the form of a dedicated environmental information report, disclosure within a social responsibility report, or disclosure within an annual report), and the core content elements for disclosure: annual overview, governance structure, policy framework, product and service innovation, risk management processes, environmental impact of investment and financing activities, environmental impact of operations, data collation, verification and protection, and green finance innovation research outcomes. The Guidelines apply to financial institutions — including banks, asset management companies, insurance companies, trust companies, futures companies and securities companies — legally established within the territory of China. The standard is a recommended standard; financial institutions adopt it voluntarily, and there are no mandatory compliance obligations or penalties."
        ),
        objective="Standardise environmental information disclosure by financial institutions and improve environmental information transparency in the financial sector",
        mitigation="Indirect",
        channel="Environment",
        country="CHN",
        jurisdiction="National",
        jurisdiction_name="N/A",
        adoption="22/07/2021",
        effective="22/07/2021",
        end_date="N/A",
        last_revision="N/A",
        last_revision_detail="N/A",
        status="In force",
        admin_authorities=(
            "People's Bank of China (Research Bureau, Science and Technology Department); National Financial Standardisation Technical Committee (SAC/TC 180)"
        ),
        asset="Environmental information (disclosure object)",
        asset_status="N/A",
        asset_detail=(
            "The objects defined and covered by this instrument are environmental information related to financial institutions' operational activities and investment and financing activities, specifically including: the financial institution's annual green finance overview (green finance development strategy, objectives and annual achievements); environment-related governance structure (the board and senior management's oversight responsibilities for environmental matters); environment-related policies and systems (internal systems and processes for green finance); green finance product and service innovation (types and scale of green credit, green bonds, green insurance, ESG investment and other products); environmental risk management processes (environmental risk identification, assessment, monitoring and response mechanisms); the environmental impact of investment and financing activities (environmental performance indicators of the investment and financing portfolio such as carbon emission intensity or emission reductions); the environmental impact of operational activities (green operation indicators such as the institution's own energy consumption, carbon emissions and resource use); and data collation, verification and protection arrangements."
        ),
        asset_other="N/A",
        asset_cutoff="N/A",
        agent="Firms",
        agent_detail=(
            "Financial institutions legally established within the territory of the People's Republic of China, including banking institutions (commercial banks, policy banks, rural cooperative banks, rural credit cooperatives, etc.), asset management companies, insurance companies, trust companies, futures companies and securities companies. The standard is a recommended industry standard; financial institutions adopt it voluntarily and determine the extent and scope of disclosure based on their own circumstances."
        ),
        activity="Registration, licensing or other administrative tasks",
        activity_detail=(
            "The activity regulated and guided by this instrument is the full process by which financial institutions conduct environmental information disclosure with reference to the Guidelines, including: establishing an environmental information disclosure governance structure and assignment of responsibilities; identifying and determining the scope and content elements of environmental information disclosure; establishing environmental information data collection, measurement, verification and management systems; selecting appropriate disclosure forms and vehicles (dedicated environmental information report, social responsibility report or annual report); preparing environmental information disclosure content in accordance with the prescribed elements; and publicly disclosing the information through public distribution channels and accepting public oversight. Financial institutions may voluntarily choose the form, frequency and scope of disclosure; disclosure at least once a year is encouraged."
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1) Disclosure shall follow the four principles of truthfulness, timeliness, consistency and continuity; 2) Disclosure content shall cover the core elements of annual overview, governance structure, policy framework, product and service innovation, risk management processes, environmental impact of investment and financing activities, environmental impact of operational activities, data collation, verification and protection, and green finance innovation research outcomes; 3) Disclosure may take the form of a dedicated environmental information report, disclosure within a social responsibility report, or disclosure within an annual report; 4) Disclosure at least once a year is encouraged; 5) Financial institutions shall establish data collection, measurement, verification and management mechanisms to ensure disclosed information is accurate and reliable; 6) The standard is a recommended industry standard; financial institutions adopt it voluntarily, and there are no mandatory compliance obligations or penalties."
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "Financial institutions that adopt the Guidelines for environmental information disclosure can enhance their environmental risk management and green finance development capabilities, and strengthen market transparency and stakeholder trust; high-quality environmental information disclosure helps financial institutions achieve good performance in green finance performance evaluations, and meet the environmental information needs of investors and rating agencies; regions such as the Green Finance Reform and Innovation Pilot Zones encourage financial institutions within their jurisdictions to take the lead in achieving full environmental information disclosure."
        ),
        monitoring=(
            "At the current voluntary adoption stage, there are no mandatory compliance monitoring requirements. The People's Bank of China and relevant financial regulatory authorities track and monitor the environmental information disclosure situation of financial institutions; certain regions such as the Green Finance Reform and Innovation Pilot Zones monitor and assess the proportion and quality of environmental information disclosure by financial institutions within their jurisdictions. Financial institutions may engage third-party institutions to provide independent assurance on environmental information."
        ),
        sanctions=(
            "N/A (recommended industry standard; no non-compliance sanctions. Financial institutions adopt the standard voluntarily; there are no mandatory compliance obligations or penalties.)"
        ),
        ghg_abs=(
            "N/A (this instrument is a voluntary disclosure guideline; the amount of GHG emissions covered depends on the coverage and depth of environmental information disclosure voluntarily adopted by financial institutions — including portfolio carbon emissions — and there is no directly quantifiable fixed coverage amount)"
        ),
        ghg_pct="N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        isic="K64",
        ghg="CO2; CH4; N2O",
        mitigation_effect="Positive",
        co_benefits="Green industry development; Technological innovation; Energy consumption reduction; Pollution control",
        legal_name="Environmental Information Disclosure Guidelines for Financial Institutions (JR/T 0227—2021) issued by the People's Bank of China",
        legal_url="https://std.samr.gov.cn/hb/search/stdHBDetailed?id=C8CBBCAE2F3D5981E05397BE0A0AB29C",
        other_links="N/A",
    ),
    # ── VTG 01: Home Appliance Manufacturer Recycling Target Responsibility System ──
    make_en_row(
        pid="CHNVTGVTGI01S000",
        instrument="Instrument",
        group="Voluntary target",
        approach="Voluntary target",
        sector="Industry",
        subsector="Home appliances",
        domestic_name="家电生产企业回收目标责任制",
        english_name="Home Appliance Manufacturer Recycling Target Responsibility System",
        policy_package="N/A",
        description=(
            "The Home Appliance Manufacturer Recycling Target Responsibility System is a voluntary target responsibility framework jointly established by the National Development and Reform Commission, the Ministry of Industry and Information Technology, and the Ministry of Ecology and Environment, guiding home appliance manufacturers to independently set quantitative recycling targets for waste home appliances and publicly commit to them, advancing the implementation of the extended producer responsibility system. The Notice (Fa Gai Chan Ye [2021] No. 1102) specifies that for four categories of home appliances — televisions, refrigerators, washing machines and air conditioners — manufacturers are encouraged to set annual quantitative targets for recycling volume and recycling rate, and to implement them across six action areas: defining recycling targets (recycling volume/rate accounting for 70% of evaluation weight, with recycling behaviour targets at 30%); expanding recycling channels (using sales networks, after-sales services and e-commerce platforms for reverse recycling and trade-in programmes); optimising storage and transport networks; strengthening flow management (unified coding, chain-of-custody forms, full-process traceability; waste appliances must be handed over to qualified processors for regulated dismantling); promoting green development (increasing recycled material processing levels and procurement ratios, optimising product design for easy recycling and dismantling); and policy incentives and constraints. Responsible enterprises submit application reports by 31 January each year; the three ministries publish the list of responsible enterprises and their recycling targets by the end of March each year; enterprises conduct annual self-evaluations and disclose them publicly; the three ministries track and evaluate progress annually. The overall target is to develop a group of model enterprises by 2023. Participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        objective="Implement the extended producer responsibility system and increase the rate of regulated recycling of waste home appliances",
        mitigation="Indirect",
        channel="Supply-side",
        country="CHN",
        jurisdiction="National",
        jurisdiction_name="N/A",
        adoption="27/07/2021",
        effective="04/08/2021",
        end_date="N/A",
        last_revision="N/A",
        last_revision_detail="N/A",
        status="In force",
        admin_authorities=(
            "National Development and Reform Commission (Department of Industrial Development, lead); "
            "Ministry of Industry and Information Technology (Department of Energy Conservation and Comprehensive Utilisation); "
            "Ministry of Ecology and Environment (Department of Solid Wastes and Chemicals)"
        ),
        asset="Waste home appliances (televisions, refrigerators, washing machines, air conditioners)",
        asset_status="Existing",
        asset_detail=(
            "The objects defined and covered by this instrument are waste products in four categories of home appliances: televisions, refrigerators, washing machines and air conditioners. Recycling statistics are not restricted by product category or brand; manufacturers may recycle products not produced by their own enterprise. Waste home appliances must be handed over to qualified waste electrical and electronic equipment processors for regulated dismantling and treatment."
        ),
        asset_other="N/A",
        asset_cutoff="N/A",
        agent="Enterprises",
        agent_detail=(
            "Home appliance manufacturers (calculated on a parent-company basis). Enterprises may voluntarily apply to participate in the recycling target responsibility system initiative, independently set annual quantitative targets for recycling volume and recycling rate, and disclose them publicly. Participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        activity="Collection or sorting after use",
        activity_detail=(
            "The activities regulated and guided by this instrument are the full process by which home appliance manufacturers voluntarily establish a reverse recycling system for waste home appliances and implement a recycling target responsibility system, including: setting annual quantitative targets for recycling volume and recycling rate; using sales networks, after-sales services and e-commerce platforms to expand recycling channels; building recycling storage facilities and optimising transport networks; establishing information traceability systems covering the full process of collection, transport and treatment; and handing over waste home appliances to qualified enterprises for regulated dismantling and treatment. Participation is voluntary."
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1) Enterprises independently set annual quantitative targets for recycling volume and recycling rate (annual recycling volume divided by average sales volume over the preceding three years); recycling volume and rate indicators account for 70% of evaluation weight, and recycling behaviour targets account for 30%; 2) recycling statistics are not restricted by product category or brand; 3) waste home appliances must be handed over to qualified waste electrical and electronic equipment processors for regulated dismantling and treatment; 4) enterprises must establish information traceability systems covering the full process of collection, transport and treatment, implementing unified coding and chain-of-custody form management; 5) enterprises must submit application reports through provincial-level Development and Reform Commissions by 31 January each year; the three ministries publish the list of responsible enterprises and recycling targets by the end of March each year; 6) enterprises must conduct annual self-evaluations and disclose them publicly; 7) participation is voluntary, with no mandatory compliance obligations or penalties."
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "Enterprises that meet their recycling targets are included in a 「green responsibility list」 and receive priority support in green bond issuance, green credit approval, and dedicated government funds; the experience and models of model enterprises are promoted nationwide."
        ),
        monitoring=(
            "Responsible enterprises must conduct annual self-evaluations and disclose the results publicly. The National Development and Reform Commission, the Ministry of Industry and Information Technology, and the Ministry of Ecology and Environment track and evaluate the recycling target completion of responsible enterprises on an annual basis and publish the evaluation results."
        ),
        sanctions="N/A (voluntary target responsibility framework; enterprises participate voluntarily, with no mandatory compliance obligations or penalties)",
        ghg_abs=(
            "N/A (this instrument is a voluntary target responsibility framework; the volume of GHG emissions covered depends on the scale and extent of voluntary enterprise participation and recycling treatment, with no directly quantifiable fixed coverage)"
        ),
        ghg_pct="N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        isic="C27",
        ghg="CO2; CH4",
        mitigation_effect="Positive",
        co_benefits="Circular economy; Resource conservation; Pollution control",
        legal_name=(
            "Notice of the National Development and Reform Commission, the Ministry of Industry and Information Technology, and the Ministry of Ecology and Environment on Encouraging Home Appliance Manufacturers to Carry Out Recycling Target Responsibility System Actions (Fa Gai Chan Ye [2021] No. 1102)"
        ),
        legal_url="https://www.miit.gov.cn/jgsj/jns/wjfb/art/2021/art_5df08ed7493e4a40af80f0124fc2e7b7.html",
        other_links="N/A",
    ),
    # ── VTG 02: Self-Built or Purchased Peak-Shaving Capacity ──
    make_en_row(
        pid="CHNVTGVTGI02S000",
        instrument="Instrument",
        group="Voluntary target",
        approach="Voluntary target",
        sector="Energy",
        subsector="Wind power; Solar power",
        domestic_name="可再生能源发电企业自建或购买调峰能力增加并网规模",
        english_name="Self-Built or Purchased Peak-Shaving Capacity by Renewable Energy Power Generation Enterprises to Increase Grid-Connected Scale",
        policy_package="N/A",
        description=(
            "The Self-Built or Purchased Peak-Shaving Capacity by Renewable Energy Power Generation Enterprises to Increase Grid-Connected Scale is a voluntary target mechanism jointly established by the National Development and Reform Commission and the National Energy Administration, guiding renewable energy power generation enterprises to increase the scale of renewable energy installed capacity connected to the grid by self-building or purchasing peak-shaving and energy storage capacity. The Notice (Fa Gai Yun Xing [2021] No. 1138) specifies that, on the basis of grid enterprises undertaking guaranteed grid-connection responsibilities, wind power and solar power generation enterprises are encouraged to increase grid-connected scale by self-building, co-building, or market-based purchasing of peak-shaving resources. Peak-shaving resources include pumped-storage hydropower, new-type energy storage such as electrochemical storage, gas-fired power, concentrating solar power (CSP) plants, and flexibility-retrofitted coal-fired power. Linkage ratio requirements: for capacity beyond guaranteed grid-connection, peak-shaving capacity shall be built at an initial linkage ratio of 15% of power capacity (with a duration of four hours or more); enterprises building at a ratio of 20% or above receive priority grid connection. Co-built capacity may be converted pro-rata to the capital contribution ratio. Purchasing peak-shaving capacity includes both purchasing peak-shaving and energy storage projects and purchasing peak-shaving and energy storage services; the purchased entity is limited to newly built peak-shaving resources in the current year. Power generation projects must be constructed and connected to the grid synchronously with new peak-shaving projects. Unused peak-shaving resources may be traded to other power generation enterprises within the province but may not be carried forward to the following year. Grid dispatch agencies conduct dispatch tests on peak-shaving projects from time to time to ensure that capacity is genuinely available. Participation is voluntary in nature, but enterprises making false commitments shall have their peak-shaving capacity deducted at twice the uncompleted amount and shall be disqualified from self-assuming renewable energy consumption responsibility in the following year."
        ),
        objective="Promote the consumption of renewable energy and improve the flexibility and regulation capacity of the power system",
        mitigation="Direct",
        channel="Supply-side",
        country="CHN",
        jurisdiction="National",
        jurisdiction_name="N/A",
        adoption="29/07/2021",
        effective="10/08/2021",
        end_date="N/A",
        last_revision="N/A",
        last_revision_detail="N/A",
        status="In force",
        admin_authorities=(
            "National Development and Reform Commission (Department of Economic Operation and Regulation); "
            "National Energy Administration (Department of New and Renewable Energy)"
        ),
        asset="Peak-shaving resources (pumped-storage hydropower, new-type energy storage such as electrochemical storage, gas-fired power, CSP plants, flexibility-retrofitted coal-fired power)",
        asset_status="New",
        asset_detail=(
            "The objects defined and covered by this instrument are peak-shaving and energy storage resources used to increase the grid-connected scale of renewable energy, including pumped-storage hydropower stations, new-type energy storage facilities such as electrochemical storage, natural-gas-fired power generation, concentrating solar power (CSP) plants, and coal-fired power units that have undergone flexibility retrofitting. Peak-shaving capacity is recognised by installed capacity (for pumped storage, electrochemical storage and CSP), by design output of the unit (for gas-fired power), or by the difference in the adjustable output range before and after retrofitting (for coal-fired power flexibility retrofitting)."
        ),
        asset_other="N/A",
        asset_cutoff="N/A",
        agent="Enterprises",
        agent_detail=(
            "Renewable energy power generation enterprises such as wind power and solar power enterprises. Enterprises may voluntarily choose to self-build, co-build, or market-purchase peak-shaving and energy storage capacity to increase grid-connected scale. Participation is voluntary, but enterprises making false commitments shall be disqualified from self-assuming renewable energy consumption responsibility in the following year."
        ),
        activity="Production, transmission and distribution of electricity",
        activity_detail=(
            "The activities regulated and guided by this instrument are the full process by which renewable energy power generation enterprises increase the grid-connected scale of renewable energy installed capacity by self-building or purchasing peak-shaving and energy storage capacity, including: enterprises determining the required peak-shaving capacity scale according to the linkage ratio (initial period 15%, recommended 20% or above); choosing self-building, co-building or market-based purchasing to fulfil peak-shaving resources; ensuring that power generation projects and new peak-shaving projects are constructed and connected to the grid synchronously; accepting dispatch tests by grid dispatch agencies from time to time; and intra-provincial market-based trading of unused peak-shaving resources (carry-forward to the following year not permitted). Participation is voluntary, following the confirmation principle of 「enterprise commitment, government filing, process verification, and double penalty for false claims」."
        ),
        intensity_val="N/A",
        intensity_unit="N/A",
        intensity_detail="N/A",
        req_spec=(
            "1) For capacity beyond guaranteed grid-connection, peak-shaving capacity shall be built at an initial linkage ratio of 15% of power capacity (duration of four hours or above); enterprises building at 20% or above receive priority grid connection; 2) co-built capacity shall be converted pro-rata to the capital contribution ratio, which may initially be moderately higher than the capital contribution ratio; 3) purchased peak-shaving capacity is limited to newly built peak-shaving resources in the current year; 4) power generation projects must be constructed and connected to the grid synchronously with new peak-shaving projects; 5) peak-shaving capacity is recognised by installed capacity, design output of the unit, or the difference in the adjustable output range; 6) the confirmation principle of 「enterprise commitment, government filing, process verification, and double penalty for false claims (twice the uncompleted capacity deducted, with rectification within a prescribed period)」 applies; 7) unused peak-shaving resources may be traded intra-provincially but may not be carried forward to the following year; 8) participation is voluntary."
        ),
        calc_i="N/A",
        calc_ii="N/A",
        incentives=(
            "Enterprises building peak-shaving capacity at a linkage ratio of 20% or above receive priority grid-connection arrangements; unused peak-shaving resources may be traded intra-provincially to other power generation enterprises, generating additional revenue."
        ),
        monitoring=(
            "Grid dispatch agencies conduct dispatch tests on peak-shaving and energy storage projects from time to time to ensure that peak-shaving capacity is genuinely available. Provincial (autonomous region, municipal) Development and Reform Commissions and energy authorities supervise the implementation in their respective jurisdictions. The National Development and Reform Commission and the National Energy Administration track progress across all regions and commission third-party evaluations as appropriate."
        ),
        sanctions=(
            "Enterprises making false commitments or failing to fulfil commitments shall have their peak-shaving capacity deducted at twice the uncompleted amount and be ordered to rectify within a prescribed period; those failing to complete rectification on time shall be disqualified from self-assuming renewable energy consumption responsibility in the following year."
        ),
        ghg_abs=(
            "N/A (this instrument is a voluntary target mechanism; it indirectly promotes emission reductions by increasing the grid-connected scale of renewable energy; the volume of GHG emissions covered depends on the actual scale of voluntary enterprise participation and new peak-shaving capacity, with no directly quantifiable fixed coverage)"
        ),
        ghg_pct="N/A (this instrument is a voluntary tool; the share of GHG emissions covered depends on voluntary uptake)",
        isic="D35",
        ghg="CO2",
        mitigation_effect="Positive",
        co_benefits="Renewable energy development; Technological innovation",
        legal_name=(
            "Notice of the National Development and Reform Commission and the National Energy Administration on Encouraging Renewable Energy Power Generation Enterprises to Self-Build or Purchase Peak-Shaving Capacity to Increase Grid-Connected Scale (Fa Gai Yun Xing [2021] No. 1138)"
        ),
        legal_url="https://www.ndrc.gov.cn/xwdt/tzgg/202108/t20210810_1293397_ext.html",
        other_links="N/A",
    ),
]


def _load_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def _write_rows(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main():
    for row in ROWS:
        if len(row) != 50:
            print(f"ERROR: {row[0]} has {len(row)} columns, expected 50")
            return 1

    existing = _load_rows(CSV_PATH)
    header, data = existing[0], existing[1:]

    inserted = 0
    updated = 0
    for row in ROWS:
        pid = row[0]
        existing_idx = next((i for i, r in enumerate(data) if r and r[0] == pid), None)
        if existing_idx is not None:
            if data[existing_idx] != list(row):
                data[existing_idx] = list(row)
                updated += 1
                print(f"  Updated {pid} in place at EN data index {existing_idx}")
            else:
                print(f"  {pid} already up to date in EN CSV — skipping")
            continue

        # Insert at the same position as CN CSV
        # VLB rows: after last VLB row
        # VID rows: after last VII non-VLB row (VCN) and before VLB rows
        insert_pos = len(data)

        if pid.startswith("CHNVIIVLB"):
            # VLB: insert after last VLB
            for i in range(len(data)):
                if data[i] and data[i][3] == "Voluntary certification and labelling scheme":
                    insert_pos = i + 1
        elif pid.startswith("CHNVIIVID"):
            # VID: insert after last VID or after last VII non-VLB (VCN)
            for i in range(len(data)):
                if data[i] and data[i][2] == "Voluntary information instrument":
                    app = data[i][3]
                    if app in ("Sustainable finance taxonomy",
                               "Voluntary procurement guidance",
                               "Voluntary carbon neutrality methodology",
                               "Voluntary information disclosure"):
                        insert_pos = i + 1
        elif pid.startswith("CHNVTGVTG"):
            # VTG: insert after last VTG row, or at end if none
            for i in range(len(data)):
                if data[i] and data[i][2] == "Voluntary target":
                    insert_pos = i + 1

        data.insert(insert_pos, list(row))
        inserted += 1
        print(f"  Inserted {pid} at EN data index {insert_pos}")

    _write_rows(CSV_PATH, [header] + data)
    print(f"Wrote {CSV_PATH} ({len(data)} data rows, {inserted} inserted, {updated} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
