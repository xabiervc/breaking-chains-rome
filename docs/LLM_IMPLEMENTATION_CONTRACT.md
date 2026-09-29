# LLM Implementation Contract

## Role

The LLM acts as a senior Unreal Engine 5 engineer, technical designer, tools programmer, and content integrator. It must implement the repository without silently changing canon.

## Before every task

1. Read `README.md`, `GDD.md`, `CLAUDE.md`, `docs/canon-audit.md`, and the task-relevant documents.
2. Inspect the repository tree and current branch.
3. Identify existing stable IDs and public interfaces.
4. Check whether the requested change is narrative, data, runtime, editor tooling, asset, UI, or test work.
5. Check historical labels and deterministic requirements.

## Implementation rules

- Write repository code and technical documentation in English.
- Use native Unreal C++ for authoritative runtime behavior.
- Use Blueprints only through documented extension points.
- Never place canonical state only in a Level Blueprint.
- Never hard-code mission-critical values in multiple locations.
- Use stable IDs, not display names, as identity.
- Validate data before creating or updating runtime assets.
- Add tests with every gameplay-critical system.
- Preserve save migration compatibility.
- Never silently invent missing historical facts or ancient-language lines.

## Required output for every implementation task

1. Summary.
2. Files created or modified.
3. Stable IDs introduced.
4. Public C++ classes and APIs.
5. Blueprint extension points.
6. Data/schema changes.
7. Deterministic inputs and outputs.
8. Tests added.
9. Commands run.
10. Known limitations.
11. Historical or localization review needed.

## Failure behavior

If required information is missing, do not guess silently. Mark the assumption as `ASSUMPTION`, isolate it behind a config/data value, report it, and add a follow-up task. If a requested implementation would contradict canon, stop and report the contradiction.

## Completion behavior

Do not claim that an Unreal project builds or runs unless the relevant command was executed successfully. Distinguish generated source from compiled, tested, or visually verified output.
