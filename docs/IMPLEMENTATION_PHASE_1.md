# Implementation Phase 1 — Foundations

## Objective

Convert the documentation-first production bible into a verifiable content package and define the first implementable vertical slice.

## Scope

- Validate all structured content before runtime integration.
- Create deterministic content-loading conventions.
- Implement the Ashgrove-to-Alban-Hills vertical slice.
- Preserve the fixed canon and mission dependency graph.
- Keep runtime systems separate from narrative source data.

## Definition of done

1. YAML files parse successfully.
2. JSON schemas validate their corresponding content objects.
3. Mission, character, location, route, evidence, fire, and evacuation IDs are unique.
4. Every referenced mission, character, location, route, evidence item, and fire zone exists.
5. The vertical slice has reproducible test saves and acceptance tests.
6. Final-state invariants remain unchanged.

## Implementation order

1. Content loader and schema validation.
2. Canonical state model.
3. Mission dependency resolver.
4. Deterministic clock and schedule service.
5. Ashgrove location blockout.
6. Mission state machine for ACT-ROME-001 through ACT-ROME-007.
7. Save/load persistence.
8. Vertical-slice QA.

## Non-goals

- No full combat system.
- No procedural quest generation.
- No online multiplayer.
- No random main-story outcomes.
- No final-fire implementation in this phase.

## Required outputs

- Validator command that fails on invalid content.
- Human-readable validation report.
- Test fixtures for a new campaign and each vertical-slice checkpoint.
- Versioned content manifest.
