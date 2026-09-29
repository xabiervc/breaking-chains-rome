# Claude Opus 5.5 — Repository Contract

This repository is the canonical design source for Breaking Chains: Rome. Read `GDD.md` and the relevant documents in `docs/` before creating or changing content.

## Absolute rules

- Write repository content in English.
- Preserve the fixed canon: AD 54–64, Dama, Livia, the four targets, the ten regions, and the 18 July AD 64 climax.
- Never move this project to the American South; that is Breaking Chains: Blood and Cotton.
- Do not make the Great Fire optional.
- Do not claim Dama ended Roman slavery.
- Do not present Nero's historical responsibility as proven.
- Never invent sources or ancient-language quotations.
- Mark internal claims `[FACT]`, `[RECONSTRUCTION]`, `[FICTION]`, or `[OPEN QUESTION]`.
- Inspect existing files before edits and preserve stable IDs.

## Operating procedure

1. Read the applicable canon documents.
2. Identify impacted entities and IDs.
3. Check chronology, geography, language, faction, and mission dependencies.
4. Write the smallest complete change.
5. Add deterministic inputs, constants, formulas, state transitions, persistence, edge cases, and tests.
6. Update indexes and cross-references.
7. Run validation or document why it cannot run.
8. Report changed files and unresolved questions.

## Forbidden ambiguity

Do not use “randomly,” “usually,” “as needed,” “roughly,” or “depending on the situation” for gameplay-critical behavior. Allowed randomness is cosmetic crowd behavior, ambient wildlife, minor predefined loot variation, and non-narrative idle dialogue.

## Required entity fields

Missions: stable ID, title, act, date, locations, prerequisites, ordered objectives, failure states, success state, characters, factions, rewards, reputation, historical classification, deterministic tests.

Characters: stable ID, age, origin, legal/social status, languages, faction, motivation, internal conflict, relationships, appearances, survival status, historical classification.

Locations: stable ID, region, settlement type, geographic inspiration, languages, factions, resources, connections, security, missions, historical classification.

## Naming

Mission IDs use `ACT-ROME-###`; side missions use `SIDE-REGION-###`; characters use `CHAR-###`; locations use `LOC-REGION-###`; factions use `FACTION-###`. Never reuse an ID.

## Scope

Use the fixed 300-square-mile abstraction and ten regions. Add depth through interiors, schedules, routes, factions, dialogue, systems, and missions rather than uncontrolled map expansion.
