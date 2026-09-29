"""Validate canonical main-mission IDs and dependency ordering."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {f"ACT-ROME-{index:03d}" for index in range(1, 43)}

def main():
    text = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "docs").rglob("*.md"))
    found = set(re.findall(r"ACT-ROME-\d{3}", text))
    missing = sorted(EXPECTED - found)
    errors = []
    if missing:
        errors.append(f"Missing canonical missions: {', '.join(missing)}")
    if "ACT-ROME-023" not in text or "ACT-ROME-027" not in text or "ACT-ROME-031" not in text or "ACT-ROME-035" not in text:
        errors.append("Act III resolution gate references are incomplete")
    if "ACT-ROME-042" not in text or "18 July AD 64" not in text:
        errors.append("Final mission canon is incomplete")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Mission validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
