"""Parse all YAML files and report syntax errors."""
from pathlib import Path
import sys
try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]

def main():
    if yaml is None:
        print("ERROR: PyYAML is required")
        return 2
    errors = []
    for path in sorted((ROOT / "data").rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                yaml.safe_load(handle)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("YAML validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
