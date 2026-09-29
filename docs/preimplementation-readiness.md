# Preimplementation Readiness

## Status vocabulary

- Specified: approved design documentation exists.
- Structured: validated YAML/JSON with stable IDs exists.
- Generated: source files or assets exist.
- Compiled: the locked Unreal project builds.
- Executed: tools or tests have run.
- Verified: a qualified reviewer has inspected the result.

## Current status

- Narrative canon: specified and undergoing source-of-truth normalization.
- Main missions 001–042: individual briefs exist; canonical structured definitions exist.
- Supporting characters 001–026: structured.
- Duplicate legacy data: isolated under `data/legacy/` and excluded from runtime.
- Cross-reference validators: implemented; execution requires PyYAML.
- Unreal architecture: specified.
- Unreal project: not generated.
- C++ and Blueprint runtime: not generated.
- Engine compilation: not executed.
- Historical, language, and sensitivity review: not verified.

## Step 1 exit criteria

- One documented source hierarchy.
- One canonical structured-definition layer.
- Legacy duplicates excluded from runtime.
- No ambiguity about which files an LLM should read for implementation.

## Remaining gates

Resolve canonical timeline, geography, evidence, route, Act III calendar, and fire/evacuation contradictions. Then execute validators, lock the exact UE5 minor version and target hardware, and generate the Unreal project.
