"""Validate canonical mission graph, references, and final gate."""
from pathlib import Path
import sys
try:
    import yaml
except ImportError:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
def main():
    if yaml is None: print('ERROR: PyYAML is required'); return 2
    data = yaml.safe_load((ROOT/'data/mission-definitions.yaml').read_text(encoding='utf-8'))
    missions = {m['id']: m for m in data['missions']}; errors=[]
    if len(missions) != 42: errors.append(f'expected 42 missions, found {len(missions)}')
    visiting=set(); visited=set()
    def visit(node):
        if node in visiting: errors.append(f'cycle detected at {node}'); return
        if node in visited: return
        visiting.add(node)
        for dep in missions[node].get('prerequisites', []):
            if dep not in missions: errors.append(f'{node} missing mission prerequisite {dep}')
            else: visit(dep)
        visiting.remove(node); visited.add(node)
    for node in missions: visit(node)
    final = missions.get('ACT-ROME-042', {})
    if set(final.get('prerequisites', [])) != {'ACT-ROME-041'}: errors.append('final mission must follow ACT-ROME-041')
    gates = set(missions.get('ACT-ROME-036', {}).get('prerequisites', []))
    if gates != {'ACT-ROME-023','ACT-ROME-027','ACT-ROME-031','ACT-ROME-035'}: errors.append('ACT-ROME-036 gate mismatch')
    if errors:
        for e in errors: print('ERROR:', e)
        return 1
    print('Mission graph validation passed.')
    return 0
if __name__ == '__main__': sys.exit(main())
