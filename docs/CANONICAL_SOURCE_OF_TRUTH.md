# Canonical Source of Truth

## Authority

`docs/DESIGN_AUTHORITY.md` is the normative governance document for implementation. This file lists the canonical design set; it does not permit filename recency to override it.

## Canonical specification set

- Governance: `docs/DESIGN_AUTHORITY.md`, `docs/IMPLEMENTATION_DECISION_REGISTER.md`, `docs/DOCUMENT_STATUS_INDEX.md`.
- Vision and scope: `GDD.md`, `docs/CONTENT_SCOPE_MATRIX.md`.
- Gameplay: `docs/GAMEPLAY_SYSTEMS.md`, `docs/GAMEPLAY_PILLARS_AND_MASTERY.md`, `docs/RESISTANCE_NETWORK_SYSTEM.md`, `docs/PLAYER_AGENCY_AND_COSTS.md`.
- Narrative: `docs/CAMPAIGN_ARC_AND_TIMELINE.md`, `docs/NARRATIVE_STATE_MACHINE.md`, `docs/CHARACTER_ARCS_RELATIONSHIPS_AND_CONFLICTS.md`, `docs/CANON_RULES.md`, `docs/NARRATIVE_SYSTEM_TRACEABILITY.md`.
- Slice: `docs/VERTICAL_SLICE_OPERATIONAL_SPEC.md`, `docs/DESIGN_TRACEABILITY_MATRIX.md`.
- Accessibility: `docs/ACCESSIBILITY_REQUIREMENTS.md`, `docs/ACCESSIBILITY_QUALITY_GATE.md`.
- Technical: `docs/TECHNICAL_ARCHITECTURE.md`, `docs/TECHNICAL_QUALITY_GATE.md`, `docs/PLATFORM_MATRIX.md`, `docs/PERFORMANCE_AND_MEMORY_BUDGET.md`, `docs/SAVE_MIGRATION_AND_RECOVERY.md`.
- Research and ethics: `docs/research/README.md`, `docs/HISTORICAL_PLAY_POLICY.md`, `docs/HISTORICAL_SENSITIVITY.md`.

## Conflict rule

Implementation stops for an affected feature when canonical documents conflict. A dated change record must name the conflict, affected stable IDs, decision owner, migration impact, and regression test before implementation resumes.
