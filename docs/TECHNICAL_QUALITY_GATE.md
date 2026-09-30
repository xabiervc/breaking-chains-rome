# Technical Quality Gate

## Gate requirements

- CI installs a declared environment and runs lint, schema validation, unit tests, and deterministic replay tests.
- All data loaders reject malformed IDs, dangling references, duplicate identifiers, invalid enums, and inconsistent chronology.
- Save/load is versioned, migration-tested, and resilient to interrupted writes.
- Route, evidence, faction, fire, and outcome systems have deterministic seeds and replay fixtures.
- Target-hardware performance budgets are explicit for frame time, memory, streaming, loading, and save latency.
- Crash and error telemetry is privacy-conscious and disabled or documented for offline builds.
- No secrets, credentials, generated binaries, or local absolute paths enter the repository.
- Content patching and localization fail loudly when placeholders or missing keys remain.

## Current status

The Conda workflow has existed but its first reported run failed because `environment.yml` was missing. That failure is a release-blocking infrastructure issue until a subsequent run proves the corrected environment and downstream steps.

## Evidence required

Commit SHA, workflow run URL/status, test summary, validator report, deterministic replay output, target-hardware capture, and known-issues list.
