"""Validate the canonical 42-mission dependency graph."""
from pathlib import Path
import sys
try:
    import yaml
except ImportError:
    yaml=None
ROOT=Path(__file__).resolve().parents[1]
def main():
    if yaml is None: print('ERROR: PyYAML is required'); return 2
    data=yaml.safe_load((ROOT/'data/mission-definitions.yaml').read_text(encoding='utf-8')) or {}
    missions={item['id']:item for item in data.get('missions',[])}; errors=[]
    expected={f'ACT-ROME-{i:03d}' for i in range(1,43)}
    if set(missions)!=expected: errors.append(f'mission set mismatch: expected 42, found {len(missions)}')
    visiting=set(); visited=set()
    def visit(node):
        if node in visiting: errors.append(f'cycle detected at {node}'); return
        if node in visited or node not in missions: return
        visiting.add(node)
        for dep in missions[node].get('prerequisites',[]):
            if dep not in missions: errors.append(f'{node} references missing prerequisite {dep}')
            else: visit(dep)
        visiting.remove(node); visited.add(node)
    for node in missions: visit(node)
    if set(missions.get('ACT-ROME-042',{}).get('prerequisites',[])) != {'ACT-ROME-041'}: errors.append('ACT-ROME-042 final gate mismatch')
    if set(missions.get('ACT-ROME-036',{}).get('prerequisites',[])) != {'ACT-ROME-023','ACT-ROME-027','ACT-ROME-031','ACT-ROME-035'}: errors.append('ACT-ROME-036 Act IV gate mismatch')
    if errors:
        for error in errors: print('ERROR:',error)
        return 1
    print('Mission graph validation passed.')
    return 0
if __name__=='__main__': sys.exit(main())
