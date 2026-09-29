"""Validate canonical manifest paths and ensure runtime sources exclude legacy data."""
from pathlib import Path
import sys
try:
    import yaml
except ImportError:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
def main():
    if yaml is None:
        print('ERROR: PyYAML is required'); return 2
    data=yaml.safe_load((ROOT/'docs/canon/canonical-manifest.yaml').read_text(encoding='utf-8')) or {}
    errors=[]
    for paths in data.get('canonical_sources',{}).values():
        for relative in paths:
            if not (ROOT/relative).exists(): errors.append(f'missing canonical path: {relative}')
    for relative in data.get('canonical_exclusions',[]):
        if not str(relative).startswith('data/'): errors.append(f'exclusion outside data/: {relative}')
    if errors:
        for error in errors: print('ERROR:',error)
        return 1
    print('Manifest validation passed.')
    return 0
if __name__=='__main__': sys.exit(main())
