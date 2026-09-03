"""One-shot: add missing commas after field values that lost their trailing comma
when field blocks were inserted before an entry's closing brace."""
import ast

path = "scripts/generate_english_from_chinese.py"
with open(path, encoding="utf-8") as f:
    text = f.read()
lines = text.split("\n")

fixed = []
for i in range(len(lines) - 1):
    l = lines[i].rstrip()
    if not l or l.endswith(",") or l.endswith("{"):
        continue
    if not (l.endswith(")") or l.endswith('"')):
        continue
    if not (lines[i].startswith(" " * 8) and not lines[i].startswith(" " * 12)):
        continue
    j = i + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j < len(lines):
        nxt = lines[j]
        if nxt.startswith(" " * 8 + '"') and not nxt.startswith(" " * 12):
            lines[i] = lines[i] + ","
            fixed.append((i + 1, l[-40:], nxt[:40]))

with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

src = "\n".join(lines)
try:
    ast.parse(src)
    print("ast.parse OK after", len(fixed), "comma fix(es)")
except SyntaxError as e:
    print("STILL BROKEN:", e)
for ln, old, nxt in fixed:
    print(f"line {ln}: ...{old}  ->  next field: {nxt}")
