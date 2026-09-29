# Canonical Fire and Evacuation Decision

## Required versus optional routes

- `EVAC-001` is the mandatory rescue route and is always open after ACT-ROME-036.
- `EVAC-002` and `EVAC-003` are optional capacity routes unlocked by ACT-ROME-039.
- The 40 captive rescue objective uses EVAC-001 and is available at every valid evacuation tier.
- Optional tiers change additional civilian survival and traversal options, not the canonical fire, rescue count, or named-character outcomes.

## Fire-zone authority

`data/fire-zones.yaml` defines zones and prerequisites. `data/fire-transitions.yaml` defines the only canonical transitions. The final fire cannot transition before ACT-ROME-042 begins.

## Fixed sequence

1. Dama verifies EVAC-001.
2. FIRE-ZONE-001 ignites at 21:10 on AD64-07-18.
3. FIRE-ZONE-002 burns at 21:18 after zone 001.
4. FIRE-ZONE-003 burns at 21:24 only when EVAC-002 is open; if it is not open, the zone remains unlit and the final mission still proceeds through EVAC-001.
5. FIRE-ZONE-004 burns at 21:32 after the archive route is active; it does not require zone 003, because optional routes cannot block the canonical finale.
6. The rescue packet is copied before the archive collapses.
7. The epilogue unlocks after the escape state commits.
