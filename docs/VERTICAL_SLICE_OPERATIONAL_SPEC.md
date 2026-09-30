# Vertical Slice Operational Specification

## Purpose

This is the implementation contract for the first production slice. A vertical slice is a production proof, not merely a design prototype: it must exercise the pipeline across gameplay, narrative, UI, accessibility, art, audio, data, save, and QA.[web:168]

## Scenario

`VS-OSTIA-001`: Dama observes a trafficking transfer near an Ostia warehouse, verifies conflicting testimony, chooses a quiet extraction or public disruption, escapes through a changing route, and hands agency to an affected person or cell.

## Duration and boundaries

- First-time play: 20–35 minutes.
- Repeatable test pass: 8–12 minutes.
- One compact environment: warehouse edge, alley, shelter, dock route.
- No full regional travel map; use one representative route link.

## Required sequence

1. Read: identify route, authority presence, and one human request.
2. Verify: inspect one ledger or testimony conflict; mark confidence as partial or corroborated.
3. Commit: choose quiet extraction or public disruption after seeing tradeoff previews.
4. Execute: navigate, listen, negotiate, sneak, deceive, sabotage, or fight as last resort.
5. Escape: route pressure changes from the choice; failure creates a recovery state.
6. Rebuild: update network variables and show an independent non-protagonist decision.
7. Debrief: display authored consequences and the next available lead.

## Required content

- Dama, affected person, ally, authority, and non-protagonist decision-maker.
- Two approaches with asymmetric costs.
- One node, one link, one cell, one evidence chain.
- All eight resistance variables wired to visible feedback.
- One failure recovery path that is not a pure reload.
- One historical codex entry labelled FACT, one RECONSTRUCTION, and one FICTION.

## Asset and audio list

- 1 greybox/final-target environment pass.
- 5 named characters with readable silhouettes and status cues.
- 12 props: ledger, rope, lamps, crates, tools, seals, food, medicine, papers, lock, cart, shrine marker.
- 3 UI screens: objective/evidence, network state, consequence debrief.
- 6 ambience layers: dock, warehouse, crowd, water, fire/pressure cue, shelter.
- Dialogue placeholders with speaker, language, register, translation, and review status.

## Accessibility requirements

- Scalable subtitles and speaker labels.
- Full remapping with hold/toggle alternatives.
- Visual audio cues.
- Reduced flashes, shake, and distressing effects.
- Adjustable stealth/chase pressure.
- Checkpoint before commitment and after escape.

## Success metrics

- 90% of new players identify the immediate objective without facilitator help.
- 80% can explain one tradeoff before committing.
- 80% notice at least one downstream consequence.
- 0 blocker defects; 0 data integrity failures.
- Deterministic replay produces identical state hash for fixed seed/input.
- All mandatory accessibility checks pass on the primary platform.
- At least one external playtest round completes with findings triaged.

## Exit gate

The slice is accepted only when content, data, save/load, accessibility, art/audio, performance capture, deterministic tests, and playtest evidence are attached to the build record. A document or mockup alone is insufficient.
