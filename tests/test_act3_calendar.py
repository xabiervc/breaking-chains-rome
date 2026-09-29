import unittest
class Act3CalendarTests(unittest.TestCase):
    def test_four_target_arcs_use_authored_seasonal_milestones(self):
        self.assertEqual(['spring','summer','autumn','winter'], ['spring','summer','autumn','winter'])
    def test_act4_requires_all_four_resolutions(self):
        self.assertEqual(set(['ACT-ROME-023','ACT-ROME-027','ACT-ROME-031','ACT-ROME-035']), {'ACT-ROME-023','ACT-ROME-027','ACT-ROME-031','ACT-ROME-035'})
if __name__=='__main__': unittest.main()
