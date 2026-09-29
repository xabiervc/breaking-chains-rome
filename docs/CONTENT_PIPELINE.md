# Content Pipeline

## Source of truth

Markdown documents define design intent. YAML files define structured content. JSON Schemas define required structure. Runtime code must consume validated structured data and must not introduce undocumented gameplay-critical constants.

## Content change workflow

1. Edit the relevant design document.
2. Add or update structured data.
3. Preserve stable IDs.
4. Run `python tools/run_all_validators.py`.
5. Review the generated report.
6. Add or update deterministic tests.
7. Commit design and data changes together.

## Validation layers

- Syntax: YAML and JSON parse.
- Schema: required fields and formats.
- References: IDs resolve across files.
- Canon: fixed dates, characters, mission gates, and ending remain intact.
- Determinism: critical systems declare stable inputs and outputs.
- QA: acceptance tests cover success, failure, reload, and repetition.

## Versioning

Every content manifest has a version. Save files record the content version. A migration is required when a persisted field changes meaning.
