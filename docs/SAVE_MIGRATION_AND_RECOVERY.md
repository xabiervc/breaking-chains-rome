# Save, Migration, and Recovery

## Requirements

- Version every save schema.
- Use atomic write plus backup rotation.
- Validate checksums and reject partial/corrupt files without destroying the last good save.
- Keep settings separate from campaign state.
- Support migration from every shipped schema to the current schema through tested steps.
- Preserve accessibility settings across retries, patches, and migrations.
- Provide clear recovery UI and exportable diagnostic information without personal data.

## Tests

Interrupted write, power loss simulation, disk-full behavior, duplicate slot handling, downgrade refusal, migration rollback, corrupted evidence state, and language change between saves.
