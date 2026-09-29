# Technical Architecture

## Documentation-first implementation

Narrative and systems data must be machine-readable before full implementation. Use stable IDs and versioned schemas.

## Data domains

- Characters.
- Locations.
- Regions.
- Missions.
- Dialogue scenes.
- Factions.
- Routes.
- Schedules.
- Economy.
- Rescue ledger.
- Historical sources.

## Recommended formats

- YAML or JSON for structured content.
- Markdown for design and research prose.
- JSON Schema for validation.
- Deterministic seed utilities for allowed non-canonical variation.

## Architecture constraints

Separate canonical narrative data from presentation, localization, and runtime state. No dialogue line should encode a hidden gameplay rule that cannot be validated. No gameplay-critical constant should exist only in prose.
