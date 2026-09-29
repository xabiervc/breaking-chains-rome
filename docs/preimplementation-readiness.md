# Preimplementation readiness

## Status vocabulary

Specified means documented; structured means machine-readable; validated means actual validators passed; compiled means an Unreal build ran. These states are not interchangeable.

## Current status

- The 42 main mission briefs exist and the 42-entry structured mission index has been restored; parsing and cross-document consistency are not yet verified.
- The Act I time-passage condition is a campaign flag, not a nonexistent mission.
- Duplicate YAML files remain in `data/` and are explicitly excluded by the manifest. `data/legacy/` contains notice stubs, not copies of those files.
- Canonical Act IV fire data are blocked pending consistency repair.
- No Unreal project, binary assets, C++ compilation, or gameplay test exists.

## Gate before implementation

1. Resolve chronology, geography, evidence, travel and final-fire contradictions across prose and data.
2. Make all canonical references resolve and run validators against the manifest.
3. Record the exact Unreal version and test hardware.
4. Do not mark this project verified until those tests run and pass.
