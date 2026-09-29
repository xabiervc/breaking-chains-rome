"""Validate normalized IDs and cross-references."""
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
def load(filename):
    with (ROOT / "data" / filename).open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}
def main():
    if yaml is None:
        print("ERROR: PyYAML is required")
        return 2
    errors, definitions = [], {}
    sources = [("mission-definitions.yaml", "missions", "mission"), ("side-mission-definitions.yaml", "side_missions", "mission"), ("character-definitions.yaml", "characters", "character"), ("location-definitions.yaml", "locations", "location"), ("evidence-definitions.yaml", "evidence", "evidence"), ("route-definitions.yaml", "routes", "route"), ("faction-definitions.yaml", "factions", "faction")]
    for filename, key, kind in sources:
        for item in load(filename).get(key, []):
            item_id = item.get("id")
            if not item_id or not PATTERNS[kind].match(item_id): errors.append(f"invalid {kind} ID in {filename}: {item_id}")
            elif item_id in definitions: errors.append(f"duplicate ID: {item_id}")
            else: definitions[item_id] = kind
    mission_ids = {k for k, v in definitions.items() if v == "mission"}
    character_ids = {k for k, v in definitions.items() if v == "character"}
    location_ids = {k for k, v in definitions.items() if v == "location"}
    faction_ids = {k for k, v in definitions.items() if v == "faction"}
    for item in load("mission-definitions.yaml").get("missions", []):
        for ref in item.get("prerequisites", []):
            if ref not in mission_ids: errors.append(f"{item['id']} missing prerequisite {ref}")
        for ref in item.get("locations", []):
            if ref not in location_ids: errors.append(f"{item['id']} missing location {ref}")
    for item in load("evidence-definitions.yaml").get("evidence", []):
        target = item.get("target")
        if target not in character_ids and target not in faction_ids: errors.append(f"{item['id']} missing target {target}")
        if item.get("acquired_by") not in mission_ids: errors.append(f"{item['id']} missing acquisition mission")
    for item in load("dialogue-definitions.yaml").get("dialogue_scenes", []):
        if item.get("mission") not in mission_ids: errors.append(f"{item['id']} missing mission")
        for speaker in item.get("speakers", []):
            if speaker not in character_ids: errors.append(f"{item['id']} missing speaker {speaker}")
    if errors:
        for error in errors: print(f"ERROR: {error}")
        return 1
    print("Reference validation passed.")
    return 0
if __name__ == "__main__": sys.exit(main())
