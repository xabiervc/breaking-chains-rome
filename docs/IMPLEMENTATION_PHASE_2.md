# Implementation Phase 2 — Unreal Foundations

## Objective

Create an Unreal Engine 5 project skeleton that can load validated Breaking Chains content and run the Ashgrove vertical slice without placing canonical state in Blueprints.

## Stage order

1. Lock exact UE5 minor version and target platforms.
2. Create the C++ project and module layout.
3. Add Git LFS and Unreal ignore rules.
4. Implement content manifest and YAML-to-asset import contract.
5. Implement `BCGameInstance`, `BCGameState`, and save schema.
6. Implement mission dependency and objective services.
7. Implement deterministic clock and schedule service.
8. Create Ashgrove World Partition blockout.
9. Implement ACT-ROME-001 as the first end-to-end mission.
10. Add save/load and automation tests.
11. Expand to ACT-ROME-002 through ACT-ROME-007.

## Acceptance criteria

- Project opens in the locked UE5 version.
- Development build compiles with no errors.
- Validated content manifest loads.
- Invalid content fails before runtime.
- ACT-ROME-001 starts from a new save and reaches a persisted success state.
- Replaying the same input sequence produces the same authoritative result.
- Blueprint presentation cannot bypass C++ mission validation.
- Save/load preserves the vertical-slice state.

## Explicit decision

Use **C++ plus Blueprints**, not Blueprint-only and not C++-only. C++ is authoritative; Blueprints are expressive presentation and mission composition.
