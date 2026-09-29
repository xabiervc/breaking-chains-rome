# Preimplementation Readiness

## Status vocabulary

- Specified: approved design documentation exists.
- Structured: validated YAML/JSON with stable IDs exists.
- Generated: source files or assets exist.
- Executed: validators or tests have run.
- Compiled: the locked Unreal project builds.
- Verified: a qualified reviewer has inspected the result.

## Current status

- Narrative canon: specified and continuity-audited.
- Main missions 001–042: specified and structured.
- Supporting characters 001–026: structured.
- Evidence, routes, evacuation, and fire decisions: specified and structured.
- Schemas: expanded for remaining canonical entity types.
- Fixtures and Python tests: expanded; execution pending local/CI run.
- Unreal project: not generated.
- C++/Blueprint runtime: not generated.
- Historical, linguistic, sensitivity, and hardware reviews: not verified.

## Remaining preimplementation gates

1. Run `python tools/validate_master.py`.
2. Run `python -m unittest discover -s tests -v`.
3. Fix any failures and commit the generated reports.
4. Lock exact Unreal Engine version, target hardware, and performance budget.
5. Complete historical, linguistic, sensitivity, and asset-provenance reviews.
6. Generate and compile the Unreal project.
