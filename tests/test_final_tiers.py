import unittest
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
class FinalTierTests(unittest.TestCase):
    def test_all_tiers_preserve_mandatory_rescue(self):
        for tier in range(4):
            data=yaml.safe_load((ROOT/'tests/fixtures'/f'FINAL-TIER-{tier}.yaml').read_text())
            self.assertEqual(data['mandatory_rescue_count'],40)
            self.assertEqual(data['evacuation_tier'],tier)
if __name__=='__main__': unittest.main()
