import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class SchemaContractTests(unittest.TestCase):
    def test_all_schemas_are_valid_json(self):
        for path in (ROOT/'schemas').glob('*.json'):
            with self.subTest(path=path): json.loads(path.read_text())
    def test_required_schema_files_exist(self):
        for name in ['evidence.schema.json','route.schema.json','dialogue-scene.schema.json','campaign-state.schema.json','canonical-manifest.schema.json','faction.schema.json','side-mission.schema.json','fire-transition.schema.json','evacuation-route.schema.json','specialist.schema.json','fixture.schema.json']:
            self.assertTrue((ROOT/'schemas'/name).exists(),name)
if __name__=='__main__': unittest.main()
