# Legacy Data Policy

## Reason

Earlier design iterations created duplicate YAML files before the canonical normalized definitions were established. Keeping them in the repository is useful for historical traceability, but allowing an LLM or importer to treat them as runtime input would reintroduce contradictions.

## Rules

- Files in `data/legacy/` are read-only historical snapshots.
- They are not imported, validated as runtime definitions, or used to generate Unreal assets.
- New content must never be added there.
- If a legacy fact is still needed, migrate it into the canonical definitions and record the migration in `docs/canon/change-log.md`.
- A legacy file may be deleted only after its relevant information has been migrated or explicitly rejected.
