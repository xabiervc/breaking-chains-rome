# Vertical Slice Implementation Specification

## Slice boundary

The slice contains Ashgrove Estate, its forge and south yard, the Appian transport road, the Alban Hills refuge, and missions ACT-ROME-001 through ACT-ROME-007.

## Runtime states

```text
NEW
 -> OBSERVING_ESTATES
 -> INVESTIGATING_LEDGER
 -> PREPARING_ESCAPE
 -> WITNESSING_SALE
 -> ESCAPING
 -> AT_REFUGE
 -> RETURNING_FOR_REGISTER
 -> ACT_I_COMPLETE
```

Each state has one entry condition, one allowed objective set, one persistence payload, and one deterministic transition list.

## Required runtime entities

- Dama.
- Livia.
- Nera.
- Silvanus.
- Otho.
- Vara.
- Herennius.
- Ashgrove Estate.
- Appian transport road.
- Alban Hills refuge.
- Transport wagon.
- Ownership register.

## Fixed schedule service

- First bell: 05:00.
- Second bell: 07:00.
- Ledger access: 12:10–12:20.
- Auction day: fixed campaign date after ACT-ROME-003.
- Escape diversion: 18:40.
- Patrol arrival: 18:43.

The schedule service receives campaign date, location ID, mission ID, and alert state. It returns the same schedule for identical inputs.

## Acceptance tests

- A fresh save can complete all seven main missions.
- Every mission transition is idempotent.
- A failed stealth attempt changes alert state but cannot alter canonical mission outcome.
- Livia's transfer is unavoidable in ACT-ROME-004.
- Vara's death occurs only in ACT-ROME-006.
- Herennius's death occurs only in ACT-ROME-007.
- The Ashgrove register remains destroyed after save/load.
- ACT-ROME-008 is unavailable before ACT-ROME-007.
