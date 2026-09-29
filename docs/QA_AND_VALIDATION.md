# QA and Validation

## Validation categories

1. ID uniqueness.
2. Broken cross-references.
3. Timeline contradictions.
4. Location-region mismatches.
5. Language-context mismatches.
6. Mission dependency cycles.
7. Reward duplication.
8. Impossible resource requirements.
9. Named-character survival contradictions.
10. Non-deterministic critical paths.

## Release gates

A narrative milestone cannot be marked complete until the canonical timeline, mission graph, character statuses, region connections, and final-state tests pass.

## Test examples

- Every main mission has exactly one canonical success state.
- Every Act III target has exactly three investigation missions and one resolution mission.
- ACT-ROME-042 cannot start before all four Act III resolution missions and ACT-ROME-035.
- Livia remains alive after the final mission.
- Vindex dies only during ACT-ROME-042.
- The final date is always 18 July AD 64.
