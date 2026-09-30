# Design Authority

## Frozen baseline

The implementation baseline is the canonical set listed below at commit `78b40fc52d37ec6fbfc52d869f7155bfa718d80d`, extended by this governance commit. No file named FINAL, PREMIUM, COMPLETE, 100, or PHASE overrides it.

## Normative documents by area

- Identity and scope: `GDD.md`, `docs/CANONICAL_SOURCE_OF_TRUTH.md`, `docs/CONTENT_SCOPE_MATRIX.md`.
- Gameplay and network: `docs/GAMEPLAY_SYSTEMS.md`, `docs/RESISTANCE_NETWORK_SYSTEM.md`, `docs/PLAYER_AGENCY_AND_COSTS.md`, `docs/RESISTANCE_SYSTEM_BALANCE.md`.
- Narrative and canon: `docs/CAMPAIGN_ARC_AND_TIMELINE.md`, `docs/NARRATIVE_STATE_MACHINE.md`, `docs/CHARACTER_ARCS_RELATIONSHIPS_AND_CONFLICTS.md`, `docs/CANON_RULES.md`, `docs/NARRATIVE_SYSTEM_TRACEABILITY.md`.
- Slice: `docs/VERTICAL_SLICE_OPERATIONAL_SPEC.md`, `docs/DESIGN_TRACEABILITY_MATRIX.md`.
- Accessibility: `docs/ACCESSIBILITY_REQUIREMENTS.md`, `docs/ACCESSIBILITY_QUALITY_GATE.md`.
- Technical: `docs/TECHNICAL_ARCHITECTURE.md`, `docs/PLATFORM_MATRIX.md`, `docs/PERFORMANCE_AND_MEMORY_BUDGET.md`, `docs/SAVE_MIGRATION_AND_RECOVERY.md`.
- Historical and ethical: `docs/research/`, `docs/HISTORICAL_PLAY_POLICY.md`, `docs/HISTORICAL_SENSITIVITY.md`.

## Conflict protocol

1. Stop implementation of the affected feature.
2. Open a dated change record naming the conflicting documents and stable IDs.
3. Decide whether the conflict changes canon, scope, or only supporting prose.
4. Update the authority index and traceability matrix.
5. Add or update a regression test.
6. Resume only after the change record is reviewed.

## Approval roles

- Product/canon owner: approves identity, scope, and irreversible narrative decisions.
- Design owner: approves mechanics, variables, progression, and slice behavior.
- Technical owner: approves architecture, save, performance, and CI decisions.
- Accessibility/content reviewers: approve accessibility and sensitive-content changes within their remit.

No role may silently override another domain’s canonical contract.
