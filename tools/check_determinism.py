"""Check that critical deterministic rules are documented."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["Main mission objectives are ordered", "Named character survival is scripted", "Historical dates are immutable", "Economy uses documented formulas", "Fire behavior uses fixed"]

def main():
    path = ROOT / "docs" / "DETERMINISM_SPECIFICATION.md"
    text = path.read_text(encoding="utf-8")
    missing = [item for item in REQUIRED if item not in text]
    if missing:
        for item in missing:
            print(f"ERROR: missing deterministic rule: {item}")
        return 1
    print("Determinism documentation check passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
