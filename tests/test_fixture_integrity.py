import unittest
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
class FixtureIntegrityTests(unittest.TestCase):
    def test_fixture_ids_are_unique(self):
        ids=[]
        for path in (ROOT/'tests/fixtures').glob('*.yaml'):
            data=yaml.safe_load(path.read_text()); ids.append(data['fixture_id'])
        self.assertEqual(len(ids),len(set(ids)))
    def test_final_fixture_dates(self):
        for name in ['FINAL-TIER-0.yaml','FINAL-TIER-1.yaml','FINAL-TIER-2.yaml','FINAL-TIER-3.yaml']:
            data=yaml.safe_load((ROOT/'tests/fixtures'/name).read_text())
            self.assertEqual(data['campaign_date'],'AD64-07-18')
if __name__=='__main__': unittest.main()
