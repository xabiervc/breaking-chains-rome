# Canonical Source of Truth

## Authority

`docs/CANONICAL_SOURCE_OF_TRUTH.md` is the index for design authority. It does not replace the authoritative records listed below; it resolves which document wins when summaries overlap.

1. Explicit current owner decisions and approved change records.
2. Stable-ID canon under `docs/canon/` and `data/`.
3. This index and the linked canonical specifications.
4. Supporting research and review documents.
5. Aspirational proposals, prompts, generated drafts, and legacy documents.

## Canonical specification set

- Vision and scope: `GDD.md`, `docs/PROJECT_GENERATION_SPEC.md`.
- Gameplay: `docs/GAMEPLAY_SYSTEMS.md`, `docs/GAMEPLAY_PILLARS_AND_MASTERY.md`, `docs/RESISTANCE_NETWORK_SYSTEM.md`, `docs/PLAYER_AGENCY_AND_COSTS.md`.
- Narrative: `docs/CAMPAIGN_ARC_AND_TIMELINE.md`, `docs/NARRATIVE_STATE_MACHINE.md`, `docs/CHARACTER_ARCS_RELATIONSHIPS_AND_CONFLICTS.md`, `docs/CANON_RULES.md`.
- Content: `docs/CONTENT_SCOPE_MATRIX.md`, `docs/NARRATIVE_SYSTEM_TRACEABILITY.md`, `docs/VERTICAL_SLICE_OPERATIONAL_SPEC.md`.
- Accessibility: `docs/ACCESSIBILITY_REQUIREMENTS.md`.
- Technical: `docs/TECHNICAL_ARCHITECTURE.md`, `docs/TECHNICAL_QUALITY_GATE.md`, `docs/PLATFORM_MATRIX.md`, `docs/PERFORMANCE_AND_MEMORY_BUDGET.md`.
- Research and sensitivity: `docs/research/README.md`, `docs/HISTORICAL_PLAY_POLICY.md`, `docs/HISTORICAL_SENSITIVITY.md`.
- Readiness and gates: `docs/PREIMPLEMENTATION_EXIT_CRITERIA.md`, `docs/PRODUCTION_GATES.md`, `docs/preimplementation-readiness.md`.

## Conflict rule

If two canonical documents conflict, implementation is blocked until a dated change record resolves the conflict. No “latest-looking” filename overrides authority.
