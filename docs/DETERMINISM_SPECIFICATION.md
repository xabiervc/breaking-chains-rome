# Determinism Specification

## Purpose

All gameplay-critical behavior must be reproducible for the same save state, inputs, date, location, and version.

## Deterministic inputs

- Save-state identifier.
- Campaign date and time.
- Region and location ID.
- Mission state.
- Faction states.
- Reputation values.
- Inventory and resource quantities.
- Player ability flags.
- Route and weather IDs.
- Game-version identifier.

## Fixed rules

- Main mission objectives are ordered and immutable.
- Named character survival is scripted.
- Historical dates are immutable.
- Major routes have fixed graph edges.
- NPC schedules use date/season/location tables.
- Weather uses a region/date seed.
- Economy uses documented formulas.
- Fire behavior uses fixed building, wind, water, and evacuation inputs.

## Stable random seed

`seed = hash(save_id + game_version + region_id + date_id + encounter_pool_id)`

Stable seed is permitted only for cosmetic or non-canonical selections. It must never decide named-character death, mission success, final outcome, or historical events.

## Save persistence

Persist completed mission IDs, faction states, reputation, discovered routes, rescued-person ledger, inventory, ability flags, language levels, unlocked locations, destroyed records, and named-character statuses.

## Required tests

1. Reloading before a route produces the same route options.
2. Repeating a date/location encounter with identical inputs produces the same canonical result.
3. Completing a main mission twice cannot duplicate rewards.
4. Named characters cannot die through ambient randomness.
5. The final mission date remains 18 July AD 64 in every valid save.
