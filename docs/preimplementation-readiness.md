# Preimplementation Readiness

## Status vocabulary

- **Specified:** described in an approved design document.
- **Structured:** represented in validated YAML/JSON with stable IDs.
- **Generated:** source files or assets have been created.
- **Compiled:** the Unreal project builds successfully in the locked engine version.
- **Executed:** automated tests or tools have run.
- **Verified:** a human or qualified reviewer has inspected the result.

## Current status

- Narrative canon: specified and audited.
- Main mission catalogue: specified; Act III production files included in this phase.
- Structured content: partially structured and being normalized.
- Unreal architecture: specified.
- Unreal project: not generated.
- C++ runtime: not generated.
- Blueprint runtime: not generated.
- Binary assets: not generated.
- Engine compilation: not executed.
- Unreal automation tests: not executed.
- Historical language review: not verified.

## Exit criteria for preimplementation

1. Every canonical entity has one stable ID.
2. Every reference resolves to an entity of the correct type.
3. Every main mission has an individual brief and structured record.
4. Timeline, mission dependencies, locations, characters, evidence, routes, and final states agree.
5. Root Git configuration is active.
6. Validators run without structural or canonical errors.
7. The exact Unreal version and target hardware are recorded before project generation.
8. The vertical-slice contract is complete.
9. No document claims that code or assets are compiled or playable when they are not.

## Remaining external gates

Historical specialists, language specialists, sensitivity reviewers, target-hardware profiling, exact Unreal minor-version selection, and actual engine compilation remain external verification gates.
