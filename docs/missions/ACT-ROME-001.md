# ACT-ROME-001 — The Bell Before Dawn

- Act: I
- Date: AD 54, spring, fixed opening day
- Locations: Ashgrove forge, south yard, bell tower path
- Type: Tutorial, observation, crafting
- Classification: FICTION within a historically researched setting

## Purpose

Introduce Dama's work, the estate hierarchy, material ownership, and the first private act of resistance.

## Cast

Dama; Nera, kitchen worker; Herennius, overseer; Lucan, forge assistant.

## Prerequisites

None.

## Ordered objectives

1. Reach the forge before the first bell.
2. Repair the plough coupling using iron stock and a borrowed hammer.
3. Observe the yard schedule without entering restricted areas.
4. Deliver the repair to the south field.
5. Return the hammer before the second bell.
6. Inspect the marked transport wagon after Herennius leaves.
7. Memorize the iron seal and return to the forge.

## Failure and success

Entering a restricted area twice resets Dama to the forge. Losing the hammer creates a fixed recovery objective. Permanent failure is impossible. Success sets `knowledge.transport_seal=true`, completes the mission, unlocks ACT-ROME-002, and unlocks basic Forge interaction.

## Determinism

Bell times are 05:00 and 07:00. Herennius route is office → south yard → forge entrance → north field. The wagon is always at `LOC-ITA-001.YARD.SOUTH.03`.

## Rewards

Forge XP 100; one iron scrap; +2 Enslaved Communities reputation.

## Tests

A new campaign starts without prerequisites. The seal is recorded once. Reloading before inspection reproduces the same schedule.
