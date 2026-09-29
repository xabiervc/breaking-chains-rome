# Breaking Chains: Rome

Production bible and Unreal Engine 5 preimplementation package for a deterministic, historically grounded open-world action-adventure set across the Roman Empire during AD 54–64.

## Current status

The repository is in **canon normalization and preimplementation audit**. Narrative and technical design are extensive, but Unreal project generation has not begun.

## Canonical source hierarchy

Read `docs/canon/source-of-truth.md` and `docs/canon/canonical-manifest.yaml` before using any content. Files under `data/legacy/` are historical snapshots and must not be imported.

## Start here

1. `docs/LLM_CONTEXT_INDEX.md`.
2. `CLAUDE.md`.
3. `docs/canon/source-of-truth.md`.
4. `docs/canon/continuity-matrix.md`.
5. `docs/canon/canonical-manifest.yaml`.
6. `docs/LLM_IMPLEMENTATION_CONTRACT.md`.
7. `docs/preimplementation-readiness.md`.

## Technical decision

- Unreal Engine 5.
- Native C++ for authoritative runtime systems.
- Blueprints for authored presentation and composition.
- Python for content/editor automation.
- YAML to validation to Unreal Data Assets/Data Tables.
- World Partition for open-world streaming.
- Git LFS for binary Unreal assets.

## Truthfulness rule

The repository is specified and structured, but it is not a compiled or playable Unreal project. Do not claim compilation, execution, visual verification, historical review, or production readiness unless those activities have actually occurred.
