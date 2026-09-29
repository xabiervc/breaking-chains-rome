"""Validate IDs and cross-references in normalized structured data."""
from pathlib import Path
import re
import sys
try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "mission": re.compile(r"^(ACT-ROME|SIDE-[A-Z]+)-\d{3}$"),
    "character": re.compile(r"^CHAR-\d{3}$"),
    "location": re.compile(r"^LOC-[A-Z_]+-\d{3}$"),
    "faction": re.compile(r"^FACTION-\d{3}$"),
    "evidence": re.compile(r"^EVID-[A-Z]+-\d{3}$"),
    "route": re.compile(r"^ROUTE-\d{3}$"),
}

def load(path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}

def main():
    if yaml is None:
        print("ERROR: PyYAML is required")
        return 2
    errors = []
    definitions = {}
    for path, key, kind in [
        ("mission-definitions.yaml", "missions", "mission"),
        ("character-definitions.yaml", "characters", "character"),
        ("location-definitions.yaml", "locations", "location"),
        ("evidence-definitions.yaml", "evidence", "evidence"),
        ("route-definitions.yaml", "routes", "route"),
        ("faction-definitions.yaml", "factions", "faction"),
        ("side-mission-definitions.yaml", "side_missions", "mission"),
    ]:
        path = ROOT / "data" / path
        data = load(path)
        for item in data.get(key, []):
            item_id = item.get("id")
            if not item_id or not PATTERNS[kind].match(item_id):
                errors.append(f"invalid {kind} ID in {path.name}: {item_id}")
            elif item_id in definitions:
                errors.append(f"duplicate ID: {item_id}")
            else:
                definitions[item_id] = kind
    for item_id, kind in definitions.items():
        if kind == "mission" and item_id.startswith("ACT-ROME-"):
            continue
    mission_ids = {key for key, value in definitions.items() if value == "mission"}
    location_ids = {key for key, value in definitions.items() if value == "location"}
    for item in load(ROOT / "data" / "mission-definitions.yaml").get("missions", []):
        for prerequisite in item.get("prerequisites", []):
            if prerequisite not in mission_ids:
                errors.append(f"{item['id']} references missing prerequisite {prerequisite}")
        for location in item.get("locations", []):
            if location not in location_ids:
                errors.append(f"{item['id']} references missing location {location}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Reference validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
