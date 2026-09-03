"""
Add missing English translations for Economic Instruments Trading System fields.
Modifies generate_english_from_chinese.py ROW_TRANSLATIONS in-place.
"""

import re

# ---- Translation data ----

# For instruments that already have ROW_TRANSLATIONS entries: just add missing fields
MISSING_FIELDS = {
    # REC instruments
    "CHNTRARECI02S000": {
        "Functioning channel": "Demand-side",
        "Intensity (Value)": (
            "Provincial-level annual minimum and incentive renewable electricity "
            "consumption responsibility weights; the consumption amount of each "
            "obligated entity is calculated as its annual electricity sold or "
            "consumed multiplied by its assigned provincial weight."
        ),
        "Intensity (Unit)": "Annual renewable electricity as a share of total electricity consumption (%)",
        "Trading System: Type": "Renewable electricity consumption quota / Renewables Portfolio Standard (RPS) mechanism",
        "Trading System: cap": (
            "Annual consumption responsibility weights are set by provincial-level "
            "administrative region; not a GHG emissions cap."
        ),
        "Trading System: allowance mechanism": (
            "The energy authority of the State Council calculates and issues "
            "provincial consumption responsibility weights annually. Provincial "
            "energy authorities, together with relevant departments, formulate "
            "implementation plans and allocate consumption amounts to obligated "
            "market entities."
        ),
        "Trading System: Free Allowance": (
            "N/A; this system allocates renewable electricity consumption "
            "responsibilities, not free emission allowances."
        ),
        "Trading System: Offset use allowed": (
            "N/A; GECs and excess consumption amounts are used to fulfil "
            "renewable electricity consumption responsibilities, not as "
            "GHG emission offsets."
        ),
        "Trading System: Linkages": (
            "Interconnects with the renewable energy green electricity "
            "certificate market (CHNTRARECI01S000), electricity trading "
            "institutions, and the cross-provincial excess consumption "
            "amount transfer or trading organised by Beijing Power Exchange "
            "Center and Guangzhou Power Exchange Center."
        ),
        "Trading System: market stabilisation mechanism": (
            "The State monitors and evaluates by provincial administrative "
            "region. Where renewable electricity generation is significantly "
            "reduced or transmission constrained due to natural reasons or "
            "major incidents, corresponding deductions are made in "
            "monitoring, evaluation and entity assessment."
        ),
        "Trading System: penalties for non-compliance": (
            "Market entities failing to fulfil consumption responsibilities "
            "are ordered by provincial energy authorities, together with "
            "economic operation authorities, to rectify within a prescribed "
            "period. Entities failing to complete rectification on time are "
            "dealt with according to law and regulation, entered into adverse "
            "credit records and subject to joint disciplinary sanctions."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": "Air pollution mitigation; Energy security",
    },

    "CHNTRARECI03S000": {
        "Functioning channel": "Demand-side",
        "Intensity (Value)": (
            "Annual minimum renewable energy consumption proportion targets for "
            "key energy-using industries; specific minimum proportion values are "
            "determined by relevant departments by industry classification."
        ),
        "Intensity (Unit)": "Annual renewable energy consumption proportion (%)",
        "Trading System: Type": (
            "Renewable electricity consumption quota / RPS mechanism — "
            "minimum proportion targets for key energy-using industries"
        ),
        "Trading System: cap": (
            "Annual minimum renewable energy consumption proportion targets "
            "for key energy-using industries; not a GHG emissions cap."
        ),
        "Trading System: allowance mechanism": (
            "The energy authority of the State Council, together with relevant "
            "departments, determines and issues annual minimum renewable energy "
            "consumption proportion targets for key energy-using industries. "
            "Provincial relevant authorities, together with relevant departments, "
            "decompose and allocate targets to enterprises in key energy-using "
            "industries."
        ),
        "Trading System: Free Allowance": (
            "N/A; this system allocates renewable energy consumption minimum "
            "proportion targets, not free emission allowances."
        ),
        "Trading System: Offset use allowed": (
            "N/A; GECs and excess consumption amounts are used to fulfil "
            "renewable energy consumption proportion targets, not as "
            "GHG emission offsets."
        ),
        "Trading System: penalties for non-compliance": (
            "Enterprises failing to meet minimum proportion targets are "
            "ordered by provincial relevant authorities to rectify within "
            "a prescribed period. Enterprises failing to complete rectification "
            "on time are dealt with according to law and regulation, entered "
            "into adverse credit records and subject to joint disciplinary "
            "sanctions."
        ),
    },

    # ETS instruments - add missing Trading System fields
    "CHNTRAETSI01S000": {
        "Functioning channel": "Supply-side",
        "Intensity (Value)": "69.30",
        "Intensity (Unit)": "CNY/tonne",
        "Trading System: Type": (
            "Carbon emission allowance trading system. Trading methods "
            "include agreement transfer, one-way bidding and other "
            "prescribed methods."
        ),
        "Trading System: cap": (
            "The Ministry of Ecology and Environment formulates the "
            "total allowance determination and allocation plan based on "
            "national GHG emission control requirements, taking into "
            "account economic growth, industrial restructuring, energy "
            "mix optimisation, coordinated control of air pollutant "
            "emissions and other factors. A fixed absolute total quantity "
            "is not specified in the legal text."
        ),
        "Trading System: allowance mechanism": (
            "MEE formulates the total allowance determination and allocation "
            "plan. Provincial ecology and environment authorities allocate "
            "annual carbon emission allowances to key emitting entities. "
            "Allowance allocation is primarily free of charge; paid allocation "
            "may be introduced in due course according to national requirements."
        ),
        "Trading System: Free Allowance": (
            "Primarily free allocation; paid allocation may be introduced "
            "in due course according to national requirements. The specific "
            "free allowance proportion is not found in the legal text."
        ),
        "Trading System: Offset use allowed": (
            "Allowed. China Certified Emission Reductions (CCERs) may be "
            "used to offset allowance surrender, capped at 5% of allowances "
            "due. Emission reduction projects already covered by the national "
            "carbon market allowance management may not be used for offsetting."
        ),
        "Trading System: Linkages": (
            "N/A; key emitting entities covered by the national carbon market "
            "no longer participate in local pilot carbon emission trading markets."
        ),
        "Trading System: market stabilisation mechanism": (
            "Trading institutions shall take effective measures to prevent "
            "excessive speculation and maintain healthy market development. "
            "Registration and trading institutions shall establish risk "
            "management and information disclosure systems. Allowances "
            "voluntarily cancelled for public welfare purposes are deducted "
            "from the national total allowance quantity."
        ),
        "Trading System: revenue (annual)": (
            "CNY 18.11 billion (2024 annual transaction value; "
            "Source: MEE Progress Report of China’s National "
            "Carbon Market (2025))"
        ),
        "Trading System: Volume": (
            "189 million tonnes (2024; Source: MEE Progress Report of "
            "China’s National Carbon Market (2025))"
        ),
        "Trading System: penalties for non-compliance": (
            "Failure to surrender allowances in full and on time: ordered "
            "to rectify, fined CNY 20,000–30,000; if not rectified on "
            "time, the shortfall is deducted from the next year’s "
            "allowances. False reporting, concealment or refusal to fulfil "
            "emission reporting obligations: fined CNY 10,000–30,000, "
            "and the falsely reported or concealed portion may be deducted "
            "from the next year’s allowances."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": "Air pollution mitigation",
    },

    "CHNTRAETSI01S001": {
        "Functioning channel": "Supply-side",
        "Intensity (Value)": "69.30",
        "Intensity (Unit)": "CNY/tonne",
        "Trading System: Type": "Carbon emission allowance trading system",
        "Trading System: cap": (
            "Determined by the MEE total allowance determination and "
            "allocation plan; sector-level annual totals require "
            "consultation of specific annual allocation plans."
        ),
        "Trading System: allowance mechanism": (
            "MEE formulates the total allowance determination and allocation "
            "plan. Provincial ecology and environment authorities allocate "
            "annual allowances to key emitting entities in the power "
            "generation sector, primarily free of charge."
        ),
        "Trading System: Free Allowance": (
            "Primarily free allocation; the specific sector-level annual "
            "free allowance proportion requires consultation of annual "
            "allocation plans."
        ),
        "Trading System: Offset use allowed": (
            "CCERs may be used for offsetting, capped at 5% of allowances due."
        ),
        "Trading System: Linkages": (
            "N/A; key emitting entities covered by the national carbon market "
            "no longer participate in local pilot carbon emission trading markets."
        ),
        "Trading System: market stabilisation mechanism": (
            "Registration, trading, risk management and information "
            "disclosure systems apply the unified national carbon market rules."
        ),
        "Trading System: penalties for non-compliance": (
            "Subject to the unified national carbon market penalty rules."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": "Air pollution mitigation",
    },

    "CHNTRAETSI01S002": {
        "Functioning channel": "Supply-side",
        "Intensity (Value)": "69.30",
        "Intensity (Unit)": "CNY/tonne",
        "Trading System: Type": "Carbon emission allowance trading system",
        "Trading System: cap": (
            "Determined by the MEE total allowance determination and "
            "allocation plan; sector-level annual totals require "
            "consultation of specific annual allocation plans."
        ),
        "Trading System: allowance mechanism": (
            "MEE formulates the total allowance determination and allocation "
            "plan. Provincial ecology and environment authorities allocate "
            "annual allowances to key emitting entities in the steel sector, "
            "primarily free of charge."
        ),
        "Trading System: Free Allowance": (
            "Primarily free allocation; the specific sector-level annual "
            "free allowance proportion requires consultation of annual "
            "allocation plans."
        ),
        "Trading System: Offset use allowed": (
            "CCERs may be used for offsetting, capped at 5% of allowances due."
        ),
        "Trading System: Linkages": (
            "N/A; key emitting entities covered by the national carbon market "
            "no longer participate in local pilot carbon emission trading markets."
        ),
        "Trading System: market stabilisation mechanism": (
            "Registration, trading, risk management and information "
            "disclosure systems apply the unified national carbon market rules."
        ),
        "Trading System: penalties for non-compliance": (
            "Subject to the unified national carbon market penalty rules."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": "Air pollution mitigation",
    },

    "CHNTRAETSI01S003": {
        "Functioning channel": "Supply-side",
        "Intensity (Value)": "69.30",
        "Intensity (Unit)": "CNY/tonne",
        "Trading System: Type": "Carbon emission allowance trading system",
        "Trading System: cap": (
            "Determined by the MEE total allowance determination and "
            "allocation plan; sector-level annual totals require "
            "consultation of specific annual allocation plans."
        ),
        "Trading System: allowance mechanism": (
            "MEE formulates the total allowance determination and allocation "
            "plan. Provincial ecology and environment authorities allocate "
            "annual allowances to key emitting entities in the cement sector, "
            "primarily free of charge."
        ),
        "Trading System: Free Allowance": (
            "Primarily free allocation; the specific sector-level annual "
            "free allowance proportion requires consultation of annual "
            "allocation plans."
        ),
        "Trading System: Offset use allowed": (
            "CCERs may be used for offsetting, capped at 5% of allowances due."
        ),
        "Trading System: Linkages": (
            "N/A; key emitting entities covered by the national carbon market "
            "no longer participate in local pilot carbon emission trading markets."
        ),
        "Trading System: market stabilisation mechanism": (
            "Registration, trading, risk management and information "
            "disclosure systems apply the unified national carbon market rules."
        ),
        "Trading System: penalties for non-compliance": (
            "Subject to the unified national carbon market penalty rules."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": "Air pollution mitigation",
    },

    "CHNTRAETSI01S004": {
        "Functioning channel": "Supply-side",
        "Intensity (Value)": "69.30",
        "Intensity (Unit)": "CNY/tonne",
        "Trading System: Type": "Carbon emission allowance trading system",
        "Trading System: cap": (
            "Determined by the MEE total allowance determination and "
            "allocation plan; sector-level annual totals require "
            "consultation of specific annual allocation plans."
        ),
        "Trading System: allowance mechanism": (
            "MEE formulates the total allowance determination and allocation "
            "plan. Provincial ecology and environment authorities allocate "
            "annual allowances to key emitting entities in the aluminum "
            "smelting sector, primarily free of charge."
        ),
        "Trading System: Free Allowance": (
            "Primarily free allocation; the specific sector-level annual "
            "free allowance proportion requires consultation of annual "
            "allocation plans."
        ),
        "Trading System: Offset use allowed": (
            "CCERs may be used for offsetting, capped at 5% of allowances due."
        ),
        "Trading System: Linkages": (
            "N/A; key emitting entities covered by the national carbon market "
            "no longer participate in local pilot carbon emission trading markets."
        ),
        "Trading System: market stabilisation mechanism": (
            "Registration, trading, risk management and information "
            "disclosure systems apply the unified national carbon market rules."
        ),
        "Trading System: penalties for non-compliance": (
            "Subject to the unified national carbon market penalty rules."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": "Air pollution mitigation",
    },
}

# Instruments that need entirely new ROW_TRANSLATIONS entries
NEW_ENTRIES = {
    "CHNTRARECI01S000": {
        "Policy Instrument ID": "CHNTRARECI01S000",
        "Functioning channel": "Supply-side; Demand-side",
        "Intensity (Value)": "5.57",
        "Intensity (Unit)": "CNY/GEC",
        "Trading System: Type": "Tradable renewable electricity certificate market",
        "Trading System: cap": (
            "N/A; GEC issuance volume is determined by the quantity of "
            "eligible renewable electricity generation and is not subject "
            "to a fixed emissions cap."
        ),
        "Trading System: allowance mechanism": (
            "Based on monthly settled electricity volumes provided by grid "
            "enterprises and electricity trading institutions, GECs are "
            "uniformly and automatically issued in monthly batches for "
            "registered renewable electricity generation projects. GECs "
            "circulate through a nationally unified GEC trading system, "
            "GEC trading platforms and electricity trading institutions."
        ),
        "Trading System: Free Allowance": (
            "N/A; this instrument issues certificates for the environmental "
            "attributes of renewable electricity, not free emission allowances."
        ),
        "Trading System: Offset use allowed": (
            "N/A; GECs are used for renewable electricity production and "
            "consumption certification, not as GHG emission offsets."
        ),
        "Trading System: Linkages": (
            "Linked with green electricity trading, renewable electricity "
            "consumption responsibility weight accounting, green electricity "
            "consumption certification, corporate carbon emission accounting "
            "and key product carbon footprint accounting."
        ),
        "Trading System: market stabilisation mechanism": (
            "Through full-lifecycle closed-loop management, cancellation "
            "mechanisms, GEC price monitoring and price index studies, "
            "guides GEC prices to reasonably reflect the environmental "
            "value of green electricity and reduces risks of double "
            "counting and double claiming."
        ),
        "Trading System: Volume": (
            "930 million GECs (national GEC transactions in 2025; "
            "comprising 680 million separately traded GECs and 250 million "
            "green electricity trading GECs; Source: National Energy "
            "Administration 2026 press release)."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": "Air pollution mitigation; Energy security; Technological innovation",
    },

    "CHNTRATPSI01S000": {
        "Policy Instrument ID": "CHNTRATPSI01S000",
        "Functioning channel": "Supply-side",
        "Trading System: Type": (
            "Tradable performance standard; parallel management mechanism "
            "for passenger vehicle corporate average fuel consumption "
            "credits and new energy vehicle credits."
        ),
        "Trading System: cap": (
            "No fixed absolute cap is set; compliance obligations are "
            "jointly determined by corporate fuel consumption compliance "
            "values, NEV credit ratio requirements and enterprise "
            "production/import volumes."
        ),
        "Trading System: allowance mechanism": (
            "Credits are calculated from vehicle model fuel consumption "
            "performance, NEV model credits and annual production/import "
            "volumes. Positive credits may be carried forward, transferred, "
            "traded or deposited into the credit pool in accordance with "
            "the measures."
        ),
        "Trading System: Free Allowance": (
            "N/A; this system does not allocate free allowances; credits "
            "are generated from enterprise performance calculations."
        ),
        "Trading System: Offset use allowed": (
            "Allowed. CAFC negative credits may be offset using CAFC "
            "positive credits and NEV positive credits in accordance with "
            "the rules. NEV negative credits are primarily offset through "
            "the purchase of NEV positive credits."
        ),
        "Trading System: market stabilisation mechanism": (
            "The 2023 revision established a NEV credit pool management "
            "system. CAFC positive credits are also subject to carry-forward "
            "and affiliated enterprise transfer rules."
        ),
        "Trading System: penalties for non-compliance": (
            "Enterprises with negative credits not fully offset to zero "
            "must submit an adjustment plan and may be subject to "
            "restrictions on vehicle model notification, product filing "
            "or import management. Falsification, refusal to cooperate "
            "with verification and other violations are dealt with in "
            "accordance with the measures."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": (
            "Air pollution mitigation; Energy supply security; "
            "Technological innovation; Industrial development"
        ),
    },

    "CHNTRATPSI01S001": {
        "Policy Instrument ID": "CHNTRATPSI01S001",
        "Functioning channel": "Supply-side",
        "Intensity (Unit)": "L/100 km",
        "Trading System: Type": "CAFC tradable/transferable performance credit subscheme",
        "Trading System: cap": (
            "No fixed absolute cap is set; enterprise obligations are "
            "determined by the corporate average fuel consumption "
            "compliance value and enterprise production/import volumes."
        ),
        "Trading System: allowance mechanism": (
            "CAFC positive/negative credits are calculated from the "
            "difference between corporate average fuel consumption "
            "compliance values and actual values. Positive credits "
            "may be carried forward or transferred between affiliated "
            "enterprises."
        ),
        "Trading System: Free Allowance": (
            "N/A; credits are generated from enterprise fuel consumption "
            "performance calculations."
        ),
        "Trading System: Offset use allowed": (
            "Allowed. CAFC negative credits may be offset using the "
            "enterprise’s own carried-forward or transferred CAFC "
            "positive credits and NEV positive credits."
        ),
        "Trading System: Linkages": (
            "Linked with the NEV credit subscheme; NEV positive credits "
            "may be used to offset CAFC negative credits."
        ),
        "Trading System: market stabilisation mechanism": (
            "CAFC positive credits are subject to carry-forward and "
            "affiliated enterprise transfer rules; negative credits "
            "may be offset by NEV positive credits."
        ),
        "Trading System: penalties for non-compliance": (
            "Enterprises with CAFC negative credits not fully offset "
            "to zero must submit an adjustment plan and may be subject "
            "to restrictions on vehicle model notification, product "
            "filing or import management."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": "Air pollution mitigation; Energy supply security; Technological innovation",
    },

    "CHNTRATPSI01S002": {
        "Policy Instrument ID": "CHNTRATPSI01S002",
        "Functioning channel": "Supply-side",
        "Intensity (Value)": "48; 58",
        "Intensity (Unit)": "As a share of the accounting quantity of conventional energy passenger vehicles",
        "Trading System: Type": "NEV tradable performance credit subscheme",
        "Trading System: cap": (
            "No fixed absolute cap is set; annual targets are determined "
            "by the accounting quantity of conventional energy passenger "
            "vehicles and the NEV credit ratio requirement."
        ),
        "Trading System: allowance mechanism": (
            "NEV positive/negative credits are calculated from enterprise "
            "NEV model credits and production/import volumes. NEV positive "
            "credits are tradable and may be deposited into or withdrawn "
            "from the credit pool in accordance with the rules."
        ),
        "Trading System: Free Allowance": (
            "N/A; credits are generated from enterprise NEV production/import "
            "performance calculations."
        ),
        "Trading System: Offset use allowed": (
            "Allowed. NEV negative credits are offset through the purchase "
            "of NEV positive credits and other means. NEV positive credits "
            "may also be used to offset CAFC negative credits."
        ),
        "Trading System: Linkages": (
            "Linked with the CAFC credit subscheme; NEV positive credits "
            "may be used to offset CAFC negative credits."
        ),
        "Trading System: market stabilisation mechanism": (
            "The 2023 revision established a NEV credit pool management "
            "system to regulate credit supply and demand."
        ),
        "Trading System: penalties for non-compliance": (
            "Enterprises with NEV negative credits not fully offset "
            "to zero must submit an adjustment plan and may be subject "
            "to restrictions on vehicle model notification, product "
            "filing or import management."
        ),
        "Mitigation effects": "Positive",
        "Mitigation co-benefits": (
            "Air pollution mitigation; Energy supply security; "
            "Technological innovation; Industrial development"
        ),
    },
}


def format_value(key, value):
    """Format a dict value as Python code."""
    if isinstance(value, tuple):
        # Multi-line string continuation
        return f'"{value}"' if len(value) < 80 else f'(\n            {" ".join(f"{v}" for v in value)}\n        )'
    elif isinstance(value, str):
        if len(value) <= 80:
            return f'"{value}"'
        else:
            # Break long strings
            return f'"{value}"'
    return repr(value)


def format_field(key, value):
    """Format a single field for insertion into ROW_TRANSLATIONS."""
    indent = "        "
    if isinstance(value, str) and len(value) > 80:
        # Multi-line string continuation
        words = value.split()
        lines = []
        current = ""
        for word in words:
            test = current + " " + word if current else word
            if len(test) <= 100:
                current = test
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        result = f'{indent}"{key}": (\n'
        for line in lines:
            result += f'{indent}    "{line}"\n'
        result += f'{indent}),'
        return result
    else:
        return f'{indent}"{key}": "{value}",'


def build_entry_lines(pid, fields):
    """Build lines for a complete ROW_TRANSLATIONS entry."""
    lines = []
    lines.append(f'    "{pid}": {{')
    for key, value in fields.items():
        if isinstance(value, str) and len(value) > 80:
            # Multi-line string continuation with word wrapping
            words = value.split()
            wrapped_lines = []
            current = ""
            for word in words:
                test = current + " " + word if current else word
                if len(test) <= 100:
                    current = test
                else:
                    wrapped_lines.append(current)
                    current = word
            if current:
                wrapped_lines.append(current)

            lines.append(f'        "{key}": (')
            for wl in wrapped_lines:
                lines.append(f'            "{wl}"')
            lines.append(f'        ),')
        else:
            lines.append(f'        "{key}": "{value}",')
    lines.append(f'    }},')
    return lines


def build_missing_fields_lines(fields):
    """Build lines for fields to add to an existing entry."""
    lines = []
    for key, value in fields.items():
        if isinstance(value, str) and len(value) > 80:
            words = value.split()
            wrapped_lines = []
            current = ""
            for word in words:
                test = current + " " + word if current else word
                if len(test) <= 100:
                    current = test
                else:
                    wrapped_lines.append(current)
                    current = word
            if current:
                wrapped_lines.append(current)

            lines.append(f'        "{key}": (')
            for wl in wrapped_lines:
                lines.append(f'            "{wl}"')
            lines.append(f'        ),')
        else:
            lines.append(f'        "{key}": "{value}",')
    return lines


def main():
    with open('scripts/generate_english_from_chinese.py', 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    # Phase 1: Find and update existing entries (add missing fields)
    for pid, fields in MISSING_FIELDS.items():
        # Find the PID key line
        pid_pattern = f'    "{pid}": {{'
        pid_line = None
        for i, line in enumerate(lines):
            if line.strip() == pid_pattern.strip():
                pid_line = i
                break

        if pid_line is None:
            print(f"WARNING: {pid} not found in ROW_TRANSLATIONS, skipping")
            continue

        # Find the closing brace of this entry
        # Track brace depth
        brace_depth = 0
        in_dict = False
        close_line = None
        for i in range(pid_line, len(lines)):
            stripped = lines[i].strip()
            if stripped == pid_pattern.strip():
                in_dict = True
                brace_depth = 1
                continue
            if in_dict:
                # Count braces
                brace_depth += stripped.count('{') - stripped.count('}')
                if brace_depth == 0:
                    close_line = i
                    break

        if close_line is None:
            print(f"WARNING: could not find closing brace for {pid}")
            continue

        # Build the new field lines
        new_field_lines = build_missing_fields_lines(fields)

        # Insert before the closing brace
        indent = "        "
        insert_at = close_line
        for field_line in reversed(new_field_lines):
            lines.insert(insert_at, field_line)

        # Add blank line before closing if needed
        if lines[insert_at - 1].strip() != '':
            lines.insert(insert_at, '')

        print(f"Updated {pid}: added {len(fields)} fields")

    # Phase 2: Insert new entries
    # Find insertion points in alphabetical order
    for pid, fields in NEW_ENTRIES.items():
        # Find where this PID should go alphabetically
        insert_at = None
        for i, line in enumerate(lines):
            match = re.match(r'^\s*"CHN[A-Z]{3,5}I\d{2}S\d{3}":\s*\{', line)
            if match:
                existing_pid = match.group().split('"')[1]
                if existing_pid > pid:
                    insert_at = i
                    break

        if insert_at is None:
            print(f"WARNING: could not find insertion point for {pid}")
            continue

        # Find the start of this entry (go back to the blank line before it)
        while insert_at > 0 and lines[insert_at - 1].strip() != '':
            insert_at -= 1
        # Go back past blank lines to find the end of previous entry
        while insert_at > 0 and lines[insert_at - 1].strip() == '':
            insert_at -= 1
        # Now go forward to find the actual blank line before the next entry
        while insert_at < len(lines) and lines[insert_at].strip() != '':
            insert_at += 1
        insert_at += 1  # Start after the blank line

        entry_lines = build_entry_lines(pid, fields)
        for el in reversed(entry_lines):
            lines.insert(insert_at, el)
        # Add trailing blank lines
        lines.insert(insert_at + len(entry_lines), '')
        lines.insert(insert_at + len(entry_lines) + 1, '')

        print(f"Inserted new entry for {pid}: {len(fields)} fields")

    # Write back
    with open('scripts/generate_english_from_chinese.py', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print("\nDone. All entries updated.")

if __name__ == '__main__':
    main()
