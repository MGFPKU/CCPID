"""One-shot: update generate_english_from_chinese.py for VOL->VII re-code and
add missing ROW_TRANSLATIONS fields."""
import sys

path = "scripts/generate_english_from_chinese.py"
with open(path, encoding="utf-8") as f:
    text = f.read()
lines = text.split("\n")
orig_count = text.count("CHNVOL")

# 1) VOL -> VII (prefix tuple + 6 ROW_TRANSLATIONS keys)
text = text.replace("CHNVOL", "CHNVII")
lines = text.split("\n")


def find_key(pid):
    for i, l in enumerate(lines):
        if l == '    "%s": {' % pid:
            return i
    raise SystemExit("key not found: %s" % pid)


def entry_end(key_idx, maxscan=500):
    for j in range(key_idx + 1, min(key_idx + maxscan, len(lines))):
        if lines[j] == "    },":
            return j
    raise SystemExit("no end for key at %d" % (key_idx + 1))


def assert_absent(key_idx, field):
    end = entry_end(key_idx)
    body = "\n".join(lines[key_idx:end])
    if '"%s"' % field in body:
        raise SystemExit("%s already present in entry at line %d" % (field, key_idx + 1))


def replace_in_entry(key_idx, old, new):
    end = entry_end(key_idx)
    for j in range(key_idx + 1, end):
        if lines[j] == old:
            lines[j] = new
            return
    raise SystemExit("line %r not found in entry at %d" % (old, key_idx + 1))


# 2) value fixes (global, unique strings)
n_end = text.count('"End date": "31/12/2025",')
assert n_end == 2, n_end
text = text.replace('"End date": "31/12/2025",', '"End date": "N/A",')
text = text.replace('"Asset (Other)": "",', '"Asset (Other)": "N/A",')
text = text.replace(
    '"Economic sector": "B; C; D; E",',
    '"Economic sector": "C13; C17; C19; C20; C23; C24; D35",')
text = text.replace(
    '"Economic sector": "B, C",',
    '"Economic sector": "C13; C17; C19; C20; C22; C23; C24",')
lines = text.split("\n")

C_ALL = "; ".join("C%02d" % i for i in range(10, 34))
for pid in ["CHNCBATGCI01S000", "CHNCBATGCI03S000"]:
    replace_in_entry(find_key(pid), '        "Economic sector": "C",',
                     '        "Economic sector": "%s",' % C_ALL)
replace_in_entry(find_key("CHNCBATGCI02S000"), '        "Economic sector": "C",',
                 '        "Economic sector": "C19; C20; C23; C24",')

# 3) VLBI Agent fields (insert as first field after opening brace)
for seq in ["01", "02", "04", "05", "06", "07"]:
    pid = "CHNVIIVLBI%sS000" % seq
    k = find_key(pid)
    assert_absent(k, "Agent")
    lines = lines[:k + 1] + ['        "Agent": "Firms",', ""] + lines[k + 1:]


# 4) field insertions at entry end
def field_block(field, wrapped_lines):
    body = ['        "%s": (' % field]
    body += ['            "%s "' % l for l in wrapped_lines[:-1]]
    body += ['            "%s"' % wrapped_lines[-1]]
    body += ["        ),"]
    return body


additions = {
    "CHNTRARECI03S000": [
        '        "Agent": "Firms",', "",
        '        "Activity": "Purchase or use; Production, generation or conversion",', "",
    ] + field_block("Intensity (Details)", [
        "Electricity minimum proportion targets are accounted through green certificates,",
        "covering renewable electricity consumption achieved by enterprises through",
        "self-generation for own use, green certificate/green electricity trading and",
        "transfers of excess consumption amounts. Non-electricity minimum proportion",
        "targets cover renewable heating/cooling, hydrogen/ammonia production,",
        "biomass-integrated fuel utilisation and other non-electricity uses",
        "(Source: NDRC Order No. 42 of 2026).",
    ]),
    "CHNTRATPSI01S001": field_block("Intensity (Details)", [
        "Enterprise-level intensity is calculated by weighting vehicle-model fuel",
        "consumption target values and actual values by production or import volume;",
        "the measures do not provide a single fixed intensity value.",
    ]),
    "CHNTRATPSI01S002": field_block("Intensity (Details)", [
        "The NEV credit proportion requirements for 2026 and 2027 are 48% and 58%",
        "respectively (Source: MIIT notice of 2025).",
    ]),
    "CHNPARCPAI01S000": field_block("Last revisions (Details)", [
        "These Measures were reviewed and approved at a meeting of the Standing",
        "Committee of the Political Bureau of the CPC Central Committee on 26 February",
        "2026, and issued by the General Office of the CPC Central Committee and the",
        "General Office of the State Council on 12 April 2026, with evaluation and",
        "assessment of all provinces (autonomous regions and municipalities) starting",
        "from the 2026 assessment year. This is the initial version.",
    ]),
    "CHNADPCPMI01S000": field_block("Requirement specification", [
        "Power generation enterprises and energy storage operators must provide",
        "available capacity according to dispatch instructions; the capacity tariff",
        "standards and assessment and settlement rules for each technology type are",
        "detailed in the subschemes. Capacity charges are recovered from all",
        "industrial and commercial users through system operation charges based on",
        "electricity consumption.",
    ]),
    "CHNTAXFETI01S000": field_block("Last revisions (Details)", [
        "On 13 January 2015, the Ministry of Finance and the State Taxation",
        "Administration issued Cai Shui [2015] No. 11, raising the unit tax on",
        "gasoline, naphtha, solvent oil and lubricating oil to CNY 1.52 per litre,",
        "and on diesel, aviation kerosene and fuel oil to CNY 1.20 per litre. This",
        "followed three earlier adjustments: the initial levy in 2009 (1.0/0.8 yuan",
        "per litre), the increase in November 2014 (1.12/0.94 yuan per litre) and the",
        "further increase in December 2014 (1.4/1.1 yuan per litre). Aviation",
        "kerosene remains temporarily exempt. Leaded gasoline ceased to be a separate",
        "tax item from 1 December 2014 and is taxed at the unleaded gasoline rate.",
    ]),
    "CHNTAXDVTI01S000": field_block("Last revisions (Details)", [
        "On 1 August 2008, the Ministry of Finance and the State Taxation",
        "Administration issued Cai Shui [2008] No. 105 on adjusting passenger vehicle",
        "consumption tax policy, effective from 1 September 2008. Main adjustments:",
        "the tax rate for passenger vehicles with cylinder capacity of 1.0L or less",
        "was lowered from 3% to 1%; the rate for 3.0-4.0L vehicles was raised from",
        "15% to 25%; and the rate for vehicles above 4.0L was raised from 20% to 40%.",
        "This was the second major adjustment after April 2006 and formed the",
        "seven-tier rate framework still in use today.",
    ]),
    "CHNTAXVOTI01S000": field_block("Last revisions (Details)", [
        "In May 2024, the Ministry of Industry and Information Technology, the",
        "Ministry of Finance and the State Taxation Administration jointly issued",
        "Announcement No. 10 of 2024, adjusting the technical requirements for",
        "energy-saving and new energy vehicle products eligible for vehicle and",
        "vessel tax preferences from 1 July 2024. The combined-cycle fuel consumption",
        "standards for energy-saving passenger vehicles and commercial vehicles, as",
        "well as the technical standards for new energy vehicles, were updated.",
    ]),
    "CHNTAXVOTI01S001": field_block("Last revisions (Details)", [
        "Announcement No. 10 of 2024, issued in May 2024, updated the technical",
        "standards for new energy vehicles from 1 July 2024.",
    ]),
    "CHNTAXVOTI01S002": field_block("Last revisions (Details)", [
        "Announcement No. 10 of 2024, issued in May 2024, updated the combined-cycle",
        "fuel consumption technical standards for energy-saving vehicles from",
        "1 July 2024.",
    ]),
    "CHNTAXVATI02S000": field_block("Last revisions (Details)", [
        "On 31 December 2021, the Ministry of Finance and the State Taxation",
        "Administration issued Announcement No. 40 of 2021, effective from 1 March",
        "2022, repealing and replacing the former Cai Shui [2015] No. 78. The new",
        "announcement unified the applicable rules for VAT general taxpayers and",
        "small-scale taxpayers, expanded the scope of some refund products, clarified",
        "refund conditions and supervision requirements, and adjusted the refund",
        "rates for some products in accordance with the law.",
    ]),
    "CHNTAXVATI03S000": field_block("Last revisions (Details)", [
        "Announcement No. 10 of 2026 by the Ministry of Finance and the State",
        "Taxation Administration (the supporting transition announcement for the",
        "implementation of the 2026 VAT Law), Article 2, clarifies that from",
        "1 January 2026 to 31 December 2027, the production and sale, wholesale and",
        "retail of organic fertiliser products continue to be exempt from VAT. The",
        "former indefinite exemption under Cai Shui [2008] No. 56 became a",
        "time-limited exemption. Whether the exemption will be further extended",
        "after expiry remains subject to future policy.",
    ]),
    "CHNTAXVATI04S000": field_block("Last revisions (Details)", [
        "On 17 October 2025, the Ministry of Finance, the General Administration of",
        "Customs and the State Taxation Administration jointly issued Announcement",
        "No. 10 of 2025, effective from 1 November 2025. The new announcement",
        "narrowed the 50% VAT immediate-refund policy from all wind power generation",
        "(Cai Shui [2015] No. 74) to offshore wind power generation only; onshore",
        "wind power no longer enjoys the preference. Cai Shui [2015] No. 74 was",
        "repealed on the same day.",
    ]),
}

checks = {
    "CHNTRARECI03S000": ["Agent", "Activity", "Intensity (Details)"],
    "CHNTRATPSI01S001": ["Intensity (Details)"],
    "CHNTRATPSI01S002": ["Intensity (Details)"],
    "CHNPARCPAI01S000": ["Last revisions (Details)"],
    "CHNADPCPMI01S000": ["Requirement specification"],
    "CHNTAXFETI01S000": ["Last revisions (Details)"],
    "CHNTAXDVTI01S000": ["Last revisions (Details)"],
    "CHNTAXVOTI01S000": ["Last revisions (Details)"],
    "CHNTAXVOTI01S001": ["Last revisions (Details)"],
    "CHNTAXVOTI01S002": ["Last revisions (Details)"],
    "CHNTAXVATI02S000": ["Last revisions (Details)"],
    "CHNTAXVATI03S000": ["Last revisions (Details)"],
    "CHNTAXVATI04S000": ["Last revisions (Details)"],
}
for pid, fields in checks.items():
    k = find_key(pid)
    for fld in fields:
        assert_absent(k, fld)
for pid, block in additions.items():
    k = find_key(pid)
    end = entry_end(k)
    lines = lines[:end] + [""] + block + lines[end:]

with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("generator edited; CHNVOL occurrences before:", orig_count)
