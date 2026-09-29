"""Validate declarations for gameplay-critical deterministic systems."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / "docs" / "DETERMINISM_SPECIFICATION.md",
    ROOT / "docs" / "FIRE_AND_EVACUATION_SYSTEM.md",
    ROOT / "data" / "fire-transitions.yaml",
    ROOT / "data" / "campaign-state.yaml",
]
TOKENS = ["Historical dates are immutable", "Named character survival is scripted", "Economy uses documented formulas", "Fire behavior uses fixed", "rewards: idempotent_by_mission_id"]

def main():
    errors = []
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")
    corpus = "\n".join(path.read_text(encoding="utf-8") for path in REQUIRED_FILES if path.exists())
    for token in TOKENS:
        if token not in corpus:
            errors.append(f"Missing deterministic declaration: {token}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Determinism validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
