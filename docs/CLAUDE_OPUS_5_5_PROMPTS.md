# Claude Opus 5.5 — Phased Development Prompts

## How to use this file

Claude must read `README.md`, `GDD.md`, `CLAUDE.md`, and the relevant documents before executing a phase. Work in small, reviewable commits. Never invent missing canon silently.

## Global prompt

You are working on Breaking Chains: Rome. Treat `GDD.md` as canonical. Preserve AD 54–64, Dama, Livia, the four targets, ten regions, historically researched languages, and the 18 July AD 64 final mission. Use English for all repository files. Label historical claims. Prefer stable IDs, schemas, tables, formulas, and tests. Inspect before editing. Report assumptions and unresolved research questions.

## Phase 1 — Canon audit

Read all current documentation. Build a canonical inventory of dates, characters, locations, factions, mission IDs, language contexts, and final-state rules. Detect contradictions. Do not add new narrative content until the inventory is complete. Output: `docs/canon-audit.md`.

## Phase 2 — Timeline and dependency graph

Produce a date-indexed timeline from AD 54 through the epilogue. Build a directed graph for main missions, side-mission prerequisites, regional unlocks, and final-operation requirements. Every edge must have a reason. Output: `docs/story/timeline.md` and `docs/missions/dependency-graph.md`.

## Phase 3 — Character production bible

Expand every named character with biography, competence, contradiction, relationship graph, dialogue voice, language metadata, mission appearances, survival status, and historical classification. Do not make Dama or Livia sole saviors. Output: updates to `docs/CHARACTER_BIBLE.md` and `content/characters/`.

## Phase 4 — Factions and social systems

Define faction goals, resources, leadership, public identity, internal disagreements, state transitions, and mission reactions. Include enslaved communities, freed communities, merchants, authorities, military, and resistance. Output: `docs/FACTIONS_AND_CONFLICTS.md` and structured faction data.

## Phase 5 — World and map

Expand all ten regions, major cities, roads, rivers, ports, estates, mines, forts, safe houses, and interior spaces. For each location provide stable ID, languages, residents, factions, schedules, resources, security, missions, and travel connections. Output: updates to world documents and location data.

## Phase 6 — Main mission briefs

Write full production briefs for ACT-ROME-001 through ACT-ROME-042. Each brief must include fixed date, location, cast, prerequisites, ordered objectives, fail states, success state, dialogue scenes, gameplay systems, historical classification, rewards, reputation effects, and deterministic tests. Do not alter the canonical mission order or final date.

## Phase 7 — Side-mission matrix

Expand the side-mission catalogue into a matrix of IDs, regions, prerequisites, objectives, characters, rewards, relationship effects, world effects, and links to main missions. Ensure side missions deepen the world without changing canonical outcomes.

## Phase 8 — Free-roam activities

Define production-ready activity loops for blacksmithing, travel, hunting, fishing, documents, medicine, cooking, courier work, rescue logistics, language lessons, workshops, and memorial activities. Each activity must have deterministic inputs, outputs, costs, risks, and rewards.

## Phase 9 — Dialogue and localization

Create dialogue scene metadata, not unsupported ancient-language prose. Specify intended language, register, translation mode, subtitle behavior, speaker knowledge, and localization notes. Flag all lines requiring specialist linguistic review.

## Phase 10 — Deterministic systems

Convert travel, weather, schedules, stealth, reputation, economy, rescue logistics, fire propagation, and save persistence into tables, formulas, schemas, and test cases. Critical outcomes must not rely on uncontrolled randomness.

## Phase 11 — Technical content schemas

Create JSON Schemas and sample YAML/JSON for characters, locations, missions, dialogue, factions, routes, schedules, economy, and rescued people. Add validation scripts for IDs, references, dates, dependencies, and determinism declarations.

## Phase 12 — Vertical slice plan

Specify the first playable vertical slice: Ashgrove Estate, The Bell Before Dawn, The Ledger Room, The Missing Bell, one workshop, one safe house, one patrol system, one resource loop, one language interaction, and one persistent consequence. Include acceptance criteria and deterministic test cases.

## Phase 13 — Historical review package

Create a claim ledger separating fact, reconstruction, fiction, and open questions. Identify all content requiring historian, archaeologist, linguist, or sensitivity-reader review. Do not silently resolve disputed evidence.

## Phase 14 — Final continuity audit

Check every document and structured file against the canon. Verify IDs, chronology, locations, language assignments, survival statuses, mission prerequisites, rewards, final date, and ending. Produce a blocking-issues report. Do not mark the project complete while blocking issues remain.

## Response format for every phase

1. Files inspected.
2. Changes made.
3. Canonical facts preserved.
4. New IDs introduced.
5. Deterministic rules added.
6. Tests added or executed.
7. Historical claims requiring review.
8. Unresolved questions.
9. Next phase recommendation.