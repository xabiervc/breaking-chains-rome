# Unreal Automation Specification

## Test categories

- `BC.Content.Schema`
- `BC.Content.CrossReferences`
- `BC.Canon.Invariants`
- `BC.Determinism.Clock`
- `BC.Determinism.Schedules`
- `BC.Determinism.Missions`
- `BC.Determinism.SaveLoad`
- `BC.Missions.VerticalSlice`
- `BC.Final.FireTransitions`
- `BC.Final.EvacuationTiers`

## Minimum tests

1. New campaign starts with no completed missions.
2. ACT-ROME-002 cannot start before ACT-ROME-001.
3. Objective completion is idempotent.
4. Livia transfers during ACT-ROME-004 in every valid run.
5. Vara dies only during ACT-ROME-006.
6. Herennius dies only during ACT-ROME-007.
7. Rewards cannot duplicate after reload.
8. Final date remains AD 64-07-18.
9. The four Act III resolutions gate ACT-ROME-036.
10. Fire transitions are identical for identical campaign state.
11. Mandatory rescue count remains 40 at every evacuation tier.
12. Roman slavery remains active in the epilogue state.

## Test naming

Use stable names and deterministic fixtures. Tests must report campaign version, content manifest hash, engine version, platform, and seed where applicable.
