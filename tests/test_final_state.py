import unittest
from pathlib import Path
import yaml
class FinalStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path(__file__).resolve().parents[1]
        cls.campaign=yaml.safe_load((root/'data/campaign-state.yaml').read_text())['campaign_state']
        cls.epilogue=yaml.safe_load((root/'data/epilogue-state.yaml').read_text())['epilogue']
    def test_final_invariants(self):
        self.assertEqual(self.campaign['canonical_final_mission'],'ACT-ROME-042')
        self.assertEqual(self.campaign['canonical_final_date'],'AD64-07-18')
        self.assertEqual(self.campaign['invariants']['mandatory_rescue_count'],40)
        self.assertFalse(self.campaign['invariants']['roman_slavery_ended'])
        self.assertEqual(self.epilogue['canonical_rescues'],40)
if __name__=='__main__': unittest.main()
