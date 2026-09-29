"""Run canonical validators and report an explicit execution status."""
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
VALIDATORS=['validate_yaml.py','validate_references.py','validate_continuity.py','validate_graph.py','validate_final_state.py']
def main():
    results=[]
    for name in VALIDATORS:
        path=ROOT/'tools'/name
        if not path.exists(): results.append((name,'MISSING')); continue
        result=subprocess.run([sys.executable,str(path)],cwd=ROOT,capture_output=True,text=True)
        results.append((name,'PASS' if result.returncode==0 else 'FAIL',result.stdout+result.stderr))
    for item in results:
        print(f'{item[0]}: {item[1]}')
        if len(item)>2 and item[2]: print(item[2].strip())
    return 0 if all(item[1]=='PASS' for item in results) else 1
if __name__=='__main__': sys.exit(main())
