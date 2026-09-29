# Save and Versioning

## Save format

`UBCSaveGame` stores content and campaign versions, completed mission IDs, objective states, date/time, discovered routes and locations, evidence, factions and reputation, rescue ledger, inventory, abilities, language levels, specialist statuses, fire-zone states, evacuation tier, and permanent world changes.

## Version rules

Stable IDs are never reused. Save files include a schema version. Every schema change requires a migration function. Unknown future fields are ignored only when safe. Removed fields require explicit migration behavior. Invalid critical state blocks loading and produces a diagnostic report rather than silently repairing canon.

## Deterministic save rule

Saving and loading at the same frame-equivalent gameplay state must restore the same authoritative state. Cosmetic particles, animation phase, and ambient positions may differ.
