"""One-shot: revert commas wrongly added to ETS-entry continuation lines
(string concatenation must stay comma-free)."""
import ast

path = "scripts/generate_english_from_chinese.py"
with open(path, encoding="utf-8") as f:
    text = f.read()
lines = text.split("\n")

bad = [262, 265, 268, 271, 274, 286, 298, 301, 316, 319, 331, 334, 337,
       349, 361, 373, 385]
for n in bad:
    l = lines[n - 1]
    assert l.rstrip().endswith('",'), (n, l)
    lines[n - 1] = l.rstrip()[:-1]

src = "\n".join(lines)
with open(path, "w", encoding="utf-8") as f:
    f.write(src)
ast.parse(src)
print("reverted", len(bad), "commas; ast.parse OK")
