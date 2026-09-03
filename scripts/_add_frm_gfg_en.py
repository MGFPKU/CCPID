"""Insert English row for CHNFRMGFGI01S000 into EN regulatory CSV.

Run from repo root:
    python scripts/_add_frm_gfg_en.py
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "CCPID_en_regulatory_instruments.csv"

PID = "CHNFRMGFGI01S000"

ROW = [
    PID,
    "Instrument",
    "Framework regulation",
    "Green finance governance framework",
    "Cross-sectoral",
    "N/A",
    "银行业保险业绿色金融指引",
    "Green Finance Guidelines for Banking and Insurance",
    "N/A",
    (
        "The Green Finance Guidelines for Banking and Insurance is a green finance "
        "governance framework issued by the former China Banking and Insurance "
        "Regulatory Commission (CBIRC, now the National Financial Regulatory "
        "Administration, NFRA) requiring banking and insurance institutions to "
        "advance green finance strategically and integrate environmental, social "
        "and governance (ESG) risks into their comprehensive risk management "
        "systems. The Guidelines comprise 7 chapters and 36 articles with core "
        "institutional arrangements including: (1) Organisational management: "
        "the board of directors (or council) assumes primary responsibility for "
        "green finance, determines the green finance development strategy, with "
        "senior management setting objectives and mechanisms; (2) Policy framework "
        "and capacity building: ESG risk management policies and procedures covering "
        "all business lines and asset portfolios, with classified management and "
        "dynamic assessment of client ESG risks and list-based management for "
        "significant-risk clients; (3) Investment and financing process management: "
        "strengthening ESG factor compliance review in credit and investment due "
        "diligence, using contractual clauses to require clients to strengthen ESG "
        "risk management; (4) Internal control and disclosure: integrating green "
        "finance policy implementation into internal compliance inspection and audit, "
        "establishing a green finance performance evaluation system with incentives "
        "and sanctions. Institutions must establish and improve relevant internal "
        "management systems and procedures within one year of the Guidelines taking "
        "effect (i.e. by 1 June 2023)."
    ),
    (
        "Promote green finance development in banking and insurance; advance "
        "carbon peaking and carbon neutrality in an orderly manner; prevent and "
        "control environmental, social and governance (ESG) risks"
    ),
    "Indirect",
    "Environment",
    "CHN",
    "National",
    "N/A",
    "01/06/2022",
    "01/06/2022",
    "N/A",
    "N/A",
    "N/A",
    "In force",
    "National Financial Regulatory Administration (formerly China Banking and Insurance Regulatory Commission)",
    "Green finance assets",
    "Existing; New",
    (
        "Green-finance-related assets of banking and insurance institutions, "
        "including green credit (loans and trade finance for green and low-carbon "
        "projects and industries), green bonds (green bonds held or underwritten), "
        "green insurance (environmental pollution liability insurance, climate risk "
        "insurance and other green insurance products), and ESG investments (equity "
        "and debt investment assets where ESG factors are integrated into investment "
        "decisions). Coverage extends to the institution's entire on- and off-balance-sheet "
        "asset portfolio as the management unit."
    ),
    "N/A",
    "N/A",
    "Firms",
    (
        "Banking and insurance institutions legally established within the territory "
        "of the People's Republic of China, including development banks, policy banks, "
        "commercial banks, rural cooperative banks, rural credit cooperatives, "
        "insurance group (holding) companies, insurance companies, reinsurance "
        "companies, and insurance asset management companies. Institutions must "
        "establish and improve relevant internal management systems and procedures "
        "within one year of the Guidelines taking effect (by 1 June 2023). NFRA "
        "(formerly CBIRC) and its local offices are responsible for supervisory oversight."
    ),
    "Financing and investment",
    (
        "Green investment and financing activities of banking and insurance "
        "institutions, including green credit origination and management, green "
        "bond investment and underwriting, green insurance product development "
        "and underwriting, ESG investment decision-making and portfolio management, "
        "and the integration of ESG risks into the full process of credit and "
        "investment due diligence, compliance review, approval management, fund "
        "disbursement, and post-lending/post-investment management. Institutions "
        "must implement classified management and dynamic assessment of client "
        "ESG risks, apply list-based management for significant-risk clients, "
        "and use contractual clauses to require clients to strengthen their own "
        "ESG risk management."
    ),
    "N/A",
    "N/A",
    "N/A",
    (
        "(1) Banking and insurance institutions must advance green finance "
        "strategically and integrate ESG requirements into business management "
        "processes and comprehensive risk management systems; (2) The board of "
        "directors (or council) assumes primary responsibility for green finance, "
        "determines the green finance development strategy, and approves green "
        "finance objectives and reports prepared by senior management; (3) Establish "
        "ESG risk management policies and procedures covering all business lines "
        "and asset portfolios, with classified management and dynamic assessment "
        "of client ESG risks and list-based management for significant-risk clients; "
        "(4) Strengthen ESG factor compliance review and approval management in "
        "credit and investment due diligence, and use contractual clauses to require "
        "clients to strengthen ESG risk management; (5) Integrate green finance "
        "policy implementation into internal compliance inspection and audit, and "
        "establish a green finance performance evaluation system with incentives "
        "and sanctions; (6) Publicly disclose the green finance strategy and policy, "
        "and fully disclose green-finance-related information; (7) Institutions must "
        "establish and improve relevant internal management systems and procedures "
        "within one year of the Guidelines taking effect; (8) Supervisory authorities "
        "use the assessment results of green finance policy implementation as an "
        "important reference for supervisory ratings, institutional access, business "
        "access, and senior management performance evaluation."
    ),
    "N/A",
    "N/A",
    "Information reporting; Internal audit; Supervision and inspection",
    (
        "The National Financial Regulatory Administration and its local offices "
        "are responsible for supervisory assessment and inspection of banking and "
        "insurance institutions' implementation of green finance policies, and "
        "establish and improve off-site surveillance indicator systems. Institutions "
        "must integrate green finance policy implementation into internal compliance "
        "inspection and audit, and establish a green finance performance evaluation "
        "system. Institutions must publicly disclose their green finance strategy "
        "and policy, and fully disclose green-finance-related information. Supervisory "
        "authorities conduct ongoing monitoring of institutional implementation, "
        "with assessment results serving as an important reference for supervisory "
        "ratings, institutional access, business access, and senior management "
        "performance evaluation."
    ),
    "Compliance order; Administrative penalty; Rectification order",
    (
        "Where banking and insurance institutions fail to establish a green finance "
        "management system as required by the Guidelines, fail to integrate ESG "
        "factors into investment and financing process management, or fail to fulfil "
        "information disclosure obligations, NFRA and its local offices shall reflect "
        "this in supervisory ratings and urge rectification through supervisory "
        "interviews, risk alerts and other means. Where internal control management "
        "and compliance implementation fail to meet standards, appropriate supervisory "
        "measures shall be taken in accordance with laws and regulations. For "
        "institutions that seriously violate the requirements of the Guidelines, "
        "administrative penalties may be imposed under the Banking Supervision Law, "
        "Insurance Law and other relevant laws."
    ),
    "Supervisory rating linkage; Market incentives",
    (
        "Supervisory authorities use the assessment results of green finance policy "
        "implementation as an important reference for supervisory ratings, "
        "institutional access, business access and senior management performance "
        "evaluation, creating positive incentives. Banking and insurance institutions "
        "are encouraged to pursue product and service innovation in green finance "
        "and to use big data, blockchain, artificial intelligence and other "
        "technological tools to enhance green finance management. Institutions are "
        "guided to increase financial support for green, low-carbon and circular "
        "economy activities and to support green and low-carbon development under "
        "the Belt and Road Initiative. Through market-based use of supervisory "
        "assessment results, capital is steered towards green and low-carbon fields."
    ),
    "N/A",
    "N/A",
    "K64",
    "CO2; CH4; N2O",
    "Positive",
    "Green industry development; Energy consumption reduction; Technological innovation",
    "Notice of the China Banking and Insurance Regulatory Commission on Issuing the Green Finance Guidelines for Banking and Insurance (Yin Bao Jian Fa [2022] No. 15)",
    "https://www.gov.cn/zhengce/zhengceku/2022-06/03/content_5693849.htm",
    "N/A",
]


def _load_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def _write_rows(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main():
    existing = _load_rows(CSV_PATH)
    header, data = existing[0], existing[1:]

    if any(r[0] == PID for r in data):
        print(f"  {PID} already in EN CSV — skipping")
        return 0

    # Insert after last EPR row (same position as CN CSV)
    insert_pos = None
    for i in range(len(data) - 1, -1, -1):
        if data[i][2] == "Framework regulation" and data[i][0][6:9] == "EPR":
            insert_pos = i + 1
            break

    if insert_pos is None:
        print("ERROR: No EPR row found in EN CSV")
        return 1

    data.insert(insert_pos, ROW)
    _write_rows(CSV_PATH, [header] + data)
    print(f"  Inserted {PID} at EN data index {insert_pos}")
    print(f"Wrote {CSV_PATH} ({len(data)} data rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
