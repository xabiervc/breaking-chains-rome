# Final Campaign QA

## Test groups

### Canon tests

- Confirm campaign date remains AD 64-07-18 at final start.
- Confirm ACT-ROME-042 is impossible before all four Act III resolution missions.
- Confirm Vindex cannot die before ACT-ROME-042.
- Confirm Dama and Livia survive the canonical ending.
- Confirm Roman slavery remains active in the epilogue state.

### Evacuation tests

- Tier 0: final mission remains completable; mandatory 40-captive rescue remains active.
- Tier 1: exactly one optional route opens; survival total is 140.
- Tier 2: exactly two optional routes open; survival total is 220.
- Tier 3: exactly three routes open; survival total is 320.

### Fire tests

- Replaying the same fire seed produces the same zone transitions.
- FIRE-ZONE-004 cannot collapse before `rescue_packet_copied` and `archive_destroyed`.
- Ignition before route verification enters the fixed failure state.
- Reloading before ignition restores all prior zone states.

### Persistence tests

- Completed mission rewards are idempotent.
- Rescued people are not duplicated after reload.
- Destroyed records remain destroyed.
- Discovered routes remain discovered.
- Named-character status cannot be overwritten by ambient simulation.

## Release gate

The final campaign is not production-ready until all invariant tests pass at all four evacuation tiers and after save/reload at each final-phase checkpoint.
