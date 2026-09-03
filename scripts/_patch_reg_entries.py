"""Patch regulatory instrument ROW_TRANSLATIONS entries with missing translated fields."""
import re

# Build translations from CN data
translations = {
    # 1. Asset (Status) fix
    "CHNFRMGFGI01S000": {
        "Asset (Status)": "New; Existing",
    },

    # 2. Mitigation effects
    "CHNPRFEILI01S000": {
        "Mitigation effects": "Positive",
    },

    # 3. Compliance monitoring (10 rows)
    "CHNPRFEILI03S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities and energy authorities carry out supervisory inspections "
            "on the implementation of energy intensity limit standards at coal-fired power generation "
            "enterprises. Enterprises must report energy resource data as required and are subject "
            "to energy conservation inspection and power sector regulation."
        ),
    },
    "CHNPRFEILI04S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities and energy authorities carry out supervisory inspections "
            "on the implementation of energy intensity limit standards at coal-to-coke enterprises. "
            "Enterprises must report energy resource data as required and are subject to energy "
            "conservation inspection."
        ),
    },
    "CHNPRFEILI05S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities and industry and information technology authorities carry "
            "out supervisory inspections on the implementation of energy intensity limit standards "
            "at iron and steel enterprises. Enterprises must report energy resource data as required "
            "and are subject to energy conservation inspection and industry regulation."
        ),
    },
    "CHNPRFEILI06S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities carry out supervisory inspections on the implementation "
            "of energy intensity limit standards at chemical fibre manufacturing enterprises. "
            "Enterprises must report energy resource data as required and are subject to energy "
            "conservation inspection."
        ),
    },
    "CHNPRFEILI07S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities and industry and information technology authorities carry "
            "out supervisory inspections on the implementation of energy intensity limit standards "
            "at coke and coal gas production enterprises. Enterprises must report energy resource "
            "data as required and are subject to energy conservation inspection and industry regulation."
        ),
    },
    "CHNPRFEILI08S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities carry out supervisory inspections on the implementation "
            "of energy intensity limit standards at graphite and fluorite production enterprises. "
            "Enterprises must report energy resource data as required and are subject to energy "
            "conservation inspection."
        ),
    },
    "CHNPRFEILI09S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities carry out supervisory inspections on the implementation "
            "of energy intensity limit standards at flat glass (including photovoltaic glass) "
            "enterprises. Enterprises must report energy resource data as required and are subject "
            "to energy conservation inspection."
        ),
    },
    "CHNPRFEILI10S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities carry out supervisory inspections on the implementation "
            "of energy intensity limit standards at beer production enterprises. Enterprises must "
            "report energy resource data as required and are subject to energy conservation inspection."
        ),
    },
    "CHNPRFEILI11S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities and energy authorities carry out supervisory inspections "
            "on the implementation of energy intensity limit standards at gas-fired power generation "
            "enterprises. Enterprises must report energy resource data as required and are subject "
            "to energy conservation inspection and power sector regulation."
        ),
    },
    "CHNPRFEILI12S000": {
        "Compliance monitoring": (
            "Supervisory inspections by government agencies; enterprise energy consumption data reporting"
        ),
        "Compliance monitoring (Details)": (
            "Market regulation authorities carry out supervisory inspections on the implementation "
            "of energy intensity limit standards at alumina production enterprises. Enterprises must "
            "report energy resource data as required and are subject to energy conservation inspection."
        ),
    },

    # 4. Compliance enforcement for 14 PIDs
    "CHNPRFMREI01S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell distribution transformers that do not meet the mandatory "
            "energy efficiency standards shall be ordered by the market regulation authorities "
            "to stop production and sale, with confiscation of illegal gains and imposition of "
            "fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMREI02S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell electric motor products that do not meet the mandatory "
            "energy efficiency standards shall be ordered by the market regulation authorities "
            "to stop production and sale, with confiscation of illegal gains and imposition of "
            "fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMITI01S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell industrial boiler products that do not meet the mandatory "
            "energy efficiency standards shall be ordered by the market regulation authorities "
            "to stop production and sale, with confiscation of illegal gains and imposition of "
            "fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMITI02S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell medium-frequency coreless induction furnace products that "
            "do not meet the mandatory energy efficiency standards shall be ordered by the market "
            "regulation authorities to stop production and sale, with confiscation of illegal gains "
            "and imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMITI03S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell petroleum industry heating furnace products that do not meet "
            "the mandatory energy efficiency standards shall be ordered by the market regulation "
            "authorities to stop production and sale, with confiscation of illegal gains and "
            "imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMWHI01S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell domestic solar water heating system products that do not meet "
            "the mandatory energy efficiency standards shall be ordered by the market regulation "
            "authorities to stop production and sale, with confiscation of illegal gains and "
            "imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMWHI02S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell domestic gas instantaneous water heaters and gas-fired "
            "heating and hot water combi-boiler products that do not meet the mandatory energy "
            "efficiency standards shall be ordered by the market regulation authorities to stop "
            "production and sale, with confiscation of illegal gains and imposition of fines; "
            "in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMWHI03S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell heat pump water heater products that do not meet the "
            "mandatory energy efficiency standards shall be ordered by the market regulation "
            "authorities to stop production and sale, with confiscation of illegal gains and "
            "imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMWHI04S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell storage-type electric water heater products that do not meet "
            "the mandatory energy efficiency standards shall be ordered by the market regulation "
            "authorities to stop production and sale, with confiscation of illegal gains and "
            "imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMHSI01S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell heat pump and solar water heater products that do not meet "
            "the mandatory energy efficiency standards shall be ordered by the market regulation "
            "authorities to stop production and sale, with confiscation of illegal gains and "
            "imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMCSI01S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell variable-speed air conditioner and heat pump products that "
            "do not meet the mandatory energy efficiency standards shall be ordered by the market "
            "regulation authorities to stop production and sale, with confiscation of illegal gains "
            "and imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMCSI02S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell fan and ventilator products that do not meet the mandatory "
            "energy efficiency standards shall be ordered by the market regulation authorities to "
            "stop production and sale, with confiscation of illegal gains and imposition of fines; "
            "in serious cases, business licences shall be revoked."
        ),
        "Compliance promotion": "Government financial support",
        "Compliance promotion (Details)": (
            "The State encourages the procurement and use of energy-efficient products with Grade 1 "
            "and Grade 2 energy efficiency labels, and promotes high-efficiency fan products through "
            "energy-saving product certification and energy conservation project promotion."
        ),
    },
    "CHNPRFMCSI03S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell unitary and split air conditioner products that do not meet "
            "the mandatory energy efficiency standards shall be ordered by the market regulation "
            "authorities to stop production and sale, with confiscation of illegal gains and "
            "imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },
    "CHNPRFMCSI04S000": {
        "Compliance enforcement": "Compliance requirements; Testing",
        "Compliance enforcement (Details)": (
            "Those who produce or sell unitary air conditioning unit products that do not meet "
            "the mandatory energy efficiency standards shall be ordered by the market regulation "
            "authorities to stop production and sale, with confiscation of illegal gains and "
            "imposition of fines; in serious cases, business licences shall be revoked."
        ),
    },

    # 5. Last revisions (Details) for 2 PIDs
    "CHNPRFMEAI30S000": {
        "Last revisions (Details)": (
            "First established on 18 December 2013 with GB 30255-2013 'Minimum Allowable Values "
            "of Energy Efficiency and Energy Efficiency Grades for Non-Directional Integrated LED "
            "Lamps for General Lighting', effective 1 September 2014. First revised in 2019 as "
            "GB 30255-2019, renamed 'Minimum Allowable Values of Energy Efficiency and Energy "
            "Efficiency Grades for Indoor Lighting LED Products', expanding product coverage. "
            "Second revision on 27 February 2026 as GB 30255-2026, covering small-sized LED "
            "downlights, LED spotlights, replacement double-capped LED lamps and smart dimming "
            "products, raising energy efficiency indicators, adding flicker requirements and a "
            "1.5 W standby power requirement, and establishing full-time energy efficiency "
            "assessment. Old standard has a 25-month transition period, with mandatory "
            "implementation of the new standard starting 1 September 2027."
        ),
    },
    "CHNPRFEILI68S000": {
        "Last revisions (Details)": (
            "First established on 31 December 2012 with GB 29447-2012 'Norm of Energy Consumption "
            "per Unit Product of Polysilicon Enterprises', effective 1 October 2013. First revised "
            "in 2022 as GB 29447-2022, renamed 'Norm of Energy Consumption per Unit Product of "
            "Polysilicon and Silicon Wafer', expanding scope to include silicon wafer products. "
            "Second revision on 27 June 2026 as GB 29447-2026, renamed 'Norm of Energy Consumption "
            "per Unit Product of Polysilicon and Mono-crystalline Silicon Wafer', for the first time "
            "encompassing the Czochralski method and ingot casting method with differentiated energy "
            "consumption limits, and for the first time coupling 3 energy consumption indicators "
            "with the old standard decreasing by 40%. The new standard also clarifies the statistical "
            "scope of auxiliary production processes and facilities and key energy-consuming equipment."
        ),
    },
}


def format_value(key, value, indent=8):
    """Format a dict value for Python source."""
    if isinstance(value, tuple):
        parts = value[0].split("', '")
        if len(parts) == 1:
            # Single tuple string - it's a multi-line parenthesized string
            return f'{" " * indent}"{key}": {parts[0]}'
        else:
            return f'{" " * indent}"{key}": {value[0]}'
    elif isinstance(value, str):
        if len(value) > 90:
            words = value.split()
            lines = []
            current = ''
            for w in words:
                test = current + ' ' + w if current else w
                if len(test) > 75:
                    lines.append(current)
                    current = w
                else:
                    current = test
            if current:
                lines.append(current)
            inner = ',\n'.join(
                f'{" " * (indent + 4)}"{line}"' for line in lines
            )
            return f'{" " * indent}"{key}": (\n{inner}\n{" " * indent})'
        else:
            import json
            return f'{" " * indent}"{key}": {json.dumps(value, ensure_ascii=False)}'
    else:
        import json
        return f'{" " * indent}"{key}": {json.dumps(value, ensure_ascii=False)}'


# Read the file
with open('scripts/generate_english_from_chinese.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Process each PID
for pid, fields in translations.items():
    marker = f'"{pid}": {{'
    idx = content.find(marker)
    if idx == -1:
        # Need to add new entry - find a good insertion point
        print(f'WARNING: {pid} not found - will add at end of ROW_TRANSLATIONS')
        continue

    # Find the end of this entry (closing } matching the opening)
    start = content.index('{', idx)
    depth = 1
    pos = start + 1
    while depth > 0 and pos < len(content):
        if content[pos] == '{':
            depth += 1
        elif content[pos] == '}':
            depth -= 1
        pos += 1
    entry_end = pos  # position after closing }

    # Extract current entry content
    entry_content = content[start:entry_end]

    # Build field insertions
    insertions = []
    for key, value in fields.items():
        if f'"{key}"' not in entry_content:
            insertion = format_value(key, value, indent=8)
            insertions.append(insertion)

    if not insertions:
        print(f'{pid}: all fields already present')
        continue

    # Insert new fields at the beginning of the entry (after the opening {)
    # Find the newline after {
    first_nl = content.index('\n', start)
    insert_text = '\n' + ',\n'.join(insertions) + ','
    content = content[:first_nl] + insert_text + content[first_nl:]

    print(f'{pid}: added {len(insertions)} fields: {list(fields.keys())}')

# Handle CHNFRMGFGI01S000 (not in ROW_TRANSLATIONS)
# Find a good insertion point - after CHNFRMGFGI01S001 or similar
if "CHNFRMGFGI01S000" not in content or '"CHNFRMGFGI01S000":' not in content:
    # Find the end of the last entry before where this should go
    # Look for a nearby PID
    marker_pid = '"CHNFRMITGI01S000":'
    idx = content.find(marker_pid)
    if idx == -1:
        # Try another known PID
        marker_pid = '"CHNFRMCAPI01S000":'
        idx = content.find(marker_pid)

    if idx != -1:
        # Find end of previous entry
        start = content.index('{', idx)
        depth = 1
        pos = start + 1
        while depth > 0 and pos < len(content):
            if content[pos] == '{':
                depth += 1
            elif content[pos] == '}':
                depth -= 1
            pos += 1
        insert_pos = pos

        new_entry = (
            '\n\n    "CHNFRMGFGI01S000": {\n'
            '        "Asset (Status)": "New; Existing",\n'
            '    },'
        )
        content = content[:insert_pos] + new_entry + content[insert_pos:]
        print('CHNFRMGFGI01S000: created new entry with Asset (Status)')

# Write back
with open('scripts/generate_english_from_chinese.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone patching regulatory ROW_TRANSLATIONS')
