"""Run repository validators in a stable order."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VALIDATORS = ["validate_yaml.py", "validate_content.py", "validate_cross_references.py", "validate_missions.py", "validate_determinism.py", "validate_final_state.py", "check_determinism.py"]

def main():
    for name in VALIDATORS:
        print(f"==> {name}")
        result = subprocess.run([sys.executable, str(ROOT / "tools" / name)], cwd=ROOT)
        if result.returncode != 0:
            print(f"FAILED: {name}")
            return result.returncode
    print("All validators passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
