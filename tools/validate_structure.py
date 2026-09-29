"""Validate normalized repository structure."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = ["README.md", "GDD.md", "CLAUDE.md", ".gitignore", ".gitattributes", "docs/preimplementation-readiness.md", "docs/canon/continuity-matrix.md", "docs/canon/id-registry.md", "data/mission-definitions.yaml", "data/character-definitions.yaml", "data/location-definitions.yaml", "data/evidence-definitions.yaml", "data/route-definitions.yaml", "data/faction-definitions.yaml", "tools/validate_references.py", "tools/validate_continuity.py", "tools/validate_structure.py"]

def main():
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        for path in missing:
            print(f"ERROR: missing required path: {path}")
        return 1
    print("Structure validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
