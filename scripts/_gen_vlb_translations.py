"""Generate ROW_TRANSLATIONS entries for VLB instruments from EN CSV."""
import csv, json

TRANSLATABLE_FIELDS = [
    'Emission sector', 'English name', 'Description', 'Objective',
    'Administrating authorities', 'Asset', 'Asset (Details)',
    'Agent (Detail)', 'Activity (Details)', 'Requirement specification',
    'Incentives for Participation', 'Monitoring', 'Sanctions for non-compliance',
    'GHG emission coverage (absolute)', 'GHG emission coverage (% domestic emissions)',
    'Mitigation co-benefits', 'Legal statute', 'Other weblinks',
    'Last revisions (Details)',
]

with open('outputs/CCPID_en_voluntary_approaches.csv', 'r', encoding='utf-8-sig') as f:
    vlb = [r for r in csv.DictReader(f) if r['Policy Instrument ID'].startswith('CHNVIIVLBI')]

output = []
for row in vlb:
    pid = row['Policy Instrument ID']
    parts = [f'    "{pid}": {{']
    for field in TRANSLATABLE_FIELDS:
        val = row.get(field, '').strip()
        if val and val not in ('N/A', ''):
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            parts.append(f'        "{field}": "{escaped}",')
    parts.append('    },')
    output.append('\n'.join(parts))

with open('_temp_row_translations.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print(f'Wrote {len(vlb)} entries')
