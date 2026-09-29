"""Validate final-state invariants and evacuation routes."""
from pathlib import Path
import sys
try:
    import yaml
except ImportError:
    yaml=None
ROOT=Path(__file__).resolve().parents[1]
def main():
    if yaml is None: print('ERROR: PyYAML is required'); return 2
    campaign=yaml.safe_load((ROOT/'data/campaign-state.yaml').read_text(encoding='utf-8'))['campaign_state']; epi=yaml.safe_load((ROOT/'data/epilogue-state.yaml').read_text(encoding='utf-8'))['epilogue']; routes=yaml.safe_load((ROOT/'data/evacuation-routes.yaml').read_text(encoding='utf-8'))['evacuation_routes']; errors=[]
    if campaign['canonical_final_mission']!='ACT-ROME-042': errors.append('final mission mismatch')
    if campaign['canonical_final_date']!='AD64-07-18': errors.append('final date mismatch')
    if campaign['invariants']['mandatory_rescue_count']!=40: errors.append('mandatory rescue count mismatch')
    if campaign['invariants']['roman_slavery_ended'] is not False: errors.append('slavery outcome mismatch')
    mandatory=next((r for r in routes if r['id']=='EVAC-001'),None)
    if not mandatory or mandatory.get('mandatory') is not True or mandatory.get('capacity_tier_0')!=40: errors.append('mandatory evacuation route mismatch')
    if epi.get('canonical_rescues')!=40 or epi.get('roman_slavery_ended') is not False: errors.append('epilogue mismatch')
    if errors:
        for error in errors: print('ERROR:',error)
        return 1
    print('Final-state validation passed.')
    return 0
if __name__=='__main__': sys.exit(main())
