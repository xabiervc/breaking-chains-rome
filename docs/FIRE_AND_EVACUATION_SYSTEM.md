# Fire and Evacuation System

## Design principle

The fire is a deterministic narrative simulation. It must appear dynamic while producing the same critical events for the same preparation state and inputs.

## Fire-zone states

Each zone has one state: `unlit`, `ignition_ready`, `burning`, `blocked`, `evacuated`, `collapsed`, or `safe`.

## Fixed inputs

- Zone ID.
- Ignition timestamp.
- Wind direction and intensity for 18 July AD 64.
- Building density.
- Combustibility class.
- Street width.
- Water access.
- Firebreak status.
- Civilian density.
- Evacuation route state.

## Propagation rule

A zone can transition from `ignition_ready` to `burning` only when its prerequisite zone is burning and its threshold is met. Thresholds are stored in `data/fire-zones.yaml`. No critical zone transition uses uncontrolled randomness.

## Evacuation tiers

- Tier 0: no preparation; civilian movement is blocked.
- Tier 1: warning network; one route opens.
- Tier 2: shelters and supplies; two routes open.
- Tier 3: complete specialist preparation; three routes open and medical triage functions.

The canonical campaign can always complete the final mission, but preparation changes the number of non-named civilians who reach safety. Named specialists cannot die through random simulation.

## Fixed civilian outcomes

- 40 captives are rescued during the main objective.
- Additional civilians survive according to evacuation tier: 80 at Tier 0, 140 at Tier 1, 220 at Tier 2, 320 at Tier 3.
- Dama, Livia, Nicanor, Tertia, Bato, Eirene, and Publius survive the canonical ending.

## Safety rules

The game does not reward burning civilian homes. The player receives a mission failure state if they deliberately ignite a zone before its evacuation prerequisite is met. Reloading restores the previous deterministic fire state.
