import unittest
from pathlib import Path
import yaml
class CanonicalGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path(__file__).resolve().parents[1]
        cls.missions={m['id']:m for m in yaml.safe_load((root/'data/mission-definitions.yaml').read_text())['missions']}
    def test_all_main_missions_exist(self):
        self.assertEqual(set(self.missions), {f'ACT-ROME-{i:03d}' for i in range(1,43)})
    def test_no_dependency_cycle(self):
        visiting=set(); visited=set()
        def visit(node):
            if node in visiting: self.fail(f'cycle at {node}')
            if node in visited: return
            visiting.add(node)
            for dep in self.missions[node].get('prerequisites',[]):
                if dep in self.missions: visit(dep)
            visiting.remove(node); visited.add(node)
        for node in self.missions: visit(node)
    def test_final_gate(self):
        self.assertEqual(self.missions['ACT-ROME-042']['prerequisites'], ['ACT-ROME-041'])
if __name__=='__main__': unittest.main()
