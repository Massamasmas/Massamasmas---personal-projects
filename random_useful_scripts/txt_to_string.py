# txt_to_py_literal.py
import sys
from pathlib import Path

def normalize_path(s: str) -> Path:
    s = s.strip().strip('"').strip("'")
    return Path(s).expanduser()

p = normalize_path(sys.argv[1] if len(sys.argv) > 1 else input("Path to .txt: "))
if not p.exists():
    raise FileNotFoundError(f"Not found: {p}")

text = p.read_text(encoding="utf-8")
py_literal = repr(text)  # or: import json; py_literal = json.dumps(text)
print(py_literal)