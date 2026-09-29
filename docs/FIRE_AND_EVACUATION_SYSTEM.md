# Fire and Evacuation System

## Authority

The canonical fire state is defined only by `data/fire-zones.yaml`, `data/fire-transitions.yaml`, and the fixed final-state rules.

## Evacuation tiers

- Tier 0: EVAC-001 is available for the mandatory rescue route; optional civilian survival is 80.
- Tier 1: EVAC-001 plus warning support; optional civilian survival is 140.
- Tier 2: EVAC-001 and EVAC-002; optional civilian survival is 220.
- Tier 3: EVAC-001, EVAC-002, and EVAC-003; optional civilian survival is 320.

The required 40-captive rescue is possible at all tiers. Tier 0 does not mean zero evacuation; it means no optional capacity preparation.

## Fire transitions

The transition table is deterministic and uses the final mission state, route flags, rescue-packet state, and archive state. Optional zones never block the canonical archive confrontation or mandatory rescue.

## Safety invariant

The game never rewards deliberately burning civilian homes. Any attempted ignition before ACT-ROME-042 or before EVAC-001 verification enters a fixed failure state.
