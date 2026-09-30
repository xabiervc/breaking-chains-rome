# Award-Caliber QA Plan

## Test layers

1. Static: YAML/JSON schema, IDs, references, chronology, source labels, localization keys.
2. Unit: route selection, evidence scoring, faction consequences, fire propagation, save migration.
3. Integration: mission state transitions, companion availability, rescue ledger, epilogue matrix.
4. Determinism: same seed/input produces the same state hash and outcome.
5. Accessibility: settings persistence, subtitles, remapping, visual cues, reduced effects.
6. Usability: first-session comprehension, objective recovery, failure recovery, map readability.
7. Performance: frame time, memory, streaming, loading, save latency on target hardware.
8. Narrative: continuity, historical labels, sensitivity, translation, voice direction.
9. Soak/regression: long sessions, repeated reloads, interrupted saves, language changes, checkpoint loops.

## Exit criteria

- No open blocker or critical defect.
- All mandatory tests green on the release candidate.
- Every failed test has a triaged owner and documented disposition.
- Accessibility and specialist review actions are closed or explicitly accepted by production leadership.
- Vertical slice and full campaign each receive an external playtest synthesis.
