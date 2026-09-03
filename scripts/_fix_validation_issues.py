"""One-shot: fix remaining validation errors in outputs CSVs.

- gov RDDI03/04: End date 31/12/2025 -> N/A (status stays In force)
- blank cells -> N/A (weblinks, intensity value, Asset (Other), Agent, compliance detail fields)
- ISIC section-only letters -> division-level codes
- VOL -> VII instrument ID re-code (VLB rows in voluntary CSVs)
"""
import csv
from pathlib import Path

OUT = Path("outputs")

C_ALL = "; ".join(f"C{i:02d}" for i in range(10, 34))
B_ALL = "; ".join(f"B{i:02d}" for i in range(5, 10))
F_ALL = "; ".join(f"F{i:02d}" for i in range(41, 44))
E_ALL = "; ".join(f"E{i:02d}" for i in range(36, 40))

ISIC = {
    "CHNFRMITGI01S000": f"{B_ALL}; {C_ALL}; D35; {E_ALL}",
    "CHNFRMEEMI01S000": f"{B_ALL}; {C_ALL}; D35; {F_ALL}; H49",
    "CHNFRMTRSI01S000": f"{B_ALL}; {C_ALL}; D35; {F_ALL}; H49",
    "CHNFRMTRSI02S000": f"{B_ALL}; {C_ALL}; D35; {F_ALL}; H49",
    "CHNFRMTRSI03S000": f"{B_ALL}; {C_ALL}; D35; {F_ALL}; H49",
    "CHNFRMTRSI04S000": f"{B_ALL}; {C_ALL}; D35; {F_ALL}; H49",
    "CHNFRMPDPI01S000": "C13; C17; C19; C20; C23; C24; D35",
    "CHNFRMEPRI01S000": C_ALL,
    "CHNFRMEPRI02S000": "C26; C27; E38",
    "CHNPRFEILI01S000": "C13; C17; C19; C20; C22; C23; C24",
    "CHNCBATGCI01S000": C_ALL,
    "CHNCBATGCI02S000": "C19; C20; C23; C24",
    "CHNCBATGCI03S000": C_ALL,
    "CHNCBATGCI06S000": "C13; C17; C20; C21; C22; C27; C28; C29",
    "CHNCBAGSSI01S000": C_ALL,
    "CHNCBACBPI01S000": C_ALL,
    "CHNVIIVPGI01S000": C_ALL,
    "CHNVOLVLBI01S000": C_ALL,
    "CHNVOLVLBI03S000": "A01; C13; C17; C19; C20; C23; C24; C27; D35; O84; P85; Q86",
    "CHNVOLVLBI04S000": "C19; C20; C23; C24; D35; O84; P85; Q86",
    "CHNVOLVLBI05S000": C_ALL,
    "CHNVOLVLBI07S000": "C13; C24; C26; C27",
    "CHNVOLVLBI10S000": C_ALL,
}

changes = []


def edit_rows(path, id_col, edits, id_prefix=None):
    """edits: dict pid -> {col: (old, new)}. old may be None to accept any value."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())
    for r in rows:
        pid = r.get(id_col)
        if pid in edits:
            for col, (old, new) in edits[pid].items():
                cur = r.get(col, "")
                if old is not None and cur != old:
                    raise AssertionError(f"{path} {pid} [{col}]: expected {old!r}, got {cur!r}")
                if cur != new:
                    r[col] = new
                    changes.append((str(path), pid, col, cur, new))
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


# --- government I&C ---
edit_rows(
    OUT / "CCPID_cn_government_i_c.csv", "政策工具ID",
    {
        "CHNPIVRDDI03S000": {"终止日期": ("31/12/2025", "N/A"), "其他网页链接": ("", "N/A")},
        "CHNPIVRDDI04S000": {"终止日期": ("31/12/2025", "N/A"), "其他网页链接": ("", "N/A")},
        "CHNPIVRDDI05S000": {"其他网页链接": ("", "N/A"), "强度（数值）": ("", "N/A")},
    },
)
edit_rows(
    OUT / "CCPID_en_government_i_c.csv", "Policy Instrument ID",
    {
        "CHNPIVRDDI03S000": {"End date": ("31/12/2025", "N/A"), "Other weblinks": ("", "N/A")},
        "CHNPIVRDDI04S000": {"End date": ("31/12/2025", "N/A"), "Other weblinks": ("", "N/A")},
        "CHNPIVRDDI05S000": {"Other weblinks": ("", "N/A")},
        "CHNPIVCBII04S000": {"Asset (Other)": ("", "N/A")},
    },
)

# --- regulatory ---
edit_rows(
    OUT / "CCPID_cn_regulatory_instruments.csv", "政策工具ID",
    {"CHNTECODSI01S000": {"其他网页链接": ("", "N/A")}},
)
edit_rows(
    OUT / "CCPID_en_regulatory_instruments.csv", "Policy Instrument ID",
    {"CHNTECODSI01S000": {"Other weblinks": ("", "N/A")}},
)

# --- ISIC fixes (CN + EN mirrors) ---
reg_isic = {pid: {"经济行业": (None, val)} for pid, val in ISIC.items()
            if pid in ("CHNFRMITGI01S000", "CHNFRMEEMI01S000", "CHNFRMTRSI01S000",
                       "CHNFRMTRSI02S000", "CHNFRMTRSI03S000", "CHNFRMTRSI04S000",
                       "CHNFRMPDPI01S000", "CHNFRMEPRI01S000", "CHNFRMEPRI02S000",
                       "CHNPRFEILI01S000")}
info_isic = {pid: {"经济行业": (None, val)} for pid, val in ISIC.items()
             if pid in ("CHNCBATGCI01S000", "CHNCBATGCI02S000", "CHNCBATGCI03S000",
                        "CHNCBATGCI06S000", "CHNCBAGSSI01S000", "CHNCBACBPI01S000")}
vol_isic = {pid: {"经济行业": (None, val)} for pid, val in ISIC.items()
            if pid in ("CHNVIIVPGI01S000", "CHNVOLVLBI01S000", "CHNVOLVLBI03S000",
                       "CHNVOLVLBI04S000", "CHNVOLVLBI05S000", "CHNVOLVLBI07S000",
                       "CHNVOLVLBI10S000")}
for path, id_col, edits in [
    (OUT / "CCPID_cn_regulatory_instruments.csv", "政策工具ID", reg_isic),
    (OUT / "CCPID_en_regulatory_instruments.csv", "Policy Instrument ID",
     {p: {"Economic sector": v["经济行业"]} for p, v in reg_isic.items()}),
    (OUT / "CCPID_cn_information_instruments.csv", "政策工具ID", info_isic),
    (OUT / "CCPID_en_information_instruments.csv", "Policy Instrument ID",
     {p: {"Economic sector": v["经济行业"]} for p, v in info_isic.items()}),
    (OUT / "CCPID_cn_voluntary_approaches.csv", "政策工具ID", vol_isic),
    (OUT / "CCPID_en_voluntary_approaches.csv", "Policy Instrument ID",
     {p: {"Economic sector": v["经济行业"]} for p, v in vol_isic.items()}),
]:
    edit_rows(path, id_col, edits)

# --- EN voluntary: Agent blanks + compliance details N/A in EN information ---
edit_rows(
    OUT / "CCPID_en_voluntary_approaches.csv", "Policy Instrument ID",
    {pid: {"Agent": ("", "Firms")} for pid in
     ("CHNVOLVLBI01S000", "CHNVOLVLBI02S000", "CHNVOLVLBI04S000",
      "CHNVOLVLBI05S000", "CHNVOLVLBI06S000", "CHNVOLVLBI07S000")},
)
# EN information: CN template has no compliance-detail columns; blank cells are N/A
path = OUT / "CCPID_en_information_instruments.csv"
with open(path, encoding="utf-8-sig", newline="") as f:
    info_rows = list(csv.DictReader(f))
info_fieldnames = list(info_rows[0].keys())
for r in info_rows:
    for col in ("Compliance monitoring details", "Compliance enforcement details"):
        if r.get(col, "") == "":
            changes.append((str(path), r["Policy Instrument ID"], col, "", "N/A"))
            r[col] = "N/A"
with open(path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=info_fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(info_rows)

# --- VOL -> VII re-code in voluntary CSVs ---
for path, id_col in [
    (OUT / "CCPID_cn_voluntary_approaches.csv", "政策工具ID"),
    (OUT / "CCPID_en_voluntary_approaches.csv", "Policy Instrument ID"),
]:
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())
    for r in rows:
        for col, val in r.items():
            if col == id_col:
                continue
            assert "CHNVOL" not in (val or ""), f"{path} {id_col}={r[id_col]} col {col} contains CHNVOL"
        pid = r[id_col]
        if pid.startswith("CHNVOLVLBI"):
            new = "CHNVII" + pid[6:]
            r[id_col] = new
            changes.append((str(path), pid, id_col, pid, new))
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

print(f"{len(changes)} cell changes:")
for c in changes:
    print(" ", c[1], c[2], ":", repr(c[3])[:60], "->", repr(c[4])[:60])
