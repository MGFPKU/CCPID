"""One-shot: restore C30-C32 lost to the legacy GB/T remap, and extend the
industrial restructuring catalogue row to full economy coverage (A, F, H)."""
import csv

PIDS_CN = {
    "outputs/CCPID_cn_regulatory_instruments.csv": [
        "CHNFRMITGI01S000", "CHNFRMEEMI01S000", "CHNFRMEPRI01S000",
        "CHNFRMTRSI01S000", "CHNFRMTRSI02S000", "CHNFRMTRSI03S000",
        "CHNFRMTRSI04S000",
    ],
    "outputs/CCPID_cn_information_instruments.csv": [
        "CHNCBATGCI01S000", "CHNCBATGCI03S000", "CHNCBAGSSI01S000",
        "CHNCBACBPI01S000",
    ],
    "outputs/CCPID_cn_voluntary_approaches.csv": [
        "CHNVIIVPGI01S000", "CHNVIIVLBI01S000", "CHNVIIVLBI05S000",
        "CHNVIIVLBI10S000",
    ],
}
PIDS_EN = {
    "outputs/CCPID_en_regulatory_instruments.csv": PIDS_CN["outputs/CCPID_cn_regulatory_instruments.csv"],
    "outputs/CCPID_en_information_instruments.csv": PIDS_CN["outputs/CCPID_cn_information_instruments.csv"],
    "outputs/CCPID_en_voluntary_approaches.csv": PIDS_CN["outputs/CCPID_cn_voluntary_approaches.csv"],
}

CATALOGUE = "CHNFRMITGI01S000"
CATALOGUE_OLD = ("B05; B06; B07; B08; B09; C10; C11; C12; C13; C14; C15; C16; "
                 "C17; C18; C19; C20; C21; C22; C23; C24; C25; C26; C27; C28; "
                 "C29; C33; D35; E36; E37; E38; E39")
CATALOGUE_NEW = ("A01; A02; A03; " + CATALOGUE_OLD.replace("C29; C33", "C29; C30; C31; C32; C33")
                 + "; F41; F42; F43; H49; H50; H51; H52; H53")

changes = []


def run(files, id_col, col):
    for path, pids in files.items():
        with open(path, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        fieldnames = list(rows[0].keys())
        for r in rows:
            pid = r.get(id_col)
            if pid not in pids:
                continue
            old = r[col]
            if pid == CATALOGUE:
                assert old == CATALOGUE_OLD, (path, old)
                new = CATALOGUE_NEW
            else:
                assert "C29; C33" in old and "C30" not in old, (path, pid, old)
                new = old.replace("C29; C33", "C29; C30; C31; C32; C33")
            r[col] = new
            changes.append((path, pid, new))
        with open(path, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)


run(PIDS_CN, "政策工具ID", "经济行业")
run(PIDS_EN, "Policy Instrument ID", "Economic sector")

print(len(changes), "rows updated")
for path, pid, new in changes:
    print(" ", pid, "->", new if len(new) < 100 else new[:90] + "...")
