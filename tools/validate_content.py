"""Minimal deterministic content validator for Breaking Chains: Rome."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MISSION_RE = re.compile(r"\b(?:ACT-ROME|SIDE-[A-Z]+)-\d{3}\b")
LOCATION_RE = re.compile(r"\bLOC-[A-Z]+-\d{3}\b")

def read_all_markdown():
    return "\n".join(path.read_text(encoding="utf-8") for path in DOCS.rglob("*.md"))

def validate_ids(text):
    errors = []
    for kind, values in (("mission", MISSION_RE.findall(text)), ("location", LOCATION_RE.findall(text))):
        duplicates = sorted({value for value in values if values.count(value) > 100})
        if duplicates:
            errors.append(f"Suspicious repeated {kind} IDs: {duplicates}")
    return errors

def validate_canon(text):
    required = ["AD 54", "AD 64", "18 July AD 64", "Dama", "Livia", "ACT-ROME-042"]
    return [f"Missing canonical token: {token}" for token in required if token not in text]

def main():
    text = read_all_markdown()
    errors = validate_ids(text) + validate_canon(text)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Content validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
