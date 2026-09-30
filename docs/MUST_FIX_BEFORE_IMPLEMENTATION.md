# Must Fix Before Implementation

## Structural blockers

The following list is intentionally short. A project reaches Level A only if no unresolved structural decision remains in this list.

- None identified in the canonical design baseline.

## Conditions that still block the vertical slice gate

These are execution gates, not unresolved design identity:

- Conda workflow must run green after the missing `environment.yml` failure is corrected.
- Runtime network variables, choice transitions, and save fields must be implemented.
- Slice assets, UI, audio, and accessibility settings must exist.
- Deterministic replay, schema validation, unit tests, and save-recovery tests must pass.
- Historical, language, sensitivity, accessibility, art, and audio reviews must be scheduled and recorded.

## Why this distinction matters

The first group blocks starting controlled implementation. The second group is exactly what controlled implementation is meant to produce and validate. Neither group may be hidden by a “100% complete” label.
