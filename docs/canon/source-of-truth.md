# Canonical Source Hierarchy

## Purpose

This document defines which files are authoritative and prevents contradictory duplicate data from being consumed by an LLM or runtime.

## Authority order

1. `docs/canon/continuity-matrix.md` — immutable narrative invariants.
2. `docs/canon/id-registry.md` — stable identity registry.
3. `docs/story/timeline.md` — canonical chronology.
4. `docs/missions/ACT-ROME-###.md` — individual mission intent and authored narrative detail.
5. `data/*-definitions.yaml` — canonical structured runtime content.
6. `docs/*.md` system documents — design rules and implementation contracts.
7. `data/legacy/` — historical snapshots only; never runtime input.

## Conflict rule

If two canonical sources conflict, the conflict blocks implementation. Do not choose silently. Record the conflict in `docs/canon/change-log.md`, resolve it explicitly, then update all affected canonical sources in the same commit.

## Runtime input rule

Only files explicitly marked canonical in `docs/canon/canonical-manifest.yaml` may be imported into Unreal Data Assets or Data Tables. Files under `data/legacy/` must never be imported.

## Structured-data rule

The canonical runtime definitions are:

- `data/mission-definitions.yaml`.
- `data/character-definitions.yaml`.
- `data/location-definitions.yaml`.
- `data/evidence-definitions.yaml`.
- `data/route-definitions.yaml`.
- `data/faction-definitions.yaml`.
- `data/side-mission-definitions.yaml`.
- `data/dialogue-definitions.yaml`.

Act IV and final-state definitions remain canonical only where listed in the manifest. Duplicate files elsewhere are legacy until migrated.
