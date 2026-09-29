# Code Generation Order

## Stage 1 — Buildable shell

Generate the `.uproject`, `Build.cs`, target files, module startup, logging categories, and a minimal game instance. Verify compilation.

## Stage 2 — Data contracts

Generate C++ structs and Data Assets for missions, objectives, characters, locations, routes, factions, evidence, fire zones, evacuation routes, and languages. Add stable IDs and validation methods.

## Stage 3 — Campaign state

Implement `UBCGameInstanceSubsystem` services, `FBCampaignState`, `UBCSaveGame`, serialization, schema version, and migration interface.

## Stage 4 — Deterministic services

Implement date/time, stable seed, schedule lookup, route lookup, faction transitions, evidence state, rescue ledger, and fire-zone transition validation.

## Stage 5 — Mission framework

Implement mission definition loading, dependency resolution, objective state machine, idempotent completion, rewards, failure states, and event dispatch.

## Stage 6 — Vertical slice

Implement Dama controller scaffolding, interaction interface, Ashgrove blockout, fixed schedules, ACT-ROME-001, save/load, and automation tests. Expand through ACT-ROME-007 only after ACT-ROME-001 passes.

## Stage 7 — Presentation

Add Blueprint mission staging, UI, cameras, audio hooks, VFX hooks, subtitle metadata, and debug overlay.

## Stage 8 — World expansion

Add regions and travel cells incrementally. Never create all ten regions before the vertical slice is stable.

## Stage 9 — Production validation

Run content validators, C++ tests, Unreal automation tests, packaged development build, save migration tests, and deterministic replay tests.
