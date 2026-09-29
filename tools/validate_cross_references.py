"""Static cross-reference checks for the deterministic Rome content package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def files_text():
    return "\n".join(p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md") if ".git" not in p.parts)

def main():
    text = files_text()
    required = ["ACT-ROME-023", "ACT-ROME-027", "ACT-ROME-031", "ACT-ROME-035", "ACT-ROME-042", "18 July AD 64", "Dama", "Livia", "Vindex Varro", "Roman slavery continues"]
    errors = [f"missing canonical reference: {value}" for value in required if value not in text]
    for path in (ROOT / "data" / "campaign-state.yaml", ROOT / "data" / "epilogue-state.yaml", ROOT / "data" / "fire-transitions.yaml"):
        if not path.exists():
            errors.append(f"missing data file: {path.relative_to(ROOT)}")
    mission_ids = re.findall(r"ACT-ROME-\d{3}", text)
    if "ACT-ROME-042" not in mission_ids:
        errors.append("final mission ID not found")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Cross-reference validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
