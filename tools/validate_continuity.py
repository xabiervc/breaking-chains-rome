"""Validate fixed narrative invariants in normalized data."""
from pathlib import Path
import sys
try:
    import yaml
except ImportError:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
def main():
    if yaml is None: print("ERROR: PyYAML is required"); return 2
    missions = yaml.safe_load((ROOT / "data" / "mission-definitions.yaml").read_text(encoding="utf-8"))["missions"]
    by_id = {item["id"]: item for item in missions}; errors = []
    required = [f"ACT-ROME-{i:03d}" for i in range(1, 43)]
    missing = [item for item in required if item not in by_id]
    if missing: errors.append(f"missing main missions: {missing}")
    if by_id.get("ACT-ROME-042", {}).get("date") != "AD64-july-18": errors.append("final mission date is not AD64-july-18")
    expected = [f"ACT-ROME-{i:03d}" for i in range(36, 42)]
    if by_id.get("ACT-ROME-042", {}).get("prerequisites") != expected: errors.append("final mission prerequisites are inconsistent")
    if errors:
        for error in errors: print(f"ERROR: {error}")
        return 1
    print("Continuity validation passed.")
    return 0
if __name__ == "__main__": sys.exit(main())
