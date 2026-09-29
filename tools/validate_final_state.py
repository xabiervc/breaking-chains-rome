"""Validate canonical final-state invariants."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["final_mission: ACT-ROME-042", "final_date: AD64-07-18", "roman_slavery_ended: false", "canonical_rescue_count: 40", "Vindex status", "Livia status"]

def main():
    paths = [ROOT / "data" / "act4-state.yaml", ROOT / "data" / "campaign-state.yaml", ROOT / "docs" / "FINAL_STATE_MATRIX.md"]
    corpus = "\n".join(path.read_text(encoding="utf-8") for path in paths if path.exists())
    missing = [token for token in REQUIRED if token not in corpus]
    if missing:
        for token in missing:
            print(f"ERROR: missing final-state invariant: {token}")
        return 1
    print("Final-state validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
